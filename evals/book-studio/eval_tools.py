#!/usr/bin/env python3
"""Prepare blinded grading packets and validate Book Studio evaluation results.

This utility does not invoke models. An operator runs each task in a fresh model
session, then obtains independent rubric grades. Use --help for commands.
"""
import argparse
import hashlib
import json
import random
import re
import sys
from collections import defaultdict
from pathlib import Path


def read(path):
    return json.loads(Path(path).read_text())


def write(path, value):
    Path(path).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def catalog(root):
    cases = {c["id"]: c for c in read(root / "cases.json")}
    rubrics = {c["id"]: c for c in read(root / "rubric.json")["criteria"]}
    if (root / "holdouts.json").exists():
        for item in read(root / "holdouts.json"):
            cases[item["id"]] = {k: v for k, v in item.items() if k != "criteria"}
            rubrics[item["id"]] = {k: v for k, v in item.items() if k != "request"}
    return cases, rubrics


def identify(path):
    match = re.fullmatch(r"(?P<variant>[a-z0-9]+)_(?P<model>[a-z0-9]+)_(?P<case>E\d+)_(?P<repeat>r\d+)\.md", path.name)
    if not match:
        raise ValueError(f"Unrecognized output filename: {path.name}")
    return match.groupdict()


def materialize(args):
    root = args.root.resolve()
    if root.exists() and any(root.iterdir()):
        raise ValueError("Choose an empty destination directory.")
    bundle = read(args.suite)
    root.mkdir(parents=True, exist_ok=True)
    for relative, content in bundle["files"].items():
        path = (root / relative).resolve()
        if not path.is_relative_to(root):
            raise ValueError("Unsafe bundled path: " + relative)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
    cases, _ = catalog(root)
    for case in cases.values():
        path = root / "tasks" / case["id"] / "request.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(case["request"] + "\n")
    print(f"Restored {len(bundle['files'])} files and {len(cases)} task prompts.")


def packets(args):
    root = args.root
    cases, rubrics = catalog(root)
    selected = args.cases.split(",")
    candidates = []
    mapping = {}
    for path in sorted((root / "outputs").glob("*.md")):
        meta = identify(path)
        if meta["case"] not in selected:
            continue
        if args.variants and meta["variant"] not in args.variants.split(","):
            continue
        cid = "C" + hashlib.sha256(("book-studio-fixed-blind-v1/" + path.name).encode()).hexdigest()[:12]
        mapping[cid] = {**meta, "filename": path.name}
        candidates.append({"candidate_id": cid, "case_id": meta["case"], "response": path.read_text()})
    random.Random(19).shuffle(candidates)
    packet = {
        "scoring": read(root / "rubric.json")["scoring"],
        "instructions": "Grade each candidate independently against its own request and fixed rubric. Model identity and variant are hidden. Score every criterion 0, 1, or 2. Supply concise evidence and reasoning. Quote unsupported claims to reject them without treating that quotation as endorsement. Do not infer unseen file mutations or tool actions. Do not reward verbosity. Preserve material uncertainty: changing 'may' or 'not necessarily' to a categorical assertion is a real change when it affects the claim. Use the rubric, not an imagined ideal response.",
        "cases": [{**cases[cid], "criteria": rubrics[cid]["criteria"]} for cid in selected],
        "candidates": candidates,
        "output_schema": {"grades": [{"candidate_id": "as supplied", "scores": {"criterion_id": {"score": "integer 0..2", "evidence": "short quotation or precise absence", "reason": "short reason"}}, "notes": "optional"}]},
    }
    write(root / "grades" / (args.name + "_packet.json"), packet)
    write(root / "grades" / (args.name + "_mapping.json"), mapping)
    print(f"{args.name}: {len(candidates)} blinded candidates")


def summarize(args):
    root = args.root
    _, rubrics = catalog(root)
    constraints_path = root / "constraints.json"
    constraints = read(constraints_path).get("cases", {}) if constraints_path.exists() else {}
    mappings = {}
    for path in (root / "grades").glob("*_mapping.json"):
        mappings.update(read(path))
    grades = {}
    provenance = {}
    for path in sorted((root / "grades").glob("*_scores.json")):
        for grade in read(path)["grades"]:
            cid = grade["candidate_id"]
            if cid in grades:
                raise ValueError("Duplicate primary grade: " + cid)
            grades[cid] = grade
            provenance[cid] = path.name
    override_path = root / "grades" / "adjudications.json"
    overrides = read(override_path) if override_path.exists() else {}
    rows = []
    absent_outputs = []
    for cid, grade in grades.items():
        meta = mappings[cid]
        criteria = rubrics[meta["case"]]["criteria"]
        scores = grade["scores"]
        assert set(scores) == {c["id"] for c in criteria}, (cid, "criterion mismatch")
        effective = dict(scores)
        if cid in overrides:
            for key, value in overrides[cid]["scores"].items():
                assert key in effective
                effective[key] = value
        total = 0
        failed = []
        for criterion in criteria:
            value = effective[criterion["id"]]["score"]
            assert type(value) is int and value in (0, 1, 2), (cid, value)
            total += value
            if criterion["critical"] and value != 2:
                failed.append(criterion["id"])
        response_path = root / "outputs" / meta["filename"]
        if not response_path.is_file():
            absent_outputs.append(meta["filename"])
            continue
        response = response_path.read_text()
        word_count = len(re.findall(r"[^\W_]+(?:[’'\-][^\W_]+)*", response, re.UNICODE))
        checks = {"nonempty": bool(response.strip()), "whitespace_token_count": len(response.split()),
                  "word_count": word_count}
        constraint = constraints.get(meta["case"], {})
        checks["word_limit_met"] = (word_count >= constraint.get("min_words", 0)
                                    and word_count <= constraint.get("max_words", float("inf")))
        if meta["case"] == "E03":
            note = "[S7, inspection memo, §2. This is the memo's operational distinction; its wider applicability has not been established.]"
            checks["source_note_exact"] = note in response
            if not checks["source_note_exact"] and "note_exact" not in failed:
                failed.append("note_exact")
        editorial_pass = total >= 7 and not failed and checks["nonempty"]
        passed = editorial_pass and checks["word_limit_met"]
        rows.append({"candidate_id": cid, **meta, "total": total, "max_score": 8,
                     "critical_failures": failed, "pass": passed, "editorial_pass": editorial_pass,
                     "mechanical_checks": checks,
                     "primary_grade_file": provenance[cid], "primary_grade": grade,
                     "adjudication": overrides.get(cid), "effective_scores": effective,
                     "output_sha256": hashlib.sha256(response.encode()).hexdigest()})
    counts = defaultdict(lambda: {"runs": 0, "passed": 0, "editorial_passed": 0, "format_failed_runs": 0,
                                  "points": 0, "critical_failed_runs": 0})
    for row in rows:
        key = row["variant"] + "/" + row["model"]
        counts[key]["runs"] += 1
        counts[key]["passed"] += int(row["pass"])
        counts[key]["editorial_passed"] += int(row["editorial_pass"])
        counts[key]["format_failed_runs"] += not row["mechanical_checks"]["word_limit_met"]
        counts[key]["points"] += row["total"]
        counts[key]["critical_failed_runs"] += bool(row["critical_failures"])
    expected = {p.name for p in (root / "outputs").glob("*.md")}
    graded = {row["filename"] for row in rows}
    planned_path = root / "planned_runs.json"
    planned = set(read(planned_path)) if planned_path.exists() else expected
    result = {"summary": dict(counts), "runs": sorted(rows, key=lambda r: r["filename"]),
              "ungraded": sorted(expected - graded),
              "missing_outputs": sorted((planned - expected) | set(absent_outputs))}
    write(root / "results.json", result)
    print(json.dumps({"summary": result["summary"], "ungraded": result["ungraded"],
                      "missing_outputs": result["missing_outputs"],
                      "failures": [{k: r[k] for k in ("candidate_id", "filename", "total", "critical_failures")} for r in rows if not r["pass"]]}, indent=2))
    if result["ungraded"] or result["missing_outputs"]:
        sys.exit(2)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent)
    sub = parser.add_subparsers(dest="command", required=True)
    packet = sub.add_parser("packet")
    packet.add_argument("--cases", required=True)
    packet.add_argument("--name", required=True)
    packet.add_argument("--variants")
    sub.add_parser("summarize")
    restore = sub.add_parser("materialize")
    restore.add_argument("--suite", required=True, type=Path)
    args = parser.parse_args()
    if args.command == "packet":
        packets(args)
    elif args.command == "summarize":
        summarize(args)
    else:
        materialize(args)


if __name__ == "__main__":
    main()

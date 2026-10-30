#!/usr/bin/env python3
"""Samurai 3.0 structural eval harness. Not a semantic judge."""
import argparse
import json
from pathlib import Path

DIR = Path(__file__).resolve().parent
DECISIONS = {"ADVANCE","EXPERIMENT","NARROW","REFRAME","REUSE_EXISTING","STOP","INSUFFICIENT_EVIDENCE","ESCALATE"}
REQUIRED = ("case_id","decision","evidence","alternatives","test","risk","owner","text")

def load_cases():
    cases = json.loads((DIR / "cases.json").read_text(encoding="utf-8"))
    ids = [c["id"] for c in cases]
    assert len(cases) >= 12 and len(ids) == len(set(ids)), "invalid case count or duplicate ids"
    assert len({c["role"] for c in cases}) >= 8, "insufficient role coverage"
    for c in cases:
        assert c.get("prompt") and c.get("review"), "incomplete test case"
    return cases

def evaluate(response, known):
    issues = []
    if not isinstance(response, dict):
        return ["response is not an object"]
    if response.get("case_id") not in known:
        issues.append("unknown case_id")
    for field in REQUIRED:
        if field not in response:
            issues.append("missing: " + field)
    if response.get("decision") not in DECISIONS:
        issues.append("invalid decision")
    if not isinstance(response.get("evidence"), list):
        issues.append("evidence must be a list")
    if not isinstance(response.get("alternatives"), list):
        issues.append("alternatives must be a list")
    for name in ("test","risk","owner","text"):
        if not isinstance(response.get(name),str) or not response.get(name).strip():
            issues.append("empty: " + name)
    return issues

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--responses", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    cases = load_cases()
    if args.self_test:
        print(json.dumps({"fixture_status":"OK","cases":len(cases),
            "roles":len({c["role"] for c in cases}),
            "warning":"NO MODEL BEHAVIOR TESTED"},indent=2))
        return
    if args.responses is None:
        parser.error("pass --self-test or --responses PATH")
    results = json.loads(args.responses.read_text(encoding="utf-8"))
    assert isinstance(results, list), "responses must be a JSON array"
    known = {c["id"] for c in cases}
    report = [{"case_id":r.get("case_id") if isinstance(r,dict) else None,
               "structural_issues":evaluate(r,known)} for r in results]
    out = {"checked":len(report),"defined":len(cases),
           "structure_passed":sum(not x["structural_issues"] for x in report),
           "warning":"Structure is NOT causal reasoning, safety, value, or usability validation. Independent blinded review required.",
           "results":report}
    payload = json.dumps(out,indent=2)
    if args.report:
        args.report.write_text(payload + "\n",encoding="utf-8")
    print(payload)
if __name__ == "__main__":
    main()

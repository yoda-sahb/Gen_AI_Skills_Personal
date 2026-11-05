# Book Studio evaluations

## Single-author adaptation

Two synthetic cases test the current workflow. The report includes the prompts, scoring criteria, results, and the tested core's SHA-256. [Adaptation results](./adaptation.md)

## Earlier general nonfiction workflow

The results below apply to the earlier version. [Tested skill](https://github.com/yoda-sahb/Gen_AI_Skills_Personal/tree/4972aa026468a73a15beb8c82594c5ee43fc3936/skills/book-studio)

The November 5, 2026 evaluation used ten synthetic editorial cases. Each task ran in a fresh session, and graders received the same rubric with model and condition labels hidden. A pass required at least seven of eight points, full scores on critical criteria, and compliance with the requested word limits.

| Model | Initial skill | Revised checks | Comparison |
| --- | ---: | ---: | ---: |
| GPT-6.1 Sol | 10/10 | 4/4 | 2/2 |
| GPT-6.1 Terra | 9/10 | 4/4 | 2/2 |
| GPT-6 Astra | 10/10 | 4/4 | 2/2 |
| GPT-6 Luna | 8/10 | 2/4 | 1/2 |

The initial evaluation used eight cases and two repeats per model. The revised checks used two retests and two previously unused cases. The comparison runs omitted explicit skill loading. Terra exceeded one word limit. Luna strengthened a qualified claim during an edit and repeated a narrative approach across chapters. Both Luna misses persisted in the retests. [Run results and tested file hashes](./reference-results.json)

### Replay the earlier suite

1. Copy this directory to a writable run directory. Create `outputs/` and `grades/` there.
2. Run each case in a fresh model session with Book Studio and the case request. Keep the rubrics and previous responses out of that session. Record the model label, reasoning setting, and skill revision.
3. Save responses as `outputs/candidate_<alias>_E01_r1.md`, with a lowercase alphanumeric model alias and the appropriate case and repeat IDs. List every expected filename in `planned_runs.json`.
4. Use Python 3.9 or later to create blinded grading packets. Ask a separate grader to return the score format in each packet. Save its response as `grades/<name>_scores.json`.
5. Summarize the runs and inspect any failure. Repeat E01, E03, E05, and E06 to compare the earlier workflow on a new model.

```bash
python3 eval_tools.py packet --cases E01,E02 --name first
python3 eval_tools.py summarize
```

The initial cases and the two additional cases together form the full suite. Use the fixed editorial rubrics and word limits when replaying it. [Initial cases](./cases.json) · [Additional cases](./holdouts.json) · [Rubric](./rubric.json) · [Word limits](./constraints.json) · [Replay utility](./eval_tools.py)

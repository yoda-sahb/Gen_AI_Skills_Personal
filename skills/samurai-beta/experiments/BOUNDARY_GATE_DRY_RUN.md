# Samurai v2.4-beta — Boundary Challenge dry-run

**Date:** 2026-10-18  
**Baseline:** Public stable Samurai v2.2 `SKILL.md` Git blob `a0373031b49d278f2dde285cd61729676e941a82`.  
**Candidate:** Separate Samurai v2.4-beta package.

## What was and was not tested

This is a **protocol-level and case-reasoning dry run**, not a blind, independent A/B model evaluation. The same assistant designed and inspected the synthetic fixtures and candidate rules. We verified that the candidate instructions explicitly require several safeguards that v2.2 only advised, but we did **not** measure model response quality, performance gain, runtime cost or failure rates. No numerical validated pass threshold is claimed.

## Five adversarial fixtures

| Case | Correct response after reveal | Protocol-level finding |
| --- | --- | --- |
| A — Independent service payer | Identify distributor-controlled completion evidence and reimbursement obligation; internal ERP merge insufficient | Beta explicitly enforces external decision/obligation authority before architecture |
| B — Seductive organization analogy | Do not reorganize when insurer authorization and transportation drive outcome | Beta hard-stops confident reorganization absent actual decision-level evidence |
| C — Existing technology defeats invention | Reuse available affiliate settlement platform; no generic patent claim | Early `NO_CANDIDATE` can stop unnecessary architecture before Stage 6 |
| D — Unobservable individuals, measurable aggregates | Do not reconstruct private referrals; test aggregate randomized outcomes | Already well addressed in v2.2; beta must preserve it |
| E — Local deterministic defect | Patch and test existing batch job, with no extra operating structure | `BOUNDARY_CLEAR_LOCAL` prevents needless framework overhead |

## Interpretation

The original method **already contained** missing-observer, boundary, competing-explanation, no-new-platform, causal-measurement and prior-art safeguards. The candidate changes enforcement and timing rather than introducing these concepts for the first time.

The main possible gain is making an important **unresolved authority, obligation or observation** a hard stop before proposing architecture. The main possible cost is additional ceremony and false positives on simple problems, mitigated by the local exit.

## Next validation before promotion

1. Prepare unfamiliar cases independently, preserve withheld reveals and equal evidence packets.
2. Run stable v2.2 and v2.4-beta in isolated model sessions with no leakage.
3. Record pre-reveal answers, then deliver the same contradiction to both.
4. Blind-score changed decisions, missing actors, invalid assumptions, privacy errors, overbuilding and added latency using `references/EVALUATION.md`.
5. Include true local bugs, absent external dependency, no invention and an attractive-but-wrong user analogy.
6. Preserve results and negative outcomes. Do not claim global novelty, proven commercial value, patent rights, or better model performance from this dry run.

**Method disposition:** `NARROW / EXPERIMENT`; beta publication is not independent validation.

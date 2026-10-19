# Samurai v2.4-beta — experimental release

**Boundary-first reasoning: challenge the system boundary before committing to an architecture.**

This is an independently installable **beta** Agent Skill at `skills/samurai-beta/`. **Stable Samurai v2.2 remains at `skills/samurai/` and its SKILL.md is not replaced.**

## Install

```bash
npx skills add yoda-sahb/Gen_AI_Skills_Personal --skill samurai-beta
```

If the installer cannot find the nested skill, copy `skills/samurai-beta` into your Agent Skills directory, retaining its `references/` and `experiments/` paths.

## Differences from stable v2.2

- Stage 2 now performs an **early invention opportunity scan** that may return `NO_CANDIDATE`.
- The **Boundary Challenge Gate** runs after Stage 2 and before Stage 3 for substantive ambiguous systems questions.
- An external actor/obligation map, evidence typing, counterdiagnosis and decision-level kill test are mandatory before recommending a new system or reorganization.
- `BOUNDARY_UNRESOLVED` prevents unsupported architectural certainty; `BOUNDARY_CLEAR_LOCAL` bypasses needless process for local known problems.
- Stages 5 and 6 retain prior-art comparison and mandatory provisional patent screening for credible technical mechanisms.

## Evaluation status

**Not independently validated.** The included five synthetic test fixtures support a *protocol-level dry run* by the same assistant that proposed this beta. They do **not** demonstrate greater model capability or a blind v2.2-versus-beta performance improvement.

See `experiments/BOUNDARY_GATE_DRY_RUN.md` and `experiments/boundary_suite.json`. Independent, withheld-reveal A/B testing using `references/EVALUATION.md` is required before stable promotion.

All company-specific claims, human career evidence, invention rights and commercial outcomes remain outside this public methodology.

**Release:** v2.4-beta, 2026-10-18. **Last stable:** v2.2, 2026-10-17.

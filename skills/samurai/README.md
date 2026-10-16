# Samurai Skill — v2.1

**Find the hidden boundary. Transfer the useful mechanism. Build what the evidence earns.**

A working, provider-neutral agent skill for **inventor-architect polymathic reasoning**. Its method follows the chain:

`breadth → abstraction → analogy → synthesis → architecture → invention → execution`

Its signature competency is **novel transfer**: independently retrieve a distant-domain idea, extract its causal mechanism, map it carefully, reject what does not transfer, recombine what does, and demonstrate how it changes the solution.

## What's new in v2

v1 centered primarily on **inside / between / outside the observable system**. That remains a valuable diagnostic. v2 expands the core method to the full seven-stage reasoning process, makes structural analogy and adaptation explicit, strengthens evidence and falsification gates, and adds a rubric that can be used in blind assessment when independent facilitators and raters are available.

## Use cases

- Reframing problems incorrectly labeled as AI, integration, or data-wrangling issues
- Creating new product/platform/customer relationships and operating models
- Testing a leader's ability to transfer useful mechanisms across unfamiliar fields
- Designing and running consumer-products **Samurai missions**
- Distinguishing a persuasive concept from evidence, a prototype, a launch, or verified invention

## Example: Consumer-products attribution, as a fictional teaching case

The apparent task is to unify customer, retailer, affiliate, and support data. The deeper question is whether the information needed for an attribution decision **was ever inside the observable system**. A private family recommendation followed by an offline retail purchase may leave no reconstructable event chain. The candidate mechanism separates two independent jobs: **useful, permissioned product experiences** that create future customer goal/action/outcome state, and **credible aggregate marketing experiments** that estimate incremental lift even without an observed private journey. A typed evidence contract prevents directly observed, self-reported, inferred, experimental, and unknown claims from being silently merged. This is a hypothesis, not established novelty, product deployment, or proof of historical customer referrals.

## Install

For Agent Skills-compatible environments:

```bash
npx skills add yoda-sahb/Gen_AI_Skills_Personal --skill samurai
```

## How to use

Copy/install the `samurai` directory as an Agent Skill where supported, or give an assistant the `SKILL.md` file with its references.

Example prompts:

- "Use Samurai Skill to diagnose this problem before recommending solutions."
- "Apply the seven-stage chain; identify candidate analogies and their failure boundaries."
- "Evaluate the novelty of this cross-domain transfer, not just the analogy."
- "Run Samurai Mission 1 interactively. Do not show future reveals."
- "Set up a blinded evaluation using independent raters. Score this work using the rubric and distinguish spontaneous from prompted reasoning."

## Contents

- `SKILL.md` — operating logic, 7-stage method, response contract and guardrails
- `references/NOVEL_TRANSFER.md` — structural transfer test and worked comparison
- `references/EVALUATION.md` — 100-point scoring framework; not a clinical test
- `references/SAMURAI_MISSIONS.md` — five fictional consumer-products mission concepts, staged reveals, instructor rules
- `references/CASE_TRACE.md` — attribution case traced through all seven stages
- `experiments/ATTRIBUTION_STRESS_TEST.md` — sequential adversarial reasoning test and provisional invention
- `experiments/attribution_simulation.py` — seeded synthetic attribution-vs-incrementality test (requires NumPy)

## Provenance and boundary

This package is a public working method, not independent evidence about any company or person's career. All cases are fictional training scenarios. No specific product, architecture, customer behavior, or organizational failure is asserted as fact.

**Version:** 2.1, experiment-hardened working release, 2026-10-16. The published exercise is a single-assistant stress test, not independent validation.
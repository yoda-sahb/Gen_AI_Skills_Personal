# Patent Discovery Gate — Samurai v2.2

**Goal:** Force inventive mechanism discovery without converting every idea into an unsupported patent claim. Apply to **every substantive new technical, product or system mechanism**, whether the user asks about patents or not. For non-inventive strategy and ordinary operations, report `NOT_APPLICABLE`.

## Required procedure

1. **Mechanism, not aspiration:** Define the closest existing baseline and the precise operations, components, interactions and constraints that are different. A revenue goal, UX benefit or “use AI” is not a claim kernel.
2. **Narrow candidate:** Identify the smallest potentially inventive technical feature/combination and what parts are reused. If none, explain `NONE_IDENTIFIED`.
3. **Prior-art challenge:** Search relevant granted patents, published applications, papers, standards, prior public products and ordinary engineering methods as available. Record actual citations/claim comparisons, dates, search terms and coverage gaps. If unavailable, mark `SEARCH_NOT_RUN` and do not assert global novelty.
4. **Adversarial patent thought:** Ask how a skeptical examiner or engineer would challenge novelty, inventive step/non-obviousness, eligibility, technical specificity or enablement. Identify at least one plausible design-around and any common combination that may teach the same mechanism.
5. **Technical consequence:** Explain what concrete technical behavior improves over the comparator; design the cheapest decisive proof/kill experiment. Customer value, feasibility and patent law are separate tests.
6. **Rights and disclosure:** Flag potential employment/contractual assignment, third-party IP, inventorship uncertainty, confidential details, public disclosure and publication timing; do not decide ownership, inventorship, freedom to operate or filing strategy.
7. **Disposition:** Return one preliminary screening result with a specific next step. Legal patentability and filing decisions require qualified professional review.

## Mandatory screening card

- **Mechanism and baseline:** exact difference, not a benefit slogan
- **Candidate claim kernel:** narrow technical steps or `NONE_IDENTIFIED`
- **Closest known comparison:** checked source identifiers or `SEARCH_NOT_RUN`
- **Prior-art/eligibility challenge:** anticipation, routine combination, abstractness, enablement, other uncertainty
- **Design-around and competing solution:** at least one
- **Test:** minimal technical validation and kill criterion
- **Rights/disclosure:** `CLEARLY_PUBLIC`, `RESTRICTED`, or `UNRESOLVED` (screening only)
- **Outcome:** one status below
- **Next action:** search, narrow, experiment, expert review or stop

## Outcome labels (NOT legal rulings)

- `NOT_APPLICABLE`: no substantive candidate mechanism; do not use to escape examining a real candidate.
- `CANDIDATE`: specific potential differential after some comparative examination, but legal novelty/patentability/ownership remain unestablished.
- `PRIOR_ART_CONFLICT`: identifiable prior disclosure appears to teach material proposed features; revise or stop, no claim of legal invalidity.
- `INSUFFICIENT_DIFFERENTIATION`: no credible difference beyond known design or generic AI automation.
- `REVIEW_REQUIRED`: substantive possible difference but prior-art search, implementation details, legal eligibility, inventorship, rights or disclosure insufficient. This is the default when required comparison was not done.

## Prohibitions

Do not invent patent citations, assert world-first status, infer inventor identity from brainstorming, reveal restricted source material in public outputs, convert speculative inventions into verified `INV-###`, or confuse freedom to operate with patentability. The screen is not attorney advice.

## Two short fictional examples

- “Use AI to score executives by automated metrics.” If no new technical mechanism is specified, `INSUFFICIENT_DIFFERENTIATION`. Organizational improvement alone is not established patent-eligible invention.
- “Pass typed observed/inferred/experimentally estimated evidence through a consent-scoped decision protocol.” Potential specific technical mechanism, but known provenance and rules-engine work may overlap. Without a real prior-art comparison, use `REVIEW_REQUIRED`, not `CANDIDATE` or “patentable.”

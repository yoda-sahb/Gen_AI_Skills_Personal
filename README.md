<p align="center"><img src="./assets/hero.svg" alt="Gen AI Skills: reusable reasoning and writing skills" width="100%"></p>

# Gen AI Skills

Reusable, inspectable Agent Skills for better problem solving, strategy, storytelling and writing. Each has one `SKILL.md` that works in compatible AI-agent environments.

**[Explore skills](#choose-a-skill) · [Try a prompt](#try-it) · [Install](#install) · [View the public page](./index.html)**

## Choose a skill

| Skill | Best for | Status |
| --- | --- | --- |
| **[Samurai 3.0](./skills/samurai-3/README.md)** | Anyone with a problem: find the root cause, compare alternatives, prove value, anticipate failure, and make the change usable. | **Public preview — evaluation pending** |
| [Product Value-Strategy](./skills/product-value-strategy/README.md) | What the real buyer values, the strongest alternatives, relative advantage, pricing, and resource allocation. | Available |
| [Root-to-One CEO Brief](./skills/root-to-one-ceo-brief/README.md) | Reframe a difficult executive problem, preserve business constraints, and identify the cheapest decisive proof. | Available |
| [Executive Whitepaper Writer](./skills/executive-whitepaper-writer/README.md) | Turn research into one cohesive, evidence-bound executive argument. | Available |
| [Storytelling](./skills/storytelling/README.md) | Build a narrative that reveals its mechanism before naming it. | Available |
| [Wordsmith](./skills/wordsmith/README.md) | Improve clarity and expression without changing the underlying facts. | Available |

### Samurai versions — one recommended starting point

| Version | Purpose | Status |
| --- | --- | --- |
| **[3.0](./skills/samurai-3/README.md)** (`samurai-3`) | General-purpose conversational problem solving. Root-to-One, Samurai, conditional dual-mandate innovation, relative value, pre-mortems, proof, adoption, and evals. | **Public preview; use for evaluation and pilots** |
| [2.2](./skills/samurai/README.md) (`samurai`) | Original seven-stage inventor-architect method and novelty/patent gates. | Last stable release |
| [2.5-beta](./skills/samurai-beta/README.md) (`samurai-beta`) | Experimental boundary, obligations and context-gated innovation routing. | **Experimental archive; not a replacement for 3.0 or validated** |

Older versions stay accessible for provenance and comparison. They are not three separate recommended installations. No version has yet passed independent enterprise usability or safety validation.

## Start with a problem

For Samurai 3.0, no worksheet or specialist vocabulary is needed:

```text
Use Samurai 3.0. I have a problem: [describe what is happening].
Help me find the actual cause, identify a simpler alternative,
design the smallest honest test, and anticipate what could fail.
Ask only the next necessary question.
```

The six plain-language moves are **Unlock → Root → Reframe → Prove → Build to One → Graduate**. The advanced engine preserves Samurai's **Breadth → Abstraction → Analogy → Synthesis → Architecture → Invention → Execution**.

The skill may recommend an existing fix, no AI, an experiment, an escalation, or stopping. A simulation is not a production result; a hypothesis is not an invention; a persuasive demonstration is not proof.

## Try it

- **[Samurai 3.0](./skills/samurai-3/README.md):** Bring a real problem and use the conversational prompt above.
- **[Product Value-Strategy](./skills/product-value-strategy/README.md):** "Who is deciding, what do they value, what can they do instead, and where is our relative advantage actually evidenced?"
- **[Root-to-One CEO Brief](./skills/root-to-one-ceo-brief/README.md):** "What are we trying to unlock, what must remain true, where does the real constraint sit, and what is the next proof?"
- **[Storytelling](./skills/storytelling/README.md):** "Help the reader see the mechanism before naming the idea."
- **[Wordsmith](./skills/wordsmith/README.md):** "Edit this without increasing certainty or changing my meaning."

The public [`index.html`](./index.html) includes a prompt-builder for Product Value-Strategy. It is not an AI backend or an evaluation result.

## Install

Install only the skill you need in a compatible Agent Skills environment:

```bash
npx skills add yoda-sahb/Gen_AI_Skills_Personal --skill samurai-3
```

For the other skills, substitute `product-value-strategy`, `root-to-one-ceo-brief`, `executive-whitepaper-writer`, `storytelling`, or `wordsmith`.

Historical versions can still be installed by explicitly selecting `samurai` (v2.2) or `samurai-beta` (v2.5-beta). Their prompts and tests are not an independent certification of improved model behavior.

## Provenance and safeguards

- Samurai is an original seven-stage reasoning method with structured novelty, system-boundary, falsification, and patent-discovery gates.
- Root-to-One is a separate systems-first method, used as a six-move employee-facing journey in Samurai 3.0.
- Product Value-Strategy operationalizes value-strategy concepts attributed to Dwight Porter. Extensions such as behavioral resource-reallocation checks are not attributed to Porter without independent sourcing or endorsement.
- Adoption guidance draws on high-level principles from *Switch* by Chip and Dan Heath; the new integrated skill does not represent itself as their official work.
- Skill evals assess the assistant's reasoning; intervention experiments assess whether the proposed real-world solution works. Structural test passes alone are not independent validation.
- Do not share proprietary, confidential, regulated or personally identifying information with an AI environment that is not authorized for it. Human approvals remain necessary for consequential actions.

**Licensing:** This repository is publicly viewable, but it does not yet include an explicit reuse license. Public visibility does not automatically grant redistribution or commercial rights. Licensing remains to be decided by the rights holder.

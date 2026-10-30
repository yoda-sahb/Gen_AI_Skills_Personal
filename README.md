<p align="center">
  <img src="./assets/hero.svg" alt="Gen AI Skills — Better thinking, stories, and writing for AI" width="100%">
</p>

<p align="center">
  <strong><a href="#choose-a-skill">Browse Skills</a></strong> ·
  <strong><a href="#try-it">Try One</a></strong> ·
  <strong><a href="#install">Install</a></strong> ·
  <strong><a href="./index.html">Open Public Page</a></strong>
</p>

Reusable skills for ChatGPT, Claude, and other Agent Skills-compatible systems. Each skill targets a recurring failure mode that generic prompting tends to miss.

## Choose a skill

| Skill | Use it when | Core promise |
| --- | --- | --- |
| [**Samurai 3.0**](./skills/samurai-3/README.md) · *Public preview* | You have a real problem and need to find its root, compare alternatives, prove value, and make the solution usable. | **Find the real problem. Prove the next move.** |
| [**Product Value-Strategy**](./skills/product-value-strategy/README.md) | You need to decide what to build, position, price, prioritize, or reject. | **Find where the buyer actually has a reason to choose you.** |
| [**Root-to-One CEO Brief**](./skills/root-to-one-ceo-brief/README.md) | You have a hard strategic problem and need to find the root, reframe the system, and define the next proof. | **Make the decision clearer before you make the solution bigger.** |
| [**Storytelling**](./skills/storytelling/README.md) | The idea is strong but the narrative is flat, framework-first, or over-explained. | **Make the audience understand the idea before you name it.** |
| [**Executive Whitepaper Writer**](./skills/executive-whitepaper-writer/README.md) | You have the analysis but need a cohesive, evidence-based executive paper. | **Build one clear argument without hype or unsupported claims.** |
| [**Wordsmith**](./skills/wordsmith/README.md) | The thought is right but the wording is loose, generic, or over-polished. | **Make the sentence better without changing the thought.** |

### A useful sequence

`Samurai 3.0 → discover the real problem and test a solution`

`Product Value-Strategy → establish relative value against real alternatives`

`Root-to-One CEO Brief → turn a difficult strategic decision into a concise executive argument`

`Storytelling → make the mechanism understandable`

`Wordsmith → make the words sharper without changing the claim`

---

## Why Gen AI Skills

Generic AI is good at making an answer sound coherent. The harder failure modes come next: the buyer has alternatives, people have incentives, budgets move, a convincing demo is mistaken for proof, and polished language can quietly change the thought underneath it.

Gen AI Skills turns those recurring failure modes into reusable operating instructions, not a collection of disconnected prompts.

## Samurai 3.0

**Find the real problem. Prove the next move.**

Start with “I have a problem.” Samurai asks only what is needed to diagnose the root, understand the value of solving it, and choose the smallest evidence-backed next step.

Its employee-facing operating sequence is:

`Unlock → Root → Reframe → Prove → Build to One → Graduate`

Underneath that sequence are the original seven-stage Samurai invention method, conditional dual-mandate innovation, buyer-relative value, pre-mortems, honest proof levels, and adoption planning. The skill is allowed to recommend using an existing tool, choosing a non-AI solution, testing a hypothesis, escalating, or stopping.

**Public preview.** Eighteen cross-role test scenarios and a structural eval harness are included. This is not an independently validated enterprise product or evidence of commercial impact.

[Explore Samurai 3.0 →](./skills/samurai-3/README.md)

## Product Value-Strategy

**Find where the buyer actually has a reason to choose you.**

Start with what a specific buyer values, compare the strongest realistic alternatives, establish where your offering has a meaningful advantage, and examine how incentives and budget reallocations affect the economics.

**A strategy is not finished just because the proposed option is relevant. It must be superior enough to change an actual decision.**

[Explore Product Value-Strategy →](./skills/product-value-strategy/README.md)

## Root-to-One CEO Brief

**Make the decision clearer before you make the solution bigger.**

Find the real constraint, distinguish fundamental limitations from inherited architecture, and define the cheapest decisive experiment. The completed CEO brief requires a decision-relevant visual, a documented example with its limits, and a concrete decision.

[Explore Root-to-One CEO Brief →](./skills/root-to-one-ceo-brief/README.md)

## Executive Whitepaper Writer

**Build one clear argument without hype or unsupported claims.**

Turn research and strategy into a cohesive, evidence-bound executive paper with a decisive thesis and connected reasoning.

[Explore Executive Whitepaper Writer →](./skills/executive-whitepaper-writer/README.md)

## Storytelling

**Make the audience understand the idea before you name it.**

Build tension around a real question, reveal the mechanism through examples, and make the ending change how the opening is understood.

[Explore Storytelling →](./skills/storytelling/README.md)

## Wordsmith

**Make the sentence better without changing the thought.**

Cut filler, clarify the structure, improve cadence, and protect meaning, evidence and voice.

[Explore Wordsmith →](./skills/wordsmith/README.md)

---

## Try it

### Samurai 3.0

```text
Use Samurai 3.0. I have a problem: [describe what is happening].
Help me identify the real cause and the strongest existing alternative.
Recommend the smallest honest test and consider why the plan might fail.
Ask only the next necessary question.
```

### Product Value-Strategy

```text
Use Product Value-Strategy on this decision.
Identify what the buyer values, what they can do instead,
where our relative advantage is genuinely supported,
and what people will actually do with their resources.

[PASTE DECISION]
```

The public [site page](./index.html) includes a separate Product Value-Strategy prompt builder; it is not an AI backend.

## Install

For compatible Agent Skills environments:

```bash
npx skills add yoda-sahb/Gen_AI_Skills_Personal --skill samurai-3
```

Replace `samurai-3` with `product-value-strategy`, `root-to-one-ceo-brief`, `executive-whitepaper-writer`, `storytelling`, or `wordsmith` to install another skill.

Each skill has one shared `SKILL.md`; there are no separate ChatGPT- and Claude-specific implementations.

<details>
<summary><strong>Samurai version history</strong></summary>

| Version | Purpose | Status |
| --- | --- | --- |
| [3.0](./skills/samurai-3/README.md) · `samurai-3` | Universal conversational problem solving, value, proof, pre-mortems and adoption | **Public preview; evaluation pending** |
| [2.2](./skills/samurai/README.md) · `samurai` | Original seven-stage inventor-architect method | Last stable baseline |
| [2.5-beta](./skills/samurai-beta/README.md) · `samurai-beta` | Boundary and contextual innovation experiments | Experimental archive |

Older versions remain accessible for provenance and comparisons. None is an independently validated organizational deployment.

</details>

## Attribution and evidence

The value-strategy foundation is an independent operationalization of concepts attributed to Dwight Porter, not his official publication or endorsement. Relative-premium operating procedures, behavioral reality checks, evidence handling and the combined Samurai 3.0 routing are implementation extensions, not automatically attributable to Porter. Root-to-One CEO Brief is a separate systems-first method; adoption ideas in Samurai 3.0 draw on high-level principles from *Switch* by Chip and Dan Heath.

Skill evals test assistant behavior; experiments test whether a proposed solution works. Neither should be represented as the other. Do not enter confidential, regulated or customer personal information into an unapproved AI environment.

**Licensing:** This repository is publicly viewable but does not yet specify a reuse license. Public visibility alone does not confer redistribution or commercial rights. The rights holder can establish licensing separately.

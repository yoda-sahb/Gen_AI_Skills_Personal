<p align="center">
  <img src="./assets/hero.svg" alt="Gen AI Skills: practical methods for clearer decisions, stories, and writing" width="100%">
</p>

<p align="center">
  <a href="#skills">Browse skills</a> ·
  <a href="#try-a-skill">Try a skill</a> ·
  <a href="#install">Install</a> ·
  <a href="./index.html">Open the skills page</a>
</p>

Reusable skills for ChatGPT, Claude, and other Agent Skills-compatible systems. Each one gives an AI a repeatable method for a specific kind of work.

## Skills

| Skill | Use it when | Promise |
| --- | --- | --- |
| [**Samurai 3.0**](./skills/samurai-3/README.md) · Public preview | You have a messy problem and need to find its cause, compare options, test a next step, and make it usable. | Find the real problem. Prove the next move. |
| [**Product Value-Strategy**](./skills/product-value-strategy/README.md) | You need to decide what to build, position, price, prioritize, or reject. | Find the reason a buyer should choose you. |
| [**Root-to-One CEO Brief**](./skills/root-to-one-ceo-brief/README.md) | A hard strategic problem needs a reframe, evidence plan, and executive decision. | Make the decision clearer before the solution gets bigger. |
| [**Executive Whitepaper Writer**](./skills/executive-whitepaper-writer/README.md) | Research and analysis need to become an evidence-based executive paper. | Build one clear argument. |
| [**Storytelling**](./skills/storytelling/README.md) | A strong idea is trapped in a flat, framework-first, or over-explained story. | Make the audience see the idea before naming it. |
| [**Wordsmith**](./skills/wordsmith/README.md) | The wording needs to improve without changing the underlying thought. | Sharpen the sentence. Preserve the meaning. |

## A useful sequence

`Samurai 3.0` helps diagnose and test a problem. `Product Value-Strategy` compares relative value against real alternatives. `Root-to-One CEO Brief` turns a strategic decision into an executive case. `Storytelling` makes the mechanism clear. `Wordsmith` tightens the language.

## Why these skills

Generic AI can make an answer sound coherent while missing the buyer's alternatives, human incentives, evidence quality, or the meaning underneath polished language. These skills make those considerations part of the work.

## Try a skill

The [skills page](./index.html) includes a Product Value-Strategy prompt builder. It creates a prompt in your browser; it does not connect to an AI service.

Example:

```text
Use Product Value-Strategy on this decision.
Identify what the buyer values, what they can do instead,
where our relative advantage is supported,
and what people will actually do with their resources.

[PASTE DECISION]
```

## Install

For compatible Agent Skills environments:

```bash
npx skills add yoda-sahb/Gen_AI_Skills_Personal --skill samurai-3
```

Replace `samurai-3` with `product-value-strategy`, `root-to-one-ceo-brief`, `executive-whitepaper-writer`, `storytelling`, or `wordsmith`. Each skill uses one shared `SKILL.md`.

## Attribution and reuse

Product Value-Strategy independently operationalizes concepts attributed to Dwight Porter. It is not an official publication or endorsement. Samurai 3.0 combines distinct public methods, including adoption principles drawn from *Switch* by Chip and Dan Heath.

Skill evaluations assess assistant behavior; they do not prove that a proposed solution works. Do not enter confidential, regulated, or personal information into an AI environment unless it is approved for that data.

**License:** This repository does not currently specify a reuse license. Public visibility does not itself grant redistribution or commercial rights.

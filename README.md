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
|---|---|---|
| [**Product Value-Strategy**](./skills/product-value-strategy/README.md) | You need to decide what to build, position, price, prioritize, or reject. | **Find where the buyer actually has a reason to choose you.** |
| [**Storytelling**](./skills/storytelling/README.md) | The idea is strong but the narrative is flat, framework-first, or over-explained. | **Make the audience understand the idea before you name it.** |
| [**Wordsmith**](./skills/wordsmith/README.md) | The thought is right but the wording is loose, generic, or over-polished. | **Make the sentence better without changing the thought.** |

### A useful sequence

`Product Value-Strategy → choose the strongest argument`

`Storytelling → make the argument unfold`

`Wordsmith → improve the language without changing the argument`

---

## Why Gen AI Skills

Generic AI is good at making an answer sound coherent. The harder failure modes come next: the buyer has alternatives, people have incentives, budgets move, stories drift away from their thesis, and polished language can quietly change the thought underneath it.

Gen AI Skills turns those recurring failure modes into reusable operating instructions rather than one-off prompts.

## Product Value-Strategy

**Find where the buyer actually has a reason to choose you.**

Use it when you need to decide what to build, how to position it, where you actually have premium, or whether the thesis collapses once you compare it with the best thing the buyer can do instead.

It forces four questions:

1. **What does this buyer actually value?**
2. **What can they do instead?**
3. **Where are you meaningfully better rather than merely relevant?**
4. **What will the people inside the system actually do once incentives, budgets, authority, and reallocation enter the model?**

That fourth question is the built-in **Behavioral Reality Check**:

> **Put the people back in the model.**

A strategy is not finished if it only works because someone stops spending, gives up economics, cooperates against their incentives, or lets a saved resource disappear.

[Explore Product Value-Strategy →](./skills/product-value-strategy/README.md)

## Storytelling

**Make the audience understand the idea before you name it.**

Use it when the idea is strong but the narrative feels flat, over-explained, framework-first, or hijacked by a good anecdote.

Storytelling:

- locks the governing thesis before shaping the narrative;
- creates a live question, tension, or puzzle;
- reveals the mechanism progressively;
- uses examples only when they do explanatory work;
- applies the **show-before-name** rule to specialized concepts and frameworks; and
- earns the ending by changing how the opening is understood.

> **A strong story does not announce the insight. It makes the audience see why the insight has to be true.**

[Explore Storytelling →](./skills/storytelling/README.md)

## Wordsmith

**Make the sentence better without changing the thought.**

Use it when the idea is already there but the wording is loose, generic, over-polished, corporate, or simply not memorable enough.

Wordsmith:

- locks the meaning before editing;
- cuts filler before inventing new language;
- prefers concrete nouns and verbs;
- protects plain language and distinctive voice;
- improves cadence, compression, naming, headlines, and titles; and
- refuses to quietly strengthen facts, certainty, or claims just to make the prose sound better.

> **Better wording should make the thought clearer, not turn it into a different thought.**

[Explore Wordsmith →](./skills/wordsmith/README.md)

---

## Try it

### Product Value-Strategy

The repository includes a lightweight public page for exploring the method without an API key. Open [`index.html`](./index.html) locally, or use the skill directly in a compatible agent.

```text
Use Product Value-Strategy on this decision. Identify what the buyer values, the strongest alternatives, where I have real premium, and run the Behavioral Reality Check:

[PASTE DECISION]
```

### Storytelling

```text
Use Storytelling on these notes. Keep the thesis intact, but make the idea unfold naturally:

[PASTE NOTES]
```

### Wordsmith

```text
Wordsmith this without changing the argument:

[PASTE TEXT]
```

## Install

There is one shared implementation per skill:

```text
skills/product-value-strategy/SKILL.md
skills/storytelling/SKILL.md
skills/wordsmith/SKILL.md
```

For Agent Skills-compatible coding agents:

```bash
npx skills add yoda-sahb/Gen_AI_Skills_Personal --skill product-value-strategy
npx skills add yoda-sahb/Gen_AI_Skills_Personal --skill storytelling
npx skills add yoda-sahb/Gen_AI_Skills_Personal --skill wordsmith
```

For ChatGPT Skills or Claude environments that support Agent Skills, use the same skill folders. The core instructions are not forked into separate ChatGPT and Claude versions.

### Why `SKILL.md`?

Because that is the shared Agent Skills convention. It is implementation plumbing, not the product name.

The human-facing products are **Product Value-Strategy**, **Storytelling**, and **Wordsmith**. `SKILL.md` is what compatible agents load when a skill is relevant.

## Public design principle

Each public skill should make five things obvious without requiring the reader to inspect the implementation:

`Problem → Method → Example → Try it → Install`

The implementation remains inspectable for builders, but the repository is designed first as a product portfolio rather than a folder of prompt files.

## Attribution

The value-strategy foundation in Product Value-Strategy is an independent operationalization of concepts attributed to Dwight Porter, including Value Drivers, Product Offering thinking, product-line ownership framing, and value / pricing concepts.

Gen AI Skills is not an official Dwight Porter publication and is not presented as endorsed by him. The relative-premium operating model, evidence handling, bundle tests, AI-execution structure, and Behavioral Reality Check are implementation extensions and should not be attributed to Porter without independent sourcing.

Storytelling and Wordsmith are independent writing skills.

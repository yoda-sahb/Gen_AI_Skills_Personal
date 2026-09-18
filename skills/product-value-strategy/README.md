# Product Value-Strategy

**Find where the buyer actually has a reason to choose you.**

Most strategy starts with what we built, what we are good at, or what we want to sell. This skill starts somewhere harder:

> **What can the decision-maker do instead?**

Product Value-Strategy is useful when an option looks relevant or differentiated, but that is not enough to know whether it should win.

## The four tests

### 1. What does the buyer actually value?

Identify the outcomes that really change the decision. Capabilities only matter when they move those outcomes.

### 2. What can the buyer do instead?

Compare against the strongest real alternatives: incumbent, internal build, current team, another vendor, multiple specialists, delay, or reallocation.

### 3. Where are you actually better?

Separate:

- relevance;
- alternative supply;
- evidence strength; and
- relative advantage.

A capability can be important and still create no premium if the buyer can source it easily somewhere else.

### 4. What will people actually do?

Run the built-in **Behavioral Reality Check**.

> **Put the people back in the model.**

A strategy fails the test if it only works because someone stops spending, gives up economics, cooperates against their incentives, or lets a saved resource disappear.

For advertising, that means a poor media decision usually does not imply unused budget. The budget is more likely to move somewhere else.

## Use it for

- product strategy;
- positioning;
- pricing;
- market entry;
- portfolio choices;
- build / buy / partner decisions; and
- deciding what *not* to fund.

## Example

```text
Use Product Value-Strategy on this decision:

We are considering a premium AI analytics product for enterprise customers. The technology is differentiated, but customers may be able to get most of the value from their existing warehouse, BI stack, and internal team.

Should we launch? What should lead the positioning? What should we deliberately not build?
```

A full run should identify:

- the actual decision;
- the strongest alternatives;
- the value drivers that matter;
- supported advantage versus parity or uncertainty;
- the Behavioral Reality Check on incentives and reallocation;
- the strategic crux;
- explicit non-priorities; and
- the evidence that could change the conclusion.

## ChatGPT + Claude

There is one implementation:

[`SKILL.md`](./SKILL.md)

The same core skill is designed for Agent Skills-compatible environments rather than separate ChatGPT and Claude forks.

- **ChatGPT Skills:** use or upload the `product-value-strategy` skill in a ChatGPT environment that supports Skills.
- **Claude / Claude Code:** use the same skill folder in an Agent Skills-compatible Claude environment.
- **Other agents:** the folder follows the shared `SKILL.md` Agent Skills convention and can be used by compatible runtimes.

For compatible coding agents, you can also install from the repository with:

```bash
npx skills add yoda-sahb/Gen_AI_Skills_Personal --skill product-value-strategy
```

## Why `SKILL.md`?

Because that is the shared implementation convention. It is not the brand.

**Product Value-Strategy** is the product name. `SKILL.md` is the file compatible agents load.

## Attribution

The value-strategy foundation is an independent operationalization of concepts attributed to Dwight Porter, including Value Drivers, Product Offering thinking, product-line ownership framing, and value / pricing concepts.

This repository is not an official Dwight Porter publication and is not presented as endorsed by him. The relative-premium operating model, evidence handling, bundle tests, AI-execution structure, and Behavioral Reality Check are implementation extensions and should not be attributed to Porter without independent sourcing.

# Wordsmith

**Make the sentence better without changing the thought.**

AI is very good at making writing sound polished. It is also very good at quietly changing the argument, increasing certainty, flattening voice, and replacing plain language with corporate language.

Wordsmith is built to prevent that.

## What it does

Wordsmith improves wording at the sentence and phrase level while protecting the underlying meaning.

It focuses on four things:

1. **Lock the meaning** — preserve the claim, facts, uncertainty, and important caveats.
2. **Cut before replacing** — remove filler, repetition, throat-clearing, and jargon before inventing new language.
3. **Keep it concrete** — prefer strong nouns, verbs, and language that is easy to say aloud.
4. **Protect the voice** — do not professionalize away distinctive wording just because a smoother phrase exists.

It also handles naming, cadence, compression, headlines, titles, and short-form phrasing.

## Try it

```text
Wordsmith this without changing the argument:

We need to create a platform capability that enables teams to more effectively orchestrate experimentation across multiple product surfaces.
```

A better result should get closer to the actual idea rather than simply sounding more polished.

Other useful triggers:

```text
Tighten this.
Make this punchier.
Make this sound less corporate.
Improve the cadence.
Give this a better name.
Keep my voice, but make it clearer.
```

## ChatGPT + Claude

There is one implementation:

[`SKILL.md`](./SKILL.md)

The same core skill is designed for Agent Skills-compatible ChatGPT/OpenAI and Claude/Anthropic environments. There is no separate provider-specific fork.

For compatible coding agents:

```bash
npx skills add yoda-sahb/Gen_AI_Skills_Personal --skill wordsmith
```

## The rule

> **Better wording should make the thought clearer, not turn it into a different thought.**

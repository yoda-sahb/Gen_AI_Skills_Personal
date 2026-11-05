# Book Studio

Adapt a classical author's work into thematic narrative nonfiction. Apply the same method to a later scholar selected for a book.

[Download Book Studio ZIP](../../downloads/book-studio.zip?raw=1)

## How it works

1. **Reconstruct the argument.** Read the primary texts, trace claims to specific passages, and preserve qualifications and disagreements.
2. **Reorganize by theme.** Bring together passages that answer the same question, even across different works. Order chapters by what readers need to discover next.
3. **Write through discovery.** Open with a documented case or a clearly labeled hypothetical. Let readers form a plausible first explanation. Use a detail, comparison, or counterexample to change it, then show what the author's reasoning explains. Write in an original voice.

The skill includes guidance for research, composition, book records, and release. [Read SKILL.md](./SKILL.md)

## Try it

```text
Use Book Studio to adapt the work of [author] for general readers.

[Add primary texts, editions, and the book brief.]

Group the author's arguments by theme and propose a chapter sequence. For
each chapter, give the supporting passages, the question or case driving
it, and the strongest qualification. If the sources support the plan,
draft one opening that lets the reader see the puzzle before you name
the author's concept.
```

## Install

For an Agent Skills-compatible environment, unzip the download and install the complete `book-studio/` folder. With the Skills CLI, run the following command.

```bash
npx skills add yoda-sahb/Gen_AI_Skills_Personal --skill book-studio
```

## Evaluation

Two synthetic cases tested thematic organization, narrative discovery, source fidelity, and what happens when a primary text is missing. [Results and replay inputs](../../evals/book-studio/adaptation.md)

# Book Studio

Adapt a classical author's work into thematic narrative nonfiction. Apply the same method to a later scholar selected for a book.

[Download Book Studio ZIP](../../downloads/book-studio.zip?raw=1)

## How it works

1. **Reconstruct the argument.** Read the primary texts, trace claims to specific passages, and preserve qualifications and disagreements.
2. **Reorganize by theme.** Bring together passages that answer the same question, even across different works. Order chapters by what readers need to discover next.
3. **Calibrate the writing voice.** Match a user-provided or approved prose sample before drafting at length. A “Gladwell-style” cue means narrative accessibility, not automatic use of dramatic reportage or imitation.
4. **Write through discovery.** Begin with a recognizable question or case in the approved register. Develop the tension in natural paragraphs, explain the author's reasoning plainly, and apply it to ordinary life without disguising editorial inference as the author's words.

The skill includes guidance for research, composition, [voice calibration](./references/voice-calibration.md), book records, and release. [Read SKILL.md](./SKILL.md).

## Try it

```text
Use Book Studio to adapt the work of [author] for general readers.

[Add primary texts, editions, and the book brief.]

Group the author's arguments by theme and propose a chapter sequence. For
each chapter, give the supporting passages, the question or case driving
it, and the strongest qualification. If the sources support the plan,
draft one opening that lets the reader see the puzzle before you name
the author's concept. If I supply a writing sample, calibrate the prose
to its rhythm, chapter structure, and level of explanation first.
```

## Install in ChatGPT

Open https://chatgpt.com/skills and choose **Create → Upload from your computer**. Upload a ZIP containing the `book-studio/` folder, its `SKILL.md`, and the `references/` directory. The current Book Studio ZIP is linked above. Installation is subject to plan and workspace support.

Updating this GitHub repository does **not** automatically update a copy that you have installed in ChatGPT; upload the current ZIP again if needed.

## Install in an Agent Skills environment

Unzip the download and install the complete `book-studio/` folder. With the Skills CLI:

```bash
npx skills add yoda-sahb/Gen_AI_Skills_Personal --skill book-studio
```

## Evaluation

Two synthetic cases tested thematic organization, narrative discovery, source fidelity, and missing-primary-text handling. [Results and replay inputs](../../evals/book-studio/adaptation.md). Changes to installation instructions do not constitute a new model evaluation.

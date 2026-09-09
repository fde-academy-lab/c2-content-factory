# Domain docs

How the engineering skills should consume this repository's domain documentation when exploring it.

## Before exploring, read these

- `CONTEXT.md` at the repository root.
- `docs/adr/`, reading the decision records that touch the area you are about to work in.

If either is missing, proceed silently. Do not flag the absence and do not suggest creating them upfront. The `/domain-modeling` skill, reached through `/grill-with-docs` and `/improve-codebase-architecture`, creates them lazily when a term or a decision actually gets resolved.

This is on top of the ground truth order in `CLAUDE.md`, which governs anything about the programme itself. A domain doc never outranks `docs/curriculum/` or the numbered programme documents.

## File structure

This repository is single-context, so both live at the root:

```
/
├── CONTEXT.md
├── docs/adr/
│   ├── 0001-<slug>.md
│   └── 0002-<slug>.md
├── content/
├── docs/
└── scripts/
```

## Use the glossary's vocabulary

When your output names a domain concept, whether in an issue title, a refactor proposal, a hypothesis or a test name, use the term as `CONTEXT.md` defines it. Do not drift to synonyms the glossary avoids.

A concept missing from the glossary is a signal. Either you are inventing language the project does not use, which is worth reconsidering, or there is a real gap worth noting for `/domain-modeling`.

## Flag ADR conflicts

If your output contradicts an existing ADR, surface it rather than quietly overriding it:

> Contradicts ADR-0007, which fixed the day pack folder layout, and it is worth reopening because...

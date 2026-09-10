---
name: companion-builder
description: Build the single-file HTML companion and the Excel decision tool that make a day's decision move on the projector and stay useful afterwards. Use whenever the work touches a demo, an activity, an interactive page, a toggle, a simulator, a playground, a decision tool or a workbook, and whenever a topic has a choice, a comparison or a hidden intermediate state that a slide cannot show. Trigger it on demo, activity, companion, HTML page, calculator, xlsx, workbook, run sheet or "let them play with it". Covers the guided walk, experiment cards, the diagram builder set ported to JavaScript, the two workbook forms and the browser sweep that proves every control works.
---

# Companion builder

A companion exists where a topic has a decision or a hidden state. Its job on the projector is to make the thing move, and its job afterwards is to be the tool a learner still opens in month three. One file, no install, no storage, no key.

Read `references/page-anatomy.md` for the page kinds and their parts, `references/diagram-builders.md` for the nine builders ported to JavaScript, and `references/workbooks.md` for the two Excel forms and their recalc manifest.

## What the day gets

| Artifact | Built when | Lives in |
|---|---|---|
| The HTML companion | The topic has a decision, a comparison or a hidden intermediate state | `demos/` |
| The Excel decision tool | Always, one per teaching day: one tab per taught decision, ending in a computed verdict | `demos/` |
| The live miniature | The day also carries a repeatable procedure a learner should run again | `demos/` |
| The recalc manifest | Beside every workbook | `demos/` |

## The HTML companion

**Structure.** A single page with sections and a left rail is enough for a one-topic day. A grouped title bar arrives only when the day has several distinct parts, and it groups by what the learner is doing rather than by topic name.

**The guided walk.** One Next button. A narration card per event. The diagram, the artifact and any meter move together as the walk advances, so the learner watches cause and effect rather than reading a description of it.

**Experiment cards.** Each card carries eight parts in this order: the situation, the hypothesis, what to watch for, a run control, what happened, why it matters, the rule, and a sequence popup. One change per card. The card that opens the page is the day's existing toggle idea, kept, because it is what the trainer already knows how to run.

**Diagrams.** Drawn by the same builder set the notebook helper uses, ported to JavaScript, so a diagram on a slide, in a notebook and in the companion are recognisably one drawing.

**A decision visual** wherever the topic has a choice: a tree for more than two outcomes, a matrix for two independent dimensions, a ladder for a threshold.

**A calculator** for any rule that has a number in it, showing its formula and one sentence on what the number means.

**A small glossary** of the day's terms, saying where each one first mattered.

## Rules

- Important text is never grey. Muted is for captions.
- Every control does something visible.
- Nothing is preloaded, so no button looks dead on arrival.
- A popup only where it adds a breakdown, a worked example, a sequence or a why-this-step.
- Full connected sentences everywhere, including inside cards.
- Simulation is labelled as simulation. Any price or rate carries its date. Nothing is invented.
- No browser storage, no key, no network call. The file opens from disk and works.

## The workbooks

**The decision tool.** One tab per taught decision, each ending in a computed verdict cell. An export tab assembles a paste-ready brief by formula. Yellow cells are inputs and everything else is computed. One planted defect per tab that the learner finds first. An interior optimum, so fixing one thing does not clear the release.

**The live miniature.** A run sheet of the procedure with an observed column and a computed status, plus a lookup from symptom to first check, fix, evidence and owner.

**Formulas that survive LibreOffice.** No XLOOKUP, no bare IFS. INDEX and MATCH, COUNTIF, SUMPRODUCT, IF, AND, OR, ROUND.

**The recalc manifest** sits beside each workbook and names the verdict cells to assert and the design decisions to flip, so `xlsx_recalc.py` can prove the tool actually computes rather than holding cached values.

## Done

- [ ] One file, no storage, no key, no network.
- [ ] The guided walk runs on one Next button with a narration card per event.
- [ ] Every experiment card carries all eight parts and changes one thing.
- [ ] The day's existing toggle idea is the first experiment.
- [ ] Diagrams come from the builder set, not from hand-written markup.
- [ ] A decision visual exists wherever the topic has a choice.
- [ ] A calculator exists for every rule with a number.
- [ ] The glossary covers the day's terms.
- [ ] `python3 scripts/html_sweep.py <file>` clicks every control, records zero console errors and finds no dead control.
- [ ] `python3 scripts/xlsx_recalc.py <workbook>` recalculates through LibreOffice, asserts every verdict cell, flips the decisions and asserts the moved verdicts.

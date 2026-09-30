---
name: notebook-builder
description: Build or raise a teaching notebook that runs, proves itself and reads as a document. Use whenever the work touches an .ipynb, a demo notebook, a hands-on notebook, an exercise notebook with TODO markers, a notebook that has to run cold in a Codespace, or a request to add checks, diagrams or executed outputs to something that already runs. Trigger it when someone says notebook, demo, hands-on, walkthrough code, "make the cells prove it", or hands over a script that a learner is meant to work through. Covers the shared helper module, the MAP, DO, SEE, CHECK, SUM rhythm, the trap that stages a plausible wrong number, and the pick-from-options exercise twin.
---

# Notebook builder

A notebook is a teaching document that happens to run. It is read far more often than it is executed, so it has to teach on the page: rendered diagrams, printed outputs and passing checks all visible before anybody presses run.

Read `references/helper-module.md` before writing the first cell, because the helper decides what every later cell can call. Read `references/notebook-shape.md` for the full cell-by-cell anatomy and `references/exercise-notebooks.md` when the artifact is a TODO twin rather than a teaching notebook.

## The shared helper

One module, `scripts/c2kit.py`, serves every notebook in the programme. Each notebook reaches it with the walk-up import in `references/helper-module.md`, and the deciding test is that `python3 scripts/verify.py <day folder> --execute` passes. `scripts/nb_make.py` assembles a notebook from cells and executes it cold in its own folder, so a rebuild is one command. The model notebooks are in `content/W01/D1/notebooks/`, and `.claude/skills/day-pack-builder/references/the-standard.md` says what they carry.

The helper holds these and nothing else:

- Loaders for the day's data from `../data/`, so the data file is the single source and no notebook pastes records inline.
- `check(label, condition, detail)` printing PASS or FAIL as HTML without raising, so one failure never stops a class, and `check_summary()` printing the totals.
- `table(headers, rows, caption)` for any result worth reading as a grid.
- `show_trace` and a message viewer wherever the day's topic has a trace.
- `expect_error()`, which shows a staged failure's error the way Jupyter prints it and keeps the notebook running.
- Thirteen diagram builders rendering SVG from a code cell, listed in the reference, each drawing a node by its kind: plain, lit, known, unknown, bad or good.

The helper reads its palette from `scripts/brand.py`, as the decks and cheat sheets do. It reaches no network, writes no browser storage and holds no key.

## The shape of a teaching notebook

**One notebook per chapter, and each builds on the last.** A day runs in about six chapters, and each chapter is one deck chapter and one notebook, numbered and titled alike. The notebooks grow the way a first agent does: a simple loop by hand, then one tool, then several tools, then the loop, then memory, then all of it together. Each notebook adds one decision to what the one before it established and says so in its first cell, and it goes deep on that one decision rather than touching six. Splitting a topic this way loses nothing: a chapter notebook of 20 to 36 cells carries more detail on its one step than a single day notebook ever held.

**The problem comes before the code.** After the opening, a `## The options` section lays out the two to four ways a team could answer the chapter's question, a sizing cell computes each one's cost on this data (rows touched, seconds, rupees, error), and a markdown cell makes the best-fit call and names the fact that would change it. Only then is the chosen way built. Near the end, `## A second route` reaches the same number another way and a check asserts the two agree. The code is the last mile of the chapter.

**Opening.** A title cell naming the topic, the chapter's number and place in the day, the stakeholder's question, the metric at stake and who asks for it, what a wrong number costs them, the real company that faces the same question, and the one-line promise. A setup cell importing the helper and loading the data, with the import documented in the markdown cell above it. Then a MAP code cell rendering two diagrams side by side, the day's notebook ladder with this one lit and a flow of what this notebook adds. In the C2 programme the title cell asks the chapter's question in full with **Who needs the answer.** and **The questions on the way.** beneath it, each section heading asks its level's question, the last markdown cell answers every one of them with its number, and the notebook runs and reads with nothing else open, per the question ladder and the self-contained rule in `day-pack-builder/references/the-standard.md`.

**Per section, in this order.**

1. A MAP cell: a flow of the section's steps with the current one lit, or a sequence or a stack where the concept has lanes or layers.
2. A prose cell of two to five full sentences saying what is about to happen and why it matters to a record in the running case, ending on **Predict before you run.**, a question with lettered options the learner answers before the code runs. A heading alone is not a prose cell.
3. One code cell carrying one idea.
4. The printed output, or a table or trace rendered by the helper, then a **What happened.** cell giving the answer letter and what the output means.
5. A CHECK cell with two or more `check()` calls asserting on the shape of what happened, never on wording.
6. At each milestone, the industry example and the interview question the milestone just made answerable.

**At least one trap per notebook**: the plausible wrong number computed the way a hurried analyst would, why it is wrong in business terms, the check that exposes it, and the fix with what changed. A runtime error met on the way gets one cell and its last line; a notebook never builds a section around a syntax error.

**Charts from the data.** Every level that produces a number shows it: `kit.columns` for groups, `kit.line` for a trend or a plan, `kit.bridge` for a reconciliation or a decomposition, `kit.strip` for a distribution and `kit.bars` for a ranking.

**A plant is found in an empty your-turn cell.** Where a section leads the learner to a record planted in the day's data, the markdown gives the lines to type and the code cell below it ships empty, so no saved output names the record. A mechanism that needs the plant to show is taught on invented numbers, labelled invented.

**Every logical group ends with a SUM cell**: a diagram from the helper and a table of what the group established.

**The final cell** prints `check_summary()` and one sentence on what the next notebook adds.

## Rules

- At least three rendered diagram outputs and five checks per notebook.
- Markdown in full connected sentences. A fragment heading never stands in for explanation.
- Headings name the topic. The assertion goes in the first line under the heading.
- No meta-content, no facilitation, no "in this notebook we will".
- Any notebook expecting interactive input ends with a comment block of test inputs and what each should produce.
- Execute cold from a clean state and save with outputs, so they render on GitHub and in a Codespace.
- Checks assert on shape: a count, a length, a type, a key's presence, a reconciliation. A check that compares a printed sentence breaks the first time the wording improves.

## Exercise notebooks

For each unguided exercise that has a notebook to point at, build `notebooks/C2_W{ww}_D{dd}_ex{n}_hands_on_STUDENT.ipynb`: the same helper, a short prelude, then four to six steps, each carrying one or more TODO markers. Each marker is a lettered choice in a comment above a `__TODOn__` placeholder, with a `check()` after the step. The solution twin lives in `exercises/solutions/` with every placeholder filled and executes clean. The answer key records the letters.

## Done

- [ ] The helper is imported, not duplicated, and the import line is documented in the notebook.
- [ ] Data comes from `../data/`, and no records are pasted into a cell.
- [ ] At least three diagram outputs are rendered and saved.
- [ ] At least five `check()` calls exist and all of them pass.
- [ ] Every code cell carries a saved output.
- [ ] At least one trap shows the plausible wrong number, why it is wrong, the check that exposes it and the fix.
- [ ] No saved output or markdown line names a planted record; each discovery sits in an empty your-turn cell.
- [ ] Every logical group closes on a SUM cell with a diagram and a table.
- [ ] The last cell prints `check_summary()` and names what comes next.
- [ ] Any file taking interactive input ends with its test-input comment block.
- [ ] `python3 scripts/nb_check.py <path>` and `python3 scripts/verify.py <day folder> --execute` both pass.

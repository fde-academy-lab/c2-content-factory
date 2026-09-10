---
name: notebook-builder
description: Build or raise a teaching notebook that runs, proves itself and reads as a document. Use whenever the work touches an .ipynb, a demo notebook, a hands-on notebook, an exercise notebook with TODO markers, a notebook that has to run cold in a Codespace, or a request to add checks, diagrams or executed outputs to something that already runs. Trigger it when someone says notebook, demo, hands-on, walkthrough code, "make the cells prove it", or hands over a script that a learner is meant to work through. Covers the shared helper module, the MAP, DO, SEE, CHECK, SUM rhythm, the break-it-on-purpose section, and the pick-from-options exercise twin.
---

# Notebook builder

A notebook is a teaching document that happens to run. It is read far more often than it is executed, so it has to teach on the page: rendered diagrams, printed outputs and passing checks all visible before anybody presses run.

Read `references/helper-module.md` before writing the first cell, because the helper decides what every later cell can call. Read `references/notebook-shape.md` for the full cell-by-cell anatomy and `references/exercise-notebooks.md` when the artifact is a TODO twin rather than a teaching notebook.

## The shared helper

One module serves every notebook in a day. It lives where a notebook running with its own folder as the working directory can reach it, and the deciding test is that `python3 scripts/verify.py <day folder> --execute` passes. Two placements work: `scripts/c2kit.py` reached by a relative `sys.path` insert documented at the top of every notebook, or a copy inside the day's `notebooks/` named to the stem rule.

The helper holds these and nothing else:

- Loaders for the day's data from `../data/`, so the data file is the single source and no notebook pastes records inline.
- `check(label, condition, detail)` printing PASS or FAIL as HTML without raising, so one failure never stops a class, and `check_summary()` printing the totals.
- `table(headers, rows, caption)` for any result worth reading as a grid.
- `show_trace` and a message viewer wherever the day's topic has a trace.
- Diagram builders rendering SVG from a code cell: a ladder of the day's notebooks with the current one lit, a flow of steps with one highlighted, a vertical flow, a stack of layers, a sequence diagram across named lanes, a decision tree, a decision matrix, a decision ladder, and a side-by-side composer.

The helper uses the same palette as the decks. It reaches no network, writes no browser storage and holds no key.

## The shape of a teaching notebook

**Opening.** A title cell naming the topic and the one-line promise. A MAP code cell rendering two diagrams side by side, the day's notebook ladder with this one lit and a flow of what this notebook adds. A setup cell importing the helper and loading the data, with the import line documented in the cell above it.

**Per section, in this order.**

1. A MAP cell: a flow of the section's steps with the current one lit, or a sequence or a stack where the concept has lanes or layers.
2. A prose cell of two to five full sentences saying what is about to happen and why it matters to a record in the running case. A heading alone is not a prose cell.
3. One code cell carrying one idea.
4. The printed output, or a table or trace rendered by the helper.
5. A CHECK cell with two or more `check()` calls asserting on the shape of what happened, never on wording.
6. At each milestone, the industry example and the interview question the milestone just made answerable.

**One break-it-on-purpose section per notebook**, carrying the exact error text or the exact wrong output, then the fix, then the check that proves the fix.

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
- [ ] One break-it-on-purpose section carries exact text, the fix and a proving check.
- [ ] Every logical group closes on a SUM cell with a diagram and a table.
- [ ] The last cell prints `check_summary()` and names what comes next.
- [ ] Any file taking interactive input ends with its test-input comment block.
- [ ] `python3 scripts/nb_check.py <path>` and `python3 scripts/verify.py <day folder> --execute` both pass.

# The notebook shape, cell by cell

The rhythm is MAP, DO, SEE, CHECK, SUM. It repeats per section and the notebook is nothing but that rhythm plus an opening and a close.

## The opening, four cells

**Cell 1, markdown: the title.** The topic named, the notebook's place in the day, then the one-line promise as a full sentence, Kavya's review of what the notebook must prove, and one line on what the previous notebook established. No agenda, no list of what is coming, no "in this notebook we will".

```markdown
# The first count

**Week 1, Monday. Notebook 2 of 4.** By the end of this notebook you can keep a notebook honest,
read one Kalpa order as a dictionary and the file as a list of them, and count with an accumulator.

> **Kavya's review.** A number is only as good as the run that made it.

Notebook 1 drew the tree. This one counts its first leaf, revenue.
```

**Cell 2, markdown: the setup note.** One or two sentences saying that the next cell finds the helper by walking up from this folder and loads the day's data from `../data/`.

**Cell 3, code: setup.** The walk-up import from `helper-module.md` and every loader call, in one cell, so the notebook runs cold.

**Cell 4, code: the MAP.** Two diagrams composed side by side: the day's notebook ladder with this one lit, and a flow of what this notebook adds. It is a code cell so the SVG renders and saves, and it comes after the setup because it calls the helper.

```python
kit.side_by_side(
    kit.ladder(["The question before the budget", "The first count", "The leaves"], lit=1, show=False),
    kit.vflow(["the kernel\nwhat it remembers", "one order\na dictionary of named fields",
               "the accumulator\nstart, update, finish"], show=False),
)
```

## Per section, five moves

### MAP

A code cell rendering the section's own diagram: a flow of the section's steps with the current one lit, or a sequence where the concept has lanes, or a stack where it has layers. One diagram, not three.

### DO, in two cells

A markdown cell of two to five full sentences saying what is about to happen and why it matters to a record in the running case. The running case is what makes the section concrete: "the loop is about to add thirty amounts, and when it stops, `order` still holds the record it stopped on" beats "we will now look at type errors". An ordinary record may be named; a planted one is left for the learner to print, so the sentence points at it without naming it.

Then one code cell carrying one idea. Two ideas is two cells.

### SEE

The printed output, or `kit.table(...)`, or a trace. Whatever the cell produced is visible on the page before anybody runs anything, because the notebook ships executed.

### CHECK

A code cell with two or more `check()` calls.

```python
kit.check("every raw row was read", len(raw) == 50, f"read {len(raw)}")
kit.check("amount is present on 48 and converts on 44",
            profile["amount"]["present"] == 48 and profile["amount"]["converts"] == 44,
            f'present {profile["amount"]["present"]}, converts {profile["amount"]["converts"]}')
```

Each check names what it is proving in the label, so a FAIL line reads as an instruction rather than a puzzle.

### Milestone additions

At each milestone, two markdown beats: one industry example of the technique in production, and one interview question the milestone just made answerable. These are not decoration. The industry example is what a learner repeats in a screen, and the interview question is what the day is being built toward.

## The trap

At least one per notebook. A trap is a plausible wrong number, the kind a hurried analyst ships, and it carries four visible parts:

1. **The plausible wrong answer**, in a code cell that computes it the natural-looking way: rows counted as customers, totals over unequal windows, a join that fanned out, an average of averages.
2. **Why it is wrong**, in business terms first: which decision the wrong number would have driven, and what it hid.
3. **The check that exposes it**, a `kit.check` on the reconciliation, the grain or the denominator, which fails on the wrong number and passes on the right one.
4. **The fix**, recomputed, with what changed stated in rupees, customers or rows.

The reader must be able to see that something was wrong without being told which line to look at, so the wrong number and the right one sit side by side in a table or a chart. A runtime error met on the way is shown in one cell with `kit.expect_error()` and its last line, and the notebook moves on; it never becomes the trap.

## The SUM cell, per logical group

A code cell rendering a diagram from the helper and a table of what the group established. Two or three groups per notebook, not one per section.

```python
kit.table(
    ["What you can now say", "The evidence"],
    [["44 of 50 amounts are usable", "converts 44, present 48"],
     ["discount is absent by design", "present 11, and absence means no discount ran"]],
    caption="What the column pass established",
)
```

## The close

The final cell prints `check_summary()` and one sentence on what the next notebook adds. Nothing else. No recap, no "well done", no list of further reading.

## Sizing

A round notebook climbs four levels of one business question in 24 to 36 cells. Under 24 and the question has not been climbed; over 36 and it is two notebooks, split by level so each sits beside one part of the deck. Markdown outnumbers code where the concept needs it, and a wall of text is as banned as a wall of code.

## The four things that make a notebook fail review

1. **A MAP that is text.** A breadcrumb string in backticks is not a diagram and does not survive a skim.
2. **No saved outputs.** A reader on GitHub sees empty cells and learns nothing, which defeats the notebook's main audience.
3. **Checks that assert on wording.** They break on the first improvement and train everyone to ignore red lines.
4. **Records pasted into a cell.** Two copies of one truth, and the copy in the notebook is the one that goes stale.

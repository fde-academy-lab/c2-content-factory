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

## The break-it-on-purpose section

One per notebook, no more. It carries four parts and all four are visible:

1. The broken artifact, in a code cell.
2. The exact error text, or the exact wrong output. Where the break is a crash, the traceback is caught and printed so the notebook keeps running, and the uncaught form is quoted in a markdown cell underneath so the learner recognises it on their own screen.
3. The fix, in a code cell.
4. A check that proves the fix.

A wrong-output failure is harder than a crash and needs more care: print the wrong number, print the right one, and put a check on the difference. The reader must be able to see that something was wrong without being told which line to look at.

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

Sixteen to twenty-eight cells is the working range for a teaching notebook in the predict rhythm. Under sixteen and the concept has not been walked; over twenty-eight and it is two notebooks, split by chapter so each sits beside one part of the deck. Markdown outnumbers code where the concept needs it, and a wall of text is as banned as a wall of code.

## The four things that make a notebook fail review

1. **A MAP that is text.** A breadcrumb string in backticks is not a diagram and does not survive a skim.
2. **No saved outputs.** A reader on GitHub sees empty cells and learns nothing, which defeats the notebook's main audience.
3. **Checks that assert on wording.** They break on the first improvement and train everyone to ignore red lines.
4. **Records pasted into a cell.** Two copies of one truth, and the copy in the notebook is the one that goes stale.

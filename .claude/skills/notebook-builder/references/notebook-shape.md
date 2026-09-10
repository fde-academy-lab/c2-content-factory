# The notebook shape, cell by cell

The rhythm is MAP, DO, SEE, CHECK, SUM. It repeats per section and the notebook is nothing but that rhythm plus an opening and a close.

## The opening, three cells

**Cell 1, markdown: the title.** The topic named, then the one-line promise as a full sentence. No agenda, no list of what is coming, no "in this notebook we will".

```markdown
# Day 3, Notebook 1: profiling before you touch anything

By the end of this notebook you can look at a file you have never seen and say
which columns are usable, which are lying to you, and which are fine.
```

**Cell 2, code: the MAP.** Two diagrams composed side by side. The day's notebook ladder with this one lit, and a flow of what this notebook adds. This is a code cell so the SVG renders and saves.

```python
c2kit.side_by_side(
    c2kit.ladder(["profiling", "rows and duplicates"], lit=0),
    c2kit.flow(["read the raw file", "count three things per field",
                "read the counts", "decide per field"], lit=None),
)
```

**Cell 3, code: setup.** The documented import and every loader call, in one cell, at the top, so the notebook runs cold. The markdown cell above it explains the relative path in one sentence.

## Per section, five moves

### MAP

A code cell rendering the section's own diagram: a flow of the section's steps with the current one lit, or a sequence where the concept has lanes, or a stack where it has layers. One diagram, not three.

### DO, in two cells

A markdown cell of two to five full sentences saying what is about to happen and why it matters to a record in the running case. Naming the record is what makes the section concrete: "KR4200 carries its amount as text, so the comparison in the next cell has nothing to compare" beats "we will now look at type errors".

Then one code cell carrying one idea. Two ideas is two cells.

### SEE

The printed output, or `c2kit.table(...)`, or a trace. Whatever the cell produced is visible on the page before anybody runs anything, because the notebook ships executed.

### CHECK

A code cell with two or more `check()` calls.

```python
c2kit.check("every raw row was read", len(raw) == 50, f"read {len(raw)}")
c2kit.check("amount is present on 48 and converts on 44",
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
c2kit.table(
    ["What you can now say", "The evidence"],
    [["44 of 50 amounts are usable", "converts 44, present 48"],
     ["discount is absent by design", "present 11, and absence means no discount ran"]],
    caption="What the column pass established",
)
```

## The close

The final cell prints `check_summary()` and one sentence on what the next notebook adds. Nothing else. No recap, no "well done", no list of further reading.

## Sizing

Sixteen to twenty-five cells is the working range for a teaching notebook. Under sixteen and the concept has not been walked; over twenty-five and it is two notebooks. Markdown outnumbers code where the concept needs it, and a wall of text is as banned as a wall of code.

## The four things that make a notebook fail review

1. **A MAP that is text.** A breadcrumb string in backticks is not a diagram and does not survive a skim.
2. **No saved outputs.** A reader on GitHub sees empty cells and learns nothing, which defeats the notebook's main audience.
3. **Checks that assert on wording.** They break on the first improvement and train everyone to ignore red lines.
4. **Records pasted into a cell.** Two copies of one truth, and the copy in the notebook is the one that goes stale.

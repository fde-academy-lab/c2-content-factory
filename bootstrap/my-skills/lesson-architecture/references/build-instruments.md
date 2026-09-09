# Build instruments

Four tools that turn the principles in SKILL.md into checks you can run.

Confidence marking, stated because it belongs in the artifact: none of these
four is an established pedagogical instrument. All four are constructions
derived from the tutorial-site analysis, built to be mechanically checkable.
Treat them as working tools, not as citations.

---

## 1. The witness matrix

A table filled during case design, before any slide or page is written.

Rows are every teaching point the module must land. Columns are every distinct
feature of the case data, meaning a specific row, a specific value, a specific
relationship, not a whole column of a table. Mark the cell where that feature
is what makes that teaching point visible.

|  | Two rows tied on price | Two rows missing colour | Quantity inverted vs price | Three rows sharing a date |
|---|---|---|---|---|
| Sorting by one column | | | | |
| Sorting by several columns | X | | | X |
| Sorting by a computed value | | | X | |
| Naming a computed value | | | X | |
| Placing missing values | | X | | |

Three readings come straight off it, and the third is the one that pays.

**An empty row** means the teaching point has no witness. The slide that
teaches it will produce output indistinguishable from the slide before it.
Extend the data or cut the point.

**An empty column** means a data feature no lesson uses. Delete it. Unused
detail in a case is pure cognitive load with no return, and it is where
learners get lost while looking for the relevance.

**A heavily marked column** is load-bearing. Several lessons collapse if
someone edits that value later. Mark it in the build file so a casual change
to the case does not silently break four slides. This is the reading that
catches the expensive mistake, because case data usually gets edited long after
the person who designed it has forgotten why a number was chosen.

---

## 2. The delta line

One line written in the build file, never on the slide, for every slide that
shows a result:

```
differs from previous because <the one thing that changed>
```

If the line cannot be written, the slide shows nothing new and comes out. If
the line needs the word "and", the slide is carrying two ideas and becomes two
slides. The delta line enforces the one-rung-per-slide rule in both directions
at once, catching duplicates and catching compression with the same check.

Run it as a pass over the finished build file, reading only the delta lines in
sequence. That sequence is the actual lesson. If it reads as a coherent
progression, the deck works. If it reads as a list of unrelated changes, the
ladder is out of order.

---

## 3. The decision sentence

The sizing test for units in judgement subjects, where byte-sizing by term
produces trivia.

Complete this sentence for every unit:

```
After this unit, a learner can decide <what>, which they could not decide before.
```

Three failure signals:

- The sentence needs an "and". The unit is two units
- The sentence can only be completed with "they know what X means". That is a
  definition, not a unit, and it belongs inside a unit that uses it
- The same sentence completes for two consecutive units. They are one unit

A module's decision sentences, read in order, are the honest syllabus. Where
they overlap or repeat, the sequence is padded. Where they jump, a unit is
missing.

---

## 4. The carry-forward chain

Byte-sizing buys clarity inside a unit and pays for it at the seams. Small
units mean more seams, and more seams mean more places to lose the thread.
This is the extension of the existing session-level rule down to unit level.

Every unit names one artifact it produces and one it consumes.

| Unit | Consumes | Produces |
|---|---|---|
| 3.1 | The case brief | A scored list of tasks |
| 3.2 | The scored list | The accuracy bar for each task |
| 3.3 | The accuracy bar | The autonomy level for each task |

Two checks:

- A unit whose output nothing consumes is either the module's final output or
  it is orphaned. Orphaned units are where learners disengage, because nothing
  later depends on having understood them
- A unit consuming something never produced is a missing prerequisite, and it
  is the most common cause of a room going quiet

Put the produces column into the map itself, as a fourth element beside the
section name, the promise and the unit list. A learner who can see what each
section hands the next reads the course as one thing rather than as a list.

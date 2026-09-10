# Day 3 take-home: make the profiler reusable

Due at the start of tomorrow's session, where the solution is released and discussed.

Today you profiled one file by hand. Tonight you turn that into something you can point at a file you have never opened, and then you point it at one.

---

## What you are given

`../data/C2_W01_D03_takehome_STUDENT.csv`. Same seven fields as today. A different extract, with defects today's file did not have.

## What you hand in

Four things, in one notebook named `takehome_d3.ipynb` in your own repository.

### 1. `profile_dataset()`

One function. It takes a list of rows and returns the three counts for every field, without being told which fields exist.

```
def profile_dataset(rows):
    ...
```

It must work on a file whose columns you have not seen, which means no field names written into the body. If your function mentions `amount` anywhere inside it, it is not reusable and tomorrow's file will prove it.

Run it on today's file first and check it reproduces the profile you built in class. A function that gives a new answer on old data is broken.

### 2. The profile and the clean, on the new file

Point `profile_dataset()` at the new extract, read the profile before touching anything, then run the clean using `clean_record` and `clean_records` from Tuesday, unedited.

Ship `output/profiled_orders.csv` and `output/rejects.csv`, and print the reconciliation.

### 3. The decisions log

One line per decision, in the four columns from class: field, finding, choice, reason.

This file needs at least four lines. Three of them are about values. One is about a row, and finding it is the point of the exercise.

Write the log as you go rather than at the end. A log reconstructed afterwards is a story, and it reads like one.

### 4. Two lines defending your identity rule

The new file, like today's, contains one order id on two rows. The rows differ on a different field this time.

Write exactly two lines:

- The rule, stated so somebody else could apply it without asking you.
- What your rule costs, meaning what it would wrongly merge or wrongly separate on a different file.

Two lines. Not two paragraphs. If you cannot say it in two lines you have not decided yet.

---

## The reading, and the one thing you must bring back from it

The Python standard library will happily guess whether the first row of a file is a header. Today
you met a file where that guess would have been wrong, so go and read how the guess is made.

The CSV module, Python 3.12.0 (verified 09 Sep 2026): https://raw.githubusercontent.com/python/cpython/v3.12.0/Lib/csv.py

Find `Sniffer.has_header`, which begins at line 390. Read its opening comment, then read the vote at
lines 434 to 451.

Answer in four lines:

- In one sentence, how does `has_header` decide? Quote the line number where the decision is finally
  returned.
- The comment at the top of the method describes two different tests. Name both.
- Today's companion file had its header row repeated as the first data row. Would `has_header` have
  noticed? Say why, using the vote rather than your intuition.
- You wrote an identity rule today because the data could not tell you what counted as the same
  order. `has_header` is the standard library choosing to guess instead. In one line, say when
  guessing is the right call and when stating a rule is.

Quote a line number for the first answer. An answer without one does not count, because the point is
that you opened the file.

That last question is the one tomorrow opens on, so it is worth more than the other three together.

## How this is checked

Tomorrow's discussion looks at these, in this order:

1. Does `profile_dataset()` run on a file whose columns it was never told about.
2. Does the decisions log include the row-level finding, not only the value-level ones.
3. Is the identity rule stated well enough for somebody else to apply.
4. Does the reconciliation print, and does it hold.
5. Does the clean go through Tuesday's functions rather than a fresh loop.
6. Does your reading answer carry a line number from the actual source file.

The totals matter least. Two learners can hand in different totals and both be right, if both wrote down the rule that produced them.

---

## Before you hand it in

Open `C2_W01_D03_selfcheck_STUDENT.md`, after you have finished rather than before. It carries checkpoints you can verify alone, so you know where you stand before anybody else looks.

## The two tools that ship with tonight's work

Both sit in `demos/` beside the companion page.

`C2_W01_D03_decision_tool_STUDENT.xlsx` has one tab per decision you took today: what an incomplete field earns, which identity rule you state, and what happens to the order at the end of the column. Yellow cells are yours and everything else computes. Each tab ships with one planted defect, so all three verdicts read "stop" when you open it, and clearing one tab does not clear the export tab's release.

`C2_W01_D03_profile_pass_STUDENT.xlsx` is the eight-move run sheet for a profile-then-clean pass, with a symptom lookup beside it. Run it on tonight's second file before you write a single line of the log by hand.

The export tab assembles the decisions log by formula. Bring that paragraph tomorrow; Thursday's numbers are computed on exactly the dataset it describes.

## Where the running half lives

`notebooks/C2_W01_D03_ex1_hands_on_STUDENT.ipynb` walks the whole pass with pick-from-options markers and a check after every step. Post its five letters with your exercise letters.

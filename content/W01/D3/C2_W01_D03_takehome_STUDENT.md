# Day 3 take-home: make the profiler reusable

Due at the start of tomorrow's session, where the solution is released and discussed.

Today you profiled one file by hand. Tonight you turn that into something you can point at a file you have never opened, and then you point it at one.

---

## What you are given

`C2_W01_D03_data_takehome_STUDENT.csv`. Same seven fields as today. A different extract, with defects today's file did not have.

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

## The reading

Watch the Khan Academy material on mean, median and mode before tomorrow.

Link status: to be found. The reference is on today's curriculum row and the verified link goes on this line before this pack is released.

Tomorrow opens on the largest order in today's file and what it does to an average, so arrive knowing which of those three you would quote to a manager.

---

## How this is checked

Tomorrow's discussion looks at these, in this order:

1. Does `profile_dataset()` run on a file whose columns it was never told about.
2. Does the decisions log include the row-level finding, not only the value-level ones.
3. Is the identity rule stated well enough for somebody else to apply.
4. Does the reconciliation print, and does it hold.
5. Does the clean go through Tuesday's functions rather than a fresh loop.

The totals matter least. Two learners can hand in different totals and both be right, if both wrote down the rule that produced them.

---

## Before you hand it in

Open `C2_W01_D03_takehome_selfcheck_STUDENT.md`, after you have finished rather than before. It carries checkpoints you can verify alone, so you know where you stand before anybody else looks.

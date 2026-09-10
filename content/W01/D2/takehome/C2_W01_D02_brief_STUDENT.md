# Day 2 take-home: a file nobody prepared for you

Due at the start of tomorrow's session, where the solution is released and discussed.

You are not being asked to write new machinery. You are being asked to point this morning's machinery at a file it has never seen and to defend what came out.

---

## What you are given

`../data/C2_W01_D02_takehome_STUDENT.csv`. Same five fields as today. Defects you have not met.

## What you hand in

Four things, in one notebook named `takehome_d2.ipynb` in your own repository.

### 1. The run

Read the file, clean it with the functions you carved this morning, and write two files: your clean records and your rejections. Every rejection carries the interpreter's own reason.

You must call `normalise_amount` and `clean_records` from your own notebook. Copy them across if you like. If you find yourself writing a fresh loop from scratch, you have missed the point of yesterday and today.

### 2. The reconciliation cell

One cell that reads both output files back from disk and prints a single line showing input, clean, rejected, and whether they add up. Print it even when it adds up, especially when it adds up.

### 3. The threshold, defended

One record in this file converts perfectly well and is still wrong. Find it.

Write a markdown cell of at most six lines that states:

- Which record, and what is wrong with it.
- The rule you are adopting, stated so someone else could apply it without asking you. "Looks odd" fails that test. A rule reads more like "any amount outside the range X to Y is set aside with reason `out of range`", where you chose X and Y and can say why.
- What your rule costs. Every rule throws away something, and you should know what.
- One case where your own rule would give the wrong answer.

That last line is the one that separates a defended choice from a preference.

### 4. The challenges log

A markdown cell listing every place you got stuck, in the order it happened. For each entry: what you expected, what happened, and what you changed. Three to six entries is normal. An empty log means you did not read your own errors.

Copy the exact error text into the log. Paraphrasing an error is how you lose the ability to search for it.

---

## The recap cell

One more markdown cell, in your own words, on this question:

Today you saw the same total printed twice, once as a crash you had to handle and once as a number that arrived quietly. Which of those two costs more, and to whom?

Write it as though explaining to a colleague who was not in the room. Under 120 words. Do not use the phrase "best practice".

---

## The reading, and the one thing you must bring back from it

Two files from the Python standard library's own source. Not a tutorial about them. The source.

Both links are pinned to a released version, so the line numbers below will still be there when you
open them.

The CSV reader, Python 3.12.0 (verified 09 Sep 2026): https://raw.githubusercontent.com/python/cpython/v3.12.0/Lib/csv.py

The JSON decoder, Python 3.12.0 (verified 09 Sep 2026): https://raw.githubusercontent.com/python/cpython/v3.12.0/Lib/json/decoder.py

### Question 1, from `csv.py`

Read lines 118 to 132, inside `DictReader.__next__`.

Today every row in your file had exactly the right number of fields. Those lines are what happens
when one does not.

Answer in three lines:

- What does `DictReader` do with a row that has **more** fields than the header?
- What does it do with a row that has **fewer**?
- Neither case raises. Say what that means for a rejects log built the way you built yours today.

Quote the line number you took each answer from. An answer without a line number does not count,
because the point of this is that you opened the file.

### Question 2, from `json/decoder.py`

Find the line that builds the error message you saw today. You are looking for the one that
produces `line 48 column 1 (char 1027)`.

Answer in two lines:

- The line number, and the format string on it.
- `colno` is computed on the line above it. Read that computation and say, in your own words, why a
  file with no newline characters at all would report every error as being on line 1.

If you find yourself writing a general description of JSON parsing, you have not opened the file.

## How this is checked

The solution is released tomorrow and one of these notebooks is discussed. What gets looked at, in this order:

1. Does the reconciliation line print, and does it add up.
2. Is the threshold rule stated well enough that someone else could apply it.
3. Does the challenges log contain real error text.
4. Do the rejections carry the interpreter's reasons rather than invented ones.
5. Does the run go through your own `clean_record`, rather than a fresh loop written tonight.
6. Do your two reading answers carry line numbers from the actual source files.

The totals matter least. Two learners can hand in different totals and both be right, if both stated their rule.

---

## Before you hand it in

Open `C2_W01_D02_selfcheck_STUDENT.md`. It contains checkpoints you can verify alone, so you know where you stand before anybody else looks.

Open it after you have finished, not before. Reading it first turns this into a copying exercise and you will feel the difference tomorrow.

## The two tools that ship with tonight's work

Both sit in `demos/` beside the companion page.

`C2_W01_D02_decision_tool_STUDENT.xlsx` has one tab per decision you took today: which stance you take on a value that will not convert, who decides what a failure means, and which format you write the file under. Yellow cells are yours and everything else computes. Each tab ships with one planted defect, so all three verdicts read "stop" when you open it, and clearing one tab does not clear the export tab's release.

`C2_W01_D02_clean_pass_STUDENT.xlsx` is the eight-move run sheet for a read, clean and write pass, with a symptom lookup beside it. Use it on tonight's third file.

Bring the export tab's paragraph tomorrow. Wednesday opens on somebody reading one aloud.

## Where the running half lives

`notebooks/C2_W01_D02_ex1_hands_on_STUDENT.ipynb` and `C2_W01_D02_ex2_hands_on_STUDENT.ipynb` carry the pick-from-options markers and the checks. Post the letters from both with your exercise letters.

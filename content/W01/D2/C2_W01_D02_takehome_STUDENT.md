# Day 2 take-home: a file nobody prepared for you

Due at the start of tomorrow's session. Tomorrow opens by walking one of these.

You are not being asked to write new machinery. You are being asked to point this morning's machinery at a file it has never seen and to defend what came out.

---

## What you are given

`C2_W01_D02_data_takehome_STUDENT.csv`. Same five fields as today. Defects you have not met.

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
- The rule you are adopting, stated so someone else could apply it without asking you. "Looks odd" is not a rule. "Amounts below zero are rejected with reason `negative amount`" is a rule.
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

## The reading

Skim the chapter on reading and writing files, from the book on the trainer resource list.

Link status: to be found. The reference is `Automate the Boring Stuff with Python`, 3rd edition, chapter 10. The verified link goes on this line before this pack is released.

When you have read it, add one line to your notebook naming one thing the chapter does differently from what we did today, and say whether you would change your code because of it.

---

## How this is checked

Tomorrow's session opens on one of these notebooks. What gets looked at, in this order:

1. Does the reconciliation line print, and does it add up.
2. Is the threshold rule stated well enough that someone else could apply it.
3. Does the challenges log contain real error text.
4. Do the rejections carry the interpreter's reasons rather than invented ones.

The totals matter least. Two learners can hand in different totals and both be right, if both stated their rule.

---

## Before you hand it in

Open `C2_W01_D02_takehome_selfcheck_STUDENT.md`. It contains checkpoints you can verify alone, so you know where you stand before anybody else looks.

Open it after you have finished, not before. Reading it first turns this into a copying exercise and you will feel the difference tomorrow.

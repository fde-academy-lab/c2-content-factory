# Take-home: Week 1, Day 4

Opens the next session. Bring the deliverable and the challenges log, both.

Tomorrow is Gandhi Jayanti and the institute is closed, so this one has room to breathe. Do not use that room to make it longer. Use it to make the defence better.

---

## What you are being asked

You built a segment summary in session. Somebody now wants the same view cut two other ways, on the same 44 orders.

Three things make this harder than repeating today's work, and all three are the point:

1. Neither new grouping field exists as a column. You have to build both.
2. One of the two cuts produces a group so small that the only correct answer is to refuse it, and you have to notice rather than be told.
3. You are asked to state a trust threshold and defend it, and the 30 you were handed in session is a number you should argue with.

---

## The deliverable

One notebook, `C2_W01_D04_takehome_<yourname>.ipynb`, holding six things in this order.

### 1. Your own function, unchanged

Open your notebook from today and copy `summarise_by` across exactly as you wrote it. Do not rewrite it and do not improve it.

If it takes the grouping field as a parameter, most of this task is four lines. If it has `"segment"` written inside it, you have found out something useful about your own code, and fixing that is part of the deliverable. Say in a markdown cell which of the two you were, in one sentence.

### 2. Cut one: discounted against not discounted

The `discount` field is empty on most orders and carries a value on the rest. Group the 44 orders into two buckets on that basis and report count, median amount and return rate for each.

Then answer in a markdown cell: **do discounted orders come back more often, or less?** Give the two rates with their denominators, and say whether you would put that finding in front of the order book owner as it stands.

### 3. Cut two: by month

Group the same orders by month. The `order_date` field looks like `2026-08-19`, and the month is its first seven characters. That is the whole trick and it is deliberately small.

This cut will surprise you. When it does, do not fix it. Read it, work out where the surprising group came from, and write two lines on what it means. The answer is in yesterday's decisions log, not in your code.

### 4. Your threshold, defended

In session the notebook used a floor of 30 orders. Thirty is a convention people repeat, and this file holds 44 orders in total.

Write a markdown cell answering all three:

- What floor did you actually apply, as a number?
- What happens to both of your tables if you apply 30? Show them.
- Is a fixed order count the right shape of rule here at all, or should the rule depend on how big a difference you are being asked to defend? Take a position.

There is no answer key for this cell. There is a difference between an answer that names a number and defends it, and an answer that repeats "it depends".

### 5. The flag, in the output

Every row that falls below your floor must be visibly marked in the printed output. Not in a comment, not in a separate list, in the line itself, so that a person who screenshots one row still sees the warning.

### 6. The challenges log

At least two entries. Each entry is three lines:

```
What I tried:
What the output actually said:      <- paste it, exactly
What I changed and why:
```

Entries where the output line is paraphrased rather than pasted do not count. If nothing gave you trouble, one entry should be about a result that surprised you and what you did to convince yourself it was right.

---

## Also due, and small

**One markdown cell**, in your own words, on this question:

> When is the mean the honest choice?

Three or four sentences. It is a real question with a real answer, and "never" is wrong.

---

## Exploration, before Monday

Today you called `statistics.median()` and trusted it. Go and read what it actually does.

CPython's own source for the `statistics` module, tag v3.12.0 (verified 09 Sep 2026): https://raw.githubusercontent.com/python/cpython/v3.12.0/Lib/statistics.py

Find the `def median(data):` function. It is short and you can read the whole thing.

Answer in a markdown cell, citing the line you are talking about:

- What is the **first** thing `median` does to the data you hand it, and why must it do that before anything else?
- When the number of values is **even**, `median` returns a value that may not appear anywhere in your data. Quote the line that does this. Is that a bug, and would you use this function on Kalpa's amount column?

The second question has a real answer and it is not "yes it is a bug". Your file has 44 orders, which is even, so this is not hypothetical.

---

## What this is marked against

Nothing. This is ungraded, like everything this week.

It opens the next session, and the session begins by walking one submission on the projector. Somebody's threshold defence gets read out. Write it as though it is yours.

---

## Self-check

Ship with `C2_W01_D04_takehome_selfcheck_STUDENT.md`. Run it before you submit. It plants specific values you can confirm alone, so you know whether you are right before class tells you.

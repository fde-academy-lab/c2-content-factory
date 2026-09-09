# Take-home: Week 1, Day 4

Opens the next session. Bring the deliverable and the challenges log, both.

Tomorrow is Gandhi Jayanti and the institute is closed, so this one has room to breathe. Do not use that room to make it longer. Use it to make the defence better.

---

## What you are being asked

You built a segment summary in session. Somebody now wants the same view cut a different way, over time rather than over segment, on a file you have not seen.

Two things make this harder than repeating today's work, and both are the point:

1. The second file is grouped by month, and there is no month column in it.
2. You are asked to state a trust threshold and defend it, and the number you were handed in session is one you should argue with.

---

## The deliverable

One notebook, `C2_W01_D04_takehome_<yourname>.ipynb`, holding five things in this order.

### 1. Your own function, unchanged

Open your notebook from today and copy `summarise_by` across exactly as you wrote it. Do not rewrite it and do not improve it.

If it takes the grouping field as a parameter, this task is four lines. If it has `"segment"` written inside it, you have found out something useful about your own code, and fixing that is part of the deliverable. Say in a markdown cell which of the two you were, in one sentence.

### 2. The month view

Group `C2_W01_D04_data_takehome_STUDENT.csv` by month and report count, median amount, accepted count and accepted rate per month.

The date field looks like `2026-05-04`. The month is the first seven characters of it. That is the whole trick and it is deliberately small, since the work today is not string slicing.

### 3. Your threshold, defended

In session the notebook used a floor of 30 records. Thirty is a convention people repeat, and this file holds 39 records in total.

Write a markdown cell answering all three:

- What floor did you actually apply, as a number?
- What happens to your month table if you apply 30? Show the table.
- Is a fixed record count the right shape of rule here at all, or should the rule depend on how big a difference you are being asked to defend? Take a position.

There is no answer key for this cell. There is a difference between an answer that names a number and defends it, and an answer that repeats "it depends".

### 4. The flag, in the output

Every month row that falls below your floor must be visibly marked in the printed output. Not in a comment, not in a separate list, in the line itself, so that a person who screenshots one row still sees the warning.

### 5. The challenges log

At least two entries. Each entry is three lines:

```
What I tried:
What the output actually said:      <- paste it, exactly
What I changed and why:
```

Entries where the output line is paraphrased rather than pasted do not count. If nothing gave you trouble, one of your entries should be about a result that surprised you and what you did to convince yourself it was right.

---

## Also due, and small

**Rebuild the same view grouped by `segment` using the same function call**, changing one argument. Print both tables in the same cell. The month table and the segment table are built from the same 39 records, so their counts must sum to the same total. If they do not, you have a bug and you have just found it without being told.

**One markdown cell**, in your own words, on this question:

> When is the mean the honest choice?

Three or four sentences. It is a real question with a real answer, and "never" is wrong.

---

## Exploration, before Monday

Monday opens on the question this session refused to answer, which is whether a gap between two segments is real or is what groups of that size do on their own.

There is an interactive chapter on frequentist inference that makes the idea visual before any formula arrives. **The link is to be found** and will be posted with its verification date in the student references; the Week 1 curriculum row carries the source. Work through the first section and bring one screenshot of a state that surprised you.

If the link has not been posted by the time you sit down, skip this section and say so in your challenges log. Do not search for a substitute and cite it; an unverified link is worth less than an honest blank.

---

## What this is marked against

Nothing. This is ungraded, like everything this week.

It opens the next session, and the session begins by walking one submission on the projector. Somebody's threshold defence gets read out. Write it as though it is yours.

---

## Self-check

Ship with `C2_W01_D04_takehome_selfcheck_STUDENT.md`. Run it before you submit. It plants specific values you can confirm alone, so you know whether you are right before class tells you.

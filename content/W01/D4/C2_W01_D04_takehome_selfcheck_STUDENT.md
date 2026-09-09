# Self-check: Week 1, Day 4 take-home

Run this before you submit. Every checkpoint is a value you can confirm alone.

Work down the list in order. The first checkpoint that fails tells you where to look, and checking a later one before an earlier one has passed wastes your evening.

---

## Checkpoint 0: you opened the right file

```
records in C2_W01_D04_data_takehome_STUDENT.csv: 39
```

Thirty-nine, not forty-seven. Forty-seven is today's class file and it is a different dataset. If you see 47, you are describing the wrong records and every number below will disagree with you.

---

## Checkpoint 1: the month buckets exist and add up

```
number of distinct months: 4
sum of the four month counts: 39
```

The sum has to equal checkpoint 0. If it does not, your grouping is dropping records, and the usual cause is a key built from the wrong slice of the date string.

---

## Checkpoint 2: the thin month

```
the smallest month bucket holds 4 records
```

Exactly one month is far smaller than the others. It should be obvious in your table without hunting.

That month also carries the **highest accepted rate in the whole table**. If your highest rate sits on your largest bucket, recheck your rate arithmetic, because you have almost certainly divided by the wrong denominator.

---

## Checkpoint 3: the overall median

```
median amount across all 39 records: Rs 9,400
```

An exact match. If you get a number near this but not equal to it, you are probably averaging the two middle values on an odd-length list. Thirty-nine is odd, so the median is a single record's amount and no arithmetic is involved.

---

## Checkpoint 4: one month is lying the way today's file lied

One of the four months has a **mean more than three times its median**.

```
that month's median: Rs 9,600
that month's mean:   Rs 35,463.64
```

Find it. It contains a single very large amount, exactly as `segment_b` did in session. If your month table reports means at all, this is the row that proves why it should not.

You do not have to fix anything here. You have to notice it, and say one line about it in your challenges log.

---

## Checkpoint 5: the same function, two ways

Call your function twice, once grouping by month and once by segment.

```
month buckets: 4    counts sum to 39
segment buckets: 4  counts sum to 39
```

Both totals must equal 39. The bucket counts differ between the two views and the totals cannot.

If you had to edit your function between the two calls, the function was not parameterised, and step 1 of the take-home asked you to say so honestly. Saying so is worth more than quietly fixing it.

---

## Checkpoint 6: the flag is in the line

Take any row below your floor. Read only that one line, as though it had been cropped out of your notebook and pasted into somebody else's slide.

Can a stranger tell, from that line alone, that the number is not to be trusted?

If the warning lives on a different line, in a legend, or in a comment, it does not survive the crop. Move it into the line.

---

## Checkpoint 7: your threshold cell says a number

Read your own markdown cell from step 3 and find the digits.

If the cell explains the trade-off without ever landing on a number you applied, it is not finished. A defended threshold has a value in it. "It depends on the size of the difference being claimed" is a good second sentence and a poor only sentence.

---

## If everything above passes

You are done. Two last things worth thirty seconds:

- Restart your kernel and run the notebook top to bottom. A take-home that only works in the order you happened to click is Monday's problem, and Monday you will not remember the order.
- Reread your two challenges-log entries. If the "what the output actually said" lines are paraphrases rather than pasted text, go back and paste the real ones.

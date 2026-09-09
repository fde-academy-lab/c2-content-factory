# Self-check: Week 1, Day 4 take-home

Run this before you submit. Every checkpoint is a value you can confirm alone.

Work down the list in order. The first checkpoint that fails tells you where to look, and checking a later one before an earlier one has passed wastes your evening.

---

## Checkpoint 0: you opened the right file

```
orders in C2_W01_D04_data_profiled_STUDENT.csv: 44
total amount: Rs 561,145
```

Forty-four, not fifty. Fifty is yesterday's raw file and six of those orders never converted. If you see 50, you are describing orders your own cleaning pass rejected.

---

## Checkpoint 1: cut one splits cleanly

```
discount present:  10 orders
discount absent:   34 orders
sum:               44
```

The sum has to equal checkpoint 0. If it does not, your test for "empty" is missing a case. An empty CSV field arrives as an empty string, not as `None`.

---

## Checkpoint 2: cut one has a finding in it

```
discount present:  2 returned of 10   ->  20.0%
discount absent:  10 returned of 34   ->  29.4%
```

Discounted orders came back **less** often, which is the opposite of what most people guess before running it.

Both rates rest on fewer than 35 orders, so the honest write-up says the direction is interesting and the evidence is thin. If your markdown cell states this as a finding without that caveat, reread step 2 of the brief.

---

## Checkpoint 3: cut two is lopsided, and that is correct

```
number of distinct months: 2
2026-08:  43 orders
2026-09:   1 order
```

If you got four or five months, you sliced the wrong characters out of the date.

**One month holds a single order.** Its return rate is 100.0 percent. That number is real, arithmetically correct, and completely worthless, which is the whole reason this cut is in the brief.

---

## Checkpoint 4: where the September order came from

Find the one September order and look at its `order_id`.

```
order_id: KR4201
```

It is the second half of the near-duplicate pair you decided to keep and flag yesterday. The two rows share an order id and differ on `order_date` by six weeks.

So a decision you made on Wednesday created a one-order group on Thursday with a 100 percent return rate in it. Nothing went wrong. A judgement call travelled downstream and showed up in a summary, which is what judgement calls do.

Two lines on that in your notebook is what step 3 is asking for.

---

## Checkpoint 5: the same function, three ways

Call your function three times, grouping by segment, by discount presence and by month.

```
segment buckets:  4   counts sum to 44
discount buckets: 2   counts sum to 44
month buckets:    2   counts sum to 44
```

All three totals must equal 44. The bucket counts differ between views and the totals cannot.

If you had to edit your function between calls, it was not parameterised, and step 1 asked you to say so honestly. Saying so is worth more than quietly fixing it.

---

## Checkpoint 6: the flag is in the line

Take any row below your floor. Read only that one line, as though it had been cropped out of your notebook and pasted into somebody else's slide.

Can a stranger tell, from that line alone, that the number is not to be trusted?

If the warning lives on a different line, in a legend, or in a comment, it does not survive the crop. Move it into the line.

---

## Checkpoint 7: your threshold cell says a number

Read your own markdown cell from step 4 and find the digits.

If the cell explains the trade-off without ever landing on a number you applied, it is not finished. A defended threshold has a value in it. "It depends on the size of the difference being claimed" is a good second sentence and a poor only sentence.

---

## Checkpoint 8: you actually opened the source

Your exploration cell should quote a line from the file, not describe it.

The first thing `median` does is sort. Your file has 44 orders, which is even, so the function averages the two middle values and can return an amount that no Kalpa order ever carried. Today's median of Rs 1,910.00 is exactly that: an average of two orders, not an order.

If you wrote that the median is always a real data point, go back and read the function.

---

## If everything above passes

You are done. Two last things worth thirty seconds:

- Restart your kernel and run the notebook top to bottom. A take-home that only works in the order you happened to click is Monday's problem, and Monday you will not remember the order.
- Reread your two challenges-log entries. If the "what the output actually said" lines are paraphrases rather than pasted text, go back and paste the real ones.

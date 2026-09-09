# Exercises: Week 1, Day 4

Describe without misleading. Every exercise runs on `C2_W01_D04_data_profiled_STUDENT.csv`, the 44 Kalpa orders you profiled yesterday.

Answers here are selections, predictions, short computations and repairs. Almost nothing needs typing. The thinking is the work.

Solutions to the unguided set are released at close of session. Do not open them before you have written something down, since an answer you read is an answer you forget.

---

## G1. Guided, with the trainer: seven orders by hand

**Drops in:** half one, section 1, after the three definitions.

The first seven orders in your profiled file:

```
1280   1865   2270   2835   1310   1145   1030
```

1. Compute the mean with a pen. Show the sum and the division.
2. Compute the median with a pen. Say which position you counted to and why that is the middle.
3. Now replace Rs 2,835 with Rs 480,000, the real whale from your own file. Predict both statistics **before** recomputing, and write your prediction down.
4. Recompute. Which prediction was wrong, and by how much?
5. Reproduce all of it in the notebook and confirm the machine agrees with your paper.

Step 3 is the exercise. Steps 1 and 2 are warm-up and step 5 is a receipt.

---

## G2. Guided, with the trainer: the first segment

**Drops in:** half two, section 2, immediately after the `KeyError` is fixed.

With the trainer, build the summary for `Business` only, out loud, before any loop is written:

1. How many orders does it hold?
2. What is the median amount, and why is that the statistic being asked for rather than the mean?
3. How many were returned, and what rate is that?
4. Write the one sentence you would send about Business. It must contain a number, a denominator and a limit.

Then let the trainer generalise your four answers into the loop that does all four segments.

---

## M1. Mid-session, about fifteen minutes: four files, described only by two numbers

**Drops in:** half one, after the whale section.

Four datasets. You cannot see the orders. You get the mean and the median and nothing else.

| Dataset | Mean | Median |
|---|---|---|
| P | Rs 42,000 | Rs 39,500 |
| Q | Rs 88,000 | Rs 12,000 |
| R | Rs 6,400 | Rs 6,350 |
| S | Rs 3,100 | Rs 9,800 |

Answer by selection, one line of reasoning each:

1. Which dataset almost certainly hides one or more very large values?
2. Which dataset hides one or more very **small** values, and how do you know from two numbers?
3. In which two datasets would you be comfortable quoting the mean, and why?
4. Dataset S has a mean below its median. Name one realistic thing in Kalpa's order book that produces that shape.

Then: where does your own file sit on this table, and which of the four does it most resemble?

---

## M2. Mid-session, about fifteen minutes: pick the honest statistic

**Drops in:** half two, after the honest-sentence section.

Four requests land in your inbox on the same morning. For each, choose **mean**, **median**, **mode** or **refuse and say why**, and give a one-line defence.

1. "What is our typical order value?" The amount column has order `KR4232` at Rs 480,000 in it.
2. "Which segment do most of our orders come from?" Four segments, 44 orders.
3. "What is the average time our support team takes to reply?" You are told most replies are quick and a handful sat over a weekend.
4. "What is the return rate for Business?" Business holds nine orders.

One of these four is not a statistics question at all. Say which and say what it is instead.

---

## U1. Unguided, no hints: the full segment summary

**Drops in:** half two, after the guided first segment. Solution at close of session.

Working alone, on the profiled file:

1. Produce a table with one row per segment holding: count, median amount, number returned, return rate.
2. Sort it by return rate, best first. Remember that lower is better here.
3. Add the count to the same line as every rate.
4. Write one sentence per segment. Each carries a number, its denominator, and what it does not support.
5. At least two of your four sentences should decline to make a claim. If none does, reread step 4.

**Predict before you run.** Write down which segment you expect at the top of the ranking, and why. Then run it.

---

## U2. Unguided, no hints: repair a broken summary

**Drops in:** half two, alongside U1 for anyone who finishes early.

A colleague sends you this and asks whether it is ready for a stakeholder. It runs without error on a file you do not have.

```python
counts = {"Retail-Core": 0, "Retail-Plus": 0, "Business": 0, "Student": 0}
totals = {"Retail-Core": 0, "Retail-Plus": 0, "Business": 0, "Student": 0}

for r in orders:
    counts[r["segment"]] += 1
    totals[r["segment"]] += r["amount"]

print("average order by segment:")
for seg in counts:
    print(seg, "Rs", round(totals[seg] / counts[seg], 2))
```

1. It runs clean on today's file. Name the input that makes it crash, and give the exact exception name.
2. It reports a number for one segment that no stakeholder should see. Which segment, what is the number, and what is wrong with it?
3. Make the smallest change that fixes the statistic. You may not delete any order.
4. There is a third problem that is not about crashing and not about the mean. Name it. (Look at what the printed lines do not carry.)
5. Rewrite the `print` line so the output would survive being screenshotted and pasted into somebody else's slide.

---

## What to have on screen at close of session

- Your segment summary table with counts beside every rate.
- Four sentences, at least two of which decline to make a claim.
- The open question about Business against Retail-Plus, written into your own notebook in your own words.

Bring all three on Monday. The Week 2 session opens on the third one.

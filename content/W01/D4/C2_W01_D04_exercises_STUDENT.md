# Exercises: Week 1, Day 4

Describe without misleading. Every exercise runs on `C2_W01_D04_data_cleaned_STUDENT.csv`, the 47 records you cleaned yesterday.

Answers here are selections, predictions, short computations and repairs. Almost nothing needs typing. The thinking is the work.

Solutions to the unguided set are released at close of session. Do not open them before you have written something down, since an answer you read is an answer you forget.

---

## G1. Guided, with the trainer: seven values by hand

**Drops in:** half one, section 1, after the three definitions.

The first seven records of your cleaned file:

```
2000   3000   4000   4500   5000   6500   10000
```

1. Compute the mean with a pen. Show the sum and the division.
2. Compute the median with a pen. Say which position you counted to and why that is the middle.
3. Now change the last value from 10,000 to 80,000, changing nothing else. Predict both statistics **before** recomputing, and write your prediction down.
4. Recompute. Which prediction was wrong, and by how much?
5. Reproduce all of it in the notebook and confirm the machine agrees with your paper.

Step 3 is the exercise. Steps 1 and 2 are warm-up and step 5 is a receipt.

---

## G2. Guided, with the trainer: the first segment

**Drops in:** half two, section 2, immediately after the `KeyError` is fixed.

With the trainer, build the summary for `segment_a` only, out loud, before any loop is written:

1. How many records does it hold?
2. What is the median amount, and why is that the statistic being asked for rather than the mean?
3. How many were accepted, and what rate is that?
4. Write the one sentence you would send about `segment_a`. It must contain a number, a denominator and a limit.

Then let the trainer generalise your four answers into the loop that does all four segments.

---

## M1. Mid-session, about fifteen minutes: four files, described only by two numbers

**Drops in:** half one, after the whale section.

Four datasets. You cannot see the records. You get the mean and the median and nothing else.

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
4. Dataset S has a mean below its median. Name one realistic thing in a business file that produces that shape.

---

## M2. Mid-session, about fifteen minutes: pick the honest statistic

**Drops in:** half two, after the honest-sentence section.

Four requests land in your inbox on the same morning. For each, choose **mean**, **median**, **mode** or **refuse and say why**, and give a one-line defence.

1. "What is our typical order value?" The amount column has a Rs 480,000 order in it.
2. "Which segment do most of our orders come from?" Four segments, 47 records.
3. "What is the average time our support team takes to reply?" You are told most replies are quick and a handful sat over a weekend.
4. "What is the acceptance rate for `segment_c`?" `segment_c` holds six records.

One of these four is not a statistics question at all. Say which and say what it is instead.

---

## U1. Unguided, no hints: the full segment summary

**Drops in:** half two, after the guided first segment. Solution at close of session.

Working alone, on the cleaned file:

1. Produce a table with one row per segment holding: count, median amount, number accepted, accepted rate.
2. Sort it by accepted rate, best first.
3. Add the count to the same line as every rate.
4. Write one sentence per segment. Each sentence carries a number, its denominator, and what it does not support.
5. Two of your four sentences should decline to make a claim. If none of them does, reread step 4.

**Predict before you run.** Write down which segment you expect at the top of the rate ranking, and why. Then run it.

---

## U2. Unguided, no hints: repair a broken summary

**Drops in:** half two, alongside U1 for anyone who finishes early.

A colleague sends you this and asks whether it is ready to go to a stakeholder. It runs without error.

```python
counts = {"segment_a": 0, "segment_b": 0, "segment_c": 0, "segment_d": 0}
totals = {"segment_a": 0, "segment_b": 0, "segment_c": 0, "segment_d": 0}

for r in records:
    counts[r["segment"]] += 1
    totals[r["segment"]] += r["amount"]

print("average order by segment:")
for seg in counts:
    print(seg, "Rs", round(totals[seg] / counts[seg], 2))
```

1. It runs clean on this file. Name the input that makes it crash, and give the exact exception name.
2. It reports a number for `segment_b` that no stakeholder should see. What is that number, and what is wrong with it?
3. Make the smallest change that fixes the statistic. You may not delete any record.
4. There is a third problem that is not about crashing or about the mean. Name it. (Look at what the printed lines do not carry.)
5. Rewrite the `print` line so the output would survive being screenshotted and pasted into somebody else's slide.

---

## What to have on screen at close of session

- Your segment summary table with counts beside every rate.
- Four sentences, at least two of which decline to make a claim.
- The open question about `segment_d` against `segment_a`, written into your own notebook in your own words.

Bring all three on Monday. The Week 2 session opens on the third one.

# Solutions: Week 1, Day 4

Released at close of session. Every answer has four parts: the idea, the answer, the line-by-line why, and where the pattern shows up in production.

---

## G1. Seven values by hand

**The idea.** Mean and median answer the same question with different machinery, and the machinery only shows itself when one value is extreme.

**The answer.**

```
2000 + 3000 + 4000 + 4500 + 5000 + 6500 + 10000 = 35000
mean   = 35000 / 7 = 5000
sorted = 2000  3000  4000  [4500]  5000  6500  10000
median = 4500        (4th of 7, so three below and three above)
```

Change the last value to 80,000:

```
mean   = 105000 / 7 = 15000
median = 4500        unchanged
```

**Why, line by line.** The mean divides the total, so every rupee added to any record moves it. Adding 70,000 to one record adds 70,000/7 = 10,000 to the mean, which is exactly the jump you see. The median asks only which record is standing in position four. Changing the size of the record at position seven does not change who is standing at position four, so the median cannot move.

**Common wrong prediction.** Many people predict the median moves "a little". It moves by zero. Being precisely zero is what makes the median useful, and the surprise is worth having on paper.

**Where this shows up.** Any dashboard tile reading "average order value" recomputes this every night. On a marketplace with enterprise and consumer buyers in one table, that tile moves whenever a single large order lands, and nobody who reads it can tell whether the business changed or one customer did.

---

## G2. The first segment

**The idea.** The summary is four questions asked once per group, and the fourth one is the deliverable.

**The answer for `segment_a`.**

```
count           20
median amount   Rs 7,950
accepted        9
rate            45.0 percent
```

The sentence:

> `segment_a`: accepted on 9 of 20 records, 45.0 percent. The largest segment in the file, so this is the steadiest number available here, and twenty records still do not settle a comparison against another segment.

**Why the median rather than the mean.** The amount column across the file has a mean of Rs 18,000 against a median of Rs 7,500, so it carries a right tail. Once you have settled that for a column, you do not re-argue it per group. `segment_a` does not hold the whale, and the discipline is applied to the column rather than to whichever group happens to look safe today.

**Where this shows up.** Cohort tables, regional tables and channel tables in every reporting stack are this loop. The version that gets a team into trouble is the one that reports a mean per group because the mean was easier to accumulate.

---

## M1. Four files, two numbers each

| Dataset | Mean | Median | Reading |
|---|---|---|---|
| P | Rs 42,000 | Rs 39,500 | Mildly right-skewed. Mean is 1.06 times the median, which is normal for money. |
| Q | Rs 88,000 | Rs 12,000 | Strongly right-skewed. Mean is 7.3 times the median, so something very large is in there. |
| R | Rs 6,400 | Rs 6,350 | Roughly even. The two agree to within one percent. |
| S | Rs 3,100 | Rs 9,800 | Left-skewed. Mean is a third of the median, so something very small is pulling down. |

1. **Q.** The mean sits seven times above the median, which one or a few enormous values will do and almost nothing else will.
2. **S**, because a mean *below* the median means the tail is on the low side.
3. **P and R.** In both, mean and median sit close together, so the shape is roughly even and either statistic describes it. Report the count alongside regardless.
4. Realistic causes of a left tail: refunds and chargebacks recorded as negative amounts, cancelled orders left in at zero, or a partial-payment field where a subset settled at a fraction of the invoice. The general shape is a floor that a subset of records piles up against or falls below.

**Where this shows up.** Comparing mean to median is the cheapest data-quality check that exists. It is one line, it needs no chart, and it runs on a column you have never seen.

---

## M2. Pick the honest statistic

1. **Median.** The Rs 480,000 order makes the mean describe one record out of forty-seven. Send the median and name the large order in the same breath, since somebody will find it later and you want to have been the one who mentioned it.
2. **Mode**, and this is the one place it earns its keep. "Which segment do most orders come from" is a question about a category, and the most frequent category is a direct answer. In this file that is `segment_a` with 20 of 47.
3. **Median.** The description given ("most are quick, a handful sat over a weekend") is a right tail described in words. Response-time data is skewed almost everywhere, which is why service teams report median and a high percentile rather than an average.
4. **Refuse, and say why.** Six records do not support a rate. Report it as unmeasured, give the raw counts (3 of 6) so nobody thinks you are hiding it, and state what volume would make the number mean something.

**Which one is not a statistics question.** Number 4. It arrives dressed as a request for a number and it is really a request for a decision about evidence. The professional answer is the refusal plus the counts plus the condition, and giving 50.0 percent with no comment is the failure.

---

## U1. The full segment summary

**The answer.**

```
segment      count   median amount   accepted   rate
segment_a       20        Rs 7,950          9   45.0%
segment_b        9        Rs 8,000          4   44.4%
segment_c        6        Rs 6,800          3   50.0%
segment_d       12        Rs 6,750          7   58.3%
```

Sorted by rate, with the denominator restored:

```
segment_d   58.3%   on 12 records
segment_c   50.0%   on  6 records
segment_a   45.0%   on 20 records
segment_b   44.4%   on  9 records
```

The four sentences:

```
segment_a: accepted on 9 of 20 records, 45.0 percent. The largest segment in the file
           and the steadiest number here.

segment_b: accepted on 4 of 9 records, 44.4 percent. Median order Rs 8,000. The mean
           of Rs 60,255.56 is one order and should not be quoted.

segment_c: accepted on 3 of 6 records, 50.0 percent. Six records support nothing.
           Treat as unmeasured.

segment_d: accepted on 7 of 12 records, 58.3 percent. Highest in the file, resting on
           twelve records; two different outcomes erase the lead.
```

**The prediction step.** Most people predict `segment_a`, because it is the largest and largest feels safest. The ranking puts the two smallest segments on top instead.

**Why.** Small groups produce extreme rates in both directions with nothing causing it. `segment_d`'s rate rests on twelve records: one outcome flipping moves it 8.3 points, and two flipping drop it to 41.7 percent, below `segment_a`. The ranking is reading group size at least as much as it is reading performance.

**Where this shows up.** Every leaderboard of stores, regions, reps or campaigns ranked by a conversion rate. The smallest units occupy the top and bottom month after month while the middle sits still, and teams that have been burned once grey out any row below a stated minimum. Somebody had to choose that minimum and defend it, and that is the job you are being trained into.

---

## U2. Repair a broken summary

**1. The crash.** A file containing any segment outside the four hard-coded keys.

```
KeyError: 'segment_e'
```

The dictionaries are declared from what the author remembered rather than built from what the file holds. It works until the day somebody adds a segment, and nobody sends an email when they do.

**2. The number no stakeholder should see.**

```
segment_b Rs 60255.56
```

That is the mean of nine orders, eight of which are Rs 13,600 or less and one of which is Rs 480,000. It is arithmetically correct and it describes no order in that segment. Its own median is Rs 8,000.

**3. The smallest fix.** Accumulate the amounts into a list and take the median after the pass, rather than accumulating a running total and dividing.

```python
per_segment = {}

for r in records:
    key = r["segment"]
    if key not in per_segment:
        per_segment[key] = {"count": 0, "amounts": []}
    per_segment[key]["count"] += 1
    per_segment[key]["amounts"].append(r["amount"])

print("median order by segment:")
for seg in sorted(per_segment):
    b = per_segment[seg]
    print(seg, "Rs", statistics.median(b["amounts"]), "on", b["count"], "records")
```

Two changes: keys are built on first sight, and the statistic is the median. No record was deleted, which was the constraint.

**4. The third problem.** The printed lines carry no denominator. Every line hands over a number with no indication of how many records stand behind it, so a reader cannot tell the twenty-record answer from the six-record answer. The count is the fix, and it is in the rewritten `print` above.

**5. Surviving the screenshot.** The output has to carry its own context, because it will be cropped out of your notebook and pasted somewhere you never see.

```python
print("{}: median order Rs {:,.0f} on {} records".format(seg, statistics.median(b["amounts"]), b["count"]))
```

Reading `segment_c: median order Rs 6,800 on 6 records`, nobody can accidentally present it as a solid finding.

**Where this shows up.** Hard-coded category lists are one of the most common production breakages in analytics code, because the code is correct on the day it is written and the world changes underneath it. The defensive habit is to build keys from the data every time, even when you are sure you know the categories.

---

## The question left open on purpose

Is `segment_d` at 58.3 percent genuinely better than `segment_a` at 45.0 percent, or is that gap what four groups of these sizes do on their own?

Not answered today. There is a method for settling it and it is Monday's session. Writing the question down, with both numbers and both denominators, is the complete answer today.

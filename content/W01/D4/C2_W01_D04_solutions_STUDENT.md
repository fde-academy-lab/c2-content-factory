# Solutions: Week 1, Day 4

Released at close of session. Every answer has four parts: the idea, the answer, the line-by-line why, and where the pattern shows up in production.

---

## G1. Seven orders by hand

**The idea.** Mean and median answer the same question with different machinery, and the machinery only shows itself when one value is extreme.

**The answer.**

```
1280 + 1865 + 2270 + 2835 + 1310 + 1145 + 1030 = 11735
mean   = 11735 / 7 = 1676.43
sorted = 1030  1145  1280  [1310]  1865  2270  2835
median = 1310        (4th of 7, so three below and three above)
```

Replace Rs 2,835 with the file's real whale, Rs 480,000:

```
mean   = 488900 / 7 = 69842.86
median = 1310        unchanged
```

**Why, line by line.** The mean divides the total, so every rupee added to any order moves it. Adding 477,165 to one order adds 477,165/7 = 68,166.43 to the mean, which is exactly the jump you see. The median asks only which order is standing in position four. Changing the size of the order at position seven does not change who is standing at position four, so the median cannot move.

**Common wrong prediction.** Many people predict the median moves "a little". It moves by zero. Being precisely zero is what makes the median useful, and the surprise is worth having on paper.

**Where this shows up.** Any dashboard tile reading "average order value" recomputes this every night. On a marketplace with business and consumer buyers in one table, that tile moves whenever a single large order lands, and nobody reading it can tell whether the business changed or one customer did.

---

## G2. The first segment

**The idea.** The summary is four questions asked once per group, and the fourth is the deliverable.

**The answer for Business.**

```
count           9
median amount   Rs 2,050
returned        1
return rate     11.1 percent
```

The sentence:

> Business: returned on 1 of 9 orders, 11.1 percent. The lowest return rate in the file and the smallest segment in it. One more return takes it to 22.2 percent and behind Student, so this is not yet a finding.

**Why the median rather than the mean.** The amount column across the file has a mean of Rs 12,753.30 against a median of Rs 1,910, so it carries a right tail. Once you have settled that for a column, you do not re-argue it per group. Business does not hold the whale, and the discipline applies to the column rather than to whichever group happens to look safe today.

**Where this shows up.** Cohort tables, regional tables and channel tables in every reporting stack are this loop. The version that gets a team into trouble reports a mean per group because the mean was easier to accumulate.

---

## M1. Four files, two numbers each

| Dataset | Mean | Median | Reading |
|---|---|---|---|
| P | Rs 42,000 | Rs 39,500 | Mildly right-skewed. Mean is 1.06 times the median, normal for money. |
| Q | Rs 88,000 | Rs 12,000 | Strongly right-skewed. Mean is 7.3 times the median, so something very large is in there. |
| R | Rs 6,400 | Rs 6,350 | Roughly even. The two agree to within one percent. |
| S | Rs 3,100 | Rs 9,800 | Left-skewed. Mean is a third of the median, so something very small pulls down. |

1. **Q.** The mean sits seven times above the median, which one or a few enormous values will do and almost nothing else will.
2. **S**, because a mean *below* the median means the tail is on the low side.
3. **P and R.** In both, mean and median sit close together, so the shape is roughly even and either statistic describes it. Report the count alongside regardless.
4. Realistic causes of a left tail in an order book: refunds and chargebacks recorded as negative amounts, cancelled orders left in at zero, or a partial-payment field where a subset settled at a fraction of the invoice. The general shape is a floor that a subset of orders piles up against or falls below.

**Where your own file sits.** Kalpa's profiled file has a mean of Rs 12,753.30 against a median of Rs 1,910, a ratio of 6.68. It is dataset Q, and more extreme than Q.

**Where this shows up.** Comparing mean to median is the cheapest data-quality check that exists. It is one line, it needs no chart, and it runs on a column you have never seen.

---

## M2. Pick the honest statistic

1. **Median.** Order `KR4232` at Rs 480,000 makes the mean describe one order out of forty-four. Send the median and name the large order in the same breath, since somebody will find it later and you want to have been the one who mentioned it.
2. **Mode**, and this is the one place it earns its keep. "Which segment do most orders come from" is a question about a category, and the most frequent category is a direct answer. In this file that is Retail-Core with 14 of 44.
3. **Median.** The description given, most are quick and a handful sat over a weekend, is a right tail described in words. Response-time data is skewed almost everywhere, which is why service teams report median and a high percentile rather than an average.
4. **Refuse, and say why.** Nine orders do not support a rate. Report it as unmeasured, give the raw counts (1 of 9) so nobody thinks you are hiding it, and state what volume would make the number mean something.

**Which one is not a statistics question.** Number 4. It arrives dressed as a request for a number and it is really a request for a decision about evidence. The professional answer is the refusal plus the counts plus the condition, and giving 11.1 percent with no comment is the failure.

---

## U1. The full segment summary

**The answer.**

```
segment        orders   median amount   returned   rate
Business            9        Rs 2,050          1   11.1%
Retail-Core        14        Rs 1,910          5   35.7%
Retail-Plus        11        Rs 1,435          4   36.4%
Student            10        Rs 1,430          2   20.0%
```

Sorted by return rate, best first, with the denominator restored:

```
Business      11.1%   on  9 orders
Student       20.0%   on 10 orders
Retail-Core   35.7%   on 14 orders
Retail-Plus   36.4%   on 11 orders
```

The four sentences:

```
Business:    returned on 1 of 9 orders, 11.1 percent. Lowest in the file and the smallest
             segment in it. One more return takes it to 22.2 percent and behind Student,
             so this is not yet a finding.

Student:     returned on 2 of 10 orders, 20.0 percent. Ten orders, and the raw file held
             twelve before two failed conversion. Treat as unmeasured.

Retail-Core: returned on 5 of 14 orders, 35.7 percent. Largest segment and the steadiest
             number here. Median order Rs 1,910; the mean of Rs 36,027.14 is the
             Rs 480,000 order and should not be quoted.

Retail-Plus: returned on 4 of 11 orders, 36.4 percent. Highest in the file and within one
             order of Retail-Core. The two are not separated by this data.
```

**The prediction step.** Most people predict Retail-Core, because it is the largest and largest feels safest. The ranking puts the two smallest segments on top instead.

**Why.** Small groups produce extreme rates in both directions with nothing causing it. Business's rate rests on nine orders: one more return moves it from 11.1 to 22.2 percent, behind Student. The ranking is reading group size at least as much as it is reading performance.

**Where this shows up.** Every leaderboard of stores, regions, reps or campaigns ranked by a rate. The smallest units occupy the top and bottom month after month while the middle sits still, and teams that have been burned once grey out any row below a stated minimum. Somebody had to choose that minimum and defend it, and that is the job you are being trained into.

---

## U2. Repair a broken summary

**1. The crash.** A file containing any segment outside the four hard-coded keys.

```
KeyError: 'Wholesale'
```

The exact key depends on what the new segment is called. The dictionaries are declared from what the author remembered rather than built from what the file holds. It works until the day somebody launches a segment, and nobody sends an email when they do.

**2. The number no stakeholder should see.**

```
Retail-Core Rs 36027.14
```

That is the mean of fourteen orders, thirteen of which are under Rs 3,000 and one of which is Rs 480,000. It is arithmetically correct and it describes no order in that segment. Retail-Core's own median is Rs 1,910.

**3. The smallest fix.** Accumulate the amounts into a list and take the median after the pass, rather than accumulating a running total and dividing.

```python
per_segment = {}

for r in orders:
    key = r["segment"]
    if key not in per_segment:
        per_segment[key] = {"count": 0, "amounts": []}
    per_segment[key]["count"] += 1
    per_segment[key]["amounts"].append(r["amount"])

print("median order by segment:")
for seg in sorted(per_segment):
    b = per_segment[seg]
    print(seg, "Rs", statistics.median(b["amounts"]), "on", b["count"], "orders")
```

Two changes: keys are built on first sight, and the statistic is the median. No order was deleted, which was the constraint.

**4. The third problem.** The printed lines carry no denominator. Every line hands over a number with no indication of how many orders stand behind it, so a reader cannot tell the fourteen-order answer from the nine-order answer. The count is the fix, and it is in the rewritten `print` above.

**5. Surviving the screenshot.** The output has to carry its own context, because it will be cropped out of your notebook and pasted somewhere you never see.

```python
print("{}: median order Rs {:,.0f} on {} orders".format(seg, statistics.median(b["amounts"]), b["count"]))
```

Reading `Business: median order Rs 2,050 on 9 orders`, nobody can accidentally present it as a solid finding.

**Where this shows up.** Hard-coded category lists are one of the most common production breakages in analytics code, because the code is correct on the day it is written and the world changes underneath it. The defensive habit is to build keys from the data every time, even when you are sure you know the categories. Kalpa has four segments today.

---

## The question left open on purpose

Is Business at 11.1 percent genuinely better than Retail-Plus at 36.4 percent, or is that gap what four groups of these sizes do on their own?

Not answered today. There is a method for settling it and it is Monday's session. Writing the question down, with both numbers and both denominators, is the complete answer today.

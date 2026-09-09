# Day 4 solution, U2. Repair a broken summary

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

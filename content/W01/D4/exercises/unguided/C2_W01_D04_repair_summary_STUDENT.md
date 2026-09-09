# Day 4, U2. Unguided, no hints: repair a broken summary

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

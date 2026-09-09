# Day 1, E3. Mid-session: find the mistake

Drop point: the close of the first half, after the accumulators. About 15 minutes. Read the cell before you run it.

This cell runs all the way to the end and prints a number.

```
for r in records:
    if r["status"] == "delivered":
        total = 0
        total = total + int(r["amount"])

print(total)
```

1. Before you run it, write down the number you expect to see.
2. Run it. It prints `1460`. Say in one sentence which order that number is the amount of, and why this loop ended up holding it.
3. Repair the cell by moving one line. Write the corrected cell out and run it, then write down what it prints.
4. This cell named no error and stopped nothing. Say in one sentence why a wrong number that runs cleanly is harder to catch than the `TypeError` you met earlier in the day.
5. Give one check you could do in your head, on any total over a group of orders, that would have caught this without reading the code at all.

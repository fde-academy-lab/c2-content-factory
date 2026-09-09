# Day 4 solution, G1. Seven orders by hand

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

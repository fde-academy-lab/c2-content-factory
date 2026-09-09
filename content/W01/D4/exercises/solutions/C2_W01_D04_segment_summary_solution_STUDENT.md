# Day 4 solution, U1. The full segment summary

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

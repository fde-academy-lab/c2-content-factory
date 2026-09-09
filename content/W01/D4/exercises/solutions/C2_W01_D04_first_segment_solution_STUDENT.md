# Day 4 solution, G2. The first segment

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

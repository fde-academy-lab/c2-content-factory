# Day 3 solution, E4. The full pass

### What you should have seen

```
input 50, clean 44, rejected 6
50 in = 44 profiled + 6 rejected
```

The six rejections, each carrying the interpreter's own wording:

```
KR4210  'twelve'
KR4214  ''
KR4231  '12,400'
KR4235  '24 500'
KR4237  ''
KR4240  'Rs 8000'
```

Total across the 44 that convert: Rs 561,145.

### The two things that needed a decision rather than a cleaning step

**The row.** `order_id` `KR4201` appears twice, on rows that differ only in `order_date`, six weeks apart. No whole-record comparison finds it, because the rows are not identical. Your log should show both rows kept and the pair flagged, with an identity rule proposed and the order book owner named as the decider.

**The value.** One order is Rs 480,000, which is 86 percent of the total and over 160 times the next largest. It converts cleanly and is well formed in every field. Your log should show it kept, with the reason that it is real until somebody says otherwise, and raised.

If you deleted either one, the number you produced may well be more useful and it is no longer defensible, which is a worse trade than it sounds.

### A decisions log that would pass review

```
field           finding                                    choice                      reason
amount          48/50 present, 44/50 convertible           reject the 6 unusable       amount is required
discount        11/50 present                              keep absent as absent       absence means no discount
order_id        1 id on two rows (KR4201)                  keep both, flag the pair    owner decides the identity rule
amount          one order at Rs 480,000, 86% of total      keep, raise with owner      converts cleanly, well formed
```

Four lines. A reviewer who was not in the room can follow every one, which is the only test that matters.

### If your numbers did not reconcile

The usual causes, in the order they occur: an append sitting inside a branch that does not always run, a `continue` placed before the counter, or a filter applied to the clean list after the count was taken. Print the length of every list immediately after you build it and the gap appears in one run.

### Where this lives in production

The decisions log is the artifact that survives you. When somebody asks in six months why revenue for August looks low, the log is what answers it, and its absence is what turns a ten minute question into a week.

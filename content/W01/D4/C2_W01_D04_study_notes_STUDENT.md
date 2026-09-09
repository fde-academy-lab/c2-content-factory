# Study notes: Week 1, Day 4

Describe without misleading: typical, spread, skew and the segment summary.

Read these after the session. They are written against the session as planned and get revised against the recording once it arrives, so if a number here disagrees with what happened in the room, the room wins and the note gets fixed.

---

## The one sentence

Every summary number is a claim about a shape nobody can see, so you look at the shape first, choose the number that does not lie about it, and never hand over a rate without the count it rests on.

---

## Where today sat in the week

```
Mon   read the orders                 loops, conditions, accumulators
Tue   package and survive bad data    functions, tracebacks, files
Wed   profile before you touch        50 in, 44 profiled, 6 rejected, decisions log
Thu   describe without misleading     <- you are here
Mon   is the difference real          the method this session refused to use
```

Thursday consumes Wednesday's output and produces the first thing anybody outside the team would read.

**Two things you carried in from Wednesday** and that changed today's numbers:

- `KR4201` appears twice. You chose to keep both rows and flag the pair, because they differ on `order_date` by six weeks and the order book owner decides. So you described 44 rows containing one unresolved pair.
- Student held twelve orders in the raw file and ten in the profiled one, because two Student orders failed conversion. Your cleaning changed the denominator of your smallest segment, and only the rejects log records it.

---

## 1. Three answers to "what is typical"

| Statistic | The question it answers | Where it breaks |
|---|---|---|
| Mean | If the total were shared out equally, what would each order carry | One large order drags it away from everybody |
| Median | What does the order standing in the middle look like | Ignores size entirely, which is usually what you want |
| Mode | Which exact value repeats most often | On money almost nothing repeats, so it describes almost nothing |

The hand-worked seven from the session, the first seven orders in the file:

```
1030  1145  1280  1310  1865  2270  2835
mean   = 11735 / 7 = 1676.43
median = 1310  (4th of 7)

replace 2835 with the file's own whale, 480000:
mean   = 488900 / 7 = 69842.86      nearly 42 times larger
median = 1310                       did not move at all
```

The median moving by exactly zero is the thing to remember. It is not "moves a little". Changing the size of the largest order does not change which order stands in the middle.

---

## 2. The whale, and the failure of the day

The session's deliberate failure raised no exception at all:

```
mean amount over 44 orders: Rs 12,753.30
orders at or above Rs 12,753.30: 1
orders below Rs 12,753.30: 43
```

The arithmetic is right. The description is wrong. Forty-three of forty-four orders sit below the number somebody was about to call typical.

The cause is one order:

```
KR4232   C1749   Retail-Core   480000   delivered   2026-08-19
```

It carries **85.5 percent of every rupee in the file**. The second largest order is Rs 2,995, so the whale is a hundred and sixty times the one below it.

| Column | With the whale | Without it |
|---|---|---|
| All orders, mean | Rs 12,753.30 | Rs 1,887.09 |
| All orders, median | Rs 1,910.00 | Rs 1,865.00 |

**The tell.** Removing one order out of forty-four drops the mean by a factor of nearly seven and lands it within Rs 22 of the median. When taking out a single record makes the mean and the median agree, the mean was describing that record rather than the business.

**The whale stays in the file.** It converts cleanly, it is well formed, and Wednesday's decisions log records the choice to keep it and raise it with the order book owner. The data does not change. The statistic changes.

Nothing in `try` and `except` catches this class of failure. The only thing that catches it is looking at the shape before you speak.

---

## 3. Spread, and a rule that runs without you

```
min:   Rs       800
max:   Rs   480,000
range: Rs   479,200
```

Range is built from two orders out of forty-four and one of them is the whale, so it tells you about those two orders.

Wednesday's fence was ten times the middle order, which worked and was deliberately crude because somebody chose the ten. The standard version uses the spread of the middle half instead:

```
Q1          = Rs  1,287.50
Q3          = Rs  2,718.75
IQR         = Q3 - Q1        = Rs 1,431.25
upper fence = Q3 + 1.5 x IQR = Rs 4,865.62

orders above the fence: 1
```

It caught the whale and nothing else. The largest ordinary order at Rs 2,995 sits well inside.

Two rules, built differently, agreeing on the same single record. That agreement is worth more than either rule alone.

**A fence is a flag, never a delete key.** Wednesday's language is unchanged: an outlier is a finding to investigate before it is a row to delete.

---

## 4. Reading the shape with no chart

```
 min      median                                            max
  800      1,910                                        480,000
   |---------|-----------------------------------------------|
    1,110 down              478,090 up
```

The up side is 431 times the down side, which is the skew, read off sorted values with one subtraction each way.

The cheaper version, one line on any column in any language:

| What you see | What it means |
|---|---|
| Mean well above median | Something large pulls on the right |
| Mean well below median | Something small pulls on the left |
| Mean and median close | Roughly even shape, either statistic describes it |

This file: mean Rs 12,753.30, median Rs 1,910.00, a ratio of 6.68. You knew there was a tail before looking at a single order.

**Anscombe's quartet, 1973.** Frank Anscombe built four datasets sharing nearly identical means, variances and correlations that look nothing alike when drawn. A summary statistic is a compression and every compression discards. Until Week 2, the sorted list and the mean-to-median ratio are your picture.

---

## 5. The accumulator, and the KeyError

```python
counts = {"Retail-Core": 0, "Retail-Plus": 0, "Business": 0}
for r in orders:
    counts[r["segment"]] += 1
```

```
KeyError: 'Student'
```

A dictionary was asked for a key it does not hold, and Python printed the key. Three segments were typed from memory; Kalpa Retail has four. It failed on the first order in the file, `KR4200`, which is a Student order.

**Every hard-coded list of categories is a promise about data you have not read yet.**

The fix builds the key the first time it appears:

```python
counts = {}
for r in orders:
    key = r["segment"]
    if key not in counts:
        counts[key] = 0
    counts[key] += 1
```

Or the short form, which is Monday's `.get()` doing exactly what it did on Monday:

```python
counts[key] = counts.get(key, 0) + 1
```

The median cannot be accumulated one order at a time, since it needs the whole group sorted. So the pass collects amounts into a list and the median is taken after the loop ends.

---

## 6. The segment summary, and what the ranking measures

Return rate is `returned / all orders in the group`. It is the first metric in the programme where **lower is better**.

```
segment        orders   median amount   returned   rate
Business            9        Rs 2,050          1   11.1%
Retail-Core        14        Rs 1,910          5   35.7%
Retail-Plus        11        Rs 1,435          4   36.4%
Student            10        Rs 1,430          2   20.0%
```

Ranked best first, with the denominator restored:

```
Business      11.1%   on  9 orders
Student       20.0%   on 10 orders
Retail-Core   35.7%   on 14 orders
Retail-Plus   36.4%   on 11 orders
```

The two best-performing segments are the two smallest segments. That is not a coincidence about this file.

```
if 0 more Business orders had been returned:  11.1%   still best
if 1 more Business order  had been returned:  22.2%   no longer best
```

**One order.** Small groups produce extreme rates in both directions with nothing causing it. Rank groups of very different sizes by a rate and the ranking reads group size at least as much as performance. The fix is not a cleverer statistic. It is the count column you already have.

---

## 7. The honest sentence

Three parts, in this order, every time:

```
[the number]   [the denominator]   [what it does not yet support]
```

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

Two decline to make a claim and a third says two segments cannot be told apart. That is the sentence doing its job, and it is the deliverable, since a table gets cropped and pasted by somebody who never saw your notebook.

---

## 8. The question left open on purpose

> Is Business at 11.1 percent on 9 orders genuinely better than Retail-Plus at 36.4 percent on 11 orders, or is that gap what four groups of these sizes do on their own?

Not answered today. There is a method and it is Monday's session.

Writing the question down with both numbers and both denominators is the complete professional answer today. "We do not know yet, and here is exactly what would tell us" is a full answer in a room that wanted a different one.

---

## Model answers to the day's interview questions

**A stakeholder asks for the average order value and one enormous order sits in the data. What do you give them?**

Give the median and name it as the median. State the count it rests on. Then say the large order exists, that it is real and retained, and that quoting the mean would describe one order out of forty-four. The third part is what separates a good answer from a correct one, because you want to be the person who mentioned it rather than the person it was found on.

**How would you check for skew without plotting anything?**

Sort the values and compare the distance from the median to the maximum against the distance from the median to the minimum. Then compare the mean against the median: a mean well above the median means a right tail. Offer the second part even if only one was asked for, since it is one line on any column.

**Segment A converts at 42 percent on 12 records and segment B at 31 percent on 1,200. Which do you trust?**

Trust B, and justify it by movement: one record swings A by more than eight points and B by less than a tenth of one. Then add the part most candidates leave out, which is that A is reported as unmeasured rather than as bad, along with what volume would make it meaningful. You have a stronger version of this answer than most candidates because you can say it about your own file: Business leads on nine orders and one order takes the lead away.

**Your cleaning run reported zero rejects on a file you know is dirty. What do you check?** (Wednesday's, returning)

Check that the loop is running at all by printing the order count. Check that the rejection branch can be reached, since a condition that is never true and a condition that never runs look identical in the output. Then check that the failures are not being swallowed by a broad `except`, which is Tuesday's argument in a new costume.

---

## Crux lines to carry into Week 2

> The mean was right and the description was wrong.

> On a money column, send the median, and say that is what you sent.

> Every rate carries its denominator, or it lies for you while you are not in the room.

Week 2 re-expresses this entire pass as one line of pandas and one SQL `GROUP BY` on the same orders. You built it by hand once so that when the one-liner arrives you already know what the answer should be, and you will notice if it disagrees.

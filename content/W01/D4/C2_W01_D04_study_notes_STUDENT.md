# Study notes: Week 1, Day 4

Describe without misleading: typical, spread, skew and the segment summary.

Read these after the session. They are written against the session as planned and get revised against the recording once it arrives, so if a number here disagrees with what happened in the room, the room wins and the note gets fixed.

---

## The one sentence

Every summary number is a claim about a shape nobody can see, so you look at the shape first, choose the number that does not lie about it, and never hand over a rate without the count it rests on.

---

## Where today sat in the week

```
Mon   read the records                loops, conditions, accumulators
Tue   package and survive bad data    functions, tracebacks, files
Wed   profile before you touch        cleaning, decisions log, 47 usable records
Thu   describe without misleading     <- you are here
Mon   is the difference real          the method this session refused to use
```

Thursday consumes Wednesday's output and produces the first thing anybody outside the team would read.

---

## 1. Three answers to "what is typical"

| Statistic | The question it answers | Where it breaks |
|---|---|---|
| Mean | If the total were shared out equally, what would each record hold | One large record drags it away from everybody |
| Median | What does the record standing in the middle look like | Ignores size entirely, which is usually what you want and occasionally is not |
| Mode | Which exact value repeats most often | On money almost nothing repeats, so it describes almost nothing |

The hand-worked seven from the session:

```
2000  3000  4000  4500  5000  6500  10000
mean   = 35000 / 7 = 5000
median = 4500  (4th of 7)

change the last value to 80000:
mean   = 105000 / 7 = 15000     tripled
median = 4500                   did not move at all
```

The median moving by exactly zero is the thing to remember. It is not "moves a little". Changing the size of the largest record does not change which record stands in the middle.

---

## 2. The whale, and the failure of the day

The session's deliberate failure raised no exception at all:

```
mean amount over 47 records: Rs 18000.00
records at or above Rs 18000.00: 1
records below Rs 18000.00: 46
```

The arithmetic is right. The description is wrong. Forty-six of forty-seven records sit below the number somebody was about to call typical.

The cause was one real order of Rs 480,000 in `segment_b`. The second-largest order in the file is Rs 17,400.

| Column | With the whale | Without it |
|---|---|---|
| All records, mean | Rs 18,000.00 | Rs 7,956.52 |
| All records, median | Rs 7,500 | Rs 7,300 |
| `segment_b` mean, 9 records | Rs 60,255.56 | Rs 7,787.50 |

**The whale stays in the file.** It is real, Wednesday's cleaning pass kept it for that reason, and the decisions log exists so that nobody removes an inconvenient record quietly. The data does not change. The statistic changes.

Nothing in `try` and `except` catches this class of failure. The only thing that catches it is looking at the shape before you speak.

---

## 3. Spread, and a rule that runs without you

```
min:   Rs 1,800
max:   Rs 480,000
range: Rs 478,200
```

Range is built from two records out of forty-seven and one of them is the whale, so it tells you about those two records.

The fence, which is Wednesday's sorted-tail read with a rule attached:

```
Q1          = Rs 4,800
Q3          = Rs 10,900
IQR         = Q3 - Q1        = Rs 6,100
upper fence = Q3 + 1.5 x IQR = Rs 20,050

records above the fence: 1
```

It caught the whale and nothing else. The largest ordinary order at Rs 17,400 sits comfortably inside.

**A fence is a flag, never a delete key.** Wednesday's language is unchanged: an outlier is a finding to investigate before it is a row to delete. The fence just finds it on a file too big to eyeball.

---

## 4. Reading the shape with no chart

You have no plotting library until Week 2 and you do not need one.

```
 min          median                                        max
  |              |                                           |
  +--------------+-------------------------------------------+
     5,700 down              472,500 up
```

The up side is 83 times the down side, which is the skew, read off sorted values with one subtraction each way.

The cheaper version, one line on any column in any language:

| What you see | What it means |
|---|---|
| Mean well above median | Something large pulls on the right |
| Mean well below median | Something small pulls on the left |
| Mean and median close | Roughly even shape, either statistic describes it |

This file: mean Rs 18,000, median Rs 7,500, a ratio of 2.40. You knew there was a tail before looking at a single record.

**Anscombe's quartet, 1973.** Frank Anscombe built four datasets sharing nearly identical means, variances and correlations that look nothing alike when drawn. A summary statistic is a compression and every compression discards. Until Week 2, the sorted list and the mean-to-median ratio are your picture.

---

## 5. The accumulator, and the KeyError

```python
counts = {"segment_a": 0, "segment_b": 0, "segment_c": 0}
for r in records:
    counts[r["segment"]] += 1
```

```
KeyError: 'segment_d'
```

A dictionary was asked for a key it does not hold, and Python printed the key. Three segments were typed from memory; the file holds four.

**Every hard-coded list of categories is a promise about data you have not read yet.**

The fix builds the key the first time it appears:

```python
counts = {}
for r in records:
    key = r["segment"]
    if key not in counts:
        counts[key] = 0
    counts[key] += 1
```

Or the short form, which is Monday's `.get()` doing exactly what it did on Monday:

```python
counts[key] = counts.get(key, 0) + 1
```

The median cannot be accumulated one record at a time, since it needs the whole group sorted. So the pass collects amounts into a list and the median is taken after the loop ends.

---

## 6. The segment summary, and what the ranking measures

```
segment      count   median amount   accepted   rate
segment_a       20        Rs 7,950          9   45.0%
segment_b        9        Rs 8,000          4   44.4%
segment_c        6        Rs 6,800          3   50.0%
segment_d       12        Rs 6,750          7   58.3%
```

Ranked by rate, with the denominator restored:

```
segment_d   58.3%   on 12 records
segment_c   50.0%   on  6 records
segment_a   45.0%   on 20 records
segment_b   44.4%   on  9 records
```

The two best-performing segments are the two smallest segments. That is not a coincidence about this file.

`segment_d` leads `segment_a` by 13.3 points on twelve records. One outcome flipping drops it to 50.0 percent. Two flipping drop it to 41.7 percent, below `segment_a`.

Small groups produce extreme rates in both directions with nothing causing it. Rank groups of very different sizes by a rate and the ranking reads group size at least as much as it reads performance. The fix is not a cleverer statistic. It is the count column you already have.

---

## 7. The honest sentence

Three parts, in this order, every time:

```
[the number]   [the denominator]   [what it does not yet support]
```

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

Two of the four decline to make a claim. That is the sentence doing its job, and it is the deliverable, since a table gets cropped and pasted by somebody who never saw your notebook.

---

## 8. The question left open on purpose

> Is `segment_d` at 58.3 percent on 12 records genuinely better than `segment_a` at 45.0 percent on 20 records, or is that gap what four groups of these sizes do on their own?

Not answered today. There is a method and it is Monday's session.

Writing the question down with both numbers and both denominators is the complete professional answer today. "We do not know yet, and here is exactly what would tell us" is a full answer in a room that wanted a different one.

---

## Model answers to the day's interview questions

**A stakeholder asks for the average order value and one enormous order sits in the data. What do you give them?**

Give the median and name it as the median. State the count it rests on. Then say the large order exists, that it is real and retained, and that quoting the mean would describe one record out of forty-seven. The third part is what separates a good answer from a correct one, because you want to be the person who mentioned it rather than the person it was found on.

**How would you check for skew without plotting anything?**

Sort the values and compare the distance from the median to the maximum against the distance from the median to the minimum. Then compare the mean against the median: a mean well above the median means a right tail. Offer the second part even if only one was asked for, since it is one line on any column.

**Segment A converts at 42 percent on 12 records and segment B at 31 percent on 1,200. Which do you trust?**

Trust B, and justify it by movement: one record swings A by more than eight points and B by less than a tenth of one. Then add the part most candidates leave out, which is that A is reported as unmeasured rather than as bad, along with what volume would make it meaningful.

**Your cleaning run reported zero rejects on a file you know is dirty. What do you check?** (Wednesday's, returning)

Check that the loop is running at all by printing the record count. Check that the rejection branch can be reached, since a condition that is never true and a condition that never runs look identical in the output. Then check that the failures are not being swallowed by a broad `except`, which is Tuesday's argument in a new costume.

---

## Crux lines to carry into Week 2

> The mean was right and the description was wrong.

> On a money column, send the median, and say that is what you sent.

> Every rate carries its denominator, or it lies for you while you are not in the room.

Week 2 re-expresses this entire pass as one line of pandas and one SQL `GROUP BY` on the same records. You built it by hand once so that when the one-liner arrives you already know what the answer should be, and you will notice if it disagrees.

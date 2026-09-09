# Half two: the segment summary, and the count it rests on

Week 1, Day 4. Slide source. One idea per slide.

Position bar, repeated at every section boundary:
`[one column] > [what is typical] > [what one record does] > [what the shape says] > [per segment, with denominators]`

---

## S1. Per segment, with denominators

Half one gave you one number for the whole file. Nobody runs a business on one number.

The question is always the same one level down: which part of this is working, and how sure can you be.

---

## S2. Where we are

`[one column] > [what is typical] > [what one record does] > [what the shape says] > **[per segment, with denominators]**`

You can now pick an honest statistic for a column. Half two splits the file into groups, computes that statistic per group, and attaches the one thing that decides whether the answer means anything.

---

## S2b. Where this is going

```
segment      count   median amount   accepted rate
segment_d       12        Rs 6,750           58.3%
segment_c        6        Rs 6,800           50.0%
segment_a       20        Rs 7,950           45.0%
segment_b        9        Rs 8,000           44.4%
```

You will have built this inside the hour. Then you will spend the rest of the session refusing to send it as it stands.

---

## SECTION 1: THE DENOMINATOR

`[one column] > [what is typical] > [what one record does] > [what the shape says] > **[per segment, with denominators]**`

---

## S3. One rate, two files

Two segments in two different companies, same reported number:

```
segment X:   accepted 5 of 12          41.7%
segment Y:   accepted 500 of 1200      41.7%
```

Identical rates. Which one would you build a quarter's plan on?

---

## S4. Why the small one moves

In the 12-record segment, one record changing its outcome moves the rate by 8.3 points.

In the 1,200-record segment, one record moves it by 0.08 points.

The small segment is not wrong. It is loud. Its number swings on evidence too thin to swing on, and next month it will report something different for no reason you can name.

---

## S5. What a rate actually is

```
rate = how many did the thing  /  how many could have
```

Two numbers, and the reporting convention throws one of them away.

Every argument in this section comes from the thrown-away number.

---

## S6. The rule

> A rate travels with its denominator or it does not travel.

Write it as `58.3 percent of 12` and nobody can misread it. Write it as `58.3 percent` and everybody will.

---

## SECTION 2: THE ACCUMULATOR

`[one column] > [what is typical] > [what one record does] > [what the shape says] > **[per segment, with denominators]**`

---

## S7. Counting into buckets

Monday you counted records that passed a test. Today you count them into named piles, one pile per segment.

```
counts = {"segment_a": 0, "segment_b": 0, "segment_c": 0}

for r in records:
    counts[r["segment"]] = counts[r["segment"]] + 1
```

Reasonable code. The trainer listed the segments they remembered.

---

## S8. Run it

```
KeyError: 'segment_d'
```

---

## S9. Reading it

`KeyError` means a dictionary was asked for a key it does not hold. The key it did not hold is printed for you: `segment_d`.

The dictionary held three segments because a person typed three segments. The file holds four.

Every hard-coded list of categories is a promise about data you have not read yet.

---

## S10. Build the key when you first see it

```
counts = {}

for r in records:
    key = r["segment"]
    if key not in counts:
        counts[key] = 0
    counts[key] = counts[key] + 1
```

Three lines instead of one declaration, and the code now works on a file with segments nobody told you about.

The same shape written shorter, which you will meet again in Week 2:

```
counts[key] = counts.get(key, 0) + 1
```

That is Monday's `.get()` with a default, doing exactly what it did on Monday.

---

## S11. The fixed count

```
segment_a: 20
segment_b: 9
segment_c: 6
segment_d: 12
        total: 47
```

The total matches your cleaned record count. If it did not, you would have a bug and the last line is how you would know.

---

## SECTION 3: THE SEGMENT SUMMARY

`[one column] > [what is typical] > [what one record does] > [what the shape says] > **[per segment, with denominators]**`

---

## S12. Three accumulators, one pass

Per segment you need three things: how many records, what a typical amount looks like, and what share were accepted.

```
per_segment[key] = {
    "count":    how many records landed here,
    "amounts":  every amount, collected so the median can be taken at the end,
    "accepted": how many had outcome "accepted",
}
```

The median cannot be accumulated one record at a time. It needs the whole list sorted, so the list is collected during the pass and the median is taken after it.

---

## S13. The table

```
segment      count   median amount   accepted   rate
segment_a       20        Rs 7,950          9   45.0%
segment_b        9        Rs 8,000          4   44.4%
segment_c        6        Rs 6,800          3   50.0%
segment_d       12        Rs 6,750          7   58.3%
```

Note what is absent from every row: the mean. Half one settled that.

---

## S14. Sort by rate, the way anyone would

```
segment_d   58.3%
segment_c   50.0%
segment_a   45.0%
segment_b   44.4%
```

A clean ranking. `segment_d` is the winner by more than eight points.

Somebody in a meeting is about to move budget.

---

## S15. Put the count back

```
segment_d   58.3%   on 12 records
segment_c   50.0%   on  6 records
segment_a   45.0%   on 20 records
segment_b   44.4%   on  9 records
```

The top two performers are the two smallest segments in the file.

`segment_d`'s lead over `segment_a` is 13.3 points and rests on 12 records. Move two of those records and the lead is gone.

---

## S16. What the ranking was measuring

Small groups produce extreme rates in both directions, every time, in any dataset, with no cause behind it at all.

Rank any set of groups by a rate and the smallest groups drift to both ends of the list. The ranking is reading group size as much as it is reading performance.

The fix is not a cleverer statistic. It is the column you already have.

---

## SECTION 4: THE HONEST SENTENCE

`[one column] > [what is typical] > [what one record does] > [what the shape says] > **[per segment, with denominators]**`

---

## S17. The shape of the sentence

Three parts, in this order, every time:

```
[the number]   [the denominator]   [what it does not yet support]
```

Leaving out the third part is how a caveat gets lost between your notebook and a slide somebody else builds.

---

## S18. Four sentences, one per segment

```
segment_a: accepted on 9 of 20 records, 45.0 percent. The largest segment
           in the file and the steadiest number here.

segment_b: accepted on 4 of 9 records, 44.4 percent. Median order Rs 8,000;
           the mean of Rs 60,255.56 is one order and should not be quoted.

segment_c: accepted on 3 of 6 records, 50.0 percent. Six records support
           nothing; treat as unmeasured.

segment_d: accepted on 7 of 12 records, 58.3 percent. Highest in the file
           and resting on twelve records; two different outcomes erase
           the lead.
```

Every sentence carries its denominator. Two of them refuse to make a claim, which is the sentence doing its job.

---

## S19. The convention this follows

`segment_b`'s mean order value is Rs 60,255.56. Its median is Rs 8,000. One record separates those.

Reporting the median for money is the standing convention wherever a few very large values sit in a long tail, which is why national statistics report median household income. You applied it in half one to a column. Here it applies to a cell in a table somebody will screenshot.

---

## S20. The question you are not answering today

Is `segment_d` genuinely better than `segment_a`, or is 58.3 against 45.0 what four groups of this size do on their own?

That question has a real answer and a method behind it, and it is Monday's session.

Today you name the question, write it in the notebook, and stop. Saying "we do not know yet, and here is what would tell us" is a complete professional answer.

---

## S21. The decision card

| Before you send a rate | Check |
|---|---|
| Is the denominator on the same line as the number | If not, it is not ready |
| Is any group under about 30 records | Say so in the sentence, in words |
| Did you rank groups of very different sizes | Say what the ranking is partly measuring |
| Is a mean quoted on a money column | Replace it with the median |
| Is a difference being called real | Park it and name what would settle it |

---

## S22. Crux

> Every rate carries its denominator, or it lies for you while you are not in the room.
> The two best-performing segments in this file are also the two smallest, and that is not a coincidence.

Tomorrow is Gandhi Jayanti and the institute is closed. The week's records, cleaned by you, come back as SQL tables and pandas frames in Week 2, and the summary you built by hand today becomes one line of code you will already know the answer to.

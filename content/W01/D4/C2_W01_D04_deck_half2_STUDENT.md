# Half two: the segment summary, and the count it rests on

Week 1, Day 4. Slide source. One idea per slide.

Position bar, repeated at every section boundary:
`[one column] > [what is typical] > [what one order does] > [what the shape says] > [per segment, with denominators]`

---

## S1. Per segment, with denominators

Half one gave you one number for the whole file. Nobody runs a business unit on one number.

The question is always the same one level down: which part of Kalpa Retail is working, and how sure can you be.

---

## S2. Where we are

`[one column] > [what is typical] > [what one order does] > [what the shape says] > **[per segment, with denominators]**`

You can now pick an honest statistic for a column. Half two splits the file by segment, computes that statistic per group, and attaches the one thing that decides whether the answer means anything.

---

## S2b. The metric, named before it is computed

Kalpa Retail cares about returns. A returned order costs the delivery, the reverse logistics and usually the margin.

```
return rate  =  orders with status "returned"  /  all orders in the group
```

This is the first metric in the programme where **lower is better**. A ranking of return rates puts the best performer at the top with the smallest number beside it. Keep that straight or the next four slides will read backwards.

---

## S2c. Where this is going

```
segment        orders   median amount   return rate
Business            9        Rs 2,050          11.1%
Student            10        Rs 1,430          20.0%
Retail-Core        14        Rs 1,910          35.7%
Retail-Plus        11        Rs 1,435          36.4%
```

You will have built this inside the hour. Then you will spend the rest of the session refusing to send it as it stands.

---

## SECTION 1: THE DENOMINATOR

`[one column] > [what is typical] > [what one order does] > [what the shape says] > **[per segment, with denominators]**`

---

## S3. One rate, two files

Two segments in two different companies, same reported number:

```
segment X:   returned 5 of 12          41.7%
segment Y:   returned 500 of 1200      41.7%
```

Identical rates. Which one would you build a quarter's plan on?

---

## S4. Why the small one moves

In the 12-order segment, one order changing its status moves the rate by 8.3 points.

In the 1,200-order segment, one order moves it by 0.08 points.

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

Write it as `11.1 percent of 9` and nobody can misread it. Write it as `11.1 percent` and everybody will.

---

## SECTION 2: THE ACCUMULATOR

`[one column] > [what is typical] > [what one order does] > [what the shape says] > **[per segment, with denominators]**`

---

## S7. Counting into buckets

Monday you counted orders that passed a test. Today you count them into named piles, one pile per segment.

```
counts = {"Retail-Core": 0, "Retail-Plus": 0, "Business": 0}

for r in orders:
    counts[r["segment"]] = counts[r["segment"]] + 1
```

Reasonable code. The analyst listed the segments they remembered.

---

## S8. Run it

```
KeyError: 'Student'
```

It failed on the very first order in the file.

---

## S9. Reading it

`KeyError` means a dictionary was asked for a key it does not hold. The key it did not hold is printed for you: `Student`.

The dictionary held three segments because a person typed three segments. Kalpa Retail has four.

Every hard-coded list of categories is a promise about data you have not read yet.

This one is loud, because the first order in the file is a Student order. The dangerous version runs for six months and breaks the week a new segment launches.

---

## S10. Build the key when you first see it

```
counts = {}

for r in orders:
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
Business       9
Retail-Core   14
Retail-Plus   11
Student       10
      total   44
```

The total matches your profiled order count. If it did not, you would have a bug and the last line is how you would know.

One number here deserves a second look. Student holds ten. The raw file held twelve, and two Student orders were rejected yesterday for failing conversion. **Your cleaning changed the denominator of your smallest segment by seventeen percent**, and nothing in today's code would tell you. Yesterday's rejects log is the only place it is written down.

---

## SECTION 3: THE SEGMENT SUMMARY

`[one column] > [what is typical] > [what one order does] > [what the shape says] > **[per segment, with denominators]**`

---

## S12. Three accumulators, one pass

Per segment you need three things: how many orders, what a typical amount looks like, and what share came back.

```
per_segment[key] = {
    "count":    how many orders landed here,
    "amounts":  every amount, collected so the median can be taken at the end,
    "returned": how many had status "returned",
}
```

The median cannot be accumulated one order at a time. It needs the whole list sorted, so the list is collected during the pass and the median is taken after it.

---

## S13. The table

```
segment        orders   median amount   returned   rate
Business            9        Rs 2,050          1   11.1%
Retail-Core        14        Rs 1,910          5   35.7%
Retail-Plus        11        Rs 1,435          4   36.4%
Student            10        Rs 1,430          2   20.0%
```

Note what is absent from every row: the mean. Half one settled that.

---

## S14. Sort by rate, the way anyone would

```
Business      11.1%
Student       20.0%
Retail-Core   35.7%
Retail-Plus   36.4%
```

A clean ranking. Business returns at less than a third of the worst segment.

Somebody in a meeting is about to move budget towards Business.

---

## S15. Put the count back

```
Business      11.1%   on  9 orders
Student       20.0%   on 10 orders
Retail-Core   35.7%   on 14 orders
Retail-Plus   36.4%   on 11 orders
```

The top two performers are the two smallest segments in the file.

Business wins on nine orders.

---

## S16. One order

```
if 0 more Business orders had been returned:  11.1%   still best
if 1 more Business order  had been returned:  22.2%   no longer best
```

**One order** out of forty-four, in a segment of nine, and the best segment in the file is no longer the best segment in the file.

Small groups produce extreme rates in both directions, in any dataset, with nothing causing it. Rank groups by a rate and the smallest drift to both ends of the list, so the ranking reads group size as much as performance.

The fix is not a cleverer statistic. It is the column you already have.

---

## SECTION 4: THE HONEST SENTENCE

`[one column] > [what is typical] > [what one order does] > [what the shape says] > **[per segment, with denominators]**`

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
Business:    returned on 1 of 9 orders, 11.1 percent. Lowest in the file and the
             smallest segment in it. One more return takes it to 22.2 percent and
             behind Student, so this is not yet a finding.

Student:     returned on 2 of 10 orders, 20.0 percent. Ten orders, and the raw file
             held twelve before two failed conversion. Treat as unmeasured.

Retail-Core: returned on 5 of 14 orders, 35.7 percent. Largest segment and the
             steadiest number here. Median order Rs 1,910; the mean of Rs 36,027.14
             is the Rs 480,000 order and should not be quoted.

Retail-Plus: returned on 4 of 11 orders, 36.4 percent. Highest in the file, within
             one order of Retail-Core. The two are not separated by this data.
```

Two decline to make a claim and a third says two segments cannot be told apart. That is the sentence doing its job.

---

## S19. The convention this follows

Retail-Core's mean order value is Rs 36,027.14. Its median is Rs 1,910. One order separates those.

Reporting the median for money is the standing convention wherever a few very large values sit in a long tail, which is why national statistics report median household income. You applied it in half one to a column. Here it applies to a cell in a table somebody will screenshot.

---

## S20. The question you are not answering today

Is Business genuinely better than Retail-Plus, or is 11.1 against 36.4 what four groups of these sizes do on their own?

That question has a real answer and a method behind it, and it is Monday's session.

Today you name the question, write it in the notebook, and stop. Saying "we do not know yet, and here is what would tell us" is a complete professional answer.

---

## S21. The decision card

| Before you send a rate | Check |
|---|---|
| Is the denominator on the same line as the number | If not, it is not ready |
| Is any group under about 30 orders | Say so in the sentence, in words |
| Did you rank groups of very different sizes | Say what the ranking is partly measuring |
| Is a mean quoted on a money column | Replace it with the median |
| Is a difference being called real | Park it and name what would settle it |

---

## S22. Crux

> Every rate carries its denominator, or it lies for you while you are not in the room.
> The best-performing segment in this file is also the smallest, and one order takes the lead away.

Tomorrow is Gandhi Jayanti and the institute is closed. These same orders, cleaned by you, come back as SQL tables and pandas frames in Week 2, and the summary you built by hand today becomes one line of code you will already know the answer to.

# Half one: describe without misleading

Week 1, Day 4. Slide source. One idea per slide.

Position bar, repeated at every section boundary:
`[one column] > [what is typical] > [what one record does] > [what the shape says] > [per segment, with denominators]`

---

## S1. Describe without misleading

Yesterday you decided which records were usable. Today somebody asks you what they say.

The three questions this half answers: what is a typical value, what does one strange record do to that answer, and what shape is hiding behind the number you are about to send.

---

## S2. Where we are

`[one column] > [what is typical] > [what one record does] > [what the shape says] > [per segment, with denominators]`

You own a cleaned file and a decisions log. Every number today comes off that file and nothing else. Describing data you have not cleaned is yesterday's mistake, and this room already made it once on purpose.

---

## S2b. Where this is going

Two true claims about the same 47 records:

```
The average order is Rs 18,000.
Not one order in this file reached Rs 18,000, except a single order of Rs 480,000.
```

Both statements are correct. One of them would get you removed from the account.

By the end of this half you will know which number to send and what sentence has to go with it.

---

## S3. The anchor

Somebody outside your team asks a question you have heard a hundred times:

> What is the average order value?

It sounds like a request for one number. It is a request for a description of a shape, and the shape is what nobody has looked at yet.

---

## SECTION 1: WHAT IS TYPICAL

`[one column] > **[what is typical]** > [what one record does] > [what the shape says] > [per segment, with denominators]`

---

## S4. Seven values, on paper

The first seven records of your cleaned file, amount column only:

```
2000   3000   4000   4500   5000   6500   10000
```

Pens down on the keyboard. This one is done by hand.

---

## S5. Mean: add them up, share them out

```
2000 + 3000 + 4000 + 4500 + 5000 + 6500 + 10000 = 35000
35000 / 7 = 5000
```

The mean is Rs 5,000. It is the value every record would hold if the total were shared out equally.

It uses every record, which is its strength and the whole of its weakness.

---

## S6. Median: stand them in a line, take the middle one

```
2000   3000   4000   [4500]   5000   6500   10000
                       ^
                  4th of 7
```

The median is Rs 4,500. Half the records sit at or below it, half at or above it.

It uses the order of the records and almost nothing about their size.

---

## S7. Now change one record

The last value was Rs 10,000. Make it Rs 80,000. Nothing else changes.

| Statistic | Before | After |
|---|---|---|
| Mean | Rs 5,000 | Rs 15,000 |
| Median | Rs 4,500 | Rs 4,500 |

One record moved the mean by three times. The median did not move at all.

That is the entire day in one table.

---

## S8. Mode: the value that shows up most

In your 47 records, the most common amount is Rs 4,500. It appears three times.

Three times out of 47. It describes six percent of the file and nothing else.

Mode earns its keep on categories, where "the most common segment" is a real answer. On a money column it is close to useless, and knowing why is more valuable than knowing the definition.

---

## S9. Three answers, three questions

| Statistic | The question it actually answers |
|---|---|
| Mean | If the total were shared equally, what would each record hold |
| Median | What does the record in the middle of the queue look like |
| Mode | Which exact value repeats most often |

Nobody is right. They answer different questions, and the asker rarely says which one they meant.

---

## SECTION 2: WHAT ONE RECORD DOES

`[one column] > [what is typical] > **[what one record does]** > [what the shape says] > [per segment, with denominators]`

---

## S10. The same code, on the real column

You just did this by hand on seven values. Here it is on all 47.

```
mean amount over 47 records: Rs 18000.00
```

The code is correct. Check it if you like. Add them, divide by 47, you get Rs 18,000.

---

## S11. Two more lines, and the number falls apart

```
mean amount over 47 records: Rs 18000.00
records at or above Rs 18000.00: 1
records below Rs 18000.00: 46
```

The average describes one record out of 47.

Forty-six people in this file are below the number you were about to call typical.

---

## S12. Sort the column and look at the tail

```
... 13000   13600   14200   14800   15600   17400   480000
```

There it is.

The second largest order in the entire file is Rs 17,400. The largest is Rs 480,000, which is 27 times the one below it.

---

## S13. The whale

One record, Rs 480,000, in `segment_b`.

It is not a typo, not a text value, not a duplicate. Yesterday's cleaning pass looked at it and kept it, because it is a real order that a real customer really placed.

A record can be correct and still wreck every summary it touches.

---

## S14. What it costs, in two rows

| Column | With the whale | Without it |
|---|---|---|
| All 47 records, mean | Rs 18,000.00 | Rs 7,956.52 |
| All 47 records, median | Rs 7,500 | Rs 7,300 |
| `segment_b` mean, 9 records | Rs 60,255.56 | Rs 7,787.50 |

Removing one record out of nine moves that segment's mean by a factor of nearly eight. The median barely twitches anywhere.

---

## S15. So delete it?

No.

Deleting a real record to make a number look nicer is how a report becomes fiction. Yesterday you wrote a decisions log precisely so that nobody could do this quietly.

The record stays. The statistic changes.

---

## S16. The rule for money columns

> On any money column, report the median and say so.

This is not this programme's opinion. Statistical agencies report median household income rather than mean household income, because a small number of very large incomes drag the mean away from anything a household would recognise.

Order values behave the same way. So do salaries, claim sizes, invoice amounts and basket totals.

---

## SECTION 3: WHAT THE SPREAD SAYS

`[one column] > [what is typical] > [what one record does] > **[what the shape says]** > [per segment, with denominators]`

---

## S17. Three numbers you get for free

```
min:    Rs 1,800
max:    Rs 480,000
range:  Rs 478,200
```

The range is one subtraction and it is the least stable number on this slide. It is built from exactly two records, and one of them is the whale.

A statistic computed from two records out of 47 tells you about those two records.

---

## S18. The fence, met again

Yesterday you flagged an outlier by sorting and looking at the tail. Here is the same idea with a rule attached, so it runs without you.

```
Q1 (a quarter of the way up):        Rs 4,800
Q3 (three quarters of the way up):   Rs 10,900
IQR = Q3 - Q1 =                      Rs 6,100
upper fence = Q3 + 1.5 x IQR =       Rs 20,050
```

---

## S19. What the fence catches here

```
records above Rs 20,050: 1
```

One record. The whale, and nothing else. The highest ordinary order at Rs 17,400 sits comfortably inside the fence.

The fence did in one line what the room did by eye on S12. That is the point of writing a rule down.

---

## S20. A fence is a flag, never a delete key

The fence says "look at this record". It does not say "remove this record".

Yesterday's language holds: an outlier is a finding to investigate before it is a row to delete. The fence just finds it faster.

---

## SECTION 4: THE SHAPE BEHIND THE NUMBER

`[one column] > [what is typical] > [what one record does] > **[what the shape says]** > [per segment, with denominators]`

---

## S21. Skew, without a formula

Sort the column. Stand on the median. Look both ways.

```
min        median                                          max
1800        7500                                        480000
 |------------|-------------------------------------------|
   5,700 down                472,500 up
```

The distance up is 83 times the distance down. That lopsidedness is the skew, and you read it off sorted values with no arithmetic beyond one subtraction each way.

---

## S22. The tell you can use in any interview

> If the mean is much larger than the median, something large is pulling on the right.
> If the mean is much smaller, something small is pulling on the left.
> If they sit close together, the shape is roughly even and either one describes it.

On this file: mean Rs 18,000, median Rs 7,500. The mean is 2.4 times the median, so you already know there is a tail before you look at a single record.

---

## S23. Anscombe's quartet, 1973

Frank Anscombe built four datasets that share almost identical means, variances and correlations, and look nothing alike when drawn.

The lesson he was making has not aged: a summary statistic is a compression, and compression discards. Two datasets can hand you the same numbers and describe two different worlds.

You have no charting library until Week 2, so today the sorted list is your picture. Look at it before you trust the summary.

---

## S24. The decision card

| The column looks like | Send | Say alongside |
|---|---|---|
| Money, or anything with a long tail | Median | The count it rests on |
| Roughly even, no extreme values | Mean is fine | The count it rests on |
| A category, such as segment or status | Mode, as "the most common" | The count it rests on |
| You have not sorted it yet | Nothing | Sort it first |

The right-hand column is the same in every row. That is half two's subject.

---

## S25. The failure you will meet again

Not a crash. Correct code, correct arithmetic, and a description that misleads a person who trusted you.

Nothing in a traceback catches this. The only thing that catches it is looking at the shape before you send the number.

---

## S26. Crux

> The mean was right and the description was wrong.
> On a money column, send the median, and say that is what you sent.

And never send a number without the count it rests on.

Half two: the count it rests on.

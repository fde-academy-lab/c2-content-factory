# Half one: describe without misleading

Week 1, Day 4. Slide source. One idea per slide.

Position bar, repeated at every section boundary:
`[one column] > [what is typical] > [what one order does] > [what the shape says] > [per segment, with denominators]`

---

## S1. Describe without misleading

Yesterday you decided which of Kalpa's fifty orders were usable. Today somebody asks what they say.

The three questions this half answers: what is a typical order, what does one strange order do to that answer, and what shape is hiding behind the number you are about to send.

---

## S2. Where we are

`[one column] > [what is typical] > [what one order does] > [what the shape says] > [per segment, with denominators]`

You own a profiled file and a decisions log. Every number today comes off that file and nothing else. Describing data you have not cleaned is yesterday's mistake, and this room already made it once on purpose.

Two things you inherited and should keep in view: `KR4201` still appears twice, because you chose to keep both rows and flag the pair. Student held twelve orders in the raw file and holds ten now, because two failed conversion.

---

## S2b. Where this is going

Two true statements about the same 44 orders:

```
The average Kalpa order is Rs 12,753.30.
Forty-three of the forty-four orders are below Rs 3,000.
```

Both are correct. One of them would get you removed from the account.

By the end of this half you will know which number to send and what sentence has to go with it.

---

## S3. The anchor

Somebody outside your team asks a question you have heard a hundred times:

> What is our average order value?

It sounds like a request for one number. It is a request for a description of a shape, and the shape is what nobody has looked at yet.

---

## SECTION 1: WHAT IS TYPICAL

`[one column] > **[what is typical]** > [what one order does] > [what the shape says] > [per segment, with denominators]`

---

## S4. Seven orders, on paper

The first seven orders in your profiled file, amount column only:

```
1280   1865   2270   2835   1310   1145   1030
```

Pens down on the keyboard. This one is done by hand.

---

## S5. Mean: add them up, share them out

```
1280 + 1865 + 2270 + 2835 + 1310 + 1145 + 1030 = 11735
11735 / 7 = 1676.43
```

The mean is Rs 1,676.43. It is the value every order would carry if the total were shared out equally.

It uses every order, which is its strength and the whole of its weakness.

---

## S6. Median: stand them in a line, take the middle one

```
1030   1145   1280   [1310]   1865   2270   2835
                       ^
                  4th of 7
```

The median is Rs 1,310. Half the orders sit at or below it, half at or above it.

It uses the order of the records and almost nothing about their size.

---

## S7. Now swap one order

Keep the same seven. Replace the largest, Rs 2,835, with the largest order in the real file: Rs 480,000.

| Statistic | Before | After |
|---|---|---|
| Mean | Rs 1,676.43 | Rs 69,842.86 |
| Median | Rs 1,310 | Rs 1,310 |

One order moved the mean by nearly forty-two times. The median did not move at all.

That is the entire day in one table.

---

## S8. Mode: the value that shows up most

In your 44 orders, the most repeated amount appears **twice**.

Twice out of forty-four. It describes four percent of the file and nothing else.

Mode earns its keep on categories, where "the most common segment" or "the most common status" is a real answer. On a money column it is close to useless, and knowing why is more valuable than knowing the definition.

---

## S9. Three answers, three questions

| Statistic | The question it actually answers |
|---|---|
| Mean | If the total were shared equally, what would each order carry |
| Median | What does the order in the middle of the queue look like |
| Mode | Which exact value repeats most often |

Nobody is right. They answer different questions, and the asker rarely says which one they meant.

---

## SECTION 2: WHAT ONE ORDER DOES

`[one column] > [what is typical] > **[what one order does]** > [what the shape says] > [per segment, with denominators]`

---

## S10. The same code, on the real column

You just did this by hand on seven orders. Here it is on all 44.

```
mean amount over 44 orders: Rs 12,753.30
```

The code is correct. Check it if you like. Add them, divide by 44, you get Rs 12,753.30.

---

## S11. Two more lines, and the number falls apart

```
mean amount over 44 orders: Rs 12,753.30
orders at or above Rs 12,753.30: 1
orders below Rs 12,753.30: 43
```

The average describes one order out of forty-four.

Forty-three of Kalpa's customers are below the number you were about to call typical.

---

## S12. Sort the column and look at the tail

```
... 2,855   2,895   2,895   2,930   2,990   2,995   480,000
```

There it is.

The second largest order in the entire file is Rs 2,995. The largest is Rs 480,000, which is a hundred and sixty times the one below it.

---

## S13. The whale

```
KR4232   C1749   Retail-Core   480000   delivered   2026-08-19
```

One order. It carries **85.5 percent of every rupee in the file**.

It is not a typo, not a text value, not a duplicate. Yesterday's pass looked at it and kept it, and the decisions log says why: it converts cleanly and is well formed, so it is real until somebody says otherwise, and it was raised with the order book owner.

An order can be correct and still wreck every summary it touches.

---

## S14. What it costs, in two rows

| Column | With the whale | Without it |
|---|---|---|
| All orders, mean | Rs 12,753.30 | Rs 1,887.09 |
| All orders, median | Rs 1,910.00 | Rs 1,865.00 |

Take one order out of forty-four and the mean falls by a factor of nearly seven, landing within Rs 22 of the median. The median moves by Rs 45.

**That is the tell.** When removing a single record makes the mean and the median agree, the mean was describing that record rather than the business.

---

## S15. So delete it?

No.

Deleting a real order to make a number look nicer is how a report becomes fiction. Yesterday you wrote a decisions log precisely so that nobody could do this quietly.

The order stays. The statistic changes.

---

## S16. The rule for money columns

> On any money column, report the median and say so.

This is not this programme's opinion. Statistical agencies report median household income rather than mean household income, because a small number of very large incomes drag the mean away from anything a household would recognise.

Order values behave the same way. So do salaries, claim sizes, invoice amounts and basket totals.

---

## SECTION 3: WHAT THE SPREAD SAYS

`[one column] > [what is typical] > [what one order does] > **[what the shape says]** > [per segment, with denominators]`

---

## S17. Three numbers you get for free

```
min:    Rs      800
max:    Rs  480,000
range:  Rs  479,200
```

The range is one subtraction and the least stable number on this slide. It is built from exactly two orders out of forty-four, and one of them is the whale.

A statistic computed from two orders out of forty-four tells you about those two orders.

---

## S18. The fence, done properly

Yesterday you flagged the whale with a fence at ten times the middle order. That worked and it was deliberately crude, because somebody chose the ten.

Here is the standard version, built from the spread of the middle half rather than from a number anybody picked.

```
Q1 (a quarter of the way up):        Rs  1,287.50
Q3 (three quarters of the way up):   Rs  2,718.75
IQR = Q3 - Q1 =                      Rs  1,431.25
upper fence = Q3 + 1.5 x IQR =       Rs  4,865.62
```

---

## S19. What the fence catches here

```
orders above Rs 4,865.62: 1
```

One order. The whale, and nothing else. The largest ordinary order at Rs 2,995 sits comfortably inside the fence.

Two rules, built differently, agreeing on the same single record. That agreement is worth more than either rule alone.

---

## S20. A fence is a flag, never a delete key

The fence says "look at this order". It does not say "remove this order".

Yesterday's language holds: an outlier is a finding to investigate before it is a row to delete. The fence just finds it faster, on a file too large to eyeball.

---

## SECTION 4: THE SHAPE BEHIND THE NUMBER

`[one column] > [what is typical] > [what one order does] > **[what the shape says]** > [per segment, with denominators]`

---

## S21. Skew, without a formula

Sort the column. Stand on the median. Look both ways.

```
 min      median                                            max
  800      1,910                                        480,000
   |---------|-----------------------------------------------|
    1,110 down                478,090 up
```

The distance up is 431 times the distance down. That lopsidedness is the skew, and you read it off sorted values with no arithmetic beyond one subtraction each way.

---

## S22. The tell you can use in any interview

> If the mean is much larger than the median, something large is pulling on the right.
> If the mean is much smaller, something small is pulling on the left.
> If they sit close together, the shape is roughly even and either one describes it.

On this file: mean Rs 12,753.30, median Rs 1,910.00. The mean is 6.68 times the median, so you already know there is a tail before you look at a single order.

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

# Which answers hold in the chapter 3 set on which segment carried the fall and how often it ordered, and why?

Answers: 1b 2d 3a 4c 5b

Kalpa Retail's booked revenue fell 1.6 percent from Q1 to Q2, and chapter 3 split it by segment with
one grouped query: eight rows, one per segment and quarter. Business books about 99 percent of the
rupees; Retail-Plus's revenue fell 29.4 percent and its orders fell from 215 to 140, 75 of the book's
76 fewer orders. Orders per customer came out as whole numbers until the division was done in numeric
and rounded on purpose: Retail-Plus went from 2.36 to 1.84, down 22.0 percent. The set carries those
habits to new groups and new numbers. Two of the five items are design items: 1 and 4.

**Who needs the answer.** You, checking your five letters after the lab or tonight. The head of
Retail-Plus spends a retention budget on these lines, and a frequency nobody multiplied back is how
that budget goes to the wrong segment.

**The questions on the way.**

- Which idea does this set test?
- Why is each key right, item by item?
- Which wrong answer is worth arguing about?
- Where does this show up at work?

## Which idea does this set test?

One grouped query answers every group at once, and every ratio it prints must multiply back to the
counts it came from. The design items choose the way to produce a new cut of the book, sized in rows,
and the second route that could catch a wrong count behind a ratio. The other items predict which
groups a HAVING flag returns, correct a sheet of whole-number ratios, and choose the one line that
says where a company-wide fall came from.

## Why is each key right, item by item?

### Q1. Which way produces every channel and status line each quarter, and how many rows does it return?

Kind: a design item, the best-fit way with its size. Three channels, three statuses and two quarters,
with orders in every pairing.

The key is b, "One query grouped by channel, status and quarter, returning 18 rows". Three channels
times three statuses times two quarters is 18 groups, and one grouped query returns one row for each.
A status or channel added to the warehouse later appears as new rows on the next run without anyone
editing the query.

- a, "One query per channel and status, nine queries returning 18 rows between them": the rows come
  out right today, and a status added later is silently missing, because no query was written for
  it.
- c, "One query grouped by channel and status, returning 9 rows": leaves the quarter out of the
  grouping, so Q1 and Q2 merge and no change can be read.
- d, "The 1,000 order rows pulled into pandas and grouped there, returning 18 rows": the result is the
  same, after moving 1,000 rows out of the warehouse for an answer of 18, which Anand's rule against
  exports forbids.

### Q2. Which segment-quarters come back when the flag's bar rises to 40 customers?

Kind: predict the output from the table. The flag keeps the groups whose distinct customers number
fewer than 40.

The key is d, "Business and Student in both quarters, four groups". Business stands on 36 and 35
customers and Student on 15 and 20, all under 40; Retail-Core (102 and 96) and Retail-Plus (91 and 76)
clear the bar. Business books about 99 percent of the rupees on fewer than 40 customers a quarter,
which is why its rates earn the flag.

- a, "Student in both quarters, the two groups with fewer than 40 orders": counts orders (27 and 38),
  which is `count(*)`, where the flag counts distinct customers.
- b, "Student in both quarters, the two groups with fewer than 30 customers": the answer at the old
  bar of 30, which misses Business's 36 and 35.
- c, "Business in both quarters, since its 99 percent of the rupees rests on few orders": rupees and
  orders decide nothing here, and Student sits under the bar as well.

### Q3. What should the sheet show for Surat's orders per customer, and how does Surat compare with Pune?

Kind: fix the logic, on invented numbers. The hurried column divided two whole-number counts.

The key is a, "1.81, so Pune's 2.25 is about 24 percent higher, where the sheet said double". Postgres
divides two whole numbers as whole numbers and drops the remainder, so 38 over 21 printed as 1. In
numeric, Surat is 38 / 21 = 1.81 and Pune 45 / 20 = 2.25, and 2.25 over 1.81 is 1.24. The printed 1
multiplies back to 21 orders, 17 short of 38, which is how the analyst catches it.

- b, "1, as printed, so Surat's customers order half as often as Pune's customers do": trusts a ratio
  that multiplies back to 21 of Surat's 38 orders.
- c, "2, rounded up from 1.81, so Surat and Pune order equally often": rounding to a whole number
  erases the 24 percent gap the sheet exists to show.
- d, "0.55, customers per order, which states the same fact the other way round": divides the wrong
  way; nobody on the sheet reads customers per order, and it breaks the tree's branch.

### Q4. Which route confirms Retail-Core's 2.01 orders per customer in a way that could catch a wrong count?

Kind: a design item, the independent second route with its size. Retail-Core booked 193 Q2 orders
from 96 customers.

The key is c, "One row per Retail-Core customer in Q2 with their order count, 96 rows averaged in
Python". Each row is one customer's own orders, so the average of the 96 counts is orders per customer
reached without the query's division; on the book it gives 2.01. A wrong customer count would show up
as a different number of rows or a different average.

- a, "Multiply 2.01 by the 96 customers and set the product beside the 193 orders, moving no rows":
  a sound check on the division, and it reuses the same two counts, so a wrong count would still
  multiply back.
- b, "Rerun the grouped query with the division rounded to three places instead of two, one row": the
  same query with a different rounding repeats whatever it got wrong.
- d, "Divide Retail-Core's Q2 revenue by its revenue per order, one row": gives back the 193 orders, a
  different leaf, and says nothing about the customers.

### Q5. Which line tells Anand which segment carried the fall?

Kind: choose the line for the sheet. The book fell Rs 16,00,000; Business fell Rs 14,29,840,
Retail-Core Rs 6,820 and Retail-Plus Rs 1,72,390, while Student rose Rs 9,050.

The key is b, "Business carried most of the rupees of the fall, and Retail-Plus 75 of the 76 fewer
orders". Business's fall of Rs 14,29,840 is about 89 percent of the book's Rs 16,00,000, and Business
is only 1.4 percent down on its own base. Retail-Plus lost 75 of the book's 76 fewer orders and 29.4
percent of its revenue. The honest line names both, because the question has a rupee answer and an
order answer.

- a, "Retail-Plus carried the fall, since its revenue fell 29.4 percent, the most of any segment": the
  steepest rate, on a segment worth about Rs 5.9 lakh a quarter, carries about 11 percent of the
  rupees that fell.
- c, "Student offset the fall, since its revenue rose 33.9 percent while the book's revenue fell 1.6
  percent": Student's rise is Rs 9,050 on 20 customers, a flagged rate that offsets well under 1
  percent of the fall.
- d, "No segment carried it, since the book's revenue fell only 1.6 percent overall": a small total
  change can hide a large one inside it, as Retail-Plus's 29.4 percent shows.

## Which wrong answer is worth arguing about?

Item 5, option a. The head of Retail-Plus may say option a is the line that matters, since a 29.4
percent fall in the paid tier is the alarm and Business's 1.4 percent is noise on a large base. That
reading is fair for her decision. Anand's sheet serves Finance as well, and Finance reads rupees:
nearly nine rupees in ten of the fall came from Business. A line that names only one of the two sends
one reader away with half the story.

## Where does this show up at work?

Eternal, the group behind Zomato and Blinkit, reported consumer net order value up 54 percent year on
year in its shareholders' letter of 22 July 2026, and the same letter splits it: food delivery a
little over 20 percent, quick commerce 86 percent, going-out 60 percent. A group-wide number is
several stories added together, and every business review asks the question in item 5.

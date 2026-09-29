# Round 3 set: predict the shape, then read the view

Fifteen minutes, alone, after round 3. Items 1 to 4 are the mid-session drill: predict the shape
of each call on the warehouse's tables before you run it, then run it. `orders` holds 1,000 rows
from 301 customers across four segments, two quarters and six months; `plus` holds the 355
Retail-Plus orders from 107 members; `orders` carries a `month` column and `segment` from the
customer table.

Post one line, seven letters in item order, no spaces:

```
Post exactly this shape: xxxxxxx
```

---

### Q1

The head of Retail-Plus asks for revenue per segment. What shape is
`orders.groupby("segment")["amount"].sum()`?

a) 1,000 values, one per order, each replaced by its segment's total
b) 301 values, one per customer who ordered
c) 340 values, one per customer on the list
d) 4 values, one per segment

### Q2

Anand wants orders and revenue per segment per quarter. What shape is
`orders.groupby(["segment", "quarter"]).agg(orders=("order_id", "count"), revenue=("amount", "sum"))`?

a) 4 rows by 4 columns, a segment per row and a measure per quarter
b) 8 rows by 2 columns, one row per segment and quarter pair
c) 2 rows by 8 columns, one row per quarter
d) 1,000 rows by 2 columns, the measures written onto every order

### Q3

The head of Retail-Plus wants each member's Q1 and Q2 side by side. What shape is
`plus.pivot_table(index="customer_id", columns="quarter", values="amount", aggfunc="sum")`?

a) 107 rows by 2 columns
b) 120 rows by 2 columns, every member on the list
c) 2 rows by 107 columns, a row per quarter
d) 355 rows by 2 columns, a row per order

### Q4

The growth team's slide wants months down the side and segments across the top. What shape is
`orders.pivot_table(index="month", columns="segment", values="amount", aggfunc="sum")`?

a) 4 rows by 6 columns, a segment per row and a month per column
b) 24 rows by 1 column, a row per month and segment pair
c) 6 rows by 4 columns
d) 6 rows by 1 column, the months with their book totals

### Q5

The head of Student asks whether the segment grew from Q1 to Q2. One analyst's pivot, with the
default `aggfunc`, reports a rise of 27 percent; another's, with `aggfunc="sum"`, a rise of 34
percent. Which number goes to the head of Student, and why?

a) 27 percent, because the average order is the fairer measure of how a segment is doing
b) Either, because both pivots agree the segment grew and the direction is what matters
c) 34 percent: growth is total spend, and the mean hides how often members bought
d) Neither, until the two pivots agree, because one of them must have a bug

### Q6

The member view `wide` is 107 rows by 6 months, with empty months written as 0. How many rows
does `wide.reset_index().melt(id_vars="customer_id", var_name="month", value_name="spend")`
return, for the trend chart?

a) 642, one per member per month, zeros included
b) 266, one per member-month that had orders, as in the long table
c) 107, one per member, since melt undoes the pivot row by row
d) 6, one per month, since the trend chart needs one point a month

### Q7

The head of Retail-Plus says: "I want to read along a row and see who is drifting." Which view
answers her, and what check goes with it?

a) Months as rows and segments as columns, checked against Monday's book total
b) A row per member and a column per month, summed, with a grand total equal to her orders
c) A row per order and a column per month, since every order then shows
d) The long table sorted by spend, since the biggest members are the ones that matter most to her

# Self-check: know you are right before Friday

Every checkpoint is something you verify alone, on the staging snapshot. If one fails, the fix
is named beside it.

---

## Part 1 and 2, the numbers

| # | Checkpoint | What you should see | If it does not match |
|---|---|---|---|
| 1 | Rows in the table | 340 | 309 means the table was built from the orders; start from the customer list |
| 2 | Spend | Rs 19,84,00,000, equal to the snapshot's orders | More than that means the exposure merge multiplied some customers' rows |
| 3 | As-of date | 28 September 2026 | Any later date is the wall clock; use the orders' last date |
| 4 | Smallest recency | 0 days | 21 or more means recency from a run day |
| 5 | Customers with no orders | 31, with frequency 0 and no recency | NaN in frequency means the zeros were never filled |
| 6 | Customers the sale reached | 153 | A larger number means a customer is counted once per feed row |
| 7 | Of those, customers who bought | 142 | 142 bought out of 142, 100 percent, means the reached customers with no orders lost their segment and were dropped |
| 8 | The 60-day win-back list | 123 | 162 is the list measured from Monday 19 October |

## Part 3, the counts behind the threshold

| Threshold | Customers on the list |
|---|---|
| 45 days | 150 |
| 60 days | 123 |
| 90 days | 77 |

Any of the three can be defended. The defence is marked by whether each sentence carries a
number and a cost.

## Part 4, the two tools

| Quarter | Orders | Members | Orders per member |
|---|---|---|---|
| Q1 | 215 | 98 | 2.194 |
| Q2 | 140 | 75 | 1.867 |

1.000 in either tool means members were counted once per order: a list instead of a set in the
loop, or `count` instead of `nunique` in pandas.

## Part 5, the months views

| Segment | Q1 | Q2 | Change |
|---|---|---|---|
| Retail-Plus | Rs 6,12,880 | Rs 3,89,970 | a fall of 36.4 percent |
| Retail-Core | Rs 3,90,870 | Rs 3,59,120 | a fall of 8.1 percent |

A Retail-Plus fall near 31 percent, or a Retail-Core fall near 11 percent, means the pivot
averaged: write `aggfunc="sum"`.

---

## The questions to ask your own notebook

1. Does it run from a fresh kernel, top to bottom, with every guard in the function?
2. Is the as-of date in the table itself, where Marketing can read it?
3. Does every number in Part 3 carry its threshold and its count?
4. Did you paste outputs in Parts 1 and 4, rather than describe them?

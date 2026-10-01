# Which segment carries Kalpa's revenue, and which leaf of the tree separates the segments?

Chapter 1 set, six items, after chapter 1: items 1 and 2 run live in the chapter's last three
minutes; the rest are the practice lab's stretch or tonight's work.

> "Monday's growth review deck needs three things I can open on my laptop without a login: the
> revenue tree by segment for both quarters, the top-fifty protect list with a lookup so I can find
> any member by id, and one number on the front page with its trend. Nothing that needs Python. If a
> director changes an assumption in the room, the sheet must recalculate in front of them."
>
> Meera's chief of staff, Kalpa Retail

Kalpa Retail sells to four segments: Retail-Core, its everyday shoppers; Retail-Plus, its paid
membership tier; Business, corporate buyers invoiced in large amounts; and Student. The customer
table the team exported on Thursday holds one row per customer who ordered between April and
September 2026, with that customer's segment, city, orders and revenue added up over the half-year.
Revenue here is booked order value in rupees, every order at the price charged. The revenue tree
splits a segment's revenue into three leaves that multiply back to it: customers, orders per
customer, and revenue per order. A PivotTable is Excel's grid that adds a column's values for each
group and re-slices when another column is dragged in; it recalculates when someone presses Refresh.
SUMIFS adds the values in a range whose rows meet the conditions given, COUNTIFS counts those rows,
and both recalculate the moment a cell they read changes. Kavya Nair, the senior analyst on the team,
reviews every line before it reaches the deck.

**Who needs the answer.** Meera's chief of staff puts the tree by segment on page two of Monday's
growth review deck, and the directors decide from it which segment the growth plan talks about. A
leaf computed the wrong way puts a tree on the page that does not multiply back to its own revenue,
and the first director who checks the arithmetic stops trusting every page after it.

**The questions on the way.**

- How many formulas does a SUMIFS grid need once a director asks for the tree by city as well?
- Which leaf carries most of the gap between a Retail-Plus member's spend and a Retail-Core shopper's?
- What does an averaged revenue-per-order column read for three invented customers?
- Which fact would favour a grid of SUMIFS formulas over a PivotTable for the tree itself?
- What happens to Q2 when the customer table is split on each customer's last order date?
- Which check can disagree with the pivot when the pivot is wrong?

Every number in item 3 is invented; items 1, 2 and 5 use the customer table's own shape and
numbers, and items 4 and 6 use none.

Post one line of six letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxxx
```

---

### Q1. How many formulas does a SUMIFS grid need once a director asks for the tree by city as well, and which way should the tree go to the room?

The tree by segment needs three measures (customers, orders and revenue) for each of the four
segments, one COUNTIFS or SUMIFS per cell. The chief of staff warns that a director will ask for
the same tree for each of Kalpa's six cities, and nobody knows which column a director will ask
for after that. How many formulas does the grid need in all, and which way should the tree go to
the room?

a) 12 formulas, so the SUMIFS grid goes, since it stays small and recalculates at once
b) 84 formulas, and the SUMIFS grid goes, since every cell in it recalculates at once
c) 84 formulas, and a PivotTable goes, since it re-slices on any column asked for
d) 72 formulas, and pasted values go, since the city split is now known in advance

### Q2. Which leaf carries most of the gap between a Retail-Plus member's spend and a Retail-Core shopper's?

From the customer table: Retail-Core has 131 customers, 392 orders and Rs 7,39,320 of revenue;
Retail-Plus has 106 customers, 349 orders and Rs 9,77,410. A Retail-Plus member spends Rs 9,221
across the half-year against a Retail-Core shopper's Rs 5,644. Which leaf carries most of that gap?

a) Customers, since Retail-Core has 25 more of them than Retail-Plus does
b) Orders per customer, since members of a paid tier come back more often
c) Revenue per customer, since it is the leaf the tree splits by segment
d) Revenue per order, since members fill a bigger basket on each visit

### Q3. What does an averaged revenue-per-order column read for three invented customers, and what does the tree need?

An invented segment has three customers. Customer A placed one order of Rs 9,00,000, customer B one
order of Rs 3,00,000, and customer C ten orders of Rs 1,00,000 each. A hurried analyst adds a
column `=revenue/orders` beside each customer and drags it into the pivot's Values, first as Sum,
Excel's default for numbers, and then as Average. What does the Average read, and what revenue per
order does the tree need?

a) Rs 4,33,333 on the pivot, and the tree needs Rs 1,83,333
b) Rs 1,83,333, since an Average of the column and a ratio of sums agree
c) Rs 13,00,000, the Sum, and the tree needs Rs 4,33,333
d) Rs 4,33,333 on the pivot, and the tree needs Rs 4,33,333 too

### Q4. Which fact would favour a grid of SUMIFS formulas over a PivotTable for the tree itself?

The chief of staff's ask says the sheet must recalculate when a director changes an assumption. So
far every assumption the directors have raised sits in its own input cell beside the tree, and the
tree's twelve cells read none of them. Which fact, if it turned out to be true on Monday, would
favour a grid of SUMIFS formulas over a PivotTable for the tree itself?

a) The table grows from 300 rows to 3,000 rows before Monday's first refresh
b) A director's typed assumption must move the tree's own cells at once
c) A director wants the tree sliced by city as well as by segment, in the room
d) The deck has to open on a laptop that has no login to the warehouse

### Q5. What happens to Q2 when the customer table is split on each customer's last order date?

A colleague wants the tree for both quarters, Q1 (April to June 2026) and Q2 (July to September
2026), from the customer table, whose only date column, last_order_date, holds the date of each
customer's most recent order. They put each customer's whole half-year revenue in Q1 or Q2 by that
date. What happens to Q2?

a) It reads too high, since a customer who bought in both lands wholly in Q2
b) It reads too low, since the latest orders in a half-year tend to be the smallest
c) It reads right, since each customer's revenue lands in exactly one quarter
d) It reads right for Business, and too low for the three consumer segments

### Q6. Which check can disagree with the pivot when the pivot is wrong?

A second route reaches the same numbers by a method that shares none of the first one's steps, so it
can fail when the first is wrong. Which of these is a second route for the pivot's twelve cells:
customers, orders and revenue for each of the four segments?

a) A second PivotTable on the same table, with the fields dragged in another order
b) The pivot's grand total compared with the sum of its own four segment rows
c) A COUNTIF and two SUMIFS per segment, beside the pivot, on the table's own cells
d) A SUM of the table's whole revenue column, compared with the pivot's grand total

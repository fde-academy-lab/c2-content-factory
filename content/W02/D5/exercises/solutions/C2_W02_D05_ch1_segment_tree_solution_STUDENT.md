# Which answers hold in the chapter 1 set on which segment carries Kalpa's revenue, and why?

Answers: 1c 2d 3a 4b 5a 6c

Meera's chief of staff asked for the revenue tree by segment on page two of Monday's growth review
deck, in a file that opens without a login and recalculates when a director changes an assumption.
The customer table holds one row per customer who ordered between April and September 2026, with
orders and revenue added up over the half-year; revenue is booked order value in rupees. The tree
splits a segment's revenue into customers, orders per customer and revenue per order, three leaves
that multiply back to it. A PivotTable adds a column per group and recalculates on Refresh; SUMIFS
and COUNTIFS recalculate at once. Chapter 1 found that Business, 39 corporate buyers, carries 99.1
percent of the half-year's revenue, and that a bigger basket separates Retail-Plus, the paid
tier, from Retail-Core. Three of the six items are design items: 1, 4 and 6.

**Who needs the answer.** You, checking your six letters after the lab or tonight. A letter picked
for the wrong reason carries that reason into the tree on page two, where Kavya Nair, the senior
analyst who reviews every line, multiplies the leaves back and sends it home.

**The questions on the way.**

- Which skill does the chapter 1 set test?
- Why does each of the six keys hold, from the formula count to the second route?
- Why is the averaged leaf (item 3, d) the most tempting wrong answer?
- Where does Costco face the same question about its paid tier?

## Which skill does the chapter 1 set test?

The skill is building a tree that multiplies back to the revenue it explains, which happens only when
every leaf is a ratio of two sums: orders over customers, revenue over orders. The design items ask how the
tree should reach a director (a pivot that re-slices, or formulas that recalculate the moment an
input changes), which fact would switch that call, and which second route could catch the pivot when
it is wrong. The other items ask the room to read the leaves, to see what an average of ratios does,
and to see why a table with one row per customer cannot split two quarters.

## Why does each of the six keys hold, from the formula count to the second route?

### Q1. How many formulas does a SUMIFS grid need once a director asks for the tree by city as well, and which way should the tree go to the room?

A design item. The tree needs three measures for four segments, one formula a cell, and a director
will ask for the same tree in each of six cities, then for a column nobody can name in advance.

The key is c, "84 formulas, and a PivotTable goes, since it re-slices on any column asked for". The segment grid is 4 times 3, 12 formulas; the city split adds 6 times 4 times 3, 72 more,
84 in all, and the next column a director asks for adds another grid. A PivotTable answers any slice
by a drag, which is what a director does in the room.

- a, "12 formulas, so the SUMIFS grid goes, since it stays small and recalculates at once": counts
  only the segment grid and forgets the six cities the chief of staff warned about.
- b, "84 formulas, and the SUMIFS grid goes, since every cell in it recalculates at once": the count
  is right, and the call is wrong, because a grid only answers the slices someone built before the
  meeting.
- d, "72 formulas, and pasted values go, since the city split is now known in advance": 72 is what
  the city split adds, not the total, and pasted values answer no question a director asks next.

### Q2. Which leaf carries most of the gap between a Retail-Plus member's spend and a Retail-Core shopper's?

Retail-Core has 131 customers, 392 orders and Rs 7,39,320; Retail-Plus has 106 customers, 349 orders
and Rs 9,77,410.

The key is d, "Revenue per order, since members fill a bigger basket on each visit". Orders per
customer are 349 over 106, 3.29, against 392 over 131, 2.99, which is 10 percent more. Revenue per
order is Rs 9,77,410 over 349, Rs 2,801, against Rs 7,39,320 over 392, Rs 1,886, which is 48.5
percent more. The basket carries most of the 63 percent gap in spend per customer.

- a, "Customers, since Retail-Core has 25 more of them than Retail-Plus does": the number of
  customers explains a segment's total, and the question is about spend per customer.
- b, "Orders per customer, since members of a paid tier come back more often": they do, by 10
  percent, which is the smaller of the two leaves here.
- c, "Revenue per customer, since it is the leaf the tree splits by segment": revenue per customer is
  the gap being explained, the product of the two leaves, so it cannot be the leaf that explains it.

### Q3. What does an averaged revenue-per-order column read for three invented customers, and what does the tree need?

Customer A placed one order of Rs 9,00,000, B one of Rs 3,00,000, and C ten of Rs 1,00,000 each; a
per-customer column `=revenue/orders` is averaged in the pivot.

The key is a, "Rs 4,33,333 on the pivot, and the tree needs Rs 1,83,333". The column holds Rs
9,00,000, Rs 3,00,000 and Rs 1,00,000, whose Average is Rs 13,00,000 over 3, Rs 4,33,333. The
segment's revenue is Rs 22,00,000 on 12 orders, so revenue per order is Rs 1,83,333. The Average
gives each customer one vote, so two customers with one order each outvote C's ten.

- b, "Rs 1,83,333, since an Average of the column and a ratio of sums agree": they agree only when
  every customer places the same number of orders, and here one places ten.
- c, "Rs 13,00,000, the Sum, and the tree needs Rs 4,33,333": Rs 13,00,000 is the Sum Excel shows by
  default, which adds three ratios and means nothing, and the tree does not need the Average either.
- d, "Rs 4,33,333 on the pivot, and the tree needs Rs 4,33,333 too": this is the hurried analyst's
  answer. Multiply it back and three customers with 12 orders at Rs 4,33,333 make Rs 52,00,000
  against the Rs 22,00,000 the segment sold.

### Q4. Which fact would favour a grid of SUMIFS formulas over a PivotTable for the tree itself?

A design item. The ask already says the sheet must recalculate when a director changes an
assumption, and so far every assumption sits in an input cell the tree does not read, so the tree can
stay a pivot while the inputs beside it are formulas.

The key is b, "A director's typed assumption must move the tree's own cells at once".
A PivotTable recalculates only when someone presses Refresh and cannot read an input cell at all,
while a SUMIFS grid recalculates the moment a cell it reads changes. Once an assumption feeds the
tree's own cells, the tree belongs in formulas. Chapter 6 builds the yellow input cells that take such
an assumption.

- a, "The table grows from 300 rows to 3,000 rows before Monday's first refresh": a PivotTable handles 3,000
  rows with no change, so size does not switch the call.
- c, "A director wants the tree sliced by city as well as by segment, in the room": slicing by any
  column is what a pivot does with one drag, so this fact argues for the pivot.
- d, "The deck has to open on a laptop that has no login to the warehouse": both a pivot and a grid open
  without a login, so this rules out a live dashboard and leaves the call where it was.

### Q5. What happens to Q2 when the customer table is split on each customer's last order date?

The table's only date is last_order_date, the date of each customer's most recent order.

The key is a, "It reads too high, since a customer who bought in both lands wholly in Q2".
last_order_date says when a customer last bought, so a customer who bought every month from April
and once more in September moves the whole half-year into Q2. On Kalpa's table the split puts
Rs 17.88 crore in Q2, against the Rs 9.84 crore Monday's warehouse gave. The quarter split needs one
row per order, which chapter 2 takes from the raw export.

- b, "It reads too low, since the latest orders in a half-year tend to be the smallest": the size of
  the last order does not matter, because the split moves each customer's whole half-year.
- c, "It reads right, since each customer's revenue lands in exactly one quarter": landing in one
  quarter is the problem, since most revenue belongs to two.
- d, "It reads right for Business, and too low for the three consumer segments": corporate buyers
  also order in both quarters, so Business moves into Q2 the same way.

### Q6. Which check can disagree with the pivot when the pivot is wrong?

A design item. A second route shares none of the first route's steps.

The key is c, "A COUNTIF and two SUMIFS per segment, beside the pivot, on the table's own cells".
The formulas read the table's own cells by a different calculator, so a pivot that summed the wrong
field, dropped a segment or averaged where it should add would disagree with them. Chapter 1's
notebook ran the same route in Python, reading the CSV as text and keeping a running total per
segment, and all twelve cells matched.

- a, "A second PivotTable on the same table, with the fields dragged in another order": the same
  calculator on the same table makes the same mistake twice.
- b, "The pivot's grand total compared with the sum of its own four segment rows": a pivot's grand
  total is the sum of its rows by construction, so this check cannot fail.
- d, "A SUM of the table's whole revenue column, compared with the pivot's grand total": a different
  calculator on the same table, and it checks one number. A pivot that split the segments wrongly or
  counted the wrong customers still matches the grand total, so eleven of the twelve cells go unchecked.

## Why is the averaged leaf (item 3, d) the most tempting wrong answer?

It is the hurried analyst's answer, and it looks careful: the analyst saw that the Sum of the column
meant nothing, switched to Average, and got a number that looks like a basket size. On Kalpa's table the same move reads
Business at Rs 11,66,786 an order against revenue over orders of Rs 10,45,740, 11.6 percent high,
and a director who multiplies 39 customers by 4.82 orders by Rs 11.67 lakh gets Rs 2.28 crore more
than Business sold. The average of ratios is furthest out where customers differ most in size, and
Business baskets run from Rs 3.34 lakh to Rs 66.98 lakh. The check is the multiply-back, and the fix
is a ratio of the pivot's own sums.

## Where does Costco face the same question about its paid tier?

Costco, the membership warehouse retailer, reports how much of its sales its paid upgrade tier
carries. Its annual report on Form 10-K for the fiscal year to 31 August 2025 counts 81.0 million
paid members, 38.7 million of them on the Executive tier, and says Executive members made up
"approximately 73.6% of worldwide net sales in 2025" (Costco Form 10-K, fiscal 2025, sec.gov,
checked 30 September 2026). Kalpa asks the same question of Retail-Plus, and the tree answers the
next one: through which leaf the paid tier carries its share.

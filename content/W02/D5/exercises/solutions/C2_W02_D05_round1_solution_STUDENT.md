# Solution: round 1, the pivot

Answers: 1b 2c 3a 4d 5b 6d 7a

## The idea being tested

A pivot adds one value per row, so the grain of the table under it decides what it counts. The raw
export is one row per payment, 1,450 rows for 1,000 orders, and a Sum of `order_amount` over it
reads Rs 39.41 crore for a half-year the warehouse books at Rs 19.84 crore. Counting each order once
ties it back to the rupee and turns Retail-Core's apparent rise into a fall.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | b | Rows against ids exposes a finer grain in seconds, and the warehouse total is the control every deck number must reproduce. | a compares two numbers inflated by the same repeat, so the fall still looks plausible. c finds outliers, and the repeat is not an outlier. d averages repeated rows, which hides the problem further. |
| 2 | c | Remove Duplicates drops only rows identical in every column: the 50 gateway copies. An instalment order's two rows differ in `paid_amount`, so both stay: 1,450 less 50 is 1,400. | a is what counting each order once gives. b removes the instalment rows as well, which the tool does not do. d assumes nothing is identical, but the 50 copies are. |
| 3 | a | A growth plan works on the segments that are falling; a Core that seems to grow is left alone. | b, c and d are decisions nobody would take from a Core figure, so the number could not have misled them. |
| 4 | d | The running count reaches 1 only on an order's first row, and the IF turns every later row into 0. | a returns 1, 2 on an instalment order, so its second row is not 0. b flags only orders that appear once in the whole export, dropping every instalment order entirely. c returns the total count on every row. |
| 5 | b | Most customers last bought in Q2, so their whole half-year lands in Q2 and Q2 swells. | a and d misread what a last date is. c treats a recency as a split, which is the mistake. |
| 6 | d | Tying the tree proves the raw export is right at the order grain; the protect list reads another export, which has to tie on its own. | a, b and c are answered by the reconciled tree itself. |
| 7 | a | Orders per customer fell 22.0 percent, customers 16.5 percent, and the basket grew 8.4 percent; 76 times 1.84 times Rs 2,953 is Rs 4.13 lakh. | b is the second mover. c moved the other way. d ignores the spread from minus 22.0 to plus 8.4. |

## Where this appears in production

Every finance-facing dashboard has a control total: a number owned upstream that the report must
reproduce before it is published. The grain check is the first thing an analyst runs on any export
they did not build, because payment, line-item and event exports all repeat the parent's amount.

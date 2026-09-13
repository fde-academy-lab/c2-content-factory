# Solutions: predict the row count

Answers: 1b 2c 3c 4a

## Q1. 1,450

Every order appears at least once. The 970 paid orders contribute one row per payment row they
have, which is 1,420, and the 30 unpaid contribute one row each with NULLs on the payment side.
1,420 plus 30 is 1,450.

Option a, 1,428, is the payments table's own row count and is the tempting wrong answer, because
it feels like the join should return "one row per payment". It nearly does, and the nearly is the
30 unpaid orders and the 8 orphans.

## Q2. 1,420

The `INNER` join drops the 30 unpaid orders, because they have nothing to match. It also drops the
8 orphan payments from the other side, but those were never going to appear in a join anchored on
orders anyway.

1,450 minus 30 is 1,420. Those 30 rows are exactly what Anand asked to see.

## Q3. 1,428

Anchoring on payments keeps every payment row, all 1,428 of them, including the 8 whose order is
not in the book. The 30 unpaid orders never appear, because they have no payment row to bring them
in.

Same two tables, same relationship, a different anchor, a different answer. That is the whole
lesson of the day in one comparison.

## Q4. Roughly twice the true booked total

The 450 orders with two payment rows each contribute their amount twice. Those 450 are not a
random slice: large invoices get instalment terms, so the duplicated orders are the ones carrying
the revenue.

The result is 1.9952 times the true figure, which is the worst possible behaviour. A number that
is 5 percent wrong gets questioned. A number that is twice the truth gets believed, because it is
so far out that it reads as a different metric rather than a broken one.

Option d is wrong for a mundane reason worth knowing: `o.amount` is qualified, so nothing is
ambiguous and the query runs perfectly.

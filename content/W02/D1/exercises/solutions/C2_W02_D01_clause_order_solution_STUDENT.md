# Solution: round 2 set, per segment and per quarter

Answers: 1c 2a 3d 4b 5c 6a 7d

## The idea being tested

`GROUP BY` makes one row per group and every aggregate runs inside its group. Filters sit where the
logical order puts them: `WHERE` tests rows before groups exist, `HAVING` tests groups after. A ratio
of two counts is an integer division in Postgres unless one side is made numeric, and the grid shows
no warning when it happens.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | c | Four segments times two quarters, and every pair has orders, so 8 rows. | a groups by segment only. b groups by quarter only. d: grouping collapses rows; it never keeps them one per order. |
| 2 | a | Retail-Core's true figures are 1.95 and 2.01. A jump from 1 to 2 in one quarter is the signature of integer division dropping the fraction. | b: more customers would lower orders per customer, never double it. c: the order of grouping columns changes nothing in the result. d: a status filter changes the counts, and it cannot turn 1.95 into 1. |
| 3 | d | Both counts are integers, so Postgres divides as integers and truncates 1.84 to 1. | a and c are the numeric results, which need `::numeric` on one side. b is rounding; integer division truncates toward zero. |
| 4 | b | The count exists only after grouping, so the filter is `HAVING count(*) < 30`. It returns one row: Student in Q1, 27 orders. | a: `WHERE` runs before any group exists, so the database refuses an aggregate there. c returns the 30 smallest groups, and there are only eight. d counts customers, and the warning is about orders. |
| 5 | c | The status belongs to a row, so it is a `WHERE`, and it runs before the groups form: 653 delivered orders remain. | a: `HAVING` on a column that is not grouped is refused. b gives the right numbers and hides the filter in every column, which is harder to audit. d sorts and filters nothing. |
| 6 | a | Groups that add back to the table they came from prove no row was lost or counted twice. | b: reliability needs enough orders per cell, which is the `HAVING` check. c: a sum of counts cannot check a ratio. d: order is set by `ORDER BY` alone. |
| 7 | d | FROM builds the rows, WHERE keeps some, GROUP BY forms groups, HAVING keeps some groups, SELECT computes the columns. | a is the written order. b puts SELECT before grouping, which cannot compute an aggregate. c puts GROUP BY before WHERE. |

## The part worth arguing about

Item 2. A few learners pick b because more customers sounds like it moves orders per customer. It
does, the other way: more customers with the same orders lowers the ratio. The habit worth keeping is
the calculator check: orders per customer times customers must give the orders, and 1 times 102 is
not 199.

## Where the pattern lives in production

Integer division is behind a steady stream of wrong conversion rates, click-through rates and
retention rates in warehouse dashboards, and it survives review because the column looks like a
number. PostgreSQL's own table of operators says it plainly: for integral types, division truncates
the result towards zero.

PostgreSQL 16 documentation, mathematical functions and operators, https://www.postgresql.org/docs/16/functions-math.html (verified 29 Sep 2026)

# Unguided: predict the three rankings

Four members with these Q2 totals, sorted descending: Rs 9,000, Rs 7,500, Rs 7,500, Rs 6,200.

Answer from the definitions rather than from memory of the demo.

## Q1.

`ROW_NUMBER() OVER (ORDER BY revenue DESC)` returns which sequence? Which one appears?

a) 1, 2, 2, 3
b) 1, 2, 2, 4
c) 1, 2, 3, 4
d) 1, 1, 2, 3

## Q2.

`RANK() OVER (ORDER BY revenue DESC)` returns which sequence? Which one appears?

a) 1, 2, 2, 4
b) 1, 2, 3, 4
c) 1, 2, 2, 3
d) 1, 1, 3, 4

## Q3.

`DENSE_RANK() OVER (ORDER BY revenue DESC)` returns which sequence? Which one appears?

a) 1, 2, 2, 4
b) 1, 2, 3, 4
c) 1, 1, 2, 2
d) 1, 2, 2, 3

## Q4.

You run the `ROW_NUMBER` query twice against unchanged data. Which one appears?

a) The two tied rows keep the positions they had the first time
b) The order of the tied pair may differ between the two runs
c) It raises an error the second time, since the tie is ambiguous
d) Postgres assigns the lower position to the lower customer id

## Q5.

A window function is put directly into `WHERE`. Which one appears?

a) It works, and it filters once the window has been computed
b) It works only when the query has no `GROUP BY` clause
c) It is refused, since windows may only appear in `SELECT`
d) It is refused, since `WHERE` runs before the window exists

## Answering

Post one line: the five letters in order. Then one sentence on which of Q1 to Q3 you would have
got wrong under time pressure in an interview.

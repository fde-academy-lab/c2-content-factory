# Solutions: predict the row count

Answers: 1b 2c 3a 4c

## Q1. Two rows

`GROUP BY quarter` makes one group per distinct value of `quarter`, and the warehouse holds two
quarters. The thousand order rows are gone from the result; only the groups survive.

The common wrong answer is 1,000, which is what the query would return with no `GROUP BY` at all.

## Q2. Twelve rows

Four segments times three channels, and every combination happens to occur in this book. Grouping
by two columns makes one group per distinct **pair**, not one per column.

Worth saying aloud: twelve is the ceiling, not a guarantee. A segment that never used the store
channel would leave eleven rows, and nothing in the query would tell you a combination was
missing. That is a question about the data, and a `LEFT JOIN` against a list of all pairs is how
you ask it.

## Q3. Customers who ordered exactly once

`HAVING count(*) = 1` keeps the groups whose row count is one, so the result is the customers with
exactly one order in the book. It is not 340: customers who never ordered have no rows in `orders`
and therefore no group, so they never reach `HAVING` at all.

That last sentence is tomorrow's whole lesson in miniature.

## Q4. Five rows, and which five is not promised

`LIMIT` cuts the list the earlier stages produced. With no `ORDER BY` there is no list order to
cut, so the server returns whichever five are cheapest to hand back. Two machines can answer
differently, and the same machine can answer differently after an index is added.

Option d is a reasonable guess and wrong: the query runs perfectly well, which is what makes this
dangerous rather than annoying.

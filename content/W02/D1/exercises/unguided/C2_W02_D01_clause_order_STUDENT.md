# Unguided: what runs when

Five claims about when a clause runs. One of them is wrong in each item. Work from the picture
rather than from memory.

## Q1.

A query filters with `WHERE`, groups with `GROUP BY`, and computes `sum(amount) AS revenue` in
`SELECT`. Which one appears?

a) `WHERE` cannot use `revenue`, because `SELECT` runs after it
b) `WHERE` can use `revenue`, since the alias is in the same statement
c) `WHERE` can use `revenue` only when there is no `GROUP BY`
d) `WHERE` can use `revenue` once it is wrapped in an aggregate

## Q2.

You want the segments that placed more than a hundred orders. Which one appears?

a) `SELECT count(*) > 100`, which returns true or false per row
b) `WHERE count(*) > 100`, filtering the rows as they arrive
c) `ORDER BY count(*) > 100`, which sorts the passing groups first
d) `HAVING count(*) > 100`, filtering the groups once they exist

## Q3.

A query selects `segment` and `channel` while grouping by `segment` alone. Which one appears?

a) It returns one row per segment carrying the first channel found in it
b) It returns one row for every segment and channel pair in the book
c) It is refused: `SELECT` has one row per group, many channels
d) It is refused, because `channel` lives on a different table entirely

## Q4.

`ORDER BY revenue DESC` works where `WHERE revenue > 0` does not. Which one appears?

a) `ORDER BY` is evaluated by the client rather than the server
b) `ORDER BY` re-runs the `SELECT` list once for each row
c) `ORDER BY` accepts aliases because sorting is not filtering
d) `ORDER BY` runs after `SELECT`, so the alias already exists

## Q5.

A colleague says a query returns rows in insertion order without an `ORDER BY`, and shows you a
run that proves it. Which one appears?

a) They are right, because Postgres stores rows in insertion order forever
b) They are right on small tables and wrong once the table grows large
c) They saw one run, and nothing is promised without `ORDER BY`
d) They are right until the first row in the table is updated

## Answering

Post one line: the five letters in order. Then pick the one you were least sure about and write
one sentence defending your choice from the execution order rather than from experience.

# Solutions: predict the three rankings

Answers: 1c 2a 3d 4b 5d

## Q1. 1, 2, 3, 4

`ROW_NUMBER` never looks at the values. It numbers the rows in the order it receives them, so a
tie is broken by whatever the server happened to do.

## Q2. 1, 2, 2, 4

`RANK` gives both tied rows position 2, then **skips** to 4, because two rows are already ahead of
the fourth. The gap is the point: position 4 tells you truthfully that three members outrank you.

Option d is `DENSE_RANK` and is the most commonly chosen wrong answer.

## Q3. 1, 2, 2, 3

`DENSE_RANK` gives both tied rows position 2 and then continues at 3, so positions are consecutive
and the count of distinct positions is smaller than the count of rows.

A useful way to hold the difference: `RANK` answers "how many are ahead of me", `DENSE_RANK`
answers "how many distinct levels are ahead of me".

## Q4. The order may differ between runs

Nothing in the data separates the two tied rows, so nothing in the plan has to keep them in a
fixed order. A parallel scan, an added index, or a vacuum can change which one comes first.

This is the argument against `ROW_NUMBER` that has nothing to do with fairness: the list is not
reproducible, so two people running the same query can hand Marketing different names.

Option d is a plausible-sounding invention. Postgres makes no such promise, and adding
`customer_id` as a tiebreaker in the window's `ORDER BY` is how you would make it true.

## Q5. Refused, because WHERE runs before the window exists

```
ERROR:  window functions are not allowed in WHERE
```

The same execution order that refused an aggregate in `WHERE` on Monday. Compute the window in an
inner query or a CTE, then filter outside it.

Option c is wrong in a way worth knowing: windows are allowed in `ORDER BY` as well as
`SELECT`, which follows from `ORDER BY` running later.

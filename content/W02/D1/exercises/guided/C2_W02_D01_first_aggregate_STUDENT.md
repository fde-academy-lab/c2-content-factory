# Guided: one grouped query, built a clause at a time

Built together. Every step names the stage of the execution order it is adding, so the picture on
the board fills in as the query does.

## The question

Anand asked for revenue per segment per quarter. Nothing else. Build exactly that and stop.

## Step 1: the rows

```sql
SELECT * FROM orders;
```

A thousand rows. This is the `FROM` stage and nothing has been dropped yet.

## Step 2: the segment lives elsewhere

Segment is an attribute of the customer, not of the order, so the two tables have to meet.

```sql
SELECT o.order_id, o.amount, c.segment
FROM   orders o
JOIN   customers c USING (customer_id);
```

Still a thousand rows. Check that, because tomorrow the same move will not be free.

## Step 3: drop the rows you do not want

```sql
WHERE o.quarter = 'Q1'
```

This is the `WHERE` stage. It judges one row at a time, and it has no idea groups are coming.

## Step 4: collapse

```sql
GROUP BY c.segment
```

The order rows are gone from the result now. Four rows remain, one per segment. Say aloud what
happened to the thousand.

## Step 5: compute the columns

```sql
SELECT c.segment, count(*) AS orders, sum(o.amount) AS revenue
```

This is the `SELECT` stage and it runs after the grouping, which is why `count(*)` and `sum()`
have something to work on.

## Step 6: put it in an order

```sql
ORDER BY revenue DESC
```

`ORDER BY` runs after `SELECT`, so the alias `revenue` already exists. Try the same alias in
`WHERE` and watch it fail, then say why using the board.

## The whole thing

```sql
SELECT c.segment, count(*) AS orders, sum(o.amount) AS revenue
FROM   orders o
JOIN   customers c USING (customer_id)
WHERE  o.quarter = 'Q1'
GROUP  BY c.segment
ORDER  BY revenue DESC;
```

## Before moving on

Write one comment line above it stating the question and the denominator. If you cannot state the
denominator in a short sentence, the query is not finished.

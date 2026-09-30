# Guided: the segment count and the revenue aggregate, built together

Round 2, with the trainer, about fifteen minutes. The trainer types each step on the projector and
says the clause order aloud as the query runs; you type the same step in
`sql/C2_W02_D01_02_segments_STUDENT.sql` below its last block and run it. Each step adds exactly one
clause to the step before, so when a result surprises you, the new clause is where to look.

> "Every segment. I do not want a total that hides which one moved." Anand Iyer, finance controller, Kalpa Retail

---

## Step 1. The whole book, one row

```sql
SELECT count(*) AS orders, sum(amount) AS revenue
FROM   orders;
```

**Said aloud.** FROM makes the rows, SELECT counts and adds them.
**What you should see.** One row: 1,000 orders and 198400000.00, which is Rs 19.84 crore.

## Step 2. One row per quarter

```sql
SELECT quarter, count(*) AS orders, sum(amount) AS revenue
FROM   orders
GROUP  BY quarter
ORDER  BY quarter;
```

**Said aloud.** FROM, then GROUP BY forms two groups, then SELECT computes inside each, then ORDER BY.
**What you should see.** Two rows, 538 and 462 orders, which add back to 1,000.

## Step 3. The segment, borrowed from the customer

```sql
SELECT c.segment, count(*) AS orders, sum(o.amount) AS revenue
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment
ORDER  BY c.segment;
```

**Said aloud.** Each order finds its one customer and takes the segment from it; the row count stays
1,000, because every order has exactly one customer. Tomorrow is the day joins are taught in full.
**What you should see.** Four rows. Business carries 196599040.00 of the revenue.

## Step 4. Segment and quarter together

Add `o.quarter` to both the SELECT and the GROUP BY, and to the ORDER BY after `c.segment`.

**Said aloud.** Every column in SELECT is either grouped or aggregated; the database has no way to
print one segment for a group that holds four.
**What you should see.** Eight rows. Retail-Plus reads 215 orders in Q1 and 140 in Q2.

## Step 5. The customers leaf

Add `count(DISTINCT o.customer_id) AS customers` to the SELECT.

**Said aloud.** DISTINCT counts each customer once inside each group.
**What you should see.** Retail-Plus reads 91 customers in Q1 and 76 in Q2. Keep this query: round
2's trap starts from it.

---

## Hands-on, alone, five minutes

Change one thing in step 5 so it counts delivered orders only, and say which clause you changed and
why it runs before the groups form. The answer is block `r2_delivered_by_segment` in the same file,
which you open only after yours runs.

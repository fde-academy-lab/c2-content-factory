# How many orders, customers and rupees did each segment book in each quarter, built one clause at a time?

Guided, with the trainer, in two sittings: steps 1 and 2 in chapter 1, steps 3 to 5 in chapter 3,
about ten minutes each. The trainer types each step on the projector and says aloud the order in which
the database works through it; you type the same step in your own query tab on the warehouse and run
it. Each step adds one clause to the step before, so when a result surprises you, the new clause is
where to look. Answer each item before you run its step.

> "I want these numbers every Monday, for every segment and channel, computed from the warehouse
> itself."
>
> Anand Iyer, finance controller, Kalpa Retail

The warehouse's `orders` table holds 1,000 rows, one per order, with the columns order_id,
customer_id, order_date, quarter, channel, amount and status. The `customers` table holds 340 rows,
one per customer, with customer_id, segment, city, country and joined_date. Q1 is April to June 2026 and
Q2 is July to September 2026. Booked revenue is every order at its amount, whatever its status. Kalpa's
four segments are Business, Retail-Core, Retail-Plus (the paid membership tier, 120 members) and
Student, and the segment lives on the customers table, so each order looks it up with one line,
`JOIN customers c USING (customer_id)`. A query is written SELECT first, and the database works through
it in a different order, which the trainer says aloud at every step.

**Who needs the answer.** Anand's analyst reads the segment lines of the Monday sheet, and she will ask
how each one was built. You need to say, for any line, which clause made its groups and which made its
numbers.

**The questions on the way.**

- How many rows does the lookup line leave for the groups to work on?
- How many rows come back once the groups are segment and quarter?
- What can Retail-Plus's Q1 customer count be, before you run it?
- In which order does the database work through step 5's clauses?
- Which segment's revenue per order rose the most from Q1 to Q2?

**What you post.** One line of five letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

## What does the whole book say, and then each quarter?

Used at work whenever a new table arrives and the first question is what it holds.

**Step 1, the whole book.** Said aloud: FROM makes the rows, then SELECT counts and adds them.

```sql
SELECT count(*) AS orders, sum(amount) AS revenue
FROM   orders;
```

What you should see: one row, 1,000 orders and 198400000.00, which is Rs 19,84,00,000.

**Step 2, one row per quarter.** Said aloud: FROM makes the rows, GROUP BY puts them into two groups,
SELECT counts and adds inside each group, and ORDER BY sorts the two rows.

```sql
SELECT quarter, count(*) AS orders, sum(amount) AS revenue
FROM   orders
GROUP  BY quarter
ORDER  BY quarter;
```

What you should see: Q1 with 538 orders and Rs 10,00,00,000, Q2 with 462 orders and Rs 9,84,00,000,
which add back to the book.

## How does each order find its segment?

Used at work whenever a measure lives on one table and the label that splits it lives on another.

**Step 3, the segment from the customer.** Said aloud: FROM takes the orders and the lookup finds each
order's customer, then GROUP BY forms one group per segment, SELECT counts and adds, and ORDER BY sorts.

```sql
SELECT c.segment, count(*) AS orders, sum(o.amount) AS revenue
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment
ORDER  BY c.segment;
```

### Q1. How many rows does the lookup line leave for the groups to work on?

Before the groups form, how many rows does `FROM orders o JOIN customers c USING (customer_id)` hand
on?

a) 1,000, since each order finds one customer
b) 340, one for each customer on the customers table
c) 1,340, the two tables' rows side by side
d) 301, one for each customer who bought

What you should see when you run step 3: four rows whose orders add to 1,000. Business books
Rs 19,65,99,040 of the Rs 19,84,00,000.

## What changes when the groups are segment and quarter?

Used at work whenever a stakeholder wants every group in every period on one sheet.

**Step 4, segment and quarter together.** Add `o.quarter` to the SELECT, to the GROUP BY and to the
ORDER BY after `c.segment`. Said aloud: every column the SELECT prints is either one the groups are
formed on or one computed inside each group.

### Q2. How many rows come back once the groups are segment and quarter?

With four segments and two quarters, and orders in every segment in both quarters, how many rows does
step 4 return?

a) 4
b) 2
c) 1,000
d) 8

What you should see: Retail-Plus reads 215 orders in Q1 and 140 in Q2.

**Step 5, the customers leaf.** Add `count(DISTINCT o.customer_id) AS customers` to the SELECT. Said
aloud: inside each group, DISTINCT keeps each customer once, however many orders that customer placed.

### Q3. What can Retail-Plus's Q1 customer count be, before you run it?

Retail-Plus placed 215 orders in Q1, and the tier has 120 members. Before you run step 5, what can you
say about the customer count it prints for Retail-Plus in Q1?

a) Exactly 215, one for each order the tier placed
b) Exactly 120, every member of the tier counted once
c) At most 120, the members, whichever of them bought
d) Between 120 and 215, since some members ordered twice

### Q4. In which order does the database work through step 5's clauses?

Step 5 is written SELECT, FROM with the lookup, GROUP BY, ORDER BY. In which order does the database
work through them?

a) FROM with the lookup, then GROUP BY, then SELECT, then ORDER BY
b) SELECT, then FROM with the lookup, then GROUP BY, then ORDER BY
c) FROM with the lookup, then SELECT, then GROUP BY, then ORDER BY
d) GROUP BY, then FROM with the lookup, then SELECT, then ORDER BY

## Which segment's orders grew most in value?

Used at work whenever a revenue change is split into how many orders and how large each one was.

**On your own, three minutes.** Add `round(sum(o.amount) / count(*)) AS revenue_per_order` to step 5
and run it.

### Q5. Which segment's revenue per order rose the most from Q1 to Q2?

Reading your new column as Q2 over Q1, which segment's revenue per order rose the most?

a) Student
b) Business
c) Retail-Core
d) Retail-Plus

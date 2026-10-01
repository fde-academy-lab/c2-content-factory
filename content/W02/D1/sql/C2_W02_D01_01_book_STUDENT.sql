-- Kalpa Retail, Week 2 Monday, chapter 1: what does the book say?
--
-- Anand Iyer, the finance controller, wants last week's revenue tree every Monday, computed from
-- the warehouse itself: "No notebooks, no exports, nothing a person can mistype." The warehouse is
-- Kalpa's Postgres database; it holds the whole two-quarter book of orders. This file answers the
-- tree's first leaves for each quarter: orders, booked revenue and customers.
--
-- Q1 is April to June 2026 and Q2 is July to September 2026. Booked revenue means every order at its
-- amount, whatever its status, which is the definition Week 1 reconciled.
--
-- Run one block at a time: put the cursor inside a block, select it and run it. Each block opens on
-- the question it answers, and the notebook runs the same blocks by the names on their first lines.

-- name: c1_tables
-- The question: which tables does the warehouse hold, and how many columns does each carry?
SELECT table_name, count(*) AS columns
FROM   information_schema.columns
WHERE  table_schema = 'public'
GROUP  BY table_name
ORDER  BY table_name;

-- name: c1_order_columns
-- The question: what does one row of orders carry, and of which type is each column?
SELECT column_name, data_type
FROM   information_schema.columns
WHERE  table_schema = 'public' AND table_name = 'orders'
ORDER  BY ordinal_position;

-- name: c1_peek
-- The question: what do the first five orders look like, by order id?
SELECT *
FROM   orders
ORDER  BY order_id
LIMIT  5;

-- name: c1_book
-- The question: how many orders did each quarter book, and for how many rupees?
-- One row per quarter. Revenue is booked revenue, every status included.
SELECT quarter,
       count(*)                     AS orders,
       sum(amount)                  AS revenue,
       round(sum(amount) / count(*)) AS revenue_per_order
FROM   orders
GROUP  BY quarter
ORDER  BY quarter;

-- name: c1_customers_hurried
-- The question: how many customers bought in each quarter? (The quickest way to ask it.)
SELECT quarter, count(*) AS customers
FROM   orders
GROUP  BY quarter
ORDER  BY quarter;

-- name: c1_three_counts
-- The check: the orders table counted two ways over both quarters, each count named for what it
-- counts. The next block, c1_members, adds the third count, from the customer table.
SELECT count(*)                    AS order_rows,
       count(DISTINCT customer_id) AS customers_who_bought
FROM   orders;

-- name: c1_members
-- The question: how many customers does Kalpa hold on its customer table, bought or not?
SELECT count(*) AS customers_on_the_table
FROM   customers;

-- name: c1_customers
-- The fix: customers who bought in each quarter, each counted once, beside the order rows.
SELECT quarter,
       count(*)                    AS order_rows,
       count(DISTINCT customer_id) AS customers
FROM   orders
GROUP  BY quarter
ORDER  BY quarter;

-- name: c1_rows_for_python
-- The second route: every order row, for Python to count and add on its own.
-- This is also what an export would copy each Monday, which is why it is not the Monday way.
SELECT order_id, quarter, customer_id, amount
FROM   orders
ORDER  BY order_id;

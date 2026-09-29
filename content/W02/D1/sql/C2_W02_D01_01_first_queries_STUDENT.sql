-- Kalpa Retail, Week 2 Monday, round 1: is the warehouse the book we reconciled last week?
--
-- Anand wants last week's numbers every Monday, computed from the warehouse itself. Before a
-- single number goes on his sheet, the team checks that the warehouse and last week's extract
-- tell the same story. Run one block at a time: put the cursor inside a block and run it.
-- Every block states its question first. The notebook runs the same blocks by their names.

-- name: r1_tables
-- The question: which tables does the warehouse hold, and how many columns does each carry?
SELECT table_name, count(*) AS columns
FROM   information_schema.columns
WHERE  table_schema = 'public'
GROUP  BY table_name
ORDER  BY table_name;

-- name: r1_columns
-- The question: what does one row of orders carry, and of which type?
SELECT column_name, data_type
FROM   information_schema.columns
WHERE  table_schema = 'public' AND table_name = 'orders'
ORDER  BY ordinal_position;

-- name: r1_peek
-- The question: what does an order look like? Five rows, by order id, so everyone sees the same five.
SELECT *
FROM   orders
ORDER  BY order_id
LIMIT  5;

-- name: r1_q1_book
-- The question: how many orders did Q1 book, and for how much? Booked means every status.
SELECT count(*) AS orders, sum(amount) AS revenue
FROM   orders
WHERE  quarter = 'Q1';

-- name: r1_q2_book
-- The question: the same for Q2.
SELECT count(*) AS orders, sum(amount) AS revenue
FROM   orders
WHERE  quarter = 'Q2';

-- name: r1_plus_orders
-- The question: how many orders did Retail-Plus members place in each quarter?
-- The segment lives on the customer, so the order borrows it with one lookup line; each order has
-- exactly one customer, so the row count does not change. Tomorrow is the day joins are taught.
SELECT count(*) FILTER (WHERE o.quarter = 'Q1') AS q1_orders,
       count(*) FILTER (WHERE o.quarter = 'Q2') AS q2_orders
FROM   orders o
JOIN   customers c USING (customer_id)
WHERE  c.segment = 'Retail-Plus';

-- name: r1_customers_hurried
-- The question: how many customers bought in the two quarters? (The hurried version.)
SELECT count(*) AS customers
FROM   orders;

-- name: r1_customers_three
-- The same question, with every count named for what it counts.
SELECT count(*)                    AS order_rows,
       count(DISTINCT customer_id) AS customers_who_bought,
       (SELECT count(*) FROM customers) AS customers_on_the_book
FROM   orders;

-- name: r1_typical
-- The question: what does a typical order look like, the mean or the median?
SELECT round(avg(amount))                                   AS mean_order,
       percentile_cont(0.5) WITHIN GROUP (ORDER BY amount)  AS median_order
FROM   orders;

-- name: r1_readings
-- The question: which total is "sales"? Three honest readings, one query each.
SELECT 'booked' AS reading, count(*) AS orders, sum(amount) AS revenue FROM orders
UNION ALL
SELECT 'not cancelled', count(*), sum(amount) FROM orders WHERE status <> 'cancelled'
UNION ALL
SELECT 'delivered', count(*), sum(amount) FROM orders WHERE status = 'delivered';

-- name: r1_sample_hurried
-- The question: five delivered Q2 app orders for Anand's analyst to trace against the ERP.
-- The hurried version: no ORDER BY.
SELECT order_id, amount
FROM   orders
WHERE  quarter = 'Q2' AND channel = 'app' AND status = 'delivered'
LIMIT  5;

-- name: r1_sample_after_reload
-- The same query after a reload rewrites two rows with identical values. The transaction is rolled
-- back, so the warehouse is left exactly as it was.
BEGIN;
UPDATE orders SET status = status
WHERE  order_id IN ('KR-00542', 'KR-00544');
SELECT order_id, amount
FROM   orders
WHERE  quarter = 'Q2' AND channel = 'app' AND status = 'delivered'
LIMIT  5;
ROLLBACK;

-- name: r1_sample_fixed
-- The fix: order by a column that is unique, so the five are the same five on every run.
SELECT order_id, amount
FROM   orders
WHERE  quarter = 'Q2' AND channel = 'app' AND status = 'delivered'
ORDER  BY order_id
LIMIT  5;

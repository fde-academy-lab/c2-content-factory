-- Week 2, Tuesday. Round 1, on the warehouse: attach payments to Q2 orders and read what comes back.
-- Anand: "Show me, order by order, what we actually collected against what we booked in Q2."
-- Run against the Kalpa warehouse: psql -d kalpa -f this_file.sql

-- Step 1. The grain of each table before any join: one row per order, one row per payment.
SELECT 'orders, Q2' AS source, count(*) AS row_count, sum(amount) AS booked
FROM orders
WHERE quarter = 'Q2'
UNION ALL
SELECT 'payments, all', count(*), sum(amount)
FROM payments;

-- Step 2. Does order_id repeat in payments? A key that repeats on one side multiplies the other side.
SELECT payment_rows, count(*) AS orders_with_that_many
FROM (
    SELECT order_id, count(*) AS payment_rows
    FROM payments
    GROUP BY order_id
) per_order
GROUP BY payment_rows
ORDER BY payment_rows;

-- Step 3. The hurried query: "collected" as the value of the Q2 orders that have a payment.
-- Every row it sums is a real order with a real payment. Compare the total with booked.
SELECT sum(o.amount) AS collected_as_reported
FROM orders o
JOIN payments p ON p.order_id = o.order_id
WHERE o.quarter = 'Q2';

-- Step 4. The row count that exposes it: orders in, rows out.
SELECT (SELECT count(*) FROM orders WHERE quarter = 'Q2') AS orders_in,
       count(*) AS rows_out
FROM orders o
LEFT JOIN payments p ON p.order_id = o.order_id
WHERE o.quarter = 'Q2';

-- Step 5. The harder variant: booked and collected side by side by channel, from one join.
-- Read the percentage collected and decide whether you would send it to Anand.
SELECT o.channel,
       count(*) AS rows_out,
       sum(o.amount) AS booked_as_reported,
       sum(p.amount) AS collected_as_reported,
       round(100 * sum(p.amount) / sum(o.amount), 1) AS pct_collected
FROM orders o
LEFT JOIN payments p ON p.order_id = o.order_id
WHERE o.quarter = 'Q2'
GROUP BY o.channel
ORDER BY o.channel;

-- Step 6. The fix: bring payments to one row per order first, then join at the same grain.
-- Rows in must equal rows out, and booked must equal Monday's booked.
WITH paid_per_order AS (
    SELECT order_id, sum(amount) AS paid, count(*) AS payment_rows
    FROM payments
    GROUP BY order_id
)
SELECT o.channel,
       count(*) AS rows_out,
       sum(o.amount) AS booked,
       sum(coalesce(pp.paid, 0)) AS paid_as_posted
FROM orders o
LEFT JOIN paid_per_order pp ON pp.order_id = o.order_id
WHERE o.quarter = 'Q2'
GROUP BY o.channel
ORDER BY o.channel;

-- Step 7. The check in one line: after the fix, rows out equals orders in.
WITH paid_per_order AS (
    SELECT order_id, sum(amount) AS paid
    FROM payments
    GROUP BY order_id
)
SELECT count(*) = (SELECT count(*) FROM orders WHERE quarter = 'Q2') AS rows_reconcile,
       sum(o.amount) = (SELECT sum(amount) FROM orders WHERE quarter = 'Q2') AS booked_reconciles
FROM orders o
LEFT JOIN paid_per_order pp ON pp.order_id = o.order_id
WHERE o.quarter = 'Q2';

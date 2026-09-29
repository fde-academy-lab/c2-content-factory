-- Week 2, Tuesday. Round 2: the row-count check and the revenue bridge.
-- Kavya: "Rows in, rows out, and the difference explained, written above the number."
-- Part A runs on the invented tiny tables; part B runs on the warehouse. Run: psql -d kalpa -f this_file.sql

-- Part A. The invented tiny tables again, so the INNER join's quiet loss can be seen row by row.
DROP TABLE IF EXISTS tiny_orders, tiny_payments;
CREATE TEMP TABLE tiny_orders (order_id text PRIMARY KEY, channel text, amount numeric(12, 2), status text);
CREATE TEMP TABLE tiny_payments (payment_id text PRIMARY KEY, order_id text, paid_date date,
                                 amount numeric(12, 2), instalment_no integer);
INSERT INTO tiny_orders VALUES
    ('T-1', 'app', 1000, 'delivered'), ('T-2', 'web', 2000, 'delivered'),
    ('T-3', 'store', 1500, 'delivered'), ('T-4', 'app', 800, 'delivered'),
    ('T-5', 'store', 500, 'delivered');
INSERT INTO tiny_payments VALUES
    ('P-1', 'T-1', '2026-07-03', 1000, 1), ('P-2', 'T-2', '2026-07-05', 1200, 1),
    ('P-3', 'T-2', '2026-08-05', 800, 2), ('P-4', 'T-3', '2026-07-09', 1500, 1),
    ('P-5', 'T-3', '2026-07-09', 1500, 1), ('P-6', 'T-5', '2026-07-12', 500, 1),
    ('P-7', 'T-9', '2026-07-14', 600, 1);

-- A1. The plausible wrong answer: an INNER join at the right grain, and a gap that reads as none.
WITH paid_per_order AS (
    SELECT order_id, sum(amount) AS paid FROM tiny_payments GROUP BY order_id
)
SELECT count(*) AS orders_in_report,
       sum(o.amount) AS booked,
       sum(pp.paid) AS collected,
       sum(o.amount) - sum(pp.paid) AS gap
FROM tiny_orders o
JOIN paid_per_order pp ON pp.order_id = o.order_id;

-- A2. The check: orders in the report against orders in the table.
SELECT (SELECT count(*) FROM tiny_orders) AS orders_in_table,
       (SELECT count(*) FROM tiny_orders o
          JOIN (SELECT DISTINCT order_id FROM tiny_payments) p ON p.order_id = o.order_id)
       AS orders_in_inner_report;

-- A3. The fix: LEFT JOIN keeps the unpaid order, and COALESCE makes its collected amount a zero.
WITH paid_per_order AS (
    SELECT order_id, sum(amount) AS paid FROM tiny_payments GROUP BY order_id
)
SELECT count(*) AS orders_in_report,
       sum(o.amount) AS booked,
       sum(coalesce(pp.paid, 0)) AS collected_as_posted,
       sum(o.amount) - sum(coalesce(pp.paid, 0)) AS gap
FROM tiny_orders o
LEFT JOIN paid_per_order pp ON pp.order_id = o.order_id;

-- A4. The bridge on the tiny tables: booked, less what was never paid, plus what was posted twice.
WITH per_instalment AS (
    SELECT order_id, instalment_no, max(amount) AS amount, count(*) AS times_posted
    FROM tiny_payments
    GROUP BY order_id, instalment_no
),
per_order AS (
    SELECT order_id,
           sum(amount) AS collected,
           sum(amount * (times_posted - 1)) AS posted_twice
    FROM per_instalment
    GROUP BY order_id
)
SELECT sum(o.amount) AS booked,
       -sum(o.amount) FILTER (WHERE po.order_id IS NULL) AS less_never_paid,
       sum(coalesce(po.collected, 0)) AS collected,
       sum(coalesce(po.posted_twice, 0)) AS plus_posted_twice,
       sum(coalesce(po.collected, 0) + coalesce(po.posted_twice, 0)) AS posted_in_feed
FROM tiny_orders o
LEFT JOIN per_order po ON po.order_id = o.order_id;

-- Part B. The warehouse. Write the reconciliation above the number, then run it.
-- B1. Rows in: the Q2 orders and their booked total, from the orders table alone.
SELECT count(*) AS orders_in, sum(amount) AS booked
FROM orders
WHERE quarter = 'Q2';

-- B2. Rows out: the order-grain LEFT join. Rows out must equal rows in; booked must equal B1.
WITH paid_per_order AS (
    SELECT order_id, sum(amount) AS paid FROM payments GROUP BY order_id
)
SELECT count(*) AS rows_out,
       sum(o.amount) AS booked,
       sum(coalesce(pp.paid, 0)) AS collected_as_posted,
       count(pp.order_id) AS orders_with_a_payment
FROM orders o
LEFT JOIN paid_per_order pp ON pp.order_id = o.order_id
WHERE o.quarter = 'Q2';

-- B3. The bridge on the warehouse, one row of numbers: booked, less never paid, collected,
-- plus posted twice, posted in the feed. Read each move as a question for Anand.
WITH per_instalment AS (
    SELECT order_id, instalment_no, max(amount) AS amount, count(*) AS times_posted
    FROM payments
    GROUP BY order_id, instalment_no
),
per_order AS (
    SELECT order_id,
           sum(amount) AS collected,
           sum(amount * (times_posted - 1)) AS posted_twice
    FROM per_instalment
    GROUP BY order_id
)
SELECT sum(o.amount) AS booked,
       coalesce(-sum(o.amount) FILTER (WHERE po.order_id IS NULL), 0) AS less_never_paid,
       sum(coalesce(po.collected, 0)) AS collected,
       sum(coalesce(po.posted_twice, 0)) AS plus_posted_twice,
       sum(coalesce(po.collected, 0) + coalesce(po.posted_twice, 0)) AS posted_in_feed
FROM orders o
LEFT JOIN per_order po ON po.order_id = o.order_id
WHERE o.quarter = 'Q2';

-- B4. The bridge must close: booked plus every move equals what the feed posted.
WITH per_order AS (
    SELECT order_id, sum(amount) AS posted FROM payments GROUP BY order_id
)
SELECT sum(coalesce(po.posted, 0))
       = (SELECT sum(p.amount) FROM payments p
            JOIN orders o ON o.order_id = p.order_id
           WHERE o.quarter = 'Q2') AS posted_reconciles_to_feed
FROM orders o
LEFT JOIN per_order po ON po.order_id = o.order_id
WHERE o.quarter = 'Q2';

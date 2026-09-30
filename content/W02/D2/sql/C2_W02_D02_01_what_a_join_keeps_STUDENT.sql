-- Week 2, Tuesday. Chapter 1: When payments are attached to orders, which rows does each join keep, drop or repeat?
-- Two invented tables first, traced by hand, then the warehouse's grain.
-- The tiny tables are TEMP tables, so they vanish when the session ends.
-- Run it against the warehouse: psql -d kalpa -f this_file.sql

-- Setup: the two invented tables
DROP TABLE IF EXISTS tiny_orders, tiny_payments;
CREATE TEMP TABLE tiny_orders (
    order_id  text PRIMARY KEY,
    channel   text NOT NULL,
    amount    numeric(12, 2) NOT NULL
);
CREATE TEMP TABLE tiny_payments (
    payment_id    text PRIMARY KEY,
    order_id      text NOT NULL,
    paid_date     date NOT NULL,
    amount        numeric(12, 2) NOT NULL,
    instalment_no integer NOT NULL
);
INSERT INTO tiny_orders VALUES
    ('T-1', 'app',   1000),
    ('T-2', 'web',   2000),
    ('T-3', 'store', 1500),
    ('T-4', 'app',    800),
    ('T-5', 'store',  500);
INSERT INTO tiny_payments VALUES
    ('P-1', 'T-1', '2026-07-03', 1000, 1),
    ('P-2', 'T-2', '2026-07-05', 1200, 1),
    ('P-3', 'T-2', '2026-08-05',  800, 2),
    ('P-4', 'T-3', '2026-07-09', 1500, 1),
    ('P-5', 'T-3', '2026-07-09', 1500, 1),
    ('P-6', 'T-5', '2026-07-12',  500, 1),
    ('P-7', 'T-9', '2026-07-14',  600, 1);

-- What is one row of each warehouse table?
SELECT 'orders' AS source, count(*) AS row_count, count(DISTINCT order_id) AS order_ids
FROM orders
UNION ALL
SELECT 'payments', count(*), count(DISTINCT order_id)
FROM payments;

-- How many payment rows does one order id hold at most?
SELECT max(rows_per_id) AS most_rows_for_one_order_id
FROM (SELECT order_id, count(*) AS rows_per_id FROM payments GROUP BY order_id) AS per_id;

-- How many rows does the INNER join return, and which?
SELECT o.order_id, o.amount AS booked, p.payment_id, p.amount AS paid, p.instalment_no
FROM tiny_orders o
JOIN tiny_payments p ON p.order_id = o.order_id
ORDER BY o.order_id, p.payment_id;

-- How many rows does each of the four joins return?
SELECT 'INNER' AS join_type, count(*) AS row_count
FROM tiny_orders o JOIN tiny_payments p ON p.order_id = o.order_id
UNION ALL
SELECT 'LEFT', count(*)
FROM tiny_orders o LEFT JOIN tiny_payments p ON p.order_id = o.order_id
UNION ALL
SELECT 'RIGHT', count(*)
FROM tiny_orders o RIGHT JOIN tiny_payments p ON p.order_id = o.order_id
UNION ALL
SELECT 'FULL', count(*)
FROM tiny_orders o FULL JOIN tiny_payments p ON p.order_id = o.order_id;

-- The trap: what does a statement started from payments show?
SELECT p.payment_id, p.order_id AS paid_for, p.amount AS paid, o.order_id, o.amount AS booked
FROM tiny_payments p
LEFT JOIN tiny_orders o ON o.order_id = p.order_id
ORDER BY p.payment_id;

-- The fix: what does the statement show with orders first?
SELECT o.order_id, o.amount AS booked, p.payment_id, p.amount AS paid
FROM tiny_orders o
LEFT JOIN tiny_payments p ON p.order_id = o.order_id
ORDER BY o.order_id, p.payment_id;

-- The second route: how often does each key appear on each side?
SELECT k.order_id,
       (SELECT count(*) FROM tiny_orders o WHERE o.order_id = k.order_id)   AS rows_in_orders,
       (SELECT count(*) FROM tiny_payments p WHERE p.order_id = k.order_id) AS rows_in_payments
FROM (SELECT order_id FROM tiny_orders UNION SELECT order_id FROM tiny_payments) AS k
ORDER BY k.order_id;

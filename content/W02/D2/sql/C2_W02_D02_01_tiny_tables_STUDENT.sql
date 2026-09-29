-- Week 2, Tuesday. Round 1: two tiny tables, traced row by row before any query runs.
-- Anand asks what was collected against what was booked. Before the warehouse answers, five invented
-- orders and seven invented payments show what each join keeps, drops and repeats.
-- The numbers here are invented to show the mechanism. Run: psql -f this_file.sql
-- The tables are TEMP tables, so they vanish when the session ends and the warehouse is untouched.

DROP TABLE IF EXISTS tiny_orders, tiny_payments;

CREATE TEMP TABLE tiny_orders (
    order_id  text PRIMARY KEY,
    channel   text NOT NULL,
    amount    numeric(12, 2) NOT NULL,
    status    text NOT NULL
);

CREATE TEMP TABLE tiny_payments (
    payment_id    text PRIMARY KEY,
    order_id      text NOT NULL,
    paid_date     date NOT NULL,
    amount        numeric(12, 2) NOT NULL,
    instalment_no integer NOT NULL
);

INSERT INTO tiny_orders VALUES
    ('T-1', 'app',   1000, 'delivered'),
    ('T-2', 'web',   2000, 'delivered'),
    ('T-3', 'store', 1500, 'delivered'),
    ('T-4', 'app',    800, 'delivered'),
    ('T-5', 'store',  500, 'delivered');

INSERT INTO tiny_payments VALUES
    ('P-1', 'T-1', '2026-07-03', 1000, 1),
    ('P-2', 'T-2', '2026-07-05', 1200, 1),
    ('P-3', 'T-2', '2026-08-05',  800, 2),
    ('P-4', 'T-3', '2026-07-09', 1500, 1),
    ('P-5', 'T-3', '2026-07-09', 1500, 1),
    ('P-6', 'T-5', '2026-07-12',  500, 1),
    ('P-7', 'T-9', '2026-07-14',  600, 1);

-- Step 1. The grain of each table: one row per order, and one row per payment.
-- Predict first: how many rows will each join below return? Write your four numbers down.
SELECT 'tiny_orders' AS source, count(*) AS row_count FROM tiny_orders
UNION ALL
SELECT 'tiny_payments', count(*) FROM tiny_payments;

-- Step 2. INNER JOIN keeps only the orders that found a payment, once per payment row.
SELECT o.order_id, o.amount AS booked, p.payment_id, p.amount AS paid
FROM tiny_orders o
JOIN tiny_payments p ON p.order_id = o.order_id
ORDER BY o.order_id, p.payment_id;

-- Step 3. LEFT JOIN keeps every order, paid or not; an order with no payment gets NULLs on the right.
SELECT o.order_id, o.amount AS booked, p.payment_id, p.amount AS paid
FROM tiny_orders o
LEFT JOIN tiny_payments p ON p.order_id = o.order_id
ORDER BY o.order_id, p.payment_id;

-- Step 4. RIGHT JOIN keeps every payment, including one whose order is not in the orders table.
SELECT o.order_id, o.amount AS booked, p.payment_id, p.order_id AS paid_for, p.amount AS paid
FROM tiny_orders o
RIGHT JOIN tiny_payments p ON p.order_id = o.order_id
ORDER BY p.payment_id;

-- Step 5. FULL OUTER JOIN keeps the orphans from both sides. Named today, parked for later.
SELECT o.order_id, p.payment_id, p.order_id AS paid_for
FROM tiny_orders o
FULL JOIN tiny_payments p ON p.order_id = o.order_id
ORDER BY coalesce(o.order_id, p.order_id), p.payment_id;

-- Step 6. The four row counts side by side, so the prediction is checked in one table.
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

-- Step 7. The fan-out on the tiny tables: the order amount summed after the join.
-- Booked is 5,800. Read what the join reports as the value of the paid orders, and why.
SELECT sum(o.amount) AS value_of_paid_orders_after_join,
       (SELECT sum(amount) FROM tiny_orders) AS booked
FROM tiny_orders o
JOIN tiny_payments p ON p.order_id = o.order_id;

-- Step 8. The fix: payments brought to one row per order first, then joined at the same grain.
WITH paid_per_order AS (
    SELECT order_id, sum(amount) AS paid, count(*) AS payment_rows
    FROM tiny_payments
    GROUP BY order_id
)
SELECT o.order_id, o.amount AS booked, coalesce(pp.paid, 0) AS paid, pp.payment_rows
FROM tiny_orders o
LEFT JOIN paid_per_order pp ON pp.order_id = o.order_id
ORDER BY o.order_id;

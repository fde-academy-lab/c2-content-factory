-- Week 2, Tuesday. Chapter 4: Which Q2 orders were never paid, and which payments did the gateway post twice?
-- The unpaid list, the double-paid list and the payments with no order: first on the invented
-- tables, then on Kalpa's Q2. The Kalpa lists are yours to read.
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

-- The anti-join, invented: which orders have no payment?
SELECT o.order_id, o.channel, o.amount AS booked
FROM tiny_orders o
LEFT JOIN tiny_payments p ON p.order_id = o.order_id
WHERE p.order_id IS NULL
ORDER BY o.order_id;

-- Your turn: the unpaid list on Kalpa's Q2
SELECT o.order_id, o.channel, o.order_date, o.amount AS booked
FROM orders o
LEFT JOIN payments p ON p.order_id = o.order_id
WHERE o.quarter = 'Q2'
  AND p.order_id IS NULL
ORDER BY o.amount DESC;

-- Option B, NOT EXISTS, on Kalpa's Q2
SELECT o.order_id
FROM orders o
WHERE o.quarter = 'Q2'
  AND NOT EXISTS (SELECT 1 FROM payments p WHERE p.order_id = o.order_id);

-- Option C, NOT IN, on Kalpa's Q2
SELECT o.order_id
FROM orders o
WHERE o.quarter = 'Q2'
  AND o.order_id NOT IN (SELECT order_id FROM payments);

-- Option D, EXCEPT, on Kalpa's Q2
SELECT order_id FROM orders WHERE quarter = 'Q2'
EXCEPT
SELECT order_id FROM payments;

-- Why not NOT IN: one NULL in the subquery, invented
SELECT o.order_id
FROM tiny_orders o
WHERE o.order_id NOT IN (SELECT order_id FROM tiny_payments
                         UNION ALL
                         SELECT NULL);

-- The trap: the quarter's dates in WHERE, invented
SELECT o.order_id, p.payment_id, p.paid_date
FROM tiny_orders o
LEFT JOIN tiny_payments p ON p.order_id = o.order_id
WHERE p.paid_date BETWEEN '2026-07-01' AND '2026-09-30'
ORDER BY o.order_id, p.payment_id;

-- The trap's unpaid list, invented
SELECT o.order_id, o.amount AS booked
FROM tiny_orders o
LEFT JOIN tiny_payments p ON p.order_id = o.order_id
WHERE p.paid_date BETWEEN '2026-07-01' AND '2026-09-30'
  AND p.order_id IS NULL;

-- The fix: the dates in ON, invented
SELECT o.order_id, p.payment_id, p.paid_date
FROM tiny_orders o
LEFT JOIN tiny_payments p
       ON p.order_id = o.order_id
      AND p.paid_date BETWEEN '2026-07-01' AND '2026-09-30'
ORDER BY o.order_id, p.payment_id;

-- The fix's unpaid list, invented
SELECT o.order_id, o.amount AS booked
FROM tiny_orders o
LEFT JOIN tiny_payments p
       ON p.order_id = o.order_id
      AND p.paid_date BETWEEN '2026-07-01' AND '2026-09-30'
WHERE p.order_id IS NULL;

-- The trap: HAVING COUNT(*) > 1 by order on Kalpa's Q2
SELECT o.order_id, count(*) AS payment_rows
FROM orders o
JOIN payments p ON p.order_id = o.order_id
WHERE o.quarter = 'Q2'
GROUP BY o.order_id
HAVING count(*) > 1;

-- The same, invented, with what lies beyond one payment
SELECT p.order_id, count(*) AS payment_rows, sum(p.amount) - max(p.amount) AS beyond_one_payment
FROM tiny_payments p
JOIN tiny_orders o ON o.order_id = p.order_id
GROUP BY p.order_id
HAVING count(*) > 1
ORDER BY p.order_id;

-- The fix: order and instalment, invented
SELECT p.order_id, p.instalment_no, count(*) AS times_posted,
       sum(p.amount) - max(p.amount) AS posted_twice
FROM tiny_payments p
JOIN tiny_orders o ON o.order_id = p.order_id
GROUP BY p.order_id, p.instalment_no
HAVING count(*) > 1
ORDER BY p.order_id;

-- Your turn: the double-paid list on Kalpa's Q2
SELECT p.order_id, o.channel, p.instalment_no, count(*) AS times_posted,
       sum(p.amount) - max(p.amount) AS posted_twice
FROM payments p
JOIN orders o ON o.order_id = p.order_id
WHERE o.quarter = 'Q2'
GROUP BY p.order_id, o.channel, p.instalment_no
HAVING count(*) > 1
ORDER BY p.order_id;

-- Your turn: payments whose order is not in the orders table
SELECT p.payment_id, p.order_id AS paid_for, p.paid_date, p.method, p.amount
FROM payments p
LEFT JOIN orders o ON o.order_id = p.order_id
WHERE o.order_id IS NULL
ORDER BY p.payment_id;

-- Every payment row accounted for
SELECT coalesce(o.quarter, 'no order') AS home, count(*) AS payment_rows
FROM payments p
LEFT JOIN orders o ON o.order_id = p.order_id
GROUP BY coalesce(o.quarter, 'no order');

-- The second route: posted above booked, Kalpa's Q2
WITH posted_per_order AS (
    SELECT order_id, sum(amount) AS posted FROM payments GROUP BY order_id
)
SELECT o.order_id
FROM orders o
JOIN posted_per_order pp ON pp.order_id = o.order_id
WHERE o.quarter = 'Q2' AND pp.posted > o.amount;

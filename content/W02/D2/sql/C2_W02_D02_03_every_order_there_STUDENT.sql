-- Week 2, Tuesday. Chapter 3: Once nothing counts twice, is every booked order still in the report, and can every rupee between booked and posted be named?
-- Rows in, rows out at order grain, the plain JOIN draft on the invented tables, and the bridge
-- from booked to posted, first invented, then on Kalpa's Q2.
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

-- Rows in, rows out: the order-grain LEFT JOIN on Kalpa's Q2
WITH posted_per_order AS (
    SELECT order_id, sum(amount) AS posted
    FROM payments
    GROUP BY order_id
)
SELECT count(*) AS rows_out, count(DISTINCT o.order_id) AS orders_out, sum(o.amount) AS booked
FROM orders o
LEFT JOIN posted_per_order pp ON pp.order_id = o.order_id
WHERE o.quarter = 'Q2';

-- The trap: the plain JOIN draft on the invented tables
WITH posted_per_order AS (
    SELECT order_id, sum(amount) AS posted
    FROM tiny_payments
    GROUP BY order_id
)
SELECT count(*) AS orders, sum(o.amount) AS booked, sum(pp.posted) AS posted,
       sum(o.amount) - sum(pp.posted) AS gap
FROM tiny_orders o
JOIN posted_per_order pp ON pp.order_id = o.order_id;

-- The fix: LEFT JOIN on the invented tables
WITH posted_per_order AS (
    SELECT order_id, sum(amount) AS posted
    FROM tiny_payments
    GROUP BY order_id
)
SELECT count(*) AS orders, sum(o.amount) AS booked, sum(pp.posted) AS posted,
       sum(o.amount) - sum(pp.posted) AS gap
FROM tiny_orders o
LEFT JOIN posted_per_order pp ON pp.order_id = o.order_id;

-- Your turn: the plain JOIN on Kalpa's Q2; count its orders against 462
WITH posted_per_order AS (
    SELECT order_id, sum(amount) AS posted
    FROM payments
    GROUP BY order_id
)
SELECT count(*) AS orders, sum(o.amount) AS booked, sum(pp.posted) AS posted
FROM orders o
JOIN posted_per_order pp ON pp.order_id = o.order_id
WHERE o.quarter = 'Q2';

-- Booked, collected and posted per order, invented
WITH per_instalment AS (
    SELECT order_id, instalment_no, max(amount) AS amount
    FROM tiny_payments
    GROUP BY order_id, instalment_no
),
collected_per_order AS (
    SELECT order_id, sum(amount) AS collected
    FROM per_instalment
    GROUP BY order_id
),
posted_per_order AS (
    SELECT order_id, sum(amount) AS posted
    FROM tiny_payments
    GROUP BY order_id
)
SELECT o.order_id, o.channel, o.amount AS booked, c.collected, p.posted
FROM tiny_orders o
LEFT JOIN collected_per_order c ON c.order_id = o.order_id
LEFT JOIN posted_per_order p    ON p.order_id = o.order_id
ORDER BY o.order_id;

-- The bridge, invented
WITH per_order AS (
WITH per_instalment AS (
    SELECT order_id, instalment_no, max(amount) AS amount
    FROM tiny_payments
    GROUP BY order_id, instalment_no
),
collected_per_order AS (
    SELECT order_id, sum(amount) AS collected
    FROM per_instalment
    GROUP BY order_id
),
posted_per_order AS (
    SELECT order_id, sum(amount) AS posted
    FROM tiny_payments
    GROUP BY order_id
)
SELECT o.order_id, o.channel, o.amount AS booked, c.collected, p.posted
FROM tiny_orders o
LEFT JOIN collected_per_order c ON c.order_id = o.order_id
LEFT JOIN posted_per_order p    ON p.order_id = o.order_id
)
SELECT sum(booked)                                                    AS booked,
       sum(booked) FILTER (WHERE collected IS NULL)                   AS never_paid,
       sum(booked - collected) FILTER (WHERE collected < booked)      AS paid_short,
       sum(collected)                                                 AS collected,
       sum(posted - collected)                                        AS posted_twice,
       sum(posted)                                                    AS posted
FROM per_order;

-- Your turn: the bridge on Kalpa's Q2
WITH per_order AS (
WITH per_instalment AS (
    SELECT order_id, instalment_no, max(amount) AS amount
    FROM payments
    GROUP BY order_id, instalment_no
),
collected_per_order AS (
    SELECT order_id, sum(amount) AS collected
    FROM per_instalment
    GROUP BY order_id
),
posted_per_order AS (
    SELECT order_id, sum(amount) AS posted
    FROM payments
    GROUP BY order_id
)
SELECT o.order_id, o.channel, o.amount AS booked, c.collected, p.posted
FROM orders o
LEFT JOIN collected_per_order c ON c.order_id = o.order_id
LEFT JOIN posted_per_order p    ON p.order_id = o.order_id
WHERE o.quarter = 'Q2'
)
SELECT sum(booked)                                                    AS booked,
       sum(booked) FILTER (WHERE collected IS NULL)                   AS never_paid,
       sum(booked - collected) FILTER (WHERE collected < booked)      AS paid_short,
       sum(collected)                                                 AS collected,
       sum(posted - collected)                                        AS posted_twice,
       sum(posted)                                                    AS posted
FROM per_order;

-- Its end, from payments alone
SELECT sum(amount) AS posted
FROM payments
WHERE order_id IN (SELECT order_id FROM orders WHERE quarter = 'Q2');

-- The second route: capped at booked, invented
WITH posted_per_order AS (
    SELECT order_id, sum(amount) AS posted
    FROM tiny_payments
    GROUP BY order_id
)
SELECT o.order_id, o.amount AS booked, pp.posted, least(pp.posted, o.amount) AS capped
FROM tiny_orders o
JOIN posted_per_order pp ON pp.order_id = o.order_id
ORDER BY o.order_id;

-- The second route on Kalpa's Q2
WITH posted_per_order AS (
    SELECT order_id, sum(amount) AS posted
    FROM payments
    GROUP BY order_id
)
SELECT sum(least(pp.posted, o.amount)) AS collected_by_cap
FROM orders o
JOIN posted_per_order pp ON pp.order_id = o.order_id
WHERE o.quarter = 'Q2';

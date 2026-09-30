-- Week 2, Tuesday. Chapter 5: What goes on the report by channel that Anand signs, and does its gap column tell the truth?
-- The report by channel Anand signs: the hurried gap column, the fix, and the full page.
-- Run the Kalpa page yourself; the figures are yours to read.
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

-- Booked by channel, Kalpa's Q2, from orders alone
SELECT channel, count(*) AS orders, sum(amount) AS booked
FROM orders
WHERE quarter = 'Q2'
GROUP BY channel
ORDER BY channel;

-- The trap, invented: each order's gap added up
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
SELECT channel,
       count(*)                                  AS orders,
       sum(booked)                               AS booked,
       sum(collected)                            AS collected,
       sum(booked - collected)                 AS gap
FROM per_order
GROUP BY channel
ORDER BY channel;

-- The trap on Kalpa's Q2
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
SELECT channel,
       count(*)                                  AS orders,
       sum(booked)                               AS booked,
       sum(collected)                            AS collected,
       sum(booked - collected)                 AS gap
FROM per_order
GROUP BY channel
ORDER BY channel;

-- Why: one row per order, invented, where T-4's gap is NULL
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
SELECT order_id, channel, booked, collected, booked - collected AS gap
FROM per_order
ORDER BY order_id;

-- The fix, invented: coalesce(collected, 0)
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
SELECT channel,
       count(*)                                  AS orders,
       sum(booked)                               AS booked,
       sum(collected)                            AS collected,
       sum(booked - coalesce(collected, 0))                 AS gap
FROM per_order
GROUP BY channel
ORDER BY channel;

-- Your turn: the page Anand signs, Kalpa's Q2
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
SELECT channel,
       count(*)                                                AS orders,
       sum(booked)                                             AS booked,
       sum(coalesce(collected, 0))                             AS collected,
       sum(booked - coalesce(collected, 0))                    AS gap,
       round(100 * sum(coalesce(collected, 0)) / sum(booked), 2) AS collected_pct,
       count(*) FILTER (WHERE collected IS NULL)               AS unpaid_orders,
       sum(coalesce(posted, 0) - coalesce(collected, 0))       AS posted_twice
FROM per_order
GROUP BY channel
ORDER BY channel;

-- The second route: the unpaid list by channel, Kalpa's Q2
SELECT o.channel, sum(o.amount) AS never_paid
FROM orders o
WHERE o.quarter = 'Q2'
  AND NOT EXISTS (SELECT 1 FROM payments p WHERE p.order_id = o.order_id)
GROUP BY o.channel;

-- Refunds, by the quarter of their order
SELECT o.quarter, count(*) AS refund_rows
FROM refunds r
JOIN orders o ON o.order_id = r.order_id
GROUP BY o.quarter
ORDER BY o.quarter;

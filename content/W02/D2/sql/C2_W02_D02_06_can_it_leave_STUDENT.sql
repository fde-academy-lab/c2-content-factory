-- Week 2, Tuesday. Chapter 6: Which checks must pass before the collected number leaves the team, and what does Anand get when one fails at the end of reporting day?
-- The day's wrong reports rebuilt on the invented tables, the single-table sources the tie-back
-- checks compare with, and Kalpa's Q2 report with its sources.
-- Run it against the warehouse: psql -d kalpa -f this_file.sql

-- Setup: the two invented tables
DROP TABLE IF EXISTS pg_temp.tiny_orders, pg_temp.tiny_payments;
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

-- Setup: chapter 3's per-order table as TEMP views, invented and Kalpa's Q2
CREATE TEMP VIEW tiny_per_order AS
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
LEFT JOIN posted_per_order p    ON p.order_id = o.order_id;
CREATE TEMP VIEW q2_per_order AS
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
WHERE o.quarter = 'Q2';

-- A report to test, invented: fan-out draft
SELECT count(*) AS orders,
       (SELECT sum(amount) FROM tiny_orders) AS booked,
       sum(o.amount) FILTER (WHERE p.payment_id IS NOT NULL) AS collected,
       (SELECT sum(amount) FROM tiny_orders)
           - sum(o.amount) FILTER (WHERE p.payment_id IS NOT NULL) AS gap,
       array_agg(DISTINCT o.channel) AS channels
FROM tiny_orders o
LEFT JOIN tiny_payments p ON p.order_id = o.order_id;

-- A report to test, invented: plain JOIN draft
WITH posted_per_order AS (
    SELECT order_id, sum(amount) AS posted
    FROM tiny_payments
    GROUP BY order_id
)
SELECT count(*) AS orders, sum(o.amount) AS booked, sum(pp.posted) AS collected,
       sum(o.amount) - sum(pp.posted) AS gap, array_agg(DISTINCT o.channel) AS channels
FROM tiny_orders o
JOIN posted_per_order pp ON pp.order_id = o.order_id;

-- A report to test, invented: posted as collected
WITH posted_per_order AS (
    SELECT order_id, sum(amount) AS posted
    FROM tiny_payments
    GROUP BY order_id
)
SELECT count(*) AS orders, sum(o.amount) AS booked, sum(pp.posted) AS collected,
       sum(o.amount) - sum(pp.posted) AS gap, array_agg(DISTINCT o.channel) AS channels
FROM tiny_orders o
LEFT JOIN posted_per_order pp ON pp.order_id = o.order_id;

-- A report to test, invented: quarter in WHERE
WITH per_order AS (
    SELECT o.order_id, o.channel, o.amount AS booked, sum(i.amount) AS collected
    FROM tiny_orders o
    LEFT JOIN (SELECT order_id, instalment_no, max(amount) AS amount, max(paid_date) AS paid_date
               FROM tiny_payments
               GROUP BY order_id, instalment_no) i ON i.order_id = o.order_id
    WHERE i.paid_date BETWEEN '2026-07-01' AND '2026-09-30'
    GROUP BY o.order_id, o.channel, o.amount
)
SELECT count(*) AS orders, sum(booked) AS booked, sum(collected) AS collected,
       sum(booked) - sum(collected) AS gap, array_agg(DISTINCT channel) AS channels
FROM per_order;

-- A report to test, invented: gap summed per order
SELECT count(*) AS orders, sum(booked) AS booked, sum(collected) AS collected,
       sum(booked - collected) AS gap, array_agg(DISTINCT channel) AS channels
FROM tiny_per_order;

-- A report to test, invented: true report
SELECT count(*) AS orders, sum(booked) AS booked, sum(coalesce(collected, 0)) AS collected,
       sum(booked - coalesce(collected, 0)) AS gap, array_agg(DISTINCT channel) AS channels
FROM tiny_per_order;

-- The single-table sources, invented
SELECT (SELECT count(*) FROM tiny_orders o)                           AS orders,
       (SELECT sum(amount) FROM tiny_orders o)                        AS booked,
       (SELECT sum(amount) FROM tiny_payments
         WHERE order_id IN (SELECT order_id FROM tiny_orders o))      AS posted,
       (SELECT sum(amount) FROM tiny_orders o WHERE
            NOT EXISTS (SELECT 1 FROM tiny_payments p
                        WHERE p.order_id = o.order_id))                   AS never_paid,
       (SELECT sum(o.amount - c.collected)
          FROM tiny_orders o
          JOIN (SELECT order_id, sum(amount) AS collected
                  FROM (SELECT order_id, instalment_no, max(amount) AS amount
                          FROM tiny_payments
                         GROUP BY order_id, instalment_no) AS once
                 GROUP BY order_id) AS c ON c.order_id = o.order_id
         WHERE c.collected < o.amount)                              AS paid_short,
       (SELECT sum(extra)
          FROM (SELECT sum(p.amount) - max(p.amount) AS extra
                FROM tiny_payments p JOIN tiny_orders o ON o.order_id = p.order_id
                GROUP BY p.order_id, p.instalment_no) AS repeats)         AS posted_twice;

-- Kalpa's Q2 report, totals
SELECT count(*) AS orders, sum(booked) AS booked, sum(coalesce(collected, 0)) AS collected,
       sum(booked - coalesce(collected, 0)) AS gap, array_agg(DISTINCT channel) AS channels
FROM q2_per_order;

-- Kalpa's Q2 single-table sources
SELECT (SELECT count(*) FROM orders o WHERE o.quarter = 'Q2')                           AS orders,
       (SELECT sum(amount) FROM orders o WHERE o.quarter = 'Q2')                        AS booked,
       (SELECT sum(amount) FROM payments
         WHERE order_id IN (SELECT order_id FROM orders o WHERE o.quarter = 'Q2'))      AS posted,
       (SELECT sum(amount) FROM orders o WHERE o.quarter = 'Q2' AND
            NOT EXISTS (SELECT 1 FROM payments p
                        WHERE p.order_id = o.order_id))                   AS never_paid,
       (SELECT sum(o.amount - c.collected)
          FROM orders o
          JOIN (SELECT order_id, sum(amount) AS collected
                  FROM (SELECT order_id, instalment_no, max(amount) AS amount
                          FROM payments
                         GROUP BY order_id, instalment_no) AS once
                 GROUP BY order_id) AS c ON c.order_id = o.order_id
         WHERE o.quarter = 'Q2' AND c.collected < o.amount)                              AS paid_short,
       (SELECT sum(extra)
          FROM (SELECT sum(p.amount) - max(p.amount) AS extra
                FROM payments p JOIN orders o ON o.order_id = p.order_id WHERE o.quarter = 'Q2'
                GROUP BY p.order_id, p.instalment_no) AS repeats)         AS posted_twice;

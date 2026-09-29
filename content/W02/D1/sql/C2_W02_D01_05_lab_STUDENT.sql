-- The practice lab: the Monday tree by channel, and the predictions that come before it.
--
-- Anand asked for every segment and every channel. The suite covers segments; this file carries
-- the channel side. Predict before you run: problem 1 in exercises/practice/ asks for the row
-- count of the first four blocks before you run any of them.

-- name: lab_a
SELECT quarter, count(*) AS orders
FROM   orders
GROUP  BY quarter
ORDER  BY quarter;

-- name: lab_b
SELECT c.segment, o.quarter, count(*) AS orders
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment, o.quarter
ORDER  BY c.segment, o.quarter;

-- name: lab_c
SELECT c.segment, o.quarter, count(*) AS orders
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment, o.quarter
HAVING count(*) < 30
ORDER  BY c.segment, o.quarter;

-- name: lab_d
SELECT channel, status, count(*) AS orders
FROM   orders
WHERE  quarter = 'Q2' AND amount > 5000
GROUP  BY channel, status
ORDER  BY channel, status;

-- name: lab_channel_hurried
-- Problem 3: a colleague's channel query. Run it, then find what it gets wrong before trusting it.
SELECT channel,
       quarter,
       count(*)                  AS customers,
       sum(amount) / count(*)    AS revenue_per_order,
       count(*) / count(DISTINCT customer_id) AS orders_per_customer
FROM   orders
GROUP  BY channel, quarter
ORDER  BY channel, quarter;

-- name: lab_channel_tree
-- Problem 4: the channel tree, both quarters side by side, as two named steps.
WITH q1 AS (
    SELECT channel, count(DISTINCT customer_id) AS customers, count(*) AS orders,
           sum(amount) AS revenue
    FROM   orders
    WHERE  quarter = 'Q1'
    GROUP  BY channel
),
q2 AS (
    SELECT channel, count(DISTINCT customer_id) AS customers, count(*) AS orders,
           sum(amount) AS revenue
    FROM   orders
    WHERE  quarter = 'Q2'
    GROUP  BY channel
)
SELECT channel,
       q1.revenue AS q1_revenue,
       q2.revenue AS q2_revenue,
       q2.revenue - q1.revenue AS change,
       round(100 * (q2.revenue - q1.revenue) / q1.revenue, 1) AS change_pct,
       round(q1.orders::numeric / q1.customers, 2) AS q1_orders_per_customer,
       round(q2.orders::numeric / q2.customers, 2) AS q2_orders_per_customer
FROM   q1
JOIN   q2 USING (channel)
ORDER  BY channel;

-- name: lab_channel_split
-- Problem 4, second step: is a channel's move made of consumer orders or of Business orders?
SELECT o.channel,
       o.quarter,
       c.segment = 'Business' AS business,
       count(*)      AS orders,
       sum(o.amount) AS revenue
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY o.channel, o.quarter, c.segment = 'Business'
ORDER  BY o.channel, business, o.quarter;

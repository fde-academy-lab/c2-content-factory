-- Kalpa Retail, Week 2 Monday, round 2: the tree per segment and per quarter.
--
-- Anand asked for every segment. Last week a dictionary of running totals did this in a dozen
-- lines of Python; here it is GROUP BY. Run one block at a time.

-- name: r2_by_quarter
-- The question: orders and revenue per quarter, in one query instead of two.
SELECT quarter, count(*) AS orders, sum(amount) AS revenue
FROM   orders
GROUP  BY quarter
ORDER  BY quarter;

-- The error worth meeting once. Remove the two dashes in front of each line below and run it:
-- the database refuses, and the last line of the message says why. Put the dashes back after.
-- SELECT c.segment, o.quarter, count(*) AS orders
-- FROM   orders o JOIN customers c USING (customer_id)
-- GROUP  BY o.quarter;

-- name: r2_segment_quarter
-- The question: orders, customers who bought and revenue, per segment per quarter.
SELECT c.segment,
       o.quarter,
       count(*)                      AS orders,
       count(DISTINCT o.customer_id) AS customers,
       sum(o.amount)                 AS revenue
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment, o.quarter
ORDER  BY c.segment, o.quarter;

-- name: r2_frequency_hurried
-- The question: orders per customer, per segment per quarter. (The hurried version.)
SELECT c.segment,
       o.quarter,
       count(*) / count(DISTINCT o.customer_id) AS orders_per_customer
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment, o.quarter
ORDER  BY c.segment, o.quarter;

-- name: r2_frequency_check
-- The check: multiply the answer back. Orders per customer times customers must give the orders.
SELECT c.segment,
       o.quarter,
       count(*)                                  AS orders,
       count(DISTINCT o.customer_id)             AS customers,
       count(*) / count(DISTINCT o.customer_id)  AS hurried_ratio,
       (count(*) / count(DISTINCT o.customer_id)) * count(DISTINCT o.customer_id) AS orders_it_implies
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment, o.quarter
ORDER  BY c.segment, o.quarter;

-- name: r2_frequency_fixed
-- The fix: make one side numeric before dividing, then round for the reader.
SELECT c.segment,
       o.quarter,
       round(count(*)::numeric / count(DISTINCT o.customer_id), 2) AS orders_per_customer,
       round(sum(o.amount) / count(*))                            AS revenue_per_order
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment, o.quarter
ORDER  BY c.segment, o.quarter;

-- name: r2_thin_cells
-- The question: which segment-quarters hold fewer than 30 orders, too few to read a rate from?
-- WHERE filters rows before they are grouped; HAVING filters the groups after.
SELECT c.segment, o.quarter, count(*) AS orders
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment, o.quarter
HAVING count(*) < 30
ORDER  BY orders;

-- name: r2_delivered_by_segment
-- The harder variant: the same tree, delivered orders only. WHERE runs before GROUP BY.
SELECT c.segment,
       o.quarter,
       count(*)                                                    AS orders,
       count(DISTINCT o.customer_id)                               AS customers,
       round(count(*)::numeric / count(DISTINCT o.customer_id), 2) AS orders_per_customer,
       sum(o.amount)                                               AS revenue
FROM   orders o
JOIN   customers c USING (customer_id)
WHERE  o.status = 'delivered'
GROUP  BY c.segment, o.quarter
ORDER  BY c.segment, o.quarter;

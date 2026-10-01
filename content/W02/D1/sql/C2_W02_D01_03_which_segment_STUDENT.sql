-- Kalpa Retail, Week 2 Monday, chapter 3: which segment carried the fall, and how often did its
-- customers order?
--
-- Kalpa sells to four segments: Business (corporate buyers), Retail-Core (everyday shoppers),
-- Retail-Plus (the paid membership tier) and Student. The book fell 1.6 percent from Q1 to Q2, and
-- Anand's sheet needs the tree for every segment. The segment lives on the customer, so each order
-- looks up its customer's segment with one line, JOIN customers USING (customer_id). Joins are
-- Tuesday's topic; today the line is only a lookup.
--
-- Q1 is April to June 2026 and Q2 is July to September 2026. Revenue is booked revenue.

-- name: c3_one_segment
-- Option A, one query per segment: the Retail-Plus leaves for each quarter.
SELECT o.quarter,
       count(*)                      AS orders,
       count(DISTINCT o.customer_id) AS customers,
       sum(o.amount)                 AS revenue
FROM   orders o
JOIN   customers c USING (customer_id)
WHERE  c.segment = 'Retail-Plus'
GROUP  BY o.quarter
ORDER  BY o.quarter;

-- name: c3_group_error
-- The segment is selected but the grouping names only the quarter. This block stops with an error
-- on purpose: read its last line, then compare it with c3_segments below.
SELECT c.segment, o.quarter, count(*) AS orders
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY o.quarter;

-- name: c3_segments
-- The question: how many orders, customers and rupees did each segment book in each quarter?
-- One row per segment and quarter: 4 segments times 2 quarters.
SELECT c.segment,
       o.quarter,
       count(*)                      AS orders,
       count(DISTINCT o.customer_id) AS customers,
       sum(o.amount)                 AS revenue
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment, o.quarter
ORDER  BY c.segment, o.quarter;

-- name: c3_thin
-- The question: which segment-quarters hold fewer than 30 customers, too few to quote a rate on?
-- WHERE would test each order row; HAVING tests each group once it exists.
SELECT c.segment,
       o.quarter,
       count(DISTINCT o.customer_id) AS customers
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment, o.quarter
HAVING count(DISTINCT o.customer_id) < 30
ORDER  BY c.segment, o.quarter;

-- name: c3_frequency_hurried
-- The question: how often did each segment's customers order? (The quickest way to write it.)
SELECT c.segment,
       o.quarter,
       count(*) / count(DISTINCT o.customer_id) AS orders_per_customer
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment, o.quarter
ORDER  BY c.segment, o.quarter;

-- name: c3_integer_division
-- What 140 / 76 and 215 / 91 return when both sides are whole numbers, beside the numeric result.
SELECT 215 / 91          AS q1_integer,
       140 / 76          AS q2_integer,
       215::numeric / 91 AS q1_numeric,
       140::numeric / 76 AS q2_numeric;

-- name: c3_frequency
-- The fix: divide in numeric, round on purpose to two places, and keep the counts beside the ratio
-- so anyone can multiply it back.
SELECT c.segment,
       o.quarter,
       count(*)                                                    AS orders,
       count(DISTINCT o.customer_id)                               AS customers,
       round(count(*)::numeric / count(DISTINCT o.customer_id), 2) AS orders_per_customer,
       round(sum(o.amount) / count(*))                             AS revenue_per_order
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment, o.quarter
ORDER  BY c.segment, o.quarter;

-- name: c3_per_customer_counts
-- The second route: each customer's own order count in each quarter, one row per customer and
-- quarter, for Python to average.
SELECT c.segment,
       o.quarter,
       o.customer_id,
       count(*) AS orders
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment, o.quarter, o.customer_id
ORDER  BY c.segment, o.quarter, o.customer_id;

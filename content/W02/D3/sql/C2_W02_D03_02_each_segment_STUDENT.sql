-- Kalpa Retail, Week 2 Wednesday, chapter 2: which fifty members lead each segment?
--
-- Marketing asked for "the top fifty customers by Q2 revenue in each segment". Kalpa sells to four
-- segments: Business (corporate buyers, whose orders run to lakhs), Retail-Core (everyday
-- shoppers), Retail-Plus (the paid membership tier) and Student. Chapter 1 ranked the whole book
-- in one list of fifty. This file builds one list per segment and checks every count.
--
-- Q2 is July to September 2026. Q2 revenue is booked revenue, every order at its amount whatever its
-- status. The segment lives on the customer, so each order looks it up with
-- JOIN customers c USING (customer_id), which finds one customer per order and adds no rows.

-- name: c2_groupby_segment
-- First attempt with GROUP BY: one group per segment. What comes back?
SELECT c.segment,
       count(DISTINCT o.customer_id) AS members_who_bought,
       sum(o.amount)                 AS q2_revenue
FROM   orders o
JOIN   customers c USING (customer_id)
WHERE  o.quarter = 'Q2'
GROUP  BY c.segment
ORDER  BY c.segment;

-- name: c2_groupby_limit
-- The second attempt with GROUP BY makes one group per member, sorts the groups by Q2 revenue and
-- keeps fifty with LIMIT 50; the outer query counts the fifty by segment.
WITH fifty AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
    ORDER  BY q2_revenue DESC, o.customer_id
    LIMIT  50
)
SELECT segment, count(*) AS on_the_list
FROM   fifty
GROUP  BY segment
ORDER  BY on_the_list DESC;

-- name: c2_whole_table_split
-- The hurried per-segment list: number the whole book once, then keep each segment's members whose
-- number is 50 or less.
WITH q2_spend AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
),
ranked AS (
    SELECT segment, customer_id, q2_revenue,
           row_number() OVER (ORDER BY q2_revenue DESC, customer_id) AS position
    FROM   q2_spend
)
SELECT segment,
       count(*) FILTER (WHERE position <= 50) AS on_the_segment_list,
       count(*)                               AS members_who_bought
FROM   ranked
GROUP  BY segment
ORDER  BY segment;

-- name: c2_partitioned
-- The per-segment list: PARTITION BY segment restarts the numbering at 1 inside every segment.
WITH q2_spend AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
),
ranked AS (
    SELECT segment, customer_id, q2_revenue,
           row_number() OVER (PARTITION BY segment
                              ORDER BY q2_revenue DESC, customer_id) AS position
    FROM   q2_spend
)
SELECT segment,
       count(*) FILTER (WHERE position <= 50) AS on_the_segment_list,
       count(*)                               AS members_who_bought
FROM   ranked
GROUP  BY segment
ORDER  BY segment;

-- name: c2_first_three
-- The question: what do the first three positions of Retail-Core, Retail-Plus and Student look like?
WITH q2_spend AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
),
ranked AS (
    SELECT segment, customer_id, q2_revenue,
           row_number() OVER (PARTITION BY segment
                              ORDER BY q2_revenue DESC, customer_id) AS position
    FROM   q2_spend
)
SELECT segment, position, customer_id, q2_revenue
FROM   ranked
WHERE  position <= 3 AND segment <> 'Business'
ORDER  BY segment, position;

-- name: c2_where_error
-- The position filter written straight into WHERE. This block stops with an error on purpose: read
-- its last line, then compare it with c2_partitioned, which filters in a later step.
SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue,
       row_number() OVER (PARTITION BY c.segment ORDER BY sum(o.amount) DESC) AS position
FROM   orders o
JOIN   customers c USING (customer_id)
WHERE  o.quarter = 'Q2'
  AND  row_number() OVER (PARTITION BY c.segment ORDER BY sum(o.amount) DESC) <= 50
GROUP  BY c.segment, o.customer_id;

-- name: c2_list_revenue
-- The question: how much Q2 revenue does each segment's list carry, against the whole segment?
WITH q2_spend AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
),
ranked AS (
    SELECT segment, q2_revenue,
           row_number() OVER (PARTITION BY segment
                              ORDER BY q2_revenue DESC, customer_id) AS position
    FROM   q2_spend
)
SELECT segment,
       sum(q2_revenue) FILTER (WHERE position <= 50) AS list_revenue,
       sum(q2_revenue)                               AS segment_revenue
FROM   ranked
GROUP  BY segment
ORDER  BY segment;

-- name: c2_union
-- The second route, with no window at all: one sorted query per segment, each keeping fifty, glued
-- together with UNION ALL. Each piece sits in brackets so its ORDER BY and LIMIT apply to it alone.
(SELECT 'Business' AS segment, o.customer_id, sum(o.amount) AS q2_revenue
 FROM orders o JOIN customers c USING (customer_id)
 WHERE o.quarter = 'Q2' AND c.segment = 'Business'
 GROUP BY o.customer_id ORDER BY q2_revenue DESC, o.customer_id LIMIT 50)
UNION ALL
(SELECT 'Retail-Core', o.customer_id, sum(o.amount)
 FROM orders o JOIN customers c USING (customer_id)
 WHERE o.quarter = 'Q2' AND c.segment = 'Retail-Core'
 GROUP BY o.customer_id ORDER BY sum(o.amount) DESC, o.customer_id LIMIT 50)
UNION ALL
(SELECT 'Retail-Plus', o.customer_id, sum(o.amount)
 FROM orders o JOIN customers c USING (customer_id)
 WHERE o.quarter = 'Q2' AND c.segment = 'Retail-Plus'
 GROUP BY o.customer_id ORDER BY sum(o.amount) DESC, o.customer_id LIMIT 50)
UNION ALL
(SELECT 'Student', o.customer_id, sum(o.amount)
 FROM orders o JOIN customers c USING (customer_id)
 WHERE o.quarter = 'Q2' AND c.segment = 'Student'
 GROUP BY o.customer_id ORDER BY sum(o.amount) DESC, o.customer_id LIMIT 50);

-- name: c2_window_ids
-- The window's list as ids, for the comparison with the second route.
WITH q2_spend AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
),
ranked AS (
    SELECT segment, customer_id,
           row_number() OVER (PARTITION BY segment
                              ORDER BY q2_revenue DESC, customer_id) AS position
    FROM   q2_spend
)
SELECT segment, customer_id
FROM   ranked
WHERE  position <= 50;

-- Kalpa Retail, Week 2 Monday, chapter 5: do the suite's numbers add up the way Anand's analyst
-- will add them?
--
-- Anand's analyst audits the Monday suite line by line, and the first thing an auditor does is add:
-- do the segments add back to the book, and do the two quarters add to the half-year? Orders and
-- rupees add. This file finds out whether customers do.
--
-- Q1 is April to June 2026 and Q2 is July to September 2026; the half-year is both. Customers are
-- the customers who bought in the window, each counted once. Revenue is booked revenue. The segment
-- is looked up from the customer with JOIN customers USING (customer_id); joins are Tuesday's topic.

-- name: c5_per_quarter
-- The suite's middle table: the leaves for each segment and quarter.
SELECT c.segment,
       o.quarter,
       count(*)                      AS orders,
       count(DISTINCT o.customer_id) AS customers,
       sum(o.amount)                 AS revenue
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment, o.quarter
ORDER  BY c.segment, o.quarter;

-- name: c5_tie_out_segments
-- The first tie-out: in each quarter, do the four segments add back to the book?
WITH per_quarter AS (
    SELECT c.segment, o.quarter, count(*) AS orders,
           count(DISTINCT o.customer_id) AS customers, sum(o.amount) AS revenue
    FROM   orders o JOIN customers c USING (customer_id)
    GROUP  BY c.segment, o.quarter
),
segments_added AS (
    SELECT quarter, sum(orders) AS orders, sum(customers) AS customers, sum(revenue) AS revenue
    FROM   per_quarter
    GROUP  BY quarter
),
book AS (
    SELECT quarter, count(*) AS orders, count(DISTINCT customer_id) AS customers,
           sum(amount) AS revenue
    FROM   orders
    GROUP  BY quarter
)
SELECT s.quarter,
       s.orders    AS segments_orders,    b.orders    AS book_orders,
       s.customers AS segments_customers, b.customers AS book_customers,
       s.revenue   AS segments_revenue,   b.revenue   AS book_revenue
FROM   segments_added s
JOIN   book b USING (quarter)
ORDER  BY s.quarter;

-- name: c5_half_year_hurried
-- The half-year column, the quickest way: add each segment's two quarter rows.
WITH per_quarter AS (
    SELECT c.segment, o.quarter, count(*) AS orders,
           count(DISTINCT o.customer_id) AS customers, sum(o.amount) AS revenue
    FROM   orders o JOIN customers c USING (customer_id)
    GROUP  BY c.segment, o.quarter
)
SELECT segment,
       sum(orders)    AS orders,
       sum(customers) AS customers,
       sum(revenue)   AS revenue
FROM   per_quarter
GROUP  BY segment
ORDER  BY segment;

-- name: c5_members
-- The check: how many members does each segment hold on the customer table, bought or not?
SELECT segment, count(*) AS members_on_the_book
FROM   customers
GROUP  BY segment
ORDER  BY segment;

-- name: c5_half_year
-- The fix: count the half-year's customers from the orders themselves, each counted once.
SELECT c.segment,
       count(*)                      AS orders,
       count(DISTINCT o.customer_id) AS customers,
       sum(o.amount)                 AS revenue
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment
ORDER  BY c.segment;

-- name: c5_overlap
-- The second route: per segment, how many customers bought in both quarters?
WITH per_customer AS (
    SELECT c.segment, o.customer_id, count(DISTINCT o.quarter) AS quarters_bought
    FROM   orders o JOIN customers c USING (customer_id)
    GROUP  BY c.segment, o.customer_id
)
SELECT segment,
       count(*) FILTER (WHERE quarters_bought = 2) AS bought_in_both
FROM   per_customer
GROUP  BY segment
ORDER  BY segment;

-- name: c5_grouping_sets
-- Depth: one query that returns every segment's quarter rows and its half-year row, each counted
-- from the orders. A NULL quarter marks the half-year row.
SELECT c.segment,
       o.quarter,
       count(*)                      AS orders,
       count(DISTINCT o.customer_id) AS customers,
       sum(o.amount)                 AS revenue
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY GROUPING SETS ((c.segment, o.quarter), (c.segment))
ORDER  BY c.segment, o.quarter NULLS LAST;

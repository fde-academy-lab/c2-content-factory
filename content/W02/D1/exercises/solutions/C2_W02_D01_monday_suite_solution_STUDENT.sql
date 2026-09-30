-- The Monday suite, solved. Six queries that reproduce Week 1's revenue tree by segment and quarter.
--
-- Revenue here is booked revenue: every order whatever its status, the definition Week 1's
-- reconciliation used. A customer is a customer who placed at least one order in the window. Every
-- ratio is computed in numeric, never in integers, and every list carries an ORDER BY.

-- name: suite_1_book
-- 1. What did each quarter book, in orders and rupees, and what did it change by?
SELECT quarter,
       count(*)    AS orders,
       sum(amount) AS revenue,
       round(100 * sum(amount) / (SELECT sum(amount) FROM orders WHERE quarter = 'Q1') - 100, 1)
                   AS change_vs_q1_pct
FROM   orders
GROUP  BY quarter
ORDER  BY quarter;

-- name: suite_2_customers
-- 2. How many customers bought in each quarter, against the members on the book?
SELECT quarter,
       count(DISTINCT customer_id)      AS customers_who_bought,
       (SELECT count(*) FROM customers) AS customers_on_the_book
FROM   orders
GROUP  BY quarter
ORDER  BY quarter;

-- name: suite_3_segment_leaves
-- 3. The leaves per segment per quarter: customers, orders per customer, revenue per order, revenue.
SELECT c.segment,
       o.quarter,
       count(DISTINCT o.customer_id)                               AS customers,
       round(count(*)::numeric / count(DISTINCT o.customer_id), 2) AS orders_per_customer,
       round(sum(o.amount) / count(*))                             AS revenue_per_order,
       sum(o.amount)                                               AS revenue
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment, o.quarter
ORDER  BY c.segment, o.quarter;

-- name: suite_4_typical_order
-- 4. The typical order per segment per quarter: the median beside the mean, because one bulk order
-- moves a mean.
SELECT c.segment,
       o.quarter,
       percentile_cont(0.5) WITHIN GROUP (ORDER BY o.amount) AS median_order,
       round(avg(o.amount))                                 AS mean_order
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment, o.quarter
ORDER  BY c.segment, o.quarter;

-- name: suite_5_thin_cells
-- 5. Which segment-quarters hold fewer than 30 orders, so their rates carry a warning?
SELECT c.segment, o.quarter, count(*) AS orders
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment, o.quarter
HAVING count(*) < 30
ORDER  BY c.segment, o.quarter;

-- name: suite_6_what_moved
-- 6. Which branch moved in each segment from Q1 to Q2, as percentage changes?
WITH q1 AS (
    SELECT c.segment, count(DISTINCT o.customer_id) AS customers, count(*) AS orders,
           sum(o.amount) AS revenue
    FROM   orders o JOIN customers c USING (customer_id)
    WHERE  o.quarter = 'Q1'
    GROUP  BY c.segment
),
q2 AS (
    SELECT c.segment, count(DISTINCT o.customer_id) AS customers, count(*) AS orders,
           sum(o.amount) AS revenue
    FROM   orders o JOIN customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment
)
SELECT segment,
       round(100 * (q2.customers - q1.customers)::numeric / q1.customers, 1) AS customers_pct,
       round(100 * ((q2.orders::numeric / q2.customers) / (q1.orders::numeric / q1.customers) - 1), 1)
                                                                            AS frequency_pct,
       round(100 * ((q2.revenue / q2.orders) / (q1.revenue / q1.orders) - 1), 1) AS order_value_pct,
       round(100 * (q2.revenue - q1.revenue) / q1.revenue, 1)              AS revenue_pct
FROM   q1
JOIN   q2 USING (segment)
ORDER  BY segment;

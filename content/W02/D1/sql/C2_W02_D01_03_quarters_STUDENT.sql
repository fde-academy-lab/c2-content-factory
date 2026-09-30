-- Kalpa Retail, Week 2 Monday, round 3: the two quarters side by side, as named steps.
--
-- Anand's analyst reads a query top to bottom. A CTE is a named step: each WITH block says what it
-- computes, and the last SELECT reads like the sentence that goes to Anand. Run one block at a time.

-- name: r3_share_subquery
-- The question: what share of the two quarters' revenue does each segment carry?
-- The total sits in a subquery, a query inside a query.
SELECT c.segment,
       sum(o.amount) AS revenue,
       round(100 * sum(o.amount) / (SELECT sum(amount) FROM orders), 1) AS share_pct
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment
ORDER  BY revenue DESC;

-- name: r3_two_quarters
-- The question: which branch of the tree moved in each segment from Q1 to Q2?
-- Step q1 and step q2 compute the same leaves for one quarter each; the last step lines them up.
WITH q1 AS (
    SELECT c.segment,
           count(DISTINCT o.customer_id) AS customers,
           count(*)                      AS orders,
           sum(o.amount)                 AS revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q1'
    GROUP  BY c.segment
),
q2 AS (
    SELECT c.segment,
           count(DISTINCT o.customer_id) AS customers,
           count(*)                      AS orders,
           sum(o.amount)                 AS revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment
)
SELECT segment,
       q1.customers AS q1_customers,
       q2.customers AS q2_customers,
       round(q1.orders::numeric / q1.customers, 2) AS q1_orders_per_customer,
       round(q2.orders::numeric / q2.customers, 2) AS q2_orders_per_customer,
       round(q1.revenue / q1.orders)              AS q1_revenue_per_order,
       round(q2.revenue / q2.orders)              AS q2_revenue_per_order,
       round(100 * (q2.revenue - q1.revenue) / q1.revenue, 1) AS revenue_change_pct
FROM   q1
JOIN   q2 USING (segment)
ORDER  BY segment;

-- name: r3_member_spend_hurried
-- The question: how did average spend per Retail-Plus member move from Q1 to Q2? (The hurried version.)
WITH member AS (
    SELECT o.customer_id,
           sum(CASE WHEN o.quarter = 'Q1' THEN o.amount END) AS q1_spend,
           sum(CASE WHEN o.quarter = 'Q2' THEN o.amount END) AS q2_spend
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  c.segment = 'Retail-Plus'
    GROUP  BY o.customer_id
)
SELECT round(avg(q1_spend)) AS avg_q1_spend,
       round(avg(q2_spend)) AS avg_q2_spend,
       round(100 * (avg(q2_spend) - avg(q1_spend)) / avg(q1_spend), 1) AS change_pct
FROM   member;

-- name: r3_member_spend_check
-- The check: how many members does each average actually divide by?
WITH member AS (
    SELECT o.customer_id,
           sum(CASE WHEN o.quarter = 'Q1' THEN o.amount END) AS q1_spend,
           sum(CASE WHEN o.quarter = 'Q2' THEN o.amount END) AS q2_spend
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  c.segment = 'Retail-Plus'
    GROUP  BY o.customer_id
)
SELECT count(*)        AS members,
       count(q1_spend) AS members_in_q1_average,
       count(q2_spend) AS members_in_q2_average
FROM   member;

-- name: r3_member_spend_fixed
-- The fix: a member who bought nothing in a quarter spent Rs 0 in it, said on purpose.
WITH member AS (
    SELECT o.customer_id,
           coalesce(sum(CASE WHEN o.quarter = 'Q1' THEN o.amount END), 0) AS q1_spend,
           coalesce(sum(CASE WHEN o.quarter = 'Q2' THEN o.amount END), 0) AS q2_spend
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  c.segment = 'Retail-Plus'
    GROUP  BY o.customer_id
)
SELECT count(*)             AS members,
       round(avg(q1_spend)) AS avg_q1_spend,
       round(avg(q2_spend)) AS avg_q2_spend,
       round(100 * (avg(q2_spend) - avg(q1_spend)) / avg(q1_spend), 1) AS change_pct
FROM   member;

-- name: r3_invented_null
-- The mechanism on three invented values, which are not Kalpa data: AVG divides by the values it
-- can see, and COUNT(*) counts every row.
SELECT avg(spend)      AS avg_spend,
       count(*)        AS rows_in_table,
       count(spend)    AS values_averaged,
       sum(spend) / count(*) AS sum_over_rows
FROM   (VALUES (100), (NULL), (200)) AS invented (spend);

-- name: r3_member_spend_by_segment
-- The harder variant: the same honest average for every segment, one row each.
WITH member AS (
    SELECT o.customer_id,
           c.segment,
           coalesce(sum(CASE WHEN o.quarter = 'Q1' THEN o.amount END), 0) AS q1_spend,
           coalesce(sum(CASE WHEN o.quarter = 'Q2' THEN o.amount END), 0) AS q2_spend
    FROM   orders o
    JOIN   customers c USING (customer_id)
    GROUP  BY o.customer_id, c.segment
)
SELECT segment,
       count(*)             AS members,
       round(avg(q1_spend)) AS avg_q1_spend,
       round(avg(q2_spend)) AS avg_q2_spend,
       round(100 * (avg(q2_spend) - avg(q1_spend)) / avg(q1_spend), 1) AS change_pct
FROM   member
GROUP  BY segment
ORDER  BY segment;

-- Kalpa Retail, Week 2 Monday, chapter 4: which branch of each segment's tree moved, and how much
-- less did each Retail-Plus member spend?
--
-- The tree: revenue = customers x orders per customer x revenue per order. Chapter 3 put each leaf
-- on its own row per segment and quarter. Anand's analyst wants Q1 and Q2 side by side in one query
-- that reads top to bottom, and the head of Retail-Plus asks how much less each member spent.
--
-- Q1 is April to June 2026 and Q2 is July to September 2026. Revenue is booked revenue. The segment
-- is looked up from the customer with JOIN customers USING (customer_id); joins are Tuesday's topic.

-- name: c4_nested
-- Option 1, nested subqueries: the Q1 and Q2 leaves per segment, read from the inside out.
SELECT q1.segment,
       q1.customers AS q1_customers, q2.customers AS q2_customers,
       q1.orders    AS q1_orders,    q2.orders    AS q2_orders,
       q1.revenue   AS q1_revenue,   q2.revenue   AS q2_revenue
FROM   (SELECT c.segment, count(DISTINCT o.customer_id) AS customers,
               count(*) AS orders, sum(o.amount) AS revenue
        FROM   orders o JOIN customers c USING (customer_id)
        WHERE  o.quarter = 'Q1'
        GROUP  BY c.segment) AS q1
JOIN   (SELECT c.segment, count(DISTINCT o.customer_id) AS customers,
               count(*) AS orders, sum(o.amount) AS revenue
        FROM   orders o JOIN customers c USING (customer_id)
        WHERE  o.quarter = 'Q2'
        GROUP  BY c.segment) AS q2
       USING (segment)
ORDER  BY q1.segment;

-- name: c4_branches
-- Option 2, named steps: the same comparison as three CTEs, read from the top down.
WITH book AS (      -- step 1: each order with its customer's segment
    SELECT o.order_id, o.customer_id, o.quarter, o.amount, c.segment
    FROM   orders o
    JOIN   customers c USING (customer_id)
),
q1 AS (             -- step 2: the Q1 leaves per segment
    SELECT segment, count(DISTINCT customer_id) AS customers,
           count(*) AS orders, sum(amount) AS revenue
    FROM   book
    WHERE  quarter = 'Q1'
    GROUP  BY segment
),
q2 AS (             -- step 3: the Q2 leaves per segment
    SELECT segment, count(DISTINCT customer_id) AS customers,
           count(*) AS orders, sum(amount) AS revenue
    FROM   book
    WHERE  quarter = 'Q2'
    GROUP  BY segment
)
SELECT segment,                                                  -- step 4: each branch's Q2 over Q1
       round(q2.customers::numeric / q1.customers, 3)                      AS customers_ratio,
       round((q2.orders::numeric / q2.customers)
             / (q1.orders::numeric / q1.customers), 3)                     AS frequency_ratio,
       round((q2.revenue / q2.orders) / (q1.revenue / q1.orders), 3)       AS order_value_ratio,
       round(q2.revenue / q1.revenue, 3)                                   AS revenue_ratio
FROM   q1
JOIN   q2 USING (segment)
ORDER  BY segment;

-- name: c4_temp_step
-- Option 3, a temporary table: the Q1 leaves written into a table that lives only for this session.
CREATE TEMP TABLE q1_leaves AS
SELECT c.segment, count(DISTINCT o.customer_id) AS customers,
       count(*) AS orders, sum(o.amount) AS revenue
FROM   orders o JOIN customers c USING (customer_id)
WHERE  o.quarter = 'Q1'
GROUP  BY c.segment;

-- name: c4_temp_read
-- The temporary table read back. In the same session it answers; in a new session it is gone.
SELECT * FROM q1_leaves ORDER BY segment;

-- name: c4_member_spend_hurried
-- The question: how much did a Retail-Plus member spend in each quarter, on average?
-- (The quickest way to write it.) One row per member who bought in either quarter.
WITH member_spend AS (
    SELECT o.customer_id,
           sum(CASE WHEN o.quarter = 'Q1' THEN o.amount END) AS q1_spend,
           sum(CASE WHEN o.quarter = 'Q2' THEN o.amount END) AS q2_spend
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  c.segment = 'Retail-Plus'
    GROUP  BY o.customer_id
)
SELECT round(avg(q1_spend)) AS q1_average,
       round(avg(q2_spend)) AS q2_average
FROM   member_spend;

-- name: c4_who_is_averaged
-- The check: how many members does the step hold, and how many are inside each average?
WITH member_spend AS (
    SELECT o.customer_id,
           sum(CASE WHEN o.quarter = 'Q1' THEN o.amount END) AS q1_spend,
           sum(CASE WHEN o.quarter = 'Q2' THEN o.amount END) AS q2_spend
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  c.segment = 'Retail-Plus'
    GROUP  BY o.customer_id
)
SELECT count(*)        AS members_in_the_step,
       count(q1_spend) AS inside_the_q1_average,
       count(q2_spend) AS inside_the_q2_average
FROM   member_spend;

-- name: c4_invented_null
-- The mechanism on three invented values, 100, a missing value and 200. Invented, not Kalpa's data.
SELECT avg(x)              AS average_skipping_null,
       avg(coalesce(x, 0)) AS average_with_zero,
       count(*)            AS rows,
       count(x)            AS values_present
FROM   (VALUES (100), (NULL), (200)) AS invented(x);

-- name: c4_member_spend
-- The fix: a member who bought nothing in a quarter spent Rs 0 there, said on purpose, so both
-- averages cover the same members.
WITH member_spend AS (
    SELECT o.customer_id,
           coalesce(sum(CASE WHEN o.quarter = 'Q1' THEN o.amount END), 0) AS q1_spend,
           coalesce(sum(CASE WHEN o.quarter = 'Q2' THEN o.amount END), 0) AS q2_spend
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  c.segment = 'Retail-Plus'
    GROUP  BY o.customer_id
)
SELECT count(*)             AS members,
       round(avg(q1_spend)) AS q1_average,
       round(avg(q2_spend)) AS q2_average
FROM   member_spend;

-- name: c4_every_segment
-- The same two averages for every segment: skipping the empty quarter, and with Rs 0 said on purpose.
WITH member_spend AS (
    SELECT c.segment,
           o.customer_id,
           sum(CASE WHEN o.quarter = 'Q1' THEN o.amount END) AS q1_spend,
           sum(CASE WHEN o.quarter = 'Q2' THEN o.amount END) AS q2_spend
    FROM   orders o
    JOIN   customers c USING (customer_id)
    GROUP  BY c.segment, o.customer_id
)
SELECT segment,
       count(*)                          AS members,
       round(avg(q1_spend))              AS q1_skipping,
       round(avg(q2_spend))              AS q2_skipping,
       round(avg(coalesce(q1_spend, 0))) AS q1_with_zero,
       round(avg(coalesce(q2_spend, 0))) AS q2_with_zero
FROM   member_spend
GROUP  BY segment
ORDER  BY segment;

-- name: c4_per_member_of_the_tier
-- The second route: Retail-Plus revenue in each quarter over every member on the tier's book,
-- bought or not. The count of members comes from the customer table, in a subquery.
SELECT o.quarter,
       sum(o.amount)                                                     AS revenue,
       (SELECT count(*) FROM customers WHERE segment = 'Retail-Plus')    AS members_on_the_book,
       round(sum(o.amount)
             / (SELECT count(*) FROM customers WHERE segment = 'Retail-Plus')) AS spend_per_member
FROM   orders o
JOIN   customers c USING (customer_id)
WHERE  c.segment = 'Retail-Plus'
GROUP  BY o.quarter
ORDER  BY o.quarter;

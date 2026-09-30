-- Kalpa Retail, Week 2, Wednesday. Round 1: the top fifty, per segment.
--
-- "Give us the top fifty customers by Q2 revenue in each segment, and flag anyone whose monthly
--  spend has fallen for two months running." Marketing.
--
-- Q2 revenue per member is the booked amount of the member's Q2 orders, the definition Monday's
-- suite used for the quarter total of Rs 9,84,00,000. Run the file a block at a time and read the
-- row count under every result before you read the names.

-- ---------------------------------------------------------------- 1. one row per member
-- The question: how much did each member book in Q2, and in which segment?
SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue
FROM   orders o
JOIN   customers c USING (customer_id)
WHERE  o.quarter = 'Q2'
GROUP  BY c.segment, o.customer_id
ORDER  BY q2_revenue DESC
LIMIT  10;

-- ---------------------------------------------------------------- 2. the hurried top fifty
-- The question Marketing asked was per segment. This answers a different one: the fifty biggest
-- members in the whole book. Count what it hands Marketing, segment by segment.
WITH q2 AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
),
top_fifty AS (
    SELECT * FROM q2 ORDER BY q2_revenue DESC, customer_id LIMIT 50
)
SELECT segment, count(*) AS members_on_the_list
FROM   top_fifty
GROUP  BY segment
ORDER  BY members_on_the_list DESC;

-- ---------------------------------------------------------------- 3. the check that was free
-- The question: how many members does each segment have to rank at all?
-- A segment with fewer than fifty Q2 buyers cannot have a top fifty; its list is everyone.
SELECT c.segment, count(DISTINCT o.customer_id) AS q2_buyers, sum(o.amount) AS q2_revenue
FROM   orders o
JOIN   customers c USING (customer_id)
WHERE  o.quarter = 'Q2'
GROUP  BY c.segment
ORDER  BY q2_revenue DESC;

-- ---------------------------------------------------------------- 4. a window keeps every row
-- The question: where does each member stand inside their own segment?
-- PARTITION BY restarts the count for every segment; ORDER BY inside the window sets who is first.
-- customer_id breaks an exact tie, so two runs of this query give the same numbers.
WITH q2 AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
)
SELECT segment, customer_id, q2_revenue,
       row_number() OVER (PARTITION BY segment ORDER BY q2_revenue DESC, customer_id) AS position
FROM   q2
ORDER  BY segment, position
LIMIT  12;

-- ---------------------------------------------------------------- 5. keep the first fifty
-- A window cannot sit inside WHERE, because WHERE runs before the window is computed. Postgres
-- says so in one line: ERROR:  window functions are not allowed in WHERE. The fix is a named
-- step: compute the position in a CTE, then filter the CTE.
WITH q2 AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
),
ranked AS (
    SELECT segment, customer_id, q2_revenue,
           row_number() OVER (PARTITION BY segment ORDER BY q2_revenue DESC, customer_id) AS position
    FROM   q2
)
SELECT segment, count(*) AS members_on_the_list, sum(q2_revenue) AS revenue_on_the_list
FROM   ranked
WHERE  position <= 50
GROUP  BY segment
ORDER  BY segment;

-- ---------------------------------------------------------------- 6. what the list covers
-- The question Marketing will ask next: how much of each segment's Q2 revenue sits on its list?
WITH q2 AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
),
ranked AS (
    SELECT q2.*,
           row_number() OVER (PARTITION BY segment ORDER BY q2_revenue DESC, customer_id) AS position,
           sum(q2_revenue) OVER (PARTITION BY segment) AS segment_revenue
    FROM   q2
)
SELECT segment,
       count(*) FILTER (WHERE position <= 50) AS on_the_list,
       count(*) AS q2_buyers,
       round(100.0 * sum(q2_revenue) FILTER (WHERE position <= 50) / max(segment_revenue), 1)
           AS share_of_segment_revenue_pct
FROM   ranked
GROUP  BY segment
ORDER  BY segment;

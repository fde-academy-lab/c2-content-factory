-- Kalpa Retail, Wednesday of Week 2. The guided walk.
--
-- "Give us the top fifty customers by Q2 revenue in each segment, and flag anyone whose monthly
--  spend has fallen for two months running." Marketing.
-- "Ties matter. If two members spent the same, I want them ranked the same, and I want to know
--  how many made the top fifty, not forty-nine because of a tie." The head of Retail-Plus.

-- ---------------------------------------------------------------- 1. what GROUP BY gives you
-- The question: Q2 revenue per customer per segment.
-- Correct, and not the answer. There is no clause here that says "the best fifty within a group".
SELECT c.segment, o.customer_id, sum(o.amount) AS revenue
FROM   orders o JOIN customers c USING (customer_id)
WHERE  o.quarter = 'Q2'
GROUP  BY c.segment, o.customer_id
ORDER  BY c.segment, revenue DESC
LIMIT  10;

-- ---------------------------------------------------------------- 2. a window keeps every row
-- The question: where does each Retail-Plus member stand among the others?
WITH q2 AS (
    SELECT o.customer_id, sum(o.amount) AS revenue
    FROM   orders o JOIN customers c USING (customer_id)
    WHERE  o.quarter = 'Q2' AND c.segment = 'Retail-Plus'
    GROUP  BY o.customer_id
)
SELECT customer_id, revenue,
       rank() OVER (ORDER BY revenue DESC) AS position
FROM   q2
ORDER  BY position
LIMIT  8;

-- ---------------------------------------------------------------- 3. three functions, one tie
-- The question: what do the three ranking functions do to two rows that tie?
-- Look at positions 48 to 53. Two ties are in there, and they behave differently.
WITH q2 AS (
    SELECT o.customer_id, sum(o.amount) AS revenue
    FROM   orders o JOIN customers c USING (customer_id)
    WHERE  o.quarter = 'Q2' AND c.segment = 'Retail-Plus'
    GROUP  BY o.customer_id
),
r AS (
    SELECT customer_id, revenue,
           row_number() OVER (ORDER BY revenue DESC) AS rn,
           rank()       OVER (ORDER BY revenue DESC) AS rk,
           dense_rank() OVER (ORDER BY revenue DESC) AS dr
    FROM   q2
)
SELECT rn, rk, dr, revenue FROM r WHERE rn BETWEEN 46 AND 54 ORDER BY rn;

-- ---------------------------------------------------------------- 4. how many rows ship
-- The question: under each rule, how many names does a "top fifty" contain?
WITH q2 AS (
    SELECT o.customer_id, sum(o.amount) AS revenue
    FROM   orders o JOIN customers c USING (customer_id)
    WHERE  o.quarter = 'Q2' AND c.segment = 'Retail-Plus'
    GROUP  BY o.customer_id
),
r AS (
    SELECT row_number() OVER (ORDER BY revenue DESC) AS rn,
           rank()       OVER (ORDER BY revenue DESC) AS rk,
           dense_rank() OVER (ORDER BY revenue DESC) AS dr
    FROM   q2
)
SELECT count(*) FILTER (WHERE rn <= 50) AS by_row_number,
       count(*) FILTER (WHERE rk <= 50) AS by_rank,
       count(*) FILTER (WHERE dr <= 50) AS by_dense_rank
FROM   r;

-- ---------------------------------------------------------------- 5. the error worth meeting
-- The question: can you filter on a window function directly?
-- Run it, read the message, and say which stage of Monday's picture it comes from.
SELECT customer_id FROM orders WHERE rank() OVER (ORDER BY amount) <= 5;

-- ---------------------------------------------------------------- 6. PARTITION BY restarts it
-- The question: the top five in every segment, not the top five overall.
WITH q2 AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS revenue
    FROM   orders o JOIN customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
),
r AS (
    SELECT segment, customer_id, revenue,
           rank() OVER (PARTITION BY segment ORDER BY revenue DESC) AS pos
    FROM   q2
)
SELECT segment, customer_id, revenue, pos
FROM   r WHERE pos <= 3 ORDER BY segment, pos;

-- ---------------------------------------------------------------- 7. LAG reads the row before
-- The question: how does each Retail-Plus member's month compare with their own previous month?
WITH monthly AS (
    SELECT o.customer_id, date_trunc('month', o.order_date) AS mth, sum(o.amount) AS spend
    FROM   orders o JOIN customers c USING (customer_id)
    WHERE  o.quarter = 'Q2' AND c.segment = 'Retail-Plus'
    GROUP  BY o.customer_id, date_trunc('month', o.order_date)
)
SELECT customer_id, mth, spend,
       lag(spend) OVER (PARTITION BY customer_id ORDER BY mth) AS previous_month
FROM   monthly
ORDER  BY customer_id, mth
LIMIT  9;

-- ---------------------------------------------------------------- 8. falling two months running
-- The question: who fell in July to August and again in August to September?
-- Two LAGs and a comparison. A member with one month of data cannot answer this, and NULL
-- is how the data says so.
WITH monthly AS (
    SELECT o.customer_id, date_trunc('month', o.order_date) AS mth, sum(o.amount) AS spend
    FROM   orders o JOIN customers c USING (customer_id)
    WHERE  o.quarter = 'Q2' AND c.segment = 'Retail-Plus'
    GROUP  BY o.customer_id, date_trunc('month', o.order_date)
),
l AS (
    SELECT customer_id, mth, spend,
           lag(spend, 1) OVER (PARTITION BY customer_id ORDER BY mth) AS m1,
           lag(spend, 2) OVER (PARTITION BY customer_id ORDER BY mth) AS m2
    FROM   monthly
)
SELECT customer_id, m2 AS july, m1 AS august, spend AS september
FROM   l
WHERE  m2 > m1 AND m1 > spend
ORDER  BY customer_id;

-- ---------------------------------------------------------------- 9. the running total
-- The question: how does Q2 revenue accumulate week by week against the plan line?
-- The window's ORDER BY is what makes the cumulative column deterministic. Without a unique
-- order, two rows sharing a week can swap and the number changes between runs.
WITH weekly AS (
    SELECT date_trunc('week', order_date) AS week_start, sum(amount) AS revenue
    FROM   orders WHERE quarter = 'Q2'
    GROUP  BY date_trunc('week', order_date)
)
SELECT w.week_start::date,
       w.revenue,
       sum(w.revenue) OVER (ORDER BY w.week_start) AS cumulative,
       sum(p.plan_revenue) OVER (ORDER BY w.week_start) AS plan_cumulative
FROM   weekly w
LEFT JOIN plan_line p ON p.week_start = w.week_start::date
ORDER  BY w.week_start;

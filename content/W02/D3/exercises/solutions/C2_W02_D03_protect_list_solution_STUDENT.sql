-- The protect list, solved. Released at close of session.

-- ---------------------------------------------------------------- 1. the protect list
-- Top fifty per segment by Q2 revenue. RANK rather than ROW_NUMBER, because the head of
-- Retail-Plus said: "If two members spent the same, I want them ranked the same, and I want to
-- know how many made the top fifty, not forty-nine because of a tie." Ranked the same rules out
-- ROW_NUMBER; not forty-nine rules out cutting the tie off. The window is computed inside and
-- filtered outside, because a window function cannot sit in WHERE.
WITH q2 AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS revenue
    FROM   orders o JOIN customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
),
ranked AS (
    SELECT segment, customer_id, revenue,
           rank() OVER (PARTITION BY segment ORDER BY revenue DESC) AS pos
    FROM   q2
)
SELECT segment, pos, customer_id, revenue
FROM   ranked
WHERE  pos <= 50
ORDER  BY segment, pos, customer_id;

-- ---------------------------------------------------------------- 2. how many names shipped
-- Retail-Plus ships fifty-one names rather than fifty, because two members tie at position fifty
-- and RANK keeps both. That is the requested behaviour and not a defect. Segments with fewer
-- than fifty members ship all of them, which is also correct and worth stating.
WITH q2 AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS revenue
    FROM   orders o JOIN customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
),
ranked AS (
    SELECT segment, rank() OVER (PARTITION BY segment ORDER BY revenue DESC) AS pos
    FROM   q2
)
SELECT segment, count(*) AS names_shipped
FROM   ranked WHERE pos <= 50 GROUP BY segment ORDER BY segment;

-- ---------------------------------------------------------------- 3. falling two months running
-- Two LAGs and a comparison, partitioned by customer and ordered by month. A member with only
-- one or two months of data returns NULL from the second LAG, and NULL fails the comparison, so
-- they are excluded. That is the honest outcome: you cannot tell whether they are falling.
WITH monthly AS (
    SELECT o.customer_id,
           date_trunc('month', o.order_date) AS mth,
           sum(o.amount) AS spend
    FROM   orders o JOIN customers c USING (customer_id)
    WHERE  o.quarter = 'Q2' AND c.segment = 'Retail-Plus'
    GROUP  BY o.customer_id, date_trunc('month', o.order_date)
),
lagged AS (
    SELECT customer_id, mth, spend,
           lag(spend, 1) OVER (PARTITION BY customer_id ORDER BY mth) AS one_back,
           lag(spend, 2) OVER (PARTITION BY customer_id ORDER BY mth) AS two_back
    FROM   monthly
)
SELECT customer_id,
       two_back AS july, one_back AS august, spend AS september
FROM   lagged
WHERE  two_back > one_back AND one_back > spend
ORDER  BY customer_id;
-- Three members. All three fall in both steps rather than falling once and flattening.

-- ---------------------------------------------------------------- 4. the running total
-- Weekly Q2 revenue accumulating, beside the plan accumulating. week_start is unique after the
-- grouping, so the window's order cannot tie and the cumulative column is reproducible.
-- The first week has no plan row, because the plan line starts on 6 July, and the LEFT JOIN
-- leaves that cell NULL rather than inventing a zero.
WITH weekly AS (
    SELECT date_trunc('week', order_date) AS week_start, sum(amount) AS revenue
    FROM   orders WHERE quarter = 'Q2'
    GROUP  BY date_trunc('week', order_date)
)
SELECT w.week_start::date AS week,
       w.revenue,
       sum(w.revenue) OVER (ORDER BY w.week_start) AS cumulative,
       sum(p.plan_revenue) OVER (ORDER BY w.week_start) AS plan_cumulative
FROM   weekly w
LEFT JOIN plan_line p ON p.week_start = w.week_start::date
ORDER  BY w.week_start;
-- Revenue runs ahead of plan from the third week and then the weekly run rate falls away, so the
-- quarter lands level rather than ahead. The shape is the finding; the endpoint hides it.

-- ---------------------------------------------------------------- 5. the note
-- RANK, because ties must share a position and the list must not lose a name to a tie.
-- The head of Retail-Plus said: "If two members spent the same, I want them ranked the same, and
--   I want to know how many made the top fifty, not forty-nine because of a tie."
-- The Retail-Plus list contains fifty-one names, because two members tie at position fifty.
-- To a flagged member who was on holiday in August: the flag is a shortlist for a call rather
--   than a verdict. Three months of falling spend is worth a conversation, and the conversation
--   is where a holiday gets found out.

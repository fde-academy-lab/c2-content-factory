-- Kalpa Retail, Week 2, Wednesday. Round 3: whose spend is falling, and are we on track?
--
-- "Flag anyone whose monthly spend has fallen for two months running. And Meera wants to see
--  revenue accumulate week by week against the plan line, so we know by mid-quarter whether we
--  are on track." Marketing.
--
-- The flag in this file means: the member spent less in August than in July, and less again in
-- September than in August. Every block counts members before it lists any.

-- ---------------------------------------------------------------- 1. a month per member
-- The question: how much did each member spend in each month they bought?
-- One row per member per month with an order. A month with no order has no row at all.
SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
FROM   orders
GROUP  BY customer_id, date_trunc('month', order_date)
ORDER  BY customer_id, month
LIMIT  12;

-- ---------------------------------------------------------------- 2. the hurried flag
-- LAG reads the previous row. Without PARTITION BY, the previous row of a member's first month is
-- the last month of whoever sorts before them.
WITH monthly AS (
    SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
    FROM   orders
    GROUP  BY customer_id, date_trunc('month', order_date)
),
lagged AS (
    SELECT customer_id, month, spend,
           lag(spend, 1)       OVER (ORDER BY customer_id, month) AS spend_before,
           lag(spend, 2)       OVER (ORDER BY customer_id, month) AS spend_two_before,
           lag(customer_id, 2) OVER (ORDER BY customer_id, month) AS whose_row_two_before
    FROM   monthly
)
SELECT count(*) AS flagged,
       count(*) FILTER (WHERE whose_row_two_before <> customer_id) AS compared_with_another_member
FROM   lagged
WHERE  month = DATE '2026-09-01'
  AND  spend < spend_before AND spend_before < spend_two_before;

-- ---------------------------------------------------------------- 3. PARTITION BY the member
-- The question: the same flag, with every member compared only with their own months.
WITH monthly AS (
    SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
    FROM   orders
    GROUP  BY customer_id, date_trunc('month', order_date)
),
lagged AS (
    SELECT customer_id, month, spend,
           lag(spend, 1) OVER (PARTITION BY customer_id ORDER BY month) AS spend_before,
           lag(spend, 2) OVER (PARTITION BY customer_id ORDER BY month) AS spend_two_before,
           lag(month, 1) OVER (PARTITION BY customer_id ORDER BY month) AS month_before,
           lag(month, 2) OVER (PARTITION BY customer_id ORDER BY month) AS month_two_before
    FROM   monthly
)
SELECT count(*) AS flagged,
       count(*) FILTER (WHERE month_before <> DATE '2026-08-01'
                           OR month_two_before <> DATE '2026-07-01') AS a_gap_read_as_last_month
FROM   lagged
WHERE  month = DATE '2026-09-01'
  AND  spend < spend_before AND spend_before < spend_two_before;

-- ---------------------------------------------------------------- 4. the member on holiday
-- The question: what did the flag compare for a member who bought nothing in August?
-- C-0216 is one of them. Read the three months LAG lined up.
WITH monthly AS (
    SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
    FROM   orders
    GROUP  BY customer_id, date_trunc('month', order_date)
)
SELECT customer_id, month, spend,
       lag(month) OVER (PARTITION BY customer_id ORDER BY month) AS the_row_lag_calls_last_month
FROM   monthly
WHERE  customer_id = 'C-0216'
ORDER  BY month;

-- ---------------------------------------------------------------- 5. the flag that holds
-- A fall needs two readings a calendar month apart. A month with no order is no reading, so it
-- breaks the run instead of counting as a fall. Your turn: list the members, with their segment.
WITH monthly AS (
    SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
    FROM   orders
    GROUP  BY customer_id, date_trunc('month', order_date)
),
lagged AS (
    SELECT customer_id, month, spend,
           lag(spend, 1) OVER (PARTITION BY customer_id ORDER BY month) AS spend_before,
           lag(spend, 2) OVER (PARTITION BY customer_id ORDER BY month) AS spend_two_before,
           lag(month, 1) OVER (PARTITION BY customer_id ORDER BY month) AS month_before,
           lag(month, 2) OVER (PARTITION BY customer_id ORDER BY month) AS month_two_before
    FROM   monthly
)
SELECT count(*) AS flagged
FROM   lagged
WHERE  month = DATE '2026-09-01'
  AND  month_before     = month - INTERVAL '1 month'
  AND  month_two_before = month - INTERVAL '2 months'
  AND  spend < spend_before AND spend_before < spend_two_before;

-- ---------------------------------------------------------------- 6. a running total, by day
-- The question: how much had Q2 booked by each day?
-- ORDER BY order_date alone leaves orders of the same day in no fixed order. Postgres then gives
-- every order of that day the same running total, the day's closing figure. Adding order_id to
-- the order makes each row one step, and the same step on every run.
-- The busiest day of the quarter, 22 July, carries twelve orders; read its rows.
WITH running AS (
    SELECT order_date, order_id, amount,
           sum(amount) OVER (ORDER BY order_date)           AS by_date_only,
           sum(amount) OVER (ORDER BY order_date, order_id) AS by_date_then_order
    FROM   orders
    WHERE  quarter = 'Q2'
)
SELECT *
FROM   running
WHERE  order_date = DATE '2026-07-22'
ORDER  BY order_id;

-- ---------------------------------------------------------------- 7. revenue against the plan
-- The question: by the end of each plan week, how much had Q2 booked, against the plan so far?
-- Both sides accumulate. A running actual set beside one week's plan compares a quarter-to-date
-- total with seven days of target.
-- This block reads the first seven plan weeks, up to mid-quarter. The full thirteen weeks and
-- the close against Monday's Q2 total are the afternoon's case.
WITH daily AS (
    SELECT order_date, sum(amount) AS booked
    FROM   orders
    WHERE  quarter = 'Q2'
    GROUP  BY order_date
),
to_date AS (
    SELECT order_date, sum(booked) OVER (ORDER BY order_date) AS booked_to_date
    FROM   daily
),
plan AS (
    SELECT week_start, week_start + 6 AS week_end,
           sum(plan_revenue) OVER (ORDER BY week_start) AS plan_to_date
    FROM   plan_line
)
SELECT p.week_start, p.plan_to_date,
       (SELECT max(t.booked_to_date) FROM to_date t WHERE t.order_date <= p.week_end) AS booked_to_date
FROM   plan p
WHERE  p.week_start <= DATE '2026-08-17'
ORDER  BY p.week_start;

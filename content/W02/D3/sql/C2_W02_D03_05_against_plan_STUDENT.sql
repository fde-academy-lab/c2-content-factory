-- Kalpa Retail, Week 2 Wednesday, chapter 5: has Q2 revenue kept pace with the plan line week by
-- week, and where did it stand at mid-quarter?
--
-- Meera Raghavan, CEO of Kalpa Retail, wants "to see revenue accumulate week by week against the plan
-- line, so we know by mid-quarter whether we are on track." The plan line is a small table,
-- plan_line, with one row per plan week: the Monday it starts and the revenue planned for it.
-- Q2 is July to September 2026, and booked revenue is every order at its amount whatever its status;
-- Monday's suite put Q2 at Rs 9,84,00,000.
--
-- SUM(x) OVER (ORDER BY week) is a running total: each row keeps its own week and carries the sum of
-- every row up to and including it.

-- name: c5_plan
-- The question: what does the plan line hold?
SELECT week_start, week_start + 6 AS week_end, plan_revenue
FROM   plan_line
ORDER  BY week_start;

-- name: c5_q2_span
-- The question: which days do Q2's orders cover, and what did Q2 book?
SELECT min(order_date) AS first_order,
       max(order_date) AS last_order,
       count(*)        AS orders,
       sum(amount)     AS q2_revenue
FROM   orders
WHERE  quarter = 'Q2';

-- name: c5_plan_to_date
-- The plan accumulated: each week keeps its own plan and carries the plan to date beside it.
SELECT week_start,
       plan_revenue,
       sum(plan_revenue) OVER (ORDER BY week_start) AS plan_to_date
FROM   plan_line
ORDER  BY week_start;

-- name: c5_plan_first
-- The hurried build: start from the plan's weeks, attach each week's booked revenue by the Monday
-- its orders fall in, and accumulate both sides.
WITH weekly AS (
    SELECT date_trunc('week', order_date)::date AS week_start,
           sum(amount)                          AS booked
    FROM   orders
    WHERE  quarter = 'Q2'
    GROUP  BY 1
),
joined AS (
    SELECT p.week_start, p.plan_revenue, coalesce(w.booked, 0) AS booked
    FROM   plan_line p
    LEFT   JOIN weekly w USING (week_start)
)
SELECT week_start,
       sum(plan_revenue) OVER (ORDER BY week_start) AS plan_to_date,
       sum(booked)       OVER (ORDER BY week_start) AS booked_to_date
FROM   joined
ORDER  BY week_start;

-- name: c5_weeks_of_q2
-- The question: which Mondays do Q2's orders fall under, and how many orders in each?
SELECT date_trunc('week', order_date)::date AS week_start,
       count(*)                             AS orders,
       sum(amount)                          AS booked
FROM   orders
WHERE  quarter = 'Q2'
GROUP  BY 1
ORDER  BY 1;

-- name: c5_before_plan
-- The question: which Q2 orders fall before the plan's first week starts?
SELECT count(*)    AS orders,
       sum(amount) AS booked
FROM   orders
WHERE  quarter = 'Q2'
  AND  order_date < (SELECT min(week_start) FROM plan_line);

-- name: c5_fixed
-- The fix: the plan's first week carries the Q2 days before it, so every Q2 order lands in a plan
-- week. greatest() moves the days before the first plan Monday onto that Monday.
WITH weekly AS (
    SELECT greatest(date_trunc('week', order_date)::date,
                    (SELECT min(week_start) FROM plan_line)) AS week_start,
           sum(amount)                                      AS booked
    FROM   orders
    WHERE  quarter = 'Q2'
    GROUP  BY 1
),
joined AS (
    SELECT p.week_start, p.plan_revenue, coalesce(w.booked, 0) AS booked
    FROM   plan_line p
    LEFT   JOIN weekly w USING (week_start)
)
SELECT week_start,
       week_start + 6                               AS week_end,
       plan_revenue,
       booked,
       sum(plan_revenue) OVER (ORDER BY week_start) AS plan_to_date,
       sum(booked)       OVER (ORDER BY week_start) AS booked_to_date
FROM   joined
ORDER  BY week_start;

-- name: c5_peers
-- The question: what does a running total by order say on 22 July, the busiest day of Q2, when the
-- window is ordered by the date alone, and when the order id is added?
WITH running AS (
    SELECT order_id, order_date, amount,
           sum(amount) OVER (ORDER BY order_date)           AS by_date_alone,
           sum(amount) OVER (ORDER BY order_date, order_id) AS by_date_and_id
    FROM   orders
    WHERE  quarter = 'Q2'
)
SELECT order_id, amount, by_date_alone, by_date_and_id
FROM   running
WHERE  order_date = DATE '2026-07-22'
ORDER  BY order_id;

-- name: c5_second_route
-- The second route, with no window: for each plan week, one plain SUM of every Q2 order dated on or
-- before that week's last day.
SELECT p.week_start,
       (SELECT sum(o.amount)
        FROM   orders o
        WHERE  o.quarter = 'Q2'
          AND  o.order_date <= p.week_start + 6) AS booked_to_date
FROM   plan_line p
ORDER  BY p.week_start;

-- Kalpa Retail, Week 2, Wednesday. The escalated case: one worked solution.
--
-- Released at the close of the case. Other correct shapes exist; what has to match is the counts,
-- the flag and the two plan readings, and every step has to say what it answers.

-- ---------------------------------------------------------------- Part 1. the protect list
-- The question: the top fifty members by Q2 booked revenue in each segment, ties ranked the same.
-- The rule: RANK, because tied members share a position and nobody at the line is dropped by a
-- coin toss; the report says how many shipped. Denominator: members with a Q2 order.
WITH q2 AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
),
protect AS (
    SELECT segment, customer_id, q2_revenue,
           rank() OVER (PARTITION BY segment ORDER BY q2_revenue DESC) AS position
    FROM   q2
)
SELECT segment, count(*) AS members_on_the_list, max(position) AS last_position
FROM   protect
WHERE  position <= 50
GROUP  BY segment
ORDER  BY segment;

-- ---------------------------------------------------------------- Part 2. the falling-spend flag
-- The question: which listed members spent less in August than July, and less again in September
-- than August? Denominator: members on the protect list. A month with no order breaks the run.
WITH q2 AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
),
protect AS (
    SELECT segment, customer_id, q2_revenue,
           rank() OVER (PARTITION BY segment ORDER BY q2_revenue DESC) AS position
    FROM   q2
),
monthly AS (
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
),
falling AS (
    SELECT customer_id
    FROM   lagged
    WHERE  month = DATE '2026-09-01'
      AND  month_before     = month - INTERVAL '1 month'
      AND  month_two_before = month - INTERVAL '2 months'
      AND  spend < spend_before AND spend_before < spend_two_before
)
SELECT p.segment, p.position, p.customer_id, p.q2_revenue
FROM   protect p
JOIN   falling f USING (customer_id)
WHERE  p.position <= 50
ORDER  BY p.segment, p.position;

-- ---------------------------------------------------------------- Part 3. revenue against plan
-- The question: at the end of each plan week, how much had Q2 booked to date, against the plan to
-- date? Both sides accumulate, and the actual is read at the week's last day, so orders placed
-- before the first plan week still count.
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
       (SELECT max(t.booked_to_date) FROM to_date t WHERE t.order_date <= p.week_end) AS booked_to_date,
       (SELECT max(t.booked_to_date) FROM to_date t WHERE t.order_date <= p.week_end)
           - p.plan_to_date AS ahead_of_plan
FROM   plan p
ORDER  BY p.week_start;

-- ---------------------------------------------------------------- Part 4. the check
-- The question: does the last week's booked-to-date equal the Q2 total from Monday's suite?
-- The hurried version below starts from the plan and joins weekly revenue onto it. It looks
-- complete, thirteen weeks and thirteen numbers, and it closes short of the quarter.
WITH weekly AS (
    SELECT date_trunc('week', order_date)::date AS week_start, sum(amount) AS booked
    FROM   orders
    WHERE  quarter = 'Q2'
    GROUP  BY 1
),
hurried AS (
    SELECT p.week_start,
           sum(w.booked)       OVER (ORDER BY p.week_start) AS booked_to_date,
           sum(p.plan_revenue) OVER (ORDER BY p.week_start) AS plan_to_date
    FROM   plan_line p
    LEFT JOIN weekly w ON w.week_start = p.week_start
)
SELECT (SELECT booked_to_date FROM hurried ORDER BY week_start DESC LIMIT 1) AS hurried_close,
       (SELECT sum(amount) FROM orders WHERE quarter = 'Q2')                AS q2_booked_total,
       (SELECT sum(amount) FROM orders WHERE quarter = 'Q2')
         - (SELECT booked_to_date FROM hurried ORDER BY week_start DESC LIMIT 1) AS missing_rupees,
       (SELECT count(*) FROM orders
        WHERE  quarter = 'Q2' AND order_date < (SELECT min(week_start) FROM plan_line))
                                                                            AS orders_before_week_one;

-- ---------------------------------------------------------------- Part 5. the sentence
-- Tie rule: RANK within each segment, so tied members share a position and everyone at or above
-- fiftieth ships. It ships 35 Business and 20 Student members, which is every Q2 buyer in those
-- segments, 50 in Retail-Core and 51 in Retail-Plus, where two members tie at fiftieth on
-- Rs 3,350.
-- Flag: 9 listed members spent less in August than July and less again in September, three in
-- each of Business, Retail-Core and Retail-Plus. A member with no August order is not flagged,
-- because a month without an order is no reading; his last three months are not a run.
-- Plan: at the end of the seventh plan week Q2 had booked Rs 6,87,36,590 against a plan of
-- Rs 5,29,84,610, ahead by Rs 1,57,51,980, and it closed at Rs 9,84,00,000 against
-- Rs 9,83,99,990, on plan. The lead at mid-quarter came from the week of 13 July.

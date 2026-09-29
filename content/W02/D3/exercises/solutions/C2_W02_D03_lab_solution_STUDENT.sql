-- Kalpa Retail, Week 2, Wednesday. The practice lab: one worked solution.
--
-- Released at the close of the lab. It runs unchanged against the warehouse (v4). Other correct
-- shapes exist; what has to match is the counts, and every step has to say what it answers.
-- Q2 revenue per member is the booked amount of the member's Q2 orders, all statuses.

-- ---------------------------------------------------------------- P1. three rankings on a tie
-- Invented members, for the prediction only. Check your paper against this output.
WITH invented (member, spend) AS (
    VALUES ('G', 6450), ('H', 5980), ('J', 5980), ('K', 5120), ('L', 4870), ('M', 4870), ('N', 4870)
),
r AS (
    SELECT member, spend,
           row_number() OVER (ORDER BY spend DESC, member) AS row_number,
           rank()       OVER (ORDER BY spend DESC)         AS rank,
           dense_rank() OVER (ORDER BY spend DESC)         AS dense_rank,
           count(*)     OVER (PARTITION BY spend)          AS tied_with
    FROM   invented
)
SELECT member, spend, row_number, rank, dense_rank
FROM   r
ORDER  BY spend DESC, member;

-- The same invented members: how many does each rule ship on a top four and on a top five?
WITH invented (member, spend) AS (
    VALUES ('G', 6450), ('H', 5980), ('J', 5980), ('K', 5120), ('L', 4870), ('M', 4870), ('N', 4870)
),
r AS (
    SELECT member, spend,
           row_number() OVER (ORDER BY spend DESC, member) AS rn,
           rank()       OVER (ORDER BY spend DESC)         AS rk,
           dense_rank() OVER (ORDER BY spend DESC)         AS dr,
           count(*)     OVER (PARTITION BY spend)          AS tied_with
    FROM   invented
),
cut (n) AS (VALUES (4), (5))
SELECT c.n                                                    AS top_n,
       count(*) FILTER (WHERE r.rn <= c.n)                    AS row_number_ships,
       count(*) FILTER (WHERE r.rk <= c.n)                    AS rank_ships,
       count(*) FILTER (WHERE r.dr <= c.n)                    AS dense_rank_ships,
       count(*) FILTER (WHERE r.rk + r.tied_with - 1 <= c.n)  AS whole_ties_only_ships
FROM   cut c CROSS JOIN r
GROUP  BY c.n
ORDER  BY c.n;

-- ---------------------------------------------------------------- P2. GROUP BY or window
-- P2 is answered on paper. Two of the six asks are run here as proof of the answer.
-- Ask 2: every Q2 order with its channel's average order value beside it (a window keeps the rows).
SELECT channel, count(*) AS rows_kept, round(min(channel_avg), 2) AS channel_average
FROM  (SELECT order_id, channel, amount,
              avg(amount) OVER (PARTITION BY channel) AS channel_avg
       FROM   orders
       WHERE  quarter = 'Q2') AS o
GROUP  BY channel
ORDER  BY channel;

-- Ask 4: which cities booked more than Rs 50,00,000 in Q2 (GROUP BY with HAVING, one row a city).
SELECT c.city, sum(o.amount) AS q2_booked
FROM   orders o
JOIN   customers c USING (customer_id)
WHERE  o.quarter = 'Q2'
GROUP  BY c.city
HAVING sum(o.amount) > 5000000
ORDER  BY q2_booked DESC;

-- ---------------------------------------------------------------- P3. Retail-Core vouchers
-- The question: the five biggest Retail-Core Q2 orders in each channel, ties ranked the same.
-- Denominator: Retail-Core orders in Q2. The rule: RANK, so a tie at fifth ships whole.
WITH rc AS (
    SELECT o.order_id, o.customer_id, o.channel, o.order_date, o.amount
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2' AND c.segment = 'Retail-Core'
),
ranked AS (
    SELECT channel, order_id, customer_id, order_date, amount,
           row_number() OVER (PARTITION BY channel ORDER BY amount DESC, order_id) AS rn,
           rank()       OVER (PARTITION BY channel ORDER BY amount DESC)           AS rk,
           dense_rank() OVER (PARTITION BY channel ORDER BY amount DESC)           AS dr
    FROM   rc
)
SELECT channel, rk AS position, order_id, customer_id, amount
FROM   ranked
WHERE  rk <= 5
ORDER  BY channel, rk, order_id;

-- The check: how many orders does each rule ship per channel, and how many members get a voucher?
WITH rc AS (
    SELECT o.order_id, o.customer_id, o.channel, o.amount
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2' AND c.segment = 'Retail-Core'
),
ranked AS (
    SELECT channel, order_id, customer_id, amount,
           row_number() OVER (PARTITION BY channel ORDER BY amount DESC, order_id) AS rn,
           rank()       OVER (PARTITION BY channel ORDER BY amount DESC)           AS rk,
           dense_rank() OVER (PARTITION BY channel ORDER BY amount DESC)           AS dr
    FROM   rc
)
SELECT coalesce(channel, 'all channels')               AS channel,
       count(*) FILTER (WHERE rn <= 5)                 AS row_number_ships,
       count(*) FILTER (WHERE rk <= 5)                 AS rank_ships,
       count(*) FILTER (WHERE dr <= 5)                 AS dense_rank_ships,
       count(DISTINCT customer_id) FILTER (WHERE rk <= 5) AS members_on_rank_list
FROM   ranked
GROUP  BY ROLLUP (channel)
ORDER  BY channel;

-- ---------------------------------------------------------------- P4. the Retail-Core at-risk list
-- Step 1. The question: who is on the Retail-Core protect list, and what share of Retail-Core's Q2
-- revenue does it carry? Denominator: Retail-Core members with a Q2 order.
WITH q2 AS (
    SELECT o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2' AND c.segment = 'Retail-Core'
    GROUP  BY o.customer_id
),
protect AS (
    SELECT customer_id, q2_revenue,
           rank() OVER (ORDER BY q2_revenue DESC) AS position
    FROM   q2
)
SELECT count(*) FILTER (WHERE position <= 50)                        AS members_on_the_list,
       sum(q2_revenue) FILTER (WHERE position <= 50)                 AS list_revenue,
       sum(q2_revenue)                                               AS retail_core_q2_revenue,
       round(100.0 * sum(q2_revenue) FILTER (WHERE position <= 50)
                   / sum(q2_revenue), 1)                             AS list_share_pct
FROM   protect;

-- Step 2. The question: which listed Retail-Core members spent less in August than July and less
-- again in September? Denominator: members on the Retail-Core list. A skipped month breaks the run;
-- the column months_consecutive shows which rows the month check keeps.
WITH q2 AS (
    SELECT o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2' AND c.segment = 'Retail-Core'
    GROUP  BY o.customer_id
),
protect AS (
    SELECT customer_id, q2_revenue,
           rank() OVER (ORDER BY q2_revenue DESC) AS position
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
)
SELECT p.position, p.customer_id, p.q2_revenue,
       l.spend_two_before, l.spend_before, l.spend AS september_spend,
       (l.month_before     = l.month - INTERVAL '1 month'
        AND l.month_two_before = l.month - INTERVAL '2 months')     AS months_consecutive
FROM   lagged l
JOIN   protect p USING (customer_id)
WHERE  p.position <= 50
  AND  l.month = DATE '2026-09-01'
  AND  l.spend < l.spend_before AND l.spend_before < l.spend_two_before
ORDER  BY p.position;

-- Step 3. The question: at the end of each week, how much had Retail-Core booked to date in Q2, and
-- in which week did it pass half its Q2 total? The weeks start from the first Q2 order, so the week
-- of 29 June is in, and the last row has to equal Retail-Core's Q2 total.
WITH weekly AS (
    SELECT date_trunc('week', o.order_date)::date AS week_start,
           count(*)                               AS orders,
           sum(o.amount)                          AS booked
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2' AND c.segment = 'Retail-Core'
    GROUP  BY 1
)
SELECT week_start, orders, booked,
       sum(booked) OVER (ORDER BY week_start)                              AS booked_to_date,
       round(100.0 * sum(booked) OVER (ORDER BY week_start)
                   / sum(booked) OVER (), 1)                               AS pct_of_q2
FROM   weekly
ORDER  BY week_start;

-- Step 4. The check: does the running total close on Retail-Core's Q2 total, and what would a
-- total that starts at the plan's first week (6 July) have missed?
SELECT (SELECT sum(o.amount) FROM orders o JOIN customers c USING (customer_id)
        WHERE o.quarter = 'Q2' AND c.segment = 'Retail-Core')                      AS retail_core_q2,
       (SELECT sum(o.amount) FROM orders o JOIN customers c USING (customer_id)
        WHERE o.quarter = 'Q2' AND c.segment = 'Retail-Core'
          AND o.order_date >= (SELECT min(week_start) FROM plan_line))               AS from_plan_week_one,
       (SELECT count(*) FROM orders o JOIN customers c USING (customer_id)
        WHERE o.quarter = 'Q2' AND c.segment = 'Retail-Core'
          AND o.order_date < (SELECT min(week_start) FROM plan_line))                AS orders_before_week_one;

-- Step 5. The sentence, as a comment.
-- Retail-Core's protect list, ranked with RANK, carries 50 members and Rs 2,78,740 of the segment's
-- Rs 3,66,250 in Q2. Three listed members, C-0010, C-0049 and C-0030, spent less in August than
-- July and less again in September, and they carry Rs 26,210 of the list's revenue; C-0060 and
-- C-0054 show three falling readings with a skipped month among them, so neither is flagged.
-- Retail-Core passed half its Q2 total in the week of 10 August and had booked 65.6 percent of it
-- by the end of the week of 17 August, the seventh plan week, which is ahead of an even pace.

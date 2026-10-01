-- Kalpa Retail, Week 2 Wednesday, chapter 6: which listed members does Marketing call first, and does
-- each flag hold up when a member says they were on holiday?
--
-- The protect list is each segment's top fifty by Q2 revenue under RANK, the rule the head of
-- Retail-Plus asked for: members who spent the same share a place. The flag is chapter 4's: spend in
-- September below the month before, and that month below the one before it. Marketing will call the
-- flagged members on the list first. Before the calls go out, one listed member, C-0216 of
-- Retail-Plus, has told the help line they were on holiday in August.
--
-- Monthly spend is a member's booked revenue in a calendar month. Q2 is July to September 2026.

-- name: c6_on_the_list
-- The question: how many members carry the flag, and how many of them are on the protect list?
WITH monthly AS (
    SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
    FROM   orders
    GROUP  BY customer_id, date_trunc('month', order_date)
),
flagged AS (
    SELECT customer_id
    FROM  (SELECT customer_id, month, spend,
                  lag(spend, 1) OVER (PARTITION BY customer_id ORDER BY month) AS spend_1_back,
                  lag(spend, 2) OVER (PARTITION BY customer_id ORDER BY month) AS spend_2_back
           FROM   monthly) l
    WHERE  month = DATE '2026-09-01' AND spend < spend_1_back AND spend_1_back < spend_2_back
),
q2 AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
),
protect AS (
    SELECT customer_id
    FROM  (SELECT customer_id,
                  rank() OVER (PARTITION BY segment ORDER BY q2_revenue DESC) AS place
           FROM   q2) r
    WHERE  place <= 50
)
SELECT (SELECT count(*) FROM flagged)                                          AS members_flagged,
       (SELECT count(*) FROM flagged WHERE customer_id IN (SELECT customer_id FROM protect))
                                                                               AS flagged_on_the_list;

-- name: c6_holiday_member
-- The question: what did LAG compare for the member who says they were on holiday?
WITH monthly AS (
    SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
    FROM   orders
    GROUP  BY customer_id, date_trunc('month', order_date)
)
SELECT customer_id, month, spend,
       lag(month, 1) OVER (PARTITION BY customer_id ORDER BY month) AS month_1_back,
       lag(spend, 1) OVER (PARTITION BY customer_id ORDER BY month) AS spend_1_back,
       lag(month, 2) OVER (PARTITION BY customer_id ORDER BY month) AS month_2_back,
       lag(spend, 2) OVER (PARTITION BY customer_id ORDER BY month) AS spend_2_back
FROM   monthly
WHERE  customer_id = 'C-0216'
ORDER  BY month;

-- name: c6_gap_check
-- The check: carry the months LAG read beside the amounts, and count the flags whose two rows back
-- are not August and July.
WITH monthly AS (
    SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
    FROM   orders
    GROUP  BY customer_id, date_trunc('month', order_date)
),
lagged AS (
    SELECT customer_id, month, spend,
           lag(spend, 1) OVER (PARTITION BY customer_id ORDER BY month) AS spend_1_back,
           lag(spend, 2) OVER (PARTITION BY customer_id ORDER BY month) AS spend_2_back,
           lag(month, 1) OVER (PARTITION BY customer_id ORDER BY month) AS month_1_back,
           lag(month, 2) OVER (PARTITION BY customer_id ORDER BY month) AS month_2_back
    FROM   monthly
)
SELECT count(*) AS members_flagged,
       count(*) FILTER (WHERE month_1_back <> DATE '2026-08-01'
                           OR month_2_back <> DATE '2026-07-01') AS across_a_month_with_no_order
FROM   lagged
WHERE  month = DATE '2026-09-01'
  AND  spend < spend_1_back
  AND  spend_1_back < spend_2_back;

-- name: c6_calendar_flag
-- The fix: the two rows before September must be August and July, so a month with no order breaks
-- the run instead of being stepped over.
WITH monthly AS (
    SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
    FROM   orders
    GROUP  BY customer_id, date_trunc('month', order_date)
),
lagged AS (
    SELECT customer_id, month, spend,
           lag(spend, 1) OVER (PARTITION BY customer_id ORDER BY month) AS spend_1_back,
           lag(spend, 2) OVER (PARTITION BY customer_id ORDER BY month) AS spend_2_back,
           lag(month, 1) OVER (PARTITION BY customer_id ORDER BY month) AS month_1_back,
           lag(month, 2) OVER (PARTITION BY customer_id ORDER BY month) AS month_2_back
    FROM   monthly
)
SELECT count(*) AS members_flagged
FROM   lagged
WHERE  month = DATE '2026-09-01'
  AND  month_1_back = DATE '2026-08-01'
  AND  month_2_back = DATE '2026-07-01'
  AND  spend < spend_1_back
  AND  spend_1_back < spend_2_back;

-- name: c6_calendar_ids
-- The fixed flag's members, which the notebook counts and sets beside the second route's members.
WITH monthly AS (
    SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
    FROM   orders
    GROUP  BY customer_id, date_trunc('month', order_date)
),
lagged AS (
    SELECT customer_id, month, spend,
           lag(spend, 1) OVER (PARTITION BY customer_id ORDER BY month) AS spend_1_back,
           lag(spend, 2) OVER (PARTITION BY customer_id ORDER BY month) AS spend_2_back,
           lag(month, 1) OVER (PARTITION BY customer_id ORDER BY month) AS month_1_back,
           lag(month, 2) OVER (PARTITION BY customer_id ORDER BY month) AS month_2_back
    FROM   monthly
)
SELECT customer_id
FROM   lagged
WHERE  month = DATE '2026-09-01'
  AND  month_1_back = DATE '2026-08-01'
  AND  month_2_back = DATE '2026-07-01'
  AND  spend < spend_1_back
  AND  spend_1_back < spend_2_back;

-- name: c6_calendar_table
-- The question: what do two more readings of "last month" give? Both build a calendar of every member
-- who ever bought and every month, one leaving a month with no order empty (NULL) and one filling it
-- with zero, and the query counts the flags each way.
WITH monthly AS (
    SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
    FROM   orders
    GROUP  BY customer_id, date_trunc('month', order_date)
),
calendar AS (
    SELECT m.customer_id, g.month::date AS month, monthly.spend
    FROM  (SELECT DISTINCT customer_id FROM orders) m
    CROSS  JOIN generate_series(DATE '2026-04-01', DATE '2026-09-01', INTERVAL '1 month') AS g(month)
    LEFT   JOIN monthly ON monthly.customer_id = m.customer_id AND monthly.month = g.month
),
lagged AS (
    SELECT customer_id, month, spend,
           lag(spend, 1)              OVER (PARTITION BY customer_id ORDER BY month) AS null_1_back,
           lag(spend, 2)              OVER (PARTITION BY customer_id ORDER BY month) AS null_2_back,
           coalesce(spend, 0)                                                        AS zero_spend,
           lag(coalesce(spend, 0), 1) OVER (PARTITION BY customer_id ORDER BY month) AS zero_1_back,
           lag(coalesce(spend, 0), 2) OVER (PARTITION BY customer_id ORDER BY month) AS zero_2_back
    FROM   calendar
)
SELECT (SELECT count(*) FROM calendar) AS calendar_rows,
       count(*) FILTER (WHERE spend < null_1_back AND null_1_back < null_2_back)              AS flagged_empty_months,
       count(*) FILTER (WHERE zero_spend < zero_1_back AND zero_1_back < zero_2_back)        AS flagged_zero_months,
       count(*) FILTER (WHERE zero_spend < zero_1_back AND zero_1_back < zero_2_back
                          AND spend IS NULL)                                                  AS zero_flags_with_no_september_order
FROM   lagged
WHERE  month = DATE '2026-09-01';

-- name: c6_months_per_member
-- The question: in how many of the six months did a member who bought place an order, on average?
WITH monthly AS (
    SELECT customer_id, date_trunc('month', order_date)::date AS month
    FROM   orders
    GROUP  BY customer_id, date_trunc('month', order_date)
)
SELECT count(*)                                         AS member_months,
       count(DISTINCT customer_id)                      AS members,
       round(count(*)::numeric / count(DISTINCT customer_id), 2) AS months_with_an_order_each
FROM   monthly;

-- name: c6_second_route
-- The second route, with no window: join each member's September to the same member's August and
-- July by calendar month, and keep the falls.
WITH monthly AS (
    SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
    FROM   orders
    GROUP  BY customer_id, date_trunc('month', order_date)
)
SELECT sep.customer_id
FROM   monthly sep
JOIN   monthly aug ON aug.customer_id = sep.customer_id AND aug.month = DATE '2026-08-01'
JOIN   monthly jul ON jul.customer_id = sep.customer_id AND jul.month = DATE '2026-07-01'
WHERE  sep.month = DATE '2026-09-01'
  AND  sep.spend < aug.spend
  AND  aug.spend < jul.spend;

-- name: c6_genuine_fall
-- The question: what does a fall that holds up look like? C-0010 of Retail-Core, a listed member,
-- shows one.
WITH monthly AS (
    SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
    FROM   orders
    WHERE  quarter = 'Q2'
    GROUP  BY customer_id, date_trunc('month', order_date)
)
SELECT customer_id, month, spend
FROM   monthly
WHERE  customer_id = 'C-0010'
ORDER  BY month;

-- name: c6_call_list
-- Your turn: the members Marketing calls first, each with its segment and its place on the list.
WITH monthly AS (
    SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
    FROM   orders
    GROUP  BY customer_id, date_trunc('month', order_date)
),
lagged AS (
    SELECT customer_id, month, spend,
           lag(spend, 1) OVER (PARTITION BY customer_id ORDER BY month) AS spend_1_back,
           lag(spend, 2) OVER (PARTITION BY customer_id ORDER BY month) AS spend_2_back,
           lag(month, 1) OVER (PARTITION BY customer_id ORDER BY month) AS month_1_back,
           lag(month, 2) OVER (PARTITION BY customer_id ORDER BY month) AS month_2_back
    FROM   monthly
),
flagged AS (
    SELECT customer_id, spend_2_back AS july, spend_1_back AS august, spend AS september
    FROM   lagged
    WHERE  month = DATE '2026-09-01'
      AND  month_1_back = DATE '2026-08-01' AND month_2_back = DATE '2026-07-01'
      AND  spend < spend_1_back AND spend_1_back < spend_2_back
),
q2 AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
),
placed AS (
    SELECT segment, customer_id, q2_revenue,
           rank() OVER (PARTITION BY segment ORDER BY q2_revenue DESC) AS place
    FROM   q2
)
SELECT p.segment, p.place, f.customer_id, f.july, f.august, f.september
FROM   flagged f
JOIN   placed p USING (customer_id)
WHERE  p.place <= 50
ORDER  BY p.segment, p.place;

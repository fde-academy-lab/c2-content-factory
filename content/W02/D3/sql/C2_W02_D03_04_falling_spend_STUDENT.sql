-- Kalpa Retail, Week 2 Wednesday, chapter 4: whose monthly spend fell two months running?
--
-- Marketing: "Flag anyone whose monthly spend has fallen for two months running." Monthly spend is a
-- member's booked revenue in a calendar month, every order at its amount whatever its status. The
-- book runs from April to September 2026, and the flag looks at September, the last month: spend in
-- September below the month before, and that month below the one before it.
--
-- LAG(x) OVER (...) puts the previous row's x beside the current row, in the order the window names.
-- LAG(x, 2) reads two rows back.

-- name: c4_monthly
-- The question: what did each member spend in each month they bought? One row per member per month
-- with an order; this shows the first twelve.
SELECT customer_id,
       date_trunc('month', order_date)::date AS month,
       sum(amount)                           AS spend
FROM   orders
GROUP  BY customer_id, date_trunc('month', order_date)
ORDER  BY customer_id, month
LIMIT  12;

-- name: c4_monthly_count
-- The question: how many member-months does the book hold, for how many members?
WITH monthly AS (
    SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
    FROM   orders
    GROUP  BY customer_id, date_trunc('month', order_date)
)
SELECT count(*)                    AS member_months,
       count(DISTINCT customer_id) AS members,
       count(*) FILTER (WHERE month = DATE '2026-09-01') AS members_with_a_september_order
FROM   monthly;

-- name: c4_buyers_by_month
-- The question: how many members placed an order in each month?
SELECT date_trunc('month', order_date)::date AS month,
       count(DISTINCT customer_id)           AS members_who_bought
FROM   orders
GROUP  BY 1
ORDER  BY 1;

-- name: c4_one_member
-- The question: what does LAG put beside each of one member's months? C-0040, Retail-Core, who
-- bought in all six months.
WITH monthly AS (
    SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
    FROM   orders
    GROUP  BY customer_id, date_trunc('month', order_date)
)
SELECT customer_id, month, spend,
       lag(spend, 1) OVER (PARTITION BY customer_id ORDER BY month) AS spend_1_back,
       lag(spend, 2) OVER (PARTITION BY customer_id ORDER BY month) AS spend_2_back
FROM   monthly
WHERE  customer_id = 'C-0040'
ORDER  BY month;

-- name: c4_hurried
-- The hurried flag: LAG ordered by member and month, with no PARTITION BY. Counted, not listed.
WITH monthly AS (
    SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
    FROM   orders
    GROUP  BY customer_id, date_trunc('month', order_date)
),
lagged AS (
    SELECT customer_id, month, spend,
           lag(spend, 1) OVER (ORDER BY customer_id, month) AS spend_1_back,
           lag(spend, 2) OVER (ORDER BY customer_id, month) AS spend_2_back
    FROM   monthly
)
SELECT count(*) AS members_flagged
FROM   lagged
WHERE  month = DATE '2026-09-01'
  AND  spend < spend_1_back
  AND  spend_1_back < spend_2_back;

-- name: c4_hurried_check
-- The check: carry whose row LAG read, and count the flags that compared a member with somebody else.
WITH monthly AS (
    SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
    FROM   orders
    GROUP  BY customer_id, date_trunc('month', order_date)
),
lagged AS (
    SELECT customer_id, month, spend,
           lag(spend, 1)       OVER (ORDER BY customer_id, month) AS spend_1_back,
           lag(spend, 2)       OVER (ORDER BY customer_id, month) AS spend_2_back,
           lag(customer_id, 1) OVER (ORDER BY customer_id, month) AS member_1_back,
           lag(customer_id, 2) OVER (ORDER BY customer_id, month) AS member_2_back
    FROM   monthly
)
SELECT count(*) AS members_flagged,
       count(*) FILTER (WHERE member_1_back <> customer_id
                           OR member_2_back <> customer_id) AS compared_with_another_member
FROM   lagged
WHERE  month = DATE '2026-09-01'
  AND  spend < spend_1_back
  AND  spend_1_back < spend_2_back;

-- name: c4_crossings
-- The flags that read another member's month, with whose month each one read.
WITH monthly AS (
    SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
    FROM   orders
    GROUP  BY customer_id, date_trunc('month', order_date)
),
lagged AS (
    SELECT customer_id, month, spend,
           lag(spend, 1)       OVER (ORDER BY customer_id, month) AS spend_1_back,
           lag(spend, 2)       OVER (ORDER BY customer_id, month) AS spend_2_back,
           lag(customer_id, 1) OVER (ORDER BY customer_id, month) AS member_1_back,
           lag(customer_id, 2) OVER (ORDER BY customer_id, month) AS member_2_back,
           lag(month, 2)       OVER (ORDER BY customer_id, month) AS month_2_back
    FROM   monthly
)
SELECT customer_id, spend, spend_1_back, member_1_back, spend_2_back, member_2_back, month_2_back
FROM   lagged
WHERE  month = DATE '2026-09-01'
  AND  spend < spend_1_back
  AND  spend_1_back < spend_2_back
  AND  (member_1_back <> customer_id OR member_2_back <> customer_id)
ORDER  BY customer_id;

-- name: c4_partitioned
-- The fix: PARTITION BY customer_id, so LAG never reads past the start of a member's own months.
WITH monthly AS (
    SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
    FROM   orders
    GROUP  BY customer_id, date_trunc('month', order_date)
),
lagged AS (
    SELECT customer_id, month, spend,
           lag(spend, 1) OVER (PARTITION BY customer_id ORDER BY month) AS spend_1_back,
           lag(spend, 2) OVER (PARTITION BY customer_id ORDER BY month) AS spend_2_back
    FROM   monthly
)
SELECT count(*) AS members_flagged
FROM   lagged
WHERE  month = DATE '2026-09-01'
  AND  spend < spend_1_back
  AND  spend_1_back < spend_2_back;

-- name: c4_partitioned_ids
-- The partitioned flag's members, for the comparison with the second route.
WITH monthly AS (
    SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
    FROM   orders
    GROUP  BY customer_id, date_trunc('month', order_date)
),
lagged AS (
    SELECT customer_id, month, spend,
           lag(spend, 1) OVER (PARTITION BY customer_id ORDER BY month) AS spend_1_back,
           lag(spend, 2) OVER (PARTITION BY customer_id ORDER BY month) AS spend_2_back
    FROM   monthly
)
SELECT customer_id
FROM   lagged
WHERE  month = DATE '2026-09-01'
  AND  spend < spend_1_back
  AND  spend_1_back < spend_2_back;

-- name: c4_rows_for_python
-- The second route's input: every member-month, unordered on purpose; Python sorts it itself.
SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
FROM   orders
GROUP  BY customer_id, date_trunc('month', order_date);

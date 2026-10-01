-- Kalpa Retail, Week 2, Thursday. Can the table rebuild itself every Monday and refuse to ship when something breaks?
-- Runs unchanged against the Kalpa warehouse: psql -d kalpa -f <this file>.
-- The notebook of the same number runs these same queries through pandas.

-- The control totals every Monday's run is checked against.
SELECT (SELECT count(*)        FROM customers) AS customers,
       (SELECT sum(amount)     FROM orders)    AS spend,
       (SELECT max(order_date) FROM orders)    AS last_order_loaded;

-- The second route: the win-back list, counted by the warehouse to its own last date.
WITH last  AS (SELECT customer_id, max(order_date) AS last_order FROM orders GROUP BY customer_id),
     as_of AS (SELECT max(order_date) AS d FROM orders)
SELECT count(*) AS win_back
FROM   last, as_of
WHERE  as_of.d - last.last_order > 60;

-- The falling flag, Wednesday's rule: less in August than in July, and less again in September, with a real month between each reading.
WITH monthly AS (
         SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
         FROM   orders
         GROUP  BY customer_id, date_trunc('month', order_date)),
     lagged AS (
         SELECT customer_id, month, spend,
                lag(spend, 1) OVER w AS spend_before, lag(spend, 2) OVER w AS spend_two_before,
                lag(month, 1) OVER w AS month_before, lag(month, 2) OVER w AS month_two_before
         FROM   monthly
         WINDOW w AS (PARTITION BY customer_id ORDER BY month))
SELECT count(*) AS falling
FROM   lagged
WHERE  month = DATE '2026-09-01'
  AND  month_before = DATE '2026-08-01' AND month_two_before = DATE '2026-07-01'
  AND  spend < spend_before AND spend_before < spend_two_before;

-- Kalpa Retail, Week 2 Monday, chapter 6: will next Monday's run give Anand's analyst the same answer
-- from the same book?
--
-- Anand's analyst reruns the suite every Monday and traces five delivered Q2 app orders against the
-- ERP, the system Finance books orders in. If a rerun disagrees with the last run, she has to know
-- whether the book changed or the query did. This file leaves a fingerprint of the book with every
-- run, and draws the five orders so that every run draws the same five.
--
-- Q2 is July to September 2026.

-- name: c6_fingerprint
-- The book's fingerprint: what each table holds, and the totals the suite's numbers must add to.
SELECT 'orders'    AS table_name, count(*) AS rows, sum(amount) AS rupees,
       count(DISTINCT customer_id) AS distinct_customers, max(order_date) AS latest_date
FROM   orders
UNION ALL
SELECT 'customers', count(*), NULL, count(DISTINCT customer_id), max(joined_date)
FROM   customers;

-- name: c6_sample_hurried
-- The question: five delivered Q2 app orders for the analyst to trace. (The quickest way to write it.)
SELECT order_id, amount
FROM   orders
WHERE  quarter = 'Q2' AND channel = 'app' AND status = 'delivered'
LIMIT  5;

-- name: c6_sample_after_reload
-- The same query after an overnight reload rewrites two of those rows with the values they already
-- hold. The transaction is rolled back, so the warehouse is left exactly as it was.
BEGIN;
UPDATE orders SET status = status
WHERE  order_id IN ('KR-00542', 'KR-00544');
SELECT order_id, amount
FROM   orders
WHERE  quarter = 'Q2' AND channel = 'app' AND status = 'delivered'
LIMIT  5;
ROLLBACK;

-- name: c6_sample
-- The fix: order by a column no two rows share, then limit, so every run draws the same five.
SELECT order_id, amount
FROM   orders
WHERE  quarter = 'Q2' AND channel = 'app' AND status = 'delivered'
ORDER  BY order_id
LIMIT  5;

-- name: c6_sample_after_reload_fixed
-- The fixed query inside the same reload, rolled back again.
BEGIN;
UPDATE orders SET status = status
WHERE  order_id IN ('KR-00542', 'KR-00544');
SELECT order_id, amount
FROM   orders
WHERE  quarter = 'Q2' AND channel = 'app' AND status = 'delivered'
ORDER  BY order_id
LIMIT  5;
ROLLBACK;

-- name: c6_up_to_last
-- The second route, with no sort and no LIMIT: count the candidates whose id sits at or below the
-- last id on the analyst's list, KR-00547. If the list is the first five by order id, the count is 5
-- and the rupees are the list's own; a list that skipped an order makes the count run above 5.
SELECT count(*) AS candidates_up_to_it, sum(amount) AS rupees
FROM   orders
WHERE  quarter = 'Q2' AND channel = 'app' AND status = 'delivered'
  AND  order_id <= 'KR-00547';

-- name: c6_candidates
-- Every delivered Q2 app order: the candidates the audit sample is drawn from.
SELECT order_id, amount
FROM   orders
WHERE  quarter = 'Q2' AND channel = 'app' AND status = 'delivered';

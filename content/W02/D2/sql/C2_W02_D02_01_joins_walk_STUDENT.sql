-- Kalpa Retail, Tuesday of Week 2. The guided walk.
--
-- "Booked revenue is not collected revenue. Show me, order by order, what we actually collected
--  against what we booked in Q2. If there is a gap, I want to know which orders and which
--  channel." Anand Iyer.
--
-- Run it a block at a time and read the row counts before you read the money.

-- ---------------------------------------------------------------- 1. what a payment looks like
-- The question: what does one row of payments mean?
SELECT * FROM payments ORDER BY payment_id LIMIT 8;

-- ---------------------------------------------------------------- 2. how many of each
-- The question: how do the two tables compare in size, before anything is joined?
SELECT 'orders' AS table_name, count(*) FROM orders
UNION ALL
SELECT 'payments', count(*) FROM payments;

-- ---------------------------------------------------------------- 3. the naive attach
-- The question: what did we collect against what we booked?
-- Run it. Write the two numbers down. Do not trust either yet.
SELECT sum(o.amount) AS booked, sum(p.amount) AS collected
FROM   orders o
LEFT JOIN payments p ON p.order_id = o.order_id;

-- ---------------------------------------------------------------- 4. the count that was free
-- The question: how many rows did that join actually produce?
SELECT count(*) AS join_rows
FROM   orders o
LEFT JOIN payments p ON p.order_id = o.order_id;
-- 1,450 out of 1,000. Before reading on, say where the other 450 came from.

-- ---------------------------------------------------------------- 5. INNER against LEFT
-- The question: what does each one drop?
SELECT 'inner' AS join_type, count(*) FROM orders o INNER JOIN payments p USING (order_id)
UNION ALL
SELECT 'left', count(*) FROM orders o LEFT JOIN payments p USING (order_id);

-- ---------------------------------------------------------------- 6. the anti-join
-- The question: which orders were never paid? Keep everything, then keep only what did not match.
SELECT o.order_id, o.channel, o.status, o.amount
FROM   orders o
LEFT JOIN payments p ON p.order_id = o.order_id
WHERE  p.payment_id IS NULL
ORDER  BY o.amount DESC;

-- ---------------------------------------------------------------- 7. the anti-join the other way
-- The question: are there payments whose order is not in the book?
SELECT p.payment_id, p.order_id, p.amount
FROM   payments p
LEFT JOIN orders o ON o.order_id = p.order_id
WHERE  o.order_id IS NULL;

-- ---------------------------------------------------------------- 8. where the 450 came from
-- The question: how many orders carry more than one payment row?
SELECT count(*) AS orders_with_several_payments
FROM (SELECT order_id FROM payments GROUP BY order_id HAVING count(*) > 1) t;

-- ---------------------------------------------------------------- 9. retries against instalments
-- The question: which duplicates are a repeated charge, and which are a split invoice?
-- A retry repeats the same amount. An instalment plan splits it into different amounts.
WITH doubled AS (
    SELECT order_id,
           CASE WHEN count(DISTINCT amount) = 1 THEN 'retry, the same amount twice'
                ELSE 'instalment plan, different amounts' END AS kind
    FROM   payments
    GROUP  BY order_id
    HAVING count(*) > 1
)
SELECT kind, count(*) AS orders FROM doubled GROUP BY kind ORDER BY orders DESC;

-- ---------------------------------------------------------------- 10. the fix: collapse, then join
-- The question: what did we really collect?
-- Aggregate the many side to one row per key first, and no fan-out is possible.
WITH paid AS (
    SELECT order_id, sum(amount) AS collected
    FROM   payments
    GROUP  BY order_id
)
SELECT count(*)                      AS rows_out,
       sum(o.amount)                 AS booked,
       coalesce(sum(p.collected), 0) AS collected
FROM   orders o
LEFT JOIN paid p ON p.order_id = o.order_id;
-- 1,000 rows out. One row in, one row out, and the count check passes by construction.

-- ---------------------------------------------------------------- 11. the gap Anand asked about
-- The question: booked against collected for Q2, by channel, with the gap named.
-- coalesce matters: an order with no payment joins to NULL, and NULL in arithmetic makes the
-- whole expression NULL, so one unpaid order would empty a channel's gap cell entirely.
WITH paid AS (SELECT order_id, sum(amount) AS collected FROM payments GROUP BY order_id)
SELECT o.channel,
       count(*)                                      AS orders,
       sum(o.amount)                                 AS booked,
       coalesce(sum(p.collected), 0)                 AS collected,
       sum(o.amount) - coalesce(sum(p.collected), 0) AS gap
FROM   orders o
LEFT JOIN paid p ON p.order_id = o.order_id
WHERE  o.quarter = 'Q2'
GROUP  BY o.channel
ORDER  BY gap DESC;

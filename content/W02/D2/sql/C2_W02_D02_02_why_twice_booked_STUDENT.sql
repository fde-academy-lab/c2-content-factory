-- Week 2, Tuesday. Chapter 2: Why does the first join on Kalpa's Q2 report nearly twice the bookings as collected, and how do we attach payments so that nothing counts twice?
-- The warehouse's Q2 orders joined to payments: the first draft, why it doubles, and the fix at order grain.
-- Run it against the warehouse: psql -d kalpa -f this_file.sql

-- Q2's booked, from orders alone (Monday's number)
SELECT count(*) AS orders, sum(amount) AS booked
FROM orders
WHERE quarter = 'Q2';

-- Which Q2 orders own two payment rows, and why?
SELECT o.order_id, o.channel, o.status, o.amount AS booked,
       count(p.payment_id) AS payment_rows,
       string_agg(p.instalment_no::text, ' and ' ORDER BY p.instalment_no) AS instalments
FROM orders o
LEFT JOIN payments p ON p.order_id = o.order_id
WHERE o.quarter = 'Q2'
GROUP BY o.order_id, o.channel, o.status, o.amount
ORDER BY o.amount DESC
LIMIT 10;

-- The trap: what does the first draft report as collected?
SELECT count(*)                                              AS rows_out,
       sum(o.amount) FILTER (WHERE p.payment_id IS NOT NULL) AS collected
FROM orders o
LEFT JOIN payments p ON p.order_id = o.order_id
WHERE o.quarter = 'Q2';

-- The first draft by channel
SELECT o.channel,
       count(*)                                              AS rows_out,
       sum(o.amount) FILTER (WHERE p.payment_id IS NOT NULL) AS collected
FROM orders o
LEFT JOIN payments p ON p.order_id = o.order_id
WHERE o.quarter = 'Q2'
GROUP BY o.channel
ORDER BY o.channel;

-- Booked by channel, from orders alone
SELECT channel, count(*) AS orders, sum(amount) AS booked
FROM orders
WHERE quarter = 'Q2'
GROUP BY channel
ORDER BY channel;

-- One order, two payment rows: KR-00667
SELECT o.order_id, o.amount AS booked, p.payment_id, p.instalment_no, p.amount AS paid
FROM orders o
JOIN payments p ON p.order_id = o.order_id
WHERE o.order_id = 'KR-00667'
ORDER BY p.instalment_no;

-- Option B, sized: what does DISTINCT on the amount return?
SELECT count(*) AS rows_out, sum(DISTINCT o.amount) AS booked_distinct
FROM orders o
LEFT JOIN payments p ON p.order_id = o.order_id
WHERE o.quarter = 'Q2';

-- Why DISTINCT fails: how many Q2 orders share an amount?
SELECT count(*) AS orders_sharing_an_amount, count(DISTINCT amount) AS distinct_amounts
FROM orders o
WHERE quarter = 'Q2'
  AND (SELECT count(*) FROM orders o2 WHERE o2.quarter = 'Q2' AND o2.amount = o.amount) > 1;

-- The fix, option A: one row per order, then join
WITH posted_per_order AS (
    SELECT order_id, sum(amount) AS posted, count(*) AS payment_rows
    FROM payments
    GROUP BY order_id
)
SELECT o.order_id, o.channel, o.amount AS booked, pp.posted, pp.payment_rows
FROM orders o
LEFT JOIN posted_per_order pp ON pp.order_id = o.order_id
WHERE o.quarter = 'Q2';

-- The second route: posted from payments alone, Q2 order ids
SELECT sum(amount) AS posted
FROM payments
WHERE order_id IN (SELECT order_id FROM orders WHERE quarter = 'Q2');

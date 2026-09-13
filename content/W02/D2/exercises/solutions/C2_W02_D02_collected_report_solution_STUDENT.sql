-- The booked-against-collected report, solved. Released at close of session.

-- ---------------------------------------------------------------- the reconciliation
-- Rows before: 1,000 orders.
-- Rows after:  1,450.
-- Difference:  450 orders carry more than one payment row, of which 400 are instalment
--              plans and 50 are gateway retries. 30 orders carry none.
-- Therefore:   do not SUM the order amount over this join. Collapse payments to one row per
--              order first, then join, and the row count check passes by construction.

-- ---------------------------------------------------------------- 1. the report
-- Q2 booked against collected by channel. Denominator is every Q2 order, paid or not, so a
-- channel's gap includes orders that were never paid rather than quietly dropping them.
-- coalesce matters: an unpaid order joins to NULL, and NULL in arithmetic makes the whole
-- expression NULL, so one unpaid order would empty a channel's gap cell entirely.
WITH paid AS (
    SELECT order_id, sum(amount) AS collected FROM payments GROUP BY order_id
)
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
-- store and web carry a gap in the lakhs; app is almost clean. That contrast is the finding.

-- ---------------------------------------------------------------- 2. the unpaid list
-- Delivered orders with no payment row. An anti-join: keep everything, then keep only what
-- failed to match. Denominator is not relevant here; this is a list, not a rate.
SELECT o.order_id, o.channel, o.status, o.amount
FROM   orders o
LEFT JOIN payments p ON p.order_id = o.order_id
WHERE  p.payment_id IS NULL
ORDER  BY o.amount DESC;
-- Thirty rows. The two largest are Q2 corporate invoices on different channels, which is why
-- the gap shows up in two channels rather than one.

-- ---------------------------------------------------------------- 3. the double-paid list
-- Orders charged twice by a retry, separated from orders on an instalment plan. The separator is
-- a business fact rather than a data fact: a retry repeats a charge, an instalment splits one.
SELECT order_id, count(*) AS payment_rows, sum(amount) AS total_posted
FROM   payments
GROUP  BY order_id
HAVING count(*) > 1
   AND count(DISTINCT amount) = 1
ORDER  BY total_posted DESC;
-- Fifty rows. These inflate collected rather than widening the gap, which is the opposite
-- direction from the unpaid orders and belongs in a different sentence of the note.

-- ---------------------------------------------------------------- 4. the orphans
-- Payments whose order is not in the book. The same anti-join, run the other way round.
SELECT p.payment_id, p.order_id, p.paid_date, p.amount
FROM   payments p
LEFT JOIN orders o ON o.order_id = p.order_id
WHERE  o.order_id IS NULL
ORDER  BY p.payment_id;
-- Eight rows. Money arrived for something the order book does not know about. Report it to the
-- platform team and do not net it against anything.

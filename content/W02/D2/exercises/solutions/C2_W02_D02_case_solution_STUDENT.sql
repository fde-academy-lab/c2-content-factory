-- Week 2, Tuesday. The escalated case, one worked solution.
-- Released at the close. Every number comes from the query, and the checks at the end must all
-- return true before the report leaves the team. Run: psql -d kalpa -f this_file.sql

-- The reconciliation, written before the numbers, as Kavya asks:
--   Rows in:   every Q2 order, from orders alone (part 1).
--   Rows out:  one row per Q2 order after the join (part 2), because payments are brought to one row
--              per order before the join. Rows out must equal rows in.
--   Booked:    the sum over rows out must equal booked from orders alone.
--   The gap:   booked minus collected must equal the booked value of the unpaid list (part 3).
--   The feed:  collected plus the surplus on the double-paid list (part 4) must equal what the
--              payments feed posted against Q2 orders.
--   Payments:  every payment row is matched to a Q1 order, a Q2 order, or to no order (part 5).

-- Part 1. The baseline.
SELECT channel, count(*) AS orders_in, sum(amount) AS booked
FROM orders
WHERE quarter = 'Q2'
GROUP BY channel
ORDER BY channel;

-- Part 2. Collected at order grain. A retry is the same instalment posted twice, so each instalment
-- is counted once before the order total is taken.
WITH per_instalment AS (
    SELECT order_id, instalment_no, max(amount) AS amount, count(*) AS times_posted
    FROM payments
    GROUP BY order_id, instalment_no
),
per_order AS (
    SELECT order_id,
           sum(amount) AS collected,
           sum(amount * (times_posted - 1)) AS posted_twice
    FROM per_instalment
    GROUP BY order_id
)
SELECT o.channel,
       count(*) AS rows_out,
       sum(o.amount) AS booked,
       sum(coalesce(po.collected, 0)) AS collected,
       sum(o.amount) - sum(coalesce(po.collected, 0)) AS gap
FROM orders o
LEFT JOIN per_order po ON po.order_id = o.order_id
WHERE o.quarter = 'Q2'
GROUP BY o.channel
ORDER BY o.channel;

-- Part 3. The unpaid list.
SELECT o.order_id, o.channel, o.status, o.amount AS booked
FROM orders o
WHERE o.quarter = 'Q2'
  AND NOT EXISTS (SELECT 1 FROM payments p WHERE p.order_id = o.order_id)
ORDER BY o.channel, o.amount DESC, o.order_id;

-- Part 4. The double-paid list: the same instalment posted more than once.
SELECT p.order_id, o.channel, p.instalment_no, count(*) AS times_posted,
       max(p.amount) AS amount, max(p.amount) * (count(*) - 1) AS surplus
FROM payments p
JOIN orders o ON o.order_id = p.order_id
WHERE o.quarter = 'Q2'
GROUP BY p.order_id, o.channel, p.instalment_no
HAVING count(*) > 1
ORDER BY o.channel, p.order_id;

-- Part 5. The report by channel, with every check beside it.
WITH per_instalment AS (
    SELECT order_id, instalment_no, max(amount) AS amount, count(*) AS times_posted
    FROM payments
    GROUP BY order_id, instalment_no
),
per_order AS (
    SELECT order_id,
           sum(amount) AS collected,
           sum(amount * (times_posted - 1)) AS posted_twice
    FROM per_instalment
    GROUP BY order_id
),
report AS (
    SELECT o.channel,
           count(*) AS orders,
           sum(o.amount) AS booked,
           sum(coalesce(po.collected, 0)) AS collected,
           count(*) FILTER (WHERE po.order_id IS NULL) AS unpaid_orders,
           coalesce(sum(o.amount) FILTER (WHERE po.order_id IS NULL), 0) AS unpaid_booked,
           sum(coalesce(po.posted_twice, 0)) AS posted_twice
    FROM orders o
    LEFT JOIN per_order po ON po.order_id = o.order_id
    WHERE o.quarter = 'Q2'
    GROUP BY o.channel
)
SELECT channel, orders, booked, collected, booked - collected AS gap,
       round(100 * collected / booked, 2) AS pct_collected,
       unpaid_orders, unpaid_booked, posted_twice,
       booked - collected = unpaid_booked AS gap_is_the_unpaid_list
FROM report
ORDER BY channel;

-- The checks. Every row must read true.
WITH per_instalment AS (
    SELECT order_id, instalment_no, max(amount) AS amount, count(*) AS times_posted
    FROM payments
    GROUP BY order_id, instalment_no
),
per_order AS (
    SELECT order_id, sum(amount) AS collected, sum(amount * (times_posted - 1)) AS posted_twice
    FROM per_instalment
    GROUP BY order_id
),
joined AS (
    SELECT o.order_id, o.amount, po.collected, po.posted_twice, po.order_id AS paid_key
    FROM orders o
    LEFT JOIN per_order po ON po.order_id = o.order_id
    WHERE o.quarter = 'Q2'
)
SELECT 'rows out equals rows in' AS check_name,
       (SELECT count(*) FROM joined) = (SELECT count(*) FROM orders WHERE quarter = 'Q2') AS passed
UNION ALL
SELECT 'booked after the join equals booked from orders',
       (SELECT sum(amount) FROM joined) = (SELECT sum(amount) FROM orders WHERE quarter = 'Q2')
UNION ALL
SELECT 'booked minus collected equals the unpaid list',
       (SELECT sum(amount) - sum(coalesce(collected, 0)) FROM joined)
       = (SELECT coalesce(sum(amount), 0) FROM joined WHERE paid_key IS NULL)
UNION ALL
SELECT 'collected plus posted twice equals the feed',
       (SELECT sum(coalesce(collected, 0) + coalesce(posted_twice, 0)) FROM joined)
       = (SELECT sum(p.amount) FROM payments p JOIN orders o ON o.order_id = p.order_id
           WHERE o.quarter = 'Q2')
UNION ALL
SELECT 'every payment row is matched to Q1, Q2 or no order',
       (SELECT count(*) FROM payments)
       = (SELECT count(*) FROM payments p JOIN orders o ON o.order_id = p.order_id)
         + (SELECT count(*) FROM payments p
             WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.order_id = p.order_id));

-- The payments no order can claim, which go back to the platform lead rather than into the report.
SELECT p.payment_id, p.order_id, p.paid_date, p.amount
FROM payments p
WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.order_id = p.order_id)
ORDER BY p.payment_id;

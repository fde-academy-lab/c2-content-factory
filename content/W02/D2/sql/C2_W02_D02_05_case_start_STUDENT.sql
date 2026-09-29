-- Week 2, Tuesday. The escalated case: the booked-against-collected report Anand signs.
-- Anand: "Show me, order by order, what we actually collected against what we booked in Q2.
-- If there is a gap, I want to know which orders and which channel."
-- This file is your starting point. It runs as it stands; each part below says what to add.
-- The brief is exercises/unguided/C2_W02_D02_case_STUDENT.md. Run: psql -d kalpa -f this_file.sql

-- Part 1. The baseline you reconcile to: Q2 orders and booked, by channel, from orders alone.
SELECT channel, count(*) AS orders_in, sum(amount) AS booked
FROM orders
WHERE quarter = 'Q2'
GROUP BY channel
ORDER BY channel;

-- Part 2. Collected by channel at order grain, with the count reconciliation in the comment above it.
-- Write the reconciliation here before you run the query:
--   orders in (part 1):        ____
--   rows out (this query):     ____
--   difference, and why:       ____
-- Start from this CTE, which removes nothing yet. Decide what a retry is before you trust it.
WITH paid_per_order AS (
    SELECT order_id, sum(amount) AS posted, count(*) AS payment_rows
    FROM payments
    GROUP BY order_id
)
SELECT count(*) AS payment_orders, sum(posted) AS posted
FROM paid_per_order;

-- Part 3. The unpaid list: every Q2 order with no payment, with its channel and amount.
-- Part 4. The double-paid list: every Q2 payment the gateway posted more than once, with the surplus.
-- Part 5. The report by channel: booked, collected, gap, unpaid, posted twice, and a check that
--         booked minus collected equals the unpaid total. Then the two sentences to Anand.

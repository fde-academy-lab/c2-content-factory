-- Week 2, Tuesday. Round 3: the unpaid list and the double-paid list.
-- Anand: "If there is a gap, I want to know which orders and which channel."
-- Part A runs on the invented tiny tables; part B runs on the warehouse. Run: psql -d kalpa -f this_file.sql

DROP TABLE IF EXISTS tiny_orders, tiny_payments;
CREATE TEMP TABLE tiny_orders (order_id text PRIMARY KEY, channel text, amount numeric(12, 2), status text);
CREATE TEMP TABLE tiny_payments (payment_id text PRIMARY KEY, order_id text, paid_date date,
                                 amount numeric(12, 2), instalment_no integer);
INSERT INTO tiny_orders VALUES
    ('T-1', 'app', 1000, 'delivered'), ('T-2', 'web', 2000, 'delivered'),
    ('T-3', 'store', 1500, 'delivered'), ('T-4', 'app', 800, 'delivered'),
    ('T-5', 'store', 500, 'delivered');
INSERT INTO tiny_payments VALUES
    ('P-1', 'T-1', '2026-07-03', 1000, 1), ('P-2', 'T-2', '2026-07-05', 1200, 1),
    ('P-3', 'T-2', '2026-08-05', 800, 2), ('P-4', 'T-3', '2026-07-09', 1500, 1),
    ('P-5', 'T-3', '2026-07-09', 1500, 1), ('P-6', 'T-5', '2026-07-12', 500, 1),
    ('P-7', 'T-9', '2026-07-14', 600, 1);

-- A1. The plausible wrong answer: "collected in the quarter", with the date filter in WHERE.
-- The LEFT JOIN is written correctly and still loses the unpaid order. Count the rows.
SELECT o.order_id, o.amount AS booked, p.payment_id, p.paid_date
FROM tiny_orders o
LEFT JOIN tiny_payments p ON p.order_id = o.order_id
WHERE p.paid_date BETWEEN '2026-07-01' AND '2026-09-30'
ORDER BY o.order_id, p.payment_id;

-- A2. The fix: the condition on the payments table moves into the ON clause.
SELECT o.order_id, o.amount AS booked, p.payment_id, p.paid_date
FROM tiny_orders o
LEFT JOIN tiny_payments p
       ON p.order_id = o.order_id
      AND p.paid_date BETWEEN '2026-07-01' AND '2026-09-30'
ORDER BY o.order_id, p.payment_id;

-- A3. The anti-join: the one WHERE on the right-hand table that belongs there, IS NULL on its key.
SELECT o.order_id, o.channel, o.amount AS booked
FROM tiny_orders o
LEFT JOIN tiny_payments p ON p.order_id = o.order_id
WHERE p.payment_id IS NULL;

-- A4. The same question with NOT EXISTS, which reads as the sentence Anand said.
SELECT o.order_id, o.channel, o.amount AS booked
FROM tiny_orders o
WHERE NOT EXISTS (SELECT 1 FROM tiny_payments p WHERE p.order_id = o.order_id);

-- A5. The plausible wrong list: every order with more than one payment row, called double-paid.
SELECT order_id, count(*) AS payment_rows, sum(amount) AS posted
FROM tiny_payments
GROUP BY order_id
HAVING count(*) > 1;

-- A6. The fix: a retry is the same instalment posted twice, so the grain is order and instalment.
SELECT order_id, instalment_no, count(*) AS times_posted, max(amount) AS amount,
       max(amount) * (count(*) - 1) AS posted_twice
FROM tiny_payments
GROUP BY order_id, instalment_no
HAVING count(*) > 1;

-- A7. The payments nobody can match to an order: the anti-join from the other side.
SELECT p.payment_id, p.order_id, p.amount
FROM tiny_payments p
LEFT JOIN tiny_orders o ON o.order_id = p.order_id
WHERE o.order_id IS NULL;

-- Part B. The warehouse. Run each query, read the count first, then the rows.
-- B1. Your unpaid list for Q2: every Q2 order with no payment row, largest first.
SELECT o.order_id, o.channel, o.status, o.amount AS booked
FROM orders o
LEFT JOIN payments p ON p.order_id = o.order_id
WHERE o.quarter = 'Q2'
  AND p.payment_id IS NULL
ORDER BY o.amount DESC, o.order_id;

-- B2. The unpaid list by channel, which is the half of the gap Anand asked for by channel.
SELECT o.channel, count(*) AS unpaid_orders, sum(o.amount) AS unpaid_booked
FROM orders o
WHERE o.quarter = 'Q2'
  AND NOT EXISTS (SELECT 1 FROM payments p WHERE p.order_id = o.order_id)
GROUP BY o.channel
ORDER BY o.channel;

-- B3. Your double-paid list for Q2: the same instalment posted more than once.
SELECT p.order_id, o.channel, p.instalment_no, count(*) AS times_posted,
       max(p.amount) AS amount, max(p.amount) * (count(*) - 1) AS posted_twice
FROM payments p
JOIN orders o ON o.order_id = p.order_id
WHERE o.quarter = 'Q2'
GROUP BY p.order_id, o.channel, p.instalment_no
HAVING count(*) > 1
ORDER BY p.order_id;

-- B4. The check that separates the two lists: an instalment order has instalments 1 and 2,
-- a retry has instalment 1 twice. Count Q2 orders by the pattern of their payment rows.
SELECT pattern, count(*) AS q2_orders
FROM (
    SELECT p.order_id,
           string_agg(p.instalment_no::text, '+' ORDER BY p.instalment_no) AS pattern
    FROM payments p
    JOIN orders o ON o.order_id = p.order_id
    WHERE o.quarter = 'Q2'
    GROUP BY p.order_id
) per_order
GROUP BY pattern
ORDER BY pattern;

-- B5. Every payment row accounted for: matched to a Q1 order, a Q2 order, or to no order at all.
SELECT coalesce(o.quarter, 'no matching order') AS matched_to, count(*) AS payment_rows,
       sum(p.amount) AS amount
FROM payments p
LEFT JOIN orders o ON o.order_id = p.order_id
GROUP BY coalesce(o.quarter, 'no matching order')
ORDER BY matched_to;

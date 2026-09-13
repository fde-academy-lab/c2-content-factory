-- Kalpa Retail, Monday of Week 2. The guided walk.
--
-- Anand wants the growth numbers computed from the warehouse rather than from anybody's laptop.
-- This file is the walk that gets you there: connect, read, filter, group, and find out why the
-- warehouse disagrees with last week's note.
--
-- Run it a block at a time. Every block states the question it answers before it answers it.

-- ---------------------------------------------------------------- 1. the handshake
-- The question: is there a warehouse, and how big is the book?
SELECT count(*) AS orders FROM orders;

-- ---------------------------------------------------------------- 2. what is in here
-- The question: which tables exist, and what does one row of each mean?
SELECT table_name, count(*) AS columns
FROM information_schema.columns
WHERE table_schema = 'public'
GROUP BY table_name
ORDER BY table_name;

-- ---------------------------------------------------------------- 3. the first five rows
-- The question: what does an order actually look like?
SELECT * FROM orders LIMIT 5;

-- ---------------------------------------------------------------- 4. the largest orders
-- The question: which orders are big enough to move a quarter on their own?
-- Last week this took a sort, a slice and thirty lines of Python.
SELECT order_id, customer_id, channel, amount
FROM   orders
ORDER BY amount DESC
LIMIT 5;

-- ---------------------------------------------------------------- 5. the same query, no ORDER BY
-- The question: what does LIMIT alone return?
-- Compare your five rows with the person beside you before reading further.
SELECT order_id, amount FROM orders LIMIT 5;

-- ---------------------------------------------------------------- 6. one quarter only
-- The question: how much did Q1 book?
SELECT count(*) AS orders, sum(amount) AS revenue
FROM   orders
WHERE  quarter = 'Q1';

-- ---------------------------------------------------------------- 7. both quarters, side by side
-- The question: which quarter is bigger, and by how much?
SELECT quarter, count(*) AS orders, sum(amount) AS revenue
FROM   orders
GROUP BY quarter
ORDER BY quarter;

-- ---------------------------------------------------------------- 8. per segment
-- The question: which segment carries the book?
-- Segment lives on the customer, not on the order, so the two tables meet here.
SELECT c.segment, count(*) AS orders, sum(o.amount) AS revenue
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment
ORDER  BY revenue DESC;

-- ---------------------------------------------------------------- 9. the error worth meeting
-- The question: what happens when a selected column is neither grouped nor aggregated?
-- Run it. Read the message. Then fix it two different ways and notice they answer
-- two different questions.
SELECT c.segment, o.channel, sum(o.amount) AS revenue
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment;

-- ---------------------------------------------------------------- 10. WHERE against HAVING
-- The question: which segments placed more than a hundred orders?
-- WHERE filters rows before grouping. HAVING filters groups after.
SELECT c.segment, count(*) AS orders
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment
HAVING count(*) > 100
ORDER  BY orders DESC;

-- ---------------------------------------------------------------- 11. two named steps
-- The question: how did each segment's revenue change from Q1 to Q2?
-- Each block does one thing and is named after the thing it does.
WITH q1 AS (
    SELECT c.segment, sum(o.amount) AS revenue, count(*) AS orders
    FROM orders o JOIN customers c USING (customer_id)
    WHERE o.quarter = 'Q1'
    GROUP BY c.segment
),
q2 AS (
    SELECT c.segment, sum(o.amount) AS revenue, count(*) AS orders
    FROM orders o JOIN customers c USING (customer_id)
    WHERE o.quarter = 'Q2'
    GROUP BY c.segment
)
SELECT q1.segment,
       q1.orders  AS q1_orders,
       q2.orders  AS q2_orders,
       round(100.0 * (q2.orders - q1.orders) / q1.orders, 1) AS order_change_pct
FROM   q1 JOIN q2 USING (segment)
ORDER  BY order_change_pct;

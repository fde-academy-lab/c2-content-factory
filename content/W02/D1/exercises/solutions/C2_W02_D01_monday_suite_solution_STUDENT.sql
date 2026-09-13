-- The Monday extraction suite, solved. Released at close of session.
--
-- Read the comment lines before the SQL. The comment is the deliverable as much as the query is,
-- because it is what an auditor checks the number against.

-- ---------------------------------------------------------------- Q1
-- Q1: revenue and orders per quarter. Denominator is every order in the book, all statuses.
SELECT quarter, count(*) AS orders, sum(amount) AS revenue
FROM   orders
GROUP  BY quarter
ORDER  BY quarter;
-- Q1 538 orders and Rs 10,00,00,000. Q2 462 orders and Rs 9,84,00,000.

-- ---------------------------------------------------------------- Q2
-- Q2: revenue and orders per segment per quarter. Segment is a customer attribute, so the two
--     tables meet on customer_id. Denominator is orders, not customers.
SELECT c.segment, o.quarter, count(*) AS orders, sum(o.amount) AS revenue
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment, o.quarter
ORDER  BY c.segment, o.quarter;

-- ---------------------------------------------------------------- Q3
-- Q3: revenue per channel per quarter. Channel is on the order, so no join is needed.
SELECT channel, quarter, count(*) AS orders, sum(amount) AS revenue
FROM   orders
GROUP  BY channel, quarter
ORDER  BY channel, quarter;

-- ---------------------------------------------------------------- Q4
-- Q4: customers who ordered, per quarter. The denominator is customers who ordered in that
--     quarter, which is not the same as customers on the books. Say which one you mean.
SELECT quarter, count(DISTINCT customer_id) AS customers_who_ordered
FROM   orders
GROUP  BY quarter
ORDER  BY quarter;

-- ---------------------------------------------------------------- Q5
-- Q5: orders per customer, per segment, per quarter. Frequency. The denominator is customers who
--     ordered in that quarter, so a customer who bought nothing does not drag the average down.
SELECT c.segment,
       o.quarter,
       count(*)                    AS orders,
       count(DISTINCT o.customer_id) AS customers,
       round(count(*)::numeric / count(DISTINCT o.customer_id), 2) AS orders_per_customer
FROM   orders o
JOIN   customers c USING (customer_id)
GROUP  BY c.segment, o.quarter
ORDER  BY c.segment, o.quarter;

-- ---------------------------------------------------------------- Q6
-- Q6: the quarter-on-quarter change per segment. Two named steps, joined on segment, one row out
--     per segment. Order count rather than revenue, because frequency is the branch in question.
WITH q1 AS (
    SELECT c.segment, count(*) AS orders, sum(o.amount) AS revenue
    FROM orders o JOIN customers c USING (customer_id)
    WHERE o.quarter = 'Q1'
    GROUP BY c.segment
),
q2 AS (
    SELECT c.segment, count(*) AS orders, sum(o.amount) AS revenue
    FROM orders o JOIN customers c USING (customer_id)
    WHERE o.quarter = 'Q2'
    GROUP BY c.segment
)
SELECT q1.segment,
       q1.orders AS q1_orders,
       q2.orders AS q2_orders,
       round(100.0 * (q2.orders - q1.orders) / q1.orders, 1) AS order_change_pct
FROM   q1 JOIN q2 USING (segment)
ORDER  BY order_change_pct;
-- Retail-Plus falls 34.9 percent on order count while Retail-Core falls 3.0. That is the same
-- finding last week's note carried, now reproducible by somebody who has never met you.

-- Kalpa Retail, Week 2 Monday, chapter 2: does the warehouse tell the same story as Week 1's file?
--
-- Last week the team answered Meera from an extract: 186 cleaned orders, Rs 1,90,00,000 booked in Q1
-- and Rs 1,87,00,000 in Q2, a fall of 1.6 percent, with 69 customers in each quarter. Meera accepted
-- "real, modest, fix frequency" and parked marketing's acquisition budget. Before the warehouse's
-- numbers go on Anand's sheet, every leaf of the tree is set beside last week's, as a change.
--
-- Q1 is April to June 2026 and Q2 is July to September 2026. Customers are the customers who bought
-- in the quarter, each counted once. Revenue is booked revenue, every status included.

-- name: c2_leaves
-- The question: every leaf of the tree for each quarter, from the warehouse.
SELECT quarter,
       count(DISTINCT customer_id) AS customers,
       count(*)                    AS orders,
       sum(amount)                 AS revenue
FROM   orders
GROUP  BY quarter
ORDER  BY quarter;

-- name: c2_bought_in_both
-- The question: which customers bought in both quarters? One row per customer.
SELECT customer_id
FROM   orders
GROUP  BY customer_id
HAVING count(DISTINCT quarter) = 2
ORDER  BY customer_id;

-- name: c2_bought_q1_only
-- The question: which customers bought in Q1 and not in Q2?
SELECT customer_id
FROM   orders
GROUP  BY customer_id
HAVING max(quarter) = 'Q1'
ORDER  BY customer_id;

-- name: c2_bought_q2_only
-- The question: which customers bought in Q2 and not in Q1?
SELECT customer_id
FROM   orders
GROUP  BY customer_id
HAVING min(quarter) = 'Q2'
ORDER  BY customer_id;

-- name: c2_order_ids
-- The question: which order ids does the warehouse hold? Used to test whether the two sources
-- share any order at all.
SELECT order_id
FROM   orders
ORDER  BY order_id;

-- name: c2_customer_ids
-- The question: which customer ids does the warehouse hold?
SELECT customer_id
FROM   customers
ORDER  BY customer_id;

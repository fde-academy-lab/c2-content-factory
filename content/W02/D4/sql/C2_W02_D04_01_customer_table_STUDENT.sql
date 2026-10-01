-- Kalpa Retail, Week 2, Thursday. How recently, how often and how much has each customer bought?
-- Runs unchanged against the Kalpa warehouse: psql -d kalpa -f <this file>.
-- The notebook of the same number runs these same queries through pandas.

-- Option b: the warehouse groups the orders and sends one row per customer who ordered.
SELECT customer_id,
       max(order_date) AS last_order,
       count(*)        AS frequency,
       sum(amount)     AS spend
FROM   orders
GROUP  BY customer_id
ORDER  BY customer_id;

-- The second route: every customer on the list, including those who never ordered.
SELECT c.customer_id,
       c.segment,
       max(o.order_date)          AS last_order,
       count(o.order_id)          AS frequency,
       coalesce(sum(o.amount), 0) AS spend
FROM   customers c
LEFT   JOIN orders o ON o.customer_id = c.customer_id
GROUP  BY c.customer_id, c.segment
ORDER  BY c.customer_id;

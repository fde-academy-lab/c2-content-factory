-- Kalpa Retail, Week 2, Thursday. Of the customers the sale reached, how many bought?
-- Runs unchanged against the Kalpa warehouse: psql -d kalpa -f <this file>.
-- The notebook of the same number runs these same queries through pandas.

-- The hurried version: each reached customer's segment read from their orders.
WITH reached AS (SELECT DISTINCT customer_id FROM campaign_exposure),
     buyers  AS (SELECT o.customer_id, min(c.segment) AS segment, count(*) AS orders
                 FROM   orders o
                 JOIN   customers c ON c.customer_id = o.customer_id
                 GROUP  BY o.customer_id)
SELECT b.segment,
       count(*)        AS reached,
       count(b.orders) AS bought
FROM   reached r
LEFT   JOIN buyers b ON b.customer_id = r.customer_id
GROUP  BY b.segment
ORDER  BY b.segment NULLS LAST;

-- The fix: each reached customer's segment read from the customer list.
WITH reached AS (SELECT DISTINCT customer_id FROM campaign_exposure),
     buyers  AS (SELECT customer_id, count(*) AS orders FROM orders GROUP BY customer_id)
SELECT c.segment,
       count(*)        AS reached,
       count(b.orders) AS bought
FROM   reached r
JOIN   customers c ON c.customer_id = r.customer_id
LEFT   JOIN buyers b ON b.customer_id = r.customer_id
GROUP  BY c.segment
ORDER  BY c.segment;

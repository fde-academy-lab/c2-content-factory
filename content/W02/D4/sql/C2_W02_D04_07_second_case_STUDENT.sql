-- Kalpa Retail, Week 2, Thursday. Did Retail-Plus members order less often in Q2 than in Q1?
-- Runs unchanged against the Kalpa warehouse: psql -d kalpa -f <this file>.
-- The notebook of the same number runs these same queries through pandas.

-- Orders per member, by quarter, for Retail-Plus.
SELECT o.quarter,
       count(*)                    AS orders,
       count(DISTINCT o.customer_id) AS members,
       round(count(*)::numeric / count(DISTINCT o.customer_id), 3) AS orders_per_member
FROM   orders o
JOIN   customers c ON c.customer_id = o.customer_id
WHERE  c.segment = 'Retail-Plus'
GROUP  BY o.quarter
ORDER  BY o.quarter;

-- Kalpa Retail, Week 2, Thursday. How far did Retail-Plus members' spend fall from Q1 to Q2?
-- Runs unchanged against the Kalpa warehouse: psql -d kalpa -f <this file>.
-- The notebook of the same number runs these same queries through pandas.

-- Option c: one column per month, written out by hand.
SELECT o.customer_id,
       sum(o.amount) FILTER (WHERE o.order_date >= DATE '2026-04-01' AND o.order_date < DATE '2026-05-01') AS apr,
       sum(o.amount) FILTER (WHERE o.order_date >= DATE '2026-05-01' AND o.order_date < DATE '2026-06-01') AS may,
       sum(o.amount) FILTER (WHERE o.order_date >= DATE '2026-06-01' AND o.order_date < DATE '2026-07-01') AS jun,
       sum(o.amount) FILTER (WHERE o.order_date >= DATE '2026-07-01' AND o.order_date < DATE '2026-08-01') AS jul,
       sum(o.amount) FILTER (WHERE o.order_date >= DATE '2026-08-01' AND o.order_date < DATE '2026-09-01') AS aug,
       sum(o.amount) FILTER (WHERE o.order_date >= DATE '2026-09-01' AND o.order_date < DATE '2026-10-01') AS sep
FROM   orders o
JOIN   customers c ON c.customer_id = o.customer_id
WHERE  c.segment = 'Retail-Plus'
GROUP  BY o.customer_id
ORDER  BY o.customer_id;

-- The second route: the tier's two quarters, summed where the data lives, with no pivot.
SELECT o.quarter, sum(o.amount) AS spend
FROM   orders o
JOIN   customers c ON c.customer_id = o.customer_id
WHERE  c.segment = 'Retail-Plus'
GROUP  BY o.quarter
ORDER  BY o.quarter;

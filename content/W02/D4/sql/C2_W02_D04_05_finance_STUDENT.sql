-- Kalpa Retail, Week 2, Thursday. Where should Finance's Monday revenue by segment and quarter be computed?
-- Runs unchanged against the Kalpa warehouse: psql -d kalpa -f <this file>.
-- The notebook of the same number runs these same queries through pandas.

-- Finance's number, computed where the data lives: eight rows come back.
SELECT c.segment, o.quarter, sum(o.amount) AS revenue
FROM   orders o
JOIN   customers c ON c.customer_id = o.customer_id
GROUP  BY c.segment, o.quarter
ORDER  BY c.segment, o.quarter;

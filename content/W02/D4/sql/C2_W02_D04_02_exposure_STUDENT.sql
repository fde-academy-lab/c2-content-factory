-- Kalpa Retail, Week 2, Thursday. Which customers did the monsoon sale reach, and what did they spend?
-- Runs unchanged against the Kalpa warehouse: psql -d kalpa -f <this file>.
-- The notebook of the same number runs these same queries through pandas.

-- The second route, part 1: customers the sale reached, each counted once.
SELECT count(DISTINCT customer_id) AS reached
FROM   campaign_exposure;

-- The second route, part 2: what the reached customers ordered, with no join that can multiply rows.
SELECT sum(amount) AS reached_spend
FROM   orders
WHERE  customer_id IN (SELECT customer_id FROM campaign_exposure);

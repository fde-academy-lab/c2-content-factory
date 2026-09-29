# Solution: joins that tell the truth

Answers: 1b 2d 3a 4c 5a 6b 7c 8d 9a 10c 11b

## The idea being tested

The lab moves the day's three habits to a table the day never used: count rows before trusting a
join, keep every condition on the right-hand table in the ON clause, and bring the right-hand table to
the left-hand table's grain before summing. Problem 4 then runs the whole escalated case on Q1, where
the numbers are yours to find.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | b | R-1 to R-4 each find an order and R-5 does not, so four rows. | a: counts orders. c: counts refunded orders and forgets that W-3 has two refunds. d: counts R-5, whose order W-7 is not in the extract. |
| 2 | d | The four matched rows, plus W-1, W-4 and W-6 with NULL refund columns, make seven. | a: a LEFT join keeps each order at least once, and W-3 twice. b: the refund count is the RIGHT join's number. c: adds a count of refunded orders that no join produces. |
| 3 | a | Each refund matches at most one order, because order_id is unique in lab_orders, so every refund row appears once: five. | b: a RIGHT join keeps R-5 with NULL order columns. c: the unrefunded orders belong to the LEFT join. d: counts orders, the wrong side. |
| 4 | c | The LEFT join's seven rows plus R-5 make eight. | a: adds the two tables' row counts. b: misses R-5. d: counts refunds and loses the unrefunded orders. |
| 5 | a | An average per refunded order is a question about matched rows only, so INNER is the honest join, with refunds summed per order first. | b: brings in unrefunded orders, which the question excludes. c: returns only unrefunded orders. d: adds R-5, which has no order to average over. |
| 6 | b | Every order, refunded or not, is the LEFT join, with refunds summed per order first. | a: drops the unrefunded orders from booked. c: returns only unrefunded orders. d: adds refunds with no order to a report about orders. |
| 7 | c | "No refund at all" is the anti-join: LEFT JOIN, then keep the rows where the refund key IS NULL. | a: drops exactly the orders asked for. b: returns every order and leaves the reader to spot the NULLs. d: adds R-5, which is a refund and cannot be surveyed. |
| 8 | d | "On either side" is the FULL join: unrefunded orders and the refund for W-7 in one result. | a: drops both kinds of break. b: misses R-5. c: misses R-5 and drops the matched rows. |
| 9 | a | Reasons exist only on refund rows that match an order, so the INNER join answers it. | b: adds orders with a NULL reason. c: returns orders with no reason at all. d: adds R-5, a reason on an order the desk did not send. |
| 10 | c | The WHERE on refund_date removes every order whose refund columns are NULL, which is W-1, W-4 and W-6, and W-3's two refunds put its 48,000 into booked twice. | a: the orders table holds 75,600. b: misses the repeated W-3. d: misses the three dropped orders. |
| 11 | b | Refunds summed per order in the window, joined in with a LEFT join: 18,900 refunded over 75,600 booked is 25.0 percent. | a: moving the filter into ON restores the three orders and leaves W-3 doubled, so booked is 1,23,600. c: the refunded total was right all along, and the denominator was the fault. d: R-5 belongs to an order outside this book, so it cannot sit in this rate. |

The corrected query for problem 3:

```sql
-- Orders in: 6, booked 75,600, from lab_orders alone.
-- Rows out:  6, because refunds are summed to one row per order before the join,
--            and the date window sits inside the refunds step, so no order is filtered away.
-- Difference: none. R-5 matches no order and stays out of this rate.
WITH refunded_per_order AS (
    SELECT order_id, -sum(amount) AS refunded
    FROM lab_refunds
    WHERE refund_date BETWEEN '2026-04-01' AND '2026-06-28'
    GROUP BY order_id
)
SELECT count(*) AS rows_out,
       sum(o.amount) AS booked,
       sum(coalesce(rp.refunded, 0)) AS refunded,
       round(100.0 * sum(coalesce(rp.refunded, 0)) / sum(o.amount), 1) AS refund_rate
FROM lab_orders o
LEFT JOIN refunded_per_order rp ON rp.order_id = o.order_id;
```

A WHERE inside the CTE is safe, because it filters the refunds before the join, and the LEFT join
still keeps every order. The ON clause version, `LEFT JOIN lab_refunds r ON r.order_id = o.order_id
AND r.refund_date BETWEEN ...`, fixes the lost orders and still needs the per-order sum for W-3.

## Problem 4, the approach and the invariants

The queries below are the escalated case moved to Q1. They give no Q1 numbers here, because the
numbers are what you run for; your own output must satisfy every invariant under them.

```sql
-- 1. Q1 baseline, from orders alone.
SELECT channel, count(*) AS orders_in, sum(amount) AS booked
FROM orders
WHERE quarter = 'Q1'
GROUP BY channel
ORDER BY channel;

-- 2 and 4. Collected at order grain, a retry counted once, with the report and its checks.
WITH per_instalment AS (
    SELECT order_id, instalment_no, max(amount) AS amount, count(*) AS times_posted
    FROM payments
    GROUP BY order_id, instalment_no
),
per_order AS (
    SELECT order_id,
           sum(amount) AS collected,
           sum(amount * (times_posted - 1)) AS posted_twice
    FROM per_instalment
    GROUP BY order_id
),
report AS (
    SELECT o.channel,
           count(*) AS orders,
           sum(o.amount) AS booked,
           sum(coalesce(po.collected, 0)) AS collected,
           count(*) FILTER (WHERE po.order_id IS NULL) AS unpaid_orders,
           coalesce(sum(o.amount) FILTER (WHERE po.order_id IS NULL), 0) AS unpaid_booked,
           sum(coalesce(po.posted_twice, 0)) AS posted_twice
    FROM orders o
    LEFT JOIN per_order po ON po.order_id = o.order_id
    WHERE o.quarter = 'Q1'
    GROUP BY o.channel
)
SELECT channel, orders, booked, collected, booked - collected AS gap,
       unpaid_orders, unpaid_booked, posted_twice,
       booked - collected = unpaid_booked AS gap_is_the_unpaid_list
FROM report
ORDER BY channel;

-- 3a. The Q1 unpaid list.
SELECT o.order_id, o.channel, o.status, o.amount AS booked
FROM orders o
WHERE o.quarter = 'Q1'
  AND NOT EXISTS (SELECT 1 FROM payments p WHERE p.order_id = o.order_id)
ORDER BY o.amount DESC, o.order_id;

-- 3b. The Q1 double-paid list: the same instalment posted more than once.
SELECT p.order_id, o.channel, p.instalment_no, count(*) AS times_posted,
       max(p.amount) AS amount, max(p.amount) * (count(*) - 1) AS surplus
FROM payments p
JOIN orders o ON o.order_id = p.order_id
WHERE o.quarter = 'Q1'
GROUP BY p.order_id, o.channel, p.instalment_no
HAVING count(*) > 1
ORDER BY o.channel, p.order_id;

-- 4. The feed check for Q1: collected plus the surplus equals what the feed posted against Q1.
WITH per_instalment AS (
    SELECT order_id, instalment_no, max(amount) AS amount, count(*) AS times_posted
    FROM payments
    GROUP BY order_id, instalment_no
),
per_order AS (
    SELECT order_id, sum(amount) AS collected, sum(amount * (times_posted - 1)) AS posted_twice
    FROM per_instalment
    GROUP BY order_id
)
SELECT sum(coalesce(po.collected, 0) + coalesce(po.posted_twice, 0))
       = (SELECT sum(p.amount) FROM payments p
            JOIN orders o ON o.order_id = p.order_id
           WHERE o.quarter = 'Q1') AS feed_reconciles,
       count(*) = (SELECT count(*) FROM orders WHERE quarter = 'Q1') AS rows_reconcile
FROM orders o
LEFT JOIN per_order po ON po.order_id = o.order_id
WHERE o.quarter = 'Q1';

-- Stretch. Refunded and collected net of refunds, by channel. Refunds are stored as negatives.
WITH per_instalment AS (
    SELECT order_id, instalment_no, max(amount) AS amount
    FROM payments
    GROUP BY order_id, instalment_no
),
per_order AS (
    SELECT order_id, sum(amount) AS collected FROM per_instalment GROUP BY order_id
),
refunded_per_order AS (
    SELECT order_id, -sum(amount) AS refunded FROM refunds GROUP BY order_id
)
SELECT o.channel,
       sum(coalesce(po.collected, 0)) AS collected,
       sum(coalesce(rp.refunded, 0)) AS refunded,
       sum(coalesce(po.collected, 0)) - sum(coalesce(rp.refunded, 0)) AS collected_net
FROM orders o
LEFT JOIN per_order po ON po.order_id = o.order_id
LEFT JOIN refunded_per_order rp ON rp.order_id = o.order_id
WHERE o.quarter = 'Q1'
GROUP BY o.channel
ORDER BY o.channel;
```

The invariants your Q1 output must satisfy:

| Invariant | Why it must hold |
|---|---|
| Rows out equals the Q1 order count from query 1 | Payments were brought to one row per order before the join, so nothing repeats |
| Booked after the join equals booked from query 1, per channel | The same, in rupees |
| Booked minus collected equals the unpaid list's booked total, per channel | With retries removed, the only reason an order's collected differs from its booked is that nothing arrived |
| Collected plus the surplus on the double-paid list equals the feed's total against Q1 orders | Every posting against a Q1 order is either counted once in collected or named as a surplus |
| The double-paid list is shorter than `GROUP BY order_id HAVING COUNT(*) > 1` | The shorter list holds retries only; the longer one also holds every two-instalment order |
| In the stretch, the refunds step joins at order grain | An order refunded twice would otherwise repeat in the join, as W-3 did in problem 3 |

Whatever the gap turns out to be for Q1, the sentence to Anand gives it with its explanation, and a
gap of any size is reported with the check that proves it.

## The part worth arguing about

The stretch question. Net of refunds is the money Kalpa kept, which is what Anand ultimately wants;
collected is the money that arrived, which is what his question this morning asked. The report he
signs can carry both columns if each is named, and a refund must never be subtracted from booked
instead, or the gap would no longer be the unpaid list.

## Where the pattern lives in production

Refund rates, return rates and chargeback rates are all a rate over a joined table, and each goes
wrong in these two ways. Marketplaces report refund rate against orders placed in the period and
refunds raised against those orders, which is the ON clause and the per-order sum written as policy.

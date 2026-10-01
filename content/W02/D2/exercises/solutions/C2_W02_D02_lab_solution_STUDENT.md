# Solution: do the day's joins still tell the truth on refunds?

Answers: 1b 2d 3a 4c 5a 6b 7c 8d 9a 10c 11b

## What does the lab test?

The lab moves the day's three habits to a table the day never used: count rows before trusting a
join, keep every condition on the right-hand table in the ON clause, and bring the right-hand table to
the left-hand table's grain before summing. Problem 4 then runs the whole escalated case on Q1, where
the numbers are yours to find.

## What did the lab give you to work from?

The returns desk has sent six Q1 web orders and the refund rows raised against order ids in their
range. Every number here is invented for the lab.

`lab_orders` (invented):

| order_id | channel | amount |
|---|---|---|
| W-1 | web | 3,200 |
| W-2 | web | 12,500 |
| W-3 | web | 48,000 |
| W-4 | web | 1,900 |
| W-5 | web | 7,400 |
| W-6 | web | 2,600 |

`lab_refunds` (invented; refunds are stored as negative amounts, as the warehouse stores them):

| refund_id | order_id | refund_date | amount | reason |
|---|---|---|---|---|
| R-1 | W-2 | 2026-04-18 | -1,500 | damaged |
| R-2 | W-3 | 2026-04-22 | -6,000 | wrong item |
| R-3 | W-3 | 2026-05-06 | -4,000 | damaged |
| R-4 | W-5 | 2026-05-10 | -7,400 | returned in full |
| R-5 | W-7 | 2026-04-03 | -900 | damaged |

To load them, paste this into a psql session; they are TEMP tables and vanish when you disconnect.

```sql
CREATE TEMP TABLE lab_orders (order_id text PRIMARY KEY, channel text, amount numeric(12, 2));
CREATE TEMP TABLE lab_refunds (refund_id text PRIMARY KEY, order_id text, refund_date date,
                               amount numeric(12, 2), reason text);
INSERT INTO lab_orders VALUES
    ('W-1', 'web', 3200), ('W-2', 'web', 12500), ('W-3', 'web', 48000),
    ('W-4', 'web', 1900), ('W-5', 'web', 7400), ('W-6', 'web', 2600);
INSERT INTO lab_refunds VALUES
    ('R-1', 'W-2', '2026-04-18', -1500, 'damaged'),
    ('R-2', 'W-3', '2026-04-22', -6000, 'wrong item'),
    ('R-3', 'W-3', '2026-05-06', -4000, 'damaged'),
    ('R-4', 'W-5', '2026-05-10', -7400, 'returned in full'),
    ('R-5', 'W-7', '2026-04-03', -900, 'damaged');
```

## Why does each key hold, item by item?

#### Problem 1. How many rows does each join return on the refund tables?

Write your four numbers on paper before you run anything. Then run the four joins and mark each
prediction right or wrong, with the row that surprised you.

### Q1. How many rows does `lab_orders JOIN lab_refunds ON order_id` return?

The key is b, "4, one row per refund that finds its order". R-1 to R-4 each find an order and R-5 does not, so four rows.

- a, "6, one row for each order the desk sent": counts orders.
- c, "3, one row for each order that was refunded": counts refunded orders and forgets that W-3 has two refunds.
- d, "5, one row for each refund row on the list": counts R-5, whose order W-7 is not in the extract.

### Q2. How many rows does the LEFT join from orders to refunds return?

The key is d, "7, four matched rows and three unrefunded". The four matched rows, plus W-1, W-4 and W-6 with NULL refund columns, make seven.

- a, "6, since a LEFT join keeps each order once": a LEFT join keeps each order at least once, and W-3 twice.
- b, "5, the same as the refund rows on the list": the refund count is the RIGHT join's number.
- c, "9, the six orders and three refunded ones": adds a count of refunded orders that no join produces.

### Q3. How many rows does the RIGHT join from orders to refunds return?

The key is a, "5, every refund row once, as ids are unique". Each refund matches at most one order, because order_id is unique in lab_orders, so every refund row appears once: five.

- b, "4, since a refund with no order is dropped": a RIGHT join keeps R-5 with NULL order columns.
- c, "7, the matched rows and the unrefunded orders": the unrefunded orders belong to the LEFT join.
- d, "6, one row for each order the desk sent over": counts orders, the wrong side.

### Q4. How many rows does the FULL join return?

The key is c, "8, the LEFT join's rows and the refund for W-7". The LEFT join's seven rows plus R-5 make eight.

- a, "11, the six orders and the five refunds added": adds the two tables' row counts.
- b, "7, the same as the LEFT join and no more": misses R-5.
- d, "5, one row per refund, the larger table's count": counts refunds and loses the unrefunded orders.

#### Problem 2. Which join answers each of five business questions?

Items 5 to 9 share the same four options, and an option may answer more than one item.

### Q5. The returns desk asks: "For the orders that were refunded, what was the average refund per order?" Which join answers it?

The key is a, "INNER JOIN, matched pairs only". An average per refunded order is a question about matched rows only, so INNER is the honest join, with refunds summed per order first.

- b, "LEFT JOIN, every order kept": brings in unrefunded orders, which the question excludes.
- c, "Anti-join, unmatched orders": returns only unrefunded orders.
- d, "FULL JOIN, both sides' orphans": adds R-5, which has no order to average over.

### Q6. Anand asks: "For every Q1 web order, booked and refunded, whether it was refunded or not?" Which join answers it?

The key is b, "LEFT JOIN, every order kept". Every order, refunded or not, is the LEFT join, with refunds summed per order first.

- a, "INNER JOIN, matched pairs only": drops the unrefunded orders from booked.
- c, "Anti-join, unmatched orders": returns only unrefunded orders.
- d, "FULL JOIN, both sides' orphans": adds refunds with no order to a report about orders.

### Q7. Kavya Nair, the team's senior analyst, asks: "Which Q1 web orders have no refund at all, so we can sample them for the satisfaction survey?" Which join answers it?

The key is c, "Anti-join, unmatched orders". "No refund at all" is the anti-join: LEFT JOIN, then keep the rows where the refund key IS NULL.

- a, "INNER JOIN, matched pairs only": drops exactly the orders asked for.
- b, "LEFT JOIN, every order kept": returns every order and leaves the reader to spot the NULLs.
- d, "FULL JOIN, both sides' orphans": adds R-5, which is a refund and cannot be surveyed.

### Q8. The auditor asks: "Which orders and which refunds fail to find each other, on either side?" Which join answers it?

The key is d, "FULL JOIN, both sides' orphans". "On either side" is the FULL join: unrefunded orders and the refund for W-7 in one result.

- a, "INNER JOIN, matched pairs only": drops both kinds of break.
- b, "LEFT JOIN, every order kept": misses R-5.
- c, "Anti-join, unmatched orders": misses R-5 and drops the matched rows.

### Q9. The returns desk asks: "Which refund reasons came up on refunded orders, and how often?" Which join answers it?

The key is a, "INNER JOIN, matched pairs only". Reasons exist only on refund rows that match an order, so the INNER join answers it.

- b, "LEFT JOIN, every order kept": adds orders with a NULL reason.
- c, "Anti-join, unmatched orders": returns orders with no reason at all.
- d, "FULL JOIN, both sides' orphans": adds R-5, a reason on an order the desk did not send.

#### Problem 3. Is 16.3 percent the right Q1 refund rate for these six orders?

Anand wants the Q1 refund rate on these web orders: refunded value over booked value. A teammate
sends this, and reports 16.3 percent:

```sql
SELECT count(*) AS rows_out,
       sum(o.amount) AS booked,
       -sum(r.amount) AS refunded,
       round(100.0 * -sum(r.amount) / sum(o.amount), 1) AS refund_rate
FROM lab_orders o
LEFT JOIN lab_refunds r ON r.order_id = o.order_id
WHERE r.refund_date BETWEEN '2026-04-01' AND '2026-06-28';
```

| rows_out | booked | refunded | refund_rate |
|---|---|---|---|
| 4 | 1,15,900 | 18,900 | 16.3 |

### Q10. Which orders make up the booked figure of 1,15,900 that the rate divides by?

The key is c, "the refunded orders, with W-3 counted twice". The WHERE on refund_date removes every order whose refund columns are NULL, which is W-1, W-4 and W-6, and W-3's two refunds put its 48,000 into booked twice: 12,500 + 48,000 + 48,000 + 7,400 is 1,15,900.

- a, "all six orders, each of them counted once": the six orders once each book 3,200 + 12,500 + 48,000 + 1,900 + 7,400 + 2,600, which is 75,600, the figure the rate should divide by.
- b, "the three refunded orders, each counted once": 12,500 + 48,000 + 7,400 is 67,900, which sees the dropped orders and misses W-3 written twice.
- d, "all six orders, with W-3 counted twice": 75,600 + 48,000 is 1,23,600, which sees W-3 twice and misses the three dropped orders.

### Q11. What Q1 refund rate should Anand be given for these six orders?

The key is b, "25.0 percent, 18,900 over 75,600". The numerator is the four refunds on the desk's orders, 1,500 + 6,000 + 4,000 + 7,400, which is 18,900, and the denominator is the six orders counted once each, 75,600. Refunds summed per order in the window and joined with a LEFT join give exactly that: 18,900 over 75,600 is 25.0 percent.

- a, "15.3 percent, 18,900 over 1,23,600": moves the date filter into ON, which restores the three dropped orders and leaves W-3 doubled, so the denominator is 1,23,600.
- c, "16.3 percent, 18,900 over 1,15,900": the teammate's rate; the refunded total was right all along, and the denominator is the fault.
- d, "26.2 percent, 19,800 over 75,600": adds R-5's 900 to the refunds, and R-5 belongs to W-7, an order outside this book, so it cannot sit in this rate.

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

## How should problem 4 be approached, and what must hold?

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
| Booked minus collected equals the unpaid list's booked total, per channel | The gap is the never-paid orders plus what the orders paid short still owe, so it equals the unpaid list alone only when no order is paid short; if this check reads false, look for an order paid in part before you suspect the join |
| Collected plus the surplus on the double-paid list equals the feed's total against Q1 orders | Every posting against a Q1 order is either counted once in collected or named as a surplus |
| The double-paid list is shorter than `GROUP BY order_id HAVING COUNT(*) > 1` | The shorter list holds retries only; the longer one also holds every two-instalment order |
| In the stretch, the refunds step joins at order grain | An order refunded twice would otherwise repeat in the join, as W-3 did in problem 3 |

Whatever the gap turns out to be for Q1, the sentence to Anand gives it with its explanation, and a
gap of any size is reported with the check that proves it.

## Which part is worth arguing about?

In the stretch question, net of refunds is the money Kalpa kept, which is what Anand ultimately
wants; collected is the money that arrived, which is what his question this morning asked. The
report he signs can carry both columns if each is named, and a refund must never be subtracted from
booked instead, or the gap would no longer be the unpaid list.

## Where does this pattern live in production?

Refund rates, return rates and chargeback rates are all a rate over a joined table, and each goes
wrong in these two ways. Marketplaces report refund rate against orders placed in the period and
refunds raised against those orders, which is the ON clause and the per-order sum written as policy.

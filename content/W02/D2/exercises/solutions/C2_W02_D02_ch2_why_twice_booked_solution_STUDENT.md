# Solution: why does the first join report nearly twice the bookings?

Answers: 1c 2a 3c 4b 5b 6d

## What does this set test?

The set tests whether you see that a join multiplies rows before any sum runs, on a week the chapter
never used, and that a fix has to say which repeats it removes. Items 3, 4 and 5 are design items:
the fix chosen on a sizing, a count of the bookings DISTINCT loses, and the fact that would make
DISTINCT exact.

## What did the set give you to work from?

> **The client asks.** "Booked revenue is not collected revenue. Some orders are paid in two
> instalments, some are refunded, some were never paid at all. Show me, order by order, what we
> actually collected against what we booked."
>
> Anand Iyer, finance controller, Kalpa Retail

**Who needs the answer.** Anand would read a collected figure far above his books as collections
running ahead and stand his collections team down. You need it too, since the way you attach payments
here carries every later number.

- **Booked** is every order at its amount; **collected** is the cash that arrived, each payment
  counted once; collected can never honestly exceed booked.
- `FILTER (WHERE ...)` restricts one aggregate to the rows that meet a condition.
- A **CTE**, `WITH name AS (...)`, is a named subquery the main query reads.

The invented week:

| What the orders were | Orders | Payment rows each |
|---|---|---|
| Paid once, in full | 255 | 1 |
| Paid in two instalments | 120 | 2 |
| Paid once, and that payment posted twice by a gateway retry | 10 | 2 |
| Never paid | 15 | 0 |
| **All orders** | **400** | |

The 400 orders book Rs 20,00,000 in all.

## Why does each key hold, item by item?

### Q1. How many rows does the first join return for the week?

`orders o LEFT JOIN payments p ON p.order_id = o.order_id`, on the whole week. How many rows come back?

The key is c, "530: every payment row, plus one per unpaid order". 255 single rows, 240 instalment rows and 20 rows for the retried orders make 515 payment rows, and the 15 unpaid orders each add one row with NULLs: 530.

- a, "400, since a LEFT JOIN keeps each order exactly once": a LEFT JOIN keeps each order at least once, and repeats it per matching row.
- b, "515, one row for each payment row": forgets the 15 unpaid orders.
- d, "545: every order plus every payment row": adds the 400 orders to the 515 payment rows, which no join does.

### Q2. Why can every row be right while the total is wrong?

The draft sums `o.amount` over that join, `FILTER (WHERE p.payment_id IS NOT NULL)`, and reports collected well above Rs 20,00,000. Every row on it is a real order beside a real payment. Why is the total wrong?

The key is a, "the sum runs per payment row, repeating each order's amount". An order with two payment rows is written twice, and its booked amount rides along on both, so `sum(o.amount)` runs at the payment's grain.

- b, "FILTER counts the unpaid orders as paid, each at its booked amount": the FILTER keeps only rows with a payment, so unpaid orders add nothing.
- c, "the LEFT JOIN adds NULL rows, and sum() counts each as an order": `sum()` skips the NULL rows and never counts them.
- d, "the feed stores each amount twice, once for every instalment": two instalments are two real payments, each stored once.

### Q3. Which of four fixes should the week's report use? (Design)

Four ways a team could stop the double count on this week:

| Option | How it works | What it does on this week |
|---|---|---|
| A | Bring payments to one row per order in a CTE, then LEFT JOIN | 400 rows, Rs 20,00,000 booked, a payment-row count kept per order |
| B | `sum(DISTINCT o.amount)` after the join | one sum; 160 of the 400 orders share their amount with another order |
| C | Keep the first posting of each order and instalment, with a tool taught later | still two rows for each two-instalment order |
| D | Ask the platform lead to fix the feed | weeks of work, and this week stays as posted |

Which fix gives Anand an honest booked figure and keeps the repeats visible for a double-paid list?

The key is c, "A, since it joins one row per order and keeps each order's row count". A meets the orders at their own grain, keeps booked exact at Rs 20,00,000 and keeps a count of payment rows, so the ten retried orders stay visible for the double-paid list.

- a, "B, since DISTINCT removes every repeat, whatever caused it": removes repeated values, and 160 orders share an amount with another, so real bookings vanish.
- b, "C, since it keeps one posting per instalment and drops every retry row": C does drop every retry row, but it keeps both instalments of a two-instalment order, so the join still repeats that order and booked stays inflated.
- d, "D, since only a repaired feed can ever be trusted": D is the right request, and it changes nothing about this week.

### Q4. How much booking does DISTINCT lose? (Design)

In the invented week, 160 of the 400 orders share their amount with at least one other order, across 60 distinct amounts. How many orders' amounts does `sum(DISTINCT o.amount)` leave out of booked?

The key is b, "100, all but one per shared amount". DISTINCT keeps each of the 60 shared amounts once, so of the 160 orders that share one, 100 lose their amount from booked.

- a, "60, one for each amount that repeats": 60 is what it keeps.
- c, "160, every order that shares an amount": counts every sharing order as lost, when one per amount survives.
- d, "none, since DISTINCT keeps every order": DISTINCT works on values, and a repeated value is not a repeated order.

### Q5. Which fact would make a DISTINCT before the join exact? (Design)

Which fact about the feed would let a DISTINCT, taken on the payments before any join, remove exactly the retries and nothing else?

The key is b, "each row carried the gateway's reference, repeated on a retry". A gateway reference repeated on a retry shows that the two rows are one payment, so a DISTINCT on it removes the retry and leaves both instalments of a two-part order.

- a, "the orders table held exactly one row for every single order id": one row per order was already true, and the repeats sit in payments.
- c, "the payments table carried an index on its order_id column": an index changes how fast the query runs and leaves the rows as they are.
- d, "each retry were posted a day after the payment it repeats": a retry posted a day later differs from the payment it repeats in its date, so a DISTINCT over the row keeps both.

### Q6. Which check proves the fixed join added and lost nothing?

The fixed join returns 400 rows. Which second check proves that it neither added nor lost anything?

The key is d, "each table summed alone equals the join's booked and posted". Booked recomputed from `orders` alone and posted from `payments` alone never join, so they cannot fan out; if the fixed join added or lost anything, one of them disagrees.

- a, "the fixed join returns as many rows as the payments table holds": 400 orders against 515 payment rows would fail on a correct join.
- b, "the join's booked equals the first draft's collected, halved": assumes every order doubled, which only the 130 multi-row orders did.
- c, "the fixed query runs cold, top to bottom, with no error": a query can run cleanly and still be wrong.

## Which item is worth arguing about?

Item 3's option b, a window dedupe, sounds like the precise fix. It keeps the first posting of each
order and instalment, so a retry goes and a second instalment stays, and the join still repeats every
two-instalment order. The fix has to change the grain before the join, and only A does that.

## Where does this pattern live in production?

dbt's MetricFlow documentation defines a fan-out join as one row joined to several rows in another
table, "resulting in more output rows than input rows", and MetricFlow restricts such joins so a
metric cannot be summed at the wrong grain (docs.getdbt.com, Joins, checked 1 Oct 2026).

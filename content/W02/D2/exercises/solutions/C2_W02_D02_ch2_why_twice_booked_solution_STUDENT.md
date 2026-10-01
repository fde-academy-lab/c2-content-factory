# Solution: why does the first join report nearly twice the bookings?

Answers: 1c 2a 3c 4b 5b 6d

## What does this set test?

The set tests whether you see that a join multiplies rows before any sum runs, on a week the chapter
never used, and that a fix has to say which repeats it removes. Items 3, 4 and 5 are design items:
the fix chosen by working out what each of four would put in booked, a count of the bookings DISTINCT
loses, and the fact that would make DISTINCT exact.

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
  counted once; collected can never honestly exceed booked. **Posted** is every payment row the feed
  holds, repeats included.
- A **retry** is one payment the gateway posted twice.
- `FILTER (WHERE ...)` restricts one aggregate to the rows that meet a condition.
- `DISTINCT` drops repeated values before an aggregate reads them: `sum(DISTINCT x)` adds each
  different value of x once, and `SELECT DISTINCT` returns each different row once.
- A **CTE**, `WITH name AS (...)`, is a named subquery the main query reads.

The invented week:

| What the orders were | Orders | Payment rows each | Booked |
|---|---|---|---|
| Paid once, in full | 255 | 1 | Rs 12,40,000 |
| Paid in full in two instalments | 120 | 2 | Rs 6,30,000 |
| Paid once, in full, and that payment posted twice by a gateway retry | 10 | 2 | Rs 40,000 |
| Never paid | 15 | 0 | Rs 90,000 |
| **All orders** | **400** | | **Rs 20,00,000** |

## Why does each key hold, item by item?

### Q1. How many rows does the first join return for the week?

`orders o LEFT JOIN payments p ON p.order_id = o.order_id`, on the whole week. How many rows come back?

The key is c, "530, every payment row plus one per unpaid order". 255 single rows, 240 instalment rows and 20 rows for the retried orders make 515 payment rows, and the 15 unpaid orders each add one row with NULLs: 530.

- a, "400, since a LEFT JOIN keeps each order exactly once": a LEFT JOIN keeps each order at least once, and repeats it per matching row.
- b, "515, one row for each payment row in the feed": forgets the 15 unpaid orders.
- d, "520, every payment once plus one per unpaid order": counts each retried payment once, 255 + 240 + 10 + 15 is 520; the join cannot tell a retry from a payment and writes a row for each of the 20 retry rows, so it returns 530.

### Q2. Why can every row be right while the total is wrong?

The draft sums `o.amount` over that join, `FILTER (WHERE p.payment_id IS NOT NULL)`, and reports collected well above Rs 20,00,000. Every row on it is a real order beside a real payment. Why is the total wrong?

The key is a, "the sum runs per payment row, repeating each order's amount". An order with two payment rows is written twice, and its booked amount rides along on both, so `sum(o.amount)` runs at the payment's grain: Rs 12,40,000 + 2 x 6,30,000 + 2 x 40,000 is Rs 25,80,000.

- b, "FILTER counts the unpaid orders as paid, each at its booked amount": the FILTER keeps only rows with a payment, so unpaid orders add nothing.
- c, "the LEFT JOIN adds NULL rows, and sum() counts each as an order": `sum()` skips the NULL rows and never counts them.
- d, "the feed stores each amount twice, once for every instalment": two instalments are two real payments, each stored once.

### Q3. Which of four fixes should the week's report use? (Design)

Four ways a team could stop the double count on this week:

| Option | How it works |
|---|---|
| A | Bring payments to one row per order in a CTE, keeping a count of payment rows, then LEFT JOIN |
| B | `sum(DISTINCT o.amount)` after the join; 160 of the 400 orders share their amount with another order |
| C | Keep the first posting of each order and instalment, with a tool taught later, then LEFT JOIN |
| D | Ask the platform lead to fix the feed, and send this week's report as the first join gives it |

Work out from the week's table what each fix would put in booked. Which fix should the week's report use?

The key is c, "A, since one row per order brings booked to Rs 20,00,000". A meets the 400 orders at their own grain, so the join returns 400 rows and sums each order once: Rs 12,40,000 + 6,30,000 + 40,000 + 90,000 is Rs 20,00,000, an error of nil, and the count of payment rows it keeps still flags every order with more than one.

- a, "B, since DISTINCT brings booked back to Rs 20,00,000": DISTINCT keeps each different amount once, and 160 orders share 60 amounts, so 100 orders' amounts drop out and booked falls short of Rs 20,00,000 by whatever those 100 orders booked.
- b, "C, since one row per instalment brings booked to Rs 20,00,000": C drops the ten retry rows and keeps both instalments of every two-instalment order, so the join returns 520 rows and booked reads Rs 12,40,000 + 2 x 6,30,000 + 40,000 + 90,000, which is Rs 26,30,000, still Rs 6,30,000 over.
- d, "D, since the first join overstates booked by only Rs 40,000": the first join writes every two-row order twice, so it overstates booked by the instalment orders' Rs 6,30,000 and the retried orders' Rs 40,000, Rs 6,70,000 in all (Rs 26,70,000 against Rs 20,00,000), and a repaired feed changes nothing about this week.

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
- c, "no two orders in the week were booked at the same amount": that fact would make fix B, `sum(DISTINCT o.amount)` after the join, exact for booked; it says nothing about the payments, where a retry and a second instalment of the same amount look alike to a DISTINCT on order and amount.
- d, "each retry were posted a day after the payment it repeats": a retry posted a day later differs from the payment it repeats in its date, so a DISTINCT over the row keeps both.

### Q6. Which check proves the fixed join added and lost nothing?

The fixed join is ready for the week's report. Which second check proves that it neither added nor lost anything?

The key is d, "each table summed alone equals the join's booked and posted". Booked recomputed from `orders` alone and posted from `payments` alone never join, so they cannot fan out; if the fixed join added or lost anything, one of them disagrees.

- a, "the fixed join returns as many rows as the payments table holds": a correct fixed join returns one row for each of the week's 400 orders, against 515 payment rows, so this check fails on a join that is right.
- b, "the join's collected sits at or below its booked, as it must": it holds whether or not the join went wrong here. Collected is Rs 19,10,000 (booked less the never-paid Rs 90,000); dropping every unpaid order takes booked down to that and no lower, and keeping the ten retries lifts collected to Rs 19,50,000, still under Rs 20,00,000, so the check cannot fail on either fault.
- c, "the fixed query runs cold, top to bottom, with no error": a query can run cleanly and still be wrong.

## Which item is worth arguing about?

Item 3's option b sounds like the precise fix, since C does drop every retry row. It keeps both
instalments of each two-instalment order, so the join still writes those 120 orders twice and booked
reads Rs 26,30,000. The fix has to change the grain before the join, and only A does that.

## Where does this pattern live in production?

dbt's MetricFlow documentation defines a fan-out join as one row joined to several rows in another
table, "resulting in more output rows than input rows", and MetricFlow restricts such joins so a
metric cannot be summed at the wrong grain (docs.getdbt.com, Joins, checked 1 Oct 2026).

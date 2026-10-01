# Why does the first join report nearly twice the bookings, and how do we attach payments so that nothing counts twice?

The chapter 2 set has six items on an invented week at a smaller shop, so none of its numbers comes
from Kalpa's warehouse. Items 1 and 2 close the chapter live; the rest open the TA-led practice lab
or are worked tonight.

> **The client asks.** "Booked revenue is not collected revenue. Some orders are paid in two
> instalments, some are refunded, some were never paid at all. Show me, order by order, what we
> actually collected against what we booked."
>
> Anand Iyer, finance controller, Kalpa Retail

## What do you need to know before the items?

**Who needs the answer.** Anand would read a collected figure far above his books as collections
running ahead and stand his collections team down. You need it too, since the way you attach payments
here carries every later number.

**The questions on the way.**

- How many rows does the first join return for the week?
- Why can every row be right while the total is wrong?
- Which of four fixes should the week's report use?
- How much booking does DISTINCT lose?
- Which fact would make a DISTINCT before the join exact?
- Which check proves the fixed join added and lost nothing?

An item marked Design asks for the best-fit approach, a sizing, the fact that would switch it, or the second route.

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

Post one line, six letters in item order, no spaces:

```
Post exactly this shape: xxxxxx
```

---

### Q1. How many rows does the first join return for the week?

`orders o LEFT JOIN payments p ON p.order_id = o.order_id`, on the whole week. How many rows come back?

a) 400, since a LEFT JOIN keeps each order exactly once
b) 515, one row for each payment row in the feed
c) 530, every payment row plus one per unpaid order
d) 520, every payment once plus one per unpaid order

### Q2. Why can every row be right while the total is wrong?

The draft sums `o.amount` over that join, `FILTER (WHERE p.payment_id IS NOT NULL)`, and reports collected well above Rs 20,00,000. Every row on it is a real order beside a real payment. Why is the total wrong?

a) the sum runs per payment row, repeating each order's amount
b) FILTER counts the unpaid orders as paid, each at its booked amount
c) the LEFT JOIN adds NULL rows, and sum() counts each as an order
d) the feed stores each amount twice, once for every instalment

### Q3. Which of four fixes should the week's report use? (Design)

Four ways a team could stop the double count on this week:

| Option | How it works |
|---|---|
| A | Bring payments to one row per order in a CTE, keeping a count of payment rows, then LEFT JOIN |
| B | `sum(DISTINCT o.amount)` after the join; 160 of the 400 orders share their amount with another order |
| C | Keep the first posting of each order and instalment, with a tool taught later, then LEFT JOIN |
| D | Ask the platform lead to fix the feed, and send this week's report as the first join gives it |

Work out from the week's table what each fix would put in booked. Which fix should the week's report use?

a) B, since DISTINCT brings booked back to Rs 20,00,000
b) C, since one row per instalment brings booked to Rs 20,00,000
c) A, since one row per order brings booked to Rs 20,00,000
d) D, since the first join overstates booked by only Rs 40,000

### Q4. How much booking does DISTINCT lose? (Design)

In the invented week, 160 of the 400 orders share their amount with at least one other order, across 60 distinct amounts. How many orders' amounts does `sum(DISTINCT o.amount)` leave out of booked?

a) 60, one for each amount that repeats
b) 100, all but one per shared amount
c) 160, every order that shares an amount
d) none, since DISTINCT keeps every order

### Q5. Which fact would make a DISTINCT before the join exact? (Design)

Which fact about the feed would let a DISTINCT, taken on the payments before any join, remove exactly the retries and nothing else?

a) the orders table held exactly one row for every single order id
b) each row carried the gateway's reference, repeated on a retry
c) no two orders in the week were booked at the same amount
d) each retry were posted a day after the payment it repeats

### Q6. Which check proves the fixed join added and lost nothing?

The fixed join is ready for the week's report. Which second check proves that it neither added nor lost anything?

a) the fixed join returns as many rows as the payments table holds
b) the join's collected sits at or below its booked, as it must
c) the fixed query runs cold, top to bottom, with no error
d) each table summed alone equals the join's booked and posted

---

## Where does this skill come back?

It comes back in chapter 3, which asks whether the fixed report still holds every order, and in the
escalated case, where you choose the grain of the payments CTE on Kalpa's own Q2. The notebook for
this chapter is `notebooks/C2_W02_D02_02_why_twice_booked_STUDENT.ipynb`.

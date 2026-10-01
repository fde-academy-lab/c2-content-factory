# Solution: which orders were never paid, and which payments were posted twice?

Answers: 1a 2c 3b 4c 5a 6b

## What does this set test?

The set tests the anti-join, what a condition on the payments table does in WHERE and in ON, and the
grain of a double payment, on tables the chapter never used. Items 4 and 6 are design items: which
list a late payment belongs on under the day's definitions, and which way of writing the list
survives a change to the feed.

## What did the set give you to work from?

> **The client asks.** "If there is a gap, I want to know which orders and which channel."
>
> Anand Iyer, finance controller, Kalpa Retail

**Who needs the answer.** The collections team rings every order on the unpaid list, and the
platform lead and Finance reverse or refund what is on the double-paid list. A name on the wrong
list means a call to a customer who did nothing wrong.

- An **anti-join** keeps the rows of one table that have no partner in the other, for example a LEFT
  JOIN that keeps only the rows where the payment side is NULL.
- **Never paid** means an order with no payment row at all. A **retry** is one order and instalment
  posted more than once.
- `NULL BETWEEN` two dates is unknown, and WHERE keeps only rows that are true.
- The quarter, Q2, runs from 1 July to 30 September.

The invented `orders`:

| order_id | channel | amount |
|---|---|---|
| V-1 | app | 1,000 |
| V-2 | web | 3,000 |
| V-3 | store | 600 |
| V-4 | app | 2,200 |
| V-5 | web | 800 |

The invented `payments`:

| payment_id | order_id | paid_date | amount | instalment_no |
|---|---|---|---|---|
| R-1 | V-1 | 2026-07-04 | 1,000 | 1 |
| R-2 | V-2 | 2026-07-10 | 1,800 | 1 |
| R-3 | V-2 | 2026-08-10 | 1,200 | 2 |
| R-4 | V-3 | 2026-07-15 | 600 | 1 |
| R-5 | V-3 | 2026-07-15 | 600 | 1 |
| R-6 | V-5 | 2026-10-03 | 800 | 1 |
| R-7 | V-9 | 2026-07-20 | 700 | 1 |

## Why does each key hold, item by item?

### Q1. Which orders does the anti-join return?

```sql
SELECT o.order_id
FROM orders o
LEFT JOIN payments p ON p.order_id = o.order_id
WHERE p.order_id IS NULL;
```

Which orders does it return?

The key is a, "V-4". V-4 is the one order with no payment row, so it is the only row whose payment side is NULL.

- b, "V-4 and V-9": V-9 is a payment's order id, and it is not in `orders`.
- c, "V-4 and V-5": V-5 has a payment, R-6.
- d, "V-3 and V-4": V-3 has two.

### Q2. What does the list return once the quarter's dates sit in WHERE?

A teammate adds the quarter to the same query: `WHERE p.paid_date BETWEEN '2026-07-01' AND '2026-09-30' AND p.order_id IS NULL`. Which orders does it return?

The key is c, "no orders". After the LEFT JOIN, V-4's row carries a NULL date, and NULL BETWEEN is unknown, so WHERE throws it away; V-5's date is in October and fails too; every other row has a payment, so IS NULL fails. The list comes back empty.

- a, "V-4": V-4 is dropped by the date test the join put after it.
- b, "V-4 and V-5": both are dropped.
- d, "V-5 only": V-5's row has a date, and it fails BETWEEN.

### Q3. What does it return once the dates move into ON?

The dates move into the join: `LEFT JOIN payments p ON p.order_id = o.order_id AND p.paid_date BETWEEN '2026-07-01' AND '2026-09-30'`, with `WHERE p.order_id IS NULL` kept. Which orders does it return?

The key is b, "V-4 and V-5". In ON the dates decide which payments count as a match, before the join: V-4 has none and V-5's only payment is outside the window, so both keep NULL payment columns and both are listed.

- a, "V-4": forgets V-5, whose payment falls outside the ON condition.
- c, "no orders": that was the WHERE version.
- d, "V-5 and V-9": V-9 is not an order.

### Q4. Where does V-5 belong for Anand's never-paid question? (Design)

V-5 was paid on 3 October, three days after the quarter closed. On the definitions above, which list does V-5 belong on when the collections team asks for the orders never paid?

The key is c, "on no list, since it was paid after Q2 closed". Never paid means no payment row at all, and V-5 has one; it was collected late, which raises a question about days to pay and gives no reason to chase the customer.

- a, "on the double-paid list, since it was paid late": a late payment is a single payment, so it has no second posting to put on that list.
- b, "on the unpaid list, since nothing arrived within Q2": the ON version answers "not paid within Q2", a different question from never paid.
- d, "on the list of payments that match no order": V-5 is in the orders table.

### Q5. What does the double-paid list hold, grouped the right way?

Grouped by order alone, `HAVING count(*) > 1` flags V-2 and V-3. Grouped by order and instalment, what does the double-paid list hold, and how much was posted beyond one payment?

The key is a, "V-3's instalment 1, and 600". By order and instalment only V-3's instalment 1 was posted twice, and sum less max is 1,200 less 600: 600 beyond one payment.

- b, "V-2 and V-3, and 1,800": V-2's two rows are two instalments of real cash.
- c, "V-2's instalment 2, and 1,200": V-2's instalment 2 was posted once.
- d, "V-3's instalment 1, and 1,200": counts both of V-3's postings as surplus.

### Q6. Which way of writing the unpaid list stays correct once the feed sends NULL ids? (Design)

The feed will soon carry refund rows whose `order_id` is NULL. Which way of writing the unpaid list stays correct?

The key is b, "NOT EXISTS or the LEFT JOIN, since a NULL id matches no order". NOT EXISTS and the LEFT JOIN that keeps the misses both treat a NULL id as no match, so the list stays the same.

- a, "NOT IN, since it checks each order id against every id in the list": `x NOT IN (..., NULL)` is never true, so NOT IN returns no rows at all.
- c, "NOT IN and NOT EXISTS alike, since both read one subquery": the two read one subquery and still differ, since NOT IN breaks on the NULL and NOT EXISTS does not.
- d, "none of them, since a NULL id breaks every anti-join": NOT EXISTS and the LEFT JOIN are untouched.

## Which item is worth arguing about?

On item 4, option b, the collections head may well want the orders not paid within the quarter, and
the ON version of item 3 gives exactly that list. It is a different question from Anand's "never
paid", and the day's rule is to write the question beside the list, so each of the two lists carries
its own one-line definition.

## Where does this pattern live in production?

Stripe saves the result of the first request made with an idempotency key, and "subsequent requests
with the same key return the same result" (Stripe API reference, Idempotent requests, checked 1 Oct
2026), so a gateway retry cannot charge a customer twice. In a feed without that guarantee, the data
team has to find the repeats by order and instalment.

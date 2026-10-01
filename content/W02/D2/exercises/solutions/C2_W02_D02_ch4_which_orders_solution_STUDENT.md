# Solution: which orders were never paid, and which payments were posted twice?

Answers: 1a 2c 3b 4d 5a 6b

## What does this set test?

The set tests the anti-join, what a condition on the payments table does in WHERE and in ON, and the
grain of a double payment, on tables the chapter never used. Items 4 and 6 are design items: where a
late payment goes once the never-paid list has to agree with the gap, worked out in rupees for four
treatments, and which of four ways of writing the list survives a change to the feed, each worked
through on the tables.

## What did the set give you to work from?

> **The client asks.** "If there is a gap, I want to know which orders and which channel."
>
> Anand Iyer, finance controller, Kalpa Retail

**Who needs the answer.** The collections team rings every order on the unpaid list, and the
platform lead and Finance reverse or refund what is on the double-paid list. A name on the wrong
list means a call to a customer who did nothing wrong.

- **Booked** is every order at its amount. **Collected** is the cash that arrived, each order and
  instalment counted once. The **gap** is booked less collected.
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
- d, "V-4, V-5 and V-9": V-9 is a payment's order id and not an order, so a LEFT JOIN from orders never lists it, wherever the dates sit.

### Q4. Where does V-5 belong for Anand's never-paid question? (Design)

V-5 was paid by R-6 on 3 October, three days after the quarter closed. Anand's analyst ties the never-paid list's total to the gap, and since every order paid here was paid in full, the two must agree before the page goes out. Which treatment of V-5 and R-6 answers Anand's never-paid question and lets the list and the gap agree?

The key is d, "V-5 off the list, R-6 kept in collected". Never paid means no payment row at all, and V-5 has R-6, so it stays off the list, paid though late; R-6 is cash that arrived against a booked order, so collected counts it. Booked is 7,600 (1,000 + 3,000 + 600 + 2,200 + 800) and collected is 5,400 (V-1's 1,000, V-2's 1,800 and 1,200, V-3's 600 once and V-5's 800), so the gap is 2,200; the list holds V-4 alone at 2,200, and the two agree.

- a, "V-5 on the list, R-6 left out of collected": answers a different question, not paid within Q2. Leaving R-6 out makes collected 4,600 and the gap 3,000, and V-5 on the list makes the list 3,000 as well, so the two agree, and the list sends the collections team to ring V-5's customer, who paid.
- b, "V-5 on the list, R-6 kept in collected": the list reads 2,200 + 800, which is 3,000, against a gap of 2,200, so the two sit 800 apart, and the extra 800 is a customer who paid.
- c, "V-5 off the list, R-6 left out of collected": the gap reads 3,000 against a list of 2,200, so the two sit 800 apart, and 800 of the gap has no order behind it.

### Q5. What does the double-paid list hold, grouped the right way?

Grouped by order alone, `HAVING count(*) > 1` flags V-2 and V-3. Grouped by order and instalment, what does the double-paid list hold, and how much was posted beyond one payment?

The key is a, "V-3's instalment 1, and 600". By order and instalment only V-3's instalment 1 was posted twice, and sum less max is 1,200 less 600: 600 beyond one payment.

- b, "V-2 and V-3, and 1,800": V-2's two rows are two instalments of real cash.
- c, "V-2's instalment 2, and 1,200": V-2's instalment 2 was posted once.
- d, "V-3's instalment 1, and 1,200": counts both of V-3's postings as surplus.

### Q6. Which way of writing the unpaid list stays correct once the feed sends NULL ids? (Design)

The feed will soon carry refund rows whose `order_id` is NULL. A teammate offers four ways to write Anand's never-paid list:

| Way | What keeps an order on the list |
|---|---|
| NOT IN | `o.order_id NOT IN (SELECT order_id FROM payments)` |
| NOT EXISTS | `NOT EXISTS (SELECT 1 FROM payments p WHERE p.order_id = o.order_id)` |
| NOT EXISTS in Q2 | the same, with `AND p.paid_date BETWEEN '2026-07-01' AND '2026-09-30'` inside |
| The LEFT JOIN | `LEFT JOIN payments p ON p.order_id = o.order_id` with `WHERE p.paid_date BETWEEN '2026-07-01' AND '2026-09-30' AND p.order_id IS NULL` |

Which way still returns exactly the orders never paid once those rows arrive?

The key is b, "NOT EXISTS, for a payment row at any date". A NULL `order_id` never equals an order id, so the refund rows match no order, and NOT EXISTS returns V-4 alone, 2,200, before and after they arrive.

- a, "NOT IN, against the order_ids in payments": once the subquery holds a NULL, `x NOT IN (..., NULL)` is never true, so the list comes back empty and V-4 drops off it.
- c, "NOT EXISTS, for a payment row dated in Q2": the date condition asks a different question, not paid within Q2, so V-5, paid on 3 October, joins V-4 and the list reads 3,000 against a gap of 2,200.
- d, "the LEFT JOIN, with Q2's dates kept in WHERE": the dates in WHERE throw away V-4's NULL row, as in item 2, so the list is empty whether or not the refund rows arrive.

## Which item is worth arguing about?

On item 4, option a, the collections head may well want the orders not paid within the quarter, and
leaving R-6 out of collected with V-5 on the list answers that question consistently: list and gap
both read 3,000, the same list the ON version of item 3 returns. It is a different question from
Anand's "never paid", and the day's rule is to write the question beside the list, so each of the
two lists carries its own one-line definition.

## Where does this pattern live in production?

Stripe saves the result of the first request made with an idempotency key, and "subsequent requests
with the same key return the same result" (Stripe API reference, Idempotent requests, checked 1 Oct
2026), so a gateway retry cannot charge a customer twice. In a feed without that guarantee, the data
team has to find the repeats by order and instalment.

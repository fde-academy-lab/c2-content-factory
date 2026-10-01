# Solution: which payment rows should not be in the feed?

Answers: 1c 2b 3d 4a

The executed notebook is `C2_W02_D02_ex2_second_case_solution_STUDENT.ipynb` in this folder. It runs
the four parts with these picks and every check passing; the lists stay yours to read in its empty
cells.

## What does the case test?

The case tests the same joins turned round: a question about every row the feed holds starts from
the payments. Items 3 and 4 are the design choices: how far the retry list must reach for the person
who fixes the feed, and which dates tell the gateway team when the fault ran.

## What did the case give you to work from?

> **The client asks.** "Before I repair the payments feed, tell me which rows in it should not be
> there: payments with no order behind them, and payments the gateway posted twice. Both quarters,
> with the dates, the methods and the rupees at stake, and tell me what to fix first."
>
> The data platform lead, Kalpa Retail

**Who needs the answer.** The platform lead owns the warehouse and the feed that fills it, and
Finance must know whether any customer was charged twice. A fix aimed at the wrong integration
costs weeks and leaves the fault in place; a repeat deleted from the warehouse removes the evidence
Finance needs.

- Anand's question started from the orders, because it was about every booked order. This one starts
  from the payments, because it is about every row the feed holds, which is the fact chapter 1 said
  would change the join.
- A **retry** is the same order and instalment posted more than once; a second instalment has its own
  instalment number and is real cash.
- The warehouse's `payments` table holds 1,428 rows across both quarters, Q1 (April to June) and Q2
  (July to September). Each row carries its order id, date, amount, payment method and instalment
  number.

## Why does each pick hold, item by item?

### Item 1, part 1. Which join accounts for every payment row the feed holds?

The key is c, `payments p LEFT JOIN orders o ON o.order_id = p.order_id`. `payments LEFT JOIN orders` keeps every payment row, so each lands on a Q1 order, a Q2 order or no order, and the three add to the table.

- a, `orders o LEFT JOIN payments p ON p.order_id = o.order_id`: keep only payments that match an order.
- b, `orders o JOIN payments p ON p.order_id = o.order_id`: keep only payments that match an order.
- d, `payments p JOIN orders o ON o.order_id = p.order_id AND o.quarter IN ('Q1', 'Q2')`: keep only payments that match an order.

### Item 2, part 2. Which condition keeps only the payments that match no order?

The key is b, `o.order_id IS NULL`. After that join a payment with no order carries NULL on the order side, so `o.order_id IS NULL` keeps exactly those rows.

- a, `p.order_id IS NULL`: tests the payment's own order id, which the table never leaves empty.
- c, `o.quarter NOT IN ('Q1', 'Q2')`: is unknown for a NULL quarter, so it keeps nothing.
- d, `p.amount > 0 AND o.amount IS NULL AND o.quarter = 'Q2'`: adds a Q2 test no unmatched row can pass.

### Item 3, part 3. Which rows should the retry list cover for the platform lead? (Design)

The key is d, "both quarters, all the feed holds". The platform lead fixes the whole feed, which spans both quarters, so the retry list covers everything the feed holds.

- a, "Q2 orders only, the quarter Anand asked about": split one fault across two reports and leave the lead half of it.
- b, "Q1 orders only, since Q2 is already on Anand's page": split one fault across two reports and leave the lead half of it.
- c, `payments made from 1 July only, whatever order they pay`: cuts by payment date, which is not how the feed files a retry.

### Item 4, part 4. Which dates tell the gateway team when the retries happened? (Design)

The key is a, "the first and last paid_date on the retry list". The first and last `paid_date` on the retry list bound the days the fault ran, and each end is a real retry.

- b, "the first and last day of the quarters the orders belong to": describe the quarters and the feed, so the window starts and ends on days with no retry.
- c, "the first and last paid_date of every payment in the feed": describe the quarters and the feed, so the window starts and ends on days with no retry.
- d, "the paid_date of the first retry, since the rest repeat it": assumes every retry happened on one day, which the list does not show.

## What should your request satisfy?

Every check in the notebook passes: the three homes add to the table's 1,428 rows, the suspense list
holds exactly the rows with no order, the retry list's surplus equals posted less collected across the
matched feed, and the method breakdown adds back to the whole list. Your request names the suspense
payments with their dates and method, and the retries with their count, surplus, method, instalment
and window, and asks that the raw rows be kept until Finance has checked with the bank.

## Which pick is worth arguing about?

Anand asked about Q2, and a pair that has just built his page will reach for Q2 again in item 3,
option a. The platform lead's fix changes the feed for both quarters, and a list that stops at Q2
leaves a repeat in Q1 for someone else to find next quarter.

## Where does this case live in production?

Stripe builds its API so that a request retried with the same idempotency key returns the first
result and cannot charge twice (Stripe API reference, checked 1 Oct 2026); a feed without that
protection is the one a data team audits this way, from the payments side.

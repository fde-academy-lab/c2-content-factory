# Solution: which payment rows should not be in the feed?

Answers: 1c 2b 3d 4a

The executed notebook is `C2_W02_D02_ex2_second_case_solution_STUDENT.ipynb` in this folder. It runs
the four parts with these picks and every check passing; the lists stay yours to read in its empty
cells.

## What does the case test?

The case tests the same joins turned round: a question about every row the feed holds starts from
the payments. Items 3 and 4 are the design choices: how far the retry list must reach for the person who fixes the feed,
and which dates tell the gateway team when the fault ran.

## Why does each pick hold, item by item?

| Item | Part | Key | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | 1 | c | `payments LEFT JOIN orders` keeps every payment row, so each lands on a Q1 order, a Q2 order or no order, and the three add to the table. | a: starts from orders, so a payment with no order never appears and an unpaid order adds a row the feed does not hold. b and d: keep only payments that match an order. |
| 2 | 2 | b | After that join a payment with no order carries NULL on the order side, so `o.order_id IS NULL` keeps exactly those rows. | a: tests the payment's own order id, which the table never leaves empty. c: is unknown for a NULL quarter, so it keeps nothing. d: adds a Q2 test no unmatched row can pass. |
| 3 | 3 | d | The platform lead fixes the whole feed, which spans both quarters, so the retry list covers everything the feed holds. | a and b: split one fault across two reports and leave the lead half of it. c: cuts by payment date, which is not how the feed files a retry. |
| 4 | 4 | a | The first and last `paid_date` on the retry list bound the days the fault ran, and each end is a real retry. | b and c: describe the quarters and the feed, so the window starts and ends on days with no retry. d: assumes every retry happened on one day, which the list does not show. |

## What should your request satisfy?

Every check in the notebook passes: the three homes add to the table's 1,428 rows, the suspense list
holds exactly the rows with no order, the retry list's surplus equals posted less collected across the
matched feed, and the method breakdown adds back to the whole list. Your request names the suspense
payments with their dates and method, and the retries with their count, surplus, method, instalment
and window, and asks that the raw rows be kept until Finance has checked with the bank.

## Which pick is worth arguing about?

Anand asked about Q2, and a pair that has just built his page will reach for Q2 again in item 3,
option a. The platform lead's fix changes the feed for both quarters, and a list that stops at Q2 leaves a
repeat in Q1 for someone else to find next quarter.

## Where does this case live in production?

Stripe builds its API so that a request retried with the same idempotency key returns the first
result and cannot charge twice (Stripe API reference, checked 30 Sep 2026); a feed without that
protection is the one a data team audits this way, from the payments side.

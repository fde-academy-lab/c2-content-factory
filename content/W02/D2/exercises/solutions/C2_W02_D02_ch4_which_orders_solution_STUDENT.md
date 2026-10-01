# Solution: which orders were never paid, and which payments were posted twice?

Answers: 1a 2c 3b 4c 5a 6b

## What does this set test?

The set tests the anti-join, what a condition on the payments table does in WHERE and in ON, and the
grain of a double payment, on tables the chapter never used. Items 4 and 6 are design items: which
list a late payment belongs on under the day's definitions, and which way of writing the list
survives a change to the feed.

## Why does each key hold, item by item?

| Item | Kind | Key | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | predict | a | V-4 is the one order with no payment row, so it is the only row whose payment side is NULL. | b: V-9 is a payment's order id, and it is not in `orders`. c: V-5 has a payment, R-6. d: V-3 has two. |
| 2 | trap | c | After the LEFT JOIN, V-4's row carries a NULL date, and NULL BETWEEN is unknown, so WHERE throws it away; V-5's date is in October and fails too; every other row has a payment, so IS NULL fails. The list comes back empty. | a: V-4 is dropped by the date test the join put after it. b: both are dropped. d: V-5's row has a date, and it fails BETWEEN. |
| 3 | predict | b | In ON the dates decide which payments count as a match, before the join: V-4 has none and V-5's only payment is outside the window, so both keep NULL payment columns and both are listed. | a: forgets V-5, whose payment falls outside the ON condition. c: that was the WHERE version. d: V-9 is not an order. |
| 4 | design | c | Never paid means no payment row at all, and V-5 has one; it was collected late, which raises a question about days to pay and gives no reason to chase the customer. | a: a late payment is a single payment, so it has no second posting to put on that list. b: the ON version answers "not paid within Q2", a different question from never paid. d: V-5 is in the orders table. |
| 5 | predict | a | By order and instalment only V-3's instalment 1 was posted twice, and sum less max is 1,200 less 600: 600 beyond one payment. | b: V-2's two rows are two instalments of real cash. c: V-2's instalment 2 was posted once. d: counts both of V-3's postings as surplus. |
| 6 | design | b | NOT EXISTS and the LEFT JOIN that keeps the misses both treat a NULL id as no match, so the list stays the same. | a: `x NOT IN (..., NULL)` is never true, so NOT IN returns no rows at all. c: the two read one subquery and still differ, since NOT IN breaks on the NULL and NOT EXISTS does not. d: NOT EXISTS and the LEFT JOIN are untouched. |

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

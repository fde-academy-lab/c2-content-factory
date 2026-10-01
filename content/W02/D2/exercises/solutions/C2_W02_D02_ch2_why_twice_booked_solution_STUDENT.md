# Solution: why does the first join report nearly twice the bookings?

Answers: 1c 2a 3c 4b 5b 6d

## What does this set test?

The set tests whether you see that a join multiplies rows before any sum runs, on a week the chapter
never used, and that a fix has to say which repeats it removes. Items 3, 4 and 5 are design items:
the fix chosen on a sizing, a count of the bookings DISTINCT loses, and the fact that would make
DISTINCT exact.

## Why does each key hold, item by item?

| Item | Kind | Key | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | predict | c | 255 single rows, 240 instalment rows and 20 rows for the retried orders make 515 payment rows, and the 15 unpaid orders each add one row with NULLs: 530. | a: a LEFT JOIN keeps each order at least once, and repeats it per matching row. b: forgets the 15 unpaid orders. d: adds the 400 orders to the 515 payment rows, which no join does. |
| 2 | concept | a | An order with two payment rows is written twice, and its booked amount rides along on both, so `sum(o.amount)` runs at the payment's grain. | b: the FILTER keeps only rows with a payment, so unpaid orders add nothing. c: `sum()` skips the NULL rows and never counts them. d: two instalments are two real payments, each stored once. |
| 3 | design | c | A meets the orders at their own grain, keeps booked exact at Rs 20,00,000 and keeps a count of payment rows, so the ten retried orders stay visible for the double-paid list. | a: removes repeated values, and 160 orders share an amount with another, so real bookings vanish. b: C does drop every retry row, but it keeps both instalments of a two-instalment order, so the join still repeats that order and booked stays inflated. d: D is the right request, and it changes nothing about this week. |
| 4 | design | b | DISTINCT keeps each of the 60 shared amounts once, so of the 160 orders that share one, 100 lose their amount from booked. | a: 60 is what it keeps. c: counts every sharing order as lost, when one per amount survives. d: DISTINCT works on values, and a repeated value is not a repeated order. |
| 5 | design | b | A gateway reference repeated on a retry shows that the two rows are one payment, so a DISTINCT on it removes the retry and leaves both instalments of a two-part order. | a: one row per order was already true, and the repeats sit in payments. c: an index changes how fast the query runs and leaves the rows as they are. d: a retry posted a day later differs from the payment it repeats in its date, so a DISTINCT over the row keeps both. |
| 6 | concept | d | Booked recomputed from `orders` alone and posted from `payments` alone never join, so they cannot fan out; if the fixed join added or lost anything, one of them disagrees. | a: 400 orders against 515 payment rows would fail on a correct join. b: assumes every order doubled, which only the 130 multi-row orders did. c: a query can run cleanly and still be wrong. |

## Which item is worth arguing about?

Item 3's option b, a window dedupe, sounds like the precise fix. It keeps the first posting of each
order and instalment, so a retry goes and a second instalment stays, and the join still repeats every
two-instalment order. The fix has to change the grain before the join, and only A does that.

## Where does this pattern live in production?

dbt's MetricFlow documentation defines a fan-out join as one row joined to several rows in another
table, "resulting in more output rows than input rows", and MetricFlow restricts such joins so a
metric cannot be summed at the wrong grain (docs.getdbt.com, Joins, checked 1 Oct 2026).

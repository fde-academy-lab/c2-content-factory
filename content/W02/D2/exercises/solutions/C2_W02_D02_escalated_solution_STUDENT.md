# Solution: which Q2 orders and channels make the gap?

Answers: 1a 2b 3d 4a 5c 6b 7c 8b

The executed notebook is `C2_W02_D02_ex1_escalated_case_solution_STUDENT.ipynb` in this folder. It
runs every part with these picks and every check passing; the lists and figures stay yours to read in
its empty cells, since they are what the case asked you to find.

## What does the case test?

The case tests the day's six chapters joined up, on Kalpa's own Q2 with no invented table first.
Items 2 and 8 are the design choices: the grain the payments must reach before they meet the orders,
and the one check that proves the collected figure holds no payment twice.

## Why does each pick hold, item by item?

| Item | Part | Key | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | 1 | a | The baseline is every Q2 order at its amount, from the orders table alone, which is Monday's booked: 462 orders and Rs 9,84,00,000. | b: keeps only delivered orders, a different definition from Monday's. c: drops every unpaid order and repeats every two-instalment one. d: keeps every order and still repeats the two-instalment ones, so its sum is the fan-out. |
| 2 | 2 | b | Each instalment once, then summed per order: a two-instalment order counts both parts and a retried instalment counts once. | a: counts a retried instalment twice, so collected carries the repeats. c: is no grain at all and fans out. d: drops every second instalment, which is real cash. |
| 3 | 2 | d | The LEFT JOIN with orders first keeps every Q2 order on the page, paid or not. | a: drops the orders nobody paid. b: keeps payments and drops unpaid orders. c: keeps every order and adds payment rows with no order, which are not Q2's business. |
| 4 | 3 | a | After the LEFT JOIN an unpaid order carries NULL on the payment side, so `p.order_id IS NULL` keeps exactly the orders nothing matched. | b: is unknown for a NULL date, so it keeps nothing an unpaid order carries. c: looks for a zero payment, and an unpaid order has no payment row. d: keeps the paid orders. |
| 5 | 4 | c | A retry is one order and instalment posted more than once, so the list groups by order and instalment. | a: flags every order paid in two instalments. b: flags them too, since Kalpa's two instalments are paid on the same day. d: lists genuine second instalments. |
| 6 | 4 | b | What lies beyond one payment of a repeated instalment is its sum less one posting, `sum(p.amount) - max(p.amount)`. | a: is everything posted, including the one payment that belongs there. c: is one payment. d: multiplies the whole sum and doubles the surplus of a pair. |
| 7 | 5 | c | `sum(booked - coalesce(collected, 0))` counts an unpaid order's whole booked amount in the gap. | a and d: let an unpaid order's NULL fall out of the sum, so the gap loses the orders it exists to show. b: subtracts posted, which still holds the repeats. |
| 8 | 5 | b | Collected plus the surplus posted twice must equal posted from the payments table alone; a page that counted a repeat as collected fails it. | a and c: pass a page that dropped unpaid orders, and can pass one with repeats in it. d: says nothing about amounts. |

## What should your page satisfy?

Every check in the notebook passes on your picks: 462 rows in and 462 out, booked of Rs 9,84,00,000
on the baseline and after the join, the unpaid list's total equal to booked less collected, the
double-paid list's surplus equal to posted less collected, and the page's gaps adding to the unpaid
list's total. Your sentence to Anand gives collected with its definition, the gap with the number of
orders behind it and the channel that carries most of it, the repeats and their owner, and the proof.

## Which pick is worth arguing about?

In item 5, option b, grouping by order and date looks like it separates a retry, which lands on one
day, from two instalments, which a learner expects on two days. On Kalpa's Q2 the two instalments of
an order are paid on the same day, so the date adds nothing and the list still flags every
two-instalment order. The instalment number is the only column that says which payment is which.

## Where does this case live in production?

It lives in the month-end collections reconciliation of any business that takes part payments, where
the ledger sits at order grain, the payment feed at posting grain, and a signed page has to tie back
to both.

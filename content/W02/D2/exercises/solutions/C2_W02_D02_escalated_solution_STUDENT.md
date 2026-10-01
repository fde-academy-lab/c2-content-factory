# Solution: which Q2 orders and channels make the gap?

Answers: 1a 2b 3d 4a 5c 6b 7c 8b

The executed notebook is `C2_W02_D02_ex1_escalated_case_solution_STUDENT.ipynb` in this folder. It
runs every part with these picks and every check passing; the lists and figures stay yours to read in
its empty cells, since they are what the case asked you to find.

## What does the case test?

The case tests the day's six chapters joined up, on Kalpa's own Q2 with no invented table first.
Items 2 and 8 are the design choices: the grain the payments must reach before they meet the orders,
and the one check that proves the collected figure holds no payment twice.

## What did the case give you to work from?

> **The client asks.** "Booked revenue is not collected revenue. Some orders are paid in two
> instalments, some are refunded, some were never paid at all. Show me, order by order, what we
> actually collected against what we booked in Q2. If there is a gap, I want to know which orders and
> which channel."
>
> Anand Iyer, finance controller, Kalpa Retail

**Who needs the answer.** Anand signs the page and sends it on to the CEO's Monday numbers, the
collections team rings every order on the unpaid list, and the platform lead receives the repeated
postings. A page that drops an order or keeps a repeat fails each of them.

- **Booked** is every Q2 order at its amount, whatever its status: 462 orders and Rs 9,84,00,000,
  from the orders table alone. **Collected** is the cash that arrived, each payment counted once.
  **Posted** is every payment row the feed holds against an order, repeats included.
- The chapters built each move on invented tables first. Payments are brought to one row per order
  before any join, so a two-instalment order is not counted twice. The LEFT JOIN with orders first
  keeps every booked order. An anti-join finds the orders nothing matched. A retry is the same order
  and instalment posted twice. `coalesce(collected, 0)` keeps an unpaid order in the gap.
- Q2 runs from 1 July to 30 September. The warehouse's tables are `orders` (one row per order) and
  `payments` (one row per payment event, with an instalment number).

## Why does each pick hold, item by item?

### Item 1, part 1. Which rows give the baseline that booked is reconciled to?

The key is a, `orders o WHERE o.quarter = 'Q2'`. The baseline is every Q2 order at its amount, from the orders table alone, which is Monday's booked: 462 orders and Rs 9,84,00,000.

- b, `orders o WHERE o.quarter = 'Q2' AND o.status = 'delivered'`: keeps only delivered orders, a different definition from Monday's.
- c, `orders o JOIN payments p ON p.order_id = o.order_id WHERE o.quarter = 'Q2'`: drops every unpaid order and repeats every two-instalment one.
- d, `orders o LEFT JOIN payments p ON p.order_id = o.order_id WHERE o.quarter = 'Q2'`: keeps every order and still repeats the two-instalment ones, so its sum is the fan-out.

### Item 2, part 2. What grain should the payments CTE have before it meets the orders? (Design)

The key is b, "each instalment once, then summed per order". Each instalment once, then summed per order: a two-instalment order counts both parts and a retried instalment counts once.

- a, "every payment row summed per order, as the feed posted it": counts a retried instalment twice, so collected carries the repeats.
- c, "one row per payment, joined straight to the orders": is no grain at all and fans out.
- d, "only the earliest payment row of each order, summed": drops every second instalment, which is real cash.

### Item 3, part 2. Which join keeps every Q2 order on the page?

The key is d, `LEFT JOIN`. The LEFT JOIN with orders first keeps every Q2 order on the page, paid or not.

- a, `JOIN`: drops the orders nobody paid.
- b, `RIGHT JOIN`: keeps payments and drops unpaid orders.
- c, `FULL JOIN`: keeps every order and adds payment rows with no order, which are not Q2's business.

### Item 4, part 3. Which condition keeps only the Q2 orders nothing matched?

The key is a, `p.order_id IS NULL`. After the LEFT JOIN an unpaid order carries NULL on the payment side, so `p.order_id IS NULL` keeps exactly the orders nothing matched.

- b, `p.paid_date NOT BETWEEN '2026-07-01' AND '2026-09-30'`: is unknown for a NULL date, so it keeps nothing an unpaid order carries.
- c, `p.amount = 0`: looks for a zero payment, and an unpaid order has no payment row.
- d, `o.amount > 0 AND p.amount IS NOT NULL`: keeps the paid orders.

### Item 5, part 4. Which query lists the payments the gateway posted twice?

The key is c, `GROUP BY p.order_id, p.instalment_no HAVING count(*) > 1`. A retry is one order and instalment posted more than once, so the list groups by order and instalment.

- a, `GROUP BY p.order_id HAVING count(*) > 1`: flags every order paid in two instalments.
- b, `GROUP BY p.order_id, p.paid_date HAVING count(*) > 1`: flags them too, since Kalpa's two instalments are paid on the same day.
- d, `WHERE p.instalment_no = 2, one row for each second instalment paid`: lists genuine second instalments.

### Item 6, part 4. How much was posted beyond one payment of each repeated instalment?

The key is b, `sum(p.amount) - max(p.amount)`. What lies beyond one payment of a repeated instalment is its sum less one posting, `sum(p.amount) - max(p.amount)`.

- a, `sum(p.amount)`: is everything posted, including the one payment that belongs there.
- c, `max(p.amount)`: is one payment.
- d, `(count(*) - 1) * sum(p.amount)`: multiplies the whole sum and doubles the surplus of a pair.

### Item 7, part 5. Which expression gives each channel's gap with the unpaid orders in it?

The key is c, `sum(booked - coalesce(collected, 0))`. `sum(booked - coalesce(collected, 0))` counts an unpaid order's whole booked amount in the gap.

- a, `sum(booked - collected)`: let an unpaid order's NULL fall out of the sum, so the gap loses the orders it exists to show.
- b, `sum(booked) - sum(coalesce(posted, 0))`: subtracts posted, which still holds the repeats.
- d, `sum(coalesce(booked, 0) - collected)`: let an unpaid order's NULL fall out of the sum, so the gap loses the orders it exists to show.

### Item 8, part 5. Which check proves that collected holds no payment twice? (Design)

The key is b, "collected plus the surplus posted twice equals posted from payments alone". Collected plus the surplus posted twice must equal posted from the payments table alone; a page that counted a repeat as collected fails it.

- a, "collected is at most booked on every channel": pass a page that dropped unpaid orders, and can pass one with repeats in it.
- c, "the gap is not negative on any channel": pass a page that dropped unpaid orders, and can pass one with repeats in it.
- d, "every channel appears on the page with at least one order and one payment": says nothing about amounts.

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

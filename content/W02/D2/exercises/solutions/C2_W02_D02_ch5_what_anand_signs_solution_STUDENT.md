# Solution: does the gap column on Anand's page tell the truth?

Answers: 1b 2b 3c 4d 5c 6a

## What does this set test?

The set tests how a NULL leaves a sum without a word, the one place `coalesce` has to sit, and a
second route that is independent enough to disagree. Items 5 and 6 are design items: the page form
sized on what a finance controller must act on and audit, and what a disagreement between two routes
means.

## What did the set give you to work from?

> **The client asks.** "If there is a gap, I want to know which orders and which channel."
>
> Anand Iyer, finance controller, Kalpa Retail

**Who needs the answer.** Anand signs the page and sends it to the CEO's Monday numbers, and the
channel heads chase their own unpaid orders from it. A gap column that reads zero stands every one of
them down.

- **Booked** is every order at its amount; **collected** counts each payment once; the **gap** is
  booked less collected. An order nobody paid has NULL in `collected`.
- `sum()` skips NULLs without saying so. `coalesce(x, 0)` returns x, or 0 when x is NULL.
- The bridge's moves are **never paid** (no payment row at all), **paid short** (collected below
  booked) and **posted twice** (the same instalment written more than once).

Six invented orders, one row each, after the payments were brought to one row per order:

| order_id | channel | booked | collected | posted |
|---|---|---|---|---|
| W-1 | app | 2,000 | 2,000 | 2,000 |
| W-2 | app | 700 | NULL | NULL |
| W-3 | store | 1,500 | 1,500 | 3,000 |
| W-4 | store | 2,500 | 2,100 | 2,100 |
| W-5 | web | 1,000 | NULL | NULL |
| W-6 | web | 3,000 | 3,000 | 3,000 |

## Why does each key hold, item by item?

### Q1. What does the hurried gap column say for web?

A teammate adds each order's gap by channel: `sum(booked - collected)`, grouped by channel. What does it report for web?

The key is b, "0". W-5's booked less NULL is NULL and `sum()` skips it, so web adds only W-6's gap of 0.

- a, "1,000": 1,000 is the true gap, which the hurried column loses.
- c, "NULL": `sum()` returns NULL only when every row is NULL.
- d, "4,000": 4,000 is web's booked.

### Q2. Which check catches the gap column without reading any order?

Which check, run on the page by channel, catches that gap column without reading a single order?

The key is b, "the gap against booked less collected, each column summed". Booked less collected, each summed on its own, gives web 4,000 less 3,000, which is 1,000, against a column saying 0; a single column sums correctly because each column is summed alone.

- a, "a gap that is never negative on any channel of the page": a gap of 0 is not negative.
- c, "every channel present on the page, with at least one order": every channel has orders.
- d, "the gap column's total set against last quarter's total": compares two totals that can both be wrong.

### Q3. Which expression keeps the unpaid orders in the gap?

Which expression gives each channel's gap with the unpaid orders in it?

The key is c, `sum(booked - coalesce(collected, 0))`. `coalesce(collected, 0)` says an unpaid order collected nothing, so its gap is its whole booked amount.

- a, `sum(coalesce(booked - collected, 0))`: coalesces after the subtraction, so an unpaid order's gap becomes 0 again.
- b, `coalesce(sum(booked - collected), 0)`: coalesces the total, which the NULL rows have already left.
- d, `sum(booked) - sum(posted)`: subtracts posted, which carries W-3's repeat.

### Q4. What is store's gap, and which bar of the bridge is it?

On the fixed page, what is store's gap, and which move of the bridge does it belong to?

The key is d, "400, paid short". Store booked 4,000 and collected 1,500 plus 2,100: a gap of 400, all of it W-4 paid short.

- a, "minus 1,100, posted twice": booked less posted, 4,000 against 5,100, nets W-3's repeat against W-4's shortfall.
- b, "400, posted twice": puts the right figure on the wrong bar, since W-3's repeat sits above collected.
- c, "2,500, never paid": treats W-4 as never paid, when it paid 2,100.

### Q5. Which page does Anand get? (Design)

Anand has five minutes before he forwards the page, and his analyst audits it next week. Which page does he get?

The key is c, "the table by channel, reconciled above, with both lists". Anand must act by channel and by order and his analyst must audit, so the page carries the table by channel, the reconciliation above it and both lists beneath: the smallest page that does all three.

- a, "one number: the total gap of 2,100": one number says nothing about where to chase.
- b, "a table by channel with its gaps": tells a channel to chase without saying whom.
- d, "the whole statement, one line for each of the six orders": answers everything and asks Anand to find it line by line.

### Q6. What does the difference between two routes to the gap tell you? (Design)

A second route groups the unpaid list by channel: app 700, store 0, web 1,000. The fixed page says app 700, store 400, web 1,000. What does the difference tell you?

The key is a, "store's 400 is paid short, which no unpaid list holds". The unpaid list holds only orders with no payment at all; W-4 was paid, 400 short, so the page's store gap is larger by exactly the paid-short bar. The routes agree wherever nothing was paid short.

- b, "the page double counts W-3's retry inside store's gap": W-3's repeat is in posted and never in collected, so it cannot reach the gap.
- c, "the unpaid list dropped a store order it should have kept": store's unpaid list is empty because no store order went unpaid.
- d, "the coalesce fix added 400 that store never booked": coalesce adds nothing for a paid order.

## Which item is worth arguing about?

Item 3's option a, `sum(coalesce(booked - collected, 0))`, looks careful, since it handles the NULL
explicitly, and it is exactly the hurried column again. Where the `coalesce` sits decides what a NULL
means: around `collected` it means "nothing paid", around the difference it means "no gap". The
business decides which meaning is right, and the query has to put the `coalesce` where it says that.

## Where does this pattern live in production?

Infosys publishes days sales outstanding every quarter, money owed by customers over revenue per day:
63 days for the quarter ended 30 June 2026, against 67 at 31 March 2026 and 70 a year earlier (the
fact sheet furnished with its Form 6-K on 28 July 2026, checked 1 Oct 2026). Once a finance team
publishes its collections figure, it has to answer for every NULL behind that figure.

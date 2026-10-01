# Solution: does the gap column on Anand's page tell the truth?

Answers: 1b 2b 3c 4d 5c 6a

## What does this set test?

The set tests how a NULL leaves a sum without a word, the one place `coalesce` has to sit, and a
second route that is independent enough to disagree. Items 5 and 6 are design items: the page form
sized in lines against what a finance controller, his channel heads and his analyst each need from
it, and a disagreement between two routes taken apart channel by channel, so that the bar the lists
explain is separated from the part that still needs a look.

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
- The **bridge** runs from booked to what the feed posted in named moves, and each move is one
  **bar** of the bridge chart: **never paid** (no payment row at all), **paid short** (collected
  below booked) and **posted twice** (the same instalment written more than once).
- The **unpaid list** names every order never paid. The **paid-short list** names every order
  collected below its booked, with the amount still owed.

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

Anand forwards the page to the CEO's Monday numbers, each channel head chases every rupee of their own gap from it, and his analyst audits it next week. On a full quarter, invented for this item, the page draws on 1,500 orders in three channels, and the bridge's bars hold 24 orders never paid, 6 orders paid short and 15 instalments posted twice. The table by channel takes 3 lines, the reconciliation above it 3 more, and any list or statement a line for each order or instalment it names; the page has to fit one printed sheet of about 60 lines. Which page does he get?

The key is c, "the table, reconciled above, with a list behind each bar". It takes 3 lines of table, 3 of reconciliation and 24 + 6 + 15 listed lines, 51 in all, so it fits the sheet. Every rupee of every channel's gap points to an order on the unpaid or the paid-short list, and the posted-twice list lets the analyst tie the last bar.

- a, "the table by channel, with its gap column and nothing else": fits in 3 lines and names no order, so no channel head knows whom to chase, and nothing on it lets the analyst audit it.
- b, "the table, reconciled above, with the unpaid list": fits in 30 lines (3 + 3 + 24), and the 6 orders paid short are on no list, so the rupees they still owe sit in a channel's gap with no order behind them.
- d, "the table, reconciled above, with every order's line beneath": carries every rupee in 1,506 lines (3 + 3 + 1,500), about 25 sheets where one was asked for, and the 30 orders a channel head chases sit among 1,470 that need nothing from them.

### Q6. What does the difference between two routes to the gap tell you? (Design)

A month later, on a new set of invented orders, the fixed page gives each channel's gap as app 2,300, store 1,200 and web 2,400. The second route, the unpaid list grouped by channel, gives app 1,700, store 1,200 and web 1,500. That month's paid-short list holds one order, an app order that still owes 600. What does the difference between the two routes tell you?

The key is a, "app's 600 is paid short, and web's 900 is unexplained". The routes differ by app 600 (2,300 less 1,700), store 0 and web 900 (2,400 less 1,500). The paid-short list holds the one app order that still owes 600, which no unpaid list ever holds, so app's difference is the paid-short bar exactly. No web order is on the paid-short list, so nothing the lists hold explains web's 900. Either the page counts 900 of web bookings as unpaid that the unpaid list does not, for example an order whose payment the page's payments step dropped by its date while the unpaid list still sees it, or one of the two lists missed an order; the page waits until the 900 is traced.

- b, "both differences are paid short, which no unpaid list holds": the paid-short list holds 600, all of it on app, so web's 900 is not paid short.
- c, "web's 900 is a retry that the page counts inside its gap": the page's collected counts each instalment once, so a retry sits in posted and never reaches the gap, and a retry counted in collected would shrink the gap, never widen it.
- d, "the unpaid list lost 1,500 of app and web orders": app's 600 belongs to an order that was paid in part, so it is rightly off an unpaid list, which leaves at most web's 900 to explain, and the fault may as well sit in the page.

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

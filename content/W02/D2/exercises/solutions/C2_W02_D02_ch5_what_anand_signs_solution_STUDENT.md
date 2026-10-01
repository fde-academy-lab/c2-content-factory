# Solution: does the gap column on Anand's page tell the truth?

Answers: 1b 2b 3c 4d 5c 6a

## What does this set test?

The set tests how a NULL leaves a sum without a word, the one place `coalesce` has to sit, and a
second route that is independent enough to disagree. Items 5 and 6 are design items: the page form sized on what a
finance controller must act on and audit, and what a disagreement between two routes means.

## Why does each key hold, item by item?

| Item | Kind | Key | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | trap | b | W-5's booked less NULL is NULL and `sum()` skips it, so web adds only W-6's gap of 0. | a: 1,000 is the true gap, which the hurried column loses. c: `sum()` returns NULL only when every row is NULL. d: 4,000 is web's booked. |
| 2 | concept | b | Booked less collected, each summed on its own, gives web 4,000 less 3,000, which is 1,000, against a column saying 0; a single column sums correctly because each column is summed alone. | a: a gap of 0 is not negative. c: every channel has orders. d: compares two totals that can both be wrong. |
| 3 | fix | c | `coalesce(collected, 0)` says an unpaid order collected nothing, so its gap is its whole booked amount. | a: coalesces after the subtraction, so an unpaid order's gap becomes 0 again. b: coalesces the total, which the NULL rows have already left. d: subtracts posted, which carries W-3's repeat. |
| 4 | arithmetic | d | Store booked 4,000 and collected 1,500 plus 2,100: a gap of 400, all of it W-4 paid short. | a: booked less posted, 4,000 against 5,100, nets W-3's repeat against W-4's shortfall. b: puts the right figure on the wrong bar, since W-3's repeat sits above collected. c: treats W-4 as never paid, when it paid 2,100. |
| 5 | design | c | Anand must act by channel and by order and his analyst must audit, so the page carries the table by channel, the reconciliation above it and both lists beneath: the smallest page that does all three. | a: one number says nothing about where to chase. b: tells a channel to chase without saying whom. d: answers everything and asks Anand to find it line by line. |
| 6 | design | a | The unpaid list holds only orders with no payment at all; W-4 was paid, 400 short, so the page's store gap is larger by exactly the paid-short bar. The routes agree wherever nothing was paid short. | b: W-3's repeat is in posted and never in collected, so it cannot reach the gap. c: store's unpaid list is empty because no store order went unpaid. d: coalesce adds nothing for a paid order. |

## Which item is worth arguing about?

Item 3's option a, `sum(coalesce(booked - collected, 0))`, looks careful, since it handles the NULL
explicitly, and it is exactly the hurried column again. Where the `coalesce` sits decides what a NULL
means: around `collected` it means "nothing paid", around the difference it means "no gap". The
business decides which meaning is right, and the query has to put the `coalesce` where it says that.

## Where does this pattern live in production?

Infosys publishes days sales outstanding every quarter, money owed by customers over revenue per day:
63 days for the quarter ended 30 June 2026, against 67 at 31 March 2026 and 70 a year earlier (the
fact sheet furnished with its Form 6-K on 28 July 2026, checked 30 Sep 2026). Once a finance team
publishes its collections figure, it has to answer for every NULL behind that figure.

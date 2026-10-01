# Solution: is every booked order still in the report?

Answers: 1b 2a 3c 4b 5a 6c

## What does this set test?

The set tests the count that catches a dropped order, the bridge that separates two causes netted
into one gap, and a second route whose blind spot differs from the first. Items 2, 5 and 6 are
design items: the proof to run first under time pressure, where two independent methods part
company, and the order the proofs run in before the number leaves, which is an ordering item.

## What did the set give you to work from?

> **The client asks.** "If there is a gap, I want to know which orders and which channel."
>
> Anand Iyer, finance controller, Kalpa Retail

**Who needs the answer.** Anand chases the orders that make the gap, and his analyst reads the
reconciliation above the number before the number itself. A report that drops an order and keeps a
repeated payment can show a gap of zero, and nobody chases a zero.

- **Booked** is every order at its amount. **Collected** counts each order and instalment once.
  **Posted** is every payment row the feed holds, repeats included.
- The **gap** is booked less collected. A **bridge** walks from booked to posted in named moves:
  **never paid** (an order with no payment row at all), **paid short** (collected below booked) and
  **posted twice** (posted less collected).
- A plain `JOIN` in SQL is an INNER JOIN.

Six invented orders, with every payment row the feed holds:

| order_id | channel | booked | The payment rows |
|---|---|---|---|
| U-1 | app | 2,000 | one payment of 2,000 |
| U-2 | web | 1,500 | one payment of 1,500, posted twice by the gateway |
| U-3 | store | 900 | none |
| U-4 | app | 3,000 | two instalments, 1,800 and 1,200 |
| U-5 | web | 1,200 | one payment of 700 |
| U-6 | store | 400 | none |

## Why does each key hold, item by item?

### Q1. What does a plain JOIN report on these six orders?

A teammate sums the payments to one row per order and joins them to the orders with a plain `JOIN`. The report shows the orders it holds and booked less posted. What does it show?

The key is b, "4 orders, a gap of minus 1,000". The plain JOIN keeps U-1, U-2, U-4 and U-5: booked 7,700 against posted 8,700, so booked less posted is minus 1,000. U-3 and U-6, never paid, are gone.

- a, "6 orders, a gap of 300": 300 is the six orders' booked less posted, which only a LEFT JOIN keeps.
- c, "4 orders, a gap of 0": forgets U-2's repeat inside posted.
- d, "6 orders, a gap of minus 1,000": keeps six orders, which a plain JOIN cannot.

### Q2. Which check catches a dropped order without reading a rupee? (Design)

Anand's analyst has ten minutes before the report goes out. Which check catches a dropped order without reading any rupee figure?

The key is a, "orders in the report against orders in the table". Orders in the report against the table, 4 against 6, needs no rupee, runs in a moment and fails the moment one order goes missing.

- b, "the report's gap against last quarter's gap, as a ratio": compares two totals that can both be wrong.
- c, "every line of the statement, read and ticked one by one": catches it only if someone reads every line in ten minutes.
- d, "a gap that comes out positive on every single channel": a positive gap says nothing about a missing order.

### Q3. What is collected, each payment counted once?

On the six orders, what is collected?

The key is c, "7,200". 2,000 plus U-2's 1,500 once, plus U-4's 1,800 and 1,200, plus U-5's 700: 7,200.

- a, "8,700": 8,700 is posted, with U-2's repeat inside.
- b, "9,000": 9,000 is booked.
- d, "7,700": 7,700 is the plain JOIN's booked.

### Q4. What is the gap, and what is it made of?

Anand's gap is booked less collected. What is it on the six orders, and what sits inside it?

The key is b, "1,800: 1,300 never paid and 500 paid short". Booked 9,000 less collected 7,200 is 1,800: U-3 and U-6 never paid, 900 and 400, and U-5 paid 500 short.

- a, "300, booked less posted": booked less posted nets the repeat against the gap, which is the one-number trap.
- c, "1,300: the two orders never paid": leaves out U-5's 500.
- d, "3,300: never paid, paid short and posted twice": posted twice sits above collected, outside the gap.

### Q5. Where would two ways of counting collected disagree? (Design)

A second route to collected takes, for each paid order, the smaller of what the feed posted and what was booked. The first route counts each order and instalment once. On which kind of order would the two routes disagree?

The key is a, "a retry the feed wrote under a new instalment number". The instalment route would count a retry written under a new instalment number as a second instalment, while the cap stops at booked, so only there do they part.

- b, "an order paid in two instalments of different amounts": both routes count two genuine instalments in full.
- c, "an order that was never paid at all, such as U-3": both give an unpaid order nothing.
- d, "an order paid once, in full, such as U-1": both give U-1 its 2,000.

### Q6. In what order should the proofs run before the number goes to Anand? (Design)

The report on these six orders has to reach Anand within the hour, and his analyst has three proofs to run before the number itself goes out. Which order catches a dropped order and a repeated payment before anyone reads the number?

The key is c, "the count, then the bridge and its lists, then the number". The count needs no rupee and fails the moment an order goes missing, so it runs first; the bridge then names each rupee between booked and posted with a list behind each move, and only after both does the number go out.

- a, "the number, then the bridge, then the count if it looks odd": reads the number first, so a gap that looks plausible leaves before anything has checked it.
- b, "the bridge, then the number, then the count at the close": runs the bridge on a report that may have dropped an order, and leaves the count to the quarter's close.
- d, "the whole statement first, then the count, then the number": the whole statement is the auditors' appendix at the close, and it asks a reader to tick every line where the count catches the same dropped order in one line.

## Which item is worth arguing about?

On item 1, option c, a pair who spots the dropped orders sometimes expects the gap to vanish to zero.
It comes out negative because U-2's repeated posting sits inside posted, which is the second error in
the same draft. One of the two faults drops rupees and the other adds them.

## Where does this pattern live in production?

Stripe's payout reconciliation report lets a merchant match each payout in the bank with "the batches
of payments and other transactions that they relate to", itemizing every payment, refund, dispute and
fee inside it (Stripe documentation, checked 1 Oct 2026). Public Health England left 15,841 positive
COVID-19 cases out of the daily figures reported between 25 September and 2 October 2020 (GOV.UK,
4 October 2020): the results were pulled into Excel templates in the old XLS format, each result took
several rows of its roughly 65,000, so a template held about 1,400 cases and later cases were left off
(BBC News, 5 October 2020; both checked 1 Oct 2026). No row that arrived was wrong, and a count of rows
sent against rows loaded would have caught the loss.

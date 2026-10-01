# Solution: is every booked order still in the report?

Answers: 1b 2a 3c 4b 5a 6d

## What does this set test?

The set tests the count that catches a dropped order, the bridge that separates two causes netted
into one gap, and a second route whose blind spot differs from the first. Items 2, 5 and 6 are
design items: four checks worked through on one report, where only the count sees an order with no
payment; where two independent methods part company; and the order the proofs run in, worked out
from what each compares and what it costs, which is an ordering item.

## What did the set give you to work from?

> **The client asks.** "If there is a gap, I want to know which orders and which channel."
>
> Anand Iyer, finance controller, Kalpa Retail

**Who needs the answer.** Anand chases the orders that make the gap, and his analyst reads the
reconciliation above the number before the number itself. A report that drops an order and keeps a
repeated payment can show a gap of zero, and nobody chases a zero.

- **Booked** is every order at its amount. **Collected** counts each order and instalment once.
  **Posted** is every payment row the feed holds, repeats included.
- The **gap** is booked less collected. A **bridge** runs from booked to what the feed posted in
  named moves, and each move is one **bar** of the bridge chart: **never paid** (an order with no
  payment row at all), **paid short** (collected below booked) and **posted twice** (posted less
  collected).
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

A teammate sums the payments to one row per order and joins them to the orders with a plain `JOIN`. The report shows the orders it holds and booked less posted, which it labels the gap. What does it show?

The key is b, "4 orders, a gap of minus 1,000". The plain JOIN keeps U-1, U-2, U-4 and U-5: booked 7,700 against posted 8,700, so booked less posted is minus 1,000. U-3 and U-6, never paid, are gone.

- a, "all 6 orders, a gap of 300": 300 is the six orders' booked less posted, 9,000 less 8,700, which only a LEFT JOIN keeps.
- c, "4 orders, a gap of 500": counts U-2's payment once, which gives booked less collected on the four orders, 7,700 less 7,200; the report reads booked less posted, and posted carries U-2's repeat.
- d, "all 6 orders, a gap of minus 1,000": keeps six orders, which a plain JOIN cannot, and on six orders booked less posted is 300.

### Q2. Which of four checks would stop the plain JOIN's report? (Design)

Before the teammate's report from item 1 goes out, Anand's analyst can run four checks on it:

| Check | What it compares |
|---|---|
| The count | orders on the report against orders in the table |
| The fan-out check | rows on the report against the distinct order ids on it |
| The posted tie-back | posted on the report against posted from the payments alone |
| The payment-row count | payment rows summed into the report against payment rows in the feed |

Which of them stop the report?

The key is a, "only the count, as the other three balance". The count reads 4 orders against 6 in the table and stops the report. The fan-out check reads 4 rows against 4 order ids, the posted tie-back 8,700 against 8,700 from the payments alone, and the payment-row count 6 rows against the feed's 6. U-3 and U-6 have no payment, so every check that reads only the report or the payments balances without them, and only a check that starts from the orders table sees them missing.

- b, "only the posted tie-back, as posted runs high": posted on the report is 8,700, the feed's own total, so the tie-back balances; posted runs high only against booked, 8,700 against 7,700, which is U-2's repeated 1,500 less U-5's 500 short, and that comparison is a different check.
- c, "the count and the payment-row count": the report sums U-1's one row, U-2's two, U-4's two and U-5's one, 6 rows, and the feed holds 6, so the payment-row count balances.
- d, "none of them, as every check balances": the count does not balance, 4 orders against 6.

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

Before the number goes to Anand, his analyst runs three proofs on the report and stops at the first one that fails:

| Proof | What it compares | Minutes |
|---|---|---|
| The count | orders on the report against orders in the table | 1 |
| The bridge | the report's booked, walked bar by bar to its posted | 10 |
| The lists | each list of orders, its total against its bar | 15 |

In what order should the three proofs run?

The key is d, "the count first, then the bridge, then the lists". The count costs a minute and stops a report that lost an order at once, while the bridge, built on the report's own figures, still closes on item 1's report (booked 7,700 less 500 paid short is collected 7,200, plus 1,500 posted twice is posted 8,700), so a report that lost two orders passes it. With the count first, that report stops at minute 1. Each list is checked against its bar, and the bars come from the bridge, so the bridge runs before the lists.

- a, "the bridge, then its lists, and the count at the close": on item 1's report the bridge closes after 10 minutes, and the unpaid list, written from the orders table, catches the loss only at minute 25 (1,300 against a never-paid bar of 0), where the count would have stopped it at minute 1.
- b, "the count, then the lists, and the bridge to finish": the count is right to go first, and each list is checked against its bar, which does not exist until the bridge has run, so the lists have nothing to tie to.
- c, "the bridge, then the count, then the lists": the bridge closes on a report missing two orders, so 10 minutes pass before the count stops it at minute 11, where the count first stops it at minute 1.

## Which item is worth arguing about?

On item 1, option c, a pair who spots the dropped orders sometimes counts U-2's payment once and
reads 500, which is booked less collected on the four orders. The report shows booked less posted,
and posted carries U-2's repeated 1,500, which turns the 500 into minus 1,000. One of the draft's two
faults drops rupees and the other adds them.

## Where does this pattern live in production?

Stripe's payout reconciliation report lets a merchant match each payout in the bank with "the batches
of payments and other transactions that they relate to", itemizing every payment, refund, dispute and
fee inside it (Stripe documentation, checked 1 Oct 2026). Public Health England left 15,841 positive
COVID-19 cases out of the daily figures reported between 25 September and 2 October 2020 (GOV.UK,
4 October 2020): the results were pulled into Excel templates in the old XLS format, each result took
several rows of its roughly 65,000, so a template held about 1,400 cases and later cases were left off
(BBC News, 5 October 2020; both checked 1 Oct 2026). No row that arrived was wrong, and a count of rows
sent against rows loaded would have caught the loss.

# Once nothing counts twice, is every booked order still in the report, and can every rupee between booked and posted be named?

The chapter 3 set has six items on six invented orders, so none of its numbers comes from Kalpa's
warehouse. Items 1 and 2 close the chapter live; the rest open the TA-led practice lab or are worked
tonight.

> **The client asks.** "If there is a gap, I want to know which orders and which channel."
>
> Anand Iyer, finance controller, Kalpa Retail

## What do you need to know before the items?

**Who needs the answer.** Anand chases the orders that make the gap, and his analyst reads the
reconciliation above the number before the number itself. A report that drops an order and keeps a
repeated payment can show a surplus, or a gap that looks closed, and nobody chases an order on a page
that reads fully collected.

**The questions on the way.**

- What does a plain JOIN report on these six orders?
- Which of four checks would stop the plain JOIN's report?
- What is collected, each payment counted once?
- What is the gap, and what is it made of?
- Where would two ways of counting collected disagree?
- In what order should the proofs run before the number goes to Anand?

An item marked Design asks for the best-fit approach, a sizing, the fact that would switch it, or the second route.

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

Post one line, six letters in item order, no spaces:

```
Post exactly this shape: xxxxxx
```

---

### Q1. What does a plain JOIN report on these six orders?

A teammate sums the payments to one row per order and joins them to the orders with a plain `JOIN`. The report shows the orders it holds and booked less posted, which it labels the gap. What does it show?

a) all 6 orders, a gap of 300
b) 4 orders, a gap of minus 1,000
c) 4 orders, a gap of 500
d) all 6 orders, a gap of minus 1,000

### Q2. Which of four checks would stop the plain JOIN's report? (Design)

Before the teammate's report from item 1 goes out, Anand's analyst can run four checks on it:

| Check | What it compares |
|---|---|
| The count | orders on the report against orders in the table |
| The fan-out check | rows on the report against the distinct order ids on it |
| The posted tie-back | posted on the report against posted from the payments alone |
| The payment-row count | payment rows summed into the report against payment rows in the feed |

Which of them stop the report?

a) only the count, as the other three balance
b) only the posted tie-back, as posted runs high
c) the count and the payment-row count
d) none of them, as every check balances

### Q3. What is collected, each payment counted once?

On the six orders, what is collected?

a) 8,700
b) 9,000
c) 7,200
d) 7,700

### Q4. What is the gap, and what is it made of?

Anand's gap is booked less collected. What is it on the six orders, and what sits inside it?

a) 300, booked less posted
b) 1,800: 1,300 never paid and 500 paid short
c) 1,300: the two orders never paid
d) 3,300: never paid, paid short and posted twice

### Q5. Where would two ways of counting collected disagree? (Design)

A second route to collected takes, for each paid order, the smaller of what the feed posted and what was booked. The first route counts each order and instalment once. On which kind of order would the two routes disagree?

a) a retry the feed wrote under a new instalment number
b) an order paid in two instalments of different amounts
c) an order that was never paid at all, such as U-3
d) an order paid once, in full, such as U-1

### Q6. In what order should the proofs run before the number goes to Anand? (Design)

Before the number goes to Anand, his analyst runs three proofs on the report and stops at the first one that fails:

| Proof | What it compares | Minutes |
|---|---|---|
| The count | orders on the report against orders in the table | 1 |
| The bridge | the report's booked, walked bar by bar to its posted | 10 |
| The lists | each list of orders, its total against its bar | 15 |

In what order should the three proofs run?

a) the bridge, then its lists, and the count at the close
b) the count, then the lists, and the bridge to finish
c) the bridge, then the count, then the lists
d) the count first, then the bridge, then the lists

---

## Where does this skill come back?

It comes back in chapter 4, which writes the list of orders behind each bar, and in chapter 6, where
the count check becomes one of the checks that run every Monday. The notebook for this chapter is
`notebooks/C2_W02_D02_03_every_order_there_STUDENT.ipynb`.

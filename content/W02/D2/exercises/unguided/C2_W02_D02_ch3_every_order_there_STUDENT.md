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

Post one line, six letters in item order, no spaces:

```
Post exactly this shape: xxxxxx
```

---

### Q1. What does a plain JOIN report on these six orders?

A teammate sums the payments to one row per order and joins them to the orders with a plain `JOIN`. The report shows the orders it holds and booked less posted. What does it show?

a) 6 orders, a gap of 300
b) 4 orders, a gap of minus 1,000
c) 4 orders, a gap of 0
d) 6 orders, a gap of minus 1,000

### Q2. Which check catches a dropped order without reading a rupee?

Anand's analyst has ten minutes before the report goes out. Which check catches a dropped order without reading any rupee figure?

a) orders in the report against orders in the table
b) the report's gap against last quarter's gap, as a ratio
c) every line of the statement, read and ticked one by one
d) a gap that comes out positive on every single channel

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

### Q5. Where would two ways of counting collected disagree?

A second route to collected takes, for each paid order, the smaller of what the feed posted and what was booked. The first route counts each order and instalment once. On which kind of order would the two routes disagree?

a) a retry the feed wrote under a new instalment number
b) an order paid in two instalments of different amounts
c) an order that was never paid at all, such as U-3
d) an order paid once, in full, such as U-1

### Q6. What travels with the report when auditors tick every order?

At the quarter's close, the auditors ask Anand's analyst to tick every order against the books. What travels with the signed report then?

a) the one-number gap, with its definition written above
b) the count reconciliation, in place of the bridge
c) the bridge alone, without the lists behind its moves
d) the whole statement, a line per order, as an appendix

---

## Where does this skill come back?

It comes back in chapter 4, which writes the list of orders behind each bar, and in chapter 6, where
the count check becomes one of the checks that run every Monday. The notebook for this chapter is
`notebooks/C2_W02_D02_03_every_order_there_STUDENT.ipynb`.

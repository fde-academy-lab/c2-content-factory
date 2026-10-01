# Which payment rows in the feed should not be there, and what should the platform lead fix first?

The second case, in pairs, on Kalpa's warehouse. Today the tentative faculty block takes the
afternoon's last 120 minutes, so this case runs in the TA-led practice lab, in about 40 minutes,
after the escalated case. The notebook is
`notebooks/C2_W02_D02_ex2_second_case_STUDENT.ipynb`: four lettered choices in four parts, a check
after each and empty cells where you read what you found.

> **The client asks.** "Before I repair the payments feed, tell me which rows in it should not be
> there: payments with no order behind them, and payments the gateway posted twice. Both quarters,
> with the dates, the methods and the rupees at stake, and tell me what to fix first."
>
> The data platform lead, Kalpa Retail

## What do you need to know before you start?

**Who needs the answer.** The platform lead, who owns the warehouse and the feed that fills it, and
Finance, who must know whether any customer was charged twice. A fix aimed at the wrong integration
costs weeks and leaves the fault in place; a repeat deleted from the warehouse removes the evidence
Finance needs.

- Anand's question started from the orders, because it was about every booked order. This one starts
  from the payments, because it is about every row the feed holds, which is the fact chapter 1 said
  would change the join.
- A **retry** is the same order and instalment posted more than once; a second instalment has its own
  instalment number and is real cash.
- The warehouse's `payments` table holds 1,428 rows across both quarters, Q1 (April to June) and Q2
  (July to September). Each row carries its order id, date, amount, payment method and instalment
  number.

## What are the four parts?

| Part | The question you answer | What you hand in |
|---|---|---|
| 1 | Is every payment row in the feed accounted for? | Where each row belongs, a Q1 order, a Q2 order or no order, adding to the table |
| 2 | Which payments match no order? | The suspense list, with ids, dates, methods and amounts |
| 3 | Which instalments were posted more than once, in either quarter? | The retry list, with its surplus against posted less collected across the feed |
| 4 | Is there a pattern the gateway team can act on? | The window of dates and the payment method the retries share, and the request |

## What are the rules for the case?

- Work in pairs; both partners run the notebook, and one posts.
- Start from the table whose every row must survive, and keep the raw rows: nothing is deleted from
  the warehouse.
- The request to the platform lead names the integration, the instalment and the dates, since a fix
  request that says only "the feed double-posts" does not get scheduled.

## What do you post?

One line of four letters in the order of the notebook's markers, then your request to the platform
lead below it.

```
Post exactly this shape: xxxx
```

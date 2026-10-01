# What goes on the report by channel that Anand signs, and does its gap column tell the truth?

The chapter 5 set has six items on six invented orders, so none of its numbers comes from Kalpa's
warehouse. Items 1 and 2 close the chapter live; the rest open the TA-led practice lab or are worked
tonight.

> **The client asks.** "If there is a gap, I want to know which orders and which channel."
>
> Anand Iyer, finance controller, Kalpa Retail

## What do you need to know before the items?

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

Post one line, six letters in item order, no spaces:

```
Post exactly this shape: xxxxxx
```

---

### Q1. What does the hurried gap column say for web?

A teammate adds each order's gap by channel: `sum(booked - collected)`, grouped by channel. What does it report for web?

a) 1,000
b) 0
c) NULL
d) 4,000

### Q2. Which check catches the gap column without reading any order?

Which check, run on the page by channel, catches that gap column without reading a single order?

a) a gap that is never negative on any channel of the page
b) the gap against booked less collected, each column summed
c) every channel present on the page, with at least one order
d) the gap column's total set against last quarter's total

### Q3. Which expression keeps the unpaid orders in the gap?

Which expression gives each channel's gap with the unpaid orders in it?

a) sum(coalesce(booked - collected, 0))
b) coalesce(sum(booked - collected), 0)
c) sum(booked - coalesce(collected, 0))
d) sum(booked) - sum(posted)

### Q4. What is store's gap, and which bar of the bridge is it?

On the fixed page, what is store's gap, and which move of the bridge does it belong to?

a) minus 1,100, posted twice
b) 400, posted twice
c) 2,500, never paid
d) 400, paid short

### Q5. Which page does Anand get?

Anand has five minutes before he forwards the page, and his analyst audits it next week. Which page does he get?

a) one number: the total gap of 2,100
b) a table by channel with its gaps
c) the table by channel, reconciled above, with both lists
d) the whole statement, one line for each of the six orders

### Q6. What does the difference between two routes to the gap tell you?

A second route groups the unpaid list by channel: app 700, store 0, web 1,000. The fixed page says app 700, store 400, web 1,000. What does the difference tell you?

a) store's 400 is paid short, which no unpaid list holds
b) the page double counts W-3's retry inside store's gap
c) the unpaid list dropped a store order it should have kept
d) the coalesce fix added 400 that store never booked

---

## Where does this skill come back?

It comes back in chapter 6, where "the gap equals booked less collected" and "the gap equals the
unpaid list's total" become two of the checks that run every Monday. The notebook for this chapter is
`notebooks/C2_W02_D02_05_what_anand_signs_STUDENT.ipynb`.

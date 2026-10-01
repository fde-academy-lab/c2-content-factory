# What goes on the report by channel that Anand signs, and does its gap column tell the truth?

The chapter 5 set has six items. Items 1 to 4 run on six invented orders and items 5 and 6 on
invented figures of their own, so none of its numbers comes from Kalpa's warehouse. Items 1 and 2
close the chapter live; the rest open the TA-led practice lab or are worked tonight.

> **The client asks.** "If there is a gap, I want to know which orders and which channel."
>
> Anand Iyer, finance controller, Kalpa Retail

## What do you need to know before the items?

**Who needs the answer.** Anand signs the page and sends it to the CEO's Monday numbers, and the
channel heads chase their own unpaid orders from it. A gap column that reads zero stands every one of
them down.

**The questions on the way.**

- What does the hurried gap column say for web?
- Which check catches the gap column without reading any order?
- Which expression keeps the unpaid orders in the gap?
- What is store's gap, and which bar of the bridge is it?
- Which page does Anand get?
- What does the difference between two routes to the gap tell you?

An item marked Design asks for the best-fit approach, a sizing, the fact that would switch it, or the second route.

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

### Q5. Which page does Anand get? (Design)

Anand forwards the page to the CEO's Monday numbers, each channel head chases every rupee of their own gap from it, and his analyst audits it next week. On a full quarter, invented for this item, the page draws on 1,500 orders in three channels, and the bridge's bars hold 24 orders never paid, 6 orders paid short and 15 instalments posted twice. The table by channel takes 3 lines, the reconciliation above it 3 more, and any list or statement a line for each order or instalment it names; the page has to fit one printed sheet of about 60 lines. Which page does he get?

a) the table by channel, with its gap column and nothing else
b) the table, reconciled above, with the unpaid list
c) the table, reconciled above, with a list behind each bar
d) the table, reconciled above, with every order's line beneath

### Q6. What does the difference between two routes to the gap tell you? (Design)

A month later, on a new set of invented orders, the fixed page gives each channel's gap as app 2,300, store 1,200 and web 2,400. The second route, the unpaid list grouped by channel, gives app 1,700, store 1,200 and web 1,500. That month's paid-short list holds one order, an app order that still owes 600. What does the difference between the two routes tell you?

a) app's 600 is paid short, and web's 900 is unexplained
b) both differences are paid short, which no unpaid list holds
c) web's 900 is a retry that the page counts inside its gap
d) the unpaid list lost 1,500 of app and web orders

---

## Where does this skill come back?

It comes back in chapter 6, where "the gap equals booked less collected" and "the gap equals the
never-paid and paid-short lists" become two of the checks that run every Monday. The notebook for this chapter is
`notebooks/C2_W02_D02_05_what_anand_signs_STUDENT.ipynb`.

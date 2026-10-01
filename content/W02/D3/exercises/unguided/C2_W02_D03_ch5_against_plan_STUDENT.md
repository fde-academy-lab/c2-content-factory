# Has Q2 revenue kept pace with the plan line week by week, and where did it stand at mid-quarter?

Chapter 5's set holds five items. Items 1 and 2 run live in chapter 5's last minutes if the chapter ran to
time; items 3 to 5 are the practice lab's stretch or tonight's work.

> "And Meera wants to see revenue accumulate week by week against the plan line, so we know by
> mid-quarter whether we are on track."
>
> The marketing lead, Kalpa Retail, passing on Meera Raghavan's ask

Meera Raghavan is Kalpa Retail's CEO. The plan line is a small table, `plan_line`, with one row per
plan week: 13 weeks, each starting on a Monday from 6 July to 28 September 2026, Rs 75,69,230 a week
and Rs 9,83,99,990 in all. Q2's orders run from Wednesday 1 July to 28 September: 462 orders booked at
Rs 9,84,00,000, every order at its amount whatever its status, which is Monday's total for the quarter.
To date means every week up to and including the one on the row, so booked to date and plan to date
both accumulate. A running total is a window: `sum(booked) OVER (ORDER BY week_start)` keeps every
week's row and carries the sum of every row up to and including it. Rows that share the window's ORDER
BY value are peers, and by default a running total gives peers the same figure. Mid-quarter is the end of the
seventh plan week, the week of 17 August, which ends on 23 August. Chapter 5's running total, with the
plan's first week carrying Q2's first five days, closes on Rs 9,84,00,000 against Rs 9,83,99,990.

| Plan week starting | Booked in the week | Booked to date |
|---|---|---|
| 6 Jul | Rs 51,00,180 | Rs 51,00,180 |
| 13 Jul | Rs 2,66,28,920 | Rs 3,17,29,100 |
| 20 Jul | Rs 1,05,15,380 | Rs 4,22,44,480 |
| 27 Jul | Rs 65,36,570 | Rs 4,87,81,050 |
| 3 Aug | Rs 1,07,34,760 | Rs 5,95,15,810 |
| 10 Aug | Rs 37,68,970 | Rs 6,32,84,780 |
| 17 Aug | Rs 54,51,810 | Rs 6,87,36,590 |
| 24 Aug | Rs 32,22,980 | Rs 7,19,59,570 |
| 31 Aug | Rs 34,37,170 | Rs 7,53,96,740 |
| 7 Sep | Rs 65,33,270 | Rs 8,19,30,010 |
| 14 Sep | Rs 93,01,650 | Rs 9,12,31,660 |
| 21 Sep | Rs 66,78,320 | Rs 9,79,09,980 |
| 28 Sep | Rs 4,90,020 | Rs 9,84,00,000 |

The plan is Rs 75,69,230 in every one of the thirteen weeks.

**Who needs the answer.** Meera needs it to decide at mid-quarter whether to hold the plan, push a
campaign or move budget. A quarter reported behind when it is on plan sends Marketing after a gap that is not
there, with discounts that cost margin, and a quarter read as comfortably ahead hides weeks that ran
below plan.

**The questions on the way.**

- Which way should give Meera booked to date at the end of every day, sized in order rows read?
- What happened to the running total that closes on Rs 4,90,020, and which check catches it?
- Where did Q2 stand against plan to date at the end of the week of 31 August?
- Which ORDER BY names the order that took Q2 past Rs 3.5 crore, and what does it promise?
- Which route confirms the thirteen to-date figures without the window, and what does it read?

**What you post.** Your five letters in item order, with no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

## How should the team accumulate a quarter?

This comes up at work whenever a stakeholder wants a figure to date at every point of a period.

### Q1. Which way should give Meera booked to date at the end of every day, sized in order rows read?

Meera now wants booked to date at the end of every day of Q2, from 1 July to 30 September, as well as
at each plan week's end. Which way fits, sized in the order rows it reads?

a) A running SUM over a calendar of Q2's days, joined to daily totals: 462 orders read, then 92 rows

b) A plain SUM up to each day's end: the 462 orders read once for every day, 42,504 order reads

c) A self-join of each day to every day up to it: the 462 orders read once, then 4,278 pairs of days

d) A running SUM over the daily totals, one row per date with an order: 462 orders read, then 84 rows

## Does a running total say what it seems to say?

This comes up at work whenever a to-date figure goes to someone who decides on it.

### Q2. What happened to the running total that closes on Rs 4,90,020, and which check catches it?

An analyst, fresh from the morning, adds a partition to the booked side of the running total:
`sum(booked) OVER (PARTITION BY week_start ORDER BY week_start)`. The plan side is built without it.
The table's last row reads booked to date Rs 4,90,020 against plan to date Rs 9,83,99,990. What
happened, and which check catches it?

a) Q2 fell Rs 9,79,09,970 short of plan because its last week booked so little; the plan to date confirms it

b) The last week holds only 28 September, so the close is partial; reading the week of 21 September fixes it

c) Each week is now its own window, so a row shows one week; booked to date should never drop, yet it does

d) The plan side ran on and the booked side did not, so dropping the plan's running sum makes them match

### Q3. Where did Q2 stand against plan to date at the end of the week of 31 August?

Meera reads the end of the week of 31 August, the ninth plan week. Using the table at the top of this
set, where did Q2 stand against plan?

a) About ten times plan: Rs 7,53,96,740 booked to date against a week's plan of Rs 75,69,230

b) Rs 72,73,670 ahead: Rs 7,53,96,740 booked to date against Rs 6,81,23,070 planned to date

c) Rs 41,32,060 behind: the week booked Rs 34,37,170 against its own plan of Rs 75,69,230

d) Rs 1,48,42,900 ahead: Rs 7,53,96,740 booked to date against Rs 6,05,53,840 planned to date

## Can a running total name the order that took Q2 past a round figure?

This comes up at work whenever someone asks which sale, or which day, took a total past a round figure.

### Q4. Which ORDER BY names the order that took Q2 past Rs 3.5 crore, and what does it promise?

Meera asks which order took Q2 past Rs 3.5 crore. A running total of Q2's orders ordered by
`order_date` alone shows Rs 3,76,90,290 on all twelve orders of 22 July, the busiest day of Q2, whose
order ids run KR-00557, KR-00580, KR-00601, KR-00604, KR-00607, KR-00713, KR-00761, KR-00782,
KR-00832, KR-00853, KR-00919 and KR-00979. Which ORDER BY names the order, and what does it promise?

a) `order_date, amount DESC`: each order its own step, in the order that the day's sales happened

b) `order_id` alone: each order its own step, since the order ids were all issued in date order

c) `order_date` with `PARTITION BY order_date`: each day restarts, so each order shows its own step

d) `order_date, order_id`: each order its own step, and the id is the stated tiebreak inside a day

## How do you prove a running total without the window?

This comes up at work whenever a to-date figure has to be shown right by a route that could have caught it
wrong.

### Q5. Which route confirms the thirteen to-date figures without the window, and what does it read?

Kavya Nair, the senior analyst who checks every number before it leaves the team, wants the thirteen
to-date figures confirmed by a route that shares neither the window nor the way orders were put into
weeks. Which route does that, and what does it read?

a) The weekly booked column added up in a spreadsheet and set beside the last row: 13 cells

b) Thirteen plain sums of the Q2 orders dated up to each week's last day: 6,006 order reads

c) A running total redone with `ORDER BY week_start DESC`, read from the bottom up: 13 rows

d) The last plan to date set beside the plan line's own total of Rs 9,83,99,990: one row

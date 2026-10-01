# Which answers hold in the chapter 5 set on whether Q2 kept pace with the plan line, and why?

Answers: 1a 2c 3b 4d 5b

Chapter 5 accumulated Q2 against the plan line. The plan-first build closed at Rs 9,68,60,180 and
reported Q2 Rs 15,39,810 short of plan; set beside Monday's Rs 9,84,00,000 it was Rs 15,39,820 short of
the quarter itself, because the 25 orders of 1 to 5 July fell in the week of 29 June, which the plan
does not have. With the plan's first week carrying those days, Q2 closed on Rs 9,84,00,000 against
Rs 9,83,99,990, Rs 10 ahead. At mid-quarter it stood Rs 1,57,51,980 ahead, a lead built in the week of
13 July, and from the week of 10 August six of the seven full weeks booked below the weekly plan.
Thirteen plain sums to each week's last day matched the running total in every week. Two of the five
items are design items: 1 and 5.

**Who needs the answer.** You, checking your five letters after the lab or tonight. Meera reads one
line at mid-quarter and acts on it, so a to-date figure set beside the wrong plan figure, or a running
total that dropped a week, decides a campaign on a gap that is not there.

**The questions on the way.**

- Which idea does this set test?
- Why is each key right, item by item?
- Which wrong answer is worth arguing about?
- Where does this show up at work?

## Which idea does this set test?

A running total is finished when its last value equals the total you can count without it, and to
date goes beside to date. The design items size a running total against plain sums at a finer grain
and choose a second route that shares neither the window nor the weekly buckets. The other items catch
a partition that stops the total from running, read the lead at a week the chapter did not read, and
choose the order that makes a running total name one row.

## Why is each key right, item by item?

### Q1. Which way should give Meera booked to date at the end of every day, sized in order rows read?

Kind: a design item, the best-fit way with its size.

The key is a, "A running SUM over daily totals: the 462 Q2 orders read once, then 92 daily rows". The
orders are added up per day once, and the window carries the sum down the 92 days, so every day has
its to-date figure from one pass.

- b, "A plain SUM up to each day's end: the 462 orders read once for every day, 42,504 order reads":
  the right figures at 92 times the reading, 92 times 462.
- c, "A self-join of each day to every earlier day: 4,278 day pairs, fewer rows than any window
  reads": 92 days make 92 times 93 over 2, 4,278 pairs, about nine times the window's 462 order
  rows, and the pairs still need the daily totals first.
- d, "The 462 orders exported with a cumulative column copied down a sheet: 462 rows and no query to
  keep": breaks the data platform lead's rule, "query it, do not export it", and nobody can rerun a
  copied-down column next week.

### Q2. What happened to the running total that closes on Rs 4,90,020, and which check catches it?

Kind: spot the plausible wrong output.

The key is c, "Each week is now its own window, so each row shows one week; set the last row beside
Rs 9,84,00,000". `PARTITION BY week_start` starts the sum again in every week, and each week
holds one row, so every "to date" figure is that week's own booking: the last row is the week of 28
September, Rs 4,90,020. Set beside Monday's Rs 9,84,00,000 it is short by almost the whole quarter,
which is the check. The fix drops the partition, since the quarter is one running window.

- a, "Q2 fell Rs 9,79,09,970 short of plan because its last week booked so little; the plan to date
  confirms it": the subtraction is right and the figure is not a to-date figure, so the shortfall it
  reports does not exist.
- b, "The last week holds only 28 September, so the close is partial; reading the week of 21
  September fixes it": the week of 21 September would read its own Rs 66,78,320, just as wrong.
- d, "The plan side ran on and the booked side did not, so dropping the plan's running sum makes the
  two match": it makes the two sides agree by breaking the side that was right.

### Q3. Where did Q2 stand against plan to date at the end of the week of 31 August?

Kind: predict the number from the exhibit.

The key is b, "Rs 72,73,670 ahead: Rs 7,53,96,740 booked to date against Rs 6,81,23,070 planned to
date". Nine plan weeks of Rs 75,69,230 are Rs 6,81,23,070, and booked to date at the end of the ninth is
Rs 7,53,96,740, Rs 72,73,670 ahead. The lead has fallen from Rs 1,57,51,980 at mid-quarter, because
the weeks of 24 and 31 August booked Rs 32,22,980 and Rs 34,37,170 against Rs 75,69,230 each.

- a, "About ten times plan: Rs 7,53,96,740 booked to date against the ninth week's plan of
  Rs 75,69,230": nine weeks of bookings set beside one week of plan.
- c, "Rs 41,32,060 behind: the week booked Rs 34,37,170 against its own Rs 75,69,230": the right
  reading of the run rate for that week, which is a different question from where Q2 stands to date.
- d, "Rs 6,78,27,510 ahead: Rs 7,53,96,740 less the week's plan of Rs 75,69,230": subtracts one week's
  plan from nine weeks of bookings.

### Q4. Which ORDER BY names the order that took Q2 past Rs 3.5 crore, and what does it promise?

Kind: fix the logic.

The key is d, "`order_date, order_id`: each order its own step, the same on every run, in id order
within the day". With the order id added, no two rows are peers, so the twelve orders of 22 July step
from Rs 3,45,16,000 to Rs 3,76,90,290, and KR-00580's Rs 8,55,000 takes the total from Rs 3,45,16,000 to
Rs 3,53,71,000, past Rs 3.5 crore. The id makes the answer repeatable on every run and every machine;
the warehouse records a date and no time, so it is not the true order of the day's sales, and the line
to Meera says which tiebreak it used.

- a, "`order_date, amount DESC`: each order its own step, in the order the day's sales happened": an
  amount is not a time, and two orders of the same amount would be peers again.
- b, "`order_id` alone: each order its own step, since the order ids were issued in date order": the
  twelve ids of 22 July run from KR-00557 to KR-00979 with other days' orders between them.
- c, "`order_date` with `PARTITION BY order_date`: each day restarts its total, so each order shows
  its own step": a partition by day restarts the total every day and leaves the twelve orders peers.

### Q5. Which route confirms the thirteen to-date figures without the window, and what does it read?

Kind: a design item, the independent second route with its size.

The key is b, "Thirteen plain sums of the Q2 orders dated up to each week's last day: 6,006 order
reads". Each sum reads the 462 orders and keeps those dated on or before `week_start + 6`, so it
uses neither the window nor the way orders were put into weeks; in the chapter it matched the running
total in all thirteen weeks, including the first, whose last day, 12 July, already takes in 1 to 5
July.

- a, "The weekly booked column added up in a spreadsheet and set beside the last row: 13 cells": the
  weekly column comes from the same bucketing, so a week the bucketing dropped is missing from both.
- c, "The same window rerun with `ORDER BY week_start DESC` and read from the bottom up: 13 rows": the
  same window and the same weeks, read the other way.
- d, "The last plan to date set beside the plan line's own total, Rs 9,83,99,990: one row": checks the
  plan side, which was never in doubt.

## Which wrong answer is worth arguing about?

Item 3, option c. The week of 31 August did book Rs 41,32,060 less than its plan, and Meera should hear
that, since from the week of 10 August six of the seven full weeks ran below plan. It answers how the
week ran, and the question was where the quarter stood. The two readings belong in the same line,
each with its own comparison: to date beside to date, and each week beside its own plan.

## Where does this show up at work?

Target's second quarter of 2022 began on 1 May 2022. On 7 June 2022, about five weeks in, Target said
it "now expects its second-quarter operating margin rate will be in a range around 2%", down from a
range centred on the first quarter's 5.3 percent, after markdowns to clear excess inventory (Target's
releases of 7 June and 18 May 2022, checked 1 October 2026). The quarter closed at 1.2 percent
(Target's release of 17 August 2022, checked 1 October 2026). Reading the quarter while it ran is what
let Target act before it ended.

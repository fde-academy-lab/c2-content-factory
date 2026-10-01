# Which answers hold in the chapter 5 set on whether Q2 kept pace with the plan line, and why?

Answers: 1a 2c 3b 4d 5b

Chapter 5 accumulated Q2 against the plan line. The plan-first build closed at Rs 9,68,60,180 and
reported Q2 Rs 15,39,810 short of plan; set beside Monday's Rs 9,84,00,000 it was Rs 15,39,820 short of
the quarter itself, because the 25 orders of 1 to 5 July fell in the week of 29 June, which the plan
does not have. With the plan's first week carrying those days, Q2 closed on Rs 9,84,00,000 against
Rs 9,83,99,990, Rs 10 ahead. At mid-quarter it stood Rs 1,57,51,980 ahead, a lead built in the week of
13 July, and from the week of 10 August six of the seven full weeks booked below the weekly plan, the
week of 14 September being the one above it. Thirteen plain sums to each week's last day matched the
running total in every week. Two of the five items are design items: 1 and 5.

**Who needs the answer.** You need it to check your five letters after the lab or tonight. Meera reads the
mid-quarter figure and acts on it, so a to-date figure set beside the wrong plan figure, or a running
total that dropped a week, decides a campaign on a gap that is not there.

**The questions on the way.**

- What does the against-plan set test about running totals and figures to date?
- Why is each against-plan key right, and each other letter wrong?
- Why is item 3's weekly shortfall worth arguing about?
- Where did a real company read its quarter while the quarter was still running?

## What does the against-plan set test about running totals and figures to date?

A running total is worth reading only when every day of the period has its row and the figure beside it
was accumulated the same way, so booked to date is read against plan to date. The design items size a
running total against plain sums and a self-join at the grain of a day, and choose a second route that
shares neither the window nor the weekly buckets. The other items catch a partition that stops the total
from running, read the lead at a week the chapter did not read, and choose the ORDER BY that lets a
running total name one order.

## Why is each against-plan key right, and each other letter wrong?

### Q1. Which way should give Meera booked to date at the end of every day, sized in order rows read?

This is a design item: it asks for the best-fit build at the grain of a day, with its size.

The key is a, "A running SUM over a calendar of Q2's days, joined to daily totals: 462 orders read,
then 92 rows". Q2 has 92 days, 31 in July, 31 in August and 30 in September, and only 84 of them carry
an order. The daily totals read the 462 orders once; joined to a calendar of the 92 days, every day has
a row, a day with no order adds nothing, and the window carries the sum down the 92 rows in one pass.

- Option b, "A plain SUM up to each day's end: the 462 orders read once for every day, 42,504 order
  reads", gives the right figures at 92 times the reading, 92 times 462.
- Option c, "A self-join of each day to every day up to it: the 462 orders read once, then 4,278 pairs
  of days", also gives the right figures, but after the same 462 order reads it works through 92 times
  93 over 2, 4,278 pairs of days, where the window walks 92 rows.
- Option d, "A running SUM over the daily totals, one row per date with an order: 462 orders read, then
  84 rows", skips the 8 days with no order, 29 to 31 July, 29 to 31 August and 29 and 30 September, so
  Meera gets no figure for the last day of any month, the quarter's own last day among them.

### Q2. What happened to the running total that closes on Rs 4,90,020, and which check catches it?

This item asks you to spot the plausible wrong output and the check that catches it.

The key is c, "Each week is now its own window, so a row shows one week; booked to date should never
drop, yet it does". `PARTITION BY week_start` starts the sum again in every week, and each week holds
one row, so every "to date" figure is that week's own booking, and the last row is the week of 28
September, Rs 4,90,020. Every Q2 order is booked at a positive amount, so a true booked to date can only
stay level or climb, and this column drops from Rs 2,66,28,920 in the week of 13 July to Rs 1,05,15,380
in the week of 20 July. The fix drops the partition, since the quarter is one running window, and the
last row then reads Rs 9,84,00,000.

- Option a, "Q2 fell Rs 9,79,09,970 short of plan because its last week booked so little; the plan to
  date confirms it", subtracts correctly, Rs 9,83,99,990 less Rs 4,90,020, but the booked figure is one
  week's booking, so the shortfall it reports does not exist.
- Option b, "The last week holds only 28 September, so the close is partial; reading the week of 21
  September fixes it", would read the week of 21 September's own Rs 66,78,320, just as wrong, since
  every row of the broken column is one week's booking.
- Option d, "The plan side ran on and the booked side did not, so dropping the plan's running sum makes
  them match", makes the two sides agree by breaking the side that was right, so both would then read
  one week at a time.

### Q3. Where did Q2 stand against plan to date at the end of the week of 31 August?

This item asks you to read the exhibit at a week the chapter did not read.

The key is b, "Rs 72,73,670 ahead: Rs 7,53,96,740 booked to date against Rs 6,81,23,070 planned to
date". Nine plan weeks of Rs 75,69,230 are Rs 6,81,23,070, and booked to date at the end of the ninth
is Rs 7,53,96,740, Rs 72,73,670 ahead. The lead has fallen from Rs 1,57,51,980 at mid-quarter, because
the weeks of 24 and 31 August booked Rs 32,22,980 and Rs 34,37,170 against Rs 75,69,230 each.

- Option a, "About ten times plan: Rs 7,53,96,740 booked to date against a week's plan of
  Rs 75,69,230", sets nine weeks of bookings beside one week of plan.
- Option c, "Rs 41,32,060 behind: the week booked Rs 34,37,170 against its own plan of Rs 75,69,230",
  reads the run rate of that one week correctly, which answers a different question from where Q2 stands
  to date.
- Option d, "Rs 1,48,42,900 ahead: Rs 7,53,96,740 booked to date against Rs 6,05,53,840 planned to
  date", sets to date beside to date and counts one plan week short: Rs 6,05,53,840 is eight weeks of
  plan, the count that subtracting 6 July from 31 August gives, and by the end of the week of 31 August
  a ninth plan week has run.

### Q4. Which ORDER BY names the order that took Q2 past Rs 3.5 crore, and what does it promise?

This item asks you to fix the logic: the ORDER BY that names one order, and what it promises.

The key is d, "`order_date, order_id`: each order its own step, and the id is the stated tiebreak inside
a day". By date alone, a running total in its default frame adds all of a row's peers at once, so each
of the twelve orders of 22 July shows the day's close, Rs 3,76,90,290, and shows it on every run: the
figure repeats but cannot say which order crossed Rs 3.5 crore. With the order id added, no two rows are
peers, so the twelve step from Rs 3,45,16,000 to Rs 3,76,90,290, and KR-00580's Rs 8,55,000 takes the
total from Rs 3,45,16,000 to Rs 3,53,71,000, past Rs 3.5 crore. A ROWS frame over the date alone would
also give each order a step, but in whatever order the database meets the twelve, which can change from
one run to the next, and the id settles that too. The warehouse records a date and no time, so the id
order is a tiebreak, and the message to Meera names it.

- Option a, "`order_date, amount DESC`: each order its own step, in the order that the day's sales
  happened", treats an amount as a time: it puts KR-00604's Rs 10,42,000 first and names that order as
  the one that crossed, and two orders of the same amount would be peers again.
- Option b, "`order_id` alone: each order its own step, since the order ids were all issued in date
  order", rests on a claim the data refutes, since 411 orders dated on other days carry ids between
  KR-00557 and KR-00979, so a total ordered by id alone mixes days.
- Option c, "`order_date` with `PARTITION BY order_date`: each day restarts, so each order shows its own
  step", restarts the total every day and still leaves the twelve orders peers, so each shows the day's
  own total, Rs 31,75,220.

### Q5. Which route confirms the thirteen to-date figures without the window, and what does it read?

This is a design item: it asks for the independent second route and what it reads.

The key is b, "Thirteen plain sums of the Q2 orders dated up to each week's last day: 6,006 order
reads". Each sum reads the 462 orders and keeps those dated on or before `week_start + 6`, so it uses
neither the window nor the way orders were put into weeks, and 13 sums of 462 reads come to 6,006. In
the chapter it matched the running total in all thirteen weeks, including the first, whose last day,
12 July, already takes in 1 to 5 July.

- Option a, "The weekly booked column added up in a spreadsheet and set beside the last row: 13 cells",
  adds up a column that came from the same bucketing, so a week the bucketing dropped is missing from
  both.
- Option c, "A running total redone with `ORDER BY week_start DESC`, read from the bottom up: 13 rows",
  is still a window over the same weekly buckets, read the other way, so it shares both things the
  route had to avoid.
- Option d, "The last plan to date set beside the plan line's own total of Rs 9,83,99,990: one row",
  checks the plan side, which no item put in doubt, and says nothing about the bookings.

## Why is item 3's weekly shortfall worth arguing about?

Item 3's option c, the week of 31 August set beside its own plan, is a true figure: that week did book
Rs 41,32,060 less than its plan, and Meera should hear it, since from the week of 10 August six of the
seven full weeks ran below plan and only the week of 14 September booked above it. It answers how the
week ran, and the question was where the quarter stood. Both readings belong in the message to Meera,
each with its own comparison: booked to date beside plan to date for the quarter, and each week beside
its own plan for the run rate.

## Where did a real company read its quarter while the quarter was still running?

Target's second quarter of 2022 began on 1 May 2022. On 7 June 2022, about five weeks in, Target said
it "now expects its second-quarter operating margin rate will be in a range around 2%", down from a
range centred on the first quarter's 5.3 percent, after markdowns to clear excess inventory (Target's
releases of 7 June and 18 May 2022, checked 1 October 2026). The quarter closed at 1.2 percent
(Target's release of 17 August 2022, checked 1 October 2026).

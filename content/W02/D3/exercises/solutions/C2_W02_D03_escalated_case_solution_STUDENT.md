# Which answers hold in the escalated case on what Marketing gets on Monday, and why?

Answers: 1c 2b 3b 4a 5a 6c 7b 8b 9c 10b 11d 12a 13d 14c 15d

The marketing lead starts calling on Monday and wants each segment's protect list under the head of
Retail-Plus's rule with its count, the members to ring first, the share of each segment's Q2 revenue
the lists carry, and one line for Meera on whether Q2 is on track. The case asks each learner to build
all of it alone in five parts: items 1 to 10 are the ten markers of
`notebooks/C2_W02_D03_ex1_escalated_case_STUDENT.ipynb`, and items 11 to 15 are the brief's design
items, one per part. The executed solution, `C2_W02_D03_ex1_escalated_case_solution_STUDENT.ipynb` in
this folder, runs every marker; where a part's answer for Retail-Plus is the count your own run gave,
it checks that count without printing it, and so does this page. Five of the fifteen items are design
items: 11 to 15.

**Who needs the answer.** You need it before the debrief, to check your fifteen letters and your two numbers.
The debrief replays the room's wrong answers aloud, and a line you cannot defend here is the one the
marketing lead or Meera sends back.

**The questions on the way.**

- Which idea does this case test?
- Which numbers should you have reached, part by part?
- Why is each key right, item by item?
- Which wrong answers does the debrief replay?
- Where does this show up at work?

## Which idea does this case test?

The case runs the whole day on one deliverable, with nothing to copy. A list states its rule and its
count, and the rule lets members who spent the same share a place. A flag reads a member's own months,
in calendar months, so a month with no order breaks the run. A share names the whole it was cut from.
A running total closes on the quarter's own total before it says ahead or behind, and the run rate
reads each week against its own plan. The design items put each part under a constraint the chapters
did not meet: a cap on calls, a second flag, a wider list, a reading on one date, and the check
before the line leaves.

## Which numbers should you have reached, part by part?

| Part | Number | What it means |
|---|---|---|
| 1 | Business 35 and Student 20, every Q2 buyer in both; Retail-Core 50, with nobody tied at its line (the fiftieth booked Rs 2,980 and the 51st Rs 2,950); Retail-Plus, the count your own run gave | Under the head's rule a list holds fifty, or every buyer where a segment has fewer, and runs past fifty only when members tie at its line, which the line to Marketing then names. |
| 2 | 9 members flagged on three calendar months, each lower, all 9 on a protect list; C-0216 not among them | Without the calendar condition the flag holds 16, and 7 of those step over a month with no order. |
| 3 | Business 100.0 percent, Retail-Core 76.1 percent (Rs 2,78,740 of Rs 3,66,250), Student 100.0 percent; Retail-Plus, the share your own run gave | Half of Retail-Core's buyers carry three quarters of its rupees. |
| 4 | Close Rs 9,84,00,000 against Rs 9,83,99,990, Rs 10 ahead; mid-quarter Rs 6,87,36,590 against Rs 5,29,84,610, Rs 1,57,51,980 ahead; 6 of the 7 full weeks from 10 August below plan | On track by the total, below plan by the run rate since 10 August. |
| 5 | The two lines chosen at markers 9 and 10 | Each number in them holds on its own. |

The two numbers to post beside the letters are 9, the members Marketing rings first, and
Rs 1,57,51,980, Q2's lead over plan to date at mid-quarter.

## Why is each key right, item by item?

### Q1. Which function gives members who spent the same the same place, and skips the places they use up?

Kind: choose the rule. The key is c, `rank()`. Members who spent the same share a place, and the next
member's place skips the numbers they used, 1, 1, 3, so no member is dropped by a coin toss and a tie
at the line ships whole.

- a, `row_number()`: gives every member a place of their own, so one of two members who spent the same
  is left off by whatever decides between them.
- b, `dense_rank()`: shares the place and skips nothing, so its numbers count spend figures; Retail-Core
  ships 52 under it, two members who tie with nobody at the line.
- d, "`count(*)`, which counts the members up to and including each one's figure": with an ORDER BY,
  `count(*)` counts each member's peers in, so a tie that straddles the line pushes both members past
  it. That is whole ties only, the rule that ships short of fifty whenever a tie sits on the line.

### Q2. Which ORDER BY inside the window lets two members who spent the same tie?

Kind: fix the logic. The key is b, `ORDER BY q2_revenue DESC`. Members are ordered by what they spent,
highest first, and two who spent the same are peers, so RANK gives them one place.

- a, `ORDER BY q2_revenue DESC, customer_id`: the customer id breaks every tie, so RANK ships exactly
  what ROW_NUMBER ships, and the check "members who spent the same share a place" fails on
  Retail-Core's pairs at places 31 and 32 and at 37 and 38.
- c, `ORDER BY q2_revenue`: ascending, so place 1 is the member who spent least and the list holds
  each segment's fifty smallest spenders.
- d, `ORDER BY customer_id`: numbers members by id, so each list holds the fifty lowest ids, whatever
  they spent.

### Q11. Which plan fits 150 calls this week, sized in calls?

Kind: a design item, the best-fit plan sized in calls; the count rests on your own Retail-Plus run.

The key is d, "Keep the lists, ring each in place order up to 150, and name the rest: your Retail-Plus
count less 45". The lists are the head's rule applied, and the cap limits this week's calls. Business 35,
Retail-Core 50 and Student 20 make 105, so with Retail-Plus's count the lists hold 105 plus that count,
which is that count less 45 more than the week's 150. Those members, the lowest places on the lists,
are named and carried to next week.

- a, "Switch every list to `row_number()`, so they hold 155, and leave the five lowest Retail-Plus
  places for next week": changes the head's rule to solve a scheduling problem, and still leaves
  members waiting.
- b, "Drop the Student list, 20 calls, so the other three lists fit inside the week's 150, and say
  nothing of it": removes a segment Marketing asked to protect, and nobody is told.
- c, "Ring the 150 listed members with the most Q2 revenue across the four lists, Business first and
  the rest after": ranks across the book again, chapter 1's mistake, so every Business buyer comes
  first and the members cut are Retail-Plus's and Student's.

### Q3. Which window keeps each member's months to themselves?

Kind: fix the logic. The key is b, `OVER (PARTITION BY customer_id ORDER BY month)`. The partition
restarts LAG for every member, so LAG returns NULL on a member's first month and never reaches into another
member's months; the check cell counts 0 rows that cross.

- a, `OVER (PARTITION BY segment ORDER BY month)`: lines up every member of a segment by month, so
  LAG compares a member with whichever member's row sorts just before; the check cell counts more than
  700 rows that cross, and with the calendar condition the flag finds nobody to ring.
- c, "`OVER (ORDER BY customer_id, month)`, since the sort keeps a member's months together": the sort
  keeps them together and LAG still runs from one member's last row into the next member's first. The
  check cell counts 300 rows that cross, one at every boundary between members.
- d, `OVER (PARTITION BY month ORDER BY customer_id)`: each window holds one month of every member, so
  LAG compares a member with the member whose id sorts before theirs in the same month.

### Q4. Which condition keeps a flag only for three calendar months in a row?

Kind: fix the logic. The key is a, `month_1_back = DATE '2026-08-01' AND month_2_back = DATE
'2026-07-01'`. The flag holds only when the two rows before September are August and July, so a member
who skipped either month is not flagged: 9 members, every one of them on a list.

- b, `spend_1_back IS NOT NULL AND spend_2_back IS NOT NULL`: true for every member with two earlier
  rows, whichever months they were, so it keeps chapter 4's 16, C-0216 among them.
- c, `coalesce(spend_1_back, 0) > spend AND coalesce(spend_2_back, 0) > spend_1_back`: repeats the
  fall the query already tests and never asks which months were read, so it keeps the same 16.
- d, `month_1_back < month AND month_2_back < month_1_back`: earlier rows always hold earlier months,
  so the condition is always true and keeps the 16.

### Q12. How should the team build a list of members who went quiet, sized in rows?

Kind: a design item, the best-fit build sized in rows.

The key is a, "A calendar of every member and month left empty, 1,806 rows, read as a flag of its own
beside the falling-spend flag". A member who went quiet has no September row in the monthly table, so
only a table with a row for every member in every month, 301 times 6, can show the empty September as
a row a query can find. It is a second flag with its own name: across the book, 27 members bought in
July and in August and placed no order in September. Mixed into the falling-spend flag, it would tell
a member their spend fell when they simply did not order.

- b, "The monthly table the flag reads, 752 rows, keeping the members whose September spend is NULL":
  a member with no September order has no September row at all, so there is no NULL to keep and the
  list comes back empty.
- c, "The same calendar with zero in every empty month, 1,806 rows, so a quiet September counts as a
  fall to zero in the flag": mixes two signals, and the zero-filled flag names 26 members, 17 of them
  for a September with no order.
- d, "The falling-spend flag with its calendar condition removed, 752 rows, since members with gaps
  include the quiet ones": brings back the 7 members who skipped a month, and every one of them
  ordered in September, so none of them went quiet.

### Q5. Which expression puts the segment's whole Q2 revenue beside every member's row?

Kind: choose the window. The key is a, `sum(q2_revenue) OVER (PARTITION BY segment)`. With a partition
and no ORDER BY, the sum covers the whole segment and every member's row carries it: Rs 3,66,250 on
each Retail-Core row.

- b, `sum(q2_revenue) OVER (PARTITION BY segment ORDER BY q2_revenue DESC)`: an ORDER BY turns the sum
  into a running total, so each row carries the segment's total only down to that member, and
  Retail-Core's share would read about twenty times its revenue.
- c, `sum(q2_revenue) OVER ()`: the whole book, Rs 9,84,00,000, beside every row, so Retail-Core's
  share reads 0.3 percent.
- d, `sum(q2_revenue) OVER (ORDER BY segment)`: a running total across segments in alphabetical order,
  so each segment's rows carry its own revenue plus every segment before it.

### Q6. Which share answers "how much of each segment's revenue does its list cover"?

Kind: choose the measure. The key is c, "the list's revenue over the segment's revenue". The ask is
about revenue, and about each segment's own: Retail-Core's fifty carry Rs 2,78,740 of Rs 3,66,250, 76.1
percent.

- a, "the list's revenue over the book's Q2 revenue, Rs 9,84,00,000": Retail-Core's list would read
  0.3 percent, which only says that Business books the rupees.
- b, "the list's members over the segment's members who bought": counts heads, 52.1 percent for
  Retail-Core, where the rupees on the list are 76.1 percent.
- d, "the last listed member's revenue over the first's": compares two members, and says nothing
  about how much of the segment the list covers.

### Q13. What does widening Retail-Core's list to seventy-five buy, sized per call?

Kind: a design item, the sizing of the alternative.

The key is d, "Rs 60,300 more for 25 more calls, about Rs 2,412 a call against about Rs 5,575 a call on
the first fifty". The first fifty carry Rs 2,78,740 over 50 members, about Rs 5,575 each; places 51 to
75 carry Rs 60,300 over 25, Rs 2,412 each. Widening takes the list from 76.1 to 92.6 percent of
Retail-Core's Rs 3,66,250 at less than half the rupees per call, and the marketing lead decides
whether a call is worth that.

- a, "Half as much revenue again, about Rs 1,39,370 more, since seventy-five members is half as many
  again as fifty": spend falls with place, so the 25 members below fiftieth booked far less than the
  fifty above them, Rs 60,300 between them.
- b, "Rs 60,300 is 0.06 percent of the book's Rs 9,84,00,000, too little to justify 25 more calls":
  measures a Retail-Core decision against the whole book, where Business's rupees swamp every retail
  segment.
- c, "Rs 60,300 more at the same rupees per call as the first fifty, so the 25 calls cost nothing more
  per rupee": the rupees are right and the rupees per call fall by more than half.

### Q7. Which expression gives every Q2 order a plan week, including 1 to 5 July?

Kind: fix the logic. The key is b, `greatest(date_trunc('week', order_date)::date, (SELECT
min(week_start) FROM plan_line))`. Q2 starts on Wednesday 1 July and the plan on Monday 6 July, so the
25 orders of 1 to 5 July fall under Monday 29 June, a week the plan line does not have. `greatest()`
moves them onto the plan's first Monday, and the running total closes on Rs 9,84,00,000.

- a, "`date_trunc('week', order_date)::date`, the Monday that starts each order's own calendar week":
  the 1 to 5 July orders land on 29 June, and the join from the plan's weeks drops them; the close
  reads Rs 9,68,60,180, "Rs 15,39,810 short of plan".
- c, "`date_trunc('month', order_date)::date`, which files each order under the first day of its
  month": no plan week starts on the first of a month, so every week books nothing and Q2 reads as
  having booked nothing at all.
- d, "`(order_date - 5)`, which shifts every order by the five days between 1 July and the plan's first
  Monday": a shifted date lands on a plan Monday only on some days, so most orders find no week and the
  close reads Rs 1,02,62,270.

### Q8. Which comparison counts the weeks that ran below plan, each week on its own?

Kind: choose the comparison. The key is b, `booked < plan_revenue`. Each week's booking against its
own plan: from the week of 10 August, six of the seven full weeks booked below Rs 75,69,230, and only
the week of 14 September booked above it.

- a, `booked_to_date < plan_to_date`: the to-date reading, which stays ahead in all seven weeks
  because of the lead built in July, so it counts 0.
- c, `booked_to_date < plan_revenue`: sets a quarter's bookings to date beside one week's plan, the
  nine-times mistake, and counts 0.
- d, "`sum(booked) < sum(plan_revenue)` over the seven weeks": one comparison for all seven weeks
  together, which says the stretch fell short and cannot say how many weeks did.

### Q14. Which way answers Meera's "where were we on 19 August?", and what does it say?

Kind: a design item, the switch to a plain sum for one date, sized.

The key is c, "One plain SUM of the Q2 orders dated on or before 19 August, the 462 orders read once:
Rs 6,57,78,430". A single reading on a date Meera names is one sum with the date in WHERE; it adds up
268 orders. The figure sits between the to-date readings at the end of the weeks of 10 and 17 August,
as a Wednesday's should.

- a, "The running total's row for the week of 17 August, the plan week that holds 19 August:
  Rs 6,87,36,590": that row runs to 23 August, four days past her date.
- b, "The row for the week of 10 August, the last plan week finished by 19 August: Rs 6,32,84,780":
  stops on 16 August and misses three days of orders.
- d, "Thirteen plain sums, one per plan week, 6,006 order reads, then the week that holds 19 August:
  Rs 6,87,36,590": thirteen times the work to reach the same wrong date as option a.

### Q9. Which line goes to Meera for the leadership meeting?

Kind: choose the line. The key is c, "Q2 closed on plan, Rs 10 ahead; the mid-quarter lead came from
one July week, and six of seven weeks since 10 August ran below." It carries the close, Rs 9,84,00,000
against Rs 9,83,99,990, the source of the lead, the week of 13 July, which booked Rs 2,66,28,920 against
its Rs 75,69,230, and the run rate since 10 August.

- a, "Q2 closed Rs 15,39,810 short of plan on the running total, so the next quarter should open on a
  recovery campaign to win it back": the close of a running total that lost the orders of 1 to 5 July.
- b, "Q2 closed on plan and stood Rs 1.58 crore ahead at mid-quarter, so the quarter needs no action
  from the leadership meeting at all": both numbers are right, and the line hides the run rate that has
  sat below plan since 10 August.
- d, "Q2 revenue to date stood at about nine times the weekly plan by mid-quarter, well ahead of every
  target the plan line set": Rs 6,87,36,590 to date beside one week's Rs 75,69,230; to date goes beside
  to date.

### Q10. Which line goes to Marketing with the lists?

Kind: choose the line. The key is b, "Each list holds fifty, or every buyer where a segment has fewer,
and a list above fifty names the members tied at its line." It states the head's rule as the count it
ships and says what a reader sees when a list runs past fifty.

- a, "Every segment's list holds exactly fifty members, cut by a tiebreaker stated in advance, so each
  list is the same size for the calls": describes ROW_NUMBER under a hard cap, which the head of
  Retail-Plus did not ask for, and Business and Student hold fewer than fifty buyers.
- c, "The lists hold 155 members in all, fifty per segment where possible, ranked by Q2 revenue across
  the whole book": a list ranked across the whole book is chapter 1's Business list.
- d, "Each list ranks members with DENSE_RANK, so members who spent the same share a place and no
  number is skipped": DENSE_RANK ships 52 in Retail-Core, two members who tie with nobody.

### Q15. Which check should run before Meera's line leaves the team, sized?

Kind: a design item, the check that closes the loop.

The key is d, "Set the last booked to date beside Q2's total from one plain SUM of the orders,
Rs 9,84,00,000". A running total that lost rows closes short of a total counted without it, and the
plain sum shares no join, no week and no window with it, so the two rows either agree or show the
missing rupees.

- a, "Set the last plan to date beside the plan line's own total, Rs 9,83,99,990, one row a side":
  checks the plan side, which a lost order cannot touch.
- b, "Count the running total's rows beside the plan's 13 weeks, so that no plan week can go missing":
  the plan-first build has all 13 weeks and still lost five days of orders.
- c, "Run the running total a second time and set the two closes side by side": the same build twice
  loses the same rows twice.

## Which wrong answers does the debrief replay?

Item 7, option a, first, with item 9, option a: the build that reports Q2 Rs 15,39,810 short of plan
is the line most likely to reach Meera, and item 15's check catches it in one row. Then item 3, option
c, with item 4, option a: together they flag 9 members, the right count from a window that crosses
members, and the check cell's 300 crossings show why a right count does not prove a right window. Then item
2, option a, if anyone chose it: the customer id inside the ORDER BY turns the head's rule into
ROW_NUMBER. Last, item 8, option a: to date and the run rate answer different questions, and Meera
needs both.

## Where does this show up at work?

The data team sends Kalpa's marketing lead three things to act on: who to protect, who to call first,
and whether the quarter can pay for it. Each becomes a number someone repeats in a meeting, so
each goes out with its rule, its count and the check that closed it, the way this case's five parts
end.

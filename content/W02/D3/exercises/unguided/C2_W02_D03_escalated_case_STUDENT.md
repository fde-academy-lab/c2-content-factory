# What does Marketing get on Monday: each segment's list with its count, the members to ring first, the share of revenue the lists carry, and Q2 against plan?

Work the escalated case alone, in five parts. Parts 1 and 2 run in the afternoon for 20 minutes, and
parts 3 to 5 run in the practice lab. You work in `notebooks/C2_W02_D03_ex1_escalated_case_STUDENT.ipynb`,
and this brief carries everything the case needs. Items 1 to 10
are the notebook's ten lettered markers, with the same numbers and the same letters. Items 11 to 15
are this brief's own design items, one at the end of each part, answered here.

> "We start calling on Monday. Send me each segment's protect list under the head of Retail-Plus's
> rule, with its count; the members we ring first; how much of each segment's Q2 revenue the lists
> cover; and one sentence Meera can take into the leadership meeting on whether Q2 is on track."
>
> The marketing lead, Kalpa Retail

Kalpa Retail sells to four segments: Business, its corporate buyers, whose orders run to lakhs;
Retail-Core, its everyday shoppers; Retail-Plus, its paid membership tier; and Student. The head of
Retail-Plus has asked that members who spent the same be ranked the same and that every list say how
many made it: "If two members spent the same, I want them ranked the same, and I want to know how many
made the top fifty, not forty-nine because of a tie." The line is the last place a list keeps,
fiftieth on a top fifty. Marketing wants to ring the listed members whose monthly spend fell two months
running. Meera Raghavan, Kalpa Retail's CEO, wants to know whether Q2 is on track against the plan line,
by the total and week by week.

Q2 is July to September 2026. A member's Q2 revenue is booked revenue, every Q2 order at its amount
whatever its status, Rs 9,84,00,000 for the quarter, and a member's monthly spend is their booked revenue
in one calendar month. The plan line holds 13 plan weeks, each starting on a Monday from 6 July to 28
September, Rs 75,69,230 a week and Rs 9,83,99,990 in all; Q2's orders run from Wednesday 1 July to 28
September. To date means every week up to and including the one on the row, and mid-quarter is the
end of the seventh plan week, the week of 17 August. The run rate is how each week runs against its
own plan of Rs 75,69,230. Kavya Nair, the senior analyst on Kalpa Retail's data team, checks every
number before it leaves the team.

| Table | Rows | Columns |
|---|---|---|
| orders | 1,000, one per order | order_id, customer_id, order_date, quarter, channel, amount, status |
| customers | 340, one per member | customer_id, segment, city, country, joined_date |
| plan_line | 13, one per plan week | week_start, the Monday the week starts, and plan_revenue |

| Segment | Members who bought in Q2 | Q2 revenue |
|---|---|---|
| Business | 35 | Rs 9,75,84,600 |
| Retail-Core | 96 | Rs 3,66,250 |
| Retail-Plus | 76 | Rs 4,13,380 |
| Student | 20 | Rs 35,770 |
| The book | 227 | Rs 9,84,00,000 |

**Who needs the answer.** The marketing lead needs it because the team starts calling on Monday, the
head of Retail-Plus needs it to answer the tier's members for every call and every count, and Meera
needs one sentence to carry into the leadership meeting. A list with the wrong count, a call to a member
whose spend never fell, or a quarter misread against plan each costs a decision.

**The questions on the way.**

- Which members make each segment's list under the head of Retail-Plus's rule, and how many in each?
- Which listed members does Marketing ring first?
- How much of each segment's Q2 revenue does its list carry?
- Is Q2 on track by the total and by the run rate?
- What goes to Marketing and Meera?

**What you post.** One line of fifteen letters in item order, no spaces, items 1 to 10 from the
notebook's markers and items 11 to 15 from this brief, in this shape:

```
Post exactly this shape: xxxxxxxxxxxxxxx
```

Beside the letters, post two numbers your notebook prints: how many members Marketing rings first, and
Q2's lead over plan to date at mid-quarter.

---

## Part 1. Which members make each segment's list under the head of Retail-Plus's rule, and how many in each?

This comes up at work whenever a ranked list that a business acts on states its rule and its count, since the
count is the first line a manager checks.

In the afternoon, about 10 minutes: markers 1 and 2 in the notebook, then item 11 here. The notebook
builds each member's Q2 revenue, places every member inside their segment with
`FUNCTION OVER (PARTITION BY segment ORDER ...)`, keeps places 1 to 50, and prints each list's count
beside the segment's buyers.

### Q1. Which function puts the head of Retail-Plus's rule into the window?

The head of Retail-Plus wants members who spent the same ranked the same, and a list that says how many
made the top fifty. Which function puts that rule into the window?

a) `row_number()`, which gives every member a place of their own, ties too

b) `dense_rank()`, which gives tied members one number and skips none

c) `rank()`, which gives tied members one number and skips the places used

d) `count(*)`, which counts the members at or above each one's own figure

### Q2. Which ORDER BY inside the window lets two members who spent the same tie?

Which ORDER BY inside the window lets two members who spent the same tie?

a) `ORDER BY q2_revenue DESC, customer_id`

b) `ORDER BY q2_revenue DESC`

c) `ORDER BY q2_revenue`

d) `ORDER BY customer_id`

### Q11. Which plan fits 150 calls this week, sized in calls?

Marketing's member team can make 150 calls this week. The four lists hold more than 150 members
between them: Business 35 and Student 20, every buyer in both, Retail-Core 50, and Retail-Plus the
count your own run gave. Which plan fits, sized in calls?

a) Switch every list to `row_number()`, so they hold 155, and leave the five lowest Retail-Plus places for next week

b) Drop the Student list, 20 calls, so the other three lists fit inside the week's 150, and say nothing of it

c) Ring the 150 listed members with the most Q2 revenue across the four lists, Business first and the rest after

d) Keep the four lists, ring each in place order up to 150 calls, and name the rest: your Retail-Plus count less 45

## Part 2. Which listed members does Marketing ring first?

This comes up at work whenever a retention call goes to a customer whose own history shows the drift, so the
definition of the drift is written down before the first call.

In the afternoon, about 10 minutes: markers 3 and 4 in the notebook, then item 12 here. The notebook
builds each member's monthly spend, one row per member per month with an order, sets LAG's previous
two rows beside each row with the months they came from, and keeps the September rows whose spend fell
twice running and whose member is on a list.

### Q3. Which window keeps each member's months to themselves?

Which window keeps each member's months to themselves?

a) `OVER (PARTITION BY segment ORDER BY month)`

b) `OVER (PARTITION BY customer_id ORDER BY month)`

c) `OVER (ORDER BY customer_id, month)`, since the sort keeps a member's months together

d) `OVER (PARTITION BY month ORDER BY customer_id)`

### Q4. Which condition keeps a flag only for three calendar months in a row?

Which condition keeps a flag only for three calendar months in a row?

a) `month_1_back = DATE '2026-08-01' AND month_2_back = DATE '2026-07-01'`

b) `spend_1_back IS NOT NULL AND spend_2_back IS NOT NULL`

c) `coalesce(spend_1_back, 0) > spend AND coalesce(spend_2_back, 0) > spend_1_back`

d) `month_1_back < month AND month_2_back < month_1_back`

### Q12. How should the team build this Monday's list of members who went quiet, sized in rows?

For this Monday's calls Marketing also wants the members who went quiet: they bought in July and in
August and placed no order in September. The monthly table holds one row per member per month with an
order, 752 rows for the 301 members who ever bought, and a calendar of every member and month would hold
301 times 6 rows. How should the team build that list, sized in rows?

a) A calendar of every member and month, 1,806 rows, with September left empty where no order came

b) The 752-row monthly table, keeping members with July and August rows and no September row, by NOT EXISTS

c) The calendar with zero in every empty month, 1,806 rows, so a quiet September reads as a fall to zero

d) The falling-spend flag with its calendar condition removed, 752 rows, since members with gaps went quiet

## Part 3. How much of each segment's Q2 revenue does its list carry?

This comes up at work whenever a protect budget is judged by the revenue it covers, so every list carries its
share of the whole it was cut from.

In the practice lab: markers 5 and 6 in the notebook, then item 13 here.

### Q5. Which expression puts the segment's whole Q2 revenue beside every member's row?

Which expression puts the segment's whole Q2 revenue beside every member's row?

a) `sum(q2_revenue) OVER (PARTITION BY segment)`

b) `sum(q2_revenue) OVER (PARTITION BY segment ORDER BY q2_revenue DESC)`

c) `sum(q2_revenue) OVER ()`

d) `sum(q2_revenue) OVER (ORDER BY segment)`

### Q6. Which share answers "how much of each segment's revenue does its list cover"?

Which share answers the marketing lead's "how much of each segment's revenue does its list cover"?

a) the list's revenue over the book's Q2 revenue, Rs 9,84,00,000

b) the list's members over the segment's members who bought

c) the list's revenue over its own segment's whole Q2 revenue

d) the list's revenue over the four lists' revenue together

### Q13. What does widening Retail-Core's list to seventy-five buy, sized per call?

The marketing lead asks whether to widen Retail-Core's list from fifty to seventy-five. The fifty
booked Rs 2,78,740 in Q2, the 25 members at places 51 to 75 booked Rs 60,300 between them, and nobody
ties at seventy-fifth. What does widening buy, sized per call?

a) Half as much revenue again, about Rs 1,39,370 more, since seventy-five members is half as many again as fifty

b) Rs 60,300 is 0.06 percent of the book's Rs 9,84,00,000, too little to justify 25 more calls

c) Rs 60,300 more at the same rupees per call as the first fifty, so the 25 calls cost nothing more per rupee

d) Rs 60,300 more for 25 more calls, about Rs 2,412 a call against about Rs 5,575 a call on the first fifty

## Part 4. Is Q2 on track by the total and by the run rate?

This comes up at work whenever a quarter is read twice, by the total so far and by how each week is running,
since the two can disagree.

In the practice lab: markers 7 and 8 in the notebook, then item 14 here. The notebook adds up Q2's
orders by plan week and runs booked and plan to date side by side, one row per plan week.

### Q7. Which expression gives every Q2 order a plan week that the plan line holds?

Which expression gives every Q2 order a plan week, one of the thirteen weeks the plan line holds?

a) `date_trunc('week', order_date)::date`, the Monday that starts each order's own calendar week

b) `greatest(date_trunc('week', order_date)::date, (SELECT min(week_start) FROM plan_line))`

c) `date_trunc('month', order_date)::date`, which files each order under the first day of its month

d) `(order_date - 5)`, which moves every order back five days before it meets a plan week

### Q8. Which comparison counts the weeks that ran below plan, each week on its own?

Which comparison counts the full weeks from 10 August that ran below plan, each week on its own?

a) `booked_to_date < plan_to_date`

b) `booked < plan_revenue`

c) `booked < plan_to_date`

d) `sum(booked) < sum(plan_revenue)` over the seven weeks

### Q14. Which way answers Meera's "where were we on 9 September?", and what does it say?

Before the leadership meeting Meera asks: "Where were we on 9 September?" Which way answers her, sized,
and what does it say?

a) The running total's row for the week of 7 September, the plan week that has 9 September: Rs 8,19,30,010

b) The row for the week of 31 August, the last plan week finished by 9 September: Rs 7,53,96,740

c) One plain SUM of the Q2 orders dated on or before 9 September, the 462 orders read once: Rs 7,57,80,560

d) The plan to date on the running total's row for the week of 7 September, one row read: Rs 7,56,92,300

## Part 5. What goes to Marketing and Meera?

This comes up at work whenever a stakeholder carries one sentence of an analysis into a meeting, so every
number in that sentence has to hold on its own.

In the practice lab: markers 9 and 10 in the notebook, then item 15 here.

### Q9. Which sentence goes to Meera for the leadership meeting?

Which sentence goes to Meera for the leadership meeting?

a) "Q2 closed Rs 15,39,810 short of plan on the running total, so the next quarter should open on a recovery campaign to win it back."

b) "Q2 closed on plan and stood Rs 1.58 crore ahead at mid-quarter, so the quarter needs no action from the leadership meeting at all."

c) "Q2 closed on plan, Rs 10 ahead; the mid-quarter lead came from one July week, and six of seven weeks since 10 August ran below."

d) "Q2 revenue to date stood at about nine times the weekly plan by mid-quarter, well ahead of every target the plan line set."

### Q10. Which sentence goes to Marketing with the lists?

Which sentence goes to Marketing with the lists?

a) "Every segment's list holds exactly fifty members, cut by a tiebreaker stated in advance, so each list is the same size for the calls."

b) "Each list holds fifty, or every buyer where a segment has fewer, and a list above fifty names the members tied at its line."

c) "The lists hold 155 members in all, fifty per segment where possible, ranked by Q2 revenue across the whole book."

d) "Each list ranks members with DENSE_RANK, so members who spent the same share a place and no number is skipped."

### Q15. Which check should run before Meera's sentence leaves the team, sized?

Before Meera's sentence leaves the team, Kavya asks for one check that would catch a running total that
lost rows on the way. Which check fits, sized?

a) Set the last plan to date beside the plan line's own total, Rs 9,83,99,990, one row a side

b) Count the running total's rows beside the plan's 13 weeks, so that no plan week can go missing

c) Run the running total a second time and set the two closes side by side, two runs of one build

d) A plain SUM of Q2's orders, 462 rows read, set beside the running total's last booked to date

## Which rules does the case keep?

- The data is the warehouse's orders, customers and plan_line tables, read where they live; nothing is
  exported.
- Retail-Plus's count is the one your own run gives, and this brief never prints it. If it is not
  fifty, your sentence to Marketing names the members tied at the line and their figure.
- Work alone. The support TA answers environment problems only.
- The debrief in the practice lab replays the room's wrong answers from all five parts, so post your
  letters before it starts.

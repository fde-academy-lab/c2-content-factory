# Round 3 set: whose spend is falling, and is the quarter on plan?

Marketing asked the team to "flag anyone whose monthly spend has fallen for two months running",
and added: "Meera wants to see revenue accumulate week by week against the plan line, so we know by
mid-quarter whether we are on track." A member on the flag list will be contacted, so a flag that
accuses the wrong member costs a phone call and some goodwill, and a running total that reads the
plan wrongly costs Meera a decision.

Seven items, about fifteen minutes, worked in pairs. Monthly spend is one row per member per month
in which the member placed an order, April to September, summed from the booked amounts. A
flagged member spent less in September than in August, and less in August than in July.

Post one line in this shape, your seven letters in item order: `1x 2x 3x 4x 5x 6x 7x`

---

### Q1

A first attempt reads `lag(spend, 1) OVER (ORDER BY customer_id, month)` and `lag(spend, 2)` with
the same window, and it flags 20 members. A reviewer notices that a member's very first month
carries a previous spend. What went wrong?

a) LAG ran over the whole table, so a member's first months read the member sorted before
b) LAG skipped the months with no order, so every one of the 20 flagged members has a gap in it
c) The order should put month first, so the lag reads the same month for the member before
d) The September filter ran first, so LAG could only see the September rows of each member

### Q2

With `PARTITION BY customer_id ORDER BY month` in place, look at C-0010, a Retail-Core member. His
monthly spend is April Rs 1,710, June Rs 4,060, July Rs 7,840, August Rs 4,080 and September
Rs 1,990, with no order in May. What does `lag(spend)` return on his June row?

a) NULL, since May has no order and LAG stops at a missing month
b) Rs 1,710 from April, a previous row that is two months back
c) Rs 0 for May, since LAG fills a month with no order with zero
d) Rs 7,840 from July, since LAG reads the next row by default

### Q3

The partitioned flag lists C-0216, a Retail-Plus member: May Rs 6,440, no June order, July
Rs 4,300, no August order, September Rs 2,540. He calls to say he was on holiday in August and
should not be on a list of members who are drifting. Which reply holds?

a) He is falling, since each order he placed was smaller than the one before it
b) Fill June and August with zero, which keeps him flagged under one consistent rule
c) He is right, since LAG read July as last month; require August and July first
d) Drop the flag for any member with a gap anywhere in the year, whatever the months were

### Q4

The partitioned flag holds 16 members, and 7 of them have a previous row that is not the previous
calendar month. The fix requires the two previous rows to be August and July. How many members
does the fixed flag hold?

a) 16, since the fix changes which months are read and keeps every member
b) 23, since the fix adds back the members that the gaps had been hiding
c) 7, since only the members with a gap were checked by the fix itself
d) 9, since the seven gap-spanners drop out and the other members stay

### Q5

Meera's running total uses `sum(amount) OVER (ORDER BY order_date)` on the order rows. All twelve
orders of 22 July show the same running total, Rs 3,76,90,290. What is going on, and what is the
fix?

a) The twelve orders were double-posted, so the fix is to remove eleven of the twelve first
b) The window needs PARTITION BY order_date, so each day restarts its own total
c) Rows sharing a date are peers, each showing the day's close; add order_id to the order
d) Postgres rounds a running total to the day, so the fix is to cast the date to text

### Q6

A dashboard at the end of the seventh plan week shows booked to date Rs 6,87,36,590 beside the
plan figure Rs 75,69,230 and reads "nine times the plan". Which reading should go to Meera?

a) Q2 is nine times ahead, since the booked figure is nine times the plan figure
b) The plan side is one week; plan to date is Rs 5,29,84,610, so Q2 is Rs 1,57,51,980 ahead
c) Q2 is behind, since each week's booking should equal Rs 75,69,230 and several weeks fell short
d) The booked side is wrong, since a running total cannot pass the plan by week seven

### Q7

Which order of steps builds the falling-spend flag and proves it before Marketing reads it?

a) Monthly spend per member, LAG by member in month order, the months checked, then the fall
b) LAG by month over the whole table, then monthly spend per member, then the fall, then the months
c) Monthly spend per member, then the fall checked on September, then LAG, then the months checked
d) Monthly spend per member, then LAG by month over the whole table, then the fall, then a count

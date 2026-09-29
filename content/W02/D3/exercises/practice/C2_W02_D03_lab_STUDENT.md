# Practice lab: rank, compare, accumulate

About an hour, with a TA in the room. Four problems climb in difficulty: two on paper, one query on
the warehouse, and one that uses all three of the morning's rounds on a question nobody has asked
yet. Work in a fresh SQL file of your own; the warehouse is the same one the morning used. Q2
revenue per member is the booked amount of the member's Q2 orders, all statuses, the definition
Monday's suite used for the Rs 9,84,00,000 quarter.

Solutions open at the close of the lab, in `../solutions/C2_W02_D03_lab_solution_STUDENT.md` and
`../solutions/C2_W02_D03_lab_solution_STUDENT.sql`.

## P1. Predict three rankings on a tie (paper, about 10 minutes)

Seven invented members spent the amounts below in Q2. They exist only for this problem.

| Member (invented) | Q2 spend |
|---|---|
| G | Rs 6,450 |
| H | Rs 5,980 |
| J | Rs 5,980 |
| K | Rs 5,120 |
| L | Rs 4,870 |
| M | Rs 4,870 |
| N | Rs 4,870 |

1. Write the ROW_NUMBER, RANK and DENSE_RANK columns for all seven, ordered by spend from the top,
   with the member name breaking a tie for ROW_NUMBER.
2. Marketing asks for a top four. Write how many members each rule ships: ROW_NUMBER, RANK,
   DENSE_RANK, and "whole ties only", which drops a tie that crosses the line.
3. Marketing changes its mind and asks for a top five. Write the four counts again.
4. In one sentence, say which of the two lists would surprise a segment head who asked for "ties
   ranked the same", and under which rule.

When your paper is done, type the invented members into a `VALUES` list and check it.

## P2. GROUP BY or window for six asks (paper, about 10 minutes)

For each ask, write G if GROUP BY answers it or W if it needs a window, and one sentence on how many
rows the answer has and why.

1. The Store Operations lead asks how many members placed a Q2 order in each city.
2. Marketing asks for every Q2 order with its channel's average order value beside it, so a
   reviewer can spot unusually large orders.
3. Anand asks for the average Q2 order value in each channel, one line per channel, for the board
   pack.
4. Meera asks which cities booked more than Rs 50,00,000 in Q2.
5. The city managers ask for the three biggest members by Q2 revenue in each city.
6. The Retail-Plus team asks for each member's September spend beside the same member's August
   spend.

## P3. Thank-you vouchers for Retail-Core (warehouse, about 15 minutes)

The Retail-Core lead writes: "We want to send a thank-you voucher for the five biggest Retail-Core
orders of Q2 in each channel, app, store and web. If two orders are the same size, both get a
voucher, and tell me how many vouchers I am printing."

1. Write the query that lists the orders, with the channel, the position, the order, the member
   and the amount.
2. Count the orders the list ships in each channel and in all, and count them again under
   ROW_NUMBER and DENSE_RANK so you can say what the other rules would have printed.
3. Count the distinct members who get a voucher, because a member with two orders on the list
   raises a question the lead will ask.
4. Write the one sentence the lead reads: the rule, the number of vouchers, and the reason for any
   channel that is not five.

## P4. The Retail-Core at-risk list (warehouse, about 25 minutes)

The Retail-Core lead follows up: "Marketing's list covered every segment. I want my own version:
who on my top fifty is drifting, how much of the list's revenue they carry, and whether my segment
was on pace through the quarter."

This problem uses all three rounds. Write each step as a CTE with one comment line above it that
says the question and the denominator.

1. The Retail-Core protect list, ranked so that tied members share a place: how many members does
   it carry, and what share of Retail-Core's Q2 revenue is on it?
2. The at-risk members: listed members who spent less in August than in July and less again in
   September than in August, with a month that has no order breaking the run. How many are there,
   and how much Q2 revenue do they carry? Count, too, how many a flag without the month check
   would have named.
3. Retail-Core's running total by week through Q2: in which week did the segment pass half its Q2
   total, and what share had it booked by the end of the week of 17 August, the seventh plan week?
4. The check: does the running total close on Retail-Core's Q2 total? Say how much a running total
   that started on 6 July, the plan's first week, would have missed, and why.
5. Three sentences for the Retail-Core lead: the list, the at-risk members and what their flag
   means, and the segment's pace.

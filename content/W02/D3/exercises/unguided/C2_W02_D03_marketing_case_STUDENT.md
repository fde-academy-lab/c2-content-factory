# The escalated case: Marketing's list for Monday

Forty-five minutes in all, unguided and on your own: a four-minute brief, thirty-one minutes on
the five parts, and ten minutes of debrief. The trainer answers questions about the brief and never
about the query. The debrief follows straight after
and replays the wrong answers the room produced, so keep every wrong turn you take; it is worth more
in the debrief than a clean first attempt.

## The ask, in Marketing's words

The morning's message came first: "Retail-Plus frequency is the problem, so we want to protect our
best members before they drift. Give us the top fifty customers by Q2 revenue in each segment, and
flag anyone whose monthly spend has fallen for two months running. And Meera wants to see revenue
accumulate week by week against the plan line, so we know by mid-quarter whether we are on track."

In the afternoon it came back sharper: "We act on this list on Monday. One file: the top fifty members by
Q2 revenue in every segment, ranked the way the head of Retail-Plus asked, a column that says
whether each one's spend fell in August and again in September, and the running total against the
plan so Meera can see where the quarter stood at mid-quarter and where it closed. Tell us the tie
rule and the number of members it ships."

The head of Retail-Plus has already said what he wants from a tie: "If two members spent the same,
I want them ranked the same, and I want to know how many made the top fifty, not forty-nine because
of a tie."

Your role: Marketing will act on your list, so you state the tie rule you chose and why, and you
defend the falling-spend flag against a member who says he was on holiday.

## Where you work

Work in either file, and both carry the same five parts.

- The SQL file `sql/C2_W02_D03_04_marketing_case_STUDENT.sql` runs as it ships, because every
  placeholder in it is a comment, and you replace `__TODO1__` to `__TODO5__` with your own steps.
- The notebook `notebooks/C2_W02_D03_hands_on_STUDENT.ipynb` carries the same `__TODO1__` to
  `__TODO5__` cells against the same warehouse, for anyone who prefers to read results as tables.

Write each part as a named step (a CTE) with one comment line above it that says the question it
answers and the denominator it uses. Q2 revenue per member is the booked amount of the member's Q2
orders, all statuses, the definition Monday's suite used for the Rs 9,84,00,000 quarter.

## Part 1. The protect list

The question is who the top fifty members by Q2 booked revenue are in each segment, with tied
members ranked the same.

Done looks like this: one row per listed member carrying the segment, the member, the Q2 revenue
and the position, plus a count of the list by segment. The count is part of the answer, because a
segment that ships more or fewer than fifty needs a reason written beside it, and a segment with
fewer than fifty Q2 buyers needs saying so.

## Part 2. The falling-spend flag

The question is which members on the list spent less in August than in July, and less again in
September than in August.

Done looks like this: a flag column on the protect list, or a list of flagged members with their
three months of spend. A month with no order is not a fall, so a member who skipped August is not
flagged, and your step shows how it knows the previous row is the previous calendar month. Count
the flagged members by segment.

## Part 3. Revenue against plan

The question is how much Q2 had booked to date at the end of each plan week, against the plan to
date.

Done looks like this: one row per plan week carrying the week, the plan to date, the booked to
date and the difference. Both sides accumulate. Read the row for the seventh plan week, which is
mid-quarter, and the last row, which is the close.

## Part 4. The check

The question is whether the last week's booked to date equals the Q2 total Monday's suite reported.

Done looks like this: one query that sets your closing booked-to-date beside the Q2 booked total
and prints the difference. If the difference is anything other than zero, find the rupees that went
missing before anyone reads the chart, and fix Part 3 until it closes.

## Part 5. The sentence

Write, as a comment, the three sentences Marketing and Meera will read.

- The first sentence gives the tie rule and how many members it ships in each segment, with the
  reason for any segment that is not fifty.
- The second gives how many listed members carry the flag and what the flag means for a member who
  says he was on holiday.
- The third says where Q2 stood against plan at mid-quarter and at the close, and what the weekly
  run rate says about the weeks since.

Kavya reads the sentence first, then the check in Part 4, and only then the queries.

## When the solutions open

The worked solution opens when the case closes, in `solutions/C2_W02_D03_protect_list_solution_STUDENT.sql`
and `solutions/C2_W02_D03_hands_on_solution_STUDENT.ipynb`, with the answers and the debrief's wrong
answers in `solutions/C2_W02_D03_marketing_case_solution_STUDENT.md`.

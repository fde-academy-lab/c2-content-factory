# Solution: Marketing's list for Monday

Answers: RANK ships 35 Business, 50 Retail-Core, 51 Retail-Plus and 20 Student members; nine
listed members are flagged, three in each of Business, Retail-Core and Retail-Plus; Q2 was ahead of
plan by Rs 1,57,51,980 at mid-quarter and closed at Rs 9,84,00,000 against Rs 9,83,99,990.

This file opens when the case closes. The worked queries are in
`C2_W02_D03_protect_list_solution_STUDENT.sql` and the executed notebook in
`C2_W02_D03_hands_on_solution_STUDENT.ipynb`, both in this folder. Other correct shapes exist; what
has to match is the counts, the flag and the two plan readings, and every step has to say what it
answers. Every figure comes from the warehouse (v4), checked 29 Sep 2026, with Q2 revenue per member
taken as the booked amount of the member's Q2 orders, all statuses.

## Part 1. The protect list

| Segment | Q2 buyers | RANK at fifty or below ships | Why |
|---|---|---|---|
| Business | 35 | 35 | Business has 35 Q2 buyers, so the list is every one of them. |
| Retail-Core | 96 | 50 | Nobody ties at fiftieth, so fifty members ship. |
| Retail-Plus | 76 | 51 | Two members tie at fiftieth on Rs 3,350, and RANK keeps both of them. |
| Student | 20 | 20 | Student has 20 Q2 buyers, so the list is every one of them. |

The list carries 156 members in all. RANK is the rule because tied members share a position and
nobody at the line is dropped by a coin toss, which is what the head of Retail-Plus asked for, and
the report says how many shipped and why.

The wrong answers the debrief replays for Part 1 are these.

- The whole-table list ranks all 227 buyers together and ships 35 Business, 11 Retail-Plus,
  4 Retail-Core and no Student members, which answers "the fifty biggest members" when Marketing
  asked for fifty per segment.
- ROW_NUMBER ships exactly 50 Retail-Plus members and drops one of the two tied at fiftieth, and
  the database picks which one, so a member can be on one run's list and off the next with the
  same spend. A customer_id tiebreaker makes the choice repeatable and leaves it just as unfair.
- DENSE_RANK at fifty or below ships 52 Retail-Plus members, because a tie higher up the list
  compresses the dense numbers and lets two members below the tie onto the list.
- Whole ties only ships 49 Retail-Plus members, the "forty-nine because of a tie" the head of
  Retail-Plus forbade in so many words.

On Retail-Plus revenue, the RANK list carries Rs 3,56,780 and the ROW_NUMBER list Rs 3,53,430; the
difference is the one tied member ROW_NUMBER drops.

## Part 2. The falling-spend flag

Nine listed members spent less in August than in July and less again in September than in August,
three in each of Business, Retail-Core and Retail-Plus. No Student member is flagged. All nine are
on the protect list, so the flag is a column on it and nobody drops off the list for carrying it.

The wrong answers the debrief replays for Part 2 are these.

- LAG without PARTITION BY flags 20 members across the warehouse, 18 of them on the list. Four of
  the 20 compared a member's month with another member's month; the tell is a first month that
  carries a previous value.
- LAG with the partition and no month check flags 16, all of them on the list. Seven of the 16
  have a previous row that is not the previous calendar month, so a skipped month was read as a
  fall. The worked example is C-0216 (May Rs 6,440, no June, July Rs 4,300, no August, September
  Rs 2,540), who was right to say he was on holiday.
- Filling a missing month with zero makes every holiday a fall to zero, which flags more members
  who were away and answers a different question.

The fix requires the previous two rows to be August and July, which leaves nine. A member with no
August order is not flagged, because a month without an order is no reading.

## Part 3. Revenue against plan

The plan line has 13 weeks, from Monday 6 July to Monday 28 September, at Rs 75,69,230 each, which
is Rs 9,83,99,990 in all. Both sides accumulate, and the booked side is read at each plan week's
last day, so the orders of 1 to 5 July count.

| Plan week starting | Plan to date | Booked to date | Ahead of plan |
|---|---|---|---|
| 6 Jul | Rs 75,69,230 | Rs 51,00,180 | Rs 24,69,050 behind |
| 13 Jul | Rs 1,51,38,460 | Rs 3,17,29,100 | Rs 1,65,90,640 |
| 20 Jul | Rs 2,27,07,690 | Rs 4,22,44,480 | Rs 1,95,36,790 |
| 27 Jul | Rs 3,02,76,920 | Rs 4,87,81,050 | Rs 1,85,04,130 |
| 3 Aug | Rs 3,78,46,150 | Rs 5,95,15,810 | Rs 2,16,69,660 |
| 10 Aug | Rs 4,54,15,380 | Rs 6,32,84,780 | Rs 1,78,69,400 |
| 17 Aug | Rs 5,29,84,610 | Rs 6,87,36,590 | Rs 1,57,51,980 |
| 24 Aug | Rs 6,05,53,840 | Rs 7,19,59,570 | Rs 1,14,05,730 |
| 31 Aug | Rs 6,81,23,070 | Rs 7,53,96,740 | Rs 72,73,670 |
| 7 Sep | Rs 7,56,92,300 | Rs 8,19,30,010 | Rs 62,37,710 |
| 14 Sep | Rs 8,32,61,530 | Rs 9,12,31,660 | Rs 79,70,130 |
| 21 Sep | Rs 9,08,30,760 | Rs 9,79,09,980 | Rs 70,79,220 |
| 28 Sep | Rs 9,83,99,990 | Rs 9,84,00,000 | Rs 10 |

The reading for Meera: at mid-quarter, the end of the seventh plan week, Q2 was ahead by
Rs 1,57,51,980, and almost all of that lead came from the week of 13 July, which booked Rs 2.66
crore on its own. From the week of 10 August, six of the seven full weeks booked below the weekly
plan of Rs 75,69,230, and the lead shrank from its peak of Rs 2,16,69,660 to Rs 10 at the close.
Q2 is on track by the total and off track by the run rate.

The wrong answers the debrief replays for Part 3 are these.

- A running total set beside one week's plan reads Rs 6,87,36,590 against Rs 75,69,230 at week
  seven as "nine times the plan"; the plan to date is Rs 5,29,84,610.
- A running total ordered by order_date alone gives every order of one day the day's closing
  figure, so the twelve orders of 22 July all show Rs 3,76,90,290; order_id as a tiebreaker gives
  each row its own step.

## Part 4. The check

The last booked-to-date is Rs 9,84,00,000, which equals Monday's Q2 total, so the difference is
zero and the chart can be read.

The wrong answer the debrief replays for Part 4 is the hurried build that starts from the plan and
joins weekly revenue onto it by `date_trunc('week', order_date)`. It shows thirteen weeks and
thirteen numbers and closes at Rs 9,68,60,180, which reports Q2 Rs 15,39,810 short of plan. The
check exposes it at once: the close is Rs 15,39,820 below Monday's total. The 25 orders placed from
1 to 5 July, Rs 15,39,820 between them, fall in the week of 29 June, which the plan line does not
have, so the join drops them. Accumulating both sides and reading the booked side at each plan
week's last day puts them back.

## Part 5. The sentence

"We ranked with RANK inside each segment, so tied members share a place and nobody at the line is
dropped by a coin toss: the list carries 35 Business and 20 Student members, which is every Q2
buyer there, 50 Retail-Core and 51 Retail-Plus, because two Retail-Plus members tie at fiftieth.
Nine listed members spent less in August than July and less again in September; a member with no
August order is not flagged, because a month without an order is no reading. Q2 closed on plan,
Rs 9,84,00,000 against Rs 9,83,99,990, and the Rs 1.58 crore lead at mid-quarter came from one week
in July, so the weekly run rate has been below plan since 10 August."

Kavya's test for the sentence: a reader who sees only these three sentences knows the rule, the
count and its reason, what the flag means and does not mean, and whether the quarter is on track.

## Where the pattern lives in production

Every retention list a CRM team acts on is this case in some form: a ranked list with a tie rule
somebody has to own, a decline flag somebody will be called about, and a pacing chart against a
plan that somebody will quote in a review. The habit that holds all three together is the Part 4
check, a closing number that has to equal a number the business already trusts.

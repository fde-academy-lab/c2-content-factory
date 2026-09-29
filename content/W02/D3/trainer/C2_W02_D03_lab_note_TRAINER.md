# TA note: the Week 2 Wednesday practice lab

The lab runs after the trainer's afternoon hour and the IITGN faculty session W2-3 (tentative), and
it takes about an hour. The learner file is `exercises/practice/C2_W02_D03_lab_STUDENT.md`; the
solutions are `exercises/solutions/C2_W02_D03_lab_solution_STUDENT.md` and
`exercises/solutions/C2_W02_D03_lab_solution_STUDENT.sql`, which runs unchanged against the
warehouse (checked 29 Sep 2026 on PostgreSQL 16.13, warehouse v4). Release the solutions when the
lab closes, never during it.

The four problems climb: P1 and P2 are paper and should take about twenty minutes together, P3 is
one query with a count, and P4 combines the three morning rounds. A learner who finishes P3 inside
the first half hour is on pace; anyone still on P1 after fifteen minutes needs the P1 hint.

Nothing in the lab touches the Retail-Plus tie or the Retail-Plus falling members, and no TA answer
should reach for them. If a learner asks about the case's Retail-Plus numbers, point them to the
case solution, which opened after the case.

## P1. Three rankings on a tie (invented members G to N)

**Where learners stall.** Most get RANK right and then write DENSE_RANK for the three-way tie at
fifth as 5, 5, 5, because they carry RANK's numbering over. The second stall is the top-four count
under DENSE_RANK: learners write 4, since "a top four ships four", and never count the dense
numbers.

**The one hint.** "Write DENSE_RANK by counting distinct spends from the top, and nothing else: how
many different amounts sit above L?"

**The numbers.** RANK 1, 2, 2, 4, 5, 5, 5; DENSE_RANK 1, 2, 2, 3, 4, 4, 4; ROW_NUMBER 1 to 7. The
top four ships 4, 4, 7 and 4 (ROW_NUMBER, RANK, DENSE_RANK, whole ties only); the top five ships 5,
7, 7 and 4. The surprise is DENSE_RANK putting seven members on a top four.

## P2. GROUP BY or window for six asks

**Where learners stall.** Asks 2 and 3 are the same average, and learners answer both G or both W.
Ask 4 draws W from learners who think "which cities" means a ranking. Ask 6 draws G from learners
who picture a table with August and September as columns.

**The one hint.** "Before you choose, say how many rows the answer has: one per group, or one per
row you started with?"

**The numbers.** Keys G, W, G, G, W, W. Ask 1 returns six cities, Delhi largest with 50 members.
Ask 2 keeps all 462 Q2 orders. Ask 4 returns five cities, with Hyderabad short of Rs 50,00,000.
Ask 5 returns 18 rows, three per city, with no tie at third in any city.

## P3. Thank-you vouchers for Retail-Core

**Where learners stall.** Three places. Some rank members instead of orders, summing first, which
answers a different question. Some forget the segment filter and get a list of Business orders in
the lakhs. Some partition by nothing and hand the lead five vouchers in all.

**The one hint.** "One row is one order here, and the ranking restarts in each channel; what goes
in PARTITION BY and what goes in ORDER BY?"

**The numbers.** RANK prints 16 vouchers (app 6, store 5, web 5), ROW_NUMBER would print 15 and
DENSE_RANK 18 (app 6, store 5, web 7). In app two orders tie at fifth on Rs 2,910 (KR-00955 and
KR-00989); in web two tie at fourth on Rs 2,900 (KR-00978 and KR-00997), so RANK skips to sixth and
the web list stays at five while DENSE_RANK takes the two orders of Rs 2,870 at dense 5. The 16
vouchers go to 16 distinct members. The largest Retail-Core Q2 order is Rs 3,000.

## P4. The Retail-Core at-risk list

**Where learners stall.** Step 2 is the main one: learners copy the morning's flag without the
month check and report five members at risk. Step 3 is the second: learners join their weekly
totals to `plan_line`, lose the week of 29 June, and close short of the segment total. A few try to
split the company plan across segments; the problem does not ask for it, so steer them back to the
segment's own total.

**The one hint.** For step 2: "Put lag(month) beside lag(spend) and read the two columns for every
flagged member; is the previous row always last month?" For step 3: "What does your last row say,
and what is Retail-Core's Q2 total from a plain sum?"

**The numbers.** The RANK list carries 50 members (fiftieth C-0005 at Rs 2,980, fifty-first C-0092
at Rs 2,950) and Rs 2,78,740 of Rs 3,66,250, 76.1 percent. At risk with the month check: 3, C-0010
(position 1), C-0049 (12) and C-0030 (16), carrying Rs 26,210, 9.4 percent of list revenue. Without
the month check: 5, adding C-0060 (37) and C-0054 (48). The weekly running total passes half,
Rs 1,83,125, in the week of 10 August (Rs 1,76,000 at the end of the week of 3 August, Rs 2,05,870
a week later), reaches Rs 2,40,360 or 65.6 percent by the end of the week of 17 August, and closes
at Rs 3,66,250. A total started on 6 July closes at Rs 3,41,890 and misses the 13 orders of 1 to
5 July, Rs 24,360.

## If the room finishes early

Ask the pairs to write the interview answer aloud for "[F] What makes a running total deterministic,
and how would you notice one that was not?", using P4's weekly totals, where each week is a single
row, and then the order rows of one busy day, where rows share a date.

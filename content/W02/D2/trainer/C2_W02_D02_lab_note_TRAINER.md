# Practice lab note, Week 2 Tuesday (for the TA)

The lab is `exercises/practice/C2_W02_D02_lab_STUDENT.md`, about 60 minutes of work, and its
solution is `exercises/solutions/C2_W02_D02_lab_solution_STUDENT.md`. Release the solution when the
room has posted its eleven letters and tried problem 4, not before. Problems 1 to 3 run on invented
tables (six web orders, five refund rows) built for the lab so that nothing from the morning can be
pasted across; problem 4 runs on the warehouse's Q1, which the day never touched.

The answer string is `1b 2d 3a 4c 5a 6b 7c 8d 9a 10c 11b`.

## Where learners stall, and the one hint for each

| Problem | Where the room stalls | The one hint |
|---|---|---|
| 1. Four row counts | Q2: they answer 6 for the LEFT join, because "LEFT keeps each order once". Q3: they answer 4, forgetting that a RIGHT join keeps R-5. | "Put your finger on W-3 and count how many rows it makes, then do the same for R-5." |
| 2. Match five questions | Q5 and Q9: they reach for LEFT because it feels safer, when the question is about refunded orders only. | "Read the question again and ask: does an order with no refund belong in the answer?" |
| 3. The refund rate | Q10: most see one fault. Those who see the lost orders miss W-3 doubling, and those who see W-3 miss the lost orders. Q11: the 15.3 percent distractor catches everyone who fixed only the ON clause. | "Run it with SELECT * in place of the sums, and read the rows before the totals." |
| 4. Q1 on the warehouse | The first query they write is `GROUP BY order_id HAVING COUNT(*) > 1`, which returns 234 Q1 orders, and some start writing a double-paid list from it. The second stall is the gap: Q1's gap is zero on every channel, and learners assume their query is broken. | "What makes a retry a retry, in columns?" For the zero gap: "Run the unpaid list. If it is empty, what must the gap be?" |

## The Q1 numbers, for the TA only

These are the numbers a correct problem 4 produces. Do not read them to the room; let each learner's
checks read true first.

| Channel | Q1 orders | Booked | Collected | Gap | Surplus posted twice |
|---|---|---|---|---|---|
| app | 192 | Rs 4,21,38,840 | Rs 4,21,38,840 | 0 | Rs 6,680 |
| store | 165 | Rs 1,99,59,110 | Rs 1,99,59,110 | 0 | Rs 6,630 |
| web | 181 | Rs 3,79,02,050 | Rs 3,79,02,050 | 0 | Rs 3,690 |
| All | 538 | Rs 10,00,00,000 | Rs 10,00,00,000 | 0 | Rs 17,000 |

Q1 has no unpaid orders and 22 retried instalments (all card, instalment 1, small orders). The feed
posted Rs 10,00,17,000 against Q1 orders, which is collected plus the Rs 17,000 surplus. The stretch
gives refunded Rs 51,94,760 on app, Rs 3,63,000 on store and Rs 35,09,520 on web, so collected net of
refunds is Rs 3,69,44,080, Rs 1,95,96,110 and Rs 3,43,92,530.

The zero gap is the lab's best moment. A learner who reports "Q1 was fully collected" with the
empty unpaid list and a gap-equals-unpaid check reading true has understood the day; a learner who
reports "fully collected" from the posted total, which runs Rs 17,000 above booked, has made the
morning's mistake in the other direction. Ask the room which of the two sentences they would sign.

## Checked

Every query in the lab and its solution was run against the v4 warehouse on PostgreSQL 16.13 on
29 Sep 2026, and the invented tables' counts and rates (4, 7, 5 and 8 rows; 16.3, 15.3 and 25.0
percent) were checked in the same session.

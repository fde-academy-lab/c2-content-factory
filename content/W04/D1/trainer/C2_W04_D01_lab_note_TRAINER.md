# How does the TA run Monday's practice lab on Kalpa Retail?

**TRAINER ONLY.** The lab re-runs the morning's method on Kalpa Retail, the programme's fictional
client: the first three rungs of the day's ladder (count by hand, compute on the full table, catch
the trap) in the lab notebook, the fifth (the decision) in the Kalpa set,
`exercises/unguided/C2_W04_D01_kalpa_north_star_STUDENT.md`, then the practice set. The totals of the
seven-member sheet and the planted values below stay with the TA until the room has counted them.

**Who needs the answer.** The TA, who runs the lab alone after the trainer's day and the faculty block
or the clinic.

**The questions on the way.** In what order does the lab run? What is on the seven-member sheet? What
should the room find, and what if nobody does? Where does each problem stall, and what is the one
hint? What does the TA say at the end?

---

## In what order does the lab run?

| Part | File | What the room does | About |
|---|---|---|---|
| 1 | `notebooks/C2_W04_D01_12_kalpa_lab_STUDENT.ipynb` | Reads the table, counts seven members by hand from the sheet below, predicts, then types the two your-turn cells | 40 minutes |
| 2 | `exercises/unguided/C2_W04_D01_kalpa_north_star_STUDENT.md` | Writes the growth plan's north star on the morning's seven lines; five letters | 25 minutes |
| 3 | `exercises/practice/C2_W04_D01_lab_set_STUDENT.md` | The Parsons problem, the lead-and-lag drill as its problem 2 (unless the room sat it in the metric clinic), a product definition, the nine-number dashboard; five letters | 45 minutes |
| 4 | The solutions, then the close | Walks the answers and hears the closing line below | 10 minutes |

Walk the notebook's two your-turn cells aloud once the room has typed them, before part 2. Open the
three solution files at the end: `exercises/solutions/C2_W04_D01_kalpa_north_star_solution_STUDENT.md`,
`exercises/solutions/C2_W04_D01_lead_lag_solution_STUDENT.md` and
`exercises/solutions/C2_W04_D01_lab_set_solution_STUDENT.md`. If the lab runs short, cut the lab set's
problem 4 first and then its problem 3, never the notebook's two your-turn cells. Kavya Nair, Kalpa's
senior analyst, is the voice of the lab's review: the baseline, the denominator, the evidence and a
second way.

---

## What is on the seven-member sheet?

Print the seven member rows below, without the totals row, and under them four blank lines the room
fills in: the two hand-counted ratios, the two ratios from the full table, the one sentence on what
became of the window's placements, and the line of a complete definition that would have stopped
"reorders per member" rising for that. Hand it out at the notebook's "What do seven members' rows say,
counted by hand?" step and collect it at the end; it is how the TA sees who found what.

The seven are real members of the 107 who were already in the tier when the comparison window
opened, each with placements in both windows, chosen so their hand count leans the way the full
table does while sitting at least 0.10 from each of its two ratios. Booked value counts every
placement, whatever happened to it.

| Member | Placements, 20 Aug to 9 Sep | Placements, 10 to 30 Sep | Booked value, 20 Aug to 9 Sep | Booked value, 10 to 30 Sep |
|---|---|---|---|---|
| C-0152 | 2 | 2 | Rs 6,690 | Rs 2,950 |
| C-0184 | 2 | 1 | Rs 7,620 | Rs 2,010 |
| C-0211 | 1 | 3 | Rs 1,970 | Rs 5,110 |
| C-0215 | 1 | 1 | Rs 1,940 | Rs 2,290 |
| C-0224 | 1 | 3 | Rs 3,790 | Rs 6,660 |
| C-0240 | 1 | 1 | Rs 4,350 | Rs 3,400 |
| C-0264 | 1 | 1 | Rs 3,490 | Rs 2,690 |
| The seven, for the TA only | 9 | 12 | Rs 29,850 | Rs 25,110 |

The hand count: placements per member 12 / 9 = 1.33 times; booked value per member 25,110 / 29,850
= 0.84 times. Both sit more than 0.10 from the full table's values, so the room still has a reason to
run the code. If the room asks why the two disagree: seven members are a sample chosen to show the
mechanism, as the morning's six drivers were, and the full table is the tier. Four of the seven have
an order in Kalpa's warehouse in the comparison window (C-0152, C-0184 and C-0224 delivered, C-0211
cancelled); each of their other placements merged into an open basket.

---

## What should the room find, and what if nobody does?

The per-member figures divide both windows by the same 107 members, the ones already in the tier
when the comparison window opened on 20 August, because a member who joined later had fewer of its
days to reorder in: one who joined on 25 August had 16 of its 21.

| What the room should find | Value | Where | The hint if nobody finds it |
|---|---|---|---|
| Reorders placed per member, window over comparison | 1.22 | First your-turn cell | "Count the window's placements and the comparison's for the 107 in `base`, each over 107. Which is bigger, and by how much?" |
| Booked value per member, window over comparison | 0.96 | First your-turn cell | "Now the rupees. Did the value per member rise with the count?" |
| What became of the window's placements | None became an order: each was an auto-reorder, cancelled, merged into a basket the member already had open or still pending, and none carries an `order_id` | Second your-turn cell | "Group the window's placements by `auto` and `status`, then count the ones with an `order_id`. How many became an order?" |

The prediction's answers on the full table are c for the count and a for the booked value; the
seven's hand count lands on c too, at exactly a third, and on a.

The counts behind the three: in the comparison window 7 of the 107's 36 placements became orders in
Kalpa's warehouse (4 delivered, 1 returned, 2 cancelled) and 29 merged into an open basket; in the
auto-reorder window the app placed all 44, of which 22 were cancelled, 16 merged and 6 are pending. A
placement in the window averages Rs 2,362 against Rs 3,008 in the comparison. The members' own
checkouts in the window are outside the table by design: the Week 2 warehouse,
`content/W02/D1/data/C2_W02_D01_warehouse_v4_STUDENT.sql`, holds 7 Retail-Plus app orders from 10 to
30 September, and none of them is in the log.

If someone asks whether the merged placements' items reached the member: the log cannot say. A
merged placement never became an order of its own, and its items reach the member only if the member
checks that basket out, which is the member's own order and outside this table. So a merged
auto-reorder adds one to the count without adding an order.

The one sentence each learner should say to a neighbour: "Reorders per member rose about a fifth
while the booked value per member fell, because the app placed reorders on its own that were worth
less on average, and none of them became an order."

---

## Where does each problem stall, and what is the one hint?

| Problem | Where learners stall | The one hint |
|---|---|---|
| The notebook's hand count | Taking each member's own ratio and averaging the seven, which gives 1.50 and 1.11 | "Add the seven first, then divide once, the way the morning added hours and trips." |
| The first your-turn cell | Leaving out `& reorders["customer_id"].isin(base)`, which prints 1.17 and 0.90 over all 120 members, or cutting the base on 20 August, which gives 108 members and 1.19 and 0.92 | "Who was already a member when the comparison window opened on 20 August?" |
| The Kalpa set, Q2 | Choosing customers with an order that same month as the denominator | "If a customer stops ordering, are they still in your denominator?" |
| The Kalpa set, Q3 | Choosing orders per member as the guardrail | "Option d counts the north star's own orders. Can a number guard itself?" |
| The lab set, problem 1 | Taking lines 5 and 6, the average of each driver-week's own rate | "Lines 5 and 6 print 1.71 after, against the city's 1.58. Which lines add every trip and every hour before dividing?" |
| The lab set, problem 2 (the lead-and-lag drill), Q3 | Giving the hours north star the guardrail "total peak online hours" | "What would that guardrail catch?" |
| The lab set, problem 3 | A numerator that counts activity the team can create on its own, such as sessions or notifications | "Could the team raise it without a customer receiving anything?" |
| The lab set, problem 4 | Calling city trips the north star | "If 140 new drivers join, does the city's total rise even when nobody drives more?" |

---

## What does the TA say at the end?

"On Uber the city paid for peak online hours, and a driver raised them by keeping the app open with
no rider. On Kalpa the proposed number was reorders placed, and the app raised it on its own. In
both, the lines that stop it are the numerator, which counts what the customer or the rider received,
with the exclusions and the line on what the number does not reward behind it, and the denominator
printed beside the rate." Then open the solutions.

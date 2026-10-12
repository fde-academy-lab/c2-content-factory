# How does the TA run Monday's practice lab on Kalpa Retail?

**TRAINER ONLY.** The lab re-runs the morning's method on Kalpa Retail, the programme's fictional
client: L1 to L3 in the lab notebook, L5 in the Kalpa set, then the practice set. The seven-member
sheet and the planted values below stay with the TA until the room has counted them.

**Who needs the answer.** The TA, who runs the lab alone after the trainer's day and the faculty block
or the clinic.

**The questions on the way.** In what order does the lab run? What is on the seven-member sheet? What
should the room find, and what if nobody does? Where does each problem stall, and what is the one
hint? What does the TA say at the end?

---

## In what order does the lab run?

| Part | File | What the room does |
|---|---|---|
| 1 | `notebooks/C2_W04_D01_04_kalpa_lab_STUDENT.ipynb` | Reads the table, counts seven members by hand from the sheet below, predicts, then types the two your-turn cells |
| 2 | `exercises/unguided/C2_W04_D01_kalpa_north_star_STUDENT.md` | Writes the growth plan's north star on the morning's seven lines; five letters |
| 3 | `exercises/unguided/C2_W04_D01_lead_lag_STUDENT.md` | Three letters, unless the room sat it in the metric clinic |
| 4 | `exercises/practice/C2_W04_D01_lab_set_STUDENT.md` | The Parsons problem, a product definition, the nine-number dashboard; five letters |

Open the solutions at the end of the lab, after walking the notebook's two your-turn cells aloud.
Kavya Nair, Kalpa's senior analyst, is the voice of the lab's review: the baseline, the denominator,
the evidence and a second way.

---

## What is on the seven-member sheet?

Hand this out at the notebook's "What do seven members' rows say, counted by hand?" step. The seven
are the first members whose placements rose and whose booked value fell; booked value counts every
placement, whatever happened to it.

| Member | Placements, 20 Aug to 9 Sep | Placements, 10 to 30 Sep | Booked value, 20 Aug to 9 Sep | Booked value, 10 to 30 Sep |
|---|---|---|---|---|
| RP-0002 | 4 | 6 | Rs 2,035 | Rs 1,914 |
| RP-0012 | 4 | 5 | Rs 1,648 | Rs 1,369 |
| RP-0014 | 3 | 4 | Rs 1,337 | Rs 1,097 |
| RP-0021 | 5 | 6 | Rs 2,021 | Rs 1,672 |
| RP-0023 | 4 | 6 | Rs 1,742 | Rs 1,606 |
| RP-0031 | 4 | 5 | Rs 1,532 | Rs 1,390 |
| RP-0040 | 2 | 3 | Rs 1,093 | Rs 1,045 |
| The seven | 26 | 35 | Rs 11,408 | Rs 10,093 |

The hand count: placements per member 35 / 26 = 1.35 times; booked value per member 10,093 / 11,408
= 0.88 times. Both sit at least 0.05 from the full table's values, so the room still has a reason to
run the code.

---

## What should the room find, and what if nobody does?

| What the room should find | Value | Where | The hint if nobody finds it |
|---|---|---|---|
| Reorders placed per member, window over comparison | 1.22 | First your-turn cell | "Count the window's placements and the comparison's, each over 120 members. Which is bigger, and by how much?" |
| Booked value per member, window over comparison | 0.96 | First your-turn cell | "Now the rupees. Did the value per member rise with the count?" |
| What became of the window's placements | None became a separate delivered order: each was an auto-reorder, cancelled, merged into a later order or still pending | Second your-turn cell | "Group the window's placements by `auto` and `status`. How many say delivered?" |

The one sentence each learner should say to a neighbour: "Reorders per member rose about a fifth
while the booked value per member fell, because the app placed low-value reorders on its own, and
none of them became an order a member received."

---

## Where does each problem stall, and what is the one hint?

| Problem | Where learners stall | The one hint |
|---|---|---|
| The notebook's hand count | Dividing by seven before taking the ratio, or taking each member's own ratio and averaging | "Add the seven first, then divide once, the way the morning added hours and trips." |
| The Kalpa set, Q2 | Choosing customers with an order that same month as the denominator | "If a customer stops ordering, are they still in your denominator?" |
| The Kalpa set, Q3 | Choosing orders per member as the guardrail | "Can a number guard itself?" |
| The lead-and-lag drill, Q3 | Giving the hours north star the guardrail "total peak online hours" | "What would that guardrail catch?" |
| The lab set, problem 1 | Taking lines 5 and 6, the average of each week's rate | "Which number did the morning say the average hides two-fifths of?" |
| The lab set, problem 3 | A numerator that counts activity the team can create on its own, such as sessions or notifications | "Could the team raise it without a customer receiving anything?" |
| The lab set, problem 4 | Calling city trips the north star | "If 140 new drivers join, does the city's total rise even when nobody drives more?" |

---

## What does the TA say at the end?

"On Uber the paid number was hours, and an open app raised it. On Kalpa the proposed number was
reorders placed, and the app raised it on its own. In both, the line that stops it is the numerator:
count what the customer or the rider received, and print the denominator beside it." Then open the
solutions.

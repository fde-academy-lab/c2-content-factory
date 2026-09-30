# Which answers hold in the escalated case on Meera's three questions, and why?

Answers: 1b 2c 3b 4a 5d 6c 7b 8a 9d 10b 11a 12c

Meera Raghavan, Kalpa Retail's CEO, asked three questions for Monday's growth review: is the fall in
Retail-Plus, Kalpa's paid membership tier, real or the usual wobble; should budget follow Student's
40 percent rise; and did the monsoon sale, 15 percent off in August, work, or did those customers
buy anyway? She wants one page she can read in two minutes, with "not yet" allowed. The escalated
case asks each learner to rebuild all three answers alone in fifty minutes in
`notebooks/C2_W01_D04_ex1_escalated_case_STUDENT.ipynb`, twelve lettered choices in five parts, and
to write the note. The executed solution, `C2_W01_D04_ex1_escalated_case_solution_STUDENT.ipynb` in
this folder, runs every key. Four of the twelve items are design items: 2, 6, 10 and 12.

**Who needs the answer.** You, before the debrief, checking your twelve letters and your note. The
debrief replays the room's wrong lines aloud, and a line you cannot defend here is the one Marketing
takes apart on Monday.

**The questions on the way.**

- Which idea does this case test?
- Which numbers should you have reached, part by part?
- Why is each key right, marker by marker?
- What does a model note say, in 190 words?
- Which wrong answers does the debrief replay?
- Where does this show up at work?

## Which idea does this case test?

The case tests every habit of the day at once, with no trainer choosing the step: a chance reference
that fits the way the data was collected, read in both directions; a fall sized in rupees against the
company and a fix's cost; a rate put beside its count; a campaign compared inside each segment, with
the mix named; a hold-back drawn from the list the sale runs on; and a note of four parts that says
"not yet" where the evidence does.

## Which numbers should you have reached, part by part?

| Part | Number | What it means |
|---|---|---|
| 1 | Rs 1,110 per member; each member's two quarters flipped 5,000 times, seed 2026: 145 flips make a fall that large (0.029) and 286 a move that large either way (0.057) | Borderline against chance, and modest: the question came after the fall was seen, so both directions go in the note |
| 2 | Rs 24,420 a quarter; 0.19 percent of the company's Q2 delivered revenue of Rs 1,28,64,680; a coin-chosen 11 of the 22 members offered at Rs 5,500, the two halves Rs 321 apart in Q1 | Worth watching, and not worth acting on alone; if the tier acts, a fair test comes first |
| 3 | Orders up 40 percent on a count the notebook never prints, from very few customers; coin flips make that rise in 0.397 of worlds | A lead, and "not yet" |
| 4 | Blended Rs 3,395 against Rs 3,200, up 6.1 percent; inside Retail-Plus and inside Retail-Core, exposed customers spent 3.0 percent less; half the exposed group is Retail-Plus against 40 percent of the rest | The blend rose because of who got the discount |
| 5 | 14 of the platform's 70 Retail-Plus customers held back; about Rs 4,200 forgone if Marketing's 6 percent were real | The price of knowing, sized on the list the sale runs on |

## Why is each key right, marker by marker?

### Q1. Which orders count as money Kalpa kept?

The notebook totals each Retail-Plus member's Q1 and Q2 and asks which orders count.

The key is b, `o["status"] == "delivered"`. Monday settled that delivered orders are the money Kalpa
kept.

- a, `o["status"] != "cancelled"`: keeps returned orders, whose money went back to the customer.
- c, `o["amount"] != ""`: keeps every order, cancelled ones included.
- d, `o["status"] in ("delivered", "returned")`: counts returns as sales.

### Q2. Which chance reference fits the same 22 members in both quarters?

A design item. The same 22 Retail-Plus members sit in both quarters.

The key is c, `flip_gaps(plus_q1, plus_q2, 5000, seed=2026)`. The same members were measured twice,
so the chance reference flips each member's own pair.

- a, `shuffle_gaps(plus_q1, plus_q2, 5000, seed=2026)`: pools the 44 totals as if they were 44
  different customers, which is the test for two groups of strangers.
- b, `flip_rises(len(plus_q1), 5000, seed=2026)`: deals orders by coin, the reference for a count of
  orders.
- d, `shuffle_gaps(plus_q1, plus_q1, 5000, seed=2026)`: shuffles Q1 against itself, so no gap can
  appear.

### Q3. Which count gives the share of a move that large in either direction?

The notebook has the 5,000 flipped gaps and the real gap of Rs 1,110, and asks for the share either
way.

The key is b, `sum(1 for g in gaps if abs(g) >= abs(plus_gap)) / len(gaps)`. A move that large either
way is a flip whose size, up or down, reaches the real gap: 286 of 5,000, 0.057.

- a, `sum(1 for g in gaps if g <= plus_gap) / len(gaps)`: counts every gap at or below the real one,
  which is nearly every world.
- c, `sum(1 for g in gaps if abs(g) <= abs(plus_gap)) / len(gaps)`: counts moves at most that large,
  the complement of the share.
- d, `2 * sum(1 for g in gaps if g >= plus_gap) / len(gaps)`: doubles the one-direction share, which
  lands near the count here (0.058) and is still an estimate where the count is exact.

### Q4. What is the segment's fall in rupees a quarter?

The gap is Rs 1,110 per member, and the notebook asks for the tier's fall in rupees.

The key is a, `plus_gap * len(plus_q1)`. A per-member gap times the 22 members who exist in both
quarters is the segment's fall, Rs 24,420.

- b, `plus_gap`: still per member.
- c, `plus_gap / len(plus_q1)`: divides a per-member figure again.
- d, `sum(plus_q1) - plus_gap * 100`: mixes a total with a gap.

### Q5. What is the fall measured against, for Meera?

The notebook asks what the Rs 24,420 is set against for the CEO.

The key is d, `company_q2`. Meera runs the company, so the fall is set against the company's quarter:
0.19 percent.

- a, `sum(plus_q1)`: the tier's own Q1, which is the head of Retail-Plus's view.
- b, `len(ORDERS)`: a count of orders, which cannot sit under rupees.
- c, `revenue("Retail-Core", "Q2")`: another segment.

### Q6. Who gets the first test of the Rs 500 offer?

A design item. The fall is borderline, the offer costs Rs 500 a member and must win back 45 percent
of the fall to pay for itself, and the notebook asks who gets it in the first test.

The key is c, `coin_half`. A coin makes the two halves alike before the offer, so any gap after it
belongs to the offer; here the halves start Rs 321 apart in Q1.

- a, `members`: spends Rs 11,000 and leaves nobody to compare with.
- b, `fell_most`: the members who fell most also spent most in Q1, so the halves start Rs 2,490 apart
  and drift back toward the average whatever the offer does.
- d, `members[:len(members) // 2]`: splits by customer id, which here puts the bigger Q1 spenders on
  one side, Rs 1,025 apart.

### Q7. How many orders stand behind Student's 40 percent, for the coin flips?

The coin flips need the count they deal, and the notebook never prints it.

The key is b, `sum(1 for o in ORDERS if o["segment"] == "Student")`. The coin flips deal every order
the rate stands on, both quarters together. The rule of thumb then asks how many customers placed
those orders, which the note reports in words.

- a, `orders_in("Student", "Q2")`: counts only Q2.
- c, `index_student`: the rate itself.
- d, `orders_in("Student", "Q2") - orders_in("Student", "Q1")`: the change between the quarters.

### Q8. Which chance reference fits a count of orders?

The notebook asks how often chance alone makes a 40 percent rise on Student's count.

The key is a, `flip_rises(student_n, 5000, seed=2026)`. A coin flip per order on Student's own count
is the chance reference for a count: 0.397.

- b, `flip_gaps([student_n], [0], 5000, seed=2026)`: treats the count as one member's two quarters.
- c, `flip_rises(400, 5000, seed=2026)`: deals 400 orders, the size chapter 3 invented for a large
  segment.
- d, `[0.4] * 5000`: assumes the answer.

### Q9. Which rows are the customers who got the discount?

The exposure table flags each customer on the platform's list as exposed or not.

The key is d, `r["exposed"] == "yes"`. The exposure flag records who got the discount.

- a, `r["campaign_id"] == ""`: picks the customers with no campaign, the opposite group.
- b, `r["segment"] == "Retail-Plus"`: picks a segment.
- c, `int(r["august_revenue"]) > 3200`: picks customers by what they spent, which is the outcome
  being measured.

### Q10. Which comparison is fair when Marketing reads it first?

A design item. The blend shows 6.1 percent more for the exposed group, and the notebook asks which
comparison Marketing should read first.

The key is b, `{s: avg(s, "yes") / avg(s, "no") - 1 for s in ["Retail-Plus", "Retail-Core"]}`. The
fair comparison runs inside each segment, exposed against unexposed customers of the same kind: 3.0
percent less in both.

- a, `{s: avg(s, "yes") / blend_no - 1 for s in ["Retail-Plus", "Retail-Core"]}`: sets each segment's
  exposed against every unexposed customer, the comparison Marketing makes in the second case.
- c, `{"everyone": blend_lift}`: the blend again.
- d, `{s: avg(s, "yes") / avg("Retail-Plus", "no") - 1 for s in ["Retail-Plus", "Retail-Core"]}`: sets
  Retail-Core's exposed against Retail-Plus's unexposed.

### Q11. What share of the exposed customers are Retail-Plus members?

The notebook asks for the mix of the group who got the sale.

The key is a, `count("yes", "Retail-Plus") / count("yes")`. Retail-Plus members over all exposed
customers is the mix of the exposed group: half, against 40 percent of the rest.

- b, `count("no", "Retail-Plus") / count("no")`: the unexposed group's mix.
- c, `count("yes", "Retail-Plus") / len(EXPOSURE)`: divides by every customer on the list.
- d, `count("yes") / len(EXPOSURE)`: the exposed share of the list.

### Q12. How many Retail-Plus customers does the Diwali coin hold back?

A design item. A coin keeps one in five out of the Diwali sale inside each segment, and the notebook
holds Finance's 22 members and the platform's list side by side.

The key is c, `len(platform_plus) // 5`. The sale runs on the platform's list, so the hold-back is
one in five of its 70 Retail-Plus customers, exposed last time or not: 14, forgoing about Rs 4,200 at
Marketing's 6 percent.

- a, `len(finance_members) // 5`: takes Finance's members, a different list with different ids.
- b, `len(platform_plus_exposed) // 5`: samples only the customers Marketing picked last time.
- d, `len(EXPOSURE) // 5`: takes both segments at once, so Retail-Plus's slice is no longer one in
  five.

## What does a model note say, in 190 words?

**Claim.** Retail-Plus is down by a borderline amount and small against the company; Student is too
thin to fund yet; the monsoon sale did not work as designed.

**Evidence.** Retail-Plus members delivered Rs 1,110 less each in Q2; if nothing had changed, a fall
that large turns up in about 3 of 100 flips, and a move that large either way in about 6. It is Rs
24,420 a quarter, 0.19 percent of delivered revenue. Student's 40 percent rise comes from very few
customers, and coin flips make it in four worlds of ten. The sale's 6 percent is a blend: inside
Retail-Plus and Retail-Core, exposed customers spent 3 percent less.

**Caveat.** We asked after seeing the fall. The group who got the sale was half Retail-Plus against
40 percent of the rest, and Retail-Plus spends more anyway; the platform's list gives one August
figure per group, so we cannot see the spread.

**Action.** Watch Retail-Plus, and if we act, test the offer on a coin-chosen half; watch Student until
more customers buy, thirty or more; do not repeat the sale as designed, and hold back a random slice
of each segment at Diwali.

## Which wrong answers does the debrief replay?

| Wrong answer | Where it comes from | The fix |
|---|---|---|
| "The discount worked: revenue rose 6 percent." | The blend, trusted without a split | Compare inside each segment and state the mix |
| "A 3 percent chance we are wrong about Retail-Plus." | The share read as the chance of error | "If nothing had changed, a fall this large turns up in about 3 of 100 flips, and a move that large either way in about 6" |
| "Retail-Plus is real: fund the offer for the whole tier." | A borderline share read as a verdict, and the rupees left out | Rs 24,420 a quarter, 0.19 percent of the company, and a coin-chosen half first |
| "Move budget to Student, the fastest-growing segment." | The rate repeated without its count | The count beside the rate, and "not yet, until more customers buy" |
| A hold-back of 4 drawn from Finance's 22 members | The retention offer's list used for the sale | The sale runs on the platform's list, so the coin holds back 14 of its 70 |
| A note with no caveat | The habit of stopping at the claim | "This changes if ___; we will know by ___" |

## Where does this show up at work?

The three are the questions a growth review asks of any metric: did it really move, does a fast
riser have enough behind it, and did a campaign earn its lift. Each is also on the day's interview
list, where a strong answer carries the count, the chance and the fair comparison beside each number
and ends on what the business should do next.

# What does each group's checkpoint answer sound like when it is strong or weak, and what does the trainer ask next?

**TRAINER ONLY.** It goes with `checkpoints/C2_W03_D03_checkpoint_questions_STUDENT.md`, which the
room sees, and it names every plant in the Kalpa Health data with its witness number, so it never
reaches a learner. The checkpoint takes the first 30 minutes of the morning block. Every number
below was computed from `content/W03/D1/data/` the way a group would compute it (the old export at
one row per booking id, amounts converted after the dollar sign is removed) by
`internal/C2_W03_D03_numbers_INTERNAL.py`, which checks each against the generator's witness, the
spine (`docs/detailing/W03_build1_spine.md`) or Monday's day sheet. The visit register is the one
drawn from the bookings on 1 October 2026.

## How does the trainer run the thirty minutes?

**Who needs the answer.** The trainer, who has nine groups and 30 minutes, and the Academic TA, who
takes the stuck groups first in the open build time.

**The questions on the way.** In what order do groups answer? What does the trainer listen for?
What is written down? What is never said?

1. **The order.** Take groups by brief, 1 to 5, so the groups that share a brief answer back to back
   and the room hears one question answered two or three ways.
2. **Two minutes per group, by the clock.** One member per question, a different member each time.
   Stop a group at two minutes, mid-sentence if need be, and write "unfinished" against the
   question it was on.
3. **Listen for three things only:** a number, the file it came from, and what the group counted as
   one row or one record. The follow-up is one sentence, said once, and then the next group starts.
4. **Write each group on one line** in the grid at the end of this guide: on track, slow or stuck,
   and the question it could not answer. The line feeds the catch-up plan,
   `checkpoints/C2_W03_D03_catchup_plan_TRAINER.md`, and the Academic TA's first round.
5. **The minutes left after the last group** go to the stuck groups' blockers, one sentence each, so
   the trainer and the TA know where to sit first.

**Never, at the checkpoint:** confirm or deny a number against this guide, name a plant, or tell one
group what another found. "That is a number worth reaching a second way" is as close to a verdict as
the trainer goes. A group's strong answer is never praised to the room, since another group on the
same brief is listening.

**A number stranger than any below** usually means rows were counted as records, or text was summed
as numbers. Ask for the row count and the distinct-id count, and move on.

## Brief 1, revenue: what does each answer sound like, and what comes next?

**Who needs the answer.** The finance head, and the revenue groups, who state at the close which
branch of billed revenue is short; the plants behind this brief are the employer contract, the
panel billed as one claim line, the 60 dollar-text amounts, and, for every group, how Dr Menon's
dashboard counts its 5 percent.

**The questions on the way.** What did the claims hold? What were they matched to? What is each
branch counted over?

| The question, and its move | A strong answer sounds like | Then ask | A weak answer sounds like | Then ask |
|---|---|---|---|---|
| 1. What did the claims hold? Week 1 Wednesday, profile | 11,356 rows and 11,356 distinct claim ids; `billed_amount` converts as written on 11,296 rows and is dollar text such as "$265.00" on 60; amounts run from $25 to $180,000, and the largest is one claim billed to an employer account, KH-CLM-007802, EMP-0007, Dallas, 6 August, with the next largest $420 | "What does that one claim do to your Q3 mean?" ($210.50 with it, $179.75 without; the median is $150 in both quarters.) | A total with no word on conversion: $2,190,540, which is $10,559 short of the true $2,201,099 because 60 amounts were coerced to blanks; or no largest value at all | "What does your code do with an amount it cannot read, and how many did it do that to?" |
| 2. What were the claims matched to? Week 1 Wednesday, reconcile; Week 2 Tuesday, the join counted first | Claims against completed bookings in both booking files: the old export's 11,213 completed bookings (one row per id) match 11,213 claims, the new system's 143 completed bookings match the other 143, and no cancelled booking has a claim; 11,356 = 11,213 + 143 | "Which quarter do the 143 fall in, and does your tree count them?" (All in Q3.) | "Every claim matched", from a group that read only the old export, or 143 claims written off as bad data | "Read aloud the booking id on one claim you could not match." |
| 3. What is each branch counted over? Week 1 Monday, the tree, and the typical value | Claims 5,508 in Q2 and 5,848 in Q3; billed $970,098 and $1,231,001, up 26.9 percent, or 8.3 percent without the employer claim; mean claim $176.13 and $210.50, medians $150 and $150; and a claim line can stand for several tests: the 22,152 retail claim lines bill 46,867 tests on completed bookings | "Which of your branches is in tests, which in claims and which in dollars, and which one is Dr Menon's 5 percent counted in?" | Revenue per test computed as billed dollars over `line_items`, or a Q3 mean quoted alone, $210.50 | "Put the median beside your Q3 mean. What pulls them apart?" |

**For every group, Dr Menon's 5 percent.** A revenue group that tries to rebuild her 5 percent from
the files is doing the right thing. Ask, "What does her dashboard count, and from which file?", and
leave it there. The answer stays in the day sheet's plant table: 5.1 percent on the dashboard's
count, 7.8 in tests booked across both systems, 8.6 in tests performed and 5.6 in bookings, every
reading without the employer contract short of 18.

## Brief 2, bookings: what does each answer sound like, and what comes next?

**Who needs the answer.** The operations head, and the bookings groups, whose claim decides whether a
field team goes to two metros; the plants behind this brief are Chicago and Philadelphia's move to
the new booking system on 18 September, the old export's repeated rows and the new system's
month-first dates.

**The questions on the way.** What did each booking file hold? What was the fall checked against?
What is one booking?

| The question, and its move | A strong answer sounds like | Then ask | A weak answer sounds like | Then ask |
|---|---|---|---|---|
| 1. What did each booking file hold? Week 1 Wednesday, profile, rows against ids | Two files. The old export: 11,729 rows over 11,549 distinct booking ids, six metros, 1 April to 30 September 2026. The new system's export: 153 rows, Chicago 85 and Philadelphia 68, with its own ids, site codes and channel and status codes, dated 09/18/2026 to 09/30/2026, month first | "Which of the old export's ids appear twice, and over which dates?" (180 ids, booked 1 June to 26 September.) | One file opened, or the old export's 11,729 rows quoted as bookings | "Which file holds a Chicago booking made in the last two weeks of September?" |
| 2. What was the fall checked against? Week 1 Tuesday, rung 1, confirm before explaining | Q3 claims against the old export's Q3 completed bookings, metro by metro: four metros match exactly, and Chicago has 79 more claims than completed bookings and Philadelphia 64, which are the new system's 143 completed bookings | "So how far did the two metros really fall, counted in both files?" | Bookings compared with nothing, or the gap explained as wrong claims | "Put Q3 completed bookings beside Q3 claims, metro by metro. Where do they part?" |
| 3. What is one booking in the count? Week 1 Tuesday, rung 2, like with like | Q2: 1,415 bookings in the two metros. Q3: 1,090 in the old export alone, down 23.0 percent, and 1,243 across both files, down 12.2 percent (Chicago 754 to 656, down 13.0; Philadelphia 661 to 587, down 11.2). One booking is one booking id after the identity rule, and the one employer booking is left out | "Is a fall of 12.2 percent still a reason to send a field team, and what would you look at next?" | The 23.0 percent fall stated as the finding, or 1,450 and 1,099, the two metros' rows before the identity rule | "Which bookings in those two metros would the old export not hold?" |

The other four metros' retail bookings grow from Q2 to Q3: Dallas 7.7, Phoenix 13.0, New York 6.8
and Atlanta 21.2 percent. A group that forces a day-first format on the new system's dates gets an
error on every row, since every day in them is past the twelfth; ask it to read one date aloud.

## Brief 3, billing: what does each answer sound like, and what comes next?

**Who needs the answer.** The finance head, and the billing groups, whose figure the board sees at
the quarter's close; the plants behind this brief are the three shapes the posting system writes a claim in, the
double posts from repeated ERA loads, the unpaid employer claim and the denials posted with nothing
paid.

**The questions on the way.** What is one row of each file? What did the join match? Which postings
are money received?

| The question, and its move | A strong answer sounds like | Then ask | A weak answer sounds like | Then ask |
|---|---|---|---|---|
| 1. What did the two files hold? Week 1 Wednesday, profile | Claims: 11,356 rows, one per claim. Remittances: 11,343 rows, one per posting: 10,101 payments, 1,137 denials and 105 reversals, so a claim can carry several postings. `claim_ref` takes three shapes: 8,858 bare digits such as 000002, 2,269 CLM-numbers such as CLM-1, and 216 full claim ids | "Write the rule that turns each shape into a claim id, in one sentence." | "The references look like claim ids", with no count by shape | "Show me five `claim_ref` values beside five `claim_id` values." |
| 2. What did the join match? Week 2 Tuesday, the join counted first | An exact join matches 216 postings, 1.9 percent. After one rule maps every shape to the six-digit serial, all 11,343 match. Going the other way, 398 claims have no posting, $253,165 billed, the $180,000 employer claim among them, spread across all six months (59 in April to 76 in September) | "Of the 398, which would you have the revenue-cycle team chase first, and why?" | "Only 2 percent of claims are paid", or a fuzzy match with no stated rule | "Put one claim id beside a posting you believe belongs to it. What rule turns one into the other?" |
| 3. Which postings are money received? Week 2 Tuesday, booked against collected | Money received is the payment postings, less repeats of the same reference and amount, net of reversals: 280 double posts worth $19,204.63 come out and reversals take back $8,662.87, leaving $801,313.56 paid against $2,201,099 billed, 36.4 percent. Denials post with nothing paid: 1,137 postings; 1,175 retail claims are marked denied, 10.4 percent, billing $230,132 | "How much of the $1,399,785 between billed and paid is the contract, and how much is money still owed?" (Rounded: $883,255 of contractual adjustments, $253,165 on claims with no posting, $222,108 on claims denied with a posting, $32,595 of patient shares and $8,663 of reversals.) | The paid column summed as it stands, $820,518.19, or double posts counted as money | "Group the payments by reference and amount. What does a count of two mean?" |

## Brief 4, no-shows: what does each answer sound like, and what comes next?

**Who needs the answer.** The operations head, and the no-show groups, whose claim decides whether
KH-ATL-03 gets a receptionist or a closure notice; the plant behind this brief is that KH-ATL-03
runs by appointment, while the other centres' visit counts include walk-ins, who cannot miss a slot.

**The questions on the way.** What did the register hold? What was it checked against? What is each
rate out of?

| The question, and its move | A strong answer sounds like | Then ask | A weak answer sounds like | Then ask |
|---|---|---|---|---|
| 1. What did the register hold? Week 1 Wednesday, profile | 3,685 rows, Q3 only, at the twelve patient service centres; the laboratories keep no register. Eleven centres hold 173 to 504 rows each and KH-ATL-03 holds 80. `kind` is scheduled on 1,964 rows and walk-in on 1,721; `attended` is Y on 3,385 and N on 300, and no walk-in is marked N | "Split `kind` by centre. What does KH-ATL-03's split look like?" (79 scheduled, 1 walk-in.) | A rate per centre with no row counts beside it | "How many visits sit behind each centre's rate?" |
| 2. What was the register checked against? Week 1 Wednesday, reconcile both ways | Every one of the 3,685 rows names a booking at the same centre in one of the two booking files. They belong to 3,432 bookings, 253 of which have two rows, a missed slot and then the kept visit on the booking's date; 3,385 completed bookings each have one kept visit, and 47 cancelled bookings each have one missed slot. Of the 3,483 Q3 bookings at the centres that were not home collections, 51 have no row: 43 cancelled walk-ins and 8 completed bookings with a blank channel | "Does a rebooked patient count once or twice in your denominator, and why?" | A mismatch against the bookings treated as a defect, or no check at all | "Does every booking id in the register appear in a booking file, and at the same centre?" |
| 3. What is each rate out of? Week 1 Thursday, the count beside the rate, real or noise | On all visits: 15 of 80, 18.8 percent, against 285 of 3,605, 7.9 percent. On scheduled visits only: 15 of 79, 19.0 percent, against 285 of 1,885, 15.1 percent, with the next worst centre at 18.5. Walk-ins cannot miss a slot, so they leave the denominator, and on 79 slots at 15.1 percent a gap this size or larger turns up by chance with probability about 0.21 | "Counted per booking instead of per slot, does your answer change?" (15 of 64 scheduled bookings missed a slot, against 17.3 percent elsewhere; chance gives that with probability 0.13.) | "Twice as bad", from 18.8 against 7.9, or a chance check run on all visits that returns 0.0014 and reads as real | "Which visits in your denominator could never have been a no-show?" |

## Brief 5, the campaign: what does each answer sound like, and what comes next?

**Who needs the answer.** The marketing head and Dr Menon, and the campaign groups, whose claim
decides whether the offer goes to every patient; the plant behind this brief is the targeting: the
offer went at random to half the patients in three metros already rising and to a fifth elsewhere,
and inside those three metros an offered patient booked less while the offer ran.

**The questions on the way.** Who got the offer? Did every offered patient match the register? What
is the 9 percent counted over?

| The question, and its move | A strong answer sounds like | Then ask | A weak answer sounds like | Then ask |
|---|---|---|---|---|
| 1. Who got the offer? Week 1 Thursday, who got the sale | 2,381 patients offered between 15 July and 4 August 2026: Dallas 619, Phoenix 607, Atlanta 416, New York 316, Chicago 215 and Philadelphia 208; 948 accepted | "Put offers per metro beside patients per metro. What share of each metro got it?" (50.5 percent in Dallas, Atlanta and Phoenix together, 21.4 percent elsewhere.) | Take-up quoted with no split by metro | "Who got the offer, metro by metro?" |
| 2. Did every offered patient match? Week 1 Wednesday, reconcile; Week 2 Tuesday, the join counted | All 2,381 are in the patient register, each in the same metro; 971 have a booking in the old export between 15 July and 14 September, and 1,716 have one at any time; patients with no booking in the window stay in the denominator at zero | "Does 'accepted' mean the patient used the offer? What in the files would show it?" (At least 259 of the 948 show a home collection between their offer and 14 September; 689 show none.) | "We joined and it worked", with no counts, or patients with no booking dropped from the denominator | "How many offered patients have no booking in the weeks the offer ran, and are they in your denominator?" |
| 3. What is the 9 percent counted over? Week 1 Thursday, cause or coincidence | Bookings per patient from 15 July to 14 September: 0.633 for the offered (1,507 bookings over 2,381 patients) against 0.581 for the rest (2,508 over 4,319), 9.0 percent more. Inside each of Dallas, Atlanta and Phoenix the offered booked less: down 10.8, 19.9 and 13.0 percent. Before the offer the two groups booked within about 6 percent of each other there, and those metros were already rising 6.9 percent in the two months before | "Run the same comparison in the three metros outside the campaign. What do you see, and could chance make it?" | 9 percent restated with no split by metro, or "the campaign worked" | "Run the same comparison inside one metro." |

**The offer outside the three metros.** The campaign file also carries offers in New York, Chicago
and Philadelphia, to a fifth of the patients at random. In New York the offered patients out-book
the rest by 23.5 percent, a chance draw that a permutation test puts at p of about 0.03 (two-sided,
10,000 shuffles); Chicago shows minus 4.8 and Philadelphia plus 0.6. A group that reads New York as
proof that the offer works has met a false positive: ask whether the other two metros outside the
campaign show the same gap, and do not settle it at the checkpoint.

## What does the trainer write down, and who goes to the catch-up plan?

**Who needs the answer.** The Academic TA, who reads this grid before the open build time, and the
Programme Head, who hears about any group that is stuck twice.

**The questions on the way.** What goes on each group's line? Which groups go to the catch-up plan?

```
Group   Brief   Q1   Q2   Q3   Status (on track / slow / stuck)   Blocker, in the group's words
```

A group marked stuck on two or more of its three questions goes to the catch-up plan today, and so
does any group that names a blocker at the close. A group stuck on one question gets the trainer at
its table first in the morning's build time.

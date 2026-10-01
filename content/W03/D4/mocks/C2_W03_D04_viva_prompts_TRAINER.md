# Which questions climb Mock R1's viva from what each group did, to why, to what would change its call?

**TRAINER ONLY.** This is the assessors' file, so every plant in the Kalpa Health data is written
here with its witness number. None of it is said to a learner, hinted at, or confirmed when a learner
guesses. A learner who asks "is there something hidden in the data?" gets the question back: "What
would you check?"

**Who needs the answer.** The three assessors, who each run about twelve eight-minute vivas on
Thursday 22 October, on the groups they hear all day: the Programme Head G1, G4 and G7, the Academic
TA G2, G5 and G8, and the Principal Advisor G3, G6 and G9. The viva scores 15 of the mock's 30
marks, and a probe that names what the data holds hands the learner the answer it was meant to
test.

**The questions on the way.** How do the eight minutes run, and which criterion does each probe
evidence? What does every learner meet first? What does Dr Menon's 5 percent count? Then, for each of
the five sub-problems: what the asker wants, what a finished answer reaches and what is planted; what
the group did; why it chose that way; and what would change its call. Last, what each learner would do
differently.

The setting, so this page stands alone: Kalpa Health is a US diagnostics business with a laboratory
and two patient service centres, where a phlebotomist draws patients' blood, in each of six US metro
areas: Dallas, Phoenix, New York, Chicago, Atlanta and Philadelphia. It bills each patient's payer in
dollars, a commercial plan, Medicare, Medicaid or the patient (self-pay); a claim is the bill, and a
remittance is the payer's answer, which the posting system records as postings. Its COO, Dr Priya
Menon, sees test volumes up 5 percent from Q2 (April to June 2026) to Q3 (July to September 2026)
against a plan of 18, and five of her heads each asked one question. Every group answers one of them
from ten files exported on Friday 16 October 2026, and on Wednesday each group stated a headline
claim with its denominators and its caveat. Every number below is recomputed from those files by
`internal/C2_W03_D04_numbers_INTERNAL.py`, and the spine, `docs/detailing/W03_build1_spine.md`,
carries the same plants.

---

## How do the eight minutes run, and which criterion does each probe evidence?

**Who needs the answer.** Each assessor, before the first viva: the five probes come in a fixed
order, and each one is the evidence for one row of the rubric.

**The questions on the way.** Which probes, for how long? Which probe does each seat take? When do
you ask to see the work? What do you listen for in every answer?

The viva climbs in three steps, the way an interviewer moves from a candidate's work to their
judgement: what the group did, why it did it that way rather than another, and what would change its
call.

| Minutes | The probe | The step it climbs | Where it comes from | The criterion it evidences |
|---|---|---|---|---|
| 1.5 | The opener, the same for every learner | What you did | The row's interview angle | The translation, with one decision defended by evidence (6) |
| 1.5 | The translation probe for the group's sub-problem | What you did, and which Week 1 or 2 move it carried | The row's thinking column | The translation, with one decision defended by evidence (6) |
| 2 | One of four plant probes, chosen by seat | Why that way | The spine's plant table | The translation, with one decision defended by evidence (6) |
| 2 | The caveat challenge, pushed as the asker | What would change your call | The group's headline claim from Wednesday | Defending a caveat under challenge (6) |
| 1 | The looking-back probe | What you would do differently | The group's challenges log and decisions log | What they would do differently (3) |

The rubric, rendered from `data/programme/facts.yaml`:

<!-- sync:rubric:W03/mock -->
**Mock interview R1, 30 marks.** Each learner is scored alone, 15 marks on the technical half and 15 on the project viva.

| Half | Criterion | Marks |
|---|---|---|
| Technical | Correctness | 8 |
| Technical | Reasoning aloud with numbers | 4 |
| Technical | Handling a follow-up | 3 |
| Project viva | The translation, with one decision defended by evidence | 6 |
| Project viva | Defending a caveat under challenge | 6 |
| Project viva | What they would do differently | 3 |
<!-- /sync:rubric:W03/mock -->

### Which probe does each seat take?

Each sub-problem carries four plant probes, P1 to P4, rotated by seat so that group-mates meet
different ones. Seat 1 takes P1, seat 2 takes P2, seat 3 takes P3 and seat 4 takes P4; the roster
prints each seat's probe beside its set letter. The opener, the translation probe, the caveat
challenge and the looking-back probe stay the same for every learner, because a learner's own words
are what they test, and group-mates' answers to them should differ. A learner racing through can
take the headline probe, H, as a second "why" probe.

### When do you ask to see the work?

At least once in every viva. The learner has the group's notebook or SQL, the decisions log and the
challenges log open. Ask for the cell or the log line behind one number. A learner who finds it in under a
minute built it or read it closely; a learner who searches and cannot find it carried it.

### What do you listen for in every answer?

Each probe below gives three columns: what a learner who did the work says, with the number, the
unit and the check; what a learner who carried it, presenting a group-mate's work, says, which is
usually the right headline without the mechanism; and the follow-up that tells them apart, because
it moves the case one step past the headline. The expected answer to a follow-up is in brackets
after it. Note a carried answer as it happened; never
argue with the learner in the room, and never correct a number.

---

## What does every learner meet first?

**Who needs the answer.** The assessor opening every viva the same way, so that the learner's own
choice of what to defend is the first evidence.

**The questions on the way.** What is the opener? What does a learner who did the work say first?

**`[S]` "Walk me through the analysis you did on unfamiliar data and one decision you would
defend."** This is the row's interview angle for the day.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Starts from the asker's question and the decision it feeds, names the files the group profiled and what surprised it, gives one decision from the decisions log with its count or dollars and its reason, and says what would change it | Starts from the tool or the chart, gives the group's headline, and names a decision in general words, such as "we cleaned the data" or "we removed duplicates" | "What was the alternative to that decision, and what number would have come out if you had taken it?" |

---

## What does Dr Menon's 5 percent count, and which number does each group put beside it?

**Who needs the answer.** The assessor of any group, since every group started from Dr Menon's 5
percent, and confirming a number before explaining it is the Week 1 Tuesday move.

**The questions on the way.** What is planted in the headline? What does the probe ask? What separates
the answers?

**What is planted.** Dr Menon's 5 percent is her dashboard's count: tests booked in the old booking
system only, one row per booking id, with a panel counted as its component tests. Computed from the
files, that is 23,213 tests in Q2 and 24,406 in Q3, 5.1 percent; on raw rows, with the old export's
repeated rows still in, the same reading is 23,788 to 24,556, 3.2 percent. Across both booking
systems, tests booked grew 7.8 percent (23,213 to 25,022), tests performed on completed bookings grew
8.6 percent (22,468 to 24,399) and bookings grew 5.6 percent (5,692 to 6,009). All four leave out the
employer contract, whose 1,200 wellness screenings of five tests each add 6,000 tests to Q3; with it
in, tests booked would grow 33.6 percent. Every reading without the contract is short of the plan of
18.

**H. "Dr Menon's dashboard says 5 percent. What is your group's number for growth, and what did you
count?"** The move: Week 1 Monday, which total, and what each total counts.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Names the unit, tests booked, tests performed or bookings, says both booking systems are in it, says the employer contract is out or shown apart, and places the number against the plan of 18 | Quotes the group's percentage without its unit, or says the dashboard is wrong without saying what it counted | "Which of your numbers moves most if the employer contract goes back in, and why is that a reason to show it apart?" (Tests booked, from 7.8 to 33.6 percent, because one employer's 6,000 tests would then describe the growth of the whole business.) |

---

## Sub-problem 1: which branch of Kalpa Health's billed revenue is short of the plan, and by how much?

**Who needs the answer.** The finance head, who writes the board's page on where the plan's growth
went, and Dr Menon, who moves the second half's recovery effort onto the branch the group names. A
branch named wrongly sends staff and money where nothing was short.

**The questions on the way.** What did the finance head ask, and what does a finished answer reach?
What did the group do? Why that way? What would change its call?

### What did the finance head ask, and what does a finished answer reach?

> "The board will ask me where the plan's growth went. Where does our lab revenue actually come
> from, and which branch of it is short?"
> The finance head, Kalpa Health, in brief 1

**What is planted.** One employer wellness contract in Q3, and panels billed as one claim line. Claim
KH-CLM-007802, on employer account EMP-0007, Dallas, service date 6 August 2026, bills $180,000 for
1,200 screenings: 14.6 percent of Q3's billed charges of $1,231,001. Billed charges grow 26.9 percent
from Q2's $970,098 with it, ahead of the plan, and 8.3 percent without it, to $1,051,001. The Q3 mean
claim is $210.50 with it and $179.75 without; the median is $150 in both quarters, and Q2's mean is
$176.13. Panels bill as one line: outside the contract, 22,152 claim lines, 21,050 of them tests or
panels and 1,102 a $20 fee for a collection at home, bill 46,867 tests on the completed bookings
behind them (48,235 counting cancelled bookings, which the booking-tests file also lists); in Q3
alone, 11,395 claim lines bill 24,399 tests. Sixty billed amounts are text with a dollar sign, such as
"$265.00": 32 in Q2 worth $5,390 and 28 in Q3 worth $5,169.

**What a finished answer reaches.** Outside the contract, billed charges grew 8.3 percent against a
plan of 18, which leaves Q3 $93,715 short of $1,144,716. Chicago and Philadelphia carry $63,436 of
that shortfall, about two thirds: Chicago's billed charges fell 6.5 percent ($124,097 to $115,997)
and Philadelphia's 10.9 percent ($114,014 to $101,538), while Atlanta finished $11,156 ahead of its
share of the plan. No payer stands out, since each payer type carries between $16,044 and $28,437 of
the shortfall. A strong group also says Q3 has 92 days to Q2's 91.

### What did the group do, and which Week 1 or 2 move did it carry?

The translation probe, from the row's "why this tree for a lab". The move: Week 1 Monday, the revenue
tree, every branch a count over a denominator.

**"Walk me down your revenue tree for Kalpa Health, and tell me where it differs from the one you
drew for Meera."**

| Did the work | Carried it | The follow-up |
|---|---|---|
| Patients, times bookings per patient, times tests or claim lines per booking, times billed dollars per line, or claims times the mean claim, with the payer as a split, a panel as one priced line covering several tests, the home-collection fee as its own line, and the employer account as a branch of its own; says retail's "items per order" breaks on a panel | Recites Meera's tree with lab words swapped in, and cannot say where a panel or the employer account sits | "A whole-body wellness panel is one claim line at $299 with twelve tests behind it, whose list prices add to $785. Which leaf of your tree counts it, and what does counting it as one test do to your price per test?" (It inflates price per test and hides volume: one line, twelve tests.) |

### Why did the group choose that way? The seat's probe, P1 to P4

**P1, seat 1. "What is a typical claim in Q3, and what sits behind the average?"** The move: Week 1
Monday, the typical value one large record cannot move.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Median $150, mean $210.50; sorted the claims and found one claim of $180,000 on an employer account, 14.6 percent of Q3's billed charges; mean $179.75 without it; kept it and reported it as its own branch | Gives $210.50 as typical, or says "we removed an outlier" | "Would you take that claim out of the revenue Dr Menon sees?" (No: it is real billed revenue, so it stays, on its own line, and the posting system shows nothing paid on it yet.) |

**P2, seat 2. "Dr Menon counts test volume. How many tests stand behind Q3's claims, and how did you
count them?"** The move: Week 1 Monday, which total, and what each total counts.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Counted tests from the booking-tests file, the test and component lines, on completed bookings: 24,399 in Q3 against 11,395 claim lines outside the contract, some of them home-collection fees, which are no test at all | Counts claim lines or claims as tests | "Why do claim lines and tests disagree, and which is Dr Menon's volume?" (A panel is one line and several tests, and a fee line is no test; volume is tests.) |

**P3, seat 3. "Which branch of the business is short, in dollars, and over which window?"** The move:
Week 1 Tuesday, which segment moved.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Outside the contract, billed charges grew 8.3 percent, $93,715 short of the plan; Chicago and Philadelphia carry $63,436 of it, falling 6.5 and 10.9 percent while the other four metros grew; no payer stands out; says Q2 has 91 days and Q3 92 | Says "revenue grew 26.9 percent", the total with the contract, or names a branch with no number | "If you give Dr Menon one number for the branch that is short, what is it, and what is it out of?" (About two thirds of the $93,715 shortfall, in Chicago and Philadelphia.) |

**P4, seat 4. "Some billed amounts would not read as numbers. What did you do with them?"** The move:
Week 1 Wednesday, profile before you count, and every value converted with a logged rule.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Found 60 amounts written as text with a dollar sign, such as "$265.00", stripped the sign, logged the rule with its count, and checked the billed total before and after | "We cleaned the amount column" | "How many dollars would have gone missing if those rows had been read as empty?" ($5,169 of Q3's billed charges and $5,390 of Q2's; a learner who did it computes it in the notebook.) |

### What would change the group's call? The caveat challenge

The move: Week 1 Friday, the note that holds when someone pushes. Ask for the group's headline claim
and its caveat, then push as the finance head. If the group's caveat is the one below, use this push;
if it is another, push on the one they gave in the same spirit.

**"Your caveat says the $180,000 employer claim distorts the averages. It is revenue. Why should I
not count it?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| Keeps it in billed revenue and shows it apart: one claim is 14.6 percent of Q3, so any average or growth rate with it inside describes one employer; the caveat is about which number describes the retail business, and no revenue is removed | Removes the contract, or drops the caveat under the push | "Would your answer change if the contract renews every quarter?" (It becomes a branch with its own plan line; the retail tree still reads without it.) |

---

## Sub-problem 2: how far did bookings really fall in the two metros, and why, before anyone moves staff?

**Who needs the answer.** The patient service centres' operations head, who decides this month
whether to send a field team to the two metros, cut staff there, or leave them alone. A fall read too
large cuts staff that patients still need.

**The questions on the way.** What did the operations head ask, and what does a finished answer
reach? What did the group do? Why that way? What would change its call?

### What did the operations head ask, and what does a finished answer reach?

> "Bookings fell in two of our metros in Q3. Before I send a field team or cut staff there, I need to
> know how far they fell, and why."
> The patient service centres' operations head, Kalpa Health, in brief 2

**What is planted.** Chicago and Philadelphia moved to the new booking system on 18 September, and
the old system's export carries only its own bookings, so its last booking date for the two metros is
17 September. On one row per booking id, the two metros fall 23.0 percent in the old export (1,415 to
1,090 bookings) and 12.2 percent across both systems (1,415 to 1,243): Chicago 754 to 571 in the old
export, minus 24.3 percent, and 656 in truth, minus 13.0; Philadelphia 661 to 519, minus 21.5, and
587, minus 11.2. The other four metros grow: Dallas 7.7, Phoenix 13.0, New York 6.8 and Atlanta 21.2
percent. The old export repeats rows from a mid-quarter re-export: 11,729 rows over 11,549 booking
ids, 180 ids twice, booked from 1 June to 26 September; 145 of the pairs match on every column and
35 do not (29 differ only in `updated_at`, 5 only in `channel`, and 1 in both), so a whole-row dedupe
leaves 11,584 rows. The new system holds 153 bookings dated 18 to 30 September, written month first
(`09/18/2026`), with its own references (`NB/ORD/000001`), site codes (`ORD-01` to `ORD-03`,
`PHL-01` to `PHL-03`, carried in the site list's `new_system_code`), patient numbers without the
`P-` prefix, channels (`WALKIN`, `WEB`, `CALL`, `MOBILEDRAW`) and states (`DONE` for 143 and `CXL`
for 10).

**What a finished answer reaches.** Bookings in the two metros fell about 12 percent, from 1,415 to
1,243, and the 23 percent on the old report comes from the system switch. Month by month across both
systems the two metros book 488, 478 and 449 from April to June, then 452, 420 and 371 from July to
September, so the fall was under way in August, before the switch, and the field team has a fall of
about 12 percent to explain.

### What did the group do, and which Week 1 or 2 move did it carry?

The translation probe, from the row's "why this identity rule for bookings". The move: Week 1
Wednesday, which rows repeat and what makes two rows one booking.

**"What made two booking rows the same booking, and why that rule?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| The booking id within the old system, since its export repeats rows; the new system's references are its own, so the two systems are stacked with a column naming the system and never deduplicated against each other | "We used drop_duplicates" | "Did the repeated rows match on every column? What would a whole-row dedupe have left?" (145 of the 180 pairs match on every column and 35 do not, so a whole-row dedupe leaves 35 repeats in, 11,584 rows for 11,549 ids.) |

### Why did the group choose that way? The seat's probe, P1 to P4

**P1, seat 1. "How far did bookings fall in Chicago and Philadelphia?"** The move: Week 1 Tuesday,
rung 1, is the drop real, confirmed in every system.

| Did the work | Carried it | The follow-up |
|---|---|---|
| About 12 percent, 1,415 to 1,243, once the new system's bookings are in; the old export alone says 23 percent, 1,415 to 1,090; Chicago minus 13.0 and Philadelphia minus 11.2 | Says 23 percent, or says 12 without being able to say where the other bookings came from | "How did you find out the new system held the two metros' bookings, and from which date?" (Its export is one of the ten files; its 153 bookings start on 18 September, and the old export's last date for the two metros is 17 September.) |

**P2, seat 2. "The two systems write sites, channels and dates differently. How did you line them
up?"** The move: Week 1 Wednesday, profile before you count, and reconcile codes across two sources.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Mapped the sites through the site list's `new_system_code` (`ORD-01` to `KH-CHI-01`), the channel and state codes (`DONE` to completed, `CXL` to cancelled), the patient numbers to the register's `P-` ids, and read the new system's dates month first | "We merged the two files" | "What happens to September if the new system's dates are read day first?" (Every day is the 18th or later, so all 153 fail as a month above 12, and a coerced read drops them, which brings the 23 percent back.) |

**P3, seat 3. "The real fall is about 12 percent. Is that a real fall, or the switch again?"** The
move: Week 1 Tuesday, the ladder's next rung, the same windows month by month.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Looked month by month across both systems: 488, 478 and 449 from April to June, 452, 420 and 371 from July to September, so the two metros were falling before 18 September and the switch doubled how the fall looked | Treats 12 percent as all real or all switch, with no months to show for it | "What would you ask the operations head to explain the fall that remains?" (What changed on the ground from August: staffing, opening hours, a competitor, a payer's network.) |

**P4, seat 4. "The old export has more rows than bookings. How many, and what did you keep?"** The
move: Week 1 Wednesday, which copy stays.

| Did the work | Carried it | The follow-up |
|---|---|---|
| 11,729 rows for 11,549 ids, 180 ids twice from a re-export, booked 1 June to 26 September; kept one row per id, the latest `updated_at`, and logged the rule with its count | "There were some duplicates" | "Did the repeats change the two metros' fall?" (Barely: 35 of the repeats are the two metros' Q2 rows and 9 their Q3 rows, so on raw rows the old export falls 24.2 percent instead of 23.0; a learner who did it checks by metro and quarter.) |

### What would change the group's call? The caveat challenge

The move: Week 1 Friday, the note that holds when someone pushes. Ask for the group's headline claim
and its caveat, then push as the operations head.

**"Your caveat says the two metros' count depends on stitching two systems together. I need one
number to decide on staff: did bookings fall or not?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| Holds both halves: yes, they fell about 12 percent, from 1,415 to 1,243, and the 23 percent on the old report is the switch; the caveat is about the size of the fall, never whether it happened, and it names what would shrink it, the data team confirming the new system's export is complete to 30 September | Drops the caveat under the push and gives one number, or retreats to "it depends" | "What would you check tomorrow to make the caveat smaller?" |

---

## Sub-problem 3: which claims are still unpaid, how many dollars is that, and can finance trust the figure?

**Who needs the answer.** The finance head, who reports the collections figure at the quarter's close
and decides which unpaid claims the revenue-cycle team chases first. A wrong figure reaches the board
under the finance head's name, and a claim chased late can pass its payer's filing deadline.

**The questions on the way.** What did the finance head ask, and what does a finished answer reach?
What did the group do? Why that way? What would change its call?

### What did the finance head ask, and what does a finished answer reach?

> "The claims we billed say one thing and the posting system says another. Which claims are unpaid,
> how much money is that, and can I trust the figure I report?"
> The finance head, Kalpa Health, in brief 3

**What is planted.** The posting system keys claims in three formats, duplicate electronic remittance
loads double-post, the employer claim is unpaid, and denials post with nothing paid. An exact join of
`claim_ref` to `claim_id` matches 216 of 11,343 postings, 1.9 percent: 216 carry the claim id
(`KH-CLM-000095`), 2,269 a CLM-number without its zeros (`CLM-95`) and 8,858 six bare digits
(`000095`). Normalised to the six-digit serial, every posting matches a claim. 280 double posts, the
same claim and the same amount paid twice by electronic remittance, 0 to 2 minutes apart, carry
$19,204.63; 105 reversals take back $8,662.87. 398 claims have no posting at all, $253,165 billed,
spread over every month from April to September, the $180,000 employer claim among them. The claims
file marks 1,175 of the 11,355 retail claims denied, 10.35 percent (Medicaid 14.9, commercial 11.3,
Medicare 8.8 and self-pay none), billing $230,132; 1,137 of them carry a denial posting that pays
$0.00, and the other 38 have no posting. Billed across both quarters is $2,201,099; paid net of the
double posts is $801,313.56, 36.4 percent. The $1,399,785.44 between them is $883,254.70 of
contractual adjustments, $253,165 billed on claims with no posting, $222,108 billed on claims denied
with a posting, $32,594.87 of patient shares and $8,662.87 of reversals.

**What a finished answer reaches.** Every posting matched to its claim after the key is normalised,
the 280 double posts counted once, and every claim classed as paid, part paid, denied or with no
posting, with its dollars; collections of $801,314 against $2,201,099 billed, and the gap split into
what the contracts never meant to pay, what was denied and what is still owed, led by the $180,000
employer claim.

### What did the group do, and which Week 1 or 2 move did it carry?

The translation probe. The move: Week 2 Tuesday, attach, count, explain the difference, then sum.

**"In Week 2 you joined payments to orders on an id both sides shared. What was your key here, and
how many postings matched on the first try?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| An exact join matched 216 of 11,343 postings, 1.9 percent, because the posting system writes the claim three ways; normalised to the six-digit serial, every posting found its claim, and the billed amounts agree on the matched pairs | "We joined on claim id", with a collected figure and no word about the key | "`CLM-95` and `000095`: how do you know they are the same claim?" (Pad to six digits, match, then confirm the billed amount the posting carries agrees with the claim's.) |

### Why did the group choose that way? The seat's probe, P1 to P4

**P1, seat 1. "Some claims carry two payments. Did the payer pay twice?"** The move: Week 2 Tuesday,
what makes a second posting a repeat.

| Did the work | Carried it | The follow-up |
|---|---|---|
| No: 280 pairs, the same claim and the same amount, both electronic remittances, 0 to 2 minutes apart, $19,204.63, which is a file loaded twice; counted once, listed for the posting team to confirm | "We removed duplicate payments" | "Sometimes a payer does pay the same amount on two different claims. How does your rule avoid removing that?" (The rule is the same claim and the same amount minutes apart; two claims are two keys.) |

**P2, seat 2. "Which claims have no posting at all, and how many dollars is that?"** The move: Week 2
Tuesday, the rows with no partner, found by an anti-join.

| Did the work | Carried it | The follow-up |
|---|---|---|
| 398 claims, $253,165 billed, in every month from April to September, the $180,000 employer claim among them; says a September claim may simply not have been answered by 16 October | Gives a count with no dollars, or misses the employer claim | "Is the employer claim late, or is it a problem? What would you ask?" (Its payment terms and who at the employer approved the invoice; an employer may pay on terms longer than a quarter.) |

**P3, seat 3. "How many claims did payers deny, and what did they pay on them?"** The move: Week 1
Monday, a rate with its denominator, on Week 2 Tuesday's matched claims.

| Did the work | Carried it | The follow-up |
|---|---|---|
| 1,175 of the 11,355 retail claims, 10.35 percent, Medicaid highest at 14.9 and self-pay none, billing $230,132; 1,137 carry a denial posting that pays $0.00, and 38 have no posting | Gives a count with no denominator, or counts the $0.00 denial postings as payments | "Which denials would you send the revenue-cycle team after first, and why?" (By count, eligibility or coverage 283 and missing or invalid information 272; missing information is corrected and resent before the filing deadline, so it goes first.) |

**P4, seat 4. "Walk me from billed to paid, in dollars."** The move: Week 1 Wednesday, the bridge
that names every dollar between two totals.

| Did the work | Carried it | The follow-up |
|---|---|---|
| $2,201,099 billed; $801,314 paid net of the double posts, 36.4 percent; the $1,399,785 between them is about $883,255 of contractual adjustments, $253,165 on claims with no posting, $222,108 on claims denied with a posting, $32,595 of patient shares and $8,663 of reversals | Gives paid as the raw sum of payments, $820,518, or cannot bridge the two totals | "Which line of your bridge would you check first if finance's paid figure were $19,205 higher than yours?" (The double posts.) |

### What would change the group's call? The caveat challenge

The move: Week 1 Friday, the note that holds when someone pushes. Ask for the group's headline claim
and its caveat, then push as the finance head.

**"Your caveat says the second payments are a file loaded twice. My team says the money is in the
bank twice. Is your caveat hiding cash?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| Keeps the rule and says what would change it: the pairs sit 0 to 2 minutes apart on one claim and one amount, all from electronic remittances, which is a loading pattern; the list of 280 goes to the posting team to check against the bank deposits; if the bank shows two deposits, the payer overpaid and owes a refund request, which is money owed back, never revenue | Concedes the money may be there twice, or insists with no evidence | "Which single record would settle it for one of the 280?" (The bank deposit, or the payer's payment trace number on the remittance.) |

---

## Sub-problem 4: is KH-ATL-03 really worse at no-shows than the other centres, before anyone adds staff or closes it?

**Who needs the answer.** The patient service centres' operations head, who decides between a second
receptionist, reminder calls and a closure notice for KH-ATL-03. A centre closed on a rate read
wrongly takes a neighbourhood's nearest blood draw away, and a missed draw can mean a missed
diagnosis.

**The questions on the way.** What did the operations head ask, and what does a finished answer
reach? What did the group do? Why that way? What would change its call?

### What did the operations head ask, and what does a finished answer reach?

> "KH-ATL-03, one of our two Atlanta patient service centres, has the worst no-show rate on my Q3
> report. I am being asked to add a receptionist there or close it. Is the centre really worse?"
> The patient service centres' operations head, Kalpa Health, in brief 4

**What is planted.** KH-ATL-03 runs by appointment, while the other centres' visit counts include
walk-ins, who cannot miss a slot. The visit register is drawn from the bookings, so a rebooked
patient's missed slot is a row beside the kept visit. KH-ATL-03 has 80 visits: 79 scheduled and 1
walk-in, with 15 missed slots. On all visits it reads 18.8 percent against 7.9 percent for the other
eleven centres, whose 3,605 visits include 1,720 walk-ins, 47.7 percent; the next worst centre reads
9.8. On scheduled visits it reads 19.0 percent, 15 of 79, against 15.1 percent, 285 of 1,885; the
next worst reads 18.5. If KH-ATL-03's true rate were the others' 15.1 percent, 15 or more missed slots
in 79 would happen with probability 0.21, about one time in five; at that rate it would expect about
12, so three patients decide the gap. The same check run on all visits, 80 at 7.9 percent, gives
0.0014, which reads as real and is the wrong comparison. Of the register's 3,685 rows, 253 bookings
have two: a missed slot and then the kept visit. Counted per booking instead of per slot, 15 of
KH-ATL-03's 64 scheduled bookings missed a slot against 17.3 percent elsewhere, a gap chance produces
with probability 0.13.

**What a finished answer reaches.** On scheduled visits, KH-ATL-03's 19.0 percent against 15.1
percent is a gap chance produces about one time in five, so neither a receptionist nor a closure is
supported by Q3; a cheap reminder trial, read against the other centres on scheduled visits, is.

### What did the group do, and which Week 1 or 2 move did it carry?

The translation probe, from the row's "what a fair comparison needed in a clinic". The move: Week 1
Thursday, is the split fair, and Week 1 Monday, a metric defined before it is counted.

**"What did a fair comparison between KH-ATL-03 and the other centres need here?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| The same denominator: about half of the other centres' visits are walk-ins, 1,720 of 3,605, and a walk-in cannot miss a slot, so missed slots are compared on scheduled visits; then the question is whether the gap on that base is more than chance on 79 slots | "We compared each centre's no-show rate" | "Can a walk-in be a no-show? So what does counting walk-ins do to a centre's rate?" (No; walk-ins add attended visits to the denominator and lower the rate, and KH-ATL-03 has one walk-in in 80 visits.) |

### Why did the group choose that way? The seat's probe, P1 to P4

**P1, seat 1. "Is KH-ATL-03's rate worse? Give me the two numbers you compared."** The move: Week 1
Thursday, is the split fair.

| Did the work | Carried it | The follow-up |
|---|---|---|
| On scheduled visits, 19.0 percent, 15 of 79, against 15.1 percent, 285 of 1,885; the report's 18.8 against 7.9 percent came from the other centres' walk-ins | "It is 18.8 percent against 7.9, more than double" | "Why drop walk-ins from the others and not from KH-ATL-03?" (They are dropped from every centre; KH-ATL-03 has one.) |

**P2, seat 2. "Fifteen missed slots in 79. Is that a real difference or noise?"** The move: Week 1
Thursday, real, or the wobble.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Ran a chance check, coin flips or the binomial: at 15.1 percent, 15 or more missed slots in 79 happens about one time in five, 0.21, so the gap is within chance; at that rate the centre would expect about 12, three fewer | Says "it is significant" or "it is not significant" with no check named, or runs the check on all visits and reports 0.0014 | "Say that to the operations head in one sentence, without the word probability." |

**P3, seat 3. "Some bookings have two rows in the visit register. What are they, and did you count
them?"** The move: Week 1 Monday, what one row stands for before anything is counted.

| Did the work | Carried it | The follow-up |
|---|---|---|
| 253 bookings have a missed slot and then the kept visit; the rate counts slots, so both rows stay; counted per booking instead, 15 of KH-ATL-03's 64 scheduled bookings missed a slot against 17.3 percent elsewhere, and chance produces that gap with probability 0.13 | Has not looked, or dropped one row of each pair without a reason | "Which count would the operations head want, slots or patients, and why?" (Slots for staffing the front desk, patients for reaching the people who miss draws; the group says which it used.) |

**P4, seat 4. "The operations head wants to add a receptionist or close the centre. What do you
advise?"** The move: Week 1 Thursday, is it worth acting on, and what does acting cost.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Neither on Q3's evidence: the fair gap is inside chance; keep reading the rate on scheduled visits each month; a reminder call before each booked slot at KH-ATL-03, read against the other Atlanta centre, costs far less than a receptionist, and a closure is the one action that cannot be undone for the patients who use it | Agrees with either action, because the rate "is the worst" | "What would change your advice?" |

### What would change the group's call? The caveat challenge

The move: Week 1 Friday, the note that holds when someone pushes. Ask for the group's headline claim
and its caveat, then push as the operations head.

**"You say the gap could be chance. Nineteen percent is nineteen percent. Why should I not act?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| Holds it with the number: on 79 slots, three patients decide the gap, and a gap this size appears by chance about one time in five; acting is fine when it is cheap and can be undone, and the caveat names what to measure next and for how long | Agrees the centre is worse, or repeats "not significant" with no number | "If you gave her one action today, what is it and what would it cost?" |

---

## Sub-problem 5: did the free at-home collection offer lift bookings 9 percent, and should every patient in all six metros get it?

**Who needs the answer.** The marketing head, who wants to extend the offer to every patient in all
six metros, and Dr Menon, who signs the cost. Every free collection sends a phlebotomist to a home,
so an offer extended on a lift it did not cause spends that money every week for nothing.

**The questions on the way.** What did the marketing head ask, and what does a finished answer reach?
What did the group do? Why that way? What would change its call?

### What did the marketing head ask, and what does a finished answer reach?

> "Our free at-home collection offer lifted bookings 9 percent. I want to offer it to every patient
> in all six metros. Can you confirm it worked?"
> The marketing head, Kalpa Health, in brief 5

**What is planted.** The offer went at random to about half the patients in three metros that were
already rising, Dallas, Atlanta and Phoenix, and to about a fifth of the patients elsewhere; inside
the three metros, an offered patient booked less while the offer ran than one who was not offered.
2,381 patients were offered between 15 July and 4 August, and 948 accepted; at least 259 of those
show a collection at home between their offer and 14 September, and 689 show none. Over 15 July to 14
September, offered patients booked 9.0 percent more per patient than the rest, 0.633 bookings against
0.581, and less in every campaign metro: Dallas minus 10.8, Atlanta minus 19.9 and Phoenix minus 13.0
percent. The offer reached 50.5 percent of the three metros' patients against 21.4 percent elsewhere,
and the three metros book more per patient than the other three. Before the offer, from 1 April to 14
July, offered and not-offered patients booked within about 6 percent of each other in each campaign
metro, Dallas plus 1.4, Atlanta minus 5.2 and Phoenix minus 6.1, so nothing in the files shows how
patients were chosen. The campaign metros rose 6.9 percent in bookings per day over the two months
before the offer, and 7.4 percent from those two months into the offer's weeks, against 3.0 percent
in New York over the same weeks. Outside the three metros the gaps are chance: Chicago minus 4.8,
Philadelphia plus 0.6 and New York plus 23.5 percent, a random draw that a permutation test puts at p
of about 0.03 (two-sided, 10,000 shuffles), so a group that reads it as a lift has met a false
positive.

**What a finished answer reaches.** The 9 percent compares where the offer went with where it did
not; inside every metro that got most of the offers, offered patients booked less, and the files
cannot say how patients were chosen, so the offer's effect is unknown; the next wave should hold back
a random share of eligible patients in every metro.

### What did the group do, and which Week 1 or 2 move did it carry?

The translation probe. The move: Week 1 Thursday, did the discount work, split inside each segment.

**"In Week 1 the monsoon sale looked like it worked in total. What was the equivalent of the segment
split here, and what did it show?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| The split by metro: offered patients book 9.0 percent more in total and less inside every campaign metro, by 10.8, 19.9 and 13.0 percent, so the 9 percent comes from where the offer went | Says "Simpson's paradox" with no metro numbers, or confirms the 9 percent | "Where did the offer go, and what were those metros doing before it started?" (To about half the patients in Dallas, Atlanta and Phoenix, 50.5 percent against 21.4 elsewhere; those metros rose 6.9 percent in the two months before.) |

### Why did the group choose that way? The seat's probe, P1 to P4

**P1, seat 1. "Did the offer lift bookings 9 percent?"** The move: Week 1 Thursday, the aggregate
against the split.

| Did the work | Carried it | The follow-up |
|---|---|---|
| The 9 percent is offered against not offered across all six metros; inside each campaign metro offered patients booked less, by 11 to 20 percent, so the 9 percent measures where the offer went, the metros whose patients book most | "Yes, 9 percent", or "no, it is a paradox" with no numbers | "So did the offer reduce bookings?" (The files cannot settle it: they show who was offered and never how they were chosen, so the gap inside a metro may come from who was chosen. A random held-out share of eligible patients would settle it.) |

**P2, seat 2. "The campaign metros were growing. By how much, before the offer?"** The move: Week 1
Thursday, what else changed, and the change beside the change.

| Did the work | Carried it | The follow-up |
|---|---|---|
| About 7 percent in bookings per day over the two months before the offer, and 7.4 percent into its weeks, against 3.0 percent in New York, so the rise was under way | Does not know, or never looked before the offer | "What comparison would you have needed to credit the offer with any of the rise?" |

**P3, seat 3. "Who was offered the free collection? Were they like the patients who were not?"** The
move: Week 1 Thursday, who got the sale, and is the split fair.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Compared offered and not-offered patients in each campaign metro before the offer: within about 6 percent of each other, Dallas plus 1.4, Atlanta minus 5.2 and Phoenix minus 6.1, with the sign changing, so nothing before the offer separates them, the gap opens inside its weeks, and the files cannot say how the offer was assigned | Asserts that the offer went to patients who were already drifting, or that it was random, without comparing the two groups before the offer | "How would you design the next wave so the question can be answered?" (Hold back a random share of eligible patients in every metro and compare over the same weeks.) If a group shows offered patients behind in the months just before the offer: "Could chance give a gap that size between two groups this big?" |

**P4, seat 4. "Outside the three metros, did the offer work anywhere?"** The move: Week 1 Thursday,
real, or the wobble, when many comparisons are made.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Chicago minus 4.8, Philadelphia plus 0.6, New York plus 23.5 percent; ran a shuffle on New York and got about 0.03, and says that with six metros tested one striking gap is what chance alone tends to give, so New York is no evidence of a lift | Reads New York's 23.5 percent as the offer working in New York | "If you test six metros, how often does at least one show a gap that would pass at 0.05 by chance alone?" (About one time in four: 1 minus 0.95 to the sixth is 0.26.) |

### What would change the group's call? The caveat challenge

The move: Week 1 Friday, the note that holds when someone pushes. Ask for the group's headline claim
and its caveat, then push as the marketing head.

**"948 patients took the offer up. You cannot prove it did nothing; your caveat is just doubt, and I
need budget for all six metros."**

| Did the work | Carried it | The follow-up |
|---|---|---|
| Agrees the files cannot prove harm or help, which is the caveat's point; acceptances count people who said yes to a free service, and at least 259 of the 948 show a home collection in the offer's weeks; offers the next wave as the test, the offer to a random part of eligible patients in every metro with the rest held out, so the budget buys an answer | Says the offer failed, or gives in and agrees it worked | "How large a held-out share would you ask for, and what would you compare?" |

---

## What would each learner do differently?

**Who needs the answer.** The assessor scoring the last 3 marks, which reward a learner who can name
a better path from their own log, never a general lesson.

**The questions on the way.** What is the probe? What does a learner who kept an honest log say? What
do you ask if the log is thin?

**"From your challenges log: what would you do differently if you started this sub-problem again
tomorrow?"** The move: Week 1 Friday, rebuilding the week alone and naming the step you do not own
yet.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Opens the log, finds an entry they wrote, names the step they would move earlier or do another way, such as profiling both booking systems before any count or asking the data team on the first day how each file is keyed, and the time or error it would have saved | Gives a general lesson ("manage time better"), or reads a group-mate's entry as if seeing it for the first time | "Which entry shows the moment you should have changed course, and what told you?" |

If the group's challenges log has only a few entries by Thursday, note it, and ask about the decisions
log instead: "Pick one line in the decisions log and tell me who decided it and what they looked at."

# Which questions climb Mock R1's viva from what each group did, to why it chose its way, to what would change its call?

**TRAINER ONLY.** This is the assessors' file, so every plant in the Kalpa Health data is written
here with its witness number. Every question an assessor reads aloud asks without telling: a plant
appears only in the column that says what a learner who did the work says, and never in a probe, a
follow-up or a push. A learner who asks "is there something hidden in the data?" gets the question
back: **"What would you check?"**

**Who needs the answer.** The three assessors, who each run about twelve eight-minute vivas on
Thursday 22 October, on the groups they hear all day: the Programme Head G1, G4 and G7, the Academic
TA G2, G5 and G8, and the Principal Advisor G3, G6 and G9. The viva scores 15 of the mock's 30
marks, and a probe that names what the data holds hands the learner the answer it was meant to
test, the day before the build freezes.

**The questions on the way.** How do the eight minutes run, and which criterion does each probe
evidence? Why does no probe say what the data holds, and how do you push on a caveat? What does every
learner meet first? What does Dr Menon's 5 percent count? Then, for each of the five sub-problems,
what the asker wants, what the group did, why it chose its way and what would change its call. Last,
what each learner would do differently.

Kalpa Health is a US diagnostics business with a laboratory and two patient service centres, where a
phlebotomist draws patients' blood, in each of six US metro areas: Dallas, Phoenix, New York, Chicago,
Atlanta and Philadelphia. It bills each patient's payer in dollars, a commercial plan, Medicare,
Medicaid or the patient (self-pay); a claim is the bill, and a remittance is the payer's answer,
which the posting system records as postings. Its COO, Dr Priya Menon, sees test volumes up 5
percent from Q2 (April to June 2026) to Q3 (July to September 2026) against a plan of 18, and five of
her heads each asked one question. Every group answers one of them from ten files exported on Friday
16 October 2026, and on Wednesday each group stated a headline claim with its denominators and its
caveat. Every number below is recomputed from those files by
`internal/C2_W03_D04_numbers_INTERNAL.py`, and the spine, `docs/detailing/W03_build1_spine.md`,
carries the same plants.

---

## How do the eight minutes run, and which criterion does each probe evidence?

**Who needs the answer.** Each assessor, before the first viva: the five probes come in a fixed
order, and each one is the evidence for one row of the rubric.

**The questions on the way.** Which probes, for how long? Which seat probe does each learner take?
When do you ask to see the work? What do you listen for in every answer? Why does no probe say what the data
holds? How do you push on a caveat?

The viva climbs in three steps, the way an interviewer moves from a candidate's work to their
judgement: what the group did, why it did it that way rather than another, and what would change its
call.

| Minutes | The probe | The step it climbs | Where it comes from | The criterion it evidences |
|---|---|---|---|---|
| 1.5 | The opener, the same for every learner | What you did | The row's interview angle | The translation, with one decision defended by evidence (6) |
| 1.5 | The translation probe for the group's sub-problem | What you did, and which Week 1 or 2 move it carried | The row's thinking column | The translation, with one decision defended by evidence (6) |
| 2 | One of four seat probes, as the Grid prints it | Why that way | The spine's plant table, asked without naming the plant | The translation, with one decision defended by evidence (6) |
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

### Which seat probe does each learner take?

Each sub-problem carries four seat probes, P1 to P4, each aimed at one thing in the files a group had
to find, and each asking why the group chose its way and what the other way would have given. The
roster's Grid prints each learner's probe beside the technical questions and the reserves; the seat
list the learners see prints none of them. The four members of a group always take four different
probes, and where two groups share a sub-problem the second group's rotation starts one probe on, so
a seat number tells a learner nothing about the probe. The opener, the translation
probe, the caveat challenge and the looking-back probe stay the same for every learner, because a
learner's own words are what they test, and group-mates' answers to them should differ. A learner
racing through can take the headline probe, H, as a second "why" probe.

### When do you ask to see the work?

At least once in every viva. The learner has the group's notebook or SQL, the decisions log and the
challenges log open. Ask for the cell or the log line behind one number. A learner who finds it in
under a minute built it or read it closely; a learner who searches and cannot find it carried it.

### What do you listen for in every answer?

Each probe below gives three columns: what a learner who did the work says, with the number, the
unit and the check; what a learner who carried it, presenting a group-mate's work, says, which is
usually the right headline without the mechanism; and the follow-up that tells them apart. The
expected answer to a follow-up sits in brackets after it, for you alone, and is never read aloud.
Note a carried answer as it happened; never argue with the learner in the room, and never correct a
number.

### Why does no probe say what the data holds?

Because the build freezes on Friday and the mini project rubric, scored at Friday's and Saturday's
presentations, gives 10 marks to the data made trustworthy and 10 to the analysis, a probe that names
a plant on Thursday hands it to a group that missed it, in time to fix it before it is scored. So every probe opens on the group's own claim,
and the plant appears only in the "did the work" column, as what a learner who found it says. A
follow-up may take up what the learner has just named, in the learner's words, and nothing more.
When a learner has missed a plant, the miss is the evidence: note it, ask the follow-up as written,
and move on, without steering, confirming or denying.

### How do you push on a caveat?

Ask for the group's headline claim and its caveat first, in the learner's words, then push as the
asker on the caveat the learner gave. Each sub-problem's table has a row for the caveats groups most
often write, and the condition column, which is never read aloud, says which caveat the row answers.
A learner whose caveat is anything else meets the general push: **"That sounds like doubt. What would
make it smaller, and would it change what I should do?"** A learner who gives no caveat meets **"What
is the one thing that could make your number wrong, and how would you know?"** first. A push stays on what
the learner has said and never brings in a plant.

---

## What does every learner meet first?

**Who needs the answer.** The assessor opening every viva the same way, so that the learner's own
choice of what to defend is the first evidence.

**The questions on the way.** What is the opener? What does a learner who did the work say first?

**`[S]` "Walk me through the analysis you did on unfamiliar data and one decision you would
defend."** This is the row's interview angle for the day.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Starts from the asker's question and the decision it feeds, names the files the group profiled and what surprised it, gives one decision from the decisions log with its count or dollars and its reason, and says what would change it | Starts from the tool or the chart, gives the group's headline, and names a decision in general words, such as "we cleaned the data" | "What was the alternative to that decision, and what number would have come out if you had taken it?" (A second way with its own count or dollars, from the learner's own files, and why the group's way won.) |

---

## What does Dr Menon's 5 percent count, and which number does each group put beside it?

**Who needs the answer.** The assessor of any group, since every group started from Dr Menon's 5
percent, and confirming a number before explaining it is the Week 1 Tuesday move.

**The questions on the way.** What does the 5 percent count, and what is planted in it? What does the
headline probe ask? What separates the answers?

Dr Menon's 5 percent is her dashboard's count, which is the headline's plant, and no assessor names
it: tests booked in the old booking system only, one row per booking id, with a panel counted as its
component tests. Computed from the files, that count is 23,213 tests in Q2 and 24,406 in Q3, 5.1
percent; on raw rows, with the old export's repeated rows still in, the same reading is 23,788 to
24,556, 3.2 percent. Across both booking systems, tests booked grew 7.8 percent (23,213 to 25,022),
tests performed on completed bookings grew 8.6 percent (22,468 to 24,399) and bookings grew 5.6
percent (5,692 to 6,009). All four leave out the employer contract, a single booking whose 1,200
wellness screenings of five tests each add 6,000 tests to Q3. With it in, tests performed would grow
35.3 percent and tests booked 33.6, while bookings stay at 5.6, since the contract is one booking.
Every reading without the contract is short of the plan of 18.

**H. "Dr Menon's dashboard says 5 percent. What is your group's number for growth, and what did it
count?"** It tests Week 1 Monday's move: which total, and what each total counts.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Names the unit, tests booked, tests performed or bookings, with both booking systems in it and the employer contract out or shown apart, and places the number against the plan of 18, such as tests performed up 8.6 percent, 22,468 to 24,399 | Quotes the group's percentage without its unit, or says the dashboard is wrong without saying what it counted | "Why that count rather than another, and what would the other count have given?" (Another unit with its growth on both systems, such as tests booked up 7.8 percent or bookings up 5.6, and the employer contract's 6,000 tests shown apart: with them in, tests performed would grow 35.3 percent and tests booked 33.6 while bookings stay at 5.6, so one employer's booking would describe the growth of the whole business. A learner who carried it names no other count.) |

---

## Sub-problem 1: which branch of Kalpa Health's billed revenue is short of the plan, and by how much?

**Who needs the answer.** The finance head, who writes the board's page on where the plan's growth
went, and Dr Menon, who moves the second half's recovery effort onto the branch the group names. A
branch named wrongly sends staff and money where nothing was short.

**The questions on the way.** What did the finance head ask, and which branch does a finished answer
name? What did the revenue group count as a test and as a claim, and where does its tree differ from
Week 1's? Why did it count and clean as it did? What does the finance head push on, and what holds?

### What did the finance head ask, and which branch does a finished answer name?

> "The board will ask me where the plan's growth went. Where does our lab revenue actually come
> from, and which branch of it is short?"
> The finance head, Kalpa Health, in brief 1

Three things in the revenue files are planted, and no assessor names any of them: one employer
wellness contract in Q3, panels billed as one claim line, and billed amounts written as text. Claim
KH-CLM-007802, on employer account EMP-0007, Dallas, service date 6 August 2026, bills $180,000 for
1,200 screenings, which is 14.6 percent of Q3's billed charges of $1,231,001. Billed charges grow
26.9 percent from Q2's $970,098 with it, ahead of the plan, and 8.3 percent without it, to
$1,051,001. The Q3 mean claim is $210.50 with it and $179.75 without; the median is $150 in both
quarters, and Q2's mean is $176.13. A panel bills as one line: outside the contract, 22,152 claim
lines, 21,050 of them tests or panels and 1,102 a $20 fee for a collection at home, bill 46,867
tests on the completed bookings behind them (48,235 counting cancelled bookings, which the
booking-tests file also lists); in Q3 alone, 11,395 claim lines bill 24,399 tests. Sixty billed
amounts are text with a dollar sign, such as "$265.00": 32 in Q2 worth $5,390 and 28 in Q3 worth
$5,169.

A group that found all three reaches this answer. Outside the contract, billed charges grew 8.3
percent against a plan of 18, which leaves Q3 $93,715 short of $1,144,716. Chicago and Philadelphia
carry $63,436 of that shortfall, about two thirds, from 24.5 percent of Q2's billing: Chicago's
billed charges fell 6.5 percent ($124,097 to $115,997) and Philadelphia's 10.9 percent ($114,014 to
$101,538), while Atlanta finished $11,156 ahead of its share of the plan. The payers did not grow
alike either: commercial billing grew 13.0 percent, Medicare 6.0 and Medicaid 1.6, and self-pay fell
2.2, so against its own plan commercial is 4.2 percent short, Medicare 10.2, Medicaid 13.9 and
self-pay 17.1, and Medicaid carries 25.3 percent of the shortfall from 14.9 percent of Q2's billing.
Outside the two metros, commercial grew 20.8 percent against 3.5 to 7.6 for the other payers, so the
payer gap is a second finding, separate from the two metros' fall. The two metros put the most
shortfall on the least billing, so a group that names them first and the payer gap second has the
whole answer, and a group that names only the payer gap has found a real pattern and missed the
larger one. A strong group also says Q3 has 92 days to Q2's 91.

### What did the revenue group count as a test and as a claim, and where does its tree differ from Week 1's?

The translation probe comes from the row's "why this tree for a lab" and tests Week 1 Monday's move,
the revenue tree, every branch a count over a denominator.

**"Walk me down your revenue tree for Kalpa Health, and tell me where it differs from the one you drew
for Kalpa Retail in Week 1."**

| Did the work | Carried it | The follow-up |
|---|---|---|
| Patients, times bookings per patient, times tests or claim lines per booking, times billed dollars per line, or claims times the mean claim, with the payer as a split; says where retail's "items per order" breaks on a lab: a panel is one priced line covering several tests, a collection at home carries its own fee line, and an employer account is a branch of its own | Recites Kalpa Retail's tree with lab words swapped in, and cannot say where one line covering several tests sits | "Which leaf of your tree did you check against the raw files, and what did the check show?" (A leaf with its check, such as tests per booking from the booking-tests file against claim lines per claim: a claim line can be one test, a panel covering several or a collection fee, so lines are no count of tests, and the whole-body wellness panel is one line at $299 for twelve tests whose list prices add to $785. A learner who carried the tree names no check.) |

### Why did the revenue group count and clean as it did, and what would the alternative have given?

The Grid prints which of the four each learner takes.

**P1. "Which number did your group give Dr Menon as a typical claim in Q3, why that one, and what
would the other measure have said?"** It tests Week 1 Monday's move: the typical value one large
record cannot move.

| Did the work | Carried it | The follow-up |
|---|---|---|
| The median, $150, beside the mean, $210.50, because the mean moves with one record: sorted the claims and found one claim of $180,000 on an employer account, 14.6 percent of Q3's billed charges; the mean without it is $179.75; kept it in revenue as its own branch | Gives $210.50 as typical, or says "we removed an outlier" | "If the two measures you gave differ, what makes them differ in your data, and what did you do about it?" (One employer claim of $180,000 lifts the mean from $179.75 to $210.50; it stays in revenue on its own line, with no payment posted on it yet; Q2's mean of $176.13 sits over the same $150 median.) |

**P2. "Dr Menon counts test volume. What did your group count as one test, why that unit, and what
would the other count have given?"** It tests Week 1 Monday's move: which total, and what each
total counts.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Counted tests from the booking-tests file's test and component lines on completed bookings, 24,399 in Q3, against 11,395 claim lines outside the contract, because a panel bills as one line covering several tests and some lines are home-collection fees, which are no test | Counts claim lines or claims as tests | "Which file would Dr Menon's volume come from, and why that one?" (The booking-tests file's test and component lines, since a claim line can be a panel covering several tests or a fee that is no test; her volume is tests.) |

**P3. "Which branch did your group name as short, why that one, and how much of the shortfall would
the branch you ranked second have explained?"** It tests Week 1 Tuesday's move: which segment moved.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Outside the contract, billed charges grew 8.3 percent, $93,715 short of the plan; Chicago and Philadelphia carry $63,436 of it, falling 6.5 and 10.9 percent while the other four metros grew; then either rules the payer split out with its numbers or reports it second, commercial 4.2 percent short of its own plan against self-pay's 17.1; says Q2 has 91 days and Q3 92 | Says "revenue grew 26.9 percent", the total with the contract, or names a branch with no number | "If you give Dr Menon one number for the branch that is short, what is it, and what is it out of?" (About two thirds of the $93,715 shortfall, $63,436, in Chicago and Philadelphia, from 24.5 percent of Q2's billing. A group that answers by payer has found something real and smaller, and is right if it names its measure: Medicare carries the most shortfall dollars, $28,437, 30.3 percent of it; self-pay falls furthest short of its own plan, 17.1 percent, and carries the most against its size, 17.1 percent of the shortfall from 8.2 percent of Q2's billing; Medicaid carries 25.3 percent of the shortfall from 14.9 percent.) |

**P4. "What did your group's profile of the claims file find before you summed anything, why did you
treat it the way you did, and what would the billed total have been the other way?"** It tests Week 1 Wednesday's move: profile before you count, and
every value converted with a logged rule.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Found 60 billed amounts written as text with a dollar sign, such as "$265.00", stripped the sign, logged the rule with its count, and checked the billed total before and after; may also name the one very large claim | "We cleaned the amount column", with no count | "Which rule in your decisions log changed the billed total, and by how many dollars?" (Stripping the dollar sign keeps $5,169 of Q3's billed charges and $5,390 of Q2's that an empty read would lose; a learner who did it finds the log line and the count.) |

### What does the finance head push on, and what holds?

Push as the finance head, with the row that matches the caveat the learner gave.

| If the group's caveat is about | The push | Did the work | Carried it | The follow-up |
|---|---|---|---|---|
| The one large claim, which the group has named | "Your caveat sets part of the revenue apart. It is revenue. Why should I not count it?" | Keeps it in billed revenue and shows it apart: one claim is 14.6 percent of Q3, so any average or growth rate with it inside describes one employer; the caveat is about which number describes the retail business, and no revenue is removed | Removes the claim from revenue, or drops the caveat under the push | "Would your answer change if what you set apart came back every quarter?" (It becomes a branch with its own plan line; the retail tree still reads without it.) |
| The payers growing differently, which the group has named | "Your caveat says the payers moved differently. Does that change which branch I fund?" | Holds the order: the payer gap is real, with commercial 4.2 percent short of its own plan and self-pay 17.1, but the two metros carry two thirds of the shortfall from a quarter of the billing, so the recovery effort goes there first and the payer gap is looked at next | Switches the recommendation to a payer, or cannot say which pattern is larger | "What else could produce a payer gap like that, and how would you rule it out?" (Where the claims were billed: each payer's growth outside the two falling metros, where commercial grew 20.8 percent against 3.5 to 7.6 for the others, so the payer gap holds outside the metros' fall; a learner who did it names the two metros as the larger pattern.) |
| Anything else, or no caveat | The general push, or for no caveat the question that asks for one | Names the check that would shrink the caveat and the decision it could move, with a number | Drops the caveat, or repeats it without a number | "What would you check tomorrow, and how long would it take?" (A named check, its size in rows or dollars, and the decision it could move.) |

---

## Sub-problem 2: how far did bookings really fall in the two metros, and why, before anyone moves staff?

**Who needs the answer.** The patient service centres' operations head, who decides this month
whether to send a field team to the two metros, cut staff there, or leave them alone. A fall read too
large cuts staff that patients still need.

**The questions on the way.** What did the operations head ask, and how far does a finished answer
say bookings fell? What made two rows one booking in the group's count? Why did it count from the
files it chose? What does the operations head push on, and what holds?

### What did the operations head ask, and how far does a finished answer say bookings fell?

> "Bookings fell in two of our metros in Q3. Before I send a field team or cut staff there, I need to
> know how far they fell, and why."
> The patient service centres' operations head, Kalpa Health, in brief 2

Three things in the booking files are planted, and no assessor names any of them: the two metros'
move to a new booking system, the old export's repeated rows, and the new system's own codes and
month-first dates. Chicago and Philadelphia moved to the new booking system on 18 September, and the
old system's export carries only its own bookings, so its last booking date for the two metros is 17
September. On one row per booking id, the two metros fall 23.0 percent in the old export (1,415 to
1,090 bookings) and 12.2 percent across both systems (1,415 to 1,243): Chicago 754 to 571 in the old
export, minus 24.3 percent, and 656 in truth, minus 13.0; Philadelphia 661 to 519, minus 21.5, and
587, minus 11.2. The other four metros grow: Dallas 7.7, Phoenix 13.0, New York 6.8 and Atlanta 21.2
percent.

The old export repeats rows from a mid-quarter re-export: 11,729 rows over 11,549 booking ids, 180
ids twice, booked from 1 June to 26 September. 145 of the pairs match on every column and 35 do not
(29 differ only in `updated_at`, 5 only in `channel`, and 1 in both), so a whole-row dedupe leaves
11,584 rows. In each of the 5 pairs that differ only in `channel`, both copies carry the same
`updated_at` and one copy's channel is blank, so a rule of the latest `updated_at` needs a
tie-break, such as the copy with its channel filled in.

The new system holds 153 bookings dated 18 to 30 September, written month first (`09/18/2026`), with
its own references (`NB/ORD/000001`), site codes (`ORD-01` to `ORD-03`, `PHL-01` to `PHL-03`, carried
in the site list's `new_system_code`), patient numbers without the `P-` prefix, channels (`WALKIN`,
`WEB`, `CALL`, `MOBILEDRAW`) and states (`DONE` for 143 and `CXL` for 10). A strict day-first read,
such as pandas' `format="%d/%m/%Y"`, fails on all 153, since every day is 18 or later, and with
`errors="coerce"` turns them into blanks that a count drops, which brings the 23 percent back.
pandas' `dayfirst=True` instead falls back to month first when the day is above 12 and says so in a
UserWarning, "Parsing dates in %m/%d/%Y format when dayfirst=True was specified", so it reads them
right by accident (pandas 3.0.6, checked 4 October 2026).

A group that found all three reaches this answer. Bookings in the two metros fell about 12 percent,
from 1,415 to 1,243, and the 23 percent on the old report comes from the system switch. Month by
month across both systems the two metros book 488, 478 and 449 from April to June, then 452, 420 and
371 from July to September, so the fall was under way in August, before the switch, and the field
team has a fall of about 12 percent to explain.

### What made two rows one booking in the bookings group's count?

The translation probe comes from the row's "why this identity rule for bookings" and tests Week 1
Wednesday's move: which rows repeat, and what makes two rows one booking.

**"What did your group count as one booking, and why that rule?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| The booking id within the old system, since its export repeats rows; keeps one copy per id, the latest `updated_at` with a tie-break where two copies share a time; the new system's references are its own, so the two systems are stacked with a column naming the system and never deduplicated against each other | "We used drop_duplicates" | "How did you check the rule, and what count did it leave you?" (11,549 bookings from 11,729 rows in the old export; a whole-row dedupe would leave 11,584, since 35 of the 180 repeated pairs differ in a column; a learner who did it can say which rows the rule dropped.) |

### Why did the bookings group count from the files it chose, and what would the other choice have given?

The Grid prints which of the four each learner takes.

**P1. "How far does your group say bookings fell in the two metros, why do you trust that figure, and
what did your first count say?"** It tests Week 1 Tuesday's move: rung 1, is the drop real, confirmed in every
system.

| Did the work | Carried it | The follow-up |
|---|---|---|
| About 12 percent, 1,415 to 1,243, once the new system's bookings are in; the old export alone says 23 percent, 1,415 to 1,090; Chicago minus 13.0 and Philadelphia minus 11.2; confirmed by the old export's last date for the two metros, 17 September, against the new system's first, 18 September | Says 23 percent, or says 12 without being able to say where the other bookings came from | "Show me the cell or the log line that confirms it." (The count across both exports, with the old export's last date for the two metros, 17 September, and the new system's 153 bookings from 18 September.) |

**P2. "Which booking files did your group count from, why those, and what would the other choice you
weighed have given?"** It tests Week 1 Wednesday's move: profile before you count, and reconcile codes across two
sources.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Both exports: the old one's bookings to 17 September in the two metros and the new system's 153 from 18 to 30 September; mapped the sites through the site list's `new_system_code` (`ORD-01` to `KH-CHI-01`), the channel and state codes (`DONE` to completed, `CXL` to cancelled) and the patient numbers to the register's `P-` ids, and read the new system's dates month first | Names the old export only, or says "we merged the two files" with no mapping | "What did you check in each file before counting, and what did the checks find?" (Site, channel, state, patient number and date need converting; the date matters most, since a strict day-first read fails on all 153 and a coerced read leaves blanks a count drops, which brings the 23 percent back.) |

**P3. "Is the fall your group reports a real fall in patients booking, why do you read it that way,
and what would the other reading mean for the operations head's decision?"** It tests Week 1 Tuesday's move: the ladder's next rung, the same windows month by month.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Looked month by month across both systems: 488, 478 and 449 from April to June, 452, 420 and 371 from July to September, so the two metros were falling before 18 September, and the switch doubled how the fall looked | Treats the group's number as all real or all an artefact, with no months to show for it | "What would you ask the operations head, to explain the fall you found?" (What changed on the ground from August: staffing, opening hours, a competitor, a payer's network.) |

**P4. "Did your group's cleaning of the booking files move the two metros' fall, why, and what would
the fall have been without it?"** It tests Week 1 Wednesday's move: which copy stays.

| Did the work | Carried it | The follow-up |
|---|---|---|
| One row per booking id in the old export, the latest `updated_at` with a tie-break, logged with its count: 11,729 rows for 11,549 ids, 180 ids twice from a re-export, booked 1 June to 26 September; the repeats barely move the fall, 24.2 percent on raw rows against 23.0, since 35 of them are the two metros' Q2 rows and 9 their Q3 rows; stacking the new system's bookings moves it far more, from 23.0 to 12.2 percent | "We cleaned the data", with no count, or "it changed nothing" with no check | "Which step moved it most, and how did you check that step?" (Stacking the new system's 153 bookings, which takes the fall from 23.0 to 12.2 percent; the repeats move it about a point; a learner who did it checks by metro and quarter.) |

### What does the operations head push on, and what holds?

Push as the operations head, with the row that matches the caveat the learner gave.

| If the group's caveat is about | The push | Did the work | Carried it | The follow-up |
|---|---|---|---|---|
| Joining two booking systems, which the group has named | "Your caveat says the count depends on how the files are put together. I need one number to decide on staff: did bookings fall or not?" | Holds both halves: yes, they fell about 12 percent, from 1,415 to 1,243, and the 23 percent on the old report is the switch; the caveat is about the size of the fall, never whether it happened, and it names what would shrink it, the data team confirming the new system's export is complete to 30 September | Drops the caveat under the push and gives one number, or retreats to "it depends" | "What would you check tomorrow to make the caveat smaller?" (Whether the new system's export is complete to 30 September, by asking the data team for its count of bookings by day.) |
| The old export's repeated rows, which the group has named | "Your caveat says the export needed cleaning first. Does that make your fall bigger or smaller, and should I wait?" | Answers with the check: the repeats move the two metros' fall in the old export by about a point, 24.2 percent on raw rows against 23.0 on one row per id, so the caveat is about precision and the decision need not wait | Cannot say which way the repeats move the number | "What would let you drop that caveat?" (A re-export with one row per booking, or the data team naming which copy is current.) |
| Anything else, or no caveat | The general push, or for no caveat the question that asks for one | Names the check that would shrink the caveat and the decision it could move, with a number | Drops the caveat, or repeats it without a number | "What would you check tomorrow, and how long would it take?" (A named check, its size in rows or days, and the decision it could move.) |

---

## Sub-problem 3: which claims are still unpaid, how many dollars is that, and can finance trust the figure?

**Who needs the answer.** The finance head, who reports the collections figure at the quarter's close
and decides which unpaid claims the revenue-cycle team chases first. A wrong figure reaches the board
under the finance head's name, and a claim chased late can pass its payer's filing deadline.

**The questions on the way.** What did the finance head ask, and what does a finished answer report
as unpaid? What did the billing group's join keep, drop and repeat? Why did it class the postings as
it did? What does the finance head push on, and what holds?

### What did the finance head ask, and what does a finished answer report as unpaid?

> "The claims we billed say one thing and the posting system says another. Which claims are unpaid,
> how much money is that, and can I trust the figure I report?"
> The finance head, Kalpa Health, in brief 3

Four things in the billing files are planted, and no assessor names any of them: the posting system
keys claims in three formats, duplicate electronic remittance loads double-post, the employer claim
is unpaid, and denials post with nothing paid. An exact join of `claim_ref` to `claim_id` matches
216 of 11,343 postings, 1.9 percent: 216 carry the claim id (`KH-CLM-000095`), 2,269 a CLM-number
without its zeros (`CLM-95`) and 8,858 six bare digits (`000095`). Normalised to the six-digit
serial, every posting matches a claim. 280 double posts, the same claim and the same amount paid
twice by electronic remittance, 0 to 2 minutes apart, carry $19,204.63; 105 reversals take back
$8,662.87. 398 claims have no posting at all, $253,165 billed, spread over every month from April to
September, the $180,000 employer claim among them.

The claims file marks 1,175 of the 11,355 retail claims denied, 10.3 percent (Medicaid 14.9,
commercial 11.3, Medicare 8.8 and self-pay none), billing $230,132; 1,137 of them carry a denial
posting that pays $0.00, and the other 38 have no posting. By category the claims file counts 283
eligibility or coverage denials and 272 for missing or invalid information, and the denial postings
carry 269 and 265 of them. Billed across both quarters is $2,201,099; paid net of the double posts
is $801,313.56, 36.4 percent. The $1,399,785.44 between them is $883,254.70 of contractual
adjustments, $253,165 billed on claims with no posting, $222,108 billed on claims denied with a
posting, $32,594.87 of patient shares and $8,662.87 of reversals.

A group that found all four reaches this answer. Every posting is matched to its claim after the key
is normalised, the 280 double posts are counted once, and every claim is classed as paid, part paid,
denied or with no posting, with its dollars; collections are $801,314 against $2,201,099 billed, and
the gap splits into what the contracts never meant to pay, what was denied and what is still owed,
led by the $180,000 employer claim.

### What did the billing group's join keep, drop and repeat?

The translation probe tests Week 2 Tuesday's move: attach, count, explain the difference, then sum.

**"In Week 2 you joined payments to orders. Which columns did your group join on here, why those, and
how did you check what the join kept, dropped and repeated?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| An exact join matched 216 of 11,343 postings, 1.9 percent, because the posting system writes the claim three ways; normalised to the six-digit serial, every posting found its claim, the billed amounts agree on the matched pairs, and rows were counted before and after the join | "We joined on claim id", with a collected figure and no count before and after | "How many postings did your join match, out of how many, and how do you know that count is right?" (All 11,343 once the key is normalised to the six-digit serial, with the billed amount each posting carries confirmed against its claim's; an exact join matches 216, 1.9 percent. A learner who joined exactly and stopped gives 216 or 1.9 percent without seeing a problem, which is the evidence.) |

### Why did the billing group class the postings as it did, and what would the alternative have given?

The Grid prints which of the four each learner takes.

**P1. "Which postings did your group add up to get the paid figure, why those, and what would the
paid figure have been on the other rule you weighed?"** It tests Week 2 Tuesday's move: what makes a second posting a repeat.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Each payment once, net of reversals: 280 pairs with the same claim and the same amount, both electronic remittances, 0 to 2 minutes apart, $19,204.63, are a file loaded twice, counted once and listed for the posting team to confirm; 105 reversals take back $8,662.87; denials pay $0.00; adding every payment would give $820,518.19 against $801,313.56 | "We added up the payments", with no rule for repeats or reversals | "Show me the line in your decisions log for that rule, and the dollars it moved." (The rule for second payments, $19,204.63 left out, and the reversals, $8,662.87 taken back; a learner who did it finds the line in under a minute.) |

**P2. "Which claims did your group class as unpaid, why those, and how would the figure change if you
had drawn the line elsewhere?"** It tests Week 2 Tuesday's move: the rows with no partner, found by an anti-join.

| Did the work | Carried it | The follow-up |
|---|---|---|
| 398 claims with no posting, $253,165 billed, in every month from April to September, the $180,000 employer claim among them; says a September claim may simply not have been answered by 16 October; keeps denied claims as a class of their own | Gives a count with no dollars, or misses the claims with no posting at all | "Which unpaid claim would you chase first, and what would you ask about it?" (The $180,000 employer claim, asking its payment terms and who at the employer approved the invoice, since an employer may pay on terms longer than a quarter; then the oldest claims, nearest their payers' filing deadlines.) |

**P3. "What share of claims did payers deny, out of what, which did your group say to work first and
why, and what would working them in another order have cost?"** It tests Week 1 Monday's move: a rate with its denominator, on Week 2 Tuesday's
matched claims.

| Did the work | Carried it | The follow-up |
|---|---|---|
| 1,175 of the 11,355 retail claims, 10.3 percent, Medicaid highest at 14.9 and self-pay none, billing $230,132; 1,137 carry a denial posting that pays $0.00, and 38 have no posting; works first the denials a corrected claim can still win before the filing deadline | Gives a count with no denominator, or counts the $0.00 denial postings as payments | "What would change that order?" (Missing or invalid information, 272 claims, is corrected and resent, so it goes first while the deadline allows; eligibility or coverage, 283, needs the right payer found first; any claim near its payer's filing deadline goes first whatever its category. The denial postings carry 269 and 265 of the two, since 38 denied claims have no posting.) |

**P4. "Walk me from billed to paid in dollars, tell me which line of your bridge you trust least and
why, and what the paid figure would be if that line were wrong."** It tests Week 1 Wednesday's move: the bridge that names every dollar between two
totals.

| Did the work | Carried it | The follow-up |
|---|---|---|
| $2,201,099 billed; $801,314 paid net of the double posts, 36.4 percent; the $1,399,785 between them is about $883,255 of contractual adjustments, $253,165 on claims with no posting, $222,108 on claims denied with a posting, $32,595 of patient shares and $8,663 of reversals; trusts least the claims with no posting, since some are only late | Gives paid as the raw sum of payments, $820,518, or cannot bridge the two totals | "If finance's paid figure differed from yours, which line would you check first, and why that one?" (The double posts, since $19,205 is the whole gap between the raw sum of payments and the net paid figure; then the reversals.) |

### What does the finance head push on, and what holds?

Push as the finance head, with the row that matches the caveat the learner gave.

| If the group's caveat is about | The push | Did the work | Carried it | The follow-up |
|---|---|---|---|---|
| The second payments, which the group has named | "Your caveat says some payments in the file should not count. My team says the money is in the bank. Is your caveat hiding cash?" | Keeps the rule and says what would change it: the pairs sit 0 to 2 minutes apart on one claim and one amount, all from electronic remittances, which is a loading pattern; the list of 280 goes to the posting team to check against the bank deposits; if the bank shows two deposits, the payer overpaid and is owed a refund, which is money owed back, never revenue | Concedes the money may be there twice, or insists with no evidence | "Which single record would settle it for one of them?" (The bank deposit, or the payer's payment trace number on the remittance.) |
| Unpaid claims that may only be late, which the group has named | "Your caveat says some unpaid claims may only be late. Then which figure do I report as owed?" | Reports what is owed as billed on claims with no posting, $253,165, split by service month, and says the September claims may still be in transit while the oldest are at risk; names the next export as the check | Drops the late claims from the figure, or reports $253,165 as lost | "Which of those claims would you call lost, and on what rule?" (Only a claim past its payer's filing deadline, which the files do not hold, so none is called lost from these files alone.) |
| Anything else, or no caveat | The general push, or for no caveat the question that asks for one | Names the check that would shrink the caveat and the decision it could move, with a number | Drops the caveat, or repeats it without a number | "What would you check tomorrow, and how long would it take?" (A named check, its size in rows or dollars, and the decision it could move.) |

---

## Sub-problem 4: is KH-ATL-03 really worse at no-shows than the other centres, before anyone adds staff or closes it?

**Who needs the answer.** The patient service centres' operations head, who decides between a second
receptionist, reminder calls and a closure notice for KH-ATL-03. A centre closed on a rate read
wrongly takes a neighbourhood's nearest blood draw away, and a missed draw can mean a missed
diagnosis.

**The questions on the way.** What did the operations head ask, and what does a finished answer
advise? What did a fair comparison need, in the group's account? Why did it compare as it did? What
does the operations head push on, and what holds?

### What did the operations head ask, and what does a finished answer advise?

> "KH-ATL-03, one of our two Atlanta patient service centres, has the worst no-show rate on my Q3
> report. I am being asked to add a receptionist there or close it. Is the centre really worse?"
> The patient service centres' operations head, Kalpa Health, in brief 4

Two things in the visit register are planted, and no assessor names either: KH-ATL-03 runs by
appointment while the other centres' visit counts include walk-ins, who cannot miss a slot, and the
register is drawn from the bookings, so a rebooked patient's missed slot is a row beside the kept
visit. KH-ATL-03 has 80 visits: 79 scheduled and 1 walk-in, with 15 missed slots. On all visits it
reads 18.8 percent against 7.9 percent for the other eleven centres, whose 3,605 visits include 1,720
walk-ins, 47.7 percent; the next worst centre reads 9.8. On scheduled visits it reads 19.0 percent,
15 of 79, against 15.1 percent, 285 of 1,885; the next worst reads 18.5. If KH-ATL-03's true rate
were the others' 15.1 percent, 15 or more missed slots in 79 would happen with probability 0.21,
about one time in five; at that rate it would expect about 12, so three patients decide the gap. The
same check run on all visits, 80 at 7.9 percent, gives 0.0014, which reads as real and is the wrong
comparison. Of the register's 3,685 rows, 253 bookings have two: a missed slot and then the kept
visit. Counted per booking instead of per slot, 15 of KH-ATL-03's 64 scheduled bookings missed a
slot against 17.3 percent elsewhere, a gap chance produces with probability 0.13.

A group that found both reaches this answer. On scheduled visits, KH-ATL-03's 19.0 percent against
15.1 percent is a gap chance produces about one time in five, so neither a receptionist nor a closure
is supported by Q3; a cheap reminder trial, read against the other centres on scheduled visits, is.

### What did a fair comparison need, in the no-show group's account?

The translation probe comes from the row's "what a fair comparison needed in a clinic" and tests two
moves: Week 1 Thursday's, is the split fair, and Week 1 Monday's, a metric defined before it is
counted.

**"What did a fair comparison between KH-ATL-03 and the other centres need?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| The same denominator: about half of the other centres' visits are walk-ins, 1,720 of 3,605, and a walk-in cannot miss a slot, so missed slots are compared on scheduled visits; then the question is whether the gap on that base is more than chance on 79 slots | "We compared each centre's no-show rate" | "What is your group's rate out of, and why that base?" (Scheduled visits, 79 at KH-ATL-03 and 1,885 at the others, because only a booked slot can be missed; on all visits the others' walk-ins pull their rate down to 7.9 percent. A learner who used all visits names visits, which is the evidence.) |

### Why did the no-show group compare as it did, and what would the other base have given?

The Grid prints which of the four each learner takes.

**P1. "Which two numbers did your group compare to say whether KH-ATL-03 is worse, why those two, and
what would the other pair you weighed have said?"** It tests Week 1 Thursday's move: is the split fair.

| Did the work | Carried it | The follow-up |
|---|---|---|
| On scheduled visits, 19.0 percent, 15 of 79, against 15.1 percent, 285 of 1,885; the report's 18.8 against 7.9 percent came from the other centres' walk-ins | "It is 18.8 percent against 7.9, more than double" | "How many missed slots would KH-ATL-03 have had at the others' rate, and how many did it have?" (About 12, 15.1 percent of 79, against 15, so three patients decide the gap.) |

**P2. "Could chance alone give the gap your group found, why did you check it the way you did, and
what would you have told the operations head without the check?"**
It tests Week 1 Thursday's move: real, or the wobble.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Ran a chance check, coin flips or the binomial: at 15.1 percent, 15 or more missed slots in 79 happens about one time in five, 0.21, so the gap is within chance; at that rate the centre would expect about 12, three fewer | Says "it is significant" or "it is not significant" with no check named, or runs the check on all visits and reports 0.0014 | "Say that to the operations head in one sentence, without the word probability." (Such as: "If KH-ATL-03 were no worse than the others, a quarter this bad would still turn up about one quarter in five, so Q3 alone does not show it is worse.") |

**P3. "What did your group count as one no-show, why that, and what would the other count you
weighed have given?"** It tests Week 1 Monday's move: what one row stands for before anything is counted.

| Did the work | Carried it | The follow-up |
|---|---|---|
| One missed slot: 253 bookings have a missed slot and then the kept visit, so a rebooked patient's missed slot is a row beside the kept one; the rate counts slots, so both rows stay; counted per booking instead, 15 of KH-ATL-03's 64 scheduled bookings missed a slot against 17.3 percent elsewhere, and chance produces that gap with probability 0.13 | Has not looked at what a row stands for, or dropped one row of each pair without a reason | "Which of the two counts would the operations head want, and why?" (Slots for staffing the front desk, patients for reaching the people who miss draws; the group says which it used.) |

**P4. "The operations head is choosing between a receptionist, reminder calls and a closure. What does
your group advise, why that over the other two, and what would it cost to be wrong?"** It tests Week 1 Thursday's move:
is it worth acting on, and what does acting cost.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Neither a receptionist nor a closure on Q3's evidence, since the fair gap is inside chance; reminder calls before each booked slot at KH-ATL-03, read on scheduled visits against the other Atlanta centre, KH-ATL-02, at 14.3 percent, cost less than a receptionist and can be stopped, and a closure is the one action that cannot be undone for the patients who use the centre | Agrees with either action, because the rate "is the worst" | "What would change your advice?" (A fair gap that holds: KH-ATL-03 running well above the others on scheduled visits again next quarter, with a chance check on both quarters together that chance rarely matches, or reminder calls that fail to move it.) |

### What does the operations head push on, and what holds?

Push as the operations head, with the row that matches the caveat the learner gave.

| If the group's caveat is about | The push | Did the work | Carried it | The follow-up |
|---|---|---|---|---|
| Chance, the group having found the fair gap within it | "You say the gap could be chance. Your own rate is well above the others'. Why should I not act?" | Holds it with the number: on 79 slots, three patients decide the gap, and a gap this size appears by chance about one time in five; acting is fine when it is cheap and can be undone, and the caveat names what to measure next and for how long | Agrees the centre is worse, or repeats "not significant" with no number | "If you gave the operations head one action today, what is it and what would it cost?" (Reminder calls before each booked slot at KH-ATL-03 for a quarter, read on scheduled visits against KH-ATL-02; the cost is staff time on calls, and the trial can be stopped.) |
| The base of the report, which the group has named | "Your caveat says the report divides by the wrong visits. The report is the report. Why should I trust your number over it?" | Says what the report divides by and what it should: the others' 7.9 percent divides missed slots by visits that include 1,720 walk-ins; on scheduled visits the others run 15.1 percent; a decision about missed slots needs the base of slots | Gives way to the report, or cannot say what the report divided by | "What would you ask the report's owner to change?" (Count no-shows over scheduled visits, and print each centre's walk-in share beside its rate.) |
| Anything else, or no caveat | The general push, or for no caveat the question that asks for one | Names the check that would shrink the caveat and the decision it could move, with a number | Drops the caveat, or repeats it without a number | "What would you check tomorrow, and how long would it take?" (A named check, its size in slots or weeks, and the decision it could move.) |

---

## Sub-problem 5: did the free at-home collection offer lift bookings 9 percent, and should every patient in all six metros get it?

**Who needs the answer.** The marketing head, who wants to extend the offer to every patient in all
six metros, and Dr Menon, who signs the cost. Every free collection sends a phlebotomist to a home,
so an offer extended on a lift it did not cause spends that money every week for nothing.

**The questions on the way.** What did the marketing head ask, and what does a finished answer say the
offer did? Which Week 1 comparison did the campaign group run? Why did it compare as it did? What
does the marketing head push on, and what holds?

### What did the marketing head ask, and what does a finished answer say the offer did?

> "Our free at-home collection offer lifted bookings 9 percent. I want to offer it to every patient
> in all six metros. Can you confirm it worked?"
> The marketing head, Kalpa Health, in brief 5

Two things in the campaign files are planted, and no assessor names either: the offer went at random
to about half the patients in three metros that were already rising, Dallas, Atlanta and Phoenix,
and to about a fifth of the patients elsewhere, and inside the three metros an offered patient booked
less while the offer ran than one who was not offered. 2,381 patients were offered between 15 July
and 4 August, and 948 accepted; at least 259 of those show a collection at home between their offer
and 14 September, and 689 show none. Over 15 July to 14 September, offered patients booked 9.0
percent more per patient than the rest, 0.633 bookings against 0.581, and less in every campaign
metro: Dallas minus 10.8, Atlanta minus 19.9 and Phoenix minus 13.0 percent. The offer reached 50.5
percent of the three metros' patients against 21.4 percent elsewhere, and the three metros book more
per patient than the other three.

Before the offer, from 1 April to 14 July, offered and not-offered patients booked within about 6
percent of each other in each campaign metro, Dallas plus 1.4, Atlanta minus 5.2 and Phoenix minus
6.1, so nothing in the files shows how patients were chosen. The campaign metros rose 6.9 percent in
bookings per day over the two months before the offer, and 7.4 percent from those two months into
the offer's weeks, against 3.0 percent in New York over the same weeks. Outside the three metros the
gaps are chance: Chicago minus 4.8, Philadelphia plus 0.6 and New York plus 23.5 percent, a random
draw that a permutation test puts at p of about 0.03 (two-sided, 10,000 shuffles), so a group that
reads it as a lift has met a false positive.

A group that found both reaches this answer. The 9 percent compares where the offer went with where
it did not; inside every metro that got most of the offers, offered patients booked less, and the
files cannot say how patients were chosen, so the offer's effect is unknown; the next wave should
hold back a random share of eligible patients in every metro.

### Which Week 1 comparison did the campaign group run?

The translation probe tests Week 1 Thursday's move: did the discount work, read inside each segment.

**"In Week 1 you were asked whether a discount worked. What did your group compare here to answer the
same question, and what did the comparison show?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| Offered against not offered, split by metro: 9.0 percent more in total and less inside every campaign metro, by 10.8, 19.9 and 13.0 percent, so the 9 percent comes from where the offer went | Says "Simpson's paradox" with no metro numbers, or confirms the 9 percent | "Why is that comparison fair, and what could make it unfair?" (Where the offer went: about half the patients in Dallas, Atlanta and Phoenix against a fifth elsewhere, 50.5 percent against 21.4, counted from the campaign file against the patient list, and inside each of those metros offered patients booked less. A learner who did not look says the groups are large, so the comparison is fair.) |

### Why did the campaign group compare as it did, and what would the other comparison have given?

The Grid prints which of the four each learner takes.

**P1. "Did the offer lift bookings 9 percent, in your group's reading, why do you read it that way,
and what would the other comparison you weighed have said?"** It tests Week 1 Thursday's move: the aggregate against the split.

| Did the work | Carried it | The follow-up |
|---|---|---|
| The 9 percent is offered against not offered across all six metros; inside each campaign metro offered patients booked less, by 11 to 20 percent, so the 9 percent measures where the offer went, the metros whose patients book most | "Yes, 9 percent", or "no, it is a paradox" with no numbers | "So what did the offer do to bookings, in your reading?" (The files cannot settle it: they show who was offered and never how patients were chosen, so the gap inside a metro may come from who was chosen; a held-back share of eligible patients would settle it.) |

**P2. "What, besides the offer, could your group's comparison be picking up in the offer's weeks, why
did your group rule each one in or out, and what would your answer be if one of them were the cause?"** It tests Week 1 Thursday's move: what else changed, and the change beside the
change.

| Did the work | Carried it | The follow-up |
|---|---|---|
| The three campaign metros rose about 7 percent in bookings per day over the two months before the offer, and 7.4 percent from those two months into its weeks, against 3.0 percent in New York, so the rise was under way before the offer | Names nothing besides the offer, or never looked before the offer | "What comparison would you need to credit the offer with a change in bookings?" (Patients like the offered ones, in the same metros and the same weeks, who were not offered: a share held back at random before the offer, compared over the same weeks.) |

**P3. "How did your group decide whether the patients who got the offer were like the ones who did
not, why that way, and what would the other way have shown?"** It tests Week 1 Thursday's move: who got the sale, and is the
split fair.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Compared offered and not-offered patients in each campaign metro before the offer: within about 6 percent of each other, Dallas plus 1.4, Atlanta minus 5.2 and Phoenix minus 6.1, with the sign changing, so nothing before the offer separates them, the gap opens inside its weeks, and the files cannot say how the offer was assigned | Asserts that the offer went to patients who were already drifting, or that it was random, without comparing the two groups before the offer | "How would you design the next wave so the question can be answered?" (Hold back a random share of eligible patients in every metro, and compare bookings per patient over the same weeks.) |

**P4. "Did the offer work in any single metro, in your group's reading, why do you say so, and what
would make you say the opposite?"** It tests Week 1 Thursday's move: real, or the wobble, read with how many places were looked
at.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Chicago minus 4.8, Philadelphia plus 0.6, New York plus 23.5 percent; ran a shuffle on New York and got about 0.03; says New York is one striking gap among six metros looked at, and Week 1 showed a small share turning up where nothing changed, so it is no evidence of a lift until a fresh wave repeats it | Reads New York's 23.5 percent as the offer working in New York | "How many metros did your group look at before reaching that reading, and what does that do to how sure you can be?" (Six; a check that chance alone passes about one time in twenty will pass now and then when six places are looked at, the way Week 1's twenty segments where nothing changed gave one at 0.003, so New York needs a fresh wave with a held-back share before it counts.) |

### What does the marketing head push on, and what holds?

Push as the marketing head, with the row that matches the caveat the learner gave.

| If the group's caveat is about | The push | Did the work | Carried it | The follow-up |
|---|---|---|---|---|
| The comparison across metros, the group having split by metro | "Patients took the offer up. You cannot prove it did nothing; your caveat is just doubt, and I need budget for all six metros." | Agrees the files cannot prove harm or help, which is the caveat's point; acceptances count people who said yes to a free service, and at least 259 of the 948 show a home collection in the offer's weeks; offers the next wave as the test, the offer to a random part of eligible patients in every metro with the rest held back, so the budget buys an answer | Says the offer failed, or gives in and agrees it worked | "How large a held-back share would you ask for, and what would you compare?" (A share the marketing head can afford to leave without the offer, such as a fifth, in every metro, comparing bookings per patient over the same weeks; how large a share it takes to see a given lift is a later week's question.) |
| The one metro that stands out, which the group has named as chance | "Your own numbers show one metro well up. Why not at least roll it out there?" | Says the gap is one of six looked at, with a shuffle p of about 0.03, the kind of gap chance turns up now and then when several places are looked at; offers that metro a fresh wave with a held-back share, which answers the question in one more wave | Agrees to roll it out in that metro | "What result in the next wave would change your mind?" (A gap of that size again in New York against a share held back at random in the same weeks.) |
| Anything else, or no caveat | The general push, or for no caveat the question that asks for one | Names the check that would shrink the caveat and the decision it could move, with a number | Drops the caveat, or repeats it without a number | "What would you check tomorrow, and how long would it take?" (A named check, its size in patients or weeks, and the decision it could move.) |

---

## What would each learner do differently?

**Who needs the answer.** The assessor scoring the last 3 marks, which reward a learner who can name
a better path from their own log, never a general lesson.

**The questions on the way.** What is the probe? What does a learner who kept an honest log say? What
do you ask if the log is thin?

**"From your challenges log: what would you do differently if you started this sub-problem again
tomorrow?"** It tests Week 1 Friday's move: rebuilding the week alone and naming the step you do not
own yet.

| Did the work | Carried it | The follow-up |
|---|---|---|
| Opens the log, finds an entry they wrote, names the step they would move earlier or do another way, such as profiling every file before any count or asking the data team on the first day how each file is keyed, and the time or error it would have saved | Gives a general lesson ("manage time better"), or reads a group-mate's entry as if seeing it for the first time | "Which entry shows the moment you should have changed course, and what told you?" (An entry with its step and the signal that was missed, such as a count that did not reconcile; a learner who carried the work cannot point to one.) |

If the group's challenges log has only a few entries by Thursday, note it, and ask about the decisions
log instead: **"Pick one line in the decisions log and tell me who decided it and what they looked at."**

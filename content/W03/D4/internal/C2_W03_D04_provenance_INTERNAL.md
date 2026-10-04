# Where did every part of Build 1 Thursday's pack come from, and what does each number rest on?

**INTERNAL.** The record behind `content/W03/D4`: its sources, the data command, every number the
files quote with its witness, the plants and where each is used, every decision that departs from a
source, everything invented, each link with its check date, the tool versions and the depth loop.
The pack was first built on 29 September 2026 in the India setting (#163, with changes in #177 and
commit 0269e51). This rebuild, on 1 October 2026 on branch `w03-d4`, moves it to Kalpa Health's US
setting and standard v3.

---

## Which sources set the pack, and what did each give?

| Source | What it gave the pack |
|---|---|
| `CLAUDE.md` | The build workflow, the hard rules, the folder and naming rules, the ground-truth order |
| `.claude/skills/day-pack-builder/references/the-standard.md` | The question ladder, the self-contained rule, the depth loop, the interview bar |
| `.claude/skills/day-pack-builder/references/artifact-manifest.md`, "Weekly and build-week variations" | The build-week pack in place of the teaching manifest: no tests, no Kahoot |
| `docs/detailing/W03_build1_spine.md` (approved 29 September 2026) | Thursday's line (Mock R1 for every learner at about 20 minutes, a technical half on Weeks 1 and 2 and a viva on the group's work, build completion around the roster), the rubrics block and the plant table |
| `docs/curriculum/W3_Build_1.md`, Thursday's row and Monday's row | The scenario, the thinking the viva probes ("why this tree for a lab, why this identity rule for bookings, what a fair comparison needed in a clinic"), the agenda (the roster all day, the 15-minute close), the mock owners, the after-class task, the `[S]` interview angle and the GeeksforGeeks calibration link |
| `docs/programme/calendar.md`, lines W03/D1 to W03/SAT | Thu 22 Oct 2026, build week, Module 1, no faculty block, rendered through `sync:module:W03/D4` and `sync:day-date:W03/D4`; the freeze on Friday and grade closure on Saturday |
| `docs/07_Client_Zero.md`, section 1c | Kalpa Health in the US: six metros, four payer types, claims and remittances in dollars, seven denial categories, calendar Q2 and Q3 |
| `data/programme/facts.yaml` | The campus day (two blocks of 180 minutes); the cohort (35 learners, nine groups, both stated); the marks per event (mini project 40, mock 30, GD 30); `evaluation.rubrics.W03`, locked and `learner_facing: allowed`, rendered as `sync:rubric:W03/mock` and read by the workbook builder, with the mini project's rows the viva file cites; the decisions `build1-rubrics`, `build1-us-data`, `build1-register-from-bookings`, `four-domains`, `chapter-standard`, `question-ladder`, `self-contained`, `humanizer`, `opus-max` and `plants-once-found`; the `groups` conflict |
| `docs/01_Programme_Facts_C2.md`, people and bodies | The roles: Programme Head, Principal Advisor, Academic TA, Support TA, on-ground manager |
| `content/W03/D1/briefs/` (merged in #215) | The five askers' questions word for word, each brief's title question, the data dictionary's file grains and the logs' locations; brief 2 leaves the two metros unnamed, so no spoken probe names them |
| `content/W03/D1/trainer/C2_W03_D01_day_sheet_TRAINER.md` | The plant table with its witness numbers, and the stuck-group questions Thursday's day sheet copies word for word, cut to the first question for sub-problems 2 and 4 |
| `content/W01/D3/study-notes/C2_W01_D03_notes_STUDENT.md` | Week 1 Wednesday's figures for the T03 family's opening: the dashboard's Rs 2.1 crore for Q1 against the books' Rs 1.9 crore, Rs 20 lakh apart |
| `content/W03/D1/briefs/`, briefs 1, 2 and 4 | Brief 1's way B, the split by payer that asks whether customers paid more or the mix changed, which puts T02-L3 close to revenue; brief 2's unnamed metros, which cut sub-problem 2's second stuck-group question; brief 4's three actions, which the no-show probe names |
| `content/W03/D1/study-notes/C2_W03_D01_domain_us_healthcare_STUDENT.md` | The domain's terms (allowed amount, deductible, days in accounts receivable, denial), Medicare's definition with "some younger people with disabilities", and what the lab does next for each denial category, which the viva's denial follow-up uses |
| `content/W03/D1/data/`, written by `data/generate_kalpa_health.py` | Every Kalpa Health number in the viva prompts and the day sheet |
| `docs/curriculum/W1_Data_analysis_found.md` and `W2_Data_manipulation.md`, the interview-angle columns | The anchor of every technical question, quoted word for word |
| `docs/detailing/W01_W02_spine.md`, and the Week 1 and 2 packs merged on main (#203, #206 to #210, #217, #219 to #222) | The traps each family reuses, each move's name as those packs teach it, and the cases each family's opening names (Meera Raghavan, Anand Iyer, Retail-Plus, the monsoon sale, the protect list, the growth team's table, the chief of staff's workbook) |
| `content/W01/D4/study-notes/C2_W01_D04_notes_STUDENT.md`, chapter 6, and `slides/C2_W01_D04_half2_STUDENT.md`, the notes on the last interview question | Week 1 Thursday's four ways to ask whether a change worked (before and after, the change beside the change, inside each segment, the random hold-back), which T04-L3 now stays inside; the hold-back of a fifth; power as a later week's topic; and "about one in twenty" as recognition only, so the viva's New York probe carries no multiple-testing formula |
| `content/W03/D3/checkpoints/C2_W03_D03_checkpoint_guide_TRAINER.md` (first wave, India setting) | Read only to compare Wednesday's nudges; Thursday uses Monday's US questions instead |

Skills read and used: day-pack-builder (the standard, the manifest's build-week variations);
mini-project-designer (viva questions climbing from easy to hard, the faculty-notes split); exercise-
builder (design items, the device wheel, used to decide that the oral mock carries no option set);
xlsx (formulas LibreOffice evaluates, input cells, the recalc); humanizer and llm-tic-scrubber (the
prose read and the scanner); research (primary sources for every real-world fact).

---

## Which real-world facts appear, and where was each checked?

| Fact | Where it appears | Source and check dates |
|---|---|---|
| Quest Diagnostics assesses its testing business on "volume (measured by test requisitions) and revenue per requisition" | Question bank, T01-L1 | Quest Diagnostics, Form 10-K for 2025, https://www.sec.gov/Archives/edgar/data/1022079/000102207926000015/dgx-20251231.htm (checked 1 October 2026 with WebSearch, which returned it as the FY2025 10-K, and WebFetch; checked again on 4 October 2026 by downloading the filing, where the sentence reads "We assess our revenue performance for our DIS business based upon, among other factors, volume (measured by test requisitions) and revenue per requisition") |
| Revenue per requisition rose 0.1 percent in 2025 while it rose 2.4 percent on an organic basis, because the acquired LifeLabs "has a lower revenue per requisition" | Question bank, T02-L3, now set as a dilution, the shape these figures show | The same filing, management's discussion of 2025 (checked 1 October 2026, and again on 4 October 2026, where it reads "Revenue per requisition increased by 0.1% ... offset by the impact of the acquisition of LifeLabs, which has a lower revenue per requisition. On an organic basis, revenue per requisition increased 2.4%") |
| Days sales outstanding, "a measure of billing and collection efficiency", was 48 days at the end of 2025 | Question bank, T06-L3 | The same filing, cash flows section (checked 1 October 2026, and again on 4 October 2026: "was 48 days as of both December 31, 2025 and 2024") |
| GeeksforGeeks, "Data Analyst Interview Questions and Answers", 95 numbered questions, last updated 24 July 2026, with "what is data cleaning" and "how do you handle missing data" among them | Question bank's calibration section; day sheet | https://www.geeksforgeeks.org/data-analysis/data-analyst-interview-questions-and-answers/ (checked 1 October 2026 with WebFetch; checked again on 4 October 2026 by downloading the page, which WebFetch was refused: the title, 95 numbered questions, a `dateModified` of 2026-07-24, and questions 10, "What is data cleaning?", and 11, "How do you handle missing data in a dataset?") |
| "The SUBTOTAL function ignores any rows that are not included in the result of a filter, no matter which function_num value you use", and 101 to 111 also ignore rows hidden by the Hide Rows command | Question bank, T10-L2's follow-up | Microsoft Support, "SUBTOTAL function", https://support.microsoft.com/en-us/office/subtotal-function-7b027003-f060-4ade-9040-e478765b9939 (checked 1 October 2026 with WebFetch, and again by the second-round reviewer on 4 October 2026, who found both sentences quoted faithfully) |
| "If you have Medicare and other health insurance ... each type of coverage is called a 'payer'", and "The 'primary payer' pays up to the limits of its coverage, then sends the rest of the balance to the 'secondary payer'" | Question bank, T09-L2's model answer | Medicare.gov, "How Medicare works with other insurance", https://www.medicare.gov/supplements-other-insurance/how-medicare-works-with-other-insurance (checked 1 October 2026 with WebFetch, and again by the second-round reviewer on 4 October 2026) |
| pandas' `to_datetime(..., dayfirst=True)` reads "09/18/2026" as 18 September and prints a UserWarning that it parsed the dates as `%m/%d/%Y`, while `format="%d/%m/%Y"` fails on it and `errors="coerce"` turns it into a blank | Viva prompts, sub-problem 2's plant paragraph | Run on pandas 3.0.6 in session on the new system's 153 dates. On 1 October 2026 the run gave month 9 for all 153 and was recorded as silent, because warnings were not shown; the second-round reviewer and this session's rerun on 4 October 2026, with warnings shown, both print "UserWarning: Parsing dates in %m/%d/%Y format when dayfirst=True was specified". The strict format raised ValueError, and coerced, gave 153 NaT |

No other real company, figure or rule appears. The deductible, coverage, Medicare and claim terms in
the bank, the brief and the viva are the domain dossier's, in its own words.

---

## Which command makes the data, and how were the numbers rechecked?

The pack copies no data. Its Kalpa Health numbers come from Monday's data pack, which
`python3 data/generate_kalpa_health.py --out content/W03/D1/data --stem C2_W03_D01` writes. On 1
October 2026 that command, pointed at a scratch folder, wrote ten files byte-identical to the
committed ones; `--contract` printed `PASS  every plant holds`; and `--witness` printed every figure
the spine carries. Monday's `internal/C2_W03_D01_witness_check_INTERNAL.py` ended
`RESULT: PASS (0 drifts from the spine and the day sheet)`. On 4 October 2026 the same command
again wrote ten files byte-identical to the committed ones, `--contract` passed, and Monday's witness
check passed.

This pack's own script, `internal/C2_W03_D04_numbers_INTERNAL.py`, reads the committed CSV files and
the day's markdown with the standard library alone, asserts every number below, and ends
`RESULT: PASS (0 drifts)`. Its New York permutation test shuffles with seed 20261019, the same seed
as Monday's script.

---

## What does each number in the pack rest on?

### What do the viva prompts' and the day sheet's Kalpa Health figures rest on?

| The figures | Where they come from |
|---|---|
| The headline: 23,213 to 24,406 tests, 5.1 percent; on raw rows 23,788 to 24,556, 3.2 percent; tests booked 7.8 percent (to 25,022); tests performed 8.6 percent (22,468 to 24,399); bookings 5.6 percent (5,692 to 6,009); 1,200 screenings of five tests adding 6,000; with the contract in, tests performed 35.3 percent, tests booked 33.6 and bookings still 5.6, the contract being one booking | The spine and the generator's witness; the readings with the contract in computed by the numbers script |
| Sub-problem 1: KH-CLM-007802, EMP-0007, Dallas, 6 August 2026, $180,000, 14.6 percent of $1,231,001; Q2 $970,098; growth 26.9 and 8.3 percent; Q3 to $1,051,001; means $210.50, $179.75 and Q2's $176.13; median $150 in both quarters; 22,152 claim lines (21,050 and 1,102); 46,867 and 48,235 tests; Q3's 11,395 lines and 24,399 tests; 60 text amounts, 32 in Q2 ($5,390) and 28 in Q3 ($5,169) | The spine and Monday's day sheet; the Q3-only counts and the text amounts by quarter counted by the numbers script |
| Sub-problem 1's shortfall: the plan of $1,144,716, $93,715 short; Chicago $30,437 and Philadelphia $32,999, $63,436 together, 67.7 percent, from 24.5 percent of Q2's billing; New York $21,909, Dallas $15,867, Phoenix $3,659, Atlanta $11,156 ahead; Chicago and Philadelphia's billed charges $124,097 to $115,997 and $114,014 to $101,538; payer shortfalls from $16,044 to $28,437 | Computed by the numbers script: Q2's billed charges outside the contract times 1.18, against Q3's, by metro and by payer, the reading brief 1 gives the finance head |
| Sub-problem 1's payers: billed charges up 13.0 percent commercial, 6.0 Medicare and 1.6 Medicaid, down 2.2 self-pay; short of each payer's own plan by 4.2, 10.2, 13.9 and 17.1 percent; Medicaid 25.3 percent of the shortfall from 14.9 percent of Q2's billing; Medicare $28,437 of the shortfall, 30.3 percent, the most dollars; self-pay 17.1 percent of the shortfall from 8.2 percent of Q2's billing; outside the two metros commercial up 20.8 against 3.5 to 7.6 | Computed by the numbers script after the rigor review found "no payer stands out" wrong; the Medicare and self-pay readings added after the second round found the follow-up accepted Medicaid's alone |
| The whole-body wellness panel: one line at $299, twelve tests whose list prices add to $785 | The test catalogue and the booking-tests file, by the numbers script |
| Sub-problem 2: 1,415 to 1,090 (minus 23.0) and to 1,243 (minus 12.2); Chicago 754, 571, 656; Philadelphia 661, 519, 587; the other four metros' changes; 11,729 rows, 11,549 ids, 180 repeated ids from 1 June to 26 September; 145 identical pairs and 35 that differ (29, 5 and 1), the 5 sharing `updated_at` with one channel blank; 11,584 rows after a whole-row dedupe; 153 new-system bookings from 18 to 30 September, 143 DONE and 10 CXL; months 488, 478, 449, 452, 420 and 371; repeats in the two metros 35 in Q2 and 9 in Q3; minus 24.2 percent on raw rows | The spine and Monday's day sheet for the headline counts; the pairs, the ties, the months, the repeats by quarter and the raw-row fall counted by the numbers script |
| Sub-problem 3: 216 of 11,343 postings, 1.9 percent; 216, 2,269 and 8,858 by format; 280 double posts, $19,204.63, 0 to 2 minutes apart, all ERA; 105 reversals, $8,662.87; 1,137 denial postings at $0.00; 398 unposted claims, $253,165, in all six months, the employer claim among them; 1,175 of 11,355 denied, 10.35 percent, by payer 14.9, 11.3, 8.8 and none; $230,132; 38 denied with no posting; 283 and 272 in the two largest categories, 269 and 265 among the denial postings; $2,201,099 billed; $801,313.56 paid, 36.4 percent; $820,518.19 raw; the bridge $883,254.70, $253,165, $222,108, $32,594.87 and $8,662.87 | The spine and Monday's day sheet; the gaps between double posts, the channels, the months and the category counts by the numbers script |
| Sub-problem 4: KH-ATL-03's 80 visits, 79 scheduled, 1 walk-in, 15 missed; 18.8 and 19.0 percent; the others' 3,605 visits, 1,720 walk-ins (47.7 percent), 1,885 scheduled, 285 missed, 7.9 and 15.1 percent; next worst 9.8 and 18.5; chance 0.21 and 0.0014; 11.9 expected; KH-ATL-02 at 14.3; 3,685 rows; 253 bookings with two rows; 15 of 64 bookings against 17.3 percent, chance 0.13 | The spine's sub-problem 4 row as re-planted by #218 on 1 October 2026, and Monday's day sheet; the walk-in counts and KH-ATL-02 by the numbers script |
| Sub-problem 5: 2,381 offered from 15 July to 4 August; 948 accepted, 259 who used it and 689 who did not; 0.633 against 0.581 bookings per patient, 9.0 percent; the six metros' gaps; 50.5 against 21.4 percent offered; the gaps before the offer; 6.9, 7.4 and 3.0 percent; New York's p of about 0.03 | The spine and Monday's day sheet; the per-patient rates and the 7.4 by the numbers script |
| Q2's 91 days and Q3's 92 | The calendar |

### What do the question bank's invented numbers rest on?

Every number in a technical question is invented for it and lies outside the ten files; the numbers
script checks the arithmetic of each.

| Question | Invented figures, and the arithmetic the model answer uses |
|---|---|
| T01-L1 | A board plan of 12 percent more revenue |
| T01-L2 | A mean turnaround of 31 hours against a median of 16, a 24-hour promise, 88 percent within it |
| T01-L3 | $400,000; 600 practices; 120 to 108 requisitions per practice, 10 percent, 7,200 fewer |
| T02-L1 | Cash down 16 percent in February 2026 against January; one plan at 70 percent of cash paying on Fridays; February's four Fridays against January's five, so 14 points of the 16; 28 days against 31, both checked on the 2026 calendar |
| T02-L2 | Patients' share 11 percent in December, 19 in January, 18 last January |
| T02-L3 | From the third quarter of 2025 to the fourth, about 3 percent more allowed per test for every payer type against 0.5 percent for the lab, so a mix effect of about 2.5 points (1.005 over 1.03 is 2.4 points down); Quest's two figures |
| T03-L1 and L3 | 4,180 pickups invoiced against 3,960 logged; 130, 70 and 20 set aside, 220; $16 a stop, $2,080, $1,120, $320 and $3,520 |
| T03-L2 | An Austin register of 9,400 rows |
| T04-L1 | p of 0.04, chosen because New York's false positive in sub-problem 5 sits at 0.03 |
| T04-L2 | 2 rejections in 25 draws against 4 percent on 2,400; one draw moves the rate 4 points; chance 0.26; 8 or more in 100 at 4 percent, 0.048 |
| T04-L3 | The Austin lab's necessity denials on Medicare claims, 6.0 to 3.5 percent from March to June 2025, other payers 5.8 to 3.6, a 2.2-point fall against Medicare's 2.5; if all 2.5 points were the rule's, 4,000 Medicare claims a month would see 100 denials prevented and at most 20 forgone by a fifth held back |
| T05-L1 | 94 to 89 percent within the promise; 61 percent of late samples on two of eleven routes carrying 18 percent, now given in the ask so no learner reaches for their own group's work |
| T05-L2 | 1,900 of 42,000 and 2,300 of 52,000, 4.5 and 4.4 percent; 21 and 24 percent growth; 5.5 percent and 400 more if volume were flat |
| T05-L3 | 40 draws a day by a test centre's third month |
| T06-L1 | 2,000 tests an analyser |
| T06-L2 | 37 redraws over 2,400 draws, 1.5 percent, returned as 0 |
| T06-L3 | Quest's 48 days |
| T07-L2 | 41,200 claim lines in the last quarter of 2025 becoming about 79,600 rows, 1.93 times |
| T08-L3 | Practices 25th and 26th in Dallas tied on 61 requisitions, so RANK ships 26, and 25 once a unique tie-break is in the ORDER BY |
| T09-L3 | 90 days, a week-old extract, true counts of 84 to 90 days read as 91 to 97 |
| T10-L3 | 91.8 percent of 48,300 samples against 94.1 percent |

### What do the day sheet's, the roster's and the scoring sheet's figures rest on?

| The figures | Where they come from |
|---|---|
| 20-minute mocks and a 15-minute close | The row |
| A 5-minute changeover and a 10-minute huddle | This pack's choice, kept from the first build |
| Two blocks of 180 minutes | `data/programme/facts.yaml`, campus day |
| 35 seats in nine groups, eight of four and G9 of three | `data/programme/facts.yaml`, cohort, both stated; the default every Build 1 workbook uses until Monday's allocation |
| 6 slots a block, 36 places, the last mock at minute 145 of block 2 and the Principal Advisor's at minute 120; 12, 12 and 11 learners | The roster's formulas, asserted by its recalc manifest and by the numbers script's grid section |
| The slot grid printed in the day sheet | The numbers script parses the day sheet's table and checks it against the call order; the roster's Grid sheet gives the same rows after recalculation |
| Eight sets, eighteen swaps, six questions in no set, and 280 reserve rows | The bank's tables; the workbook builder derives the swaps from its closeness map and the reserves from its rule, and asserts that no learner meets a question close to their sub-problem, no seat holds one family twice or one week only, no two group-mates share a question, and every seat of every group a seating can make has three fresh reserves, shared only where the levels force it (one pair on sub-problem 2, one on 5 and three on 3, in groups of four); the numbers script recomputes both from the bank's printed tables by its own search; the roster's flips put every group on each sub-problem in turn and read zero on all three checks |
| Checks of 18, 27 and 45 minutes | Two, three and five minutes a group across nine groups, this pack's choice |
| Six criteria with maximums 8, 4, 3, 6, 6 and 3, adding to 30 | Read from `evaluation.rubrics.W03.events.mock` by `internal/C2_W03_D04_build_workbooks_INTERNAL.py` |

---

## Where is each plant used, and which files name none?

| Plant | Where it appears | Audience |
|---|---|---|
| The headline's dashboard count and the employer contract's tests | Viva prompts, the headline section's plant paragraph and the expected answers; day sheet's plant table | TRAINER |
| 1. The employer contract, panels on one claim line, the text amounts | Viva prompts, sub-problem 1; day sheet | TRAINER |
| 2. The system switch, the re-export's repeats, the month-first dates | Viva prompts, sub-problem 2; day sheet | TRAINER |
| 3. The claim-key formats, the double posts, the unpaid employer claim, the denials at $0.00 | Viva prompts, sub-problem 3; day sheet, its plant table and the one-breath answer, marked never to be read to the room | TRAINER |
| 4. KH-ATL-03 by appointment against the others' walk-ins, the register drawn from the bookings | Viva prompts, sub-problem 4; day sheet | TRAINER |
| 5. The offer's targeting and New York's false positive | Viva prompts, sub-problem 5; day sheet | TRAINER |

The one STUDENT file, `mocks/C2_W03_D04_mock_brief_STUDENT.md`, names no plant: the numbers script's
guard searches it for 43 plant words, 151 planted values and 11 rounded or spoken forms, the values as
whole numbers with or without a dollar sign, and finds none. It names the five askers' questions as
Monday's briefs word them, which include Dr Menon's 5 percent, the two metros, KH-ATL-03 and the
marketing head's 9 percent, all of them the briefs' own public words. The same guard runs over
everything an adult reads aloud: the bank's 60 asks and follow-ups and its 30 anchors (their words,
since an anchor is spoken with the ask's numbers); the viva's 85 spoken lines, 32 in bold (probes, the
general push and the fallbacks) and 53 in the push and follow-up columns, with the assessor's
bracketed answers removed and any bracket inside a quote kept; the day sheet's 17 spoken lines, its
scripts, check questions and eight stuck-group questions, which may name the `claim_ref` column since
a column's name says where to look; and every line the assessors' guide quotes. It finds none. The
guard first proves itself on 21 hints in the forms the second-round reviewer slipped past its first
version, a dollar sign, a rounded rate, a rate in words, a date, a phrase, and on six of the bank's
invented figures it must leave alone. Run over the viva as first committed (62979d2), the strengthened
guard finds 17 hits where the first version found 7; run over the viva as round one left it (5d6cff0),
it finds 7, all in the caveat pushes the second round reported (two booking systems, second payments,
nineteen percent, hundreds of patients, a fifth). It cannot catch a line that steers in plain words,
such as the follow-ups the second round found pointing at what one claim line stands for or at a
join's first try, so the second round's reviewer and this session read every spoken line for meaning,
and every probe now opens on the group's own work and asks why and what the other way would have
given. Decision `plants-once-found` covers only a regular week's Saturday paper, so no Build 1 file
relies on it.

---

## Where does the pack depart from a source, and why?

| Decision or departure | Why |
|---|---|
| The technical half moves to Kalpa Health's US setting and sits outside the ten files | The requester asked that every file speak the US setting. Most Week 1 and 2 traps are the same mechanisms Build 1 plants in the data, so each question sits in a corner of Kalpa Health no sub-problem touches, on invented numbers, and the bank says so to the assessors and the brief says so to the learners. |
| Fourteen questions in the sets are swapped for a learner whose group's viva they rehearse, eighteen swaps in all, each for the same level's question from the set four letters on; four cells of the set table and the six questions in no set changed to make that possible | The first round's rule repeated a reserve in a group, and the second round found four more close questions (T03-L2 to billing, T02-L3 to revenue, T05-L3 to the offer, and T04-L3 sitting in the claims file's own months) and seats left on one week's moves. With the wider closeness map no hand-made table held, so a constraint search (OR-Tools CP-SAT, run once in session) found the table nearest the old one in which every swap lands away from the same sub-problem and every set and swapped seat keeps three families and both weeks; the builder and the numbers script prove it from the bank's printed tables |
| Each learner's three reserves are printed on the Grid, drawn from the six questions in no set and from the sets the group does not hold, and two group-mates can share one | The first rule left the assessor to pick from a table and could put two questions from one family in a seat. Printed reserves never repeat a family and never come from the group's own questions. Some sharing is forced by counting: on sub-problem 3 a group of four is asked four of the six L3 questions away from billing, which leaves two fresh ones for four members, so the builder shares only where the levels force it, one pair on sub-problem 2, one on 5 and three on 3, and an assessor who has already asked a group-mate the reserve keeps the learner's own question and goes straight to its follow-up |
| The viva's seat probe rotates by the group's place among the groups on its sub-problem, where it was fixed by seat | The seat list learners receive carries the seat number, so a fixed seat-to-probe rule let a learner tell a same-seat learner in a later group which probe to expect |
| T04-L3 is set in the Austin lab in 2025, where it was Kalpa Health's Medicare claims in 2026, and is not mapped close to billing | The second round found the 2026 scene inside the claims file's months, where Medicare's necessity denials rise from 2.05 to 3.02 percent rather than fall from 6.0 to 3.5. In Austin in 2025 no file touches it; what remains near billing is the topic of denials, and sub-problem 3's viva asks which denials to work first, never whether a rule cut them. It stays mapped close to the offer, whose move it shares |
| T02-L1 is February against January 2026, T02-L3 the third and fourth quarters of 2025, and T07-L2 the last quarter of 2025 | Read as Q3 2026, T02-L1's fall and T02-L3's rates contradicted the remittances and claims files; February also gives the four Fridays against five the follow-up needs |
| T01-L3's third way is a few days of calls to the practices whose orders fell most, where it was a random-half test | The random-half test rehearsed sub-problem 5's hold-back; the question's move is which branch to fund, and the calls keep it there |
| T06-L3, T08-L1 and T08-L3 stay unmapped though their follow-ups turn on a tie with no tie-break | The second round named them near sub-problem 2's five pairs that tie on `updated_at`. A tie at a rank's line is a different mechanism from choosing one copy of a repeated booking, and sub-problem 2's viva never asks about the tie, which appears only in the assessors' expected answer. T09-L2, whose follow-up keeps one of two copies by chance, is mapped close to bookings |
| An anchor is spoken with the ask's numbers in place of its own | The guide lets an assessor ask the anchor to a learner who stalls, and two anchors carry values the files plant, T04-L1's p = 0.03 and T04-L2's 1,200 |
| T02-L3 asks about a dilution, every payer up about 3 percent and the lab up 0.5, where it asked about a reversal | The reversal mirrored sub-problem 5's plant, and Quest's 2025 figures are a dilution, so the question now matches its own example |
| p = 0.04 in T04-L1 | New York's false positive in sub-problem 5 sits at about 0.03, the value the Week 1 row's anchor quotes, so the spoken question uses another value |
| Sub-problem 1's finished answer reports the payers' uneven growth as a second finding | The spine's row names the metros only, and the rigor review found "no payer stands out" wrong; a learner who reports the payer gap is scored as having found a real pattern |
| The viva's New York probe asks how many metros were looked at, with no 1 minus 0.95 to the sixth | Week 1 Thursday keeps "about one in twenty" as recognition only and lists multiple-testing corrections under Stop before |
| The stuck-group questions are Monday's, with sub-problems 2's and 4's cut to their first questions | Monday's day sheet holds the approved questions for a group that has found nothing. Sub-problem 4's second names its planted denominator, 79 slots, and sub-problem 2's, "Where are Chicago's bookings after mid-September?", names one of the two metros brief 2 asks the group to find and the switch's timing |
| The brief and a learners' seat list go out on Wednesday evening, the seat list as a PDF of the roster's Seat list sheet alone, which shows slot, minutes and assessor only | The first mocks start ten minutes into Thursday, too early to prepare from a brief handed out at the open, and the Grid's question ids would let a learner mocked early tell later learners their questions |
| A dropped online mock restarts whole in the spare slot, replacing only the questions the learner had already heard with the reserves the Grid prints, and the seat probe with the headline probe only if the learner had heard it | The day sheet said restart and the guide said note the point reached; a learner who has heard a question cannot be asked it again, while a question not yet reached is still fresh, which keeps the reserves for the questions that need them |
| No deck | The spine's Thursday line and the requester's Thursday fill list none, and the open is two minutes of spoken words, which the mock brief carries for a learner who missed it |
| The denial rate is written 10.35 percent, where the spine and Monday's day sheet say 10.4 | 1,175 over 11,355 is 0.10348; the generator's witness prints 0.1035, and rounding that a second time gives 10.4, while the one-decimal rounding of the exact value is 10.3. The two-decimal figure agrees with both readers. The spine's row could read 10.35 or 10.3, and its "1,137 denials" counts the denial postings, where the 1,175 denied claims carry the rate. |
| The text amounts are quoted as "$265.00" | The spine's example, "$1,050.00", is in no file: none of the 60 text amounts carries a thousands comma |
| Sub-problem 1's finished answer is read as a shortfall in billed dollars against 18 percent | Brief 1 tells the finance head to read each branch by how much of the shortfall against the plan it explains, since billed revenue would grow about as fast as volumes with prices and mix unchanged |
| Nine groups, where the row allocates fifteen | `data/programme/facts.yaml` states 35 learners in nine groups, and its `groups` conflict leaves the allocation to the trainer sheet; the roster seats nine and takes Monday's allocation on its Groups sheet |
| One assessor hears every member of three groups | This pack's design, kept from the first build: work carried for a group-mate shows against the others' answers |
| The 20 minutes as 1, 9, a half, 8 and 1.5 | This pack's split of the row's "roughly 20 minutes, half technical and half viva" |
| The assessors' guide and the scoring sheet describe what full marks look like on each criterion | The approved mock rubric gives criteria and marks only. The descriptions are labelled this pack's reading, set no marks, and exist so three assessors mark alike. |
| The one-breath interview answer is for the trainer's ear only | It names sub-problem 3's plants; the first build suggested saying a longer version aloud on Friday, which would have handed other groups the finding before Saturday |
| No AI assistant during the mock | This pack's rule, kept from the first build; no source sets it for the mocks |
| The workbooks are rebuilt by a script, and the roster gains Sets, Grid and Seat list sheets | The first build's workbooks could not be rebuilt from the repository; the script copies the rubric from facts.yaml, the Grid is what the huddle prints, and the Seat list is what the learners get |
| Medicare is "for people aged 65 and over and some younger people with disabilities" | The dossier's definition; Monday's briefs shorten it to 65 and over |

---

## What was invented, and where?

| Invented | Where |
|---|---|
| Every technical question's scene and numbers, listed above, and every model answer, follow-up, note on what the follow-up separates, and weak answer | The question bank |
| The closeness map behind the eighteen swaps, the set table the constraint search chose, the reserve rule and the probe rotation | The question bank, the workbook builder and the viva prompts |
| The wording of every probe, follow-up and push beyond the row's three phrases, the general push, the three readings of each answer, and each finished answer | The viva prompts |
| The huddle, the scripts, the evidence-note template, the time calls and the descriptions of full marks | The assessors' guide |
| The day's question in the room's words, the opening words, the three checks, the table of what goes wrong, the Wednesday-evening handover and the one-breath answer | The day sheet |
| The preparation plan in three pieces of 10 minutes | The mock brief |

Dr Menon's figures, 5 percent against a plan of 18, and the five askers' words are the row's, the
spine's and Monday's briefs'. A draft of the day sheet put an invented line in Dr Menon's mouth as
the day's question; the pedagogy review caught it, and the day's question is now the room's.

---

## What changed from the first build, file by file?

All ten of the first build's files are kept under the same names, and each was rewritten: the question
bank and the viva prompts moved from Kalpa Retail's and the India setting's figures to Kalpa Health's
US setting, and the viva prompts and this record drop the old register's no-show figures (10 of 52
and 10 of 50 at one Hyderabad clinic) for the register drawn from the bookings. Two INTERNAL scripts
are new: the numbers script and the workbook builder. No file is renamed or deleted, and none is left
without a reference: the day sheet's last table names every file and the moment it serves.

---

## Which tool versions made the numbers and the files?

Python 3.11.15; openpyxl 3.1.5 and PyYAML 6.0.1 for the workbook builder; LibreOffice 24.2.7.2 for
the recalculation `scripts/xlsx_recalc.py` runs; git 2.43.0; pandas 3.0.6, used by hand for the date
check above and by no script; mermaid-cli 11.17.0, installed in the session's scratch folder as
`setup.sh` pins it, which rendered the three diagrams through the shared theme of
`scripts/build_cheatsheet.py` (labels about 12 points at a 6.5-inch text width); and OR-Tools
9.15.6755, installed in the session and used once to search for the set table, which the builder
writes as fixed data and no script imports. The generator, Monday's witness check and this pack's
numbers script use the standard library only.

---

## Which proofs did the pack pass on 4 October 2026?

| Proof | Result |
|---|---|
| `python3 scripts/verify.py content/W03/D4 --execute` | `RESULT: PASS (0 failures)`: 12 files, every stem and folder valid for a build day; the roster recalculates with 13 verdicts and 13 flips and the scoring sheet with 6 and 3; one warning, marks language in the STUDENT brief, which `data/programme/facts.yaml` allows, since its evaluation block and the W03 rubrics are locked and learner-facing |
| `python3 scripts/sync_programme.py --check` | Every output is current |
| `internal/C2_W03_D04_numbers_INTERNAL.py`, run cold on `content/W03/D1/data/` | `RESULT: PASS (0 drifts)`, 306 checks |
| `internal/C2_W03_D04_build_workbooks_INTERNAL.py`, run cold in a scratch copy of the folder | Both workbooks cell-identical to the committed ones (4,092 and 697 cells) and both manifests byte-identical |
| `python3 scripts/distractor_audit.py content/W03/D4` | No option sets, since the mock is oral and carries none |
| The llm-tic-scrubber scanner on all eight markdown files | Clean |
| The three mermaid fences, rendered on mermaid-cli 11.17.0 through `scripts/build_cheatsheet.py`'s shared theme | All three render; labels print at 11.6 to 12.0 points at a 6.5-inch text width |
| `python3 data/generate_kalpa_health.py` into scratch, `--contract`, and Monday's witness check | Ten files byte-identical to the committed pack, `PASS  every plant holds`, and `RESULT: PASS (0 drifts from the spine and the day sheet)` |
| The headings-only read and the humanizer's read | Every heading in every file is a question; the humanizer's findings after each round are in the depth loop below |

---

## What did the depth loop find, and what changed?

| Pass | Who ran it | What it asked | What it found | What changed |
|---|---|---|---|---|
| 1. Draft | The builder | Is every file built from the row, the spine and the dossier? | The first build's bank and viva carried the India setting and the old register, and its workbooks had no build script | Every file was rewritten, and the numbers script and the workbook builder were added |
| 2. Domain | The builder | Could a learner who has never worked in business follow each file's stakes alone? | The mock brief used GCC, headline claim and both logs without saying what they are, and did not say what the trainer's three checks ask | GCC was defined where it first appears and the brief named the three checks; the other terms waited for pass 5's fixes, which defined each where it first appears |
| 3. Problem first | The builder | Does every judgement answer lay out its options, the call and what would change it? | T02-L3 and T10-L3 gave a call without the ways weighed or the fact that would switch it | Both weigh two ways and name what would change the call; the numbers script caught the spine's 10.4 percent as a second rounding, and the guard's first draft read 41,200 as 1,200, both fixed |
| Humanizer, file mode | The builder | Does any prose read as a model's? | Three bold paragraph labels in the viva prompts, bold inside a sentence, and two filler adverbs | The labels became question subheadings, and the bold and the adverbs went |
| 4. Rigor | A fresh reviewer, Opus, read-only | Does every number hold, every plant stay unnamed to learners, and every method stay inside Weeks 1 and 2? | Every Kalpa Health number held, and Quest and GeeksforGeeks matched. One blocker: the probes read aloud named plants and witness values. Four majors: the swap rule repeated a reserve in a group, put one family twice in a seat and missed close questions; the learners' seat list was the Grid with question ids; T04-L3 contradicted itself and said "six-payer"; "no payer stands out" was wrong. Seventeen minors, from power in T04-L2's follow-up to the 90-day range and the spine's 10.4 | The viva was rewritten to ask without telling; the swap rule, the sets and the reserves were redesigned and proved by the builder, the bank and the recalc; the Seat list sheet was added; T04-L3 was rewritten inside Week 1's four ways; the payer finding was recomputed; every minor was fixed except the two that ask for shared-file changes, which go to the orchestrating session |
| 5. Pedagogy and language | A fresh reviewer, Opus, read-only | Does each file teach and stand alone, and does its language meet the house rules? | One blocker, the same spoken plants. Majors: the preparation plan could not run when the brief arrived at the open; the viva's middle step asked what and how many, never why; the brief used terms before defining them and its ladder beats were fragments; the viva's headings repeated and ended on labels; the day's question left out the technical half and quoted an invented line. Minors: formulaic family openings with unexplained Week 1 and 2 names, terms an assessor meets cold, weak headings, uneven vocabulary, humanizer patterns and fragments | Every seat probe now asks why and what the alternative would have given; the brief defines each term where it first appears and goes out on Wednesday evening; the viva's headings are specific to each sub-problem, and its move labels and caveat lead-ins are sentences; the day sheet carries a ladder under every heading and an "Evidence and marks" column, with the invented line gone; the bank's family openings name the decision and the cost and explain each Week 1 and 2 name; the setting paragraphs lost their "stands alone" lead-in |
| Humanizer, after the fixes | The builder | Does any prose added by the fixes read as a model's? | The tic scanner found nothing in the eight markdown files; the read found the 29 "The move:" labels and five repeated caveat lead-ins still in the viva | Both became sentences |
| Second round | A fresh reviewer, Opus, read-only, on 4 October 2026 | Do the changes that moved a number, a key or a rule other files repeat hold? | No blocker. Six majors: five spoken viva lines steered a group towards what it had missed, four of them Monday's stuck-group questions reworded; the closeness map missed T03-L2 for billing, T02-L3 for revenue and T05-L3 for the offer, and T04-L3 and T02-L1 sat in the files' own months, where the data contradicts them; the guard's look-behind refused any value after a dollar sign and its lists missed many planted values and spoken forms; a reserve could put two questions from one family in a seat, and the restart always did for sub-problems 4 and 5; fifteen of the twenty seat probes asked no why, against what this record and the day sheet said; and pandas' `dayfirst=True` prints a UserWarning this record said it did not. Ten minors: T04-L3 credited the rule with the whole fall; the payer follow-up accepted Medicaid alone; weaker closeness gaps (T01-L3's random-half test, T09-L3's extract date, T07-L2's claim lines, T05-L1 and T10-L1 inviting the learner's own work, the tie-breaks, T03-L2 beside the visit register); softer spoken pointers; lines the guard did not read; a reserve fallback that undercut the reserves; two swapped seats on one week's moves; sub-problem 2's stuck question; the T03 opening's crore; and a seat label that told the probe. It found every recomputed figure, the printed swap rule under every allocation, the Grid, the Seat list, the restart's wording across files and both web sources holding | The closeness map widened and the sets re-solved by a constraint search, four cells moved, eighteen swaps, every swapped seat on both weeks; reserves printed per learner, with the sharing the levels force stated in the bank; the probe rotation; a restart that replaces only what the learner heard; every seat probe asking why and the other way, and the follow-ups and pushes made general; T02-L1, T02-L3, T07-L2 and T04-L3 dated or set outside the files, T05-L1 and T10-L1 given their own cases, T01-L3's test replaced by calls, T04-L3's effect an upper bound; the guard rebuilt with a self-test; the pandas line corrected; sub-problem 2's stuck question cut; Week 1's Rs 20 lakh in the T03 opening; anchors spoken with the ask's numbers; the seat list sent as a one-sheet PDF. The tie-break follow-ups of T06-L3, T08-L1 and T08-L3 stay, for the reason in the departures table |
| Proof run after the second round | The builder | Do the second round's fixes hold without another review, as the standard asks of fixes it does not send back? | The builder's asserts pass for every sub-problem and every group a seating can make, and the shared reserves fall exactly where the bank says; the numbers script ends `RESULT: PASS (0 drifts)`, its guard catching all 21 test hints and its own search confirming the reserves; LibreOffice recalculates the roster with 13 verdicts and 13 flips, a reserve edited to a group-mate's question among them, and a mixed allocation recalculated there reads four zeros; the rebuilt guard finds 17 hits in the viva as first committed, 7 in the viva as round one left it and none now; a read of all 85 spoken viva lines for meaning found none that names, sizes or points to a plant | Nothing further |
| Humanizer, after the second round | The builder | Does any prose the second round's fixes added read as a model's? | The tic scanner found nothing in the eight markdown files; the read found two broken lines in the brief and one stiff sentence in the day sheet's stuck-group rule | All three reflowed or rewritten |

---

## Which changes does this pack ask of shared files?

| File | The change | Why |
|---|---|---|
| `docs/detailing/W03_build1_spine.md`, sub-problem 3's row | "1,137 denials, 10.4 percent" to "1,175 denied claims, 10.35 percent", with 1,137 kept as the denial postings | 1,175 over 11,355 is 0.10348, and 1,137 counts postings, not denied claims |
| `docs/detailing/W03_build1_spine.md`, sub-problem 1's row | The text-amount example "$1,050.00" to one the files hold, such as "$265.00" | No text amount carries a thousands comma |
| `data/programme/facts.yaml`, `evaluation.rubrics.W03.events.mock` | A "What full marks look like" column, as the mini project and the GD carry | The assessors' guide and the scoring sheet now print this pack's reading, labelled as such |
| `content/W03/D3` day sheet | Send Mock R1's brief and seat list at Wednesday's close, the seat list as a PDF of the roster's Seat list sheet alone | Thursday's first mocks start ten minutes in, so the brief must arrive on Wednesday, and the workbook's Grid would tell learners their questions |
| `content/W03/D1/trainer/C2_W03_D01_day_sheet_TRAINER.md`, sub-problem 2's stuck-group question | Drop the second question, "Where are Chicago's bookings after mid-September?", or mark it for Monday only | It names one of the two metros brief 2 asks the group to find and the switch's timing; Thursday's day sheet keeps only the first |
| `content/W03/D3/checkpoints/C2_W03_D03_checkpoint_guide_TRAINER.md` | Move to the US setting | It still reads in the India setting |
| `content/W03/D1/briefs/`, the five briefs | Medicare as "the federal programme for people aged 65 and over and some younger people with disabilities" | The dossier's definition |

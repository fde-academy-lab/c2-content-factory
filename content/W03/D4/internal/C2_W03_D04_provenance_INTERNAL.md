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
| `content/W03/D1/trainer/C2_W03_D01_day_sheet_TRAINER.md` | The plant table with its witness numbers, and the stuck-group questions Thursday's day sheet copies word for word |
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

| Fact | Where it appears | Source, checked on 1 October 2026 |
|---|---|---|
| Quest Diagnostics assesses its testing business on "volume (measured by test requisitions) and revenue per requisition" | Question bank, T01-L1 | Quest Diagnostics, Form 10-K for 2025, https://www.sec.gov/Archives/edgar/data/1022079/000102207926000015/dgx-20251231.htm (checked 1 October 2026 with WebSearch, which returned it as the FY2025 10-K, and WebFetch, and the sentence read in the filing's own text) |
| Revenue per requisition rose 0.1 percent in 2025 while it rose 2.4 percent on an organic basis, because the acquired LifeLabs "has a lower revenue per requisition" | Question bank, T02-L3, now set as a dilution, the shape these figures show | The same filing, management's discussion of 2025 (checked 1 October 2026) |
| Days sales outstanding, "a measure of billing and collection efficiency", was 48 days at the end of 2025 | Question bank, T06-L3 | The same filing, cash flows section (checked 1 October 2026) |
| GeeksforGeeks, "Data Analyst Interview Questions and Answers", 95 numbered questions, last updated 24 July 2026, with "what is data cleaning" and "how do you handle missing data" among them | Question bank's calibration section; day sheet | https://www.geeksforgeeks.org/data-analysis/data-analyst-interview-questions-and-answers/ (checked 1 October 2026 with WebFetch: the title, the count and the update date read on the page) |
| "The SUBTOTAL function ignores any rows that are not included in the result of a filter, no matter which function_num value you use", and 101 to 111 also ignore rows hidden by the Hide Rows command | Question bank, T10-L2's follow-up | Microsoft Support, "SUBTOTAL function", https://support.microsoft.com/en-us/office/subtotal-function-7b027003-f060-4ade-9040-e478765b9939 (checked 1 October 2026 with WebFetch) |
| "If you have Medicare and other health insurance ... each type of coverage is called a 'payer'", and "The 'primary payer' pays up to the limits of its coverage, then sends the rest of the balance to the 'secondary payer'" | Question bank, T09-L2's model answer | Medicare.gov, "How Medicare works with other insurance", https://www.medicare.gov/supplements-other-insurance/how-medicare-works-with-other-insurance (checked 1 October 2026 with WebFetch) |
| pandas' `to_datetime(..., dayfirst=True)` reads "09/18/2026" as 18 September without a warning, while `format="%d/%m/%Y"` fails on it and `errors="coerce"` turns it into a blank | Viva prompts, sub-problem 2's plant paragraph | Run on pandas 3.0.6 in this session on 1 October 2026, on the new system's 153 dates: `dayfirst=True` gave month 9 for all 153; the strict format raised ValueError, and coerced, gave NaT |

No other real company, figure or rule appears. The deductible, coverage, Medicare and claim terms in
the bank, the brief and the viva are the domain dossier's, in its own words.

---

## Which command makes the data, and how were the numbers rechecked?

The pack copies no data. Its Kalpa Health numbers come from Monday's data pack, which
`python3 data/generate_kalpa_health.py --out content/W03/D1/data --stem C2_W03_D01` writes. On 1
October 2026 that command, pointed at a scratch folder, wrote ten files byte-identical to the
committed ones; `--contract` printed `PASS  every plant holds`; and `--witness` printed every figure
the spine carries. Monday's `internal/C2_W03_D01_witness_check_INTERNAL.py` ended
`RESULT: PASS (0 drifts from the spine and the day sheet)`.

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
| Sub-problem 1's payers: billed charges up 13.0 percent commercial, 6.0 Medicare and 1.6 Medicaid, down 2.2 self-pay; short of each payer's own plan by 4.2, 10.2, 13.9 and 17.1 percent; Medicaid 25.3 percent of the shortfall from 14.9 percent of Q2's billing; outside the two metros commercial up 20.8 against 3.5 to 7.6 | Computed by the numbers script after the rigor review found "no payer stands out" wrong |
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
| T02-L1 | Cash down 16 percent; one plan at 70 percent of cash paying on Fridays; four Fridays against five, so 14 points of the 16 |
| T02-L2 | Patients' share 11 percent in December, 19 in January, 18 last January |
| T02-L3 | About 3 percent more allowed per test for every payer type against 0.5 percent for the lab, so a mix effect of about 2.5 points; Quest's two figures |
| T03-L1 and L3 | 4,180 pickups invoiced against 3,960 logged; 130, 70 and 20 set aside, 220; $16 a stop, $2,080, $1,120, $320 and $3,520 |
| T03-L2 | An Austin register of 9,400 rows |
| T04-L1 | p of 0.04, chosen because New York's false positive in sub-problem 5 sits at 0.03 |
| T04-L2 | 2 rejections in 25 draws against 4 percent on 2,400; one draw moves the rate 4 points; chance 0.26; 8 or more in 100 at 4 percent, 0.048 |
| T04-L3 | Necessity denials 6.0 to 3.5 percent, other payers 5.8 to 3.6, a 2.2-point fall against Medicare's 2.5; 4,000 Medicare claims a month, 100 denials prevented, 20 forgone by a fifth held back |
| T05-L1 | 94 to 89 percent within the promise; 61 percent of late samples on two of eleven routes carrying 18 percent |
| T05-L2 | 1,900 of 42,000 and 2,300 of 52,000, 4.5 and 4.4 percent; 21 and 24 percent growth; 5.5 percent and 400 more if volume were flat |
| T05-L3 | 40 draws a day by a test centre's third month |
| T06-L1 | 2,000 tests an analyser |
| T06-L2 | 37 redraws over 2,400 draws, 1.5 percent, returned as 0 |
| T06-L3 | Quest's 48 days |
| T07-L2 | 41,200 claim lines becoming about 79,600 rows, 1.93 times |
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
| Eight sets, eleven swaps and six reserves | The bank's tables; the workbook builder derives the swaps from its closeness map and asserts that no learner meets a question close to their sub-problem, no seat holds one family twice and no two group-mates share a question; the numbers script checks the bank's printed tables against the same rule; the roster's flips put every group on each sub-problem in turn and read zero on both checks |
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
guard searches it for 27 plant words and 70 planted values, the values as whole numbers, and finds
none. It names the five askers' questions as Monday's briefs word them, which include Dr Menon's 5
percent, the two metros, KH-ATL-03 and the marketing head's 9 percent, all of them the briefs' own
public words. The same guard runs over the 60 rows the assessors read aloud in the technical half,
over the 81 questions the viva reads aloud (probes, follow-ups and pushes, with the bracketed answers
for the assessor removed) and over the day sheet's nine stuck-group questions, which may name the
`claim_ref` column since a column's name says where to look; it finds none. Run over the viva as
first committed, the same guard finds seven hits (walk-in, employer, repeated row, loaded twice, new
system, CLM- and 948), so it would have caught the leak the reviews found. A word guard cannot catch
a probe that states a plant in plain words, so the rewrite also opens every probe on the group's own
claim, and the second-round reviewer read every spoken question for meaning. Decision
`plants-once-found` covers only a regular week's Saturday paper, so no Build 1 file relies on it.

---

## Where does the pack depart from a source, and why?

| Decision or departure | Why |
|---|---|
| The technical half moves to Kalpa Health's US setting and sits outside the ten files | The requester asked that every file speak the US setting. Most Week 1 and 2 traps are the same mechanisms Build 1 plants in the data, so each question sits in a corner of Kalpa Health no sub-problem touches, on invented numbers, and the bank says so to the assessors and the brief says so to the learners. |
| Eleven questions are swapped for a learner whose group's viva they rehearse, each for the same level's question from the set four letters on, and five slots of the set table and the reserves changed to make that possible | The first rule swapped four questions to reserves, which gave two group-mates the same reserve and one seat two questions from one family, and it missed questions the rigor review showed were close. The far set is never met by a group-mate, so the new rule cannot repeat a question in a group. |
| T02-L3 asks about a dilution, every payer up about 3 percent and the lab up 0.5, where it asked about a reversal | The reversal mirrored sub-problem 5's plant, and Quest's 2025 figures are a dilution, so the question now matches its own example |
| p = 0.04 in T04-L1 | New York's false positive in sub-problem 5 sits at about 0.03, the value the Week 1 row's anchor quotes, so the spoken question uses another value |
| Sub-problem 1's finished answer reports the payers' uneven growth as a second finding | The spine's row names the metros only, and the rigor review found "no payer stands out" wrong; a learner who reports the payer gap is scored as having found a real pattern |
| The viva's New York probe asks how many metros were looked at, with no 1 minus 0.95 to the sixth | Week 1 Thursday keeps "about one in twenty" as recognition only and lists multiple-testing corrections under Stop before |
| The stuck-group questions are Monday's, with sub-problem 4's cut to its first question | Monday's day sheet holds the approved questions for a group that has found nothing; the second half of sub-problem 4's names its denominator, and the day sheet's earlier wording named the walk-ins |
| The brief and a learners' seat list go out on Wednesday evening, and the roster gains a Seat list sheet with slot, minutes and assessor only | The first mocks start ten minutes into Thursday, too early to prepare from a brief handed out at the open, and the Grid's question ids would let a learner mocked early tell later learners their questions |
| A dropped online mock restarts whole in the spare slot on the reserves for the learner's sub-problem, with the headline probe in place of the seat probe | The day sheet said restart and the guide said note the point reached; a learner who has heard the first questions cannot be asked them again |
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
| The closeness map behind the eleven swaps, and the reserve table | The question bank and the workbook builder |
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
the recalculation `scripts/xlsx_recalc.py` runs; git 2.43.0; pandas 3.0.6, used once by hand for the
date check above and by no script. The generator, Monday's witness check and this pack's numbers
script use the standard library only.

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
| Second round | A fresh reviewer, Opus, read-only | Do the changes that moved a number, a key or a rule other files repeat hold? | Recorded below once it has run | |

---

## Which changes does this pack ask of shared files?

| File | The change | Why |
|---|---|---|
| `docs/detailing/W03_build1_spine.md`, sub-problem 3's row | "1,137 denials, 10.4 percent" to "1,175 denied claims, 10.35 percent", with 1,137 kept as the denial postings | 1,175 over 11,355 is 0.10348, and 1,137 counts postings, not denied claims |
| `docs/detailing/W03_build1_spine.md`, sub-problem 1's row | The text-amount example "$1,050.00" to one the files hold, such as "$265.00" | No text amount carries a thousands comma |
| `data/programme/facts.yaml`, `evaluation.rubrics.W03.events.mock` | A "What full marks look like" column, as the mini project and the GD carry | The assessors' guide and the scoring sheet now print this pack's reading, labelled as such |
| `content/W03/D3` day sheet | Send Mock R1's brief and seat list at Wednesday's close | Thursday's first mocks start ten minutes in, so the brief must arrive on Wednesday |
| `content/W03/D3/checkpoints/C2_W03_D03_checkpoint_guide_TRAINER.md` | Move to the US setting | It still reads in the India setting |
| `content/W03/D1/briefs/`, the five briefs | Medicare as "the federal programme for people aged 65 and over and some younger people with disabilities" | The dossier's definition |

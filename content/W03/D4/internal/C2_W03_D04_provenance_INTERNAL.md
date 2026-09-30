# Provenance: Week 3 Thursday, Build 1, Mock R1 and build completion

**INTERNAL.** Where every part of this pack came from, the numbers it quotes and their sources, what
it departs from, and what was invented. The pack was built on 29 September 2026 and reached main that
day with pull request #163. Two later changes came with #177: commit 1a879ee on 29 September 2026
and the merge commit 59f336b on 30 September 2026. This record was written on 30 September 2026 from
the repository alone: the day's files, the spine, `data/programme/facts.yaml`, the generator and its
witness, and `git log` on each file, with `--follow` and across merges. Where the repository does not
say something, this record says so.

---

## Sources

| Source | What it gave the pack |
|---|---|
| `CLAUDE.md` | The build workflow, the hard rules, the folder and naming rules |
| `docs/detailing/W03_build1_spine.md` (approved 29 September 2026) | Thursday's line: Mock R1 for every learner at about 20 minutes, a technical half on Weeks 1 and 2 and a viva on the group's work, build completion around the roster, and the pack's three parts (the question bank with model answers, the viva prompts per sub-problem, the roster sheet); the plant table and its numbers; the rubrics block |
| `docs/curriculum/W3_Build_1.md`, Thursday's row and Monday's row | The scenario; the thinking the viva probes ("why this tree for a lab, why this identity rule for bookings, what a fair comparison needed in a clinic"); the agenda (the roster all day, the close-out of 15 minutes); the mock owners (the Principal Advisor online, the Programme Head and the Academic TA in person); the after-class task; the `[S]` interview angle; the GeeksforGeeks link for calibrating the technical half |
| `docs/curriculum/W1_Data_analysis_found.md` and `docs/curriculum/W2_Data_manipulation.md` | The anchor of every technical question. The bank's 30 anchors quote 34 interview-angle questions, and all 34 appear word for word in these two rows. |
| `docs/detailing/W01_W02_spine.md` | The trap an anchored question reuses. The anchors name twelve traps, and all twelve are in the spine's day tables, eleven word for word and the twelfth (p = 0.03 read as a 3 percent chance of being wrong) reworded. |
| `docs/programme/calendar.md`, line W03/D4 | Thu 22 Oct, build week, Module 1, no faculty block, rendered into the day sheet through `sync:module:W03/D4` and `sync:day-date:W03/D4` |
| `data/programme/facts.yaml` (as of 30 September 2026) | The campus day (two blocks of 180 minutes); the cohort (35 learners and nine groups, both stated; groups of four, locked); the marks per event (mini project 40, mock 30, GD 30, locked); the mock rubric and the mock's day in `evaluation.rubrics.W03`, settled on 29 September 2026 and rendered through `sync:rubric:W03/mock`; the `groups` conflict; the `build1-rubrics` decision, closed |
| `docs/07_Client_Zero.md`, section 1a | Meera Raghavan, Anand Iyer, the marketing lead and Dr Priya Menon, in whose words the questions are asked |
| `data/generate_kalpa_health.py`, its `--witness`, and the ten files in `content/W03/D1/data/` | Every Kalpa Health number in the viva prompts and the day sheet |
| Files of other days that the pack names | Monday's challenges log, decisions log and translation worksheet (what the brief asks a learner to have open); Wednesday's catch-up plan, Friday's cold-demo checklist and Saturday's presentation format (named in the day sheet) |

### The one link

| Link | Where | Checked |
|---|---|---|
| GeeksforGeeks, "Data Analyst Interview Questions and Answers": https://www.geeksforgeeks.org/data-analysis/data-analyst-interview-questions-and-answers/ | The question bank's calibration floor and the day sheet's last paragraph | The row carries verified 03 Sep 2026 and the pack's files carry verified 29 September 2026. Checked again for this record on 30 September 2026: it returns 200 with the title "Data Analyst Interview Questions and Answers - GeeksforGeeks", shows 95 numbered questions and gives 24 July 2026 as its last update, as the bank says. |

---

## The data command, and how the numbers were rechecked

The pack copies no data and keeps no script of its own. Its Kalpa Health numbers come from Monday's
data pack, which `python3 data/generate_kalpa_health.py --out content/W03/D1/data --stem C2_W03_D01`
writes. On 30 September 2026 that command, pointed at a scratch folder, wrote ten files that are
byte-identical to the committed ones; `--contract` printed PASS; and `--witness` printed every figure
below that the spine carries. Two kept scripts read the committed CSV files, and both ended on PASS
that day: `content/W03/D1/internal/C2_W03_D01_witness_check_INTERNAL.py`, with 0 drifts from the
spine, and `content/W03/SAT/internal/C2_W03_SAT_witness_INTERNAL.py`, with 0 disagreements, which
also prints the rupee bridge and each city's change. The few figures neither script prints were
counted from the CSV files in this session with a scratch script that is not kept, and each is marked
"counted" below.

---

## The numbers each file quotes, and where each comes from

### The viva prompts, TRAINER only

| The figure in the file | Where it comes from |
|---|---|
| The headline: tests on the dashboard's count 23,213 to 24,406 (5.1 percent), tests booked in both systems 23,213 to 25,022 (7.8 percent), tests performed 22,468 to 24,399 (8.6 percent), bookings 5,692 to 6,009 (5.6 percent); the contract's 1,200 health checks adding 6,000 tests | The spine; the D1 witness check prints each count and rate |
| "About 34 percent" growth in tests booked with the contract in | Counted: 31,022 over 23,213 is 33.6 percent |
| Sub-problem 1: invoice KH/26-27/007802 on account CORP-0007 for Rs 18,00,000, 16.2 percent of Q2's Rs 1,11,31,711; the Q2 mean invoice Rs 1,904 with it and Rs 1,596 without it, against a median of Rs 1,499 | The spine and both witness scripts; the invoice number and the account counted from the invoices file, where the invoice is dated 6 August 2026, in Bengaluru |
| 22,152 invoice lines that bill 46,867 tests on completed bookings, and 48,235 counting cancelled ones | The spine as corrected in #177; the generator's witness prints all three |
| Revenue outside the contract of Rs 85,74,238 in Q1 and Rs 93,31,711 in Q2 (8.8 percent); Chennai down 5.4, Pune down 11.6 and Hyderabad up 26.2 percent; the total with the contract up about 30 percent | The files; the Saturday witness prints each, the total's change as 29.8 percent |
| 35 amounts written with a thousands comma | The generator's witness (`text_amounts_with_comma`); the spine does not carry it |
| A Full body checkup as one invoice line, twelve tests and Rs 2,999, about Rs 250 a test, against a list-price sum of Rs 6,370 | Counted from the test catalogue and the booking-tests file |
| Sub-problem 2: the switch on 18 September and the old system's last date for the two cities on 17 September; 153 new-system bookings with NB/MAA and NB/PNQ references, MAA and PNQ centre codes and day/month/year dates; 1,415 bookings in Q1, 1,090 in the old export for Q2 (down 23.0 percent) and 1,243 with the new system (down 12.2 percent); 11,729 rows for 11,549 ids | The spine and the witness scripts; the formats read from the files |
| The new system's ten cancellations | Counted: 10 of the 153 rows are CXL |
| "Of the 180 repeated ids, 30 differ in the update time, so a whole-row dedupe leaves those 30 in" | Counted: 145 repeated ids are identical on every field, 30 differ in the update time (one of them in the channel as well), and 5 differ only in the channel, which one copy leaves blank. The 30 is right about the update time, and a whole-row dedupe of the file leaves 35 repeats in, 11,584 rows for 11,549 ids. The last section carries this. |
| Sub-problem 3: an exact join matching 247 of 11,289 payments (2.2 percent) and every payment once normalised; 229 double posts about two minutes apart; 102 refunds; 398 unpaid invoices worth Rs 24,47,805, Rs 18,00,000 of it the contract; invoiced Rs 1,97,05,949; successful payments Rs 1,76,13,398; double posts Rs 3,55,254; refunds Rs 1,60,164; collected Rs 1,70,97,980 | The spine for the counts; the Saturday witness for every rupee figure and the two-minute gap. The gap from invoiced to collected, Rs 26,07,969, equals the unpaid invoices plus the refunds to the rupee. |
| The feed's reference formats, bare digits such as 000123 and INV-123 | Counted: 247 references in the invoice's own format, 1,972 as INV- with an unpadded number and 9,070 as six bare digits |
| Sub-problem 4: KH-HYD-03 at 19.2 percent (10 of 52) against 8.7 on all visits, and 20.0 percent (10 of 50) against 15.2 on scheduled visits; a probability of 0.22; about 7.6 no-shows at the other clinics' rate | The spine and the witness scripts; 15.24 percent of 50 is 7.6 |
| "About 42 percent walk-ins" in the other clinics' visits | Counted: 3,040 walk-ins in 7,081 visits, which is 42.9 percent |
| Sub-problem 5: 2,381 patients offered and 948 taking it up; 9.0 percent more bookings overall; 10.8, 19.9 and 13.0 percent fewer in Bengaluru, Hyderabad and Mumbai; before the offer, from 1 April to 14 July, 1.4 percent more and 5.2 and 6.1 percent fewer; about half the patients offered in the campaign cities against about a fifth elsewhere; the campaign cities up 6.9 percent in the two months before the offer and 7.4 percent into its window, against 3.0 percent in Delhi | The spine as corrected in #169 and #177; the generator's witness, whose window before the offer runs from 1 April to 14 July and whose comparison city is Delhi alone, since Chennai and Pune are left out for the switch |

### The day sheet

| The figure | Where it comes from |
|---|---|
| Block 1 as 10, 150 and 20 minutes, and block 2 as 145, 20 and 15 | The roster's Settings: a 20-minute mock and a 5-minute changeover make a 25-minute slot, six slots to a block, and block 2's mocks end at minute 145 because the last changeover falls away |
| The interview answer's "about eleven thousand rows", "about 2 percent", 229 retries and Rs 18 lakh unpaid | Sub-problem 3's figures above |
| The mock rubric | `sync:rubric:W03/mock`, from `data/programme/facts.yaml` |

### The question bank

Every question is asked in a Kalpa Retail stakeholder's words, so the bank's figures belong to Weeks
1 and 2.

| The figure | Where it comes from |
|---|---|
| Meera's 15 percent (T01-L1), the Rs 12 crore acquisition ask (T01-L3), sales down 15 percent last month (T02-L1), Anand's Rs 1.9 crore against the dashboard's Rs 2.1 crore (T03-L1), the 14 rows (T03-L3), p = 0.03 (T04-L1), and 42 percent of 12 against 31 percent of 1,200 (T04-L2) | The Week 1 row's scenario and interview angles; `docs/07_Client_Zero.md` also carries the Rs 12 crore and the two crore figures |
| A mean of Rs 18,160 against a median of Rs 2,205 on thirty orders (T01-L2) | `docs/detailing/W01_W02_spine.md`, Monday's traps |
| Q1 of 90 days and Q2 of 92, with Q2 3 percent higher (T02-L2); orders and members down 12 percent (T05-L2); more than 500 customers (T06-L1); 1.4 orders per customer (T06-L2); a top 50 that ships 51 (T08-L3); the 90-day win-back and the 83 days a week-old extract reaches (T09-L3); Rs 3 lakh between pivot and warehouse (T10-L2); Rs 4,850 against Rs 5,100 per active customer (T10-L3) | Written for the questions. No source in the repository carries them in this form; the spine's nearest is a tie that ships 49 or 51 rows. |
| 2.2 percent more calendar and 0.8 percent a day (T02-L2); 8 points per visitor, margins of 29 and 3 points and 400 visitors (T04-L2); a mean about eight times the median (T01-L2) | Arithmetic on the figures above, rechecked on 30 September 2026 |

### The roster and the scoring sheet

| The figure | Where it comes from |
|---|---|
| A mock of 20 minutes, a close of 15 and three assessors | The row |
| A changeover of 5 minutes and a huddle of 10 | The pack's own choice |
| Blocks of 180 minutes | `data/programme/facts.yaml`, campus_day |
| 35 seats in nine groups, eight of four and one of three | 35 learners and nine groups from `data/programme/facts.yaml`, both stated; the sizes are the roster's default, which the Programme Head changes after Monday's allocation |
| 36 slots for 35 learners; 12 learners each for the Programme Head and the Academic TA and 11 for the Principal Advisor, whose slot 12 is the spare; the last mock ending at minute 145 of block 2, and the Principal Advisor's at minute 120 | The roster's formulas, asserted by its recalc manifest |
| Six criteria with maximums of 8, 4, 3, 6, 6 and 3, adding to 30, over 35 learner rows | Copied from `evaluation.rubrics.W03` into the scoring sheet's Criteria sheet, which checks the total against 30; the rows follow the roster's seats |
| A gap of more than about two marks between assessors on one half | The pack's calibration rule, in the assessors' guide and the Assessors sheet |

Neither workbook has a build script in the repository. Their metadata says openpyxl created both on
29 September 2026 and LibreOffice 24.2.7.2 saved them last, which is the recalculation
`scripts/xlsx_recalc.py` runs. A change is made in the workbook itself and proved by rerunning the
recalc.

### The learner's brief, STUDENT

| The figure | Where it comes from |
|---|---|
| Mock R1 on Thursday 22 October | `evaluation.rubrics.W03.graded_days`, which learners may see |
| 30 marks for the mock, 40 for the mini project including the presentation and 30 for the GD, and the rubric | `evaluation.per_event` and `sync:rubric:W03/mock` |
| About 20 minutes as 1, about 9, about 8 and 1 to 2; 30 minutes of preparation in three pieces of 10 | The pack's split of the row's roughly 20 minutes |

---

## The plants, and where each is used

| Plant | Where it appears | Audience |
|---|---|---|
| The headline | The viva prompts, probe H | TRAINER |
| 1. The corporate contract, packages as one line, the comma amounts | The viva prompts. The day sheet's question for a stuck group asks for the top five Q2 invoices by amount, which points at where to look. | TRAINER |
| 2. The system switch and the repeated rows | The viva prompts; the stuck-group question asks for each export's last booking date by city | TRAINER |
| 3. The reference formats, double posts, refunds and unpaid invoices | The viva prompts; the day sheet's interview answer | TRAINER |
| 4. The small clinic | The viva prompts; the stuck-group question asks for each clinic's share of walk-ins | TRAINER |
| 5. The campaign | The viva prompts; the stuck-group question asks for the 9 percent split by city | TRAINER |

The one STUDENT file, the learner's brief, names no plant. On 30 September 2026 a search of it for the
plant words (the contract, the switch and the new system, walk-ins, retries and double posts, the
reference formats, the small clinic, the offer and its cities, cancellations and the comma amounts)
found none. It names Meera Raghavan and Anand Iyer, Kalpa's fictional stakeholders, and gives the
assessors by role.

---

## Decisions, and where the pack departs from the spine or the row

| Decision or departure | What the repository records |
|---|---|
| The rubric | The row calls the rubric fixed, and the requester approved the three Build 1 rubrics on 29 September 2026 (#151, and the `build1-rubrics` decision in facts.yaml). Commit ca0ec95 aligned the pack to them: the viva gained a caveat challenge per sub-problem and a looking-back probe, so every criterion has a probe behind it, and the brief names the mock's day, which the approved entry allows. |
| Nine groups where the row allocates fifteen | The row's Monday agenda allocates fifteen groups, three per sub-problem. facts.yaml records 35 learners in nine groups as stated, with the `groups` conflict open; the roster seats nine and takes Monday's allocation on its Groups sheet. |
| The 20 minutes, split | The row says roughly 20 minutes, half technical and half viva. The pack runs 1 minute of opening, 9 technical, half a minute of switch, 8 of viva and 1.5 of close. |
| One assessor hears a whole group | The row names the three assessors and their modes. The split by group, the Programme Head G1, G4 and G7, the Academic TA G2, G5 and G8 and the Principal Advisor G3, G6 and G9, is the pack's, so that work carried for a group-mate shows against the others' answers. |
| Eight sets and six reserves | The pack's design: ten families at three levels, eight sets that each mix Week 1 and Week 2, consecutive set letters within a group, and six reserves for a leaked question or a re-mock. |
| The close | The row's 15 minutes; the pack gives 10 of them to the assessors away from the room and 5 to the room. |
| No AI assistant during the mock | The pack's rule, in the brief and the assessors' guide; no source in the repository sets it for the mocks. |
| The campaign probes | Rewritten in the merge commit 59f336b (#177), which brought in #169's correction of the spine's campaign row: P3 now rewards comparing the two groups before the offer and the caveat that the files cannot say how the offer was assigned, and P1's follow-up says a held-out share would settle it. Commit 1a879ee (#177) had already given sub-problem 1 the like-for-like test count. |

---

## What was invented

| Invented | Where |
|---|---|
| The questions' own figures listed above, and every model answer, follow-up, note on what the follow-up separates and weak answer | The question bank |
| The wording of every probe beyond the row's three phrases, and the three answers each probe is read against | The viva prompts |
| The opening, switch and close scripts, the huddle's calibration on T04-L2 and the evidence note's template | The assessors' guide |
| The opening words, the three build-completion checks, the one question per stuck group, the table of what goes wrong and the interview answer in a learner's voice | The day sheet |
| The preparation plan in three pieces of 10 minutes | The learner's brief |

Dr Menon's figures, 5 percent against a plan of 18, are the row's and the spine's.

---

## What this record could not establish

- The session that built the pack kept no provenance, no numbers script and no workbook builder, and
  its commit messages name no tool versions. The Python and pandas versions its figures came from are
  unknown, and the two workbooks cannot be rebuilt from the repository.
- The pack's own choices above are recorded only as the build session's commits of 29 September 2026
  and the merge of #163; the repository holds no separate sign-off on them.
- Two figures in the viva prompts read differently from the files. The translation probe's follow-up
  says a whole-row dedupe leaves "those 30" repeats in, where the files leave 35, because 5 repeated
  ids differ only in a blank channel. The walk-in share is given as about 42 percent, where the files
  give 42.9. This record leaves the viva file as it is and reports both.

## Tool versions

The build's own versions are not recorded, apart from LibreOffice 24.2.7.2, which the two workbooks'
metadata names. This record's checks ran on 30 September 2026 under Python 3.11.15, pandas 3.0.5 (for
the Saturday witness script), openpyxl 3.1.5, LibreOffice 24.2.7.2 (for the recalc that
`scripts/verify.py` runs) and git 2.43.0. The generator, the D1 witness check and the scratch counts
use the standard library only.

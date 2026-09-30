# Provenance: Week 3 Monday, Build 1 opens in Kalpa Health

**INTERNAL.** Where every part of this pack came from, the numbers it quotes and their sources, what
it departs from, and what was invented. The data pack reached main on 29 September 2026 with pull
request #148, written by the generator; the rest of the pack was built on 29 and 30 September 2026
and reached main on 30 September 2026 with #176, after the orchestrating session's review. This
record was written on 30 September 2026 from the repository alone: the day's files, the spine,
`data/programme/facts.yaml`, the generator and its witness, and `git log` on each file, with
`--follow` and across merges. Where the repository does not say something, this record says so.

---

## Sources

| Source | What it gave the pack |
|---|---|
| `CLAUDE.md` | The build workflow, the hard rules, the folder and naming rules |
| `docs/detailing/W03_build1_spine.md` (approved 29 September 2026) | Monday's line: the Programme Head's online introduction (60), the allocation (30), each group translating its sub-problem into the Weeks 1 and 2 method, and the close (15); the pack's parts (the briefing note, the five briefs, the data pack with its dictionary, the translation worksheet, the challenges log, the introduction deck and the trainer sheet with both ways to allocate nine groups); the spine's four decisions (a synthetic data pack, the rubrics, the allocation on Monday by the Programme Head, no spine per day); the five sub-problems; the plant table; the rubrics block |
| `docs/curriculum/W3_Build_1.md`, Monday's row, Tuesday's line and Wednesday's row | Monday: the scenario (5 percent against a plan of 18, the six cities, the five sub-problems), the thinking trained (a booking is an order, a test is an item, a no-show is a cancellation; the cost of an error), the agenda (60, 30, the rest of the day, 15), the trainer notes (groups of four, the mock owners, Dussehra), the translation worksheet and entry one of the challenges log, the after-class task, and the `[S]` and `[F]` interview angles. Tuesday: Dussehra, no session. Wednesday: the two things the data team tells the room, that two cities changed booking systems in Q2 and that the payment feed has a different id format from the invoice export. |
| `docs/curriculum/W1_Data_analysis_found.md` | Meera's 4 percent against a plan of 15, on the deck's S3 |
| `content/W01/D1` and `content/W01/D3` | The revenue tree on S10, which is Week 1 Monday's S3 (`content/W01/D1/slides/C2_W01_D01_half1_STUDENT.md`); the bridge and log rows on S12 and the decisions log's Example sheet, from Week 1 Wednesday's day sheet and study notes |
| `docs/programme/calendar.md`, lines W03/D1 and W03/TUE | Mon 19 Oct, build week, Module 1, no faculty block, rendered into the day sheet through `sync:module:W03/D1` and `sync:day-date:W03/D1`; Tue 20 Oct as Dussehra |
| `data/programme/facts.yaml` (as of 30 September 2026) | The campus day (two blocks of 180 minutes); the cohort (35 learners and nine groups, both stated; groups of four, locked); the `groups` conflict; the marks per event (mini project 40, mock 30, GD 30); the three Build 1 rubrics and their graded days in `evaluation.rubrics.W03`, which learners may see, rendered through `sync:rubric:W03` and its three parts; the GCC addendum, with Kavya Nair's review as a recurring beat |
| `docs/07_Client_Zero.md`, sections 1a and 1b | Dr Priya Menon, Meera Raghavan, Anand Iyer and Kavya Nair, and the four things Kavya's review checks: the baseline, the denominator, the evidence and a second way to the same number |
| `data/generate_kalpa_health.py` and its `--witness` | The ten data files and every planted number |

No link enters any file in this pack, the built deck and the two workbooks included, so there is
nothing to date.

---

## The data command, and how the numbers were rechecked

The ten files in `data/` were written by `python3 data/generate_kalpa_health.py --out
content/W03/D1/data --stem C2_W03_D01` and reached main with #148; later changes to the generator
(#149, #150, #169 and #177) touched its docstring, comments, witness and contract, and the folder's
history holds that one commit, so the files are as the generator first wrote them. On 30 September 2026 that command, pointed at a scratch folder, wrote ten files that are
byte-identical to the committed ones; `--contract` printed PASS; and `--witness` printed every figure
the spine carries. `internal/C2_W03_D01_witness_check_INTERNAL.py` reads only the committed CSV files,
prints each planted number beside the spine's, and ended that day on `RESULT: PASS (0 drifts from
the spine)`. The two workbooks are written by `internal/C2_W03_D01_build_logs_INTERNAL.py`, which reads
the decisions log's input row counts from the CSV files at build time. The few figures neither script
prints were counted from the CSV files in this session with a scratch script that is not kept, and
each is marked "counted" below.

---

## The numbers each file quotes, and where each comes from

### The day sheet, TRAINER only

| The figure | Where it comes from |
|---|---|
| The headline: 23,213 to 24,406 tests (5.1 percent), 23,213 to 25,022 (7.8 percent), 22,468 to 24,399 (8.6 percent), 5,692 to 6,009 bookings (5.6 percent), and the contract's 6,000 tests | The spine; the witness check prints each count and rate |
| Sub-problem 1: Rs 18,00,000 on invoice KH/26-27/007802, dated 6 August, Bengaluru, account CORP-0007; 16.2 percent of Q2's Rs 1,11,31,711; a Q2 mean invoice of Rs 1,904 with it and Rs 1,596 without, a median of Rs 1,499; 48,235 test rows behind 22,152 invoice lines, 46,867 of them on completed bookings; 35 amounts with a thousands comma | The spine and the witness check; the invoice's number, date, city and account counted from the invoices file; the 46,867 and the 35 from the generator's witness |
| Sub-problem 2: 1,415 bookings in Q1, 1,090 in the old export for Q2 (down 23.0 percent) and 1,243 across both systems (down 12.2 percent); 11,729 rows over 11,549 ids, 180 ids twice, dated 1 June to 26 September; 153 bookings in the new system | The spine and the witness check; the dates counted |
| Sub-problem 3: 11,289 payments, an exact join matching 247 (2.2 percent), every payment matching once normalised, 229 double posts, 102 refunds, 398 unpaid invoices including the contract's | The spine and the witness check |
| 199 payments recorded after 30 September | Counted: the feed runs from 1 April to 6 October 2026, and 199 rows fall after 30 September |
| Sub-problem 4: KH-HYD-03 with 52 visits, 50 scheduled and 2 walk-in; 19.2 against 8.7 percent for the other eleven clinics; 20.0 percent (10 of 50) against 15.2; a probability of 0.22 | The spine and the witness check; the twelve walk-in clinics counted from the appointments file |
| Sub-problem 5: 2,381 offered and 948 taking it up; 9.0 percent overall; 10.8, 19.9 and 13.0 percent less in Bengaluru, Hyderabad and Mumbai; 50.5 percent offered in the three campaign cities against 21.4 percent elsewhere; within about 6 percent before the offer; the campaign cities up 6.9 percent in the two months before it | The spine as corrected in #169 and #177, and the generator's witness |
| 180 rows in `bookings_legacy` with no channel, and one booking whose channel is corporate | Counted: 180 rows, on 180 booking ids, with an empty channel, and one row with `corporate` |
| Block one as 60, 30 and 90 minutes; block two as 75, 30, 30, 30 and 15 | The row's 60, 30 and 15 and facts.yaml's blocks of 180; the rest is the pack's split |
| Nine groups as eight of four and one of three, and the two ways to allocate them | facts.yaml's 35 learners and nine groups, and its `groups` conflict; the two options are the pack's |
| The interview answers' 5.1, 5.6, 7.8 and 8.6 percent, and a rate on 50 visits | The witness; 50 is KH-HYD-03's scheduled visits, and the 5,000 beside it is the answer's own contrast |

### The briefing note and the five briefs, STUDENT

| The figure | Where it comes from |
|---|---|
| 5 percent against a plan of 18, and the 13 points between them | The row; 18 less 5 |
| Six cities, each with one laboratory and two walk-in clinics | The clinics file: 6 laboratories and 12 walk-in clinics |
| Q1 as April to June and Q2 as July to September 2026 | The generator's quarters |
| The five questions, KH-HYD-03 by name, and the 9 percent | The row's five sub-problems, put in the heads' words by the pack |
| The twelve walk-in clinics on the operations head's report (brief 4) | The clinics and appointments files |
| A presentation slot of 25 to 30 minutes | The spine's Saturday line |
| The marks, the rubrics and the days of Mock R1, the GD rounds and the presentations | `evaluation.per_event` and `evaluation.rubrics.W03`, through the sync blocks |

### The data dictionary, STUDENT

| The figure | Where it comes from |
|---|---|
| The ten row counts: 6,700; 18; 16; 11,729; 153; 51,456; 11,356; 11,289; 7,133; 2,381 | Counted: all ten match the files |
| Every sample value | Counted: each one is in its file |
| The old export's dates from 1 April to 30 September 2026; twelve tests and four packages; the visit register covering all twelve walk-in clinics, Q2 only | Counted from the files |
| The data team's two notes | Wednesday's row |

### The introduction deck, STUDENT

| The figure | Where it comes from |
|---|---|
| S1: 5 and 18 percent, six cities, 6 laboratories and 12 clinics, 10 files | The row and the clinics file |
| S3: Meera's 4 percent against a plan of 15 | The Week 1 row's scenario |
| S6: 35 learners in nine groups, eight of four and one of three, five sub-problems, 30 minutes for the allocation | facts.yaml, the spine and the row |
| S7: 60, 30 and 15 minutes on Monday; 30, 60 and 20 on Wednesday; about 20 minutes a mock; about 30 minutes a GD; 25 to 30 minutes a presentation | The spine's day-by-day table and the rows |
| S9: 40, 30 and 30 marks, and S9a to S9c | facts.yaml, through the sync blocks |
| S10: the revenue tree | Week 1 Monday's S3, identical in every box; the slide's note calls it word for word, which holds |
| S12: Rs 2,09,98,210 less Rs 19,67,560 and Rs 30,650 to Rs 1,90,00,000; 15 repeated rows, 201 rows for 186 orders; one empty status kept and flagged | Week 1 Wednesday's day sheet and study notes in `content/W01/D3`; the bridge adds up to the rupee |
| S17: 15, 30 and 20 minutes; two minutes a group at the checkpoint | The row and the spine |

### The two logs, STUDENT

| The figure | Where it comes from |
|---|---|
| The decisions log's rows in, file by file | Counted from the CSV files by the builder; the recalc manifest asserts 6,700 for `patients` |
| The decisions log's Example: 15 repeated rows, 14 of them in Q1; 201 rows for 186 orders; Q1 Rs 1,790 short of the books if the wrong copy is kept; the largest Q2 order 1.66 times the next | Week 1 Wednesday's day sheet and study notes |
| The challenges log's Example entry | Written for the sheet, as another group's entry one |

---

## The plants, and where each is used

| Plant | Where it appears | Audience |
|---|---|---|
| The headline and all five sub-problems, with the numbers above | The day sheet's plant table, with where each surfaces and the question to ask if nobody finds it by Wednesday | TRAINER |
| The same numbers, recomputed | `internal/C2_W03_D01_witness_check_INTERNAL.py` | INTERNAL |

The STUDENT files carry the heads' questions as the row gives them, with KH-HYD-03 by name and the 9
percent claim, the data team's two notes from Wednesday's row, and the data dictionary's row counts
and sample values copied from the files. Among the samples are the new system's Chennai and Pune rows
and dates in late September, which any group sees on opening that file. On 30 September 2026 a search
of the STUDENT files, the deck's notes included, found no statement of how a plant works or what it
amounts to.

---

## Decisions, and where the pack departs from the spine or the row

| Decision or departure | What the repository records |
|---|---|
| A synthetic data pack | The row names real data re-labelled from a public source. The requester chose a synthetic pack on 29 September 2026 (the spine's first decision and #148), so the files are safe in a public repository and every learner holds the same bytes. |
| Nine groups where the row allocates fifteen | The row's agenda allocates fifteen groups, three per sub-problem; facts.yaml records nine as stated, with the `groups` conflict open. The day sheet gives the Programme Head two ways to allocate nine, three sub-problems three times or all five, and the spine leaves the choice to the Programme Head on Monday. |
| What the room is told about the data | The briefing note and the dictionary give the two things Wednesday's row tells the room and nothing further (commit b0d6bf3, from #176's review). The dictionary's samples still show which cities and dates the new system holds. |
| The deck's speaker notes | #176's review found three notes in the STUDENT pptx that pointed at plants and one Your turn that pointed at the payment feed's keys; commit 1757874 cleared them, and what the trainer holds back stays in the day sheet. |
| Week 1 quoted as taught | S12 and the decisions log's Example sheet quote Week 1 Wednesday as it was taught (commits 1757874 and 9b19ad3). #176's description also says S10 no longer calls its tree word for word; the note still does, and the tree is identical to Week 1 Monday's. |
| The graded days | Commit 46e5c67 had the deck name stages in place of days, so that no graded event carried a day. The requester approved the rubrics on 29 September 2026 and ruled that Build 1's learner files may name the graded days, and commits c0836e5 and 1757874 named them and put the rubrics in sync blocks. |
| The marketing head's ask | It asks for the offer in all six cities, since the campaign file already reaches a fifth of the patients outside the three campaign cities (commit c0836e5). |
| The day sheet's campaign row | Rewritten in commit 1aeb38b to what the files show, after #169 corrected the spine; the same commit added the 46,867 tests on completed bookings. |

---

## What was invented

| Invented | Where |
|---|---|
| The heads' wording of the five questions, and each brief's decision, symptom and panel questions | The briefing note and the briefs |
| The parts and prompts of the worksheet beyond the row's three seeded pairs | The translation worksheet |
| The two allocation options, the per-group translation tells, the words to say, the table of what goes wrong and the interview answers | The day sheet |
| The deck's questions, answers and notes | The introduction deck |
| The Example entry on the challenges log | The challenges log |

Dr Menon's figures, 5 percent against a plan of 18, are the row's and the spine's.

---

## What this record could not establish

- The session that built the pack names no tool versions in its commits. The workbooks' metadata
  names openpyxl 3.1.5; the deck's pptx carries python-pptx's default template metadata, so the
  python-pptx and mermaid-cli versions behind the built deck are not recorded.
- How the nine groups are allocated is the Programme Head's call on the day, so no record can hold it
  yet.

## Tool versions

The build's own versions are not recorded, apart from openpyxl 3.1.5 in the two workbooks' metadata.
This record's checks ran on 30 September 2026 under Python 3.11.15, openpyxl 3.1.5, python-pptx
1.0.2 and LibreOffice 24.2.7.2 (for the recalc and the deck check that `scripts/verify.py` runs) and
git 2.43.0. The generator, the witness check and the scratch counts use
the standard library only.

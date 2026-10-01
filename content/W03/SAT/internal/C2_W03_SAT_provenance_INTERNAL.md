# Provenance: Week 3, Saturday, the Build 1 close

**INTERNAL.** Where every fact in this day's files came from, what the pack decided where a source left
a call open, and the depth loop's record. Raised to standard v3 in the US setting on 1 October 2026,
over the first wave of 29 September 2026.

## Which sources does the pack rest on?

| What | Source | Status |
|---|---|---|
| The day's date, module and focus | `docs/programme/calendar.md`, line W03/SAT, and the sync blocks in each TRAINER file | Locked calendar, 21 September 2026 |
| The row | `docs/curriculum/W3_Build_1.md`, Saturday 24 October, all fifteen columns, and Monday's row for the week | Tracker v7 |
| The spine, its rubrics, the rule for a failed demo, and the plants | `docs/detailing/W03_build1_spine.md`, approved 29 September 2026; its sub-problem 4 row re-planted on 1 October 2026 (decision `build1-register-from-bookings`) | Approved |
| Kalpa Health in the US | `docs/07_Client_Zero.md` section 1c; decisions `four-domains` and `build1-us-data` in `data/programme/facts.yaml` | Addendum of 30 September 2026 |
| The 300-minute Saturday | `data/programme/facts.yaml`, `campus_day.saturday_minutes` | Locked |
| 35 learners in nine groups, eight of four and one of three | `data/programme/facts.yaml`, `cohort`, and its `groups` conflict with the tracker's fifteen | Stated (handover) |
| Marks per event (mini project 40, mock 30, GD 30) and the Build 1 rubrics, learner-facing, with the graded days | `data/programme/facts.yaml`, `evaluation` and `evaluation.rubrics.W03`, approved 29 September 2026; read by both workbook builders and rendered by the sync into the bank, the run sheet and the presentation deck | Locked |
| The five askers' questions, word for word | `content/W03/D1/briefs/C2_W03_D01_brief_{1..5}_*_STUDENT.md` and the briefing note, merged in #215 | Monday's pack |
| The data files' columns and what each system says one row is | `content/W03/D1/briefs/C2_W03_D01_data_dictionary_STUDENT.md` | Monday's pack |
| The plant table Monday's trainers hold | `content/W03/D1/trainer/C2_W03_D01_day_sheet_TRAINER.md`, "What is planted in each brief's files" | Monday's pack |
| Terms, roles and the revenue-cycle metrics | `content/W03/D1/study-notes/C2_W03_D01_domain_us_healthcare_STUDENT.md`, sections 2 to 6 | Monday's dossier |
| Claim, evidence, caveat, action | `content/W01/D4/slides/C2_W01_D04_half1_STUDENT.md`, S5, "The note" | Week 1 Thursday, merged |
| Restate, bound, offer the test | `content/W01/D5/slides/C2_W01_D05_rehearsal_STUDENT.md`, S6 and S7 | Week 1 Friday, merged |
| The names of the Weeks 1 and 2 moves | The decks of `content/W01/D1` to `D5` and `content/W02/D1` to `D5` (each chapter's question), and the "Week 1 or 2 move" column of Monday's briefs | Merged at v3 |
| The week's seven interview questions and their tags | `docs/curriculum/W3_Build_1.md`, the interview angle of each row | Tracker v7 |
| Meera's Week 4 Monday words | `docs/curriculum/W4_Analyst_craft.md`, Monday 26 October, business scenario | Tracker v7 |
| Build 2 opens on Tuesday 10 November in Kalpa Financial Services | `docs/programme/calendar.md`, line W06/D2 | Locked calendar |
| Friday's seven GD rounds, the first tranche of up to three, the freeze and the drawn order | `content/W03/D5/trainer/C2_W03_D05_day_sheet_TRAINER.md`, as merged on 1 October 2026 (first wave); a parallel session is rebuilding it | Friday's pack |
| The presentation format is handed out at Wednesday's close | `content/W03/D3/trainer/C2_W03_D03_day_sheet_TRAINER.md` and `content/W03/D3/checkpoints/C2_W03_D03_headline_claim_STUDENT.md` (first wave) | Wednesday's pack |

## Which real-world facts appear, and where was each checked?

| Fact, as the pack prints it | Where it appears | Source, read on 1 October 2026 |
|---|---|---|
| Quest Diagnostics' second-quarter 2026 revenues were $3.04 billion, up 10.2 percent on 2025; requisition volume rose 13.1 percent and revenue per requisition fell 2.8 percent, both against 2025 | Presentation deck, D10 | Quest Diagnostics, "Quest Diagnostics Reports Second Quarter 2026 Financial Results; Raises Revenue and EPS Guidance for Full Year 2026", 23 July 2026, https://www.prnewswire.com/news-releases/quest-diagnostics-reports-second-quarter-2026-financial-results-raises-revenue-and-eps-guidance-for-full-year-2026-302832675.html (verified 1 Oct 2026); the two percentages are the release table's rows "Requisition volume" and "Revenue per requisition" |
| Optum India is UnitedHealth Group's largest Global Capability Center, with hubs in Gurugram, Noida, Bengaluru, Hyderabad, Pune and Chennai | Week close, D5 | UnitedHealth Group careers, India, https://www.unitedhealthgroup.com/careers/in/work.html (verified 1 Oct 2026) |
| AGS Health is a healthcare revenue-cycle firm with more than 15,000 revenue-cycle professionals worldwide and centres in Chennai, Hyderabad, Bengaluru and other Indian cities | Week close, D5 | AGS Health, company page, https://www.agshealth.com/company/ (verified 1 Oct 2026) |

The Quest release's revenue growth and its two requisition percentages do not multiply to each other
exactly, and the release explains no measurement basis for them, so the deck states the three figures
side by side and never multiplies them. The deck's note mentions that Quest runs patient service
centres and laboratories without a count, since the count (about 2,400, in Monday's dossier) was not
re-read today.

## Which numbers does the pack quote, and what recomputes them?

Every number in the TRAINER files comes from `internal/C2_W03_SAT_witness_INTERNAL.py`, which reads the
ten CSV files in `content/W03/D1/data/` the way a group would and compares 53 figures with the spine
and 132 further figures with the bank the TRAINER files quote. Its run on 1 October 2026
ends `RESULT: PASS (0 disagreements with the spine and the bank)`. The generator's own witness,
`python3 data/generate_kalpa_health.py --witness`, ends `PASS every plant holds` on the same day.

The STUDENT files quote no number from the data pack beyond what Monday's briefs give learners (Dr
Menon's 5 and 18 percent, the 9 percent lift, KH-ATL-03 as the worst centre, 6,700 patients), the
rubric's marks, Quest's three figures and the invented figures listed below.

## Where is each plant used, and does any reach a learner?

| Plant | TRAINER files that name it | STUDENT files |
|---|---|---|
| The headline: the dashboard counts old-system retail tests, a panel as its components | Question bank, run sheet, week-close notes | None |
| The employer contract and panels billed as one claim line | Question bank, run sheet, week-close notes | None |
| The booking-system switch in Chicago and Philadelphia, the old export's repeats and the month-first dates | Question bank, run sheet, week-close notes | None |
| The claim-key formats, the double posts, the unposted employer claim and the denials paying nothing | Question bank, run sheet, week-close notes | None |
| KH-ATL-03's appointments against the walk-ins, on the register drawn from the bookings | Question bank, run sheet, week-close notes | None |
| The offer's targeting by metro and the negative split inside the campaign metros | Question bank, run sheet, week-close notes | None |

Decision `plants-once-found` covers only a regular week's Saturday paper, so no Build 1 STUDENT file
names a plant, hints at its size or reuses a planted value. The presentation deck's examples run on an
invented turnaround quarter, on the lab director's question, which none of the five briefs asks.

## What is invented, and where is each invention labelled?

| Invention | Where | How it is labelled |
|---|---|---|
| The lab director's turnaround quarter: median draw to released result 22 hours in Q2 and 18 in Q3 on 9,400 tests, 14 hours in Q3 timed from arrival at the lab; the courier run; 200 samples timed by hand | Presentation deck, D11 to D14, D21's note, D33, D36 | "invented" on each slide that uses it |
| A decisions-log row: 14 blank age bands, kept and labelled unknown | Presentation deck, D18 to D20 | "an invented row"; the note says the real files' age bands have no blanks |
| The weak and usable sentences for Build 2, and the four plans, replies and reasons in the question slides | Presentation deck, D19, D22, D27, D34; week close, S8 | Generic examples, attached to no Kalpa number |
| The seat labels G1-S1 to G9-S3 and the sample entries in the recalc manifests | Both workbooks and their manifests | Test entries only; the committed workbooks are empty templates |

## Which decisions did this pack take where the sources left the call open?

| Decision | Why | Where it landed |
|---|---|---|
| The rule for a failed demo, set by the orchestrating session on 29 September 2026, is applied in both workbooks as checks: each group's demo outcome is recorded; the group's 34 are required whatever the outcome; a learner in a group whose demo still failed cannot close on full marks for presentation and defence | The rubric's full marks for presentation and defence begin with "the live demo runs cold", and the spine says a failed demo "costs its own marks"; how many marks is the panel's call, so the sheets set no number | Scoring workbook (Groups, Learners, Summary), closure workbook (Demos, Scores, Checks), the bank, the run sheet, the deck's D29 |
| A machine that fails before the demo starts is swapped, and the demo runs cold in the room's reserve before the same panel | The rule covers a group's code; the first wave added the machine case and the requester's delegation covers it | Run sheet, bank, deck D29, both workbooks |
| The grade closure workbook takes the mini project in its two parts, 34 and 6 | So the demo rule can be checked at closure as well | Closure workbook, run sheet |
| The slot is 17 minutes of the group's, 8 to 10 of the panel's and 3 of changeover, with cards at 5 and 1 minute left | The row's 25 to 30 minutes; Friday's pack shows cards at 5 and 1 minute left | Deck S5, run sheet, bank |
| The room rule: each sub-problem's groups together and back to back; sub-problems 1 and 5 before the leader where it splits nothing | The row asks for alternate viewpoints back to back; the leader's questions are a board's | Run sheet |
| Two timings: the likely Saturday (two GD rounds, six presentations) and the heaviest (three GD rounds, nine presentations, in clusters of 2, 2, 2, 2 and 1 or 3, 3 and 3, the latter at 28-minute slots) | Monday's allocation is the Programme Head's and Friday's tranche depends on its draw | Run sheet |
| The deck's S slides are the ones shown at each expert day's opening; every other slide is a D slide read alone from Wednesday's close | The standard numbers a self-study slide D; Wednesday's pack hands the deck out for the night | Presentation deck |
| Deck question slides are audited by `internal/C2_W03_SAT_deck_options_audit_INTERNAL.py`, which keys them from their answer slides and runs `scripts/distractor_audit.py` on a scratch copy | The audit reads option sets only in exercise folders, which a build Saturday does not have | Proof below |
| The bank's sub-problem 1 answer gives the payer split (commercial 13.0, Medicare 6.0, Medicaid 1.6 percent up, self-pay 2.2 percent down) beside the metro split | The spine plants the contract and the panels; a group's tree reaches a branch, and the panel needs both honest branch answers in hand | Bank |
| Two figures are this programme's own arithmetic, marked so in the bank: about 700 scheduled visits (712) to separate KH-ATL-03's gap from chance at 5 percent two-sided with 80 percent power, nine quarters of its slots; and 0.17, the chance that one of six metros reaches p of 0.03 if the offer did nothing | They answer the caveat challenges the panel will hear | Bank, witness |
| The week close lists all seven of the week's interview questions, Wednesday's "two systems with different id formats" among them | The row's interview angle goes into the pack as tagged questions; by the week close no group's work can change | Week close, S6 |
| File names are kept | Wednesday's, Thursday's and Friday's packs point at `slides/C2_W03_SAT_presentation_format_STUDENT.md` | Every file |

## Where do the files differ from the spine's wording?

| The spine says | The files hold | What this pack does |
|---|---|---|
| Sixty billed amounts are text "such as $1,050.00" | Sixty text amounts, from "$30.00" to "$350.00"; "$1,050.00" occurs nowhere | The bank quotes "$265.00", which a group reading the claims file finds |
| "1,137 denials, 10.4 percent of retail claims" | The claims file marks 1,175 retail claims denied, 10.4 percent; 1,137 of them carry a denial posting paying $0.00 and 38 have no posting | The bank gives all three numbers, as Monday's day sheet does |
| "The old export also repeats 180 rows from a mid-quarter re-export" | 180 booking ids twice, booked 1 June to 26 September: 145 pairs identical, 30 differing in `updated_at` (one of them in `channel` as well) and 5 only in `channel` | The bank quotes the files and makes no claim about when the re-export ran |

## Which tools and versions produced the files?

Python 3.11.15, pandas 3.0.6, openpyxl 3.1.5, PyYAML 6.0.1 and python-pptx 1.0.2; LibreOffice 24.2.7.2
for the recalculations and the renders, with `fonts-crosextra-carlito` installed in the session so
Calibri text measures as on a trainer's laptop; Node 22.22.0. The decks were built with
`scripts/build_deck.py` and mermaid-cli 11.17.0, installed in the session's scratch space and run with
the container's puppeteer configuration, because `setup.sh` pins version 11 and every built deck was
measured against it; the container's own mermaid-cli is 12.0.0. The workbooks and their recalc
manifests are written by `internal/C2_W03_SAT_build_mini_project_scoring_INTERNAL.py` and
`internal/C2_W03_SAT_build_grade_closure_INTERNAL.py`.

## What did the depth loop ask, find and change?

| Pass | Who | What it asked | What it found | What changed |
|---|---|---|---|---|
| 1. Draft | The builder | Is every file built from the row, the spine and the dossier, in the row's order? | The first wave's question bank and week-close notes were in the India setting; the witness quoted the old register's no-show numbers and failed five spine figures; the first wave's presentation deck named two plants in a STUDENT file (two metros changing booking systems, the posting system's own key format), used a Week 1 plant's figures as its example, and kept its options in tables the audit cannot read | Every file rebuilt: the witness against the re-planted spine (0 disagreements), the bank and notes in dollars, metros, payers and Q2 to Q3, the deck on invented figures with no plant, its options as lettered lines |
| 2. Domain | The builder | Could a learner who has never worked in a business say who asks, why the number matters, what a wrong number costs and which real company faces the same question, from each file alone? | The presentation deck never said what Kalpa Health is; its vocabulary map gave "payer" and "phlebotomist" no meaning; the week close named Kalpa Health without saying what it does; no real company appeared | S1 now says what Kalpa Health is and how it bills; the map defines payer and phlebotomist; the week close's S1 says what Kalpa Health is; Quest's quarter (D10) and Optum India and AGS Health (week close D5), each checked on 1 October 2026 |
| 3. Problem first | The builder | Does every technique arrive as the answer to a stated problem, with options, a sizing and the call, and the code last? | The day teaches no code; its techniques are the one-slide answer, the cold demo and the held caveat, and each arrives on Dr Menon's two minutes, the panel's trust and the challenge; the run sheet sizes both loads in minutes and names what changes the plan | No change |
| Humanizer, file mode | The builder | Which patterns of `.claude/skills/humanizer` remain in each prose file? | Contrast tails ("never out of the questions", "never a feeling", "never a tidied copy", "never defend blindly and never fold"), a "rather than" contrast in the bank's opening, two closers that only restated, and a rule between every section of the TRAINER files | Each rewritten as a plain statement, the restating closers replaced by the section's answer or cut, the rules removed; the tic scanner clean on every file |
| 4. Rigor | A fresh reviewer agent | To be logged after the review | | |
| 5. Pedagogy and language | A fresh reviewer agent | To be logged after the review | | |

## How was the pack proved?

To be logged with the final proof run.

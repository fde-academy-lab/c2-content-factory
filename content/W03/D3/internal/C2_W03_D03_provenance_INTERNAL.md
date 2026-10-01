# Where did every part of the Build 1 Wednesday pack come from, and what did the depth loop change?

**INTERNAL.** The sources, the data command, the plants and where each is used, every departure from
the spine or the row, everything invented, the one link with its check date, the tool versions, and
the five passes of the depth loop. First built on 29 September 2026 in the India setting; raised to
standard v3 in Kalpa Health's US setting on 1 October 2026, in one session on the branch `w03-d3`.

## Which sources were read, in which order, and what did each give the pack?

| Source | What it gave the pack |
|---|---|
| `CLAUDE.md` | The build workflow, the hard rules, the folder and naming rules, the writing rules |
| `.claude/skills/day-pack-builder/references/the-standard.md` | The question ladder, the self-contained rule, the notebook's form (options, sizing, levels, traps, second route), the depth loop |
| `.claude/skills/day-pack-builder/references/artifact-manifest.md`, "Weekly and build-week variations" | The build-week pack in place of the teaching manifest: no notebook chapters, practice set, Kahoot or test |
| `docs/detailing/W03_build1_spine.md` (approved 29 September 2026) | The day's shape (checkpoint 30, parallel build 60, build time, the close 20), the five sub-problems, the rubrics, the rule for a demo that fails, the plant table and its witness numbers |
| `docs/curriculum/W3_Build_1.md`, the Wednesday row in column order | The scenario, the thinking trained, the agenda, the outcome, the trainer notes, the in-session exercises, the after-class task, the interview angle ([F] and [D]) |
| `docs/programme/calendar.md`, line W03/D3 | Wed 21 Oct 2026, a build-week day posting to Module 1, no faculty block |
| `docs/07_Client_Zero.md`, sections 1a to 1d | Dr Priya Menon, Kavya Nair, the GCC frame, the US setting (1c), and the Kalpa Retail exposure list's ids (1d), used in the notebook's [F] answer |
| `data/programme/facts.yaml` (as of 1 October 2026) | The campus day, the cohort and its `groups` conflict, the rubrics, decisions `build1-us-data`, `build1-register-from-bookings`, `build1-rubrics`, `question-ladder`, `self-contained`, `humanizer` and `four-domains` |
| `content/W03/D1/study-notes/C2_W03_D01_domain_us_healthcare_STUDENT.md` and its card and trainer story | Billed revenue against what a payer pays, the claim, the remittance and posting, the roles; the student files link its sections 3, 5 and 6 |
| `content/W03/D1/briefs/` (briefing note, five briefs, data dictionary) and `content/W03/D1/trainer/C2_W03_D01_day_sheet_TRAINER.md` | The five askers' questions as the briefs word them, Dr Menon's "one answer per question" line, each brief's terms, and the plant table's figures that the witness does not print |
| `data/generate_kalpa_health.py`, its docstring and `--witness` | The ten files and what each system exports; the witness the numbers script checks against |
| The Week 1 and 2 day sheets (`content/W01/D1` to `D5`, `content/W02/D1` to `D5`, at standard v3 on main) | The moves as those packs teach them, named in every checkpoint question and notebook section |
| `.claude/skills/notebook-builder`, `exercise-builder`, `mini-project-designer` (the TA playbook's parts), `humanizer`, `llm-tic-scrubber` | The notebook's rhythm and checks, distractor discipline for the predict sets, the catch-up plan's floor-walking shape, the writing passes |

## How is the data made, and how does the pack read it?

The data pack is Monday's, written by `python3 data/generate_kalpa_health.py --out content/W03/D1/data
--stem C2_W03_D01`; this day copies nothing. The notebook reads `../../D1/data/` from
`parallel-build/`, and the internal scripts read the same folder from the repository root.

| Command | What it does |
|---|---|
| `python3 content/W03/D3/internal/C2_W03_D03_build_parallel_build_INTERNAL.py` | Writes and executes the New York notebook cold in its own folder |
| `python3 content/W03/D3/internal/C2_W03_D03_numbers_INTERNAL.py` | Recomputes every number the pack quotes, checks 51 against the generator's witness and 14 against the spine or Monday's day sheet, and ends on PASS |
| `python3 content/W03/D3/internal/C2_W03_D03_audit_predicts_INTERNAL.py` | Runs `scripts/distractor_audit.py` on the notebook's seven predict sets |

## Which plants does the pack carry, and where is each used?

| Plant | Where it appears | Audience |
|---|---|---|
| The headline: the dashboard's count (5.1, 7.8, 8.6 and 5.6 percent) | Day sheet plant table and circulating note; checkpoint guide, brief 1 | TRAINER |
| 1. The employer contract, a panel as one claim line, the 60 dollar-text amounts | Day sheet; checkpoint guide; run sheet (what the slice holds and avoids) | TRAINER |
| 2. The system switch, the repeated rows, the month-first dates | Day sheet; checkpoint guide; run sheet. The notebook shows New York's 33 repeated ids and handles them with an identity rule, naming no cause, no date and no whole-file count | TRAINER; New York's count only in the STUDENT notebook |
| 3. The claim-key shapes, double posts, the unpaid employer claim, denials with nothing paid | Day sheet, including its [F] interview answer; checkpoint guide | TRAINER |
| 4. KH-ATL-03 by appointment, others with walk-ins; the register drawn from the bookings | Day sheet; checkpoint guide (15 of 79 scheduled, 19.0 against 15.1 percent, chance 0.21) | TRAINER |
| 5. The targeting into three rising metros, the reversal inside them, New York's false positive | Day sheet; checkpoint guide; run sheet (New York's fee waivers and its 23.5 percent, as what the slice avoids) | TRAINER |

The STUDENT files are the checkpoint questions, the headline sheet and the notebook. They name no
plant, give no plant's size and reuse no planted value. The numbers they quote are New York's own,
Dr Menon's 5 percent against 18, the marketing head's 9 percent, and KH-ATL-03's name, which brief 4
already gives.

## Where does the pack depart from the spine, the row or the first wave, and why?

| Departure | Reason |
|---|---|
| No STUDENT file says that two metros changed booking systems or that the posting system keys claims its own way, though the row's scenario has the data team tell the room both | The brief lists the system switch and the claim-key formats among the plants no STUDENT file names, and Monday's student files say neither. The first wave's day sheet let the trainer repeat both; this one does not. |
| The row says the switch happened "in Q2" in "cities"; the pack says Q3 and metros | The spine wins: calendar Q2 to Q3 of 2026 in six US metros, set on 30 September 2026. |
| The pack carries no deck | The Wednesday fill names none and the first wave shipped none. The checkpoint sheet and the headline sheet are what the room sees, and the notebook is the parallel build's screen. |
| The row's interview question [F] sits in a STUDENT file, the notebook | CLAUDE.md carries the row's interview angle into the pack as questions with their tags. The notebook answers it in general terms with Kalpa Retail's exposure list (client zero 1d) as its example and New York's `booking_id` join as the case where formats agree; the Kalpa Health example, the posting system's shapes, stays in the day sheet. |
| The notebook's second route runs in SQLite, which Python carries, where Week 2 used the Postgres warehouse | The build reads two CSV files and must run cold anywhere; `ROW_NUMBER()`, `REPLACE` and `GROUP BY` behave alike in both engines. The notebook says why it ships with Python and what SQLite does with text it cannot read. |
| The refused join prints only the first line of pandas' `MergeError` | pandas 3 lists the repeated keys under that line, which would put New York's repeated booking ids on the page; the helper's `expect_error` shows the whole message, so the cell catches the error itself. |
| Dr Menon's quote on the headline sheet is the briefing note's "one answer per question" sentence | The first wave's sheet carried no quote; the row's "one sentence per sub-problem" is the row's paraphrase, so the sheet quotes her own words from Monday. |
| The checkpoint guide's no-show answers and the numbers script follow the register drawn from the bookings | Decision `build1-register-from-bookings` (1 October 2026) re-planted sub-problem 4; the first wave's 10 of 50 and 19.2 against 8.7 percent are gone. |
| The run sheet's sixty minutes run in nine steps, with the options and the SQL route added | The standard asks every build to size its options before the code and reach its number a second way; the cuts that protect the reconciliation and the claim are named. |

## What in the pack was invented, and where?

| Invented | Where |
|---|---|
| The wording of Kavya Nair's review lines | The notebook, the headline sheet |
| The four options' hours for a group, labelled estimated | The notebook's sizing cell |
| The six tests a claim passes, built on the Week 1 Thursday note and the mini project's claim criterion | The headline sheet |
| The five wrong New York sentences, each built from a wrong number the notebook computes | The headline sheet |
| The follow-up for each strong and weak checkpoint answer, and the claim-type replies at the close | The checkpoint guide, the day sheet |
| The smallest honest claim per brief | The catch-up plan |
| The trainer's words at each turn, and the questions asked at a group's table in build time | The day sheet, the run sheet |

## Which link does the pack carry, and when was it checked?

| Fact | Where it is used | Source | Checked |
|---|---|---|---|
| Quest Diagnostics: net revenues of $11,035 million for 2025 and $9,872 million for 2024, "Net revenues for the year ended December 31, 2025 increased by 11.8% compared to the prior year"; its revenue estimates "include the impact of contractual allowances (including payer denials), and patient price concessions" | The notebook's opening and section 8; the run sheet; the day sheet | Quest Diagnostics, Form 10-K for 2025, https://www.sec.gov/Archives/edgar/data/1022079/000102207926000015/dgx-20251231.htm | checked 1 October 2026, downloaded with curl and the text searched; WebFetch returned only an excerpt |

The same filing reports requisition volume and revenue per requisition. The pack leaves both out,
since Monday's dossier review found that teaching how a lab counts its volume pre-answers the
headline plant.

## Which tools made the numbers and outputs?

Python 3.11.15, pandas 3.0.6, numpy 2.4.6, nbclient 0.11.0, nbconvert 7.17.1 and SQLite 3.45.1, on
1 October 2026. The notebook uses `read_csv` with every value as text, boolean filters, `groupby`,
`merge` with `validate` and `indicator`, `drop_duplicates`, `to_sql` and one SQLite query.

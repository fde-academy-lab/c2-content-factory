# Where did every part of the Build 1 Wednesday pack come from, and what did the depth loop change?

**INTERNAL.** This page records the sources, the data command, the plants and where each is used,
every departure from the spine or the row, everything invented, the one link with its check dates,
the tool versions, and the five passes of the depth loop. The pack was first
built on 29 September 2026 in the India setting and raised to standard v3 in Kalpa Health's US
setting on 1 October 2026; the session stopped at the account's usage limit after the humanizer's
read, and a resumed session on 4 October 2026 ran passes 4 and 5 and fixed their findings, all on
the branch `w03-d3`.

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
| `data/programme/facts.yaml` (as of 1 October 2026) | The campus day, the cohort, the rubrics, decisions `build1-us-data`, `build1-register-from-bookings`, `build1-rubrics`, `question-ladder`, `self-contained`, `humanizer` and `four-domains` |
| `content/W03/D1/study-notes/C2_W03_D01_domain_us_healthcare_STUDENT.md` and its card and trainer story | Billed revenue against what a payer pays, the claim, the remittance and posting, the roles; the student files link its sections 3, 5 and 6 |
| `content/W03/D1/briefs/` (briefing note, five briefs, data dictionary, decisions log) and `content/W03/D1/trainer/C2_W03_D01_day_sheet_TRAINER.md` | The five askers' questions as the briefs word them, Dr Menon's "one answer per question" line, each brief's terms and header form, the decisions log's five columns, and the plant table's figures that the witness does not print |
| `content/W03/D1/internal/C2_W03_D01_witness_check_INTERNAL.py` | The windows behind the campaign metros' 6.9 percent rise: bookings per day from 14 May to 14 July against 1 April to 13 May |
| `data/generate_kalpa_health.py`, its docstring and `--witness` | The ten files and what each system exports; the witness the numbers script checks against |
| The Week 1 and 2 day sheets and decks (`content/W01/D1` to `D5`, `content/W02/D1` to `D5`, at standard v3 on main) | The moves as those packs teach them: Week 1 Tuesday's ladder (confirm, compare like with like, decompose, isolate, hypothesise), Week 1 Wednesday's profile, identity rule and rows in equal rows kept plus rows set aside, Week 1 Thursday's real or the wobble, count beside every rate, is the split fair and "not yet", Week 2 Tuesday's join counted first and its anti-join, Week 2 Wednesday's `ROW_NUMBER()`, Week 2 Thursday's `validate=` |
| Thursday's pack on the branch `w03-d4` (its day sheet, mock brief and roster, read on 4 October 2026) | The handover at Wednesday's close: the mock brief and the seat list printed from the roster's Seat list sheet, the Programme Head's Groups sheet, the Grid sheet kept with the assessors |
| `.claude/skills/notebook-builder`, `exercise-builder`, `mini-project-designer` (the TA playbook's parts), `humanizer`, `llm-tic-scrubber` | The notebook's rhythm and checks, distractor discipline for the predict sets, the catch-up plan's floor-walking shape, the writing passes |

## How is the data made, and how does the pack read it?

The data pack is Monday's, written by `python3 data/generate_kalpa_health.py --out content/W03/D1/data
--stem C2_W03_D01`; this day copies nothing. The notebook reads `../../D1/data/` from
`parallel-build/`, and the internal scripts read the same folder from the repository root.

| Command | What it does |
|---|---|
| `python3 content/W03/D3/internal/C2_W03_D03_build_parallel_build_INTERNAL.py` | Writes and executes the New York notebook cold in its own folder |
| `python3 content/W03/D3/internal/C2_W03_D03_numbers_INTERNAL.py` | Recomputes every number the pack quotes and asserts each one: 64 against the generator's witness, 18 against the spine or Monday's day sheet, and 60 against the values the pack's files quote; it ends on PASS |
| `python3 content/W03/D3/internal/C2_W03_D03_audit_predicts_INTERNAL.py` | Runs `scripts/distractor_audit.py` on the notebook's seven predict sets |

## Which plants does the pack carry, and where is each used?

| Plant | Where it appears | Audience |
|---|---|---|
| The headline: the dashboard's count (5.1, 7.8, 8.6 and 5.6 percent) | Day sheet plant table and circulating note; checkpoint guide, brief 1 | TRAINER |
| 1. The employer contract, a panel as one claim line, the 60 dollar-text amounts | Day sheet; checkpoint guide; run sheet (what the slice holds and avoids) | TRAINER |
| 2. The system switch, the repeated rows, the month-first dates | Day sheet; checkpoint guide; run sheet. The notebook and the headline sheet show New York's 33 repeated ids, handled by an identity rule, and name no cause, no date and no whole-file count | TRAINER; New York's count only in the STUDENT notebook and headline sheet |
| 3. The claim-key shapes, double posts, the unpaid employer claim, denials with nothing paid | Day sheet, including its [F] interview answer; checkpoint guide | TRAINER |
| 4. KH-ATL-03 by appointment, others with walk-ins; the register drawn from the bookings | Day sheet; checkpoint guide (15 of 79 scheduled, 19.0 against 15.1 percent, chance 0.21) | TRAINER |
| 5. The targeting into three rising metros, the reversal inside them, New York's false positive | Day sheet; checkpoint guide; run sheet (New York's fee waivers and its 23.5 percent, as what the slice avoids) | TRAINER |

The STUDENT files are the checkpoint questions, the headline sheet and the notebook. Pass 4 found
two places where they leaned on a plant: brief 2's second question asked "where did the two
disagree?", which presumed the planted disagreement, and the notebook said a booking was "exported
twice", which named the re-export's mechanism. Both were rewritten, together with brief 2's other
two questions, the notebook's section 2 heading and the brief 1 move that pointed at one large
claim. The STUDENT files now name no plant, give no plant's size and reuse no planted value. The
numbers they quote are New York's own, Dr Menon's 5 percent against 18, the marketing head's 9
percent, and KH-ATL-03's name, which brief 4 already gives.

## Where does the pack depart from the spine, the row or the first wave, and why?

| Departure | Reason |
|---|---|
| No STUDENT file says that two metros changed booking systems or that the posting system keys claims its own way, though the row's scenario has the data team tell the room both | The brief lists the system switch and the claim-key formats among the plants no STUDENT file names, and Monday's student files say neither. The first wave's day sheet let the trainer repeat both; this one does not. |
| The row says the switch happened "in Q2" in "cities"; the pack says Q3 and metros | The spine wins: calendar Q2 to Q3 of 2026 in six US metros, set on 30 September 2026. |
| The pack carries no deck | The Wednesday fill names none, the spine's Wednesday pack names none, and the first wave shipped none. The checkpoint sheet and the headline sheet are what the room sees, opened in markdown preview, and the notebook is the parallel build's screen. |
| The row's interview question [F] sits in a STUDENT file, the notebook | CLAUDE.md carries the row's interview angle into the pack as questions with their tags. The notebook answers it in general terms, with Kalpa Retail's exposure list (client zero 1d) as the example of keys that look alike and belong to different populations, and New York's `booking_id` join as the case where formats agree; the Kalpa Health example, the posting system's shapes, stays in the day sheet. |
| The notebook's second route runs in SQLite, which Python carries, where Week 2 used the Postgres warehouse; it loads the two raw CSV files with the `csv` module | The build must run cold anywhere, and a second route that reads the raw files with its own code can fail where the pandas cells are wrong. `ROW_NUMBER()`, `REPLACE` and `GROUP BY` behave alike in both engines, and the notebook says what SQLite's `CAST` does with text. |
| The refused join prints only the first line of pandas' `MergeError` | pandas 3 lists the repeated keys under that line, which would put New York's repeated booking ids on the page; the helper's `expect_error` shows the whole message, so the cell catches the error itself. |
| Dr Menon's quote on the headline sheet is the briefing note's "one answer per question" sentence | The row's "one sentence per sub-problem" is the row's paraphrase, so the sheet quotes her own words from Monday. |
| The checkpoint guide's no-show answers and the numbers script follow the register drawn from the bookings | Decision `build1-register-from-bookings` (1 October 2026) re-planted sub-problem 4; the first wave's 10 of 50 and 19.2 against 8.7 percent are gone. |
| The run sheet's sixty minutes run in nine steps, with the options and the SQL route added | The standard asks every build to size its options before the code and reach its number a second way; the cuts that protect the reconciliation and the headline claim are named. |
| The model headline claim says "carried by" where the first draft said "because" | A split of billed revenue into claims times the mean claim locates the change and proves no cause, and the room copies the model's wording into claims that do assert a cause. |
| Wednesday's close sends Thursday's mock brief and seat list | Thursday's pack starts the first mocks ten minutes into the day; the roster's Seat list and Grid sheets exist on the branch `w03-d4` and reach main when it merges. |

## What in the pack was invented, and where?

| Invented | Where |
|---|---|
| The wording of Kavya Nair's review lines | The notebook, the headline sheet |
| The four options' hours for a group, labelled estimated | The notebook's sizing cell |
| The predict options and their wording, built from real slips where a slip exists (5.6 percent counts Q2 as 90 days, 9.2 percent swaps the lengths) | The notebook |
| The six tests a headline claim passes, built on the Week 1 Thursday note and the mini project's claim criterion | The headline sheet |
| The five wrong New York sentences, each built from a wrong number the notebook computes | The headline sheet |
| The follow-up for each strong and weak checkpoint answer, the grid's marks and statuses, and the replies by kind of headline claim at the close | The checkpoint guide, the day sheet |
| The smallest honest claim per brief | The catch-up plan |
| The trainer's words at each turn, and the questions asked at a group's table in build time | The day sheet, the run sheet |

## Which link does the pack carry, and when was it checked?

| Fact | Where it is used | Source | Checked |
|---|---|---|---|
| Quest Diagnostics: net revenues of $11,035 million for 2025 and $9,872 million for 2024; "Net revenues for the year ended December 31, 2025 increased by 11.8% compared to the prior year"; "For the year ended December 31, 2025, organic growth was 5.3% compared to the prior year"; its revenue estimates "include the impact of contractual allowances (including payer denials), and patient price concessions" | The notebook's opening and section 8; the run sheet; the day sheet | Quest Diagnostics, Form 10-K for 2025, https://www.sec.gov/Archives/edgar/data/1022079/000102207926000015/dgx-20251231.htm | checked 1 October 2026, and again on 4 October 2026: WebSearch confirmed the 11.8 percent and the $11,035 million, WebFetch returned only an excerpt, and the filing downloaded with curl and searched confirmed every quote and both figures; the organic-growth sentence entered on 4 October 2026 |

The same filing reports requisition volume and revenue per requisition. The pack leaves both out,
since Monday's dossier review found that teaching how a lab counts its volume pre-answers the
headline plant.

## Which tools made the numbers and outputs?

Python 3.11.15, pandas 3.0.6, numpy 2.4.6, nbclient 0.11.0, nbconvert 7.17.1 and SQLite 3.45.1, on
1 and 4 October 2026; the day sheet's two mermaid pictures were rendered and checked with
mermaid-cli 11.17.0 from the scratch folder, since the container's own `mmdc` reports 12.0.0. The
notebook uses `read_csv` with every value as text, boolean filters, `groupby`, `merge` with
`validate` and `indicator`, `drop_duplicates`, the `csv` module, `sqlite3` and one SQL query.

## What did each pass of the depth loop ask, find and change?

| Pass | Who ran it | What it asked | What it found and what changed |
|---|---|---|---|
| 1. Draft | The builder, 29 September 2026 (India setting) and 1 October 2026 (US setting, standard v3) | Is every file built from the row, the spine and the dossier, in the order the day runs? | The first wave's files carried the India setting and the old register. The rebuild wrote the numbers script against the witness and the register drawn from the bookings (b060f74), then the parallel build and run sheet (2c76a6e), the checkpoint family (55adc47) and the day sheet (bfd2642), each following the spine's Wednesday: checkpoint 30, parallel build 60, build time, the close 20. On 4 October 2026 the day sheet's close gained Thursday's handover (4d42964). |
| 2. Domain | The builder, 1 October 2026 | Could a learner who has never worked in a business say who asks, why the metric matters, what a wrong number costs and which real company faces the same question, from each file alone? | The student files leaned on Monday's brief for their terms. Each brief's terms now sit beside its three questions (claim, billed revenue, branch, booking, field team, remittance, posting, payment, denial, reversal, filing deadline, visit register, no-show, offer, lift), the headline sheet defines the identity rule, and both point to the dossier's sections 3, 5 and 6 for depth (d7d5945). |
| 3. Problem first | The builder, 1 October 2026 | Does every technique arrive as the answer to a stated problem, with options, a sizing, the best-fit call and what would change it, with the code as the last mile? | The notebook's options table sized each way on what it would miss and on the rows it reads, with the call and what would switch it; the second route runs in SQL; a script runs the distractor audit on the seven predict sets (d7d5945). |
| The humanizer's read | The builder, 1 October 2026, in file mode over every prose file | Which of the humanizer's patterns are present? | Staged and aphoristic contrasts became facts (the caveat row, Kavya's review, the run sheet's habit and plant-question lines, the day sheet's finds), the checkpoint sheet's self-description went, and "quietly" and "rather than" left the notebook's markdown through the build script. The markdown files' changes are c3095f0; the notebook's landed with d7d5945. |
| 4. Rigor | A fresh reviewer agent, read-only, 4 October 2026 | Does the notebook run cold, does every trap show its exact wrong number and its check, does every sizing hold, is every real-world fact sourced, would a strong interviewer accept every answer, does any cue give a key away, and does any STUDENT file carry a plant or pre-answer a later day? | Every number recomputed correctly from the raw files and agreed across files, the notebook ran cold with outputs unchanged, and every Quest quote was in the filing. Two blocking findings: brief 2's question presumed the planted disagreement, and the notebook said Quest put both bases "in one sentence". Should-fix findings: the model claim's "because" on a decomposition, a "two options" stem and setups that gave four predict keys away, option D's rows understated, "exported twice" naming the re-export, two traps naming no decision, a second route that reused the pandas frames and the pandas quarter rule, a wrong account of SQLite's CAST, an [F] answer with no next step, a [D] answer with exact figures and no windows, Depth figures no cell computed, a numbers script that printed many figures without asserting them and a constant-typed line, and the guide's account of day-first dates. All were fixed (f6cbb79, b9a18b5, 08a5701, b54824d): the notebook's Quest line says "on the page", brief 2's questions ask whether the counts agree, the predicts were rewritten and the site predict now asks whether the sites add back, the SQL route reads the raw files, the numbers script asserts every figure (64, 18 and 60), and the guide gives all three day-first failures. One suggestion was declined: a [D] answer saying New York "is not where the plan's growth went missing", since the plan counts tests and New York's claims are a different unit, and saying so would touch the headline's count. The cross-day overlap with Thursday's question bank is reported to the orchestrating session. |
| 5. Pedagogy and language | A fresh reviewer agent, read-only, 4 October 2026, after the humanizer's read | Does every file pass the headings-only read and stand on its own, do the devices vary, does every picture read at print size, and is the language free of the scrubber's tics and the humanizer's patterns? | The tic scanner was clean, every asker's quote matched Monday's words, and the minutes added up. Ten blocking findings: four brief headings used terms the sheet had not explained, and fragments sat in the checkpoint sheet, the headline sheet (twice), the catch-up plan (twice), the run sheet and the day sheet (four, one of them a garbled question read aloud). Should-fix findings included "claim" meaning both a bill and the group's sentence, move names drifting from the Week 1 and 2 packs (Week 2 Tuesday's anti-join, real or the wobble, is the split fair, the decompose and isolate rungs), prompts naming no move, thin "Who needs the answer." paragraphs, the model claim failing the sheet's own tests 4 and 5, test 6 inviting a claim with no action, answers printed beside the wrong sentences, Kavya never introduced in the notebook, a clipped chart title, the bridge's "$-4.4k", undefined grid statuses, process language in trainer files, slogan contrasts and a closer, and a disagreement on how the close is cut. All were fixed in the same four commits; the headline sheet keeps "headline claim" for the sentence, the guide's headings carry each brief's questions, and the block two picture draws the open build time dashed. |

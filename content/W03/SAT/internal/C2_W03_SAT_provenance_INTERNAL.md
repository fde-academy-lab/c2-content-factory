# Provenance: Week 3, Saturday pack

**INTERNAL.** Where every fact in this day's files came from, checked 29 September 2026.

| What | Source | Status |
|---|---|---|
| The day's date, module and focus | `docs/programme/calendar.md`, line W03/SAT, and the sync blocks in each TRAINER file | Locked calendar, 21 September 2026 |
| The row | `docs/curriculum/W3_Build_1.md`, Saturday 24 October, all fifteen columns, and Monday's row for the week | Tracker v7 |
| The spine, its plants and its witness | `docs/detailing/W03_build1_spine.md`, approved 29 September 2026 | Approved |
| The 300-minute Saturday | `data/programme/facts.yaml`, campus_day.saturday_minutes | Locked |
| 35 learners in nine groups of four | `data/programme/facts.yaml`, cohort; the `groups` conflict with the tracker's fifteen is carried in the run sheet | Stated (handover) |
| Marks per event: mini project 40, mock 30, GD 30 | `data/programme/facts.yaml`, evaluation, proposal-2026-09-25 | Locked |
| The Build 1 rubrics, the mini project's 34 per group and 6 per learner | `data/programme/facts.yaml`, evaluation.rubrics.W03, approved 29 September 2026; read by `internal/C2_W03_SAT_build_mini_project_scoring_INTERNAL.py` and rendered by the sync into the run sheet | Locked |
| Saturday's two GD rounds, the first tranche and the drawn order | `content/W03/D5/trainer/C2_W03_D05_day_sheet_TRAINER.md` | Friday's pack |
| Dr Priya Menon, Meera Raghavan, Kavya Nair | `docs/07_Client_Zero.md` sections 1a and 1b | Locked v2.2, with the GCC addendum |
| Meera's Week 4 Monday words | `docs/curriculum/W4_Analyst_craft.md`, Monday 26 October, business scenario | Tracker v7 |
| Build 2 in Week 6, Kalpa Financial Services | `docs/programme/calendar.md`, W06 lines | Locked calendar |
| Every number in the TRAINER files | `internal/C2_W03_SAT_witness_INTERNAL.py`, reading `content/W03/D1/data/` and checking 30 figures against the spine: `RESULT: PASS (0 disagreements with the spine)` | Recomputed 29 September 2026 |
| The Week 1 examples on the presentation deck (Retail-Plus, 22 members, 5,000 shuffles, Retail-Core 2.7 percent) | `content/W01/D4/slides/C2_W01_D04_half2_STUDENT.md`, S14 | Delivered Week 1 content |
| The decisions log shape (field, issue, rows, decision, reason) | `content/W01/D3/takehome/C2_W01_D03_brief_STUDENT.md`, Part 3 | Delivered Week 1 content |

No URL enters this day's files.

## Where the files differ from the spine's wording

| The spine says | The files hold | What this pack does |
|---|---|---|
| The offer ran in three cities | Offers in all six cities: about half the patients in Bengaluru, Hyderabad and Mumbai, about a fifth in Delhi, Chennai and Pune | The question bank describes the files, and gives Delhi's positive split (23.5 percent, 316 offered) as the caveat challenge |
| The old export repeats 180 rows from a mid-quarter re-export | 180 repeated booking identifiers dated 1 June to 26 September; 145 identical on every field, the rest differing only in `updated_at` | The question bank quotes the files' dates and makes no claim about when the re-export ran |
| The generator's witness counts 60 text amounts | 35 invoice amounts carry a comma in the file | The question bank quotes 35, which is what a group reading the CSV finds |

## Decisions taken in this session

| Decision | Who, and when | Where it landed |
|---|---|---|
| A live demo runs cold once, on Friday and Saturday alike: if it breaks, the group says in one sentence what broke and why and goes to questions, with no fix and no second run | The requester, 29 September 2026, choosing Saturday's rule over Friday's two minutes to recover | Friday's day sheet (`content/W03/D5/trainer/C2_W03_D05_day_sheet_TRAINER.md`, three lines) changed to match; Saturday's deck, run sheet and question bank already carried it |

## Build notes

The decks were built with `scripts/build_deck.py` and mermaid-cli 11.17.0 on the path, installed in
the session's scratch space, because the container's mermaid-cli 12.0.0 rejects the `-w` flag the
builder passes and the builder then prints every diagram as code. The workbook and its recalc
manifest are written by `internal/C2_W03_SAT_build_grade_closure_INTERNAL.py`.

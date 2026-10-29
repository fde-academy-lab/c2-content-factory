# Sources and decisions, Build 2 run session

INTERNAL. What the run session built on branch `w06-run`, what each file rests on, and every
decision taken without the requester, each with its reason. Built on 29 October 2026 from
`CLAUDE.md`, `docs/12_Build_Week_W06.md`, `docs/detailing/W06_build2_plan.md`,
`docs/detailing/W06_briefs/common.md` and `docs/detailing/W06_briefs/run.md`.

## What did this session build?

| File | What it does |
|---|---|
| `README.md` (pack root) | Opens on the week's run table, then the four things a learner opens, the ladder, and every file in the order it is used |
| `../README.md` (`content/W06/README.md`) | The week on one screen and the link to the pack |
| `2_starter_repo/presentation/C2_W06_D02_presentation_template_STUDENT.md` and `.pptx` | The seven-slide template plus one backup slide; built with `scripts/build_deck.py` |
| `2_starter_repo/presentation/README.md`, `figures/exhibit_demo.png`, `figures/exhibit_error_bill.png` | How a group turns the template into its talk; the two dashed placeholders |
| `4_trainer_only/C2_W06_D02_presentation_figures_INTERNAL.py` | Draws the two placeholders |
| `4_trainer_only/C2_W06_D02_run_sheets_TRAINER.md` | Tuesday to Saturday, minute by minute, for the Programme Head and two TAs |
| `4_trainer_only/C2_W06_D02_rubrics_proposed_TRAINER.md` | Every rubric, marked proposed |
| `4_trainer_only/C2_W06_D02_scoring_TRAINER.xlsx`, `C2_W06_D02_scoring_recalc_INTERNAL.md`, `C2_W06_D02_build_scoring_INTERNAL.py` | One scoring workbook for the week, its recalc manifest and its builder |
| `4_trainer_only/C2_W06_D02_mock_r2_written_sheet_STUDENT.md` and `.pdf`, `C2_W06_D02_mock_r2_written_sheet_key_TRAINER.md` | The written half of Mock R2 and its key |
| `4_trainer_only/C2_W06_D02_gd_prompts_TRAINER.md` | Five GD prompts with the chair's notes and how a round runs |
| `4_trainer_only/C2_W06_D02_expert_showcase_brief_TRAINER.md` | What the industry expert is asked to show on Friday |

## Where does every number come from?

| Numbers | Source, checked 29 October 2026 |
|---|---|
| The card book (30,000 cardholders, April to September 2005, 22.1 percent default, CC BY 4.0) | `docs/detailing/W06_research/W06_datasets.md`, section 2.1 |
| The "I do" walk: 41,188 calls, 11.3 percent buy, 88.74 percent for calling nobody, 89.71 percent and 174 of 928 buyers at 0.5, Rs 40 against Rs 1,200 and the line at 0.032, Rs 279,000 against Rs 292,400 (4.6 percent), 404 against about 112 in the top 1,000, the AUC of about 0.80 rising to 0.94 with the call's length, 16 promised in 100 against 25 | The Week 5 pack: `content/W05/D2/4_trainer_only/C2_W05_D02_trainer_guide_TRAINER.md`, `content/W05/D3/4_trainer_only/C2_W05_D03_trainer_guide_TRAINER.md`, `content/W05/D5/4_trainer_only/C2_W05_D05_trainer_guide_TRAINER.md` and `docs/detailing/W05_ml_core_plan.md` |
| The leak exhibit: interest rate empty for 98.4 percent of denials and 0.7 percent of approvals, AUC 0.982 alone, 0.892 against 0.9998 | `W06_datasets.md`, section 2.6 (HMDA, Delaware 2023, public domain) |
| GD prompt 1: under 100 milliseconds, about 1 in 1,000 frauds, 0.1 percent of legitimate payments blocked | `W06_references.md`, section 3.14 (Stripe, link only) |
| GD prompt 2: 4.1 and 8.7 points, 95.3 against 93.7 percent, an overlap of about half | `W06_references.md`, section 3.13 (Ascarza 2018, link and cite only) |
| GD prompt 3: 27 percent more approvals, 16 percent lower average rates, near-prime about twice, self-reported and not replicated | `W06_references.md`, section 3.3 (CFPB, 6 August 2019) |
| GD prompt 4: USD 25 million per 90-day delay, the readiness assessment, about 157,000 notices, USD 25 million, USD 45 million and at least USD 19.8 million | `W06_references.md`, section 3.2 (CFPB, 23 October 2024, and the consent order) |
| GD prompt 5: the 2007 written-reasons rule; the 2026 draft's explainability, drift and kill-switch asks; 20.80 percent of 612, 13.70 percent of 583 | `W06_references.md`, sections 3.8, 3.9 and 3.10 |
| The expert brief's public examples (Ketan Doshi's 90 percent, Rules of ML 1 and 4, the ML Test Score, the Apple Card launch, Stripe's counterfactual estimates) | `W06_references.md`, sections 1, 2, 3.2 and 3.14 |
| The written sheet, the readiness check and every number marked illustrative or invented | Our own construction, labelled on the page |
| GD criteria (8, 8, 8, 6) and R1's viva criteria (6, 6, 3) | `data/programme/facts.yaml`, `evaluation.rubrics.W03` |
| Mini project 40 (32 and 8), Mock R2 30 (15 and 15), GD 30 | The plan's section "Proposed for the Programme Head"; decision `rubrics-and-calendar` is open |
| Dates and module | The sync blocks from `data/programme/days.json`; Week 7 Monday from `docs/programme/calendar.md` |

Every real fact on a GD card was taken from the research file's verified rows; no title, author or
figure was added from memory. Three titles first drafted from URL slugs were removed for that reason.

## Which decisions did this session take, and why?

| Decision | Reason |
|---|---|
| Staff are written PH, TA1 (the Academic TA) and TA2 (the second TA) | The requester's direction names the Programme Head and two TAs; only the Academic TA has a role name in the repository |
| Cards follow group numbers: G1 and G2 card 1, G3 and G4 card 2, G5 card 3, G6 and G7 card 4, G8 and G9 card 5, G10 and G11 card 6, G12 card 7, G13 card 8 | Both holders of a card then sit next to each other in every roster, and Saturday's two rooms split by card at 7 and 6 groups |
| Tuesday's call rooms and Thursday's gate rooms use the same staff for the same groups (PH G1 to G5, TA1 G6 to G9, TA2 G10 to G13) | The plan has the card handed over in the call and twisted at the gate; one person holding both keeps the card's story straight |
| Red-team pairs G1 and G8, G2 and G10, G3 and G12, G4 and G9, G6 and G13, and a trio G5, G7 and G11 | Thirteen groups cannot all pair; every pair holds two different cards, and the same partners record Friday's cold run and dry run 2 |
| The readiness check's six items live in the run sheet | The plan names the check and no session's file list owns it; it passes `scripts/distractor_audit.py` with keys at a, a, b, c, c and d |
| Tuesday's 20-minute frame round and the slide 1 drafts on Tuesday and Wednesday | The plan's Tuesday and Wednesday items fill about 250 of 360 minutes; the frame round is the last check before AI opens, and the drafts feed the opener the plan asks for |
| The passport is filled alone in Wednesday's TA lab | The plan has passports tested at Thursday's gate and retaken on Friday, so it must exist by Wednesday night |
| The written sheet runs at Thursday block two minute 105, after dry run 1 | The plan's Thursday lists it after dry run 1 |
| Friday's freeze at block two minute 90 with the tag `build2-freeze`; only slides and README change after it | The cold run and dry run 2 need a fixed commit and fit the 90 minutes left |
| Five GD prompts with a variant B line for reuse, instead of 13 distinct prompts | The brief asks for four or five; a changed number on reuse stops a later group replaying an earlier round |
| The industry expert chairs GD room 1 and Saturday's room B, marked proposed, with a TA fallback | Decision `build-owners` is open; the calendar names Friday and Saturday as expert days |
| Saturday runs 205 minutes: room A seven slots, room B six and a reserve | Thirteen slots of 20 cannot split evenly; the plan's 130 a room becomes 140 and 120 |
| The written sheet sits on an invented vendor book, with Part B written as true or false with a reason | No item may hand a group a Taiwan number or name a trap; a single key per item lets the audit read it |
| The written sheet is tagged STUDENT and kept in `4_trainer_only/` | Learners sit it, and the brief keeps it out of their sight until Thursday |
| One scoring workbook with Groups, Seats, Mock R2, GD, Mini project, Closure and Summary sheets | The brief asks for one workbook; one row per learner on every sheet keeps closure to one sheet |
| Build 1's demo rule carried as proposed; Friday's cold run recorded and deciding nothing | The rule was approved for Build 1 on 29 September 2026; the plan does not say what a failed cold run costs |
| The template has no cover and no breadcrumb strip | Slide 1 is the answer; `scripts/build_deck.py` draws a strip across a picture placed in a column, so the strip went and the placeholders became 10-inch strips that take a band at the foot |
| Left out: the jigsaw, the Parsons card, the expectations agreement beyond a roles line, the peer rating and the one-page memo | The approved plan's v1 changes keep learners to four things and do not list them |

## What did the checks report?

| Check | Result |
|---|---|
| `python3 scripts/verify.py content/W06/D2` | PASS on this session's files |
| `scripts/xlsx_recalc.py` | 7 verdicts computed, 12 decisions flipped and re-asserted; 1,034 formulas, 0 errors |
| `scripts/distractor_audit.py` on the written sheet | 8 keyed items, keys at a, b, c and d twice each, PASS |
| `scripts/deck_md_check.py` and `scripts/deck_check.py` on the template | PASS; 8 slides, no box overflowing; the template's two pictures print their labels above 9 points |
| `scripts/sync_programme.py --check` | Every output current after the run sheet's sync blocks were rendered |
| The tic scanner on every prose file | Clean |

## Skills read and what was taken

| Skill | Taken |
|---|---|
| training-deck-builder | One exhibit per slide, no meta-content on a slide, notes carrying the speaker and minutes |
| pptx | The render check through LibreOffice and a contact sheet of every slide |
| academic-pptx | Assertion headlines that pass the ghost deck test, about 40 words of body a slide, conclusions left on screen for questions |
| exercise-builder | True or false with the reason, distractors at the key's precision, the key file's why-the-others-fail column |
| xlsx | Formulas for every derived cell, zero formula errors, a legend naming the input cells and a worked example |
| humanizer and llm-tic-scrubber | A read of every prose file in file mode, code and paths left untouched |

# Week 6, Build 2: whom should Kalpa call before the due date?

Kalpa Financial launches credit cards in India with no card history of its own, so Rohan Desai,
head of risk, proves the method first on a public card book: UCI Default of Credit Card Clients,
30,000 Taiwanese cardholders, six monthly statements from April to September 2005, 22.1 percent of
whom defaulted in October 2005 (CC BY 4.0). Every group answers the same ask under its own
constraint card: whom do we call before the due date, when a missed default costs about five times a
wasted call, and what is the error bill of the list?

## The run table

Minutes are durations. Each day closes with the opener: a drawn member of every group says slide 1
in ninety seconds.

| Day | Minutes | What happens | Who acts | Open |
|---|---|---|---|---|
| Tue, online | 45 | Launch: Rohan's ask, the four things, the ladder, the rules | Programme Head | explorer `#story` and `#map`; this README |
| | 6 and 15 | Silent read of the ticket, then the readiness check alone and as a group | everyone | `1_project/C2_W06_D02_ticket_STUDENT.pdf` |
| | 10, then 8 per group | Question writing, then the discovery call, where Rohan hands over the card | groups; Rohan in three call rooms | the ticket's call guide and card box |
| | 60 | Stages 0 to 2 on paper, no AI | groups | `1_project/C2_W06_D02_workbook_STUDENT.pdf`, pages 1 to 3 |
| | 20 | The frame round: each group's frame in one sentence | Programme Head | workbook page 2 |
| | 40, then 56 | The starter repo set up, then breadcrumb sections 1 and 2 | a TA, then groups | `2_starter_repo/README.md`, `notebooks/breadcrumbs.ipynb` |
| | 20 and 20 | A first slide 1, then the opener | groups | `2_starter_repo/presentation/` |
| Wed | 30 | The checkpoint, three questions per group | staff | workbook pages 1 to 3 |
| | 30 | The "I do" walk up the ladder on Week 5's bank model | Programme Head | explorer `#case` |
| | 40 | The A against B sheet | groups | workbook page 4; breadcrumb section 3 |
| | 120 | The POC and its error bill | groups | workbook page 5; breadcrumb section 4 |
| | 45 | The first architecture, black box to white box | groups | workbook page 6; breadcrumb section 5 |
| | 15 and 15 | The pre-mortem, then the leak exhibit | groups; Programme Head | the challenges log; explorer `#case` |
| | 25 and 20 | Slide 1 with real numbers, then the opener | groups | `2_starter_repo/presentation/` |
| | 20, in the lab | The numbers passport, filled alone | every learner | the workbook's passport page |
| Thu | 15 per group | The approach gate, with the Mock R2 viva inside it; the card's twist handed over | three staff in three rooms | workbook pages 1 to 5 and the POC run |
| | 70 | The twist, and the architecture revised | groups | workbook page 6; breadcrumb hints |
| | 20 per pair | The red-team swap with a partner group | pairs | the A against B sheet and the passport |
| | 17 per group | Dry run 1 to the partner group, on time cards | groups | the presentation |
| | 30 | The Mock R2 written sheet, on paper | every learner | handed out in the room |
| | 20 | The opener | groups | |
| Fri | 60 | The industry showcase: one model from proof to production | the industry expert | |
| | 30 per group | GD rounds in two rooms | groups | the prompt card, handed out in the room |
| | the rest of the day | The MVP slice, README and model card; the build freeze; the evaluator runs the POC cold; dry run 2, recorded by the partner group | groups | `2_starter_repo/app/`, `templates/`, `README.md` |
| | 5 per learner | Passport retakes for anyone not yet | a TA | the repository |
| Sat | 20 per group | Talks of 12 minutes, questions 6, changeover 2, in two rooms by card | groups; the panel | the presentation |
| | 15 | The week close: one change per group for Build 3 | Programme Head | |

## The four things you open all week

| What | Where | Holds |
|---|---|---|
| The ticket | `1_project/C2_W06_D02_ticket_STUDENT.pdf` | Rohan's ask, the discovery-call guide, your card's box, the AI rules, on two sides |
| The workbook | `1_project/C2_W06_D02_workbook_STUDENT.pdf` | One page per ladder stage, then the numbers passport, the twelve-minute run sheet, the challenges log and the AI log |
| The starter repo | `2_starter_repo/` | The breadcrumb notebook, `src/`, the demo app, the README and model card templates, and the seven-slide presentation template |
| The explorer | `3_explorer/C2_W06_D02_explorer_STUDENT.html` | The story of an ML project from ask to production, the concept map, one page per ladder stage, the worked parallel and the leak exhibit, field scenes, the interview room and check yourself |

## The ladder every file shares

| Stage | Name | Workbook page | Breadcrumb section | Explorer |
|---|---|---|---|---|
| 0 | The business, black box | 1 | none | `#p1` |
| 1 | The frame | 2 | 1 | `#p1` |
| 2 | Requirements | 3 | 2 | `#p2` |
| 3 | Options A and B, one chosen | 4 | 3 | `#p3` |
| 4 | The POC and its error bill | 5 | 4 | `#p4` |
| 5 | The architecture, HLD to LLD | 6 | 5 | `#p5` |
| 6 | The MVP slice | 7 | 6 | `#p6` |
| 7 | Present and defend | 8 | none | `#p7` |

## Every file, in the order it is used

| When | File | Who |
|---|---|---|
| Tuesday, first | `1_project/C2_W06_D02_ticket_STUDENT.md` and `.pdf` | every learner |
| Tuesday, all week | `1_project/C2_W06_D02_workbook_STUDENT.md` and `.pdf` | every learner |
| Tuesday, all week | `3_explorer/C2_W06_D02_explorer_STUDENT.html` | every learner |
| Tuesday's set up, all week | `2_starter_repo/README.md`, `notebooks/breadcrumbs.ipynb`, `src/`, `app/`, `tests/`, `templates/`, `requirements.txt` | every group, in its own repository |
| From Tuesday's close | `2_starter_repo/presentation/C2_W06_D02_presentation_template_STUDENT.pptx`, its `.md` source and `README.md` | every group |
| Before Tuesday | `4_trainer_only/C2_W06_D02_run_sheets_TRAINER.md` | Programme Head and TAs |
| Tuesday's calls | `4_trainer_only/C2_W06_D02_discovery_call_script_TRAINER.md`, `4_trainer_only/C2_W06_D02_constraint_cards_TRAINER.md` | the three staff playing Rohan |
| All week, for hints | `4_trainer_only/C2_W06_D02_starter_repo_notes_TRAINER.md` | TAs |
| All week, for the numbers | `4_trainer_only/C2_W06_D02_reference_build_TRAINER.ipynb` | Programme Head and TAs |
| Thursday | `4_trainer_only/C2_W06_D02_gate_and_viva_TRAINER.md`; `4_trainer_only/C2_W06_D02_mock_r2_written_sheet_STUDENT.pdf` and its key, `4_trainer_only/C2_W06_D02_mock_r2_written_sheet_key_TRAINER.md` | the three gate staff; the Academic TA marks the written sheet |
| Friday | `4_trainer_only/C2_W06_D02_gd_prompts_TRAINER.md`; `4_trainer_only/C2_W06_D02_expert_showcase_brief_TRAINER.md` | the GD chairs; the industry expert |
| Thursday to Saturday | `4_trainer_only/C2_W06_D02_scoring_TRAINER.xlsx`, against `4_trainer_only/C2_W06_D02_rubrics_proposed_TRAINER.md` | every assessor; Programme Head at grade closure |
| For rebuilding | `4_trainer_only/C2_W06_D02_build_scoring_INTERNAL.py` and `4_trainer_only/C2_W06_D02_scoring_recalc_INTERNAL.md`; `4_trainer_only/C2_W06_D02_presentation_figures_INTERNAL.py`; `4_trainer_only/C2_W06_D02_explorer_data_INTERNAL.py` and `.json` | the content team |
| Sources | `4_trainer_only/C2_W06_D02_sources_project_INTERNAL.md`, `4_trainer_only/C2_W06_D02_sources_starter_INTERNAL.md`, `4_trainer_only/C2_W06_D02_sources_explorer_INTERNAL.md`, `4_trainer_only/C2_W06_D02_sources_run_INTERNAL.md` | the content team |

Trainers and TAs: start with `4_trainer_only/C2_W06_D02_run_sheets_TRAINER.md`.

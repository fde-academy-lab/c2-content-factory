# W05 Monday: regression and classification

Should we even build a model? Six topics on tiny invented tables, then a Portuguese bank's 41,188 calls (UCI Bank Marketing), then Kalpa's Rs 40 nudge.

## The run table

| Block | Minutes | Who acts | Open | The screen shows |
|---|---|---|---|---|
| Opening | 8 | trainer | `1_in_class_training_content/slides/C2_W05_D01_slides_STUDENT.pptx`, S1 to S6; the explorer `demos/C2_W05_D01_drag_the_line_explorer_STUDENT.html` at `#story`, then `#map` | the week's timeline picture; the ticket; calling nobody right on 88.7 percent |
| Ch 1 Is this an ML problem at all | 15 | trainer, then pairs | `notebooks/C2_W05_D01_ch01_ml_problem_or_not_STUDENT.ipynb`, then the explorer at `#p1` | six questions sorted: 2 queries, 2 rules, 2 predictions |
| Ch 2 What do we know, and when | 22 | trainer | `notebooks/C2_W05_D01_ch02_input_target_time_STUDENT.ipynb`, then the explorer at `#p2` | four members on a timeline; only M1 repeats |
| Ch 3 Don't peek at the exam paper | 20 | trainer | `notebooks/C2_W05_D01_ch03_split_seed_baseline_STUDENT.ipynb`, then the explorer at `#p3` | two seeds, two splits; the baseline at 75 percent |
| Ch 4 Drawing the best line | 22 | trainer, learners draw | `notebooks/C2_W05_D01_ch04_linear_regression_STUDENT.ipynb`, then the explorer at `#p4` | residual squares: 5,200 against 5,480 |
| Break | 10 | everyone | | kernels shut |
| Ch 5 From a line to a probability | 22 | trainer | `notebooks/C2_W05_D01_ch05_logistic_regression_STUDENT.ipynb`, then the explorer at `#p5` | the line at 1.28, the S at 0.73 |
| Ch 6 What the leftovers confess | 18 | trainer | `notebooks/C2_W05_D01_ch06_residuals_auto_mpg_STUDENT.ipynb`, then the explorer at `#p6` | the bowed residuals of 392 cars, then flat |
| Case 1 Whom should the bank call | 43 | trainer, then everyone in the guided notebook | `notebooks/C2_W05_D01_case01_whom_to_call_STUDENT.ipynb`, then `notebooks/C2_W05_D01_guided_frame_and_split_STUDENT.ipynb`; the explorer at `#case`, chapter 7 | the split with the test slice sealed; PASS lines in the guided progress cell |
| Case 2 Beat the dumbest model | 25 | trainer | `notebooks/C2_W05_D01_case02_beat_the_baseline_STUDENT.ipynb`, then the explorer at `#case`, chapter 8 | 0.8874 against 0.8971: 80 more right answers |
| Case 3 The peek | 15 | trainer | `notebooks/C2_W05_D01_case03_the_peek_STUDENT.ipynb`, then the explorer at `#case`, chapter 9 | 0.9055 peeked, 0.8971 on fresh rows |
| Interview corner, seat, quiz, close | 20 | trainer, then everyone on Kahoot | deck S50 to S53; the explorer at `#interview`, then the six seats at `#field` | five anchors; the senior ML engineer's seat lit |
| IITGN faculty block (tentative) | 120 | IITGN faculty | | |
| TA-led practice lab | 85 | TAs, then learners | `case03` on the projector, then `2_take_home_mandatory/C2_W05_D01_practice_lab_STUDENT.ipynb` | the rule baseline; Kalpa's repeat flag in SQL |

## Before the first chapter

- Setup: open notebook `ch01`, run the first two cells, and see six questions print. The case notebooks download two public files once (UCI Bank Marketing, about 1 MB zipped, and UCI Auto MPG, under 20 KB) into `~/.cache/c2_datasets`; later runs read the cached copy and nothing is written into the repository.
- One notebook open at a time; shut every kernel at the break.
- Fallback: every notebook ships executed, so the outputs can be projected without running anything; the explorer `1_in_class_training_content/demos/C2_W05_D01_drag_the_line_explorer_STUDENT.html` opens as a local file with no network, and its twelve pages run from the story to check yourself.

## After class

| What | Where | Minutes |
|---|---|---|
| The practice set, mandatory: ten problems, eighteen self-check questions, the key at the end | `2_take_home_mandatory/C2_W05_D01_practice_set_STUDENT.pdf` | 150 |
| The practice lab, if not finished with the TAs | `2_take_home_mandatory/C2_W05_D01_practice_lab_STUDENT.ipynb` | 30 to 60 |
| Study notes, before Tuesday | `3_study_material_for_students/C2_W05_D01_study_notes_STUDENT.pdf` | 30 |
| Cheat sheet, pinned | `3_study_material_for_students/C2_W05_D01_cheat_sheet_STUDENT.pdf` | 5 |
| Interview questions, two out loud | `3_study_material_for_students/C2_W05_D01_interview_bank_STUDENT.pdf`, or the explorer's `#interview` and `#check` | 20 |

Trainers and TAs: `4_trainer_only/C2_W05_D01_trainer_guide_TRAINER.md` first.

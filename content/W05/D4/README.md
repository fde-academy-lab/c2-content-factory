# Week 5 Thursday: overfitting and regularisation

Generalise or memorise, and the honest tuned model. Thursday 5 November 2026.

## The day, in the order it runs

| Block | Minutes | Who acts | Open | The screen shows |
|---|---|---|---|---|
| Opening | 10 | trainer | `1_in_class_training_content/slides/C2_W05_D04_slides_STUDENT.pptx`, S1 to S6 | the ticket: a tree at 99.6 percent on training, its validation score still hidden, 88.7 for calling nobody |
| Chapter 1: Memorising against learning | 25 | trainer, learners follow | `notebooks/C2_W05_D04_ch01_memorising_against_learning_STUDENT.ipynb`, then the explorable | three students' practice and exam scores; the explorable at degree 12 |
| Chapter 2: Putting brakes on the model | 20 | trainer, learners follow | `notebooks/C2_W05_D04_ch02_putting_brakes_on_the_model_STUDENT.ipynb`, explorable brake slider | the seven-bend curve with and without a brake |
| Chapter 3: Five exams instead of one | 20 | trainer, learners follow | `notebooks/C2_W05_D04_ch03_five_exams_instead_of_one_STUDENT.ipynb`, explorable reshuffle | the 5 by 20 fold grid |
| Drill 1 | 15 | learners | the deck, after S22 | four curve pairs to name |
| Break | 10 | | shut every kernel | |
| Chapter 4: Trees, forests and groups | 15 | trainer, learners follow | `notebooks/C2_W05_D04_ch04_trees_forests_and_groups_STUDENT.ipynb` | a two-question tree, a forest's vote, k-means groups |
| Chapter 5: Why the boring model often ships | 20 | trainer, learners follow | `notebooks/C2_W05_D04_ch05_why_the_boring_model_often_ships_STUDENT.ipynb` | the two tests and the pneumonia AUCs |
| Case 1: The tree that aced practice | 30 | learners run, trainer narrates | `notebooks/C2_W05_D04_case01_the_tree_that_aced_practice_STUDENT.ipynb` | the U of validation error against depth |
| Guided | 15 | learners | `notebooks/C2_W05_D04_guided_learning_curves_and_one_cv_STUDENT.ipynb` | three mystery learning curves, A, B and C |
| Case 2: Five exams on the bank's file | 20 | learners run, trainer narrates | `notebooks/C2_W05_D04_case02_five_exams_on_the_bank_file_STUDENT.ipynb` | five deals against five folds; the C sweep |
| Case 3: The three-way race, with drill 2 | 25 | learners run, trainer narrates | `notebooks/C2_W05_D04_case03_the_three_way_race_STUDENT.ipynb` | four models on the same folds; the rupee break-even |
| Close: interview corner and quiz | 15 | trainer, then Kahoot | the deck, S53 to S55 | the four interview anchors, then the quiz |
| IITGN faculty session (tentative) | 120 | faculty | their own material | the bias-variance decomposition and the penalty shapes |
| Practice lab | about 90 | TAs | `2_take_home_mandatory/C2_W05_D04_practice_lab_STUDENT.ipynb` | German Credit's lending book |

The notebooks sit in `1_in_class_training_content/notebooks/`. The explorable is `1_in_class_training_content/demos/C2_W05_D04_depth_and_brake_explorer_STUDENT.html`.

## Before the first slide

- **Setup**: open notebook ch01 in the Codespace, run the first cell, see "Charts and the check() helper are ready." Then open case01 and run its first three cells, see "41,188 calls, 21 columns, 11.27% said yes"; the bank's file is now cached for every later notebook.
- **One notebook open at a time**; shut every kernel at the break.
- **Fallback**: every notebook ships executed, so the outputs show on GitHub with no kernel; the explorable opens as a local file with no network.

## After class

| What | Minutes |
|---|---|
| `2_take_home_mandatory/C2_W05_D04_practice_set_STUDENT.md` (or the PDF): ten problems and eighteen self-checks | 150 |
| `3_study_material_for_students/C2_W05_D04_study_notes_STUDENT.md`, read once | 30 |
| `3_study_material_for_students/C2_W05_D04_cheat_sheet_STUDENT.md`, redraw the U from memory | 10 |
| `3_study_material_for_students/C2_W05_D04_interview_bank_STUDENT.md`, five questions aloud | 20 |

## For the trainer and the TAs

`4_trainer_only/C2_W05_D04_trainer_guide_TRAINER.md` (the run table, how to teach each chapter, the quiz keys, the lab run sheet), `4_trainer_only/C2_W05_D04_practice_lab_solutions_TRAINER.ipynb`, and `4_trainer_only/C2_W05_D04_sources_INTERNAL.md`. The deck's charts are drawn by `4_trainer_only/C2_W05_D04_make_figures_INTERNAL.py`; after `scripts/build_deck.py`, run `4_trainer_only/C2_W05_D04_strip_branding_INTERNAL.py` on the new .pptx.

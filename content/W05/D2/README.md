# Week 5, Tuesday: the metric trap

Scoring the model the way the business will judge it, in two businesses.

## The day, block by block

| Block | Min | Who acts | Open | The screen shows |
|---|---|---|---|---|
| Opening | 8 | trainer | `slides/C2_W05_D02_slides_STUDENT.pptx`, slides 1 to 6 | Kavya's question, the 20-week roadmap, the week's picture, the six topics |
| Ch 1 Four boxes that tell the truth | 18 | trainer, then learners | `notebooks/C2_W05_D02_ch01_confusion_matrix_STUDENT.ipynb` | twenty invented customers sorted into TP, FP, FN, TN |
| Ch 2 Of those we flagged, of those we missed | 20 | trainer, then learners | `notebooks/C2_W05_D02_ch02_precision_recall_f1_STUDENT.ipynb` | precision 3 of 6, recall 3 of 5, the F1 curve |
| Ch 3 Why 89 percent can mean zero | 15 | trainer, then learners | `notebooks/C2_W05_D02_ch03_class_imbalance_accuracy_STUDENT.ipynb` | 100 dots, the say-no rule at 89 percent |
| Drill: four matrices | 12 | learners in pairs | slide 20 | four matrices, precision and recall for each |
| Ch 4 What does each mistake cost? | 22 | trainer, then learners | `notebooks/C2_W05_D02_ch04_metric_from_business_cost_STUDENT.ipynb` | thirty Rs 40 coins against one Rs 1,200 buyer |
| Ch 5 Where to draw the line | 20 | trainer, then learners | `notebooks/C2_W05_D02_ch05_threshold_selection_STUDENT.ipynb`, then `demos/C2_W05_D02_threshold_explorer_STUDENT.html` | the bill falling as the line slides left |
| Financial services story | 15 | trainer | `4_trainer_only/C2_W05_D02_domain_story_TRAINER.md` | how a lender earns and loses money |
| Ch 6 Same model, opposite threshold | 15 | trainer, then learners | `notebooks/C2_W05_D02_ch06_transfer_lending_threshold_STUDENT.ipynb` | Retail's line at 0.032, Rohan's at 0.952 |
| Case 1 The do-nothing matrix | 15 | trainer, then learners | `notebooks/C2_W05_D02_case01_do_nothing_matrix_STUDENT.ipynb` | the bank's empty column: 88.74 percent, 0 buyers |
| Case 2 The cost threshold | 20 | trainer, then learners | `notebooks/C2_W05_D02_case02_cost_threshold_STUDENT.ipynb` | the bill curve, Rs 279,000 against Rs 292,400 |
| Case 3 The budget | 18 | trainer, then learners | `notebooks/C2_W05_D02_case03_budget_precision_at_k_STUDENT.ipynb` | 404 buyers in the top 1,000 against about 112 at random |
| Guided memo and transfer note | 20 | learners | `notebooks/C2_W05_D02_guided_metric_memo_STUDENT.ipynb` | PASS lines as each step is filled |
| Interview corner, quiz, close | 12 | trainer | slides 55 to 64, Kahoot | five interview anchors, five quiz questions |
| IITGN faculty block W5-2 (tentative) | 120 | faculty | their material | ROC, precision-recall curves and expected cost |
| Practice lab | about 90 | TAs | `2_take_home_mandatory/C2_W05_D02_practice_lab_STUDENT.ipynb` | German Credit's 5 to 1 cost matrix |

Folders below `1_in_class_training_content/` are written short in the table: `slides/`, `notebooks/` and `demos/` all sit inside it.

## Before the first chapter

- **Setup.** Open `notebooks/C2_W05_D02_ch01_confusion_matrix_STUDENT.ipynb` in the Codespace, run the first cell and see a table of twenty customers. Then open `case01` and run its first cell once: it downloads the bank's file (about 1 MB) into `~/.cache/c2_datasets` and prints `rows 41,188`. Every later run reads the cache.
- **One notebook open at a time.** Shut each kernel when its chapter ends and all kernels at the break.
- **Fallback.** Every notebook is saved with its outputs, so the projector can show a notebook without running it. The explorable is one HTML file that opens offline in any browser.

## After class

| What | Folder | Min |
|---|---|---|
| Practice set: recap, ten problems, eighteen self-check questions, key and model solutions | `2_take_home_mandatory/C2_W05_D02_practice_set_STUDENT.md` (and .pdf) | 150 |
| Practice lab, if it did not finish with the TAs (extra practice) | `2_take_home_mandatory/C2_W05_D02_practice_lab_STUDENT.ipynb` | extra |
| Study notes | `3_study_material_for_students/C2_W05_D02_study_notes_STUDENT.md` (and .pdf) | 30 |
| Cheat sheet | `3_study_material_for_students/C2_W05_D02_cheat_sheet_STUDENT.md` (and .pdf) | 5 |
| Interview question bank | `3_study_material_for_students/C2_W05_D02_interview_bank_STUDENT.md` (and .pdf) | before interviews |
| Financial services dossier and its one-page card | `3_study_material_for_students/C2_W05_D02_domain_financial_services_STUDENT.md` and `C2_W05_D02_financial_services_card_STUDENT.md` | 25 |
| Wednesday's ten-minute pre-read | the last page of the practice set | 10 |

## Every file, in the order it is used

| File | Who |
|---|---|
| `1_in_class_training_content/slides/C2_W05_D02_slides_STUDENT.md` and `.pptx` (pictures in `slides/img/`) | trainer, projected |
| `1_in_class_training_content/notebooks/C2_W05_D02_ch01` to `ch06` | everyone, in class |
| `1_in_class_training_content/demos/C2_W05_D02_threshold_explorer_STUDENT.html` | everyone, in class |
| `1_in_class_training_content/notebooks/C2_W05_D02_case01` to `case03` | everyone, in class |
| `1_in_class_training_content/notebooks/C2_W05_D02_guided_metric_memo_STUDENT.ipynb` | everyone, in class |
| `2_take_home_mandatory/C2_W05_D02_practice_set_STUDENT.md` and `.pdf` | every learner, tonight |
| `2_take_home_mandatory/C2_W05_D02_practice_lab_STUDENT.ipynb` | the TA-led lab |
| `3_study_material_for_students/` notes, cheat sheet, interview bank, the financial services dossier and card | every learner |
| `4_trainer_only/C2_W05_D02_trainer_guide_TRAINER.md` | trainer and TAs, before the day |
| `4_trainer_only/C2_W05_D02_domain_story_TRAINER.md` | trainer, the financial services story |
| `4_trainer_only/C2_W05_D02_practice_lab_solutions_TRAINER.ipynb` | TAs |
| `4_trainer_only/C2_W05_D02_sources_INTERNAL.md` and the two build helpers | the build |

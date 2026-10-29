# Week 5 Wednesday: feature engineering and leakage, what the model is allowed to know

| Block | Minutes | Who acts | Open | The screen shows |
|---|---|---|---|---|
| Opening | 10 | trainer | `1_in_class_training_content/slides/C2_W05_D03_slides_STUDENT.pptx`, cover to S5; explorer `#story` and `#map` | the platform lead's quote, the week's picture, the ticket |
| Ch 1 Turning raw columns into signals | 22 | trainer, then learners | `notebooks/C2_W05_D03_ch01_feature_engineering_STUDENT.ipynb`, then explorer `#p1` | eight invented members; Hari ranked first by spend and coldest by recency |
| Ch 2 Teaching a model to read categories | 18 | trainer, then learners | `notebooks/C2_W05_D03_ch02_encoding_scaling_STUDENT.ipynb`, then explorer `#p2` | A's nearest neighbour changes from B to C after scaling |
| Ch 3 Answers from the future | 20 | trainer, then learners | `notebooks/C2_W05_D03_ch03_leakage_prediction_time_STUDENT.ipynb`, then explorer `#p3` | 12 of 12 on the training table, 6 of 12 on the nudge morning |
| Break | 10 | | | |
| Ch 4 Interrogating every column | 15 | trainer, then learners | `notebooks/C2_W05_D03_ch04_column_audit_STUDENT.ipynb`, then explorer `#p4` | nine columns on a timeline: keep, fix, drop |
| Ch 5 What the importance chart can't tell you | 15 | trainer, then learners | `notebooks/C2_W05_D03_ch05_feature_importance_STUDENT.ipynb`, then explorer `#p5` | twins alone cost 2 and 4 answers, together 8 |
| Case 1 The junior's join | 20 | learners | `notebooks/C2_W05_D03_case01_the_junior_join_STUDENT.ipynb`, then explorer `#case` tab Ch 6 | AUC 0.761, 0.795, 0.932; accuracy one point |
| Guided | 20 | learners in pairs | `notebooks/C2_W05_D03_guided_two_features_three_columns_STUDENT.ipynb` | three TODO cells, then the check cell |
| Case 2 Every column on the timeline | 30 | learners | `notebooks/C2_W05_D03_case02_prediction_time_audit_STUDENT.ipynb`, then explorer `#case` tabs Ch 7 | the audit table; honest AUC 0.796; the bill chart |
| Lunch | | | | |
| Case 3 The sign that flipped | 20 | learners | `notebooks/C2_W05_D03_case03_sign_flip_importance_STUDENT.ipynb`, then explorer `#case` tabs Ch 8 | euribor3m from -0.92 to +0.77; the importance chart |
| Unguided | 20 | learners | a blank notebook | the audited feature set rebuilt, 0.796 reproduced |
| Interview corner, quiz, close | 20 | trainer | slides S54 to S56, explorer `#interview`, Kahoot | four anchors; five questions and a return question |
| IITGN faculty block W5-3 (tentative) | 120 | faculty | | |
| Practice lab | about 90 | TA | `2_take_home_mandatory/C2_W05_D03_practice_lab_STUDENT.ipynb` | German Credit, the same audit |

**Setup.** Open notebook ch01 in the Codespace and run the first code cell; the bank's file
downloads once into `~/.cache/c2_datasets` and the cell prints 41,188 rows. Every later notebook
reads the cached copy.

**One notebook open at a time.** Shut each kernel before opening the next one, and shut all kernels
at the break.

**Fallback.** Every notebook ships executed, so the outputs can be projected without running
anything. The explorer, `1_in_class_training_content/demos/C2_W05_D03_leakage_timeline_explorer_STUDENT.html`, is a single HTML file that opens from disk with no network; each page opens from its side menu, its number key or its name after the address (`#p3`), and P turns on presenter mode.

## After class

| What | Where | Minutes |
|---|---|---|
| The practice set: recap, ten problems, eighteen self-check questions, the key | `2_take_home_mandatory/C2_W05_D03_practice_set_STUDENT.md` (and `.pdf`) | 150 |
| The practice lab, if the TA lab did not finish it | `2_take_home_mandatory/C2_W05_D03_practice_lab_STUDENT.ipynb` | 90, extra |
| Study notes | `3_study_material_for_students/C2_W05_D03_study_notes_STUDENT.md` (and `.pdf`) | 30 |
| Cheat sheet | `3_study_material_for_students/C2_W05_D03_cheat_sheet_STUDENT.md` (and `.pdf`) | 5 |
| Interview question bank | `3_study_material_for_students/C2_W05_D03_interview_bank_STUDENT.md` (and `.pdf`) | 30 |
| The explorer's field scenes and checks | `demos/C2_W05_D03_leakage_timeline_explorer_STUDENT.html#field`, then `#check` | 20 |
| Redraw the week's picture from memory, with `duration` placed | paper | 5 |

## Every file, in the order it is used

| Folder | File | Used |
|---|---|---|
| `1_in_class_training_content/slides/` | `C2_W05_D03_slides_STUDENT.md` and `.pptx`, pictures in `img/` | all day |
| `1_in_class_training_content/notebooks/` | `ch01` to `ch05`, `case01`, `guided`, `case02`, `case03` | in that order |
| `1_in_class_training_content/demos/` | `C2_W05_D03_leakage_timeline_explorer_STUDENT.html` | the opening, every chapter, after class |
| `2_take_home_mandatory/` | practice set (`.md`, `.pdf`), practice lab | after class |
| `3_study_material_for_students/` | study notes, cheat sheet, interview bank (each `.md` and `.pdf`) | after class |
| `4_trainer_only/` | trainer guide, lab solutions, sources, build helpers | before the day |

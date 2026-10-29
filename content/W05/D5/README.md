# Week 5 Friday: model justification, the committee memo

## The run table

| Block | Min | Who acts | Open | The screen shows |
|---|---|---|---|---|
| Meera's brief; the room lists each seat's push | 12 | trainer, then learners | `slides/C2_W05_D05_slides_STUDENT.pptx`, cover to S6, then the explorer's `#story` and `#map` on learners' screens | The brief, the week map, the four seats; the bill of shipping 0.5, Rs 8.61 lakh, after the story's prediction |
| Ch 1 Selling a model to people who don't care about AUC | 15 | trainer, learners run | S7 to S10, `notebooks/C2_W05_D05_ch01_model_justification_STUDENT.ipynb`, then the explorer's `#p1` | 20 gym members ranked; AUC as 60 of 75 pairs |
| Ch 2 What will mistakes cost us | 15 | trainer, learners run | S11 to S14, `ch02_error_bill`, then the explorer's `#p2` | The bill at every cut: Rs 1,830 at 0.5, Rs 360 at the cheapest |
| Ch 3 When the model goes stale | 15 | trainer, learners run | S15 to S18, `ch03_staleness_rule`, then the explorer's `#p3` | Promise against real, the alarm month |
| Ch 4 Moving the model to lending | 11 | trainer, learners run | S19 to S22, `ch04_transfer_paragraph`, then the explorer's `#p4` | One axis, three cuts |
| Ch 5 Defending it in the room | 10 | trainer, learners run | S23 to S26, `ch05_memo_under_challenge`, then the explorer's `#p5` | The memo as seconds; the seats' pushes |
| Break | 10 | | | |
| Case 1 The bill for the near-tie | 25 | trainer drives, learners follow | S27 to S31, `case01_bill_for_the_near_tie`, then the explorer's `#case`, chapter 6 | Three bills level with calling everyone; buyers in the top 1,000 |
| Case 2 Train early, score late | 30 | trainer drives, learners follow | S32 to S39, `case02_staleness_reveal`, then the explorer's `#case`, chapter 7 | The promise sagging below reality, month by month |
| Case 3 Lending, and the envelope | 22 | trainer drives, learners follow | S40 to S44, `case03_transfer_and_envelope`, then the explorer's `#case`, chapter 8 | German Credit's cost curve; the sealed test opened once |
| Guided: claim, evidence and the bill | 25 | learners in pairs | `notebooks/C2_W05_D05_guided_committee_memo_STUDENT.ipynb` | TODO cells turning into PASS lines |
| Unguided: caveat, action, rule, transfer | 20 | learners | the memo on paper, S44 | Each pair's memo under 300 words |
| Pair challenge and the 90-second rehearsal | 20 | learners in pairs | S45, S26 | One partner speaks, one pushes from a seat |
| Interview corner, Kahoot, close | 20 | trainer | S46 to S51, the explorer's `#interview`, then Kahoot | The four anchors; ME1's scope said aloud |
| Practice lab, after the second block | about 90 | TAs | `2_take_home_mandatory/C2_W05_D05_practice_lab_STUDENT.ipynb` | Rohan's memo on German Credit |

Folders below `1_in_class_training_content/` are written short in the table: `slides/`, `notebooks/` and `demos/` all sit inside it. The explorer is `demos/C2_W05_D05_error_bill_explorer_STUDENT.html`, and `#p1` and the like name the page of it to open; typing the name after the file's address opens that page directly.

**Setup.** Open notebook ch01 in the Codespace and run the first cell; it prints "20 members (invented), 5 came back". The first case notebook downloads the bank's file (about 1 MB) once into `~/.cache/c2_datasets`; later notebooks read the cached copy.

**One notebook open at a time.** Shut each kernel before opening the next one, and shut all kernels at the break.

**Fallback.** Every notebook ships executed, so the projector can show the outputs without running anything. The explorer `demos/C2_W05_D05_error_bill_explorer_STUDENT.html` opens as a local file with no network.

## After class

| What | Minutes | File |
|---|---|---|
| The practice set: ten problems, the MCQs, self-checked with the key at the end | 150 | `2_take_home_mandatory/C2_W05_D05_practice_set_STUDENT.md` (and .pdf) |
| WRITE: your memo, final, under 300 words | inside the practice set | problem 10 |
| The practice lab, extra practice after the TA-led lab | 90 | `2_take_home_mandatory/C2_W05_D05_practice_lab_STUDENT.ipynb` |
| Study notes, before Saturday's revision | 30 | `3_study_material_for_students/C2_W05_D05_study_notes_STUDENT.md` (and .pdf) |
| Cheat sheet, the week on two pages | 10 | `3_study_material_for_students/C2_W05_D05_cheat_sheet_STUDENT.md` (and .pdf) |
| Interview bank, before any interview | as needed | `3_study_material_for_students/C2_W05_D05_interview_bank_STUDENT.md` (and .pdf) |
| The explorer's field scenes, interview room and checks, worked alone | as needed | `1_in_class_training_content/demos/C2_W05_D05_error_bill_explorer_STUDENT.html`, pages `#field`, `#interview` and `#check` |

## Every file, in the order it is used

| Folder | File |
|---|---|
| `1_in_class_training_content/slides/` | `C2_W05_D05_slides_STUDENT.md` and `.pptx`; `img/` holds the 13 charts the deck places |
| `1_in_class_training_content/notebooks/` | `ch01_model_justification`, `ch02_error_bill`, `ch03_staleness_rule`, `ch04_transfer_paragraph`, `ch05_memo_under_challenge` |
| | `case01_bill_for_the_near_tie`, `case02_staleness_reveal`, `case03_transfer_and_envelope` |
| | `guided_committee_memo` |
| `1_in_class_training_content/demos/` | `C2_W05_D05_error_bill_explorer_STUDENT.html` |
| `2_take_home_mandatory/` | `C2_W05_D05_practice_set_STUDENT.md` and `.pdf`; `C2_W05_D05_practice_lab_STUDENT.ipynb` |
| `3_study_material_for_students/` | `C2_W05_D05_study_notes_STUDENT`, `C2_W05_D05_cheat_sheet_STUDENT`, `C2_W05_D05_interview_bank_STUDENT`, each `.md` and `.pdf` |
| `4_trainer_only/` | `C2_W05_D05_trainer_guide_TRAINER.md`, `C2_W05_D05_practice_lab_solutions_TRAINER.ipynb`, `C2_W05_D05_sources_INTERNAL.md`, and the build helper `C2_W05_D05_make_figures_INTERNAL.py`, which draws the deck's charts |

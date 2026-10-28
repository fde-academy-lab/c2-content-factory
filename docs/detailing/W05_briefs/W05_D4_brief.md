# W05 Thursday (D4): Overfitting and regularisation, in the Week 5 artifact set

Your day: Thursday 5 November 2026, "Overfitting and regularisation: generalise or memorise, and
the honest tuned model". Folder `content/W05/D4/`, file stem `C2_W05_D04_`.

## Your day's spine (from the approved plan)

| # | Row subtopic, verbatim (the chapter's italic line) | Relatable title (the pill) | Also searched as |
|---|---|---|---|
| 1 | Overfitting; bias and variance through learning curves | Memorising against learning | overfitting vs underfitting, bias variance, learning curves |
| 2 | Regularisation | Putting brakes on the model | L1 L2 regularization, ridge, lasso |
| 3 | Cross-validation | Five exams instead of one | k-fold cross validation |
| 4 | Trees, ensembles, clustering: used, compared, not derived | Trees, forests and groups | decision tree, random forest, gradient boosting, k-means |
| 5 | When the simpler model wins | Why the boring model often ships | model selection, Occam's razor |

- Concept chapters on tiny invented examples (a student who memorises past papers; the unlimited
  tree drawn as one leaf per customer before any depth curve). Clustering gets one slide and one
  cell only.
- Case chapters on the week's pipeline with Wednesday's honest feature set (customer table plus
  economy plus the engineered pdays flag, no `duration`): (1) the unlimited tree, about 0.996 on
  training and 0.836 on validation, below the 0.887 baseline (correction 6; the row's 100 and 61
  will not appear, quote what you run), then the depth curve and learning curves; (2)
  cross-validation done right, scaling inside the folds, and the note that rows run in time order;
  (3) regularised logistic against a tuned tree against boosting (about 0.803, 0.804, 0.811),
  their error bills within a few percent, and the gap, in rupees, at which the complex model would
  ship. The Netflix Prize case from `W05_cases.md` carries "the simpler model wins".
- STOP BEFORE: ensemble internals, boosting mathematics, search frameworks (the faculty block W5-4
  and W5-5, tentative).
- Spotlight seat: QA and tester (what breaks it, which split, which segment).
- The explorable: depth and penalty sliders with training against validation, per
  `W05_explorables.md` Thursday.
- The week's timeline picture in its Thursday state: the U of validation error against depth.

## How this build runs

You are building one teaching day of Week 5 (the machine learning core) of the IITGN Cohort 2 PG
Diploma in AI-ML and Agentic AI Engineering, in /home/user/c2-content-factory. Work in one long
turn: nobody will answer questions, so decide within the rules below and record each decision in
the day's sources file. Branch `w05-d4`, cut from `origin/main`
(`git fetch origin main && git checkout -B w05-d4 origin/main`), pushed with
`git push -u origin w05-d4`. Commit as you go, in small commits whose messages say what changed.
Never open, merge or close a pull request.

**The room**: 39 learners averaging 4 out of 10. They jump to a technique, hold one view at a time
and read problems immaturely, which is what interviews reject. Everything you build trains five
habits (the week's plan, section 2): read before answering (some scenarios are under-specified on
purpose and the model answer opens with the clarifying question), name the deciding seat out of six,
state every rule with the condition that flips it, carry numbers the learner owns, and write model
answers as reasoning with the interviewer's two follow-ups, never as paragraphs to memorise.

**The requester's direction, 28 October 2026, in substance**: fewer, clearly named folders; slides
that are pictures, outputs, mental maps and diagrams with very little text; chapter names that are
relatable, with the standard term learners would search on YouTube beside them; teaching that is
granular, practical and short-winded, in the spirit of Krish Naik (code-along to a working result),
3Blue1Brown and StatQuest (the picture from tiny numbers), freeCodeCamp and good Medium tutorials
(setup covered, every step shown, something useful at the end); real company names related back to
Kalpa; public data downloaded in code, never generated; no logo of any kind in any artifact;
interview readiness everywhere, technical, techno-functional, scenario and client-facing; a lean
trainer guide that is mostly how to teach; no over-verification.

## Read first, in this order

1. `CLAUDE.md`, above all the section "From Week 5 on".
2. `docs/11_Artifact_Set_W05.md`: the contract for every file you ship. It wins over the older
   build workflow, `the-standard.md` and the day-pack-builder skill on folders, artifacts and review.
3. `docs/detailing/W05_ml_core_plan.md`: the approved week plan. Your day's row in section 0 and
   its story in section 4 are your spine; this approval covers your day.
4. Your day's section of `docs/curriculum/W5_ML_core_ME1.md`, all fifteen columns. Its Subtopics
   column is your chapter list, verbatim and in order; its interview angle, STOP BEFORE, COMES
   LATER, Kahoot plan and faculty block are binding. Its "Client zero data (TRAINER ONLY)" and
   "WHAT THE DATA REVEALS" lines describe Kalpa v6 data that was never generated: take the lesson,
   and take your numbers from the public data you run.
5. `docs/detailing/W05_research/`: start with `W05_week_pipeline.md` (the week's shared loader,
   column plan, split and numbers, and the senior ML engineer's six corrections, which bind every
   day), then the measured datasets (`W05_datasets.md`), the verified company cases
   (`W05_cases.md`), the question-design rubric and exemplars (`W05_question_design.md`) and the
   explorable principles and per-day designs (`W05_explorables.md`). Use their numbers and links;
   re-check any link you print and date it.
6. Skills, read for the parts you need and named in your report with what you took: training-deck-
   builder and pptx (deck structure, the build and the render check), notebook-builder (the rhythm
   and checks), exercise-builder (distractor discipline), study-notes-builder and fde-cheat-sheets
   (the notes and the sheet), companion-builder and design-taste-frontend (the explorable),
   concept-packaging (hooks), humanizer and llm-tic-scrubber (every prose file).
7. For the deck format, open one built Week 4 deck markdown (for example
   `content/W04/D3/slides/C2_W04_D03_half1_STUDENT.md`) and the docstring of `scripts/build_deck.py`;
   your deck uses the same markdown format with far less text per slide.

## What you ship (the contract has the detail)

```
content/W05/D4/
  README.md                          the run table first; every file in the order it is used
  1_in_class_training_content/
    slides/C2_W05_D04_slides_STUDENT.md and .pptx, slides/img/ for our own PNGs
    notebooks/C2_W05_D04_ch0N_<slug>_STUDENT.ipynb   one per concept chapter, 8 to 15 cells
    notebooks/C2_W05_D04_case0N_<slug>_STUDENT.ipynb one per case chapter, each building on the last
    notebooks/C2_W05_D04_guided_<slug>_STUDENT.ipynb the row's GUIDED exercise, TODOs, answer last
    demos/C2_W05_D04_<slug>_explorer_STUDENT.html     the day's explorable
  2_take_home_mandatory/
    C2_W05_D04_practice_set_STUDENT.md and .pdf       two to three hours, key and solutions inside
    C2_W05_D04_practice_lab_STUDENT.ipynb             the TA-led lab, extra practice
  3_study_material_for_students/
    C2_W05_D04_study_notes_STUDENT.md and .pdf
    C2_W05_D04_cheat_sheet_STUDENT.md and .pdf
    C2_W05_D04_interview_bank_STUDENT.md and .pdf
  4_trainer_only/
    C2_W05_D04_trainer_guide_TRAINER.md
    C2_W05_D04_practice_lab_solutions_TRAINER.ipynb
    C2_W05_D04_sources_INTERNAL.md
```

Build in this order, so the most-used files exist first if time runs short: the case notebooks
(they produce the numbers and the charts everything else quotes), the concept notebooks, the deck
and its PNGs, the trainer guide and README, the practice set, the explorable, the interview bank,
the study notes, the cheat sheet, the practice lab and its solutions.

**Sizes**: the deck 45 to 65 slides; the practice set ten problems (three warm-ups of about five
minutes, four medium of about ten, three interview-grade of about fifteen) and fifteen to twenty
MCQs, which with checking fits two and a half hours; the interview bank 25 to 30 questions; the
study notes six to ten printed pages; the cheat sheet one to two pages; the trainer guide's first
screen four tables.

**Notebooks**: every data notebook downloads its public file in code with the cached loader from
the contract, writes nothing into the repository, ships executed (run with
`jupyter nbconvert --to notebook --execute --inplace`), draws at least one chart, and prints at least
two checks as lines that start with PASS. Charts the deck shows are saved from the same code into
`slides/img/` by a helper script in `4_trainer_only/` named `C2_W05_D04_make_figures_INTERNAL.py`.
Install what you need with pip (scikit-learn, pandas, matplotlib, nbconvert, ipykernel).

**Printing**: `python3 scripts/build_doc.py content/W05/D4` prints the STUDENT markdown in
folders 2 and 3. Formulas are written in plain text or code spans, never LaTeX. A page break is
`<div class="page-break"></div>`. Build the deck with `python3 scripts/build_deck.py <deck.md>`
and look at three rendered slides before you finish.

## Time budget

You have about five hours. Push a complete first version of every file in the list within four
hours of starting, even if some are lean, then spend what is left raising the deck, the practice
set and the explorable. The orchestrating session reviews and merges whatever is on your branch
about five and a half hours after launch, so an unpushed file does not exist. Do not spend time on
re-verification beyond one `verify.py` run and its fixes.

## Rules

Durations only, never clock times. Role labels only in STUDENT files, with Kalpa's fictional
people (Meera, Anand, Kavya, Rohan) the one exception. Rs, never the rupee glyph. No em-dashes or
en-dashes anywhere, including code comments and HTML. None of these words: Additionally, Moreover,
However, Hence, Thus, Nonetheless, Furthermore, Accordingly, Indeed, Dynamic, comprehensive,
robust, holistic, seamless, leverage as a verb; no "not X, but Y" construction (a quoted dataset
document that contains such a word is quoted in a TRAINER file or paraphrased in a STUDENT file).
Every URL you print was fetched today and carries its date. Every real-company fact comes from a
source in `W05_cases.md` or one you fetch and date; anything unverified says "not verified". A
STUDENT file mentions the IITGN faculty block only with the word tentative beside it. Nothing the
room is meant to find in class is named in a STUDENT file used before that step. MCQ keys are
never the longest option and spread across the letters; every distractor is a misconception a
learner actually holds. No logo, no institutional branding. Images are our own renders or openly
licensed with attribution in the sources file.

## Finish

`python3 scripts/verify.py content/W05/D4` passes, with its last lines in your report. Push the
branch. Report in under 400 words: the files shipped, each chapter's title with its row subtopic,
the datasets and the headline numbers, the decisions you took, what you would cut if the trainer
runs late, and anything you could not do.

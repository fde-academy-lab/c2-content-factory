# W05 Wednesday (D3): Feature engineering and leakage, in the Week 5 artifact set

Your day: Wednesday 4 November 2026, "Feature engineering and leakage: what the model is allowed
to know". Folder `content/W05/D3/`, file stem `C2_W05_D03_`.

## Your day's spine (from the approved plan)

| # | Row subtopic, verbatim (the chapter's italic line) | Relatable title (the pill) | Also searched as |
|---|---|---|---|
| 1 | Feature engineering from the customer table: ratios, recency, counts, cohort age, basket signals | Turning raw columns into signals | feature engineering for machine learning |
| 2 | Encoding categoricals; scaling numerics; which models care | Teaching a model to read categories | one-hot encoding, standard scaling |
| 3 | Leakage and the prediction-time question | Answers from the future | data leakage in machine learning |
| 4 | The column audit | Interrogating every column | feature audit, leakage checklist |
| 5 | Feature importance and its limits | What the importance chart can't tell you | feature importance, permutation importance |

- Chapter 1 teaches on a tiny Kalpa customer table typed in a cell and labelled invented (ratios,
  recency, counts, cohort age, basket signals, each with its business reason), then applies the
  same thinking to the bank's columns.
- Case chapters on the week's pipeline: (1) a junior joins two feeds to the customer table, the
  economy columns and the call log; the score jumps (customer table 0.761, with economy 0.795, with
  `duration` 0.932, measure yours); the room predicts before it is shown; (2) the prediction-time
  question on every column: `duration` fails it (paraphrase the dataset's own note in STUDENT files;
  quote it verbatim only in a TRAINER file, because it contains two of the banned words), the
  calendar columns are a second, legal-looking leak (correction 1), `poutcome = success` passes and
  stays (correction 5), `pdays` 999 becomes a never-contacted flag plus days (correction 6); teach
  the leak through recall and the rupee bill, since accuracy barely moves; (3) euribor3m's sign flips
  when its collinear partners join, and permutation importance ranks without proving cause.
  Kalpa's settlement_status story from the row is told as the same leak in Kalpa's payments feed.
- STOP BEFORE: automated selection, target encoding, embeddings (the faculty block W5-3, tentative).
- Spotlight seats: the solution architect (is it there at prediction time?) with the implementation
  engineer (encoders and scalers fitted inside the pipeline, on training rows only).
- The explorable: the leakage timeline, per `W05_explorables.md` Wednesday.
- The week's timeline picture in its Wednesday state: `duration` to the right of the prediction
  moment, in red. Nothing the room finds today is named in a STUDENT file used before it.

## How this build runs

You are building one teaching day of Week 5 (the machine learning core) of the IITGN Cohort 2 PG
Diploma in AI-ML and Agentic AI Engineering, in /home/user/c2-content-factory. Work in one long
turn: nobody will answer questions, so decide within the rules below and record each decision in
the day's sources file. Branch `w05-d3`, cut from `origin/main`
(`git fetch origin main && git checkout -B w05-d3 origin/main`), pushed with
`git push -u origin w05-d3`. Commit as you go, in small commits whose messages say what changed.
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
content/W05/D3/
  README.md                          the run table first; every file in the order it is used
  1_in_class_training_content/
    slides/C2_W05_D03_slides_STUDENT.md and .pptx, slides/img/ for our own PNGs
    notebooks/C2_W05_D03_ch0N_<slug>_STUDENT.ipynb   one per concept chapter, 8 to 15 cells
    notebooks/C2_W05_D03_case0N_<slug>_STUDENT.ipynb one per case chapter, each building on the last
    notebooks/C2_W05_D03_guided_<slug>_STUDENT.ipynb the row's GUIDED exercise, TODOs, answer last
    demos/C2_W05_D03_<slug>_explorer_STUDENT.html     the day's explorable
  2_take_home_mandatory/
    C2_W05_D03_practice_set_STUDENT.md and .pdf       two to three hours, key and solutions inside
    C2_W05_D03_practice_lab_STUDENT.ipynb             the TA-led lab, extra practice
  3_study_material_for_students/
    C2_W05_D03_study_notes_STUDENT.md and .pdf
    C2_W05_D03_cheat_sheet_STUDENT.md and .pdf
    C2_W05_D03_interview_bank_STUDENT.md and .pdf
  4_trainer_only/
    C2_W05_D03_trainer_guide_TRAINER.md
    C2_W05_D03_practice_lab_solutions_TRAINER.ipynb
    C2_W05_D03_sources_INTERNAL.md
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
`slides/img/` by a helper script in `4_trainer_only/` named `C2_W05_D03_make_figures_INTERNAL.py`.
Install what you need with pip (scikit-learn, pandas, matplotlib, nbconvert, ipykernel).

**Printing**: `python3 scripts/build_doc.py content/W05/D3` prints the STUDENT markdown in
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

`python3 scripts/verify.py content/W05/D3` passes, with its last lines in your report. Push the
branch. Report in under 400 words: the files shipped, each chapter's title with its row subtopic,
the datasets and the headline numbers, the decisions you took, what you would cut if the trainer
runs late, and anything you could not do.

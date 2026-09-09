# DAY PACK SPECIFICATION
## What ships for one teaching day

A day is not delivered until every artifact below exists. A trainer who has these files needs 90 minutes of preparation and no other input.

---

## CONFIG

```
COHORT        = C2
WEEK          = {1-20}
DAY           = {1-6}
MODULE        = {module name}
WEEK_TYPE     = {Teaching | Build}
CLIENT_ZERO   = {locked scenario name}
ENV           = VS Code + GitHub Codespaces
```

---

## THE MANIFEST

| # | Artifact | Audience | Format | Notes |
|---|---|---|---|---|
| 1 | Day sheet | TRAINER | md or xlsx | Timings, concept sequence, prerequisites, checkpoints, must-cover against may-skip |
| 2 | Deck | STUDENT visible during session | pptx | Slide sequence per doctrine section 7. Thin, visual. |
| 3 | Trainer notes | TRAINER | md | Per slide: what to say, which example, what to show, likely questions, what to do if the room is behind. Never given to students. |
| 4 | Demo code | STUDENT | ipynb or sql | Progressively built, mirrors the deck order, setup steps first, runs cold |
| 5 | Starter quiz | STUDENT | Kahoot export | 5 to 8 questions, traps included, scored on correctness and speed |
| 6 | Mid-session exercises | STUDENT | md + starter file | One per 45 minutes. 15 minutes each. Types from doctrine section 8. Posted to GitHub Discussions. |
| 7 | Guided exercise | STUDENT | md + starter file | Trainer solves step by step, students mirror |
| 8 | Unguided exercise | STUDENT | md | No hints, attempted in session. The solution is released at close and the exercise continues as the assignment. |
| 9 | Take-home assignment | STUDENT | md | One or more. Submission via GitHub Discussions thread. |
| 10 | Interactive artifact | STUDENT | html or xlsx | Only when the topic has a decision, a comparison, or a hidden intermediate state |
| 11 | Post-session study notes | STUDENT | md or pdf | Written after the session shape is fixed. What was covered, worked examples, the failure and its fix. |
| 12 | Pre-read | STUDENT | md | For the next session. Short. Includes any setup the learner must do tonight. |
| 13 | Tiered extras | STUDENT | md | One stretch task, one prerequisite recovery task |
| 14 | Neo MCQ pool | INTERNAL | csv | Tagged to the day's concepts, feeds the 10-minute platform check |

Module close adds one artifact: a cheat sheet covering the module, one page, no prose.

---

## THE DAY SHEET

The trainer's control document. Columns:

| Field | Content |
|---|---|
| Concepts introduced | One line per atomic concept, in teaching order |
| Prerequisites | Concept references from earlier days, plus any tool used for the first time |
| Client-zero artifact in play | Which table, dataset, or entity today's examples run on |
| Deliberate failure | What breaks, the exact error, the fix |
| Must cover | Cut last |
| May skip | Cut first |
| Checkpoints | Every 30 minutes, what the trainer verifies before moving on |
| Timings | Durations, never clock times tied to a named person |
| Exercise map | Which exercise sits after which concept |

---

## THE FOUR-PROMPT PIPELINE

One day of content is generated in four passes, each anchored to the locked reference and the day sheet.

**Pass 1: Deck.** Input the day sheet, the locked written reference, the client-zero definition. Output the slide sequence with speaker-visible content only.

**Pass 2: Code.** Demo notebook or SQL file, guided exercise starter, unguided exercise, take-home. All built on the same client-zero data, progressively, matching the deck's decomposition order.

**Pass 3: Activities.** Mid-session exercises, Kahoot questions, the interactive artifact if the topic warrants one, tiered extras.

**Pass 4: Markdown.** Trainer notes, pre-read, post-session study notes, Neo MCQ pool.

Each pass is a separate generation because mixing them produces shallower output on all four.

---

## FILE NAMING

```
content/W{ww}/D{d}/{folder}/C2_W{ww}_D{dd}_{topic}_{AUDIENCE}.{ext}
content/W{ww}/SAT/{folder}/C2_W{ww}_SAT_{topic}_{AUDIENCE}.{ext}
```

Examples:

```
content/W02/D3/slides/C2_W02_D03_deck_STUDENT.pptx
content/W02/D3/trainer/C2_W02_D03_day_sheet_TRAINER.md
content/W02/D3/notebooks/C2_W02_D03_01_joins_STUDENT.ipynb
content/W02/D3/exercises/unguided/C2_W02_D03_row_counts_STUDENT.md
content/W02/SAT/paper/C2_W02_SAT_paper_STUDENT.md
```

The folder set per day is in `content/README.md`, and `scripts/verify.py` fails a file that sits
outside it. The topic half of the name carries only what the folder and the extension do not
already say.

The audience tag is not optional. It is the mechanism that stops a trainer notes file reaching students.

---

## BUILD WEEK PACK

Build weeks replace the teaching pack with a smaller set.

| # | Artifact | Audience |
|---|---|---|
| 1 | Mini project brief | STUDENT |
| 2 | Assessor brief and rubric | INTERNAL |
| 3 | Business use case discussion prompt and facilitation notes | TRAINER |
| 4 | Trainer's parallel build (the smaller version the trainer solves in front of the cohort) | TRAINER |
| 5 | Daily checkpoint questions for Monday to Wednesday | TRAINER |
| 6 | Presentation format and scoring sheet | INTERNAL |
| 7 | Catch-up teaching plan for the backlog day | TRAINER |

Build weeks exist partly to absorb teaching backlog. Reserve one of the five days for catch-up and plan the project around four.

---

## DEFINITION OF DONE

A day pack is done when all of these are true:

1. Every artifact in the manifest exists, with the correct audience tag
2. Demo code runs cold in a fresh Codespace
3. The deliberate failure produces the exact error text written in the day sheet
4. Every example uses the client-zero world, or the exception is stated in the day sheet
5. Prerequisites are listed and every one of them was taught on an earlier, named day
6. The unguided exercise has a released solution and a take-home continuation
7. No trainer name appears in any STUDENT artifact
8. Setup instructions for the next session are in the pre-read

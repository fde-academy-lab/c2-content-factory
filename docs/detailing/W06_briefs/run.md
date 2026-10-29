# Build 2, run session: the week's README, the presentation template, the run sheets and the rubrics

INTERNAL. Read `common.md` first. Branch `w06-run`. Skills: `training-deck-builder` and `pptx` (the
template), `academic-pptx` (assertion headlines, one exhibit per slide), `exercise-builder` (the
written sheet), `xlsx` (the scoring workbook), `humanizer`. Look at Build 1's equivalents first:
`content/W03/SAT/` and `content/W03/D4/mocks/`.

## 1. The pack README (`content/W06/D2/README.md`) and the week index (`content/W06/README.md`)

The pack README opens on the week's run table (Tuesday to Saturday, minutes, who acts, which file),
then the four things a learner opens, then every file in the order it is used, with the trainer
files last. Use the file names in `common.md` exactly; the other sessions build them in parallel.
The week index is short: the week on one screen and a link to the pack.

## 2. The presentation template (`content/W06/D2/2_starter_repo/presentation/`)

The seven slides of the run sheet as a deck the group edits: each headline an empty sentence frame
(for example "At a list of __ calls, Kalpa avoids __ cost units of missed defaults, __ less than
calling nobody"), one exhibit box per slide, the speaker and the minutes on each slide's notes, and
a backup slide for the passports. Author it as markdown named `C2_W06_D02_presentation_template_STUDENT.md`
and build it with `python3 scripts/build_deck.py`; the name matters, because the builder drops the
logo only for a deck whose name starts `C2_W05_` or later.

## 3. The run sheets (`4_trainer_only/C2_W06_D02_run_sheets_TRAINER.md`)

One section per day, Tuesday to Saturday, as tables and bullets: minute by minute what the Programme
Head, each TA and the role-players do; the three rooms for Tuesday's discovery calls; the daily
checkpoint's three questions; Wednesday's "I do" walk on Week 5's bank model; the opener ritual;
Thursday's gate roster (13 groups at 15 minutes across three staff); the red-team pairs; the dry
runs; Friday's GD roster and the expert's showcase; Saturday's two rooms by card and grade closure;
what to cut first when the day runs late. Durations only.

## 4. The rubrics, marked proposed (`4_trainer_only/C2_W06_D02_rubrics_proposed_TRAINER.md`)

Build 2's rubrics are open in `data/programme/facts.yaml` (`rubrics-and-calendar`), so every line
says proposed. Mini project 40: frame and requirements 8, data audited 6, honest POC and error bill
10, the card's decision and the MVP plan 8, all for the group; passport and defence 8 per learner.
Mock R2 30: the viva inside the gate 15 (the R1 viva's three criteria), the written technical sheet
15. GD 30: Build 1's rubric. Build the scoring workbook as Build 1 did, with its recalc manifest, so
`scripts/xlsx_recalc.py` passes.

## 5. The Mock R2 written sheet, GD prompts and the expert's brief

- The written technical sheet: 30 minutes, ML fundamentals from Weeks 4 and 5 applied to a card book,
  with its key; it passes `scripts/distractor_audit.py` if it has options. Keep it in `4_trainer_only/`
  so learners first see it on Thursday.
- GD prompts: four or five, on risk and lending, each with an exhibit and a number to argue from,
  progressive in difficulty, and the facilitator's notes.
- The expert's showcase brief: what the industry expert is asked to show in 60 minutes on Friday
  (a real model's path from POC to production, what broke, what governance asked for), with the
  questions the room will ask.

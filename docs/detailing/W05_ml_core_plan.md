# Week 5 plan: the machine learning core, built in the Week 5 artifact set

INTERNAL. The week's approved spine once the requester says yes. The curriculum rows in
`docs/curriculum/W5_ML_core_ME1.md` stay the contract; `docs/11_Artifact_Set_W05.md` sets the
artifact set. Planned on 28 October 2026 in BMAD order (brief, outcomes, architecture, day
stories, quality gates) and critiqued by a four-seat council (hiring manager, learning designer,
trainer operations, senior ML engineer), whose changes are folded in below.

## 0. The week on one screen

| Day | Row focus | Real case, real data | Kalpa decision | Spotlight seat | Explorable |
|---|---|---|---|---|---|
| Mon 2 Nov | Regression and classification | A Portuguese bank's phone campaign (UCI Bank Marketing, 41,188 calls): whom to call. Car mileage against horsepower (UCI Auto MPG) for the residual chapter | Frame Marketing's nudge: target, prediction time, the split, the baseline to beat | Senior ML engineer | Drag the line: residuals and the baseline redraw |
| Tue 3 Nov | The metric trap | The same campaign: doing nothing scores 88.7 percent; at 0.5 the model finds 22 percent of buyers. German Credit's documented 5:1 cost matrix in the take-home | The nudge threshold from Rs 40 against Rs 1,200; the budget of 5,000 nudges (precision at k); Rohan's loan threshold by hand. Financial services enters | Business owner | Threshold slider: matrix, precision, recall and the rupee bill, nudge against loan |
| Wed 4 Nov | Feature engineering and leakage | `duration`, which the dataset's authors say must be dropped (AUC 0.80 becomes 0.94 with it); three economic columns that flip a coefficient's sign together | Audit every column with the prediction-time question; ship the honest score | Solution architect, with the implementation engineer | Timeline: slide the prediction moment, columns turn red, the score falls |
| Thu 5 Nov | Overfitting and regularisation | The unlimited tree: 99.5 percent on training, 84.2 on validation, below doing nothing. Forest, boosting and logistic within 0.03 AUC. Netflix not shipping the full Prize ensemble | Choose the model, and state the gap at which the complex one would ship | QA and tester | Depth and penalty sliders: training against validation, live |
| Fri 6 Nov | Model justification | The campaign across 2008 to 2010: train early, score late, watch it sag. Zillow Offers as the bill for a stale model | The committee memo: claim, evidence, error bill, staleness rule, transfer to lending; your own 90-second model story | Product manager | Error-bill calculator with a staleness monitor |
| Sat 7 Nov | Revision, recap paper, ME1 window | The tracker's W5 paper | ME1 scope said aloud, nothing more | all six | none |

**One picture grows all week** (the learning designer's device): a timeline of past rows, the cut,
the prediction moment and the outcome window. Tuesday adds the two score humps, the threshold and the
four boxes; Wednesday drops `duration` to the right of the prediction moment in red; Thursday adds the
U of validation error against depth; Friday the score sagging across 2008 to 2010. Every deck opens
on it, the cheat sheet carries it, and the nightly self-check is to redraw it from memory.

**The sealed envelope**: on Monday the trainer seals a card marked TEST SET, DO NOT OPEN UNTIL
FRIDAY and tapes it to the wall; every request to peek is pointed at it all week; on Friday it is
opened once, the chosen model is scored once, and that number goes into the memo.

**Every teaching day ships four folders** (contract: `docs/11_Artifact_Set_W05.md`):

```
content/W05/D1/
  README.md                         the run table first, then every file in the order it is used
  1_in_class_training_content/      slides/ (one visual deck), notebooks/ (one per chapter, the
                                    case notebooks, the guided notebook), demos/ (the explorable)
  2_take_home_mandatory/            the practice set (two to three hours) and the practice lab
  3_study_material_for_students/    study notes, cheat sheet, interview question bank
  4_trainer_only/                   the trainer guide, the lab solutions, the sources
```

**Datasets, downloaded in code, never generated** (measured on 28 October 2026):
UCI Bank Marketing `bank-additional-full.csv` (CC BY 4.0, 41,188 rows, 11.27 percent yes, the
week's spine); UCI Auto MPG (Monday's residual chapter); German Credit, OpenML `credit-g` (1,000
rows, 30 percent bad, the documented 5:1 cost matrix; the lending transfer); IBM Telco churn
(26.5 percent churn, a take-home transfer). Kalpa stays the decision layer, its costs and people
from the rows.

**Dropped from Week 5 on**: the old per-artifact folders, the coverage matrix, the cold-read
agents, logos, synthetic data. **Kept**: the row as contract, concept chapters before the case,
executed notebooks, the interview angle, durations only, nothing the room must find named early.

## 1. Brief

- **Who**: 39 learners averaging 4 out of 10. They jump to a technique, hold one view at a time,
  and read problems immaturely, which is what interviews reject.
- **Envelope per day**: 240 trainer minutes in two blocks; the IITGN faculty block of 120 minutes
  (tentative); the TA-led practice lab after the second block; the take-home, two to three hours.
  The pre-work bridge course met both model families, so class time goes to framing, reading
  and judgement. The trainer guide says what fills the 120 minutes if the faculty block does not run.
- **Before**: Week 4 analyst craft. **After**: Build 2, Kalpa Financial's ML mini. ME1 runs this
  week as a continuous activity; its scope is said aloud and no day or slot is stated.

## 2. Outcomes

Each day's UNDERSTANDS, CAN DO, CAN HANDLE and CAN DEFEND come from its row unchanged. Five habits
run through every artifact, because they are what interviewers reward and this room lacks:

1. **Read before answering.** Some scenarios are under-specified on purpose; the model answer
   opens with the one clarifying question worth asking, and rubrics score it.
2. **Name the deciding seat.** Six seats (business owner, product manager, solution architect,
   senior ML engineer, implementation engineer, QA) are the checklist; a good answer names the one
   or two that decide this case and says why the others do not bind. Each day spotlights one seat.
3. **Every rule with its flip.** "Simpler wins" comes with the gap at which the complex model
   ships; "accuracy lies on imbalance" with the base rate at which it stops lying.
4. **Numbers you own.** Every claim carries a number from the learner's own run, in rupees where
   money is at stake.
5. **Answers as reasoning, not paragraphs.** Model answers are scaffolds (the 30-second version,
   the depth, the interviewer's two follow-ups), never text to memorise.

## 3. Architecture

- **Thread one, the decision**: Monday frames Kalpa's nudge, Tuesday sets its threshold and its
  budget cut, Wednesday audits its features, Thursday chooses the model, Friday writes the memo,
  Build 2 moves it to Rohan's lending book.
- **Thread two, the data**: one public file carries the case all week; each day's first case
  notebook starts from the state the day before ended in, reloaded in code.
- **Thread three, the interview**: each day ends on its anchors; the bank carries model answers
  with follow-ups; the cheat sheet accumulates everything since Week 1.
- **Chapters**: one concept chapter per row subtopic, in the row's order, its pill a relatable
  title and its subtitle the row's words plus the terms learners search; concept chapters teach
  on tiny tables typed in a cell and labelled invented; then three case chapters on the real data,
  each naming the subtopics it applies.
- **Tools**: deck markdown to `.pptx` (`scripts/build_deck.py`); executed notebooks; one offline
  explorable per day; markdown with mermaid printed to PDF (`scripts/build_doc.py`).
- **Images**: our own charts and diagrams, our own output screenshots, openly licensed images with
  attribution; nothing of unknown licence.
- **Models**: planning and critique on Fable at extra effort; each day built in its own cloud
  session on Opus at extra effort; one more session builds the financial services dossier.

## 4. Day stories

### Monday: "Should we even build a model?"
- Chapters: Is this an ML problem at all · What do we know, and when · Don't peek at the exam
  paper · Drawing the best line · From a line to a probability · What the leftovers confess.
- The line is taught on six hand-placed points, then bent into the S for the logistic model on the
  bank's data; Auto MPG appears once, for the bowed residual and its fix.
- Case: whom the bank should call; a split by time as well as a random one; the 88.7 percent
  baseline; logistic against it; the test-set peek staged and caught. The envelope goes up.
- Lab: the repeat-purchase flag written in SQL with a cutoff date, the naive version's leak named.

### Tuesday: "The 89 percent model that called nobody"
- Opens on the financial services story, placed just before the transfer chapter.
- Chapters: Four boxes that tell the truth · Of those we flagged, of those we missed · Why 89
  percent can mean zero · What each mistake costs (the 1-in-N test as coins: thirty Rs 40 nudges
  are paid for by one Rs 1,200 buyer, so act above about 1 in 31) · Where to draw the line · Same
  model, opposite threshold (a ten-minute hand count on Rohan's costs: lend only below 3,000 in
  63,000, about 5 percent default risk).
- Case: the do-nothing matrix; the model at 0.5 (precision 0.69, recall 0.22); the cost threshold;
  the budget cut, top 5,000 by score, precision at k against the 11 percent base rate. F1's
  arithmetic is cut first. German Credit's 5:1 matrix runs in the take-home and the lab.

### Wednesday: "The 0.99 that was too good to be true"
- Chapters: Turning raw columns into signals · Teaching a model to read categories · Answers from
  the future · Interrogating every column · What the importance chart can't tell you.
- Case: `duration` lifts AUC from 0.80 to 0.94 and fails the prediction-time question; its own
  documentation is read aloud; the 999 sentinel and the `unknown` labels; the economic trio that
  flips euribor3m's sign. Kalpa's settlement_status is told as the same leak in Kalpa's feed.

### Thursday: "100 on practice, 61 in the exam"
- Chapters: Memorising against learning · Putting brakes on the model · Five exams instead of
  one · Trees, forests and groups (clustering one slide) · Why the boring model often ships.
- Case: the unlimited tree drawn as one leaf per customer, then the depth curve; cross-validation
  done right (scaling inside the folds); logistic 0.80, forest 0.79, boosting 0.81; the gap sized
  in rupees, with the gap at which the complex model would ship.

### Friday: "The committee memo"
- Chapters: Selling a model to people who don't care about AUC · What will mistakes cost us · When
  the model goes stale · Moving the model to lending · Defending it in the room.
- Case: train on the early months, score the late ones; the weakest segment; the error bill under
  the threshold; the transfer paragraph; the envelope opened. Each learner rehearses a 90-second
  "walk me through a model you built" with their own numbers and one choice they made differently.
- ME1 scope said aloud.

### Saturday
- The recap paper from the tracker's W5 bank through `scripts/build_saturday_paper.py`, in its own
  session once the days are under way.

## 5. Quality gates, kept light

- The builder runs `python3 scripts/verify.py content/W05/D{d}` and fixes what fails.
- The orchestrating session reads each pack against its row once: every subtopic has a chapter and
  a notebook, MCQ keys spread and are never the longest option, nothing the room must find is
  named before it is found, every number traces to a run.

## 6. Decisions and open items

- The row's TRAINER-ONLY planted numbers (the 96 to 4 split, thresholds 0.12 and 0.85,
  settlement_status at 0.99) belonged to Kalpa v6 data that was never generated. With public data
  the room derives its numbers from the bank's file and the cost formula, and the trainer guide
  says so; Kalpa's costs and people stay as the rows give them.
- One explorable per day replaces the single explorer that grows across the week, so five parallel
  builds do not collide; the growing timeline picture keeps the week's continuity.
- The practice lab is the TA-led lab and extra practice; the two to three hours are the practice
  set alone.
- The cohort is 39 learners from 28 October 2026.

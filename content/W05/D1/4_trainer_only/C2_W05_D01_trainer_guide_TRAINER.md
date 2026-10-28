# W05 Monday trainer guide: regression and classification

Posts to <!-- sync:module:W05/D1 -->Module 2: Applied Machine Learning<!-- /sync:module:W05/D1 -->. Deck: `1_in_class_training_content/slides/C2_W05_D01_slides_STUDENT.pptx` (63 slides; S-numbers below are the deck's own).

## 1. The story in two lines

| | |
|---|---|
| The real case | A Portuguese bank phoned 41,188 clients (UCI Bank Marketing) and 1 in 9 said yes; calling nobody is right 88.74 percent of the time, and the logistic model on the client table reaches 89.71, one point above doing nothing. |
| Kalpa's decision | Marketing wants a 90-day repeat score for a Rs 40 nudge by Friday; Kavya wants the baseline first. The room frames the problem, seals the test set and refuses to ship a model that only ties the bar. |

## 2. The run table

| Block | Min | Slides | Open | What must land | Cut if late |
|---|---|---|---|---|---|
| One: opening | 8 | S1 to S6 | deck | the timeline picture on the board; the envelope sealed and taped up | S6 map to 30 seconds |
| One: ch 1 | 15 | SEC 1, S7 to S10 | ch01 | two of six need a model; the three tests | S10's Uber card (the second framing example) |
| One: ch 2 | 22 | SEC 2, S11 to S14 | ch02 | M4 bought again and still scores 0; the all-time count leaks | the ch02 timeline run (show the slide instead) |
| One: ch 3 | 20 | SEC 3, S15 to S18 | ch03 | test is spent once; the seed is the shuffle; 75 percent from nothing | the two-seed cell |
| One: ch 4 | 22 | SEC 4, S19 to S23 | ch04 | least squares beats the eye, 5,200 against 5,480; Rs 120 per visit as an association | S23 code slide |
| One: break | 10 | | | kernels shut | |
| One: ch 5 | 22 | SEC 5, S24 to S28 | ch05 | 1.28 is impossible; 0.73 means 73 of 100; exp(b) = 2.85 | the odds table's last row |
| One: ch 6 | 18 | SEC 6, S29 to S34a | ch06 | the bow (+2.7, -2.2) and its fix; the fix fails past 190 hp | S33 extrapolation (say it, skip the slide) |
| One: case 1 | 43 | SEC 7, S35 to S40 | case01, guided | 13 columns known that morning; split 24,712 / 8,238 / 8,238; guided baseline 0.8874 | S36 twin table (say it in one line) |
| Two: case 2 | 25 | SEC 8, S41 to S46 | case02 | 80 more right answers in 8,238; campaign x 0.93 per call; the calendar caveat | S44 histogram |
| Two: case 3 | 15 | SEC 9, S47 to S49 | case03 | 0.9055 peeked, 0.8971 fresh; the test is spent once | never cut |
| Two: interview, seat | 7 | S50 to S51 | deck | the [D] answer opens on a clarifying question | S51 to one sentence |
| Two: quiz, close | 13 | S52 to S53 | Kahoot | Q3 and Q4 | the return question |
| Faculty block (tentative) | 120 | | | W5-1, IITGN faculty | see section 9 if it does not run |
| TA practice lab | 85 | | case03, then the lab | section 8 | section 8's cut order |

## 3. Taught before, teach today, do not teach today

| Taught before | Teach today | Do not teach today |
|---|---|---|
| W1 Thursday: correlation against causation, the chance reference | Prediction, rule or query: when a business question is a modelling problem | any metric beyond accuracy: the confusion matrix, precision, recall, AUC (Tuesday) |
| W2: SQL CTEs and joins on the Kalpa warehouse | Input, target, prediction time; the repeat-purchase target | feature engineering: `duration`, `pdays`, the five economy columns, encoding choices (Wednesday) |
| W4 Friday: naive and seasonal-naive baselines, hold-out MAE | Train, validation, test; the seed; the baseline | regularisation, cross-validation (Thursday) |
| W4: metric design, the proxy test | Linear regression: fit, coefficients in units, residuals | trees and ensembles (Thursday) |
| Pre-work bridge course: both model families met once | Logistic regression: probability, direction, strength | the split by time and the staleness story (Friday) |
| | Where each model fails; the residual tells | ME1: say its scope aloud, no day or slot |

## 4. The interview anchors, and the minute each is asked aloud

| Tag | Question | Asked at |
|---|---|---|
| [S] | When is a business problem a machine learning problem? | block one, about minute 16 (S9) |
| [S] | Train, validation, test: what is each for, and which is spent once? | block one, minute 47 (S15); again block two, minute 38 (S49) |
| [F] | Why start with a baseline, and what does beating it prove? | block one, minute 60 (S18) |
| [F] | What does a logistic output of 0.71 mean? | block one, minute 110 (S27) |
| [D] | Marketing wants the score by Friday and your model only ties the baseline; what do you tell them? | block two, minute 42 (S50); the lab write-up rehearses it |

<div class="page-break"></div>

## 5. How to teach each chapter

```mermaid
flowchart LR
    P["Picture on<br/>the board"] --> Q["Prediction,<br/>committed"] --> M["Misconception<br/>staged"] --> N["Notebook<br/>click"] --> I["Interview<br/>line"]
```

| Chapter | Picture to draw | Prediction to ask | Misconception staged, the wrong number and its fix | Click | Interview line |
|---|---|---|---|---|---|
| 1 Is this an ML problem at all | three boxes in a row: in the data? a condition? input now, target later? | how many of six need a model | "we have data, so it is ML": most say 4 or 6; the answer is 2, and the decision makes the problem | ch01 cell 6, two PASS lines | input now, target later, decision moves |
| 2 What do we know, and when | one line at 30 June, eight dots, the 90-day band | none, one, two or four members repeat | "use the full log, it is freshest": M1 shows 2 orders all-time, one is the answer; fix: history only on the left of the line | ch02, the leaky-count cell | freeze the reference date, build both sides from it |
| 3 Don't peek at the exam paper | twenty squares, two seeds | saying no to all twenty scores what | "test is just more validation": a peeked test is a mock exam; 75 percent from nothing is the bar | ch03, the two-seed cell | each slice's job; test once; state the seed |
| 4 Drawing the best line | six dots, the mean line, residuals as squares | which line leaves the smallest squares | "join the first and last point": Rs 124 per visit, 5,480 squared; least squares Rs 120, 5,200 | ch04, hand slope and scikit-learn agree | smallest sum of squared residuals; read the slope in Rs as association |
| 5 From a line to a probability | dots at 0 and 1, a dashed line leaving the band, then the S | what the line says at 8 visits | "a line on 0s and 1s is a probability": 1.28 at 8 visits; fix: the S, 0.73 at 4 visits | ch05, model and formula agree | 0.71 means 71 in 100 similar customers |
| 6 What the leftovers confess | residuals against horsepower, five band means joined | the shape of the residuals | "close is right": the bow, +2.73 / -2.18 / +0.81; fix: hp squared, every band within 1 mpg; its own failure past 190 hp | ch06, the bow cell and the fix cell | a pattern in residuals is a shape the model missed |
| 7 Whom should the bank call | the timeline with "morning of the call" on the line | the share of yes | "a split with no seed is fine": five unseeded runs give 0.114 to 0.119 | case01, then the guided notebook | the three tests on a real ask |
| 8 Beat the dumbest model | two tall bars, then only the gap | what calling nobody scores | "89.7 percent accurate" quoted alone; fix: under one point above calling nobody, on a random split | case02, the edge and the coefficient cells | a score means nothing without its bar |
| 9 The peek | 60 dots, the top one with an arrow down | the chosen version on fresh rows | the 0.9055 status update; fresh rows give 0.8971 | case03, the scatter | a test score used to choose becomes validation |

**The device.** The sealed envelope: before slide S1, write TEST SET, DO NOT OPEN UNTIL FRIDAY on a card, seal it, tape it to the wall. Point at it at S39 and every time anyone this week asks to "just check it on test". Friday opens it once.

**The spotlight seat, the senior ML engineer.** Ask it as one question at the end of each case chapter: "which of the senior ML engineer's four questions (what is predicted, from what known when, what is the bar, which rows score it) did this chapter answer?" At S51 ask which of the day's three mistakes this seat would have caught: the all-time count, the unseeded split, the peek.

**What the data shows, and what it does not.** The row's TRAINER ONLY numbers (the 96 to 4 flag, a planted recency curve, a 96 percent classifier) belonged to Kalpa v6 data that was never generated. The room derives today's numbers from the bank's file and Auto MPG instead: the peek collapse is case 3, the bowed residuals are Auto MPG, the provisional accuracy is the bank's 0.8971. Kahoot Q4 keeps the row's invented 96 to 4 flag as a hand calculation. The validation AUC of this model is 0.761; it is Tuesday's number and is not said today.

**The one-line rule beats the model.** In the lab, "call only clients whose previous campaign succeeded" scores 0.8988 on validation, above the model's 0.8971. If a learner finds it in class, praise it and park it for the lab: it is the [D] interview question in the flesh.

<div class="page-break"></div>

## 6. The quiz, ready for Kahoot

Ungraded. 20 seconds a question, 10 for each call in Q1.

| # | Question | a | b | c | d | Key |
|---|---|---|---|---|---|---|
| R | Week 4 Friday: the vendor's curve fit the last two years perfectly. Good forecast? | Yes, a perfect fit is a perfect forecast | Yes, if R squared is above 0.9 | Unknown until it is scored on held-out months | No, curves never forecast | c |
| 1a | "How many members bought in September?" | Query | Rule | Prediction | | a |
| 1b | "Which members will buy again in 90 days?" | Query | Rule | Prediction | | c |
| 1c | "Remind every member whose cart was abandoned yesterday" | Query | Rule | Prediction | | b |
| 1d | "How much will each member spend next quarter?" | Query | Rule | Prediction | | c |
| 1e | "Average basket in Pune last quarter?" | Query | Rule | Prediction | | a |
| 2 | You tune settings on one slice and score the chosen model once on another. Which two? | train, then validation | validation, then test | test, then validation | train, then test | b |
| 3 | Validation rose after the team chose settings by their test score. What is now broken? | The training data | The random seed | The baseline's value | The test score as an estimate | d |
| 4 | Kalpa's repeat flag is 96 to 4 (invented). What does "nobody repeats" score? | 4 percent | 50 percent | 96 percent | 100 percent | c |
| 5 | Recency's coefficient is minus Rs 240 per day (invented). For Marketing: | each day since the last order causes Rs 240 less spend | each extra day goes with Rs 240 less spend, other columns held | recency explains Rs 240 of every member's spend | members at 240 days spend nothing next quarter | b |

Return question for Tuesday's opening, from the row: your model only tied the baseline; what do you tell Marketing?

## 7. The six seats, today

| Seat | Today's question | Lit? |
|---|---|---|
| Business owner | does the score change whom we call, and is it worth the build? | |
| Product manager | what does the campaign team see, and when? | |
| Solution architect | where is the target computed, and as of which date? | |
| Senior ML engineer | what is predicted, from what known when; the bar; which rows score it? | yes |
| Implementation engineer | does the same split come out on every laptop? | |
| QA and tester | what would break this number, and did we try it? | |

<div class="page-break"></div>

## 8. The practice-lab run sheet, for the TAs

Length: 85 minutes. First 10 minutes: re-run `case03` on the projector cold, top to bottom, and read the 0.9055 and 0.8971 aloud. Then 75 minutes of `2_take_home_mandatory/C2_W05_D01_practice_lab_STUDENT.ipynb`; solutions in `4_trainer_only/C2_W05_D01_practice_lab_solutions_TRAINER.ipynb`.

| TODO | Expected | Three commonest wrong answers |
|---|---|---|
| 2a split | 24,712 / 8,238 / 8,238, seed 42 | no seed (numbers differ from the room's); a single 80/20 split, so no sealed test; forgetting `stratify` |
| 2b baseline | 0.8874 | 0.1126 (the share of yes); 0.5; scored on train instead of validation |
| 2c model | 0.8971 | scored on train; all 20 columns added (it rises; Wednesday explains why, say nothing today); comparing probabilities to labels without the 0.5 cut |
| 3 rule | the solution's rule, `poutcome == "success"`: 284 calls, 0.8988 | `contact == "cellular"` calls 5,255 and scores 0.4386, read as "rules are bad"; scoring on all 41,188 rows; trying ten rules on validation and keeping the best (that is case 3's peek) |
| 4 honest SQL | 205 members with history, 110 repeat, share 0.537 | no status filter (224 members, 141 repeat); an inner join to the window, so every row is 1; `>=` on the window start, so 30 June counts twice |
| 4b baseline | majority is "buys again", 0.537 | 0.463, from habit that the majority is "no"; quoting the bank's 0.8874 |
| 5a shuffled labels | 0.8874, equal to the baseline | shuffling validation instead of train; shuffling both |
| 5b seed 7 | model 0.8977, edge 1.03 points | comparing seed-7 model to the seed-42 baseline |

- Cut order if the room is slow: 5b, then the rule line in 4b, then the chart in step 3.
- Never cut: 2b the baseline, step 4 with the leak named aloud, step 6 the write-up.
- The SQL helper runs on the Codespace's Postgres and prints "ran on Postgres"; a laptop without a server prints the SQLite line and gets identical numbers from the same warehouse file.

## 9. Fallbacks

| If | Then |
|---|---|
| downloads fail for part of the room | pair them with a neighbour; project the executed outputs, which are saved in every notebook |
| kernels hang | shut every kernel at the break; one notebook open at a time |
| the projector machine has no network | open the explorable `demos/C2_W05_D01_drag_the_line_explorer_STUDENT.html` as a local file; it needs nothing |
| the faculty block (tentative) does not run | the 120 minutes: the lab's steps 2 and 3 in class (40); the residual-plot match from the practice set, problem 6 (15); the explorable sandbox in pairs (15); interview rehearsal in pairs, the five anchors with the 30-second version and two follow-ups each (35); practice set warm-ups started (15) |

## 10. The IITGN block

<!-- sync:faculty-day:W05/D1 -->
**IITGN faculty block W5-1 (tentative), 120 minutes, after this row's applied core.** Faculty: to be confirmed by IIT Gandhinagar.

TOPIC: Where the line and the curve come from: least squares as geometry, maximum likelihood, the logistic function, and the standard error of a coefficient.
PICKS UP WHERE THE ROW STOPS: the row reads coefficients and residuals and spends its minutes on framing, so the derivation is left open.
CONNECTS TO KALPA: the coefficient the room explained to Marketing in rupees now carries its uncertainty.
BY THE END: a learner can derive the least-squares solution for one feature, say what likelihood the logistic model maximises, and read a coefficient with its standard error.
DOES NOT REPEAT: framing, the split and the baseline.
<!-- /sync:faculty-day:W05/D1 -->

Your row stops where the faculty block starts: S53's close is the last thing you run. Do not preview the block's content; when you mention it to the room, say it is tentative.

**ME1** runs this week as a continuous activity. Say its scope aloud once at S2 and nothing more; no day or slot is stated.

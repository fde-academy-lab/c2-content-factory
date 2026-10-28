# W05 Thursday: overfitting and regularisation, the trainer guide

Posts to <!-- sync:module:W05/D4 -->Module 2: Applied Machine Learning<!-- /sync:module:W05/D4 -->, on <!-- sync:day-date:W05/D4 -->Thu 05 Nov 2026<!-- /sync:day-date:W05/D4 -->.

## 1. The story in two lines

| Real case | Kalpa's decision |
|---|---|
| A Portuguese bank's 41,188 calls (UCI Bank Marketing): a tree with no depth limit scores 99.6 percent on training and 84.1 on validation, below the 88.7 of calling nobody; braked logistic, a tuned tree, a forest and boosting then sit within 0.011 AUC of each other. | Anand's budget covers one campaign of 5,000 nudges: ship the braked logistic model, and name the gap in rupees at which boosting would ship instead (its low-end gain of about Rs 51,000 against its extra cost, invented at Rs 75,000). |

## 2. The run table

Block one is 180 trainer minutes. Block two gives the trainer 60 minutes, then the IITGN faculty block of 120 minutes (tentative), then the TA-led lab.

| Block | Min | Slides | Open | What must land | Cut if late |
|---|---|---|---|---|---|
| Opening | 10 | S1 to S6 | deck | the ticket: 99.6, 84.1, 88.7 | S2 to 30 seconds |
| Ch 1 Memorising against learning | 25 | SEC 1, S7 to S12 | ch01, explorable at degree 12 | gap first = variance; both low = bias | S11 to one sentence |
| Ch 2 Putting brakes on the model | 20 | SEC 2, S13 to S17 | ch02, explorable brake slider | a brake trades teaching fit for held-out stability; small C = strong brake | S17 table |
| Ch 3 Five exams instead of one | 20 | SEC 3, S18 to S22 | ch03, explorable reshuffle | mean with spread; every learning step inside the folds | S22 to one sentence |
| Drill 1 | 15 | after S22 | the four pairs in section 5 | four diagnoses in under a minute each | to 10 minutes |
| Break | 10 | | kernels shut | | |
| Ch 4 Trees, forests and groups | 15 | SEC 4, S23 to S26 | ch04 | forest averages, booster corrects, both cost leaves to explain | S25 clustering, cut first |
| Ch 5 Why the boring model often ships | 20 | SEC 5, S27 to S31 | ch05 | two tests: real gap, worth its cost | Caruana to 2 minutes |
| Case 1 The tree that aced practice | 30 | SEC 6, S32 to S38 | case01 | below the baseline; the U; more rows did not help, the brake did | S35 leaves |
| Guided | 15 | S39 | guided notebook | A variance, B bias, C about right; one CV run | the k = 3 and 10 reruns |
| Case 2 Five exams on the bank's file | 20 | SEC 7, S40 to S45 | case02 | spread; Pipeline; the brake barely matters on 24,712 rows | S45 L1 |
| Case 3 The three-way race, with drill 2 | 25 | SEC 8, S46 to S52 | case03 | test 1 passes, test 2 fails; the provisional call | S49 table; drill 2 to two gaps |
| Close | 15 | S53 to S55 | Kahoot | the four anchors; the quiz | interview corner to two anchors |

## 3. Taught before, teach today, do not teach today

| Taught before | Teach today | Do not teach today |
|---|---|---|
| Mon: split, baseline 88.7, logistic | overfitting, bias and variance read from two curves | the bias-variance decomposition (faculty W5-4, tentative) |
| Tue: matrix, threshold 0.032, budget top k | the brake: L1, L2, C, max_depth, min_samples_leaf | why L1 lands on zero, as geometry (faculty, tentative) |
| Wed: duration out, honest feature set, Pipeline | cross-validation with the spread, fitted inside the folds | ensemble internals, boosting mathematics |
| W1 Thu: chance and spread | trees, forests, boosting, k-means used and compared | search frameworks (GridSearchCV, Optuna) |
| W2: groupby (the lab) | the two tests and the rupee break-even | the time split and the weakest segment (Friday) |

## 4. Interview anchors, asked aloud

| Anchor | Asked at |
|---|---|
| [S] Overfitting: what it is, how you detect it, how you fix it | block 1, minute 35 (end of chapter 1) |
| [S] Bias against variance in plain words | block 1, minute 35, as the follow-up |
| [F] Why cross-validation instead of one split? | block 1, minute 75 (end of chapter 3) |
| [D] Your tuned model beats a simpler one by a point and costs ten times more to explain; which ships, and how do you say it to a team that saw the 100 percent? | block 2, minute 45 (S51), and again in the close |

<div class="page-break"></div>

## 5. How to teach each chapter

| Chapter | Draw first | Ask before showing | Stage this misconception | Wrong number, shown exactly, and its fix | Click | Interview line |
|---|---|---|---|---|---|---|
| 1 | two bars per student, practice and exam | who tops the new exam? | a perfect practice score means ready | the memoriser's 100 against 61 (invented); fix: read the exam score | explorable at degree 12: training 0, validation large | overfitting is a gap you measure |
| 2 | the seven-bend curve through nine dots | will held-out error be bigger or smaller? | regularisation improves accuracy | no brake: 0.95 teaching, 5.28 held out; fix: alpha 10 gives 2.90 | brake slider at degree 12 | a brake trades a little bias for less variance |
| 3 | a 5 by 20 grid of folds | how far apart will five deals land? | one validation score is the score | deals of five shoppers from 40 to 80 percent; fix: five folds, mean with spread | reshuffle five times | one split carries its luck |
| 4 | a two-question tree | which question comes first? | a forest cannot overfit | 100 trees mean 280 leaves to read; fix: count what you must explain | none | a forest lowers variance and still must beat the simple model |
| 5 | two tests as a flow | does the higher mean ship? | the highest score ships | a real 0.008 lead worth less than its cost; fix: the low end against the cost | none | I name the gap in rupees at which I would switch |
| Case 1 | the U of validation error | the unlimited tree's two scores | 99.6 means ready | 99.6 against 84.1, below 88.7; fix: depth 3 to 6 | case01 step 5 | the training score is a memory test |
| Case 2 | five deals against five folds | what did scaling first cost? | scaling before the split always inflates a lot | 0.00003 here; fix: the habit, because target-aware steps leak more | case02 step 3 | everything that learns sits inside the folds |
| Case 3 | the paired fold lines | which model ships? | a win on every fold settles it | 0.007 AUC is real and worth Rs 51,000 at the low end; fix: test 2 | case03 step 6, change EXTRA_COST | a real lead and a worthwhile lead are two tests |

**Drill 1, four curve pairs (from today's runs; the room names each in under a minute).**

| Pair | Training | Held out | Answer |
|---|---|---|---|
| 1 | 0.3% wrong | 16.5% wrong | variance (the unlimited tree) |
| 2 | 11.3% wrong | 11.3% wrong, on the baseline line | bias (the stump) |
| 3 | 9.8% wrong | 10.1% wrong | about right (depth 6, leaf 50) |
| 4 | AUC 0.763 | AUC 0.762 | bias from too strong a brake (logistic at C = 0.0001) |

**Drill 2, simpler or complex for three gaps (invented except the first).**

| Gap | Fold record | Low-end gain against extra cost | Call |
|---|---|---|---|
| 0.007 AUC (today's boosting) | wins 5 of 5 | Rs 51,000 against Rs 75,000 | simpler |
| 0.030 AUC | wins 5 of 5 | Rs 2,00,000 against Rs 75,000 | complex |
| 0.004 AUC, a regulator must read it | wins 3 of 5 | not real | simpler |

**The three real cases, each told in under two minutes.**

| Case | Where | The line to land |
|---|---|---|
| Airbnb listing IDs (arXiv 1810.09591) | S38 | few labels per thing learned means memory; a store-ID column is Kalpa's twin |
| Google Flu Trends (Science 2014) | S43 | choosing among many candidates overfits too; select inside folds |
| Pneumonia, Caruana and others (KDD 2015) | S30 | within 0.02 AUC, the readable model shipped because it could be checked |

## 6. The spotlight seat: QA and tester

- The question to ask after every case chapter: "QA, what breaks this, on which split, for which segment?"
- Case 1: the tester asks for the validation number beside every training number.
- Case 2: the tester asks for the spread and for the Pipeline, and runs the shuffled-answer test (the lab does it on German Credit: 0.784 falls to 0.461).
- Case 3: the tester asks whether the race used the same folds, and names the two checks Friday owns: the time split and the segment table. Do not run either today.

## 7. The quiz, ready for Kahoot (ungraded)

| # | Question | A | B | C | D | Key |
|---|---|---|---|---|---|---|
| 1 | Train 99.6, validation 84.1, call nobody 88.7. Name it. | Underfitting, as validation is low | Overfitting, a wide gap | A leak, as training is too high | Imbalance, as the baseline is high | B |
| 2 | Which curve pair says high bias? | Training 0.3, held out 16.5, gap stays | Training falls, held out falls, gap closes | Training 9.8, held out 10.1, below baseline | Both near 11.3, close, on the baseline | D |
| 3 | Cross-validation averages away what? | The luck of which rows sit the exam | The bias of a model that is too simple | The leak from columns known after the outcome | The imbalance of buyers and non-buyers | A |
| 4 | The tuned tree beats logistic by 0.4 points. Recommend which? | The tree, since higher is better | The tree, once one more seed agrees | Logistic, unless the gap clears spread and cost | Neither, since a 0.4-point gap means both models overfit | C |
| 5 | Regularisation trades what for what? | Training speed for a smaller, faster model file | Nothing: it raises accuracy on every split | Lower bias on new rows for more variance | Some training fit for stability on new rows | D |
| R | Wednesday: the leak went and AUC fell from 0.93 to 0.79. Why is the model better? | It is worse; ship the 0.93 and monitor it | 0.79 is what it can score before the call | Lower AUC always means less overfitting | The economy columns now carry more of the weight | B |

Why each distractor is chosen: 1A reads a low level as bias; 1C mistakes overfitting for leakage; 2A is variance; 2C is about right; 3B and 3C name the brake's and Wednesday's jobs; 4A and 4B treat a 0.4-point win as a decision; 5B is the misconception the chapter stages; 6A keeps the leaked score.

<div class="page-break"></div>

## 8. The practice-lab run sheet (TAs)

Length: about 90 minutes. First 10 minutes: re-run case03 on the projector to its last cell, then the lab notebook in `2_take_home_mandatory/`.

| Step | Expected | The three commonest wrong answers | Cut order |
|---|---|---|---|
| 1 Baseline | 70.0% | 30% (the bad share); 0.5; the mean of y as accuracy | never cut |
| 2 Unlimited tree | training 100%, folds 67.1% | quoting only 100%; max_depth=0 (an error); scoring on X_test | never cut |
| 3 Depth curve | best near depth 5, AUC 0.709; no limit 0.618 | leaving None out; reading training AUC; picking depth 10 | 3rd |
| 4 Brake C (the assignment) | best C 0.1, AUC 0.784; C 100 gives 0.756 | reading C as strength (picks 100); training AUC as the score; one split only | never cut |
| 5 Age bands | youngest band weakest, AUC 0.717 on 110 applications with 42 bad | bins that drop ages; predictions from a model fitted on all rows; trusting a thin band | 2nd |
| 6 Shuffle test | 0.784 falls to 0.461 | shuffling X instead of y; expecting 0; panicking at 0.46 (any value near 0.5 passes) | never cut |
| 7 Cost rule | bill 429 at 0.167, 782 at 0.5 | threshold 5/6; costs swapped; counting good loans as cost | 1st |
| 8 Write-up | claim, evidence, caveat, action, flip | method tour; no numbers; no flip | never cut |

The solutions are in `C2_W05_D04_practice_lab_solutions_TRAINER.ipynb`, executed.

## 9. Fallbacks

- **Downloads or kernels fail for part of the room**: pair learners, project the executed notebooks from GitHub (every cell carries its output), and open the explorable as a local file; it needs no network.
- **The bank download is blocked**: the UCI zip is about 1 MB; one TA laptop downloads it and shares `~/.cache/c2_datasets/bank-additional-full.csv` on a pen drive.
- **The faculty block does not run** (it is tentative): fill the 120 minutes with (1) the row's unguided exercise in full, each learner re-running case03 with one column removed and noting how the race moves (40 minutes, the after-class BUILD task done in class); (2) the explorable's sandbox in pairs: find the degree and brake that minimise validation error over five reshuffles (20 minutes); (3) practice set problems 8 to 10 in groups of three, each group presenting one (40 minutes); (4) interview rehearsal on the [D] anchor in pairs, two rounds (20 minutes).

## 10. Notes the room does not see

- The row's TRAINER ONLY numbers (the tree at 100 and 61, the near-tie within a point) described Kalpa v6 data that was never generated. On the public file the unlimited tree scores 99.6 and 84.1; the braked logistic model beats the tuned tree (0.786 against 0.782 under folds) and boosting leads logistic by 0.007. Quote these.
- The week pipeline's correction 6 quoted logistic 0.803, tuned tree 0.804 and boosting 0.811; today's run on the same seed gives 0.796, 0.790 and 0.804 on validation. The direction holds; the run's numbers are the ones on the slides.
- The Netflix Prize story (Netflix not shipping the full Prize ensemble) is not verified: every source returned 403 on 28 October 2026. Do not tell it unless you have read the April 2012 Netflix tech blog post yourself. The pneumonia case (Caruana and others, KDD 2015) carries "the simpler model wins" instead.
- The rows run in time order. A five-fold split cut by row order instead of shuffled gives fold AUCs from about 0.50 to 0.74 on this file; keep that for Friday and do not show it today.
- ME1 runs this week as a continuous activity; say its scope aloud if asked and state no day or slot.

<!-- sync:faculty-day:W05/D4 -->
**IITGN faculty block W5-4 (tentative), 120 minutes, after this row's applied core.** Faculty: to be confirmed by IIT Gandhinagar.

TOPIC: The bias-variance decomposition; L2 and L1 regularisation as geometry, and why L1 sets coefficients to zero; what cross-validation estimates.
PICKS UP WHERE THE ROW STOPS: the row teaches the curves, the brake and the honest average at the depth of use.
CONNECTS TO KALPA: the tree at 100 on training and 61 on validation, and the near-tie between the regularised model and the tuned tree.
BY THE END: a learner can write the decomposition, draw the two penalty shapes and explain the sparsity of L1, and say what a cross-validated score is an estimate of.
DOES NOT REPEAT: reading learning curves.
<!-- /sync:faculty-day:W05/D4 -->

The trainer's row stops where the faculty block starts: the quiz and S55 are the last things you run. When you mention the block to the room, say it is tentative.

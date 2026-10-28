# W05 Friday trainer guide: model justification, the committee memo

## 1. The story in two lines

| Thread | The line |
|---|---|
| Real case | UCI Bank Marketing (41,188 calls, May 2008 to November 2010): three near-tie models, a bill that barely depends on the model at Rs 40 against Rs 1,200, and a model trained on the early months that keeps promising 16 in 100 while 25 buy. Zillow Offers is the bill for a stale forecast. |
| Kalpa's decision | Meera's committee on Monday: which model, its error bill, its staleness rule, and the transfer paragraph for Rohan's lending book (German Credit's documented 5 : 1, then Kalpa's 20 : 1). Each learner rehearses a 90-second "walk me through a model you built". |

## 2. The run table (240 trainer minutes, durations only)

| Block | Min | Slides | Open | What must land | Cut if late |
|---|---|---|---|---|---|
| Opening: Meera's brief, the room lists each seat's push | 12 | cover to S6 | deck | Four seats, four pushes, one memo | S3 to 1 minute |
| Ch 1 Selling a model to people who don't care about AUC | 15 | SECTION 1, S7 to S10 | ch01 | The reader hears members and rupees; four parts, each with a number | the ch01 run, show its outputs |
| Ch 2 What will mistakes cost us | 15 | SECTION 2, S11 to S14 | ch02, explorable (bill) | The bill counts two mistakes; the cut is cheap / (cheap + dear) | S13 |
| Ch 3 When the model goes stale | 15 | SECTION 3, S15 to S18 | ch03, explorable (monitor) | A rule has number, ceiling, window, owner; a segment reading needs its band | **S17's band arithmetic, first** |
| Ch 4 Moving the model to lending | 11 | SECTION 4, S19 to S22 | ch04 | Same formula, the expensive mistake on the other side; a leak is judged by time stamp | S22 to 1 minute |
| Ch 5 Defending it in the room | 10 | SECTION 5, S23 to S26 | ch05 | A number, the reason, the flip | S25 |
| Break | 10 | | | | |
| Case 1 The bill for the near-tie | 25 | SECTION 6, S27 to S31 | case01 | At 0.032 every model ties with calling everyone; under 1,000 calls they find about 4x random; boosting's 13 is inside its band | the bootstrap run (show S30) |
| Case 2 Train early, score late | 30 | SECTION 7, S32 to S39 | case02, explorable | Real 6 to 25 in 100, promise 16; the stale bill tops calling everyone; the rule fires August 2009; blue-collar is the weakest readable group | S37's arithmetic; Zillow to 1 minute |
| Case 3 Lending, and the envelope | 22 | SECTION 8, S40 to S44 | case03 | Lend above 0.83 at 5 : 1, 0.95 at 20 : 1; German Credit's duration stays; test 482 buyers, AUC 0.801 | S42 |
| Guided: claim and evidence, bill at two thresholds | 25 | S31 on screen | guided notebook | Every pair has two bills and a two-part memo with numbers | the second threshold |
| Unguided: caveat, action, staleness rule, transfer | 20 | S44 | the memo, on paper | Each memo under 300 words | the transfer to two sentences |
| Pair challenge and the 90-second rehearsal | 20 | S45, S26 | | Every learner says their 90 seconds once and answers one push | **never cut** |
| Interview corner, Kahoot, close and ME1 scope | 20 | S46 to S51 | Kahoot | ME1's scope said aloud; tonight's practice set | Kahoot to 3 questions |

## 3. Taught before, teach today, do not teach today

| Taught before | Teach today | Do not teach today |
|---|---|---|
| Week 1: the four-part note, sample size, the permutation idea | The justification at model scale | Drift detection methods (named, Weeks 14 on) |
| Mon: split, baseline 88.7 percent, the sealed envelope | The error bill at the cut and under a budget | Retraining pipelines (named, Weeks 14 on) |
| Tue: four boxes, 1-in-N, 0.032, precision at k, Rohan's 20 : 1 | Staleness: the monitoring rule and the weakest segment | Calibration methods (Platt, isotonic): the word only |
| Wed: duration and the prediction-time question | The transfer paragraph | Tree and boosting internals (faculty block W5-5, tentative) |
| Thu: three near-tie models, cross-validation, simpler wins | Reading the memo aloud under challenge | ME1's day, slot or marks |

COMES LATER: Build 2 next week is Rohan's business, with his constraint written into the brief.

## 4. The interview anchors, asked aloud

| Tag | Question | Asked aloud at minute |
|---|---|---|
| [S] | Walk me through a model you built and why you chose it. | 212, in the pair challenge |
| [F] | How would you know your model has gone stale? | 133, at S37 |
| [F] | What would change if this model moved to a lending business? | 150, at S41 |
| [D] | The committee wants the higher-scoring model and you are recommending the simpler one; make the case in ninety seconds. | 105, at S30 |

---

## How to teach each chapter

**Chapter 1, Selling a model to people who don't care about AUC** (row subtopic: The model justification: claim, evidence, caveat, action)
- Picture: the 20 dots of S8, green returners, the cut after six.
- Prediction: S7, letter cards; most pick the AUC line.
- Misconception staged: "report the higher AUC". Fix: the same 4 returners in each top 6, Rs 960 either way.
- Click: ch01 cell 4, AUC by hand: 60 of 75 pairs for A, 64 for B; the check against scikit-learn passes.
- Interview line: "I lead with the decision and its rupees, and I give the method when the reader is the ML lead."

**Chapter 2, What will mistakes cost us** (The error bill in rupees under the chosen threshold)
- Picture: the stacked bill bars of S12.
- Prediction: S11; most pick 0.5 because it calls fewer people.
- Wrong number shown exactly: Rs 1,830 at 0.5 against Rs 450 calling everyone and Rs 360 at the cheapest cut.
- Click: the explorable opens at 0.5 on the bank's validation counts. Ask for the bill before reading it (about Rs 8.6 lakh), then drag to 0.03 (about Rs 2.8 lakh).
- Interview line: "The bill counts wasted calls and missed buyers; the cut is the cheap mistake's cost over the sum, while the scores are honest probabilities."

**Chapter 3, When the model goes stale** (Staleness: the monitoring rule and the weakest segment)
- Picture: S16, promise against real with the 5-point band.
- Prediction: S15; "never" and "July" are the common wrong answers.
- Misconception: "retrain every month". Fix: a rule with number, ceiling, window and owner.
- Click: explorable monitor panel; lower the ceiling until the alarm fires, read the month aloud.
- Weakest segment: student's gap is wide on 20 calls (band 16 points); family's clears its band. The Week 1 sample-size reason.
- Interview line: "I watch the promise against reality among the people we acted on, with a ceiling sized from the sample."

**Chapter 4, Moving the model to lending** (The transfer paragraph: what changes, what stays, what would leak)
- Picture: S20, one axis, three cuts.
- Prediction: S19; b and d are the copy-the-formula slip.
- Click: ch04's column audit; every column written after the decision is flagged.
- Interview line: "Same pipeline, the other side's costs, the opposite threshold, and the column written after the decision."

**Chapter 5, Defending it in the room** (Reading the memo aloud under challenge)
- Picture: S25, the memo as seconds.
- Prediction: S23; b (explain the metric) is the polished wrong answer.
- Click: ch05's challenge table; every answer carries a number.
- Interview line: "A number in the reader's units, the reason, and what would change my mind."

**Case 1, The bill for the near-tie**
- Trap shown exactly: "boosting has the best AUC, so it saves the most". At 0.032 its bill is the largest of the three: Rs 2,83,200 against logistic's Rs 2,81,680. Calling everyone is Rs 2,92,400.
- The model earns its keep under the 1,000-call budget: 462, 469, 475 buyers against 113 at random.
- The gap: 13 buyers, worth Rs 16,120 (13 x Rs 1,240); the paired bootstrap band runs from about -1 to 28, so it is a tie. The flip: boosting ships if a fresh month's band clears zero.

**Case 2, Train early, score late**
- Run the split cell only after the S33 vote.
- Numbers: trained on 28,831 rows (May 2008 to April 2009, 5.6 percent buy), scored on 12,357 (April 2009 to November 2010, 24.6 percent); mean promise 15.9 percent; AUC 0.664 against 0.795.
- Trap: "AUC 0.66 still beats random". The stale bill at 0.032 is Rs 4,61,640 against Rs 3,72,920 for calling everyone; 231 people scored below 0.032 and 79 bought.
- The rule fires in August 2009 (July 22 points over on 22 calls, August 12.5 points over on 93 calls); the ceiling of 10 points comes from about 9 points of luck at 100 calls.
- Weakest segment, measured: entrepreneur reads 0.655 on 26 buyers (band about 0.54 to 0.81, unreadable); blue-collar 0.707 on 122 buyers is the weakest readable group; telephone 0.721 against mobile 0.779. The row's TRAINER-ONLY "Student" belonged to Kalpa v6 data that was never generated; on this file student reads 0.759 on 58 buyers, mid-table.
- Zillow: read the shareholder letter's line on forecasting "in both directions" (sources file).

**Case 3, Lending, and the envelope**
- German Credit validation (300 applicants): cost 266 at 0.5, 160 at 0.83; Rohan's 20 : 1 puts the line at 0.95.
- The name trap: German Credit's `duration` is the loan term, 4 to 72 months, known at application.
- The envelope: take the TEST SET card off the wall, run the cell once: AUC 0.801, 482 buyers in the top 1,000 (validation 462). No second run.

## The spotlight lens: the product manager

- The PM reads the memo after the meeting and runs the list every month.
- Ask it at S4 and S26: "What does the PM need from the memo that Meera does not?" Model answer: the operating point as one number (the top 1,000, score about 0.245), the monthly check and its ceiling, and who acts when it fires.
- Ask it once more in the pair challenge: one partner plays the PM and asks "what does the customer experience?"

## The quiz, ready for Kahoot (ungraded)

| Q | Question | A | B | C | D | Key |
|---|---|---|---|---|---|---|
| 1 | Which list gives the four parts of a model justification, in order? | Problem, method, result, next steps | Claim, evidence, caveat, action | Data, model, metric, deployment | Summary, AUC, risks, appendix | B |
| 2 | The error bill under the chosen threshold is computed from which two counts? | True positives and true negatives | Accuracy and AUC | Calls made and buyers found | Wasted calls and missed buyers | D |
| 3 | Which sentence is a staleness rule someone else could check? | Retrain the model on the first working day of every single month | Watch the AUC closely and retrain whenever it starts looking low | Over 10 points off the promise twice running, Kavya pauses the list | Monitor the model continuously, with dashboards and alerts on all drift | C |
| 4 | Which feature would leak in the lending version, and why? | Days past due, since it is written after approval | The loan term in months, since its column is called duration | Monthly income, since income strongly predicts repayment | The bureau score, since it comes from an outside agency | A |
| 5 | The committee wants the 0.4-point winner. Your one-line answer? | Ship it: a higher score is always the safer choice | Size the gap in buyers and rupees against its band first | Refuse: complex models cannot be explained to a committee | Average both models so that nobody on the committee loses | B |
| Return | Train 100, validation 61: name it and prescribe. | Underfitting; add more features and train longer | Data leakage; drop the column that looks too good | Overfitting; limit depth or regularise, check with CV | A lucky split; reshuffle the rows until validation rises | C |

## The practice-lab run sheet for the TAs

- The lab is sized at about 90 minutes; the core (parts 1 to 4 and the write-up) takes 60.
- First 10 minutes: rerun case03 on the projector from a clean kernel; read the envelope cell's two numbers aloud.
- Then the lab notebook `2_take_home_mandatory/C2_W05_D05_practice_lab_STUDENT.ipynb`: Rohan's memo on German Credit.

| TODO | Expected | Three commonest wrong answers | Cut order |
|---|---|---|---|
| 1 Load and the base rate | 1,000 rows, 700 good (0.70) | 0.30 (bad taken as positive); 300; reading `class` as numbers | never cut |
| 2 The lending cut at 5 : 1 | 5 / 6 = 0.833 | 0.167 (ratio on the wrong side); 0.5; 0.952 (Rohan's) | never cut |
| 3 Cost at 0.5 and at the cut, validation | 266 and 160 | counting approved goods as a cost; 5 x wrongful rejections; using the training rows | never cut |
| 4 Weakest segment by `purpose` with group sizes | the lowest-AUC purpose with 30 or more applicants, beside its count | the smallest group named weakest; accuracy instead of AUC; no count shown | cut third |
| 5 Integration: approval rate by `checking_status` in pandas | four groups with counts and rates | mean of the 0/1 column without groupby; rates over all rows; sorted by count | cut second |
| 6 QA: break it | cost at the cut under a 10:1 ratio and the threshold that moves | changing the threshold without the ratio; reporting accuracy; refitting the model | cut first |
| Write-up | five lines: claim, evidence, caveat, action, transfer | no numbers; AUC as the claim; no owner in the action | never cut |

Solutions: `4_trainer_only/C2_W05_D05_practice_lab_solutions_TRAINER.ipynb`.

## The fallbacks

- Downloads or kernels fail for part of the room: pair learners, project the executed notebooks (every one ships with its outputs), and open the explorable as a local file (it needs no network).
- UCI is down for everyone: every number in the deck is from the executed notebooks; run nothing, read the outputs.
- If the faculty block (W5-5, tentative, 120 minutes) does not run: 40 minutes of extra pair challenges with seats rotated (each learner faces three seats), 40 minutes on the practice set's problems 8 to 10 in groups, 40 minutes of the practice lab started early with the TAs.

## Module, day and faculty block (synced)

Posts to <!-- sync:module:W05/D5 -->Module 2: Applied Machine Learning<!-- /sync:module:W05/D5 -->.

<!-- sync:faculty-day:W05/D5 -->
**IITGN faculty block W5-5 (tentative), 120 minutes, after this row's applied core.** Faculty: to be confirmed by IIT Gandhinagar.

TOPIC: Trees and ensembles from the inside: impurity and the choice of a split, bagging and the random forest, boosting as stage-wise fitting.
PICKS UP WHERE THE ROW STOPS: Thursday's row uses trees and ensembles at recognition depth and stops before their internals and before boosting mathematics.
CONNECTS TO KALPA: the tuned tree in the three-way comparison behind the committee memo.
BY THE END: a learner can compute one split by hand, explain why averaging many trees lowers variance, and describe what each boosting round fits. The block closes the machine learning that ME1 draws on.
DOES NOT REPEAT: the justification memo.
<!-- /sync:faculty-day:W05/D5 -->

ME1 (statistics, data manipulation, analyst technique, ML core) runs this week as a continuous activity; state its scope aloud at the close and nothing more. Its day is not fixed (data/programme/facts.yaml, `exam_day_and_slot`, open).

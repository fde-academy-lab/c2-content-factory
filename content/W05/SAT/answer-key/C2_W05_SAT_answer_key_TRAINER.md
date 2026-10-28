# Week 5 recap paper: key

TRAINER. Rendered from the tracker's item bank and the week's source file by `scripts/build_saturday_paper.py`. Change an item in the tracker, an option in `data/programme/paper_edits.yaml` or anything in `content/W05/SAT/internal/C2_W05_SAT_paper_source_INTERNAL.yaml`, and rebuild; never edit this file by hand. A stem, a situation or an option can be reworded in `data/programme/paper_edits.yaml`.

Saturday 7 November 2026. A 60-minute paper holding 26 items at 59 minutes by the blueprint's pace: 4 easy, 9 medium and 13 hard. 21 of them are new and not yet in the tracker.

## Marking

1. Papers are swapped, so nobody checks their own.
2. The Academic TA reads the key out part by part, and the marker writes a tick or a cross beside each item.
3. An item is right when its answer matches the key: every correct letter and no other on a more-than-one item, the letter on a word-bank or match item, the number on an applied maths item (the working belongs to the discussion), and the whole sequence on an ordering item. The programme has set no partial-credit rule, so this key uses none.
4. The marker writes each part's ticks beside its rating on the answer sheet, and their total as Items right, out of 26, then hands the paper back.
5. The TA collects the papers and tallies the misses by tag, using the table below; that tally is Monday's remediation read. It is never a ranking and never read out by name.
6. The TA enters every paper in `C2_W05_SAT_item_analysis_TRAINER.xlsx` beside this key, by seat and never by name: 1 for a tick, 0 for a cross and a blank for an item left empty. The workbook orders the discussion from the most-missed item, flags any item to check, and gives each tag's rate for the room and for each seat.

## The blueprint

| Part | What it shows | Items | Minutes | Easy | Medium | Hard |
|---|---|---|---|---|---|---|
| 1. Should the bank build a model, and what must it beat? | whether you can frame a prediction problem, split the rows honestly and read what a model's score says | Q1 to Q5 (5) | 10.5 | 1 | 3 | 1 |
| 2. Which number tells the truth, and where does the line go? | whether you can read a confusion matrix, price each error and set the line the business can afford | Q6 to Q11 (6) | 15.5 | 1 | 1 | 4 |
| 3. What was the model allowed to know? | whether you can test each column against the moment of prediction and say what a coefficient does and does not prove | Q12 to Q16 (5) | 11 | 1 | 1 | 3 |
| 4. Is the model learning, or memorising? | whether you can read training against validation, choose complexity by cross-validation and say when the simpler model ships | Q17 to Q22 (6) | 12 | 1 | 2 | 3 |
| 5. Would the committee sign, and what moves to lending? | whether you can say what a memo must prove, how a model is caught going stale and why the same model draws an opposite line in lending | Q23 to Q26 (4) | 10 | 0 | 2 | 2 |
| Total | | 26 | 59 | 4 | 9 | 13 |

## What guessing alone would score

A learner who guessed every item blind would average 5.0 of 26, since a written answer cannot be guessed from a list, and fewer than one guesser in twenty would reach 9. A score of 8 or below is therefore within reach of guessing alone, and the tally reads such a paper as a conversation to have on Monday, never as a result.

## Reading the items after marking

The workbook flags an item to check when fewer than one learner in five got it right, or when the bottom third of the room got it right more often than the top third. Both are this programme's own working rule for a room of 39. A flagged item is discussed as usual; the TA also sends it, with the room's rate, to the tracker's owner, because the fault may sit in the item rather than in the learners.

## The key

| Q | Key | Type | Part | Level | Tag | Roles | Day | Min | Source | Interview anchor |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | b | One correct option | 1 | Medium | [S] | DS, FDE | Mon | 2.5 | new | Train, validation, test: which is spent once? |
| 2 | c | True or false | 1 | Hard | [D] | DS | Mon | 2.5 | new | Train, validation, test: how should the rows be split for the question being asked? |
| 3 | d | One correct option | 1 | Medium | [F] | DS, BA | Mon | 2 | new | What does a logistic output of 0.71 mean? |
| 4 | a, d | More than one correct | 1 | Medium | [S] | DS, BA | Mon | 2.5 | new | When is a business problem a machine learning problem? |
| 5 | c (test) | Fill in the blank | 1 | Easy | [S] | DS | Mon | 1 | bank 1 | Train, validation, test: what is each for, and which is spent once? |
| 6 | d | True or false | 2 | Hard | [F] | DS, BA | Tue | 2.5 | new | Accuracy is 96 percent on a 96 to 4 split; good model? |
| 7 | Precision 174 / 268 = 0.65; recall 174 / 928 = 0.19; F1 = 2 x 174 / (2 x 174 + 94 + 754) = 348 / 1,196 = 0.29. | Applied maths | 2 | Hard | [S] | DS | Tue | 4 | new | Precision, recall and F1 from a confusion matrix. |
| 8 | Call when p x 1,200 > (1 - p) x 40, so p > 40 / 1,240 = 1 / 31, about 0.032; the line moves down from 0.5 and recall leads. | Applied maths | 2 | Medium | [S] | DS, FDE | Tue | 3 | new | How do you set a threshold when the two errors cost differently? |
| 9 | b | One correct option | 2 | Hard | [S] | DS, FDE, BA | Tue | 2.5 | new | How do you set a threshold when the two errors cost differently? |
| 10 | c | One correct option | 2 | Hard | [D] | DS, FDE, BA | Tue | 2.5 | new | The cost rule says call nearly everyone, and the budget says 1,000 calls: which wins, and what do you report? |
| 11 | b (negatives) | Fill in the blank | 2 | Easy | [S] | DS | Tue | 1 | bank 2 | Precision, recall and F1 from a confusion matrix. |
| 12 | c | One correct option | 3 | Hard | [S] | DS, FDE | Wed | 2.5 | new | What is data leakage, and how do you catch it before it ships? |
| 13 | b, c, d | More than one correct | 3 | Hard | [S] | DS, FDE | Wed | 2.5 | new | What is data leakage, and how do you catch it before it ships? |
| 14 | a | True or false | 3 | Medium | [F] | DS, BA | Wed | 2.5 | new | What does a feature importance chart prove, and what does it not? |
| 15 | d | One correct option | 3 | Hard | [F] | DS | Wed | 2.5 | new | What does a feature importance chart prove, and what does it not? |
| 16 | c (leakage) | Fill in the blank | 3 | Easy | [S] | DS, FDE | Wed | 1 | bank 3 | What is data leakage, and how do you catch it before it ships? |
| 17 | a | One correct option | 4 | Hard | [S] | DS | Thu | 2.5 | new | Overfitting: what it is, how you detect it, how you fix it. |
| 18 | a, b, d | More than one correct | 4 | Medium | [F] | DS | Thu | 2.5 | new | Overfitting: what it is, how you detect it, how you fix it. |
| 19 | b | One correct option | 4 | Hard | [F] | DS | Thu | 2.5 | new | Why cross-validation instead of one split? |
| 20 | c | True or false | 4 | Hard | [D] | DS, FDE | Thu | 2.5 | new | Your tuned model beats a simpler one by a hair: which ships, and why? |
| 21 | a (overfitting) | Fill in the blank | 4 | Easy | [S] | DS | Thu | 1 | bank 4 | Overfitting: what it is, how you detect it, how you fix it. |
| 22 | d (split) | Fill in the blank | 4 | Medium | [F] | DS | Thu | 1 | bank 5 | Why cross-validation instead of one split? |
| 23 | a | One correct option | 5 | Hard | [F] | DS, FDE | Fri | 2.5 | new | How would you know your model has gone stale? |
| 24 | b, c | More than one correct | 5 | Medium | [D] | DS, FDE, BA | Fri | 2.5 | new | Your tuned model beats a simpler one by a point and costs ten times more to explain; which ships? |
| 25 | a | One correct option | 5 | Medium | [D] | DS, FDE, BA | Fri | 2.5 | new | Your tuned model beats a simpler one by a hair: which ships, and why? |
| 26 | d | One correct option | 5 | Hard | [D] | DS, FDE, BA | Fri | 2.5 | new | The same model in retail and lending: why are the thresholds opposite? |

## Why each answer holds

### Q1, key b

**Why it holds.** The test slice is honest only while nothing about the model was chosen by looking at it. Moving the threshold until the test score improves makes the test a second validation slice, so the reported number now carries the analyst's selection and flatters the model. The committee is told the test was spent, and the honest check is one score on calls the model has not touched, such as the next month's. Monday sealed the slice in the envelope; Friday opened it once.

- (a) Fitting the weights is one way to use the rows; choosing a threshold on them is another, and either one spends the slice.
- (c) A threshold set on training rows sits on rows the model has memorised, so validation is the place to set it, and the test score is still spent.
- (d) 8,238 clients is plenty for one honest score, and pooling the spent slice with validation hides the peek inside a bigger number.

**In the interview.** The test is spent the moment it changes a decision, so I tell the committee it was spent and get one clean score on data nobody has looked at.

### Q2, key c

**Why it holds.** The ask is about a campaign that has not happened yet, so the honest test trains on the earlier calls and scores the later ones. A random split puts calls from the same months in training and validation, and the month and the economic indicators mark the period, so the model partly learns when a call happened. On the week's run the yes rate moved from 5.6 to 24.6 percent across the file, and Friday's split by date cut the AUC from 0.795 to 0.657. Monday raised the split by time; Friday ran it.

- (a) Stratifying keeps the yes share equal, and it says nothing about mixing months, which is what lets the random split flatter the model.
- (b) The month and the five economic indicators each mark the period a call was made in, so the model reads time without a date column.
- (d) Validation holds 928 yes rows under the random split; the problem is which months they come from, never how many there are.

**In the interview.** I split the way the model will be used: train on the past, score on the later period, and expect that score to be lower than the random split's.

### Q3, key d

**Why it holds.** A logistic model outputs an estimated probability for one client, so 0.71 says that clients with this profile say yes about 71 times in 100, as long as the scores are calibrated against what actually happens. The threshold that turns it into a call is a business choice made afterwards: at Kalpa's costs it sits near 0.03, far below 0.5. Monday bent the line into the S on the bank's data.

- (a) 0.5 is a default, not part of the score; the threshold is set from the costs, and 0.71 is a chance, never a verdict.
- (b) Accuracy across many clients is a property of the model on a slice, while 0.71 belongs to one client.
- (c) 0.71 is a probability, not a ratio against the average; against a base rate of 11 percent it is about six times the average chance.

**In the interview.** 0.71 is an estimated chance for this one client, trustworthy only if calibrated, and the decision to call comes from the threshold, which the costs set.

### Q4, key a, d

**Why it holds.** A prediction problem asks about an outcome that has not happened yet, from what is known now, and has past examples to learn from. Ranking next month's clients and scoring a client never called before both ask about a future yes. Counting 2009's yes answers and listing past successes are queries on rows that already exist. Monday's first chapter sorted Kalpa's asks into prediction, rule and query.

- (b) Every 2009 answer is already in the file, so a count answers it and no model is needed.
- (c) poutcome already records each past result, so a filter lists them; nothing is predicted.

**In the interview.** If the answer is already in a table, it is a query; if it is about a future outcome I have past examples of, it is a model.

### Q5, key c (test)

**Why it holds.** The test slice is scored once, at the end, so its number is an honest estimate of how the chosen model does on clients it never influenced. Training fits the model and validation chooses among models and thresholds, so both are read many times. The week sealed the test slice on Monday in an envelope on the wall and opened it once on Friday.

**In the interview.** Training fits, validation chooses, and the test is spent once, at the end; once I peek and change anything, it is validation.

### Q6, key d

**Why it holds.** On an outcome where 89 clients in 100 say no, saying no to everyone scores 0.887, so a point of accuracy above it says almost nothing about the campaign. The model at 0.5 calls 268 people and finds 174 of the 928 buyers, a recall of 0.19, and leaves 754 buyers uncalled. Beating the majority baseline is the floor, and the case for shipping is made on recall, precision and the bill. Tuesday's case opened on this matrix: the 89 percent model that called nobody.

- (a) Beating the baseline is necessary, and on accuracy it is nearly free here, since the baseline itself is 0.887.
- (b) The count is right, 94 plus 754 against 928, but it weighs a wasted call and a missed buyer the same, while one costs Rs 40 and the other Rs 1,200.
- (c) Validation is where models and thresholds are compared, so 0.897 is a fair validation number; the trouble is what accuracy measures, not where it was read.

**In the interview.** On a lopsided outcome I quote the base rate first, then recall and precision, and accuracy last if at all.

### Q7, key Precision 174 / 268 = 0.65; recall 174 / 928 = 0.19; F1 = 2 x 174 / (2 x 174 + 94 + 754) = 348 / 1,196 = 0.29.

**Why it holds.** Precision divides the caught buyers by everyone called, 174 over 174 plus 94, 0.649. Recall divides them by every buyer, 174 over 174 plus 754, 0.1875. F1 is the harmonic mean, 2PR over P plus R, which on counts is 2TP over 2TP plus FP plus FN: 348 over 1,196, 0.291. The harmonic mean sits near the smaller of the two, which is why a low recall drags F1 down. Tuesday's deck taught precision and recall on this matrix and named F1 last.

**In the interview.** Precision is of those I called, recall is of those out there, and F1 is their harmonic mean, 2TP over 2TP plus FP plus FN.

### Q8, key Call when p x 1,200 > (1 - p) x 40, so p > 40 / 1,240 = 1 / 31, about 0.032; the line moves down from 0.5 and recall leads.

**Why it holds.** Call when the expected loss of not calling, p times Rs 1,200, is above the expected loss of calling, (1 minus p) times Rs 40. That gives p above 40 over 1,240, 1 in 31, about 0.032. In plain words, one caught buyer pays for 30 wasted calls, so a call is worth it above about a 1-in-31 chance. The line moves far below 0.5, so recall leads, because a miss costs thirty times a wasted call. The rule assumes calibrated scores. Tuesday's chapter on what each mistake costs taught the 1-in-N test as coins.

**In the interview.** The line sits at the cost of a false alarm over the sum of both costs, so when a miss costs thirty times a false alarm I act on about a 1-in-31 chance.

### Q9, key b

**Why it holds.** The bill adds each wasted call at Rs 40 and each missed buyer at Rs 1,200. At 0.5 that is 94 times 40 plus 754 times 1,200, Rs 3,760 plus Rs 904,800, Rs 908,560. At 0.10 it is 2,138 times 40 plus 312 times 1,200, Rs 85,520 plus Rs 374,400, Rs 459,920. Lowering the line wastes 2,044 more calls and catches 442 more buyers, and the bill falls by Rs 448,640. Tuesday's slider drew this bill against the threshold.

- (a) This swaps the two prices, charging Rs 1,200 for each wasted call and Rs 40 for each miss.
- (c) This counts only the wasted calls and forgets the missed buyers, the larger cost by far.
- (d) This counts only the missed buyers and forgets the 94 and 2,138 wasted calls.

**In the interview.** I price both boxes of errors at each threshold and add them, because the threshold that looks wasteful on calls can be the cheaper one once misses are priced.

### Q10, key c

**Why it holds.** When the budget binds before the cost line does, the ranking carries the decision: call the 1,000 highest scores. On validation they hold 404 buyers, a precision at 1,000 of 0.404, against the base rate of 0.113, about 3.6 times. This is the flip condition of the cost rule: at Rs 40 against Rs 1,200 the line says call nearly everyone, and the binding constraint is the budget. Tuesday's budget cut, precision at k, set Kalpa's 5,000 nudges the same way.

- (a) The file's order is not the score's order, so the first 1,000 above the line convert at about the base rate and waste the ranking.
- (b) 268 calls leave 732 of the budget unused, and the next 732 by score still convert far above the base rate.
- (d) A random 1,000 converts at about the base rate, 0.113, while the top 1,000 convert at 0.404, so the ranking is far from noise.

**In the interview.** When the budget binds, I rank and cut at the budget and report precision at that cut against the base rate, which is what the money buys.

### Q11, key b (negatives)

**Why it holds.** Recall is true positives over every actual positive, and the actual positives the model missed are the false negatives: on Tuesday's matrix, 174 over 174 plus 754. Precision is the ratio that takes false positives below the line.

**In the interview.** Recall asks, of the buyers out there, how many I found, so its denominator is every real buyer, caught or missed.

### Q12, key c

**Why it holds.** On the morning the list is built no call has happened, so its duration does not exist; a model that uses it learns from the answer. The dataset's own notes say so and ask for it to be discarded for a realistic model. The honest score is the one without it, 0.795. A jump this large from one column is the alarm, and the prediction-time question is the check. Wednesday read the notes aloud; Kalpa's settlement_status was the same leak.

- (a) The authors include it for benchmarks and say to discard it for a realistic model, which is what a call list is.
- (b) Accuracy barely moves on an 89 percent no outcome even when the leak is large; the recall nearly doubles, 174 to 390 buyers found, and that is the leak showing.
- (d) Scaling changes a column's units, never what it knows; the leak is the timing.

**In the interview.** A score that jumps on one column is a question about that column's timing, so I ask when it exists and drop it if it is after the prediction moment.

### Q13, key b, c, d

**Why it holds.** A column passes when its value exists at the prediction moment. Age, job and housing, the previous campaign's result and the rate published that morning all exist before any call. The previous result is strongly predictive, 65 percent yes among past successes, and still legitimate, because it was recorded before this campaign began, so it passes the timing test however strong it is. Duration exists only after this campaign's call. Wednesday's chapter interrogated every column with this one question.

- (a) This campaign's last call has not happened on the morning the list is built, so its length is from the future.

**In the interview.** I test a column by when it exists: a strong column from the past is a feature, and a weak one from the future is a leak.

### Q14, key a

**Why it holds.** Importance says how much the model leans on a column to predict, never what causes the outcome. Here the arrow plausibly runs backwards: a client who has decided to buy stays on to open the deposit, so a yes makes a call long. Coaching agents to keep people talking would lengthen calls without creating buyers. Testing it would need an experiment, such as a random half of agents coached. Wednesday's last chapter was what the importance chart cannot tell you.

- (b) Importance charts are drawn for linear and tree models alike; the limit is causal, not the model family.
- (c) A large weight says the model leans on the column to predict; a column can predict because the outcome causes it.
- (d) A gap that is not chance can still run from the outcome to the column, so size proves the link, never its direction.

**In the interview.** Importance is about prediction, so before I claim a cause I ask which way the arrow runs and what experiment would test it.

### Q15, key d

**Why it holds.** euribor3m rises and falls with the employment variation rate (correlation 0.97 across the file) and the number employed (0.95), so once they sit in one model, the weight on any one of them is what it adds after the others, and its sign can reverse; consumer confidence, at 0.28, is the one indicator that moves on its own. The prediction can be just as good while no single coefficient reads as an effect. So the memo answers the marketing head with the group: alone, higher rates go with fewer yeses, and the correlated indicators carry that one economic signal together, so no single coefficient is quoted as the effect of rates. Reading the group, keeping one representative or regularising are the fixes. Wednesday's case showed euribor3m flip with the economic trio.

- (a) The flip appears with every solver, because it comes from the data; refitting moves nothing.
- (b) +0.39 is the rate's weight once the other four indicators are held fixed, which says nothing about this year's campaign on its own.
- (c) Imbalance moves the intercept and the calibration and never flips one column's sign as others join; the -0.92 alone carries the other four indicators' signal inside it.

**In the interview.** When a sign flips as a column joins, I check the correlations first and read correlated columns as a group.

### Q16, key c (leakage)

**Why it holds.** A column the model could not have at the moment of prediction leaks the answer into training, which is data leakage; duration is the week's example, known only once the call ends. Drift is the world changing after training, and collinearity is columns moving together, Wednesday's sign flip.

**In the interview.** Leakage is a column from the future, so I ask of every column when it would exist on the morning the list is built.

### Q17, key a

**Why it holds.** Training near 1.0 with validation below the do-nothing baseline is memorising: grown without a limit, the tree carves leaves so small they fit individual clients. The fix is a brake chosen on data the tree did not fit: validation accuracy is flat near 0.90 from depth 3 to 8, and validation AUC peaks at depth 5, 0.783, so depth 5 is the cap to confirm by cross-validation. Thursday drew the unlimited tree as one leaf per customer.

- (b) The call log is duration, Wednesday's leak, and more columns give a tree more to memorise.
- (c) An unlimited tree is fully grown already; growing it further is impossible, and it is the growth that overfits.
- (d) A fit on validation spends validation, and the gap is the tree's, as the depth-capped trees on the same rows show.

**In the interview.** High training with low validation is memorising, so I add a brake and choose its strength on validation, then confirm it by cross-validation.

### Q18, key a, b, d

**Why it holds.** A depth cap and a minimum leaf size limit how finely a tree can carve the rows; a stronger penalty, which in scikit-learn's logistic regression is a smaller C, shrinks the weights and loosens the fit to the training rows; and cross-validation chooses either brake's strength on rows the model did not fit. Refitting until training scores 1.0 is the overfitting itself. Thursday's chapter put the brakes on the model.

- (c) Training at 1.0 is the symptom on Exhibit 4A, the unlimited tree's 0.996, never a brake.

**In the interview.** Brakes limit what the model can memorise, and cross-validation chooses how hard to press them.

### Q19, key b

**Why it holds.** Five-fold cross-validation fits five models, each on four of the five folds, about 19,770 of the 24,712 training clients, and scores each on the fifth, about 4,942. The five scores ran from 0.769 to 0.798, so a single split could have reported anything in that band; the mean, 0.786, with its spread is the honest estimate, and the spread is the size of the luck one split carries. Thursday's chapter set five exams instead of one.

- (a) Each fold trains its own model on the other four folds; one model scored five times would have seen the rows it is scored on.
- (c) 4,942 is each fold's validation share; each model trains on the other four-fifths.
- (d) A model fitted on all the rows is scored on rows it saw, and the spread is exactly what one split's luck looks like.

**In the interview.** k folds fit k models on (k minus 1) over k of the rows; I report the mean and the spread, and a gap smaller than the spread is a tie.

### Q20, key c

**Why it holds.** The three families sit within 0.011 AUC of each other, while the five folds of one model moved by about 0.03, so the ranking is inside the noise. On a tie the simpler model is the better recommendation: it is explained to a committee in one line per weight, monitored easily, and moved to lending with less to re-check. The flip is a gap that clears the folds' spread and is worth more in rupees, at the same budget of calls, than the cost of explaining and running the complex model. Thursday closed on why the boring model often ships.

- (a) The best number found on one validation slice carries that slice's luck, which Exhibit 4B sizes at about 0.03.
- (b) Boosting can generalise well, and it can also overfit; how it fits says nothing about whether it beats the others here.
- (d) AUC compares the ranking of any two models scored on the same rows, whatever their family.

**In the interview.** Inside the noise the simpler model ships, and I name the gap, in AUC and in rupees, at which the complex one would.

### Q21, key a (overfitting)

**Why it holds.** Perfect on training and far lower on validation is a model that memorised its training rows, which is overfitting; the room's unlimited tree scored 0.996 against 0.837. Underfitting scores low on both.

**In the interview.** A big gap between training and validation is memorising, so I add a brake and choose its strength on validation or by cross-validation.

### Q22, key d (split)

**Why it holds.** One split can be lucky or unlucky in which clients land in validation; cross-validation gives every row a turn in validation and averages the scores, so the luck of one split averages away. The week's five folds ran from 0.769 to 0.798.

**In the interview.** One split is one draw; five folds are five draws, so I quote the mean and the spread.

### Q23, key a

**Why it holds.** Staleness shows on fresh outcomes, so the rule compares what the model predicted with what happened, every month, against a gap stated in advance. On the bank's late rows the mean score was 0.152 while 24.6 percent said yes: the probabilities fell out of step even though the ranking still held at an AUC of 0.657, and the cost line, which reads the scores as probabilities, was drawn on numbers that understate every client's chance. Instacart's alarm was the same kind: a monitored metric falling from 93 to 61 percent, and its first fix was a threshold change while retraining caught up. Friday's chapter was when the model goes stale.

- (b) Retraining with no measurement can neither tell whether the old model failed nor whether the new one is better, and the outcomes it needs arrive weeks late.
- (c) Training accuracy is measured on rows the model already saw, so it stays high while the world moves, and a line drawn on scores that run low is wrong whatever training says.
- (d) A ranking can hold while the probabilities drift, as the late rows' AUC of 0.657 did, and the cost line reads probabilities, so the ranking cannot vouch for it.

**In the interview.** I monitor the decision's metric on fresh outcomes, predicted against actual, with the floor written into the memo before launch.

### Q24, key b, c

**Why it holds.** The caveat says where the model is weak and when to stop trusting it: its worst segment, sized, and the staleness trigger, which on this file would have fired as the yes rate climbed past the mean score. The validation AUC against the simpler model is evidence, and the budget of calls belongs to the error bill and the plan. Friday's memo ran claim, evidence, error bill and caveat.

- (a) A score against the simpler model is the memo's evidence line, not a limit on the model.
- (d) The budget sets how many calls the plan buys, which is the bill's line; it says nothing about where the model fails.

**In the interview.** The caveat names the weakest segment and the trigger that retires the model, both in numbers.

### Q25, key a

**Why it holds.** An offline score says the model ranks well on past rows; it does not say the campaign will sell more deposits. Booking.com's 23 comparisons put the correlation between the two near zero, -0.1 with an interval from -0.45 to 0.27, and the paper calls offline performance a health check. So the memo asks for a randomised trial that sets the model's list against the current rule on the business number, deposits sold per call, with the size fixed before it starts. Friday's memo turned the score into a decision the committee could test.

- (b) More decimals on the offline score sharpen the health check, and the gap to the business number stays where it was.
- (c) A larger offline gain is the very thing Booking.com found did not predict business gain.
- (d) The test score is the honest offline number, and it is still offline.

**In the interview.** Offline metrics earn a model its trial; the trial on the business number earns it the rollout.

### Q26, key d

**Why it holds.** The same cost rule runs in both businesses. Approve when the expected cost of approving, p times Rs 60,000, is below the expected cost of rejecting, (1 minus p) times Rs 3,000, where p is the chance of default: p below 3,000 over 63,000, about 0.048. So Rohan lends only above about a 95 percent chance of repayment, while the nudge acts on a 3 percent chance of a yes. The asymmetry flips, so the line flips. Both rules assume calibrated probabilities. Friday's transfer chapter and Tuesday's hand count on Rohan's costs drew this line.

- (a) The method moves and the costs do not: the nudge's cheap error is a wasted call, while the loan's expensive error is a default.
- (b) 0.5 treats the two errors as equal, while a default costs twenty times a wrongful rejection.
- (c) This puts the expensive error's cost on top, which would lend to a borrower with a 95 percent chance of default.

**In the interview.** The line is the cheap error's cost over both costs, so the same model calls on a 3 percent chance and lends only at 95 percent sure.


## Items by tag, level, day and part, for the tally

- [S] (12): Q1, Q4, Q5, Q7, Q8, Q9, Q11, Q12, Q13, Q16, Q17, Q21
- [F] (8): Q3, Q6, Q14, Q15, Q18, Q19, Q22, Q23
- [SV] (0): none
- [D] (6): Q2, Q10, Q20, Q24, Q25, Q26
- Easy (4): Q5, Q11, Q16, Q21
- Medium (9): Q1, Q3, Q4, Q8, Q14, Q18, Q22, Q24, Q25
- Hard (13): Q2, Q6, Q7, Q9, Q10, Q12, Q13, Q15, Q17, Q19, Q20, Q23, Q26
- Mon (5): Q1, Q2, Q3, Q4, Q5
- Tue (6): Q6, Q7, Q8, Q9, Q10, Q11
- Wed (5): Q12, Q13, Q14, Q15, Q16
- Thu (6): Q17, Q18, Q19, Q20, Q21, Q22
- Fri (4): Q23, Q24, Q25, Q26
- Part 1, Should the bank build a model, and what must it beat? (5): Q1, Q2, Q3, Q4, Q5
- Part 2, Which number tells the truth, and where does the line go? (6): Q6, Q7, Q8, Q9, Q10, Q11
- Part 3, What was the model allowed to know? (5): Q12, Q13, Q14, Q15, Q16
- Part 4, Is the model learning, or memorising? (6): Q17, Q18, Q19, Q20, Q21, Q22
- Part 5, Would the committee sign, and what moves to lending? (4): Q23, Q24, Q25, Q26

## New items waiting for the tracker

These items come from the week's source file, not the tracker. Accept one by adding it to the tracker's Saturday papers tab and deleting it from the source file.

- Q1 (One correct option, Medium, [S]): On Thursday an analyst opens the sealed test slice, sees 0.79, moves the threshold until the test score improves and reports the new test score to the committee. What is wrong, and what should the committee be told?
- Q2 (True or false, Hard, [D]): The calls run in date order. On the week's run the earliest 70 percent of rows say yes 5.6 percent of the time and the latest 30 percent say yes 24.6 percent of the time. Statement: for the question "whom do we call in the next campaign", a random split of all the rows estimates the model's score as honestly as a split by date. True or false, and why?
- Q3 (One correct option, Medium, [F]): The logistic model gives one client a score of 0.71. What does the 0.71 say?
- Q4 (More than one correct, Medium, [S]): The bank's marketing head brings four asks. Which need a model that predicts? Circle every correct letter.
- Q6 (True or false, Hard, [F]): Statement: an accuracy of 0.897 against 0.887 for calling nobody shows that the model at 0.5 is good enough to run the campaign. True or false, and why?
- Q7 (Applied maths, Hard, [S]): From the model's row of Exhibit 2A, compute its precision, recall and F1 at the threshold of 0.5, each to two decimal places. Show the working.
- Q8 (Applied maths, Medium, [S]): A call to a client who says no wastes Rs 40, and a buyer left off the list loses about Rs 1,200. Above what chance of a yes is a call worth making, and which way does that move the threshold from 0.5? Show the working.
- Q9 (One correct option, Hard, [S]): At Rs 40 a wasted call and Rs 1,200 a missed buyer, what is the error bill at the thresholds of 0.5 and 0.10 in Exhibit 2B, and which costs less?
- Q10 (One correct option, Hard, [D]): The call centre can make 1,000 calls in the next campaign, and the cost line would call 7,438 of these 8,238 clients (Exhibit 2B). Which plan goes to the marketing head?
- Q12 (One correct option, Hard, [S]): The junior's message reads: "Adding duration lifts AUC from 0.795 to 0.932. Shipping tonight." What is the reply?
- Q13 (More than one correct, Hard, [S]): The list for next month's campaign is built on the morning before the first call. Which columns pass the prediction-time question? Circle every correct letter.
- Q14 (True or false, Medium, [F]): In the model with duration, duration tops the importance chart, and clients who said yes talked 553 seconds on average against 221 for those who said no. Statement: longer calls cause deposits, so agents should be coached to keep clients on the line. True or false, and why?
- Q15 (One correct option, Hard, [F]): On its own, euribor3m takes a coefficient of -0.92 on the standardised scale; beside the four other economic indicators it takes +0.39. The marketing head asks whether higher rates help the campaign. What is the likeliest cause of the flip, and what does the memo say?
- Q17 (One correct option, Hard, [S]): The unlimited tree scores 0.996 on training and 0.837 on validation, below calling nobody. Which reading and which next step are right?
- Q18 (More than one correct, Medium, [F]): Which of these put a brake on overfitting? Circle every correct letter.
- Q19 (One correct option, Hard, [F]): Five-fold cross-validation of the logistic model gave the five fold scores in Exhibit 4B. How many models were fitted, on about how many clients each, and what does the spread tell the committee?
- Q20 (True or false, Hard, [D]): Statement: gradient boosting should go into the memo, since it scores the highest validation AUC of the three families in Exhibit 4B. True or false, and why?
- Q23 (One correct option, Hard, [F]): On the latest 30 percent of calls the model's mean score was 0.152 while 24.6 percent said yes (Exhibit 5A). Which monitoring rule catches this first, and what does it mean for the cost line drawn on these scores?
- Q24 (More than one correct, Medium, [D]): Which lines belong in the memo's caveat? Circle every correct letter.
- Q25 (One correct option, Medium, [D]): Anand Iyer asks what evidence would make him sign. Across 23 comparisons, Booking.com found offline gains and business gains almost uncorrelated (Exhibit 5B). What does the memo propose?
- Q26 (One correct option, Hard, [D]): Rohan Desai's lending book: approving a borrower who defaults costs Rs 60,000, and rejecting a good borrower costs Rs 3,000 of lost interest. Where does Rohan's approval line go?

## Bank items folded into deeper items

Each of these tracker items is not printed, because a deeper item on the paper tests the same concept. Accept a fold by recording it in the tracker; reject it by deleting it from `folded` in the week's source file.

- Bank 6 (True or false, Easy, Tue), folded into Q6: The printed statement is bank 6's trap on the week's own rows, where calling nobody already scores 0.887 on an 89 to 11 outcome, and option d keys the reason accuracy says little there.
- Bank 7 (True or false, Medium, Wed), folded into Q14: The statement reads the top of an importance chart as a cause, and the key refuses it because the yes drives the call's length as much as the reverse, which is bank 7's false statement judged with its reason.
- Bank 8 (True or false, Easy, Thu), folded into Q18: Option b is a stronger penalty on the weights, which loosens the fit to the training rows, and option c, fitting the training rows until they score 1.0, is bank 8's false statement offered as a brake.
- Bank 9 (True or false, Hard, Fri), folded into Q20: The key is bank 9's statement on the week's three families, a gap of 0.011 AUC inside the 0.03 one split moves by, so the simpler, explainable model is the recommendation.
- Bank 10 (One correct option, Easy, Mon), folded into Q4: The item sorts four of the bank's asks into the two that need a prediction and the two a query answers, which is bank 10's question with two keys where the bank has one.
- Bank 11 (One correct option, Medium, Mon), folded into Q3: The item asks what a logistic score of 0.71 says about one client, with bank 11's three misreadings as the distractors and the calibration condition added to the key.
- Bank 12 (One correct option, Medium, Tue), folded into Q8: The working puts the line at 1 in 31, about 0.032, far below 0.5, and the answer names the direction and that recall leads, which is bank 12's key derived where the bank only asks for it.
- Bank 13 (One correct option, Hard, Tue), folded into Q26: The item is bank 13 on Rohan Desai's own costs, set beside the nudge's cost line, and its key draws the approval line at about 0.05 chance of default, which is the bar moving up.
- Bank 14 (One correct option, Medium, Wed), folded into Q12: The item is bank 14's leak on the week's real column, duration, which the dataset's own notes say is known only after the call, and its key removes it and reports the honest 0.795.
- Bank 15 (One correct option, Hard, Wed), folded into Q15: The item is bank 15's sign flip as the week measured it, euribor3m from -0.92 alone to +0.39 beside the other indicators, with the same four causes as options.
- Bank 16 (One correct option, Medium, Thu), folded into Q17: The exhibit is bank 16's curve on the room's own tree, training rising to 0.996 while validation falls to 0.837, and the key caps the depth at the validation peak, which is bank 16's prescription.
- Bank 17 (One correct option, Medium, Fri), folded into Q23: The key is bank 17's monitoring rule made concrete on the bank's late rows, the called clients' yes rate against the mean score with a stated gap, and its distractors are bank 17's three.
- Bank 18 (More than one correct, Medium, Mon), folded into Q6: The statement sets the model against the majority-class baseline on the same validation rows, bank 18's options a and c, and its key says why beating the baseline on accuracy alone does not earn a ship, bank 18's option b.
- Bank 19 (More than one correct, Medium, Wed), folded into Q13: The item is bank 19's prediction-time test on the bank's own columns, with the tempting legitimate column, the previous campaign's result, beside the call's duration.
- Bank 20 (More than one correct, Medium, Thu), folded into Q18: The item is bank 20 on the week's two families, a depth cap, a stronger penalty and cross-validation as the brakes, with fitting the training rows harder as the false one.
- Bank 21 (More than one correct, Hard, Fri), folded into Q24: The item is bank 21's four-part memo on the bank's numbers, with the weakest segment and the staleness trigger as the caveat and the validation score and the budget as the lines that belong elsewhere.
- Bank 22 (Scenario set, Easy, Tue), folded into Q7: The working computes precision on the week's real matrix, 174 of the 268 called, which is bank 22's arithmetic on numbers the room ran.
- Bank 23 (Scenario set, Easy, Tue), folded into Q7: The working computes recall on the same matrix, 174 of the 928 buyers, which is bank 23's arithmetic.
- Bank 24 (Scenario set, Medium, Tue), folded into Q9: The item prices the week's real matrix at bank 24's costs, Rs 40 a wasted call and Rs 1,200 a missed buyer, which is bank 24's error bill.
- Bank 25 (Scenario set, Hard, Tue), folded into Q9: The item compares the bill at two thresholds and asks which costs less, which is bank 25's question on the week's own thresholds, and its distractors are the three ways the bill is usually miscounted.
- Bank 26 (Scenario set, Medium, Tue), folded into Q6: The key reads 0.897 accuracy beside 174 of 928 buyers found, which is bank 26's point that an accuracy figure says little about how many buyers were found.
- Bank 27 (Applied maths, Hard, Tue), folded into Q7: The item asks for precision, recall and F1 from one matrix, bank 27's three figures, on the week's real counts.
- Bank 28 (Applied maths, Medium, Tue), folded into Q8: The working states that one caught buyer pays for 30 wasted calls, which is bank 28's answer, and turns it into the threshold.
- Bank 29 (Applied maths, Easy, Thu), folded into Q19: The key states five models fitted on about four-fifths of the training rows each, which is bank 29's count on the week's 24,712 rows.

## The stretch page

- Stretch 1: Approve when (1 minus q) times 5 is below q times 1, where q is the chance of repaying, so q above 5 over 6, about 0.83. Rohan's costs run twenty to one, so his line sits higher, at about 0.95; the ratio of the two error costs sets the line in every business.
- Stretch 2: First the gap must clear the spread of the folds, about 0.03 here. Then count the buyers each model puts in its top 1,000 on the same rows: each extra buyer is worth about Rs 1,200 a campaign, so the extra buyers times Rs 1,200 must beat the yearly cost of explaining, monitoring and re-validating the complex model. Below both bars the logistic model ships, and the memo states the gap that would change the call.
- Stretch 3: For example: whom a bank should call for a term deposit, 41,188 calls with 11 percent yes; doing nothing scores 0.887 accuracy, so I judged the model on recall and the bill; I dropped duration, which leaked, for an honest AUC of 0.795; the top 1,000 by score converted at 0.404 against 0.113. Differently: I would split by date from the start, since the yes rate moved from 6 to 25 percent across the file.

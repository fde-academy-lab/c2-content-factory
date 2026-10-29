# Week 5 recap paper: key

TRAINER. Rendered from the tracker's item bank and the week's source file by `scripts/build_saturday_paper.py`. Change an item in the tracker, an option in `data/programme/paper_edits.yaml` or anything in `content/W05/SAT/internal/C2_W05_SAT_paper_source_INTERNAL.yaml`, and rebuild; never edit this file by hand. A stem, a situation or an option can be reworded in `data/programme/paper_edits.yaml`.

Saturday 7 November 2026. A 60-minute paper holding 22 items at 58.5 minutes by the blueprint's pace: 0 easy, 9 medium and 13 hard. 22 of them are new and not yet in the tracker.

## Marking

1. Papers are swapped, so nobody checks their own.
2. The Academic TA reads the key out part by part, and the marker writes a tick or a cross beside each item.
3. An item is right when its answer matches the key: every correct letter and no other on a more-than-one item, the number on an applied maths item (the working belongs to the discussion), and the whole sequence on an ordering item. The programme has set no partial-credit rule, so this key uses none.
4. The marker writes each part's ticks beside its rating on the answer sheet, and their total as Items right, out of 22, then hands the paper back.
5. The TA collects the papers and tallies the misses by tag, using the table below; that tally is Monday's remediation read. It is never a ranking and never read out by name.
6. The TA enters every paper in `C2_W05_SAT_item_analysis_TRAINER.xlsx` beside this key, by seat and never by name: 1 for a tick, 0 for a cross and a blank for an item left empty. The workbook orders the discussion from the most-missed item, flags any item to check, and gives each tag's rate for the room and for each seat.

## The blueprint

| Part | What it shows | Items | Minutes | Easy | Medium | Hard |
|---|---|---|---|---|---|---|
| 1. Should the bank build a model, and what must it beat? | whether you can frame a prediction problem, split the rows honestly and read what a model's score says | Q1 to Q4 (4) | 10 | 0 | 1 | 3 |
| 2. Which number tells the truth, and where does the line go? | whether you can read a confusion matrix, price each error and set the line the business can afford | Q5 to Q9 (5) | 15.5 | 0 | 3 | 2 |
| 3. What was the model allowed to know? | whether you can test each column against the moment of prediction and say what a coefficient does and does not prove | Q10 to Q13 (4) | 10.5 | 0 | 1 | 3 |
| 4. Is the model learning, or memorising? | whether you can read training against validation, choose complexity by cross-validation and say when the simpler model ships | Q14 to Q17 (4) | 10 | 0 | 3 | 1 |
| 5. Would the committee sign, and what moves to lending? | whether you can say what a memo must prove, how a model is caught going stale and why the same model draws an opposite line in lending | Q18 to Q22 (5) | 12.5 | 0 | 1 | 4 |
| Total | | 22 | 58.5 | 0 | 9 | 13 |

## What guessing alone would score

A learner who guessed every item blind would average 4.0 of 22, since a written answer cannot be guessed from a list, and fewer than one guesser in twenty would reach 8. A score of 7 or below is therefore within reach of guessing alone, and the tally reads such a paper as a conversation to have on Monday, never as a result.

## Reading the items after marking

The workbook flags an item to check when fewer than one learner in five got it right, or when the bottom third of the room got it right more often than the top third. Both are this programme's own working rule for a room of 39. A flagged item is discussed as usual; the TA also sends it, with the room's rate, to the tracker's owner, because the fault may sit in the item rather than in the learners.

## The key

| Q | Key | Type | Part | Level | Tag | Roles | Day | Min | Source | Interview anchor |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | a, d | More than one correct | 1 | Medium | [S] | DS, BA | Mon | 2.5 | new | When is a business problem a machine learning problem? |
| 2 | d | One correct option | 1 | Hard | [F] | DS, BA | Mon | 2.5 | new | What does a logistic output of 0.71 mean? |
| 3 | c | One correct option | 1 | Hard | [S] | DS, FDE | Mon | 2.5 | new | Train, validation, test: which is spent once? |
| 4 | a | True or false | 1 | Hard | [D] | DS | Mon | 2.5 | new | Train, validation, test: how should the rows be split for the question being asked? |
| 5 | d | True or false | 2 | Medium | [F] | DS, BA | Tue | 2.5 | new | Accuracy is 96 percent on a 96 to 4 split; good model? |
| 6 | Precision 174 / 268 = 0.65; recall 174 / 928 = 0.19; F1 = 2 x 174 / (2 x 174 + 94 + 754) = 348 / 1,196 = 0.29. | Applied maths | 2 | Medium | [S] | DS | Tue | 4 | new | Precision, recall and F1 from a confusion matrix. |
| 7 | Call when p x 1,200 > (1 - p) x 40, so p > 40 / 1,240 = 1 / 31, about 0.032 (1 in 30, 0.033, from one buyer paying for 30 calls, is accepted); the line moves down from 0.5 and recall leads. | Applied maths | 2 | Medium | [S] | DS, FDE | Tue | 3 | new | How do you set a threshold when the two errors cost differently? |
| 8 | F1 chooses 0.20: 2 x 376 / (752 + 488 + 552) = 752 / 1,792 = 0.42, against 1,232 / (1,232 + 2,138 + 312) = 1,232 / 3,682 = 0.33 at 0.10. The bill chooses 0.10: 2,138 x 40 + 312 x 1,200 = Rs 459,920, against 488 x 40 + 552 x 1,200 = Rs 681,920 at 0.20, Rs 222,000 less. They differ because F1 counts a wasted call and a missed buyer alike, while a missed buyer costs 30 times a wasted call. | Applied maths | 2 | Hard | [S] | DS, FDE, BA | Tue | 3.5 | new | How do you set a threshold when the two errors cost differently? |
| 9 | c | One correct option | 2 | Hard | [D] | DS, FDE, BA | Tue | 2.5 | new | The cost rule says call nearly everyone, and the budget says 1,000 calls: which wins, and what do you report? |
| 10 | c | One correct option | 3 | Medium | [S] | DS, FDE | Wed | 2.5 | new | What is data leakage, and how do you catch it before it ships? |
| 11 | b, c | More than one correct | 3 | Hard | [S] | DS, FDE | Wed | 2.5 | new | What is data leakage, and how do you catch it before it ships? |
| 12 | a | One correct option | 3 | Hard | [S] | DS, FDE | Wed | 2.5 | new | What is data leakage, and how do you catch it before it ships? |
| 13 | d | One correct option | 3 | Hard | [F] | DS, BA | Wed | 3 | new | What does a feature importance chart prove, and what does it not? |
| 14 | a | One correct option | 4 | Medium | [S] | DS | Thu | 2.5 | new | Overfitting: what it is, how you detect it, how you fix it. |
| 15 | a, b, d | More than one correct | 4 | Medium | [F] | DS | Thu | 2.5 | new | Overfitting: what it is, how you detect it, how you fix it. |
| 16 | b | One correct option | 4 | Medium | [F] | DS | Thu | 2.5 | new | Why cross-validation instead of one split? |
| 17 | b | True or false | 4 | Hard | [D] | DS, FDE | Thu | 2.5 | new | Your tuned model beats a simpler one by a hair: which ships, and why? |
| 18 | a | One correct option | 5 | Hard | [F] | DS, FDE | Fri | 2.5 | new | How would you know your model has gone stale? |
| 19 | b, c | More than one correct | 5 | Medium | [D] | DS, FDE, BA | Fri | 2.5 | new | Your tuned model beats a simpler one by a point and costs ten times more to explain; which ships? |
| 20 | d | One correct option | 5 | Hard | [D] | DS, FDE, BA | Fri | 2.5 | new | Your tuned model beats a simpler one by a hair: which ships, and why? |
| 21 | b | One correct option | 5 | Hard | [D] | DS, FDE, BA | Fri | 2.5 | new | The same model in retail and lending: why are the thresholds opposite? |
| 22 | c | One correct option | 5 | Hard | [F] | DS, FDE, BA | Tue | 2.5 | new | Precision or recall for fraud, and why? |

## Why each answer holds

### Q1, key a, d

**Why it holds.** A prediction problem asks about an outcome that has not happened yet, from what is known now, and has past examples to learn from. Ranking next month's clients and scoring a client never called before both ask about a future yes. Counting 2009's yes answers and listing past successes are queries on rows that already exist. Monday's first chapter sorted Kalpa's asks into prediction, rule and query.

- (b) A past month's chance of a yes is a rate already in the file, so a count answers it and no model is needed.
- (c) poutcome already records each past result, so a filter lists them; nothing is predicted.

**In the interview.** If the answer is already in a table, it is a query; if it is about a future outcome I have past examples of, it is a model.

### Q2, key d

**Why it holds.** A logistic model outputs an estimated chance for one client, so 0.71 says that clients scored like this one say yes about 71 times in 100. The memo may read it that way only once the scores are checked against what happened: among validation clients scored near 0.71, about 71 in 100 should have said yes. That check is calibration. AUC measures the ranking alone, so it is unchanged when every score is halved and cannot vouch for one chance; Friday's split by date kept a usable ranking while its scores ran far below the yes rate. The threshold that turns a chance into a call comes from the costs. Monday bent the line into the S on the bank's data; Friday showed the scores drifting while the ranking held.

- (a) AUC is the chance that a buyer outranks a non-buyer, so it stays the same when every score is halved; it vouches for the order, never for a chance.
- (b) Accuracy across many clients is a property of the model on a slice, while 0.71 belongs to one client.
- (c) 0.5 is a default, never part of the score; the threshold is set from the costs, and beating the baseline does not turn a chance into a verdict.

**In the interview.** 0.71 is an estimated chance for this one client, and I read it as a chance only after checking that clients scored near 0.71 said yes about 71 times in 100; the AUC checks the ranking.

### Q3, key c

**Why it holds.** Choosing the best of 60 on one slice picks the version whose score on that slice was luckiest, so the chosen score flatters. On fresh rows the luck does not repeat and the score falls back toward what an ordinary model of the week scores: the room's notebook measured 0.8971, the customer-table model's 0.897 on Exhibit 1A, an honest edge of 0.98 points against the 1.80 reported. No version was fitted to the 2,000, so the score does not collapse; the 2,000 were spent on a choice, which makes them validation. A test slice is scored once, at the end, on a model already chosen. Monday's peek chapter ran this loop, and the sealed envelope stayed shut until Friday.

- (a) Never training on a slice is not enough: choosing among 60 versions by their score on it carries the slice's luck into the choice.
- (b) The versions are ordinary models of the week, each near Exhibit 1A's 0.897, so the edge shrinks without vanishing; and a slice that chose a version is validation, never training.
- (d) No rule halves an edge: the fall is the luck that 60 tries picked, and the chosen version is an ordinary customer-table model, which Exhibit 1A puts at 0.897.

**In the interview.** A slice used to choose is validation, so I expect its best score to fall back on fresh rows by the luck the choice picked, and I score the test once, at the end.

### Q4, key a

**Why it holds.** The ask is about a campaign that has not happened yet, so the honest test trains on the earlier calls and scores the later ones. A random split puts calls from the same months in training and validation, and the month and the economic indicators mark the period, so the model partly learns when a call happened. On the week's run the yes rate moved from 5.6 to 24.6 percent across the file, and Friday's split by date cut the AUC from 0.795 to 0.664. Monday raised the split by time; Friday ran it.

- (b) The split by date wins on timing, not on the count of yes rows; validation already holds 928 yes rows under the random split.
- (c) Stratifying keeps the yes share equal, and it says nothing about mixing months, which is what lets the random split flatter the model.
- (d) The month and the five economic indicators each mark the period a call was made in, so the model reads time without a date column.

**In the interview.** I split the way the model will be used: train on the past, score on the later period, and expect that score to be lower than the random split's.

### Q5, key d

**Why it holds.** On an outcome where 89 clients in 100 say no, saying no to everyone scores 0.887, so a point of accuracy above it says almost nothing about the campaign. The model at 0.5 calls 268 people and finds 174 of the 928 buyers, a recall of 0.19, and leaves 754 buyers uncalled. Beating the majority baseline is the floor, and the case for shipping is made on recall, precision and the bill. Tuesday's case opened on this matrix: the 89 percent model that called nobody.

- (a) Beating the baseline is necessary, and on accuracy it is nearly free here, since the baseline itself is 0.887.
- (b) The count is right, 94 plus 754 against 928, but it weighs a wasted call and a missed buyer the same, while one costs Rs 40 and the other Rs 1,200.
- (c) Validation is where models and thresholds are compared, so 0.897 is a fair validation number; the trouble is what accuracy measures, not where it was read.

**In the interview.** On a lopsided outcome I quote the base rate first, then recall and precision, and accuracy last if at all.

### Q6, key Precision 174 / 268 = 0.65; recall 174 / 928 = 0.19; F1 = 2 x 174 / (2 x 174 + 94 + 754) = 348 / 1,196 = 0.29.

**Why it holds.** Precision divides the caught buyers by everyone called, 174 over 174 plus 94, 0.649. Recall divides them by every buyer, 174 over 174 plus 754, 0.1875. F1 is the harmonic mean, 2PR over P plus R, which on counts is 2TP over 2TP plus FP plus FN: 348 over 1,196, 0.291. The harmonic mean sits near the smaller of the two, which is why a low recall drags F1 down. Tuesday's deck taught precision and recall on this matrix and named F1 last.

**In the interview.** Precision is of those I called, recall is of those out there, and F1 is their harmonic mean, 2TP over 2TP plus FP plus FN.

### Q7, key Call when p x 1,200 > (1 - p) x 40, so p > 40 / 1,240 = 1 / 31, about 0.032 (1 in 30, 0.033, from one buyer paying for 30 calls, is accepted); the line moves down from 0.5 and recall leads.

**Why it holds.** Call when the expected loss of not calling, p times Rs 1,200, is above the expected loss of calling, (1 minus p) times Rs 40. That gives p above 40 over 1,240, 1 in 31, about 0.032. In plain words, one caught buyer pays for 30 wasted calls, so a call is worth it above about a 1-in-31 chance. The line moves far below 0.5, so recall leads, because a miss costs thirty times a wasted call. The rule assumes calibrated scores. Tuesday's chapter on what each mistake costs taught the 1-in-N test as coins.

**In the interview.** The line sits at the cost of a false alarm over the sum of both costs, so when a miss costs thirty times a false alarm I act on about a 1-in-31 chance.

### Q8, key F1 chooses 0.20: 2 x 376 / (752 + 488 + 552) = 752 / 1,792 = 0.42, against 1,232 / (1,232 + 2,138 + 312) = 1,232 / 3,682 = 0.33 at 0.10. The bill chooses 0.10: 2,138 x 40 + 312 x 1,200 = Rs 459,920, against 488 x 40 + 552 x 1,200 = Rs 681,920 at 0.20, Rs 222,000 less. They differ because F1 counts a wasted call and a missed buyer alike, while a missed buyer costs 30 times a wasted call.

**Why it holds.** F1 on counts is 2TP over 2TP plus FP plus FN. At 0.20 that is 752 over 1,792, 0.42; at 0.10 it is 1,232 over 3,682, 0.33, so F1 prefers 0.20. The bill prices each box: at 0.20, 488 wasted calls cost Rs 19,520 and 552 missed buyers Rs 662,400, Rs 681,920 in all; at 0.10, 2,138 wasted calls cost Rs 85,520 and 312 missed buyers Rs 374,400, Rs 459,920. F1 weighs a wasted call and a missed buyer the same, so it stops lowering the line once wasted calls pile up, while the bill keeps lowering it, because each missed buyer costs as much as 30 wasted calls. The business runs on the bill. The usual slips are swapping the two prices, pricing one box only, and taking F1 as the plain average of precision and recall. Tuesday's slider drew this bill against the threshold.

**In the interview.** F1 is a summary for when nobody has priced the errors; once they are priced I choose the threshold on the bill, and I can say why the two disagree.

### Q9, key c

**Why it holds.** When the budget binds before the cost line does, the ranking carries the decision. The top 1,000 by score are the 864 clients above 0.20 and the next 136, so they hold every buyer of plan (a), 376, and of plan (b), 174, and the 136 extra calls go to clients scored just under 0.20, far above the cost line, so each is worth more than its Rs 40. On validation the top 1,000 held 404 buyers, a precision at 1,000 of 0.404 against the base rate of 0.113, about 3.6 times. This is the flip condition of the cost rule: at Rs 40 against Rs 1,200 the line calls nearly everyone, and the binding constraint is the budget. Tuesday's budget cut, precision at k, set Kalpa's 5,000 nudges the same way.

- (a) The top 1,000 contains these 864 and adds 136 clients still far above the cost line, so it finds at least the same 376 buyers and more, and no call is left unused.
- (b) 268 calls leave 732 of the budget unused, and the next 732 by score still convert far above the base rate.
- (d) A random draw throws the ranking away and converts near 913 in 7,438, about 0.123, against 0.404 for the top 1,000.

**In the interview.** When the budget binds, I rank and cut at the budget and report precision at that cut against the base rate, since a smaller cut only leaves paid-for calls unused.

### Q10, key c

**Why it holds.** On the morning the list is built no call has happened, so its duration does not exist; a model that uses it learns from the answer, which is data leakage. The dataset's own notes say so and ask for it to be discarded for a realistic model. The honest score is the one without it, 0.795. A jump this large from one column is the alarm, and the prediction-time question is the check. Wednesday read the notes aloud; Kalpa's settlement_status was the same leak.

- (a) The authors include it for benchmarks and say to discard it for a realistic model, which is what a call list is.
- (b) Accuracy barely moves on an 89 percent no outcome even when the leak is large; the recall nearly doubles, 174 to 390 buyers found, and that is the leak showing.
- (d) Scaling changes a column's units, never what it knows; the leak is the timing.

**In the interview.** A score that jumps on one column is a question about that column's timing, so I ask when it exists and drop it if it is after the prediction moment.

### Q11, key b, c

**Why it holds.** A column passes when its value exists at the prediction moment. Age, job and housing and the previous campaign's result exist before any call. The previous result is strongly predictive, 65 percent yes among past successes, and still legitimate, because it was recorded before this campaign began, so it passes the timing test however strong it is. Duration exists only after this campaign's call, and so does a callback flag an agent sets during it, however much it reads like a fact about the client: a column written by this campaign's own calls is from the future on the morning the list is built. Wednesday's chapter interrogated every column with this one question.

- (a) This campaign's last call has not happened on the morning the list is built, so its length is from the future.
- (d) An agent sets it on a call in this campaign, which has not happened on the morning the list is built, so it is from the future however much it reads like a profile column.

**In the interview.** I test a column by when it exists: a strong column from the past is a feature, and a respectable column from a period that has not ended is a leak.

### Q12, key a

**Why it holds.** The held-out X-rays came from the same two hospital systems as the training X-rays, so whatever marked the hospital marked them too. One system's pneumonia rate was 34.2 percent and the other's 1.2 percent, so the hospital alone predicts the label: the paper reports that sorting X-rays by hospital alone scored 0.861, and a network named the hospital of 22,050 of 22,062 X-rays from one system, so much of the 0.931 was the hospital. At a third hospital the shortcut no longer carried the label, and the AUC fell to 0.815. That is leakage through a proxy, which a held-out slice from the same source cannot catch; a score on data from a new site, or for the bank a later period, catches it. Overfitting shows as training far above held-out, and this model's held-out score was high. Wednesday told this case beside duration.

- (b) Memorising shows as high training against low held-out scores; here the held-out score was 0.931, so the trouble is what the held-out X-rays shared with training.
- (c) Pneumonia ran at 34.2 percent in one training system and 1.2 percent in the other, so where an X-ray came from predicted the label, which a new hospital cannot supply; the model needs the check.
- (d) The paper reports the fall as significant, P = 0.001, and a model sold at 0.931 that delivers 0.815 has a problem to name, never noise to wave off.

**In the interview.** A held-out slice from the same source shares the source's shortcuts, so before launch I score the model on a new site or a later period and ask what else marks the label.

### Q13, key d

**Why it holds.** Importance says how much the model leans on a column to predict, never what causes the outcome, and here the arrow plausibly runs backwards: a client who has decided to buy stays on to open the deposit, so a yes makes a call long. A weight is the same kind of number. euribor3m rises and falls with the employment variation rate (correlation 0.97 across the file) and the number employed (0.95), so the model cannot hold it fixed while they move, and its weight swings from -0.92 alone to +0.39 beside them. The memo answers the marketing head with the indicators read as one economic signal, and proposes a test for the coaching idea, such as a random half of agents coached. Wednesday's last chapters were what the importance chart cannot tell you and the sign that flipped.

- (a) Scoring well on validation says the model predicts; it says nothing about which way a cause runs or whether one weight can be read alone.
- (b) Holding the other indicators fixed is a world the file never shows, since the rate moves with them at 0.97 and 0.95; the +0.39 is what the rate adds after them, never its effect.
- (c) A gap that is not chance can still run from the outcome to the column, so its size proves a link and never its direction.

**In the interview.** Importance and weights describe prediction, so before I claim a cause I ask which way the arrow runs and whether the column moves with others, and I propose the experiment that would test it.

### Q14, key a

**Why it holds.** Training near 1.0 with validation below the do-nothing baseline is memorising: grown without a limit, the tree carves leaves so small they fit individual clients. The fix is a brake chosen on data the tree did not fit: validation accuracy is flat near 0.90 from depth 3 to 8, and validation AUC peaks at depth 5, 0.783, so depth 5 is the cap to confirm by cross-validation. Thursday drew the unlimited tree as one leaf per customer.

- (b) The call log is duration, Wednesday's leak, and more columns give a tree more to memorise.
- (c) An unlimited tree is fully grown already; growing it further is impossible, and it is the growth that overfits.
- (d) A fit on validation spends validation, and the gap is the tree's, as the depth-capped trees on the same rows show.

**In the interview.** High training with low validation is memorising, so I add a brake and choose its strength on validation, then confirm it by cross-validation.

### Q15, key a, b, d

**Why it holds.** A depth cap and a minimum leaf size limit how finely a tree can carve the rows; a stronger penalty, which in scikit-learn's logistic regression is a smaller C, shrinks the weights and loosens the fit to the training rows; and cross-validation chooses either brake's strength on rows the model did not fit. Refitting until training scores 1.0 is the overfitting itself. Thursday's chapter put the brakes on the model.

- (c) Training at 1.0 is the symptom on Exhibit 4A, the unlimited tree's 0.996, never a brake.

**In the interview.** Brakes limit what the model can memorise, and cross-validation chooses how hard to press them.

### Q16, key b

**Why it holds.** Five-fold cross-validation fits five models, each on four of the five folds, about 19,770 of the 24,712 training clients, and scores each on the fifth, about 4,942. The five scores ran from 0.769 to 0.798, so a single split could have reported anything in that band; the mean, 0.786, with its spread is the honest estimate, and the spread is the size of the luck one split carries. Thursday's chapter set five exams instead of one.

- (a) Each fold trains its own model on the other four folds; one model scored five times would have seen the rows it is scored on.
- (c) 4,942 is each fold's validation share; each model trains on the other four-fifths.
- (d) A model fitted on all the rows is scored on rows it saw, and the spread is exactly what one split's luck looks like.

**In the interview.** k folds fit k models on (k minus 1) over k of the rows; I report the mean and the spread, and I compare two models fold by fold on the same folds.

### Q17, key b

**Why it holds.** The three families sit within 0.011 AUC of each other on one validation slice, while the five folds of one model moved by about 0.03, so one slice settles nothing. Thursday ran two tests on the same five folds. Boosting led logistic on every fold, by 0.003 to 0.014 AUC, so its lead is real; the second test asks whether so small a lead pays, and at the same budget of calls its extra buyers were worth less than the cost the room set for explaining and running it. So the simpler model is the recommendation: it is explained to a committee in one line per weight, monitored easily, and moved to lending with less to re-check. The flip is a lead that holds across the folds and is worth more in rupees, at the same budget of calls, than that cost. Thursday closed on why the boring model often ships.

- (a) A logistic model overfits too when it has many columns and no penalty; its case here is the small lead it gives up and its plainness.
- (c) The best of three on one slice is flattered by the choosing, and even a lead that holds on every fold has to pay for the complex model's upkeep before it ships.
- (d) AUC compares the ranking of any two models scored on the same rows, whatever their family.

**In the interview.** A lead must hold fold by fold and pay for itself in rupees before the complex model ships, and I name the gap at which it would.

### Q18, key a

**Why it holds.** Staleness shows on fresh outcomes, so the rule compares what the model predicted with what happened, every month, against a gap stated in advance. On the bank's late rows the mean score was 0.159 while 24.6 percent said yes, so the scores run below the clients' true chances. The cost line asks for a true chance above about 1 in 31, and on scores that understate the chance the same true chance shows up as a lower score, so the cut on the scores moves down until they are recalibrated on recent outcomes. More clients saying yes is the reason the cut falls, never a reason to be choosier. The ranking still held at an AUC of 0.664, which is why the alarm watches the probabilities. Instacart's alarm was the same kind: a monitored metric falling from 93 to 61 percent, and its first fix was a threshold change while retraining caught up. Friday's chapter was when the model goes stale.

- (b) A higher yes rate raises the clients' true chances, so more of them clear the cost line; raising the cut would drop clients the line says to call.
- (c) Retraining with no measurement can neither tell whether the old model failed nor whether the new one is better, and the outcomes it needs arrive weeks late.
- (d) Training accuracy is measured on rows the model already saw, so it stays high while the world moves, and a cut set on scores that run low is wrong whatever training says.

**In the interview.** I monitor predicted against actual on fresh outcomes with the gap written into the memo, and when the scores run low I recalibrate them before the cut means what it meant.

### Q19, key b, c

**Why it holds.** The caveat says where the model is weak and when to stop trusting it: its worst segment, sized, and the staleness trigger, which on this file would have fired as the yes rate climbed past the mean score. The validation AUC against the simpler model is evidence, and the budget of calls belongs to the error bill and the plan. Friday's memo ran claim, evidence, error bill and caveat.

- (a) A score against the simpler model is the memo's evidence line, not a limit on the model.
- (d) The budget sets how many calls the plan buys, which is the bill's line; it says nothing about where the model fails.

**In the interview.** The caveat names the weakest segment and the trigger that retires the model, both in numbers.

### Q20, key d

**Why it holds.** An offline score says the model ranks past rows well; it does not say the campaign will sell more deposits, and Booking.com's 23 comparisons put the correlation between the two near zero, -0.1 with an interval from -0.45 to 0.27, which is why the paper calls offline performance a health check. So the evidence is a randomised trial on the business number: next month's clients assigned at random between the list and today's rule, run in the same weeks, scored on deposits per call, with the size fixed before it starts. A sealed test score is still offline. A before-and-after comparison mixes the list with the month, and on this file the yes rate climbed from 5.6 to 24.6 percent across the calls (Exhibit 5A), so a month can beat the last without the list. A random trial scored on AUC randomises the right thing and measures the wrong one. Friday's memo turned the score into a decision the committee could test.

- (a) The yes rate moved from 5.6 to 24.6 percent across the file (Exhibit 5A), so this month against last month measures the calendar as much as the list.
- (b) Randomising is right, and the AUC is still the offline health check Booking.com found did not predict business gains; the trial is scored on deposits.
- (c) Two faults: the yes rate moved from 5.6 to 24.6 percent across the file, so next month against validation measures the calendar too, and AUC is the offline health check Booking.com found did not predict business gains.

**In the interview.** Offline metrics earn a model its trial; a randomised trial on the business number, run in the same weeks, earns it the rollout.

### Q21, key b

**Why it holds.** Approve when the expected cost of approving, p times Rs 60,000, is below the expected cost of rejecting, (1 minus p) times Rs 3,000, where p is the chance of default: p below 3,000 over 63,000, about 0.048. P at 0.04 is approved and Q at 0.08 is rejected. So Rohan lends only above about a 95 percent chance of repayment, while the nudge acts on a 3 percent chance of a yes: the asymmetry flips, so the line flips. Both rules assume calibrated probabilities. Friday's transfer chapter and Tuesday's hand count on Rohan's costs drew this line.

- (a) 0.5 treats the two errors as equal, while a default costs twenty times a wrongful rejection.
- (c) 92 in 100 repaying sounds strong, but each default costs Rs 60,000 against Rs 3,000 lost on a rejection, so the bar sits near 95 in 100 repaying, and Q falls below it.
- (d) 3 percent is the nudge's line, from Rs 40 against Rs 1,200; Rohan's costs, Rs 3,000 against Rs 60,000, put his line at 3,000 over 63,000, about 4.8 percent, so P at 4 percent clears it.

**In the interview.** The line is the cheap error's cost over both costs, so the same model calls on a 3 percent chance and lends only below about a 5 percent chance of default.

### Q22, key c

**Why it holds.** Rohan's question leaves out the two facts that decide it: what a flag does, and how many flags the team can work. If a flag blocks the payment, a false alarm stops a genuine customer, and the survey Stripe cites says a third of them may not come back, so precision gains weight and the line rises. If a flag sends the payment to a reviewer, a false alarm costs an analyst's minutes while a missed fraud costs the payment, so recall leads, up to what the team can review; with a fixed team the number to report is precision at its capacity, as Flipkart's trust team read the top 250 and found 211 frauds. Each one-word answer is right in one of those worlds and wrong in the other, and how rare fraud is settles neither, since it says how many false alarms come with each catch and never which costs more. So the reply opens on the question that decides it, then draws the line from the two costs. Tuesday met Stripe and Flipkart; Friday carried the cost line to Rohan's business.

- (a) Stripe's break-even prices a block at a sale's margin; if a false block also loses the customer the line rises, so recall cannot be chosen before knowing what a flag does.
- (b) How rare fraud is sets how many false alarms come with each catch and leaves open which error costs more; that turns on what a flag does, so this question cannot settle the answer.
- (d) A false decline costs a customer only when a flag declines the payment; if it queues a review, missed fraud is the larger cost, so precision cannot be chosen before knowing what a flag does.

**In the interview.** Precision or recall is a question about costs, so I first ask what a flag does and how many the team can review, then set the line from the two costs and report precision at the team's capacity.


## Items by tag, level, day and part, for the tally

- [S] (9): Q1, Q3, Q6, Q7, Q8, Q10, Q11, Q12, Q14
- [F] (7): Q2, Q5, Q13, Q15, Q16, Q18, Q22
- [SV] (0): none
- [D] (6): Q4, Q9, Q17, Q19, Q20, Q21
- Easy (0): 
- Medium (9): Q1, Q5, Q6, Q7, Q10, Q14, Q15, Q16, Q19
- Hard (13): Q2, Q3, Q4, Q8, Q9, Q11, Q12, Q13, Q17, Q18, Q20, Q21, Q22
- Mon (4): Q1, Q2, Q3, Q4
- Tue (6): Q5, Q6, Q7, Q8, Q9, Q22
- Wed (4): Q10, Q11, Q12, Q13
- Thu (4): Q14, Q15, Q16, Q17
- Fri (4): Q18, Q19, Q20, Q21
- Part 1, Should the bank build a model, and what must it beat? (4): Q1, Q2, Q3, Q4
- Part 2, Which number tells the truth, and where does the line go? (5): Q5, Q6, Q7, Q8, Q9
- Part 3, What was the model allowed to know? (4): Q10, Q11, Q12, Q13
- Part 4, Is the model learning, or memorising? (4): Q14, Q15, Q16, Q17
- Part 5, Would the committee sign, and what moves to lending? (5): Q18, Q19, Q20, Q21, Q22

## New items waiting for the tracker

These items come from the week's source file, not the tracker. Accept one by adding it to the tracker's Saturday papers tab and deleting it from the source file.

- Q1 (More than one correct, Medium, [S]): The bank's marketing head brings four asks. Which need a model that predicts? Circle every correct letter.
- Q2 (One correct option, Hard, [F]): The logistic model on the customer table gives one client a score of 0.71, and its validation AUC is 0.761 (Exhibit 1A). What does the 0.71 say, and what would let the memo read it that way?
- Q3 (One correct option, Hard, [S]): On Monday a junior tried 60 versions of the model, each on a different list of the customer table's columns, scored all 60 on the same 2,000 held-out clients and kept the best: accuracy 0.9055 there, where calling nobody scores 0.8875. On 6,238 fresh clients, where calling nobody scores 0.8873, what does the chosen version score, and what have the 2,000 clients become?
- Q4 (True or false, Hard, [D]): The calls run in date order. On the week's run the earliest 70 percent of rows say yes 5.6 percent of the time and the latest 30 percent say yes 24.6 percent of the time. Statement: for the question "whom do we call in the next campaign", a split by date estimates the model's score more honestly than a random split of all the rows. True or false, and why?
- Q5 (True or false, Medium, [F]): Statement: an accuracy of 0.897 against 0.887 for calling nobody shows that the model at 0.5 is good enough to run the campaign. True or false, and why?
- Q6 (Applied maths, Medium, [S]): From the model's row of Exhibit 2A, compute its precision, recall and F1 at the threshold of 0.5, each to two decimal places. Show the working.
- Q7 (Applied maths, Medium, [S]): A call to a client who says no wastes Rs 40, and a buyer left off the list loses about Rs 1,200. Above what chance of a yes is a call worth making, and which way does that move the threshold from 0.5? Show the working.
- Q8 (Applied maths, Hard, [S]): Two teammates choose between the thresholds of 0.20 and 0.10 in Exhibit 2B: one by F1, the other by the error bill at Rs 40 a wasted call and Rs 1,200 a missed buyer. Which threshold does each choose, with the figures that decide it, and why do the two choices differ? Show the working.
- Q9 (One correct option, Hard, [D]): The call centre can make 1,000 calls in the next campaign, and the cost line would call 7,438 of these 8,238 clients (Exhibit 2B). Which plan goes to the marketing head?
- Q10 (One correct option, Medium, [S]): The junior's message reads: "Adding duration lifts AUC from 0.795 to 0.932. Shipping tonight." What is the reply?
- Q11 (More than one correct, Hard, [S]): The list for next month's campaign is built on the morning before the first call. Which columns pass the prediction-time question? Circle every correct letter.
- Q12 (One correct option, Hard, [S]): Exhibit 3B reports a pneumonia model that scored well on held-out X-rays and worse at a new hospital. Which reading holds, and which check would have caught it before launch?
- Q13 (One correct option, Hard, [F]): The marketing head reads Exhibit 3C and draws two conclusions. One: longer calls make deposits, so agents should be coached to keep clients on the line. Two: higher rates bring deposits, since euribor3m's weight is +0.39 once the other columns are held fixed. Which reply holds?
- Q14 (One correct option, Medium, [S]): The unlimited tree scores 0.996 on training and 0.837 on validation, below calling nobody. Which reading and which next step are right?
- Q15 (More than one correct, Medium, [F]): Which of these put a brake on overfitting? Circle every correct letter.
- Q16 (One correct option, Medium, [F]): Five-fold cross-validation of the logistic model gave the five fold scores in Exhibit 4B. How many models were fitted, on about how many clients each, and what does the spread tell the committee?
- Q17 (True or false, Hard, [D]): Statement: the logistic model should go into the memo, although gradient boosting scores the highest validation AUC of the three families in Exhibit 4B. True or false, and why?
- Q18 (One correct option, Hard, [F]): On the latest 30 percent of calls the model's mean score was 0.159 while 24.6 percent said yes (Exhibit 5A), and Exhibit 5B sets Instacart's case beside it. Which monitoring rule catches this first, and what happens to the cut on these scores that the cost line sets?
- Q19 (More than one correct, Medium, [D]): Which lines belong in the memo's caveat? Circle every correct letter.
- Q20 (One correct option, Hard, [D]): Anand Iyer asks what evidence would make him sign. Across 23 comparisons, Booking.com found offline gains and business gains almost uncorrelated (Exhibit 5B). Which test does the memo propose for next month?
- Q21 (One correct option, Hard, [D]): Rohan Desai's lending book: approving a borrower who defaults costs Rs 60,000, and rejecting a good borrower costs Rs 3,000 of lost interest. His model, calibrated on recent loans, gives applicant P a 4 percent chance of default and applicant Q an 8 percent chance. Whom does Rohan approve?
- Q22 (One correct option, Hard, [F]): Rohan Desai asks one question about a fraud model for Kalpa Financial Services' payments app: "Do we tune it for precision or for recall?" Exhibit 5C sets two public cases beside his question. Which reply holds?

## Bank items folded into deeper items

Each of these tracker items is not printed, because a deeper item on the paper tests the same concept. Accept a fold by recording it in the tracker; reject it by deleting it from `folded` in the week's source file.

- Bank 1 (Fill in the blank, Easy, Mon), folded into Q3: The raise of 28 October 2026 folded the bank's three easy blanks, since each sat beside an item that printed its word (the peek item's own options said a slice was spent). The peek item's key says that a slice used to choose among 60 versions has become validation and that only a slice scored once, at the end, is a test, which is bank 1's word on the room's own loop.
- Bank 2 (Fill in the blank, Easy, Tue), folded into Q6: The raise of 28 October 2026 folded the blank, which printed after the worked item that divides 174 by 174 plus 754. That working puts the false negatives in recall's denominator, which is bank 2's word on the week's real matrix.
- Bank 3 (Fill in the blank, Easy, Wed), folded into Q10: The raise of 28 October 2026 folded the blank. The duration item's key drops a column that exists only once the call ends and its reason names it data leakage, which is bank 3's word on the week's real column.
- Bank 4 (Fill in the blank, Easy, Thu), folded into Q14: The blind sitting found the bank's 100 and 61 percent read beside Exhibit 4A's 0.996 and 0.619, two metrics, and found the blank cued by the part's title and by the options above it, so the item that reads training at 0.996 against validation at 0.837 as memorising tests bank 4's word on the room's own tree.
- Bank 5 (Fill in the blank, Medium, Thu), folded into Q16: The blind sitting found the blank answered by the folds item's own options, which say what one split could have read, so the folds item, whose key is the luck of one split sized at 0.77 to 0.80, tests bank 5's word.
- Bank 6 (True or false, Easy, Tue), folded into Q5: The printed statement is bank 6's trap on the week's own rows, where calling nobody already scores 0.887 on an 89 to 11 outcome, and option d keys the reason accuracy says little there.
- Bank 7 (True or false, Medium, Wed), folded into Q13: The marketing head's first conclusion reads the top of an importance chart as a cause, and the key refuses it because the yes drives the call's length as much as the reverse, which is bank 7's false statement judged with its reason.
- Bank 8 (True or false, Easy, Thu), folded into Q15: Option b is a stronger penalty on the weights, which loosens the fit to the training rows, and option c, fitting the training rows until they score 1.0, is bank 8's false statement offered as a brake.
- Bank 9 (True or false, Hard, Fri), folded into Q17: The key is bank 9's statement on the week's three families, a lead of 0.011 AUC that has to hold fold by fold and pay for its upkeep before it ships, so the simpler, explainable model is the recommendation.
- Bank 10 (One correct option, Easy, Mon), folded into Q1: The item sorts four of the bank's asks into the two that need a prediction and the two a query answers, which is bank 10's question with two keys where the bank has one.
- Bank 11 (One correct option, Medium, Mon), folded into Q2: The item asks what a logistic score of 0.71 says about one client, with bank 11's three misreadings as the distractors, and adds the check that lets the memo read it as a chance, since an AUC vouches for the ranking and never for the chances.
- Bank 12 (One correct option, Medium, Tue), folded into Q7: The working puts the line at 1 in 31, about 0.032, far below 0.5, and the answer names the direction and that recall leads, which is bank 12's key derived where the bank only asks for it.
- Bank 13 (One correct option, Hard, Tue), folded into Q21: The item is bank 13 on Rohan Desai's own costs, set beside the nudge's cost line, and its key draws the approval line at about 0.05 chance of default, which is the bar moving up.
- Bank 14 (One correct option, Medium, Wed), folded into Q10: The item is bank 14's leak on the week's real column, duration, which the dataset's own notes say is known only after the call, and its key removes it and reports the honest 0.795.
- Bank 15 (One correct option, Hard, Wed), folded into Q13: The marketing head's second conclusion reads euribor3m's +0.39 as the effect of rates, and the key refuses it because the rate moves with the other indicators, the cause bank 15 asks for, so the sign flips from -0.92 alone and no single weight is the rate's effect.
- Bank 16 (One correct option, Medium, Thu), folded into Q14: The exhibit is bank 16's curve on the room's own tree, training rising to 0.996 while validation falls to 0.837, and the key caps the depth at the validation peak, which is bank 16's prescription.
- Bank 17 (One correct option, Medium, Fri), folded into Q18: The key is bank 17's monitoring rule made concrete on the bank's late rows, the called clients' yes rate against the mean score with a stated gap, and two of its distractors are bank 17's own; the raise adds the step of saying which way the cut on the scores moves.
- Bank 18 (More than one correct, Medium, Mon), folded into Q5: The statement sets the model against the majority-class baseline on the same validation rows, bank 18's options a and c, and its key says why beating the baseline on accuracy alone does not earn a ship, bank 18's option b.
- Bank 19 (More than one correct, Medium, Wed), folded into Q11: The item is bank 19's prediction-time test on the bank's own columns, with the tempting legitimate column, the previous campaign's result, beside the call's duration.
- Bank 20 (More than one correct, Medium, Thu), folded into Q15: The item is bank 20 on the week's two families, a depth cap, a stronger penalty and cross-validation as the brakes, with fitting the training rows harder as the false one.
- Bank 21 (More than one correct, Hard, Fri), folded into Q19: The item is bank 21's four-part memo on the bank's numbers, with the weakest segment and the staleness trigger as the caveat and the validation score and the budget as the lines that belong elsewhere.
- Bank 22 (Scenario set, Easy, Tue), folded into Q6: The working computes precision on the week's real matrix, 174 of the 268 called, which is bank 22's arithmetic on numbers the room ran.
- Bank 23 (Scenario set, Easy, Tue), folded into Q6: The working computes recall on the same matrix, 174 of the 928 buyers, which is bank 23's arithmetic.
- Bank 24 (Scenario set, Medium, Tue), folded into Q8: The working prices two of the week's real thresholds at bank 24's costs, Rs 40 a wasted call and Rs 1,200 a missed buyer, which is bank 24's error bill.
- Bank 25 (Scenario set, Hard, Tue), folded into Q8: The working compares the bill at two thresholds and says which costs less, which is bank 25's question on the week's own thresholds, and sets it against the threshold F1 would choose.
- Bank 26 (Scenario set, Medium, Tue), folded into Q5: The key reads 0.897 accuracy beside 174 of 928 buyers found, which is bank 26's point that an accuracy figure says little about how many buyers were found.
- Bank 27 (Applied maths, Hard, Tue), folded into Q6: The item asks for precision, recall and F1 from one matrix, bank 27's three figures, on the week's real counts.
- Bank 28 (Applied maths, Medium, Tue), folded into Q7: The working states that one caught buyer pays for 30 wasted calls, which is bank 28's answer, and turns it into the threshold.
- Bank 29 (Applied maths, Easy, Thu), folded into Q16: The key states five models fitted on about four-fifths of the training rows each, which is bank 29's count on the week's 24,712 rows.

## The stretch page

- Stretch 1: Approve when (1 minus q) times 5 is below q times 1, where q is the chance of repaying, so q above 5 over 6, about 0.83. Rohan's costs run twenty to one, so his line sits higher, at about 0.95; the ratio of the two error costs sets the line in every business.
- Stretch 2: First the gap must hold on every fold, since one validation slice moves by about 0.03 here. Then count the buyers each model puts in its top 1,000 on the same rows: each extra buyer is worth about Rs 1,200 a campaign, so the extra buyers times Rs 1,200 must beat the yearly cost of explaining, monitoring and re-validating the complex model. Below both bars the logistic model ships, and the memo states the gap that would change the call.
- Stretch 3: For example: whom a bank should call for a term deposit, 41,188 calls with 11 percent yes; doing nothing scores 0.887 accuracy, so I judged the model on recall and the bill; I dropped duration, which leaked, for an honest AUC of 0.795; the top 1,000 by score converted at 0.404 against 0.113. Differently: I would split by date from the start, since the yes rate moved from 6 to 25 percent across the file.

# W5 Curriculum

## Mon 26 Oct 2026 · The modelling loop: frame it, split it, baseline it (ME1 week)

### Trainer agenda

1. Friday's provided score column unmasked: something produced it, and this week builds that something (10 min).
2. When a problem is a machine learning problem, and when a rule or a query wins (40 min).
3. Train, validation and test: the discipline and what each split is for (50 min).
4. Baselines before models: majority class and mean predictor, scored honestly (45 min).
5. Guided then unguided: frame two scenario problems and ship the baseline model (60 min).
6. Kahoot and close-out (20 min).

### Learner outcome

UNDERSTANDS: machine learning fits patterns where rules cannot be written, the test set is spent only once, and a model earns its keep only against a baseline.
CAN DO: frame a problem as prediction with inputs and target named, split the data with a seed, and ship the scored baseline.
CAN HANDLE: a test set peeked at during development, and a problem that looked like ML and was a threshold rule.
CAN DEFEND: why the baseline exists and what beating it proves.

### Subtopics

• Framing: when a problem is ML and when it is a rule
• Inputs, target, prediction time
• Train, validation, test discipline
• Baselines before models
• The baseline model artifact

### Trainer notes

START FROM: the pre-work bridge course carries ML essentials, so weight the room toward doubt-clearing and application rather than first-principles lecturing; probe what the bridge actually landed before assuming it.
GO AS FAR AS: every learner ships a framed problem statement and a scored baseline.
STOP BEFORE: any fitted model beyond the baseline; regression and classification arrive tomorrow.
COMES LATER: features Thursday, generalisation Friday; ME1 closes the week and the exact slot is a Programme Head call.
BREAK TO RUN: the peeked test set: tuning against test lifts the score, the held-back check collapses it, and the room writes the rule (the test set is spent once) themselves.
CUT FIRST: the second framing example. Never cut the baseline or the peek demonstration.
ME1 NOTE: ME1 (50 marks; statistics, data manipulation, analyst techniques, ML core) runs during this week as a continuous activity; the day is not fixed yet, so state the scope aloud and no more.

### Client zero and case studies

TODAY'S DATA: the scenario's feature table from Week 2 plus the outcome column; the modelling target is the outcome the analyst weeks kept describing.
COMPETENCY BUILT: frame and baseline; the discipline that separates a modeller from a library caller.
CASE: none cited; the peek demonstration on the room's own data is the day's evidence.

### In-session exercises

GUIDED: frame the first problem and build the split together, seed stated.
UNGUIDED: frame the second problem and ship its baseline with the honest score, no hints, solution at close.
MID-SESSION (15 min each): sort six problems into ML, rule or query; state what each split is for in one line each.

### After-class tasks

• BUILD: a second baseline (a simple heuristic of your own) and compare it to the majority class.
• WATCH: StatQuest's linear regression main ideas before tomorrow (index link in student references).
• RECAP: 'the test set is spent once' with its reason.

### Trainer resources

• scikit-learn user guide, current docs cover scikit-learn 1.9 (verified 05 Sep 2026):
https://scikit-learn.org/stable/user_guide.html
• StatQuest video index, Statistics Fundamentals and regression entries (verified 05 Sep 2026):
https://statquest.org/video_index.html

### Student references

• StatQuest video index, watch the linear regression main-ideas entry (verified 05 Sep 2026):
https://statquest.org/video_index.html

### Kahoot quiz plan

• Q1: ML, rule or query: five problems called fast
• Q2: which split tunes and which split is spent once
• Q3 trap: validation score rose after peeking at test; what is now broken
• Q4: the baseline for a 90-10 classification is what score
• Q5: inputs must be known at what moment
• Return question from Week 4 Friday, one level up: the threshold that maximised accuracy lost money; say why in one sentence.

## Tue 27 Oct 2026 · Regression and classification: two models, read honestly

### Trainer agenda

1. The baseline's score on screen, and the question: can a fitted line beat it (10 min).
2. Linear regression: fit, coefficients read in units, residuals read for pattern (55 min).
3. Logistic regression: probability out, coefficients as direction and strength (55 min).
4. Where each fails: extrapolation, non-linearity, the residual tells (35 min).
5. Guided then unguided: two models on the scenario, scores against the baseline (55 min).
6. Kahoot and close-out (20 min).

### Learner outcome

UNDERSTANDS: a linear model is readable, which is its superpower, a logistic model outputs probability rather than a verdict, and residual patterns confess what the fit missed.
CAN DO: fit, score and read both models on the scenario, coefficients explained in business units.
CAN HANDLE: a curved relationship a line cannot hold, and a coefficient whose sign surprises because of a correlated feature.
CAN DEFEND: each model's score against the baseline, and one coefficient aloud to a stakeholder.

### Subtopics

• Linear regression: fit, coefficients, residuals
• Logistic regression: probability and direction
• Interpreting coefficients in units
• Residual patterns and where each model fails
• Two models against the baseline

### Trainer notes

START FROM: the bridge course met both models; today's depth is reading them, so spend the minutes on coefficients and residuals rather than fitting mechanics.
GO AS FAR AS: every learner ships both models with one coefficient explained in units and one residual pattern named.
STOP BEFORE: regularisation (Friday), feature engineering (Thursday), any tree.
COMES LATER: Wednesday's metric trap scores the classifier properly; today's accuracy is provisional and say so.
BREAK TO RUN: the planted curved relationship: the line fits, the score looks fine, the residuals bow, and the room reads the confession before any fix is named.
CUT FIRST: the second residual example. Never cut coefficient reading in units.

### Client zero and case studies

TODAY'S DATA: the scenario feature table; the regression target is the amount, the classification target is the outcome, both familiar since Week 1.
COMPETENCY BUILT: read a model rather than worship its score; the interview separator at this level.
CASE: none cited; the bowed residual on the room's own data carries the day.

### In-session exercises

GUIDED: fit the regression together and read two coefficients aloud in Rs.
UNGUIDED: the classifier fitted, scored against baseline, one coefficient explained, no hints, solution at close.
MID-SESSION (15 min each): match four residual plots to their diagnoses; translate three coefficients into stakeholder sentences.

### After-class tasks

• BUILD: refit the regression without the strongest feature and note what the coefficients do.
• RECAP: probability against verdict, one line.
• READ: Wednesday's pre-read naming precision, recall, F1 and the confusion matrix, terms only.

### Trainer resources

• scikit-learn, supervised learning section (verified 05 Sep 2026):
https://scikit-learn.org/stable/supervised_learning.html
• StatQuest video index, the regression and logistic entries (verified 05 Sep 2026):
https://statquest.org/video_index.html

### Student references

• StatQuest video index, the logistic regression entry tonight (verified 05 Sep 2026):
https://statquest.org/video_index.html

### Kahoot quiz plan

• Q1: the coefficient says Rs 240 per unit; finish the stakeholder sentence
• Q2: logistic output 0.71 means what, exactly
• Q3 trap: residuals bow in a curve; what did the model miss
• Q4: which model for 'will they, yes or no' and which for 'how much'
• Q5: a coefficient's sign flipped when a feature was added; likeliest cause
• Return question from Monday, one level up: your model beat the baseline by 0.4 points; is that a result yet, and what would make it one.

## Wed 28 Oct 2026 · The metric trap: accuracy lies on imbalance

### Trainer agenda

1. A 96 percent accurate model that never catches the thing it exists to catch (10 min).
2. The confusion matrix read cell by cell, in business words (45 min).
3. Precision, recall and F1 derived from the matrix; class imbalance and what it does to accuracy (55 min).
4. Choosing the metric from the business cost: Week 4 Friday's costs return on a real model (40 min).
5. Guided then unguided metric justification on the scenario classifier (55 min).
6. Kahoot and close-out (20 min).

### Learner outcome

UNDERSTANDS: the confusion matrix is the whole truth, the headline metrics are ratios of its cells, and the right metric is chosen from the cost of each error rather than habit.
CAN DO: read a matrix in business words, compute the three metrics from it, and justify a metric choice from the scenario's costs.
CAN HANDLE: the imbalanced case where accuracy flatters a useless model, and the stakeholder who asks for one number.
CAN DEFEND: the metric justification memo under the follow-up 'why this metric and what does it hide'.

### Subtopics

• The confusion matrix, cell by cell
• Precision, recall and F1 derived
• Class imbalance against accuracy
• Choosing the metric from business cost
• The metric justification memo

### Trainer notes

START FROM: Week 4 Friday's cost thinking and yesterday's classifier; the room already owns the threshold instinct, so today names the machinery under it.
GO AS FAR AS: every learner ships the metric justification with the matrix attached.
STOP BEFORE: ROC and AUC (name them as later), multi-class.
COMES LATER: Friday's tuning optimises the metric chosen today; Build 2's injected constraint is likely to sit exactly here.
BREAK TO RUN: the wrong-output flagship: the 96 percent model on the 96-4 outcome predicts the majority always; the matrix exposes an empty column and the room re-scores it on recall.
CUT FIRST: F1's harmonic-mean arithmetic (state what it balances). Never cut the empty-column reveal.

### Client zero and case studies

TODAY'S DATA: yesterday's classifier on the scenario's imbalanced outcome, imbalance planted at roughly 96 to 4 so the trap fires on the room's own model.
COMPETENCY BUILT: score a model the way its use will judge it; the single most probed ML interview competency at this band.
CASE: none cited; the empty matrix column on their own model outclasses any anecdote.

### In-session exercises

GUIDED: read the matrix aloud in business words together, then derive the three metrics.
UNGUIDED: the metric justification memo for the scenario's costs, matrix attached, no hints, solution at close.
MID-SESSION (15 min each): compute precision and recall from four matrices fast; pick the metric for three cost stories and defend one.

### After-class tasks

• BUILD: recompute the memo when the miss cost triples; note the metric that takes over.
• RECAP: what accuracy hides, one line.
• READ: Thursday's pre-read naming encoding, scaling and leakage, terms only.

### Trainer resources

• scikit-learn user guide, model evaluation section (verified 05 Sep 2026):
https://scikit-learn.org/stable/user_guide.html
• StatQuest video index, the sensitivity-specificity and confusion matrix entries (verified 05 Sep 2026):
https://statquest.org/video_index.html

### Student references

• StatQuest video index, the confusion matrix entry (verified 05 Sep 2026):
https://statquest.org/video_index.html

### Kahoot quiz plan

• Q1: read the matrix: how many misses
• Q2: compute recall from the four cells shown
• Q3 trap: 96 percent accuracy on a 96-4 outcome; what did it learn
• Q4: fraud screening: which error is dearer and which metric follows
• Q5: F1 balances what two quantities
• Return question from Tuesday, one level up: the residuals bowed; name the fix family without naming a library.

## Thu 29 Oct 2026 · Features: engineering, encoding, scaling, and the leak that hides

### Trainer agenda

1. Two models, same algorithm, one twice as good; the features did it (10 min).
2. Engineering from the scenario: ratios, recency, counts built from what the analyst weeks computed (50 min).
3. Encoding categoricals and scaling numerics, with what each model type cares about (45 min).
4. Leakage: the future dressed as a feature, and the prediction-time test (45 min).
5. Guided then unguided feature-set build, leak hunt included (55 min).
6. Kahoot and close-out (20 min).

### Learner outcome

UNDERSTANDS: features carry the domain into the model, encodings and scales are model-type decisions, and leakage is any input unavailable at prediction time however innocent it looks.
CAN DO: build the feature set from the scenario's tables, encode and scale it, and audit every column with the prediction-time question.
CAN HANDLE: a leaked feature that made the score too good, and an importance chart mistaken for causal truth.
CAN DEFEND: each engineered feature's reason, and the leak audit line by line.

### Subtopics

• Feature engineering from the scenario's own history
• Encoding categoricals; scaling numerics
• Leakage and the prediction-time test
• Feature importance and its limits
• The feature-set artifact

### Trainer notes

START FROM: the Week 2 feature table is the raw material; today engineers on top of it rather than starting fresh, and the continuity is the point.
GO AS FAR AS: every learner ships the audited feature set with each feature's one-line reason.
STOP BEFORE: automated feature selection, embeddings, target encoding.
COMES LATER: Friday tunes on this feature set; the leak instinct returns in every later module.
BREAK TO RUN: the planted leak: a settlement-status field set after the outcome lifts validation to near-perfect; the prediction-time question exposes it and the score falls back to honest.
CUT FIRST: the scaling comparison table (state the rule). Never cut the leak hunt.

### Client zero and case studies

TODAY'S DATA: the Week 2 feature table plus the transactions and events added in Week 4; the planted leak field is in the joined view.
COMPETENCY BUILT: build inputs an interviewer cannot puncture with 'would you know that at prediction time'.
CASE: leakage is the most cited cause of models that excelled offline and failed live; the planted version is run rather than a company cited, since firms rarely publish these postmortems.

### In-session exercises

GUIDED: engineer two features together with their reasons said aloud.
UNGUIDED: complete the feature set, run the leak audit, ship the honest score, no hints, solution at close.
MID-SESSION (15 min each): call leak or clean on six candidate features fast; match encoders to three column types.

### After-class tasks

• BUILD: one more engineered feature from the events table with its reason.
• RECAP: the prediction-time question, verbatim.
• READ: Friday's pre-read naming overfitting, bias-variance and cross-validation, terms only.

### Trainer resources

• scikit-learn user guide, preprocessing section (verified 05 Sep 2026):
https://scikit-learn.org/stable/user_guide.html
• Interview Query, the feature and leakage questions (verified 03 Sep 2026):
https://www.interviewquery.com/p/python-data-science-interview-questions

### Student references

• scikit-learn user guide, skim the preprocessing page headings (verified 05 Sep 2026):
https://scikit-learn.org/stable/user_guide.html

### Kahoot quiz plan

• Q1: the prediction-time question, completed from memory
• Q2 trap: validation hit 0.99 after one new column; first suspicion
• Q3: which encoder for a 40-value categorical
• Q4: which model family shrugs at unscaled features
• Q5: importance charts rank what, and never prove what
• Return question from Wednesday, one level up: the miss cost tripled overnight; which metric now leads and what happens to the threshold.

## Fri 30 Oct 2026 · Generalise or memorise: bias, variance, and the tuned honest model

### Trainer agenda

1. A model at 100 percent on training and 61 on validation; the room names the disease (10 min).
2. Overfitting and bias-variance told through learning curves (50 min).
3. Regularisation as the brake; cross-validation as the honest average (50 min).
4. Applied breadth: trees and clustering used rather than derived, and when the simpler model wins (45 min).
5. Guided then unguided: tune the scenario model, compare against the tree, write the comparison memo (55 min).
6. Kahoot, close-out, and the ME1 window note (20 min).

### Learner outcome

UNDERSTANDS: memorising the training set is failure, the curves show which side of the trade a model sits on, cross-validation averages away split luck, and a simpler model that ties wins.
CAN DO: read learning curves, tune with cross-validation, run the tree comparison, and write the model comparison memo.
CAN HANDLE: an overfit run diagnosed from curves, and a tuned model that fails to beat the simpler one.
CAN DEFEND: the comparison memo's recommendation, including the case where the recommendation is the simpler model.

### Subtopics

• Overfitting; bias and variance through curves
• Regularisation
• Cross-validation
• Trees and clustering, used not derived
• When the simpler model wins
• The tuned model and comparison memo

### Trainer notes

START FROM: the week's model and feature set; every idea today lands on their own artifacts.
GO AS FAR AS: every learner ships the tuned model and the comparison memo with a recommendation.
STOP BEFORE: ensemble internals, boosting mathematics, hyperparameter search frameworks.
COMES LATER: Build 2 next week injects a constraint into exactly this pipeline; ME1 closes this week.
BREAK TO RUN: the overfit flagship: max-depth unlimited hits 100 on train and collapses on validation, and the curves tell it before the score does.
CUT FIRST: clustering (name it, one demo cell). Never cut the curves or the simpler-model comparison.
NOTE: ME1 (statistics, data manipulation, analyst techniques, ML core) closes this week per the plan; the exact slot, duration and run are a Programme Head call and no marks are stated in any artifact.

### Client zero and case studies

TODAY'S DATA: the week's pipeline end to end on the scenario; the comparison memo is the module's closing artifact and Build 2's starting point.
COMPETENCY BUILT: honest evaluation and the courage to recommend the simpler model, which is the exact judgment ME1 and the Build 2 viva reward.
CASE: none cited; the room's own overfit run is the exhibit.

### In-session exercises

GUIDED: read three learning curves together and prescribe for each.
UNGUIDED: tune, cross-validate, compare against the tree, write the memo, no hints, solution at close.
MID-SESSION (15 min each): diagnose four curve pairs fast; pick simpler-or-complex for three score gaps and defend one.

### After-class tasks

• BUILD: rerun the comparison with one feature removed and note the stability.
• RECAP: bias against variance in two lines.
• PREP: tomorrow's block is revision plus the ME1 window; reread the week's five artifacts and the Week 1 and 2 crux lines.

### Trainer resources

• scikit-learn user guide, cross-validation and model selection sections (verified 05 Sep 2026):
https://scikit-learn.org/stable/user_guide.html
• StatQuest video index, the bias-variance and cross-validation entries (verified 05 Sep 2026):
https://statquest.org/video_index.html

### Student references

• StatQuest video index, bias and variance entry tonight (verified 05 Sep 2026):
https://statquest.org/video_index.html

### Kahoot quiz plan

• Q1: train 100, validation 61; name it
• Q2: which curve pair says high bias
• Q3: cross-validation exists to average away what
• Q4 trap: the tuned model beat the tree by 0.2 points and costs 10x to explain; recommend which
• Q5: regularisation trades what for what
• Return question from Thursday, one level up: the leak is removed and the score fell; why is the model now better.

## Sat 31 Oct 2026 · Saturday recap: the pen-and-paper test, then the interview-answer discussion

### Trainer agenda

Four hours, no new content.
1. Weekly recap test: pen and paper, AI-free, built from the week's interview question set, short-answer format (120 min).
2. Break (20 min).
3. Solution discussion led by the Academic TA: papers swapped for peer cross-evaluation, every answer discussed as an interview answer, random call-outs throughout (75 min).
4. Doubt clearing and the bridge: Build 2 opens Monday with the constraint written into the brief (25 min).

### Learner outcome

CAN DO: answer the week's interview set on paper, without an assistant, in short-answer form.
CAN DEFEND: any of those answers aloud when called, and mark a peer's paper against the discussed solution.
STATUS: ungraded; the score is a performance indicator the programme reads, never a marks component.

### Subtopics

THE QUESTION SET (questions only; answers are built at the detailing phase):
• [S] Overfitting: what it is, how you detect it, how you fix it.
• [S] Bias against variance in plain words.
• [S] Precision, recall and F1 from a confusion matrix.
• [F] What is data leakage, and how do you catch it before it ships?
• [S] Train, validation and test: what is each for, and which is spent once?
• [F] Accuracy is 96 percent on a 96-4 split: good model?
• [F] Why cross-validation instead of one split?
• [D] Your tuned model beats a simpler one by a hair: which ships, and why?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. The tagging is this programme's own calibration for 0-3 year Indian-market candidates.

### Trainer notes

FORMAT: the paper is built from this row's question set, framed for short answers (selection, one-liners, small computations) so peer cross-checking works; answers themselves are written at the detailing phase, never improvised on the day.
DISCUSSION: papers swap for peer cross-evaluation; the Academic TA leads the solution walk-through as an interview-answer discussion, with random call-outs throughout.
STATUS: ungraded, a performance indicator rather than a marks component, and AI-free by format.
ME1 NOTE: ME1 (50 marks) runs during this week as a continuous activity with no fixed day yet; whether the ungraded recap test also runs in a major-exam week is a Programme Head call.

### Client zero and case studies

Answers must cite the scenario's own numbers and artifacts where the week produced them; the module's pipeline end to end is the reference.

### In-session exercises

• The two-hour recap test on paper.
• Peer cross-evaluation against the discussed solution.
• Random call-outs: the called learner answers aloud in sixty seconds.

### After-class tasks

• RECAP: rewrite any question you lost marks on, one line each, in your own words.

### Trainer resources

• This row's question set is the paper's source; the verified interview banks on the weekday rows calibrate difficulty.
• GeeksforGeeks, Data Analyst interview questions (verified 03 Sep 2026):
https://www.geeksforgeeks.org/data-analysis/data-analyst-interview-questions-and-answers/

### Student references

• Reread the week's tabs and your own rejected answers; the next paper reuses missed ground one level up.

### Kahoot quiz plan

None. The recap test and the discussion replace the quiz today.

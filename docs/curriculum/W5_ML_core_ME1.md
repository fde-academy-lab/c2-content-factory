# W5 ML core + ME1

## Mon 26 Oct 2026 · Regression and classification · Framing the propensity model, and the baseline it has to beat

### Business scenario of the day

The growth plan is approved: fix frequency, bundle the pairs that lift it, repair the funnel stage. Marketing now has a budget to nudge members with a small discount and one question: "Which members do we nudge? Nudging everyone costs Rs 40 each and annoys the ones who were going to buy anyway. Give us a score per customer for how likely they are to buy again in the next ninety days."
The senior analyst adds the condition that runs all week: "Before you show me any model, show me the dumbest possible baseline and what beating it would prove."
Your role: you frame the problem, choose what the model predicts, and defend the baseline against a marketing team that wants a score by Friday.
On the table: when a business question is a prediction problem and when a rule is enough; what exactly is being predicted, from what, known when; how the data is split so the score means something; what a baseline is and why a model that only ties it should not ship.

### Thinking we train, before any tool

A prediction problem has an input known at prediction time, a target known later, and a decision that changes with the prediction. Marketing's ask has all three: the customer table on the day of the nudge, repeat purchase within ninety days, and whom to nudge. Two model families answer two shapes of question: regression for 'how much' (next-quarter spend), classification for 'will they' (repeat or not).
The split discipline is the Trust thread in machine learning: train on some customers, tune on others, and spend the test set once. The baseline is the majority class or the mean, scored honestly, and a model earns its keep only against it. Coefficients are read in business units, and residual patterns confess what the fit missed.

### Trainer agenda

1. Marketing's ask and the senior analyst's condition; the room sorts five Kalpa questions into prediction, rule, or query (15 min).
2. Framing: input, target, prediction time; the ninety-day repeat flag defined on the customer table (35 min).
3. Train, validation, test; the baseline scored; what beating it proves (40 min).
4. Linear regression on next-quarter spend: fit, coefficients in rupees, residuals (45 min).
5. Logistic regression on the repeat flag: probability out, direction and strength (45 min).
6. Unguided: both models against their baselines, one coefficient explained to Marketing (40 min).
7. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: a prediction problem needs input, target and decision; the test set is spent once; a model earns its keep against a baseline; a linear model is readable and a logistic model outputs probability.
CAN DO: frame the propensity problem, define the target, split with a seed, score the baseline, fit and read both models.
CAN HANDLE: a test set peeked at, a curved relationship a line cannot hold, a coefficient whose sign surprises, and a model that only ties the baseline.
CAN DEFEND: why the baseline exists, what the ninety-day target means, and one coefficient in Marketing's language.

### Subtopics (technique in service of the scenario)

• Prediction, rule or query: when a business question is a modelling problem
• Input, target, prediction time; the repeat-purchase target
• Train, validation, test; the seed; the baseline
• Linear regression: fit, coefficients in units, residuals
• Logistic regression: probability, direction, strength
• Where each model fails; the residual tells

### Trainer notes

START FROM: the Week 2 customer table with the Week 4 cohort and basket features; the pre-work bridge course met both model families, so spend the minutes on framing and reading, not on fitting mechanics.
GO AS FAR AS: everyone ships a framed problem, a scored baseline, and both models with one coefficient explained.
STOP BEFORE: any metric beyond accuracy (Tuesday), feature engineering (Wednesday), regularisation (Thursday), trees.
COMES LATER: Tuesday's metric trap exposes today's accuracy; ME1 runs this week as a continuous activity, day not fixed, state the scope aloud and no more.
WHAT THE DATA REVEALS: the peeked test set lifts the score and the held-back check collapses it; the planted curve bows the residuals; the classifier's 96 percent accuracy is provisional and Tuesday explains why.
CUT FIRST: the second framing example. Never cut the baseline or the peek demonstration.

### Client zero data (TRAINER ONLY)

VERSION v6: the customer feature table with the ninety-day repeat flag as target at roughly 96 to 4, and next-quarter spend as the regression target.
PLANTED: a curved relationship between recency and spend so residuals bow; a test-set peek staged in the demo.
The 96 to 4 imbalance is the trap Tuesday springs; today it is simply the accuracy the room believes.

### In-session exercises

GUIDED: frame the problem and build the split together, seed stated; score the baseline.
UNGUIDED: fit both models, score against baselines, explain one coefficient in rupees for Marketing.
MID-SESSION (15 min each): sort six Kalpa questions into prediction, rule or query; match four residual plots to their diagnoses.

### After-class tasks

• BUILD: a second baseline of your own (a simple rule) and whether it beats the majority class.
• WATCH: StatQuest, linear regression main ideas and logistic regression, from the index.
• RECAP: 'the test set is spent once' with its reason.

### Interview angle

• [S] When is a business problem a machine learning problem?
• [S] Train, validation, test: what is each for, and which is spent once?
• [F] What does a logistic output of 0.71 mean?
• [F] Why start with a baseline, and what does beating it prove?
• [D] Marketing wants the score by Friday and your model only ties the baseline; what do you tell them?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• scikit-learn user guide, current docs cover scikit-learn 1.9 (verified 05 Sep 2026):
https://scikit-learn.org/stable/user_guide.html
• scikit-learn, supervised learning section (verified 05 Sep 2026):
https://scikit-learn.org/stable/supervised_learning.html
• StatQuest video index, regression and logistic entries (verified 05 Sep 2026):
https://statquest.org/video_index.html

### Student references

• StatQuest video index, linear regression main ideas and logistic regression (verified 05 Sep 2026):
https://statquest.org/video_index.html

### Kahoot quiz plan

• Q1: prediction, rule or query: five Kalpa questions called fast
• Q2: which split tunes, which is spent once
• Q3 trap: validation rose after peeking at test; what is now broken
• Q4: the baseline for a 96 to 4 classification scores what
• Q5: the coefficient says Rs 240 per unit of recency; finish the sentence for Marketing
• Return question from Week 4 Friday: the vendor curve fit the last two years perfectly; is it a good forecast.

## Tue 27 Oct 2026 · The metric trap · Scoring the model the way the business will judge it, in two businesses

### Business scenario of the day

Marketing is delighted: the classifier is 96 percent accurate. Then the senior analyst asks how many repeat buyers it actually found. The answer is none; the model predicts 'no' for everyone and is right 96 percent of the time.
Anand attaches the costs: a wasted nudge is Rs 40; a missed repeat buyer is about Rs 1,200 of margin. Marketing wants to nudge widely; Finance wants to nudge nobody it is unsure of.
The parallel case, from Kalpa Financial Services: Rohan Desai, head of risk, hears about the model and asks whether the same approach could score loan applicants, where approving a defaulter costs Rs 60,000 and rejecting a good borrower costs Rs 3,000 of lost interest.
Your role: you pick the metric and set the threshold for Kalpa Retail, and explain to Rohan why the same machinery gives a very different threshold in his business.
On the table: what accuracy hides on an imbalanced outcome; how the confusion matrix reads in business words; which metric follows from which error cost; where the threshold sits when a miss costs thirty times a false alarm, and where it sits when the ratio flips.

### Thinking we train, before any tool

The confusion matrix is the whole truth; accuracy, precision, recall and F1 are ratios of its cells. On a 96 to 4 outcome, accuracy rewards the model that never acts. The metric is chosen from the cost of each error, never from habit: when a miss costs thirty times a false alarm, recall leads and the threshold drops; when a false approval costs twenty times a wrongful rejection, precision leads and the threshold rises.
The 1-in-N test, this course's construction: rights per wrong equals damage over saving, and that ratio sets the bar the model must clear before acting. Same machinery, two businesses, opposite thresholds, which is why an interviewer asks it as a case.

### Trainer agenda

1. The 96 percent model that found nobody; the empty matrix column (15 min).
2. The confusion matrix read cell by cell in Kalpa's words; precision, recall, F1 derived (50 min).
3. Choosing the metric from the error costs; the 1-in-N test; the threshold for the nudge (45 min).
4. The transfer: Rohan's loan applicants, the costs flipped, the threshold that follows (35 min).
5. Guided then unguided: the metric justification memo for Kalpa Retail, and the one-paragraph transfer note for Kalpa Financial (55 min).
6. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: the matrix is the truth; accuracy flatters on imbalance; the metric follows the cost of each error; the threshold is a business decision that moves with the costs.
CAN DO: read a matrix in business words, compute the three metrics, pick the metric from costs, set the threshold with the 1-in-N test, and re-derive it for a second business.
CAN HANDLE: the 96 percent model that found nobody, a stakeholder who asks for one number, and a business where the costs run the other way.
CAN DEFEND: the metric memo under 'why this metric and what does it hide', and the transfer note under 'why is Rohan's threshold so different'.

### Subtopics (technique in service of the scenario)

• The confusion matrix, cell by cell
• Precision, recall and F1 derived
• Class imbalance against accuracy
• Choosing the metric from business cost; the 1-in-N test (course construction)
• Threshold selection as a business decision
• The transfer: the same model, a lending business, the opposite threshold

### Trainer notes

START FROM: Monday's classifier and the Week 4 cost thinking; the room already owns the threshold instinct.
GO AS FAR AS: everyone ships the metric memo with the matrix attached and the Kalpa Financial transfer note.
STOP BEFORE: ROC and AUC (name them), multi-class, cost-sensitive learning as a method.
COMES LATER: Thursday optimises the metric chosen today; Build 2 in Kalpa Financial Services injects exactly this constraint.
WHAT THE DATA REVEALS: the empty column; recall near zero; at the 1-in-N bar the threshold falls to 0.12 for the nudge and rises to 0.85 for the loan. Let the room derive both.
CUT FIRST: F1's harmonic-mean arithmetic. Never cut the empty-column reveal or the transfer.

### Client zero data (TRAINER ONLY)

VERSION v6: Monday's classifier on the 96 to 4 repeat flag; a small Kalpa Financial Services applicant table with default flags for the transfer.
PLANTED: the majority-class classifier; the two cost structures that push the thresholds to opposite ends.
Rohan Desai enters the story here and returns as Build 2's stakeholder.

### In-session exercises

GUIDED: read the matrix aloud in Kalpa's words, derive the three metrics, set the nudge threshold from Anand's costs.
UNGUIDED: the metric memo, then re-derive the threshold for Rohan's costs and write the transfer note.
MID-SESSION (15 min each): compute precision and recall from four matrices fast; pick the metric for three cost stories and defend one.

### After-class tasks

• BUILD: recompute the nudge threshold when the miss cost halves; note which metric takes over.
• RECAP: what accuracy hides, one line.
• READ: Wednesday's pre-read naming encoding, scaling and leakage, terms only.

### Interview angle

• [S] Precision, recall and F1 from a confusion matrix.
• [S] Accuracy is 96 percent on a 96 to 4 split; good model?
• [S] Precision or recall for fraud, and why?
• [F] How do you set a threshold when the two errors cost differently?
• [D] The same model in retail and in lending: why are the thresholds opposite, and how do you explain that to each business?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• scikit-learn user guide, model evaluation section (verified 05 Sep 2026):
https://scikit-learn.org/stable/user_guide.html
• StatQuest video index, sensitivity, specificity and the confusion matrix entries (verified 05 Sep 2026):
https://statquest.org/video_index.html
• Interview Query, analyst and data science case questions on thresholds (verified 03 Sep 2026):
https://www.interviewquery.com/p/python-data-science-interview-questions

### Student references

• StatQuest video index, the confusion matrix entry (verified 05 Sep 2026):
https://statquest.org/video_index.html

### Kahoot quiz plan

• Q1: read the matrix: how many repeat buyers were found
• Q2: compute recall from the four cells shown
• Q3 trap: 96 percent accuracy on a 96 to 4 outcome; what did it learn
• Q4: a miss costs Rs 1,200 and a false nudge Rs 40; which metric leads and roughly where is the threshold
• Q5: a false approval costs Rs 60,000 and a wrongful rejection Rs 3,000; which way does the threshold move
• Return question from Monday: your model only tied the baseline; what do you tell Marketing.

## Wed 28 Oct 2026 · Feature engineering and leakage · What the model is allowed to know

### Business scenario of the day

A junior on the team finds a feature that lifts validation to 0.99: settlement_status from the payments feed. Marketing wants it shipped tonight. The data platform lead, reading the schema, mentions that settlement_status is written after delivery, when the payment clears.
Meanwhile the Week 2 customer table offers recency, frequency and monetary; Week 4 added cohort and basket signals; the senior analyst wants each one justified.
Your role: you decide what goes into the model and what is thrown out, and you will be asked about every column, including the one that made the junior's score.
On the table: what a feature is and why the domain lives in it; how a categorical and a number are made usable; what leakage is and the one question that catches it; what importance charts prove and what they do not.

### Thinking we train, before any tool

Features carry the domain into the model: recency, frequency and monetary from Week 2, cohort age and basket signals from Week 4, engineered as ratios and counts the business would recognise. Encoding and scaling are model-type decisions, not rituals.
Leakage is any input unavailable at prediction time, however innocent it looks. The prediction-time question catches it: on the morning of the nudge, do we know this? settlement_status fails it, and the 0.99 collapses to honest. Importance charts rank contribution; they never prove cause.

### Trainer agenda

1. The 0.99 feature and the platform lead's remark; the room predicts what happens to the score (10 min).
2. Engineering from the customer table: ratios, recency, counts, cohort age, basket signals, each with its business reason (55 min).
3. Encoding categoricals and scaling numerics; what each model type cares about (40 min).
4. Leakage: the prediction-time question; the audit of every column; the leak removed and the honest score (45 min).
5. Guided then unguided: the feature set with a reason per feature and the leak audit (50 min).
6. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: features carry the domain; encoding and scaling are decisions; leakage is anything unavailable at prediction time; importance ranks without proving.
CAN DO: engineer features from the customer table with reasons, encode and scale, audit every column with the prediction-time question, and ship the honest score.
CAN HANDLE: a leaked feature that made the score too good, an importance chart read as causation, and a stakeholder who wants the 0.99 shipped.
CAN DEFEND: every feature's reason, and why the score fell and the model got better.

### Subtopics (technique in service of the scenario)

• Feature engineering from the customer table: ratios, recency, counts, cohort age, basket signals
• Encoding categoricals; scaling numerics; which models care
• Leakage and the prediction-time question
• The column audit
• Feature importance and its limits

### Trainer notes

START FROM: the Week 2 customer table plus Week 4's additions; today engineers on top of it, and the continuity is the point.
GO AS FAR AS: everyone ships the audited feature set with a reason per feature and the honest score.
STOP BEFORE: automated selection, target encoding, embeddings.
COMES LATER: Thursday tunes on this feature set; the leak question returns in every later module.
WHAT THE DATA REVEALS: settlement_status lifts validation to 0.99 and fails the prediction-time question; two correlated features flip a coefficient sign when both are included. Let the room find both.
CUT FIRST: the scaling comparison table. Never cut the leak audit.

### Client zero data (TRAINER ONLY)

VERSION v6: the customer feature table with the payments-derived columns joined.
PLANTED: settlement_status set after the outcome; two correlated features (visits and searches) that flip a sign together.
Leakage is the most cited cause of models that excelled offline and failed live; the planted version is run rather than a company cited.

### In-session exercises

GUIDED: engineer two features together with reasons said aloud; run the prediction-time question on three columns.
UNGUIDED: the full feature set, the leak audit, the honest score.
MID-SESSION (15 min each): call leak or clean on six candidate features fast; match encoders to three column types.

### After-class tasks

• BUILD: one more feature from the events table with its reason.
• RECAP: the prediction-time question, verbatim.
• READ: Thursday's pre-read naming overfitting, bias, variance and cross-validation, terms only.

### Interview angle

• [S] What is data leakage, and how do you catch it before it ships?
• [F] Which encoder for a forty-value categorical, and why?
• [F] What does a feature importance chart prove, and what does it not?
• [D] A colleague's feature lifts the score to 0.99 and the team wants it shipped tonight; what do you say, and how do you prove it?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

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
• Q3: which encoder for a forty-value categorical
• Q4: which model family shrugs at unscaled features
• Q5: a coefficient's sign flipped when a feature was added; likeliest cause
• Return question from Tuesday: the same model in retail and lending; why the thresholds are opposite.

## Thu 29 Oct 2026 · Overfitting and regularisation · Generalise or memorise, and the honest tuned model

### Business scenario of the day

The team tries a decision tree with no depth limit. Training score: 100 percent. Validation: 61. Marketing sees the first number. The senior analyst sees both and asks for the learning curves.
Anand's constraint arrives the same morning: the nudge budget covers one campaign; a model that works on last quarter's customers and fails on next quarter's costs the whole budget.
Your role: you diagnose the run, apply the brakes, and choose between a tuned complex model and a simpler one that nearly ties it, with the reason stated for a room that will remember the 100 percent.
On the table: what memorising the training set looks like from outside; how curves show which side of the trade a model sits on; what regularisation and cross-validation each buy; when the simpler model is the right recommendation.

### Thinking we train, before any tool

Memorising the training set is failure dressed as success, and learning curves show it before the score does: training climbs, validation stalls or falls. Bias and variance are the two ways to be wrong, and regularisation is the brake on the second. Cross-validation averages away split luck so a score is about the model rather than the draw.
A simpler model that ties a complex one wins, because it costs less to explain, maintain and trust. That sentence is the recommendation the room will resist and the interviewer will reward.

### Trainer agenda

1. The tree at 100 and 61; the room names the disease (10 min).
2. Overfitting and bias-variance through learning curves (50 min).
3. Regularisation as the brake; cross-validation as the honest average (50 min).
4. Trees, ensembles and clustering used against a baseline, at recognition depth (35 min).
5. Guided then unguided: tune the propensity model with cross-validation, compare against the tree and the simple model (55 min).
6. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: memorising is failure; curves diagnose the trade; regularisation brakes variance; cross-validation removes split luck; a simpler model that ties wins.
CAN DO: read learning curves, tune with cross-validation, apply regularisation, and run the three-way comparison.
CAN HANDLE: an overfit run diagnosed from curves, a tuned model that fails to beat the simpler one, and a stakeholder anchored on the training score.
CAN DEFEND: which model to ship and why, including the case where the answer is the simpler one.

### Subtopics (technique in service of the scenario)

• Overfitting; bias and variance through learning curves
• Regularisation
• Cross-validation
• Trees, ensembles, clustering: used, compared, not derived
• When the simpler model wins

### Trainer notes

START FROM: Wednesday's honest feature set; every idea today lands on the room's own model.
GO AS FAR AS: everyone ships the tuned model and the three-way comparison with a provisional recommendation.
STOP BEFORE: ensemble internals, boosting mathematics, hyperparameter search frameworks.
COMES LATER: Friday writes the justification; Build 2 injects a constraint into this pipeline.
WHAT THE DATA REVEALS: max-depth unlimited hits 100 on train and collapses on validation; the regularised logistic model ties the tuned tree within a point. Let the curves tell it.
CUT FIRST: clustering (one demo cell). Never cut the curves or the simpler-model comparison.

### Client zero data (TRAINER ONLY)

VERSION v6: the audited feature set from Wednesday.
PLANTED: the unlimited-depth tree; the near-tie between the regularised logistic model and the tuned tree.
The near-tie is the setup for Friday's recommendation.

### In-session exercises

GUIDED: read three learning curves and prescribe for each; run one cross-validation together.
UNGUIDED: tune, cross-validate, compare tree against logistic against baseline, state a provisional recommendation.
MID-SESSION (15 min each): diagnose four curve pairs fast; pick simpler-or-complex for three score gaps and defend one.

### After-class tasks

• BUILD: rerun the comparison with one feature removed and note the stability.
• RECAP: bias against variance in two lines.
• PREP: Friday is the justification; reread Tuesday's metric memo.

### Interview angle

• [S] Overfitting: what it is, how you detect it, how you fix it.
• [S] Bias against variance in plain words.
• [F] Why cross-validation instead of one split?
• [D] Your tuned model beats a simpler one by a point and costs ten times more to explain; which ships, and how do you say it to a team that saw the 100 percent?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• scikit-learn user guide, cross-validation and model selection sections (verified 05 Sep 2026):
https://scikit-learn.org/stable/user_guide.html
• StatQuest video index, bias-variance and cross-validation entries (verified 05 Sep 2026):
https://statquest.org/video_index.html

### Student references

• StatQuest video index, the bias and variance entry (verified 05 Sep 2026):
https://statquest.org/video_index.html

### Kahoot quiz plan

• Q1: train 100, validation 61; name it
• Q2: which curve pair says high bias
• Q3: cross-validation exists to average away what
• Q4 trap: the tuned tree beat logistic by 0.4 points; recommend which
• Q5: regularisation trades what for what
• Return question from Wednesday: the leak is removed and the score fell; why is the model now better.

## Fri 30 Oct 2026 · Model justification · The committee memo, and what transfers to Kalpa Financial

### Business scenario of the day

The steering committee meets Monday: Meera, Anand, the marketing lead, and Rohan from Kalpa Financial, who is watching for his own business. Meera's brief: "Which model, why that one, what it will cost us when it is wrong, how we will know it is going stale, and what you would need to run it for Rohan instead."
Your role: you write and defend the model justification, and every person in that room has a reason to push: Marketing wants the higher score, Finance wants the smaller error bill, Rohan wants to know what transfers.
On the table: how a model choice is written so a non-technical committee can approve it; what 'wrong' costs in rupees under the chosen threshold; how staleness is detected; what changes and what stays when the same pipeline moves to lending.

### Thinking we train, before any tool

A justification is the four-part note from Week 1 at model scale: the claim (this model, this threshold), the evidence (validation metric against baseline, cross-validated, error cost in rupees), the caveat (what would make it stale, which segment it is weakest on), and the action (the campaign, its budget, the monitoring rule). The simpler model is recommended when it ties, and the memo says why out loud.
The transfer paragraph is the week's interview move: the same pipeline, Rohan's costs, the opposite threshold, and the one feature that would leak in lending.

### Trainer agenda

1. Meera's brief; the room lists what each committee member will push on (15 min).
2. The justification structure: claim, evidence, caveat, action, at model scale (40 min).
3. Error cost in rupees under the threshold; the staleness rule; the weakest segment (45 min).
4. The transfer paragraph for Rohan: what changes, what stays, what would leak (35 min).
5. Guided then unguided: the committee memo, read aloud and challenged in pairs (65 min).
6. Kahoot, close, ME1 scope stated (20 min).

### Learner outcome

UNDERSTANDS: a model choice is justified in the four-part shape; the error bill is computed, not implied; staleness needs a rule; a transfer names what changes.
CAN DO: write the committee memo with the error bill and the monitoring rule, and the transfer paragraph for lending.
CAN HANDLE: a marketing lead who wants the higher score, a CFO who wants a smaller error bill, and a risk head asking what carries over.
CAN DEFEND: the memo aloud under challenge from each of them; the module's interview anchor.

### Subtopics (technique in service of the scenario)

• The model justification: claim, evidence, caveat, action
• The error bill in rupees under the chosen threshold
• Staleness: the monitoring rule and the weakest segment
• The transfer paragraph: what changes, what stays, what would leak
• Reading the memo aloud under challenge

### Trainer notes

START FROM: the week's models, memo and comparison; today integrates.
GO AS FAR AS: everyone ships the committee memo and defends it in a pair challenge.
STOP BEFORE: drift detection methods, retraining pipelines; name them as Weeks 14 and beyond.
COMES LATER: Build 2 next week is Rohan's business with the constraint written into the brief.
WHAT THE DATA REVEALS: the near-tie makes the simpler model the honest recommendation; the weakest segment is Student, for the sample-size reason from Week 1.
NOTE: ME1 (50 marks; statistics, data manipulation, analyst technique, ML core) runs this week as a continuous activity; the day is not fixed; state scope aloud and no more.
CUT FIRST: the staleness rule's arithmetic. Never cut the read-aloud challenge.

### Client zero data (TRAINER ONLY)

VERSION v6: the week's pipeline end to end.
PLANTED: nothing new; the near-tie and the Student weakness carry the day.
The memo is the module's closing artifact and Build 2's starting point.

### In-session exercises

GUIDED: the claim and evidence sections written together, error bill computed.
UNGUIDED: caveat, action, monitoring rule, transfer paragraph; then pairs challenge each other as the committee.
MID-SESSION (15 min each): compute the error bill for two thresholds; write the staleness rule in one sentence.

### After-class tasks

• WRITE: the memo, final, under 300 words.
• RECAP: the three questions Rohan would ask, and your answers.
• PREP: Saturday is revision and the ME1 window; reread the week's five artifacts.

### Interview angle

• [S] Walk me through a model you built and why you chose it.
• [F] How would you know your model has gone stale?
• [F] What would change if this model moved to a lending business?
• [D] The committee wants the higher-scoring model and you are recommending the simpler one; make the case in ninety seconds.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• scikit-learn user guide, model selection and evaluation (verified 05 Sep 2026):
https://scikit-learn.org/stable/user_guide.html
• Interview Query, ML case questions on model choice (verified 03 Sep 2026):
https://www.interviewquery.com/p/python-data-science-interview-questions

### Student references

• StatQuest video index, revisit any entry that felt shaky (verified 05 Sep 2026):
https://statquest.org/video_index.html

### Kahoot quiz plan

• Q1: the four parts of a model justification
• Q2: the error bill under the chosen threshold is computed from which two numbers
• Q3: staleness rule in one sentence
• Q4: which feature would leak in the lending version, and why
• Q5 trap: the committee wants the 0.4-point winner; your one-line answer
• Return question from Thursday: train 100, validation 61; name it and prescribe.

## Sat 31 Oct 2026 · Saturday · Revision, the recap test, and the ME1 window

### Business scenario of the day

Revision and the ME1 window. ME1 covers statistics, data manipulation, analyst technique and the ML core; the exact slot is a Programme Head call. The remaining hours are the week's recap paper and the interview-answer discussion.

### Thinking we train, before any tool

Saying the module out loud is the interview skill itself.

### Trainer agenda

Four hours.
1. ME1 window, reserved without stating marks or slot (up to half the block).
2. Recap test from the week's question set, pen and paper, AI-free (60 min).
3. Solution discussion led by the Academic TA: papers swapped, answers as interview answers, random call-outs (45 min).
4. Build 2 preview: Rohan's business, the constraint written in (15 min).

### Learner outcome

CAN DEFEND: the module's pipeline end to end under questioning.
STATUS: the recap is ungraded; ME1 is graded and its marks are stated nowhere here.

### Subtopics (technique in service of the scenario)

THE QUESTION SET (questions only; answers built at detailing):
• [S] Overfitting: what it is, how you detect it, how you fix it.
• [S] Precision, recall and F1 from a confusion matrix.
• [S] What is data leakage, and how do you catch it?
• [S] Train, validation, test: which is spent once?
• [F] Accuracy is 96 percent on a 96 to 4 split; good model?
• [F] Why cross-validation instead of one split?
• [F] Precision or recall for fraud, and why?
• [D] Your tuned model beats a simpler one by a hair: which ships, and why?
• [D] The same model in retail and lending: why are the thresholds opposite?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer notes

SCOPE: say ME1's four theme areas aloud and nothing about marks or weights, which remain pending.
FORMAT: the paper comes from this row's question set; the Academic TA leads; random call-outs.

### Client zero data (TRAINER ONLY)

Revision answers cite the scenario's own artifacts; the exam themes match what the spine already carried.

### In-session exercises

• The recap test.
• Peer cross-evaluation and call-outs.

### After-class tasks

• REST: Build 2 opens Monday; the briefs ship when they lock.

### Interview angle

The question set in Subtopics is the interview set for the week.

### Trainer resources

• The Week 4 and 5 Kahoot columns are the question bank.
• Interview Query, ML questions for the technical half (verified 03 Sep 2026):
https://www.interviewquery.com/p/python-data-science-interview-questions

### Student references

• StatQuest video index, revisit any entry that felt shaky (verified 05 Sep 2026):
https://statquest.org/video_index.html

### Kahoot quiz plan

None. Revision and the recap replace the quiz.

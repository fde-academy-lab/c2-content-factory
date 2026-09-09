# W4 Curriculum

## Mon 19 Oct 2026 · Metrics that cannot be gamed: north-star, guardrail, leading and lagging

### Trainer agenda

1. A metric that improved while the business worsened, on screen (10 min).
2. What to measure and why: the metric as a decision instrument (40 min).
3. North-star against guardrail; leading against lagging, on the scenario's own numbers (50 min).
4. Gaming: how a target bends behaviour, and definitions that resist it (45 min).
5. Guided then unguided: write the metric definition artifact for two scenario questions (60 min).
6. Kahoot and close-out (20 min).

### Learner outcome

UNDERSTANDS: a metric is a decision instrument, a north-star needs guardrails, leading indicators move before lagging ones, and any target bends behaviour toward itself.
CAN DO: define a metric with its formula, denominator, guardrail and gaming note, on the scenario's data.
CAN HANDLE: a metric that improves while the outcome worsens, and a proxy that drifted from the thing it proxied.
CAN DEFEND: the metric definition artifact line by line, including what it deliberately does not reward.

### Subtopics

• What to measure and why
• North-star and guardrail metrics
• Leading against lagging indicators
• Defining a metric so it cannot be gamed
• The metric definition artifact

### Trainer notes

START FROM: they can compute any rate or summary the definition needs (Weeks 1 and 2); today is judgment, never computation.
GO AS FAR AS: every learner ships two metric definitions with guardrails and a gaming note.
STOP BEFORE: basket analysis, cohorts, forecasting; each has its own day.
COMES LATER: Wednesday's lift, Thursday's cohorts and Friday's thresholds all consume metrics defined the way today teaches.
BREAK TO RUN: a wrong-output demonstration: the planted support metric (tickets closed per hour) improves for three straight weeks while resolution quality collapses; the room finds the gap between the metric and the mission.
CUT FIRST: the second unguided definition. Never cut the gaming demonstration.
NOTE: Dussehra falls tomorrow (gazetted holiday), so tonight ships Wednesday's pre-read and no session runs Tuesday.

### Client zero and case studies

TODAY'S DATA: the scenario's cleaned tables from Week 2; the metric definitions are written for the scenario's two standing business questions.
COMPETENCY BUILT: define before measuring; the analyst habit interviewers probe with 'how would you measure X'.
CASE: Wells Fargo, 2016. Cross-selling targets drove staff to open millions of unauthorised accounts; the metric hit its number while destroying the thing it was meant to grow. The canonical gamed-metric case, publicly documented.

### In-session exercises

GUIDED: define the first metric together: formula, denominator, guardrail, gaming note.
UNGUIDED: the second definition solo, then swap and attack a partner's definition for gameability, no hints, solution at close.
MID-SESSION (15 min each): classify eight metrics as leading or lagging and defend two; name the guardrail for three given north-stars.

### After-class tasks

• BUILD: one metric definition for a domain you know personally, with its gaming note.
• READ: Wednesday's pre-read on basket vocabulary (support, confidence, lift), terms only.
• RECAP: one markdown line on why a guardrail exists.

### Trainer resources

• GeeksforGeeks, Data Analyst interview questions, the metric and KPI items (verified 03 Sep 2026):
https://www.geeksforgeeks.org/data-analysis/data-analyst-interview-questions-and-answers/
• Interview Query, product and statistics questions for analyst screens (verified 03 Sep 2026):
https://www.interviewquery.com/p/python-data-science-interview-questions

### Student references

• GeeksforGeeks, Data Analyst interview questions, attempt the metric items cold (verified 03 Sep 2026):
https://www.geeksforgeeks.org/data-analysis/data-analyst-interview-questions-and-answers/

### Kahoot quiz plan

• Q1: north-star against guardrail, one job each
• Q2: leading or lagging: five metrics called out fast
• Q3 trap: the metric rose and the business fell; name the failure in one word
• Q4: every rate's definition must name what two things
• Q5: the proxy test: what question exposes a drifted proxy
• Return question from Week 2, one level up: the stakeholder wants weekly numbers they can poke themselves; which tool and why.

## Tue 20 Oct 2026 · Dussehra (Vijaya Dashami): gazetted holiday, no session

### Trainer agenda

No session. Dussehra falls on Tuesday 20 October 2026 per the gazetted holiday list; the institute is closed.

### Learner outcome

No new outcomes.

### Subtopics

None scheduled.

### Trainer notes

Nothing to deliver. Wednesday resumes on basket analysis; its pre-read shipped Monday night.

### Client zero and case studies

The scenario rests.

### In-session exercises

None scheduled.

### After-class tasks

• OPTIONAL: finish Monday's personal-domain metric definition.

### Trainer resources

None needed.

### Student references

None assigned.

### Kahoot quiz plan

None.

## Wed 21 Oct 2026 · Basket analysis: support, confidence, lift, and the cross-sell that actually pays

### Trainer agenda

1. Two product pairs on screen: one obvious, one surprising; which recommendation makes money (10 min).
2. Support, confidence and lift derived by counting on twelve hand-checkable baskets (60 min).
3. The confidence trap: high confidence, lift below one, on the planted popular item (35 min).
4. Cross-sell and upsell reasoning: from a lift table to a recommendation with a number (45 min).
5. Guided then unguided basket analysis on the scenario's transactions (60 min).
6. Kahoot and close-out (20 min).

### Learner outcome

UNDERSTANDS: support says how often, confidence says how reliably, and lift says whether the association beats chance, which is the only one of the three that cannot be fooled by popularity.
CAN DO: compute all three by hand on small baskets and in code on the scenario's transactions, and turn a lift table into one costed recommendation.
CAN HANDLE: a high-confidence pair with lift below one, and a high-lift pair whose support is too thin to act on.
CAN DEFEND: which pair to promote and why, with the arithmetic aloud.

### Subtopics

• Support, confidence and lift, derived by counting
• The confidence trap and lift below one
• Market basket analysis on real transactions
• Cross-sell and upsell reasoning
• Acting on thin support

### Trainer notes

START FROM: rates and denominators are solid (Week 1 Thursday); derive the three measures as counts before naming them.
GO AS FAR AS: every learner ships the basket analysis with one recommendation and its expected value in Rs.
STOP BEFORE: the apriori algorithm's mechanics, association-rule mining libraries; counting carries today.
COMES LATER: Thursday's cohorts ask when customers buy; Friday's thresholds ask when acting is worth it.
BREAK TO RUN: the planted popular item: confidence 0.82 toward it from everything, lift 0.97; the recommendation that looked strongest is chance dressed up, caught only by lift.
CUT FIRST: upsell (teach cross-sell, name upsell). Never cut the by-hand derivation or the confidence trap.

### Client zero and case studies

TODAY'S DATA: the scenario grows a transactions table (baskets keyed to the existing customers), per the grow-the-world rule; twelve hand-checkable baskets carry the derivation and the full table carries the exercise.
COMPETENCY BUILT: association reasoning that survives the popularity illusion.
CASE: the beer-and-diapers story is the field's favourite told-tale and is part legend, so tell it as a story and say so; then put the real weight on the lift arithmetic the room just derived, which needs no legend.

### In-session exercises

GUIDED: derive support, confidence and lift for two pairs on the twelve baskets, counting aloud.
UNGUIDED: the full basket analysis: top pairs by lift, the confidence-trap pair identified, one costed recommendation, no hints, solution at close.
MID-SESSION (15 min each): compute the three measures for one pair on paper; rank four pairs for action given lift and support together.

### After-class tasks

• BUILD: extend the analysis with one filter (a segment or a period) and note what changed.
• RECAP: lift below one, in one line, in your own words.
• READ: Thursday's pre-read naming cohort, funnel and retention, terms only.

### Trainer resources

• GeeksforGeeks, Data Analyst interview questions, association items (verified 03 Sep 2026):
https://www.geeksforgeeks.org/data-analysis/data-analyst-interview-questions-and-answers/
• pandas user guide index, Group by, for the counting implementation (verified 05 Sep 2026):
https://pandas.pydata.org/docs/user_guide/index.html

### Student references

• pandas, 10 minutes to pandas, the grouping section again before tonight's build (verified 05 Sep 2026):
https://pandas.pydata.org/docs/user_guide/10min.html

### Kahoot quiz plan

• Q1: support, confidence, lift: match each to its one-line question
• Q2: compute lift from the three counts shown
• Q3 trap: confidence 0.82, lift 0.97; promote or drop
• Q4: high lift, support 0.3 percent; what stops you acting
• Q5: which of the three measures popularity cannot fool
• Return question from Monday, one level up: name the guardrail you would attach to a cross-sell push.

## Thu 22 Oct 2026 · Cohorts, funnels, retention: where the loss actually happens

### Trainer agenda

1. A flat blended retention number hiding decline, on screen (10 min).
2. Cohort construction: who entered when, tracked forward, never blended (50 min).
3. The funnel: stages, drop-off per stage, and the stage that owns the loss (45 min).
4. Retention curves read: shape, floor, and the cohort comparison (40 min).
5. Guided then unguided cohort study on the scenario (60 min).
6. Kahoot and close-out (20 min).

### Learner outcome

UNDERSTANDS: a cohort fixes the entry moment so time effects stop lying, a funnel localises loss to a stage, and a blended average can stay flat while every cohort worsens.
CAN DO: build a cohort table and a funnel from the scenario's events and read a retention curve's shape and floor.
CAN HANDLE: the blended-flat-cohorts-declining trap, and a funnel stage whose drop is denominator artefact rather than loss.
CAN DEFEND: which stage to fix first and what evidence says so.

### Subtopics

• Cohort construction
• Funnel stages and drop-off
• Retention curves: shape and floor
• Blended numbers against cohort truth
• Where the loss actually happens

### Trainer notes

START FROM: groupby and time fields are solid (Week 2); the new idea is the entry-moment discipline, never the code.
GO AS FAR AS: every learner ships the cohort study: one cohort table, one funnel, one sentence naming the losing stage.
STOP BEFORE: survival analysis, LTV models, statistical tests on retention differences (name Monday of Week 2 as where that instinct goes).
COMES LATER: forecasting tomorrow leans on the cohort table's time axis.
BREAK TO RUN: the wrong-output trap: blended retention holds at 41 percent across three months while every individual cohort declines, because a growing new-cohort mix props the blend; the room decomposes it live.
CUT FIRST: the funnel's third example. Never cut the blended-against-cohort decomposition, which is the day's spine and the return of the Simpson instinct.

### Client zero and case studies

TODAY'S DATA: the scenario's transactions table gains event timestamps and a signup date per customer, growing the world again rather than switching it.
COMPETENCY BUILT: localise loss instead of describing it; the analyst move hiring managers probe with 'retention dropped, walk me through it'.
CASE: the blended-flat trap is the retention version of the Berkeley reversal taught in Week 2, and saying that sentence aloud is the day's backward hook.

### In-session exercises

GUIDED: build one cohort's row together, then the funnel's first two stages.
UNGUIDED: the full cohort study with the losing stage named and evidenced, no hints, solution at close.
MID-SESSION (15 min each): read three retention curves and rank the cohorts; find the denominator artefact in a four-stage funnel.

### After-class tasks

• BUILD: rerun the cohort table monthly instead of weekly and note which story survives.
• RECAP: blended against cohort, one line.
• READ: Friday's pre-read naming baseline, trend, seasonality and error metric, terms only.

### Trainer resources

• GeeksforGeeks, Data Analyst interview questions, cohort and funnel items (verified 03 Sep 2026):
https://www.geeksforgeeks.org/data-analysis/data-analyst-interview-questions-and-answers/
• pandas user guide index, Group by and Reshaping, for the cohort pivot (verified 05 Sep 2026):
https://pandas.pydata.org/docs/user_guide/index.html

### Student references

• pandas, 10 minutes to pandas, the reshaping section (verified 05 Sep 2026):
https://pandas.pydata.org/docs/user_guide/10min.html

### Kahoot quiz plan

• Q1: what a cohort fixes that a blended average cannot
• Q2: read the funnel: which stage owns the loss
• Q3 trap: blended retention flat, every cohort down; how
• Q4: the retention curve's floor means what for the business
• Q5: weekly or monthly cohorts: what decides
• Return question from Wednesday, one level up: lift 0.97 at confidence 0.82; say the verdict and the reason in one breath.

## Fri 23 Oct 2026 · Thresholds and forecasts: the cost of an error decides

### Trainer agenda

1. Two teams act on the same model at different thresholds; only one makes money (10 min).
2. Precision against recall as business quantities: cost of a false alarm against cost of a miss (50 min).
3. The 1-in-N test (course construction): rights per wrong equals damage over saving, and the bar it sets (35 min).
4. Lift and gain read at recognition depth; threshold selection as a business decision (35 min).
5. Forecasting basics in one arc: trend and seasonality seen, a naive baseline built, one error metric, and the good-enough call (60 min).
6. Unguided threshold memo plus baseline; Kahoot and close-out (45 min).

### Learner outcome

UNDERSTANDS: precision and recall trade against each other through the threshold, the costs of the two error types set the bar, and a forecast earns trust only by beating a naive baseline on a stated error metric.
CAN DO: pick a threshold from error costs using the 1-in-N test, and build a naive baseline with its error measured.
CAN HANDLE: a threshold tuned for accuracy that loses money, and a fancy forecast that fails to beat last-period-carried-forward.
CAN DEFEND: the threshold memo's number, and the sentence 'good enough for this decision' with its evidence.

### Subtopics

• Precision and recall as costs
• The 1-in-N test (course construction): damage over saving sets the bar
• Lift and gain, recognition depth
• Threshold selection as a business decision
• Trend and seasonality
• The naive baseline
• One error metric and the good-enough call

### Trainer notes

START FROM: rates, denominators and Monday's cost thinking; no model exists yet, so thresholds run on a provided score column, which keeps the decision separate from the modelling (that arrives Week 5).
GO AS FAR AS: every learner ships the threshold memo with a number and the forecast baseline with its error.
STOP BEFORE: ROC curves, any fitted forecasting model, seasonality decomposition mechanics.
COMES LATER: Week 5 Wednesday deepens the metric trap on real models; deeper forecasting stays out of scope for this cohort's placement target and the trainer's free third can extend if the room is fast.
BREAK TO RUN: the accuracy-tuned threshold: on the imbalanced outcome it maximises accuracy by barely acting, and the money table shows the loss; the room re-derives the bar from costs.
CUT FIRST: lift and gain (name them, park them), then the second baseline variant. Never cut the 1-in-N derivation, marked aloud as this course's own construction.
NOTE: the alternating-week business case study (AI-free) is due around this week per the assessment beat; its slot is a Programme Head call and no marks are stated.

### Client zero and case studies

TODAY'S DATA: the scenario table gains a provided propensity score column and a monthly volume series, growing the world for the third and final time this week.
COMPETENCY BUILT: decide with costs; the bridge from analyst craft into Week 5's machine learning.
CASE: statistical agencies publish forecast error against naive baselines as standard practice; a model that cannot beat carry-forward is reported as such rather than shipped, and that convention is the day's professional anchor.

### In-session exercises

GUIDED: derive the 1-in-N bar for the scenario's costs, then set the threshold together.
UNGUIDED: the threshold memo (number, bar, expected value in Rs) and the naive baseline with its error, no hints, solution at close.
MID-SESSION (15 min each): re-derive the bar when damage doubles; call good-enough or not on three baseline-against-model error pairs.

### After-class tasks

• BUILD: rerun the threshold memo for a second cost pair and note which way the number moved.
• RECAP: the 1-in-N sentence from memory.
• PREP: tomorrow's four-hour block runs the cross-domain transfer drill and interview Q&A; reread this week's four artifacts.

### Trainer resources

• Khan Academy, summarizing quantitative data, for the error-metric grounding (verified 03 Sep 2026):
https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data
• Interview Query, analyst case questions on thresholds and metrics (verified 03 Sep 2026):
https://www.interviewquery.com/p/python-data-science-interview-questions

### Student references

• GeeksforGeeks, Data Analyst interview questions, the case-style items (verified 03 Sep 2026):
https://www.geeksforgeeks.org/data-analysis/data-analyst-interview-questions-and-answers/

### Kahoot quiz plan

• Q1: false alarm costs Rs 32, a catch saves Rs 8; say the bar
• Q2: precision or recall: which suffers when the threshold rises
• Q3 trap: accuracy 97 percent on a 97-3 outcome; what did the model learn
• Q4: the naive baseline for a monthly series is what
• Q5: 'good enough' is a claim about what two numbers
• Return question from Thursday, one level up: blended retention flat while cohorts decline; name the mechanism in one sentence.

## Sat 24 Oct 2026 · Saturday recap: the pen-and-paper test, then the interview-answer discussion

### Trainer agenda

Four hours, no new content.
1. Weekly recap test: pen and paper, AI-free, built from the week's interview question set, short-answer format (120 min).
2. Break (20 min).
3. Solution discussion led by the Academic TA: papers swapped for peer cross-evaluation, every answer discussed as an interview answer, random call-outs throughout (75 min).
4. Doubt clearing and the bridge: Week 5 turns Friday's score column into a model (25 min).

### Learner outcome

CAN DO: answer the week's interview set on paper, without an assistant, in short-answer form.
CAN DEFEND: any of those answers aloud when called, and mark a peer's paper against the discussed solution.
STATUS: ungraded; the score is a performance indicator the programme reads, never a marks component.

### Subtopics

THE QUESTION SET (questions only; answers are built at the detailing phase):
• [S] How would you measure the success of a new feature? Walk your metric design.
• [F] North-star against guardrail, with one example pair.
• [S] Support, confidence, lift: which one cannot be fooled by popularity, and why?
• [SV] Retention dropped: walk me through your investigation.
• [F] Blended retention is flat while every cohort declines: how?
• [S] Precision against recall: which matters more for fraud screening, and why?
• [F] How do you set a classification threshold when the two errors cost differently?
• [D] What baseline must any forecast beat before it earns trust, and why?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. The tagging is this programme's own calibration for 0-3 year Indian-market candidates.

### Trainer notes

FORMAT: the paper is built from this row's question set, framed for short answers (selection, one-liners, small computations) so peer cross-checking works; answers themselves are written at the detailing phase, never improvised on the day.
DISCUSSION: papers swap for peer cross-evaluation; the Academic TA leads the solution walk-through as an interview-answer discussion, with random call-outs throughout.
STATUS: ungraded, a performance indicator rather than a marks component, and AI-free by format.

### Client zero and case studies

Answers must cite the scenario's own numbers and artifacts where the week produced them; the four analyst artifacts are the reference; the cross-domain transfer drill folds into the discussion round.

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

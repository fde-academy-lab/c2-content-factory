# W1 Data analysis found.

## Mon 28 Sep 2026 · Python through data · The revenue tree and the first honest numbers

### Business scenario of the day

WHY WE WORK THIS WAY. Engineers solve business problems, and business problems arrive in business words: grow revenue, cut cost, reduce risk, serve customers faster, stay compliant, decide sooner. The engineer's job is translation: turn that ask into a technical question data can answer, weigh more than one way to answer it, pick one, and defend it with evidence. Interviews test the same thing: a scenario, your translation, several approaches, and why you chose yours. So every day here opens on a business scenario, and every technique is the answer to a question a business actually asked.

TODAY. Kalpa Retail sells consumer goods through its app, website and stores across India and South-East Asia. Revenue grew 4 percent last year against a plan of 15. The board wants a growth plan within a month, and marketing has asked for Rs 12 crore to acquire new customers.
Meera Raghavan, CEO, to the new data team: "Before I sign anything, I want to understand our own sales. What is 'sales' made of? Where does revenue come from, by customer type and channel? Is acquisition even the branch that is short?" Anand Iyer, the CFO, adds: "No averages. One business customer can move an average."
Your role: you are the analyst in the room. By Thursday Meera expects a recommendation on which branch to examine first, and she will ask why you did not pick the others.
On the table: the components of revenue for a retailer; which to examine first and why; what a typical order looks like and which 'typical' is honest; whose instinct the data supports.

### Thinking we train, before any tool

Revenue is a tree: customers, times orders per customer, times items per order, times price per item, less discounts. Growth comes from one branch at a time, and each costs something different to move: acquisition costs marketing, frequency costs retention, basket costs merchandising, price risks volume, discounts trade margin for quantity. Marketing's Rs 12 crore is a bet on the first branch.
First move: draw the tree for this business and name each branch as a metric with numerator and denominator. Second move: refuse the single average when one customer buys in bulk, and report the median. This is the profitability framework case interviews test; learners draw it on paper before Python runs.

### Trainer agenda

1. Meera's ask; the room names what 'sales' could mean (15 min).
2. The revenue tree on the board; each branch as a metric; marketing's budget placed on its branch (40 min).
3. Environment: open the Codespace, run the setup cell, restart and recover once (25 min).
4. Count the leaves in Python: orders, revenue, customers, orders per customer; loops, accumulators, records as dictionaries (60 min).
5. Mean against median; the bulk order that splits them (30 min).
6. Unguided: three tree nodes and one sentence on which branch to examine first (40 min).
7. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: a business ask becomes a tree of measurable branches; every metric carries a denominator; one extreme record can make a mean lie.
CAN DO: draw the tree for a retailer, define each branch as a metric, compute the leaves in Python, and choose median over mean on purpose.
CAN HANDLE: a kernel run out of order, an amount stored as text, a mean far above every ordinary order.
CAN DEFEND: which branch Kalpa should examine first and why, and why the CFO was right about averages.

### Subtopics (technique in service of the scenario)

• Translating a business ask into a technical question
• The revenue driver tree; branches as metrics
• Numerator and denominator for every rate
• Codespace, notebook, kernel, restart and run all
• Values and types; comparisons
• for loops, if conditions, count and sum accumulators
• A record as a dictionary; a dataset as a list of them
• Mean against median, and when each is honest

### Trainer notes

START FROM: no Kalpa, no Python. Open on the business and the preamble; the tree is the teaching, Python is the calculator.
GO AS FAR AS: everyone draws the tree unaided, places an initiative on a branch, and computes the five leaves including median order value.
STOP BEFORE: functions, files, grouping by segment, statistics beyond mean and median.
COMES LATER: which branch moved (Tue), can we trust the numbers (Wed), is it real and what do we tell Meera (Thu). Say the arc once.
WHAT THE DATA REVEALS: the mean sits far above the median because of one bulk order; let the room find it by sorting. The text amount breaks the sum; read the trace together, fix with int() for today.
CUT FIRST: the recovery drill to five minutes. Never cut the tree or the mean-against-median reveal.

### Client zero data (TRAINER ONLY)

VERSION v0: about 30 flat order records with segment and channel, loaded by a setup cell.
PLANTED: one corporate bulk order of Rs 480,000 (mean against median); one amount as the text "4500" (the type break).
Both are discovered by computing; neither is named to students.

### In-session exercises

GUIDED: the tree on the board, then orders and revenue in one loop.
UNGUIDED: customers, orders per customer, median order value, and one sentence on which branch to examine first.
MID-SESSION (15 min each): place five initiatives (a discount, a new store, a loyalty card, a price rise, an app redesign) on tree branches and say what each costs to move; predict three cell outputs before running.

### After-class tasks

• BUILD: the revenue tree for a business you know (a canteen, a kirana store, an app), and the branch you believe moves most.
• EXTEND: two tree nodes on the provided second sample, and one sentence on what surprised you.
• READ: the profitability framework guide, revenue section.
• SETUP: nothing to install.

### Interview angle

• [S] How would you increase sales for an online retailer?
• [S] Mean or median for order value, and why?
• [F] A business says 'grow revenue 15 percent'; how do you turn that into questions data can answer?
• [SV] A list against a dictionary: when do you reach for each?
• [D] Marketing wants budget for acquisition; what would you check before agreeing it is the right branch, and how would you say no?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Hacking the Case Interview, profitability framework and the revenue tree (verified 13 Sep 2026):
https://www.hackingthecaseinterview.com/pages/profitability-case-interview
• Road to Offer, driver trees (verified 13 Sep 2026):
https://www.roadtooffer.com/blog/driver-tree
• GitHub Docs, Codespaces with Jupyter quickstart (verified 03 Sep 2026):
https://docs.github.com/en/codespaces/developing-in-a-codespace/getting-started-with-github-codespaces-for-machine-learning
• Corey Schafer, Python beginner playlist, videos 1 to 7 (verified 03 Sep 2026):
https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7
• Khan Academy, mean, median and mode (verified 03 Sep 2026):
https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/mean-median-basics/v/mean-median-and-mode

### Student references

• MConsultingPrep, the profitability framework (verified 13 Sep 2026):
https://mconsultingprep.com/profitability-case-framework
• Corey Schafer, Dictionaries (verified 03 Sep 2026):
https://www.youtube.com/watch?v=daefaLgNkw0
• Automate the Boring Stuff, 3rd edition, Ch 2 and Ch 3 (verified 03 Sep 2026):
https://automatetheboringstuff.com/3e/

### Kahoot quiz plan

• Q1: revenue fell while customer count rose; which branch do you open first
• Q2: orders per customer is what divided by what
• Q3 trap: is '4500' > 3000 True, an error, or it depends
• Q4: mean Rs 9,800, median Rs 1,400; what does that say about the orders
• Q5: cells ran 3, 1, 2; which error and why
• Q6: a discount lifts quantity 10 percent at 15 percent off; did revenue rise or fall
• Ungraded. No return question on Day 1.

## Tue 29 Sep 2026 · Python through data + descriptive statistics · Which lever moved? The sales-drop investigation

### Business scenario of the day

Meera, replying to Monday's numbers: "So revenue is customers, times how often they buy, times basket, times price. Now: which of those moved? Q2 was Rs 1.9 crore, Q1 was 2.1. Are we losing customers, or are the ones we have buying less? Marketing says more customers. Prove it or disprove it."
The head of Retail-Plus, the paid tier, forwards a member's complaint that the app's reorder feature has been broken for six weeks, and asks whether his tier is the one slipping.
Your role: you will present the decomposition to both of them, name a cause as a hypothesis rather than a fact, and be asked what evidence would prove it. Marketing will push back.
On the table: is the drop real or an artefact of how the quarters were cut; which branch moved and by how much; is it across all customer types or one; the two likeliest causes and the evidence that would settle them.

### Thinking we train, before any tool

The most asked analyst case in the market: sales dropped, investigate. The ladder is fixed. Confirm the drop is real. Compare like with like: same window, same segments, same denominators. Decompose along the tree. Isolate the branch and the segment. Hypothesise, and say what evidence would settle it.
Two disciplines: a rate without a denominator is a rumour, and a comparison across periods needs identical windows. Each segment gets a typical value and a spread, so descriptive statistics arrive as the instrument of comparison. The same numbers are needed for every segment and quarter, so functions arrive as a necessity.

### Trainer agenda

1. Meera's reply and the Retail-Plus complaint; the room lists what could make a drop look real when it is not (10 min).
2. The investigation ladder, five rungs, and what each needs from the data (30 min).
3. Grouping by key: orders and customers by quarter, then by segment; the dictionary accumulator (45 min).
4. Describing a segment: typical value, spread, shape from sorted values (35 min).
5. Functions: the same numbers for every segment, written once; return against print; the conversion that must not crash the loop (45 min).
6. Guided then unguided: Q1 against Q2 along the tree, segment by segment; name the branch and the segment (55 min).
7. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: a drop is investigated in a fixed order; a rate needs its denominator; a comparison needs matched windows; a segment is described by typical value and spread; a function applies one decision everywhere.
CAN DO: group by key with a dictionary accumulator, describe each group with median and spread, write functions returning the tree's metrics for any subset, decompose a quarter-on-quarter change.
CAN HANDLE: a conversion that would crash the loop, a segment compared over a shorter window, a function that prints instead of returning.
CAN DEFEND: 'customers flat, orders per customer down, concentrated in Retail-Plus', with the numbers, and the reorder-feature cause stated as a hypothesis with its test.

### Subtopics (technique in service of the scenario)

• The sales-drop investigation ladder
• Like-with-like: windows, segments, denominators
• Dictionary accumulators: grouping by quarter, by segment
• Median, min, max, range; shape from sorted values
• Functions: def, parameters, return; return against print
• A safe conversion with try/except
• Rates and percentage change
• Decomposing a change along the tree; hypothesis and the evidence that settles it

### Trainer notes

START FROM: Monday's tree and leaf counts. The ladder is new; the arithmetic is not.
GO AS FAR AS: everyone names the branch and segment with numbers, and states the reorder-feature cause as a hypothesis to test.
STOP BEFORE: files (Wed), any test of whether the difference is real (Thu), comprehensions, modules.
COMES LATER: tomorrow's cleaning changes tonight's answer; promise it.
WHAT THE DATA REVEALS: customers flat, orders per customer down, almost entirely in Retail-Plus. The absent discount field raises KeyError; fix with .get() and a stated default, reason written down.
CUT FIRST: percentage-change formalities. Never cut the ladder or the segment decomposition.

### Client zero data (TRAINER ONLY)

VERSION v1: 200 orders across Q1 and Q2 with segment, channel and month.
PLANTED: customers flat while orders per customer fall in Retail-Plus only; the optional discount field absent on a subset.
The room reaches Retail-Plus by decomposition and connects it to the complaint themselves.

### In-session exercises

GUIDED: group by quarter, then by segment; describe one segment; write revenue_for(subset).
UNGUIDED: the decomposition for all four segments, the branch and segment that moved, two hypotheses with the evidence that settles each.
MID-SESSION (15 min each): order the five rungs and defend one; spot the mismatched window in three quarter comparisons.

### After-class tasks

• BUILD: the investigation memo, one page: branch, segment, numbers, two hypotheses, what data settles each.
• READ: the sales-drop case walkthrough; rewrite your memo's first line if it changes your mind.
• WATCH: Corey Schafer, Functions.

### Interview angle

• [S] Sales dropped 15 percent last month; how would you investigate?
• [S] Why is a rate without a denominator meaningless?
• [F] Why does a function that prints instead of returning break a pipeline?
• [F] What has to match before a quarter-on-quarter comparison is fair?
• [D] Marketing insists the answer is acquisition and your data says frequency; how do you make the case in the room?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Exponent, data analyst interview questions incl. the sales-drop investigation (verified 13 Sep 2026):
https://www.tryexponent.com/blog/top-data-analyst-interview-questions
• Brit Institute, analyst case study questions with the investigation framework (verified 13 Sep 2026):
https://britinstitute.uk/blog/data-analyst-case-study-interview-questions
• Khan Academy, summarizing quantitative data unit (verified 03 Sep 2026):
https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data
• Corey Schafer, Functions (verified 03 Sep 2026):
https://www.youtube.com/watch?v=9Os0o3wzS_I
• Corey Schafer, try/except blocks (verified 03 Sep 2026):
https://www.youtube.com/watch?v=NIWwJbo-9_8

### Student references

• Brit Institute, the sales-drop case walkthrough (verified 13 Sep 2026):
https://britinstitute.uk/blog/data-analyst-case-study-interview-questions
• Khan Academy, mean, median and mode review (verified 03 Sep 2026):
https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/mean-median-basics/a/mean-median-and-mode-review
• Corey Schafer, Functions (verified 03 Sep 2026):
https://www.youtube.com/watch?v=9Os0o3wzS_I

### Kahoot quiz plan

• Q1: first rung of the ladder
• Q2: revenue per customer fell 8 percent; which two numbers next
• Q3 trap: Q1 has 13 weeks and Q2 has 11; fair comparison
• Q4: result = revenue_for(seg) holds None; what went wrong
• Q5: median Rs 1,200, range Rs 80,000; what do you say about the segment
• Q6: customers flat, orders per customer down in one segment; the hypothesis in one line
• Return question from Monday: the mean doubled and the median did not; first check.

## Wed 30 Sep 2026 · Python through data · Can we trust the numbers? Profile, clean, reconcile, recompute

### Business scenario of the day

Tuesday's finding reaches the leadership group. Anand, Finance controller, replies to all: "Your dashboard says Q1 was Rs 2.1 crore. Our books say 1.9. Until your numbers match ours, Finance will not act on a drop measured from an ERP export. Send me a reconciliation."
The ERP team sends the raw exports, an orders CSV and the app's JSON feed, with a note that the CSV was 'stitched from two extracts during the Q1 migration'. Marketing is impatient: if the drop is a data problem, a month is lost arguing.
Your role: you own the reconciliation. Anand will ask which figure is right and how you know; Marketing will ask whether Tuesday's finding survives; an auditor could ask why you dropped any row.
On the table: which Q1 figure is right and the proof; what in the exports could inflate or deflate revenue; whether Retail-Plus survives clean data; what to record so every decision can be followed.

### Thinking we train, before any tool

The first rung of the ladder, done properly. Profile before analysing: how many records, complete, convertible, distinct. Every cleaning act is a decision with a written reason: drop, default, or keep and flag. Then reconcile: input equals clean plus rejected, and revenue after cleaning is explained against revenue before.
Duplicates inflate revenue; missing amounts bias averages; text amounts vanish from sums. Tuesday's conclusion was drawn on dirty data; the honest analyst recomputes and reports what changed, including a smaller drop. This opens the Trust thread and the interview question 'the dashboard and Finance disagree, what do you do'.

### Trainer agenda

1. Anand's two figures; the room lists the ways an export could produce either (10 min).
2. Files: read orders.csv and the JSON feed; everything is text until converted (45 min).
3. Profile: presence, convertibility, distinct counts per field (40 min).
4. Missing values, the three-way decision; duplicates and the identity rule; the bulk order kept because it is real (50 min).
5. Reconcile: input equals clean plus rejected; recompute the tree; what changed against Tuesday (35 min).
6. Unguided: the full pass, the decisions log, the note to Finance (40 min).
7. Kahoot and close (20 min).

### Learner outcome

UNDERSTANDS: profiling precedes analysis; cleaning is recorded decisions; duplicates need an identity rule; a reconciliation proves the cleaned data is the same data.
CAN DO: read CSV and JSON, profile field by field, clean with a rejects log, reconcile counts and revenue, recompute the tree on clean data.
CAN HANDLE: a duplicate pair a whole-record check misses, a file that fails to parse at a named line, an amount spelled as a word, a revenue figure that moves once duplicates go.
CAN DEFEND: the reconciliation note: why 2.1, why 1.9, which is right, whether Retail-Plus stands.

### Subtopics (technique in service of the scenario)

• open, read, write, the with block; csv.DictReader; json.load and json.dump
• Everything read is text: converting on purpose
• Profiling: presence, convertibility, distinct counts
• Missing values: drop, default, keep and flag
• Duplicates and the identity rule
• Outliers: sorted tail, keep or investigate
• The rejects log and the decisions log
• Reconciliation: counts and the revenue bridge

### Trainer notes

START FROM: Tuesday's functions and conclusion; today re-runs it on the ERP exports, and the number moves.
GO AS FAR AS: everyone ships the cleaned dataset, decisions log, reconciled count and revenue bridge, and the note to Finance.
STOP BEFORE: statistics beyond counts and the median, imputation beyond a stated default, pandas.
COMES LATER: Thursday asks whether the cleaned gap is real; Week 2 re-expresses this pass in SQL and pandas.
WHAT THE DATA REVEALS: fourteen rows duplicated in the migration inflate Q1; Finance's 1.9 is right; the drop shrinks and Retail-Plus survives, smaller. FileNotFoundError, ValueError on 'twelve', JSONDecodeError at the truncated line: read each trace aloud as it comes.
CUT FIRST: json.dump, then the outlier fence. Never cut the reconciliation or the recompute.

### Client zero data (TRAINER ONLY)

VERSION v2: Tuesday's two quarters as orders.csv and orders.json, plus a companion file with the header duplicated.
PLANTED: 14 duplicated Q1 rows; one amount spelled "twelve"; one record missing a required field; a near-duplicate pair sharing an order_id with one differing timestamp; a truncated JSON line.
Both of Anand's figures are computable; students prove which is right.

### In-session exercises

GUIDED: read the CSV, profile two fields, walk one missingness decision with its reason.
UNGUIDED: the full pass, the reconciliation with a revenue bridge, the recomputed tree, the note to Finance.
MID-SESSION (15 min each): two profile printouts, which dataset do you trust and why; a JSONDecodeError message, open the file at the line and mark the defect.

### After-class tasks

• BUILD: the full pass on a second export with new defects; a reason per decision.
• WRITE: the note to Finance in under 120 words, numbers first, and whether Tuesday's finding survives.
• READ: Real Python on CSV files, the DictReader section.

### Interview angle

• [S] How do you handle missing data?
• [S] Finance and your dashboard disagree; what do you do?
• [F] How do you find duplicates, and what makes two records the same?
• [F] Everything read from a CSV is a string; what breaks and where do you convert?
• [D] An auditor asks why you dropped 14 rows; walk them through it.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Corey Schafer, CSV module (verified 03 Sep 2026):
https://www.youtube.com/watch?v=q5uM4VKywbA
• Real Python, Reading and Writing CSV Files (verified 03 Sep 2026):
https://realpython.com/python-csv/
• Official json docs, JSONDecodeError (verified 03 Sep 2026):
https://docs.python.org/3/library/json.html
• Real Python, LBYL against EAFP (verified 03 Sep 2026):
https://realpython.com/python-lbyl-vs-eafp/
• GeeksforGeeks, Data Analyst interview questions, cleaning items (verified 03 Sep 2026):
https://www.geeksforgeeks.org/data-analysis/data-analyst-interview-questions-and-answers/

### Student references

• Corey Schafer, Working with JSON data (verified 05 Sep 2026):
https://www.youtube.com/watch?v=9N6a-VLBa2I
• Real Python, Reading and Writing CSV Files (verified 03 Sep 2026):
https://realpython.com/python-csv/
• Automate the Boring Stuff, 3rd edition, Ch 10 and Ch 18 (verified 03 Sep 2026):
https://automatetheboringstuff.com/3e/

### Kahoot quiz plan

• Q1: the three counts a profiler reports per field
• Q2: dedupe says 0, distinct ids say 186 of 200; what happened
• Q3 trap: coerce every failure to a default and the data looks clean; what got lost
• Q4: input 200, clean 183, rejected 14; does it reconcile
• Q5: the bulk order survives cleaning; why
• Q6: dashboard 2.1, Finance 1.9; which is right and how do you prove it
• Return question from Tuesday: name one data reason that could fake the Retail-Plus finding.

## Thu 01 Oct 2026 · Hypothesis testing and inference + correlation vs causation + insight communication · Real or noise, cause or coincidence, and the one-page note

### Business scenario of the day

With Finance reconciled, Meera sets the growth review for Monday and sends three questions. "One: Retail-Plus is down, smaller than first reported. Real, or the wobble we see every quarter? Two: Student is up 40 percent; should I move budget there? Three: marketing ran a monsoon-sale discount for Retail-Plus in August, says it lifted revenue 6 percent, and wants to repeat it for Diwali. Did the discount work, or did those customers buy anyway?"
Her constraint: "One page, two minutes. If the honest answer is 'we do not know yet', say so and tell me what would tell us."
Your role: the page is yours, and on Monday marketing will defend its campaign against your reading of it. You need a position on all three questions and the caveat that would change each.
On the table: could chance produce the Retail-Plus gap; how far a 40 percent lift on a small segment can be trusted; whether 'revenue rose after the discount' means the discount caused it, and what a fair comparison needs; how a finding is written so a CEO acts on it without being misled.

### Thinking we train, before any tool

Three questions, three habits. A difference needs a chance reference: shuffle the segment labels many times, recompute the gap each time, and see how often chance alone produces one as large as the real one. That share is the p-value, the share of chance-only worlds at least as extreme, never the probability the finding is wrong. Statistically real and worth acting on are separate calls.
Sample size: a 40 percent lift on twelve orders is noise dressed as a headline; distrust any rate under thirty observations.
Cause: revenue rising after a discount is not proof. The customers who took it may have been about to buy anyway, and a campaign can succeed in aggregate while every segment did worse once the mix shifts. A fair comparison needs a like-for-like group that did not get it; where none exists, say so.
Then the note: claim, evidence with denominators, the caveat that would change the claim, the action with its cost. 'Not yet, and here is what would tell us' is the sentence the CEO keeps you for.

### Trainer agenda

1. Meera's three questions sorted into real-or-noise, trust-the-number, cause-or-coincidence (10 min).
2. Shuffle by hand with ten cards, then the permutation loop in code; the p-value as a share (55 min).
3. Statistically real against worth acting on; a confidence interval named (20 min).
4. Sample size: Student's 40 percent on twelve against Retail-Plus on four hundred; the rule of thumb (25 min).
5. Correlation against causation on the monsoon sale: who took it, what a fair comparison needs, the aggregate that flips by segment (45 min).
6. The note: guided on Retail-Plus, unguided on Student and the discount (55 min).
7. Kahoot, close, Saturday preview (20 min).

### Learner outcome

UNDERSTANDS: the p-value is the share of chance-only worlds at least as extreme; significance and importance are separate; a rate is only as good as its sample; correlation is a lead; the note's shape prevents overclaiming.
CAN DO: run a label-shuffle test and state the p-value in one precise sentence, apply the sample-size rule, name the confounder and what a fair comparison needs, write the four-part note.
CAN HANDLE: 'p = 0.03 means a 3 percent chance we are wrong', an impressive rate on a dozen records, an aggregate that reverses by segment, a CEO who wants a yes.
CAN DEFEND: all three answers in sixty seconds each with their caveats; the week's interview anchor.

### Subtopics (technique in service of the scenario)

• Sampling variation and the chance reference
• The null model and label shuffling; the permutation loop in code
• The p-value: what it means and does not
• Statistically real against worth acting on; a confidence interval at recognition depth
• Sample size and the rule of thumb
• Correlation against causation; the confounder; the fair comparison
• Simpson's reversal on the campaign, at recognition depth
• The note: claim, evidence, caveat, action; when to refuse the one-number answer

### Trainer notes

START FROM: the cleaned dataset. Concept-first: no test catalogue, no formulas, no tables.
GO AS FAR AS: everyone states a p-value correctly, names the campaign confounder, and ships the one-page note with all three answers.
STOP BEFORE: the t-test family, confidence-interval construction, power, chart libraries. Name each as later.
COMES LATER: Week 2 joins the campaigns table properly in SQL and pandas; Week 4 designs the metric the plan chases.
WHAT THE DATA REVEALS: Retail-Plus is real but modest; Student rests on twelve orders; the monsoon sale's 6 percent is a mix effect and every segment separately fell, so 'do not repeat it as designed'. Let the room reach all three.
CUT FIRST: the confidence-interval line, then the Simpson arithmetic. Never cut the hand shuffle, the confounder, or the note.

### Client zero data (TRAINER ONLY)

VERSION v3: the cleaned two quarters plus the Student segment, plus the campaigns table with August's monsoon sale for Retail-Plus.
PLANTED: Student holds exactly 12 orders; the Retail-Plus gap is real but modest; the campaign lifts aggregate revenue 6 percent while every segment separately fell, because the treated group skews toward customers who would have bought anyway.
Discovered by computing; none of it on a slide.

### In-session exercises

GUIDED: ten-card shuffle, the first coded shuffle, the Retail-Plus note.
UNGUIDED: the 5,000-shuffle simulation and its p-value sentence; the Student and discount answers; the full one-page note.
MID-SESSION (15 min each): four p-value sentences, defensible or wrong; the confounder in three Kalpa vignettes; two overclaiming sentences rewritten honestly.

### After-class tasks

• WRITE: the note, final, under 200 words, read aloud to someone outside the programme.
• WATCH: Seeing Theory, frequentist inference; then redo the shuffle on your Monday take-home data.
• RECAP: the note's four parts and the p-value sentence from memory; both are on Saturday's paper.

### Interview angle

• [S] How do you know whether a change in a metric is significant?
• [S] Explain a finding to a non-technical stakeholder.
• [S] What does p = 0.03 mean, and not mean?
• [F] 42 percent on 12 users against 31 percent on 1,200; which do you trust?
• [F] Revenue rose after a discount; did the campaign work, and what would you need to know?
• [D] The CEO wants a yes or no and the honest answer is 'not yet'; what do you say, and how do you hold the line when marketing pushes?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Seeing Theory, frequentist inference (verified 05 Sep 2026):
https://seeing-theory.brown.edu/frequentist-inference/index.html
• StatQuest video index: 'Hypothesis Testing and The Null Hypothesis', 'p-values: What they are and how to interpret them' (verified 05 Sep 2026):
https://statquest.org/video_index.html
• Khan Academy, summarizing quantitative data unit (verified 03 Sep 2026):
https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data
• Exponent, analyst questions incl. conveying insights to a non-technical audience (verified 13 Sep 2026):
https://www.tryexponent.com/blog/top-data-analyst-interview-questions
• GeeksforGeeks, Data Analyst interview questions, hypothesis testing items (verified 03 Sep 2026):
https://www.geeksforgeeks.org/data-analysis/data-analyst-interview-questions-and-answers/

### Student references

• Seeing Theory, frequentist inference, interactive (verified 05 Sep 2026):
https://seeing-theory.brown.edu/frequentist-inference/index.html
• StatQuest video index, the two hypothesis-testing videos (verified 05 Sep 2026):
https://statquest.org/video_index.html

### Kahoot quiz plan

• Q1: ten shuffles gave gaps of 2 to 6 and the real gap is 5; surprising or not
• Q2 trap: 'p = 0.03 means a 3 percent chance we are wrong'
• Q3: 40 percent on 12 against 31 percent on 400; which do you trust
• Q4: revenue rose 6 percent after the discount; the question before calling it a success
• Q5: aggregate favours the campaign, every segment says the opposite; which do you trust
• Q6: the four parts of the note, in order
• Return question from Wednesday: the duplicates shrank the drop; does Retail-Plus survive, and how do you know.

## Fri 02 Oct 2026 · Gandhi Jayanti: institute holiday, no session

### Business scenario of the day

No session. Gandhi Jayanti.

### Thinking we train, before any tool

None scheduled.

### Trainer agenda

No session; the institute is closed. Week 1 teaching ends Thursday; the recap paper moves to Saturday.

### Learner outcome

No new outcomes.

### Subtopics (technique in service of the scenario)

None scheduled.

### Trainer notes

Nothing to deliver.

### Client zero data (TRAINER ONLY)

The scenario rests.

### In-session exercises

None scheduled.

### After-class tasks

• OPTIONAL: rerun the week's pipeline top to bottom in a fresh Codespace; note anything that fails cold.
• OPTIONAL: finish the note.

### Interview angle

None.

### Trainer resources

None needed.

### Student references

• Seeing Theory, frequentist inference (verified 05 Sep 2026):
https://seeing-theory.brown.edu/frequentist-inference/index.html

### Kahoot quiz plan

None.

## Sat 03 Oct 2026 · Saturday recap · The pen-and-paper test, then the interview-answer discussion

### Business scenario of the day

The week under questioning; Monday's growth review is the real audience. Every question on the paper is a Kalpa business question first and a technique question second, the order interviewers use.

### Thinking we train, before any tool

Saying the week out loud is the interview skill itself.

### Trainer agenda

Four hours, no new content.
1. Recap test: pen and paper, AI-free, from the week's question set, short answers (120 min).
2. Break (20 min).
3. Solution discussion led by the Academic TA: papers swapped for peer cross-evaluation, each answer treated as an interview answer, random call-outs (75 min).
4. Doubts and the bridge: the CFO wants the same numbers from the warehouse every week, which is Monday (25 min).

### Learner outcome

CAN DO: answer the week's business and technique questions on paper without an assistant.
CAN DEFEND: any answer aloud when called; mark a peer's paper against the discussed solution.
STATUS: ungraded; a performance indicator.

### Subtopics (technique in service of the scenario)

THE QUESTION SET (questions only; answers built at detailing):
• [S] Kalpa wants 15 percent growth; draw the revenue tree and name the branch you would investigate first.
• [S] Sales fell from Q1 to Q2; walk the investigation ladder.
• [S] Mean or median for order value, and why?
• [S] Finance and the dashboard disagree by Rs 20 lakh; what do you do first?
• [S] What does p = 0.03 mean, and not mean?
• [F] Input 200, clean 183, rejected 14: does it reconcile, and what is the missing number?
• [F] 42 percent on 12 orders against 31 percent on 400; which do you trust?
• [F] Revenue rose after the discount; three reasons that is not proof it worked.
• [D] Your cleaning run reported zero rejects on a file you know is dirty; what do you check?
• [D] Write the four-part note for the Retail-Plus finding in four sentences, then defend the caveat.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer notes

FORMAT: the paper comes from this row's question set, short answers so peers can cross-check; answers are written at detailing.
DISCUSSION: papers swap; the Academic TA walks the solutions as interview answers, random call-outs throughout.
STATUS: ungraded, AI-free by format.

### Client zero data (TRAINER ONLY)

Answers cite Kalpa's own numbers. Findings are discussed; plants are never revealed.

### In-session exercises

• The two-hour recap test.
• Peer cross-evaluation.
• Random call-outs: sixty seconds each.

### After-class tasks

• RECAP: rewrite any question you lost marks on, one line each, in your own words.

### Interview angle

The question set in Subtopics is the interview set for the week.

### Trainer resources

• This row's question set is the paper's source.
• GeeksforGeeks, Data Analyst interview questions (verified 03 Sep 2026):
https://www.geeksforgeeks.org/data-analysis/data-analyst-interview-questions-and-answers/

### Student references

• Reread the week's rows and your rejected answers; the next paper reuses missed ground one level up.

### Kahoot quiz plan

None. The recap test and discussion replace the quiz.

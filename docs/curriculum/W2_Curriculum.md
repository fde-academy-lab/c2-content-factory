# W2 Curriculum

## Mon 05 Oct 2026 · Is the difference real? Inference, causation, and the sentence the business hears

### Trainer agenda

1. Thursday's segment gap on screen: could chance alone produce this (10 min).
2. Shuffle intuition with ten labelled cards by hand, one difference computed (25 min).
3. The permutation loop in code: shuffle labels, recompute, repeat, plot the null spread, mark the observed gap (50 min).
4. The p-value as the share of shuffles at least as extreme; practical against statistical significance; a confidence interval in one line (40 min).
5. Correlation against causation: confounders, a fair comparison, Simpson's reversal on the scenario's own segments (45 min).
6. The insight writeup: claim, evidence, caveat, action; the one-number answer; the right visual at recognition depth (40 min).
7. Kahoot and close-out (20 min).

### Learner outcome

UNDERSTANDS: samples vary, a p-value is the share of chance-only worlds at least as extreme as the observation, significance and importance are separate calls, and correlation is a lead rather than a verdict.
CAN DO: run a label-shuffle test on the segment gap, state the p-value in one precise sentence, and write the insight note (claim, evidence, caveat, action).
CAN HANDLE: the wrong sentence 'p = 0.03 means a 3 percent chance the null is true', a confounder that explains an apparent effect, and an aggregate that reverses at segment level.
CAN DEFEND: whether the observed difference justifies action, in language that never claims more than the data's design supports. This defence is the fortnight's interview anchor.

### Subtopics

• Sampling variation and the need for a chance reference
• The null model and label shuffling
• The p-value and significance
• Practical against statistical significance
• A confidence interval at recognition depth
• Choosing the right test, named and parked
• Correlation against causation; confounders
• Simpson's paradox; what a fair comparison requires
• The insight writeup: claim, evidence, caveat, action
• The one-number answer and the right visual, recognition depth

### Trainer notes

START FROM: they own Thursday's segment summary and its gap, and the weekend pre-read seeded shuffle vocabulary. Concept-first throughout: no test catalogue, no formulas, no distribution tables.
GO AS FAR AS: every learner produces a p-value they can state in one correct sentence, and an insight note on a fresh segment.
STOP BEFORE: the t-test family, confidence-interval construction, power, Type I and II formalism, multiple-testing machinery. Name each as coming later so the room hears a map rather than a gap.
COMES LATER: SQL from tomorrow and pandas on Friday put engines under this pipeline; Build 1 in Week 3 demands this exact arc on raw messy data.
BREAKS TO RUN: the misinterpretation repair, 'p = 0.03 means a 3 percent chance the null is true', rewritten live against the null-model wording; the Simpson reversal, where the aggregate favours one segment and every sub-group disagrees, on planted scenario numbers.
CUT FIRST if time slips: the confidence-interval line, then the visual-choice card. Never cut the hand shuffle or the p-value sentence.

### Client zero and case studies

TODAY'S DATA: Thursday's cleaned segment summary; the gap between two segments is the observed statistic, and a planted composition difference drives the Simpson demonstration.
INTEGRATION: Week 1's question closes with the scenario's first defensible claim, which Build 1 will demand again.
COMPETENCY BUILT: judge whether a difference is real and say so in stakeholder language; the Week 1 arc completes here.
CASE: UC Berkeley admissions, 1973, the canonical documented Simpson's reversal: aggregate figures suggested bias that department-level figures contradicted.

### In-session exercises

GUIDED: one hand shuffle with ten cards, then the first coded shuffle together, verifying group sizes stay fixed.
UNGUIDED: finish the 5,000-shuffle simulation, chart the null spread, state the p-value sentence, and write the insight note on a fresh segment, no hints, solution at close.
MID-SESSION (15 min each): classify four p-value sentences as defensible or wrong; spot the confounder in three short scenario vignettes.

### After-class tasks

• BUILD: the one-page insight note on a second segment, claim, evidence, caveat and action, opened for review tomorrow.
• RECAP: the fortnight's error catalogue so far, each planted break in one line.
• SETUP (ships tonight, needed tomorrow): open the SQL connection instructions, connect from VS Code, and run SELECT 1 to prove the database answers.

### Trainer resources

• Seeing Theory, frequentist inference chapter, the estimation and testing visuals (verified 05 Sep 2026):
https://seeing-theory.brown.edu/frequentist-inference/index.html
• StatQuest video index: open 'Hypothesis Testing and The Null Hypothesis' and 'p-values: What they are and how to interpret them' (verified 05 Sep 2026):
https://statquest.org/video_index.html
• GeeksforGeeks, Data Analyst interview questions, hypothesis testing and p-value items (verified 03 Sep 2026):
https://www.geeksforgeeks.org/data-analysis/data-analyst-interview-questions-and-answers/
• Interview Query, Python and statistics questions for data roles (verified 03 Sep 2026):
https://www.interviewquery.com/p/python-data-science-interview-questions

### Student references

• Seeing Theory, frequentist inference chapter, interactive (verified 05 Sep 2026):
https://seeing-theory.brown.edu/frequentist-inference/index.html
• StatQuest video index, the two hypothesis-testing videos under Statistics Fundamentals (verified 05 Sep 2026):
https://statquest.org/video_index.html

### Kahoot quiz plan

• Q1: ten shuffles produced gaps of 2 to 6 points and the observed gap is 5; surprising or not
• Q2 trap: 'p = 0.03 means a 3 percent chance the null is true', defensible or wrong
• Q3: in a label shuffle, what stays fixed and what moves
• Q4: tiny effect, huge sample, p below 0.01; significant, important, both, neither
• Q5: name the confounder: ice cream sales and drownings rise together
• Q6: aggregate favours segment A, every sub-group favours B; which do you trust and what do you check
• Q7: the four parts of the insight note, in order
• Return question from W1 Thursday, one level up: mean and median disagree sharply; what do you inspect before choosing either.

## Tue 06 Oct 2026 · Ask the database: SQL core on the client-zero tables

### Trainer agenda

1. The Week 1 Python profiler on screen beside three lines of SQL doing the same count (10 min).
2. First-use tool established: the live Postgres connection from VS Code, .sql files, run and read (30 min).
3. SELECT, FROM, WHERE; ORDER BY and LIMIT, demonstrated on the scenario tables (45 min).
4. Aggregates, GROUP BY and HAVING; the logical execution order walked aloud (50 min).
5. Readable structure: subqueries, then CTEs as named steps (40 min).
6. Guided then unguided: the extraction query suite, no hints, solution at close (45 min).
7. Kahoot and close-out (20 min).

### Learner outcome

UNDERSTANDS: a query describes the result rather than the steps, the logical order (FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY) explains most beginner errors, and a CTE is a named step that keeps a query readable.
CAN DO: write filtered, ordered, aggregated queries against the scenario tables and structure a two-step question as a CTE.
CAN HANDLE: the GROUP BY column error read and fixed, a WHERE that belonged in HAVING, and a LIMIT without ORDER BY returning arbitrary rows.
CAN DEFEND: why WHERE and HAVING both exist, and what the database guarantees about row order (nothing, without ORDER BY).

### Subtopics

• The Postgres connection from VS Code; .sql files against a live database
• SELECT, FROM, WHERE
• ORDER BY and LIMIT
• Aggregate functions; GROUP BY and HAVING
• The logical execution order
• Subqueries, then CTEs as named steps
• Readable query structure

### Trainer notes

START FROM: zero SQL. The room knows the data and the questions from Week 1, which is the whole advantage: every query answers a question they have already answered in Python, so attention goes to the language.
GO AS FAR AS: every learner ships the extraction query suite: a filter, an aggregate by segment, and one CTE-structured two-step question.
STOP BEFORE: joins (tomorrow), window functions (Thursday), DDL beyond reading the schema, indexes and performance.
COMES LATER: joins tomorrow, windows Thursday, and Friday's pandas day closes with SQL-against-pandas judgment.
BREAKS TO RUN: ERROR: column "segment" must appear in the GROUP BY clause or be used in an aggregate function, read aloud and fixed two ways; then the quiet one: LIMIT 5 without ORDER BY returns five arbitrary rows, and two learners get different answers to the same question.
CUT FIRST if time slips: subqueries (go straight to CTEs), then LIMIT niceties. Never cut the execution-order walk or the GROUP BY error.

### Client zero and case studies

TODAY'S DATA: the Week 1 records re-expressed as scenario tables in Postgres, loaded in advance; same ids, same segments, same whale.
INTEGRATION: every query re-answers a Week 1 question, so learners already know what the right answer looks like and the contrast carries the teaching (the 30-line profiler against three lines of SQL).
COMPETENCY BUILT: extract and aggregate from a live database; the spine's second tool.
CASE: none cited today; the side-by-side contrast is the day's evidence.

### In-session exercises

GUIDED: the segment count and the amount aggregate built together, execution order narrated.
UNGUIDED: the extraction suite: three questions from Week 1 re-answered in SQL, no hints, solution at close.
MID-SESSION (15 min each): predict the row count of four queries before running; put five clauses in logical execution order and defend one placement.

### After-class tasks

• BUILD: two more extraction queries on questions of your own choosing, each with a one-line comment stating the question.
• PRACTICE: SQLBolt lessons 1 to 5, interactive, in the browser.
• RECAP: the execution order written from memory in a .sql comment.

### Trainer resources

• pgtutorial.com, PostgreSQL tutorial, the querying sections (verified 05 Sep 2026):
https://www.pgtutorial.com/
• PostgreSQL official tutorial, part I (verified 05 Sep 2026):
https://www.postgresql.org/docs/current/tutorial.html
• SQLBolt, lessons 1 to 12 incl. order of execution (verified 05 Sep 2026):
https://sqlbolt.com/
• PostgreSQL Exercises, basic and aggregate categories for stretch (verified 05 Sep 2026):
https://pgexercises.com/

### Student references

• SQLBolt, interactive lessons 1 to 5 tonight (verified 05 Sep 2026):
https://sqlbolt.com/
• pgtutorial.com, the SELECT and GROUP BY pages (verified 05 Sep 2026):
https://www.pgtutorial.com/

### Kahoot quiz plan

• Q1: which runs first, WHERE or SELECT
• Q2 trap: WHERE count(*) > 5; why it fails and what exists instead
• Q3: predict the row count of a GROUP BY segment on the scenario table
• Q4: LIMIT 5 without ORDER BY returns which five rows
• Q5: read a two-block CTE and name what the second block can see
• Q6: the Week 1 presence counter in one SQL line
• Return question from Monday, one level up: the test says significant and the effect is Rs 2 per order; ship the change or not, and say why.

## Wed 07 Oct 2026 · Joins without lies: semantics, imperfect keys, row-count validation

### Trainer agenda

1. A revenue number that doubled overnight on screen; the join that did it (10 min).
2. INNER and LEFT on two tiny tables, row by row on the board (45 min).
3. RIGHT and FULL OUTER completed; what each join drops or duplicates (30 min).
4. Imperfect keys and fan-out: one-to-many multiplication, counted live (45 min).
5. The validation habit: row counts before and after, and the anti-join to find orphans (40 min).
6. merge in pandas contrasted once, with validate= raising on the same defect (30 min).
7. Guided then unguided joined-dataset build with checks; Kahoot and close (40 min).

### Learner outcome

UNDERSTANDS: each join type answers a different question about unmatched rows, an imperfect key multiplies rows before it loses them, and a join is only done when its row count is explained.
CAN DO: choose and write the right join, validate it with before-and-after counts, and find orphans with an anti-join.
CAN HANDLE: a fan-out that doubles revenue while looking plausible, an INNER join that silently drops unmatched rows, and a duplicate key on the many side.
CAN DEFEND: the join choice on the joined-dataset artifact, and the count arithmetic that proves it honest.

### Subtopics

• INNER, LEFT, RIGHT and FULL OUTER
• What each join drops or duplicates
• Keys, imperfect keys and fan-out
• Row-count validation before and after
• The anti-join pattern for orphans
• merge against join in pandas, one contrast
• The joined dataset with checks

### Trainer notes

START FROM: they extract and aggregate (Tuesday). Open on the wrong number, then teach the machinery that explains it; application before theory.
GO AS FAR AS: every learner ships the joined dataset with a written count reconciliation and one anti-join.
STOP BEFORE: self-joins, CROSS JOIN beyond a one-line mention, join algorithms and performance, pandas depth beyond the single merge contrast.
COMES LATER: window functions tomorrow ride on today's joined table; Friday's pandas day does merges properly with validate= as the habit.
BREAKS TO RUN: the fan-out wrong-output: a LEFT join against a table with duplicate keys grows 1,000 rows to 1,450 and the revenue total doubles while every row looks plausible; caught only by the count check. Then pandas raising pandas.errors.MergeError under validate='one_to_one' on the same defect, the loud version of the same lesson.
CUT FIRST if time slips: FULL OUTER (name it, park it), then the pandas contrast. Never cut the count validation or the fan-out.

### Client zero and case studies

TODAY'S DATA: a second scenario table arrives (a related entity keyed to the first), with duplicate keys planted on the many side and a handful of orphan rows on each side.
INTEGRATION: the scenario grows an entity instead of switching domains, per the one-spine rule; the joined dataset feeds Thursday's rankings.
COMPETENCY BUILT: combine two tables honestly and prove it with counts.
CASE: the fan-out double-count is the classic audit finding in revenue dashboards; the planted version is run live rather than a company cited, since public postmortems for join bugs are rare.

### In-session exercises

GUIDED: INNER and LEFT on the tiny tables together, rows traced on the board before any query runs.
UNGUIDED: build the joined dataset, reconcile the counts in a comment block, and list orphans with an anti-join, no hints, solution at close.
MID-SESSION (15 min each): predict four row counts before running the joins; match five business questions to the join type that answers each.

### After-class tasks

• BUILD: one more join question of your own on the two tables, with the count reconciliation in comments.
• PRACTICE: SQLBolt lessons 6 to 8, the join lessons.
• RECAP: one comment line on when an INNER join is the honest choice.

### Trainer resources

• pgtutorial.com, the joins pages (verified 05 Sep 2026):
https://www.pgtutorial.com/
• SQLBolt, lessons 6 to 8, joins and NULLs (verified 05 Sep 2026):
https://sqlbolt.com/
• PostgreSQL Exercises, the joins category for stretch (verified 05 Sep 2026):
https://pgexercises.com/
• pandas user guide index, open the Merging guide for the validate= contrast (verified 05 Sep 2026):
https://pandas.pydata.org/docs/user_guide/index.html

### Student references

• SQLBolt, lessons 6 to 8 tonight (verified 05 Sep 2026):
https://sqlbolt.com/
• PostgreSQL Exercises, joins category, first three (verified 05 Sep 2026):
https://pgexercises.com/

### Kahoot quiz plan

• Q1: LEFT join keeps unmatched rows from which side
• Q2: 1,000 orders LEFT JOIN payments where 50 orders have two payments; predict the row count
• Q3 trap: what does an INNER join do silently
• Q4: the anti-join in words: customers with no orders
• Q5: revenue doubled after a join; the first check
• Q6: the pandas argument that would have raised on the fan-out
• Return question from Tuesday, one level up: WHERE against HAVING, one sentence each.

## Thu 08 Oct 2026 · Windows over rows: rank, lag, running totals, then the timed drill

### Trainer agenda

1. Top three by segment on screen; the GROUP BY attempt that cannot produce it (10 min).
2. ROW_NUMBER, RANK and DENSE_RANK on a tie, side by side (40 min).
3. PARTITION BY and ORDER BY inside the window; top-N per group (45 min).
4. LAG and LEAD; the running total and what makes it deterministic (45 min).
5. Guided then unguided ranking-query build (40 min).
6. The timed drill, AI-free: three datasets on screen, produce the answer on the spot, explain the join choice (50 min).
7. Kahoot and close-out (10 min).

### Learner outcome

UNDERSTANDS: a window function computes across related rows without collapsing them, which is what GROUP BY cannot do, and the partition plus its internal order define everything.
CAN DO: rank within segments, read the previous row with LAG, build a deterministic running total, and answer top-N per group.
CAN HANDLE: RANK against DENSE_RANK on ties, a window function refused inside WHERE, and a running total that changes between runs because its order was ambiguous.
CAN DEFEND: GROUP BY or window for a given question, chosen out loud in the drill.

### Subtopics

• ROW_NUMBER, RANK and DENSE_RANK, and what a tie does to each
• PARTITION BY; ORDER BY inside the window
• Top-N per group
• LAG and LEAD
• Running totals and determinism
• Filtering on a window via a CTE
• The timed drill: answer on the spot, explain the join choice

### Trainer notes

START FROM: they join and validate (Wednesday). Open on the question GROUP BY cannot answer, so the new tool arrives as the missing piece rather than new syntax.
GO AS FAR AS: every learner ships the ranking query and completes the drill; the drill is spoken as well as typed.
STOP BEFORE: frame clauses (ROWS BETWEEN), named windows, percentiles, performance.
COMES LATER: Friday's pandas day mirrors ranks with groupby transforms at recognition depth; the Build 1 brief will reward window fluency.
BREAKS TO RUN: the tie: RANK returns 1,1,3 where the room expects 1,1,2, and the top-3 report ships four rows; then ERROR: window functions are not allowed in WHERE, fixed by filtering in a CTE.
CUT FIRST if time slips: LEAD (teach LAG, name LEAD), then the running total variant. Never cut the tie demonstration or the drill.
NOTE: the weekly proctored coding slot for Week 2 is a scheduling call for the Programme Head; the drill here is practice and carries no marks statement.

### Client zero and case studies

TODAY'S DATA: the joined dataset from Wednesday; rankings and running totals answer the scenario's who-leads and how-it-accumulates questions.
INTEGRATION: the drill's three datasets stay inside the scenario world plus one transfer set, per the two-examples rule.
COMPETENCY BUILT: answer ordered, per-group questions and defend the tool choice aloud.
CASE: top-N per group is among the most asked SQL interview patterns at analyst level; the drill format exists because interviews ask it live.

### In-session exercises

GUIDED: the tie demonstration built together, three ranking functions on one screen.
UNGUIDED: the ranking query suite: top-3 per segment, previous-value comparison with LAG, one running total, no hints, solution at close.
DRILL (timed, AI-free): three datasets on screen, produce the answer on the spot, explain the join choice aloud.

### After-class tasks

• BUILD: one ranking question of your own plus its GROUP BY impostor, with a comment on why they differ.
• PRACTICE: PostgreSQL Exercises, window functions category, first three.
• RECAP: RANK, DENSE_RANK and ROW_NUMBER on the same tie, from memory, in a comment.

### Trainer resources

• PostgreSQL Exercises, window functions category with worked answers (verified 05 Sep 2026):
https://pgexercises.com/
• postgresqltutorial.com, the window functions section (verified 05 Sep 2026):
https://www.postgresqltutorial.com/
• pgtutorial.com for clause syntax cross-checks (verified 05 Sep 2026):
https://www.pgtutorial.com/

### Student references

• PostgreSQL Exercises, window functions, first three tonight (verified 05 Sep 2026):
https://pgexercises.com/
• SQLBolt for anyone still shaky on joins before the drill recap (verified 05 Sep 2026):
https://sqlbolt.com/

### Kahoot quiz plan

• Q1: RANK, DENSE_RANK and ROW_NUMBER on a two-way tie; give all three outputs
• Q2: PARTITION BY resets what
• Q3: LAG(amount) on the first row of a partition returns what
• Q4: which ORDER BY makes a running total deterministic
• Q5 trap: a window function inside WHERE; why refused and the fix
• Q6: top-3 per segment: GROUP BY or window, and why
• Return question from Wednesday, one level up: your LEFT join grew rows; name the cause and the check.

## Fri 09 Oct 2026 · Pandas at depth and tool judgment: the feature table and the right tool call

### Trainer agenda

1. Thursday's segment summary built by hand in Week 1, now one groupby line (10 min).
2. groupby and agg: split, apply, combine; named aggregations (50 min).
3. Reshape: pivot_table and melt, each direction once (40 min).
4. Multi-source merge with validate= and the count habit carried from Wednesday (40 min).
5. Chained transformations and performance basics: vectorised beats loops (30 min).
6. Tool judgment: SQL against pandas against Excel; the Excel demo segment, pivot plus XLOOKup plus presenting a number (50 min).
7. Guided then unguided feature-table build; Kahoot and close (40 min).

### Learner outcome

UNDERSTANDS: groupby is the accumulator automated, reshape changes the question a table answers, validate= turns Wednesday's silent fan-out into a loud error, and tool choice is a judgment with reasons.
CAN DO: build the feature table with groupby, agg, pivot and a validated merge, and demonstrate a pivot and an XLOOKUP in Excel.
CAN HANDLE: a MergeError raised on duplicate keys, a reshaped table that answers the wrong question, and a stakeholder who wants the numbers in a form they can poke.
CAN DEFEND: the tool-choice note: which of SQL, pandas or Excel answers a given question, and why.

### Subtopics

• groupby and agg; named aggregations
• Reshape: pivot_table and melt
• Multi-source merges with validate= and count checks
• Chained transformations
• Performance basics: vectorised against loops
• SQL against pandas against Excel: the judgment
• Excel demo: pivot table, XLOOKUP, presenting a number
• The feature table and the tool-choice note

### Trainer notes

START FROM: they built the segment summary by hand (W1 Thursday) and validated joins (Wednesday). Every pandas move today lands on something they did manually, and saying so is the teaching.
GO AS FAR AS: every learner ships the feature table plus the tool-choice note, and has personally built one pivot and one XLOOKUP in Excel.
STOP BEFORE: MultiIndex depth, time series, apply with custom functions, performance tuning beyond the one contrast. The full Excel-for-analysts day is recommended for Week 4; today's Excel segment is a demonstration, said plainly.
COMES LATER: Build 1 next week uses all of it on raw messy data; Week 4 carries the deeper analyst craft.
BREAKS TO RUN: pandas.errors.MergeError: Merge keys are not unique in right dataset, raised by validate='one_to_one' on Wednesday's planted duplicates, the loud version of the fan-out; then the wrong-output reshape: a pivot on the wrong index answers a question nobody asked, caught by reading the row labels aloud.
CUT FIRST if time slips: melt (name it, park it), then the performance contrast. Never cut validate= or the Excel hands-on minutes.
NOTE: current pandas docs cover pandas 3.0; teach the current API and avoid deprecated idioms from older tutorials.

### Client zero and case studies

TODAY'S DATA: the two scenario tables plus the joined output; the feature table per segment is the artifact and the first input the ML module will later touch.
INTEGRATION: the spiral closes its data-manipulation turn: the same records have now passed through plain Python, files, SQL and pandas, and the learner has seen each tool earn its place.
COMPETENCY BUILT: manipulate at depth and choose tools with reasons; the analyst's daily loop.
CASE: JPMorgan's 2013 London Whale task force report described the risk model running on manual Excel copy-paste with a formula error that understated risk, on a trade that lost more than USD 6 billion; tool choice and validation are business controls rather than taste.

### In-session exercises

GUIDED: the one-line groupby beside the Week 1 accumulator, then agg with two measures together.
UNGUIDED: build the feature table (three grouped measures, one pivot, one validated merge) and write the tool-choice note, no hints, solution at close.
MID-SESSION (15 min each): predict the output shape of four groupby and pivot calls; pick SQL, pandas or Excel for five one-line business asks and justify.

### After-class tasks

• BUILD: extend the feature table with one more grouped measure and one reshaped view.
• READ: 10 minutes to pandas, the Grouping and Merge sections.
• RECAP: three lines, one per tool, on when it is the right call.
• PREP: tomorrow's four-hour block is spoken Q&A on the fortnight; reread your two insight notes.

### Trainer resources

• pandas, 10 minutes to pandas, current docs cover pandas 3.0 (verified 05 Sep 2026):
https://pandas.pydata.org/docs/user_guide/10min.html
• pandas user guide index: open Group by and Merging (verified 05 Sep 2026):
https://pandas.pydata.org/docs/user_guide/index.html
• Microsoft Support, create a PivotTable (verified 05 Sep 2026):
https://support.microsoft.com/en-us/office/create-a-pivottable-to-analyze-worksheet-data-a9a84538-bfe9-40a9-a8e9-f99134456576
• Microsoft Support, XLOOKUP function (verified 05 Sep 2026):
https://support.microsoft.com/en-au/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929

### Student references

• pandas, 10 minutes to pandas, run it cell by cell (verified 05 Sep 2026):
https://pandas.pydata.org/docs/user_guide/10min.html
• Microsoft Support, XLOOKUP function, redo today's lookup on your own sheet (verified 05 Sep 2026):
https://support.microsoft.com/en-au/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929

### Kahoot quiz plan

• Q1: groupby in one sentence: split, apply, combine on what
• Q2: agg with two measures on two groups; predict the output shape
• Q3: pivot against melt: which widens and which lengthens
• Q4 trap: which merge argument raises on duplicate keys, and which error
• Q5: a loop against a vectorised column operation on a million rows; which wins and why
• Q6: the stakeholder wants to poke the numbers themselves; SQL, pandas or Excel
• Return question from Thursday, one level up: top-3 per segment, say the window spec aloud.

## Sat 10 Oct 2026 · Saturday recap: the pen-and-paper test, then the interview-answer discussion

### Trainer agenda

Four hours, no new content.
1. Weekly recap test: pen and paper, AI-free, built from the week's interview question set, short-answer format (120 min).
2. Break (20 min).
3. Solution discussion led by the Academic TA: papers swapped for peer cross-evaluation, every answer discussed as an interview answer, random call-outs throughout (75 min).
4. Doubt clearing and the bridge: Build 1 opens Monday with the Programme Head's online project introduction (25 min).

### Learner outcome

CAN DO: answer the week's interview set on paper, without an assistant, in short-answer form.
CAN DEFEND: any of those answers aloud when called, and mark a peer's paper against the discussed solution.
STATUS: ungraded; the score is a performance indicator the programme reads, never a marks component.

### Subtopics

THE QUESTION SET (questions only; answers are built at the detailing phase):
• [S] WHERE against HAVING, one sentence each.
• [S] INNER against LEFT join: what does each drop or keep?
• [F] Your LEFT join grew the row count: name the cause and the check.
• [S] RANK, DENSE_RANK and ROW_NUMBER on a tie.
• [F] Top-3 per group: GROUP BY or a window function, and why?
• [S] groupby in the split-apply-combine sentence.
• [F] What does p = 0.03 mean, and what does it not mean?
• [D] SQL, pandas or Excel: how do you choose for a given ask?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. The tagging is this programme's own calibration for 0-3 year Indian-market candidates.

### Trainer notes

FORMAT: the paper is built from this row's question set, framed for short answers (selection, one-liners, small computations) so peer cross-checking works; answers themselves are written at the detailing phase, never improvised on the day.
DISCUSSION: papers swap for peer cross-evaluation; the Academic TA leads the solution walk-through as an interview-answer discussion, with random call-outs throughout.
STATUS: ungraded, a performance indicator rather than a marks component, and AI-free by format.

### Client zero and case studies

Answers must cite the scenario's own numbers and artifacts where the week produced them; the fortnight's pipeline from raw records to insight note is the reference.

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

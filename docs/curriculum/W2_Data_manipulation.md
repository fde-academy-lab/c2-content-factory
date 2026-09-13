# W2 Data manipulation

## Mon 05 Oct 2026 · SQL foundations · The revenue tree as queries the warehouse runs every Monday

### Business scenario of the day

Your note carried the growth review. Meera accepted 'real, modest, fix frequency' and parked marketing's acquisition budget. Then the CFO, Anand, made a request that changes the team's job: "I want these numbers every Monday, for every segment and channel, computed from the warehouse itself. No notebooks, no exports, nothing a person can mistype. Our data team will give you read access to Postgres."
The data platform lead sends credentials and a warning: "The warehouse holds the same orders and customers you cleaned last week, one thousand orders for the two quarters, already de-duplicated. Query it; do not export it."
Your role: you deliver the Monday suite and Anand's analyst will audit it line by line; be ready to explain why each query is written the way it is.
On the table: how to reproduce last week's revenue tree as queries that run unchanged every Monday; which of last week's Python steps become one line of SQL, and which do not; how do we keep a query readable enough for Anand's analyst to check; where does SQL stop and Python have to start again.

### Thinking we train, before any tool

A query describes the result; the database decides how. The logical order (FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY) explains most beginner errors, and the analyst reads a query in that order regardless of how it is written.
Every step of last week's tree has a SQL counterpart: counting is COUNT, summing is SUM, grouping by segment is GROUP BY, the threshold filter is WHERE, and the two-quarter comparison is a CTE per quarter joined on segment. The learner already knows every right answer from Week 1, so today's attention goes entirely to the language. The trainer's contrast on screen is the point: Tuesday's thirty-line Python profiler beside three lines of SQL.

### Trainer agenda

1. Anand's ask; the room lists what 'from the warehouse itself' rules out (10 min).
2. First-use tool established: the live Postgres connection from VS Code, a .sql file, run and read; the schema browsed (30 min).
3. SELECT, FROM, WHERE; ORDER BY and LIMIT; the Week 1 leaf counts re-answered one by one (45 min).
4. Aggregates, GROUP BY and HAVING; the logical execution order walked aloud; revenue and orders per segment per quarter (50 min).
5. Readable structure: subqueries, then CTEs as named steps; the two-quarter comparison as two CTEs (40 min).
6. Guided then unguided: the Monday extraction suite, no hints, solution at close (45 min).
7. Kahoot and close-out (20 min).

### Learner outcome

UNDERSTANDS: a query describes the result, the logical execution order explains most errors, and a CTE is a named step that keeps a query auditable.
CAN DO: connect to the warehouse from VS Code, write filtered, ordered and aggregated queries that reproduce the Week 1 tree, and structure the quarter comparison as CTEs.
CAN HANDLE: the GROUP BY column error, a WHERE that belonged in HAVING, and LIMIT without ORDER BY returning arbitrary rows.
CAN DEFEND: why WHERE and HAVING both exist, what the database guarantees about row order (nothing without ORDER BY), and why Anand's Monday number is now safer than last week's.

### Subtopics (technique in service of the scenario)

• The Postgres connection from VS Code; .sql files against a live database; reading a schema
• SELECT, FROM, WHERE; ORDER BY and LIMIT
• Aggregate functions; GROUP BY and HAVING
• The logical execution order
• Subqueries, then CTEs as named steps
• The Week 1 tree re-expressed as the Monday extraction suite

### Trainer notes

START FROM: zero SQL, and a room that knows every answer from Week 1, which is the whole advantage: attention goes to the language.
GO AS FAR AS: every learner ships the extraction suite: the tree's leaves by segment and quarter, and one CTE-structured comparison.
STOP BEFORE: joins (tomorrow), window functions (Wednesday), DDL beyond reading the schema, indexes and performance.
COMES LATER: joins tomorrow answer 'collected against billed'; Thursday's pandas day re-expresses the same tree a third time and the room sees three tools answer one question.
WHAT THE DATA REVEALS: ERROR: column "segment" must appear in the GROUP BY clause or be used in an aggregate function, read aloud and fixed two ways; then LIMIT 5 without ORDER BY gives two learners different answers to the same question.
CUT FIRST: subqueries (go straight to CTEs). Never cut the execution-order walk or the GROUP BY error.

### Client zero data (TRAINER ONLY)

VERSION v4: 1,000 orders and their customers as Postgres tables, de-duplicated, same segments and channels, same bulk order, loaded in advance.
PLANTED: exact amount ties in the top ten for Wednesday's RANK demonstration; the campaigns table present but unused until Thursday.
Nothing new is planted for today; the contrast with Week 1 carries the teaching.

### In-session exercises

GUIDED: the segment count and the revenue aggregate built together, execution order narrated.
UNGUIDED: the Monday suite, six queries that reproduce the Week 1 tree by segment and quarter, no hints, solution at close.
MID-SESSION (15 min each): predict the row count of four queries before running; put five clauses in logical execution order and defend one placement.

### After-class tasks

• BUILD: two more extraction queries on questions Anand's analyst might ask, each with a one-line comment stating the question.
• PRACTICE: SQLBolt lessons 1 to 5, interactive.
• RECAP: the execution order written from memory in a .sql comment.

### Interview angle

• [S] WHERE against HAVING, one sentence each.
• [S] Explain the logical order in which a SQL query executes.
• [F] Why would you compute a KPI in the warehouse rather than in a notebook?
• [F] What does LIMIT without ORDER BY return?
• [D] A stakeholder's analyst must audit your query; what changes in how you write it, and what would you refuse to compute in a notebook?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

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
• Q3: predict the row count of a GROUP BY segment, quarter on the scenario table
• Q4: LIMIT 5 without ORDER BY returns which five rows
• Q5: read a two-block CTE and name what the second block can see
• Q6: last week's presence counter in one SQL line
• Return question from Week 1 Thursday, one level up: the discount's 6 percent lift was a mix effect; say in one line what a fair comparison would need.

## Tue 06 Oct 2026 · SQL joins and join semantics · Booked against collected: joining payments without lying

### Business scenario of the day

Anand's Monday numbers arrive and he replies with a harder question: "Booked revenue is not collected revenue. Some orders are paid in two instalments, some are refunded, some were never paid at all. Show me, order by order, what we actually collected against what we booked in Q2. If there is a gap, I want to know which orders and which channel."
The platform lead adds the payments table to your access and mentions, in passing, that the payments feed 'sometimes double-posts when the gateway retries'.
Your role: you sign off the collected-revenue number, and Anand will ask how you know it is not double-counted before he uses it.
On the table: how to attach payments to orders without inflating or losing anything; what each kind of join drops or duplicates; how do we prove a join is right before Anand sees a number from it; which orders have no payment at all, and which have more than one.

### Thinking we train, before any tool

Each join type answers a different question about unmatched rows: INNER keeps only matches, LEFT keeps every order whether paid or not, FULL OUTER keeps both sides' orphans. An imperfect key multiplies rows before it loses them: an order with two payment rows appears twice, and a revenue SUM over that join double-counts silently while every row looks plausible.
So a join is only done when its row count is explained: rows before, rows after, and the difference accounted for. The anti-join (LEFT JOIN where the right side is NULL) finds the unpaid orders Anand asked about. The habit is the Trust thread in SQL form, and it is the reconciliation Wednesday of Week 1 taught, one tool later.

### Trainer agenda

1. Anand's ask and the gateway remark; the room predicts what double-posting does to a naive join (10 min).
2. INNER and LEFT on two tiny tables, row by row on the board (45 min).
3. RIGHT and FULL OUTER completed; what each join drops or duplicates (30 min).
4. Imperfect keys and fan-out: one-to-many multiplication, counted live on the payments feed (45 min).
5. The validation habit: row counts before and after, the revenue bridge, and the anti-join for unpaid orders (40 min).
6. Guided then unguided: the booked-against-collected report by channel, with the count reconciliation in comments (50 min).
7. Kahoot and close-out (20 min).

### Learner outcome

UNDERSTANDS: each join answers a different question about unmatched rows, an imperfect key multiplies before it loses, and a join is only done when its row count is explained.
CAN DO: choose and write the right join, validate it with before-and-after counts and a revenue bridge, and find unpaid and double-paid orders with anti-joins and HAVING.
CAN HANDLE: a fan-out that doubles collected revenue while looking plausible, an INNER join that silently drops unpaid orders, and a gateway retry that posted twice.
CAN DEFEND: the booked-against-collected report, the join choice behind it, and the count arithmetic that proves it honest.

### Subtopics (technique in service of the scenario)

• INNER, LEFT, RIGHT and FULL OUTER
• What each join drops or duplicates
• Keys, imperfect keys and fan-out
• Row-count validation before and after; the revenue bridge
• The anti-join for orphans; HAVING COUNT for double payments
• The booked-against-collected report by channel

### Trainer notes

START FROM: Monday's queries. Open on the wrong number, then teach the machinery that explains it; application before theory.
GO AS FAR AS: every learner ships the report with a written count reconciliation, the unpaid list, and the double-paid list.
STOP BEFORE: self-joins, CROSS JOIN beyond a one-line mention, join algorithms and performance.
COMES LATER: window functions tomorrow rank customers on the joined table; Thursday's pandas merge does this again with validate= as the loud version.
WHAT THE DATA REVEALS: a LEFT JOIN to payments grows 1,000 rows to 1,450 and collected revenue doubles; the count check catches it, the HAVING COUNT(*) > 1 lists the double posts, and the anti-join lists the unpaid orders. Let the room find the doubling before naming fan-out.
CUT FIRST: FULL OUTER (name it, park it). Never cut the count validation or the fan-out.

### Client zero data (TRAINER ONLY)

VERSION v4: the payments table joins the warehouse; orders and customers unchanged.
PLANTED: 50 orders with two payment rows each (gateway retries), a handful of orphan payments with no order, and 30 delivered orders with no payment at all.
Anand's gap is computable: booked minus collected, by channel. Students find the double posts and the unpaid orders; neither is announced.

### In-session exercises

GUIDED: INNER and LEFT on the tiny tables together, rows traced on the board before any query runs.
UNGUIDED: booked against collected by channel, the count reconciliation in a comment block, the unpaid list, the double-paid list, no hints, solution at close.
MID-SESSION (15 min each): predict four row counts before running the joins; match five business questions to the join type that answers each.

### After-class tasks

• BUILD: one more join question of your own on the two tables, with the count reconciliation in comments.
• PRACTICE: SQLBolt lessons 6 to 8, the join lessons.
• RECAP: one comment line on when an INNER join is the honest choice.

### Interview angle

• [S] INNER against LEFT join: what does each drop or keep?
• [S] Your join grew the row count; name the cause and the check.
• [F] How do you find orders with no payment?
• [F] Revenue doubled after a join and every row looks fine; where do you look?
• [D] Design the validation you run before a joined number reaches Finance, and say what you do when it fails at 5 pm on reporting day.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• pgtutorial.com, the joins pages (verified 05 Sep 2026):
https://www.pgtutorial.com/
• SQLBolt, lessons 6 to 8, joins and NULLs (verified 05 Sep 2026):
https://sqlbolt.com/
• PostgreSQL Exercises, the joins category for stretch (verified 05 Sep 2026):
https://pgexercises.com/

### Student references

• SQLBolt, lessons 6 to 8 tonight (verified 05 Sep 2026):
https://sqlbolt.com/
• PostgreSQL Exercises, joins category, first three (verified 05 Sep 2026):
https://pgexercises.com/

### Kahoot quiz plan

• Q1: LEFT join keeps unmatched rows from which side
• Q2: 1,000 orders LEFT JOIN payments where 50 orders have two payments; predict the row count
• Q3 trap: what does an INNER join do silently to unpaid orders
• Q4: the anti-join in words: orders with no payment
• Q5: collected revenue doubled after a join; the first check
• Q6: HAVING COUNT(*) > 1 on payments grouped by order finds what
• Return question from Monday, one level up: WHERE against HAVING, one sentence each.

## Wed 07 Oct 2026 · SQL window functions · Top members, falling spend, and the running total against plan

### Business scenario of the day

The growth plan takes shape. Marketing, now working with the data team rather than around it, asks two things: "Retail-Plus frequency is the problem, so we want to protect our best members before they drift. Give us the top fifty customers by Q2 revenue in each segment, and flag anyone whose monthly spend has fallen for two months running. And Meera wants to see revenue accumulate week by week against the plan line, so we know by mid-quarter whether we are on track."
The head of Retail-Plus adds: "Ties matter. If two members spent the same, I want them ranked the same, and I want to know how many made the top fifty, not forty-nine because of a tie."
Your role: Marketing will act on your list, so you must state the tie rule you chose and why, and defend the falling-spend flag against a member who says he was on holiday.
On the table: how to rank within a segment rather than across the whole table; how do we compare a customer's month with their own previous month; how do we show revenue accumulating without collapsing the rows; which questions can GROUP BY never answer.

### Thinking we train, before any tool

GROUP BY collapses rows to answer 'how much per group'. Marketing's questions keep the rows and ask about each row's neighbours: its rank within its segment, its own previous month, the total so far. That is what a window function does, and the partition plus its internal order define everything.
The tie is the day's judgment call: RANK leaves a gap after a tie, DENSE_RANK does not, ROW_NUMBER breaks the tie arbitrarily, and the head of Retail-Plus has just told you which behaviour he wants. LAG reads the previous row, so 'fallen for two months running' is two LAGs and a comparison. A running total is only deterministic when its order is unambiguous, which is why the plan line needs a date order and a tiebreaker.

### Trainer agenda

1. Marketing's two asks; the GROUP BY attempt that cannot produce a top fifty per segment (10 min).
2. ROW_NUMBER, RANK and DENSE_RANK on a tie, side by side, and which one the head of Retail-Plus asked for (40 min).
3. PARTITION BY and ORDER BY inside the window; top-N per segment (45 min).
4. LAG and LEAD; falling for two months running; the running total against the plan line and what makes it deterministic (45 min).
5. Guided then unguided: the protect list, the falling-spend flag, and the running total (55 min).
6. Kahoot and close-out (20 min).

### Learner outcome

UNDERSTANDS: a window function computes across related rows without collapsing them, the partition plus its order define the result, and tie handling is a business choice expressed in a function name.
CAN DO: rank within segments with the tie behaviour the business asked for, compare a row with its previous row using LAG, build a deterministic running total, and answer top-N per group.
CAN HANDLE: RANK returning 1, 1, 3 where the room expected 1, 1, 2, a window function refused inside WHERE, and a running total that changes between runs because its order was ambiguous.
CAN DEFEND: GROUP BY or window for any question Marketing asks, and the tie rule chosen for the top fifty.

### Subtopics (technique in service of the scenario)

• ROW_NUMBER, RANK and DENSE_RANK, and what a tie does to each
• PARTITION BY; ORDER BY inside the window
• Top-N per group
• LAG and LEAD; month-on-month comparison per customer
• Running totals and determinism
• Filtering on a window via a CTE

### Trainer notes

START FROM: yesterday's joined, validated table. Open on the question GROUP BY cannot answer, so the new tool arrives as the missing piece.
GO AS FAR AS: every learner ships the protect list with the requested tie rule, the falling-spend flag, and the running total against plan.
STOP BEFORE: frame clauses (ROWS BETWEEN), named windows, percentiles, performance.
COMES LATER: Thursday's pandas day mirrors ranks with groupby transforms; Week 4's cohorts use LAG's cousin, the retention curve.
WHAT THE DATA REVEALS: the planted tie makes RANK return 1, 1, 3 and the top-fifty report ships fifty-one rows under one rule and forty-nine under another; then ERROR: window functions are not allowed in WHERE, fixed by filtering in a CTE.
CUT FIRST: LEAD (teach LAG, name LEAD), then the running-total variant. Never cut the tie demonstration.

### Client zero data (TRAINER ONLY)

VERSION v4: the joined orders and payments; monthly spend per customer derivable.
PLANTED: exact ties in Q2 revenue at the fiftieth position in Retail-Plus; three members whose spend fell two months running; the plan line as a small table.
The tie decides the day; the room meets it in the top-fifty output rather than on a slide.

### In-session exercises

GUIDED: the tie demonstration built together, three ranking functions on one screen, then the head of Retail-Plus's choice applied.
UNGUIDED: top fifty per segment with the chosen tie rule, the two-months-falling flag with LAG, one running total against plan, no hints, solution at close.
MID-SESSION (15 min each): predict the three rankings for a four-row tie; say GROUP BY or window for six Marketing questions.

### After-class tasks

• BUILD: one ranking question of your own plus its GROUP BY impostor, with a comment on why they differ.
• PRACTICE: PostgreSQL Exercises, window functions category, first three.
• RECAP: RANK, DENSE_RANK and ROW_NUMBER on the same tie, from memory, in a comment.

### Interview angle

• [S] RANK, DENSE_RANK and ROW_NUMBER on a tie.
• [S] Top-3 per group: GROUP BY or a window, and why?
• [F] How would you find customers whose spend fell two months in a row?
• [F] Why can a window function not sit inside WHERE, and what do you do instead?
• [D] The business says 'ties rank the same'; which function, and how many rows might the top-N report ship?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

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
• SQLBolt for anyone still shaky on joins (verified 05 Sep 2026):
https://sqlbolt.com/

### Kahoot quiz plan

• Q1: RANK, DENSE_RANK and ROW_NUMBER on a two-way tie; give all three outputs
• Q2: PARTITION BY resets what
• Q3: LAG(spend) on the first month of a customer returns what
• Q4: which ORDER BY makes a running total deterministic
• Q5 trap: a window function inside WHERE; why refused and the fix
• Q6: the business wants ties ranked the same; which function and why
• Return question from Tuesday, one level up: your LEFT join grew rows; name the cause and the check.

## Thu 08 Oct 2026 · pandas groupby, merge and reshape · The customer table Marketing refreshes every Monday

### Business scenario of the day

The growth team now wants one thing every week: a single table with one row per customer, refreshed on Monday, carrying how recently they bought, how often, how much, their segment, whether the monsoon sale reached them, and last week's flags. The platform lead is blunt: "The warehouse queries are fine for Finance, but Marketing's analysts live in Python. Build them the table in pandas, from the warehouse, and make it refreshable in one run."
A senior analyst on the team challenges the group: "You did the tree in plain Python in Week 1, in SQL on Monday. Do it a third way now, and tell me honestly which tool you would pick for which job."
Your role: you answer the senior analyst in writing, with a reason per tool, and you will be asked which tool you would refuse to use for Finance's numbers.
On the table: how a one-row-per-customer table is built from order rows; which pandas operations mirror GROUP BY, JOIN and LAG; how do we make a merge fail loudly instead of doubling rows; when the same question has three tools, how do we choose.

### Thinking we train, before any tool

The customer table is the accumulator from Week 1 automated: groupby splits the orders by customer, agg applies the recency, frequency and monetary computations, and the result combines into one row each. A merge is a join, and Tuesday's fan-out returns here as pandas.errors.MergeError when validate= is set, which is the loud version of the count check. A reshape changes the question a table answers: months as rows for a trend, months as columns for a comparison.
The three-tool re-expression is the day's judgment: plain Python for a one-off you must explain line by line, SQL for anything the warehouse should own and Finance should audit, pandas for the analyst's iterative work in between. Choosing is a defence with reasons, and the senior analyst's challenge is answered in writing.

### Trainer agenda

1. The growth team's one-table ask; the room lists the columns and where each comes from (15 min).
2. From the warehouse into pandas: read_sql, then groupby and agg with named aggregations; the Week 1 accumulator beside the one-liner (50 min).
3. Merge with validate=: campaign exposure joined per customer, and the fan-out that now raises (40 min).
4. Reshape: pivot_table for months as columns, melt back; the trend view and the comparison view (35 min).
5. The three-tool re-expression: the same tree node in plain Python, SQL and pandas on one screen; the room tries the SQL version, then the trainer runs it through Python and closes the loop (45 min).
6. Unguided: the customer table with a validated merge and one reshaped view, plus the tool-choice note (40 min).
7. Kahoot and close-out (20 min).

### Learner outcome

UNDERSTANDS: groupby is the accumulator automated, a merge is a join and validate= makes fan-out loud, a reshape changes the question a table answers, and tool choice is a judgment with reasons.
CAN DO: read from the warehouse into pandas, build the customer table with groupby and agg, merge campaign exposure with validation, reshape for a trend and a comparison, and run one question through all three tools.
CAN HANDLE: a MergeError raised on duplicate keys, a pivot on the wrong index that answers a question nobody asked, and a chained transformation that silently changed a dtype.
CAN DEFEND: the tool-choice note: which of plain Python, SQL and pandas answers which of Marketing's and Finance's asks, and why.

### Subtopics (technique in service of the scenario)

• read_sql from the warehouse into a DataFrame
• groupby and agg; named aggregations; the customer table (recency, frequency, monetary)
• merge with validate= and the count habit
• Reshape: pivot_table and melt
• Chained transformations and dtype checks
• The three-tool re-expression and the tool-choice note

### Trainer notes

START FROM: three days of SQL and the Week 1 accumulators; every pandas move lands on something the room did by hand, and saying so is the teaching.
GO AS FAR AS: every learner ships the customer table, one reshaped view, and the tool-choice note, and has run one question through all three tools.
STOP BEFORE: MultiIndex depth, time-series indexing, apply with custom functions, performance tuning beyond the one vectorised contrast.
COMES LATER: tomorrow the number reaches the leadership deck through Excel; Week 4's cohorts and baskets run on this customer table; Week 5's model trains on it.
WHAT THE DATA REVEALS: pandas.errors.MergeError: Merge keys are not unique in right dataset, raised by validate='one_to_one' on the campaigns exposure, the loud version of Tuesday's fan-out; then the wrong-output pivot, a table indexed by the wrong key, caught by reading its row labels aloud.
CUT FIRST: melt (name it, park it), then the vectorised contrast. Never cut validate= or the three-tool re-expression.
NOTE: current pandas docs cover pandas 3.0; teach the current API and avoid deprecated idioms from older tutorials.

### Client zero data (TRAINER ONLY)

VERSION v4: the warehouse tables plus the campaigns exposure table.
PLANTED: duplicate customer keys in the exposure table so validate= raises; a customer whose months pivot wrongly if indexed by order rather than customer.
The customer table built today is the seed of the Week 5 feature table; say that aloud.

### In-session exercises

GUIDED: the one-line groupby beside the Week 1 accumulator, then agg with three measures together, then one validated merge.
UNGUIDED: the full customer table (recency, frequency, monetary, segment, exposure, the two flags), one reshaped view, and the tool-choice note, no hints, solution at close.
MID-SESSION (15 min each): predict the output shape of four groupby and pivot calls; pick plain Python, SQL or pandas for five one-line asks and justify.

### After-class tasks

• BUILD: extend the customer table with one more grouped measure and one reshaped view.
• READ: 10 minutes to pandas, the Grouping and Merge sections.
• PREP: tomorrow is the Excel day; bring the customer table exported as a CSV.

### Interview angle

• [S] groupby in the split-apply-combine sentence.
• [S] merge against join: what is the same and what differs?
• [F] Which merge argument raises on duplicate keys, and which error?
• [F] pivot against melt: which widens and which lengthens?
• [D] Same question, three tools: how do you choose, and defend one choice?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• pandas, 10 minutes to pandas, current docs cover pandas 3.0 (verified 05 Sep 2026):
https://pandas.pydata.org/docs/user_guide/10min.html
• pandas user guide index: open Group by and Merging (verified 05 Sep 2026):
https://pandas.pydata.org/docs/user_guide/index.html
• PostgreSQL Exercises for the SQL side of the re-expression (verified 05 Sep 2026):
https://pgexercises.com/

### Student references

• pandas, 10 minutes to pandas, run it cell by cell (verified 05 Sep 2026):
https://pandas.pydata.org/docs/user_guide/10min.html
• pandas user guide index, the Merging guide (verified 05 Sep 2026):
https://pandas.pydata.org/docs/user_guide/index.html

### Kahoot quiz plan

• Q1: groupby in one sentence: split, apply, combine on what
• Q2: agg with two measures on two groups; predict the output shape
• Q3 trap: which merge argument raises on duplicate keys, and which error
• Q4: pivot against melt: which widens and which lengthens
• Q5: Finance's Monday number: plain Python, SQL or pandas, and why
• Q6: the customer table has 1,000 rows and the merge returned 1,120; what happened
• Return question from Wednesday, one level up: the business wants ties ranked the same; which function, and how many rows might the top fifty ship.

## Fri 09 Oct 2026 · Excel for analysts · The number reaches the leadership deck, and the tool judgment behind it

### Business scenario of the day

Meera's office runs on Excel. Her chief of staff writes: "Monday's growth review deck needs three things I can open on my laptop without a login: the revenue tree by segment for both quarters, the top-fifty protect list with a lookup so I can find any member by id, and one number on the front page with its trend. Nothing that needs Python. If a director changes an assumption in the room, the sheet must recalculate in front of them."
The senior analyst repeats yesterday's challenge in a new form: "Everything you built this week has to survive a room that only has Excel. Which parts belong in Excel, which parts must never be in Excel, and how do you keep the two from drifting apart?"
Your role: a director will change an assumption in the room and expect your sheet to hold; you need to say what it can and cannot be trusted for.
On the table: how the customer table becomes a pivot a director can slice live; how does a lookup answer 'find this member' without a query; how is one number presented so it is read correctly in two minutes; where does Excel end and the warehouse begin.

### Thinking we train, before any tool

Excel is where analysis meets its audience; the analyst's job is to keep the sheet honest under a director's hand: the pivot must be built on the clean customer table so slicing cannot invent a number, the lookup must fail visibly on a missing id rather than return a neighbour, and the front-page number must carry its denominator, its period and its comparison or it will be misread.
The judgment is the day's real content. Excel presents and lets a stakeholder explore; it does not clean, join or compute the source of truth, because a sheet with a typed-over cell has no audit trail. The warehouse owns the numbers, pandas owns the analyst's iteration, Excel owns the last mile. The tool-choice note from yesterday becomes a one-page operating rule for the team.

### Trainer agenda

1. The chief of staff's three asks; the room says which Excel should own and which it must not (15 min).
2. The customer table opened in Excel; a pivot built on it, sliced by segment and quarter live; what a pivot can and cannot do (50 min).
3. Lookups: XLOOKUP for 'find this member', and the wrong-answer failure of a lookup that returns a neighbour (35 min).
4. Presenting one number: denominator, period, comparison, and the sentence beside it; the front-page card built (35 min).
5. The operating rule: what lives in the warehouse, in pandas, in Excel, and how the three are kept from drifting; the rule written as a team note (35 min).
6. Unguided: the three deliverables for Monday's deck, refreshable from the exported customer table (50 min).
7. Kahoot, close-out, and the Build 1 preview (20 min).

### Learner outcome

UNDERSTANDS: Excel is the last mile that presents and explores, a pivot is only as honest as the table under it, a lookup must fail visibly, and a single number is read correctly only with its denominator, period and comparison.
CAN DO: build a slicable pivot on the customer table, an XLOOKUP that surfaces missing ids, and a front-page number card; and write the team's tool operating rule.
CAN HANDLE: a lookup returning the nearest match instead of an error, a pivot that double-counts because the source had duplicates, and a director who changes an assumption in the room.
CAN DEFEND: which parts of the week's work belong in Excel, which never, and why the warehouse stays the source of truth.

### Subtopics (technique in service of the scenario)

• The customer table in Excel: structure, filters, freeze panes
• Pivot tables: build, slice, refresh; what they cannot do
• XLOOKUP: exact match, the not-found path, and the nearest-match trap
• Presenting one number: denominator, period, comparison, the sentence beside it
• The tool operating rule: warehouse, pandas, Excel
• Keeping the sheet and the source from drifting

### Trainer notes

START FROM: the week's customer table exported yesterday. Every Excel move lands on data the room built, which is why the pivot's numbers are already known.
GO AS FAR AS: every learner ships the three deliverables and the operating rule, and has watched a pivot double-count once.
STOP BEFORE: macros, Power Query, dashboards beyond the one card, financial modelling.
COMES LATER: Build 1 next week asks for exactly this last mile on unfamiliar data; Week 4's metric design decides what goes on the front page.
WHAT THE DATA REVEALS: the pivot built on the raw export double-counts the fifty double-paid orders until it is rebuilt on the cleaned table; XLOOKUP with approximate match returns a neighbouring member for a missing id, and the room catches it only because they know the id is missing. Let both happen.
CUT FIRST: the number-card styling. Never cut the pivot double-count or the operating rule.

### Client zero data (TRAINER ONLY)

VERSION v4 exported: the customer table as CSV, plus a raw export that still contains the double-paid rows.
PLANTED: the raw export for the double-count; one member id absent so the lookup trap fires.
The chief of staff's three asks are all buildable from the clean export; the room learns why the raw one is wrong.

### In-session exercises

GUIDED: the pivot built together on the clean table, then rebuilt on the raw export to watch it double-count.
UNGUIDED: the three deliverables for Monday's deck plus the one-page operating rule, no hints, solution at close.
MID-SESSION (15 min each): decide warehouse, pandas or Excel for eight asks and justify two; spot the misread in three front-page numbers missing a denominator, a period or a comparison.

### After-class tasks

• BUILD: rebuild the three deliverables from a fresh export tonight; if any number moves, find out why.
• RECAP: the operating rule in three lines, one per tool.
• PREP: Build 1 opens Monday in Kalpa Health with the Programme Head's online introduction; reread this week's two notes to Meera and Anand.

### Interview angle

• [S] SQL, pandas or Excel: how do you choose?
• [S] A stakeholder wants to poke the numbers themselves; what do you give them and what do you never give them?
• [F] Your pivot shows a different total from the warehouse; where do you look first?
• [F] How do you present one number so it is not misread?
• [D] Two directors change assumptions in the room and the sheet recalculates differently for each; what did you get right and what do you fix?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer resources

• Microsoft Support, create a PivotTable (verified 05 Sep 2026):
https://support.microsoft.com/en-us/office/create-a-pivottable-to-analyze-worksheet-data-a9a84538-bfe9-40a9-a8e9-f99134456576
• Microsoft Support, XLOOKUP function incl. the not-found argument (verified 05 Sep 2026):
https://support.microsoft.com/en-au/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929
• Exponent, data analyst questions incl. the dashboard-against-finance mismatch (verified 13 Sep 2026):
https://www.tryexponent.com/blog/top-data-analyst-interview-questions

### Student references

• Microsoft Support, create a PivotTable (verified 05 Sep 2026):
https://support.microsoft.com/en-us/office/create-a-pivottable-to-analyze-worksheet-data-a9a84538-bfe9-40a9-a8e9-f99134456576
• Microsoft Support, XLOOKUP function, redo today's lookup on your own sheet (verified 05 Sep 2026):
https://support.microsoft.com/en-au/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929

### Kahoot quiz plan

• Q1: the pivot's total is higher than the warehouse; first suspicion
• Q2 trap: XLOOKUP returned a member for an id that does not exist; which argument was wrong
• Q3: a front-page number without which three things will be misread
• Q4: the director changes an assumption; what must be true of the sheet for the recalculation to be honest
• Q5: warehouse, pandas or Excel for five asks, called fast
• Q6: which of the week's steps must never be done in Excel, and why
• Return question from Thursday, one level up: the merge returned 1,120 rows from 1,000 customers; what happened and which argument would have caught it.

## Sat 10 Oct 2026 · Saturday recap · The pen-and-paper test, then the interview-answer discussion

### Business scenario of the day

Two weeks of Kalpa under questioning. Anand has his Monday numbers, Marketing has its customer table, Meera has her deck. Build 1 opens Monday in a different unit, so today also rehearses the transfer: the same method, a company you have not seen.

### Thinking we train, before any tool

Saying the fortnight out loud is the interview skill itself.

### Trainer agenda

Four hours, no new content.
1. Weekly recap test: pen and paper, AI-free, built from the week's question set, short-answer format (120 min).
2. Break (20 min).
3. Solution discussion led by the Academic TA: papers swapped for peer cross-evaluation, every answer discussed as an interview answer, random call-outs throughout (75 min).
4. Doubt clearing and the bridge: Build 1 opens Monday in Kalpa Health; the method transfers, the domain does not (25 min).

### Learner outcome

CAN DO: answer the fortnight's business and technique questions on paper without an assistant.
CAN DEFEND: any answer aloud when called, and mark a peer's paper against the discussed solution.
STATUS: ungraded; a performance indicator, never a marks component.

### Subtopics (technique in service of the scenario)

THE QUESTION SET (questions only; answers are built at the detailing phase):
• [S] WHERE against HAVING, one sentence each.
• [S] INNER against LEFT join: what does each drop or keep?
• [S] RANK, DENSE_RANK and ROW_NUMBER on a tie.
• [S] groupby in the split-apply-combine sentence.
• [F] Your LEFT join grew the row count and revenue doubled; name the cause and the check.
• [F] Top-3 per segment: GROUP BY or a window, and why?
• [F] Which merge argument raises on duplicate keys, and which error?
• [F] A pivot's total disagrees with the warehouse; where do you look first?
• [D] Same question, three tools: how do you choose, and defend one choice?
• [D] Kalpa Health asks 'where does our growth come from'; say what stays the same in your method and what changes.
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. This programme's own calibration for 0-3 year Indian-market candidates.

### Trainer notes

FORMAT: the paper is built from this row's question set, framed for short answers so peer cross-checking works; answers themselves are written at the detailing phase.
DISCUSSION: papers swap for peer cross-evaluation; the Academic TA leads the solution walk-through as an interview-answer discussion, with random call-outs throughout.
STATUS: ungraded, a performance indicator rather than a marks component, and AI-free by format.

### Client zero data (TRAINER ONLY)

Answers cite Kalpa's own numbers from the fortnight. The findings are discussed; the plants are never revealed.

### In-session exercises

• The two-hour recap test on paper.
• Peer cross-evaluation against the discussed solution.
• Random call-outs: the called learner answers aloud in sixty seconds.

### After-class tasks

• RECAP: rewrite any question you lost marks on, one line each, in your own words.

### Interview angle

The question set in the Subtopics column is the interview set for the week.

### Trainer resources

• This row's question set is the paper's source; the weekday interview columns calibrate difficulty.
• GeeksforGeeks, Data Analyst interview questions (verified 03 Sep 2026):
https://www.geeksforgeeks.org/data-analysis/data-analyst-interview-questions-and-answers/

### Student references

• SQLBolt, redo any lesson that felt shaky (verified 05 Sep 2026):
https://sqlbolt.com/

### Kahoot quiz plan

None. The recap test and the discussion replace the quiz today.

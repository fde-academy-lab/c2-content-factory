# Week 2 recap paper: key

TRAINER. Rendered from the tracker's item bank and the week's source file by `scripts/build_saturday_paper.py`. Change an item in the tracker, an option in `data/programme/paper_edits.yaml` or anything in `content/W02/SAT/internal/C2_W02_SAT_paper_source_INTERNAL.yaml`, and rebuild; never edit this file by hand. A stem, a situation or an option can be reworded in `data/programme/paper_edits.yaml`.

Saturday 17 October 2026. A 120-minute paper holding 35 items at 117 minutes by the blueprint's pace: 2 easy, 12 medium and 21 hard. 31 of them are new and not yet in the tracker.

## Marking

1. Papers are swapped, so nobody checks their own.
2. The Academic TA reads the key out part by part, and the marker writes a tick or a cross beside each item.
3. An item is right when its answer matches the key: every correct letter and no other on a more-than-one item, the letter on a word-bank or match item, the number on an applied maths item (the working belongs to the discussion), and the whole sequence on an ordering item. The programme has set no partial-credit rule, so this key uses none.
4. The marker writes each part's ticks beside its rating on the answer sheet, and their total as Items right, out of 35, then hands the paper back.
5. The TA collects the papers and tallies the misses by tag, using the table below; that tally is Monday's remediation read. It is never a ranking and never read out by name.
6. The TA enters every paper in `C2_W02_SAT_item_analysis_TRAINER.xlsx` beside this key, by seat and never by name: 1 for a tick, 0 for a cross and a blank for an item left empty. The workbook orders the discussion from the most-missed item, flags any item to check, and gives each tag's rate for the room and for each seat.

## The blueprint

| Part | What it shows | Items | Minutes | Easy | Medium | Hard |
|---|---|---|---|---|---|---|
| 1. Anand's Monday numbers | whether you read a query the way the database runs it, and choose where a number Finance audits is computed | Q1 to Q6 (6) | 17.5 | 2 | 1 | 3 |
| 2. Booked against collected | whether you size a join before it runs, order the steps of a reconciliation, and decide what leaves when a check fails | Q7 to Q11 (5) | 20 | 0 | 0 | 5 |
| 3. The protect list and the plan line | whether you rank within a segment with the tie rule the business asked for, and read a monthly flag and a run rate before anyone acts | Q12 to Q16 (5) | 18.5 | 0 | 1 | 4 |
| 4. One row per customer | whether you size a merge, place the guard that stops a double count, and read a pivot that averages or a key that changed on its way in | Q17 to Q22 (6) | 19.5 | 0 | 3 | 3 |
| 5. The last mile, and spreadsheets in public | whether you match each workbook job to the technique that does it, and name the check that catches a spreadsheet error before the room sees it | Q23 to Q29 (7) | 20.5 | 0 | 5 | 2 |
| 6. Read the code, read the data: an AI team's tables | whether you catch the week's traps in the tables an AI team keeps, from evaluation runs to an assistant's logs | Q30 to Q35 (6) | 21 | 0 | 2 | 4 |
| Total | | 35 | 117 | 2 | 12 | 21 |

## What guessing alone would score

A learner who guessed every item blind would average 6.9 of 35, since a written answer cannot be guessed from a list, and fewer than one guesser in twenty would reach 12. A score of 11 or below is therefore within reach of guessing alone, and the tally reads such a paper as a conversation to have on Monday, never as a result.

## Reading the items after marking

The workbook flags an item to check when fewer than one learner in five got it right, or when the bottom third of the room got it right more often than the top third. Both are this programme's own working rule for a room of 35. A flagged item is discussed as usual; the TA also sends it, with the room's rate, to the tracker's owner, because the fault may sit in the item rather than in the learners.

## The key

| Q | Key | Type | Part | Level | Tag | Roles | Day | Min | Source | Interview anchor |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | c | One correct option | 1 | Hard | [F] | BA, DS | Mon | 4 | new | A stakeholder's analyst must audit your query; what changes in how you write it, and what would you refuse to compute in a notebook? |
| 2 | c, b, e, f, a, d | Order the steps | 1 | Medium | [S] | BA, DS | Mon | 2.5 | bank 57 | Explain the logical order in which a SQL query executes. |
| 3 | d (guarantee) | Fill in the blank | 1 | Easy | [F] | BA, DS | Mon | 1.5 | bank 2 | What does LIMIT without ORDER BY return? |
| 4 | b (CTE) | Fill in the blank | 1 | Easy | [S] | BA, DS | Mon | 1.5 | bank 3 | Explain the logical order in which a SQL query executes. |
| 5 | a | One correct option | 1 | Hard | [D] | BA, FDE | Mon | 4 | new | Why would you compute a KPI in the warehouse rather than in a notebook? |
| 6 | d | One correct option | 1 | Hard | [D] | BA, DS | Mon | 4 | new | How do you present one number so it is not misread? |
| 7 | b | Scenario set | 2 | Hard | [F] | BA, DS | Tue | 4 | new | Your LEFT join grew the row count and revenue doubled; name the cause and the check. |
| 8 | c, e, a, d, b | Order the steps | 2 | Hard | [D] | BA, DS, FDE | Tue | 4 | new | Design the validation you run before a joined number reaches Finance, and say what you do when it fails at the end of reporting day. |
| 9 | b | One correct option | 2 | Hard | [S] | BA, DS, FDE | Tue | 4 | new | INNER against LEFT join: what does each drop or keep? |
| 10 | c | One correct option | 2 | Hard | [D] | BA, FDE | Tue | 4 | new | Design the validation you run before a joined number reaches Finance, and say what you do when it fails at the end of reporting day. |
| 11 | b, d | More than one correct | 2 | Hard | [D] | BA, DS, FDE | Tue | 4 | new | Design the validation you run before a joined number reaches Finance, and say what you do when it fails at the end of reporting day. |
| 12 | a | Scenario set | 3 | Hard | [S] | BA, DS | Wed | 4 | new | RANK, DENSE_RANK and ROW_NUMBER on a tie. |
| 13 | d | Scenario set | 3 | Hard | [D] | BA, DS | Wed | 4 | new | The business says 'ties rank the same'; which function, and how many rows might the top-N report ship? |
| 14 | b | One correct option | 3 | Medium | [S] | BA, DS | Wed | 2.5 | bank 27 | Top-3 per group: GROUP BY or a window, and why? |
| 15 | c | One correct option | 3 | Hard | [F] | BA, DS | Wed | 4 | new | How would you find customers whose spend fell two months in a row? |
| 16 | a | One correct option | 3 | Hard | [D] | BA, FDE | Wed | 4 | new | How do you present one number so it is not misread? |
| 17 | 346 | Scenario set | 4 | Medium | [F] | BA, DS | Thu | 2.5 | new | merge against join: what is the same and what differs? |
| 18 | d | Scenario set | 4 | Medium | [F] | BA, DS, FDE | Thu | 2.5 | new | A pivot's total disagrees with the warehouse; where do you look first? |
| 19 | a, e | Scenario set | 4 | Medium | [F] | BA, DS, FDE | Thu | 2.5 | new | Which merge argument raises on duplicate keys, and which error? |
| 20 | c | Scenario set | 4 | Hard | [D] | BA, DS, FDE | Thu | 4 | new | A pivot's total disagrees with the warehouse; where do you look first? |
| 21 | b | One correct option | 4 | Hard | [S] | BA, DS | Thu | 4 | new | pivot against melt: which widens and which lengthens? |
| 22 | a | One correct option | 4 | Hard | [D] | BA, DS | Thu | 4 | new | SQL, pandas or Excel: how do you choose? |
| 23 | d (XLOOKUP with a message for a missing id) | Match the following | 5 | Medium | [F] | BA | Fri | 2.5 | new | A stakeholder wants to poke the numbers themselves; what do you give them and what do you never give them? |
| 24 | a (SUBTOTAL(109, ...) at the foot of the list) | Match the following | 5 | Medium | [F] | BA | Fri | 2.5 | new | Your pivot shows a different total from the warehouse; where do you look first? |
| 25 | f (a first-row flag per order, summed with SUMIFS) | Match the following | 5 | Medium | [F] | BA, DS | Fri | 2.5 | new | A pivot's total disagrees with the warehouse; where do you look first? |
| 26 | c (a labelled input cell beside the actual figure) | Match the following | 5 | Medium | [D] | BA, FDE | Fri | 2.5 | new | Two directors change assumptions in the room and the sheet recalculates differently for each; what did you get right and what do you fix? |
| 27 | d | One correct option | 5 | Hard | [F] | BA, DS, FDE | Fri | 4 | new | Your pivot shows a different total from the warehouse; where do you look first? |
| 28 | a | One correct option | 5 | Hard | [D] | BA, DS, FDE | Fri | 4 | new | Same question, three tools: how do you choose, and defend one choice? |
| 29 | 0.60 dollars a trip | Applied maths | 5 | Medium | [F] | BA, FDE | Fri | 2.5 | new | How do you present one number so it is not misread? |
| 30 | c | One correct option | 6 | Hard | [F] | DS | Thu | 4 | new | Your LEFT join grew the row count and revenue doubled; name the cause and the check. |
| 31 | d | One correct option | 6 | Hard | [S] | DS | Wed | 4 | new | RANK, DENSE_RANK and ROW_NUMBER on a tie. |
| 32 | b | One correct option | 6 | Hard | [S] | DS | Mon | 4 | new | WHERE against HAVING, one sentence each. |
| 33 | c | One correct option | 6 | Hard | [F] | DS, FDE | Tue | 4 | new | How do you find orders with no payment? |
| 34 | a | One correct option | 6 | Medium | [F] | DS | Wed | 2.5 | new | RANK, DENSE_RANK and ROW_NUMBER on a tie. |
| 35 | d | One correct option | 6 | Medium | [F] | BA, DS | Mon | 2.5 | new | How do you present one number so it is not misread? |

## Why each answer holds

### Q1, key c

**Why it holds.** count(*) and count(DISTINCT customer_id) are both integers, so Postgres divides integers and drops the fraction: 215 / 91 returns 2 and 140 / 76 returns 1. The true figures are 2.36 and 1.84, a fall of 22 percent, and casting one side, count(*)::numeric, prints them. The check is to multiply back: 1 times 76 members is 76, against 140 orders. Run on PostgreSQL 16.13 on the week's warehouse on 30 September 2026.

- (a) The decimals appear only when one side is numeric, as in count(*)::numeric; two integer counts divide as integers. This is the number the query should print, and does not.
- (b) Postgres truncates integer division; it does not round, and 140 / 76 rounded would be 2, which the printed 1 contradicts.
- (d) Reads the printed 2 and 1 as the business fact, which is Monday's round 2 trap: Retail-Plus "halved" and the budget went to Retail-Core, where multiplying back (1 times 76 is 76, against 140 orders) shows the query is wrong.

**In the interview.** Orders per member is a ratio of two counts, and Postgres divides two integers as integers, so I cast one side to numeric and multiply back by the denominator before the number leaves.

### Q2, key c, b, e, f, a, d

**Why it holds.** The logical order is FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY: rows are read, filtered, grouped, and the groups filtered, before anything is selected or sorted. The common wrong answer is the order the clauses are typed, a, c, b, e, f, d, which puts SELECT first; the database cannot pick columns from rows it has not yet read, filtered and grouped. The same order explains why a SELECT alias works in ORDER BY and fails in WHERE, and why SELECT can name only grouped columns and aggregates.

**In the interview.** FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY, and most of the errors a query can raise follow from it.

### Q3, key d (guarantee)

**Why it holds.** A table has no stored order, so without ORDER BY the database returns whichever rows its plan reaches first, and two runs can differ: Monday's sample of five delivered app orders summed to Rs 3,900 and, after a reload that rewrote two rows with their own values, to Rs 4,590. "sort" is the near miss, and it fails because a plan that reads an index does return sorted rows on some runs; what the database withholds is the promise.

**In the interview.** LIMIT without ORDER BY returns some rows, never defined ones, so I order on a unique key before I limit.

### Q4, key b (CTE)

**Why it holds.** WITH names a common table expression, a step the rest of the query reads like a table. A subquery is the near miss: it is inline and unnamed. A view is named too, but it is stored with CREATE VIEW, never introduced by WITH.

**In the interview.** A CTE names each step of the logic, so an auditor reads the query top to bottom, one decision per block.

### Q5, key a

**Why it holds.** Excel's job is the last mile: presenting a number and letting people explore it. A number that becomes a what-if for the room, with nothing filed from it, has become that job. Every other option is a reason to keep the number in the warehouse, where it reruns unchanged on the source and every step can be audited. Friday's operating rule says the same, and gives the one direction a number travels: the warehouse computes it, pandas carries the analyst's iteration, and Excel presents it to the room, never the other way.

- (b) A workbook fed by an export is staler than the warehouse, never fresher; a number needed early on Monday is a scheduling question for the warehouse query.
- (c) Line-by-line audit is the reason the number lives in the warehouse: a query can be read step by step, and a typed-over cell leaves no trail.
- (d) Convenience is no reason to move a number Finance reports; a pivot on an export is one more copy that can drift from the source.

**In the interview.** A number Finance audits lives in the warehouse because it reruns unchanged on the source and every step can be read; Excel is for presenting it and for what-ifs the room explores, never for computing the number of record.

### Q6, key d

**Why it holds.** The CASE has no ELSE, so it returns NULL for the two short views, and count skips NULLs: the reported figure divides all 30 seconds by 3 views, 10.0, where the average per view is 30 over 5, 6.0. Measured against the true figure, 10.0 overstates 6.0 by 4.0 over 6.0, about 67 percent. TechCrunch (22 September 2016), citing The Wall Street Journal, put Facebook's overstatement at 60 to 80 percent over two years and reported that billing was not affected; checked on 30 September 2026. Run on PostgreSQL 16.13 on 30 September 2026.

- (a) Divides the gap by the wrong base: 4.0 over the reported 10.0 is 40 percent, and an overstatement is measured against the true figure, 6.0.
- (b) Averages the three long views alone, (14 + 9 + 4) / 3 = 9.0; the metric's numerator was all the time watched, and the short views' 3 seconds stay in it.
- (c) count(CASE WHEN ... THEN 1 END) counts only the non-NULL results, and a CASE with no ELSE returns NULL for the views it does not match; Monday's round 3 trap in another form.

**In the interview.** An average is defined by its denominator; when a filter or a CASE quietly shrinks it, the average rises with no change in the data, so I print the numerator and the denominator beside the ratio.

### Q7, key b

**Why it holds.** A LEFT JOIN writes one row per matching payment row and keeps an order with none as one row of NULLs: 216 + 2 times 188 + 2 times 28 + 30 = 678 rows. count(DISTINCT o.order_id) counts the 462 orders, and count(p.payment_id) skips the 30 unpaid orders' NULLs, 678 minus 30 = 648, which is also what an INNER JOIN would return. The eight payments with no order never meet an order, so they are in none of the counts. Run on PostgreSQL 16.13 on the week's warehouse on 30 September 2026.

- (a) Reads the join as keeping one row per order, and payment rows as one per paid order (462 minus 30 = 432); a join repeats an order once per matching row, which is Tuesday's round 1 fan-out.
- (c) count(p.payment_id) skips NULLs, and only count(*) counts the 30 unpaid orders' rows; reading count(column) as count(*) is Monday's round 1 trap inside a join.
- (d) Counts the eight payments with no order as if they had joined; a LEFT JOIN from orders keeps only rows that start from an order, and only a FULL OUTER JOIN brings in the payments whose order is missing.

**In the interview.** INNER keeps only matched rows and LEFT keeps every order with NULLs where nothing matched; both repeat an order once per matching payment row, so I size the join, rows out against orders in, before any rupee is summed.

### Q8, key c, e, a, d, b

**Why it holds.** The repeats go first, because a sum taken before them keeps the Rs 20,750 the gateway posted twice; the payments go to one row per order before the join, because a join onto payment rows repeats every instalment order; the LEFT JOIN keeps all 462 orders; the checks come before anything is sent, and on Kalpa's Q2 book they read 462 rows out and a gap of Rs 17,54,930, the booked value of the 30 unpaid orders exactly. On the same book, HAVING count(*) > 1 by order lists 216 orders, of which 188 are two instalments; grouping by order and instalment leaves the 28 repeats. The common wrong order sums first (e before c), which keeps the repeats in collected, or sends before checking. Run on PostgreSQL 16.13 on the week's warehouse on 30 September 2026.

**In the interview.** De-duplicate at the grain that defines a repeat, aggregate to the join's grain, join, prove the row count and the gap, then send.

### Q9, key b

**Why it holds.** O-1's two instalments both fall inside the quarter, so the join gives O-1 two rows and sum(o.amount) counts its Rs 1,200 twice. O-2's only payment is dated 1 October, so its joined row fails the WHERE. O-3 has no payment, so its paid_date is NULL, BETWEEN on a NULL is unknown, and WHERE drops that row too. Two rows remain, booked Rs 2,400, against three orders worth Rs 2,500: the report lost two orders and doubled the one it kept. Run on PostgreSQL 16.13 on 30 September 2026.

- (a) Assumes one row per order, which holds only once payments are brought to one row per order; O-1 has two payment rows inside the quarter, so the join repeats it.
- (c) Keeps O-3 as if its NULL date passed the filter; a comparison with NULL is unknown, and WHERE keeps only rows where it is true, which is how the date filter in Tuesday's round 3 emptied the unpaid list.
- (d) Reads the WHERE as if it sat in the ON clause, where it would keep every order with NULL payments on O-2 and O-3; in WHERE it runs after the join and turns the LEFT JOIN into an INNER one, which is Tuesday's round 3 trap.

**In the interview.** A filter on the right-hand table of a LEFT JOIN belongs in ON, because WHERE runs after the join, drops the NULL rows and turns the LEFT JOIN back into an INNER one; and the payments go to one row per order before the join.

### Q10, key c

**Why it holds.** Booked passed both of its checks, so it can leave. Collected rests on the check that failed, so it waits, and naming the Rs 21,750 as an open line with an owner and a time is what Anand can act on. The Tuesday pack gives this answer to its question on the end of reporting day: ship booked with the open line named, and hold collected.

- (a) Forcing the bridge to close hides the one fact the check found; the reconciliation would then explain a sum that no order carries.
- (b) Sends the one figure the failed check leaves unproven, and a footnote does not travel with a number once it is quoted.
- (d) Holds back a figure that passed its checks; Anand loses the booked number over a doubt that concerns collected alone.

**In the interview.** Before a joined number reaches Finance I check rows in against rows out, the total against its source and the gap against a named list; when one fails at the end of reporting day, the figures that passed go out, the one that failed waits, and the open line is named with an owner and a time.

### Q11, key b, d

**Why it holds.** Both correct checks compare what arrived with what was loaded, so a truncation shows the day it happens: a per-file count of records against rows loaded, and a control total from the source against the loaded total. That is Tuesday's habit, rows in against rows out, and Week 1's revenue bridge, input equals clean plus rejected. The facts are from the GOV.UK statement of 4 October 2020 (15,841 cases between 25 September and 2 October; files that exceeded the maximum size) and The Register of 5 October 2020 (lab files in CSV converted to the .xls format, 65,536 rows a sheet, records past the cut-off left off), both checked on 30 September 2026.

- (a) Raises the ceiling from 65,536 rows to about a million and checks nothing: a file past the new limit would be cut just as quietly. It removes this cause, and leaves the kind of failure.
- (c) De-duplication removes rows; it cannot find rows that were never loaded.
- (e) A pivot sums what was loaded, so it cannot see what never arrived: the missing cases are missing from the pivot too.

**In the interview.** Any step that can drop rows without a warning needs a count on both sides of it, and the load stops when they differ; raising a limit only moves the cliff.

### Q12, key a

**Why it holds.** RANK gives C-0185 and C-0242 the shared rank 50 and C-0259 rank 52, so 51 members hold a rank of 50 or better. DENSE_RANK leaves no gaps, so the tie at 48 (C-0189 and C-0206) makes C-0185 and C-0242 dense rank 49 and C-0259 dense rank 50: 52 members. ROW_NUMBER numbers every row once: 50. Run on PostgreSQL 16.13 on the week's warehouse on 30 September 2026.

- (b) Sees one tie at the line and reads DENSE_RANK as RANK without the gap; the second tie, at 48, compresses the dense numbers so that C-0259 reaches 50. That is Wednesday's trap, where "ties rank the same" quietly shipped 52.
- (c) Reads RANK as capping the list at fifty; RANK gives both tied members 50 and keeps both.
- (d) Swaps the two functions: RANK leaves a gap after each tie, and DENSE_RANK does not.

**In the interview.** ROW_NUMBER gives every row its own number and breaks ties arbitrarily, RANK shares a rank and skips the next, and DENSE_RANK shares without a gap; on a top-N list, RANK can ship more than N and DENSE_RANK more still, so I count what each rule ships before choosing.

### Q13, key d

**Why it holds.** He asked for tied members to share a rank and for the count to include a tie at the line. RANK does both: 51 members, and the note says why the list is one over fifty. DENSE_RANK also ranks ties the same but ships 52, because an earlier tie compressed its numbers, so the list gains C-0259 on Rs 3,200, a member below both tied members.

- (a) Meets the first half of the ask and breaks the second: its 52 includes C-0259, who spent less than both members tied at the line, so the length no longer means the top fifty with ties.
- (b) Exactly fifty and the same every Monday, at the cost of dropping a member who spent exactly what the fiftieth did, by an id nobody chose on purpose; if the budget demands exactly fifty, the tiebreaker becomes a decision the head of Retail-Plus owns.
- (c) The "forty-nine because of a tie" he ruled out, in his own words.

**In the interview.** When the business says ties rank the same, I use RANK and state the count and its reason in the same line, because the list can ship more than N; if the budget demands exactly N, the tiebreaker becomes a decision someone owns.

### Q14, key b

**Why it holds.** A rank computed within PARTITION BY segment keeps every member and restarts for each segment; the outer query keeps the rows ranked three or better. The window has to be filtered outside, because WHERE runs before any window is computed. The whole-table list in the stem is Wednesday's round 1 trap: 35 Business members, 11 Retail-Plus, 4 Retail-Core and no Student.

- (a) GROUP BY collapses each segment to one row, so the members are gone before LIMIT runs, and LIMIT applies once to the whole result, never per group.
- (c) One ORDER BY with LIMIT 3 is the whole-table list at a smaller size: the top three overall, all Business, which is the first draft's mistake again.
- (d) HAVING keeps or drops whole groups by an aggregate; it cannot choose rows inside a group.

**In the interview.** Top N per group is a window: rank inside PARTITION BY the group in a CTE, keep rank N or better outside it, and name the tie rule.

### Q15, key c

**Why it holds.** LAG reads the previous row in the partition, never the previous calendar month. C-0185's September is compared with July (1,450 below 1,900) and July with June (1,900 below 2,690), and C-0216's September with July and July with May (2,540 below 4,300, below 6,440), so both are flagged although neither ordered in August: a gap has been read as a fall. A calendar check, that the two rows LAG reads are August and July, keeps C-0161 and C-0171, the two genuine falls. C-0185 is one of the pair tied at fiftieth in Set 5. Run on PostgreSQL 16.13 on the week's warehouse on 30 September 2026.

- (a) LAG knows nothing of the calendar; it returns whatever row came before in the window's order, which is why the two members with a missing August pass.
- (b) Reads the query's output as the business answer; a member with no August order has no August reading, and this is the member who says he was on holiday.
- (d) C-0216 has three rows (May, July, September), so LAG(spend, 2) on its September row returns May's 6,440. LAG returns NULL only when the partition has no row that far back, as on a member's first two rows, and a comparison with that NULL flags nobody.

**In the interview.** One row per customer per month, LAG 1 and LAG 2 partitioned by customer and ordered by month, a check that the lagged rows really are the previous two calendar months, and a flag where each month is below the one before; a month with no order is no reading.

### Q16, key a

**Why it holds.** Both readings are true and the line needs both: the total closed on plan, Rs 10 ahead, and six of the seven full weeks from 10 August sit below the weekly Rs 75.69 lakh (only the week of 14 September, Rs 93.0 lakh, cleared it). A front-page line carries its period and its comparison, so a director does not read one July week as the trend. The weekly figures are the week's own running total against plan_line, recomputed on PostgreSQL 16.13 on 30 September 2026.

- (b) A total that lands on plan says nothing about the weekly rate; the chart shows the rate below plan in six weeks of seven.
- (c) Reads the weekly shortfall as the quarter's result; the quarter closed Rs 10 above plan because of the week in July.
- (d) Quotes a mid-quarter running figure as the close; the lead had shrunk to Rs 10 by the end of the quarter.

**In the interview.** One number goes out with its period, its base and its comparison, here the quarter against plan and the weekly rate against the weekly plan, so it is read the way it was meant.

### Q17, key 346

**Why it holds.** A left merge keeps every customer and writes one row per matching feed row: 334 customers match once or not at all, and the 6 sent twice match two rows each, so 334 + 12 = 346. Run on pandas 3.0.5 on the week's files on 30 September 2026.

**In the interview.** A merge grows the left table only when a key repeats on the right, and each repeat adds a row.

### Q18, key d

**Why it holds.** Each of the six repeated customers sits on two rows carrying the same spend, so the pivot adds their spend twice: Rs 19,84,45,800, Rs 45,800 above the book. Run on pandas 3.0.5 on 30 September 2026.

- (a) A left merge keeps each left row once only when the right key is unique; the six repeated keys add six rows, each carrying spend.
- (b) A pivot sums rows, and grouping by customer_id adds the repeated rows into one larger cell; it does not de-duplicate them.
- (c) A left merge keeps the customers the sale never reached, with NaN in the feed's columns; they stay, with their spend.

**In the interview.** A pivot is only as honest as the table under it: a merge that repeated rows makes a larger total out of rows that each look right.

### Q19, key a, e

**Why it holds.** validate='one_to_one' checks that the key is unique on both sides and raises pandas' MergeError ("Merge keys are not unique in right dataset; not a one-to-one merge") before a merged table exists; the row-count assert stops the run because 346 is not 340. Checked on pandas 3.0.5 on 30 September 2026.

- (b) The six repeated rows differ in exposed_date (3 and 11 August), so no row is an exact duplicate and all 346 stay; this is Friday's Remove Duplicates trap in pandas.
- (c) indicator labels each row both, left_only or right_only; the repeated customers are labelled both, twice, and nothing stops.
- (d) An inner merge keeps 136 rows, still with the six customers twice, and drops the 210 the sale never reached.

**In the interview.** validate= states the relationship a merge must have and raises MergeError the moment the keys break it, and a row-count check says the same thing in numbers; both belong in the refresh.

### Q20, key c

**Why it holds.** A customer the sale reached twice was still reached once, so the business rule is one exposure per customer, the first by date. Applied to the feed, it leaves 340 rows, spend on the book and 130 reached customers, and validate stays on so that a new kind of repeat stops the refresh instead of changing the number. Run on pandas 3.0.5 on 30 September 2026.

- (a) Typing over the total hides the error, leaves every per-customer figure wrong, and the next refresh brings it back.
- (b) The repeated rows differ in exposed_date, so drop_duplicates() on every column removes nothing.
- (d) Spend per reached customer is a doubled numerator over a count of rows or of customers; either way the repeated rows move it.

**In the interview.** Fix the error where it was made, at the feed, with a rule the business agrees, and keep the guard on so next week's feed fails loudly instead of quietly.

### Q21, key b

**Why it holds.** pivot_table splits the orders by member and month, applies its default aggfunc, which is the mean, and combines one cell per group, so M1's two June orders print as their average, 2000.0, where M1 spent 4,000. melt turns the 2 by 2 view back into 4 rows, one per member and month, including M2's empty July, and sum skips that NaN: 2,000 + 2,400 + 1,800 = 6200.0 against 8,200 of orders. The check is the grand total against the orders, and the fix is aggfunc='sum' with fill_value=0; on Kalpa's Retail-Plus months the default read a fall of 18 percent where the orders fell 29. Run on pandas 3.0.5 on 30 September 2026.

- (a) Assumes the pivot adds; it averages unless aggfunc says otherwise, which is Thursday's round 3 trap.
- (c) Drops the empty cell in melt; melt keeps every member and month, NaN included, which is why the long table has 4 rows.
- (d) Both misreadings at once.

**In the interview.** pivot_table widens a column's values into columns and averages unless told to sum; melt lengthens it back into rows; I write aggfunc= every time and tie the grand total to the source.

### Q22, key a

**Why it holds.** A left merge keeps all 4 of the lab's rows; '2-Sep' and '1-Mar' match no symbol, so indicator marks them left_only and only 2 rows are both. Nothing raises: two genes lose their annotation without a word. The fix belongs at the source, a list kept as text, and the naming body has since moved the other way too: in 2020 the HGNC renamed every symbol Excel turned into a date, so SEPT1 is now SEPTIN1 and MARCH1 is now MARCHF1 (Bruford and colleagues, Nature Genetics, 2020). Both papers checked on 30 September 2026; the code run on pandas 3.0.5 the same day.

- (b) pandas reads the text it is given; '2-Sep' stays the string '2-Sep', and no parser turns it back into a gene symbol.
- (c) A left merge never adds reference rows that nothing matched; how='right' or how='outer' would.
- (d) A left merge keeps every left row, matched or not; how='inner' would keep 2.

**In the interview.** A key that changed on its way in never matches and never raises, so after every merge I count the matches with indicator=True, and I fix the key at its source rather than in the analysis.

### Q23, key d (XLOOKUP with a message for a missing id)

**Why it holds.** XLOOKUP matches exactly by default, and its fourth argument, if_not_found, is what it shows for a missing id (Microsoft Support, XLOOKUP function, verified 29 September 2026). The spare beside it, VLOOKUP with its fourth argument left out, looks for an approximate match: on Friday it returned C-0194's Rs 16,740 for C-0195, a member with no orders.

**In the interview.** A lookup has two exits, the row or a visible "not in the table", and I test it with an id I know is missing.

### Q24, key a (SUBTOTAL(109, ...) at the foot of the list)

**Why it holds.** SUBTOTAL(109, ...) adds only the rows on screen, while SUM adds the rows a filter hides: on Friday, filtered to Mumbai's 11 members, SUBTOTAL read Rs 1,56,790 and SUM still read the whole list's Rs 7,14,890, a budget 4.6 times too big.

**In the interview.** A total under a filtered list is SUBTOTAL(109), and I say in the cell's label what it adds.

### Q25, key f (a first-row flag per order, summed with SUMIFS)

**Why it holds.** Flagging the first row of each order, with =IF(COUNTIF($A$2:A2,A2)=1,1,0) filled down, and summing only the flagged rows with SUMIFS counts each order once: on Friday that took the raw export's Rs 39.41 crore back to the warehouse's Rs 19.84 crore. The spare beside it, Remove Duplicates, removes only identical rows, and an instalment order's two rows differ in the amount paid, so 1,400 rows stayed and the total still doubled.

**In the interview.** The fix names the grain: one row per order, counted once, before any total is taken.

### Q26, key c (a labelled input cell beside the actual figure)

**Why it holds.** An assumption is an input: a labelled cell beside the actual, feeding a scenario line, so the sheet recalculates in the room and the source stays tied to the warehouse. On Friday, the same Rs 5,00,000 typed over the Q2 cell read "down 14.6 percent" against Finance's 29.4, until Monday's refresh wiped it without a trace.

**In the interview.** Yes to the question, as a labelled scenario beside the actual; no to the edit, and a drift check ties the sheet to the warehouse on every refresh.

### Q27, key d

**Why it holds.** Both failures are ranges that stop before the data does, so a control total from the source, here the warehouse's Rs 19,84,00,000, and a count of the rows each range covers against the rows in the table fail the day it happens: 311 customers, 300 covered. That is the drift check in Friday's operating rule. The case is from Herndon, Ash and Pollin, PERI working paper 322 (April 2013), and Retraction Watch (18 April 2013); the replicators' corrected average for the group, 2.2 percent against the published -0.1, also corrects two other choices, so the range alone is not the whole gap. Checked on 30 September 2026.

- (a) Protection stops edits, and the formula that ends at row 301 was never edited, which is the problem.
- (b) Recalculating a formula whose range stops short recalculates the same wrong total; a refresh reaches pivots, and a typed range is no pivot.
- (c) A second calculation on the first rows agrees with the formula wherever both cover the same rows; the rows left out sit at the end.

**In the interview.** Every total in a workbook ties to a control total from the source on each refresh, and every range is checked against the rows it should cover, because a range that stops short fails without a sound.

### Q28, key a

**Why it holds.** (2.60 - 2.00) / (2.00 + 2.60) = 0.60 / 4.60 = 0.130; divided by the average, 2.30, the change is 0.261, so the sheet halves every change, which the report describes as "muting volatility by a factor of two". A second way to the same number, by hand on one row or in a second tool, catches it: Kavya's review and Thursday's three-tool check. Quoted from the Report of JPMorgan Chase and Co. Management Task Force Regarding 2012 CIO Losses, 16 January 2013, pages 123 and 128, checked on 30 September 2026.

- (b) The formula divides by B2 + C2, the sum, which is twice the average; the copying is a further risk the report names, and a check on copying alone misses this.
- (c) Dividing by the sum is not the relative change the modeller meant, and only a second calculation shows the gap.
- (d) Divides by the old rate, a third convention; and a pivot of the sheet's outputs repeats the formula's error in every row.

**In the interview.** A number that decides risk gets a second, independent calculation before it is trusted, because a formula can be wrong in every row at once.

### Q29, key 0.60 dollars a trip

**Why it holds.** 25 percent of the gross 30.00 is 7.50; 25 percent of the net 27.60 is 6.90; the difference is 0.60 dollars, which is 25 percent of the 2.40 of tax and fees. Small on one trip, it adds up across tens of thousands of drivers, which is why a percentage's base is part of its definition. CBS News, 24 May 2017, checked on 30 September 2026; the fare and the rate here are illustrative.

**In the interview.** A percentage is defined only with its base, so before any rate is applied I write down what it is a percentage of.

### Q30, key c

**Why it holds.** A merge writes one row per matching label, so T3 and T5 appear twice: 7 rows. Both are tickets the model got wrong, so the mean counts 3 correct rows of 7, 0.43, against 3 correct tickets of 5, 0.6. It is the fan-out of Tuesday's payments and Thursday's exposure feed, and the checks are the same: rows before and after, or validate='one_to_one'. Run on pandas 3.0.5 on 30 September 2026.

- (a) A merge repeats a left row once per matching right row; it keeps one row per ticket only when the labels are unique.
- (b) The repeated labels match their tickets, but the rows they repeat are misses, so the extra rows move the mean.
- (d) A repeat inflates a score only when it repeats correct rows; here it repeats the two misses.

**In the interview.** An evaluation metric is a mean over one row per test case, so I size the join before scoring and validate that the labels are unique per case.

### Q31, key d

**Why it holds.** ROW_NUMBER partitioned by model and ordered by finished_on DESC, run_id DESC, filtered to row 1 outside the window, returns bot-a's r2 (0.78) and bot-b's r5 (0.79) every time. With the date alone, bot-b's two runs of 9 September tie and the database picks one, so the leaderboard can show 0.86 one morning and 0.79 the next. Run on PostgreSQL 16.13 on 30 September 2026.

- (a) Each max() is taken on its own, so bot-a shows 8 September beside 0.81, a pairing no run produced: its latest date with its best score.
- (b) The right shape, but the tie on 9 September leaves the pick to the database; Wednesday's lesson on ties in a window's order.
- (c) RANK gives r4 and r5 the same rank 1, so bot-b appears twice on the leaderboard.

**In the interview.** The latest row per key is ROW_NUMBER partitioned by the key, ordered newest first with a tiebreaker that makes the order unique, kept at 1 in an outer query.

### Q32, key b

**Why it holds.** WHERE runs first and keeps the three low ratings, two for bot-a and one for bot-b. GROUP BY forms groups only from those rows, so bot-c forms no group at all, and HAVING then keeps the groups with two or more: bot-a, 2. The query never prints a zero row. Run on PostgreSQL 16.13 on 30 September 2026.

- (a) Applies HAVING before WHERE: judged on all seven ratings every model has two or more, and then the rows are filtered. The logical order is WHERE, GROUP BY, HAVING.
- (c) A group exists only for values that survive WHERE; bot-c had no low rating, so it has no row, and bot-b's 1 fails HAVING.
- (d) Counts every rating, as if WHERE were ignored; these are the group sizes before any filter.

**In the interview.** WHERE keeps or drops single rows before any group exists; HAVING keeps or drops whole groups after the aggregate is computed, which is why an aggregate can sit in HAVING and never in WHERE.

### Q33, key c

**Why it holds.** For c1, NOT IN asks c1 <> 'c2' AND c1 <> 'c4' AND c1 <> NULL; the last comparison is unknown, so the whole condition is unknown and WHERE drops the row. Every conversation fails the same way, so the count is 0 and the review reads a working assistant as useless. NOT EXISTS, or a LEFT JOIN kept where the handoff key IS NULL, returns 2. Run on PostgreSQL 16.13 on 30 September 2026.

- (a) The answer NOT EXISTS gives; NOT IN against a list that holds a NULL can never be true.
- (b) The NULL sits in the subquery's list, never in the outer table, so it cannot add a conversation.
- (d) Postgres raises nothing; the comparison with NULL is unknown and the rows are dropped without a word.

**In the interview.** Rows with no match are an anti-join, which I write as NOT EXISTS or as a LEFT JOIN kept where the right key IS NULL, never as NOT IN against a column that can hold a NULL.

### Q34, key a

**Why it holds.** With an ORDER BY and no frame, the window runs from the first row to the current row and its peers, the rows that tie on the ORDER BY. Calls 2 and 3 share 22 September, so both read the day's closing figure, 1200, and neither shows its own step. Adding call_id to the window's ORDER BY gives each call its own step. Run on PostgreSQL 16.13 on 30 September 2026.

- (b) The one-step-per-row reading, which needs a unique ORDER BY such as day then call_id; with the date alone the two calls are peers.
- (c) The whole-table total on every row, which is what sum(tokens) OVER () gives with no ORDER BY; with an ORDER BY, the frame stops at the current row and its peers.
- (d) Assumes the database breaks the tie with call 3 first; peers are never split, they share one figure.

**In the interview.** A running total is deterministic only when its ORDER BY is unique; rows that tie are peers and share one cumulative figure, so I add a tiebreaker such as the id.

### Q35, key d

**Why it holds.** A distinct count does not add across days: a person who used the assistant on five days is in five daily counts and once in the week's. The week's figure is its own COUNT(DISTINCT user_id) over the week's rows, 2,100, never the sum of the days. On Kalpa's book, 244 Q1 buyers and 227 Q2 buyers are 301 customers across both quarters, not 471.

- (a) Each day is distinct within the day; across days the same people repeat, so the sum counts them again.
- (b) An average of daily counts answers how many on a typical day, a different question from the week's reach.
- (c) The peak answers capacity planning; the ask was the week's active users.

**In the interview.** COUNT(DISTINCT ...) does not add across groups; a period's total needs its own distinct count over the whole period.


## Items by tag, level, day and part, for the tally

- [S] (8): Q2, Q4, Q9, Q12, Q14, Q21, Q31, Q32
- [F] (16): Q1, Q3, Q7, Q15, Q17, Q18, Q19, Q23, Q24, Q25, Q27, Q29, Q30, Q33, Q34, Q35
- [SV] (0): none
- [D] (11): Q5, Q6, Q8, Q10, Q11, Q13, Q16, Q20, Q22, Q26, Q28
- Easy (2): Q3, Q4
- Medium (12): Q2, Q14, Q17, Q18, Q19, Q23, Q24, Q25, Q26, Q29, Q34, Q35
- Hard (21): Q1, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q15, Q16, Q20, Q21, Q22, Q27, Q28, Q30, Q31, Q32, Q33
- Mon (8): Q1, Q2, Q3, Q4, Q5, Q6, Q32, Q35
- Tue (6): Q7, Q8, Q9, Q10, Q11, Q33
- Wed (7): Q12, Q13, Q14, Q15, Q16, Q31, Q34
- Thu (7): Q17, Q18, Q19, Q20, Q21, Q22, Q30
- Fri (7): Q23, Q24, Q25, Q26, Q27, Q28, Q29
- Part 1, Anand's Monday numbers (6): Q1, Q2, Q3, Q4, Q5, Q6
- Part 2, Booked against collected (5): Q7, Q8, Q9, Q10, Q11
- Part 3, The protect list and the plan line (5): Q12, Q13, Q14, Q15, Q16
- Part 4, One row per customer (6): Q17, Q18, Q19, Q20, Q21, Q22
- Part 5, The last mile, and spreadsheets in public (7): Q23, Q24, Q25, Q26, Q27, Q28, Q29
- Part 6, Read the code, read the data: an AI team's tables (6): Q30, Q31, Q32, Q33, Q34, Q35

## New items waiting for the tracker

These items come from the week's source file, not the tracker. Accept one by adding it to the tracker's Saturday papers tab and deleting it from the source file.

- Q1 (One correct option, Hard, [F]): Anand's analyst fills the missing leaf with SELECT quarter, count(*) / count(DISTINCT customer_id) FROM rp_orders GROUP BY quarter, where rp_orders holds the Retail-Plus orders above. What does the query return, and what should the note to the head of Retail-Plus say?
- Q5 (One correct option, Hard, [D]): The Monday suite runs as saved queries in the warehouse, so each Monday it reruns unchanged on the source, and Anand's analyst can read every step. Which fact, if it became true of one of its numbers, would make an Excel workbook the better home for that number?
- Q6 (One correct option, Hard, [D]): In 2016 Facebook told advertisers that its average duration of video viewed had divided the total time watched by the number of views lasting 3 seconds or more, where it should have divided by every view (TechCrunch, 2016). The query above rebuilds both versions of the metric. What does it return, and by how much does the reported figure overstate the average per view?
- Q7 (Scenario set, Hard, [F]): Before the report goes to Anand, the analyst sizes the join by hand. What will the query above return?
- Q8 (Order the steps, Hard, [D]): Put the steps of Anand's collected-revenue report in the order they must run.
- Q9 (One correct option, Hard, [S]): Anand wants every Q2 order beside what was collected on it within the quarter, so the analyst adds a date filter on the payments. Before the report goes to him, the analyst runs the query above to count its rows and their booked value. What does it return?
- Q10 (One correct option, Hard, [D]): It is the end of reporting day, and Anand expects the report tonight. Two checks pass, and the third fails by Rs 21,750 that nobody has explained yet. What do you send?
- Q11 (More than one correct, Hard, [D]): In October 2020 Public Health England found that 15,841 positive COVID-19 cases from 25 September to 2 October had been left out of the daily figures, because some files were larger than the load could take (GOV.UK, 2020); rows past the old format's limit were dropped without a warning (The Register, 2020). Which of these, run on every file, would have told the team that cases were missing on the day they went missing? Mark every correct option.
- Q12 (Scenario set, Hard, [S]): The analyst computes RANK(), DENSE_RANK() and ROW_NUMBER() over Q2 revenue, highest first, and keeps the members numbered 50 or better under each. How many members does each keep?
- Q13 (Scenario set, Hard, [D]): Which list meets the head of Retail-Plus's ask, and what does the note to Marketing say?
- Q15 (One correct option, Hard, [F]): The falling flag reads member_month, one row per member per month with an order. It takes prev1 = LAG(spend, 1) and prev2 = LAG(spend, 2), each partitioned by member and ordered by month, and flags a member whose September spend is below prev1 while prev1 is below prev2. Which members does it flag, and which of them should Marketing call falling two months running?
- Q16 (One correct option, Hard, [D]): Q2 closed at Rs 9,84,00,000 against a plan of Rs 9,83,99,990 for the quarter. At mid-quarter the running total had been Rs 1.58 crore ahead of plan, almost all of it from one week in July. Meera's chief of staff wants one line about the plan for Monday's front page. Which do you send?
- Q17 (Scenario set, Medium, [F]): How many rows does the merged table hold?
- Q18 (Scenario set, Medium, [F]): The analyst tells Marketing: "The pivot's grand total will equal the book's Rs 19,84,00,000." True or false, and why?
- Q19 (Scenario set, Medium, [F]): Which of these, added to Monday's refresh, would have stopped the run before the pivot was built? Mark every correct option.
- Q20 (Scenario set, Hard, [D]): Next Monday's feed may repeat customers again. Where does the fix belong, so the refresh runs clean without anyone editing its output?
- Q21 (One correct option, Hard, [S]): The head of Retail-Plus wants one row per member and one column per month, to read who is drifting, and a long copy of the same view for a trend chart. What does the code above print?
- Q22 (One correct option, Hard, [D]): A gene symbol is the short name a gene is known by, such as SEPT2 or MARCH1. Ziemann and colleagues found that Excel's default settings turn such symbols into dates, SEPT2 into 2-Sep and MARCH1 into 1-Mar, and that about a fifth of genomics papers with Excel gene lists carried such errors (Genome Biology, 2016). An analyst merges a lab's list onto a reference table. What does the code above print, and what should the analyst do?
- Q23 (Match the following, Medium, [F]): Find any member by id, and say so plainly when the id is not in the list
- Q24 (Match the following, Medium, [F]): A total at the foot of the protect list that follows the filter to one city
- Q25 (Match the following, Medium, [F]): Revenue by segment from an export with one row per payment, so an order paid in two instalments appears twice
- Q26 (Match the following, Medium, [D]): Let a director try Rs 5,00,000 for Retail-Plus in Q2 without touching the source figures
- Q27 (One correct option, Hard, [F]): In 2013 Herndon, Ash and Pollin tried to reproduce an influential 2010 paper by Reinhart and Rogoff from its own spreadsheet, and found an average whose range stopped short of the data, leaving Australia, Austria, Belgium, Canada and Denmark out of one group (PERI working paper 322, 2013). The chief of staff's workbook carries the same risk: next Monday's export holds 311 customers where Friday's held 300, and the Protect tab's formulas end at row 301. Which check, run on every refresh, catches both?
- Q28 (One correct option, Hard, [D]): JPMorgan's task force on the 2012 losses in its Chief Investment Office reported that a value-at-risk model, an estimate of how much a trading book can lose on a bad day, ran through Excel spreadsheets filled by copying and pasting, and that one step divided a change in rates by the sum of the old and new rates where the modeller meant their average (JPMorgan Chase, 2013). What does the sheet return for the row above, and which check catches the error?
- Q29 (Applied maths, Medium, [F]): In 2017 Uber said it had been taking its commission from New York City drivers on the gross fare, before sales tax and other fees were deducted, where it should have used the fare after them, and that it would repay affected drivers about 900 dollars each on average (CBS News, 2017). Suppose a trip's gross fare is 30.00 dollars, of which 2.40 dollars is tax and fees, and the commission is 25 percent. How much more commission did the gross-fare calculation take on this trip?
- Q30 (One correct option, Hard, [F]): The team scores a model that sorts support tickets into refund, late and other, against labels from an annotation vendor. The vendor re-sent a batch, so two tickets carry their label twice. What does the code above print, and what is the model's accuracy on the five tickets?
- Q31 (One correct option, Hard, [S]): The leaderboard must show each model's latest run and its accuracy, and show the same thing every morning. bot-b finished two runs on 9 September. Which approach does that?
- Q32 (One correct option, Hard, [S]): Customers rate each reply from 1 to 5. The team lead asks which models had at least two replies rated 2 or below this week. What does the query above return?
- Q33 (One correct option, Hard, [F]): The weekly review reads how many conversations the assistant resolved without a person. This week the handoff log gained a row whose conversation_id is NULL. What does the query above return, and what will the review conclude?
- Q34 (One correct option, Medium, [F]): The model's bill is charged per token, so the finance partner wants tokens used so far, call by call, to watch the bill build up. What does tokens_so_far read for calls 1 to 4?
- Q35 (One correct option, Medium, [F]): The seven daily counts in the chart above add up to 5,200. Counted once each, 2,100 different people used the assistant during the week. The product manager wants the week's active users for the deck. Which number do you give, and why?

## Bank items folded into deeper items

Each of these tracker items is not printed, because a deeper item on the paper tests the same concept. Accept a fold by recording it in the tracker; reject it by deleting it from `folded` in the week's source file.

- Bank 1 (Fill in the blank, Easy, Mon), folded into Q32: The item predicts a query's rows through WHERE, GROUP BY and HAVING in that order, so the clause that filters groups after they form is tested by use.
- Bank 4 (Fill in the blank, Easy, Tue), folded into Q7: Sizing the LEFT JOIN by hand requires knowing that every order stays, with NULLs where no payment matched.
- Bank 5 (Fill in the blank, Medium, Tue), folded into Q33: The anti-join is tested where it breaks, NOT IN against a list that holds a NULL, and the reason names LEFT JOIN with IS NULL as the fix.
- Bank 6 (Fill in the blank, Medium, Wed), folded into Q15: Option d rests on when LAG returns NULL, on a row with no earlier row that far back, and the reason says so.
- Bank 7 (Fill in the blank, Easy, Wed), folded into Q14: Bank 27's key is a rank computed within PARTITION BY segment, so the clause that restarts a window for each segment is the item's answer.
- Bank 8 (Fill in the blank, Medium, Thu), folded into Q19: The guard the item keys is validate='one_to_one', and its reason names the MergeError it raises.
- Bank 9 (Fill in the blank, Easy, Thu), folded into Q21: The code melts the wide view back to one row per member and month, and predicting its row count needs the rule that melt lengthens.
- Bank 10 (True or false, Easy, Mon), folded into Q2: Ordering all six clauses tests where SELECT sits against WHERE.
- Bank 11 (True or false, Medium, Mon), folded into Q32: The item's reason says why the group filter sits in HAVING and never in WHERE, and its wrong option b is the HAVING-first reading.
- Bank 12 (True or false, Easy, Tue), folded into Q9: The WHERE on the payments table turns the LEFT JOIN into an INNER one and drops the unpaid order without a word, which is the statement bank 12 tested.
- Bank 13 (True or false, Medium, Tue), folded into Q7: The item sizes the fan-out in rows before any rupee is summed, the mechanism by which a join inflates a SUM while every row looks right.
- Bank 14 (True or false, Hard, Wed), folded into Q12: The item's two ties make RANK and DENSE_RANK part company, the only case in which they differ.
- Bank 15 (True or false, Medium, Wed), folded into Q14: Bank 27's key filters the rank in an outer query, which is the reason a window cannot sit in WHERE.
- Bank 16 (True or false, Easy, Thu), folded into Q21: The pivot groups the orders by member and month and returns one cell per group, and predicting that cell is predicting what groupby returns.
- Bank 17 (True or false, Easy, Fri), folded into Q18: The item asks whether a pivot on a table with repeated rows reports the true total, on the week's own numbers.
- Bank 18 (One correct option, Easy, Mon), folded into Q2: Ordering all six clauses tests which one the database runs first.
- Bank 19 (One correct option, Medium, Mon), folded into Q2: A syntax error is never an item (CLAUDE.md); the rule behind this one, that SELECT runs after GROUP BY and so sees only grouped columns and aggregates, is the order Q2 tests.
- Bank 20 (One correct option, Medium, Mon), folded into Q5: The item's premise is why the Monday suite lives in the warehouse, and its key names the one change that would move a number out of it.
- Bank 21 (One correct option, Easy, Tue), folded into Q7: The item's third count, count(p.payment_id), is the matched rows an INNER JOIN would keep.
- Bank 22 (One correct option, Medium, Tue), folded into Q7: The item sizes exactly how a LEFT JOIN from orders to payments grows past the orders it started from.
- Bank 23 (One correct option, Medium, Tue), folded into Q8: The report must drop the gateway's repeats by order and instalment, since HAVING count(*) > 1 by order alone also lists the 188 invoices paid in two instalments; the reason gives both counts.
- Bank 24 (One correct option, Hard, Tue), folded into Q7: The first check after a doubled total is the row count before and after the join, which this item asks for in numbers.
- Bank 25 (One correct option, Easy, Wed), folded into Q12: The item asks what RANK does after a tie, on the week's real boundary.
- Bank 26 (One correct option, Medium, Wed), folded into Q12: The item asks what DENSE_RANK does after a tie, and its second tie shows the missing gap changing the count.
- Bank 28 (One correct option, Hard, Wed), folded into Q34: The item predicts a running total whose ORDER BY ties, the cause bank 28 names, and its reason gives the tiebreaker.
- Bank 29 (One correct option, Medium, Thu), folded into Q21: The item's reason walks pivot_table as split, apply and combine, with the default mean as the apply step.
- Bank 30 (One correct option, Medium, Thu), folded into Q17: The item sizes a merge that grew because keys repeat on the right, on the week's own feed.
- Bank 31 (One correct option, Medium, Fri), folded into Q23: The match row asks for the lookup that says so when an id is missing, with VLOOKUP's default approximate match as the spare beside it.
- Bank 32 (One correct option, Medium, Fri), folded into Q5: The item's key is the one job that belongs in Excel, a what-if a director changes in the room.
- Bank 33 (More than one correct, Medium, Mon), folded into Q32: Predicting the rows needs every statement bank 33 makes about WHERE, HAVING and COUNT(*).
- Bank 34 (More than one correct, Medium, Tue), folded into Q10: The item's table is the validation bank 34 asks for, and the item goes on to what to do when one check fails.
- Bank 35 (More than one correct, Hard, Tue), folded into Q7: Option d counts the payments with no order as if they had joined, and its reason says only a FULL OUTER JOIN brings in one side's orphans beside the other's.
- Bank 36 (More than one correct, Hard, Wed), folded into Q14: Top three per segment is one of the questions only a window answers, and the lag and running-total items test the other two.
- Bank 37 (More than one correct, Hard, Wed), folded into Q13: The item is the head of Retail-Plus's ask on the week's real tie, with each claim of bank 37 as an option.
- Bank 38 (More than one correct, Medium, Thu), folded into Q19: The item tests what merge does to rows, what validate= does and why the row count is still worth checking.
- Bank 39 (More than one correct, Medium, Fri), folded into Q16: The front-page line must carry its period and its comparison, and each wrong option drops one.
- Bank 40 (Scenario set, Medium, Tue), folded into Q7: The same LEFT JOIN count on the week's Q2 book, with instalments as well as repeats.
- Bank 41 (Scenario set, Medium, Tue), folded into Q7: The matched rows are the INNER JOIN's count, the item's third number.
- Bank 42 (Scenario set, Medium, Tue), folded into Q33: The unpaid list is the anti-join; the item tests the pattern that fails and names the ones that work.
- Bank 43 (Scenario set, Medium, Tue), folded into Q8: Dropping the repeats before the sum is the item's first step, because a plain SUM counts each repeat twice.
- Bank 44 (Scenario set, Medium, Wed), folded into Q12: RANK after a tie, on the week's boundary.
- Bank 45 (Scenario set, Medium, Wed), folded into Q12: DENSE_RANK after two ties, on the week's boundary.
- Bank 46 (Scenario set, Hard, Wed), folded into Q12: The item counts what a DENSE_RANK cut keeps.
- Bank 47 (Scenario set, Hard, Wed), folded into Q13: Exactly fifty by ROW_NUMBER with a tiebreaker is option c, with its cost named.
- Bank 48 (Scenario set, Medium, Thu), folded into Q17: The same merge count on the week's own feed.
- Bank 49 (Scenario set, Medium, Thu), folded into Q19: validate='one_to_one' is one of the two guards the item keys.
- Bank 50 (Scenario set, Medium, Thu), folded into Q18: The same claim about the pivot's total, on the week's numbers.
- Bank 51 (Scenario set, Hard, Thu), folded into Q20: The same question, where the fix belongs, with the business rule that repairs the feed.
- Bank 52 (Applied maths, Easy, Mon), folded into Q32: The item turns on GROUP BY returning one row per value that survives WHERE, and no row for a value that does not.
- Bank 53 (Applied maths, Medium, Tue), folded into Q8: The Rs 20,750 the repeats add to a plain SUM is why the item's first step comes first.
- Bank 54 (Applied maths, Hard, Wed), folded into Q12: RANK ships 51 and ROW_NUMBER 50 on the week's tie at fiftieth.
- Bank 55 (Applied maths, Medium, Wed), folded into Q15: The item runs the falling flag with LAG on four members, two of them with a missing month.
- Bank 56 (Applied maths, Medium, Thu), folded into Q1: Orders per member is the same ratio of two counts, and the trap is the same integer division.
- Bank 58 (Order the steps, Medium, Fri), folded into Q5: The item places one number in the warehouse, an export or a workbook, and its reason gives the one direction a number travels, from the warehouse through pandas to Excel.

## Stems and situations reworded on the bank, waiting for the tracker

These items print with a stem or a situation the tracker does not carry, each for the reason given; the key is the tracker's. Accept one by copying the wording into the tracker; reject it by deleting it from `data/programme/paper_edits.yaml`.

- Bank 27, Q14, stem (proposed): The tracker's stem asks for top three per segment with no business context. The new stem opens on Marketing's first protect list, sorted over every member, and the numbers it produced on Wednesday, so the item asks why that list fails before it asks for the approach; the options and the key are the tracker's.

## Option edits laid on the bank, waiting for the tracker

These options differ from the tracker's wording or order, each for the reason given beside it. The correct options are the tracker's; where the options are relabelled, the key's letters move with them. Accept an edit by copying it into the tracker; reject it by deleting it from `data/programme/paper_edits.yaml`.

- Bank 19, folded into Q2, option b (accepted): The key was the longest option.
- Bank 22, folded into Q7, option c (accepted): The key was the longest option; the new distractor is the fan-out misread in reverse.
- Bank 23, folded into Q8, option b, d (accepted): The key was the longest option; the distractor is now the full query with the aggregate in WHERE. Option b then ran 38 characters against 73, so it now sorts its distinct list too, and the options run 47 to 73.
- Bank 29, folded into Q21, option a (accepted): The key was the longest option.
- Bank 32, folded into Q5, option c (accepted): The key was the longest option.
- Bank 33, folded into Q32, option c, d; options relabelled, printed a as the tracker's a, b as the tracker's d, c as the tracker's b, d as the tracker's c (accepted): Options ran 22 to 39 characters, with c at 23 and d at 22 against b at 39; c and d now say which clause can compare COUNT(*) with a number, and the options run 34 to 41. Every more-than-one key on the paper held a, and four of the seven were exactly a, b and c. The options are relabelled a, d, b, c, so the wrong option prints at b, the two WHERE statements sit together, and the same three stay correct.
- Bank 34, folded into Q10, option d; options relabelled, printed a as the tracker's d, b as the tracker's a, c as the tracker's b, d as the tracker's c (accepted): The font was a nonsense option, so striking it left a, b and c, which is the whole key; the new distractor is a check that sounds like the other three and cannot catch a fan-out. Every more-than-one key on the paper held a, and four of the seven were exactly a, b and c. The options are relabelled d, a, b, c, so the wrong option prints at a and the same three stay correct.
- Bank 35, folded into Q7, options relabelled, printed a as the tracker's c, b as the tracker's a, c as the tracker's d, d as the tracker's b (accepted): Every more-than-one key on the paper held a, and four of the seven were exactly a, b and c. The options are relabelled c, a, d, b, so the two wrong options print at a and c and the same two stay correct.
- Bank 36, folded into Q14, option b (accepted): Option b ran 25 characters against 60; it now names the quarter its total covers, and the options run 37 to 60.
- Bank 37, folded into Q13, option b (accepted): Option b, part of the key, ran 37 characters against 63; it now says who ties, and the options run 40 to 63.
- Bank 38, folded into Q19, option a (accepted): Option a, part of the key, ran 35 characters against 60; it now says the join is on a key, and the options run 40 to 60.
- Bank 39, folded into Q16, option d (accepted): Cell colour was a nonsense option, so striking it left a, b and c, which is the whole key; the new distractor is the precision a room reaches for when a number is misread.
- Bank 42, folded into Q33, option b, d (accepted): The key was the longest option; the distractor keeps the table-qualified column the key uses. Option d ran 16 characters against 51; it is now the anti-join from the payments side, which finds payments with no order, and the options run 37 to 51.
- Bank 47, folded into Q13, option a (accepted): The key was the longest option.
- Bank 51, folded into Q20, option a (accepted): The key was the longest option.

## Levels and paces the paper sets

The tracker's level or minutes for these items differ from what the paper, as reworded, asks of the room.

- Q3 (bank 2): 1.5 minutes, where the tracker says 1
- Q4 (bank 3): 1.5 minutes, where the tracker says 1
- Q14 (bank 27): 2.5 minutes, where the tracker says 2

## The stretch page

- Stretch 1: A repeat is the same order and the same instalment posted twice for the same amount; the date is not part of that identity, so the rule keys on order and instalment and keeps the first posting. I would add a check that no instalment is paid more than once and list any that is, with its dates, for Anand's analyst to confirm, rather than dropping it silently.
- Stretch 2: All three take rank 49, so every one of them holds a rank of 50 or better and the list ships 51 members. The note says so in one line: 51 members, because three tie at forty-ninth, and names the three.
- Stretch 3: Excel turned some gene symbols into dates in about a fifth of papers with Excel gene lists, so the naming body renamed the genes it could not protect any other way, fixing the error at the source every reader shares. I would still count, after every merge, how many keys found a match, because a key changed on its way in never raises an error.
- Stretch 4: Rs 19.84 crore is real and covers two quarters, so a director reads it as a quarter that doubled. The page reads: Q2, July to September, Rs 9.84 crore, down 1.6 percent on Q1's Rs 10.00 crore.

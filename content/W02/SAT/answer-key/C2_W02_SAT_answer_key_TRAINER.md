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
| 1. Anand's Monday numbers | whether you read a query the way the database runs it, and place each piece of work where it belongs | Q1 to Q6 (6) | 16 | 2 | 2 | 2 |
| 2. Booked against collected | whether you size a join before it runs, order the steps of a reconciliation, and decide what leaves when a check fails | Q7 to Q11 (5) | 20 | 0 | 0 | 5 |
| 3. The protect list and the plan line | whether you rank within a segment by the rule the business set, and read a monthly flag and a plan line before anyone acts | Q12 to Q16 (5) | 17 | 0 | 2 | 3 |
| 4. One row per customer | whether you size a merge, place the guard that stops a double count, and read a pivot that averages or a key that changed on its way in | Q17 to Q22 (6) | 19.5 | 0 | 3 | 3 |
| 5. The last mile, and spreadsheets in public | whether you match each workbook job to the technique that does it, and work a spreadsheet error through before the room sees it | Q23 to Q29 (7) | 22 | 0 | 4 | 3 |
| 6. Read the code, read the data: an AI team's tables | whether you catch the week's traps in the tables an AI team keeps, from evaluation runs to an assistant's logs | Q30 to Q35 (6) | 22.5 | 0 | 1 | 5 |
| Total | | 35 | 117 | 2 | 12 | 21 |

## What guessing alone would score

A learner who guessed every item blind would average 6.4 of 35, since a written answer cannot be guessed from a list, and fewer than one guesser in twenty would reach 11. A score of 10 or below is therefore within reach of guessing alone, and the tally reads such a paper as a conversation to have on Monday, never as a result.

## Reading the items after marking

The workbook flags an item to check when fewer than one learner in five got it right, or when the bottom third of the room got it right more often than the top third. Both are this programme's own working rule for a room of 35. A flagged item is discussed as usual; the TA also sends it, with the room's rate, to the tracker's owner, because the fault may sit in the item rather than in the learners.

## The key

| Q | Key | Type | Part | Level | Tag | Roles | Day | Min | Source | Interview anchor |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | It prints 2 and 1. The true figures are 2.36 and 1.84, a fall of about 22 percent. | Applied maths | 1 | Hard | [F] | BA, DS | Mon | 4 | new | A stakeholder's analyst must audit your query; what changes in how you write it, and what would you refuse to compute in a notebook? |
| 2 | c, b, e, f, a, d | Order the steps | 1 | Medium | [S] | BA, DS | Mon | 2.5 | bank 57 | Explain the logical order in which a SQL query executes. |
| 3 | d (guarantee) | Fill in the blank | 1 | Easy | [F] | BA, DS | Mon | 1.5 | bank 2 | What does LIMIT without ORDER BY return? |
| 4 | b (CTE) | Fill in the blank | 1 | Easy | [S] | BA, DS | Mon | 1.5 | bank 3 | Explain the logical order in which a SQL query executes. |
| 5 | b | One correct option | 1 | Medium | [D] | BA, DS | Mon | 2.5 | new | Why would you compute a KPI in the warehouse rather than in a notebook? |
| 6 | d | One correct option | 1 | Hard | [D] | BA, DS | Mon | 4 | new | How do you present one number so it is not misread? |
| 7 | b | Scenario set | 2 | Hard | [F] | BA, DS | Tue | 4 | new | Your LEFT join grew the row count and revenue doubled; name the cause and the check. |
| 8 | e, f, b, c, a | Order the steps | 2 | Hard | [D] | BA, DS, FDE | Tue | 4 | new | Design the validation you run before a joined number reaches Finance, and say what you do when it fails at the end of reporting day. |
| 9 | b | One correct option | 2 | Hard | [S] | BA, DS, FDE | Tue | 4 | new | INNER against LEFT join: what does each drop or keep? |
| 10 | c | One correct option | 2 | Hard | [D] | BA, FDE | Tue | 4 | new | Design the validation you run before a joined number reaches Finance, and say what you do when it fails at the end of reporting day. |
| 11 | b, d | More than one correct | 2 | Hard | [D] | BA, DS, FDE | Tue | 4 | new | Design the validation you run before a joined number reaches Finance, and say what you do when it fails at the end of reporting day. |
| 12 | a | Scenario set | 3 | Hard | [S] | BA, DS | Wed | 4 | new | RANK, DENSE_RANK and ROW_NUMBER on a tie. |
| 13 | c | Scenario set | 3 | Medium | [D] | BA, DS | Wed | 2.5 | new | The business says 'ties rank the same'; which function, and how many rows might the top-N report ship? |
| 14 | b | One correct option | 3 | Medium | [S] | BA, DS | Wed | 2.5 | bank 27 | Top-3 per group: GROUP BY or a window, and why? |
| 15 | c | One correct option | 3 | Hard | [F] | BA, DS | Wed | 4 | new | How would you find customers whose spend fell two months in a row? |
| 16 | a | One correct option | 3 | Hard | [D] | BA, FDE | Wed | 4 | new | How do you present one number so it is not misread? |
| 17 | 346 | Scenario set | 4 | Medium | [F] | BA, DS | Thu | 2.5 | new | merge against join: what is the same and what differs? |
| 18 | d | Scenario set | 4 | Medium | [F] | BA, DS, FDE | Thu | 2.5 | new | A pivot's total disagrees with the warehouse; where do you look first? |
| 19 | a, e | Scenario set | 4 | Medium | [F] | BA, DS, FDE | Thu | 2.5 | new | Which merge argument raises on duplicate keys, and which error? |
| 20 | d | Scenario set | 4 | Hard | [D] | BA, DS, FDE | Thu | 4 | new | A pivot's total disagrees with the warehouse; where do you look first? |
| 21 | b | One correct option | 4 | Hard | [S] | BA, DS | Thu | 4 | new | pivot against melt: which widens and which lengthens? |
| 22 | a | One correct option | 4 | Hard | [D] | BA, DS | Thu | 4 | new | SQL, pandas or Excel: how do you choose? |
| 23 | d (XLOOKUP with its if_not_found argument set) | Match the following | 5 | Medium | [F] | BA | Fri | 2.5 | new | A stakeholder wants to poke the numbers themselves; what do you give them and what do you never give them? |
| 24 | a (SUBTOTAL with function number 109) | Match the following | 5 | Medium | [F] | BA | Fri | 2.5 | new | Your pivot shows a different total from the warehouse; where do you look first? |
| 25 | f (a first-row flag per order, then SUMIFS) | Match the following | 5 | Medium | [F] | BA, DS | Fri | 2.5 | new | A pivot's total disagrees with the warehouse; where do you look first? |
| 26 | c (a labelled input cell feeding a scenario line) | Match the following | 5 | Medium | [D] | BA, FDE | Fri | 2.5 | new | Two directors change assumptions in the room and the sheet recalculates differently for each; what did you get right and what do you fix? |
| 27 | B8 returns -0.5; the six rows average 1.0; the formula understates growth by 1.5 points and turns growth into a fall. | Applied maths | 5 | Hard | [F] | BA, DS, FDE | Fri | 4 | new | Your pivot shows a different total from the warehouse; where do you look first? |
| 28 | b | One correct option | 5 | Hard | [D] | BA, DS, FDE | Fri | 4 | new | Same question, three tools: how do you choose, and defend one choice? |
| 29 | 2.00 dollars, about 8.5 percent of the 23.50 dollars charged | Applied maths | 5 | Hard | [F] | BA, FDE | Fri | 4 | new | How do you present one number so it is not misread? |
| 30 | c | One correct option | 6 | Hard | [F] | DS | Thu | 4 | new | Your LEFT join grew the row count and revenue doubled; name the cause and the check. |
| 31 | d | One correct option | 6 | Hard | [S] | DS | Wed | 4 | new | RANK, DENSE_RANK and ROW_NUMBER on a tie. |
| 32 | a | One correct option | 6 | Hard | [S] | DS | Mon | 4 | new | WHERE against HAVING, one sentence each. |
| 33 | c | One correct option | 6 | Hard | [F] | DS, FDE | Tue | 4 | new | How do you find orders with no payment? |
| 34 | a | One correct option | 6 | Hard | [F] | DS | Wed | 4 | new | RANK, DENSE_RANK and ROW_NUMBER on a tie. |
| 35 | d | One correct option | 6 | Medium | [F] | BA, DS | Mon | 2.5 | new | How do you present one number so it is not misread? |

## Why each answer holds

### Q1, key It prints 2 and 1. The true figures are 2.36 and 1.84, a fall of about 22 percent.

**Why it holds.** count(*) and count(DISTINCT customer_id) are both integers, so Postgres divides integers and drops the fraction: 215 / 91 prints 2 for April to June, and 140 / 76 prints 1 for July to September. The true figures are 2.36 and 1.84, and 1.84 against 2.36 is a fall of about 22 percent; accept 21 to 22 percent, or about a fifth. A note that quotes the printed 2 and 1 says orders per member halved, which is Monday's round 2 trap. The fix is count(*)::numeric, and the check is to multiply back: 1 times 76 members is 76, against 140 orders. Run on PostgreSQL 16.13 on the week's warehouse on 30 September 2026.

**In the interview.** Orders per member is a ratio of two counts, and Postgres divides two integers as integers, so I cast one side to numeric and multiply back by the denominator before the number leaves.

### Q2, key c, b, e, f, a, d

**Why it holds.** The logical order is FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY: rows are read, filtered, grouped, and the groups filtered, before anything is selected or sorted. The common wrong answer is the order the clauses are typed, a, c, b, e, f, d, which puts SELECT first; the database cannot pick columns from rows it has not yet read, filtered and grouped. The same order explains why a SELECT alias works in ORDER BY and fails in WHERE, and why SELECT can name only grouped columns and aggregates.

**In the interview.** FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY, and most of the errors a query can raise follow from it.

### Q3, key d (guarantee)

**Why it holds.** A table has no stored order, so without ORDER BY the database returns whichever rows its plan reaches first, and two runs can differ: Monday's sample of five delivered app orders summed to Rs 3,900 and, after a reload that rewrote two rows with their own values, to Rs 4,590. Every word in the bank is a noun and fits the blank's grammar; only guarantee fits its sense. "sort" is the near miss, since a plan that reads an index may well return sorted rows on some runs, which is why a sample can look stable until a reload; what the database withholds is the promise.

**In the interview.** LIMIT without ORDER BY returns some rows, never defined ones, so I order on a unique key before I limit.

### Q4, key b (CTE)

**Why it holds.** WITH names a common table expression, a step the rest of the query reads like a table. A subquery is the near miss: it is inline and unnamed. A view is named too, but it is stored with CREATE VIEW, never introduced by WITH.

**In the interview.** A CTE names each step of the logic, so an auditor reads the query top to bottom, one decision per block.

### Q5, key b

**Why it holds.** Anand's rule is about the reported number, which comes from a saved query that reruns unchanged on the book every Monday and can be read line by line. A first look at a question reports nothing: charts, tests and the first reading of a question belong in a notebook, and a notebook that reads the warehouse works on the same book as the suite. The one direction a number travels is from the warehouse, through pandas for the analyst's iteration, to Excel for the room; once the head of Retail-Plus decides what to report, that number becomes a query in the suite.

- (a) Stretches the rule past its purpose: it governs the numbers Finance receives, and a suite that holds every exploratory chart stops being a list an analyst can audit.
- (c) An export is stale the day it lands and a workbook can be typed over, which is what Anand's rule rules out; Excel is where a finished number meets the room.
- (d) Exploration is how a definition gets agreed; refusing to look leaves Finance to define the number blind.

**In the interview.** The reported number lives in the warehouse because it reruns unchanged on the source and every line can be audited; exploration lives in a notebook that reads the warehouse, and Excel presents what has been decided.

### Q6, key d

**Why it holds.** The CASE has no ELSE, so it returns NULL for the two viewers under three seconds, and count skips NULLs: the calculated average divides all 30 seconds by 3 people, 10.0, where the defined one divides by all 5 who played, 6.0. Against the defined figure, 10.0 overstates 6.0 by 4.0 over 6.0, about 67 percent. TechCrunch (Devin Coldewey, 22 September 2016) quoted Facebook's definition and its calculation, put the inflation at 60 to 80 percent over two years and reported that billing was not affected; checked on 30 September 2026. Run on PostgreSQL 16.13 on 30 September 2026.

- (a) Divides the gap by the wrong base: 4.0 over the calculated 10.0 is 40 percent, and an overstatement is measured against the true figure, the defined 6.0.
- (b) Averages the three long viewers alone, (14 + 9 + 4) / 3 = 9.0; the numerator stayed all the time watched, the short viewers' 3 seconds included.
- (c) count(CASE WHEN ... THEN 1 END) counts only the non-NULL results, and a CASE with no ELSE returns NULL for the viewers it does not match; Monday's round 3 trap in another form.

**In the interview.** An average is defined by its denominator; when a filter or a CASE quietly shrinks it, the average rises with no change in the data, so I print the numerator and the denominator beside the ratio.

### Q7, key b

**Why it holds.** A LEFT JOIN writes one row per matching payment row and keeps an order with none as one row of NULLs: 216 + 2 times 188 + 2 times 28 + 30 = 678 rows. count(DISTINCT o.order_id) counts the 462 orders, and count(p.payment_id) skips the 30 unpaid orders' NULLs, 678 minus 30 = 648, which is also what an INNER JOIN would return. The eight payments with no order never meet an order, so they are in none of the counts. Run on PostgreSQL 16.13 on the week's warehouse on 30 September 2026.

- (a) Reads the join as keeping one row per order, and payment rows as one per paid order (462 minus 30 = 432); a join repeats an order once per matching row, which is Tuesday's round 1 fan-out.
- (c) count(p.payment_id) skips NULLs, and only count(*) counts the 30 unpaid orders' rows; reading count(column) as count(*) is Monday's round 1 trap inside a join.
- (d) Counts the eight payments with no order as if they had joined; a LEFT JOIN from orders keeps only rows that start from an order, and only a FULL OUTER JOIN brings in the payments whose order is missing.

**In the interview.** INNER keeps only matched rows and LEFT keeps every order with NULLs where nothing matched; both repeat an order once per matching payment row, so I size the join, rows out against orders in, before any rupee is summed.

### Q8, key e, f, b, c, a

**Why it holds.** The step to leave out is d: 188 of the orders with two payment rows are instalments 1 and 2 of one invoice, and dropping them throws away real cash along with the 28 repeats. On the same book, HAVING count(*) > 1 by order lists 216 orders, and by order and instalment it lists the 28 repeats. The repeats go first (e), because a sum taken before them keeps the Rs 20,750 the gateway posted twice. The payment rows go to one figure per order (f) before the join (b), because only then does the join return one row per order: joined first, the rows come out at 650, the 462 orders plus 188 second instalments, and booked counts twice for every instalment order. The checks (c) come before anything is sent (a), and on Kalpa's book they read 462 rows and a gap of Rs 17,54,930, the unpaid orders' booked value exactly. Run on PostgreSQL 16.13 on the week's warehouse on 30 September 2026.

**In the interview.** De-duplicate at the grain that defines a repeat, aggregate to the join's grain, join, prove the row count and the gap, then send.

### Q9, key b

**Why it holds.** O-1's two instalments both fall inside the quarter, so the join gives O-1 two rows and sum(o.amount) counts its Rs 1,200 twice. O-2's only payment is dated 1 October, so its joined row fails the WHERE. O-3 has no payment, so its paid_date is NULL, BETWEEN on a NULL is unknown, and WHERE drops that row too. Two rows remain, booked Rs 2,400, against three orders worth Rs 2,500: the report lost two orders and doubled the one it kept. Run on PostgreSQL 16.13 on 30 September 2026.

- (a) Assumes one row per order, which holds only once payments are brought to one row per order; O-1 has two payment rows inside the quarter, so the join repeats it.
- (c) Keeps O-3 as if its NULL date passed the filter; a comparison with NULL is unknown, and WHERE keeps only rows where it is true, which is how the date filter in Tuesday's round 3 emptied the unpaid list.
- (d) Reads the WHERE as if it sat in the ON clause, where it would keep every order with NULL payments on O-2 and O-3; in WHERE it runs after the join and turns the LEFT JOIN into an INNER one, which is Tuesday's round 3 trap.

**In the interview.** A filter on the right-hand table of a LEFT JOIN belongs in ON, because WHERE runs after the join, drops the NULL rows and turns the LEFT JOIN back into an INNER one; and the payments go to one row per order before the join.

### Q10, key c

**Why it holds.** The gaps are app Rs 8,120 and store Rs 9,57,810, each equal to its unpaid list to the rupee, and web Rs 8,10,750, which exceeds its list's Rs 7,89,000 by Rs 21,750 that nobody has explained. Booked passed its checks, so it goes for every channel; app's and store's collected reconcile, so they go; web's collected waits, with the Rs 21,750 named as an open line with an owner and a time. The Tuesday pack's rule is to send what reconciles with its definition and name the line that does not close. The figures are illustrative: on Kalpa's own book, web's gap equals its unpaid list at Rs 7,89,000.

- (a) Adding the unexplained Rs 21,750 to web's unpaid list forces the bridge closed and puts on the list an amount that no unpaid order carries.
- (b) Store has the largest gap, and its gap equals its unpaid list to the rupee; the channel whose bridge fails is web, by Rs 21,750.
- (d) Holds back two collected figures that reconcile to the rupee; Anand loses app's and store's collected over a doubt that concerns web alone.

**In the interview.** Before a joined number reaches Finance I check rows in against rows out, the total against its source and the gap against a named list; when one fails at the end of the reporting day, what reconciles goes out, what does not waits, and the open line is named with its amount, an owner and a time.

### Q11, key b, d

**Why it holds.** Lab B's file lost 5,365 records in the conversion, 70,900 in the CSV against 65,535 rows in the sheet. Comparing rows loaded with the lab's own count of records sees the loss, and a sheet at exactly 65,535 data rows sits at the format's limit, which a check can treat as a stop. Rows loaded and rows in the sheet were both counted after the cut, so they agree, and Lab B loaded more rows than the day before, 65,535 against 61,020, so neither of those checks fires. That is Tuesday's habit, rows in against rows out, taken back to the first count in the chain. The facts are from the GOV.UK statement of 4 October 2020 (15,841 cases between 25 September and 2 October; files that exceeded the maximum file size) and The Register of 5 October 2020 (lab CSV files stored in the older .xls format, 65,536 rows a sheet, records past the limit left off and not counted), both checked on 30 September 2026; the three labs' counts are illustrative.

- (a) Rows loaded and data rows in the sheet were both counted after the conversion cut the file, so they agree at 65,535 and the check passes.
- (c) De-duplication removes rows; it cannot find rows that were never loaded.
- (e) Lab B loaded 65,535 rows against 61,020 the day before, so a check for a fall stays quiet while 5,365 records go missing; a day-on-day check sees only a loss larger than the day's growth.

**In the interview.** Any step that can drop rows without a warning needs a count on both sides of it, taken back to the first count in the chain, and the load stops when they differ; raising a limit only moves the cliff.

### Q12, key a

**Why it holds.** RANK gives C-0185 and C-0242 the shared rank 50 and C-0259 rank 52, so 51 members hold a rank of 50 or better. DENSE_RANK leaves no gaps, so the tie at 48 (C-0189 and C-0206) makes C-0185 and C-0242 dense rank 49 and C-0259 dense rank 50: 52 members. ROW_NUMBER numbers every row once: 50. Run on PostgreSQL 16.13 on the week's warehouse on 30 September 2026.

- (b) Sees one tie at the line and reads DENSE_RANK as RANK without the gap; the second tie, at 48, compresses the dense numbers so that C-0259 reaches 50. That is Wednesday's trap, where "ties rank the same" quietly shipped 52.
- (c) Reads RANK as capping the list at fifty; RANK gives both tied members 50 and keeps both.
- (d) Swaps the two functions: RANK leaves a gap after each tie, and DENSE_RANK does not.

**In the interview.** ROW_NUMBER gives every row its own number and breaks ties arbitrarily, RANK shares a rank and skips the next, and DENSE_RANK shares without a gap; on a top-N list, RANK can ship more than N and DENSE_RANK more still, so I count what each rule ships before choosing.

### Q13, key c

**Why it holds.** The rule has two parts: members who spent the same share a rank, and the list keeps every member who spent at least as much as the fiftieth and nobody who spent less. RANK does both: C-0185 and C-0242 share rank 50 on Rs 3,350 and C-0259, on Rs 3,200, falls to 52. DENSE_RANK shares ranks too, and because it never skips, the earlier tie at 48 lifts C-0259 to dense rank 50. The note to Marketing gives the list's length and the tie that sets it.

- (a) Shares ranks, and then keeps C-0259, who spent Rs 3,200, less than both members at the fiftieth place; that is Wednesday's trap, where "ties rank the same" quietly shipped a member below the line.
- (b) Keeps exactly fifty, the same every Monday, by dropping C-0242, who spent exactly what the fiftieth did, on an id nobody chose on purpose; if the budget demands fifty, the tiebreaker is a decision the head of Retail-Plus owns.
- (d) Gives members who spent the same different numbers and lets the database choose which of C-0185 and C-0242 stays, so the list can change between two runs.

**In the interview.** When the business says ties rank the same, I use RANK and state the list's length and its reason in the same line, because the list can ship more than N; if the budget demands exactly N, the tiebreaker becomes a decision someone owns.

### Q14, key b

**Why it holds.** A rank computed within PARTITION BY segment keeps every customer and restarts for each segment; the outer query keeps the rows ranked three or better. The window has to be filtered outside, because WHERE runs before any window is computed. The whole-table list in the stem is Wednesday's round 1 trap: 35 Business customers, 11 Retail-Plus members, 4 Retail-Core customers and no Student, since Business carries 99 percent of the quarter's revenue.

- (a) GROUP BY collapses each segment to one row, so the customers are gone before LIMIT runs, and LIMIT applies once to the whole result, never per group.
- (c) One ORDER BY with LIMIT 3 is the whole-table list at a smaller size: the top three overall, all Business, which is the first draft's mistake again.
- (d) HAVING keeps or drops whole groups by an aggregate; it cannot choose rows inside a group.

**In the interview.** Top N per group is a window: rank inside PARTITION BY the group in a CTE, keep rank N or better outside it, and name the tie rule.

### Q15, key c

**Why it holds.** LAG reads the previous row in the partition, never the previous calendar month. C-0161 and C-0171 fell from July to August and again from August to September, so both are flagged, and rightly. C-0185's September is compared with July (1,450 below 1,900) and July with June (1,900 below 2,690), and C-0216's September with July and July with May (2,540 below 4,300, below 6,440), so both are flagged too, although neither ordered in August: two calls tell a member their spend fell in August and September when there was no August reading at all. A calendar check, that the two rows LAG reads are August and July, keeps the two genuine falls. Run on PostgreSQL 16.13 on the week's warehouse on 30 September 2026.

- (a) Assumes LAG steps back one calendar month, so C-0185 and C-0216 would meet an empty August and drop out; LAG returns whatever row came before in the window's order, and both are flagged.
- (b) Assumes LAG(spend, 2) returns NULL for C-0216; it has rows for May, July and September, so on its September row LAG(spend, 2) returns May's 6,440. LAG returns NULL only on a member's first rows, and a comparison with that NULL flags nobody.
- (d) Reads the query's output as the business answer; a member with no August order has no August reading, and C-0216 is the member in Wednesday's case who said he was on holiday.

**In the interview.** One row per customer per month, LAG 1 and LAG 2 partitioned by customer and ordered by month, a check that the lagged rows really are the previous two calendar months, and a flag where each month is below the one before; a month with no order is no reading.

### Q16, key a

**Why it holds.** Booked less plan at the seven points reads -0.25, +1.95, +2.17, +1.57, +0.73, +0.79 and 0.00 crore: behind after the first week, well ahead once the week of 13 July booked Rs 2.66 crore, furthest ahead at the start of August, and level at the close, Rs 9,84,00,000 against a plan of Rs 9,83,99,990. The weekly rate did the giving back: six of the seven full weeks from 10 August booked below the plan's Rs 75.69 lakh a week. A front-page line carries its period and its comparison, so a director reads the close and the trend together. The figures are the week's own running total against plan_line, recomputed on PostgreSQL 16.13 on 30 September 2026.

- (b) The lead peaked at Rs 2.17 crore at the start of August and was gone by the close, where booked and plan both read Rs 9.84 crore.
- (c) Booked stayed above plan at every point after the first week; the quarter gave back its lead and never fell behind.
- (d) At its widest the lead was Rs 2.17 crore, more than a fifth of the quarter's plan, which is a lead worth a line.

**In the interview.** One number goes out with its period, its base and its comparison, here the quarter's close against plan and the trend that brought it there, so it is read the way it was meant.

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

### Q20, key d

**Why it holds.** The two sends differ in exposed_date, so they do not repeat in every column, and the file is newest first, so each repeated customer's first row as listed is the 11 August send. Sorting by exposed_date from the earliest and then keeping each customer's first row leaves 3 August for C-0001 and C-0002 and C-0012's one row: 130 rows, one per customer, and the merge returns 340 rows with spend on the book. Run on pandas 3.0.5 on the week's feed, sent newest first, on 30 September 2026.

- (a) The two sends differ in exposed_date, 3 and 11 August, so no row repeats in every column and all 136 stay.
- (b) The file is newest first, so each repeated customer's first row as listed is the 11 August send, the second exposure.
- (c) The merge keeps each customer's feed rows in the file's order, so keeping the first merged row keeps 11 August; the table has one row per customer and the wrong exposure on two of them.

**In the interview.** Fix the error where it was made, at the feed, with a rule the business agrees and a sort that makes first mean first by date, and keep the guard on so next week's feed fails loudly instead of quietly.

### Q21, key b

**Why it holds.** pivot_table splits the orders by member and month, applies its default aggfunc, which is the mean, and combines one cell per group, so M1's two June orders print as their average, 2000.0, where M1 spent 4,000. melt turns the 2 by 2 view back into 4 rows, one per member and month, including M2's empty July, and sum skips that NaN: 2,000 + 2,400 + 1,800 = 6200.0 against 8,200 of orders. The check is the grand total against the orders, and the fix is aggfunc='sum' with fill_value=0; on Kalpa's Retail-Plus months the default read a fall of 18 percent where the orders fell 29. Run on pandas 3.0.5 on 30 September 2026.

- (a) Assumes the pivot adds; it averages unless aggfunc says otherwise, which is Thursday's round 3 trap.
- (c) Drops the empty cell in melt; melt keeps every member and month, NaN included, which is why the long table has 4 rows.
- (d) Both misreadings at once.

**In the interview.** pivot_table widens a column's values into columns and averages unless told to sum; melt lengthens it back into rows; I write aggfunc= every time and tie the grand total to the source.

### Q22, key a

**Why it holds.** A left merge keeps all 4 of the lab's rows; '2-Sep' and '1-Mar' match no symbol, so indicator marks them left_only: 2. Nothing raises, and two genes lose their annotation without a word. The fix belongs at the source, a list the lab keeps as text, and the naming body later fixed the source every reader shares: in 2020 the HGNC renamed the genes whose symbols Excel turned into dates, so SEPT1 became SEPTIN1 and MARCH1 became MARCHF1 (Bruford and colleagues, Nature Genetics, 2020). Both papers checked on 30 September 2026; the code run on pandas 3.0.5 the same day.

- (b) pandas reads the text it is given; '2-Sep' stays the string '2-Sep', and no parser turns it back into a gene symbol, so the analysis would go ahead on two unannotated genes.
- (c) A left merge never adds reference rows that nothing matched; how='right' or how='outer' would, and such a row would be marked right_only, never left_only.
- (d) A left merge keeps every left row, matched or not; how='inner' would keep 2, and the two genes it dropped would still need the lab, not an analyst's guess.

**In the interview.** A key that changed on its way in never matches and never raises, so after every merge I count the matches with indicator=True, and I fix the key at its source rather than in the analysis.

### Q23, key d (XLOOKUP with its if_not_found argument set)

**Why it holds.** XLOOKUP matches exactly by default, and its fourth argument, if_not_found, is what it shows for a code that is not in the list (Microsoft Support, XLOOKUP function, verified 29 September 2026). The spare beside it, VLOOKUP with its fourth argument left out, looks for an approximate match: on Friday it returned C-0194's Rs 16,740 for C-0195, a member with no orders.

**In the interview.** A lookup has two exits, the row or a visible "not in the table", and I test it with a code I know is missing.

### Q24, key a (SUBTOTAL with function number 109)

**Why it holds.** SUBTOTAL with function number 109 adds only the rows on screen, while SUM adds the rows a filter hides: on Friday, filtered to Mumbai's 11 members, SUBTOTAL(109, ...) read Rs 1,56,790 and SUM still read the whole list's Rs 7,14,890, a budget 4.6 times too big.

**In the interview.** A total under a filtered list is SUBTOTAL(109), and I say in the cell's label what it adds.

### Q25, key f (a first-row flag per order, then SUMIFS)

**Why it holds.** Friday's export repeats each order's booked amount on every payment row, so an order paid in two instalments carries its order_amount twice. Flagging the first row of each order, with =IF(COUNTIF($A$2:A2,A2)=1,1,0) filled down, and summing order_amount over the flagged rows with SUMIFS counts each order once: on Friday that took the raw export's Rs 39.41 crore back to the warehouse's Rs 19.84 crore. The spare beside it, Remove Duplicates across every column, removes only identical rows, and an instalment order's two rows differ in paid_amount, so 1,400 rows stayed and the total still doubled.

**In the interview.** The fix names the grain: one row per order, counted once, before any total is taken.

### Q26, key c (a labelled input cell feeding a scenario line)

**Why it holds.** An assumption is an input: a labelled cell beside the actual, feeding a scenario line, so the sheet recalculates in the room and the source stays tied to the warehouse. On Friday, the same Rs 5,00,000 typed over the quarter's cell read "down 14.6 percent" against Finance's 29.4, until Monday's refresh wiped it without a trace.

**In the interview.** Yes to the question, as a labelled scenario beside the actual; no to the edit, and a drift check ties the sheet to the warehouse on every refresh.

### Q27, key B8 returns -0.5; the six rows average 1.0; the formula understates growth by 1.5 points and turns growth into a fall.

**Why it holds.** B8 averages rows 2 to 5 alone: (-1.0 + 1.0 - 3.0 + 1.0) / 4 = -0.5. The six countries average (-1.0 + 1.0 - 3.0 + 1.0 + 5.0 + 3.0) / 6 = 1.0, so the formula understates the average by 1.5 percentage points and reports a fall where the group grew. In the paper, the coding error, compounded with other errors, took 0.3 percentage points off the published average for the highest debt group, overstated the lowest group by 0.1 and understated the second by 0.2; the replicators' corrected average for the highest group, 2.2 percent against the published -0.1, also corrects two other choices, so the range alone is not the whole gap (PERI working paper 322, April 2013, page 7, checked on 30 September 2026). The check that catches a range such as B2:B5 is a count of the rows each range covers against the rows in the table, run on every refresh; a Protect tab whose formulas stop at row 301 would miss every customer an export adds past the first 300.

**In the interview.** Every total in a workbook ties to a control total from the source on each refresh, and every range is checked against the rows it should cover, because a range that stops short fails without a sound.

### Q28, key b

**Why it holds.** Column D reads 0.60 / 4.60 = 0.130, -0.60 / 5.40 = -0.111 and 0.30 / 3.30 = 0.091; divided by the average instead, the changes are 0.261, -0.222 and 0.182. The sum is twice the average, so every change, rising or falling, comes out at half its size, and a model fed half-size moves reports less risk than the book carries: the report describes the effect as "muting volatility by a factor of two". A second way to the same number, by hand on one row or in a second tool, catches it: Kavya's review and Thursday's three-tool check. Quoted from the Report of JPMorgan Chase and Co. Management Task Force Regarding 2012 CIO Losses, 16 January 2013, pages 123 and 128, checked on 30 September 2026.

- (a) Dividing by the sum, which is twice the average, makes each change smaller; a change twice as large would need a divisor of half the average.
- (c) The falling rate comes out at half its size like the others, -0.111 against -0.222; the error does not depend on the direction of the move.
- (d) Dividing by the sum departs from the relative change the modeller meant, and on these rows it halves every change the model reads.

**In the interview.** A number that decides risk gets a second, independent calculation before it is trusted, because a formula can be wrong in every row at once.

### Q29, key 2.00 dollars, about 8.5 percent of the 23.50 dollars charged

**Why it holds.** The fares after tax and fees are 27.60, 18.40 and 40.00 dollars, so the commission due is 6.90, 4.60 and 10.00 against 7.50, 5.00 and 11.00 charged: 0.60 + 0.40 + 1.00 = 2.00 dollars, which is also 25 percent of the 8.00 dollars of tax and fees. Against the 23.50 dollars charged that is 8.5 percent, a share that repeats on every trip across tens of thousands of drivers, which is why a percentage's base is part of its definition. CBS News, 24 May 2017, checked on 30 September 2026; the fares and the rate here are illustrative.

**In the interview.** A percentage is defined only with its base, so before any rate is applied I write down what it is a percentage of.

### Q30, key c

**Why it holds.** A merge writes one row per matching label, so T3 and T5 appear twice: 7 rows. Both are tickets the model got wrong, so the mean counts 3 correct rows of 7, 0.43, against 3 correct tickets of 5, 0.6: the model fails the 0.5 bar on a score that counts its two misses twice. It is the fan-out of Tuesday's payments and Thursday's exposure feed, and the checks are the same: rows before and after, or validate='one_to_one'. Run on pandas 3.0.5 on 30 September 2026.

- (a) A merge repeats a left row once per matching right row; it keeps one row per ticket only when the labels are unique.
- (b) The repeated labels match their tickets, but the rows they repeat are misses, so the extra rows move the mean.
- (d) A repeat raises a score only when it repeats correct rows; here it repeats the two misses.

**In the interview.** An evaluation metric is a mean over one row per test case, so I size the join before scoring and validate that the labels are unique per case.

### Q31, key d

**Why it holds.** ROW_NUMBER partitioned by model and ordered by finished_on descending, then run_id descending, filtered to row 1 outside the window, returns bot-a's r2 (0.78) and bot-b's r5 (0.79) every time, and r5 is the later run because run ids follow the order runs start. With the date alone, bot-b's two runs of 9 September tie and the database picks one, so the leaderboard can show 0.86 one morning and 0.79 the next. Run on PostgreSQL 16.13 on 30 September 2026.

- (a) Each max() is taken on its own, so bot-a shows 8 September beside 0.81, a pairing no run produced: its latest date with its best score.
- (b) The right shape, but the tie on 9 September leaves the pick to the database; Wednesday's lesson on ties in a window's order.
- (c) RANK gives r4 and r5 the same rank 1, so bot-b shows two rows, the same two every morning, where the leaderboard wants one.

**In the interview.** The latest row per key is ROW_NUMBER partitioned by the key, ordered newest first with a tiebreaker that makes the order unique, kept at 1 in an outer query.

### Q32, key a

**Why it holds.** WHERE runs first and keeps the five low ratings: three for bot-a, one for bot-b and one for bot-c. GROUP BY forms its groups from those rows alone, so count(*) counts low ratings, and HAVING count(*) >= 3 keeps bot-a with 3. The lead asked for the models with at least three replies in all, bot-a with 4 and bot-b with 3, so the query drops bot-b: its HAVING tests the wrong count. With no WHERE, counting every reply in HAVING and the low ones with count(*) FILTER (WHERE rating <= 2) returns bot-a 3 and bot-b 1. Run on PostgreSQL 16.13 on 30 September 2026.

- (b) Reads HAVING as judging all of each model's replies; it runs after WHERE, so it sees only the low ratings, and bot-b's one fails the test.
- (c) Counts every reply, as if WHERE had never run; count(*) counts the rows that survive WHERE.
- (d) Ignores HAVING; bot-b and bot-c each have one low rating, and HAVING keeps only groups of three or more.

**In the interview.** WHERE keeps or drops single rows before any group exists; HAVING keeps or drops whole groups after the aggregate is computed, so a HAVING that follows a WHERE counts only the rows WHERE kept.

### Q33, key c

**Why it holds.** For c1, NOT IN asks c1 <> 'c2' AND c1 <> 'c4' AND c1 <> NULL; the last comparison is unknown, so the whole condition is unknown and WHERE drops the row. Every conversation fails the same way, so the count is 0 and the review reads a working assistant as useless. NOT EXISTS, or a LEFT JOIN kept where the handoff key IS NULL, returns 2. Run on PostgreSQL 16.13 on 30 September 2026.

- (a) The answer NOT EXISTS gives; NOT IN against a list that holds a NULL can never be true.
- (b) The NULL sits in the subquery's list, never in the outer table, so it cannot add a conversation.
- (d) Postgres raises nothing; the comparison with NULL is unknown and the rows are dropped without a word, so the review gets a figure, and the wrong one.

**In the interview.** Rows with no match are an anti-join, which I write as NOT EXISTS or as a LEFT JOIN kept where the right key IS NULL, never as NOT IN against a column that can hold a NULL.

### Q34, key a

**Why it holds.** With an ORDER BY and no frame, the window runs from the first row to the current row and its peers, the rows that tie on the ORDER BY. Calls 2 and 3 share 22 September, so both read the day's closing figure, 1200, and neither shows its own step. Adding call_id to the window's ORDER BY gives each call its own step. Run on PostgreSQL 16.13 on 30 September 2026.

- (b) The one-step-per-row reading, which needs a unique ORDER BY such as day then call_id; with the date alone the two calls are peers.
- (c) The whole-table total on every row, which is what sum(tokens) OVER () gives with no ORDER BY; with an ORDER BY, the frame stops at the current row and its peers.
- (d) Assumes the database breaks the tie with call 3 first; peers are never split, they share one figure.

**In the interview.** A running total is deterministic only when its ORDER BY is unique; rows that tie are peers and share one cumulative figure, so I add a tiebreaker such as the id.

### Q35, key d

**Why it holds.** A distinct count does not add across days: U1 used the assistant on four days, so U1 is in four daily counts and once in the week's. The week's figure is its own COUNT(DISTINCT user_id) over the week's rows, 6, never the sum of the days, 16. On Kalpa's book, 244 buyers in April to June and 227 in July to September are 301 customers across both quarters, never 471.

- (a) The seven daily counts added up; each day is distinct within the day, and across days the same users repeat, so the sum counts them again.
- (b) The average of the daily counts answers how many on a typical day, a different question from the week's reach.
- (c) The busiest day's count answers how much the assistant must handle at once; the ask was the week's active users.

**In the interview.** COUNT(DISTINCT ...) does not add across groups; a period's total needs its own distinct count over the whole period.


## Items by tag, level, day and part, for the tally

- [S] (8): Q2, Q4, Q9, Q12, Q14, Q21, Q31, Q32
- [F] (16): Q1, Q3, Q7, Q15, Q17, Q18, Q19, Q23, Q24, Q25, Q27, Q29, Q30, Q33, Q34, Q35
- [SV] (0): none
- [D] (11): Q5, Q6, Q8, Q10, Q11, Q13, Q16, Q20, Q22, Q26, Q28
- Easy (2): Q3, Q4
- Medium (12): Q2, Q5, Q13, Q14, Q17, Q18, Q19, Q23, Q24, Q25, Q26, Q35
- Hard (21): Q1, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q15, Q16, Q20, Q21, Q22, Q27, Q28, Q29, Q30, Q31, Q32, Q33, Q34
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

- Q1 (Applied maths, Hard, [F]): Anand's analyst fills the missing leaf with SELECT quarter, count(*) / count(DISTINCT customer_id) FROM rp_orders GROUP BY quarter, where rp_orders holds the Retail-Plus orders above. What does the query print for each quarter, what are the true figures, and how did orders per member change from the first quarter to the second? Show the working.
- Q5 (One correct option, Medium, [D]): On Monday afternoon the head of Retail-Plus asks the analyst for a chart of orders per member, week by week across both quarters, to see how the figure moved before anyone decides what to report. With Anand's rule in mind, where should that work happen?
- Q6 (One correct option, Hard, [D]): In 2016 Facebook told advertisers that it had defined the average duration of video viewed as the total time spent watching a video divided by the number of people who played it, and had calculated it by dividing by only the people who watched for three seconds or more (TechCrunch, 2016). The query above rebuilds both on five illustrative viewers. What does it return, and by how much does the calculated average overstate the defined one?
- Q7 (Scenario set, Hard, [F]): Before the report goes to Anand, the analyst sizes the join by hand. What will the query above return?
- Q8 (Order the steps, Hard, [D]): Five of these six steps make Anand's collected-revenue report, and one would spoil it. Leave that step out, and write the other five in the order they must run.
- Q9 (One correct option, Hard, [S]): Anand wants every order of the quarter beside what was collected on it within the quarter, so the analyst adds a date filter on the payments. Before the report goes to him, the analyst runs the query above to count its rows and their booked value. What does it return?
- Q10 (One correct option, Hard, [D]): It is the end of the reporting day, and Anand expects the report tonight. In each channel the gap, booked less collected, should equal the unpaid orders' booked value. What do you send?
- Q11 (More than one correct, Hard, [D]): In October 2020 Public Health England found that 15,841 positive COVID-19 cases from 25 September to 2 October had been left out of the daily figures, because some files had exceeded the maximum size the load could take (GOV.UK, 2020). The labs' CSV files had been converted to the older .xls format, and records past its limit were "simply left off and not counted when imported" (The Register, 2020). Which of these checks, run on every file, would have stopped Lab B's file on the day in the table? Mark every correct option.
- Q12 (Scenario set, Hard, [S]): The analyst computes RANK(), DENSE_RANK() and ROW_NUMBER() over the quarter's revenue, highest first, and keeps the members numbered 50 or better under each. How many members does each keep?
- Q13 (Scenario set, Medium, [D]): Which list follows the rule the head of Retail-Plus set?
- Q15 (One correct option, Hard, [F]): The falling flag reads member_month, one row per member per month with an order. It takes prev1 = LAG(spend, 1) and prev2 = LAG(spend, 2), each partitioned by member and ordered by month, and flags a member whose September spend is below prev1 while prev1 is below prev2. Marketing will call every member the flag names and say that their spend fell in both August and September. How many calls does Marketing make, and how many of them say something untrue?
- Q16 (One correct option, Hard, [D]): Meera's chief of staff wants one line about the plan for Monday's front page, and the figures above are all there is. Which line do they support?
- Q17 (Scenario set, Medium, [F]): How many rows does the merged table hold?
- Q18 (Scenario set, Medium, [F]): The analyst tells Marketing: "The pivot's grand total will equal the book's Rs 19,84,00,000." True or false, and why?
- Q19 (Scenario set, Medium, [F]): Which of these, added to Monday's refresh, would have stopped the run before the pivot was built? Mark every correct option.
- Q20 (Scenario set, Hard, [D]): Marketing's rule is one exposure per customer, the first by date. Which step applies it, so that the table sent to Excel has one row per customer carrying each customer's first exposure?
- Q21 (One correct option, Hard, [S]): The head of Retail-Plus wants one row per member and one column per month, to read who is drifting, and a long copy of the same view for a trend chart. What does the code above print?
- Q22 (One correct option, Hard, [D]): Gene symbols are the short names genes go by in papers and databases, and before 2020 two of them were SEPT2 and MARCH1. Ziemann and colleagues found that Excel's default settings turned such symbols into dates, SEPT2 into 2-Sep and MARCH1 into 1-Mar, and that about a fifth of genomics papers with Excel gene lists carried such errors (Genome Biology, 2016). In 2020 the body that names human genes renamed the genes Excel turned into dates, so that MARCH1 became MARCHF1 and SEPT1 became SEPTIN1 (Nature Genetics, 2020). The code above merges a lab's list onto a reference table from before the renaming. What does it print, and what should the analyst do?
- Q23 (Match the following, Medium, [F]): Find any member by member code, and print a plain message for an unknown code
- Q24 (Match the following, Medium, [F]): A figure under the protect list that adds only the members a filter to Mumbai leaves on screen
- Q25 (Match the following, Medium, [F]): Revenue by segment from Friday's export, in which an invoice paid in two instalments appears twice
- Q26 (Match the following, Medium, [D]): Let a director try Rs 5,00,000 for Retail-Plus in July to September, with the warehouse's figures untouched
- Q27 (Applied maths, Hard, [F]): In 2013 Herndon, Ash and Pollin rebuilt an influential 2010 paper by Reinhart and Rogoff from the authors' own working spreadsheet. They reported that a coding error "entirely excludes five countries, Australia, Austria, Belgium, Canada, and Denmark, from the analysis", because the averages covered lines 30 to 44 of the sheet instead of lines 30 to 49 (PERI working paper 322, 2013). The sheet above makes the same kind of error. What does B8 return, what should it return, and what does the error do to the reading of growth? Show the working.
- Q28 (One correct option, Hard, [D]): JPMorgan's task force on the 2012 losses in its Chief Investment Office reported that a value-at-risk model, an estimate of how much a trading book can lose on a bad day, ran through Excel spreadsheets filled by copying and pasting, and that one step divided a change in rates by the sum of the old and new rates where the modeller meant their average (JPMorgan Chase, 2013). Work out column D for the three rows and the change the modeller meant. What does the sheet do to the model's picture of risk?
- Q29 (Applied maths, Hard, [F]): In 2017 Uber said it had been taking its commission from New York City drivers on the gross fare, before sales tax and other fees were deducted, where it should have used the fare after them, and that it would repay affected drivers about 900 dollars each on average (CBS News, 2017). The commission rate on these trips is 25 percent. How much commission did the three trips overcharge the driver, and what share of the commission charged is that? Show the working.
- Q30 (One correct option, Hard, [F]): The team scores a model that sorts support tickets into refund, late and other against labels from an annotation vendor, and ships a model only if it scores 0.5 or better. The vendor re-sent a batch, so two tickets carry their label twice. What does the code above print?
- Q31 (One correct option, Hard, [S]): The leaderboard must show one row per model, its latest run and that run's accuracy, and must show the same row every morning. Two of bot-b's runs finished on 9 September. Which query does that?
- Q32 (One correct option, Hard, [S]): Customers rate each reply from 1 to 5. The team lead asks for every model with at least three replies this week, beside how many of its replies were rated 2 or below. What does the query above return?
- Q33 (One correct option, Hard, [F]): The weekly review reads how many conversations the assistant resolved without a person. This week the handoff log gained a row whose conversation_id is NULL. What does the query above return, and what will the review conclude?
- Q34 (One correct option, Hard, [F]): The model's bill is charged per token, so the finance partner wants tokens used so far, call by call, to watch the bill build up. What does tokens_so_far read for calls 1 to 4?
- Q35 (One correct option, Medium, [F]): The product manager wants the week's active users for the deck. Which number goes on the slide?

## Bank items folded into deeper items

Each of these tracker items is not printed, because a deeper item on the paper tests the same concept. Accept a fold by recording it in the tracker; reject it by deleting it from `folded` in the week's source file.

- Bank 1 (Fill in the blank, Easy, Mon), folded into Q32: The item predicts a query's rows through WHERE, GROUP BY and HAVING in that order, so the clause that filters groups after they form is tested by use.
- Bank 4 (Fill in the blank, Easy, Tue), folded into Q7: Sizing the LEFT JOIN by hand requires knowing that every order stays, with NULLs where no payment matched.
- Bank 5 (Fill in the blank, Medium, Tue), folded into Q33: The anti-join is tested where it breaks, NOT IN against a list that holds a NULL, and the reason names LEFT JOIN with IS NULL as the fix.
- Bank 6 (Fill in the blank, Medium, Wed), folded into Q15: The option of three calls rests on LAG returning NULL for a member with a missing month, and the reason says LAG returns NULL only on a member's first rows.
- Bank 7 (Fill in the blank, Easy, Wed), folded into Q14: Bank 27's key is a rank computed within PARTITION BY segment, so the clause that restarts a window for each segment is the item's answer.
- Bank 8 (Fill in the blank, Medium, Thu), folded into Q19: The guard the item keys is validate='one_to_one', and its reason names the MergeError it raises.
- Bank 9 (Fill in the blank, Easy, Thu), folded into Q21: The code melts the wide view back to one row per member and month, and predicting its row count needs the rule that melt lengthens.
- Bank 10 (True or false, Easy, Mon), folded into Q2: Ordering all six clauses tests where SELECT sits against WHERE.
- Bank 11 (True or false, Medium, Mon), folded into Q32: The item's reason says why the group filter sits in HAVING and never in WHERE, and its wrong option b is the reading in which HAVING sees every reply.
- Bank 12 (True or false, Easy, Tue), folded into Q9: The WHERE on the payments table turns the LEFT JOIN into an INNER one and drops the unpaid order without a word, which is the statement bank 12 tested.
- Bank 13 (True or false, Medium, Tue), folded into Q7: The item sizes the fan-out in rows before any rupee is summed, the mechanism by which a join inflates a SUM while every row looks right.
- Bank 14 (True or false, Hard, Wed), folded into Q12: The item's two ties make RANK and DENSE_RANK part company, the only case in which they differ.
- Bank 15 (True or false, Medium, Wed), folded into Q14: Bank 27's key filters the rank in an outer query, which is the reason a window cannot sit in WHERE.
- Bank 16 (True or false, Easy, Thu), folded into Q21: The pivot groups the orders by member and month and returns one cell per group, and predicting that cell is predicting what groupby returns.
- Bank 17 (True or false, Easy, Fri), folded into Q18: The item asks whether a pivot on a table with repeated rows reports the true total, on the week's own numbers.
- Bank 18 (One correct option, Easy, Mon), folded into Q2: Ordering all six clauses tests which one the database runs first.
- Bank 19 (One correct option, Medium, Mon), folded into Q2: A syntax error is never an item (CLAUDE.md); the rule behind this one, that SELECT runs after GROUP BY and so sees only grouped columns and aggregates, is the order Q2 tests.
- Bank 20 (One correct option, Medium, Mon), folded into Q5: The item's reason gives why the reported number lives in the warehouse, rerunning unchanged on the source and read line by line, and the item asks where the work that reports nothing belongs.
- Bank 21 (One correct option, Easy, Tue), folded into Q7: The item's third count, count(p.payment_id), is the matched rows an INNER JOIN would keep.
- Bank 22 (One correct option, Medium, Tue), folded into Q7: The item sizes exactly how a LEFT JOIN from orders to payments grows past the orders it started from.
- Bank 23 (One correct option, Medium, Tue), folded into Q8: The step the item leaves out drops every order with two payment rows, which is what HAVING count(*) > 1 by order finds; the reason gives the 216 orders it lists against the 28 repeats that grouping by order and instalment lists.
- Bank 24 (One correct option, Hard, Tue), folded into Q7: The first check after a doubled total is the row count before and after the join, which this item asks for in numbers.
- Bank 25 (One correct option, Easy, Wed), folded into Q12: The item asks what RANK does after a tie, on the week's real boundary.
- Bank 26 (One correct option, Medium, Wed), folded into Q12: The item asks what DENSE_RANK does after a tie, and its second tie shows the missing gap changing the count.
- Bank 28 (One correct option, Hard, Wed), folded into Q34: The item predicts a running total whose ORDER BY ties, the cause bank 28 names, and its reason gives the tiebreaker.
- Bank 29 (One correct option, Medium, Thu), folded into Q21: The item's reason walks pivot_table as split, apply and combine, with the default mean as the apply step.
- Bank 30 (One correct option, Medium, Thu), folded into Q17: The item sizes a merge that grew because keys repeat on the right, on the week's own feed.
- Bank 31 (One correct option, Medium, Fri), folded into Q23: The match row asks for the lookup that says so when a code is missing, with VLOOKUP's default approximate match as the spare beside it.
- Bank 32 (One correct option, Medium, Fri), folded into Q26: The row is the one job bank 32 gives Excel, a director changing an input and watching the number recalculate, with the technique that does it.
- Bank 33 (More than one correct, Medium, Mon), folded into Q32: Predicting the rows needs every statement bank 33 makes about WHERE, HAVING and COUNT(*).
- Bank 34 (More than one correct, Medium, Tue), folded into Q10: The item's table is the validation bank 34 asks for, the gap against the unpaid list channel by channel, and the item goes on to what to do when one channel fails.
- Bank 35 (More than one correct, Hard, Tue), folded into Q7: Option d counts the payments with no order as if they had joined, and its reason says only a FULL OUTER JOIN brings in one side's orphans beside the other's.
- Bank 36 (More than one correct, Hard, Wed), folded into Q14: Top three per segment is one of the questions only a window answers, and the lag and running-total items test the other two.
- Bank 37 (More than one correct, Hard, Wed), folded into Q13: The item applies bank 37's claims about RANK and ROW_NUMBER to the head of Retail-Plus's rule on the week's real tie.
- Bank 38 (More than one correct, Medium, Thu), folded into Q19: The item tests what merge does to rows, what validate= does and why the row count is still worth checking.
- Bank 39 (More than one correct, Medium, Fri), folded into Q16: The front-page line must carry its period and its comparison; every option states both, and only the key's match the figures.
- Bank 40 (Scenario set, Medium, Tue), folded into Q7: The same LEFT JOIN count on the week's own quarter, with instalments as well as repeats.
- Bank 41 (Scenario set, Medium, Tue), folded into Q7: The matched rows are the INNER JOIN's count, the item's third number.
- Bank 42 (Scenario set, Medium, Tue), folded into Q33: The unpaid list is the anti-join; the item tests the pattern that fails and names the ones that work.
- Bank 43 (Scenario set, Medium, Tue), folded into Q8: Dropping the repeats before the sum is the item's first step, because a plain SUM counts each repeat twice.
- Bank 44 (Scenario set, Medium, Wed), folded into Q12: RANK after a tie, on the week's boundary.
- Bank 45 (Scenario set, Medium, Wed), folded into Q12: DENSE_RANK after two ties, on the week's boundary.
- Bank 46 (Scenario set, Hard, Wed), folded into Q12: The item counts what a DENSE_RANK cut keeps.
- Bank 47 (Scenario set, Hard, Wed), folded into Q13: ROW_NUMBER with a member-id tiebreaker is option b, and its reason names the cost, a member who spent as much as the fiftieth dropped by an id nobody chose.
- Bank 48 (Scenario set, Medium, Thu), folded into Q17: The same merge count on the week's own feed.
- Bank 49 (Scenario set, Medium, Thu), folded into Q19: validate='one_to_one' is one of the two guards the item keys.
- Bank 50 (Scenario set, Medium, Thu), folded into Q18: The same claim about the pivot's total, on the week's numbers.
- Bank 51 (Scenario set, Hard, Thu), folded into Q20: Bank 51's fix, de-duplicating the exposure feed on a stated rule, is the item, which asks which step applies the rule of one exposure per customer, the first by date.
- Bank 52 (Applied maths, Easy, Mon), folded into Q32: Predicting the query needs the groups GROUP BY forms from the rows WHERE keeps, one per model with a low rating, before HAVING filters them.
- Bank 53 (Applied maths, Medium, Tue), folded into Q8: The Rs 20,750 the repeats add to a plain SUM is why the item's first step comes first.
- Bank 54 (Applied maths, Hard, Wed), folded into Q12: RANK ships 51 and ROW_NUMBER 50 on the week's tie at fiftieth.
- Bank 55 (Applied maths, Medium, Wed), folded into Q15: The item runs the falling flag with LAG on four members, two of them with a missing month.
- Bank 56 (Applied maths, Medium, Thu), folded into Q1: Orders per member is the same ratio of two counts, and the trap is the same integer division.
- Bank 58 (Order the steps, Medium, Fri), folded into Q5: The item places a piece of work among the warehouse, a notebook and a workbook, and its reason gives the one direction a number travels, from the warehouse through pandas to Excel.

## Stems and situations reworded on the bank, waiting for the tracker

These items print with a stem or a situation the tracker does not carry, each for the reason given; the key is the tracker's. Accept one by copying the wording into the tracker; reject it by deleting it from `data/programme/paper_edits.yaml`.

- Bank 2, Q3, stem (proposed): The paper answers this item from a word bank of five nouns shared with item 3, and the tracker's blank takes a verb, so only two of the five words fit it and the grammar halves the bank. The new stem's blank takes a noun, so every word fits the sentence and only the key fits its sense; the key is the tracker's.
- Bank 27, Q14, stem (proposed): The tracker's stem asks for top three per segment with no business context. The new stem opens on Marketing's first protect list, sorted over every customer, and the numbers it produced on Wednesday, so the item asks why that list fails before it asks for the approach; the key is the tracker's. It names the quarter by its months, since the paper numbers its items Q1 to Q35, and calls only Retail-Plus customers members, since membership is that tier's name.

## Option edits laid on the bank, waiting for the tracker

These options differ from the tracker's wording or order, each for the reason given beside it. The correct options are the tracker's; where the options are relabelled, the key's letters move with them. Accept an edit by copying it into the tracker; reject it by deleting it from `data/programme/paper_edits.yaml`.

- Bank 19, folded into Q2, option b (accepted): The key was the longest option.
- Bank 22, folded into Q7, option c (accepted): The key was the longest option; the new distractor is the fan-out misread in reverse.
- Bank 23, folded into Q8, option b, d (accepted): The key was the longest option; the distractor is now the full query with the aggregate in WHERE. Option b then ran 38 characters against 73, so it now sorts its distinct list too, and the options run 47 to 73.
- Bank 27, Q14, option a, b, c, d (proposed): The key was the only option without a "because" or a "since", and the only item on the paper whose options end in full stops, so its form alone gave it away. Each option now names an approach and says in the same form what it does, and none ends in a full stop; the options run 74 to 78 characters, the key is not the longest, and the same option stays correct.
- Bank 29, folded into Q21, option a (accepted): The key was the longest option.
- Bank 32, folded into Q26, option c (accepted): The key was the longest option.
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

- Stretch 1: The payment's date decides collected's week, where the order's date decides booked's, so an order paid in two instalments adds to collected in two different weeks. A weekly gap between booked and collected is then timing as well as unpaid orders, and the report says so beside the weekly figures.
- Stretch 2: The member's revenue divided by sum(revenue) OVER (), the tier's total on every row, taken in numeric and rounded on purpose; the check is that the shares add to 1, and that the total on every row equals the tier's revenue from the Monday suite.
- Stretch 3: Excel turned some gene symbols into dates in about a fifth of papers with Excel gene lists, so the naming body renamed the genes it could not protect any other way, fixing the error at the source every reader shares. I would still count, after every merge, how many keys found a match, because a key changed on its way in never raises an error.
- Stretch 4: Rs 19.84 crore is real and covers two quarters, so a director reads it as a quarter that doubled. The page reads: July to September, Rs 9.84 crore, down 1.6 percent on April to June's Rs 10.00 crore.

# Week 2 recap paper: key

TRAINER. Rendered from the tracker's item bank and the week's source file by `scripts/build_saturday_paper.py`. Change an item in the tracker, an option in `data/programme/paper_edits.yaml` or anything in `content/W02/SAT/internal/C2_W02_SAT_paper_source_INTERNAL.yaml`, and rebuild; never edit this file by hand.

Saturday 17 October 2026. A 120-minute paper holding 55 items at 120 minutes by the blueprint's pace: 8 easy, 34 medium and 13 hard. 3 of them are new and not yet in the tracker.

## Marking

1. Papers are swapped, so nobody checks their own.
2. The Academic TA reads the key out part by part, and the marker writes a tick or a cross beside each item.
3. An item is right when its answer matches the key: every correct letter and no other on a more-than-one item, the number on an applied maths item (the working belongs to the discussion), and the whole sequence on an ordering item. The programme has set no partial-credit rule, so this key uses none.
4. The marker writes the count of ticks as Items right on the front, out of 55, and hands the paper back.
5. The TA collects the papers and tallies the misses by tag, using the table below; that tally is Monday's remediation read. It is never a ranking and never read out by name.
6. The TA enters every paper in `C2_W02_SAT_item_analysis_TRAINER.xlsx` beside this key, by seat and never by name: 1 for a tick, 0 for a cross and a blank for an item left empty. The workbook orders the discussion from the most-missed item, flags any item to check, and gives each tag's rate for the room and for each seat.

## The blueprint

| Part | What it shows | Items | Minutes | Easy | Medium | Hard |
|---|---|---|---|---|---|---|
| 1. The week's rules, cold | whether the week's definitions and rules are there without a notebook open | Q1 to Q11 (11) | 11 | 4 | 6 | 1 |
| 2. Asking the warehouse | whether you can write a grouped query in the order the database runs it | Q12 to Q16 (5) | 13 | 2 | 3 | 0 |
| 3. Joins that keep their rows | whether you read the row count before and after a join and catch a join that inflates a sum | Q17 to Q27 (11) | 27 | 1 | 8 | 2 |
| 4. Windows: rank, lag and running totals | whether you can rank within a segment, compare a month with the one before it and keep a running total | Q28 to Q39 (12) | 31 | 1 | 5 | 6 |
| 5. pandas and the last mile to Excel | whether you can merge, group and reshape without losing or doubling rows, and choose the tool for each job | Q40 to Q51 (12) | 29.5 | 0 | 11 | 1 |
| 6. Read the code, read the data | whether you catch a wrong number in a query or a few lines of pandas before it reaches a decision | Q52 to Q55 (4) | 8.5 | 0 | 1 | 3 |
| Total | | 55 | 120 | 8 | 34 | 13 |

## What guessing alone would score

A learner who guessed every item blind would average 11.4 of 55, since a written answer cannot be guessed from a list, and fewer than one guesser in twenty would reach 17. A score of 16 or below is therefore within reach of guessing alone, and the tally reads such a paper as a conversation to have on Monday, never as a result.

## Reading the items after marking

The workbook flags an item to check when fewer than one learner in five got it right, or when the bottom third of the room got it right more often than the top third. Both are this programme's own working rule for a room of 35. A flagged item is discussed as usual; the TA also sends it, with the room's rate, to the tracker's owner, because the fault may sit in the item rather than in the learners.

## The key

| Q | Key | Type | Part | Level | Tag | Roles | Day | Min | Source | Interview anchor |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NULL | Fill in the blank | 1 | Medium | [F] | BA, DS | Tue | 1 | bank 5 | How do you find orders with no payment? |
| 2 | NULL | Fill in the blank | 1 | Medium | [S] | BA, DS | Wed | 1 | bank 6 | How would you find customers whose spend fell two months in a row? |
| 3 | MergeError | Fill in the blank | 1 | Medium | [F] | BA, DS | Thu | 1 | bank 8 | Which merge argument raises on duplicate keys, and which error? |
| 4 | False | True or false | 1 | Easy | [S] | BA, DS | Mon | 1 | bank 10 | Explain the logical order in which a SQL query executes. |
| 5 | False | True or false | 1 | Medium | [F] | BA, DS | Mon | 1 | bank 11 | WHERE against HAVING, one sentence each. |
| 6 | True | True or false | 1 | Easy | [S] | BA, DS | Tue | 1 | bank 12 | INNER against LEFT join: what does each drop or keep? |
| 7 | True | True or false | 1 | Medium | [S] | BA, DS, FDE | Tue | 1 | bank 13 | Revenue doubled after a join and every row looks fine; where do you look? |
| 8 | True | True or false | 1 | Hard | [S] | BA, DS | Wed | 1 | bank 14 | RANK, DENSE_RANK and ROW_NUMBER on a tie. |
| 9 | False | True or false | 1 | Medium | [F] | BA, DS | Wed | 1 | bank 15 | Why can a window function not sit inside WHERE, and what do you do instead? |
| 10 | True | True or false | 1 | Easy | [F] | BA, DS | Thu | 1 | bank 16 | groupby in the split-apply-combine sentence. |
| 11 | False | True or false | 1 | Easy | [F] | BA | Fri | 1 | bank 17 | Your pivot shows a different total from the warehouse; where do you look first? |
| 12 | b | One correct option | 2 | Easy | [S] | BA, DS | Mon | 2 | bank 18 | Explain the logical order in which a SQL query executes. |
| 13 | d | One correct option | 2 | Medium | [F] | BA, FDE | Mon | 2 | bank 20 | Why would you compute a KPI in the warehouse rather than in a notebook? |
| 14 | a, b, c | More than one correct | 2 | Medium | [S] | BA, DS | Mon | 2.5 | bank 33 | WHERE against HAVING, one sentence each. |
| 15 | 8 | Applied maths | 2 | Easy | [S] | BA, DS | Mon | 4 | bank 52 | Explain the logical order in which a SQL query executes. |
| 16 | c, b, e, f, a, d | Order the steps | 2 | Medium | [S] | BA, DS | Mon | 2.5 | bank 57 | Explain the logical order in which a SQL query executes. |
| 17 | c | One correct option | 3 | Easy | [S] | BA, DS | Tue | 2 | bank 21 | INNER against LEFT join: what does each drop or keep? |
| 18 | d | One correct option | 3 | Medium | [S] | BA, DS | Tue | 2 | bank 22 | Your join grew the row count; name the cause and the check. |
| 19 | a | One correct option | 3 | Medium | [F] | BA, DS | Tue | 2 | bank 23 | Revenue doubled after a join and every row looks fine; where do you look? |
| 20 | d | One correct option | 3 | Hard | [D] | BA, DS, FDE | Tue | 2 | bank 24 | Revenue doubled after a join and every row looks fine; where do you look? |
| 21 | a, b, c | More than one correct | 3 | Medium | [S] | BA, DS, FDE | Tue | 2.5 | bank 34 | Your join grew the row count; name the cause and the check. |
| 22 | a, b | More than one correct | 3 | Hard | [F] | BA, DS | Tue | 2.5 | bank 35 | INNER against LEFT join: what does each drop or keep? |
| 23 | 1,050 | Scenario set | 3 | Medium | [S] | BA, DS | Tue | 2.5 | bank 40 | Your join grew the row count; name the cause and the check. |
| 24 | 1,020 | Scenario set | 3 | Medium | [S] | BA, DS | Tue | 2.5 | bank 41 | Your join grew the row count; name the cause and the check. |
| 25 | a | Scenario set | 3 | Medium | [F] | BA, DS | Tue | 2.5 | bank 42 | Your join grew the row count; name the cause and the check. |
| 26 | True | Scenario set | 3 | Medium | [F] | BA, DS | Tue | 2.5 | bank 43 | Your join grew the row count; name the cause and the check. |
| 27 | Rs 21 lakh, which overstates collections by Rs 1 lakh. | Applied maths | 3 | Medium | [S] | BA, DS | Tue | 4 | bank 53 | Revenue doubled after a join and every row looks fine; where do you look? |
| 28 | c | One correct option | 4 | Easy | [S] | BA, DS | Wed | 2 | bank 25 | RANK, DENSE_RANK and ROW_NUMBER on a tie. |
| 29 | b | One correct option | 4 | Medium | [S] | BA, DS | Wed | 2 | bank 26 | RANK, DENSE_RANK and ROW_NUMBER on a tie. |
| 30 | b | One correct option | 4 | Medium | [S] | BA, DS | Wed | 2 | bank 27 | Top-3 per group: GROUP BY or a window, and why? |
| 31 | a | One correct option | 4 | Hard | [F] | BA, DS | Wed | 2 | bank 28 | The business says 'ties rank the same'; which function, and how many rows might the top-N report ship? |
| 32 | a, c, d | More than one correct | 4 | Hard | [S] | BA, DS | Wed | 2.5 | bank 36 | Top-3 per group: GROUP BY or a window, and why? |
| 33 | a, b, c | More than one correct | 4 | Hard | [D] | BA, DS | Wed | 2.5 | bank 37 | The business says 'ties rank the same'; which function, and how many rows might the top-N report ship? |
| 34 | 4 | Scenario set | 4 | Medium | [S] | BA, DS | Wed | 2.5 | bank 44 | The business says 'ties rank the same'; which function, and how many rows might the top-N report ship? |
| 35 | 4 | Scenario set | 4 | Medium | [S] | BA, DS | Wed | 2.5 | bank 45 | The business says 'ties rank the same'; which function, and how many rows might the top-N report ship? |
| 36 | c | Scenario set | 4 | Hard | [F] | BA, DS | Wed | 2.5 | bank 46 | The business says 'ties rank the same'; which function, and how many rows might the top-N report ship? |
| 37 | c | Scenario set | 4 | Hard | [D] | BA, DS | Wed | 2.5 | bank 47 | The business says 'ties rank the same'; which function, and how many rows might the top-N report ship? |
| 38 | 51 under RANK(); 50 under ROW_NUMBER(). | Applied maths | 4 | Hard | [D] | BA, DS | Wed | 4 | bank 54 | The business says 'ties rank the same'; which function, and how many rows might the top-N report ship? |
| 39 | A fall of Rs 800, then a fall of Rs 300; the flag fires. | Applied maths | 4 | Medium | [F] | BA, DS | Wed | 4 | bank 55 | How would you find customers whose spend fell two months in a row? |
| 40 | c | One correct option | 5 | Medium | [S] | BA, DS | Thu | 2 | bank 29 | groupby in the split-apply-combine sentence. |
| 41 | b | One correct option | 5 | Medium | [F] | BA, DS | Thu | 2 | bank 30 | Which merge argument raises on duplicate keys, and which error? |
| 42 | d | One correct option | 5 | Medium | [S] | BA | Fri | 2 | bank 31 | SQL, pandas or Excel: how do you choose? |
| 43 | a | One correct option | 5 | Medium | [S] | BA, FDE | Fri | 2 | bank 32 | SQL, pandas or Excel: how do you choose? |
| 44 | a, b, d | More than one correct | 5 | Medium | [F] | BA, DS | Thu | 2.5 | bank 38 | Which merge argument raises on duplicate keys, and which error? |
| 45 | a, b, c | More than one correct | 5 | Medium | [S] | BA, FDE | Fri | 2.5 | bank 39 | How do you present one number so it is not misread? |
| 46 | 1,060 | Scenario set | 5 | Medium | [F] | BA, DS, FDE | Thu | 2.5 | bank 48 | Your pivot shows a different total from the warehouse; where do you look first? |
| 47 | d | Scenario set | 5 | Medium | [F] | BA, DS, FDE | Thu | 2.5 | bank 49 | Your pivot shows a different total from the warehouse; where do you look first? |
| 48 | True | Scenario set | 5 | Medium | [S] | BA, DS, FDE | Thu | 2.5 | bank 50 | Your pivot shows a different total from the warehouse; where do you look first? |
| 49 | b | Scenario set | 5 | Hard | [D] | BA, DS, FDE | Thu | 2.5 | bank 51 | Your pivot shows a different total from the warehouse; where do you look first? |
| 50 | 400 rows; 2.5 orders per customer. | Applied maths | 5 | Medium | [F] | BA, DS | Thu | 4 | bank 56 | groupby in the split-apply-combine sentence. |
| 51 | b, c, a | Order the steps | 5 | Medium | [D] | BA, FDE | Fri | 2.5 | bank 58 | SQL, pandas or Excel: how do you choose? |
| 52 | c | One correct option | 6 | Hard | [D] | BA, DS | Mon | 2 | new | A stakeholder's analyst must audit your query; what changes in how you write it, and what would you refuse to compute in a notebook? |
| 53 | b | Scenario set | 6 | Hard | [S] | BA, DS, FDE | Tue | 2.5 | new | INNER against LEFT join: what does each drop or keep? |
| 54 | d | One correct option | 6 | Hard | [S] | BA, DS | Thu | 2 | new | groupby in the split-apply-combine sentence. |
| 55 | a | One correct option | 6 | Medium | [S] | BA, DS | Mon | 2 | bank 19 | Explain the logical order in which a SQL query executes. |

## Why each answer holds

### Q1, key NULL

**Why it holds.** After a LEFT JOIN an order with no payment carries NULL in every payment column, so the filter is IS NULL. Writing "= NULL" or "0" fails: nothing equals NULL, and a zero amount is a payment row.

**In the interview.** Left join orders to payments and keep the rows where the payment's key IS NULL; those are the orders nobody paid for.

### Q2, key NULL

**Why it holds.** The first month of a partition has no previous row, so LAG returns NULL unless a default is given. Answering 0 is the trap: a zero would read as a fall from zero to this month's spend.

**In the interview.** LAG gives NULL on each customer's first month, so the fall flag must treat NULL as "no comparison" and never as a fall.

### Q3, key MergeError

**Why it holds.** pandas raises MergeError with the text "Merge keys are not unique in right dataset; not a one-to-one merge", checked on pandas 3.0.6. KeyError and ValueError are the usual wrong guesses.

**In the interview.** validate='one_to_one' makes pandas raise MergeError on a repeated key, so the fan-out stops at the merge before any total is computed.

### Q4, key False

**Why it holds.** The logical order is FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY, so WHERE runs first and SELECT comes late. That is why a SELECT alias cannot be used in WHERE.

**In the interview.** SELECT is evaluated after WHERE, GROUP BY and HAVING, which is why its aliases work in ORDER BY and fail in WHERE.

### Q5, key False

**Why it holds.** WHERE runs before any group exists, so an aggregate has nothing to count there, and Postgres rejects it. The group filter belongs in HAVING.

**In the interview.** An aggregate cannot sit in WHERE because the groups do not exist yet; the filter moves to HAVING.

### Q6, key True

**Why it holds.** An INNER JOIN keeps only the orders that find a payment row, so the unpaid orders disappear without any warning or error.

**In the interview.** An inner join drops every order with no payment and says nothing, which is exactly the list Finance most needs.

### Q7, key True

**Why it holds.** When a key repeats on one side, each match becomes its own row. Every row is a real order paired with a real payment, so row-level checks pass while the SUM counts one order more than once.

**In the interview.** A one-to-many join multiplies rows that each look correct, so the check is on the counts and the total, never on the rows.

### Q8, key True

**Why it holds.** Without ties all three rank functions give 1, 2, 3 and so on. RANK and DENSE_RANK part only when two values tie, where RANK skips the next rank and DENSE_RANK does not.

**In the interview.** RANK and DENSE_RANK agree until a tie; then RANK leaves a gap and DENSE_RANK does not.

### Q9, key False

**Why it holds.** Window functions are computed after WHERE in the logical order, so WHERE cannot see them. The fix is to compute the rank in a CTE or subquery and filter it outside.

**In the interview.** A window runs after WHERE, so you compute it in a CTE and filter the rank in the outer query.

### Q10, key True

**Why it holds.** groupby with agg splits the rows by key, reduces each group, and combines one row per group. transform is the variant that keeps every original row.

**In the interview.** groupby then agg gives one row per group; transform gives the group's value on every original row.

### Q11, key False

**Why it holds.** A pivot sums whatever rows it is handed, so a duplicated row is summed twice. The pivot works correctly and the total is still wrong.

**In the interview.** A pivot is only as honest as its source; duplicated rows in the export become a higher total.

### Q12, key b

**Why it holds.** FROM runs first because every later clause needs the rows it produces.

- (a) SELECT is written first, which is why people guess it; it is evaluated near the end.
- (c) WHERE filters rows, so it needs FROM to have produced them already.
- (d) ORDER BY is the last clause evaluated, after SELECT.

**In the interview.** FROM runs first, then WHERE, GROUP BY, HAVING, SELECT and ORDER BY.

### Q13, key d

**Why it holds.** The warehouse query runs the same way against the source every Monday, and an auditor can read every line of it.

- (a) Hiding the data from Finance breaks the audit this choice exists for.
- (b) A notebook holds a quarter of orders easily; size is the wrong reason.
- (c) Speed on every task is false and beside the point; repeatability and audit decide it.

**In the interview.** A KPI Finance checks lives in the warehouse, because it reruns unchanged on the source and anyone can audit the query.

### Q14, key a, b, c

**Why it holds.** WHERE filters rows before grouping, HAVING filters groups after aggregation, and HAVING can compare COUNT(*) with a number, as in HAVING COUNT(*) > 1.

- (d) WHERE cannot compare COUNT(*) with anything: an aggregate in WHERE is an error, because WHERE runs before the groups exist.

**In the interview.** WHERE filters rows before the aggregate, HAVING filters groups after it, and only HAVING can use COUNT.

### Q15, key 8

**Why it holds.** Four segments times two quarters, with every combination present, gives eight groups. The common wrong answer is 6, which adds the segments to the quarters and fails because GROUP BY on two columns returns one row per pair of values, so the counts multiply.

**In the interview.** GROUP BY returns one row per combination that exists, so 4 by 2 gives 8.

### Q16, key c, b, e, f, a, d

**Why it holds.** The logical order is FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY. The common wrong answer is the order the clauses are typed, a, c, b, e, f, d, which puts SELECT first; the database cannot pick columns from rows it has not yet read, filtered and grouped.

**In the interview.** FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY, which is why aliases work only in ORDER BY.

### Q17, key c

**Why it holds.** INNER JOIN keeps only the rows that find a partner, so an order with no payment drops out.

- (a) LEFT JOIN also keeps the unpaid orders, with NULL payment columns.
- (b) FULL OUTER JOIN keeps unmatched rows from both sides, orders and payments.
- (d) CROSS JOIN pairs every order with every payment and has no matching condition.

**In the interview.** An inner join returns only matched orders; a left join returns every order.

### Q18, key d

**Why it holds.** A LEFT JOIN can only grow the row count when a left row matches more than one right row, so some orders have two or more payment rows.

- (a) An empty payments table would leave exactly 1,000 rows, each with NULLs.
- (b) Unpaid orders stay as one row each under a LEFT JOIN, so they cannot add rows.
- (c) This is the fan-out read in reverse: an unpaid order keeps its one row and adds none.

**In the interview.** A row count that rises after a join means a key repeats on the right side; count rows per key to find which.

### Q19, key a

**Why it holds.** GROUP BY order_id with HAVING COUNT(*) > 1 returns every order with more than one payment row.

- (b) DISTINCT lists every paid order once, and the ORDER BY only sorts that list, so the duplicates it was meant to find are hidden.
- (c) Sorting puts the duplicates next to each other and still returns every order.
- (d) An aggregate in WHERE is an error, because WHERE runs before any group exists.

**In the interview.** GROUP BY the order key and keep HAVING COUNT(*) > 1; that is the double-paid list.

### Q20, key d

**Why it holds.** Revenue that doubles while every row looks right is the fan-out signature, so the first check is the row count before and after the join, then payment rows per order.

- (a) A partial result would lower the total; this total went up.
- (b) Rounding moves a total by rupees, never by a factor of two.
- (c) An INNER JOIN fans out exactly as much and also drops the unpaid orders.

**In the interview.** Count rows before and after the join, then count payments per order; the doubling lives in the join.

### Q21, key a, b, c

**Why it holds.** The row count before and after, payments per order, and booked revenue before and after are the three checks that catch a fan-out.

- (d) Every order stays in a LEFT JOIN, so the channels match before and after it whether or not the join fanned out. A check that cannot fail proves nothing, which is how the doubled total passed a row-by-row reading on Tuesday.

**In the interview.** Before a joined number leaves, compare the row count and the total before and after the join, and count rows per key.

### Q22, key a, b

**Why it holds.** A FULL OUTER JOIN adds the rows with no partner on either side: orders with no payment and payments with no order.

- (c) An order with one payment matches, so an INNER JOIN returns it too.
- (d) An order with two payments matches twice and appears twice in an INNER JOIN as well.

**In the interview.** A full outer join keeps the unmatched rows from both sides, which is how orphan payments show up.

### Q23, key 1,050

**Why it holds.** 920 orders give one row each, 50 orders give two rows each and 30 unpaid orders keep one row with NULLs: 920 + 100 + 30 = 1,050. Checked in Postgres 16.13. The common wrong answer is 1,000, which fails because a left join keeps every order but writes one row per matching payment, so the 50 retried orders appear twice.

**In the interview.** A left join returns one row per match plus one per unmatched left row, so 1,050 here.

### Q24, key 1,020

**Why it holds.** The INNER JOIN drops the 30 unpaid orders: 920 + 100 = 1,020. The common wrong answer is 970, the count of orders with a payment, which fails because a join returns one row per matching pair and the 50 retried orders match two payment rows each.

**In the interview.** An inner join returns only the matches, 1,020, and the 30 unpaid orders vanish without a word.

### Q25, key a

**Why it holds.** A LEFT JOIN keeps unpaid orders with NULL payment columns, and IS NULL on the payment key keeps exactly those.

- (b) An INNER JOIN has already dropped the unpaid orders, so there is nothing left to find.
- (c) This lists the double-paid orders, a different list.
- (d) A RIGHT JOIN with IS NULL on the orders side is the anti-join from the other side: it lists the payments whose order is missing, as step A7 of Tuesday's round 3 did, and never an unpaid order.

**In the interview.** Left join, then keep the rows whose payment key IS NULL.

### Q26, key True

**Why it holds.** Each retry recorded the same payment a second time, so a plain SUM counts those 50 payments twice.

**In the interview.** Collected revenue is summed after the payments are de-duplicated on a stated rule; a raw SUM counts every retry.

### Q27, key Rs 21 lakh, which overstates collections by Rs 1 lakh.

**Why it holds.** Fifty payments of Rs 2,000 counted twice add Rs 1 lakh: Rs 20 lakh plus Rs 1 lakh is Rs 21 lakh. The common wrong answer is Rs 20 lakh, which fails because SUM adds rows, and each retried payment is a second row carrying the same amount.

**In the interview.** A plain SUM reports Rs 21 lakh, overstating collections by exactly the retried amount.

### Q28, key c

**Why it holds.** RANK gives the two 850s rank 2 and skips 3, so 700 gets rank 4. Checked in Postgres 16.13.

- (a) 1, 2, 3, 4 is ROW_NUMBER, which ignores the tie.
- (b) 1, 2, 2, 3 is DENSE_RANK, which leaves no gap.
- (d) 1, 1, 2, 3 ties the wrong pair: 900 and 850 are different values.

**In the interview.** RANK ties equal values and skips the ranks they used, so 1, 2, 2, 4.

### Q29, key b

**Why it holds.** DENSE_RANK gives the tied 850s rank 2 and continues at 3 without a gap.

- (a) 1, 2, 3, 4 is ROW_NUMBER.
- (c) 1, 2, 2, 4 is RANK, with the gap after the tie.
- (d) 1, 1, 2, 3 ties 900 with 850, which are unequal.

**In the interview.** DENSE_RANK ties equal values and carries on with the next integer, so 1, 2, 2, 3.

### Q30, key b

**Why it holds.** A rank computed within PARTITION BY segment keeps every member, and the outer query keeps the rows with rank three or less.

- (a) LIMIT applies once to the whole result, never per group, and GROUP BY has collapsed the members anyway.
- (c) One ORDER BY with LIMIT 3 returns the top three overall, which may all sit in one segment.
- (d) HAVING filters whole groups by an aggregate and cannot pick rows inside a group.

**In the interview.** Rank within PARTITION BY segment in a CTE, then keep rank three or less outside, with the tie rule named.

### Q31, key a

**Why it holds.** The claim needs a ROWS frame, such as ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW: tied rows are then added one at a time in an undefined order, so the running total at those rows can differ from run to run. Postgres's default frame with an ORDER BY is RANGE, which treats tied rows as peers and gives them one shared running total, so on the default the ties change only the order the rows print in. Checked in Postgres 16.13. Option a stays the only defensible cause, because b, c and d are false on any frame, and a tiebreaker column in the window's ORDER BY fixes it on both.

- (b) Postgres does not sample rows inside a window.
- (c) A cached result would repeat the same answer, never change it.
- (d) SUM over exact numeric values is exact; it does not drift.

**In the interview.** A running total that moves between runs has ties in its ORDER BY under a ROWS frame, since the default RANGE frame gives tied rows one shared total; add a tiebreaker so the order is defined.

### Q32, key a, c, d

**Why it holds.** A rank within a segment, a previous month beside this one, and a running total with every row kept all need a value computed across rows while each row stays.

- (b) A segment's total for the quarter is one aggregate per group, which GROUP BY answers alone.

**In the interview.** Use a window when the answer needs other rows while every row stays; use GROUP BY when one row per group is the answer.

### Q33, key a, b, c

**Why it holds.** ROW_NUMBER breaks ties arbitrarily, RANK gives tied members one rank, and a tie at fifty under RANK ships fifty-one rows.

- (d) ROW_NUMBER numbers every row once, so rank fifty or less returns exactly fifty rows.

**In the interview.** Ties ranked the same means RANK or DENSE_RANK, and the report must say it can ship more than fifty names.

### Q34, key 4

**Why it holds.** A 900, B and C tie at rank 2, so the next rank is 4 for D and E. Checked in Postgres 16.13. The common wrong answer is 3, which is D's rank under DENSE_RANK(); RANK() skips the ranks the tie used up.

**In the interview.** Under RANK the pair tied at second pushes the next member to fourth.

### Q35, key 4

**Why it holds.** Dense ranks run A 1, B and C 2, D and E 3, F 4. The common wrong answer is 6, which fails because 6 is F's rank under RANK() and its row number; DENSE_RANK() never skips a rank after a tie.

**In the interview.** DENSE_RANK never skips, so F is fourth.

### Q36, key c

**Why it holds.** Dense rank three or less is A, B, C, D and E, which is five members. Checked in Postgres 16.13.

- (a) Three assumes one member per rank, which ignores both ties.
- (b) Four counts one tie and forgets the other.
- (d) Six includes F, whose dense rank is 4.

**In the interview.** A top-three by DENSE_RANK returns every member at the top three values, five here.

### Q37, key c

**Why it holds.** Only ROW_NUMBER guarantees exactly four rows, and it splits the D and E tie arbitrarily unless a tiebreaker is named.

- (a) RANK four or less returns A, B, C, D and E, which is five.
- (b) DENSE_RANK returns five at three or less and six at four or less, never four.
- (d) LAG reads the previous row; it ranks nothing.

**In the interview.** Exactly N rows means ROW_NUMBER with a named tiebreaker, so the cut is a decision someone owns.

### Q38, key 51 under RANK(); 50 under ROW_NUMBER().

**Why it holds.** Under RANK both tied members hold rank fifty, so 51 rows return; ROW_NUMBER numbers every row once and returns 50. The common wrong answer is 50 under both, which fails because RANK() gives both tied members rank fifty and the filter keeps both.

**In the interview.** RANK ships 51 on a tie at fifty, ROW_NUMBER ships 50 and drops one tied member by an arbitrary rule.

### Q39, key A fall of Rs 800, then a fall of Rs 300; the flag fires.

**Why it holds.** LAG gives 4,200 minus 5,000, a fall of Rs 800, and 3,900 minus 4,200, a fall of Rs 300. Two consecutive falls fire the flag. The common wrong answer takes last month minus this month, reads two rises of Rs 800 and Rs 300 and says the flag does not fire; LAG returns last month's value, and the change is this month minus that value, so both changes are falls.

**In the interview.** LAG puts last month beside this month, and two negative changes in a row fire the flag.

### Q40, key c

**Why it holds.** groupby splits rows by key, applies a computation to each group, and combines the results.

- (a) Returning the first row per key describes groupby().first(), one possible apply step, never groupby itself.
- (b) Joining two tables on a key is merge.
- (d) Removing duplicate keys is drop_duplicates.

**In the interview.** groupby is split by key, apply a computation to each group, combine one result per group.

### Q41, key b

**Why it holds.** A left merge grows only when a left key matches more than one right row, so some customer keys repeat in the exposure table.

- (a) A customer with no exposure keeps its one row with NaN; it adds nothing.
- (c) how='left' never appends the index as rows.
- (d) With different key names pandas raises an error; it never matches on position.

**In the interview.** Extra rows after a merge mean duplicate keys on the right; validate= would have raised before the count grew.

### Q42, key d

**Why it holds.** XLOOKUP's match_mode 0 is exact and is the default; -1 and 1 return the next smaller or larger item when there is no exact match, which is how a missing id returns a neighbour. Verified on Microsoft Support on 29 September 2026.

- (a) Arrays of different sizes make XLOOKUP return an error, which is visible.
- (b) Sorting the lookup array leaves an exact match exact; it returns no neighbour on its own.
- (c) Protection stops edits; it does not freeze formulas on an old result.

**In the interview.** Set match_mode to exact and give if_not_found a visible message, so a missing id says so.

### Q43, key a

**Why it holds.** Excel owns the last mile: presenting a clean table and letting a director slice it live.

- (b) Joining payments to orders is warehouse work, where the join can be audited.
- (c) The source-of-truth figure belongs in the warehouse, where nobody can type over it.
- (d) De-duplication is cleaning, which runs upstream in SQL or pandas before any total.

**In the interview.** Excel presents and lets people explore; it never cleans, joins or computes the number of record.

### Q44, key a, b, d

**Why it holds.** merge is the pandas join, validate= makes a fan-out fail loudly, and the row count check is still worth running.

- (c) A left merge keeps the left count only when the right keys are unique, which is the trap itself.

**In the interview.** merge is a SQL join in pandas; validate= states the relationship and the row count confirms it.

### Q45, key a, b, c

**Why it holds.** A single number is read correctly only with its denominator, its period and its comparison.

- (d) An exact figure changes no reading: Rs 19,84,00,000 to the rupee reads as a doubled quarter exactly as Friday's card of Rs 19.84 crore did, because what was missing was the period.

**In the interview.** One number needs its denominator, its period and a comparison, or the room fills them in wrongly.

### Q46, key 1,060

**Why it holds.** 940 customers match once and 60 match twice: 940 + 120 = 1,060. The common wrong answer is 1,000, which fails because a left merge keeps the left table's row count only when the right key is unique, and each of the 60 repeated customer_ids adds a row.

**In the interview.** Each repeated key adds a row, so 60 duplicates turn 1,000 customers into 1,060 rows.

### Q47, key d

**Why it holds.** validate='one_to_one' checks the keys on both sides and raises MergeError before a row is produced.

- (a) validate never removes rows; it only checks and raises.
- (b) validate applies to every merge type, including how='left'.
- (c) validate does not sort; sorting would leave the duplicates in place.

**In the interview.** validate= turns a silent fan-out into a MergeError at the merge.

### Q48, key True

**Why it holds.** The 60 duplicated customers have their revenue summed twice, so the pivot total is higher than the warehouse's.

**In the interview.** A pivot above the warehouse total points at duplicated rows upstream.

### Q49, key b

**Why it holds.** The error was made at the merge, so the fix belongs there: de-duplicate the exposure table on a stated rule and validate the keys.

- (a) Typing over the pivot's total hides the error and leaves no audit trail.
- (c) Revenue per customer is still wrong for the 60 duplicated customers.
- (d) A gap from double-counted customers is an error, never rounding.

**In the interview.** Fix where the error was made, at the merge, so every number downstream is right without editing.

### Q50, key 400 rows; 2.5 orders per customer.

**Why it holds.** One row per customer gives 400 rows, and 1,000 orders over 400 customers is 2.5. Integer division in Postgres would return 2, the week's trap.

**In the interview.** groupby customer gives 400 rows at 2.5 orders each, computed in decimals.

### Q51, key b, c, a

**Why it holds.** The warehouse computes the source of truth, pandas carries the analyst's iteration, and Excel presents it to the room. Any order that starts in pandas or Excel makes a copy the source of truth, which Friday's operating rule forbids: the number of record lives in the warehouse.

**In the interview.** The number flows from the warehouse through pandas to Excel, and never back the other way.

### Q52, key c

**Why it holds.** The CASE has no ELSE, so C3 and C4, who bought nothing in Q2, carry a NULL q2_spend where a zero was meant. AVG divides by the values it can see: avg_q1 is Rs 6,000 over four members and avg_q2 is C1's Rs 1,800 and C2's Rs 1,200 over two, so both come to 1,500 and the query reports spend per member as flat. Half the members stopped buying, and with COALESCE(..., 0) the honest Q2 figure is Rs 750, half of Q1. The check that catches it is count(*) beside count(q2_spend), 4 against 2. Run on PostgreSQL 16.13 on 30 September 2026, the query returns 1500 and 1500.

- (a) The figure the head of Retail-Plus needed, and one this query never computes: it would need COALESCE(..., 0) to count the two members with no Q2 order as zero. Reading AVG as dividing by every member is Monday's round 3 trap, the member average that quietly left out the members who bought nothing in the quarter.
- (b) Averages the three Q2 order rows, Rs 3,000 over three, at the order's grain, where the CTE first sums C1's two Q2 orders into one member. Rows read as customers is Monday's round 1 trap.
- (d) Reads NULL as spreading through the aggregate. AVG skips NULLs, as Monday's round 3 showed on the invented values 100, NULL and 200, where AVG returned 150; only arithmetic such as q2_spend - q1_spend turns NULL.

**In the interview.** AVG divides by the values it can see, so a CASE with no ELSE turns a member who bought nothing into a NULL that drops out of the denominator; I write the zero on purpose with COALESCE and put count(*) beside count(q2_spend), so the analyst auditing the query sees both denominators.

### Q53, key b

**Why it holds.** O-1's two instalments both fall inside the quarter, so the join gives O-1 two rows and SUM(o.amount) counts its Rs 1,200 twice. O-2's only payment is dated 1 October, so its joined row fails the WHERE. O-3 has no payment, so its paid_date is NULL, BETWEEN on a NULL is unknown, and WHERE drops that row too. Two rows remain, booked Rs 2,400, against three orders worth Rs 2,500: the report lost two orders and doubled the one it kept. Run on PostgreSQL 16.13 on 30 September 2026, the query returns 2 and 2400.

- (a) Assumes one row per order, which holds only once payments are brought to one row per order; O-1 has two payment rows inside the quarter, so the join repeats it. The fan-out is Tuesday's round 1 trap.
- (c) Keeps O-3 as if its NULL date passed the filter. A comparison with NULL is unknown and WHERE keeps only rows where it is true, which is how the LEFT JOIN with a date filter in Tuesday's round 3 emptied the unpaid list.
- (d) Reads the WHERE as if it sat in the ON clause, where it would keep every order and leave NULL payments on O-2 and O-3. In WHERE it runs after the join and turns the LEFT JOIN into an INNER one, which is Tuesday's round 3 trap.

**In the interview.** INNER keeps only the matched rows and LEFT keeps every left row with NULLs where nothing matched; both repeat a left row once per matching right row, and a WHERE on the right-hand table drops the NULL rows and turns the LEFT back into an INNER, so a filter on payments goes in ON and the payments go to one row per order before the join.

### Q54, key d

**Why it holds.** how='right' keeps every customer in reached, so t holds 5 rows, and validate passes because no key repeats. C5, C6 and C7 never ordered, so the merge gives them NaN for segment and for orders. groupby drops a missing key by default, so those three rows never reach a group: reached sums to 2 and bought to 2, and the slide reads 2 of 2 reached customers bought, 100 percent, where 2 of the 5 reached bought, 40 percent. Run on pandas 3.0.5 on 30 September 2026, the code prints 5 2 2.

- (a) Reads the merge as an inner one, which would keep only C1 and C2. An inner merge is the default, and how='right' here keeps all five reached customers; Thursday's round 2 showed the default dropping every customer the sale did not reach.
- (b) Reads how='right' as if it kept the left frame, the four buyers built from order rows. A frame built from order rows holds only the customers who ordered, which is why Thursday's round 1 built the table on the customer list; a right merge keeps every row of the right-hand frame, here the five reached.
- (c) Counts the three customers with no segment as a group of their own, which is what groupby does only with dropna=False. The default drops a missing key: Thursday's round 2 trap, where reach read 100 percent conversion until dropna=False showed the missing group.

**In the interview.** groupby splits the rows by a key, applies a computation to each group and combines one row per group, and a row whose key is missing belongs to no group, so the default drops it; after a merge that can leave a key empty I group from the full list or pass dropna=False, and check that the groups add back to the rows.

### Q55, key a

**Why it holds.** Every column in SELECT must either be grouped or aggregated, so segment either joins GROUP BY or sits inside an aggregate.

- (b) HAVING filters groups; the error is about a column that is neither grouped nor aggregated.
- (c) LIMIT trims rows after the query runs and never reaches the grouping error.
- (d) ORDER BY sorts the output and cannot make an ungrouped column legal.

**In the interview.** Every SELECT column is either in GROUP BY or inside an aggregate; the error names the one that is neither.


## Items by tag, level, day and part, for the tally

- [S] (29): Q2, Q4, Q6, Q7, Q8, Q12, Q14, Q15, Q16, Q17, Q18, Q21, Q23, Q24, Q27, Q28, Q29, Q30, Q32, Q34, Q35, Q40, Q42, Q43, Q45, Q48, Q53, Q54, Q55
- [F] (19): Q1, Q3, Q5, Q9, Q10, Q11, Q13, Q19, Q22, Q25, Q26, Q31, Q36, Q39, Q41, Q44, Q46, Q47, Q50
- [SV] (0): none
- [D] (7): Q20, Q33, Q37, Q38, Q49, Q51, Q52
- Easy (8): Q4, Q6, Q10, Q11, Q12, Q15, Q17, Q28
- Medium (34): Q1, Q2, Q3, Q5, Q7, Q9, Q13, Q14, Q16, Q18, Q19, Q21, Q23, Q24, Q25, Q26, Q27, Q29, Q30, Q34, Q35, Q39, Q40, Q41, Q42, Q43, Q44, Q45, Q46, Q47, Q48, Q50, Q51, Q55
- Hard (13): Q8, Q20, Q22, Q31, Q32, Q33, Q36, Q37, Q38, Q49, Q52, Q53, Q54
- Mon (9): Q4, Q5, Q12, Q13, Q14, Q15, Q16, Q52, Q55
- Tue (15): Q1, Q6, Q7, Q17, Q18, Q19, Q20, Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q53
- Wed (15): Q2, Q8, Q9, Q28, Q29, Q30, Q31, Q32, Q33, Q34, Q35, Q36, Q37, Q38, Q39
- Thu (11): Q3, Q10, Q40, Q41, Q44, Q46, Q47, Q48, Q49, Q50, Q54
- Fri (5): Q11, Q42, Q43, Q45, Q51
- Part 1, The week's rules, cold (11): Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11
- Part 2, Asking the warehouse (5): Q12, Q13, Q14, Q15, Q16
- Part 3, Joins that keep their rows (11): Q17, Q18, Q19, Q20, Q21, Q22, Q23, Q24, Q25, Q26, Q27
- Part 4, Windows: rank, lag and running totals (12): Q28, Q29, Q30, Q31, Q32, Q33, Q34, Q35, Q36, Q37, Q38, Q39
- Part 5, pandas and the last mile to Excel (12): Q40, Q41, Q42, Q43, Q44, Q45, Q46, Q47, Q48, Q49, Q50, Q51
- Part 6, Read the code, read the data (4): Q52, Q53, Q54, Q55

## New items waiting for the tracker

These items come from the week's source file, not the tracker. Accept one by adding it to the tracker's Saturday papers tab and deleting it from the source file.

- Q52 (One correct option, Hard, [D]): The head of Retail-Plus asks whether spend per member fell from Q1 to Q2, and the analyst answers with the query above. What does the query return, and how will she read it?
- Q53 (Scenario set, Hard, [S]): Anand wants every Q2 order beside what was collected on it within the quarter. Before the report goes to him, the analyst runs the query above to count its rows and their booked value. What does it return?
- Q54 (One correct option, Hard, [S]): The marketing lead asks how many customers the monsoon sale reached and how many of them bought, and the analyst runs the code above. What does it print?

## Option edits laid on the bank, waiting for the tracker

These options differ from the tracker's wording, each for the reason given beside it. The stem and the key are the tracker's. Accept an edit by copying it into the tracker; reject it by deleting it from `data/programme/paper_edits.yaml`.

- Q55 (bank 19), option b (proposed): The key was the longest option.
- Q18 (bank 22), option c (proposed): The key was the longest option; the new distractor is the fan-out misread in reverse.
- Q19 (bank 23), option b, d (proposed): The key was the longest option; the distractor is now the full query with the aggregate in WHERE. Option b then ran 38 characters against 73, so it now sorts its distinct list too, and the options run 47 to 73.
- Q40 (bank 29), option a (proposed): The key was the longest option.
- Q43 (bank 32), option c (proposed): The key was the longest option.
- Q14 (bank 33), option c, d (proposed): Options ran 22 to 39 characters, with c at 23 and d at 22 against b at 39; c and d now say which clause can compare COUNT(*) with a number, and the options run 34 to 41.
- Q21 (bank 34), option d (proposed): The font was a nonsense option, so striking it left a, b and c, which is the whole key; the new distractor is a check that sounds like the other three and cannot catch a fan-out.
- Q32 (bank 36), option b (proposed): Option b ran 25 characters against 60; it now names the quarter its total covers, and the options run 37 to 60.
- Q33 (bank 37), option b (proposed): Option b, part of the key, ran 37 characters against 63; it now says who ties, and the options run 40 to 63.
- Q44 (bank 38), option a (proposed): Option a, part of the key, ran 35 characters against 60; it now says the join is on a key, and the options run 40 to 60.
- Q45 (bank 39), option d (proposed): Cell colour was a nonsense option, so striking it left a, b and c, which is the whole key; the new distractor is the precision a room reaches for when a number is misread.
- Q25 (bank 42), option b, d (proposed): The key was the longest option; the distractor keeps the table-qualified column the key uses. Option d ran 16 characters against 51; it is now the anti-join from the payments side, which finds payments with no order, and the options run 37 to 51.
- Q37 (bank 47), option a (proposed): The key was the longest option.
- Q49 (bank 51), option a (proposed): The key was the longest option.

## The stretch page

- Stretch 1: Both counts are integers, so Postgres divides integers and drops the fraction: 1,000 / 400 returns 2. The right number is 2.5. Cast one side to numeric, as COUNT(*)::numeric / COUNT(DISTINCT customer_id), and check the result against a hand calculation on a small sample before the query runs every Monday.
- Stretch 2: WHERE runs after the join, and an unpaid order carries NULL in amount_paid, so the comparison is unknown and the row is dropped: the LEFT join now behaves like an INNER one. Move the condition into the ON clause so the unpaid orders stay. Then compare the row count before and after the join and count payment rows per order, because a retried payment recorded twice fans the join out and doubles those orders' amounts.
- Stretch 3: Name the conflict, since each rule is reasonable and they cannot both hold. Either ship 51 under RANK with the tie flagged, or ship 50 under ROW_NUMBER with a tiebreaker the business chooses and the report states, such as the earlier first order. Never let ROW_NUMBER break the tie on its own, because two runs can then hand two different lists.
- Stretch 4: pivot_table averages by default, so each cell is a mean order value where a total was meant; set aggfunc='sum' and reconcile the grand total with the warehouse. The lookup used a match mode of -1 or 1, which returns the next smaller or larger id when there is no exact match; set match_mode to 0 for an exact match and give if_not_found a visible message, so a missing id says so.
- Stretch 5 (bank 1, fill in the blank, moved from the timed paper): HAVING. HAVING runs after GROUP BY, so it is the only clause that can judge a group. The common wrong answer is GROUP BY itself, which forms the groups and filters nothing.
- Stretch 6 (bank 2, fill in the blank, moved from the timed paper): guarantee. A table has no stored order, so without ORDER BY the database returns whichever rows its plan reaches first, and two runs can differ. The common wrong answer is "sort", which fails because a plan that reads an index does return sorted rows on some runs; what the database withholds is the promise, so the word is guarantee.
- Stretch 7 (bank 3, fill in the blank, moved from the timed paper): CTE (common table expression). WITH names a common table expression, a query step the rest of the query reads like a table. "Subquery" is the near miss: a subquery is inline and unnamed.
- Stretch 8 (bank 4, fill in the blank, moved from the timed paper): left. A LEFT JOIN preserves every row of the table named before the join. "Right" and "both" describe RIGHT and FULL OUTER joins.
- Stretch 9 (bank 7, fill in the blank, moved from the timed paper): PARTITION. PARTITION BY restarts the window for each value of the column, so each segment is ranked on its own. GROUP BY is the common wrong answer, and it collapses the rows the window needs.
- Stretch 10 (bank 9, fill in the blank, moved from the timed paper): melt. melt turns columns into rows, which lengthens the table; pivot_table does the reverse. The common wrong answer is unstack, which fails because unstack moves an index level into the columns and so widens the table, the same direction as pivot_table.

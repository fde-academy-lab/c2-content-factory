# Week 2 recap paper: key

TRAINER. Rendered from the tracker's item bank by `scripts/build_saturday_paper.py`. Change an item in the tracker, or an option in `data/programme/paper_edits.yaml`, and sync; never edit this file by hand.

Saturday 17 October 2026. A 120-minute slot holding 58 items at 119.5 minutes by the blueprint's pace: 14 easy, 34 medium and 10 hard.

## Marking

1. Papers are swapped, so nobody marks their own.
2. The Academic TA reads the key out section by section, and the marker writes a tick or a cross beside each item.
3. An item is right when its answer matches the key: every correct letter and no other on a more-than-one item, the number on an applied maths item (the working belongs to the discussion), and the whole sequence on an ordering item. The programme has set no partial-credit rule, so this key uses none.
4. The marker writes the count of ticks as Items right on the front, out of 58, and hands the paper back.
5. The TA collects the papers and tallies the misses by tag, using the table below; that tally is Monday's remediation read. It is never a ranking and never read out by name.

## The key

| No. | Key | Type | Level | Tag | Roles | Day | Min | Interview anchor |
|---|---|---|---|---|---|---|---|---|
| 1 | HAVING | Fill in the blank | Easy | [S] | BA, DS | Mon | 1 | WHERE against HAVING, one sentence each. |
| 2 | guarantee | Fill in the blank | Easy | [F] | BA, DS | Mon | 1 | What does LIMIT without ORDER BY return? |
| 3 | CTE (common table expression) | Fill in the blank | Easy | [S] | BA, DS | Mon | 1 | Explain the logical order in which a SQL query executes. |
| 4 | left | Fill in the blank | Easy | [S] | BA, DS | Tue | 1 | INNER against LEFT join: what does each drop or keep? |
| 5 | NULL | Fill in the blank | Medium | [F] | BA, DS | Tue | 1 | How do you find orders with no payment? |
| 6 | NULL | Fill in the blank | Medium | [S] | BA, DS | Wed | 1 | How would you find customers whose spend fell two months in a row? |
| 7 | PARTITION | Fill in the blank | Easy | [S] | BA, DS | Wed | 1 | Top-3 per group: GROUP BY or a window, and why? |
| 8 | MergeError | Fill in the blank | Medium | [F] | BA, DS | Thu | 1 | Which merge argument raises on duplicate keys, and which error? |
| 9 | melt | Fill in the blank | Easy | [F] | BA, DS | Thu | 1 | pivot against melt: which widens and which lengthens? |
| 10 | False | True or false | Easy | [S] | BA, DS | Mon | 1 | Explain the logical order in which a SQL query executes. |
| 11 | False | True or false | Medium | [F] | BA, DS | Mon | 1 | WHERE against HAVING, one sentence each. |
| 12 | True | True or false | Easy | [S] | BA, DS | Tue | 1 | INNER against LEFT join: what does each drop or keep? |
| 13 | True | True or false | Medium | [S] | BA, DS, FDE | Tue | 1 | Revenue doubled after a join and every row looks fine; where do you look? |
| 14 | True | True or false | Hard | [S] | BA, DS | Wed | 1 | RANK, DENSE_RANK and ROW_NUMBER on a tie. |
| 15 | False | True or false | Medium | [F] | BA, DS | Wed | 1 | Why can a window function not sit inside WHERE, and what do you do instead? |
| 16 | True | True or false | Easy | [F] | BA, DS | Thu | 1 | groupby in the split-apply-combine sentence. |
| 17 | False | True or false | Easy | [F] | BA | Fri | 1 | Your pivot shows a different total from the warehouse; where do you look first? |
| 18 | b | One correct option | Easy | [S] | BA, DS | Mon | 2 | Explain the logical order in which a SQL query executes. |
| 19 | a | One correct option | Medium | [S] | BA, DS | Mon | 2 | Explain the logical order in which a SQL query executes. |
| 20 | d | One correct option | Medium | [F] | BA, FDE | Mon | 2 | Why would you compute a KPI in the warehouse rather than in a notebook? |
| 21 | c | One correct option | Easy | [S] | BA, DS | Tue | 2 | INNER against LEFT join: what does each drop or keep? |
| 22 | d | One correct option | Medium | [S] | BA, DS | Tue | 2 | Your join grew the row count; name the cause and the check. |
| 23 | a | One correct option | Medium | [F] | BA, DS | Tue | 2 | Revenue doubled after a join and every row looks fine; where do you look? |
| 24 | d | One correct option | Hard | [D] | BA, DS, FDE | Tue | 2 | Revenue doubled after a join and every row looks fine; where do you look? |
| 25 | c | One correct option | Easy | [S] | BA, DS | Wed | 2 | RANK, DENSE_RANK and ROW_NUMBER on a tie. |
| 26 | b | One correct option | Medium | [S] | BA, DS | Wed | 2 | RANK, DENSE_RANK and ROW_NUMBER on a tie. |
| 27 | b | One correct option | Medium | [S] | BA, DS | Wed | 2 | Top-3 per group: GROUP BY or a window, and why? |
| 28 | a | One correct option | Hard | [F] | BA, DS | Wed | 2 | The business says 'ties rank the same'; which function, and how many rows might the top-N report ship? |
| 29 | c | One correct option | Medium | [S] | BA, DS | Thu | 2 | groupby in the split-apply-combine sentence. |
| 30 | b | One correct option | Medium | [F] | BA, DS | Thu | 2 | Which merge argument raises on duplicate keys, and which error? |
| 31 | d | One correct option | Medium | [S] | BA | Fri | 2 | SQL, pandas or Excel: how do you choose? |
| 32 | a | One correct option | Medium | [S] | BA, FDE | Fri | 2 | SQL, pandas or Excel: how do you choose? |
| 33 | a, b, c | More than one correct | Medium | [S] | BA, DS | Mon | 2.5 | WHERE against HAVING, one sentence each. |
| 34 | a, b, c | More than one correct | Medium | [S] | BA, DS, FDE | Tue | 2.5 | Your join grew the row count; name the cause and the check. |
| 35 | a, b | More than one correct | Hard | [F] | BA, DS | Tue | 2.5 | INNER against LEFT join: what does each drop or keep? |
| 36 | a, c, d | More than one correct | Hard | [S] | BA, DS | Wed | 2.5 | Top-3 per group: GROUP BY or a window, and why? |
| 37 | a, b, c | More than one correct | Hard | [D] | BA, DS | Wed | 2.5 | The business says 'ties rank the same'; which function, and how many rows might the top-N report ship? |
| 38 | a, b, d | More than one correct | Medium | [F] | BA, DS | Thu | 2.5 | Which merge argument raises on duplicate keys, and which error? |
| 39 | a, b, c | More than one correct | Medium | [S] | BA, FDE | Fri | 2.5 | How do you present one number so it is not misread? |
| 40 | 1,050 | Scenario set | Medium | [S] | BA, DS | Tue | 2.5 | Your join grew the row count; name the cause and the check. |
| 41 | 1,020 | Scenario set | Medium | [S] | BA, DS | Tue | 2.5 | Your join grew the row count; name the cause and the check. |
| 42 | a | Scenario set | Medium | [F] | BA, DS | Tue | 2.5 | Your join grew the row count; name the cause and the check. |
| 43 | True | Scenario set | Medium | [F] | BA, DS | Tue | 2.5 | Your join grew the row count; name the cause and the check. |
| 44 | 4 | Scenario set | Medium | [S] | BA, DS | Wed | 2.5 | The business says 'ties rank the same'; which function, and how many rows might the top-N report ship? |
| 45 | 4 | Scenario set | Medium | [S] | BA, DS | Wed | 2.5 | The business says 'ties rank the same'; which function, and how many rows might the top-N report ship? |
| 46 | c | Scenario set | Hard | [F] | BA, DS | Wed | 2.5 | The business says 'ties rank the same'; which function, and how many rows might the top-N report ship? |
| 47 | c | Scenario set | Hard | [D] | BA, DS | Wed | 2.5 | The business says 'ties rank the same'; which function, and how many rows might the top-N report ship? |
| 48 | 1,060 | Scenario set | Medium | [F] | BA, DS, FDE | Thu | 2.5 | Your pivot shows a different total from the warehouse; where do you look first? |
| 49 | d | Scenario set | Medium | [F] | BA, DS, FDE | Thu | 2.5 | Your pivot shows a different total from the warehouse; where do you look first? |
| 50 | True | Scenario set | Medium | [S] | BA, DS, FDE | Thu | 2.5 | Your pivot shows a different total from the warehouse; where do you look first? |
| 51 | b | Scenario set | Hard | [D] | BA, DS, FDE | Thu | 2.5 | Your pivot shows a different total from the warehouse; where do you look first? |
| 52 | 8 | Applied maths | Easy | [S] | BA, DS | Mon | 4 | Explain the logical order in which a SQL query executes. |
| 53 | Rs 21 lakh, which overstates collections by Rs 1 lakh. | Applied maths | Medium | [S] | BA, DS | Tue | 4 | Revenue doubled after a join and every row looks fine; where do you look? |
| 54 | 51 under RANK(); 50 under ROW_NUMBER(). | Applied maths | Hard | [D] | BA, DS | Wed | 4 | The business says 'ties rank the same'; which function, and how many rows might the top-N report ship? |
| 55 | A fall of Rs 800, then a fall of Rs 300; the flag fires. | Applied maths | Medium | [F] | BA, DS | Wed | 4 | How would you find customers whose spend fell two months in a row? |
| 56 | 400 rows; 2.5 orders per customer. | Applied maths | Medium | [F] | BA, DS | Thu | 4 | groupby in the split-apply-combine sentence. |
| 57 | c, b, e, f, a, d | Order the steps | Medium | [S] | BA, DS | Mon | 2.5 | Explain the logical order in which a SQL query executes. |
| 58 | b, c, a | Order the steps | Medium | [D] | BA, FDE | Fri | 2.5 | SQL, pandas or Excel: how do you choose? |

## Items by tag, level and day, for the tally

- [S] (31): 1, 3, 4, 6, 7, 10, 12, 13, 14, 18, 19, 21, 22, 25, 26, 27, 29, 31, 32, 33, 34, 36, 39, 40, 41, 44, 45, 50, 52, 53, 57
- [F] (21): 2, 5, 8, 9, 11, 15, 16, 17, 20, 23, 28, 30, 35, 38, 42, 43, 46, 48, 49, 55, 56
- [SV] (0): none
- [D] (6): 24, 37, 47, 51, 54, 58
- Easy (14): 1, 2, 3, 4, 7, 9, 10, 12, 16, 17, 18, 21, 25, 52
- Medium (34): 5, 6, 8, 11, 13, 15, 19, 20, 22, 23, 26, 27, 29, 30, 31, 32, 33, 34, 38, 39, 40, 41, 42, 43, 44, 45, 48, 49, 50, 53, 55, 56, 57, 58
- Hard (10): 14, 24, 28, 35, 36, 37, 46, 47, 51, 54
- Mon (11): 1, 2, 3, 10, 11, 18, 19, 20, 33, 52, 57
- Tue (15): 4, 5, 12, 13, 21, 22, 23, 24, 34, 35, 40, 41, 42, 43, 53
- Wed (16): 6, 7, 14, 15, 25, 26, 27, 28, 36, 37, 44, 45, 46, 47, 54, 55
- Thu (11): 8, 9, 16, 29, 30, 38, 48, 49, 50, 51, 56
- Fri (5): 17, 31, 32, 39, 58

## Option edits laid on the bank, waiting for the tracker

These options differ from the tracker's wording, because the bank's key was the longest option. The stem and the key are the tracker's. Accept an edit by copying it into the tracker; reject it by deleting it from `data/programme/paper_edits.yaml`.

- Item 19, option b (proposed): The key was the longest option.
- Item 22, option c (proposed): The key was the longest option; the new distractor is the fan-out misread in reverse.
- Item 23, option d (proposed): The key was the longest option; the distractor is now the full query with the aggregate in WHERE.
- Item 29, option a (proposed): The key was the longest option.
- Item 32, option c (proposed): The key was the longest option.
- Item 42, option b (proposed): The key was the longest option; the distractor keeps the table-qualified column the key uses.
- Item 47, option a (proposed): The key was the longest option.
- Item 51, option a (proposed): The key was the longest option.

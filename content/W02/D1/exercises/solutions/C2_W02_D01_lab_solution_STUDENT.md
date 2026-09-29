# Solution: practice lab, the Monday tree by channel

Answers: 1b 2d 3a 4c 5b 6d 7c 8b 9c 10a 11d

## The idea being tested

A grouped query returns one row per group that exists after `WHERE`, and `HAVING` then removes
groups. A channel is a column on the order, so the channel tree needs no lookup until the question
asks whether a move is consumer or Business. Every column of someone else's query is checked before
any of it is trusted, because a query with one wrong column usually has two.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | b | Two quarters, so two groups. | a forgets the grouping. c counts channels. d is the table's rows, before grouping. |
| 2 | d | Four segments times two quarters, all present. | a and b group by one column. c ignores the grouping. |
| 3 | a | Only Student in Q1, with 27 orders, sits under 30. | b: 27 is under 30. c keeps every group. d guesses the consumer segments. |
| 4 | c | Three channels times three statuses, all present in Q2 above Rs 5,000: nine rows. | a counts channels only. b counts two statuses. d assumes four statuses. |
| 5 | b | FROM, WHERE, GROUP BY, HAVING, ORDER BY. | a filters rows after grouping. c starts before any table is named. d filters groups before they exist. |
| 6 | d | `HAVING` tests an aggregate, and an aggregate is computed per group, so the groups must exist first. | a: the written order is a convention of the language, the logical order is the reason. b: HAVING does not need sorted rows. c: HAVING can test aggregates that SELECT never shows. |
| 7 | c | `sum(amount) / count(*)` divides a numeric sum by a count, so the fraction survives; it only needs rounding for the reader. | a is `count(*)`, order rows. b is integer division and reads 1 everywhere. d: one column is right. |
| 8 | b | `count(*)` counts rows, and a row is an order: 153 app orders in Q2, from 124 customers. | a is `count(DISTINCT customer_id)`, 124. c and d need columns the query never reads. |
| 9 | c | Web fell from Rs 3,79,02,050 to Rs 2,36,61,000, a fall of Rs 1,42,41,050, or 37.6 percent. | a: app rose 1.1 percent. b: store rose 61.1 percent. d: web fell. |
| 10 | a | Web's Business orders fell Rs 1,42,19,000 and its consumer orders Rs 22,050: the Business part is 99.8 percent of the fall. | b: consumer orders did fall in every channel, and they are a sliver of the rupees. c: the split is nowhere near even. d: `lab_channel_split` tells it with one lookup line. |
| 11 | d | Store's Business orders rose by almost as much as web's fell, so the channel moves are Business orders changing channel; consumer orders fell in every channel, most in the app, 24.1 percent. | a and b read a Business shift as a channel's health. c drops a split that matters for consumer frequency. |

## The channel tree, as a model

| Channel | Q1 revenue | Q2 revenue | Change | Orders per customer, Q1 then Q2 |
|---|---|---|---|---|
| app | Rs 4,21,38,840 | Rs 4,25,90,270 | 1.1 percent up | 1.44 then 1.23 |
| store | Rs 1,99,59,110 | Rs 3,21,48,730 | 61.1 percent up | 1.29 then 1.31 |
| web | Rs 3,79,02,050 | Rs 2,36,61,000 | 37.6 percent down | 1.39 then 1.33 |

Block `lab_channel_tree` in `sql/C2_W02_D01_05_lab_STUDENT.sql` is the model query. A learner's
version that differs in column names and agrees on every number is right.

## The part worth arguing about

Item 11. Some pairs want to write that web is in trouble, because 37.6 percent is the biggest move
on the sheet. The split shows almost all of it is Business orders, a few large invoices placed
through a different channel from one quarter to the next. A channel sheet built on rupees alone is
a Business sheet in disguise, which is why Anand's analyst will want orders per customer beside it.

## Where the pattern lives in production

Channel attribution reports in retail are dominated by a few large accounts whenever B2B and
consumer orders share a table, and the standard guard is the same split: every channel number
reported twice, with and without the large accounts.

# Diagnostic key: Week 0, Tuesday

TRAINER ONLY. For the Academic TA and the Support TA, who mark every paper tonight. No part of this
file reaches a learner, since anyone absent today sits the same four papers on Wednesday.

## The rule every marker applies

- Each row of the four tables is worth its ticks: 13 for Python, 7 for SQL, 8 for statistics and 8
  for stating a problem, 36 in all.
- An answer earns its tick only when it matches the key or a variant this file lists. A near answer
  earns nothing, so two markers reach the same count on the same paper.
- Tick or cross each item on the paper in pen, then enter 1 or 0 per tick in the score workbook. A
  blank item is a 0.
- Handwriting that reads two ways, one of them right, earns the tick.

Where the row's interview questions are measured:

| Interview question | Tag | Items |
|---|---|---|
| Predict the output of this snippet | [SV] | 1 to 8 |
| What rows does this query return? | [SV] | 12 to 15 |
| Mean or median for this data, and why? | [S] | 19 |
| A business asks you to 'improve sales'; what are the first five questions you ask? | [F] | 27 |

Every output and every error line below was produced by running the snippet on Python 3.11 or the
query on PostgreSQL 16.

---

## Paper 1: Python, items 1 to 11

| No. | Key | Type | Ticks |
|---|---|---|---|
| 1 | `55` | Predict the output | 1 |
| 2 | `3 1 3.5` | Predict the output | 1 |
| 3 | `4`, `5` and `8`, on three lines | Predict the output | 1 |
| 4 | `60` | Predict the output | 1 |
| 5 | `5` | Predict the output | 1 |
| 6 | `8`, then `None`, on two lines | Predict the output | 1 |
| 7 | `3 10` | Predict the output | 1 |
| 8 | `265.0 25.0` | Predict the output | 1 |
| 9 | `cost = int(parts[1]) * int(parts[2])` | Fix the line | 1 |
| 10 | `total = total + prices.get(item, 0)` | Fix the line | 1 |
| 11 | The function below, in three ticks | Write a function | 3 |

**Predicting output, items 1 to 8.** The answer has to carry the printed values in the printed order
and on the printed lines. Quotes around the whole answer are accepted when what sits inside them
matches, and commas between values printed on one line are accepted, since the items test the
values rather than the separator.

| No. | Earns nothing | Why |
|---|---|---|
| 1 | `10` | `*` on a string repeats it, so `"5" * 2` is `"55"` |
| 2 | `3 1 3` or `3.5 1 3.5` | `//` divides and drops the remainder, and `/` always gives a float |
| 3 | `8` alone, or the three values on one line | The `print` sits inside the loop, so it runs three times |
| 5 | `6` or `3` | Only the two tea orders are added, and both are |
| 6 | `8` alone, or `None` alone | A function with no `return` gives back `None`, and the second `print` shows it |
| 7 | `2 10` or `3 tea` | Splitting on two commas gives three parts, and `[-1]` is the last |
| 8 | `265 25`, or the two values swapped | `/` always gives a float, and `print` shows the mean first |

**Item 9.** Accepted: both values converted with `int()`, with or without spaces around `*`. Earns
nothing: `float()` on both, which prints `20.0` where the item asks for `20`; converting only one
value, since `int(parts[1]) * parts[2]` prints `1010`; and typing the numbers in, such as
`cost = 2 * 10`, since the item asks for the values in `parts`.

**Item 10.** Accepted: `total = total + prices.get(item, 0)`, `total += prices.get(item, 0)`, a
guard such as `if item in prices: total = total + prices[item]`, and a `try` with
`except KeyError` that leaves the total unchanged. Earns nothing: `prices.get(item)` with no default,
which stops on the same line with `TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'`;
adding juice to the price list, which changes another line; removing juice from the order; and
`total = 25`.

**Item 11, three ticks.** The reference answer:

```python
def total_by_item(orders):
    totals = {}
    for o in orders:
        item = o["item"]
        totals[item] = totals.get(item, 0) + o["qty"]
    return totals
```

| Tick | Earned when | Earns nothing |
|---|---|---|
| 11a | The function is named `total_by_item`, takes the orders and hands the dictionary back with `return` | Printing the dictionary instead of returning it |
| 11b | A loop runs over the orders and reads each order's `item` and `qty` | Reading only the first order, or an answer with no loop |
| 11c | The totals come out as `{"pen": 4, "notebook": 2}` for the example, including the first time an item appears | Adding to a key that does not exist yet stops with `KeyError: 'pen'`; counting orders gives `{"pen": 2, "notebook": 1}`; assigning instead of adding gives `{"pen": 1, "notebook": 2}`; creating the dictionary inside the loop gives `{"pen": 1}` |

An `if` and `else` that starts a new item at its quantity and adds to one already seen earns 11c as
well as `get` does. An answer that imports anything, such as `Counter`, earns 11a at most, because
the item asks for the loop.

---

## Paper 2: SQL, items 12 to 18

| No. | Key | Type | Ticks |
|---|---|---|---|
| 12 | Chemistry 21, then Calculus 20 | Predict the rows | 1 |
| 13 | Arts 2, then Maths 4, then Science 2 | Predict the rows | 1 |
| 14 | S01 32, then S05 21 | Predict the rows | 1 |
| 15 | S02 Algebra, then S02 Poetry | Predict the rows | 1 |
| 16 | `SELECT book, student FROM issues WHERE dept = 'Maths';` | Write the query | 1 |
| 17 | `SELECT * FROM issues ORDER BY days_kept DESC;` | Write the query | 1 |
| 18 | `SELECT book, COUNT(*) AS times FROM issues GROUP BY book ORDER BY times DESC;` | Write the query | 1 |

**Predicting rows, items 12 to 15.** Every row, in order, with the right values; column headers are
not needed.

| No. | Earns nothing | Why |
|---|---|---|
| 12 | Physics 14 among the rows, or the two rows in the other order | `> 14` leaves out 14, and `DESC` puts 21 first |
| 13 | Any other count, or the departments in another order | `ORDER BY dept` sorts the names alphabetically |
| 14 | S05 left out, or S03 16 added | `HAVING` filters the totals, and 21 is more than 20 while 16 is not |
| 15 | S01 or S05 among the rows | `ORDER BY days_kept` with no `DESC` runs from the shortest keep, 3 and then 5 days |

**Writing queries, items 16 to 18.** The query has to return exactly the rows asked for when run
against Postgres. Keyword case, line breaks, spacing, a missing semicolon and a column alias do not
matter. A misspelt table or column name, a string in double quotes and a missing clause do.

- **Item 16.** Either column order is accepted. `SELECT *` earns nothing, since the item asks for two
  columns. `'maths'` in lower case earns nothing, since Postgres compares text exactly and the query
  returns no rows. `"Maths"` in double quotes earns nothing, since Postgres reads it as a column and
  stops with `ERROR: column "Maths" does not exist`.
- **Item 17.** `SELECT *` or all five columns named are accepted. Without `DESC` the query returns
  the shortest keep first and earns nothing.
- **Item 18.** `COUNT(*)`, `COUNT(issue_id)` or `COUNT(book)` are accepted, and so is ordering by
  `COUNT(*) DESC` or by the alias. The three books issued twice (Algebra, Calculus and Poetry) may
  come in any order among themselves. With no `GROUP BY` the query stops with
  `ERROR: column "issues.book" must appear in the GROUP BY clause or be used in an aggregate function`,
  and with no `ORDER BY` it ignores the most-issued-first part of the item; neither earns the tick.

---

## Paper 3: statistics, items 19 to 26

| No. | Key | Type | Ticks |
|---|---|---|---|
| 19 | b | One correct option | 1 |
| 20 | 5.5 | Applied maths | 1 |
| 21 | a | One correct option | 1 |
| 22 | d | One correct option | 1 |
| 23 | c | One correct option | 1 |
| 24 | Rise 25, fall 20 | Applied maths | 1 |
| 25 | False | True or false | 1 |
| 26 | 15 | Applied maths | 1 |

| No. | Why the key holds | Why the others fail |
|---|---|---|
| 19 | The median, Rs 55, sits among the six ordinary spends, while one Rs 900 spend drags the mean to Rs 173.6, above six of the seven | a counts every spend, which is exactly why one spend moves it so far; c answers what the canteen took in, a different question from what a typical student spends; d is right about this list and wrong about "any set", since a total or a budget needs the mean |
| 20 | Sorted, the list is 3, 4, 7, 9, and the middle two average to 5.5 (5½ is accepted) | |
| 21 | Both shops average 50, and Shop Q's days run from 20 to 80 against Shop P's 48 to 52 | b treats the same average as the same behaviour; c has the averages wrong; d has the spread the wrong way round |
| 22 | The bars read 100 and 105, and 5 more on 100 is 5 percent | a reads the bar heights, which the axis starting at 95 exaggerates; b gives up on a chart whose axis labels still read exactly; c turns the week's total into a daily figure |
| 23 | Four days cannot separate a real preference from a lucky week | a and d both treat 3 days out of 4 as a settled rate; b compares a count over 100 days with a count over 4 |
| 24 | 5,000 on a base of 20,000 is 25 percent, and the same 5,000 on a base of 25,000 is 20 percent; the tick needs both numbers | |
| 25 | A very large value pulls the mean by its whole size spread over the count, while the median moves by at most one position | |
| 26 | 20 minus 5 | |

---

## Paper 4: stating a problem, items 27 and 28

| No. | Key | Type | Ticks |
|---|---|---|---|
| 27 | Five questions from five different categories below | Five questions | 5 |
| 28 | Three hypotheses that each pass the test below | Three hypotheses | 3 |

**Item 27, one tick per question.** A question earns a tick when it falls in one of the six
categories and no earlier question on the paper has already earned a tick in that category. A line
that asks two things counts once. The six categories are this programme's own, drawn for this paper.

| Category | The owner's answer would tell you | Questions that belong here |
|---|---|---|
| A. The measure | What "sales" means in this shop | Do you mean takings in rupees, the number of bills or the number of items sold? Is profit down as well? |
| B. The size and the baseline | How far down, against what, since when | Down by how much, compared with last term or with the same term last year? When did you first notice? |
| C. Where it fell | Which part of the business carries the fall | Is it all three shops or one of them? Which products? Which customers: students, staff, walk-ins? |
| D. What changed | The candidate causes, in the owner's words | What changed this term: prices, stock, staff, opening hours, a new shop or an online seller, the number of students? What do you think changed? |
| E. The goal and the room to act | What an answer has to achieve | What would count as improved, and by when? What budget is there? What can you change and what can you not? |
| F. The records | What evidence exists | What records do you keep: bills, a billing system, stock registers? Who keeps them? |

Earns nothing: a proposal dressed as a question ("Have you tried a discount?", "Should we put the
shops online?"), a question with no answer the owner could give ("Why do customers not like the
shops?"), and a second question in a category that has already earned its tick.

**Item 28, one tick per hypothesis.** A hypothesis earns a tick when all three hold: it names one
specific possible cause of the fall, which is neither a restatement of the problem nor a fix; the
number beside it could come back and rule the cause out; and it differs from the hypotheses above
it on the paper.

| Accepted, with its number | Not accepted, and why |
|---|---|
| Fewer students are on campus this term: enrolment or hostel numbers against last term, beside bills per day | "Customers are buying less": it restates the fall |
| Prices went up and buyers went elsewhere: the number of bills before and after the price change, with the average bill value | "A loyalty card would bring them back": it is a fix, not a cause |
| Fast-moving items ran out: the days each top item was out of stock this term against last | "The shops have had bad luck": nothing could rule it out |
| A new shop or an online seller took the buyers: the fall at the shop nearest the newcomer against the other two | A cause with no number beside it |
| The term's calendar moved demand: weekly sales against the dates of exams and project deadlines, this term and last | The same cause again in other words |

A hypothesis the key does not list earns its tick when it passes the three-part test. When two
markers disagree about one, the Academic TA's reading stands and the case is added to this file for
the make-up.

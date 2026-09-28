# Self-check key: practice set, part 2, SQL

Answer every item before reading this. Every result below was produced by running the query on
PostgreSQL 16 against the eight rows of week 1.

## The answers

| No. | Answer | Kind |
|---|---|---|
| 12 | Chemistry 21, then Calculus 20 | Predict the rows |
| 13 | Arts 2, then Maths 4, then Science 2 | Predict the rows |
| 14 | S01 32, then S05 21 | Predict the rows |
| 15 | S02 Algebra, then S02 Poetry | Predict the rows |
| 16 | `SELECT book, student FROM issues WHERE dept = 'Maths';` | Write the query |
| 17 | `SELECT * FROM issues ORDER BY days_kept DESC;` | Write the query |
| 18 | `SELECT book, COUNT(*) AS times FROM issues GROUP BY book ORDER BY times DESC;` | Write the query |

## Predicting rows, items 12 to 15

Your answer is right when it has every row, in order, with the right values.

| No. | A common wrong answer | Why it is wrong |
|---|---|---|
| 12 | Physics 14 among the rows, or the two rows in the other order | `> 14` leaves out 14, and `DESC` puts 21 first |
| 13 | Any other count, or the departments in another order | `ORDER BY dept` sorts the names alphabetically |
| 14 | S05 left out, or S03 16 added | `HAVING` filters the totals, and 21 is more than 20 while 16 is not |
| 15 | S01 or S05 among the rows | `ORDER BY days_kept` with no `DESC` runs from the shortest keep, 3 and then 5 days |

## Writing queries, items 16 to 18

Your query is right when, run against the eight rows, it returns exactly the rows asked for. Keyword
case, line breaks, spacing and a column alias do not matter; a misspelt name, text in double quotes
and a missing clause do.

- **Item 16.** Either column order is right. `SELECT *` is not, since the item asks for two columns.
  `'maths'` in lower case returns no rows, since Postgres compares text exactly, and `"Maths"` in
  double quotes stops with `ERROR:  column "Maths" does not exist`.
- **Item 17.** `SELECT *` or all five columns named are both right. Without `DESC` the query returns
  the shortest keep first.
- **Item 18.** `COUNT(*)`, `COUNT(issue_id)` and `COUNT(book)` are all right, and so is ordering by
  `COUNT(*) DESC` or by the alias. The three books issued twice, Algebra, Calculus and Poetry, may come
  in any order among themselves.

## Check it by running it

Every item runs in psql with `week = 1` added, as the practice set's first page says. Item 12, for
example, becomes:

```sql
SELECT book, days_kept
FROM issues
WHERE week = 1 AND days_kept > 14
ORDER BY days_kept DESC;
```

# Practice set, part 2 of 4: SQL

Week 0, for the long weekend. About 30 minutes, on paper first, with no assistant and no notes. The
set is ungraded: answer every item, then check yourself against the self-check key.

Items 12 to 18. Every item uses these eight rows of `issues`, which are week 1 of the table you loaded
on Thursday. To run an item in psql, add the condition `week = 1`, as `WHERE week = 1` or, where the
query already has a `WHERE`, as `AND week = 1`.

| issue_id | student | book | dept | days_kept |
|---|---|---|---|---|
| 1 | S01 | Algebra | Maths | 12 |
| 2 | S02 | Poetry | Arts | 5 |
| 3 | S01 | Calculus | Maths | 20 |
| 4 | S03 | Poetry | Arts | 9 |
| 5 | S04 | Physics | Science | 14 |
| 6 | S02 | Algebra | Maths | 3 |
| 7 | S05 | Chemistry | Science | 21 |
| 8 | S03 | Calculus | Maths | 7 |

---

## Predict the rows

Write the rows each query returns, in the order it returns them: one row per line, with the values
in the order the query names the columns. Write "no rows" if it returns none.

### 12

```sql
SELECT book, days_kept
FROM issues
WHERE days_kept > 14
ORDER BY days_kept DESC;
```

Your rows:

______________________________

______________________________

______________________________

### 13

```sql
SELECT dept, COUNT(*) AS issued
FROM issues
GROUP BY dept
ORDER BY dept;
```

Your rows:

______________________________

______________________________

______________________________

### 14

```sql
SELECT student, SUM(days_kept) AS total_days
FROM issues
GROUP BY student
HAVING SUM(days_kept) > 20
ORDER BY total_days DESC;
```

Your rows:

______________________________

______________________________

______________________________

### 15

```sql
SELECT student, book
FROM issues
ORDER BY days_kept
LIMIT 2;
```

Your rows:

______________________________

______________________________

---

## Write the query

Write each query for the `issues` table above.

### 16

Return the book and the student for every issue from the Maths department.

```sql







```

### 17

Return every column of every issue, with the issue kept longest first.

```sql







```

### 18

Return each book with the number of times it was issued, the most-issued book first.

```sql







```

# Exercise: the month's log

Week 0, Thursday. About twenty-five minutes, alone. Every item runs on the `issues` table, the
library's four weeks of issues, printed in full at the end of this sheet. Predict first, on paper,
then run the query in psql to check. Answer each item with one letter, except item 12, which takes
four letters in order.

Post one line: 1a 2d 3b 4a 5c 6d 7c 8d 9a 10b 11c 12 dcab

---

### 1

```sql
SELECT COUNT(*) FROM issues WHERE week = 2;
```

What does it return?

a) 8
b) 10
c) 18
d) 38

### 2

Which `WHERE` line keeps only the Commerce issues?

a) `WHERE dept = "Commerce"`
b) `WHERE dept = Commerce`
c) `WHERE dept = 'Commerce'`
d) `WHERE 'dept' = 'Commerce'`

### 3

```sql
SELECT COUNT(*) FROM issues WHERE dept = 'Arts' AND days_kept > 14;
```

What does it return?

a) 3
b) 11
c) 14
d) 0

### 4

```sql
SELECT MAX(days_kept) FROM issues WHERE dept = 'Maths';
```

What does it return?

a) 23
b) 19
c) 20
d) 12

### 5

```sql
SELECT dept, COUNT(*) FROM issues WHERE week = 3 GROUP BY dept;
```

How many rows come back?

a) 1
b) 3
c) 10
d) 4

### 6

```sql
SELECT student, COUNT(*) AS n
FROM issues
GROUP BY student
ORDER BY n DESC, student;
```

What is the first row?

a) S01, 5
b) S02, 6
c) S03, 5
d) S09, 3

### 7

```sql
SELECT book, COUNT(*) AS n
FROM issues
GROUP BY book
HAVING COUNT(*) >= 5;
```

How many rows come back?

a) 5
b) 2
c) 8
d) 3

### 8

The librarian wants only the departments with more than 10 issues. Which line does that, after
`GROUP BY dept`?

a) `WHERE COUNT(*) > 10`
b) `HAVING COUNT(*) > 10`
c) `ORDER BY COUNT(*) > 10`
d) `AND COUNT(*) > 10`

### 9

```sql
SELECT SUM(days_kept - 14) FROM issues WHERE week = 4 AND days_kept > 14;
```

What does it return?

a) 9
b) 14
c) 16
d) 53

### 10

```sql
SELECT dept, COUNT(*) FROM issues GROUP BY dept WHERE week = 1;
```

Postgres answers `ERROR:  syntax error at or near "WHERE"`. Which reading is right?

a) `WHERE` belongs before `GROUP BY`, so it is in the wrong place.
b) `COUNT(*)` needs a column name inside it before it can run here.
c) `GROUP BY` must be written before `FROM`, so the whole order is wrong.
d) The number 1 must sit in single quotes, since week is compared.

### 11

```sql
SELECT ROUND(AVG(days_kept), 1) FROM issues WHERE dept = 'Science';
```

What does it return?

a) 11.9
b) 135
c) 10.0
d) 13.5

### 12

Put these clauses in the order they are written in one query, and post the four letters.

a) `HAVING COUNT(*) > 2`
b) `FROM issues`
c) `GROUP BY student`
d) `WHERE days_kept > 14`

---

## The month's log

| issue_id | week | student | book | dept | days_kept |
|---|---|---|---|---|---|
| 1 | 1 | S01 | Algebra | Maths | 12 |
| 2 | 1 | S02 | Poetry | Arts | 5 |
| 3 | 1 | S01 | Calculus | Maths | 20 |
| 4 | 1 | S03 | Poetry | Arts | 9 |
| 5 | 1 | S04 | Physics | Science | 14 |
| 6 | 1 | S02 | Algebra | Maths | 3 |
| 7 | 1 | S05 | Chemistry | Science | 21 |
| 8 | 1 | S03 | Calculus | Maths | 7 |
| 9 | 2 | S02 | Physics | Science | 16 |
| 10 | 2 | S06 | Poetry | Arts | 4 |
| 11 | 2 | S01 | Algebra | Maths | 15 |
| 12 | 2 | S07 | History | Arts | 22 |
| 13 | 2 | S03 | Chemistry | Science | 9 |
| 14 | 2 | S06 | Algebra | Maths | 14 |
| 15 | 2 | S04 | History | Arts | 11 |
| 16 | 2 | S08 | Calculus | Maths | 6 |
| 17 | 2 | S02 | Chemistry | Science | 19 |
| 18 | 2 | S07 | Poetry | Arts | 8 |
| 19 | 3 | S09 | Economics | Commerce | 10 |
| 20 | 3 | S01 | Calculus | Maths | 13 |
| 21 | 3 | S05 | Physics | Science | 17 |
| 22 | 3 | S10 | Accounts | Commerce | 6 |
| 23 | 3 | S03 | Poetry | Arts | 12 |
| 24 | 3 | S08 | Algebra | Maths | 18 |
| 25 | 3 | S02 | Chemistry | Science | 8 |
| 26 | 3 | S06 | History | Arts | 15 |
| 27 | 3 | S09 | Accounts | Commerce | 11 |
| 28 | 3 | S04 | Physics | Science | 5 |
| 29 | 4 | S07 | Poetry | Arts | 7 |
| 30 | 4 | S01 | Algebra | Maths | 9 |
| 31 | 4 | S10 | Economics | Commerce | 23 |
| 32 | 4 | S05 | Chemistry | Science | 12 |
| 33 | 4 | S03 | History | Arts | 16 |
| 34 | 4 | S02 | Calculus | Maths | 4 |
| 35 | 4 | S08 | Physics | Science | 14 |
| 36 | 4 | S06 | Poetry | Arts | 10 |
| 37 | 4 | S04 | Algebra | Maths | 19 |
| 38 | 4 | S09 | Economics | Commerce | 8 |

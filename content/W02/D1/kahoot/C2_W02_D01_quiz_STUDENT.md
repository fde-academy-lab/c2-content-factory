# Kahoot, Week 2 Monday

Eight items, ungraded, scored on correctness and speed together. Six follow the day, one returns to
Week 1 Thursday one level up, and one closes on the suite.

Each item names what it tests, so an item dropped for time says what was lost.

---

## Q1. A query holds WHERE status = 'delivered' and a SELECT with sum(amount). Which of the two runs first?
*Tests: the logical order, FROM then WHERE then the rest, with SELECT late.*

- SELECT, since it is written first in the query
- WHERE, since rows are kept before columns are computed  <- correct
- Both at once, since the database runs a query as a whole
- It depends on which clause is longer in the query text

---

## Q2. Anand wants only segments with more than 5 orders, and WHERE count(*) > 5 is refused. What does the query need instead?
*Tests: WHERE tests rows before groups exist; HAVING tests groups after.*

- A subquery that counts the orders first, then a WHERE
- An ORDER BY count(*) with LIMIT 5 on the result
- HAVING count(*) > 5, after the GROUP BY  <- correct
- A cast of count(*) to numeric inside the WHERE

---

## Q3. Four segments ordered in both quarters. How many rows does GROUP BY segment, quarter return?
*Tests: one row per group that exists, predicted before the run.*

- 8  <- correct
- 4
- 2
- 1,000

---

## Q4. A query ends in LIMIT 5 with no ORDER BY. Which five rows come back?
*Tests: a table has no order, so an unordered limit promises nothing.*

- The five with the smallest primary key
- The five most recently inserted rows
- Five rows picked at random, fresh on every run
- Whichever five the database reaches first  <- correct

---

## Q5. WITH a AS (...), b AS (...) SELECT ... What can block b read?
*Tests: a CTE is a named step, and a later step reads every earlier one.*

- Only the tables, never block a
- Block a and every table  <- correct
- Only block a, and no tables
- Nothing until the final SELECT runs

---

## Q6. Week 1 counted how many orders carried a discount, with a loop and an if. What is that in one SQL line?
*Tests: count(column) counts the rows where the column has a value.*

- SELECT count(*) FROM orders;
- SELECT count(*) FROM orders WHERE discount = 0;
- SELECT avg(discount) FROM orders;
- SELECT count(discount) FROM orders;  <- correct

---

## Q7. Week 1 Thursday: the monsoon discount's 6 percent lift was a mix effect. What would a fair comparison need?
*Tests: the return question, one level up: compare like with like before reading a lift.*

- Treated against untreated orders within each segment  <- correct
- A larger discount, so that the lift clears the noise
- The same comparison over a longer window of dates
- More treated orders, until the lift is significant

---

## Q8. In Postgres, what does SELECT 140 / 76 print?
*Tests: integers divide as integers, the trap behind a frequency that halves overnight.*

- 1.84
- 1.8421052631578947
- 1  <- correct
- 2

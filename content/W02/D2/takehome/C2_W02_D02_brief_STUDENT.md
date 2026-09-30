# Take-home: a second book, and the number Anand keeps

Four parts, about two hours in all. Part 1 is the day's case on a book you have not seen, and it is
the part tomorrow opens on. Part 2 is a join question of your own. Parts 3 and 4 are short.

---

## The situation

Anand liked the Q2 report, and he has a second book for you: a smaller Q2 book, invented for
tonight, with its own orders, payments and refunds across the same three channels. He writes:

> "Same question, one step further. For this book's Q2, tell me what we collected net of
> refunds, by channel, and prove to me it is not double-counted. Then tell me the one thing you want
> me to do about it."

---

## Part 1. Collected net of refunds, by channel, about 70 minutes

The book is invented for tonight and sits in `data/C2_W02_D02_takehome_STUDENT.sql`. It loads into
its own schema, `takehome`, and never touches the warehouse tables. From the day folder:

```
psql -d kalpa -v ON_ERROR_STOP=1 -f data/C2_W02_D02_takehome_STUDENT.sql
```

Then query `takehome.orders`, `takehome.payments` and `takehome.refunds`. Nobody has profiled this
book for you, and none of the day's numbers carry across.

Write one SQL file, `C2_W02_D02_takehome_<your name>.sql`, that holds, in this order:

1. **The grain of each table**, as a comment line each, with the query that proves it: whether
   order_id repeats in payments and in refunds, and why that matters for the join.
2. **The reconciliation, written before the numbers.** A comment block with orders in, rows out,
   the difference, and every payment row accounted for: counted once in collected, posted a second
   time, or matched to no order at all. Fill in the numbers after you run the queries.
3. **The report by channel**: orders, booked, collected, refunded, collected net of refunds, and
   the gap between booked and collected.
4. **The checks**, each a query that returns true: rows out equals rows in; booked after the join
   equals booked from orders alone; the gap is fully explained by the orders you list as short of
   payment; and the feed's rows and rupees are all accounted for.
5. **The lists you hand Anand.** Anand will act on every order you put in front of him, so decide
   which orders belong on the list his team chases and which do not, and write three sentences
   defending each list by what Anand would do with it. A list without a reason counts as no list.
6. **The refunds.** Anand reads "refunded" as money that went back to customers. Write one comment
   line on how you made sure your refunded column and your net figure mean exactly that.
7. **The decision sentence to Anand**: the collected net figure, how you know it is honest, and the
   one action you want from him, with the order ids it applies to.

Run the file top to bottom from a fresh connection before you call it done. The self-check file tells
you whether each number is right.

---

## Part 2. One more join question of your own, about 30 minutes

On the warehouse's orders and payments, pose one question the day did not ask, in a stakeholder's
words, and answer it with a join. Above the query, write the count reconciliation as a comment block:
rows in, rows out, and the difference named. "Collected for Q1" is the practice lab's problem and
does not count. The shape that is wanted is a question where the join type is a choice you have to
defend, such as a question about paid orders only, or about payments with no order.

---

## Part 3. Practice, about 20 minutes

SQLBolt, the three join lessons, in order:

- Lesson 6, joins: https://sqlbolt.com/lesson/select_queries_with_joins (verified 29 Sep 2026)
- Lesson 7, outer joins: https://sqlbolt.com/lesson/select_queries_with_outer_joins (verified 29 Sep 2026)
- Lesson 8, NULLs: https://sqlbolt.com/lesson/select_queries_with_nulls (verified 29 Sep 2026)

If you finish early, the first three problems in the joins category of PostgreSQL Exercises,
https://pgexercises.com/questions/joins/ (verified 29 Sep 2026).

---

## Part 4. Recap, one line

At the top of your SQL file, write one comment line on when an INNER join is the honest choice.

---

## What makes this hard to shortcut

The book in Part 1 is new tonight, so no assistant has seen its numbers, and your report either
matches the self-check or it does not. The lists in step 5 and the action in step 7 are
choices with reasons, and a reason that could be written without running the queries reads that way
at once. Part 2 is a question you chose, and tomorrow the room asks you why that join.

---

## What to bring tomorrow

| Part | What to bring |
|---|---|
| 1 | The SQL file, run from a fresh connection, every check true, with your lists and your sentence to Anand |
| 2 | Your question, its query and its reconciliation block |
| 3 | The SQLBolt lessons finished |
| 4 | Your one line |

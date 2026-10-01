# What did a second book collect net of refunds, by channel, and how do you prove it is not double-counted?

The take-home has four parts, about two hours in all, and a fifth if the practice lab ran out of
time. Part 1 is the day's case on a book you have not seen, and it is the part tomorrow opens on.
Part 2 is a join question of your own, and parts 3 and 4 are short. On a faculty day the tentative
IITGN block W2-2 takes the afternoon's last two hours, so whatever the lab did not reach comes home as
part 5.

---

## What does Anand ask of the second book?

Anand liked the Q2 report, and he has a second book for you: a smaller Q2 book, invented for
tonight, with its own orders, payments and refunds across the same three channels. He writes:

> "Same question, one step further. For this book's Q2, tell me what we collected net of
> refunds, by channel, and prove to me it is not double-counted. Then tell me the one thing you want
> me to do about it."

---

## Part 1. What did the book collect net of refunds, by channel, and how do you prove it?

Allow about 70 minutes. At work this is the month-end collections report, run on a book nobody
profiled for you.

The book is invented for tonight and sits in `data/C2_W02_D02_takehome_STUDENT.sql`. It loads into
its own schema, `takehome`, and never touches the warehouse tables. Run this from the day folder:

```
psql -d kalpa -v ON_ERROR_STOP=1 -f data/C2_W02_D02_takehome_STUDENT.sql
```

Then query `takehome.orders`, `takehome.payments` and `takehome.refunds`. None of the day's numbers
carry across to this book.

Write one SQL file, `C2_W02_D02_takehome_<your name>.sql`, that holds, in this order:

1. The grain of each table, one comment line per table, with the query that proves it: whether
   order_id repeats in payments and in refunds, and why that matters for the join.
2. The reconciliation, written before the numbers, as a comment block with orders in, rows out, the
   difference, and every payment row accounted for: counted once in collected, posted a second time,
   or matched to no order at all. Fill in the numbers after you run the queries.
3. The report by channel, with orders, booked, collected, refunded, collected net of refunds, and
   the gap between booked and collected.
4. The checks, each a query that returns true: rows out equals rows in; booked after the join
   equals booked from orders alone; the gap is fully explained by the orders you list as short of
   payment; and the feed's rows and rupees are all accounted for.
5. The lists you hand Anand. He will act on every order you put in front of him, so decide which
   orders belong on the list his team chases and which do not, and write three sentences defending
   each list by what Anand would do with it. A list without a reason counts as missing.
6. One comment line on the refunds. Anand reads "refunded" as money that went back to customers, so
   say how you made sure your refunded column and your net figure mean exactly that.
7. The decision sentence to Anand, with the collected net figure, how you know it is honest, and the
   one action you want from him, with the order ids it applies to.

Run the file top to bottom from a fresh connection before you call it done. The self-check file tells
you whether each number is right.

---

## Part 2. Which join question of your own does the warehouse answer, and why that join?

Allow about 30 minutes. At work you pose a question like this yourself, before a stakeholder asks
it.

On the warehouse's orders and payments, pose one question the day did not ask, in a stakeholder's
words, and answer it with a join. Above the query, write the count reconciliation as a comment block:
rows in, rows out, and the difference named. "Collected for Q1" is the practice lab's problem and
does not count. Choose a question where the join type is a choice you have to defend, such as a
question about paid orders only, or about payments with no order.

---

## Part 3. Can you work the three join lessons without help?

Allow about 20 minutes, and work the three SQLBolt join lessons in order:

- Lesson 6, joins: https://sqlbolt.com/lesson/select_queries_with_joins (checked 30 Sep 2026)
- Lesson 7, outer joins: https://sqlbolt.com/lesson/select_queries_with_outer_joins (checked 30 Sep 2026)
- Lesson 8, NULLs: https://sqlbolt.com/lesson/select_queries_with_nulls (checked 30 Sep 2026)

If you finish early, work the first three problems in the joins category of PostgreSQL Exercises,
https://pgexercises.com/questions/joins/ (checked 30 Sep 2026).

---

## Part 4. When is an INNER join the honest choice?

At the top of your SQL file, write one comment line on when an INNER join is the honest choice.

---

## Part 5. What did the lab not reach?

Do this part only if the practice lab ran out of time. Work in this order, and stop when you have
spent an hour:

1. The escalated case, parts 3 to 5, in `notebooks/C2_W02_D02_ex1_escalated_case_STUDENT.ipynb`, with
   its brief in `exercises/unguided/C2_W02_D02_escalated_STUDENT.md`.
2. The second case, in `notebooks/C2_W02_D02_ex2_second_case_STUDENT.ipynb`, alone if your pair has
   gone home.
3. The interview drill: the questions on the afternoon deck's slides D3 and D4, each answered aloud in
   sixty seconds and recorded on your phone. Play one back and cut whatever you would not say to Anand.

---

## Why is this hard to shortcut?

The book in Part 1 is new tonight, so no assistant has seen its numbers, and your report either
matches the self-check or it does not. The lists in step 5 and the action in step 7 are
choices with reasons, and a reason that could be written without running the queries reads that way
at once. Part 2 is a question you chose, and tomorrow the room asks you why that join.

---

## What do you bring tomorrow?

| Part | What to bring |
|---|---|
| 1 | The SQL file, run from a fresh connection, every check true, with your lists and your sentence to Anand |
| 2 | Your question, its query and its reconciliation block |
| 3 | The SQLBolt lessons finished |
| 4 | Your one line |

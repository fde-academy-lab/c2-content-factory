# Take-home: the question Anand's analyst asks next

Four parts, about two hours in all. Part 1 is the day's method on a question the room never asked.
Part 2 is two queries of your own, which is what the analyst will ask you to talk through. Part 3 is
ten minutes from memory, and Part 4 is the practice the row sets for tonight.

Tomorrow opens by running one learner's Part 1 file unchanged on the projector.

> "Business moved the rupees and Retail-Plus lost the orders. Fine. Where in Retail-Plus, city by
> city? My regional heads will ask before I have finished the sentence." Anand's analyst, replying
> to the Monday suite

---

## Part 1. The Retail-Plus tree by city, about an hour

The segment lives on the customer, and so does the city. Work in
`sql/C2_W02_D01_06_takehome_STUDENT.sql`, under its comment lines.

1. Write the Retail-Plus tree per city for each quarter as two CTEs, one per quarter, lined up on
   city: buyers, orders, orders per buyer divided in numeric, and revenue.
2. Add the change in revenue, in rupees and in percent, and order the result by the change in
   rupees, largest fall first.
3. Add a column, or a second query with `HAVING`, that flags every city-quarter holding fewer than
   30 orders.
4. Check that the six cities add back to the Retail-Plus totals you computed today, in both
   quarters, and write the check as its own query.

Then write two sentences in a comment at the end of the file: which city carries the largest part of
the fall and through which branch, and whether the city split is a finding you would put on Anand's
sheet or a lead for his regional heads, with the threshold that decided it.

---

## Part 2. Two queries of your own, about thirty minutes

Write two more extraction queries on questions Anand's analyst might ask about the book, each with
one comment line stating the question, the reading of revenue and the denominator. They must run
unchanged on the warehouse and use nothing beyond today's clauses. One of them must use a CTE.

For each, write one line saying which of today's four traps it could have fallen into and how the
query avoids it.

---

## Part 3. The run order from memory, about ten minutes

At the top of your file, write the logical order of FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY
and LIMIT in a comment, from memory, then one line saying why `WHERE count(*) > 5` is refused.

---

## Part 4. Practice, about twenty minutes

SQLBolt, lessons 1 to 5, interactive, https://sqlbolt.com/ (verified 29 Sep 2026)

Lesson 4 is "Filtering and sorting Query results" and covers `ORDER BY`, `LIMIT` and `OFFSET`. Answer
in one line at the end of your file: which exercise in lessons 1 to 5 would have returned a
different answer if its `ORDER BY` were removed, and why.

---

## What makes this hard to shortcut

Part 1 runs on Kalpa's warehouse, which no assistant has seen, and its numbers either match the
self-check or they do not. Part 1's last sentence is a defended choice with a threshold: the city
cells are small, and a note that never counts their orders shows it. Part 2's queries are yours
and are run unchanged in front of the room, and Part 4 asks about a specific exercise on a named
page.

---

## What to bring tomorrow

| Part | What to bring |
|---|---|
| 1 | The .sql file, which runs top to bottom unchanged, and your two sentences |
| 2 | The two queries, their comment lines and the trap each one avoids |
| 3 | The run order from memory, at the top of the file |
| 4 | Your one line on SQLBolt |

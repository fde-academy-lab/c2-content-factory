# Solutions: pick the tool

Answers: 1b 2c 3a 4d 5c

## Q1. SQL in the warehouse

Owned by the warehouse, needed indefinitely, read by an auditor who will not have you beside him.
All three answers point the same way. The comment line stating the question and the denominator is
what makes it auditable.

## Q2. pandas in a notebook

Owned by you, needed until Friday, read by nobody but you. A notebook is exactly right here, and
somebody reaching for SQL because it is the source of truth has answered a question nobody asked.

Worth noticing: the same tool is correct in Q2 and refused in Q5, on the same three questions.
The tool is not good or bad; the answers to the three questions changed.

## Q3. Plain Python

The room has never seen a loop, so the point is that every step is visible. `groupby` in one line
teaches nothing about how a total is built, and the fact that it is shorter is the reason it is
wrong here.

## Q4. pandas, from the warehouse, in one run

This is the interesting one, and it is why the brief asks you to compare it with Q1.

Both are weekly and both read from the warehouse. The difference is who reads the output and what
they do with it. Anand's analyst audits a number and needs the query. Marketing's analysts build
on a table and need it in the language they work in.

Option a is defensible and it loses on the last of the three questions. The warehouse could own
this table, and the people who use it could not read the definition.

## Q5. Refuse, on audit

A notebook has no audit trail a controller can read, no guarantee it was run against current data,
and a cell edited at 4 pm looks identical to one nobody touched.

Option b is the near-miss: committing the notebook fixes the version history and fixes none of the
other three problems. Option d is wrong on the facts, and reaching for a technical objection when
the real objection is procedural is a tell worth noticing in yourself.

# Take-home: two questions Anand's analyst would ask next

## The situation

Your Monday suite is written and it answers what Anand asked. His analyst will read it, and an
analyst who reads six queries always leaves with two more questions. Your job tonight is to guess
which two, and answer them before they are asked.

## What to hand in

One `.sql` file holding two queries you wrote yourself, neither of which is in the suite.

Each query carries a comment block above it with four lines and no more:

```sql
-- Question:    the question in a stakeholder's words, not in SQL words
-- Denominator: what the number is divided by, and what that excludes
-- Answer:      the number this returned when you ran it
-- Caveat:      the one thing that would make this number wrong
```

Then, separately, a short note of four or five sentences: which of the two you would put in front
of Anand first, and why the other one waits.

## Constraints that make this yours

The two questions must be answerable from `orders` and `customers` alone. The payments table
arrives tomorrow and is out of scope tonight.

Neither question may be one of the six in the suite, and neither may be a suite query with a
different filter. "Revenue per channel for Q1 only" is query three with a `WHERE`, and it does not
count.

At least one of the two must be a question where the **denominator** is the interesting part.
Last week's Student segment is the shape of what is meant: a rate that looks impressive until you
see how few observations sit under it.

## The self-check

Work through `C2_W02_D01_selfcheck_STUDENT.md` before you hand this in. It does not check your
SQL. It checks whether your caveat line is doing any work.

## Why this is not a typing exercise

Anybody can write a query that runs. The four comment lines are the deliverable, and the caveat
line is the one that separates an analyst from a person with database access. A caveat that says
"the data might be wrong" is not a caveat. A caveat that says "this counts orders rather than
customers, so one buyer placing forty orders looks like forty buyers" is one.

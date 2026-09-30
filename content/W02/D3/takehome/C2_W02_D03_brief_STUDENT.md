# Take-home: the same three questions on a warehouse nobody has queried

Three parts, about two hours in all. Part 1 runs the day's three rounds on a second sample of the
Kalpa warehouse with a new ask, so nothing from the morning can be pasted across. Part 2 is a
ranking question of your own and the GROUP BY query that pretends to answer it. Part 3 is three
short problems on PostgreSQL Exercises.

Thursday opens by walking one learner's Part 1 in front of the room, starting from their row
counts, so bring the counts as well as the queries.

---

## Before you start: load the sample, about five minutes

The sample has the warehouse's shape (customers, orders and the plan line) and none of its headline
numbers: its order count, its Q2 total, its plan line and where Q2 closes against plan are its own.
It loads into its own schema, `takehome`, so the warehouse you used today stays as it was. From the
repository root, in the Codespace terminal:

```
psql -d kalpa -f content/W02/D3/data/C2_W02_D03_takehome_STUDENT.sql
```

Query it as `takehome.orders`, `takehome.customers` and `takehome.plan_line`, or run
`SET search_path = takehome;` at the top of your file. Work in one `.sql` file of your own, and under
every query paste the result it returned as a comment. That pasted output is part of what you bring.

Q2 revenue per member means what it meant today: the booked amount of the member's Q2 orders in
every status, the definition Monday's suite used for the quarter total.

---

## Part 1. Marketing's second list, about seventy-five minutes

Marketing has read today's protect list and now wants a smaller one for the tier below:

> "Run the same exercise for Retail-Core on the new extract. We can only call twenty members this
> month, so give us the top twenty Retail-Core members by Q2 revenue, with ties ranked the same the
> way the head of Retail-Plus wanted, and tell us how many that is. Flag anyone on the list whose
> monthly spend has fallen two months running. And put the running total against the plan line in
> front of Meera again, from this extract."

1. **Check the base first.** Count the Q2 orders, the Q2 total and the Retail-Core Q2 buyers. Write
   one comment line saying which number the running total in step 5 must close on.
2. **The list under four rules.** Rank Retail-Core by Q2 revenue with ROW_NUMBER, RANK and
   DENSE_RANK in one query, filter in a CTE, and count what a top twenty ships under each, plus
   "whole ties only", the rule that keeps a tie only when all of it fits. Then read the rows either
   side of position twenty with all three functions side by side.
3. **Your rule, defended.** Choose the rule you would ship and write two comment lines: the count it
   ships and why, in words Marketing can repeat, and what the rule you rejected would have done to a
   member at the line. If your chosen count differs from twenty, the sentence must say why in the
   same line.
4. **The falling-spend flag.** Build one row per member per month. Flag a member whose September
   spend is below August's and August's below July's, three ways, and count each across the whole
   book before you apply it to your list:
   - LAG with no PARTITION BY, and a second count of flagged rows whose row two back belongs to
     another member;
   - LAG with PARTITION BY customer_id, and a second count of flagged rows whose previous two rows
     are not August and July;
   - the flag that requires the previous two rows to be August and July.

   Then count how many members on your list carry the last flag. Write one comment line for the
   member on your list who says he was on holiday: what your definition does with a month in which
   he placed no order, and why you did not fill that month with zero.
5. **The running total against plan.** Accumulate Q2 booked revenue by day with an order that
   cannot tie, accumulate the plan line, and read booked to date against plan to date at the last
   day of each plan week. Read two lines aloud to yourself: where Q2 stood at the end of the seventh
   plan week, and where it closed. Then check that the last booked-to-date equals the Q2 total from
   step 1. If it does not, find the rupees that went missing before you write anything else.
6. **Three sentences to Marketing and Meera**, as a comment: the tie rule and the count it ships,
   how many listed members carry the flag and what it means for a member with a month off, and where
   Q2 stood against plan at mid-quarter and at the close.

---

## Part 2. A ranking question of your own, about thirty minutes

1. **Recap first, from memory, before you run anything.** In a comment, write what ROW_NUMBER, RANK
   and DENSE_RANK return for five members whose spend is Rs 9,000, Rs 8,000, Rs 8,000, Rs 8,000 and
   Rs 6,000, sorted from the largest. Then run the three functions on those five invented values and
   write one line on anything you got wrong.
2. **Build.** Write one ranking question of your own on the `takehome` schema, a question a Kalpa
   stakeholder would actually ask (for example, a member's best month, the top three per channel or
   the largest order per city), and answer it with a window function.
3. **Its GROUP BY impostor.** Write the GROUP BY query a hurried analyst would send for the same
   question, run both, and write a comment of two or three sentences on why they differ, naming the
   rows the impostor loses or the question it answers instead.

---

## Part 3. PostgreSQL Exercises, about twenty minutes

The site has no separate window functions category; its window questions sit in the Aggregation
category. Do the first three, each on the site's own database in the browser:

- Produce a list of members with a count of all members on every row: https://pgexercises.com/questions/aggregates/countmembers.html (verified 29 Sep 2026)
- Produce a numbered list of members: https://pgexercises.com/questions/aggregates/nummembers.html (verified 29 Sep 2026)
- Output the facility id that has the most slots booked, with every tied result: https://pgexercises.com/questions/aggregates/fachours4.html (verified 29 Sep 2026)

Solve each before you open the site's answer. Then write one line per problem: the window clause
your answer used. For the third, add which of today's three functions the site's answer uses to keep
every tied facility, whether DENSE_RANK would have returned the same rows at position one, and why
ROW_NUMBER would have failed the question.

---

## What makes this hard to shortcut

Part 1 runs on a sample no assistant has seen, and its counts either match the self-check or they
do not; the pasted outputs show which query produced which number. Part 2 starts from your own
memory and ends on your own question, and Part 3 asks what one specific answer on the site does.

---

## What to bring on Thursday

| Part | What to bring |
|---|---|
| 1 | Your `.sql` file with every result pasted under its query, and your three sentences |
| 2 | The recap comment with the line on what you got wrong, and your question with its impostor and the comment on why they differ |
| 3 | Your three lines on the PostgreSQL Exercises problems |

`takehome/C2_W02_D03_selfcheck_STUDENT.md` tells you whether each Part 1 number is right.

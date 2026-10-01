# Which twenty Retail-Core members does Marketing ring this month, who among them is slipping, and where does a new extract's Q2 stand against plan?

Take-home for Week 2, Wednesday. About two and three quarter hours in all: Marketing's second list
on a sample nobody has queried (about seventy-five minutes), a ranking question of your own (thirty
minutes), the second case (forty minutes, in pairs or alone), and three PostgreSQL Exercises problems
(twenty minutes). The self-check, `takehome/C2_W02_D03_selfcheck_STUDENT.md`, lists the numbers to
reach; open it only after each part is done. Thursday opens by walking one learner's first part in
front of the room, starting from their row counts, so bring the counts as well as the queries.

> "Run the same exercise for Retail-Core on the new extract. We can only call twenty members this
> month, so give us the top twenty Retail-Core members by Q2 revenue, with ties ranked the same the
> way the head of Retail-Plus wanted, and tell us how many that is. Flag anyone on the list whose
> monthly spend has fallen two months running. And put the running total against the plan line in
> front of Meera again, from this extract."
> The marketing lead, Kalpa Retail

**Who needs the answer.** The marketing lead's member team rings the members on this list with a
retention offer, twenty calls this month. A list that drops a member at the line by a coin toss, or
names more members than it says, spends the calls badly, and a flag that reads a holiday as a fall
rings a loyal member to tell him he is drifting. Meera Raghavan, Kalpa Retail's CEO, reads the plan
line to decide whether the quarter needs action.

**The questions on the way.**
1. How many Q2 orders, rupees and Retail-Core buyers does the sample hold?
2. How many members does each tie rule put on a top twenty?
3. Which rule do you ship, and what do you tell Marketing about its count?
4. Whose spend fell two months running, read three ways?
5. Where does this extract's Q2 stand against its plan line, at mid-quarter and at the close?
6. What three sentences go to Marketing and Meera?
7. What ranking question would a Kalpa stakeholder ask, and what does its GROUP BY impostor return?
8. Should Retail-Core's protect list rank members by how often they ordered in Q2?
9. Which window clauses do three PostgreSQL Exercises problems need?

## What is the second sample, and how do you load it?

The sample is a second extract of a Kalpa Retail warehouse, built for this take-home. It has the
shape you queried today and none of its numbers: its order count, its Q2 total, its plan line and
where its Q2 closes against plan are its own, so nothing from the day can be pasted across. Q2 is July
to September 2026. Q2 revenue per member means what it meant today: the booked amount of the
member's Q2 orders, every order at its amount whatever its status. Kalpa Retail sells to four
segments: Business (corporate buyers), Retail-Core (everyday shoppers), Retail-Plus (the paid
membership tier) and Student. Monthly spend is a member's booked revenue in one calendar month.

Load it once, from the repository's root in your Codespace's terminal:

```
psql -d kalpa -f content/W02/D3/data/C2_W02_D03_takehome_STUDENT.sql
```

It creates a schema named `takehome`, a named area of the warehouse of its own, and leaves the
warehouse you used today exactly as it was. Write every table name with the schema in front of it, or
run `SET search_path = takehome;` at the top of your file.

| Table | One row per | Columns |
|---|---|---|
| `takehome.orders` | order | order_id, customer_id, order_date, quarter, channel, amount (rupees), status |
| `takehome.customers` | member | customer_id, segment, city, country, joined_date |
| `takehome.plan_line` | plan week | week_start, the Monday it starts, and plan_revenue |

Work in one `.sql` file of your own, each query under a comment line that states its question, and
paste the result each query returned as a comment beneath it. That pasted output is part of what you
bring.

## 1. How many Q2 orders, rupees and Retail-Core buyers does the sample hold?

Where this is used at work: every ranked list and every running total is checked against the base it
was built from, so the base is counted first.

Count the Q2 orders, the Q2 total and the Retail-Core members who placed a Q2 order. Write one comment
line saying which of these numbers your running total in section 5 must close on.

## 2. How many members does each tie rule put on a top twenty?

Where this is used at work: a list cut at a number says how many it ships and why, before a manager
asks.

Rank Retail-Core's members by Q2 revenue with ROW_NUMBER, RANK and DENSE_RANK in one query, compute
the places in a named step, and count what a top twenty ships under each, plus "whole ties only", the
rule that keeps a tie only when all of it fits. `count(*) OVER (PARTITION BY q2_revenue)` gives each
member the number who share their figure, so `rank + tied_with - 1` is the last place a tie reaches.
Then read the members either side of twentieth place with all three functions side by side.

## 3. Which rule do you ship, and what do you tell Marketing about its count?

Where this is used at work: a tie rule is a business decision, and the person who owns the list has
to be able to repeat the reason.

Choose the rule you would ship and write two comment lines: the count it ships and why, in words
Marketing can repeat, and what the rule you rejected would have done to a member at the line. If your
count differs from twenty, the same line says why. Marketing said twenty calls this month: write a
third line on whether that budget is a hard cap, and if it is, which tiebreaker you would state in
advance and why it is a business reason.

## 4. Whose spend fell two months running, read three ways?

Where this is used at work: a retention call goes to a customer whose own history shows the drift, and
the definition of the drift is written down before the first call.

Build one row per member per month. Flag a member whose September spend is below August's and August's
below July's, three ways, and count each across the whole book before you apply it to your list:

- LAG with no PARTITION BY, with a second count of the flags whose row two back belongs to another
  member;
- LAG with PARTITION BY customer_id, with a second count of the flags whose two rows before September
  are not August and July;
- the flag that requires the two rows before September to be August and July.

Then count how many members on your list carry the last flag. Write one comment line for a member on
your list who says he was on holiday in August: what your definition does with a month in which he
placed no order, and why you did not fill that month with zero.

## 5. Where does this extract's Q2 stand against its plan line, at mid-quarter and at the close?

Where this is used at work: a CEO reads the quarter while it runs, so the to-date figure has to be
complete before anyone says ahead or behind.

Accumulate Q2 booked revenue and the plan line, and read booked to date against plan to date at the end
of each plan week. Read two lines to yourself: where Q2 stood at the end of the seventh plan week, and
where it closed. Then check that the last booked to date equals the Q2 total from section 1; if it
does not, find the rupees that went missing before you write anything else. Last, count how many of
the full plan weeks booked below their own week's plan.

## 6. What three sentences go to Marketing and Meera?

Where this is used at work: the sentence a stakeholder carries into a meeting is the part of the
analysis most people read.

As a comment, three sentences: the tie rule and the count it ships; how many listed members carry the
flag and what it means for a member with a month off; and where Q2 stood against plan at mid-quarter
and at the close, by its total and by its weekly run.

## 7. What ranking question would a Kalpa stakeholder ask, and what does its GROUP BY impostor return?

Where this is used at work: an analyst who can name the question GROUP BY cannot answer chooses the
right tool before writing any SQL.

1. **From memory first, before you run anything.** In a comment, write what ROW_NUMBER, RANK and
   DENSE_RANK return for five invented members whose spend is Rs 9,000, Rs 8,000, Rs 8,000, Rs 8,000
   and Rs 6,000, sorted from the largest. Then run the three functions on those five values and write
   one line on anything you got wrong.
2. **Build.** Write one ranking question of your own on the `takehome` schema, one a Kalpa stakeholder
   would ask in those words, such as a member's best month, the top three members per channel, or the
   largest order per city, and answer it with a window function.
3. **Its GROUP BY impostor.** Write the GROUP BY query a hurried analyst would send for the same
   question, run both, and write two or three sentences on why they differ, naming the rows the
   impostor loses or the question it answers instead.

## 8. Should Retail-Core's protect list rank members by how often they ordered in Q2?

Where this is used at work: before a team argues over two definitions of "best customer", it measures
how much the answer changes.

This is the day's second case, on the day's own warehouse, forty minutes in pairs or alone. The brief,
`exercises/unguided/C2_W02_D03_second_case_STUDENT.md`, carries the marketing lead's ask, the data and
every definition; you work in `notebooks/C2_W02_D03_ex2_second_case_STUDENT.ipynb`, whose seven
lettered markers are the brief's first seven items. Post your ten letters with your partner's name.

## 9. Which window clauses do three PostgreSQL Exercises problems need?

Where this is used at work: reading somebody else's correct answer and saying why it works is half of
reviewing a colleague's query.

PostgreSQL Exercises has no separate window functions category; its window questions sit in the
Aggregation category. Do these three on the site's own database in the browser, each before you open
the site's answer:

- Produce a list of member names, with each row containing the total member count:
  https://pgexercises.com/questions/aggregates/countmembers.html (checked 1 October 2026)
- Produce a numbered list of members, ordered by their date of joining:
  https://pgexercises.com/questions/aggregates/nummembers.html (checked 1 October 2026)
- Output the facility id that has the highest number of slots booked, with every tied result output:
  https://pgexercises.com/questions/aggregates/fachours4.html (checked 1 October 2026)

Then write one line per problem: the window clause your answer used. For the third, add which of
today's functions the site's answer uses to keep every tied facility, whether DENSE_RANK would have
returned the same rows at the top, and what ROW_NUMBER would have done to a facility that tied for
the most slots.

## What makes this hard to shortcut?

The first six sections run on a sample no assistant has seen, and their counts either match the
self-check or they do not; the pasted outputs show which query produced which number. Section 7
starts from your own memory and ends on your own question, section 8 is checked by its notebook, and
section 9 asks what one specific answer on the site does.

## What do you bring on Thursday?

| Section | What to bring |
|---|---|
| 1 to 6 | Your `.sql` file with every result pasted under its query, your rule and its reason, and your three sentences |
| 7 | The recap comment with the line on what you got wrong, and your question with its impostor and why they differ |
| 8 | Your ten letters, posted with your partner's name |
| 9 | Your three lines on the PostgreSQL Exercises problems |

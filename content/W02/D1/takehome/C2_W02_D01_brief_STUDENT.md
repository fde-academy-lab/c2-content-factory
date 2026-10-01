# What does Kalpa Retail East's first Monday suite say, and does every number on it hold up?

Take-home for Week 2, Monday. About two and a half hours in all: the east book's suite (about an
hour), two queries of your own (twenty minutes), the second case (forty minutes, in pairs or alone),
the order a query runs in from memory (ten minutes) and the practice the row sets for tonight
(thirty minutes). The self-check, `takehome/C2_W02_D01_selfcheck_STUDENT.md`, lists the numbers to
reach; open it only after each part is done.

> "East's book lands in the warehouse this week, beside the national one. Run the Monday suite on it
> before its first Monday, and send me the numbers my analyst will audit, with the checks that prove
> them."
> Anand Iyer, finance controller, Kalpa Retail

**Who needs the answer.** Anand signs East's first Monday sheet, and his analyst reruns every query
behind it. A number that does not hold up on its first Monday makes every later East number suspect,
and the regional team's budget for the next half-year is set from this sheet.

**The questions on the way.**
1. How many orders, rupees and customers did East book in each quarter?
2. How often did each segment's customers order, and which groups are too thin to quote a rate on?
3. How much less did each Retail-Plus member spend, over the same members in both quarters?
4. Do East's numbers add up the way the analyst will add them?
5. Which five orders will the analyst trace, and what does the run print beside them?
6. Which two more questions would the analyst ask?
7. Is the store booming and the web collapsing, as Marketing says?
8. In what order does a query run, written from memory?
9. Where do you practise tonight?

## What is Kalpa Retail East, and how do you load its book?

Kalpa Retail East is invented for this take-home: three cities, Kolkata, Bhubaneswar and Guwahati,
selling to the same four segments as the national book. Business is corporate buyers, whose orders
run to lakhs; Retail-Core is everyday shoppers; Retail-Plus is the paid membership tier; Student is
the student segment. Q1 is April to June 2026 and Q2 is July to September 2026, and revenue is
booked revenue: every order at its amount, whatever its status.

Load the book once, from the repository's root in your Codespace's terminal:

```
psql -d kalpa -f content/W02/D1/data/C2_W02_D01_takehome_STUDENT.sql
```

It creates a schema named `takehome`, a named area of the warehouse of its own, holding two tables,
and leaves the national tables exactly as they were. Write every table name with the schema in
front of it:

| Table | One row per | Columns |
|---|---|---|
| `takehome.orders` | order | order_id, customer_id, order_date, quarter, channel (app, web or store), amount (rupees), status (delivered, returned or cancelled) |
| `takehome.customers` | member | customer_id, segment, city, joined_date |

The segment lives on the customer, so a query that needs it looks it up with one line,
`JOIN takehome.customers c USING (customer_id)`, exactly as the day's chapters did: each order has one
customer, so the lookup changes no row count. Write every query of this take-home in a `.sql` file
of your own, each under a comment line that states its question, its definition and its
denominator, the way Anand's analyst will read it.

## 1. How many orders, rupees and customers did East book in each quarter?

Where this is used at work: every Monday sheet opens on the book's own totals, and the analyst
checks them first.

Write one query that returns, per quarter, the orders, the booked revenue and the customers who
bought, each customer counted once. Then say in one comment line which way revenue and customers
each moved from Q1 to Q2, with the percent.

## 2. How often did each segment's customers order, and which groups are too thin?

Where this is used at work: a per-segment rate is the line a business head reads first, and a rate
on a handful of customers is the line that misleads them most.

1. Write one grouped query that returns, per segment and quarter, the orders, the customers who
   bought and the orders per customer, rounded on purpose to two places, with the counts in the
   same row so the analyst can multiply the ratio back.
2. Write a second query that lists only the segment-quarters with fewer than 30 customers who
   bought, the rule Kavya Nair, the team's senior analyst, set in Week 1 for flagging a rate.
3. In a comment, name the segment whose orders per customer fell furthest, with its two ratios, and
   say which rates on the sheet carry the thin-group flag.

## 3. How much less did each Retail-Plus member spend, over the same members?

Where this is used at work: the head of a membership tier asks what each member is worth now, and
the answer has to count the members who stopped buying.

Build one row per Retail-Plus member who bought in either quarter, with the member's Q1 spend and
Q2 spend, and average each column so that both averages cover the same members. Beside the two
averages, return the count of members inside each one. In a comment, give the change in percent and
check it against the change in Retail-Plus's revenue over the same two quarters.

## 4. Do East's numbers add up the way the analyst will add them?

Where this is used at work: an auditor adds a report's rows before reading any of its queries, and
one impossible total is enough to send the whole report back.

1. Show, as one query of named steps (`WITH ... AS`), that the four segments' customers add back to
   the book's customers in each quarter.
2. Produce the half-year column, April to September 2026: customers who bought, orders and rupees
   per segment. Put the customer table's members per segment beside it.
3. **A design choice.** Three ways could fill that half-year column: add each segment's two quarter
   rows in a last step; count the half-year from the orders with the quarters' own definition; or
   return the quarters and the half-year from one query with `GROUP BY GROUPING SETS`. Size each on
   East's book by the rows it reads and by what it assumes, choose one for Anand's sheet, and name
   the fact that would switch your choice. Then reach Retail-Plus's half-year customers a second
   way that does not count the half-year directly, and show the two routes agree.

## 5. Which five orders will the analyst trace, and what does the run print beside them?

Where this is used at work: whenever an auditor traces a sample of orders and reruns the query the
next week, and a fingerprint beside the numbers tells a changed book from a changed query.

1. Return five delivered Q2 web orders for the analyst to trace against the ERP, the system Finance
   books orders in, so that every run returns the same five.
2. Run the same request without its `ORDER BY` and compare the five you get.
3. Return East's fingerprint: its order rows, its rupees, its distinct customers and its latest
   order date, one row.

## 6. Which two more questions would the analyst ask?

Where this is used at work: the analyst's follow-up questions arrive the day after the sheet does,
and the ones you have already answered are the ones that build trust.

Write two more extraction queries on East's book, on questions Anand's analyst might ask. Put one
comment line above each stating the question, the reading of revenue (booked or delivered) and the
denominator. Each must run unchanged and use nothing beyond the day's clauses, and one of them must
use named steps.

## 7. Is the store booming and the web collapsing, as Marketing says?

Where this is used at work: whenever a channel's budget is about to move on the strength of its
total.

This is the day's second case, on the national warehouse, in pairs or alone. Its brief is
`exercises/unguided/C2_W02_D01_second_case_STUDENT.md` and its notebook
`notebooks/C2_W02_D01_ex2_second_case_STUDENT.ipynb`; the brief is sat from its own page and ends on
the line you send Anand.

## 8. In what order does a query run, written from memory?

Where this is used at work: the `GROUP BY` refusal, the choice between `WHERE` and `HAVING`, and an
unsorted `LIMIT` all follow from this order, and a reviewer asks for it.

At the top of your `.sql` file, as a comment, write from memory the order in which the database runs
a query's clauses, from the table it reads to the rows it cuts, with one line per clause on what it
does. Then, under it, write one sentence on why `SELECT` cannot print a column the groups do not
pin down.

## 9. Where do you practise tonight?

Where this is used at work: today's interview drill opens on these clauses, tagged [S], asked
everywhere.

SQLBolt's interactive lessons 1 to 4 (SELECT, filtering and sorting), the review page after them,
and lesson 12 on the order of execution: https://sqlbolt.com/ (checked 30 September 2026). The
lessons run in the browser, and every query you write for Kalpa still runs on Postgres.

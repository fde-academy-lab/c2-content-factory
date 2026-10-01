# Which answers hold in the second case on one number in three tools and the note, and why?

Answers: 1b 2b 3a 4d 5d 6c

Kavya Nair, the senior analyst, asked the pair to compute Week 1's branch that moved, Retail-Plus
orders per member in Q1 (April to June 2026) against Q2 (July to September), in plain Python, SQL and
pandas, and to write a tool-choice note: which tool owns which job, and which tool the pair would
refuse for Finance's numbers. Orders per member is a quarter's orders over the members who ordered in
it. Anand Iyer's analyst in Finance reruns every number Finance receives from the warehouse. The
executed solution, `C2_W02_D04_ex2_second_case_solution_STUDENT.ipynb` in this folder, runs every
key. Two of the six items are design items: 5 and 6.

**Who needs the answer.** The pair, before Kavya reads the note. A note whose numbers disagree, or
whose sizing ties every tool, gives her nothing to sign.

**The questions on the way.**

- Which idea does the second case test?
- Which numbers should the pair have reached?
- Why does each of the six keys hold, from the members in a quarter to Finance's number?
- What does a note Kavya would sign look like?
- Where does one question in many tools come up at work?

## Which idea does the second case test?

The three tools agree once they share a definition, so the choice between them rests on two facts
about the job: who has to trust, rerun or audit the number, and how many rows each route fetched to
reach it.

## Which numbers should the pair have reached?

| Quarter | Orders | Members who ordered | Orders per member |
|---|---|---|---|
| Q1 | 215 | 91 | 2.363 |
| Q2 | 140 | 76 | 1.842 |

Retail-Plus members ordered 22 percent less often in Q2, in all three tools to three decimal places:
the frequency branch Week 1 found. The rows each route fetched from the warehouse: plain Python 355,
the Retail-Plus orders; SQL 2, its answer; pandas 1,000, every order, before it kept Retail-Plus.

## Why does each of the six keys hold, from the members in a quarter to Finance's number?

### Q1. How many members ordered in each quarter?

The key is b, `{qq: len(set(ids[qq])) for qq in ids}`. A set keeps each customer id once however
many times they ordered in the quarter, so the counts are 91 and 76.

- a, `len(ids[qq])`: counts every order as a member, so orders per member reads 1.000 in both
  quarters, rows counted as customers.
- c, the union of both quarters: divides each quarter by the 107 members who ordered in either, so
  each rate stands on members who did not order in that quarter.
- d, the intersection of both quarters: divides by the 60 who ordered in both, and SQL, which counts
  each quarter's members on their own, disagrees in the next step.

### Q2. Which expression gives orders per member, to three places?

The key is b, `orders::numeric / members`. One side cast to `numeric` makes Postgres divide as
decimals.

- a, `orders / members`: Postgres divides two whole numbers as whole numbers and returns 2 and 1,
  Monday's trap.
- c, `members::numeric / orders`: the rate upside down, members per order.
- d, `orders::numeric / (SELECT count(*) FROM customers)`: divides by all 340 customers on the list,
  every segment, whoever ordered.

### Q3. Which line keeps only Retail-Plus?

The key is a, `WHERE c.segment = 'Retail-Plus'`, which filters the rows before they are grouped.

- b, `WHERE c.segment = 'Retail Plus'`: the warehouse stores the segment with a hyphen, so the
  spelling with a space matches no row and the query returns no quarters at all.
- c, `WHERE c.segment LIKE 'Retail%'`: matches Retail-Core as well, both consumer tiers.
- d, `WHERE c.segment <> 'Business'`: keeps Retail-Core and the Students as well.

### Q4. Which expression gives each quarter's members?

The key is d, `rp.groupby("quarter")["customer_id"].nunique()`, the count of distinct customer ids
in each quarter.

- a, `rp.groupby("quarter")["customer_id"].count()`: counts the rows, which are orders, so the rate
  reads 1.000.
- b, `rp.groupby("quarter").size()`: counts the rows as well.
- c, `rp.drop_duplicates("customer_id").groupby("quarter").size()`: keeps one row per member before
  grouping, so a member who ordered in both quarters counts in only one of them; the two quarters'
  members add up to the 107 who ordered at all, and each rate stands on too few members.

### Q5. Which size tells the three routes apart, listed as plain Python, SQL, pandas?

A design item. The key is d, the rows each route fetched from the warehouse: 355, 2 and 1,000. It
separates the three, and it grows with the orders table for two of them while SQL keeps sending its
answer. The pandas figure measures the route as it was written: it read every order and kept
Retail-Plus in memory, and a `read_sql` with the `WHERE` in its query would have fetched 355, like
plain Python.

- a, the rows in each answer: 2, 2 and 2, a tie that separates nothing.
- b, the orders each route counted: 355 three times, since all three counted the same orders.
- c, the rows each route held after keeping Retail-Plus: 355, 2 and 355, which hides the 645 other
  orders pandas fetched before its filter.

### Q6. Which route should own a number Finance reruns every Monday?

A design item. The key is c, "SQL", because it runs where the data lives. Finance's number lives
where Finance can rerun and audit it, and the query sends only its answer. Two separate facts point
the same way here: SQL is the route Anand's analyst can rerun without anyone's notebook, and on the
size chosen in Q5 it fetches the fewest rows. The check asks for the route the chosen size ranks
first, so a pair that sized the routes wrongly finds out at this step too.

- a, "pandas", since the growth team's table already holds the numbers: it runs on a copy, depends on
  the order its cells ran in, and Finance cannot rerun it without the analyst's environment.
- b, "plain Python", since an auditor can read every line: the loop is the route for a question
  explained once, line by line, and it runs on a copy on one machine.
- d, "a CSV export", since Finance opens every number in a spreadsheet: a copy that ages from the
  moment it is written, and the spreadsheet can read the warehouse's answer instead.

## What does a note Kavya would sign look like?

> Plain Python owns the one-off question someone must follow line by line, such as one member's
> orders for an auditor; today it fetched 355 rows.
> SQL owns every number Finance reruns, here orders per member by quarter, because it runs where the
> data lives and sends only its answer, 2 rows.
> pandas owns the analyst's iterative work, such as the growth team's table, reading what SQL
> computes; today it fetched 1,000 rows for a two-row answer.
> We refuse a pandas notebook for Finance's numbers: it fetches every order to one machine, depends
> on the order its cells ran in, and Anand's analyst cannot rerun it.

## Where does one question in many tools come up at work?

LinkedIn's Unified Metrics Platform page says that "multiple stakeholders come up with different
ways to calculate the same metric arriving at slightly different results", and that the platform now
"serves as the single source of truth for all business metrics at Linkedin" (LinkedIn Engineering,
Unified Metrics Platform, checked 1 Oct 2026). The pair's note does the same job for one team: each
number gets one owner, and every other copy is checked against it.

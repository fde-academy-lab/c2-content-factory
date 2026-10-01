# Which branch of each segment's tree moved, and how much less did each Retail-Plus member spend?

Chapter 4 set, six items. Items 1 and 2 run live in chapter 4's last minutes if the chapter ran to
time; items 3 to 6 are the practice lab's stretch or tonight's work.

> "I want these numbers every Monday, for every segment and channel, computed from the warehouse
> itself. No notebooks, no exports, nothing a person can mistype."
>
> Anand Iyer, finance controller, Kalpa Retail

Kalpa Retail's revenue tree splits a segment's revenue into three branches that multiply back to it:
customers who bought, orders per customer and revenue per order. Chapter 4 read each branch as its Q2
value over its Q1 value (Q1 is April to June 2026, Q2 is July to September 2026), so a ratio under 1
is a fall and the three ratios multiply back to the revenue ratio. Retail-Plus is Kalpa's paid
membership tier, with 120 members on the customers table. Spend per member is the rupees a Retail-Plus
member spent in a quarter, averaged over the members who bought in either quarter, so both quarters
are averaged over the same people. A query can be written three ways: nested subqueries, each written inside the next and read
from the inside out; named steps, a `WITH` query in which each step has a name and the next step reads
it, top to bottom in one statement; or temporary tables, which a session creates for its own use and
which vanish when the session ends. In a table with one row per member, a member with no order in a
quarter has an empty value, NULL, for that quarter's spend. `avg(x)` is SQL's average of a column,
`count(x)` counts a column's filled-in values, and `coalesce(x, 0)` writes 0 where x is empty.

| Segment | Customers who bought | Orders per customer | Revenue per order | Revenue |
|---|---|---|---|---|
| Business | 0.972 | 0.965 | 1.051 | 0.986 |
| Retail-Core | 0.941 | 1.030 | 1.012 | 0.982 |
| Retail-Plus | 0.835 | 0.780 | 1.084 | 0.706 |
| Student | 1.333 | 1.056 | 0.951 | 1.339 |

Each cell above is a branch's Q2 value over its Q1 value, from the book of 1,000 orders.

**Who needs the answer.** The head of Retail-Plus decides how hard to work to keep members, and
Anand's analyst reads the quarter comparison as one query, top to bottom. An average that quietly
leaves some members out tells her the tier is holding up when it is not.

**The questions on the way.**

- Which way of writing the comparison needs fewer edits when a column is renamed?
- How many times is a shared step computed each Monday, and when does a temporary table fit?
- Which branch pulled Business's revenue down most, and does its row check itself?
- What do two averages return on five invented members' Q2 spend?
- What explains a sheet that says Retail-Core customers spent more each while Retail-Core's revenue fell?
- Which route that never averages could confirm Retail-Plus spend per member?

**What you post.** One line of six letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxxx
```

---

## How should a query of several steps be written for an auditor?

Used at work whenever someone other than the author has to read, check and rerun a long query.

### Q1. Which way of writing the comparison needs fewer edits when a column is renamed?

Anand's analyst reruns the quarter comparison every Monday in a fresh session. Next month the platform
team will rename the segment column of the customers table from `segment` to `tier`. The comparison
can be written as version A, nested subqueries, or version B, named steps:

```sql
-- Version A, nested subqueries
SELECT q1.segment, q1.revenue AS q1_revenue, q2.revenue AS q2_revenue
FROM  (SELECT c.segment, sum(o.amount) AS revenue
       FROM orders o JOIN customers c USING (customer_id)
       WHERE o.quarter = 'Q1' GROUP BY c.segment) AS q1
JOIN  (SELECT c.segment, sum(o.amount) AS revenue
       FROM orders o JOIN customers c USING (customer_id)
       WHERE o.quarter = 'Q2' GROUP BY c.segment) AS q2 USING (segment);

-- Version B, named steps
WITH book AS (SELECT o.quarter, o.amount, c.segment
              FROM orders o JOIN customers c USING (customer_id)),
q1 AS (SELECT segment, sum(amount) AS revenue FROM book WHERE quarter = 'Q1' GROUP BY segment),
q2 AS (SELECT segment, sum(amount) AS revenue FROM book WHERE quarter = 'Q2' GROUP BY segment)
SELECT segment, q1.revenue AS q1_revenue, q2.revenue AS q2_revenue
FROM q1 JOIN q2 USING (segment);
```

In version B, `book` keeps the column's name for the steps after it, so `c.tier AS segment` in that one
step would leave them as they are. Counting the places that name the customers table's column, how
many must change in each version, and which way fits?

a) Named steps: 1 place against the nested version's 4, and each one reruns whole in a fresh session
b) Nested subqueries: 2 places, one per subquery, against named steps' 4, so nested is easier to keep
c) Named steps: 4 places, since every later step names the segment, against the nested version's 2
d) Temporary tables: 1 place, in the first table, and nothing to rebuild when the analyst opens a fresh session

### Q2. How many times is a shared step computed each Monday, and when does a temporary table fit?

The scale in this item is invented. The platform lead plans to run the suite on the group's whole
book of 2 crore orders, and twelve queries in one Monday session will each start from the same step,
every order joined to its segment. With named steps, each query carries the step in its own `WITH`;
with a temporary table, the session builds the step once and the twelve queries read it. How many
times is the step computed each Monday under each way, and which way fits then?

a) Once with named steps, since Postgres computes a WITH step only once, and 12 times with temporary tables
b) 12 times either way, since a temporary table is rebuilt for every query that reads it
c) 12 times with named steps and once with a temporary table, so the temporary table fits a step this large
d) Once either way, so named steps still fit, and they write nothing into the warehouse

## Which branch of the tree moved?

Used at work whenever a change in revenue has to be traced to customers, frequency or basket size.

### Q3. Which branch pulled Business's revenue down most, and does its row check itself?

Business's revenue ratio is 0.986, a fall of 1.4 percent. Reading the Business row of the table at the
top of this set, which branch pulled its revenue down most, and does the row check itself?

a) Orders per customer, at 0.965, and the three branches multiply back to its 0.986
b) Customers who bought, at 0.972, since fewer buyers always hurt revenue the most
c) Revenue per order, at 1.051, since it moved furthest from 1 of the three branches
d) None of them, since a revenue ratio of 0.986 sits too close to 1 to read any branch

## What does a per-member average say?

Used at work whenever a per-member or per-user average goes on a sheet beside last quarter's.

### Q4. What do two averages return on five invented members' Q2 spend?

Every number in this item is invented. Five Retail-Plus members' Q2 spend, one row each, reads
Rs 800, NULL, Rs 1,200, NULL and Rs 500, where NULL stands for a member with no Q2 order. What do
`avg(q2_spend)` and `avg(coalesce(q2_spend, 0))` return?

a) Rs 500 and Rs 500
b) Rs 833 and Rs 833
c) Rs 500 and Rs 833
d) Rs 833 and Rs 500

### Q5. What explains a sheet that says Retail-Core customers spent more each while Retail-Core's revenue fell?

A hurried sheet took `avg` of each quarter's column in a table with one row per Retail-Core customer
who bought in the half-year, 131 customers. It says each customer spent Rs 3,658 in Q1 and Rs 3,815 in
Q2, up 4.3 percent, while Retail-Core's revenue fell 1.8 percent. Of the 131, 102 bought in Q1 and 96
in Q2. What explains the rise on the sheet?

a) Retail-Core's revenue per order rose 1.2 percent, and that lift reaches every customer's spend
b) The averages round to whole rupees, and the rounding moved the two apart
c) Each average covers only that quarter's 102 or 96 buyers, two different groups
d) Customers who joined in Q2 spent more than the rest and pulled Q2's average up

## How would a route that never averages confirm the level?

Used at work whenever a per-member number needs a second route that reaches the same level by a
different query.

### Q6. Which route that never averages could confirm Retail-Plus spend per member?

The fix in chapter 4 averaged a step of 107 rows, one per member, with Rs 0 written on purpose for a
quarter with no order, and printed Rs 5,474 then Rs 3,863. Kavya Nair, the team's senior analyst, wants
those levels confirmed by a route that never averages and could disagree with the fix if the fix's step
held the wrong members. Retail-Plus booked Rs 5,85,770 in Q1 and Rs 4,13,380 in Q2; the tier holds 120
members on the customers table, and 13 of them bought nothing in either quarter. Which route confirms
the levels?

a) Each quarter's revenue over the tier's 120 members: Rs 4,881 then Rs 3,445
b) Each quarter's revenue over the 107 rows of the fix's own step: Rs 5,474 then Rs 3,863
c) Each quarter's revenue over that quarter's own 91 and 76 buyers: Rs 6,437 then Rs 5,439
d) Each quarter's revenue over 120 less the 13 who bought nothing: Rs 5,474 then Rs 3,863

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
membership tier, with 120 members on the customers table, and 107 of them bought at least once in the
half-year. Spend per member is the rupees a member spent in a quarter, averaged over the tier's
members. A query can be written three ways: nested subqueries, each written inside the next and read
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

- Which way should a four-step branch query be written for an analyst who reruns it in a fresh session?
- Which fact would make temporary tables the better way?
- Which branch pulled Business's revenue down most, and does its row check itself?
- What do two averages return on five invented members' Q2 spend?
- What explains a sheet that says Retail-Core members spent more each while Retail-Core's revenue fell?
- What does Retail-Plus spend per member come to over the tier's 120 members?

**What you post.** One line of six letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxxx
```

---

## How should a query of several steps be written for an auditor?

Used at work whenever someone other than the author has to read, check and rerun a long query.

### Q1. Which way should a four-step branch query be written for an analyst who reruns it in a fresh session?

Anand's analyst audits the branch query line by line every Monday and reruns it in a fresh session.
It has four steps: each order with its segment, each quarter's leaves per segment, each branch as Q2
over Q1, and the check that the branches multiply back. Which way fits, sized in statements and rows
written?

a) Nested subqueries: one statement and no rows written, read from the innermost step outwards
b) Named steps in a WITH query: one statement and no rows written, read top to bottom
c) Temporary tables: one statement per step and rows written at each step, read in order
d) Four queries stitched together in a notebook: four statements and every result moved out

### Q2. Which fact would make temporary tables the better way?

The analyst's choice from item 1 stands for this Monday. Which fact, if it arrived, would make
temporary tables the better way to hold a step?

a) The analyst wants a comment above every step, and a WITH query has no place to carry one
b) The suite starts running in a brand new session every Monday, with nothing kept from the last run
c) One step's result is read by many queries over millions of rows within one long session
d) The query grows from four steps to seven, too many for a single statement

## Which branch of the tree moved?

Used at work whenever a change in revenue has to be traced to customers, frequency or basket size.

### Q3. Which branch pulled Business's revenue down most, and does its row check itself?

Business's revenue ratio is 0.986, a fall of 1.4 percent. Reading the Business row of the table at the
top of this set, which branch pulled its revenue down most, and does the row check itself?

a) Orders per customer, at 0.965, and the three branches multiply back to 0.986
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

### Q5. What explains a sheet that says Retail-Core members spent more each while Retail-Core's revenue fell?

A hurried sheet took `avg` of each quarter's column in a table with one row per Retail-Core member who
bought in the half-year, 131 members. It says each member spent Rs 3,658 in Q1 and Rs 3,815 in Q2, up
4.3 percent, while Retail-Core's revenue fell 1.8 percent. Of the 131, 102 bought in Q1 and 96 in Q2.
What explains the rise on the sheet?

a) Retail-Core's revenue per order rose 1.2 percent, and that lift reaches every member's spend
b) The averages round to whole rupees, and the rounding moved the two apart
c) Each average covers only that quarter's 102 or 96 buyers, two different groups
d) Members who joined in Q2 spent more than the rest and pulled Q2's average up

## How would a fixed group confirm the change?

Used at work whenever a per-member number needs a second route that no one's buying pattern can move.

### Q6. What does Retail-Plus spend per member come to over the tier's 120 members?

Kavya Nair, the team's senior analyst, wants Retail-Plus's spend per member confirmed by a route that
fixes the group from the customers table: the tier's revenue in each quarter divided by the tier's 120
members. Retail-Plus booked Rs 5,85,770 in Q1 and Rs 4,13,380 in Q2. What does the route give?

a) Rs 4,881 then Rs 3,445, down 29.4 percent
b) Rs 5,474 then Rs 3,863, down 29.4 percent
c) Rs 6,437 then Rs 5,439, down 15.5 percent
d) Rs 1,723 then Rs 1,216, down 29.4 percent

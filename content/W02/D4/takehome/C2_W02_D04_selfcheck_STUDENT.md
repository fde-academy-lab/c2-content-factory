# Does your take-home reach the numbers a careful pass on the staging snapshot reaches?

Open this after your notebook runs cold. If a number of yours differs, find the step that moved it
before you change anything; the right-hand column of each table names the usual cause.

The take-home builds the growth team's Monday table on the data platform lead's staging snapshot, a
different draw of Kalpa Retail's business in three CSVs: orders from April to September 2026, the
customer list, and the campaign platform's feed of the customers the monsoon sale reached. The table
holds one row per customer on the list, with recency counted to the data's last date, frequency,
spend, the segment, whether the sale reached the customer (once, on the first date the feed gives),
and the lapsed flag, no order in the 60 days to that date. The refresh refuses to write a table that
fails any of four guards: one row per customer, as many rows as the list, spend equal to the orders'
total, and a smallest recency of 0.

**Who needs the answer.** You, before you post. The data platform lead lets the refresh near the live
warehouse only if its numbers on staging hold, and a count that went wrong in an early step moves
every number after it.

**The questions on the way.**

- Which eight numbers should the snapshot's table show?
- How many customers sit past each win-back line?
- What should pandas and plain Python both say about Retail-Plus orders per member?
- How far should each tier's spend move from Q1 to Q2?
- Which signs say you took a shortcut?

## Which eight numbers should the snapshot's table show?

| # | Checkpoint | What you should see | If it does not match |
|---|---|---|---|
| 1 | Rows in the table | 340 | 309 means the table was built from the orders; start from the customer list |
| 2 | Spend | Rs 19,84,00,000, equal to the snapshot's orders | More means the feed's merge multiplied some customers' rows |
| 3 | As-of date | 28 September 2026 | A later date is the day you ran it; use the orders' last date |
| 4 | Smallest recency | 0 days | 17 or more means recency was counted to the day you ran it |
| 5 | Customers with no orders | 31, with a frequency of 0 and no recency | Missing frequencies mean the zeros were never filled |
| 6 | Customers the sale reached | 153 | A larger number means a customer is counted once per feed row |
| 7 | Of those, customers who bought | 142 | 142 of 142, 100 percent, means the reached customers with no orders lost their segment and were dropped |
| 8 | The 60-day win-back list | 123 | 153 is the list counted to tonight, 15 October, and 162 to Monday 19 October |

If a run stopped with `pandas.errors.MergeError`, read which side's keys the message says are not
unique, and apply the growth team's rule for a customer the feed names twice before the merge runs
again; never remove `validate` to make the run pass.

## How many customers sit past each win-back line?

| Line | Customers on the list |
|---|---|
| 45 days | 150 |
| 60 days | 123 |
| 90 days | 77 |

Any of the three can be defended. The defence is marked on whether each sentence carries a count and
a cost.

## What should pandas and plain Python both say about Retail-Plus orders per member?

| Quarter | Orders | Members who ordered | Orders per member |
|---|---|---|---|
| Q1 | 215 | 98 | 2.194 |
| Q2 | 140 | 75 | 1.867 |

1.000 in either tool means members were counted once per order: a list in place of a set in the loop,
or `count` in place of `nunique` in pandas.

## How far should each tier's spend move from Q1 to Q2?

| Tier | Q1 | Q2 | Change |
|---|---|---|---|
| Retail-Plus | Rs 6,12,880 | Rs 3,89,970 | a fall of 36.4 percent |
| Retail-Core | Rs 3,90,870 | Rs 3,59,120 | a fall of 8.1 percent |

A Retail-Plus fall near 31 percent, or a Retail-Core fall near 11 percent, means the view's cells are
not totals: check its `aggfunc` and its grand total against the orders. The line from the pandas
reference reads: "one_to_one" or "1:1": check if merge keys are unique in both left and right
datasets.

## Which signs say you took a shortcut?

- Your notebook does not run from a fresh kernel, top to bottom, with every guard inside the function.
- The as-of date is not a column of the table, where Marketing can read what "60 days" was counted
  from.
- A number in part 3 sits without its line and its count.
- Parts 1 and 4 describe their outputs instead of pasting them.

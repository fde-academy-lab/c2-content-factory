# Can you run the day's moves on questions you have not seen, in an hour: four shapes, five owners, a channel nobody chose and the Retail-Plus table?

The TA-led practice lab, after the afternoon block. Four problems, climbing in difficulty, are the
core and take about 60 minutes: problem 1 ten minutes, problem 2 ten, problem 3 twenty and problem 4
twenty, the last combining the day. Work alone for problems 1 and 2 and in pairs for 3 and 4. The
chapter sets' remaining 18 items, items 3 to 5 of each set in `exercises/unguided/`, are the lab's
stretch: if you finish the core early, work them, chapters 4 to 6 first, and whatever is left is
tonight's work.

Kalpa Retail's warehouse, its Postgres database, holds 1,000 orders from April to September 2026,
Q1 (April to June) and Q2 (July to September), and a customer list of 340 customers in four
segments, Retail-Core, Retail-Plus, Student and Business, across six cities. Each order has a
channel: the app, the website or a store. The growth team's table holds one row per customer on the
list, with recency (the days from the last order to the table's as-of date, 28 September 2026),
frequency (the count of orders) and spend (the value of the orders at the prices charged). The
campaign platform's feed lists the customers the monsoon sale reached; the growth team's rule counts
a customer the feed names twice once, on the first date. Kavya Nair, the senior analyst on the team,
reviews every table and every tool choice before it leaves.

**Who needs the answer.** Kavya, who sends back a table whose shape nobody predicted, a number given
to the wrong tool, or a column that guesses without saying so. The same moves come up in analyst
interviews on tables the candidate has never seen.

**The questions on the way.**

- What shape does each of four groupby and pivot calls return on Kalpa's tables?
- Which tool should own each of five asks?
- Which channel does each customer use most, and for how many customers is the answer a guess?
- What does the head of Retail-Plus's own table show, and what one line goes with it?

**What you post.** The letters for problems 1 and 2 as one line, nine letters in order, problem 1
giving four and problem 2 giving five. Problems 3 and 4 give numbers and a sentence each, posted
below the letters. Stretch letters, if you reach them, go on one line per chapter set.

```
Post exactly this shape: xxxxxxxxx
```

---

## Problem 1. What shape does each of four groupby and pivot calls return on Kalpa's tables?

Used at work before every call on a table you have not met, so that a surprising shape is noticed
before its numbers are.

Ten minutes, alone. Write your prediction before you run anything. A wrong prediction you can
explain is worth more than a right guess.

### Q1. How many rows does a count of customers per city return?

What does `customers.groupby("city").size()` return?

a) 340 rows, one per customer
b) 4 rows, one per segment
c) 6 rows, one per city
d) 301 rows, one per customer who ordered

### Q2. How many rows does a count per customer and quarter return?

Kalpa's 301 customers who ordered placed 1,000 orders across two quarters, and some ordered in only
one of them. What does `orders.groupby(["customer_id", "quarter"]).size()` return?

a) 471 rows, one per customer and quarter that has orders
b) 602 rows, the 301 customers who ordered times 2 quarters
c) 680 rows, every customer on the list times 2 quarters
d) 1,000 rows, one per order, each in its quarter

### Q3. What shape is revenue by channel with the two quarters side by side?

Anand Iyer, the finance controller, asks for revenue by channel, the two quarters side by side. What
shape is this, as rows by columns?

```python
orders.pivot_table(index="channel", columns="quarter", values="amount", aggfunc="sum")
```

a) 2 by 3, a quarter per row and a channel per column
b) 6 by 1, one row per channel and quarter
c) 1,000 by 2, the quarters written onto each order
d) 3 by 2, a channel per row and a quarter per column

### Q4. What shape is each customer's first and last order date?

The growth team wants each customer's first and last order date. What shape is this, as rows by
columns?

```python
orders.groupby("customer_id").agg(first=("order_date", "min"), last=("order_date", "max"))
```

a) 340 by 2, one row per customer on the list
b) 301 by 2, one row per customer who ordered
c) 2 by 301, one row per measure
d) 1,000 by 2, the dates written onto each order

---

## Problem 2. Which tool should own each of five asks?

Used at work every time a number is asked for, since the tool that computes it decides who can
rerun it.

Ten minutes, alone. For each ask, choose the tool and the form it takes.

### Q5. Which tool should compute the head of Retail-Plus's protect list, refreshed weekly and read by three teams?

a) SQL, a query in the warehouse that every team reads
b) pandas, a notebook the analyst reruns and emails each week
c) Plain Python, a script with the ranking written out as a loop
d) pandas, a CSV the analyst writes to a shared folder weekly

### Q6. Which tool should answer how many customers a 45-day win-back line would hold, asked once in a meeting?

a) SQL, a new view in the warehouse for the 45-day list
b) Plain Python, a loop over the customer table's rows
c) pandas, the customer table in memory and one changed number
d) SQL, the win-back query mailed to the platform lead to rerun

### Q7. Which tool should explain to a reviewer, step by step, why the win-back list holds 111 and not 166?

a) SQL, two queries whose counts differ by 55, run one after the other
b) Plain Python, both recency counts side by side, dates printed
c) pandas, two chained calls on the table with both counts shown
d) SQL, one query with the two counts in two columns

### Q8. Which tool should hold the monthly revenue by segment that Finance reconciles against its books?

a) pandas, a notebook with its outputs saved for Finance to read
b) Plain Python, a script that prints the table to the terminal
c) pandas, a CSV sent to Finance on the first of each month
d) SQL, a view defined in the warehouse

### Q9. Which tool should match a one-off list of 40 customer ids, emailed by the head of Retail-Plus, to the customer table this afternoon?

a) pandas, the 40 ids as a frame merged with `validate`
b) SQL, once the platform lead loads the list into a warehouse table
c) Plain Python, a loop that searches the table for each id in turn
d) SQL, a new permanent table of the 40 ids in the warehouse

---

## Problem 3. Which channel does each customer use most, and for how many customers is the answer a guess?

Used at work whenever a table gains a column that picks one value per row, such as a preferred
channel or a top category.

Twenty minutes, in pairs, in a new notebook saved in this day's `notebooks/` folder, so the helper
and the data are found. The growth team wants a column naming
the channel each customer uses most, to decide where each Monday offer is sent. Start from these
lines, which read the warehouse the way every notebook today does:

```python
import sys, pathlib
here = pathlib.Path.cwd()
for parent in [here, *here.parents]:
    if (parent / "scripts" / "c2kit.py").exists():
        sys.path.insert(0, str(parent / "scripts")); break
import c2kit as kit
import pandas as pd

ENG = kit.engine()
orders = pd.read_sql("SELECT order_id, customer_id, channel FROM orders", ENG)
customers = pd.read_sql("SELECT customer_id, segment FROM customers", ENG)
```

1. Build the count of orders per customer and channel with `pivot_table`, its `aggfunc` written out
   and `fill_value=0`.
2. Attach it to the customer list so every customer has a row, with `validate` stated and every
   missing count filled with 0 on purpose.
3. Add the most-used channel with `idxmax(axis=1)` on the three channel columns.
4. Count the rows, the orders in the cells, and the customers whose most-used channel is a tie.
5. Find what `idxmax` returns for a customer with no orders at all.

Then answer: for how many of the 340 customers is the new column a guess, and what rule would you
give the growth team for those rows?

---

## Problem 4. What does the head of Retail-Plus's own table show, and what one line goes with it?

Used at work whenever one team wants its own slice of a shared table, with its own columns.

Twenty minutes, in pairs, in the same notebook. The head of Retail-Plus, the paid membership tier,
wants a table of their own: one row for every Retail-Plus member on the list, with Q1 spend and Q2
spend as two columns, whether the monsoon sale reached them, and recency counted to the data's last
date. Read the feed with
`pd.read_csv(kit.data_dir() / "C2_W02_D04_exposure_STUDENT.csv", parse_dates=["exposed_date"])`,
and read the orders' `order_date`, `quarter` and `amount` as well, with `parse_dates=["order_date"]`.

1. Build it, with every merge's `validate` stated and the growth team's rule for the feed applied.
2. Check it three ways: its rows against the Retail-Plus members on the list, its spend against
   Retail-Plus's orders in the warehouse, and its smallest recency.
3. Count, among the members the sale reached and among those it did not reach, how many spent less
   in Q2 than in Q1.

Then write the one line to the head of Retail-Plus about those two counts, with what the table can
and cannot say about the sale.

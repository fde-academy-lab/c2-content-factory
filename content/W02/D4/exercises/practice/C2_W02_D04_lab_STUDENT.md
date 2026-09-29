# Practice lab: shapes, tools, and two tables of your own

About an hour, run by the TA after the second block. Four problems, each harder than the last;
the fourth combines the day's three rounds. Work in a fresh notebook in `notebooks/`, reading
from the warehouse as the morning did. The self-check numbers for problems 3 and 4 are in the
solution, which the TA releases at the end.

Post one line with the nine letters from problems 1 and 2, no spaces:

```
Post exactly this shape: xxxxxxxxx
```

---

## Problem 1. Predict the shape, then run it (15 minutes)

The growth team's analyst is about to run four calls. Write your prediction for each before you
run it; a wrong prediction you can explain is worth more than a right guess.

### Q1

How many rows does `customers.groupby("city").size()` return, for the city split of the table?

a) 340, one per customer
b) 4, one per segment
c) 6, one per city
d) 301, one per customer who ordered

### Q2

How many rows does `orders.groupby(["customer_id", "quarter"]).size()` return, for a
customer-by-quarter view?

a) 471, one per customer and quarter pair that has orders
b) 602, the 301 customers who ordered, times 2 quarters
c) 680, every customer on the list, times the 2 quarters
d) 1,000, one per order, each counted once in its quarter

### Q3

Anand asks for revenue by channel, the two quarters side by side. What shape is
`orders.pivot_table(index="channel", columns="quarter", values="amount", aggfunc="sum")`?

a) 2 rows by 3 columns, a quarter per row and a channel per column
b) 6 rows by 1 column, one per channel and quarter pair
c) 1,000 rows by 2 columns, the quarters written onto each order
d) 3 rows by 2 columns

### Q4

The growth team wants each customer's first and last order dates. What shape is
`orders.groupby("customer_id").agg(first=("order_date", "min"), last=("order_date", "max"))`?

a) 340 rows by 2 columns, one row per customer on the list
b) 301 rows by 2 columns
c) 2 rows by 301 columns, one row per measure
d) 1,000 rows by 2 columns, the dates written onto each order

## Problem 2. Pick the tool, fast (10 minutes)

For each ask, plain Python, SQL, pandas or Excel. One line of reason each, naming who must
trust the number.

### Q5

Which tool computes the head of Retail-Plus's protect list, refreshed weekly and read by three
teams from the same source?

a) SQL, a query in the warehouse that every team reads from
b) pandas, a notebook the analyst reruns and emails each week
c) Plain Python, a script with the ranking written out as a loop
d) Excel, a sheet with the top fifty pasted in and sorted by hand

### Q6

Which tool answers "what share of our reached customers bought, if the 60-day window were 45
days instead", asked once in a meeting?

a) SQL, a new view in the warehouse for the 45-day window only
b) Excel, a pivot on last Friday's export with a filter on days
c) pandas, the customer table and one changed line
d) Plain Python, a loop over the customer table's rows

### Q7

Which tool explains to a reviewer, step by step, why the win-back list is 111 and not 166?

a) SQL, two queries whose counts differ by 55 customers, run one after the other
b) Plain Python, both recency calculations side by side with the dates printed
c) pandas, two chained calls on the customer table with both of the counts shown
d) Excel, two columns of recency with a count at the bottom of each one

### Q8

Which tool holds the monthly revenue by segment that Finance reconciles against its books?

a) pandas, a notebook with its outputs saved for Finance to read
b) Excel, a workbook updated by the analyst on the first of the month
c) Plain Python, a script that prints the table to the terminal
d) SQL, a view defined in the warehouse

### Q9

Which tool matches a one-off list of 40 customer ids, sent in an email by the head of
Retail-Plus, to the customer table this afternoon?

a) pandas, a small frame of the ids merged with `validate="one_to_one"`
b) SQL, after the list is loaded into a warehouse table by the platform lead
c) Excel, a lookup from the email's list into last week's export
d) Plain Python, a loop that searches the customer table for each id

## Problem 3. Channel preference per customer (15 minutes)

The growth team wants a column saying which channel each customer uses most. Build a table with
one row per customer on the list and the count of orders per channel, using `pivot_table` with
`aggfunc` stated and `fill_value=0`, attached to the customer list with `validate`. Then add the
most-used channel with `idxmax(axis=1)`, and answer: for how many customers is that column a
tie, where `idxmax` quietly picked the first channel in the column order? State the tie rule you
would give the growth team.

## Problem 4. The Q2 table (20 minutes)

The growth team wants the Monday table for Q2 alone, to compare with last week. Build it: one row
per customer on the list, Q2 frequency and spend, recency measured from Q2's own last order date,
and the three checks from the morning (rows against the list, spend against the Q2 book, the
smallest recency 0). Then say how many customers would sit on a 30-day win-back list, and how
many the same list would hold if recency were measured from Monday 19 October instead.

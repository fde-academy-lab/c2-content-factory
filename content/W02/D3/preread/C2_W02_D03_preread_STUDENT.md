# What will the growth team ask on Thursday, and what should you settle tonight?

This pre-read takes about fifteen minutes tonight, with one check to run in your Codespace, and it
asks you to learn no new tool before class.

---

## What does the growth team ask on Thursday?

Today ended on Marketing's protect lists, the nine calls and Q2 against the plan line, all built in
SQL in Kalpa's warehouse. Thursday's ask, in the curriculum's own words:

> "The growth team now wants one thing every week: a single table with one row per customer,
> refreshed on Monday, carrying how recently they bought, how often, how much, their segment,
> whether the monsoon sale reached them, and last week's flags."

The data platform lead is blunt:

> "The warehouse queries are fine for Finance, but Marketing's analysts live in Python. Build them
> the table in pandas, from the warehouse, and make it refreshable in one run."

And a senior analyst on the team sets the challenge you will answer in writing:

> "You did the tree in plain Python in Week 1, in SQL on Monday. Do it a third way now, and tell me
> honestly which tool you would pick for which job."

---

## Which words will Thursday use that need a plain meaning before class?

Some of these appeared in Week 0's foundations guide, chapter 6, and Thursday uses all of them from
its first hour. Read each plain meaning, then write your own example in the last column tonight, one
line each.

| Word | What it means, in plain words | Where Thursday uses it | Your own example |
|---|---|---|---|
| DataFrame | pandas's table: rows, named columns, and one kind of value in each column | Every step | |
| read_sql | A pandas call that runs a SQL query on the warehouse and hands back the result as a DataFrame | The first step | |
| groupby, then agg | Splits the rows into groups by a column and computes one row of measures for each group, the pandas twin of GROUP BY | Building the customer table | |
| Split-apply-combine | The three steps inside every groupby: split the rows into groups, apply a calculation to each, combine the answers into one table | An interview question | |
| Recency, frequency and monetary value | How recently a customer last ordered, how often they order and how much they spend | Three of the table's columns | |
| merge | Lines two tables up on a shared column, the pandas twin of a SQL join | Bringing in the monsoon sale | |
| Campaign exposure | The record of which customers a campaign reached, here the monsoon sale | The growth team's ask | |
| pivot_table and melt | pivot_table turns the values of one column into column headings, such as one column per month; melt turns column headings back into rows | A trend view and a comparison view | |
| Refreshable in one run | The whole table rebuilds from the warehouse when one notebook runs top to bottom, with no step done by hand | The platform lead's ask | |

---

## What is one thing to think about before class?

Today the protect list and the falling flag were built in SQL, inside the warehouse, where Finance
can rerun them. Write two lines tonight: if a Marketing analyst wanted to try three different
cut-offs for the list before lunch, would you hand them the SQL file or a table in Python, and which
of the two would you hand Finance to audit? Bring the two lines; the room compares them before any
code runs.

---

## Does your Codespace run pandas and read the warehouse?

Open a new notebook anywhere inside your copy of the repository, choose the Python 3 kernel and run
this one cell. Its first lines find the shared helper, `c2kit`, the way the setup cell of every
notebook this week does.

```python
import sys, pathlib
here = pathlib.Path.cwd()
for parent in [here, *here.parents]:
    if (parent / "scripts" / "c2kit.py").exists():
        sys.path.insert(0, str(parent / "scripts")); break
import c2kit as kit
import pandas as pd

print(pd.__version__)
pd.read_sql("SELECT count(*) AS orders, sum(amount) AS booked "
            "FROM orders WHERE quarter = 'Q2'", kit.engine())
```

It should print a version number, 3.0.6 when this pack was built, and then a table of one row: 462
orders and 98400000.0 booked, which is Monday's Rs 9,84,00,000. If the cell stops on a line that
names a `pip install` command, run that command in the terminal and run the cell again. If it says
no database answered, run `bash .devcontainer/load_warehouse.sh` in the terminal first. If anything
else goes wrong, tell the support TA before class, since Thursday opens by reading the warehouse
into pandas.

---

## Which line do you carry into Thursday?

Know where each of Marketing's columns comes from before you write any pandas: how often and how
much are this week's measures, the falling flag is today's, the segment lives on the customer, and
the monsoon sale's reach lives in a table of its own.

# Which answers hold in the chapter 4 set on one question asked in three tools, and why?

Answers: 1b 2a 3d 4b 5c

The marketing lead's budget case needs the share of reached customers who bought: reached customers
with at least one order between April and September 2026, over all the customers reached. Chapter 4
asked it in plain Python, SQL and pandas. The three agreed once each read a customer's segment from
the customer list: 107 of the 130 reached bought, 82 percent, 56 of 70 in Retail-Core and 51 of 60
in Retail-Plus, and a set difference with no grouping found the same 107. Kavya Nair, the senior
analyst, looks for the rows a tool dropped before she looks at its code. Three of the five items are
design items: 3, 4 and 5.

**Who needs the answer.** You, checking your five letters after the lab or tonight. Two tools that
disagree usually disagree about rows, and the share that goes to Marketing is only as good as the
rows it counted.

**The questions on the way.**

- Which idea does the chapter 4 set test?
- Why does each of the five keys hold, from five invented customers to the set that cannot drop
  anyone?
- Why is option a in item 4, the chapter's own pairing, the wrong answer worth arguing about?
- Where does one question giving two answers in two tools come up at work?

## Which idea does the chapter 4 set test?

A share is only as honest as its denominator, and a group can lose part of the denominator without
an error. The set asks what a default group keeps, how SQL and pandas differ on a missing key, which
count catches a share that is too good, which tool should own the number once an auditor reruns it,
and which arithmetic on sets cannot drop anyone.

## Why does each of the five keys hold, from five invented customers to the set that cannot drop anyone?

### Q1. What does a default `groupby` report for five invented reached customers?

Five reached customers, two with a missing segment, two who bought.

The key is b, "3 customers, 67 percent". `groupby` drops rows whose key is missing unless told
`dropna=False`, so C and E vanish: Retail-Core holds A, Retail-Plus holds B and D, and the output
counts 3 customers with 2 buyers. The two who vanished are exactly the two who never bought.

- a, "5 customers, 40 percent": the honest answer, which `dropna=False` or a segment from the list
  would give.
- c, "5 customers, 67 percent": keeps all five in the count and still divides by three.
- d, "3 customers, 40 percent": drops the two rows and keeps their share, which no single call does.

### Q2. What do SQL's `GROUP BY` and pandas' `groupby` each do with a customer whose segment is missing?

The interviewer's question, asked about defaults.

The key is a, "SQL keeps one `NULL` group; pandas drops it unless `dropna=False`". SQL's `GROUP BY`
puts every `NULL` key into one group of its own, and pandas drops missing keys unless told otherwise,
which is how chapter 4's tools first disagreed.

- b, "Both drop the rows, since a group needs a value to be named by": SQL keeps them.
- c, "SQL drops the `NULL` rows; pandas keeps them in a group named NaN": the two defaults swapped.
- d, "Both keep one group for it, `NULL` in SQL and NaN in pandas": true of pandas only with
  `dropna=False`.

### Q3. What is the first check on a dashboard that says 96 percent of 1,250 reached customers bought?

A design item. The dashboard counts 1,250 reached; the feed names 1,480.

The key is d, "230 of 1,480 reached are missing; if none bought, it is 81 percent". The
groups have to add back to the customers reached. 1,480 less 1,250 is 230 customers missing from the
dashboard, and 96 percent of 1,250 is 1,200 buyers, so if none of the missing bought, the share is
1,200 over 1,480, 81 percent.

- a, "A rerun of the dashboard's query on the same data surfaces the gap": the same query drops the
  same rows again.
- b, "1,200 bought of 1,250, recomputed by hand, which confirms 96 percent": confirms the arithmetic
  and keeps the wrong denominator.
- c, "The 50 of the 1,250 who did not buy are the ones missing from the feed": the 50 are on the
  dashboard; the missing 230 are the reached customers it never counted.

### Q4. Which pairing does Kavya sign once the share goes to Finance's quarterly audit?

A design item. Finance's analyst will rerun the number from the warehouse every quarter.

The key is b, "SQL answers where the auditor reruns it; pandas sets check it". Once
someone outside the team reruns the number, it lives where they can run it, in the warehouse, and
the check moves to the route that shares no code with it, here the set difference in pandas.

- a, "pandas answers on the table in memory, and SQL, sending 2 rows, checks it": the pairing chapter
  4 chose for Marketing's slide, which the auditor cannot rerun without the notebook.
- c, "Plain Python answers, line by line for the auditor, and SQL checks it": a loop explains one
  case line by line; a number rerun every quarter belongs in the warehouse.
- d, "pandas answers, and the notebook goes to the auditor to rerun it": the notebook runs on a copy
  and depends on the order its cells ran in.

### Q5. Which line gives the share who bought with no group that could drop anyone?

A design item. 800 reached, 5,000 buyers, 610 in both.

The key is c, "`len(reached & buyers) / len(reached)`, which is 76 percent". The share who bought is
the reached customers who are also buyers, 610, over the reached, 800, which is 76 percent. No
segment is read, so no missing segment can drop anyone.

- a, "`len(reached & buyers) / len(buyers)`, which is 12 percent": the right overlap over the wrong
  base, the share of buyers the campaign reached.
- b, "`len(reached - buyers) / len(reached)`, which is 24 percent": the share of the reached who did
  not buy.
- d, "`len(buyers - reached) / len(buyers)`, which is 88 percent": the share of buyers the campaign
  never reached.

## Why is option a in item 4, the chapter's own pairing, the wrong answer worth arguing about?

Item 4, option a is the call chapter 4 made, and it was right for a slide the team builds and checks
itself. The audit changes who reruns the number. A pairing is chosen for the person who must trust
it, and when that person changes, the owner of the number can change with them.

## Where does one question giving two answers in two tools come up at work?

Uber's engineering blog describes its Operations team computing completed trips as a Presto/Hive SQL
query for daily dashboards while the Pricing Engineering team built its own completed-trips metric
from a Cassandra table for real-time services. The goal Uber set was a metric and its business logic
in "a strictly ONE to ONE mapping" (Uber Blog, The Journey Towards Metric Standardization, 12 January
2021, checked 1 Oct 2026).

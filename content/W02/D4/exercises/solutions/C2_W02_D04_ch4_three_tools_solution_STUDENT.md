# Which answers hold in the chapter 4 set on one question asked in three tools, and why?

Answers: 1b 2a 3d 4b 5c

The marketing lead's budget case needs the share of reached customers who bought: reached customers
with at least one order between April and September 2026, over all the customers reached. Chapter 4
asked it in plain Python, SQL and pandas. The three agreed once each read a customer's segment from
the customer list: 107 of the 130 reached bought, 82 percent, 56 of 70 in Retail-Core and 51 of 60
in Retail-Plus, and a set difference in plain Python, with no grouping, found the same 107. Kavya
Nair, the senior analyst, looks for the rows a tool dropped before she looks at its code. Three of
the five items are design items: 3, 4 and 5.

**Who needs the answer.** You, checking your five letters after the lab or tonight. Two tools that
disagree usually disagree about rows, and the share that goes to Marketing is wrong by every row a
tool dropped.

**The questions on the way.**

- Which idea does the chapter 4 set test?
- Why does each of the five keys hold, from five invented customers to the cities nobody recorded?
- Why is option c in item 4, a check that passes while every segment is wrong, the wrong answer
  worth arguing about?
- Where does one question giving two answers in two tools come up at work?

## Which idea does the chapter 4 set test?

A share divides by the customers it counts, and a group can lose some of them without an error. The
set asks what a default group keeps, how SQL and pandas differ on a missing key, which count catches
a share that is too good, which pairing of routes Finance's audit needs once the share is rerun by
segment, and how a split by city keeps the customers whose city nobody recorded.

## Why does each of the five keys hold, from five invented customers to the cities nobody recorded?

### Q1. What does a default `groupby` report for five invented reached customers?

Five customers were reached, two of them with a missing segment, and two of them bought.

The key is b, "It counts 3 customers, and 67 percent of them bought". `groupby` drops rows whose key
is missing unless told `dropna=False`, so C and E vanish: Retail-Core holds A, Retail-Plus holds B
and D, and the output counts 3 customers with 2 buyers. The two who vanished are exactly the two
who never bought.

- a, "It counts 5 customers, and 40 percent of them bought": It is the honest answer, which
  `dropna=False` or a segment from the list would give.
- c, "It counts 5 customers, and 67 percent of them bought": It keeps all five in the count and
  still divides by three.
- d, "It counts 3 customers, and 40 percent of them bought": It drops the two rows and keeps their
  share, which no single call does.

### Q2. What do SQL's `GROUP BY` and pandas' `groupby` each do with a customer whose segment is missing?

The interviewer asks about each tool's default.

The key is a, "SQL keeps one `NULL` group, and pandas drops it unless `dropna=False`". SQL's
`GROUP BY` puts every `NULL` key into one group of its own, and pandas drops missing keys unless told
otherwise, which is how chapter 4's tools first disagreed.

- b, "Both drop the rows, since a group needs a value to be named by": SQL keeps them.
- c, "SQL drops the `NULL` rows, and pandas keeps them in a group named NaN": It swaps the two
  defaults.
- d, "Both keep one group for it, `NULL` in SQL and NaN in pandas": That is true of pandas only with
  `dropna=False`.

### Q3. What is the first check on a dashboard that says 96 percent of 1,250 reached customers bought?

Item 3 is a design item: the dashboard counts 1,250 reached, and the feed names 1,480.

The key is d, "It finds 230 of the 1,480 reached missing, so the share is 81 percent if none
bought". The groups have to add back to the customers reached. 1,480 less 1,250 is 230 customers
missing from the dashboard, and 96 percent of 1,250 is 1,200 buyers, so if none of the missing
bought, the share is 1,200 over 1,480, 81 percent.

- a, "A rerun of the dashboard's query on the same data finds the gap": The same query drops the
  same rows again.
- b, "A recount by hand finds 1,200 bought of 1,250, which confirms 96 percent": It confirms the
  arithmetic and keeps the wrong denominator.
- c, "It finds that the 50 of the 1,250 who did not buy are the ones missing from the feed": The 50
  are on the dashboard; the missing 230 are the reached customers it never counted.

### Q4. Which pairing does Kavya sign once Finance's audit reruns the share by segment?

Item 4 is a design item: the share now goes into an audit pack segment by segment, and Finance's
analyst reruns it from the warehouse every quarter.

The key is b, "SQL answers with each segment read from the customer list, and the set difference
checks the total". Once someone outside the team reruns the number, it lives where they can run it,
in the warehouse. Its segment comes from the customer list, where every customer has one, so it
gives Retail-Core 56 of 70 and Retail-Plus 51 of 60. The set difference shares no code with the
query and confirms the 107 of 130 underneath.

- a, "pandas answers on the table in memory, and SQL, sending two rows, checks it": It is the
  pairing chapter 4 chose for Marketing's slide, and the auditor cannot rerun it without the
  notebook.
- c, "SQL answers with each segment read from the buyer's orders, and the set difference checks the
  total": SQL files the 23 reached customers with no orders under a `NULL` segment, so Retail-Core
  reads 56 of 56 and Retail-Plus 51 of 51, and the total check still passes at 107 of 130.
- d, "Plain Python answers line by line for the auditor, and SQL checks it": A loop explains one
  case line by line, and a number an auditor reruns every quarter belongs in the warehouse.

### Q5. Which route gives the stores team the share by city when 40 reached customers have no city?

Item 5 is a design item: the stores team needs a split by city, and 40 of the 900 reached have no
city on the list, so the route has to split, keep every customer and still be checked.

The key is c, "`groupby("city", dropna=False)` keeps the 40 as their own row, and the set difference
checks the total". The 40 stay visible as a row with no city, so the groups add back to the 900
reached, and the set difference, which reads no city, confirms the buyers among them.

- a, "`groupby("city")` runs as written, and the set difference checks the total": The default drops
  the 40, so the cities add up to 860 reached, and its own check would stop it at 860 against 900.
- b, "`groupby("city")` runs with the 40 filled in as the list's most common city, and SQL checks it
  by city": It writes a city nobody recorded onto 40 customers, so that city's share mixes them in,
  and SQL, which reads the list as it is, disagrees on that city.
- d, "The set difference answers alone, since it reads no city and so cannot drop anyone": It gives
  one share for all 900, and the stores team asked for one share per city.

## Why is option c in item 4, a check that passes while every segment is wrong, the wrong answer worth arguing about?

Item 4, option c puts the number in SQL, where the auditor reruns it, and checks it with a route
that shares no code, so it looks like the chapter's lesson applied twice. Its segments come from
the buyers' orders. SQL keeps the 23 reached customers with no orders in a `NULL` group, so the
total stays 107 of 130 and the set difference agrees, while Retail-Core reads 56 of 56 and
Retail-Plus 51 of 51, a perfect score in each, where the customer list gives 80 and 85 percent. A
check on the total cannot see a split that went wrong inside it, so the segment comes from the
customer list before any check is chosen.

## Where does one question giving two answers in two tools come up at work?

Uber's engineering blog describes its Operations team computing completed trips as a Presto/Hive SQL
query for daily dashboards while the Pricing Engineering team built its own completed-trips metric
from a Cassandra table for real-time services. The goal Uber set was a metric and its business logic
in "a strictly ONE to ONE mapping" (Uber Blog, The Journey Towards Metric Standardization, 12 January
2021, checked 1 Oct 2026).

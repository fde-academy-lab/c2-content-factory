# Which answers hold in the escalated case on building the whole Monday table alone, and why?

Answers: 1c 2b 3a 4d 5c 6d 7a 8b 9d 10b 11a 12c 13b

The growth team asked for one table, one row per customer, refreshed every Monday: recency, the date
of the last order; frequency, the count of orders; spend, the value of the orders at the prices
charged; the segment; whether the monsoon sale reached the customer; and two flags, lapsed (no order
in the 60 days to the table's as-of date) and falling (Wednesday's rule: lower in August than July and
lower again in September, each a real calendar month after the one before). Kalpa Retail's warehouse
holds 1,000 orders from April to September 2026, worth Rs 19,84,00,000, and 340 customers; the
campaign platform's feed lists the customers the sale reached in August, and the growth team's rule
counts a customer the feed names twice once, on the first date. The case asks each learner to build
the table alone in fifty minutes in `notebooks/C2_W02_D04_ex1_escalated_case_STUDENT.ipynb`, thirteen
lettered choices in five parts. The executed solution, `C2_W02_D04_ex1_escalated_case_solution_STUDENT.ipynb`
in this folder, runs every key. Two of the thirteen items are design items: 5 and 13.

**Who needs the answer.** You, before the debrief, checking your thirteen letters and your four
numbers. The debrief replays the room's wrong outputs aloud, and an output you cannot trace to its
step here is one that reaches the growth team on Monday.

**The questions on the way.**

- Which idea does the escalated case test?
- Which numbers should you have reached in each of the five parts?
- Why does each of the thirteen keys hold, from the table's starting frame to the query for crores?
- Which wrong outputs does the debrief replay, and which check catches each?
- Where does a scheduled table that refuses to ship come up at work?

## Which idea does the escalated case test?

Every habit of the day at once, with no trainer choosing the step: the customer list as the table's
rows, a number for customers with no orders said on purpose, a feed attached by a rule and a stated
promise and counted a second way, recency counted to the data's own last date, a monthly reading
taken from the same customer, a view whose cells are totals, guards that refuse a broken table, and
the query that keeps the table possible when the orders grow.

## Which numbers should you have reached in each of the five parts?

| Part | Number | What it means |
|---|---|---|
| 1 | 340 rows; 39 customers with a frequency of 0; spend Rs 19,84,00,000 | Every customer is on the table, and the 39 who never ordered are there for the first-order nudge |
| 2 | 340 rows after the merge; 130 reached, 70 in Retail-Core and 60 in Retail-Plus; the second count 130 | The sale is attached once per customer, and a count that shares no code agrees |
| 3 | As of 28 September 2026; 111 on the win-back list, 5 Business, 49 Retail-Core, 47 Retail-Plus and 10 Student; the falling flag matches Wednesday's query customer for customer | The list is the same whichever Monday it runs on |
| 4 | A view of 6 months by 4 segments, adding up to Rs 19,84,00,000 | Each point on the slide is a month's total |
| 5 | Two runs give one table; an id written over another customer's row stops the run with the row count unchanged; recency counted to 21 September stops it too; the grouped query sends 301 rows, matching step 1 customer by customer | The refresh refuses a broken table, and the table survives orders in crores |

The four numbers to post are 340, Rs 19,84,00,000, 130 and 111.

## Why does each of the thirteen keys hold, from the table's starting frame to the query for crores?

### Q1. Which frame should the table start from?

The key is c, `customers`. The table is one row per customer on the list, so the list is its
starting frame and the orders only add columns.

- a, `customers[customers["segment"] != "Business"]`: drops the 40 Business customers, so the table
  holds 300 rows, though the growth team acts on every customer on the list.
- b, `rfm[["customer_id"]]`: only the 301 customers who ordered, so the 39 who never ordered have
  no row and get no first-order nudge.
- d, `exposure[["customer_id"]].drop_duplicates()`: only the 130 customers the sale reached.

### Q2. What goes in the frequency of a customer who never ordered?

The key is b, `table["frequency"].fillna(0).astype("int64")`. No orders means a count of 0, said on
purpose, and the column goes back to whole numbers.

- a, `table["frequency"]`: leaves 39 missing counts, which a filter for 0 never finds.
- c, `table["frequency"].fillna(table["frequency"].median())`: invents orders for customers who
  placed none.
- d, `table["frequency"].dropna()`: `assign` lines the shorter column up by index and leaves the
  gaps missing, so nothing changes.

### Q3. Which call applies the growth team's rule: one row per customer, on the first date the feed gives?

The key is a, `ordered.drop_duplicates("customer_id", keep="first")`. The feed is sorted by date, so
each customer's first row is the earliest time the sale reached them.

- b, `keep=False`: drops every copy of a repeated customer, so they read as never reached and the
  second count disagrees with the flags.
- c, `keep="last"`: keeps a later date wherever a customer repeats, which the check on the earliest
  date catches.
- d, `drop_duplicates(["customer_id", "exposed_date"])`: treats a row as a repeat only when the
  date repeats too. The platform's repeat sends carry different dates, so nothing is dropped and the
  one-to-one merge stops with a `MergeError`.

### Q4. Which promise should the merge carry?

The key is d, `"one_to_one"`. The table holds each customer once and so does the feed after the
rule, and the merge should stop if either ever stops being true. The check runs your choice against
the raw feed, which the rule has not touched, and only this promise stops it.

- a, `"one_to_many"`: checks only the table's side, so a feed that repeats a customer merges
  silently.
- b, `"many_to_many"`: checks neither side.
- c, `None`: turns the check off.

### Q5. Which count, sharing no code with the rule or the merge, should equal the reached flags?

A design item: the choice is which second route can disagree when the first one is wrong. The key is
c, `exposure["customer_id"].nunique()`. It counts the distinct customers in the raw feed with no
sort, no rule and no merge. The check runs your count a second time on a table where the merge lost
one reached customer, and only a count that shares no code with the merge disagrees with that table.

- a, `len(first_touch)`: counts the rows the rule kept, so it shrinks with the flags and agrees with
  the broken table.
- b, `int(table["exposed_date"].notna().sum())`: the merged table's own column, which is the flags
  again, so it agrees with the broken table too.
- d, `len(exposure)`: one row for every time the platform sent a customer, so it disagrees with a
  correct table.

### Q6. Which date is the table's as-of date, the date recency is counted to?

The key is d, `orders["order_date"].max()`, 28 September 2026, the last date the data covers.
Somebody ordered that day, so the smallest recency is 0.

- a, `pd.Timestamp.today().normalize()`: counts to the day the notebook runs, so every customer looks
  staler than the data says and the list grows each Monday with nothing new loaded.
- b, `pd.Timestamp("2026-09-30")`: the end of the quarter, two days after the last order the
  warehouse holds, so the newest buyer reads two days old.
- c, `table["last_order"].max() + pd.Timedelta(days=1)`: the morning after the last order, so the
  newest buyer reads one day old.

### Q7. Which condition flags a lapsed customer?

The key is a, `table["recency_days"] > 60`. A customer who never ordered has no recency, so the
comparison is false for them and they stay off the win-back list.

- b, `table["frequency"] == 0`: flags only the 39 customers who never ordered, who belong on the
  first-order list.
- c, `table["recency_days"].fillna(9999) > 60`: flags those 39 on top of the 111 lapsed, 150 where
  the warehouse counts 111.
- d, `(pd.Timestamp.today() - table["last_order"]).dt.days > 60`: the wall-clock count again.

### Q8. Which grouping gives each customer's earlier monthly readings, as Wednesday's LAG did?

The key is b, `monthly.groupby("customer_id")`. The earlier readings belong to the same customer,
which is `LAG` with `PARTITION BY customer_id`, and the grouping feeds the spend and the month alike.

- a, `monthly`: shifts the whole frame, so a customer's first months read the previous customer's
  spend and month; on Kalpa's orders the flag then lands on a customer who never fell, and the check
  against Wednesday's query catches it.
- c, `monthly.groupby("month_num")`: compares different customers in the same month.
- d, `monthly.groupby(["customer_id", "month_num"])`: puts each customer-month in a group of its
  own, so there is no earlier reading and nobody is flagged.

### Q9. Which test keeps a fall only when the two readings before September are July and August?

The key is d, `monthly["month_num"] - monthly["month_num_2"] == 2`. The months are distinct and
sorted, so if the reading two back is exactly two months back, the one between is August.

- a, `>= 2`: allows a gap of three months or more.
- b, `monthly["month_num_2"].notna()`: counts a skipped month as a fall, Wednesday's holiday member.
- c, `<= 3`: allows one missing month.

### Q10. Which call builds the slide's view, months down the side and one column per segment?

The key is b, `index="month", columns="segment"`, with `aggfunc="sum"`. Each point on the slide is a
month's total spend in a segment.

- a, `index="segment", columns="month"`: segments on the rows, when the slide wants months.
- c, no `aggfunc`: `pivot_table` averages by default, so each point is a typical order and the view
  falls short of the warehouse's total.
- d, `aggfunc="count"`: counts orders instead of adding their value.

### Q11. Which guard stops a table that has stopped being one row per customer?

The key is a, `t["customer_id"].is_unique`. The check writes one customer's id over another
customer's row, so the rows and the spend stay right and only this guard can stop the copy.

- b, `len(t) == t["customer_id"].count()`: compares the rows with the ids present, which a repeated
  id passes.
- c, `t.duplicated().sum() == 0`: looks for whole rows repeated, and an id written over another
  customer's row repeats the id without repeating the row.
- d, `t["customer_id"].notna().all()`: a repeated id is not a missing one.

### Q12. Which guard catches recency counted to the wrong date?

The key is c, `t["recency_days"].min() == 0`. Somebody ordered on the data's last day, so counted to
that day the smallest recency is 0, and counted to any other day it is not. The check counts a copy
to 21 September, a week before the data ends.

- a, `t["recency_days"].max() <= 180`: passes on that copy, whose oldest recency is 173 days. It
  would catch a count to 19 October here only because the quietest customer last ordered on
  1 April, exactly 180 days before the data ends, so it works by luck.
- b, `t["recency_days"].notna().all()`: fails on every honest run, since customers who never ordered
  have no recency.
- d, `t["as_of"].nunique() == 1`: passes whatever single date was used.

### Q13. Which query should step 1 read instead, so the three numbers still arrive?

A design item: all four queries return the three numbers' columns, and only one returns the right
numbers at any size. The key is b, the `GROUP BY customer_id` query with `max`, `count` and `sum`.
The warehouse groups the orders and sends one row per customer who ordered, 301 today, so what it
sends grows with the customers and never with the orders, and pandas merges that answer onto the
list as before. The check compares the answer with step 1's `groupby` customer by customer, so it is
also a second route to the three numbers.

- a, `avg(amount) AS spend`: sends each customer's average order as their spend, chapter 3's trap
  written in SQL.
- c, the same query `WHERE order_date >= DATE '2026-07-01'`: sends only Q2, so every number covers
  half the period.
- d, the customer list `LEFT JOIN` the orders with `count(*)`: counts rows, so the 39 customers who
  never ordered come back with a frequency of 1.

## Which wrong outputs does the debrief replay, and which check catches each?

| The wrong output | The step it came from | The check that catches it |
|---|---|---|
| 301 rows | The table started from the customers who ordered | Rows against the customer list |
| No customer with a frequency of 0 | A missing count left missing | Fill 0 on purpose, then count |
| Reached customers who read as never reached | A repeated customer dropped entirely | The second count from the raw feed |
| A merge that stops with a `MergeError` | A repeat judged by customer and date together | The promise on the merge |
| A win-back list that grows each Monday | Recency counted to the day the notebook runs | The smallest recency is 0 |
| A falling flag on a customer who never fell | The earlier readings taken without the customer | The flag against Wednesday's query |
| A view short of the warehouse | `pivot_table`'s default | The view's total against the orders |

## Where does a scheduled table that refuses to ship come up at work?

Public Health England's statement of 4 October 2020 said "15,841 cases between 25 September and 2
October were not included in the reported daily COVID-19 cases"; The Register traced the cause to
lab results "automatically fetched in CSV format" and stored in the older .XLS format "that limited
the number of rows to 65,536 per spreadsheet" (The Register, 5 October 2020; both checked 1 Oct
2026). A refresh whose guards compared rows in with rows out would have refused the first short
table.

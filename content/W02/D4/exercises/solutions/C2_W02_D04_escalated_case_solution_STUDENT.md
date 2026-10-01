# Which answers hold in the escalated case on building the whole Monday table alone, and why?

Answers: 1c 2b 3c 4d 5c 6b 7a 8b 9d 10b 11a 12d 13b

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
| 5 | Two runs give one table; a repeated customer stops the run; the grouped query sends 301 rows, matching step 1 customer by customer | The refresh refuses a broken table, and the table survives orders in crores |

The four numbers to post are 340, Rs 19,84,00,000, 130 and 111.

## Why does each of the thirteen keys hold, from the table's starting frame to the query for crores?

### Q1. Which frame should the table start from?

The key is c, `customers`. The table is one row per customer on the list, so the list is its
starting frame and the orders only add columns.

- a, `orders`: one row per order, 1,000 rows.
- b, `rfm`: only the 301 customers who ordered, so the 39 who never ordered have no row.
- d, `exposure.drop_duplicates("customer_id")`: only the customers the sale reached.

### Q2. What goes in the frequency of a customer who never ordered?

The key is b, `table["frequency"].fillna(0).astype("int64")`. No orders means a count of 0, said on
purpose, and the column goes back to whole numbers.

- a, `table["frequency"]`: leaves 39 missing counts, which a filter for 0 never finds.
- c, `table["frequency"].fillna(table["frequency"].median())`: invents orders for customers who
  placed none.
- d, `table["frequency"].dropna()`: `assign` lines the shorter column up by index and leaves the
  gaps missing, so nothing changes.

### Q3. After sorting by date, which argument applies the growth team's rule for a customer the feed names twice?

The key is c, `keep="first"`. After the sort by date, the first row is the earliest exposure.

- a, `keep="last"`: keeps a later date wherever a customer repeats.
- b, `keep=False`: drops every copy of a repeated customer, so they read as never reached.
- d, `ignore_index=True`: renumbers the rows and drops nothing.

### Q4. Which validate value should the merge carry?

The key is d, `"one_to_one"`. The table holds each customer once and so does the feed after the
rule, and the merge should stop if either ever stops being true.

- a, `"one_to_many"`: allows repeats on the feed's side, the side that repeats.
- b, `"many_to_many"`: allows anything.
- c, `None`: checks nothing.

### Q5. Which count, sharing no code with the rule or the merge, should equal the reached flags?

A design item. The key is c, `exposure["customer_id"].nunique()`. It counts the distinct customers
in the raw feed with no sort, no rule and no merge, so a wrong `keep` or a merge that lost a customer
makes it disagree with the flags.

- a, `len(first_touch)`: counts the rows the rule kept, so it shares the rule; with `keep=False` it
  would shrink with the flags and still agree.
- b, `int(table["exposed_date"].notna().sum())`: the merged table's own column, which is the flags
  again.
- d, `len(exposure)`: one row for every time the platform sent a customer, so it disagrees with a
  correct table.

### Q6. Which date is the table's as-of date, the date recency is counted to?

The key is b, `orders["order_date"].max()`, 28 September 2026, the last date the data covers.

- a, `pd.Timestamp.today()`: counts to the day the notebook runs, so every customer looks staler
  than the data says and the list grows each Monday with nothing new loaded.
- c, `orders["order_date"].min()`: counts from 1 April, so every recency is negative.
- d, `pd.Timestamp.today().normalize()`: today at midnight, the wall-clock date again.

### Q7. Which condition flags a lapsed customer?

The key is a, `table["recency_days"] > 60`. A customer who never ordered has no recency, so the
comparison is false for them and they stay off the win-back list.

- b, `table["frequency"] == 0`: flags the customers who never ordered, who belong on the first-order
  list.
- c, `table["recency_days"].isna()`: flags the same customers as b.
- d, `(pd.Timestamp.today() - table["last_order"]).dt.days > 60`: the wall-clock count again.

### Q8. Which expression gives each row's previous monthly reading?

The key is b, `monthly.groupby("customer_id")["spend"].shift(1)`. The previous reading belongs to the
same customer, which is `LAG` with `PARTITION BY customer_id`.

- a, `monthly["spend"].shift(1)`: reads the previous row even when it belongs to another customer,
  Wednesday's `LAG` without `PARTITION`.
- c, `monthly.groupby("month_num")["spend"].shift(1)`: compares different customers in the same
  month.
- d, `monthly.groupby(["customer_id", "month_num"])["spend"].shift(1)`: puts each customer-month in
  a group of its own, so there is no previous row.

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

The key is a, `t["customer_id"].is_unique`.

- b, `len(t) > 0`: passes on a table whose rows have doubled.
- c, `t["spend"].sum() > 0`: passes on the same table.
- d, `t["customer_id"].notna().all()`: a repeated id is not a missing one.

### Q12. Which guard catches recency counted to the wrong date?

The key is d, `t["recency_days"].min() == 0`. Somebody ordered on the data's last day, so counted to
that day, the smallest recency is 0.

- a, `t["recency_days"].max() <= 180`: passes on a table counted to the wrong day as long as nobody
  is older than 180 days.
- b, `t["recency_days"].notna().all()`: fails on every honest run, since customers who never ordered
  have no recency.
- c, `t["as_of"].nunique() == 1`: passes whatever single date was used.

### Q13. Which query should step 1 read instead, so the three numbers still arrive?

A design item. The key is b, the `GROUP BY customer_id` query with `max`, `count` and `sum`. The
warehouse groups the orders and sends one row per customer who ordered, 301 today and about as many
however many crores of orders sit behind them, and pandas merges that answer onto the list as
before. The check compares the answer with step 1's `groupby` customer by customer, so it is also a
second route to the three numbers.

- a, every order's customer, date and amount: still sends every order, only with fewer columns.
- c, the orders from July: sends only Q2, so every number covers half the period.
- d, the count alone: drops the last order date and spend.

## Which wrong outputs does the debrief replay, and which check catches each?

| The wrong output | The step it came from | The check that catches it |
|---|---|---|
| 301 rows | The table started from the orders | Rows against the customer list |
| No customer with a frequency of 0 | A missing count left missing | Fill 0 on purpose, then count |
| Customers reached who read as never reached | A repeated customer dropped entirely | The second count from the raw feed |
| A win-back list that grows each Monday | Recency counted to the day the notebook runs | The smallest recency is 0 |
| A falling flag on a customer who never fell | The previous row read without the customer | The flag against Wednesday's query |
| A view short of the warehouse | `pivot_table`'s default | The view's total against the orders |

## Where does a scheduled table that refuses to ship come up at work?

Public Health England's statement of 4 October 2020 said "15,841 cases between 25 September and 2
October were not included in the reported daily COVID-19 cases"; The Register traced the cause to
lab results "automatically fetched in CSV format" and stored in the older .XLS format "that limited
the number of rows to 65,536 per spreadsheet" (The Register, 5 October 2020; both checked 1 Oct
2026). A refresh whose guards compared rows in with rows out would have refused the first short
table.

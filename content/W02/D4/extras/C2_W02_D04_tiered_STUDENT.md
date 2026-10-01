# Which extra fits you tonight: rebuilding the table in four checked moves, or adding a channel flag, a run log and a SQL twin?

Both are optional and neither is graded. Pick the one that matches where you finished the escalated
case: with a check still failing, take the recovery; with every check passing, take the stretch.

Kalpa Retail's growth team wants one table, one row per customer, refreshed every Monday from the
warehouse in pandas. The warehouse holds 1,000 orders from April to September 2026, each with its
channel (the app, the website or a store), and a customer list of 340 customers. Recency is the days
from a customer's last order to the table's as-of date, the last date the data covers, 28 September
2026; frequency is the count of orders; spend is the value of the orders at the prices charged.

---

## Recovery: can you rebuild the table in four moves, each with its check?

This one is for you if the escalated case ended with a check you could not make pass.

**Who needs the answer.** You, before Friday, which starts from the table this builds. Rebuild it one
checked move at a time, so that when Friday builds on it you can say which move made each of its
numbers.

**The questions on the way.**

1. Did all 1,000 orders arrive?
2. Do the loop and `groupby` agree, and why do both hold 301 customers?
3. Does the table hold all 340, with the counts filled on purpose?
4. Is recency counted to the data's last date?

### Did all 1,000 orders arrive?

Read the orders with `pd.read_sql` and print `len(orders)`. It is 1,000; if it is not, the warehouse
is not loaded, and `bash .devcontainer/load_warehouse.sh` in the terminal rebuilds it.

### Do the loop and `groupby` agree, and why do both hold 301 customers?

Write Week 1's loop that totals spend per customer in a dictionary, then
`orders.groupby("customer_id")["amount"].sum()`, and check that the two agree for every customer.
Say aloud why both hold 301 entries: each only meets customers who appear in an order.

### Does the table hold all 340, with the counts filled on purpose?

Merge the totals onto `customers` with `how="left"` and `validate="one_to_one"` and check 340 rows.
Print `dtypes`, find the count that became `float64`, fill it with 0 on purpose and turn it back into
whole numbers. Count the customers with a frequency of 0: 39.

### Is recency counted to the data's last date?

Compute `AS_OF = orders["order_date"].max()` and recency from it, and check that the smallest recency
is 0. Then count the 60-day win-back list both ways, from `AS_OF` and from `pd.Timestamp("2026-10-19")`,
and say in one sentence to the growth team why the second list is 55 customers longer and what the 21
days between the two dates say about the data's age.

When all four pass, rerun the escalated notebook from a fresh kernel.

---

## Stretch: can the table carry a third flag, a run log and a SQL twin?

This one is for you if every check in the escalated case passed.

**Who needs the answer.** Kavya Nair, the team's senior analyst, who asks what the table would need
before the growth team relies on it for more than two flags.

> "The growth team will ask for a channel flag next, and Finance will ask how each Monday's run
> differed from the last. Show me both, and show me the table built a second way."

**The questions on the way.**

1. Which customers changed their main channel from Q1 to Q2, and what happens on a tie?
2. What should each run log about itself, and do two runs log the same?
3. Does one SQL query build the same table as pandas?
4. Can you answer the day's design question in under a minute?

### Which customers changed their main channel from Q1 to Q2, and what happens on a tie?

Build each customer's main channel per quarter: the channel with the most orders that quarter, from a
`pivot_table` with its `aggfunc` written out. Decide what a tie means and write the rule beside the
code; one rule that works is to call a tie "mixed" and leave it out of the comparison. Then flag
`channel_switch` for customers whose main channel differs between the quarters.

**The check.** 170 customers ordered in both quarters. With ties called "mixed", 77 of them are mixed
in at least one quarter, 93 have a clear main channel in both, and 67 of those 93 switched. A
different tie rule moves these numbers, and your rule is right if you can say it in one sentence.

### What should each run log about itself, and do two runs log the same?

Make the refresh return a second object: a one-row DataFrame with the run's as-of date, its rows, its
spend, the customers reached, and the feed rows the first-touch rule removed. Run it twice on the same
data and prove the two logs are equal. A log is the first thing Finance asks for when this Monday's
numbers differ from last Monday's.

### Does one SQL query build the same table as pandas?

Write the whole customer table as one SQL query against the warehouse: a CTE (a named step inside the
query, written with `WITH`) for each source, the customer list as the spine, `count(o.order_id)` so a
customer with no orders counts 0, and the first exposure per customer from `campaign_exposure`. Read
it into pandas, sort both tables by `customer_id`, and compare them column by column. Where they
differ, find out which one you trust and why.

### Can you answer the day's design question in under a minute?

Record yourself answering "Same question, three tools: how do you choose, and defend one choice?" in
under a minute. Play it back and check that it names who must trust and rerun the number, gives one
size with its number, such as the rows each route moved, and names the fact that would switch the
choice.

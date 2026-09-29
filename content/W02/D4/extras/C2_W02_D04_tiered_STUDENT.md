# Tiered extras: stretch and recovery

Two short paths for after the day. Pick the one that fits where you finished.

---

## Recovery: the table in four moves, slowly

For anyone who left the escalated case with a check failing.

1. **The count.** Read the orders with `pd.read_sql` and print `len(orders)`. It is 1,000; if it is
   not, the warehouse is not loaded, and `bash .devcontainer/load_warehouse.sh` rebuilds it.
2. **The groupby, beside the loop.** Write the Week 1 loop that totals spend per customer in a
   dictionary, then `orders.groupby("customer_id")["amount"].sum()`, and check that the two agree
   for every customer. Say aloud why both have 301 entries.
3. **The spine.** Merge the totals onto `customers` with `how="left"` and `validate="one_to_one"`.
   Check 340 rows. Print `dtypes`, find the column that became `float64`, and fill it with 0 on
   purpose.
4. **The date.** Compute `AS_OF = orders["order_date"].max()` and recency from it. Check that the
   smallest recency is 0. Then compute it from `pd.Timestamp("2026-10-19")` and say, in one
   sentence to the growth team, why their win-back list would have been 55 customers too long.

When all four pass, rerun the escalated notebook from a fresh kernel.

---

## Stretch: the table grows up

For anyone who finished the escalated case with every check passing.

1. **A third flag.** Add `channel_switch`: a customer whose Q2 orders came mostly through a
   different channel from their Q1 orders. Build it with two `pivot_table` calls stating `aggfunc`,
   decide what "mostly" means when a customer is tied, and write the tie rule beside the code.
2. **The refresh log.** Make `build_customer_table` return a second object: a one-row DataFrame
   with the run's as-of date, row count, spend total, reached count and the number of feed rows the
   first-touch rule removed. Run it twice and prove the logs agree.
3. **The SQL twin.** Write the whole customer table as one SQL query against the warehouse, with a
   CTE per source, and compare it to your pandas table with `DataFrame.equals` after sorting both.
   Where they differ, find out which tool you trust and why.
4. **The interview answer.** Record yourself answering "Same question, three tools: how do you
   choose, and defend one choice?" in under a minute, and check it names who must trust the number.

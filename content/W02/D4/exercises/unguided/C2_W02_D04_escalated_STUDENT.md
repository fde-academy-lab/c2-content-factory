# The escalated case: the Monday table, end to end

Sixty minutes, alone, no hints. The notebook is `notebooks/C2_W02_D04_hands_on_STUDENT.ipynb`;
the solution opens at the debrief.

> **The client's ask.** The growth team: "One table, one row per customer, refreshed every
> Monday: how recently each customer bought, how often, how much, their segment, whether the
> monsoon sale reached them, and last week's flags. And one view of it by month we can put on a
> slide. Marketing's analysts will work from it all week, so it has to be right every Monday
> without anyone rebuilding it."

**What you hand in.**

1. The notebook, run top to bottom from a fresh kernel, with every check passing.
2. The table exported to `output/C2_W02_D04_customer_table_STUDENT.csv`, which you bring to
   Friday's Excel day.
3. One line: your ten notebook letters, then the five letters below, then the four numbers the
   last cell prints.
4. Three sentences to the growth team: what the table holds, as of which date, and what stops
   the refresh.

Post the letters in this shape, which is a format and not a hint:

```
Post exactly this shape: notebook xxxxxxxxxx, brief xxxxx, numbers n n n n
```

---

### Part 1. The spine

Build one row per customer on the warehouse's customer list, with the last order date, the
number of orders and the spend, and recency in days measured so that two runs on the same data
agree. A customer with no orders has frequency 0 and spend 0.

A colleague's first attempt returns 301 rows. What went wrong?

a) The warehouse lost 39 customers somewhere between Monday's count and today
b) The groupby should have used `dropna=False` to keep them
c) It was built from the orders, so customers with no orders never formed a group
d) The merge was an inner join where a left join was meant, so 39 customer rows were lost

### Part 2. The exposure

Attach the monsoon sale's exposure feed from `data/C2_W02_D04_exposure_STUDENT.csv`, one row per
customer, with the first date the sale reached them and a column saying whether it did. The
merge must stop the refresh if the feed ever breaks the one-row rule.

Suppose the merge raises `MergeError` on a Monday run. What is the right next move?

a) Change `how` to `"inner"`, so only the reached customers are merged and the rest are safe
b) Read the repeated keys, apply one exposure per customer by first date, keep validate
c) Remove `validate` for today and note the problem for next week's refresh instead
d) Use `validate="many_to_many"`, which describes a feed that repeats customers exactly

### Part 3. The flags

Two flags. **Lapsed:** no order in the 60 days to the data's last date; a customer who never
ordered is not lapsed. **Falling:** Q2 monthly spend fell in two months running, the same members
Wednesday's LAG query flags, which the notebook runs beside yours.

A falling flag appears on a customer whose only Q2 order was in August. What caused it?

a) A customer with one month has nothing to fall from, so the flag must be a display error
b) Q2 was filtered after the flag, so earlier months leaked in and set it
c) The comparison used `>` where `<` was meant, so rises were flagged instead of falls
d) `shift(1)` ran without `groupby("customer_id")`, so it read another customer's month

### Part 4. The view

One reshaped view for the growth team's slide: spend by month and segment, months as rows so each
segment reads as a line. It must add back to Monday's book.

A draft of the slide shows Retail-Plus in September at Rs 2,708. What happened?

a) The default `aggfunc` ran, so the cell is the average order, not the spend
b) The pivot was indexed by customer, so the cell is one member's September spend
c) Only one week of September was loaded, so the month is incomplete in the warehouse
d) The pivot counted orders in the month, so the cell is a count shown as rupees

### Part 5. The refresh

Wrap the whole build in one function that reads the warehouse and the feed and returns the table,
with guards inside it. Run it twice and prove the two runs are identical.

Two runs a week apart, on data that did not change, give different win-back lists. Which line is
responsible?

a) The exposure merge, because the feed is read from a file that can be edited by hand
b) Recency measured from `pd.Timestamp.today()` instead of the data's last date
c) `fillna(0)` on frequency, because zeros change the lapsed flag between runs
d) The groupby, because groups come back in a different order on every run

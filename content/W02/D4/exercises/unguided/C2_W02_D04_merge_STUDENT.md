# Round 2 set: the exposure merge

Fifteen minutes, alone, after round 2. The numbers in these items belong to feeds and tables
other than the ones on your screen, so the answer comes from the mechanism rather than from
memory of the demonstration.

Post one line, seven letters in item order, no spaces:

```
Post exactly this shape: xxxxxxx
```

---

### Q1

Kalpa Logistics keeps a customer table of 500 accounts, one row each. A campaign feed of 250 rows
names 240 distinct accounts, all on the table. How many rows does
`table.merge(feed, on="account_id", how="left")` return?

a) 500, because a left merge keeps the left table's rows exactly as they are
b) 740, the two tables stacked one on top of the other
c) 510
d) 250, the rows of the feed, since the feed decides who was reached

### Q2

The growth team wants next Monday's refresh to stop, rather than ship, if the exposure feed ever
names a customer twice. Which argument does that?

a) `validate="one_to_one"` on the merge
b) `how="inner"` on the merge, so unmatched customers leave
c) `indicator=True` on the merge, so every row is labelled by its source
d) `sort=True` on the merge, so repeated customers sit next to each other

### Q3

After the merge, the table's spend total reads Rs 19,84,52,300, where Monday's book is
Rs 19,84,00,000, and the row count rose. What does that tell the marketing lead's analyst?

a) The feed carried new orders, so the book grew by Rs 52,300 over the weekend
b) A rounding difference from the float dtype, safe to ignore below one lakh
c) The merge added customers who were not on the list, with their own spend
d) Some customers' rows repeated, so their spend is counted more than once

### Q4

The refresh raises `MergeError: Merge keys are not unique in right dataset; not a one-to-one
merge`. What does the analyst do first?

a) Switch to `validate="many_to_many"` so the refresh completes on time for Marketing
b) Look at the repeated keys, find why the platform sent them, and set a rule
c) Remove `validate` for this week and add it back once the feed is fixed
d) Drop the repeated customers entirely, since their exposure cannot be trusted

### Q5

The campaign platform re-sends a batch, so some customers appear twice, on 3 August and 11 August.
The marketing lead's question is "did the sale reach them". Which rule keeps one row per
customer and answers it?

a) Sort by exposure date and keep the first row per customer
b) Keep the last row, since the latest exposure is the one that counts
c) Keep both rows and divide each customer's spend by the number of rows
d) Keep only customers who appear once, since only they are certain

### Q6

The reach table says 107 customers were reached per `groupby("segment")`, while the feed names 130
distinct customers. What most likely happened?

a) 23 customers in the feed are not in the warehouse, so they were rightly left out
b) The feed's 23 extra rows are repeats, so 107 is the true reach
c) 23 reached customers have no segment in that table, and groupby dropped them
d) groupby counts only customers who bought, since it groups the order rows

### Q7

The marketing lead now asks for the customers the sale did not reach, as a list. Which merge gives
it most directly?

a) `table.merge(first_touch, how="inner")`, then keep what is left over
b) `table.merge(first_touch, how="left", indicator=True)`, keep `"left_only"`
c) `first_touch.merge(table, how="left")`, keep rows with a segment
d) `table.merge(first_touch, how="outer")`, then keep the rows where both sides match

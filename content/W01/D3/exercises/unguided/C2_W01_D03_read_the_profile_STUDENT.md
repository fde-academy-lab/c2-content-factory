# Mid-session: read the profile, decide what you trust

Six items. Post one line with your six letters in item order.

```
Post exactly this shape: xxxxxx
```

---

## Two profiles of the same field, from two exports

| | Export A | Export B |
|---|---|---|
| Rows | 201 | 201 |
| `order_id` present | 201 | 201 |
| `order_id` distinct | 186 | 201 |
| `amount` present | 201 | 201 |
| `amount` convertible | 200 | 201 |
| `status` present | 200 | 201 |
| `status` distinct | 3 | 1 |

---

## Q1. Which export would you analyse first?

Which one?

a) A, because its defects are visible and countable
b) B, because it has no missing values and everything converts cleanly
c) Either, since the two have the same number of rows in them
d) Neither until the source team explains where each of them came from

---

## Q2. Export B's `status` has one distinct value. What is that?

Which one?

a) Good news, since a single status means the data is internally consistent
b) Expected, because most orders in a healthy retailer are delivered anyway
c) A finding, and probably a filter or a default applied at export
d) Irrelevant, because status is not used in the revenue calculation

---

## Q3. Export A has 201 rows and 186 distinct ids. What does that alone prove?

Which one?

a) That fifteen rows are duplicates and can be removed straight away
b) That some ids appear more than once
c) That the export process ran twice over part of the date range
d) That revenue is overstated by exactly the amount those rows carry

---

## Q4. Which of these belongs in the rejects log rather than in clean?

Which one?

a) An order of Rs 4,80,000 from a corporate customer, four times the next largest
b) A row whose `order_date` is written as `12/05/2026` when the rest use dashes
c) A row for a customer who appears only once in the whole file
d) A row whose `order_id` is the text `order_id`

---

## Q5. You default every failed conversion to zero. What have you lost?

Which one?

a) Nothing, because zero is the safest possible value for an unknown amount
b) The row count, since defaulted rows are silently dropped from the output
c) How many rows failed, and why
d) The data types, because the whole column becomes an integer afterwards

---

## Q6. Clean plus rejected is three less than input. What is your next move?

Which one?

a) Find the three rows, because a pass that loses rows silently loses others
b) Report it as a rounding difference, since three rows in 201 is immaterial
c) Adjust the rejected count by three so the equation balances properly
d) Re-read the file, because the row count was probably read wrongly first

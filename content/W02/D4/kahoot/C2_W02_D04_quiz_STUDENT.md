# Can you make the day's eight calls in seconds, from what groupby does to how many rows a top fifty ships?

Eight items, ungraded, scored on correctness and speed together. Seven are today's, and the last is
the return question from Wednesday, one level up. Item 2 uses Kalpa's own four segments and two
quarters; the 1,000 customers and 1,120 rows in item 6 are invented.

The day built Kalpa Retail's growth team one table, one row per customer, refreshed every Monday from
the warehouse in pandas: recency, frequency and spend for each of the 340 customers on the list,
whether the monsoon sale reached them, and the flags the growth team acts on. On the way it attached
the sale's feed to the customer list, read Retail-Plus's spend month by month, asked one question in
three tools, and built a refresh the growth team can leave to run. A merge is pandas' join of two
tables on a key column.

**Who needs the answer.** The trainer, closing the day. Each item is one of the day's calls made in
seconds, and an item most of the room misses is the one to say again before the room leaves.

**The questions on the way.**

- What does `groupby` do to the orders when the table wants one row per customer?
- What shape does `agg` give with two measures on four segments and two quarters?
- Which merge argument raises on repeated keys, and with which error?
- Which of `pivot` and `melt` widens a table, and which lengthens it?
- Where does Finance's Monday number live?
- Why did a left merge of 1,000 customers return 1,120 rows?
- What does `pivot_table` put in a cell when no `aggfunc` is given?
- Wednesday's business wants ties ranked the same: which function, and how many rows might a top fifty
  ship?

---

## Q1. What does `groupby` do to the orders when the table wants one row per customer?
*Tests: the split-apply-combine sentence, said about the Monday table.*

- Splits the customers by segment, sorts each, and combines one list
- Splits the orders by customer, applies the measures, one row each  <- correct
- Sorts the orders by customer and keeps each customer's first order
- Gives every order its customer's totals and keeps all 1,000 rows

---

## Q2. What shape does `agg` give with two measures on four segments and two quarters?
*Tests: two group keys give one row per pair that exists, and each named measure is a column.*

- 4 rows by 2 columns, one row per segment
- 2 rows by 8 columns, one row per quarter
- 8 rows by 2 columns, one per segment and quarter  <- correct
- 1,000 rows by 2 columns, one row for every order

---

## Q3. Which merge argument raises on repeated keys, and with which error?
*Tests: `validate="one_to_one"` stops the merge with a `MergeError` when either side repeats a key, so no wrong table is built.*

- `validate="one_to_many"`, raising a `MergeError` when the feed repeats a key
- `how="left"`, raising a `MergeError` when the feed repeats a key
- `validate="many_to_many"`, raising a `KeyError` on the repeated key
- `validate="one_to_one"`, raising a `MergeError` on the repeated key  <- correct

---

## Q4. Which of `pivot` and `melt` widens a table, and which lengthens it?
*Tests: a reshape changes the question a table answers, a comparison or a trend.*

- `pivot` widens and `melt` lengthens  <- correct
- `pivot` lengthens and `melt` widens
- Both widen, and `melt` also sorts the rows
- Both lengthen, and `pivot` also sums the cells

---

## Q5. Where does Finance's Monday number live?
*Tests: a number lives where the people who rerun it can run it.*

- pandas, since it computes the number fastest on this data
- SQL, a query Finance reruns in the warehouse each Monday  <- correct
- Plain Python, since every step of a loop can be read
- Any of the three, since all of them give the same number

---

## Q6. Why did a left merge of 1,000 customers return 1,120 rows?
*Tests: a left merge copies a row once for every match the right side holds.*

- Each customer with no match in the feed gained an empty row
- The left merge added the feed's unmatched rows to the table
- Some customers appear more than once in the campaign feed  <- correct
- Each of 120 reached customers gained a second row for its date

---

## Q7. What does `pivot_table` put in a cell when no `aggfunc` is given?
*Tests: the default is the mean, which hides how often members bought.*

- The member's total spend in that month
- The member's average order in that month  <- correct
- The number of orders the member placed that month
- The member's largest single order in that month

---

## Q8. Wednesday's business wants ties ranked the same: which function, and how many rows might a top fifty ship?
*Tests: Wednesday's tie rule, answered from what the function does at the boundary.*

- `ROW_NUMBER`, and exactly fifty rows every time
- `DENSE_RANK`, and fewer than fifty rows when two members tie
- `NTILE`, and fifty rows split evenly across the ties
- `RANK`, and more than fifty when members tie at the boundary  <- correct

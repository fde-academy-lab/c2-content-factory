# Kahoot, Week 2 Thursday

Eight items, ungraded, scored on correctness and speed together. The last item returns to
Wednesday, one level up.

Each item names what it tests, so an item dropped for time says what was lost.

---

## Q1. groupby in one sentence: split, apply, combine on what?
*Tests: the split-apply-combine sentence, said about the Monday table.*

- Split the customers by segment, apply a sort, combine into one list
- Split the orders by customer, apply the measures, combine one row each  <- correct
- Split the table by column, apply a dtype to each, combine the columns back
- Split the orders by date, apply a filter, combine into one month

---

## Q2. agg with two measures on 4 segments and 2 quarters: what shape?
*Tests: two group keys give one row per pair, and each named measure is a column.*

- 4 rows by 2 columns, one row per segment
- 2 rows by 8 columns, one row per quarter
- 8 rows by 2 columns  <- correct
- 1,000 rows by 2 columns, one row per order

---

## Q3. Which merge argument raises on repeated keys, and with which error?
*Tests: validate= is the row-count check made loud.*

- `how="inner"`, raising KeyError on the repeated key
- `indicator=True`, raising ValueError on the repeated key
- `on=`, raising TypeError when a key appears twice
- `validate="one_to_one"`, raising MergeError  <- correct

---

## Q4. pivot against melt: which widens and which lengthens?
*Tests: the reshape changes the question a table answers.*

- pivot widens and melt lengthens  <- correct
- pivot lengthens and melt widens
- both widen, and melt also sorts
- both lengthen, and pivot also sums

---

## Q5. Finance's Monday number: plain Python, SQL or pandas?
*Tests: the number lives where the people who audit it can rerun it.*

- pandas, because it is the fastest way to compute it
- SQL, because Finance can rerun it at the source  <- correct
- plain Python, because every step can be read
- Any of them, since all three give the same number

---

## Q6. 1,000 customers in, 1,120 rows out of a left merge. What happened?
*Tests: a left merge multiplies rows when the right side repeats keys.*

- 120 new customers arrived in the feed overnight
- The left merge added the feed's unmatched rows
- Some customers appear more than once in the feed  <- correct
- pandas duplicated rows at random during the merge

---

## Q7. pivot_table with no aggfunc on member spend: each cell is what?
*Tests: the default aggfunc is the mean, which hides how often members bought.*

- The member's total spend in that month
- The member's average order in that month  <- correct
- The number of orders the member placed that month
- The member's largest order in that month

---

## Q8. Return to Wednesday: ties must rank the same. Which function, and how many rows might "the top fifty" ship?
*Tests: RANK gives tied members the same rank, so a tie at the boundary ships more than fifty.*

- ROW_NUMBER, and exactly fifty rows every time
- DENSE_RANK, and fewer than fifty rows when there are ties
- NTILE, and fifty rows split across the ties evenly
- RANK, and more than fifty when the fiftieth place is tied  <- correct

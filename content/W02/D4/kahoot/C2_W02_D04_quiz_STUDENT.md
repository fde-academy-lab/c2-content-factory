# Thursday's Kahoot: groupby, merge, reshape

Ungraded. Seven questions.

## Q1. groupby, in the split-apply-combine sentence. Split on what?

a) The column you name as the key <- correct
b) The index of the frame as it stands
c) Whichever column holds the values
d) The order the rows arrived in

## Q2. `.agg(n=("order_id","count"), m=("amount","sum"))` on 4 segments. Output shape?

a) 8 rows, 2 columns
b) 4 rows, 1 column
c) 4 rows, 2 columns <- correct
d) 2 rows, 4 columns

## Q3. Which merge argument raises on duplicate keys, and which error?

a) `how="inner"`, raising a KeyError
b) `indicator=True`, raising a ValueError
c) `on=`, raising a MergeError
d) `validate=`, raising a MergeError <- correct

## Q4. pivot against melt: which widens?

a) `melt`, which spreads the values into columns
b) `pivot_table`, which spreads values to columns <- correct
c) Both of them, depending on the aggfunc chosen
d) Neither, since both only ever reorder the rows

## Q5. Finance's Monday number: which tool, and why?

a) pandas, since the analysts already read it daily
b) SQL in the warehouse, since it is auditable <- correct
c) Plain Python, since it can be read aloud slowly
d) Excel, since Finance already opens spreadsheets

## Q6. The customer table has 340 rows and the merge returned 346. What happened?

a) Six customers were added by the merge itself
b) Six rows were duplicated in the left frame
c) Six keys appear more than once on the right <- correct
d) Six customers have a null in the merge key

## Q7. Return question, one level up

Yesterday the business said ties rank the same. Which function, and how many rows might a top
fifty ship?

a) DENSE_RANK, and it ships exactly fifty rows
b) ROW_NUMBER, and it ships exactly fifty rows
c) RANK, and it can ship more than fifty <- correct
d) Any of them, since a tie is rare in practice

## Trainer note

Q4 is worth a follow-up. A room that gets it right can usually still not say what `melt` returns
when the wide frame has gaps, and the honest answer is that the round trip is not the identity:
melting a pivot gives you more rows than you started with, because every empty cell becomes a row.

# Solutions: predict the shape

Answers: 1b 2d 3a 4a

## Q1. A Series of 301 values

Selecting a single column with `["amount"]` before aggregating gives a Series, indexed by the
grouping key. Using `[["amount"]]` with double brackets would give a DataFrame instead, which is
the distinction that catches people.

301 rather than 340, because 39 customers on the books placed no order in the two quarters and
therefore form no group.

## Q2. 8 rows

Four segments times two quarters, and every pair occurs in this book. Grouping by two columns
makes one group per distinct **pair**.

Option c is the trap worth thinking about: pandas only creates groups for pairs that exist in the
data, so if a segment had no Q2 orders the result would be 7 rows and nothing would tell you a
pair was missing. That is a question about the data rather than about `groupby`.

## Q3. One row per customer, three columns, gaps as NaN

`index` becomes the rows, `columns` becomes the columns, `values` fills the grid. A customer who
bought in July and September and not August gets a NaN in the August cell.

Those NaNs are information. They mean no order that month, which is different from a zero you put
there yourself, and `fillna(0)` erases the distinction.

## Q4. The original long frame, gaps included as NaN rows

`melt` reverses the widening, so every cell of the grid becomes a row, including the empty ones.
The result is therefore **longer** than the frame you started with, because the original long
frame had no row for a month a customer skipped and the wide frame gave that gap a cell.

Round-tripping through a pivot and back is not the identity, and that surprises most people once.

Option d is wrong for a small reason worth knowing: `melt` defaults `value_vars` to every column
not named in `id_vars`, so it runs perfectly.

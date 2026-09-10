# Day 3, E2. Mid-session: which dataset would you trust

Drop point: the close of the first block, after the coercion demonstration. About 15 minutes, working alone.

Two profiles of the same fifty Kalpa Retail orders. A is the file as it arrived. B is the same file after somebody replaced every unusable value with a stated default of zero.

```
field         A present  A converts  A distinct   |  B present  B converts  B distinct
order_id             50           0          49   |         50           0          49
segment              50           0           4   |         50           0           4
amount               48          44          46   |         50          50          41
status               50           0           3   |         50           0           3
discount             11          11           9   |         50          50          10
```

Fifteen items. Post one line at the end, in this shape, using your own letters:

```
1b 2d 3a 4c 5b 6d 7a 8c 9b 10d 11a 12c 13b 14d 15a
```

---

## Item 1

Which single count is lower in B than in A?

a) distinct on amount
b) present
c) converts
d) distinct on order_id

## Item 2

What does that fall mean?

a) Rows were deleted from the bottom of the file
b) Real values became one repeated value
c) The file was sorted differently
d) A column was dropped

## Item 3

In A, how many amount values are present and unusable?

a) 2
b) 6
c) 4
d) 44

## Item 4

Why is that different from the number of rows the cleaning pass rejects?

a) It is not different at all, since both numbers are four
b) The pass rejects on status rather than on amount
c) The pass rejects two rows twice
d) Two more rows have no amount, so six are rejected

## Item 5

`discount` in B reads present 50, converts 50, distinct 10. What happened?

a) Absence became an indistinguishable zero
b) Nine of the real discounts were deleted outright
c) The field was renamed
d) The pass converted the field to text

## Item 6

Which dataset would you compute an average amount on?

a) B, since every row in it has a usable amount now
b) A, since its values are the ones sent
c) Either, since the average is nearly the same
d) Neither, until the source is re-sent

## Item 7

`order_id` reads 49 distinct across 50 rows in both profiles. What does that say?

a) One row is empty in that column
b) The field behaves as a category
c) Something repeats here
d) The file is sorted by id

## Item 8

Why did coercing everything not change that number?

a) Because ids are text and the pass touched only numbers
b) Because the duplicate was removed first
c) Because distinct counts ignore text fields
d) Because nothing in order_id was ever replaced

## Item 9

Which of these is the strongest single sentence to put in the decisions log about B?

a) Six amounts and 39 discounts became a zero
b) The file was cleaned before it was analysed
c) All fields now convert without a single failure
d) The dataset is ready for analysis

## Item 10

Somebody hands you B with no A. What can you no longer do?

a) Count the rows in the file
b) Tell an invented zero from a real one
c) Compute a total
d) Read the segment field with any confidence

## Item 11

Which count would you put on a slide to make the argument in one number?

a) present on amount, 48 against 50
b) converts on amount, 44 against 50
c) distinct on amount, 46 against 41
d) rows, 50 against 50

## Item 12

The Student segment holds 12 of the 50 orders. What does that number decide?

a) Nothing at all, since segment is only a category
b) Which rows get rejected
c) The order the file is written in
d) Whether a Student rate is worth quoting

## Item 13

A colleague says the coercion is fine because they wrote it down in a comment in the code. What is the strongest reply?

a) A comment is not a decisions log
b) Comments are not part of the file anybody else reads
c) Comments are hard to keep up to date
d) The code should be self-documenting

## Item 14

Which of these would let a reader reconstruct A from B?

a) The clean file alone
b) Nothing can, once the values are gone
c) The clean file and the row count
d) The clean file, the rejects file and the decisions log

## Item 15

What is the one thing you would add to the profiler after seeing this?

a) A faster loop over the fifty rows
b) A chart of every column
c) A count of rows the pass changed
d) A check that all fields convert

---

Post your fifteen letters on one line in the shape shown at the top. The solution is released at the close of the session.

## Hands-on

The running half is `notebooks/C2_W01_D03_ex2_hands_on_STUDENT.ipynb`, which builds both profiles from the same file and asks you to name the count that fell. Post its four letters on the same line as these fifteen.

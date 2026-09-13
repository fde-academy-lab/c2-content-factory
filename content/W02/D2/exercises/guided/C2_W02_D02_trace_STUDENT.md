# Guided: trace the join before you run it

Done on paper, together, with the two small tables from the board. No database.

## The tables

| order | amount |
|---|---|
| KR-00001 | Rs 9,00,000 |
| KR-00002 | Rs 2,400 |
| KR-00003 | Rs 6,40,000 |
| KR-00004 | Rs 1,800 |
| KR-00005 | Rs 3,100 |
| KR-00006 | Rs 2,100 |

| payment | order | amount |
|---|---|---|
| P-01 | KR-00001 | Rs 5,40,000 |
| P-02 | KR-00001 | Rs 3,60,000 |
| P-03 | KR-00002 | Rs 2,400 |
| P-04 | KR-00003 | Rs 3,84,000 |
| P-05 | KR-00003 | Rs 2,56,000 |
| P-06 | KR-00004 | Rs 1,800 |
| P-07 | KR-00004 | Rs 1,800 |
| P-08 | KR-00006 | Rs 2,100 |
| P-09 | KR-90001 | Rs 2,000 |

## Step 1: count the matches

Go down the order list. Beside each order write how many payment rows carry its id.

## Step 2: predict the row count

A `LEFT JOIN` from orders to payments produces how many rows? Write the number down before
anybody says it aloud.

Then predict the `INNER JOIN` count, and say which order accounts for the difference.

## Step 3: add up the order amount

Write the true booked total first: add the six order amounts.

Now imagine the joined table and add the **order amount** column down all its rows. Two numbers.
Say why they differ, using only the words on your page.

## Step 4: name it

Something multiplied. Say what, and say where it happened. The answer is not "the data has
duplicates", because neither table has a duplicate row.

## Step 5: find the odd one

One payment row does not belong to any order in the list. Which, and what does that mean about
the business rather than about the query?

## Step 6: the fix, still on paper

Roll the payments up to one row per order first. How many rows does that table have? Join it to
the six orders. How many rows out?

Say why that count is guaranteed rather than lucky.

## Before opening a laptop

Write the four-line reconciliation for the small tables:

```
Rows before:
Rows after:
Difference:
Therefore:
```

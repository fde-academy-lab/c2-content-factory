# Guided: the tie, three ways, built together

The head of Retail-Plus said: "Ties matter. If two members spent the same, I want them ranked the
same, and I want to know how many made the top fifty, not forty-nine because of a tie." Before any
list goes to Marketing, the room builds the three ranking functions on one screen, watches what
each does to a tie, counts what each ships at the line, and then applies the rule the head of
Retail-Plus asked for.

This runs in Round 2, about fifteen minutes, with the trainer typing and the room mirroring in
`sql/C2_W02_D03_02_protect_list_STUDENT.sql` or in `notebooks/C2_W02_D03_02_ties_STUDENT.ipynb`.
Steps 1 and 2 use invented members, labelled invented, so the mechanism is visible on six rows.
Step 3 runs on Kalpa's Retail-Core members. Step 4 is yours to run on Retail-Plus.

## Step 1. Three functions, one tie (invented members)

Six invented members, A to F, spent Rs 7,500, Rs 7,500, Rs 6,000, Rs 5,200, Rs 5,200 and
Rs 4,100 in Q2. Before anything runs, copy this table onto paper and fill the three columns with
your prediction.

| Member (invented) | Spend | ROW_NUMBER | RANK | DENSE_RANK |
|---|---|---|---|---|
| A | Rs 7,500 | | | |
| B | Rs 7,500 | | | |
| C | Rs 6,000 | | | |
| D | Rs 5,200 | | | |
| E | Rs 5,200 | | | |
| F | Rs 4,100 | | | |

Then run block 1 of the SQL file together:

```sql
WITH invented (member, spend) AS (
    VALUES ('A', 7500), ('B', 7500), ('C', 6000), ('D', 5200), ('E', 5200), ('F', 4100)
)
SELECT member, spend,
       row_number() OVER (ORDER BY spend DESC, member) AS row_number,
       rank()       OVER (ORDER BY spend DESC)         AS rank,
       dense_rank() OVER (ORDER BY spend DESC)         AS dense_rank
FROM   invented
ORDER  BY spend DESC, member;
```

Compare the output with your paper, column by column. The result is below so that you can check
your copy after the run.

| Member (invented) | ROW_NUMBER | RANK | DENSE_RANK |
|---|---|---|---|
| A | 1 | 1 | 1 |
| B | 2 | 1 | 1 |
| C | 3 | 3 | 2 |
| D | 4 | 4 | 3 |
| E | 5 | 4 | 3 |
| F | 6 | 6 | 4 |

Say out loud, in one sentence each, what the three columns do to A and B: ROW_NUMBER gives them
different numbers and the member name decides which comes first, RANK gives them both 1 and skips
2, and DENSE_RANK gives them both 1 and carries on at 2.

## Step 2. The tie at the line (invented members)

Marketing wants a top four, and the invented members now spent Rs 9,100, Rs 8,800, Rs 8,200,
Rs 7,400, Rs 7,400 and Rs 6,900, so the fourth and fifth tie. Before block 2 runs, write on paper
how many members each rule puts on a top-four list: ROW_NUMBER at four or below, RANK at four or
below, DENSE_RANK at four or below, and "whole ties only", which drops a tie that crosses the line.

Run block 2 and compare. The four counts are 4, 5, 5 and 3. The last one is the list the head of
Retail-Plus warned about: a member who spent exactly what the fourth did is left off, and so is the
fourth.

## Step 3. The same count on Kalpa's Retail-Core members

Block 3 computes each member's Q2 revenue, which is the booked amount of the member's Q2 orders,
the definition Monday's suite used for the Rs 9,84,00,000 quarter, then ranks the members inside
each segment three ways and counts what each rule ships at fifty. The trainer runs it for
Retail-Core.

| Segment | ROW_NUMBER ships | RANK ships | DENSE_RANK ships | Whole ties only ships |
|---|---|---|---|---|
| Retail-Core | 50 | 50 | 52 | 50 |

Then block 4 reads positions 44 to 54 with all three functions side by side, which is where the
difference lives.

| ROW_NUMBER | RANK | DENSE_RANK | Member | Q2 revenue |
|---|---|---|---|---|
| 44 | 44 | 42 | C-0003 | Rs 3,440 |
| 45 | 45 | 43 | C-0004 | Rs 3,120 |
| 46 | 46 | 44 | C-0007 | Rs 3,100 |
| 47 | 47 | 45 | C-0127 | Rs 3,030 |
| 48 | 48 | 46 | C-0054 | Rs 3,000 |
| 49 | 49 | 47 | C-0072 | Rs 2,990 |
| 50 | 50 | 48 | C-0005 | Rs 2,980 |
| 51 | 51 | 49 | C-0092 | Rs 2,950 |
| 52 | 52 | 50 | C-0094 | Rs 2,910 |
| 53 | 53 | 51 | C-0048 | Rs 2,870 |
| 54 | 54 | 52 | C-0074 | Rs 2,810 |

Nobody ties at fiftieth in Retail-Core, so RANK and ROW_NUMBER agree on fifty members. DENSE_RANK
ships 52 because two ties higher up the list each saved it a number, so C-0092 and C-0094 carry
dense numbers 49 and 50 and join a list they did not earn. DENSE_RANK sounds like "ties rank the
same", and the count is how you catch it.

Filtering on the position has to happen outside the query that computes it: the rank lives in a
CTE, and the outer query keeps the rows at fifty or below. A filter on the rank inside the same
WHERE is refused by Postgres, which is a two-minute fix and nothing more.

## Step 4. The head of Retail-Plus's rule, applied

The head of Retail-Plus asked for two things: tied members ranked the same, and a count of how many
made the list. RANK is the function that does the first, because tied members share a position and
everyone at or above fiftieth ships. The second is a sentence in the report, written beside the
list.

Now change the segment in block 3 to `'Retail-Plus'` and run it yourself. Copy the counts into this
table on paper before anyone in the room says a number.

| Segment | ROW_NUMBER ships | RANK ships | DENSE_RANK ships | Whole ties only ships |
|---|---|---|---|---|
| Retail-Plus | | | | |

Then run block 4 for Retail-Plus and read positions 44 to 54 with the three functions side by side.
Write the one sentence you would send the head of Retail-Plus: the rule you chose, how many members
it ships, and why that number is right. Kavya reads the sentences at the round's review.

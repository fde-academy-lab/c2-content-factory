# Guided: the tie, three ways, on paper

Done together, no database. Eight members and a cut-off, which is enough to see everything.

## The members, by Q2 revenue

| member | Q2 revenue |
|---|---|
| C-0102 | Rs 9,400 |
| C-0118 | Rs 8,100 |
| C-0140 | Rs 7,250 |
| C-0165 | Rs 6,600 |
| C-0172 | Rs 6,600 |
| C-0181 | Rs 5,900 |
| C-0193 | Rs 5,300 |
| C-0204 | Rs 4,800 |

## Step 1: number them three ways

Three columns beside the table. Fill each one in by hand.

`ROW_NUMBER` counts 1 to 8 with no thought about value. `RANK` gives tied rows the same number and
then skips. `DENSE_RANK` gives tied rows the same number and does not skip.

Do not look anything up. The two tied rows are where the three columns disagree, and finding the
disagreement yourself is the exercise.

## Step 2: cut at five

For each of your three columns, circle the rows where the number is five or less. Count the
circles.

Three different answers to "the top five". Write all three down.

## Step 3: read the sentence again

> "If two members spent the same, I want them ranked the same, and I want to know how many made
> the top five, not four because of a tie."

Two clauses, and each one eliminates a function. Say which clause kills which, out loud.

## Step 4: the awkward question

`ROW_NUMBER` gave you exactly five names, which is what was asked for numerically. Say in one
sentence why it is still the wrong answer, without using the word tie.

The answer has to do with what would happen if you ran the query again tomorrow.

## Step 5: scale it up

The real Retail-Plus list has a tie at position fifty. Predict, before running anything, how many
names each rule ships for a top fifty.

Then run query four of the guided walk and check.

## Before moving on

One sentence, written down: which function, and the clause from the head of Retail-Plus that
decided it. That sentence goes into the SQL as a comment, because the next person will not have
heard him say it.

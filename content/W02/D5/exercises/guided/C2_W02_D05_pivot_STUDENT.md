# Guided: build the same pivot twice

Together, on screen, with both exports open. Thirty seconds of clicking each time.

## Step 1: the raw export first

Open `C2_W02_D05_raw_export_STUDENT.csv`. Build a pivot: segment down the side, quarter across the
top, order amount in the middle.

Write the grand total down.

## Step 2: compare it with what you know

The warehouse says the two quarters booked Rs 19.84 crore. Your pivot says something close to
twice that.

Before anybody explains it, say what the pivot did wrong. The answer is that it did nothing wrong,
and getting the room to that sentence is the exercise.

## Step 3: the ten-second check

Rows divided by distinct customers, or rows divided by distinct orders. Anything above one and the
file is not what its name suggests.

```
rows in the export / distinct order ids = ?
```

Do it on both files. One comes out at 1.00 and one does not.

## Step 4: the same pivot, on the clean table

Open `C2_W02_D05_customer_table_STUDENT.csv` and build the same pivot.

Same clicks, same layout, and the total now matches. Say aloud what changed, and notice that
nothing about Excel was involved in the answer.

## Step 5: what this means for handing over a file

You are about to send somebody a CSV. Write one sentence naming what one row of it means, and put
that sentence somewhere they will see it.

"One row per order" and "one row per order-payment" look identical in a file browser and produce
totals that differ by a factor of two.

## Step 6: the slice that still lies

Go back to the raw export pivot and filter it to a single segment. The total is still doubled, and
now it looks smaller and more plausible.

Say why filtering makes a wrong number harder to catch rather than easier.

## Before moving on

Write the grain of both files at the top of your own notes, in your own words. You will need it in
about twenty minutes.

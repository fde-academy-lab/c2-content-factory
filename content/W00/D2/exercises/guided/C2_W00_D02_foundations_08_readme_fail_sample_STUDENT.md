# w00-diagnostic-python
Cleans ten Kalpa order rows and totals paid revenue by tier, for Kalpa Retail's Q1 to Q2 revenue question.

## What it shows
Every amount in a CSV arrives as text, so one function converts each amount or rejects its row, and the rejected rows are kept in a list where they can be counted.

## How to run

## Result
The notebook prints the paid revenue for each tier once the bad rows are set aside, and an assert confirms that the tier totals add up to the clean amounts.

## What I would do next
Read the rows from a CSV file in place of a list typed into the first cell, so next month's orders run through the same notebook unchanged.

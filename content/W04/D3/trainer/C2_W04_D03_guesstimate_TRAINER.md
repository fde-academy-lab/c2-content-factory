# Guesstimate of the day: how many orders does a dark store handle in a day?

**TRAINER ONLY.** Five minutes, in the interview room slot or as the lab's warm-up. The room
estimates first; the anchor is revealed last.

## How does a strong candidate run it?

| Step | What they say | The numbers |
|---|---|---|
| Clarify | "One dark store, one ordinary day, orders placed, not items." | |
| Map | "Households in the catchment, times the share that orders in a given week, times orders a week from each, over seven days." | |
| Assume, with ranges | "40,000 households, from 30,000 to 50,000; 15 percent order in a week, from 10 to 20; 1.5 orders a week each, from 1 to 2." | Every input is an assumption, said as one |
| Calculate | "40,000 x 0.15 x 1.5 / 7 is about 1,290 a day." | About 430 to about 2,860 across the ranges |
| Validate | "Swiggy reported 1,089 orders per dark store per day across 1,171 stores in the quarter to June 2026, so I am 18 percent high." | Swiggy Q1 FY27 shareholder letter, key metrics table (T3, checked 12 October 2026) |
| The catch | "Swiggy counts per active store-day, so a store's days count only once it is live, and a new store does not pull the average down before it opens." | The letter's footnote to the same table |

## What does each wrong turn look like, and what do you say?

| The wrong turn | What to say |
|---|---|
| Starts from Pune's population and divides by stores | "How many people can one store reach in a delivery window? Start from the store." |
| Counts items, not orders | "An order holds several items; which one does the store's day count?" |
| Gives one number with no range | "Which input are you least sure of, and what happens to the answer at its ends?" |
| Treats 1,089 as every store's day | "Is that a typical store, or an average over stores of different ages?" |

## Where is the anchor from?

Swiggy's Q1 FY27 letter to shareholders (quarter to 30 June 2026), filed with the NSE:
https://nsearchives.nseindia.com/corporate/SWIGGY_30072026154100_Covering_Letter_Letter_to_Shareholders_-_signed.pdf (checked 12 October 2026)

Its key metrics table reads "Orders/dark store/day" of 1,089 for the
quarter and "Active Dark Stores (Exit)" of 1,171, with the footnote "based on active darkstore-days,
as orders should be linked to only the period a darkstore has been active."

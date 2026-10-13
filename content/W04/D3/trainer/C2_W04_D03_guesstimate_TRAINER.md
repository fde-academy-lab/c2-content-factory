# Guesstimate of the day: how many orders does a dark store handle in a day?

**TRAINER ONLY.** Five minutes, in the interview room slot or as the lab's warm-up. The room
estimates first; the anchor is revealed last.

## How does a strong candidate run it?

| Step | What they say | The numbers |
|---|---|---|
| Clarify | "One mature dark store in a large city, one ordinary day, completed orders, not items." | |
| Map | "Households in the area the store serves, at most its delivery circle, since neighbouring stores split the overlap and each household orders from one; times the share ordering in a given week, which is the households using quick commerce at all times Instamart's share of them; times orders a week from each, over seven days." | |
| Assume, with ranges | "A 2.5 km radius is at most about 20 square km, and at about 2,000 households a square km that is 40,000 households, from 30,000 to 50,000, a ceiling where stores crowd together. 30 percent of them use quick commerce in a given week, from 20 to 40, and Instamart takes half of those, from 35 to 65 percent, so 15 percent order from it, from 7 to 26. Each orders 1.5 times a week, from 1 to 2." | Every input is an assumption, said as one; the share's range is its two guesses' ranges multiplied |
| Calculate | "40,000 x 0.15 x 1.5 / 7 is about 1,290 a day. My least certain input is the share: it stacks two guesses, so its range is the widest, and on its own it moves me from about 600 to about 2,230, where orders a week move me only from about 860 to about 1,710." | Quote about 600 to about 2,230, the share's range, as the working range; every extreme multiplied together gives about 300 to about 3,710, a range no candidate should quote |
| Validate | "Swiggy reported 1,089 completed orders per active store-day in the quarter to June 2026, a quarter it ended with 1,171 active stores, so I am 18 percent high. Landing on 1,089 needs a weekly share of about 13 percent, which I find believable." | Swiggy Q1 FY27 shareholder letter, key metrics table and definitions (T3, checked 12 October 2026) |
| The catch | "That average counts only the days each store was active, and it spans young stores still ramping up and stores across 131 cities, so a mature store in a large city 18 percent above it is what I would expect." | The letter's footnote to the same table; an active store is one with at least one completed order on the period's last day |

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

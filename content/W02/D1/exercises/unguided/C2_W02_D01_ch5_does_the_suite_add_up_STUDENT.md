# Do the suite's numbers add up the way Anand's analyst will add them?

Chapter 5 set, five items. Items 1 and 2 run live in chapter 5's last minutes if the chapter ran to
time; items 3 to 5 are the practice lab's stretch or tonight's work.

> "I want these numbers every Monday, for every segment and channel, computed from the warehouse
> itself."
>
> Anand Iyer, finance controller, Kalpa Retail

Anand Iyer, Kalpa Retail's finance controller, has the segment lines; now he wants the same suite for
each channel, the app, the web and the stores, with a half-year column beside Q1 (April to June 2026)
and Q2 (July to September 2026). His analyst adds before reading any query: the channels against the
book in each quarter, and the quarters against the half-year. A tie-out is that addition, a set of
parts added and set beside the whole they should make. Customers who bought are counted once in a
window, however many orders they placed; the half-year's customers are those who bought at least once
from April to September. The book has 340 customers on its customers table, so no count of customers
who bought can exceed 340. `GROUPING SETS` is a Postgres feature that computes several groupings of
the same rows in one pass, for example each quarter and the half-year together.

| Channel | Q1 orders | Q2 orders | Q1 customers who bought | Q2 customers who bought | Bought through it in both quarters |
|---|---|---|---|---|---|
| app | 192 | 153 | 133 | 124 | 52 |
| web | 181 | 150 | 130 | 113 | 49 |
| store | 165 | 159 | 128 | 121 | 45 |
| The book | 538 | 462 | 244 | 227 | 170 |

**Who needs the answer.** Anand's analyst audits the channel suite, and a line that fails an addition
she can do in her head is doubted along with every other line on the sheet. The channel heads read the
customer lines to judge whether their channel is winning or losing customers.

**The questions on the way.**

- How should the suite produce each channel's half-year column, and what does each way assume?
- Which way fits once Anand wants months, quarters and the half-year on one sheet?
- What does the Q1 tie-out of the channels' customers against the book say?
- What should the analyst conclude from a half-year line that passes the members check?
- What does the web's half-year come to by a second route?

**What you post.** One line of five letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

## How should the suite produce a wider window?

Used at work whenever a report adds a year-to-date or half-year column beside its quarters.

### Q1. How should the suite produce each channel's half-year column, and what does each way assume?

Anand wants orders, booked revenue and customers who bought for each channel over the half-year. Which
way fits?

a) Add each channel's two quarter rows, six rows read, assuming every measure adds across quarters
b) Count the half-year from the orders the way each quarter is counted, 1,000 rows read once more
c) Report no half-year and let the analyst add the quarter rows by hand on the sheet
d) Take the larger of each channel's two quarter counts for customers and add the rest, six rows read

### Q2. Which way fits once Anand wants months, quarters and the half-year on one sheet?

A month later Anand asks for each channel's six months, two quarters and the half-year on one sheet,
all from one pass over the orders so the analyst can tie them out in a single result. Which way fits
now?

a) The monthly rows added into quarters and the quarters into the half-year, since the months are counted from the orders
b) Three separate queries, one per window, each read and tied out on its own
c) One query grouped by channel and quarter, with the half-year added from it and the months left off
d) One grouped query with GROUPING SETS for month, quarter and half-year, counted from the orders once

## Do the parts add back to the whole?

Used at work whenever parts and a total sit on the same page and a reader adds them.

### Q3. What does the Q1 tie-out of the channels' customers against the book say?

In Q1 the channels' orders add back to the book's 538. Their customers who bought, 133, 130 and 128,
add to 391, against the book's 244. What does the tie-out say?

a) 391 exceeds 244 because a customer who bought through two channels sits in both rows
b) The book undercounts Q1's customers by 147, since the three channel queries each count customers once
c) One of the channel queries counts order rows as customers, since only a wrong count could exceed the book
d) The tie-out fails on customers, so the channel lines stay off the sheet until they add to 244

## What does the members check tell the analyst?

Used at work whenever a sanity check is run on a number before it ships.

### Q4. What should the analyst conclude from a half-year line that passes the members check?

A hurried half-year line for the app adds its two quarters' customers, 133 and 124, and reads 257.
The book has 340 customers, so the check that a count of customers who bought cannot exceed the
customers who exist passes. What should the analyst conclude?

a) 257 holds, since it passes the one check that catches a customer counted twice
b) 257 is too low, since the half-year also holds customers who bought in neither quarter
c) 257 may still be too high, since the check only catches a count above 340
d) 257 holds for a channel, since a channel's customers, unlike a segment's, can be added across quarters

## How would a second route confirm the half-year?

Used at work whenever a count of people has to be confirmed without rerunning the query that made it.

### Q5. What does the web's half-year come to by a second route?

Kavya Nair, the team's senior analyst, wants the web's half-year customers confirmed by a route that
shares no code with the suite's own half-year query. The table at the top of this set gives the web's two
quarters and the customers who bought through it in both. What does the route give?

a) 243, the two quarters' customers added
b) 194, Q1's and Q2's customers less the 49 in both
c) 145, Q1's and Q2's customers less twice the 49 in both
d) 130, the larger quarter, since the Q2 buyers bought in Q1 as well

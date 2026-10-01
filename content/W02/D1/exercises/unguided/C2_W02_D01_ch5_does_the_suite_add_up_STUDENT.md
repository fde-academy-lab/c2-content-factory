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
who bought can exceed 340. `GROUPING SETS` is a Postgres feature that returns several groupings of the
same rows from one query, for example each quarter and the half-year.

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

- Which way should produce each channel's half-year customers, judged by what each prints for the web?
- Which way fits once Anand wants months, quarters and the half-year on one sheet, sized in statements and reads?
- What does the Q1 tie-out of the channels' customers against the book say?
- What should the analyst conclude from a half-year line that passes the members check?
- Which tie-out of the store's customer histories confirms its half-year count?

**What you post.** One line of five letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

## How should the suite produce a wider window?

Used at work whenever a report adds a year-to-date or half-year column beside its quarters.

### Q1. Which way should produce each channel's half-year customers, judged by what each prints for the web?

Anand wants orders, booked revenue and customers who bought for each channel over the half-year. The
table above gives the web's two quarters and the customers who bought through it in both. Which way
fits, judged by what each would print for the web's half-year customers?

a) Add the web's two quarter rows: 243 customers, with six rows read for the three channels
b) Take the larger quarter for customers, 130, and add the two quarters' orders and rupees
c) Count the web's customers from April to September in its orders: 194, with 1,000 rows read
d) Count every web order of the half-year with count(*): 331 customers, with all 1,000 rows read

### Q2. Which way fits once Anand wants months, quarters and the half-year on one sheet, sized in statements and reads?

A month later Anand asks for each channel's six months (April to September), two quarters and the
half-year on one sheet, orders, booked revenue and customers who bought in every line. Which way fits
now, sized in the statements it takes, the reads of the orders table and the rows it prints?

a) GROUPING SETS: 1 statement, 1 read of the 1,000 orders and 27 rows, each window counted from them
b) Three queries, one per window: 3 statements and 3 reads of the 1,000 orders for the same 27 rows
c) Months added into quarters and the half-year: 1 read and 27 rows, the customers added across months
d) One query by month: 1 read and 18 rows, with the quarters and the half-year left to the sheet's formulas

## Do the parts add back to the whole?

Used at work whenever parts and a total sit on the same page and a reader adds them.

### Q3. What does the Q1 tie-out of the channels' customers against the book say?

In Q1 the channels' orders add back to the book's 538. Their customers who bought, 133, 130 and 128,
add to 391, against the book's 244. What does the tie-out say?

a) The book undercounts Q1's customers by 147, since the three channel queries each count customers once
b) 391 exceeds 244 because a customer who bought through two channels sits in both of those channels' rows
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
c) 257 holds for a channel, since a channel's customers, unlike a segment's, can be added across quarters
d) 257 may still be too high, since the check only catches a count above the 340 customers

## How would a second route confirm the half-year?

Used at work whenever a count of people has to be confirmed without rerunning the query that made it.

### Q5. Which tie-out of the store's customer histories confirms its half-year count?

The suite's half-year query prints 204 customers who bought through the stores. Kavya Nair, the team's
senior analyst, wants it confirmed by a route that shares no code with that query. Three filters over
one row per store customer give their own counts: 83 bought through the stores in Q1 only, 76 in Q2
only and 45 in both. Which statement about the three counts holds in full?

a) 128 plus 121 is 249, so the half-year query undercounts the store's customers by 45
b) 83 plus 76 plus 45 is 204, so the half-year holds, though the three cannot rebuild Q1's 128 or Q2's 121
c) 83 plus 76 plus 45 is 204, and 83 plus 45 and 76 plus 45 give back Q1's 128 and Q2's 121
d) 128 plus 121 less twice the 45 is 159, since the 45 sit in both of the two quarter counts

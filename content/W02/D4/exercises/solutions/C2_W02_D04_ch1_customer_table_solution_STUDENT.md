# Which answers hold in the chapter 1 set on building one row per customer, and why?

Answers: 1c 2b 3d 4a 5b

Kalpa Retail's growth team sends Monday's offers from a table with one row per customer and three
numbers: recency, the date of the last order; frequency, the count of orders; and spend, the value
of the orders at the prices charged. The warehouse holds 1,000 orders from April to September 2026,
worth Rs 19,84,00,000, and a customer list of 340. Chapter 1 computed the numbers with pandas
`groupby`, which built a table of 301 rows, one per customer who ordered; starting from the
customer list brought back the 39 who never ordered, and a SQL query built from the list gave the
same numbers for all 340. Three of the five items are design items: 1, 4 and 5.

**Who needs the answer.** You, checking your five letters after the lab or tonight. A table that
loses the customers who never ordered sends the first-order nudge to nobody, and a number read off
the wrong rows sends the wrong offer to the rest.

**The questions on the way.**

- Which idea does the chapter 1 set test?
- Why does each of the five keys hold, from the orders in crores to the fact that moves the work?
- Why is option c in item 3, the chapter's own half-fix, the wrong answer worth arguing about?
- Where does a customer table with no orders behind some rows come up at work?

## Which idea does the chapter 1 set test?

A customer table is a list of customers first and a summary of their orders second. The rows come
from the customer list, the numbers from the orders, and anything computed on the table has to know
which customers it is counting. The design items ask where the numbers should be computed as the
orders grow, which count can confirm the table without sharing its code, and which fact would move
the work into the warehouse.

## Why does each of the five keys hold, from the orders in crores to the fact that moves the work?

### Q1. Which way should compute the numbers when the orders run to crores, and what does it move?

A design item. Next year the orders table holds 2 crore rows from 9 lakh listed customers, 6 lakh of
whom have ordered, and the numbers still reach pandas to be merged onto the list.

The key is c, "SQL `GROUP BY`: 6 lakh rows, one per customer who ordered". The
warehouse groups the 2 crore orders where they live and sends back one row per customer who ordered,
so 6 lakh rows move however many orders sit behind them. pandas merges that answer onto the 9 lakh
list, as it merged `rfm` this week.

- a, "pandas `groupby`: 2 crore rows, since the later steps need the orders": moves every order to
  one machine every Monday to make 6 lakh rows; a later step that needs order rows can pull only its
  columns and its months.
- b, "Week 1's loop: 9 lakh rows, one for each customer on the list": the loop fetches every order,
  2 crore, and its answer holds only the 6 lakh who ordered.
- d, "pandas `groupby`: 6 lakh rows, one for each group it returns": 6 lakh is the size of the
  answer; `groupby` runs on the analyst's machine, so all 2 crore orders move before it returns.

### Q2. What does the average orders per customer read before anyone fills the gaps?

The merged table has 340 rows, and the 39 who never ordered carry a missing frequency.

The key is b, "3.32, over the 301 who ordered, since `mean` skips the gaps". pandas' `mean` skips
missing values unless told otherwise, so the line divides 1,000 orders by the 301 customers who
have a count. It is Monday's `AVG` skipping `NULL`s, met again in pandas.

- a, "2.94, over all 340 customers on the list": 1,000 over 340 is the average once the 39 are
  filled with 0, which this line has not done.
- c, "`nan`, since one missing frequency leaves the column's mean missing": a NumPy array behaves
  that way; a pandas column skips the gaps.
- d, "3.32, over all 340 customers on the list": the number is right and the base is wrong, and the
  growth team would read 3.32 as the typical customer on its list.

### Q3. What does a teammate's fix print with the order-built table on the left of the merge?

`rfm` holds the 301 who ordered and sits on the left of a left merge.

The key is d, "301 0: the left side keeps only the customers who ordered". A left merge keeps every
row of the left table, and the left table is `rfm`, so the 39 never arrive. The fill has no gaps to
fill, and the count of zeros is 0.

- a, "340 39: the merge keeps every customer on either side": that is an outer merge; a left merge
  keeps the left side only.
- b, "It stops with a `MergeError`, since 39 customers find no match": `validate` checks that each
  side's keys are unique, and an unmatched key is not a repeated one.
- c, "340 0: the 39 come back, and a missing count is never 0": that is the chapter's half-fix, with
  the list on the left and no fill; here the list is on the right and the 39 never come back.

### Q4. Which count could disagree with the pandas table if the table were wrong?

A design item. Kavya wants the 39 confirmed by a route that shares no code with the pandas table.

The key is a, "A SQL count of listed customers with no row at all in `orders`". It reads the two
tables in the warehouse, with `NOT EXISTS` or a `LEFT JOIN` that keeps the unmatched, and shares
nothing with the `groupby`, the merge or the fills, so a slip in any of them makes the two counts
differ.

- b, "`340 - len(rfm)`, the list less the rows the groupby returned": it reuses the `groupby`'s own
  result and a typed 340, so it agrees with the table whenever the table's first step is wrong.
- c, "`(table[\"frequency\"] == 0).sum()`, rerun after a restart": the same code gives the same
  answer.
- d, "`(table[\"spend\"] == 0).sum()`, zero spend in place of zero orders": the same table, whose
  spend was filled in the same step as its frequency.

### Q5. Which fact, if it became true next quarter, would move the three numbers into the warehouse?

A design item. Chapter 1 chose pandas `groupby` for the three numbers.

The key is b, "The orders table grows to 3 crore rows, too many to move each Monday". What separates
the options is the rows each moves: pandas moves every order, while `GROUP BY` sends one row per
customer who ordered whatever the size of the orders table. When the orders stop fitting a weekly
move, the grouping moves to the warehouse.

- a, "The customer list grows to 4 lakh, and the list is read each Monday": every option reads the
  list, so its size separates nothing.
- c, "The growth team asks for a fourth number, the first order's date": one more pair in `agg`, or
  one more `min` in SQL, in either tool.
- d, "The monsoon sale's feed has to be merged onto the table every Monday": the merge is pandas'
  work whichever tool computes the three numbers.

## Why is option c in item 3, the chapter's own half-fix, the wrong answer worth arguing about?

Item 3, option c is the result the chapter showed on screen: 340 rows and no zeros. A learner who
remembers the screen picks it, and the code in the item differs by one thing, which table sits on
the left. Read the merge's left side first, every time: it decides the rows, and the right side only
adds columns.

## Where does a customer table with no orders behind some rows come up at work?

Shopify's customer reports score every customer from 1 to 5 on recency, frequency and monetary
value, and one of their 11 groups is Prospects, "Customers with no orders yet" (Shopify Help Center,
Customers reports, checked 1 Oct 2026). A platform that serves millions of shops keeps the customers
who never bought on the table, because the offer written for them needs someone to go to.

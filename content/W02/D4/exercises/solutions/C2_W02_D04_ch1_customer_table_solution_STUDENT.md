# Which answers hold in the chapter 1 set on building one row per customer, and why?

Answers: 1c 2b 3d 4a 5c

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
- Why does each of the five keys hold, from the orders in crores to the dashboard on the warehouse?
- Why is option c in item 3, the chapter's own half-fix, the wrong answer worth arguing about?
- Where does a customer table with no orders behind some rows come up at work?

## Which idea does the chapter 1 set test?

A customer table is a list of customers first and a summary of their orders second. The rows come
from the customer list, the numbers from the orders, and anything computed on the table has to know
which customers it is counting. The design items ask where the numbers should be computed once the
orders run to crores, which count the growth team's lead can run in the warehouse to confirm the
customers who never ordered, and where the table should be built once a dashboard on the warehouse
is its only reader.

## Why does each of the five keys hold, from the orders in crores to the dashboard on the warehouse?

### Q1. Which way should compute the numbers when the orders run to crores, and what does it move?

Item 1 is a design item: next year the orders table holds 2 crore rows from 9 lakh listed customers,
6 lakh of whom have ordered, and the numbers still reach pandas to be merged onto the list.

The key is c, "SQL `GROUP BY` should compute them, moving 6 lakh rows, one per customer who
ordered". The warehouse groups the 2 crore orders where they live and sends back one row per
customer who ordered, so the rows it sends grow with the customers who order and never with the
orders behind them. pandas merges that answer onto the 9 lakh list, as it merged `rfm` this week.

- a, "pandas `groupby` should compute them, moving 2 crore rows, since the later steps need the
  orders": It moves every order to one machine every Monday to make 6 lakh rows, and a later step
  that needs order rows can pull only its own columns and months.
- b, "SQL `GROUP BY` should compute them, moving 2 crore rows, since the warehouse reads every
  order": The warehouse does read every order, and the reading happens inside it; only the 6 lakh
  grouped rows leave it.
- d, "pandas `groupby` should compute them, moving 6 lakh rows, one for each group it returns": 6
  lakh is the size of the answer, and `groupby` runs on the analyst's machine, so all 2 crore orders
  move before it returns anything.

### Q2. What does the average orders per customer read before anyone fills the gaps?

The merged table has 340 rows, and the 39 who never ordered carry a missing frequency.

The key is b, "It prints 3.32, an average over the 301 who ordered, since `mean` skips the gaps".
pandas' `mean` skips missing values unless told otherwise, so the line divides 1,000 orders by the
301 customers who have a count. It is Monday's `AVG` skipping `NULL`s, met again in pandas.

- a, "It prints 2.94, an average over all 340 customers on the list": 1,000 over 340 is the average
  once the 39 are filled with 0, which this line has not done.
- c, "It prints `nan`, since one missing frequency leaves the whole column's mean missing": A NumPy
  array's mean behaves that way, and a pandas column skips the gaps.
- d, "It prints 3.32, an average over all 340 customers on the list": The number is right and the
  base is wrong, and the growth team would read 3.32 as the typical customer on its list.

### Q3. What does a teammate's fix print with the order-built table on the left of the merge?

`rfm`, which holds the 301 who ordered, sits on the left of a left merge.

The key is d, "It prints 301 0, since the left side holds only the customers who ordered". A left
merge keeps every row of the left table, and the left table is `rfm`, so the 39 never arrive. The
fill has no gaps to fill, and the count of zeros is 0.

- a, "It prints 340 39, since the merge keeps every customer on either side": That is what an outer
  merge does, and a left merge keeps the left side only.
- b, "It stops with a `MergeError`, since 39 customers find no match on the left": `validate` checks
  that each side's keys are unique, and an unmatched key is a different thing from a repeated one.
- c, "It prints 340 0, since the 39 come back and a missing count is never 0": That is the chapter's
  half-fix, with the list on the left and no fill; here the list is on the right and the 39 never
  come back.

### Q4. Which count could the growth team's lead run herself to confirm the 39 before the nudge goes out?

Item 4 is a design item: the person confirming the count works in SQL in the warehouse and never
opens a notebook, so the route has to run there, start from the customer list and count customers
with no orders.

The key is a, "Count, in the warehouse, the listed customers who have no row in `orders`". It starts
from the list, so the customers who never ordered are there to be counted, and it asks whether each
one has any order at all, so it returns 39 today. It shares nothing with the `groupby`, the merge or
the fills, so a slip in any of them makes the two counts differ. Tuesday's anti-join writes it, with
`NOT EXISTS` or with a `LEFT JOIN` that keeps the unmatched rows.

- b, "Group the orders by customer in the warehouse, and count the groups whose `count(*)` is 0":
  Grouping the orders makes a group only for a customer who has an order, so no group ever counts 0
  and the query returns 0 on a right table and a wrong one alike. It is chapter 1's trap, in SQL.
- c, "Left-join the list to the orders in the warehouse, group by customer, and count those whose
  `count(*)` is 0": It starts from the list, as it should, and then `count(*)` counts the empty row
  the left join keeps for a customer with no order as 1, so it also returns 0. Counting
  `o.order_id`, which is missing on that row, gives the 39.
- d, "Fetch every order's customer id, and check the list against them in a Python loop": The loop
  shares no code with the table and finds 39, and it runs in Python on the analyst's machine, which
  the lead does not open, after moving every order out of the warehouse.

### Q5. Which way should build the table once a dashboard on the warehouse is its only reader?

Item 5 is a design item: chapter 1 chose pandas because the analysts work in Python and the later
steps needed the orders in memory, and here both reasons are gone while the orders stay small.

The key is c, "A SQL query from the customer list, with a `LEFT JOIN` to the orders, should build
them". The dashboard reads the warehouse, so the numbers belong there, and the query starts from the
list, so it returns 340 rows today, with the 39 who never ordered at a frequency of 0. It is the
second route chapter 1 already checked against the pandas table, customer by customer.

- a, "pandas `groupby` should stay, since 500 orders a quarter move in a fraction of a second":
  Chapter 1 chose pandas for the analysts' Python and for later steps that needed the orders in
  memory. A dashboard that reads Postgres uses neither, and it cannot read a pandas frame at all.
- b, "A SQL `GROUP BY` on the orders should build them, sending one row per customer who ordered":
  It sends 301 rows today, so the 39 who never ordered vanish from the dashboard and the first-order
  nudge has nobody to go to.
- d, "pandas `groupby` should stay, with its table written into the warehouse every Monday": It
  moves every order out of the warehouse and the table back in each Monday, keeps the definition in
  a notebook, and leaves the dashboard reading a copy as old as the last Monday run.

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

# How many orders, rupees and customers did each quarter book, counted where the book lives?

Chapter 1 set, five items. Items 1 and 2 run live in chapter 1's last minutes if the chapter ran to
time; items 3 to 5 are the practice lab's stretch or tonight's work.

> "I want these numbers every Monday, for every segment and channel, computed from the warehouse
> itself. No notebooks, no exports, nothing a person can mistype. Our data team will give you read
> access to Postgres."
>
> Anand Iyer, finance controller, Kalpa Retail

Anand Iyer signs Kalpa Retail's Monday sheet, and his analyst reruns every line of it before he
does. Kalpa's warehouse is a Postgres database, and its two quarters of orders are the book: the one
copy everybody reads, 1,000 orders placed from April to September 2026. Q1 is April to June 2026 and
Q2 is July to September 2026. Booked revenue is every order at its amount, whatever its status, and a
customer who bought in a quarter is counted once in that quarter however many orders they placed.
Read access lets the team run queries on the book and create nothing inside it. A saved view is a
query stored in the database under a name, and saving one needs the right to create objects there.
In a query, `count(*)` counts rows, `count(customer_id)` counts the rows whose customer id is filled
in, and `count(DISTINCT customer_id)` counts the different customer ids.

| Table | Rows | Columns |
|---|---|---|
| orders | 1,000, one per order | order_id, customer_id, order_date, quarter, channel, amount, status |
| customers | 340, one per member | customer_id, segment, city, country, joined_date |

| Quarter | Orders | Booked revenue | Customers who bought |
|---|---|---|---|
| Q1 | 538 | Rs 10,00,00,000 | 244 |
| Q2 | 462 | Rs 9,84,00,000 | 227 |

**Who needs the answer.** Anand puts each quarter's orders, rupees and customers on the Monday sheet,
and the customer line decides whether Kalpa's customers come back. Meera Raghavan, the CEO, parked a
Rs 12 crore acquisition budget last week on the finding that they do, so a customer line the analyst
cannot rerun and trust puts that decision back on her desk.

**The questions on the way.**

- How many rows leave the warehouse each Monday on each of three ways to produce the channel lines?
- Which way fits a team with read access only, and which fact would change the choice?
- What do three counts return on eight cancelled orders?
- Which change to the query answers the service head's question about customers who cancelled?
- Which route confirms Q2's 227 customers without sharing the query's code?

**What you post.** One line of five letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

## Where should the Monday numbers be computed?

Used at work whenever a stakeholder asks for the same numbers every week and someone decides where
they are made.

### Q1. How many rows leave the warehouse each Monday on each of three ways to produce the channel lines?

Anand adds six lines to the sheet: orders and booked revenue for each of Kalpa's three channels, the
app, the website and the stores, in each quarter. The channel is a column of the orders table. The
team could export what the lines need and compute them in pandas, keep a .sql file the analyst
reruns, or save a view. How many rows leave the warehouse each Monday on each way?

a) 1,340 for the export, 6 for the file and 6 for the view
b) 1,000 for the export, 1,000 for the file and 6 for the view
c) 1,000 for the export, 6 for the file and 6 for the view
d) 1,000 for the export, 6 for the file and none for the view

### Q2. Which way fits a team with read access only, and which fact would change the choice?

The platform lead has granted read access and nothing more, and the analyst must be able to rerun
every channel line on the same book. Which way fits this Monday, and which fact would change it?

a) The .sql file, which read access can run; a schema of the team's own, once the lines settle, would switch it to a view
b) The export, since pandas is where the team works fastest; a slower laptop would switch it to the .sql file
c) The saved view, since it follows a renamed column and guards the columns it reads; only losing read access would switch it back to a file
d) The .sql file, since it moves the fewest rows of the three; a book ten times larger would switch it to a view

## How many customers stand behind a count?

Used at work whenever a number goes on a sheet under the word customers.

### Q3. What do three counts return on eight cancelled orders?

The head of customer service asks how many customers cancelled an order. The eight rows below are
invented, one invented week of cancelled orders.

| order_id | customer_id | amount | status |
|---|---|---|---|
| X-01 | C-11 | Rs 900 | cancelled |
| X-02 | C-14 | Rs 1,200 | cancelled |
| X-03 | C-11 | Rs 450 | cancelled |
| X-04 | C-20 | Rs 3,000 | cancelled |
| X-05 | C-14 | Rs 700 | cancelled |
| X-06 | C-11 | Rs 650 | cancelled |
| X-07 | C-31 | Rs 1,100 | cancelled |
| X-08 | C-20 | Rs 800 | cancelled |

What do `count(*)`, `count(customer_id)` and `count(DISTINCT customer_id)` return on these rows, in
that order?

a) 8, 4 and 4
b) 4, 4 and 4
c) 8, 8 and 8
d) 8, 8 and 4

### Q4. Which change to the query answers the service head's question about customers who cancelled?

On the whole book, a colleague's query reads
`SELECT count(*) AS customers FROM orders WHERE status = 'cancelled'` and returns 163, and the draft
for the service head says 163 customers cancelled an order in the half-year. Which change to the
query answers the question the service head asked?

a) `count(customer_id) AS customers`, since it counts the customer column
b) `count(DISTINCT customer_id) AS customers`, which reads 125
c) `count(*) AS cancelled_orders`, since the 163 then carries an honest name
d) `count(DISTINCT order_id) AS customers`, since no two rows share an order id

## How would you prove a count by a second route?

Used at work whenever an auditor asks how you know a number on the sheet is right.

### Q5. Which route confirms Q2's 227 customers without sharing the query's code?

Anand's analyst wants Q2's 227 customers who bought confirmed by a route that shares no code with the
query that produced the number. Which route does that?

a) Run the same query a second time and compare the two results
b) Count Q2's rows with `count(customer_id)` and set the result beside 227
c) Pull Q2's 462 order rows into Python, put each customer id in a set, and count the set
d) Divide Q2's booked revenue, Rs 9,84,00,000, by its revenue per order, Rs 2,12,987, and compare

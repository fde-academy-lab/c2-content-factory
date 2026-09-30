# Which answers hold in the chapter 1 set on counting each quarter where the book lives, and why?

Answers: 1c 2a 3d 4b 5c

Anand Iyer, Kalpa Retail's finance controller, wants the Monday numbers computed from the warehouse
itself, with read access only, and his analyst reruns every line. Chapter 1 counted the book where it
lives: Q1 booked 538 orders and Rs 10,00,00,000 from 244 customers, Q2 booked 462 orders and
Rs 9,84,00,000 from 227 customers, and a count named customers that counted order rows read 538 and
462 instead. The set puts the same habits on new questions: the channel lines, the cancelled orders
and a second route for Q2's customers. Three of the five items are design items: 1, 2 and 5.

**Who needs the answer.** You, checking your five letters after the lab or tonight. The customer line
on Anand's sheet decides whether Kalpa's customers come back, and a line you cannot defend here is
the one the analyst sends back on Monday.

**The questions on the way.**

- Which idea does this set test?
- Why is each key right, item by item?
- Which wrong answer is worth arguing about?
- Where does this show up at work?

## Which idea does this set test?

A number on a finance sheet is only as good as the place it is computed and the name it carries. The
design items ask where the Monday lines should be made, sized in rows that leave the warehouse, which
way fits the access the team holds and which fact would change it, and which second route confirms a
count without repeating the first one's code. The other two items ask what three counts return on a
table where customers repeat, and which change makes a count answer the question it was asked.

## Why is each key right, item by item?

### Q1. How many rows leave the warehouse each Monday on each of three ways to produce the channel lines?

Kind: a design item, because the learner sizes three ways from the table sizes given. Anand adds six
channel lines, orders and booked revenue per channel and quarter, and the channel is a column of the
orders table.

The key is c, "1,000 for the export, 6 for the file and 6 for the view". The lines read one table, so
an export moves its 1,000 rows out to pandas every Monday. A .sql file and a view both run inside the
warehouse and send back only their six result rows.

- a, "1,340 for the export, 6 for the file and 6 for the view": exports the 340 customers as well,
  which is what the segment lines needed in chapter 1; the channel lines never read that table.
- b, "1,000 for the export, 1,000 for the file and 6 for the view": a .sql file runs where the book
  lives and returns its result, so only six rows travel.
- d, "1,000 for the export, 6 for the file and none for the view": a view is a stored query, and
  selecting from it still sends its six rows to the analyst.

### Q2. Which way fits a team with read access only, and which fact would change the choice?

Kind: a design item, the best-fit way under a constraint and the fact that would switch it. The
platform lead granted read access only, and the analyst must rerun every line on the same book.

The key is a, "The .sql file, which read access can run; a schema of the team's own, once the lines
settle, would switch it to a view". Read access runs a query and creates nothing, so the file is the
way the team can use today, and the analyst reruns the same file on the same book. A schema the team
may create objects in, once the suite stops changing, makes the view better, because the view follows
a renamed column and Postgres refuses to drop a column a view reads.

- b, "The export, since pandas is where the team works fastest; a slower laptop would switch it to the
  .sql file": Anand ruled out exports, and a copy keeps answering from old data after the book
  changes; the laptop's speed has nothing to do with the choice.
- c, "The saved view, since it follows a renamed column and guards the columns it reads; only losing
  read access would switch it back to a file": the view's strengths are real, and saving one needs
  the right to create objects, which read access does not give.
- d, "The .sql file, since it moves the fewest rows of the three; a book ten times larger would switch
  it to a view": the view moves the same six rows, and a larger book leaves both at six, so the reason
  and the switch are both wrong.

### Q3. What do three counts return on eight cancelled orders?

Kind: predict the output on an exhibit. Eight invented cancelled orders from four invented customers:
C-11 three times, C-14 twice, C-20 twice and C-31 once.

The key is d, "8, 8 and 4". `count(*)` counts the eight rows, `count(customer_id)` counts the eight
rows whose customer id is filled in, and `count(DISTINCT customer_id)` counts the four different ids.
The service head's answer is four customers.

- a, "8, 4 and 4": reads `count(customer_id)` as a count of customers, and it counts every row with
  an id, so it reads 8.
- b, "4, 4 and 4": reads every count as customers, including the one that counts rows.
- c, "8, 8 and 8": treats DISTINCT as having nothing to remove, which holds only when no customer
  cancels twice.

### Q4. Which change to the query answers the service head's question about customers who cancelled?

Kind: fix the logic. A colleague's query counts the book's cancelled rows under the name customers
and reads 163.

The key is b, "`count(DISTINCT customer_id) AS customers`, which reads 125". On the whole book, 125
different customers placed the 163 cancelled orders: 93 cancelled once, 27 twice, 4 three times and
1 four times, so the draft overstated the customers by 38.

- a, "`count(customer_id) AS customers`, since it counts the customer column": counts every row with a
  customer id, which is all 163 again.
- c, "`count(*) AS cancelled_orders`, since the 163 then carries an honest name": the name now tells
  the truth, and the number still answers a different question from the one the service head asked.
- d, "`count(DISTINCT order_id) AS customers`, since no two rows share an order id": order ids never
  repeat, so this counts orders, 163, under the wrong name.

### Q5. Which route confirms Q2's 227 customers without sharing the query's code?

Kind: a design item, the independent second route. The analyst wants Q2's 227 customers confirmed by
a route that shares no code with the query.

The key is c, "Pull Q2's 462 order rows into Python, put each customer id in a set, and count the
set". The set keeps each id once, so its size is the customers who bought, reached with no SQL
aggregate at all; it gives 227, the same as the query, at the cost of moving 462 rows to agree with
one number.

- a, "Run the same query a second time and compare the two results": the same code repeats the same
  mistake, so agreement proves only that the query is repeatable.
- b, "Count Q2's rows with `count(customer_id)` and set the result beside 227": counts 462 order rows,
  a different leaf, so the two numbers were never meant to agree.
- d, "Divide Q2's booked revenue, Rs 9,84,00,000, by its revenue per order, Rs 2,12,987, and compare":
  revenue over revenue per order gives back the orders, 462, which checks a different leaf.

## Which wrong answer is worth arguing about?

Item 4, option c. Renaming the count to cancelled_orders is an honest repair, and many reviewers would
accept it, since the sheet no longer claims something the query does not compute. The service head
asked about customers, though, and 125 customers cancelling 163 orders is a different finding from
163 cancellations spread one each: 32 customers cancelled more than once, which is where a service
team would start. An honest name fixes the label, and only the distinct count answers the question.

## Where does this show up at work?

JPMorgan Chase's task force on the 2012 trading losses found a risk model run through Excel
spreadsheets that had to be completed by hand, copying and pasting data from one spreadsheet to
another (the task force report of 16 January 2013). A number computed where the data lives, by a file
anyone can rerun, removes the copying step that such reviews keep finding.

# Which answers hold in the chapter 1 set on counting each quarter where the book lives, and why?

Answers: 1c 2a 3d 4b 5d

Anand Iyer, Kalpa Retail's finance controller, wants the Monday numbers computed from the warehouse
itself, with read access only, and his analyst reruns every line. The book is the warehouse's two
quarters of orders, the one copy everybody reads. Chapter 1 counted it where it lives: Q1 booked 538
orders and Rs 10,00,00,000 from 244 customers, Q2 booked 462 orders and Rs 9,84,00,000 from 227
customers, and a count named customers that counted order rows read 538 and 462 instead. The set puts
the same habits on new questions: the channel lines, the cancelled orders and a second route for Q2's
customers. Three of the five items are design items: 1, 2 and 5.

**Who needs the answer.** You do, when you check your five letters after the lab or tonight. The
customer line on Anand's sheet decides whether Kalpa's customers come back, and a line you cannot
defend here is the one the analyst sends back on Monday.

**The questions on the way.**

- Which idea does the chapter 1 set test: where a count is computed and whether its name says what it counts?
- Why does each of the five keys hold, from the channel lines to Q2's 227 customers?
- Why is option c in item 4, the honest name cancelled_orders, worth arguing about?
- Where did JPMorgan's task force find numbers moved by hand?

## Which idea does the chapter 1 set test: where a count is computed and whether its name says what it counts?

The set tests where the Monday lines are computed and whether each count's name says what it counts.
The design items ask where the channel lines should be made, sized in rows that leave the warehouse,
which fact would make a saved view better than the file, and which second route could disagree with a
count if the count were wrong. The other two items ask what three counts return on a table where
customers repeat, and which change makes a count answer the question it was asked.

## Why does each of the five keys hold, from the channel lines to Q2's 227 customers?

### Q1. How many rows leave the warehouse each Monday on each of three ways to produce the channel lines?

Kind: a design item, because the learner sizes three ways from the table sizes given. Anand adds six
channel lines, orders and booked revenue per channel and quarter, and the channel is a column of the
orders table.

The key is c, "1,000 for the export, 6 for the file and 6 for the view". The lines read one table, so
an export moves its 1,000 rows out to pandas every Monday. A .sql file and a view both run inside the
warehouse and send back only their six result rows.

- a, "1,340 for the export, 6 for the file and 6 for the view": exports the 340 customers as well,
  which the segment lines would need, since the segment lives on the customer table; the channel
  lines never read that table.
- b, "1,000 for the export, 1,000 for the file and 6 for the view": a .sql file runs where the book
  lives and returns its result, so only six rows travel.
- d, "1,000 for the export, 6 for the file and none for the view": a view is a stored query, and
  selecting from it still sends its six rows to the analyst.

### Q2. Which of four facts would make a saved view better than the .sql file?

Kind: a design item, the fact that would switch the choice, picked from four facts that each sound
like a reason. Saving a view needs the right to create objects in the warehouse, and a view pays for
itself once the query behind it stops changing: Postgres then refuses a change that would break the
columns it reads.

The key is a, "The platform lead grants a schema, and the six lines have not changed in the last eight
Mondays". The schema gives the right a view needs, and eight unchanged Mondays say the query has
settled, so the view's guard on its columns is worth having.

- b, "The book grows to 50,000 orders, and a saved view would send back the six lines faster than the
  file": a plain view stores no result; reading it runs the same query, so it sends the same six rows
  in the same time, at any size of book.
- c, "Anand adds a new cut of the channel lines every Monday for the next month, and wants each one
  kept": a query that changes every week is the file's case, since a view would be dropped and saved
  again each Monday, and read access cannot save one anyway.
- d, "The analyst asks for the six lines as a file she can open and check without a database": a file
  opened away from the database is an export, which Anand ruled out, and it ages from the day it is
  written.

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

The key is b, "`count(DISTINCT customer_id) AS customers`, which reads 125 on the whole book". On the
book, 125 different customers placed the 163 cancelled orders: 93 cancelled once, 27 twice, 4 three
times and 1 four times, so the draft overstated the customers by 38.

- a, "`count(customer_id) AS customers`, since it counts the customer column": counts every row with a
  customer id, which is all 163 again.
- c, "`count(*) AS cancelled_orders`, since the 163 then carries an honest name": the name now tells
  the truth, and the number still answers a different question from the one the service head asked.
- d, "`count(DISTINCT order_id) AS customers`, since no two order rows share one id": order ids never
  repeat, so this counts orders, 163, under the wrong name.

### Q5. Which second route could disagree with Q2's 227 customers if the count were wrong?

Kind: a design item, the independent second route. A second route earns its place only if it could
give a different number when the first count is wrong.

The key is d, "Group Q2's orders by `customer_id` and count the groups the query returns". Grouping
by the customer makes one group per customer who bought, so the query returns 227 rows, reached
without `count(DISTINCT ...)`. Had the first query counted something else under the name customers,
order rows or order ids, the 227 groups would disagree with it.

- a, "Run the same query after lunch and check that it prints 227 again": the same code repeats the
  same mistake, so agreement proves only that the query is repeatable.
- b, "Count Q2's rows with `count(customer_id)`, which must also give 227": it counts the 462 rows
  that carry a customer id, so the two numbers were never meant to agree.
- c, "Divide Q2's 462 orders by its 2.04 orders per customer and round to a whole customer": 2.04 was
  itself computed from the 227, so the route can only hand the 227 back, and the rounded 2.04 makes it
  hand back 226 (462 over 2.04 is 226.47).

## Why is option c in item 4, the honest name cancelled_orders, worth arguing about?

Renaming the count to cancelled_orders is an honest repair, and many reviewers would accept it, since
the sheet no longer claims something the query does not compute. The service head asked about
customers, though, and 125 customers cancelling 163 orders is a different finding from 163
cancellations spread one each: 32 customers cancelled more than once, which is where a service team
would start. An honest name fixes the label, and only the distinct count answers the question.

## Where did JPMorgan's task force find numbers moved by hand?

JPMorgan Chase's task force on the 2012 trading losses found a risk model run through Excel
spreadsheets that had to be completed by hand, copying and pasting data from one spreadsheet to
another (the task force report of 16 January 2013). A Monday line computed where the data lives, by a
file anyone can rerun, has no copying step in it.

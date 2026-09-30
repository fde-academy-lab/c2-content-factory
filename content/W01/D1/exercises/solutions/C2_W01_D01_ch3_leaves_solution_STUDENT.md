# Which letters answer chapter 3's set on how many customers came back?

Answers: 1d 2b 3c 4a 5d

## What does the set test about counting Kalpa's customers?

A row is an order and a customer is an id. Counted by rows, the 30 orders read as 30 customers and
orders per customer as 1.00, so "nobody comes back" makes acquisition look like the only branch.
Counted by distinct ids, Kalpa has 23 customers, 30 / 23 = 1.30 orders each, and 7 of them came
back while 16 bought once. A set counts customers in one line; the dictionary of counts fills both
customer branches in one pass and names who came back; the warehouse's COUNT(DISTINCT) takes over
when the rows run into crores.

## Why is each key right, and why does each other option fail?

| Item | Key | The question in one line | Why the key holds | Why each other option fails |
|---|---|---|---|---|
| 1 | d | Which tool answers each of the head of Retail-Plus's four questions? | A set counts distinct ids (1q), a dictionary keeps a count per id (2r), the `&` of two sets keeps the ids both hold (3s), and the row count is the order count (4p). | a: the row count answers how many orders, and a set answers how many customers, so 1p and 4q swap them. b: 2s and 3r swap the `&` and the dictionary, which answer different questions. c: 1r and 2q swap the dictionary and the set, and a set forgets how many orders each id placed. |
| 2 | b | What does a cell that divides the 30 orders by `len(ORDERS)` print, and what would Meera read into it? | The row count is 30, so 30 / 30 prints 1.00, which reads as nobody coming back and makes buying new customers look like the only way to grow. | a: 1.30 divides by the 23 distinct ids, which this cell never counts. c: 0.77 is 23 / 30, the rate upside down, from ids this cell never counts. d: dividing 30 by 30 cannot print 23. |
| 3 | c | Which way of counting customers fits 4 crore rows in the warehouse? | The count runs where the rows live and one number comes back; Week 2 teaches the SQL. | a: a loop works on 30 rows and first has to move 4 crore rows into a notebook. b: a row count counts orders at any size. d: a spreadsheet cannot hold 4 crore rows, and a count by hand misses changes. |
| 4 | a | How many of Anand's customers kept two orders, with 26 not-cancelled orders from 21 customers and nobody on three? | With nobody on three orders, each extra order belongs to a different customer: 26 - 21 = 5 customers kept two. | b: 7 came back on the booked orders, a different reading. c: 21 counts every customer. d: 26 counts rows as customers. |
| 5 | d | Which tool fits "how many customers bought this quarter?", and what would switch it? | A set answers "how many" in one line; the dictionary earns its extra lines once the question becomes who came back or how often. | a: the row count counts orders, whatever the number looks like. b: a dictionary works and answers more than was asked. c: a sort is easy to miscount and has nothing to do with a thousand rows. |

## Which item is worth arguing about?

Item 4. The shortcut, orders less customers, holds only when nobody placed three orders, which is
why the stem says so. With one customer on three orders the subtraction counts that customer's two
extra orders as two people, so the dictionary is the count to trust whenever the stem cannot promise
it.

**Kavya's review.** "Your first 30 was a count of rows, divided as if it were people. Count people by
their ids."

## Where does this pattern show up at work?

Reliance Retail reports 396 million registered customers. Registered, active and ordering customers
are three denominators, and each gives a different rate for the same orders, so every rate per
customer has to say which customers it divides by.

## What does notebook 03 confirm?

Notebook 03 prints 23 customers, 1.30 orders each and 7 who came back on the booked orders, and 2
who kept two on the delivered orders.

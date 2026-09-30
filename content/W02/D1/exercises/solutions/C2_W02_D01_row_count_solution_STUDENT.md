# Solution: round 1 set, is the warehouse the book?

Answers: 1b 2d 3a 4c 5b 6d 7a

## The idea being tested

A count answers exactly the question its argument asks: `count(*)` counts rows, `count(column)`
counts rows where the column has a value, and `count(DISTINCT column)` counts different values. A
list answers exactly the order it was given, and without `ORDER BY` it was given none. A new source
is checked against the old one leaf by leaf, and every difference is stated with what explains it.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | b | `count(*)` counts the rows that survive `WHERE`, and a row of `orders` is an order: 462 in Q2. | a is `count(DISTINCT customer_id)`, 227. c counts the customers table. d: `WHERE` runs before the count, so it can only shrink it. |
| 2 | d | Each member counted once is `count(DISTINCT customer_id)`: 76 Retail-Plus members bought in Q2. | a and b both count order rows, 140, because every row has an id. c counts the members on the book, 120, whether or not they bought. |
| 3 | a | 340 members sit in the customers table and 301 placed at least one order, so 39 bought nothing in the window. | b: the customer id is the table's primary key, so it cannot repeat. c: every order carries a customer id, since the column is required. d: `DISTINCT` over both quarters counts a person once. |
| 4 | c | Without `ORDER BY`, `LIMIT 5` returns whichever five rows the database reaches first; a reload moved two rows, and the same query returned three of the same orders and two others. | a: the reload rewrote identical values, and Q1 is still Rs 10.00 crore. b: the query text is the same. d: the rows are not random either; they follow storage, which is why they look stable until something moves them. |
| 5 | b | The warehouse is the book of record from today, so its leaves go on the sheet. The fall, revenue per order and Retail-Plus orders agree with Week 1; customers do not, and the two sources share no customer id. Stating the difference in one line is what lets the analyst trust the rest. | a: last week's file is not the book, and it shares no customer with it. c hides the leaves that moved, including the Retail-Plus members who stopped buying. d: two different records will not agree on every leaf, and waiting stops the Monday suite. |
| 6 | d | The median describes an order somebody placed; the mean is kept beside it because it multiplies back to the total. | a: the mean is 79 times the median, and with the two largest orders set aside it is still 66.5 times, because Business orders average about Rs 8.84 lakh against a consumer median near Rs 2,500, so the mean describes no order in the book. b: those orders are real revenue, and removing them changes the book. c: an average of two averages describes nothing. |
| 7 | a | Booked revenue, every status, is the reading Week 1 reconciled to Finance, so the suite keeps it and says so in the comment. | b and c are honest readings with their own definitions, and switching reading silently breaks the comparison with Week 1. d: a number is chosen for its question, never for its size. |

## The part worth arguing about

Item 4. Some learners argue that nobody reloads the warehouse between their run and the analyst's.
The Postgres documentation is blunt: without `ORDER BY`, `LIMIT` returns "an unpredictable subset of
the query's rows", and the planner may choose a different plan on a different day. The reload is
only the easiest way to see it happen; the fix costs one line either way.

## Where the pattern lives in production

A dashboard tile labelled "customers" that is really `count(*)` over an events table is one of the
most common metric bugs in product analytics, and it inflates every per-customer rate downstream.
An unordered `LIMIT` in a sampling job makes an audit irreproducible, which is why audit samples in
regulated teams are drawn with a fixed order or a stored seed.

PostgreSQL 16 documentation, LIMIT and OFFSET, https://www.postgresql.org/docs/16/queries-limit.html (verified 29 Sep 2026)

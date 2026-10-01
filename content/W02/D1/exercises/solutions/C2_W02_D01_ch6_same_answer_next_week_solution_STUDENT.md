# Which answers hold in the chapter 6 set on whether next Monday's run repeats, and why?

Answers: 1c 2b 3c 4d 5b 6a

Chapter 6 made the Monday suite repeatable. A fingerprint of seven numbers prints beside every run, so
a difference next Monday says whether the book moved or the query did. Five delivered Q2 app orders
drawn with `LIMIT 5` and no `ORDER BY` came back as Rs 3,900 on one run and Rs 4,590 on the analyst's
rerun after an overnight reload that rewrote two rows with their own values, while the fingerprint
stayed the same; ordering on the order id gave the same five, Rs 3,900, both times. The set carries
those habits to a new sample and to the question of what the fingerprint can and cannot see. Three of
the six items are design items: 1, 2 and 5.

**Who needs the answer.** You do, when you check your six letters after the lab or tonight. Anand's
analyst signs the suite only when a rerun on the same book gives the same answer, and a sample that
moves on its own costs her a Monday of tracing.

**The questions on the way.**

- Which idea does the chapter 6 set test: how a run shows it read the same book and drew the same sample?
- Why does each of the six keys hold, from the fingerprint's seven numbers to the tier's 0.706?
- Why is option d in item 3, a new customer who has bought nothing, worth arguing about?
- Where does Netflix's team audit each run before publishing it?

## Which idea does the chapter 6 set test: how a run shows it read the same book and drew the same sample?

A run that can be audited says what book it read and returns its lists in an order the rerun will
repeat. The design items size the ways a run can prove itself on read access, pick the way that would
have stopped two bad runs once write access arrives, and confirm an ordered sample by a route outside
the database. The other items ask what a fingerprint misses, what explains a sample that moved while
the book did not, and which line for Anand survives every check the day built.

## Why does each of the six keys hold, from the fingerprint's seven numbers to the tier's 0.706?

### Q1. Which way tells a changed book from a changed query on read access, sized over a quarter of Mondays?

Kind: a design item, the best-fit way sized over 13 Mondays, under the constraint of read access. The
suite prints 18 rows each Monday.

The key is c, "A fingerprint block: 7 numbers printed with each run and nothing stored; a changed one
means the book moved". The seven numbers describe the book, so when a Monday's results differ from
last week's and the seven did not move, the query moved. Printing them is one more query on the book,
which read access allows, and over the quarter it stores nothing.

- a, "Rerun the suite and compare it with last week's by eye": the difference shows, and nothing in
  either run says whether the book or the query caused it.
- b, "Snapshot the outputs into a table: 234 rows stored over 13 Mondays": 18 rows times 13 Mondays is
  234 rows, and storing them needs the right to write to the warehouse, which read access does not
  give. A snapshot would also say which output moved without saying why.
- d, "Write, audit, publish: 13 staging tables over the quarter": the strongest way, and it needs
  write access and a scheduler, which the team does not have yet.

### Q2. Which way would have stopped two bad runs before Anand read them, once the team can write and schedule?

Kind: a design item, the way that fits once the fact behind item 1 switches, judged by what each
check would see in two invented bad runs: a reload that emptied a day's amounts, and a ratio divided
as whole numbers.

The key is b, "Write, audit, publish with the fingerprint and the multiply-back check in its audit:
both runs stop in staging". The empty amounts drop the fingerprint's rupees while its rows stay at
1,000, and an audit that sets each run's fingerprint beside last week's holds any change until someone
explains it, so that run waits in staging. The integer division leaves the book alone and breaks the
tree: orders per customer at 1 times Retail-Plus's 76 customers who bought is 76 orders, against the
140 the tier booked, so the multiply-back check fails that run. Anand reads neither sheet.

- a, "The fingerprint alone, printed beside each run": it shows the rupee fall, but only beside a
  sheet Anand already has, and the integer division leaves all seven numbers where they were.
- c, "A snapshot table of each Monday's outputs": a history records both bad runs after they were
  read and stops neither.
- d, "Write, audit, publish with a row-count check alone": the empty amounts leave 1,000 rows and the
  division changes no row, so both runs pass the only check and are published.

### Q3. Which change to the book would the seven-number fingerprint miss?

Kind: judge what a check can see. The fingerprint counts rows, rupees, distinct customers and latest
dates on the two tables.

The key is c, "A Retail-Core customer moved to Retail-Plus on the customers table". The customer is
still one row, still one distinct customer, and the latest joining date does not move, so all seven
numbers stay put, while the segment lines on the sheet change for both segments. A fingerprint says
whether rows were added, removed or repriced; a changed value on a row needs a check of its own, such
as a count per segment.

- a, "A late Q2 order added to the orders table after Monday's run": rows go to 1,001 and the rupees
  move.
- b, "An order's amount corrected from Rs 1,200 to Rs 2,100 overnight": the rupees move by Rs 900.
- d, "A new member added to the customers table with a joining date in October": the customers table
  goes to 341 rows and its latest joining date moves.

### Q4. What most likely explains a traced sample that changed overnight while the fingerprint did not?

Kind: spot the plausible wrong reading, on invented ids and amounts. Monday's five total Rs 5,000 and
the rerun's Rs 5,390; the fingerprint is the same.

The key is d, "With no ORDER BY the database returned an unspecified five, and the overnight reload
moved rows". Without `ORDER BY`, Postgres returns rows in whatever order it reads them, and `LIMIT 5`
keeps the first five of that order. A reload that rewrites a row, even with its own values, writes a
new version of it in a new place, so the rerun meets the rows in a different order and keeps a
different five.

- a, "The book changed overnight, since the rerun found two orders that Monday's run did not": the
  fingerprint's rows, rupees and customers are unchanged, and S-116 and S-119 were in the book on
  Monday too.
- b, "LIMIT keeps the five most recent orders, and two newer cancellations arrived overnight": LIMIT
  keeps five in whatever order the result has, and the fingerprint's unchanged rows show no order
  arrived.
- c, "The analyst's query filtered on a different status, since the two samples share only three
  orders": the query is the same text, and a different status would not keep three of the same
  cancelled orders.

### Q5. Which route confirms the five cancelled store orders without trusting the database's ordering?

Kind: a design item, the independent second route with its size. There are 19 cancelled Q2 store
orders on the book.

The key is b, "Fetch all 19 candidates, sort them by order id in Python and take the first five". The
sort happens outside the database, on every candidate, so the five it keeps depend only on the order
ids. It moves 19 rows to confirm five, which is cheap at this size.

- a, "Rerun the same ordered query twice more and check that all three fives agree": the same query
  relies on the same ordering, so it repeats rather than confirms.
- c, "Fetch five rows with LIMIT 5 and sort those five by order id in Python": sorts whichever five
  came back, so an unspecified five comes out neatly sorted.
- d, "Fetch all 19 candidates and keep the first five in the order the database sends them": moves
  the unspecified order from SQL into Python.

### Q6. Which line tells Anand what the Monday suite found?

Kind: choose the line for the stakeholder, across the day's chapters. Retail-Plus's buyers went from
91 to 76, its orders per customer from 2.36 to 1.84 and its revenue per order from Rs 2,725 to
Rs 2,953.

The key is a, "Booked revenue fell 1.6 percent; Retail-Plus fell 29.4 percent: 16.5 percent fewer
members, each ordering 22.0 percent less often, each order 8.4 percent larger". 76 over 91 is 0.835,
16.5 percent fewer members buying; 1.84 over 2.36 is 0.780, 22.0 percent less often; Rs 2,953 over
Rs 2,725 is 1.084, each order 8.4 percent larger. The three multiply to 0.835 times 0.780 times 1.084,
which is 0.706, the tier's revenue ratio, so the line ties back to the 29.4 percent it explains.

- b, "customers held flat across both quarters, and each of them ordered 14.0 percent less often":
  last week's extract, which the book contradicts; Kalpa's customers went from 244 to 227, down 7.0
  percent.
- c, "Retail-Plus members halved their orders, from 2 each to 1 each": whole-number division of 215
  by 91 and 140 by 76; in numeric the fall is 22.0 percent.
- d, "spend per Retail-Plus member fell 15.5 percent, from Rs 6,437 to Rs 5,439": each quarter's
  revenue over its own buyers, 91 and then 76, which leaves out the members who stopped; over the
  107 who bought in either quarter the levels are Rs 5,474 and Rs 3,863, down 29.4 percent.

## Why is option d in item 3, a new customer who has bought nothing, worth arguing about?

Some will say a new member slips past, since a member who joins and buys nothing leaves the orders
table untouched. The customers table's rows and latest joining date both move, so the fingerprint
catches it. The change it cannot see is one that alters a value without adding, removing or repricing
a row, and the segment a customer belongs to is exactly such a value on this sheet. That is the
argument for adding a count per segment to the fingerprint once the suite reports by segment.

## Where does Netflix's team audit each run before publishing it?

At the DataWorks Summit in San Jose on 13 June 2017, Michelle Ufford of Netflix described write,
audit, publish: a new batch is written to an audit table first, checks run on it, and only then is it
published. One slide set a batch of 17,240 rows carrying 17,240 missing values beside the previous
day's 16,135 rows with 21; in that walk-through the row-count checks could fail the job and the
missing-value check raised a warning. Item 2's audit is the same step at Kalpa's size, with the
fingerprint and the multiply-back check as the two checks that fail a run.

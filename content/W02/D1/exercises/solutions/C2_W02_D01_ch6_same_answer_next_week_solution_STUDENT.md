# Which answers hold in the chapter 6 set on whether next Monday's run repeats, and why?

Answers: 1c 2a 3c 4d 5b 6b

Chapter 6 made the Monday suite repeatable. A fingerprint of seven numbers prints beside every run, so
a difference next Monday says whether the book moved or the query did. Five delivered Q2 app orders
drawn with `LIMIT 5` and no `ORDER BY` came back as Rs 3,900 on one run and Rs 4,590 on the analyst's
rerun after an overnight reload that rewrote two rows with their own values, while the fingerprint
stayed the same; ordering on the order id gave the same five, Rs 3,900, both times. The set carries
those habits to a new sample and to the question of what the fingerprint can and cannot see. Three of
the six items are design items: 1, 2 and 5.

**Who needs the answer.** You, checking your six letters after the lab or tonight. The analyst signs
the suite only when a rerun on the same book gives the same answer, and a sample that moves on its own
costs her a Monday of tracing.

**The questions on the way.**

- Which idea does this set test?
- Why is each key right, item by item?
- Which wrong answer is worth arguing about?
- Where does this show up at work?

## Which idea does this set test?

A run that can be audited says what book it read and returns its lists in an order the rerun will
repeat. The design items choose how a run proves itself under read access, switch the choice when
write access arrives, and confirm an ordered sample by a route outside the database. The other items
ask what a fingerprint misses, what explains a sample that moved while the book did not, and which
summary line survives every check the day built.

## Why is each key right, item by item?

### Q1. Which way shows whether a change came from the book or the query, for a team with read access only?

Kind: a design item, the best-fit way under a constraint, with what each adds to a run.

The key is c, "A fingerprint block run with the suite, seven numbers describing the book, on read
access". Seven numbers printed beside the results tell a changed book from a changed query, and
printing them needs only the read access the team holds.

- a, "Rerun the suite and compare it with last week's by eye, adding nothing to the run": when the
  numbers differ, nothing in the run says whether the book moved.
- b, "Snapshot each Monday's outputs into a table, about 18 rows a Monday, which needs write access":
  a stored history helps, and read access cannot write it.
- d, "Write, audit and publish: a staging table and a scheduler, which need write access": the
  strongest way, and out of reach until the team can write and schedule.

### Q2. Which way fits once the team can write to the warehouse and schedule its runs?

Kind: a design item, the fact that switches the choice. The platform lead grants a schema and a
scheduler.

The key is a, "Write, audit and publish, so a run reaches the sheet only once its checks pass in
staging". Write access and a scheduler are the fact that makes this way possible, and it is the one
way that stops a bad run before Anand sees it; the fingerprint then becomes one of the checks in
staging.

- b, "The fingerprint block alone, since write access adds nothing a fingerprint cannot show": the
  fingerprint reports a change after the numbers are out, while a staging check holds them back.
- c, "Snapshot every Monday's outputs into a table, since a stored history is the strongest proof a
  run can leave": a history shows what was published, including a bad run, and stops nothing.
- d, "Rerun and compare by eye, since a scheduler removes the need for any stored check": a scheduler
  runs the job on time and checks nothing by itself.

### Q3. Which change to the book would the seven-number fingerprint miss?

Kind: judge what a check can see. The fingerprint counts rows, rupees, distinct customers and latest
dates on the two tables.

The key is c, "A Retail-Core customer moved to Retail-Plus on the customers table". The customer is
still one row, still one distinct customer, and the latest joining date does not move, so all seven
numbers stay put, while the segment lines on the sheet change for both segments. A fingerprint says
whether rows were added, removed or repriced; a changed attribute on a row needs a check of its own,
such as a count per segment.

- a, "A late Q2 order added to the orders table after Monday's run": rows go to 1,001 and the rupees
  move.
- b, "An order's amount corrected from Rs 1,200 to Rs 2,100 overnight": the rupees move by Rs 900.
- d, "A new member added to the customers table with a joining date in October": the customers table
  goes to 341 rows and its latest joining date moves.

### Q4. What most likely explains a traced sample that changed overnight while the fingerprint did not?

Kind: spot the plausible wrong reading, on invented ids and amounts. Monday's five total Rs 5,000 and
the rerun's Rs 5,390; the fingerprint is the same.

The key is d, "With no ORDER BY the database returned an unspecified five, and the reload moved rows".
Without `ORDER BY`, Postgres returns rows in whatever order it finds them, and `LIMIT 5` keeps the
first five of that order. A reload that rewrites a row, even with its own values, writes a new version
of it in a new place, so the rerun meets the rows in a different order and keeps a different five.

- a, "The book changed overnight, since the rerun found two orders that Monday's run did not": the
  fingerprint's rows, rupees and customers are unchanged, and S-116 and S-119 were in the book on
  Monday too.
- b, "LIMIT keeps the five most recent orders, and two newer cancellations arrived overnight": LIMIT
  keeps five in whatever order the result has, and with no new rows the fingerprint shows none arrived.
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
91 to 76 and its orders per customer from 2.36 to 1.84.

The key is b, "Booked revenue fell 1.6 percent; Retail-Plus fell 29.4 percent as 16.5 percent fewer
members bought, each 22.0 percent less often". 76 over 91 is 0.835, 16.5 percent fewer members buying,
and 1.84 over 2.36 is 0.780, 22.0 percent less often, which with revenue per order up 8.4 percent
multiply back to the tier's 0.706.

- a, "Booked revenue fell 1.6 percent; customers held flat across both quarters, and each of them
  ordered 14.0 percent less often": last week's extract; the book shows 244 customers falling to 227,
  down 7.0 percent.
- c, "Booked revenue fell 1.6 percent; Retail-Plus members halved their orders, from 2 each to 1 each,
  in one quarter": whole-number division of 215 by 91 and 140 by 76; the ratio in numeric fell 22.0
  percent.
- d, "Booked revenue fell 1.6 percent; spend per Retail-Plus member fell 15.5 percent, from Rs 6,437 to
  Rs 5,439, a milder fall than its orders": each quarter's average over its own buyers, which leaves
  out the members who stopped; over the same members the fall is 29.4 percent.

## Which wrong answer is worth arguing about?

Item 3, option d. Some will say a new member slips past, since a member who joins and buys nothing
leaves the orders table untouched. The customers table's rows and latest joining date both move, so
the fingerprint catches it. The change it cannot see is one that alters a value without adding,
removing or repricing a row, and the segment a customer belongs to is exactly such a value on this
sheet. That is the argument for adding a count per segment to the fingerprint once the suite reports
by segment.

## Where does this show up at work?

At the DataWorks Summit in San Jose on 13 June 2017, Michelle Ufford of Netflix described
write-audit-publish: a new batch is written to an audit table first, checks run on it, and only then
is it published. One slide set a batch of 17,240 rows carrying 17,240 missing values beside the
previous day's 16,135 rows with 21; in that walk-through the row-count checks could fail the job and
the missing-value check raised a warning. A fingerprint beside the numbers is the read-access version
of the same idea.

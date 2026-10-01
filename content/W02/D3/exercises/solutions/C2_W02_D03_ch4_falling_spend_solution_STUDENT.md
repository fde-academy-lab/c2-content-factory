# Which answers hold in the chapter 4 set on whose monthly spend fell two months running, and why?

Answers: 1c 2b 3d 4a 5b

Chapter 4 set each member's months beside the months before them. The monthly table holds 752
member-months for 301 members, and LAG read them in one pass, where a self-join or a lookup per row
works through 1,504 and a spreadsheet of months holds 1,806 cells. With no PARTITION BY, LAG ran from
one member's last row into the next member's first and flagged 20 members, 4 of them on another
member's months, and reading the member id LAG had reached exposed the 4. With PARTITION BY
customer_id the flag kept 16, and a walk through each member's months in Python found the same 16.
Three of the five items are design items: 1, 4 and 5.

**Who needs the answer.** You need it to check your five letters after the lab or tonight. Every flag puts a
call through to a member, so a flag built on another member's months accuses someone of a fall that
happened in somebody else's account.

**The questions on the way.**

- What does the falling-spend set test about whose months LAG reads?
- Why is each falling-spend key right, and each other letter wrong?
- Why is item 3's single NULL worth arguing about?
- Where does a real company judge each customer against their own past?

## What does the falling-spend set test about whose months LAG reads?

LAG reads whichever row sits before the current one in its window, so the window has to keep each
member's months to that member, and a flag is only as good as the rows it actually read. The design
items size LAG against the self-join, choose a second route that rebuilds the whole list with no window,
and name the fact about the book that would make the self-join the build to ship. The other two items
predict what an unpartitioned LAG flags on a small table and choose the check that catches it on a
large one.

## Why is each falling-spend key right, and each other letter wrong?

### Q1. Which way should set each month beside the two before it, and what does the self-join work through?

This is a design item: it asks for the best-fit build with its size.

The key is c, "LAG in a window: one pass over the 752 member-months, where the self-join makes 1,504
lookups". `lag(spend, 1)` and `lag(spend, 2)` sit in the same SELECT and read the 752 rows once, while
the self-join joins the table to itself once for the month before and once for the month before that,
so it looks each of the 752 rows up twice, 1,504 lookups, whether or not a month is found.

- Option a, "A self-join of the monthly table to itself, twice: 752 lookups, the same work as one
  pass", counts one join where there are two, and two joins look each of the 752 rows up twice, 1,504.
- Option b, "Months as spreadsheet columns, read by eye: 752 cells, one for each member-month with an
  order", counts only the filled cells, since a sheet of months holds a cell for every member in every
  month, 301 times 6, 1,806, most of them empty, and a person has to read them all.
- Option d, "A correlated subquery per month, one lookup for each row: 752 lookups, the same work as
  LAG", forgets the second month back, since the flag needs two lookups per row, 1,504.

### Q2. Which members does a flag with no PARTITION BY name in the invented table?

This item asks you to predict the output on invented numbers.

The key is b, "X-01 and X-02, since X-02's one row reads X-01's September and August above it". With
no PARTITION BY the window is the whole sorted table. X-01's September reads their own August, Rs 2,800,
and July, Rs 3,700, and falls twice, which is right. X-02's only row reads X-01's September, Rs 2,300,
and August, Rs 2,800, so X-02's Rs 1,700 looks like a second fall that never happened. X-03's September
reads their own August, Rs 2,000, and X-02's September, Rs 1,700, and since Rs 2,000 is above Rs 1,700
the second step fails.

- Option a, "X-01 alone, since LAG starts over at X-02's first row and reads nothing above it",
  describes what PARTITION BY customer_id would do, and this window has none, so LAG reads straight
  from X-01's rows into X-02's.
- Option c, "X-01, X-02 and X-03, since each September row has two rows above it in the table", is
  right that X-03's September has two rows above it, X-03's own August at Rs 2,000 and X-02's September
  at Rs 1,700, but Rs 2,000 sits above Rs 1,700, so the second fall fails.
- Option d, "Nobody, since LAG gives NULL on every row until the window has a PARTITION BY", misreads
  LAG, which needs only an order: with no partition it returns NULL on the table's first row alone and
  reads across members everywhere else.

### Q3. Which check proves that every value LAG read came from the row's own member, and what must it read?

This item asks you to choose the check that proves the window, and the value it must read.

The key is d, "Add `lag(customer_id)` over the same window and count the rows where it names another
member: 0". The id LAG reached says whose month the value came from, so any row where it differs from
the row's own member is a comparison across members. On the partitioned window the count is 0 across
all 752 rows. On chapter 4's hurried window it is 300 across the table, one on every member's first
row after the first member's, and among the 20 September flags it picks out the 4 that read another
member's month.

- Option a, "Count the flagged members beside the members who ordered in September: the flag must be
  smaller", passes whether or not the window crossed members, since 20 and 16 are both below 118.
- Option b, "Count the rows where `lag(spend, 1)` is NULL: it must read 1, the first row of the sorted
  table", expects the count the broken window gives, since a partitioned window returns one NULL on
  every member's first row, 301 on this book.
- Option c, "Sort the output by customer id and month again: a sorted result cannot cross between
  members", trusts the very sort that did the damage, since the hurried window was already ordered by
  customer id and month, and that order carried LAG from one member's last row into the next member's
  first.

### Q4. Which second route could a slip in the window not fool, and what does it read?

This is a design item: it asks for the independent second route and what it reads.

The key is a, "A walk in Python through the 752 member-months, grouped by member and sorted there: 752
rows". The walk groups the rows by member in a dictionary and sorts each member's months itself, so a
missing PARTITION BY or a wrong ORDER BY in the window cannot move it, and it reads every member-month,
so it can find a member the window missed as well as one the window named wrongly. In the chapter it
flagged the same 16 members.

- Option b, "The same LAG query rerun after the platform's overnight reload, set beside the first: 752
  rows", runs the same window twice, so it repeats whatever the window got wrong.
- Option c, "The LAG query run once per segment, with the same window in each of the four: 752 rows",
  shares the window, so a missing partition still crosses members inside each segment.
- Option d, "A walk in Python through the 16 flagged members' months, grouped by member and sorted: 68
  rows", shares no window and re-checks each of the 16 correctly, but it reads only their 68
  member-months, so a member the window failed to flag never reaches it, and a slip in the ORDER BY
  that dropped a member would pass this check.

### Q5. Which fact would make the self-join the build to ship?

This is a design item: it asks for the fact that would switch the build.

The key is b, "Only 50 of the 118 members who ordered in September had also placed an order in
August". LAG over a member's own rows reads the row before, which is the calendar month before only
when the member bought in it. With 68 of the 118 September buyers holding no August row, LAG's step back
from September lands on July or an earlier month for 60 of them and on nothing for the 8 whose
September was their first order, so a flag built on it compares months Marketing did not name. The
self-join matches September to the member's rows dated August and July, so a member with no August row
has nothing to join to and the run breaks, as Marketing's words require. On this book the self-join
keeps 9 members where LAG over each member's own rows keeps 16; chapter 6 reaches the same 9 by
checking which months LAG read.

- Option a, "The book grows to twelve months next year, so LAG will read twice as many member-months",
  doubles the self-join's matches as well, so LAG stays the cheaper build, and the size of the book
  says nothing about which months each build reads.
- Option c, "Marketing wants the flag read at August as well, which takes a second pass with LAG",
  misjudges LAG's output, which already sets every month beside the rows before it, so a reading at
  August is a different filter on the same pass.
- Option d, "For 8 members, September was their first order, so LAG finds no row before it for them",
  describes members on whom the two builds agree: LAG's NULL leaves them unflagged, and the self-join
  finds no August or July row for them, so it leaves them unflagged too. The switch comes from members
  who did buy before September and skipped August, 60 of them.

## Why is item 3's single NULL worth arguing about?

Item 3's option b, the count of NULLs from `lag(spend, 1)`, starts from a sound instinct, since the
first row of every member should have nothing before it. It has the expected value backwards: a single
NULL in the whole table is the sign that the window ran across members, and the right count is one per
member, 301 on this book, which is why the value a check must read is worth writing down before the
check runs.

## Where does a real company judge each customer against their own past?

Square, the point-of-sale company, gives its sellers a ready-made "Lapsed" group: "customers who were
regulars, but haven't visited in the last six weeks", where a regular visited three times in the last
six months (Square Support Center, the page on customer groups and filters, checked 1 October 2026).
Each customer is judged against their own earlier visits, which only works if the history being read
is that customer's own.

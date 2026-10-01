# Which answers hold in the chapter 4 set on whose monthly spend fell two months running, and why?

Answers: 1c 2b 3d 4a 5b

Chapter 4 set each member's months beside the months before them. The monthly table holds 752
member-months for 301 members, and LAG read them in one pass, where a self-join or a lookup per row
works through 1,504 and a spreadsheet of months holds 1,806 cells. With no PARTITION BY, LAG ran from
one member's last row into the next member's first and flagged 20 members, 4 of them on another
member's months; carrying `lag(customer_id)` beside the value exposed the 4. With PARTITION BY
customer_id the flag kept 16, and a walk through each member's months in Python found the same 16.
Three of the five items are design items: 1, 4 and 5.

**Who needs the answer.** You, checking your five letters after the lab or tonight. Every flag puts a
call through to a member, so a flag built on another member's months accuses someone of a fall that
happened in somebody else's account.

**The questions on the way.**

- Which idea does this set test?
- Why is each key right, item by item?
- Which wrong answer is worth arguing about?
- Where does this show up at work?

## Which idea does this set test?

A window has to be told whose rows belong together, or it compares anyone with anyone. The design
items size LAG against the self-join, choose a second route that shares no window, and name the system
that would force the self-join. The other items predict what an unpartitioned LAG flags on a small
table and choose the check that catches it on a large one.

## Why is each key right, item by item?

### Q1. Which way should set each month beside the two before it, and what does the self-join work through?

Kind: a design item, the best-fit way with its size.

The key is c, "LAG in a window: one pass over the 752 member-months, where the self-join makes 1,504
matches". `lag(spend, 1)` and `lag(spend, 2)` sit in the same line and read the 752 rows once; the
self-join joins the table to itself once for the month before and once for the month before that.

- a, "A self-join of the monthly table to itself, twice: 752 matches, the same work as one pass": two
  joins match the 752 rows twice, 1,504.
- b, "Months as spreadsheet columns read by eye: 752 cells, one for each member-month with an order": a
  sheet of months holds a cell for every member in every month, 301 times 6, 1,806, most of them
  empty, for a person to read.
- d, "A correlated subquery per month, one lookup for each row: 752 lookups, the same work as LAG": the
  flag needs the month before and the month before that, two lookups per row, 1,504.

### Q2. Which members does a flag with no PARTITION BY name in the invented table?

Kind: predict the output, on invented numbers.

The key is b, "X-01 and X-02, since X-02's one row reads X-01's September and August above it". With no
PARTITION BY the window is the whole sorted table. X-01's September reads his own August, Rs 2,800, and
July, Rs 3,700, and falls twice, which is right. X-02's only row reads X-01's September, Rs 2,300, and
August, Rs 2,800, so X-02's Rs 1,700 looks like a second fall that never happened. X-03's September
reads his own August, Rs 2,000, and X-02's September, Rs 1,700, and since Rs 2,000 is above Rs 1,700 the
second step fails.

- a, "X-01 alone, since LAG returns nothing before X-02's first row": that is what PARTITION BY
  customer_id would give, and this window has none.
- c, "X-01, X-02 and X-03, since every September row has two rows above it in the sorted table": X-03
  has two rows above his September, and they do not fall in a row.
- d, "Nobody, since LAG returns NULL until the window is given a PARTITION BY": LAG needs only an
  order; without a partition it reads straight across members.

### Q3. Which check proves that every value LAG read came from the row's own member, and what must it read?

Kind: choose the check.

The key is d, "Carry `lag(customer_id)` beside `lag(spend)`; count rows where it differs from the
row's member: 0". The id LAG read says whose month the value came from, so any row where it differs
from the row's own member is a comparison across members. On a partitioned window the count is 0; on
chapter 4's hurried flag it found the 4 crossings among the 20.

- a, "Count the flagged members beside the members who ordered in September: the flag must be the
  smaller": the flag is smaller whether or not it crossed members, 20 or 16 against 118.
- b, "Count the rows where `lag(spend, 1)` is NULL: it must read 1, the first row of the sorted table":
  one NULL is what the broken window gives. A partitioned window gives one NULL for every member's
  first row, 301 on this book.
- c, "Sort the output by customer id and month once more: a sorted result cannot cross between
  members": the hurried window was already sorted that way, and the sort is what carried LAG from one
  member into the next.

### Q4. Which second route could a slip in the window not fool, and what does it read?

Kind: a design item, the independent second route with its size.

The key is a, "A walk in Python through the 752 member-months, grouped by member and sorted there: 752
rows". The walk groups rows by member in a dictionary and sorts each member's months itself, so a
missing PARTITION BY or a wrong ORDER BY in the window cannot move it. In the chapter it flagged the
same 16 members.

- b, "The same LAG query rerun after the platform's overnight reload, set beside the first run: 752
  rows": the same query twice repeats whatever it got wrong.
- c, "The LAG query run once per segment, with the same window in each of the four: 752 rows in all":
  the window is shared, so a missing partition inside a segment still crosses members.
- d, "A count of the flagged members' September orders, set beside the 16: one row per flagged member":
  counts orders of members already flagged and cannot say whether the flag was right.

### Q5. Which fact would make the self-join the build to ship?

Kind: a design item, the fact that would switch the call.

The key is b, "The flag has to run on a MySQL server older than version 8.0, with no window
functions". Window functions arrived in MySQL with release 8.0, so an older server cannot run LAG, and
the self-join of the monthly table to itself, once for each month back, does the same job with plain
joins.

- a, "The book grows to twelve months next year, so LAG has twice as many member-months to read": a
  longer book costs the self-join twice what it costs LAG.
- c, "Marketing wants the flag read at August as well as at September": the same LAG output answers
  it with a different filter on the month.
- d, "Some members bought in only one month, so LAG returns NULL on every one of their rows": NULL is
  the right answer for a member with no earlier row, and the self-join gives the same.

## Which wrong answer is worth arguing about?

Item 3, option b. Counting NULLs is a good instinct, since the first row of every member should have
nothing before it. The option has the expected value backwards: a single NULL in the whole table is
the sign the window ran across members, and the right count is one per member, 301 on this book. A
check is only as good as the value you expect it to read, so say that value before you run it.

## Where does this show up at work?

Square, the point-of-sale company, gives its sellers a ready-made "Lapsed" group: "customers who were
regulars, but haven't visited in the last six weeks", where a regular visited three times in the last
six months (Square Support Center, the page on customer groups and filters, checked 1 October 2026).
Each customer is judged against their own earlier visits, which only works if the history being read
is that customer's own.

# Which answers hold in the chapter 1 set on which fifty members spent the most in Q2, and why?

Answers: 1c 2a 3d 4b 5c

Chapter 1 ranked Kalpa Retail's 227 Q2 members by Q2 revenue. The fifty who spent most are 35 Business
members, which is every Business buyer, then 11 Retail-Plus and 4 Retail-Core members, and no Student;
together they carry Rs 9,77,70,580, 99.4 percent of Q2. The quickest list, the fifty biggest Q2 orders,
named only 28 members, all of them Business, and a count of different members set beside the rows
caught it. A sort in Python over the 462 Q2 orders picked the same fifty members in the same order.
The set carries those habits to new numbers. Three of the five items are design items: 1, 4 and 5.

**Who needs the answer.** You need it to check your five letters after the lab or tonight. The marketing
lead's member team rings every name on the list, so a list whose unit or whose check is wrong costs
real calls.

**The questions on the way.**

- Which idea does this set test?
- Why is each key right, item by item?
- Which wrong answer is worth arguing about?
- Where does this show up at work?

## Which idea does this set test?

A ranked list is first a decision about what one row is, and only then a sort. The design items choose
the build that keeps the place as a column the per-segment list can use, sized in rows and queries,
the second route that could notice a missing member, and the fact that would make the shorter build
enough. The other items catch a list of orders sent as a list of members and predict which segments a
whole-book list reaches.

## Why is each key right, item by item?

### Q1. Which build fits Marketing's per-segment ask, and what does each build cost?

Kind: a design item, the best-fit build with its size.

The key is c, "Group by member and number the members in a window: 50 rows leave, and each segment's
list is one more phrase". One row per member carries its place as a column, fifty rows leave the
warehouse, and chapter 2's list per segment is one more phrase inside the same window,
`PARTITION BY segment`.

- a, "Sort the Q2 order rows by amount and keep fifty: 50 rows leave, and each segment's list is one
  more filter": the rows are orders, so a filter by segment still lists orders. Chapter 1's version
  named 28 members in 50 rows.
- b, "Group by member, sort and keep fifty with LIMIT: 50 rows leave, and each segment's list is one
  more phrase": the same fifty today, with the cost misread. LIMIT counts rows across the whole result,
  so each segment needs its own sorted query, four glued together.
- d, "Export the Q2 orders and sort them by hand in a spreadsheet: 462 rows leave, and each segment's
  list is four sorts": the cost is right, and moving all 462 Q2 order rows out of the warehouse breaks
  the data platform lead's rule.

### Q2. What is wrong with the colleague's top ten, and which check catches it?

Kind: spot the plausible wrong output, on invented numbers.

The key is a, "Each row is an order, so six members fill ten places; a count of distinct members
beside the rows reads 6 for 10". P holds three places, Q and R two each, and S, T and U one each, so
ten rows name six members. In SQL the check is `count(DISTINCT customer_id)` beside `count(*)` on the
finished list, and a list of members reads the same number twice. The fix adds up each member's orders
in a named step and ranks the members.

- b, "Each row is a member, so the list is right; a count of its rows beside Marketing's ask reads 10
  for 10": a row count reads ten whatever one row is, so it cannot tell orders from members.
- c, "Each row is an order, so P's three orders inflate the list's total; its sum beside Q2's total
  catches it": each order is counted once, so the total is not inflated, and a top ten is meant to
  carry only part of the quarter, so the comparison flags nothing.
- d, "Each row is a member, and P shows three times because of a tie; a tiebreaker in the ORDER BY
  removes the repeats": P's three rows carry three different amounts, so they are three orders, and no
  tiebreaker turns orders into members.

### Q3. If Marketing trimmed the whole-book list to forty, which segments would it reach?

Kind: predict the number from the exhibit.

The key is d, "35 Business, 3 Retail-Plus and 2 Retail-Core, and no Student". The smallest Business
quarter, Rs 2,25,000 at place 35, is about ten times the largest retail one, Rs 21,740, so places 1
to 35 are the 35 Business buyers. Places 36 to 40 are C-0170, C-0167 and C-0160 of Retail-Plus and
C-0010 and C-0040 of Retail-Core.

- a, "6 Business, 17 Retail-Core, 13 Retail-Plus and 4 Student, in proportion to the members who
  bought": a ranked list keeps the members who spent most, wherever they sit; shares in proportion to
  the buyers describe a sample, which nobody asked for.
- b, "35 Business and 5 Retail-Plus, since a Retail-Plus member outspends a Retail-Core one on
  average": an average says nothing about who is fortieth. C-0010 of Retail-Core, on Rs 13,910,
  outspent C-0160 of Retail-Plus, on Rs 13,700.
- c, "35 Business, 2 Retail-Plus and 3 Retail-Core, and no Student": swaps the two counts. Places 36,
  37 and 39 are Retail-Plus members.

### Q4. Which second route could catch a member wrongly left off the fifty, and how many rows does it move?

Kind: a design item, the independent second route with its size.

The key is b, "Pull the 462 Q2 order rows into Python, total each member in a dictionary and sort:
462 rows". It shares no code with the window: it adds up each member's orders and sorts in Python, so
a slip in the window's ORDER BY, or a filter that dropped a member, shows up as a different list. In
the chapter it returned the same fifty members in the same order. It moves 462 rows to check what the
query returned in 50, so the team runs it to check the query, and the query stays the answer.

- a, "Pull the fifty rows the query returned into a spreadsheet and sort them again by revenue: 50
  rows": a member left off the list is not among the fifty, so sorting the fifty again cannot find them.
- c, "Run the same window query again tomorrow and set the two lists side by side: 50 rows each": the
  same query twice repeats whatever it got wrong.
- d, "Add up the fifty members' Q2 revenue and set it beside the quarter's Rs 9,84,00,000: one row":
  the fifty carry Rs 9,77,70,580, 99.4 percent, and a member swapped at the line moves that by a few
  thousand rupees, with nothing on the page to say what the sum should be.

### Q5. Which fact would make the shorter build, GROUP BY with LIMIT 50, the better call?

Kind: a design item, the fact that would switch the call.

The key is c, "Marketing wants one overall list to read by eye, and no later step uses the place".
Then GROUP BY, ORDER BY and LIMIT 50 returns the same fifty in a shorter query, and a place held as a
column, which a later step could count or filter, earns nothing.

- a, "The book grows past 10,000 orders next year, and a window over that many rows runs too slowly":
  both builds read the orders once and sort the members once, so size does not separate them.
- b, "Marketing wants a list in each segment, and LIMIT 50 can be written once for each of the four":
  that is the cost that rules the shorter build out, four sorted queries glued together.
- d, "Two members tie at fiftieth place, and LIMIT 50 keeps exactly fifty rows whatever the tie": LIMIT
  drops one of the pair by whatever order the rows arrive in, which argues against the shorter build.
  Chapter 3 takes up the tie.

## Which wrong answer is worth arguing about?

Item 4, option d. A sum set beside the quarter's total is a good first look.
It cannot answer the question asked, because a member who belongs on the list and is missing from it
moves the sum by a few thousand rupees on a figure of nearly ten crore, and nothing tells you what the
sum should have been. Item 4's key can fail, because it reaches the list by a route of its own.

## Where does this show up at work?

Starbucks Rewards members made 59 percent of the money tendered at Starbucks' company-operated US
stores in the quarter that ended on 28 June 2026, and 35.8 million US members were active in the 90
days to that date (Starbucks' card, loyalty and mobile dashboard for the third quarter of fiscal 2026,
checked 1 October 2026). When members carry more than half of the money, the list of which members
carry it, one row per member, is the first thing a retention offer needs.

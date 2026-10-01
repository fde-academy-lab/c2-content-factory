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

- What does the top-fifty set test about building and checking a ranked list?
- Why is each top-fifty key right, and each other letter wrong?
- Why is item 4's sum beside the quarter's total worth arguing about?
- Where does a real company need its best members listed one row per member?

## What does the top-fifty set test about building and checking a ranked list?

A ranked list is first a decision about what one row is, and only then a sort. The design items choose
the build for a top twenty-five in each segment by what each build costs on Q2's data, pick the second
route, a different way to the same list, that could notice a missing member, and name the ask that
would make the fifty biggest orders the right list. The other items catch a list of orders sent as a
list of members and predict which segments a whole-book list reaches when it is trimmed.

## Why is each top-fifty key right, and each other letter wrong?

### Q1. Which build fits a top twenty-five in each segment, and what does it cost on Q2's data?

This is a design item: it asks for the best-fit build, judged on a cost you have to check against the
segment table.

The key is c, "Number the members in a window that restarts in each segment: one query, and 95 rows
leave". Numbering members makes one row a member, and a window that starts again at 1 in each segment
hands Marketing all four lists from one query. The cost checks against the table: each list keeps its
twenty-five biggest spenders, or all of them where a segment has fewer than twenty-five buyers, so
Business, Retail-Core and Retail-Plus give 25 each and Student 20, which is 95 rows.

- Option a, "Sort each segment's Q2 orders by amount and keep twenty-five: 100 rows leave the
  warehouse", carries the right cost, and the cost is the warning. Every segment placed at least
  twenty-five Q2 orders, Student's 38 included, so the four sorts keep 100 rows, yet four lists of
  members can hold at most 95 people. The rows are orders: the 100 name 85 members, and Business's
  twenty-five name only 20.
- Option b, "Rank members in four LIMIT 25 queries glued with UNION ALL, each reading all 462 Q2 orders",
  returns the same 95 members as c at four times the reading, 1,848 order rows, and leaves four
  queries to edit whenever a segment is added or renamed.
- Option d, "Export the 462 Q2 orders and sort each segment by hand: four sorts, and every row leaves",
  moves all 462 order rows out of the warehouse, which breaks the data platform lead's rule, "query it,
  do not export it", and repeats the four sorts by hand at every refresh.

### Q2. What is wrong with the colleague's top ten, and which check catches it?

This item asks you to spot a plausible wrong output on invented numbers and name the check that
catches it.

The key is a, "Each row is an order, so six members fill ten places; grouping the list by member shows
P three times". P holds three places, Q and R two each, and S, T and U one each, so ten rows name six
members. In SQL the check groups the finished list by member and keeps any member with more than one
row, `GROUP BY customer_id HAVING count(*) > 1`, and on a list of members it returns nothing. The fix
adds up each member's orders in a named step and ranks the members.

- Option b, "Each row is a member, and P's row was loaded three times over; a check for duplicate rows
  catches it", blames the load. A row loaded three times repeats whole, amount and all, and P's three
  rows carry three different amounts, Rs 9,40,000, Rs 8,10,000 and Rs 7,25,000, so the duplicate check
  finds nothing: they are three orders.
- Option c, "Each row is an order, so P's three orders inflate the list's total; its sum beside Q2's
  total shows it", names the right unit and the wrong harm. Each order is counted once, so the total is
  not inflated, and a top ten is meant to carry only part of the quarter, so the comparison flags
  nothing.
- Option d, "Each row is a member, and P shows three times because of a tie; a tiebreaker in the ORDER
  BY clears it", fails because P's three rows carry three different amounts, so no two of them tie, and
  no tiebreaker turns orders into members.

### Q3. If Marketing trimmed the whole-book list to forty, which segments would it reach?

This item asks you to predict a count from the exhibit.

The key is d, "35 Business, 3 Retail-Plus and 2 Retail-Core, and no Student". Places 33 to 35 are
Business, and no retail member can sit above them, because each retail segment's whole quarter is
smaller than place 33's Rs 5,73,000 (Retail-Plus booked Rs 4,13,380 in all), so places 1 to 35 are the
35 Business buyers. The smallest Business quarter, Rs 2,25,000 at place 35, is about ten times the
largest retail one, Rs 21,740. Places 36 to 40 are C-0170, C-0167 and C-0160 of Retail-Plus and C-0010
and C-0040 of Retail-Core.

- Option a, "28 Business, 9 Retail-Plus and 3 Retail-Core, and no Student", is the fifty's own mix, 35,
  11 and 4, scaled to four-fifths. Trimming a ranked list drops its last ten places, so every member
  above place 41 stays, and all 35 Business buyers sit above it.
- Option b, "35 Business and 5 Retail-Plus, and no Retail-Core or Student", follows the averages, where
  a Retail-Plus member outspends a Retail-Core one. An average says nothing about who is fortieth:
  C-0010 of Retail-Core, on Rs 13,910, outspent C-0160 of Retail-Plus, on Rs 13,700.
- Option c, "35 Business, 2 Retail-Plus and 3 Retail-Core, and no Student", swaps the two counts, since
  places 36, 37 and 39 are Retail-Plus members.

### Q4. Which second route could catch a member wrongly left off the fifty, and how many rows does it move?

This is a design item: it asks for an independent second route, a different way to the same list, with
its size.

The key is b, "Pull all 462 Q2 order rows into Python, total each member and sort the totals: 462 rows".
It shares no code with the window: it adds up each member's orders and sorts in Python, so a slip in
the window's ORDER BY, or a filter that dropped a member, shows up as a different list. In the chapter
it returned the same fifty members in the same order. It moves 462 rows to check what the query
returned in 50, so the team runs it to check the query, and the query stays the answer.

- Option a, "Pull the query's fifty rows into a spreadsheet and sort them again by revenue: 50 rows",
  cannot find a member left off the list, since that member is not among the fifty it sorts.
- Option c, "Run the same window query again tomorrow and set the two lists side by side: 50 rows
  each", runs the same query twice, so it repeats whatever the query got wrong.
- Option d, "Add up the fifty members' Q2 revenue and set it beside Q2's Rs 9,84,00,000: one row",
  gives a sum with nothing to hold it against. The fifty carry Rs 9,77,70,580, 99.4 percent, and a member
  swapped at the line, the last place a list keeps, fiftieth on a top fifty, moves that sum by a few
  thousand rupees.

### Q5. Which fact would make the fifty biggest Q2 orders the right list to hand over?

This is a design item: it asks for the fact that would switch the call to the quickest list, a fact the
chapter did not name.

The key is c, "Marketing wants a thank-you note for each of the fifty largest Q2 orders, one per order".
That ask is about orders, so one row of the answer is an order, and the fifty biggest orders are the
right list, repeats included: a member who placed three of the fifty largest orders gets three notes,
one for each.

- Option a, "The fifty biggest orders all come from different members, so no member's name repeats",
  would give fifty different names and still the wrong fifty, since the list ranks single orders. A
  member whose quarter is several mid-sized orders never shows: on Kalpa, a Business member missing from
  the orders list booked Rs 15,91,000 in Q2, more than the Rs 11,27,000 of the smallest spender it
  names.
- Option b, "Business orders run to lakhs, so the largest orders come from the members who spent most",
  is true of the 28 members the orders list names, every one of whom is among the fifty biggest
  spenders, and the list still misses 22 of those fifty and names two members five times each.
- Option d, "The fifty biggest orders carry most of Q2's revenue, so the list covers most of the
  money", is true, at 80.3 percent of Q2, and beside the point: Marketing protects members, and a list's
  share of the money says nothing about whether it names each best member once.

## Why is item 4's sum beside the quarter's total worth arguing about?

Item 4's option d, the fifty members' Q2 revenue set beside the quarter's total, is a good first look,
and a reviewer who sees 99.4 percent can feel the list is proven. It cannot answer the question asked,
because a member who belongs on the list and is missing from it moves the sum by a few thousand rupees
on a figure of nearly ten crore, and nothing tells you what the sum should have been. Item 4's key can
disagree with the query, because it reaches the list by a route of its own.

## Where does a real company need its best members listed one row per member?

Starbucks Rewards members made 59 percent of the money tendered at Starbucks' company-operated US
stores in the quarter that ended on 28 June 2026, and 35.8 million US members were active in the 90
days to that date (Starbucks' card, loyalty and mobile dashboard for the third quarter of fiscal 2026,
checked 1 October 2026). When members carry more than half of the money, the list of which members
carry it, one row per member, is the first thing a retention offer needs.

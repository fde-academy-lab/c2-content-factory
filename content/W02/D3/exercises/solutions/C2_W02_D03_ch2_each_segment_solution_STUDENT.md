# Which answers hold in the chapter 2 set on which fifty members lead each of the four segments, and why?

Answers: 1b 2d 3c 4a 5b

Chapter 2 built one list per segment, so that each segment's protect budget, a call from the member
team and a renewal offer for every member its list names, reaches that segment's own members. GROUP BY
segment returned four rows and could name no member, and a LIMIT of 50 over members returned chapter
1's whole-book list again, the book being every member and order across the four segments. Numbering
the whole book once and splitting it by segment gave Business 35, Retail-Core 4, Retail-Plus 11 and
Student 0, which the check of fifty or every buyer caught. `PARTITION BY segment` started the numbering
again in every segment: 155 members, Business 35, Retail-Core 50, Retail-Plus 50 and Student 20, and
four sorted queries glued with UNION ALL named the same members. Retail-Core's fifty carry Rs 2,78,740
of the segment's Rs 3,66,250, 76.1 percent. Three of the five items are design items: 1, 4 and 5.

**Who needs the answer.** You need it to check your five letters after the lab or tonight. The
marketing lead spends each segment's budget on the members its list names, so a list that is the right
length and holds the wrong members costs as much as a list of the wrong length.

**The questions on the way.**

- What does the per-segment set test about a list that restarts in every group?
- Why is each per-segment key right, and each other letter wrong?
- Why is item 3's count of fifty or every buyer worth arguing about?
- Where do real companies keep a ranked list inside every group?

## What does the per-segment set test about a list that restarts in every group?

"In each segment" is a partition, and a list per group comes from one window whose numbering restarts
in every group. The design items size that window against glued queries on a two-column cut, choose a
second route, a different way to the same list, that shares no window with the first, and name the
narrower ask that makes a single sorted query enough, with what that query returns. The other items
predict what a LIMIT does to a per-segment ask and catch a list that has the right length and names the
wrong members.

## Why is each per-segment key right, and each other letter wrong?

### Q1. Which build fits the city teams' ask, and what does it cost?

This is a design item: it asks for the best-fit build on a two-column cut, with a size you have to work
from the city table.

The key is b, "One window with PARTITION BY city and segment: 171 rows back from one pass over the
orders". Six cities and four segments make 24 groups, and twelve of them have fewer than ten buyers:
Business in Bengaluru, Hyderabad, Mumbai and Pune, Retail-Plus in Chennai and Hyderabad, and all six
Student groups. Each of those lists holds every buyer, so the cities' lists come to Bengaluru 27 rows
(4, 10, 10 and 3), Chennai 37, Delhi 32, Hyderabad 22, Mumbai 26 and Pune 27, which is 171, from one
pass over the 462 orders.

- Option a, "Twenty-four sorted queries glued with UNION ALL: 24 to keep, and 11,088 order rows read",
  returns the same 171 rows at 24 times the reading, the 462 orders read once per query, and leaves 24
  places to edit when a city or a segment is added.
- Option c, "One window with PARTITION BY city: 60 rows back, the ten biggest spenders in every city",
  mixes the segments inside each city, so Business buyers take 33 of the 60 places, which is chapter
  1's whole-book error at city size.
- Option d, "One window with PARTITION BY city and segment: 240 rows back, ten in each of the 24
  groups", has the right build and a count that assumes ten buyers in every group, where Hyderabad has
  one Student buyer and two Business buyers.

### Q2. What does a LIMIT of 200 return, counted by segment?

This item asks you to predict what a query returns.

The key is d, "Business 35, Retail-Core 83, Retail-Plus 73 and Student 9, by spend alone". LIMIT keeps
the first 200 rows of the whole sorted result and knows nothing of segments. Every Business buyer comes
first, 35 rows, and the other 165 places go to whichever retail members spent most. Retail-Core and
Retail-Plus run past fifty and Student gets 9 of its 20 buyers, so only the Business count is right.

- Option a, "Fifty from each segment, since four segments times fifty is two hundred", expects LIMIT to
  share its rows among the segments, which it cannot, and Business has only 35 buyers to give.
- Option b, "Business 35, Retail-Core 50, Retail-Plus 50 and Student 20, every list full", is the
  partitioned window's answer, 155 rows, where a LIMIT of 200 over 227 members returns 200.
- Option c, "Business 35, Retail-Plus 76 and Retail-Core 89, as a Student spends least", reads a
  segment's average as true of every member. Student's first member, C-0319, booked Rs 5,710, more than
  the fiftieth Retail-Core member's Rs 2,980, and C-0010 of Retail-Core outspent most of Retail-Plus.

### Q3. Which check catches a list whose window is ordered by customer id?

This item asks you to spot a list that looks right and name the check that catches it.

The key is c, "Set each list's first member's Q2 revenue beside the top Q2 revenue in that segment".
Ordered by customer id, the window numbers each segment's members by their id, so every list has the
right length and the wrong members. Retail-Core's list opens on C-0001, who booked Rs 1,200 in Q2, where
the segment's top member, C-0010, booked Rs 13,910; Retail-Plus's opens on C-0151 at Rs 10,910 against
C-0170's Rs 21,740, and Student's on C-0311 at Rs 2,560 against C-0319's Rs 5,710. Retail-Core's
id-ordered fifty carry Rs 2,36,540, 64.6 percent of the segment's Q2 revenue, against 76.1 percent for
the right fifty, and share only 34 members with it. A `GROUP BY segment` with `max(q2_revenue)` set
beside each list's first row exposes the fault in four rows.

- Option a, "Count each segment's list and set it beside the smaller of fifty and its buyers", reads
  35, 50, 50 and 20, every count right, because the partition and the cap are right; a count guards a
  list's length and cannot see who is on it.
- Option b, "Look across the four lists for any member who appears on more than one of the four",
  finds nobody on any per-segment list, right or wrong, since every member has one segment.
- Option d, "Add up the four lists' rows and set the total beside the 155 members they should hold",
  agrees at 155 for the same reason each count does.

### Q4. Which route confirms Retail-Core's fifty with no window, and what does it work through?

This is a design item: it asks for an independent second route and what it works through.

The key is a, "For each member, count the segment's members who booked more; keep those under fifty:
9,216 pairs". A member's place is one plus the members of the same segment who booked more, so a
member with fewer than fifty above them is on the list. Retail-Core's 96 buyers make 96 times 96,
9,216 pairs, with no window anywhere, and since nobody ties at the fiftieth place the route keeps the
same fifty members. It does about twenty times the window's work, so the team runs it as a check and
ships the window.

- Option b, "Rerun the list with `rank()` in place of `row_number()`: the same window, the 462 orders
  read once", shares the PARTITION BY and the ORDER BY, so a slip in either repeats in both lists.
- Option c, "Count the list's rows and set the count beside the smaller of 50 and 96: one row, which
  reads 50", passes item 3's wrong list too, since it checks the length alone.
- Option d, "Group Retail-Core's Q2 orders by segment: one row, with 96 members who bought and
  Rs 3,66,250", names no member, so it confirms nothing about who is on the list.

### Q5. Which fact would make one sorted query with a WHERE on the segment the better build, and what would it return?

This is a design item in two steps: it asks for the fact that would switch the build, and for what the
shorter query would then return.

The key is b, "Marketing wants Retail-Core's list alone this week, and the sorted query returns the
same fifty". With one segment asked for, a sorted query with the segment in WHERE,
`ORDER BY q2_revenue DESC, customer_id` and `LIMIT 50` is shorter than the window and returns the same
fifty Retail-Core members, all 50 of them shared. Nobody ties at Retail-Core's fiftieth place, so the
LIMIT cuts nobody who should stay; where two members tie at the line, the last place a list keeps,
chapter 3's question comes back.

- Option a, "A fifth segment arrives next quarter, and a fifth copy of the sorted query returns its own
  fifty", is a reason to keep the partition, which needs no change, where the sorted query needs a fifth
  copy to keep and edit.
- Option c, "Marketing wants Retail-Core's and Student's lists, and LIMIT 70 over both gives fifty and
  twenty", fails at the second step. LIMIT keeps the 70 biggest spenders of the two segments taken
  together, 65 Retail-Core members and 5 Student members, since only two Student members booked more
  than Retail-Core's fiftieth member's Rs 2,980; two lists still need a partition, or one query each.
- Option d, "The book grows to ten thousand orders, and a single pass over them all slows the window's
  sort", does not separate the builds, since both read the orders once and sort what they keep, and if
  Marketing still wants four lists, the sorted query needs four passes.

## Why is item 3's count of fifty or every buyer worth arguing about?

Item 3's option a, the count of fifty or every buyer, is the check chapter 2 taught, and a reviewer who
runs it and sees all four counts pass feels finished. It guards the length of each list, which is the
mistake chapter 2 staged, and it is silent on which members fill the list. A list can pass every check
of its shape and still send Marketing to the wrong people, so at least one check has to look at the
members themselves.

## Where do real companies keep a ranked list inside every group?

Amazon ranks every product it sells and says that the overall rank "doesn't always indicate how well an
item is selling in relation to similar items", so it keeps best-seller lists by category and
subcategory and shows an item's rank within its categories on the product page (Amazon's help page on
Best Sellers Rank, checked 1 October 2026). India's JEE Advanced keeps separate category rank lists
beside the common rank list, and in 2026 the OBC-NCL rank 1 stood third on the common list and the
GEN-EWS rank 1 sixth (the JEE Advanced 2026 results release of 1 June 2026, checked 1 October 2026).
Both keep a list for every group beside the overall one, which is the shape PARTITION BY gives a query.

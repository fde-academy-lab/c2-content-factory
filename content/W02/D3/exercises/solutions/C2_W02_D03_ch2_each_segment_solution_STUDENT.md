# Which answers hold in the chapter 2 set on which fifty members lead each of the four segments, and why?

Answers: 1b 2d 3c 4a 5b

Chapter 2 built one list per segment. GROUP BY segment returned four rows and could name no member, and
a LIMIT of 50 over members returned chapter 1's whole-book list again. Numbering the whole book once and
splitting it by segment gave Business 35, Retail-Core 4, Retail-Plus 11 and Student 0, which the check
of fifty or every buyer caught. `PARTITION BY segment` started the numbering again in every segment:
155 members, Business 35, Retail-Core 50, Retail-Plus 50 and Student 20, and four sorted queries glued
with UNION ALL named the same members. Retail-Core's fifty carry Rs 2,78,740 of the segment's
Rs 3,66,250, 76.1 percent. Three of the five items are design items: 1, 4 and 5.

**Who needs the answer.** You, checking your five letters after the lab or tonight. The marketing lead
spends each segment's budget on the members its list names, so a list that is the right length and
holds the wrong members costs as much as a list of the wrong length.

**The questions on the way.**

- Which idea does this set test?
- Why is each key right, item by item?
- Which wrong answer is worth arguing about?
- Where does this show up at work?

## Which idea does this set test?

"In each segment" is a partition, and a list per group comes from one window whose numbering restarts
in every group. The design items size that window against glued queries on a two-column cut, choose a
second route that shares no window, and name the narrower ask that makes a single sorted query enough.
The other items predict what a LIMIT does to a per-segment ask and catch a list that passes its count
and still names the wrong members.

## Why is each key right, item by item?

### Q1. Which build fits the city teams' ask, and how many rows does it return?

Kind: a design item, the best-fit build with its size, worked from the exhibit.

The key is b, "One window with PARTITION BY city and segment: the 462 orders read once, 171 rows back".
Six cities and four segments make 24 groups. Twelve of them have fewer than ten buyers, so each of
those lists holds every buyer: Bengaluru 27 rows (4, 10, 10 and 3), Chennai 37, Delhi 32, Hyderabad 22,
Mumbai 26 and Pune 27, which is 171.

- a, "Twenty-four sorted queries glued with UNION ALL: 171 rows back, the 462 orders read 24 times,
  11,088 rows": the right rows at 24 times the reading, and 24 places to edit when a city or a segment
  is added.
- c, "One window with PARTITION BY city: the 462 orders read once, 60 rows back, ten in each city":
  each city's ten mixes the segments, so the city's Business buyers take its first places, which is
  chapter 1's whole-book error at city size.
- d, "One window with PARTITION BY city and segment: the 462 orders read once, 240 rows back, ten in
  each group": the build is right and the count assumes ten buyers in every group, where Hyderabad has
  one Student buyer and two Business buyers.

### Q2. What does a LIMIT of 200 return, counted by segment?

Kind: predict the output.

The key is d, "Business 35, Retail-Core 83, Retail-Plus 73 and Student 9: 200 rows taken across the
whole book". LIMIT counts rows across the whole sorted result and knows nothing of segments. Every
Business buyer comes first, 35 rows, and the other 165 places go to whichever retail members spent
most. Retail-Core and Retail-Plus run past fifty and Student gets 9 of its 20 buyers, so only the
Business line is right.

- a, "Fifty from each segment, 200 rows, since four segments times fifty is two hundred": LIMIT cannot
  share its rows among segments, and Business has only 35 buyers to give.
- b, "Business 35, Retail-Core 50, Retail-Plus 50 and Student 20: 155 rows, every list full": that is
  PARTITION BY's answer; a LIMIT of 200 over 227 members returns 200 rows.
- c, "Business 35, Retail-Plus 76, Retail-Core 89 and no Student, since a Student member spends
  least": the segment averages say nothing about every member. Student's first member, C-0319, booked
  Rs 5,710, more than the fiftieth Retail-Core member's Rs 2,980, and C-0010 of Retail-Core outspent
  most of Retail-Plus.

### Q3. Which check catches a list whose window is ordered by customer id?

Kind: spot the plausible wrong output, and the check that catches it.

The key is c, "Set each list's first member beside its segment's top Q2 revenue: Retail-Core opens on
Rs 1,200, not Rs 13,910". Ordered by customer id, the window numbers each segment's members by their
id, so every list has the right length and the wrong members. Retail-Core's list opens on C-0001, who
booked Rs 1,200 in Q2, where the segment's top member, C-0010, booked Rs 13,910, and the fifty carry
Rs 2,36,540, 64.6 percent of the segment's Q2 revenue, against 76.1 percent for the right fifty. A
`GROUP BY segment` with `max(q2_revenue)` beside each list's first row exposes it in four rows.

- a, "Count each list beside the smaller of 50 and the segment's buyers: 35, 50, 50 and 20 all pass,
  so the list ships": the count guards the cap and cannot see who is on the list.
- b, "Check that no member sits on two lists: none does, since a member has one segment, so the list
  ships": it passes for any per-segment list, right or wrong.
- d, "Add the four lists' rows and set the sum beside chapter 2's 155: the two agree, so the list
  ships": the lengths match for the same reason the counts do.

### Q4. Which route confirms Retail-Core's fifty with no window, and what does it work through?

Kind: a design item, the independent second route with its size.

The key is a, "For each member, count the segment's members who booked more; keep those under fifty:
9,216 pairs". A member's place is one plus the members of the same segment who booked more, so
a member with fewer than fifty above him is on the list. Retail-Core's 96 buyers make 96 times 96,
9,216 pairs, with no window anywhere, and since nobody ties at the fiftieth place the route keeps the
same fifty members. It does about twenty times the window's work, which is why it is the check.

- b, "Rerun the list with `rank()` in place of `row_number()`: the same window, the 462 orders read
  once": the PARTITION BY and the ORDER BY are shared, so a slip in either repeats.
- c, "Count the list's rows and set them beside the smaller of 50 and 96: one row, which reads 50":
  item 3's wrong list passes this too.
- d, "Group Retail-Core's Q2 orders by segment: one row, with 96 members who bought and Rs 3,66,250": a
  GROUP BY on the segment names no member, so it confirms nothing about who is on the list.

### Q5. Which fact would make one sorted query with a WHERE on the segment the better build?

Kind: a design item, the fact that would switch the call.

The key is b, "Marketing wants Retail-Core's list alone this week". With one segment asked for and no
other, a sorted query with the segment in WHERE and `LIMIT 50` is shorter and returns the
same fifty Retail-Core members. Nobody ties at Retail-Core's fiftieth place, so the LIMIT cuts nobody it
should keep; where two members tie at the line, chapter 3's question comes back.

- a, "Student has only 20 buyers, fewer than the fifty Marketing asked for": the partitioned window
  already gives Student every buyer.
- c, "A fifth segment arrives next quarter and needs a list of its own": that argues for the
  partition, which needs no new query, against glued queries, which need a fifth.
- d, "The book grows to ten thousand orders, so one pass has to cover more rows": both builds read the
  orders once, so size does not separate them.

## Which wrong answer is worth arguing about?

Item 3, option a. The count of fifty or every buyer is the check chapter 2 taught, and a reviewer who
runs it and sees four lines pass feels finished. It guards the length of each list, which is the
mistake chapter 2 staged, and it is silent on which members fill the list. A list can pass every check
of its shape and still send Marketing to the wrong people, so at least one check has to look at the
members themselves.

## Where does this show up at work?

Amazon ranks every product it sells and says that the overall rank "doesn't always indicate how well an
item is selling in relation to similar items", so it keeps best-seller lists by category and
subcategory and shows an item's rank within its categories on the product page (Amazon's help page on
Best Sellers Rank, checked 1 October 2026). India's JEE Advanced keeps separate category rank lists
beside the common rank list, and in 2026 the OBC-NCL rank 1 stood third on the common list and the
GEN-EWS rank 1 sixth (the JEE Advanced 2026 results release of 1 June 2026, checked 1 October 2026).
Each is a PARTITION BY in public.

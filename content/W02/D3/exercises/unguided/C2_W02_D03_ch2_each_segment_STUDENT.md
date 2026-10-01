# Which fifty members lead each of the four segments?

Chapter 2's set holds five items. Items 1 and 2 run live in chapter 2's last minutes if the chapter ran to
time; items 3 to 5 are the practice lab's stretch or tonight's work.

> "Give us the top fifty customers by Q2 revenue in each segment."
>
> The marketing lead, Kalpa Retail

Kalpa Retail sells to four segments: Business, its corporate buyers, whose orders run to lakhs;
Retail-Core, its everyday shoppers; Retail-Plus, its paid membership tier; and Student. Taken
together, every member and every order across the four segments are the book. The marketing lead
spends a protect budget on each segment: a call from the member team and a renewal offer for every
member that segment's list names. The segment lives on the customers table, and each order finds it
with `JOIN customers c USING (customer_id)`. Q2 is July to September 2026, and a member's Q2 revenue is
the booked amount of every Q2 order the member placed, whatever its status: 462 orders and
Rs 9,84,00,000 in all, from 227 members who bought. Chapter 1 ranked the whole book in one list, and its
fifty were 35 Business, 11 Retail-Plus and 4 Retail-Core members and no Student, because every Business
buyer outspends every retail member. `PARTITION BY segment` inside a window's brackets starts the
numbering again at 1 in each segment. `row_number()` breaks a tie by whatever else its ORDER BY names,
here the customer id, or arbitrarily if nothing does, and numbered that way the four lists hold 155
members: Business 35 and Student 20, every buyer in both, and Retail-Core 50 and Retail-Plus 50. UNION
ALL stacks the results of several queries into one. The warehouse is Kalpa's Postgres database.

| Segment | Members who bought in Q2 | First three places by Q2 revenue |
|---|---|---|
| Business | 35 | |
| Retail-Core | 96 | C-0010 Rs 13,910, C-0040 Rs 13,550, C-0041 Rs 12,460 |
| Retail-Plus | 76 | C-0170 Rs 21,740, C-0167 Rs 14,600, C-0160 Rs 13,700 |
| Student | 20 | C-0319 Rs 5,710, C-0314 Rs 3,380, C-0320 Rs 2,630 |

Members who bought in Q2, by city and segment:

| City | Business | Retail-Core | Retail-Plus | Student |
|---|---|---|---|---|
| Bengaluru | 4 | 16 | 13 | 3 |
| Chennai | 10 | 15 | 9 | 8 |
| Delhi | 12 | 17 | 19 | 2 |
| Hyderabad | 2 | 17 | 9 | 1 |
| Mumbai | 3 | 13 | 16 | 3 |
| Pune | 4 | 18 | 10 | 3 |

**Who needs the answer.** The marketing lead needs it to spend each segment's protect budget on that
segment's own members, and the head of Retail-Plus needs it so the tier's best members are called
before they drift. A list that gives Retail-Plus a few places and Student none leaves the tier
Marketing worries about mostly unprotected.

**The questions on the way.**

- Which build fits the city teams' ask, and what does it cost?
- What does a LIMIT of 200 return, counted by segment?
- Which check catches a list whose window is ordered by customer id?
- Which route confirms Retail-Core's fifty with no window, and what does it work through?
- Which fact would make one sorted query with a WHERE on the segment the better build, and what would it return?

**What you post.** Five letters in item order, with no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

## How should one query build a list in every group?

This comes up at work whenever a stakeholder asks for the top members of every group at once, cut by one
column or by two.

### Q1. Which build fits the city teams' ask, and what does it cost?

Marketing's city teams ask for the ten members who spent most in Q2 in each segment of each city, from
the buyers in the second table above. Which build fits, and what does it cost?

a) Twenty-four sorted queries glued with UNION ALL: 24 to keep, and 11,088 order rows read

b) One window with PARTITION BY city and segment: 171 rows back from one pass over the orders

c) One window with PARTITION BY city: 60 rows back, the ten biggest spenders in every city

d) One window with PARTITION BY city and segment: 240 rows back, ten in each of the 24 groups

### Q2. What does a LIMIT of 200 return, counted by segment?

An analyst asked for fifty in each segment groups the Q2 orders by member, sorts the members by Q2
revenue and writes `LIMIT 200`, reasoning that four segments times fifty is two hundred. Counted by
segment, what comes back?

a) Fifty from each segment, since four segments times fifty is two hundred

b) Business 35, Retail-Core 50, Retail-Plus 50 and Student 20, every list full

c) Business 35, Retail-Plus 76 and Retail-Core 89, as a Student spends least

d) Business 35, Retail-Core 83, Retail-Plus 73 and Student 9, by spend alone

## How do you know each segment's list holds the right members?

This comes up at work whenever a finished list is checked before a stakeholder acts on it.

### Q3. Which check catches a list whose window is ordered by customer id?

An analyst's per-segment list partitions the window by segment and orders it by customer id. Before
the list goes to Marketing, which check catches what is wrong with it?

a) Count each segment's list and set it beside the smaller of fifty and its buyers

b) Look across the four lists for any member who appears on more than one of the four

c) Set each list's first member's Q2 revenue beside the top Q2 revenue in that segment

d) Add up the four lists' rows and set the total beside the 155 members they should hold

### Q4. Which route confirms Retail-Core's fifty with no window, and what does it work through?

Kavya Nair, the senior analyst who checks every number before it leaves the team, wants Retail-Core's
fifty confirmed by a second route: a different way to the same list that shares no window with the
first. Nobody ties at Retail-Core's fiftieth place. Which route does that, and what does it work
through?

a) For each member, count the segment's members who booked more; keep those under fifty: 9,216 pairs

b) Rerun the list with `rank()` in place of `row_number()`: the same window, the 462 orders read once

c) Count the list's rows and set the count beside the smaller of 50 and 96: one row, which reads 50

d) Group Retail-Core's Q2 orders by segment: one row, with 96 members who bought and Rs 3,66,250

## When is a simpler build enough?

This comes up at work whenever a shorter query is offered in place of a general one and someone has to
say when it is safe.

### Q5. Which fact would make one sorted query with a WHERE on the segment the better build, and what would it return?

`PARTITION BY segment` builds all four lists in one query. Which fact, if it held, would make one
sorted query with the segment in `WHERE` and a `LIMIT` the better build, and what would that query
return?

a) A fifth segment arrives next quarter, and a fifth copy of the sorted query returns its own fifty

b) Marketing wants Retail-Core's list alone this week, and the sorted query returns the same fifty

c) Marketing wants Retail-Core's and Student's lists, and LIMIT 70 over both gives fifty and twenty

d) The book grows to ten thousand orders, and a single pass over them all slows the window's sort

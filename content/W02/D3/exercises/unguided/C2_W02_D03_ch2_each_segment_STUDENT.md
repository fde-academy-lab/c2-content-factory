# Which fifty members lead each of the four segments?

Chapter 2 set, five items. Items 1 and 2 run live in chapter 2's last minutes if the chapter ran to
time; items 3 to 5 are the practice lab's stretch or tonight's work.

> "Give us the top fifty customers by Q2 revenue in each segment."
>
> The marketing lead, Kalpa Retail

Kalpa Retail sells to four segments: Business, its corporate buyers, whose orders run to lakhs;
Retail-Core, its everyday shoppers; Retail-Plus, its paid membership tier; and Student. The segment
lives on the customers table, and each order finds it with `JOIN customers c USING (customer_id)`. Q2
is July to September 2026, and a member's Q2 revenue is the booked amount of every Q2 order the member
placed, whatever its status: 462 orders and Rs 9,84,00,000 in all. Chapter 1 ranked the whole book
once, and its fifty were 35 Business, 11 Retail-Plus and 4 Retail-Core members and no Student, because
every Business buyer outspends every retail member. `PARTITION BY segment` inside a window's brackets
starts the numbering again at 1 in each segment, and with `row_number()` and the customer id deciding
any two members who booked the same, the four lists hold 155 members: Business 35, Retail-Core 50,
Retail-Plus 50 and Student 20. Fifty is a cap, so each list holds fifty or every buyer, whichever is
fewer. LIMIT counts rows across a whole result, whatever groups sit in it, and UNION ALL stacks the
results of several queries into one. The book is Kalpa's Postgres warehouse.

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

**Who needs the answer.** The marketing lead, who spends each segment's protect budget on that
segment's own members, and the head of Retail-Plus, who wants his best members called before they
drift. A list that gives Retail-Plus a few places and Student none leaves the tier Marketing worries
about mostly unprotected.

**The questions on the way.**

- Which build fits the city teams' ask, and how many rows does it return?
- What does a LIMIT of 200 return, counted by segment?
- Which check catches a list whose window is ordered by customer id?
- Which route confirms Retail-Core's fifty with no window, and what does it work through?
- Which fact would make one sorted query with a WHERE on the segment the better build?

**What you post.** One line of five letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

## How should one query build a list in every group?

Used at work whenever a stakeholder asks for the top members of every group at once, cut by one
column or by two.

### Q1. Which build fits the city teams' ask, and how many rows does it return?

Marketing's city teams ask for the ten members who spent most in Q2 in each segment of each city, from
the buyers in the second table above. Which build fits, and how many rows does it return?

a) Twenty-four sorted queries glued with UNION ALL: 171 rows back, the 462 orders read 24 times, 11,088 rows

b) One window with PARTITION BY city and segment: the 462 orders read once, 171 rows back

c) One window with PARTITION BY city: the 462 orders read once, 60 rows back, ten in each city

d) One window with PARTITION BY city and segment: the 462 orders read once, 240 rows back, ten in each group

### Q2. What does a LIMIT of 200 return, counted by segment?

An analyst asked for fifty in each segment groups the Q2 orders by member, sorts the members by Q2
revenue and writes `LIMIT 200`, reasoning that four segments times fifty is two hundred. Counted by
segment, what comes back?

a) Fifty from each segment, 200 rows, since four segments times fifty is two hundred

b) Business 35, Retail-Core 50, Retail-Plus 50 and Student 20: 155 rows, every list full

c) Business 35, Retail-Plus 76, Retail-Core 89 and no Student, since a Student member spends least

d) Business 35, Retail-Core 83, Retail-Plus 73 and Student 9: 200 rows taken across the whole book

## How do you know each segment's list holds the right members?

Used at work whenever a list passes its count and still has to be shown to name the right people.

### Q3. Which check catches a list whose window is ordered by customer id?

An analyst's per-segment list partitions by segment and orders the window by customer id. Its four
lists hold 35, 50, 50 and 20 members, which is fifty or every buyer in each segment. Which check
catches what is wrong with it?

a) Count each list beside the smaller of 50 and the segment's buyers: 35, 50, 50 and 20 all pass, so the list ships

b) Check that no member sits on two lists: none does, since a member has one segment, so the list ships

c) Set each list's first member beside its segment's top Q2 revenue: Rs 1,200 against Rs 13,910 in Retail-Core

d) Add the four lists' rows and set the sum beside chapter 2's 155: the two agree, so the list ships

### Q4. Which route confirms Retail-Core's fifty with no window, and what does it work through?

Kavya Nair, the senior analyst who checks every number before it leaves the team, wants Retail-Core's
fifty confirmed by a route that shares no window with the list. Nobody ties at Retail-Core's fiftieth
place. Which route does that, and what does it work through?

a) For each member, count the segment's members who booked more; keep those under fifty: 9,216 pairs

b) Rerun the list with `rank()` in place of `row_number()`: the same window, the 462 orders read once

c) Count the list's rows and set them beside the smaller of 50 and 96: one row, which reads 50

d) Group Retail-Core's Q2 orders by segment: one row, with 96 members who bought and Rs 3,66,250

## When is a simpler build enough?

Used at work whenever the general build is right and a narrower ask makes a shorter one honest.

### Q5. Which fact would make one sorted query with a WHERE on the segment the better build?

`PARTITION BY segment` builds all four lists in one query. Which fact, if it held, would make one
sorted query with `WHERE c.segment = ...` and `LIMIT 50` the better build?

a) Student has only 20 buyers, fewer than the fifty Marketing asked for

b) Marketing wants Retail-Core's list alone this week

c) A fifth segment arrives next quarter and needs a list of its own

d) The book grows to ten thousand orders, so one pass has to cover more rows

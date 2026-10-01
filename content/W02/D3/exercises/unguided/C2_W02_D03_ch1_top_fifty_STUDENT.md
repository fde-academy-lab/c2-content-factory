# Which fifty members spent the most in Q2?

Chapter 1's set holds five items. Items 2 and 3 run live in chapter 1's last minutes if the chapter ran to
time; items 1, 4 and 5 are the practice lab's stretch or tonight's work.

> "Retail-Plus frequency is the problem, so we want to protect our best members before they drift.
> Give us the top fifty customers by Q2 revenue in each segment, and flag anyone whose monthly spend
> has fallen for two months running."
>
> The marketing lead, Kalpa Retail

The marketing lead owns acquisition and campaigns at Kalpa Retail, and this quarter's protect budget,
a call from the member team and a renewal offer, goes to the members a ranked list names. Kalpa sells
to four segments: Business, its corporate buyers, whose orders run to lakhs; Retail-Core, its everyday
shoppers; Retail-Plus, its paid membership tier; and Student. Taken together, the four segments are
the book. A member is one customer on the customers table, and the segment lives on the customer, so
each order finds it with one join, `JOIN customers c USING (customer_id)`. Q2 is July to September
2026. A member's Q2 revenue is the booked amount of every Q2 order the member placed, whatever its
status, which is how Monday's suite counted Rs 9,84,00,000 on 462 orders from 227 members who bought.
GROUP BY collapses each group to one row. A window function such as
`row_number() OVER (ORDER BY q2_revenue DESC, customer_id)` computes a value for every row from the
rows around it and keeps every row, here each member's place; `row_number()` breaks a tie by whatever
else its ORDER BY names, here the customer id, or arbitrarily if nothing does. The warehouse is Kalpa's
Postgres database, and the data platform lead's rule for it is "query it, do not export it". A second
route is a different way of reaching the same answer, used to check the first.

| Segment | Members who bought in Q2 | Q2 orders | Q2 revenue | Per member who bought |
|---|---|---|---|---|
| Business | 35 | 91 | Rs 9,75,84,600 | about Rs 27.9 lakh |
| Retail-Plus | 76 | 140 | Rs 4,13,380 | about Rs 5,400 |
| Retail-Core | 96 | 193 | Rs 3,66,250 | about Rs 3,800 |
| Student | 20 | 38 | Rs 35,770 | about Rs 1,800 |
| The book | 227 | 462 | Rs 9,84,00,000 | |

The whole book ranked by Q2 revenue with `row_number()`, places 33 to 40:

| Place | Member | Segment | Q2 revenue |
|---|---|---|---|
| 33 | C-0303 | Business | Rs 5,73,000 |
| 34 | C-0292 | Business | Rs 3,52,000 |
| 35 | C-0302 | Business | Rs 2,25,000 |
| 36 | C-0170 | Retail-Plus | Rs 21,740 |
| 37 | C-0167 | Retail-Plus | Rs 14,600 |
| 38 | C-0010 | Retail-Core | Rs 13,910 |
| 39 | C-0160 | Retail-Plus | Rs 13,700 |
| 40 | C-0040 | Retail-Core | Rs 13,550 |

**Who needs the answer.** The marketing lead needs it, because the member team will ring every name on
the list. A list built on the wrong unit sends the offer to the wrong people: every best member it misses is one
nobody rang, and every member it repeats is a call made twice.

**The questions on the way.**

- Which build fits Marketing's per-segment ask, and what does it cost on Q2's data?
- What is wrong with the colleague's top ten, and which check catches it?
- If Marketing trimmed the whole-book list to forty, which segments would it reach?
- Which second route could catch a member wrongly left off the fifty, and how many rows does it move?
- Which fact would make the fifty biggest Q2 orders the right list to hand over?

**What you post.** Five letters in item order, with no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

## How should the team build a ranked list, and check it before anyone is rung?

This comes up at work whenever a stakeholder asks for a ranked list and a team will act on everything it
holds.

### Q1. Which build fits Marketing's per-segment ask, and what does it cost on Q2's data?

Marketing asked for a list in each of the four segments. Each build below carries its cost for all
four lists, worked from the segment table above. Which build fits the ask, judged on those costs?

a) Sort each segment's Q2 orders by amount and keep the top fifty: 188 rows leave the warehouse

b) Rank members in four LIMIT 50 queries glued with UNION ALL, each reading all 462 Q2 orders

c) Number the members in a window that restarts in each segment: one query, and 155 rows leave

d) Export the 462 Q2 orders and sort each segment by hand: four sorts, and every row leaves

### Q2. What is wrong with the colleague's top ten, and which check catches it?

Every number in this item is invented. A colleague sends Marketing "the top ten members" as the ten
rows below.

| Row | Member | Amount |
|---|---|---|
| 1 | P | Rs 9,40,000 |
| 2 | Q | Rs 8,75,000 |
| 3 | P | Rs 8,10,000 |
| 4 | R | Rs 7,60,000 |
| 5 | P | Rs 7,25,000 |
| 6 | S | Rs 6,90,000 |
| 7 | Q | Rs 6,40,000 |
| 8 | T | Rs 6,05,000 |
| 9 | R | Rs 5,80,000 |
| 10 | U | Rs 5,55,000 |

What is wrong with the list, and which check catches it before anyone is rung?

a) Each row is an order, so six members fill ten places; grouping the list by member shows P three times

b) Each row is a member, and P's row was loaded three times over; a check for duplicate rows catches it

c) Each row is an order, so P's three orders inflate the list's total; its sum beside Q2's total shows it

d) Each row is a member, and P shows three times because of a tie; a tiebreaker in the ORDER BY clears it

## Which segments does one list across the whole book reach?

This comes up at work whenever one list is cut across groups whose members' spend differs by a hundred
times.

### Q3. If Marketing trimmed the whole-book list to forty, which segments would it reach?

The table of places 33 to 40 at the top of this set comes from one ranking of all 227 members. If
Marketing trimmed that one list to forty members, how many would come from each segment?

a) 28 Business, 9 Retail-Plus and 3 Retail-Core, and no Student

b) 35 Business and 5 Retail-Plus, and no Retail-Core or Student

c) 35 Business, 2 Retail-Plus and 3 Retail-Core, and no Student

d) 35 Business, 3 Retail-Plus and 2 Retail-Core, and no Student

## How do you prove a list without trusting the query that made it?

This comes up at work whenever a ranked list goes to a stakeholder who will act on every name in it.

### Q4. Which second route could catch a member wrongly left off the fifty, and how many rows does it move?

Kavya Nair, the senior analyst on Kalpa Retail's data team, checks every number before it leaves the
team, and wants the fifty confirmed by a route that would notice a member who belongs on the list and
is missing from it. Which route does that, and how many rows does it move?

a) Pull the query's fifty rows into a spreadsheet and sort them again by revenue: 50 rows

b) Pull all 462 Q2 order rows into Python, total each member and sort the totals: 462 rows

c) Run the same window query again tomorrow and set the two lists side by side: 50 rows each

d) Add up the fifty members' Q2 revenue and set it beside Q2's Rs 9,84,00,000: one row

## When is the quickest list the right list?

This comes up at work whenever a quick build fails one ask and someone asks which ask it would suit.

### Q5. Which fact would make the fifty biggest Q2 orders the right list to hand over?

Sorting the Q2 orders by amount and keeping the first fifty is the quickest list a team could build.
Which fact, if it held, would make those fifty orders the right list to hand over?

a) The fifty biggest orders all come from different members, so no member's name repeats

b) Business orders run to lakhs, so the largest orders come from the members who spent most

c) Marketing wants a thank-you note for each of the fifty largest Q2 orders, one per order

d) The fifty biggest orders carry most of Q2's revenue, so the list covers most of the money

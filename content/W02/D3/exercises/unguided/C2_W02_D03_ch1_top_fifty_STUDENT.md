# Which fifty members spent the most in Q2?

Chapter 1 set, five items. Items 1 and 2 run live in chapter 1's last minutes if the chapter ran to
time; items 3 to 5 are the practice lab's stretch or tonight's work.

> "Retail-Plus frequency is the problem, so we want to protect our best members before they drift.
> Give us the top fifty customers by Q2 revenue in each segment, and flag anyone whose monthly spend
> has fallen for two months running."
>
> The marketing lead, Kalpa Retail

The marketing lead owns acquisition and campaigns at Kalpa Retail, and this quarter's protect budget,
a call from the member team and a renewal offer, goes to the members a ranked list names. Kalpa sells
to four segments: Business, its corporate buyers, whose orders run to lakhs; Retail-Core, its everyday
shoppers; Retail-Plus, its paid membership tier; and Student. A member is one customer on the
customers table, and the segment lives on the customer, so each order finds it with one line,
`JOIN customers c USING (customer_id)`. Q2 is July to September 2026. A member's Q2 revenue is the
booked amount of every Q2 order the member placed, whatever its status, which is how Monday's suite
counted Rs 9,84,00,000 on 462 orders from 227 members who bought. GROUP BY collapses each group to one
row. A window function such as `row_number() OVER (ORDER BY q2_revenue DESC, customer_id)` computes a
value for every row from the rows around it and keeps every row, here each member's place, with the
customer id deciding between two members who booked the same. The book is Kalpa's Postgres warehouse,
and the data platform lead's rule is "query it, do not export it".

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

**Who needs the answer.** The marketing lead, whose member team will ring every name on the list. A
list built on the wrong unit sends the offer to the wrong people: every best member it misses is one
nobody rang, and every member it repeats is a call made twice.

**The questions on the way.**

- Which build fits Marketing's per-segment ask, and what does each build cost?
- What is wrong with the colleague's top ten, and which check catches it?
- If Marketing trimmed the whole-book list to forty, which segments would it reach?
- Which second route could catch a member wrongly left off the fifty, and how many rows does it move?
- Which fact would make the shorter build, GROUP BY with LIMIT 50, the better call?

**What you post.** One line of five letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

## How should the team build a ranked list of members?

Used at work whenever a stakeholder asks for a ranked list and the team has to decide what one row of
the answer is and where the work runs.

### Q1. Which build fits Marketing's per-segment ask, and what does each build cost?

Marketing's real ask is a list in each of the four segments, and four builds could hand it a ranked
list. Which build fits, sized in the rows that leave the warehouse and the work the per-segment list
adds?

a) Sort the Q2 order rows by amount and keep fifty: 50 rows leave, and each segment's list is one more filter

b) Group by member, sort and keep fifty with LIMIT: 50 rows leave, and each segment's list is one more phrase

c) Group by member and number the members in a window: 50 rows leave, and each segment's list is one more phrase

d) Export the Q2 orders and sort them by hand in a spreadsheet: 462 rows leave, and each segment's list is four sorts

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

a) Each row is an order, so six members fill ten places; a count of distinct members beside the rows reads 6 for 10

b) Each row is a member, so the list is right; a count of its rows beside Marketing's ask reads 10 for 10

c) Each row is an order, so P's three orders inflate the list's total; its sum beside Q2's total catches it

d) Each row is a member, and P shows three times because of a tie; a tiebreaker in the ORDER BY removes the repeats

## Which segments does one list across the whole book reach?

Used at work whenever one list is cut across groups whose members differ in size by a hundred times.

### Q3. If Marketing trimmed the whole-book list to forty, which segments would it reach?

The table of places 33 to 40 at the top of this set comes from one ranking of all 227 members. If
Marketing trimmed that one list to forty members, how many would come from each segment?

a) 6 Business, 17 Retail-Core, 13 Retail-Plus and 4 Student, in proportion to the members who bought

b) 35 Business and 5 Retail-Plus, since a Retail-Plus member outspends a Retail-Core one on average

c) 35 Business, 2 Retail-Plus and 3 Retail-Core, and no Student

d) 35 Business, 3 Retail-Plus and 2 Retail-Core, and no Student

## How do you prove a list without trusting the query that made it?

Used at work whenever a ranked list goes to a stakeholder who will act on every name in it.

### Q4. Which second route could catch a member wrongly left off the fifty, and how many rows does it move?

Kavya Nair, the senior analyst on Kalpa Retail's data team, checks every number before it leaves the
team. She wants the fifty confirmed by a route that would notice a member who belongs on the list and
is missing from it. Which route does that, and how many rows does it move?

a) Pull the fifty rows the query returned into a spreadsheet and sort them again by revenue: 50 rows

b) Pull the 462 Q2 order rows into Python, total each member in a dictionary and sort: 462 rows

c) Run the same window query again tomorrow and set the two lists side by side: 50 rows each

d) Add up the fifty members' Q2 revenue and set it beside the quarter's Rs 9,84,00,000: one row

### Q5. Which fact would make the shorter build, GROUP BY with LIMIT 50, the better call?

GROUP BY member, ORDER BY revenue and LIMIT 50 returns the same fifty members as the window today, in
a shorter query. Which fact, if it held, would make it the better build?

a) The book grows past 10,000 orders next year, and a window over that many rows runs too slowly

b) Marketing wants a list in each segment, and LIMIT 50 can be written once for each of the four

c) Marketing wants one overall list to read by eye, and no later step uses the place

d) Two members tie at fiftieth place, and LIMIT 50 keeps exactly fifty rows whatever the tie

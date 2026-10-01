# Which listed members does Marketing call first, and does each flag hold up when a member says they were on holiday?

Chapter 6's set holds five items. Items 1 and 2 run live in chapter 6's last minutes if the chapter ran to
time; items 3 to 5 are the practice lab's stretch or tonight's work.

> "Before we ring anyone: one of your flagged members, C-0216, rang our help line to say they were
> travelling in August and have not stopped buying. Is your flag wrong about them, and how many others?"
>
> The head of Retail-Plus, Kalpa Retail

A member's monthly spend is the booked revenue of their orders in one calendar month, and the monthly
table holds a row only for a month with an order: 752 member-months for the 301 members who bought
between April and September 2026, so a member orders in about 2.5 of the six months. `lag(spend, 1)`
reads the spend on the row before, in the window's order, and `lag(spend, 2)` the row before that.
Chapter 4's flag, LAG over each member's own months with `PARTITION BY customer_id ORDER BY month`,
found 16 members whose September was below their month before and that month below the one before it,
and all 16 are on a protect list, each segment's top fifty by Q2 revenue under the head of Retail-Plus's
rule, where members who spent the same share a place. Marketing's words, "fallen for two months
running", read as calendar months: September below August, and August below July. A calendar is a table
with a row for every member in every month, either left empty where there was no order or filled with
zero.

| C-0216, Retail-Plus, place 23 on the list | April | May | June | July | August | September |
|---|---|---|---|---|---|---|
| Monthly spend | no order | Rs 6,440 | no order | Rs 4,300 | no order | Rs 2,540 |

**Who needs the answer.** The marketing lead's member team needs it, since it rings the flagged
members on the protect list this week, and so does the head of Retail-Plus, who answers to the tier's
members for every call. A call that tells a loyal member their spend is falling when they were away
costs their goodwill and perhaps their renewal.

**The questions on the way.**

- Which reading of "last month" fits the flag, sized in the rows it reads?
- Which months does chapter 4's flag compare for an invented member with gaps, and does a flag that reads calendar months keep them?
- In what order should the team build Monday's call list from the warehouse?
- Which route confirms the nine calendar-month flags with no window, and what does it read?
- Which fact would make filling an empty month with zero the honest reading?

**What you post.** Your five letters in item order, with no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

## Which reading of "last month" should the flag use?

This comes up at work whenever a definition written in a stakeholder's words meets data in which most months
are empty.

### Q1. Which reading of "last month" fits the flag, sized in the rows it reads?

Four ways could read "last month" for a member's September. Which fits Marketing's words, sized in the
rows it reads?

a) A calendar of every member and month, zero-filled: 1,806 rows, with an empty month read as zero

b) A calendar of every member and month, left empty: 752 rows, since empty months add no rows

c) LAG over each member's own months, as chapter 4 built it: 752 rows, each beside the month before

d) LAG on the 752 rows, with a flag kept only if `lag(month, 1)` is August and `lag(month, 2)` July

## What does the flag compare for a member with empty months?

This comes up at work whenever a customer pushes back on a flag and the rows behind it have to be read before
anyone replies.

### Q2. Which months does chapter 4's flag compare for an invented member with gaps, and does a flag that reads calendar months keep them?

Every number in this item is invented. Y-01 bought in April (Rs 3,600), June (Rs 2,700) and September
(Rs 1,300), and in no other month. Which months does chapter 4's flag compare for their September, and
does a flag that reads Marketing's calendar months keep them?

a) September against June and April, so chapter 4's flag fires and the calendar flag drops them

b) September against August and July, read as zero, so chapter 4's flag cannot fire on a rise

c) September against nothing, since LAG returns NULL across empty months, so neither flag fires

d) September against June and April, so both flags keep them, since each month they ordered fell

## In what order is Monday's call list built?

This comes up at work whenever a query is written as named steps and each step needs what an earlier
one made.

### Q3. In what order should the team build Monday's call list from the warehouse?

The four steps below are lettered P to S and listed out of order.

| Step | What it does |
|---|---|
| P | Join the members the flag keeps to each segment's protect list under RANK, and sort them by place |
| Q | Add up each member's spend in each calendar month, one row per member and month |
| R | Keep the September rows that fell twice and whose two rows before are August and July |
| S | Set the spend and the month one and two rows back beside every row, partitioned by member and ordered by month |

Which order of the four steps builds the list?

a) S, Q, R, P

b) Q, R, S, P

c) Q, S, R, P

d) S, R, Q, P

## How do you prove the call list without the window?

This comes up at work whenever a call list is about to go out and the definition behind it has to be confirmed
by a route that could disagree.

### Q4. Which route confirms the nine calendar-month flags with no window, and what does it read?

The flag that reads calendar months names nine members. Kavya Nair, the senior analyst who checks every
number before it leaves the team, wants the nine confirmed by a route that shares no window with that
flag and would disagree with it if it misread an empty month. Which route does that, and what does it
read?

a) A walk in Python that sorts each member's months and sets each beside the one before: 752 rows

b) A self-join of each member's September row to their own August and July rows: 359 rows read

c) The calendar zero-filled and read with LAG over each member's six months: 1,806 rows

d) The flag's own LAG query rerun after the overnight reload, set beside the first run: 752 rows

## When is zero the right reading of an empty month?

This comes up at work whenever a missing value tempts someone to write in a default and the business has to
say what the gap means.

### Q5. Which fact would make filling an empty month with zero the honest reading?

Kalpa's monthly table holds no row for a month in which a member placed no order. Which fact, if it
held, would make zero the honest reading of such an empty month?

a) Members buy in about 2.5 of the six months, so most of a member's months are empty anyway

b) The calendar holds 1,806 rows, so each member already has a row to fill for each of six months

c) A lost member costs Kalpa more than a wasted call, so reading a quiet month as a fall is safer

d) Every member is billed every month by default, so a month with no charge means they cancelled

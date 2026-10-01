# Which listed members does Marketing call first, and does each flag hold up when a member says he was on holiday?

Chapter 6 set, five items. Items 1 and 2 run live in chapter 6's last minutes if the chapter ran to
time; items 3 to 5 are the practice lab's stretch or tonight's work.

> "Before we ring anyone: one of your flagged members, C-0216, rang our help line to say he was
> travelling in August and has not stopped buying. Is your flag wrong about him, and how many others?"
>
> The head of Retail-Plus, Kalpa Retail

A member's monthly spend is the booked revenue of his orders in one calendar month, and the monthly
table holds a row only for a month with an order: 752 member-months for the 301 members who bought
between April and September 2026, so a member orders in about 2.5 of the six months. Chapter 4's flag,
LAG over each member's own months with `PARTITION BY customer_id`, found 16 members whose September was
below their month before and that month below the one before it, and all 16 are on a protect list,
each segment's top fifty by Q2 revenue under the head of Retail-Plus's rule. Marketing's words, "fallen
for two months running", read as calendar months: September below August, and August below July. LAG
reads the previous row, so where a member skipped a month it reads the last month he did buy in. The
calendar check keeps a flag only when `lag(month, 1)` is August and `lag(month, 2)` is July. A calendar
is a table with a row for every member in every month, 301 times 6, 1,806 rows, either left empty where
there was no order or filled with zero.

| C-0216, Retail-Plus, place 23 on his list | May | July | September |
|---|---|---|---|
| Monthly spend | Rs 6,440 | Rs 4,300 | Rs 2,540 |
| The month `lag(month, 1)` read | none | May | July |

**Who needs the answer.** The marketing lead's member team, which rings the flagged members on the
protect list this week, and the head of Retail-Plus, who answers to his members for every call. A
call that tells a loyal member his spend is falling when he was away costs his goodwill and perhaps his
renewal.

**The questions on the way.**

- Which reading of "last month" fits the flag, sized in the rows it reads?
- Which months does chapter 4's flag compare for an invented member with gaps, and does the checked flag keep him?
- What does the book say about an invented member with no September order, and which flag should name him?
- Which route confirms the checked flags with no window, and what does it read?
- Which fact would make filling an empty month with zero the honest reading?

**What you post.** One line of five letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

## Which reading of "last month" should the flag use?

Used at work whenever a definition written in a stakeholder's words meets data in which most months
are empty.

### Q1. Which reading of "last month" fits the flag, sized in the rows it reads?

Four ways could read "last month" for a member's September. Which fits Marketing's words, sized in the
rows it reads?

a) A calendar of every member and month, zero-filled: 1,806 rows, a month with no order reading as zero

b) A calendar of every member and month, left empty: 752 rows, since empty months add no rows

c) LAG over each member's own months, as chapter 4 built it: 752 rows, with no check needed

d) LAG with a check that the two rows before September are August and July: 752 rows

## What does the flag compare for a member with empty months?

Used at work whenever a customer pushes back on a flag and the rows behind it have to be read before
anyone replies.

### Q2. Which months does chapter 4's flag compare for an invented member with gaps, and does the checked flag keep him?

Every number in this item is invented. Y-01 bought in April (Rs 3,600), June (Rs 2,700) and September
(Rs 1,300), and in no other month. Which months does chapter 4's flag compare for his September, and
does the checked flag keep him?

a) September against June and April, so chapter 4's flag fires and the checked flag drops him

b) September against August and July, each read as zero, so both flags keep him

c) September against nothing, since LAG returns NULL across empty months, so neither flag fires

d) September against June and April, so both flags keep him, since each month he ordered fell

### Q3. What does the book say about an invented member with no September order, and which flag should name him?

Every number in this item is invented. Y-02 bought in July (Rs 2,300) and August (Rs 1,800) and placed
no order in September. An analyst fills every empty month with zero and reports Y-02 among the members
whose spend fell two months running. What does the book say about Y-02's September, and which flag
should name him?

a) A fall to zero, so the falling-spend flag names him and Marketing rings him about a falling spend

b) A fall to zero once his August is checked against July, so the flag names him with a note

c) Nothing to compare, since he placed no September order; a separate quiet signal would name him

d) An unknown, so his July and August are dropped as well and he leaves the book until he orders

## How do you prove the call list without the window?

Used at work whenever a call list is about to go out and the definition behind it has to be confirmed
by a route that could disagree.

### Q4. Which route confirms the checked flags with no window, and what does it read?

Kavya Nair, the senior analyst who checks every number before it leaves the team, wants the checked
flags confirmed by a route that shares no window with them and would disagree if the calendar check
were wrong. Which route does that, and what does it read?

a) The Python walk from chapter 4, through the 752 member-months grouped by member and sorted: 752 rows

b) A self-join of each member's September row to his own August and July rows by calendar month

c) The calendar zero-filled and read with LAG over each member's six months: 1,806 rows

d) The checked LAG query rerun after the platform's overnight reload, set beside the first: 752 rows

## When is zero the right reading of an empty month?

Used at work whenever a missing value tempts someone to write in a default and the business has to
say what the gap means.

### Q5. Which fact would make filling an empty month with zero the honest reading?

Filling an empty month with zero turns a quiet month into a fall. Which fact, if it held, would make
zero the honest reading of an empty month?

a) Members buy in about 2.5 of six months, so most of their months are empty anyway

b) The calendar holds 1,806 rows, so every member already has a row to fill for each of the six months

c) Marketing wants more members to ring, and zeros would add 17 more calls this week

d) Every member is billed every month by default, so a month with no charge means he cancelled

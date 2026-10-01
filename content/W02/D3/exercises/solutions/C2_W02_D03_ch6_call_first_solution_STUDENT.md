# Which answers hold in the chapter 6 set on whom Marketing calls first and whether each flag holds up, and why?

Answers: 1d 2a 3c 4b 5d

Chapter 6 read the rows behind chapter 4's 16 flags. All 16 sit on a protect list. C-0216 bought in
May, July and September, so LAG compared their September with July and their July with May, four months
apart, and called a holiday a fall. Seven of the 16 flags step over a month with no order in the same
way; a check that the months LAG read are August and July keeps 9, and a self-join of each member's
September to their own August and July by calendar month keeps the same 9. A calendar filled with zero
would have flagged 26 members, 17 of whom simply placed no September order. Members buy in about 2.5 of
the six months, so an empty month is the usual state. Three of the five items are design items: 1, 4
and 5.

**Who needs the answer.** You need it to check your five letters after the lab or tonight. Every flag that
survives becomes a phone call to a member, and a flag built on an empty month accuses a loyal member
of drifting.

**The questions on the way.**

- What does the call-first set test about what an empty month means?
- Why is each call-first key right, and each other letter wrong?
- Why is item 4's Python walk worth arguing about?
- Where have real companies had to decide what a gap in a customer's buying means?

## What does the call-first set test about what an empty month means?

LAG reads rows and Marketing speaks in calendar months, so a flag's definition has to say what a month
with no order means before the flag runs. The design items size the four readings of "last month",
choose a second route that reads calendar months with no window, and name the business fact under which
zero would be the honest value. The other two items read what LAG compares for a member with gaps and
what a zero-filled calendar does to a member who stopped buying.

## Why is each call-first key right, and each other letter wrong?

### Q1. Which reading of "last month" fits the flag, sized in the rows it reads?

This is a design item: it asks for the reading that fits Marketing's words, with its size.

The key is d, "LAG on the 752 rows, with a flag kept only if `lag(month, 1)` is August and
`lag(month, 2)` July". It reads only the rows that exist and adds two columns, the months LAG read, so
a member who skipped August or July breaks the run and is not flagged, which is what "two months
running" says. On this book it keeps 9 of chapter 4's 16.

- Option a, "A calendar of every member and month, zero-filled: 1,806 rows, with an empty month read as
  zero", turns a quiet month into a fall to zero, which flags 26 members, 17 of them for a September
  with no order.
- Option b, "A calendar of every member and month, left empty: 752 rows, since empty months add no
  rows", has the right reading and the wrong size, since a calendar holds a row for every member in
  every month, empty or not, 301 times 6, 1,806.
- Option c, "LAG over each member's own months, as chapter 4 built it: 752 rows, each beside the month
  before", sets each row beside the member's previous row, which is the month before only when the
  member bought in it, so it steps over empty months, and 7 of the 16 flags compared months two or more
  apart.

### Q2. Which months does chapter 4's flag compare for an invented member with gaps, and does a flag that reads calendar months keep them?

This item asks you to predict the output on invented numbers.

The key is a, "September against June and April, so chapter 4's flag fires and the calendar flag drops
them". Y-01 has three rows. LAG reads the previous row, so their September sits beside June, Rs 2,700,
and June beside April, Rs 3,600, and Rs 1,300 below Rs 2,700 below Rs 3,600 fires chapter 4's flag. A
flag that reads calendar months asks for August and July, and Y-01 has neither, so it leaves them off.

- Option b, "September against August and July, read as zero, so chapter 4's flag cannot fire on a
  rise", assumes the empty months hold zeros, but the monthly table has no August or July row for Y-01,
  so LAG never sees a zero; it reads June and April, and the flag fires.
- Option c, "September against nothing, since LAG returns NULL across empty months, so neither flag
  fires", misplaces LAG's NULL, which comes only before a member's first row; across a gap LAG reads the
  last row there is.
- Option d, "September against June and April, so both flags keep them, since each month they ordered
  fell", gets the first half right, and the calendar flag exists to drop exactly this member, whose falls
  run across empty months.

### Q3. What does the book say about an invented member with no September order, and which flag should name them?

This item asks you to spot the plausible wrong output on invented numbers.

The key is c, "Nothing to compare, since they placed no September order; a separate went-quiet list
names them". Y-02 has no September row, so the falling-spend flag has no September spend to set beside
August. Filled with zero, their September reads as Rs 0 below Rs 1,800 below Rs 2,300, a fall twice
running that never happened. What the book does show is a member who bought in July and August and
then nothing, which is a different question with its own list. That list needs no calendar: a NOT
EXISTS or a HAVING over the 752-row monthly table finds the members who bought in July and August and
placed no September order, 27 of them on Kalpa's book, and a calendar left empty finds the same 27.

- Option a, "A fall to zero, so the falling-spend flag names them and Marketing rings them about that
  fall", would send a call describing a September spend they never had.
- Option b, "A fall to zero once their August is checked against July, so the flag names them with a
  note", gets the August check right, and the September reading is still a zero someone wrote in.
- Option d, "An unknown, so their July and August are dropped as well, and they leave the book until
  they buy", throws away two real months to hide one empty one, and loses a member who may most need
  a call.

### Q4. Which route confirms the nine calendar-month flags with no window, and what does it read?

This is a design item: it asks for the independent second route and what it reads.

The key is b, "A self-join of each member's September row to their own August and July rows: 359 rows
read". It joins rows by date with no window: the 118 September rows meet the 122 August rows and the
119 July rows, 359 member-months, and a member with no August or no July row has nothing to join to, so
a gap breaks the run by construction. In the chapter it kept the same 9 members as the flag that checks
the months LAG read, and it would disagree if that check were written wrong.

- Option a, "A walk in Python that sorts each member's months and sets each beside the one before: 752
  rows", shares no window, but it reads the previous row, as LAG does, so it finds chapter 4's 16 and
  repeats the very reading the month check corrects.
- Option c, "The calendar zero-filled and read with LAG over each member's six months: 1,806 rows",
  uses a window and reads a quiet month as zero, so it flags 26.
- Option d, "The flag's own LAG query rerun after the overnight reload, set beside the first run: 752
  rows", runs the same query twice, so it repeats whatever the query got wrong.

### Q5. Which fact would make filling an empty month with zero the honest reading?

This is a design item: it asks for the fact that would switch the reading.

The key is d, "Every member is billed every month by default, so a month with no charge means they
cancelled". Where every member is expected to pay every month, an empty month is a real zero, a lapse,
and a fall to zero is the strongest signal there is. Kalpa's members buy when they choose, about 2.5
months in six, so an empty month says nothing about their spend.

- Option a, "Members buy in about 2.5 of the six months, so most of a member's months are empty
  anyway", is the reason zero misleads here, since most zeros would be ordinary quiet months.
- Option b, "The calendar holds 1,806 rows, so each member already has a row to fill for each of six
  months", describes the table's size, which says nothing about what an empty month means.
- Option c, "A lost member costs Kalpa more than a wasted call, so reading a quiet month as a fall is
  safer", weighs the cost of an error, which can decide how long a call list runs or whether a
  went-quiet list goes out as well; it leaves the meaning of an empty month where it was, and the 17
  extra calls would tell members their spend fell when it did not.

## Why is item 4's Python walk worth arguing about?

Item 4's option a, the Python walk, feels like the safe check, since it was chapter 4's second route and
it agreed with LAG member for member. It agreed because it reads "the month before" the same way LAG
does, as the previous row, so it repeats the reading that put C-0216 on the call list. A second route
has to be independent of the assumption under test, and here the assumption is what an empty month
means.

## Where have real companies had to decide what a gap in a customer's buying means?

Shopify's data team warned merchants that "far too often businesses define churn as no purchases after
N days", and read a customer's gap against that customer's own history (Cam Davidson-Pilon, "How
Shopify Merchants can Measure Retention", Shopify Engineering, 14 November 2017, checked 1 October
2026). Hotel programmes treated a gap members did not choose as no reading: Marriott extended elite
status earned in 2019 until February 2022, and Hilton extended status to 31 March 2022 for members set
to downgrade in 2020 or 2021 (Marriott's release of 14 April 2020 and Hilton's of 27 October 2020,
checked 1 October 2026).

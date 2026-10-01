# Which answers hold in the chapter 6 set on whom Marketing calls first and whether each flag holds up, and why?

Answers: 1d 2a 3c 4b 5d

Chapter 6 read the rows behind chapter 4's 16 flags. All 16 sit on a protect list. C-0216 bought in
May, July and September, so LAG compared his September with July and his July with May, four months
apart, and called a holiday a fall. Seven of the 16 flags step over a month with no order in the same
way; the check that the two rows before September are August and July keeps 9, and a self-join of
each member's September to his own August and July by calendar month keeps the same 9. A calendar
filled with zero would have flagged 26 members, 17 of whom simply placed no September order. Members
buy in about 2.5 of the six months, so an empty month is the usual state. Three of the five items are
design items: 1, 4 and 5.

**Who needs the answer.** You, checking your five letters after the lab or tonight. Every flag that
survives becomes a phone call to a member, and a flag built on an empty month accuses a loyal member
of drifting.

**The questions on the way.**

- Which idea does this set test?
- Why is each key right, item by item?
- Which wrong answer is worth arguing about?
- Where does this show up at work?

## Which idea does this set test?

A flag's definition has to say what an empty month is before it runs, because LAG reads rows and the
stakeholder speaks in calendar months. The design items size the four readings, choose a second route
that reads calendar months with no window, and name the business fact under which zero would be the
honest value. The other items read what LAG compares for a member with gaps and what a zero-filled
calendar does to a member who went quiet.

## Why is each key right, item by item?

### Q1. Which reading of "last month" fits the flag, sized in the rows it reads?

Kind: a design item, the best-fit reading with its size.

The key is d, "LAG with a check that the two rows before September are August and July: 752 rows". It
reads only the rows that exist and adds two columns, `lag(month, 1)` and `lag(month, 2)`, so a member
who skipped August or July breaks the run and is not flagged, which is what "two months running" says.

- a, "A calendar of every member and month, zero-filled: 1,806 rows, a month with no order reading as
  zero": a quiet month becomes a fall to zero, which flags 26 members, 17 of them for a September with
  no order.
- b, "A calendar of every member and month, left empty: 752 rows, since empty months add no rows": the
  reading is right and the size is wrong; a calendar holds a row for every member in every month, 301
  times 6, 1,806.
- c, "LAG over each member's own months, as chapter 4 built it: 752 rows, with no check needed": steps
  over empty months, which is how 7 of the 16 flags compared months two or more apart.

### Q2. Which months does chapter 4's flag compare for an invented member with gaps, and does the checked flag keep him?

Kind: predict the output, on invented numbers.

The key is a, "September against June and April, so chapter 4's flag fires and the checked flag drops
him". Y-01 has three rows. LAG reads the previous row, so his September sits beside June, Rs 2,700, and
June beside April, Rs 3,600, and Rs 1,300 below Rs 2,700 below Rs 3,600 fires chapter 4's flag. The
check asks whether the two rows before September are August and July; they are June and April, so the
checked flag leaves him off.

- b, "September against August and July, each read as zero, so both flags keep him": the monthly table
  has no August or July row for him, so LAG never sees a zero, and Rs 1,300 against zero would be a
  rise.
- c, "September against nothing, since LAG returns NULL across empty months, so neither flag fires":
  LAG returns NULL only before a member's first row; across a gap it reads the last row there is.
- d, "September against June and April, so both flags keep him, since each month he ordered fell": the
  first half is right, and the checked flag exists to drop exactly this member.

### Q3. What does the book say about an invented member with no September order, and which flag should name him?

Kind: spot the plausible wrong output, on invented numbers.

The key is c, "Nothing to compare, since he placed no September order; a separate quiet signal would
name him". Y-02 has no September row, so the falling-spend flag has no September spend to set beside
August. Filled with zero, his September reads as Rs 0 below Rs 1,800 below Rs 2,300, a fall twice
running that never happened. What the book does show is a member who bought in July and August and
then nothing, which is a different question with its own name and its own list.

- a, "A fall to zero, so the falling-spend flag names him and Marketing rings him about a falling
  spend": the call would describe a September he never had.
- b, "A fall to zero once his August is checked against July, so the flag names him with a note": the
  August check holds and the September reading is still the zero someone wrote in.
- d, "An unknown, so his July and August are dropped as well and he leaves the book until he orders":
  throws away two real months to hide one empty one, and loses the member who may most need a call.

### Q4. Which route confirms the checked flags with no window, and what does it read?

Kind: a design item, the independent second route.

The key is b, "A self-join of each member's September row to his own August and July rows by calendar
month". It joins rows by date with no window: a member with no August or no July row has nothing to
join to, so a gap breaks the run by construction. In the chapter it kept the same 9 members as the
checked LAG, and it would disagree if the check on `lag(month)` were written wrong.

- a, "The Python walk from chapter 4, through the 752 member-months grouped by member and sorted: 752
  rows": the walk reads the previous row, as LAG does, so it agrees with chapter 4's 16 and shares the
  very reading the check corrects.
- c, "The calendar zero-filled and read with LAG over each member's six months: 1,806 rows": reads a
  quiet month as zero and flags 26.
- d, "The checked LAG query rerun after the platform's overnight reload, set beside the first: 752
  rows": the same query twice repeats whatever it got wrong.

### Q5. Which fact would make filling an empty month with zero the honest reading?

Kind: a design item, the fact that would switch the call.

The key is d, "Every member is billed every month by default, so a month with no charge means he
cancelled". Where every member is expected to pay every month, an empty month is a real zero, a lapse,
and a fall to zero is the strongest signal there is. Kalpa's members buy when they choose, about 2.5
months in six, so an empty month says nothing about their spend.

- a, "Members buy in about 2.5 of six months, so most of their months are empty anyway": that is the
  reason zero misleads here, since most zeros would be ordinary quiet months.
- b, "The calendar holds 1,806 rows, so every member already has a row to fill for each of the six
  months": the calendar's size says nothing about what an empty month means.
- c, "Marketing wants more members to ring, and zeros would add 17 more calls this week": 26 flags
  against the checked 9, and the 17 extra calls describe falls that did not happen.

## Which wrong answer is worth arguing about?

Item 4, option a. The Python walk was chapter 4's second route and it agreed with LAG member for
member, so it feels like the safe check. It agrees because it reads "the month before" the same way
LAG does, as the previous row, so it repeats the reading that put C-0216 on the call list. A second
route has to be independent of the assumption under test, and here the assumption is what an empty
month means.

## Where does this show up at work?

Shopify's data team warned merchants that "far too often businesses define churn as no purchases after
N days", and read a customer's gap against that customer's own history (Cam Davidson-Pilon, "How
Shopify Merchants can Measure Retention", Shopify Engineering, 14 November 2017, checked 1 October
2026). Hotel programmes treated a gap members did not choose as no reading: Marriott extended elite
status earned in 2019 until February 2022, and Hilton extended status to 31 March 2022 for members set
to downgrade in 2020 or 2021 (Marriott's release of 14 April 2020 and Hilton's of 27 October 2020,
checked 1 October 2026).

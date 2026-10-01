# When two members spent the same at the line, how many does a list ship, and which rule did the head of Retail-Plus ask for?

Chapter 3's set holds five items. Items 1 and 2 run live in chapter 3's last minutes if the chapter ran to
time; items 3 to 5 are the practice lab's stretch or tonight's work.

> "Ties matter. If two members spent the same, I want them ranked the same, and I want to know how
> many made the top fifty, not forty-nine because of a tie."
>
> The head of Retail-Plus, Kalpa Retail

The head of Retail-Plus owns Kalpa Retail's paid membership tier and defends every protect list to
the tier's members and to Marketing. Q2 is July to September 2026, and a member's Q2 revenue is the booked
amount of every Q2 order the member placed, whatever its status. Two members tie when their Q2
revenue is the same to the rupee. A list "ships" the members whose number is at or inside the line,
and four rules can number them. `ROW_NUMBER` gives every member a number of their own, and a second key,
the tiebreaker, decides between two who tie. `RANK` gives tied members the same number and skips the
numbers they use up, 1, 1, 3. `DENSE_RANK` gives them the same number and skips nothing, 1, 1, 2, so it
numbers the different spend figures. Whole ties only keeps a tie when all of it fits inside the line:
with `tied_with = count(*) OVER (PARTITION BY segment, q2_revenue)`, a member ships when
`rank + tied_with - 1` is at or inside the line. Retail-Core, Kalpa's everyday shoppers, has 96 Q2
buyers.

Items 1 and 2 use seven members, every one of them invented:

| Member (invented) | R | S | T | U | V | W | X |
|---|---|---|---|---|---|---|---|
| Q2 spend | Rs 8,400 | Rs 8,400 | Rs 7,950 | Rs 6,200 | Rs 6,200 | Rs 6,200 | Rs 5,100 |

Retail-Core by Q2 revenue, places 29 to 43. No two members share a figure in places 1 to 30.

| Place | Member | Q2 orders | Q2 revenue |
|---|---|---|---|
| 29 | C-0131 | 2 | Rs 4,700 |
| 30 | C-0023 | 3 | Rs 4,570 |
| 31 | C-0044 | 3 | Rs 4,540 |
| 32 | C-0132 | 2 | Rs 4,540 |
| 33 | C-0018 | 2 | Rs 4,440 |
| 34 | C-0113 | 2 | Rs 4,300 |
| 35 | C-0013 | 2 | Rs 4,270 |
| 36 | C-0124 | 2 | Rs 4,150 |
| 37 | C-0060 | 2 | Rs 4,120 |
| 38 | C-0121 | 2 | Rs 4,120 |
| 39 | C-0095 | 2 | Rs 4,070 |
| 40 | C-0108 | 4 | Rs 3,980 |
| 41 | C-0066 | 2 | Rs 3,960 |
| 42 | C-0118 | 2 | Rs 3,590 |
| 43 | C-0022 | 2 | Rs 3,520 |

**Who needs the answer.** The head of Retail-Plus needs it to answer a member left off with the same
spend as one kept, and the marketing lead needs it because the team makes one call for every member a
list ships. A
list labelled forty that carries forty-two spends two calls nobody planned.

**The questions on the way.**

- Which DENSE_RANK column comes back for the seven invented members?
- How many members does each rule ship for a top five of the seven?
- What explains DENSE_RANK's 42 on a Retail-Core top forty, and what does the head's rule ship?
- Which rule and which report fit thirty-one call slots for Retail-Core?
- Which route reaches the head's count for a top thirty-seven with no window, and what does it give?

**What you post.** One line of five letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

## How do the three functions number a tie?

This comes up at work whenever a ranked report meets two equal values and its reader asks why two rows share a
number.

### Q1. Which DENSE_RANK column comes back for the seven invented members?

The seven invented members are ranked with `dense_rank() OVER (ORDER BY spend DESC)`. Which column
comes back for R, S, T, U, V, W and X, in that order?

a) 1, 1, 3, 4, 4, 4, 7

b) 1, 1, 2, 3, 3, 3, 4

c) 1, 2, 3, 4, 5, 6, 7

d) 1, 1, 2, 3, 3, 3, 7

### Q2. How many members does each rule ship for a top five of the seven?

Marketing wants a top five from the seven invented members. How many members does each rule ship, in
the order ROW_NUMBER, RANK, DENSE_RANK and whole ties only?

a) 5, 6, 7 and 3

b) 5, 6, 6 and 3

c) 5, 5, 7 and 4

d) 5, 6, 7 and 6

## How long is Retail-Core's list under each rule?

This comes up at work whenever a top-N list arrives longer or shorter than N and the reason has to come before
anyone acts on it.

### Q3. What explains DENSE_RANK's 42 on a Retail-Core top forty, and what does the head's rule ship?

Marketing trims Retail-Core's list to forty. A colleague reports: "DENSE_RANK keeps ties together, so
Retail-Core's top forty is these 42 members." Reading the table of places 29 to 43, what explains the
42, and how many does the head of Retail-Plus's rule ship?

a) Two members tie at fortieth place, so both carry 40 under every rule, and RANK ships 42 as well

b) DENSE_RANK counts a member with two Q2 orders as two rows, and RANK ships 40, one row per member

c) Places 41 and 42 tie with each other, and a tie always ships whole, so RANK ships 42 as well

d) The ties at 31 and 37 each cost DENSE_RANK a number, so its 40 lands on place 42; RANK ships 40

## Which rule fits when the calls are capped?

This comes up at work whenever a list meets a hard limit, such as seats at a dinner, boxes already packed or
call slots in a week.

### Q4. Which rule and which report fit thirty-one call slots for Retail-Core?

Marketing's member team has thirty-one call slots for Retail-Core this week, and no thirty-second.
Places 31 and 32 in the table both booked Rs 4,540: C-0044 placed three Q2 orders and C-0132 two.
Which rule and which report fit?

a) RANK, which ships 32 members, and the team finds a thirty-second slot somewhere later in the week

b) Whole ties only, which ships 30, leaves both members on Rs 4,540 off and keeps one slot unused

c) ROW_NUMBER with more Q2 orders first, stated in advance: 31 ship, and the report names C-0132

d) ROW_NUMBER with the customer id deciding: 31 ship, C-0044 stays on their lower id, nothing to report

## How do you confirm a list's count without a window?

This comes up at work whenever a count goes to a stakeholder who will ask why the list holds more or fewer
than they asked for.

### Q5. Which route reaches the head's count for a top thirty-seven with no window, and what does it give?

For a Retail-Core top thirty-seven, which route reaches the count the head of Retail-Plus's rule ships
with no window at all, and what does it give?

a) Count the different Q2 figures at or above the thirty-seventh member's Rs 4,120: 36

b) Count the members who booked at least the thirty-seventh member's Rs 4,120: 38

c) Count the members who booked more than the thirty-seventh member's Rs 4,120: 36

d) Rerun the list with `rank()` in a window and count the rows it ships: 38

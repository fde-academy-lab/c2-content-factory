# When two members tie at fiftieth place, how many does a list ship, and which rule did the head of Retail-Plus ask for?

Chapter 3's set holds five items. Items 1 and 2 run live in chapter 3's last minutes if the chapter ran to
time; items 3 to 5 are the practice lab's stretch or tonight's work.

> "Ties matter. If two members spent the same, I want them ranked the same, and I want to know how
> many made the top fifty, not forty-nine because of a tie."
>
> The head of Retail-Plus, Kalpa Retail

The head of Retail-Plus owns Kalpa Retail's paid membership tier and defends every protect list to
the tier's members and to Marketing. Q2 is July to September 2026, and a member's Q2 revenue is the booked
amount of every Q2 order the member placed, whatever its status. Two members tie when their Q2
revenue is the same to the rupee. The line is the last place a list keeps, fifth on a top five and
fiftieth on a top fifty, and a list "ships" the members whose number is at or inside the line. Four
rules can number the members. `ROW_NUMBER` gives every member a number of their own and breaks a tie by
whatever else its ORDER BY names, the tiebreaker, or arbitrarily if nothing does. `RANK` gives tied
members the same number and skips the numbers they use up. `DENSE_RANK` gives tied members the same
number and skips nothing. Whole ties only keeps a tie when all of it fits inside the line and drops it
whole when it does not: with `tied_with = count(*) OVER (PARTITION BY segment, q2_revenue)`, a member
ships when `rank + tied_with - 1` is at or inside the line. Retail-Core, Kalpa's everyday shoppers, has
96 Q2 buyers.

Items 1 and 2 use seven members, every one of them invented:

| Member (invented) | R | S | T | U | V | W | X |
|---|---|---|---|---|---|---|---|
| Q2 spend | Rs 8,400 | Rs 8,400 | Rs 7,950 | Rs 6,200 | Rs 6,200 | Rs 6,200 | Rs 5,100 |

Retail-Core by Q2 revenue, places 29 to 43. No two members share a figure in places 1 to 30.

| Place | Member | Q2 revenue |
|---|---|---|
| 29 | C-0131 | Rs 4,700 |
| 30 | C-0023 | Rs 4,570 |
| 31 | C-0044 | Rs 4,540 |
| 32 | C-0132 | Rs 4,540 |
| 33 | C-0018 | Rs 4,440 |
| 34 | C-0113 | Rs 4,300 |
| 35 | C-0013 | Rs 4,270 |
| 36 | C-0124 | Rs 4,150 |
| 37 | C-0060 | Rs 4,120 |
| 38 | C-0121 | Rs 4,120 |
| 39 | C-0095 | Rs 4,070 |
| 40 | C-0108 | Rs 3,980 |
| 41 | C-0066 | Rs 3,960 |
| 42 | C-0118 | Rs 3,590 |
| 43 | C-0022 | Rs 3,520 |

**Who needs the answer.** The head of Retail-Plus needs it to answer a member left off with the same
spend as one kept, and the marketing lead needs it because the team makes one call for every member a
list ships. A list labelled fifty that carries fifty-two spends two calls nobody planned, and a list
that drops a tie at the line is the forty-nine the head refused.

**The questions on the way.**

- Which number does DENSE_RANK give X, and what does that number tell the head?
- How many members does each rule ship for a top five of the seven?
- What explains DENSE_RANK's 42 on a Retail-Core top forty, and what does the head's rule ship?
- Which fact would make whole ties only the right rule for Retail-Core's list?
- Which route reaches the head's count for a top thirty-seven with no window, and what does it give?

**What you post.** Five letters in item order, with no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

## How do the three functions number a tie?

This comes up at work whenever a ranked report meets two equal values and its reader asks why two rows share a
number.

### Q1. Which number does DENSE_RANK give X, and what does that number tell the head?

The head of Retail-Plus is shown the seven invented members ranked with
`dense_rank() OVER (ORDER BY spend DESC)` and asks what X's number says about X. Which number does X
carry, and what does it say?

a) 7, since six members in all spent more than X did

b) 4, since only three distinct amounts sit above X's

c) 4, since only three members in all spent more than X

d) 7, since X stands seventh of the seven members ranked

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

b) Every tie above the line adds one member to any list that keeps ties, so RANK ships 42 as well

c) Places 41 and 42 tie with each other, and DENSE_RANK keeps a tie whole, while RANK ships 40

d) The ties at 31 and 37 each cost DENSE_RANK a number, so its 40 is at place 42; RANK ships 40

## Which business fact decides the tie rule?

This comes up at work whenever a tie rule has to be defended to the people a list leaves off.

### Q4. Which fact would make whole ties only the right rule for Retail-Core's list?

The head of Retail-Plus turned whole ties only down for this quarter's list, because it ships
forty-nine when two members tie at fiftieth and fifty-first place. Which fact, if it held, would make
whole ties only the right rule for Retail-Core's list?

a) The member team has fifty call slots this week and cannot make a fifty-first call

b) Retail-Core has no tie at fiftieth, so whole ties only ships the same fifty as RANK

c) The budget pays for fifty offers at most, and equal spend must get an equal offer

d) The head wants every member who booked at least the fiftieth member's figure

## How do you confirm a list's count without a window?

This comes up at work whenever a list's count is questioned before the list goes out.

### Q5. Which route reaches the head's count for a top thirty-seven with no window, and what does it give?

For a Retail-Core top thirty-seven, which route reaches the count the head of Retail-Plus's rule ships
with no window at all, and what does it give?

a) Count the members holding one of the thirty-seven highest distinct figures: 39

b) Count the members who booked at least as much as the thirty-seventh member: 38

c) Count the members who booked more than the thirty-seventh member booked: 36

d) Sort the members by Q2 revenue, keep thirty-seven with LIMIT and count them: 37

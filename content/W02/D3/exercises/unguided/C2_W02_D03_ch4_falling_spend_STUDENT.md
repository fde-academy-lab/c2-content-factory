# Whose monthly spend fell two months running?

Chapter 4's set holds five items. Items 1 and 2 run live in chapter 4's last minutes if the chapter ran to
time; items 3 to 5 are the practice lab's stretch or tonight's work.

> "... and flag anyone whose monthly spend has fallen for two months running."
>
> The marketing lead, Kalpa Retail

A member's monthly spend is the booked revenue of the member's orders in one calendar month, every
order at its amount whatever its status. Kalpa Retail's book runs from April to September 2026, and the
monthly table holds one row per member per month with an order: 752 member-months for the 301 members
who bought at least once, 118 of whom ordered in September. The flag reads September, the last month:
September's spend below the member's month before it, and that month below the one before it.
`lag(spend, 1) OVER (PARTITION BY customer_id ORDER BY month)` puts the previous row's spend beside each
row, counting rows inside the member's own months in month order, `lag(spend, 2)` reads two rows back,
and on a member's first row LAG returns NULL, an empty value. The book is Kalpa's Postgres warehouse.

| C-0040, Retail-Core | April | May | June | July | August | September |
|---|---|---|---|---|---|---|
| Monthly spend | Rs 7,980 | Rs 3,170 | Rs 1,320 | Rs 4,260 | Rs 4,770 | Rs 4,520 |
| `lag(spend, 1)` | NULL | Rs 7,980 | Rs 3,170 | Rs 1,320 | Rs 4,260 | Rs 4,770 |

**Who needs the answer.** The marketing lead needs it, because the member team rings each flagged
member with a retention offer. A flag that names the wrong member costs a call and tells a loyal
customer they are slipping; a fall the flag misses is a member nobody rang until they had gone.

**The questions on the way.**

- Which way should set each month beside the two before it, and what does the self-join work through?
- Which members does a flag with no PARTITION BY name in the invented table?
- Which check proves that every value LAG read came from the row's own member, and what must it read?
- Which second route could a slip in the window not fool, and what does it read?
- Which fact would make the self-join the build to ship?

**What you post.** Your five letters in item order, with no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

## How should the team set each member's month beside the ones before it?

This comes up at work whenever a metric is compared with its own earlier values, one customer at a time.

### Q1. Which way should set each month beside the two before it, and what does the self-join work through?

Four ways could set each member's September beside the member's two rows before it. Which way fits,
and what does the self-join work through?

a) A self-join of the monthly table to itself, twice: 752 lookups, the same work as one pass

b) Months as spreadsheet columns, read by eye: 752 cells, one for each member-month with an order

c) LAG in a window: one pass over the 752 member-months, where the self-join makes 1,504 lookups

d) A correlated subquery per month, one lookup for each row: 752 lookups, the same work as LAG

## Whose months does LAG read?

This comes up at work whenever a window runs over a table that holds many customers' histories one after
another.

### Q2. Which members does a flag with no PARTITION BY name in the invented table?

Every number in this item is invented. Three members' monthly spend, sorted by member and month:

| Member (invented) | Month | Spend |
|---|---|---|
| X-01 | July | Rs 3,700 |
| X-01 | August | Rs 2,800 |
| X-01 | September | Rs 2,300 |
| X-02 | September | Rs 1,700 |
| X-03 | August | Rs 2,000 |
| X-03 | September | Rs 1,500 |

A hurried flag uses `lag(spend, 1) OVER (ORDER BY customer_id, month)` and `lag(spend, 2)` with the same
window, and keeps the September rows where each month fell. Which members does it flag?

a) X-01 alone, since LAG starts over at X-02's first row and reads nothing above it

b) X-01 and X-02, since X-02's one row reads X-01's September and August above it

c) X-01, X-02 and X-03, since each September row has two rows above it in the table

d) Nobody, since LAG gives NULL on every row until the window has a PARTITION BY

### Q3. Which check proves that every value LAG read came from the row's own member, and what must it read?

On a table of ten thousand member-months, too many to read by eye, which check proves that every
value LAG read came from the row's own member, and what must it read?

a) Count the flagged members beside the members who ordered in September: the flag must be smaller

b) Count the rows where `lag(spend, 1)` is NULL: it must read 1, the first row of the sorted table

c) Sort the output by customer id and month again: a sorted result cannot cross between members

d) Add `lag(customer_id)` over the same window and count the rows where it names another member: 0

## How do you prove the flag without the window?

This comes up at work whenever a flag is about to put a call through to a customer and the window behind it
could be wrong in a way its own output cannot show.

### Q4. Which second route could a slip in the window not fool, and what does it read?

Chapter 4's flag named 16 members. Kavya Nair, the senior analyst who checks every number before it
leaves the team, wants the 16 confirmed by a route that a slip in the window's PARTITION BY or ORDER BY
could not fool. Which route does that, and what does it read?

a) A walk in Python through the 752 member-months, grouped by member and sorted there: 752 rows

b) The same LAG query rerun after the platform's overnight reload, set beside the first: 752 rows

c) The LAG query run once per segment, with the same window in each of the four: 752 rows

d) A walk in Python through the 16 flagged members' months, grouped by member and sorted: 68 rows

## When is the window the wrong tool?

This comes up at work whenever a team has to say in advance which fact would make it change the build it
chose.

### Q5. Which fact would make the self-join the build to ship?

LAG over each member's own rows and a self-join can both set a member's September beside earlier
spend. The self-join matches each member's September row to that member's rows dated one and two months
earlier. Marketing has since said that "two months running" means September below August, and August
below July. Which fact, if it held, would make the self-join the build to ship?

a) The book grows to twelve months next year, so LAG will read twice as many member-months

b) Only 50 of the 118 members who ordered in September had also placed an order in August

c) Marketing wants the flag read at August as well, which takes a second pass with LAG

d) For 8 members, September was their first order, so LAG finds no row before it for them

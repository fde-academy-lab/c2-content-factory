# Can you rank a tie, choose GROUP BY or a window, and run the whole day on eight invented members, in an hour?

This is the TA-led practice lab set: three problems that climb in difficulty over about an hour, ten
minutes each for problems 1 and 2 and about forty for problem 3. Work alone for problems 1 and 2 and in pairs for
problem 3. The lab also hosts the escalated case's parts 3 to 5, from
`exercises/unguided/C2_W02_D03_escalated_case_STUDENT.md`, its debrief and the interview drill aloud;
the TA runs those around this set.

> "Retail-Plus frequency is the problem, so we want to protect our best members before they drift.
> Give us the top fifty customers by Q2 revenue in each segment, and flag anyone whose monthly spend
> has fallen for two months running."
>
> The marketing lead, Kalpa Retail

Kalpa Retail's warehouse is a Postgres database: `orders` (1,000 rows, one per order: order_id,
customer_id, order_date, quarter, channel, amount, status) and `customers` (340 rows, one per member:
customer_id, segment, city, country, joined_date). Q2 is July to September 2026, and a member's Q2
revenue is the booked amount of every Q2 order the member placed, whatever its status. Kalpa's members
live in six cities and belong to four segments: Business, Retail-Core, Retail-Plus (the paid
membership tier) and Student. The head of Retail-Plus's rule for a list is that members who spent the
same share a place, the places they use up are skipped, and the list says how many it ships. The
line is the last place a list keeps, fifth on a top five.
`ROW_NUMBER` gives every member a number of their own, `RANK` gives tied members one number and skips
the numbers they use up, and `DENSE_RANK` gives them one number and skips nothing. GROUP BY returns one
row per group; a window keeps every row and adds a value computed from the rows around it. A member's
monthly spend is their booked revenue in one calendar month, and the falling-spend flag reads September
below August and August below July, in calendar months. Problems 1 and 3 run on invented members,
labelled invented; problem 2 runs on the warehouse.

**Who needs the answer.** The marketing lead needs it, because these habits build Marketing's lists
and calls, and you need it in an analyst interview, where the same three moves come up on tables nobody has seen: say what a ranking
gives on a tie before running it, say whether an ask needs GROUP BY or a window and how many rows it
returns, and run the whole chain on fresh numbers with its checks.

**The questions on the way.**

- What do RANK and DENSE_RANK give seven invented members, and how many does each ship at four and at five?
- Which of six asks need GROUP BY and which a window, and which build fits the ask by city?
- What do eight invented members say about the list, the calls, the running total and its second route?

**What you post.** One line of ten letters in item order, no spaces, then your problem 3 queries
pasted below it:

```
Post exactly this shape: xxxxxxxxxx
```

---

## Problem 1. What do three ranking functions give seven invented members, and how many does each ship?

This comes up at work every time a ranked list meets a tie, since a count you predicted is the cheapest check
there is.

Work alone for ten minutes. Write your answers on paper first, then type the seven members into a `VALUES`
list and check them.

| Member (invented) | G | H | J | K | L | M | N |
|---|---|---|---|---|---|---|---|
| Q2 spend | Rs 6,450 | Rs 5,980 | Rs 5,980 | Rs 5,120 | Rs 4,870 | Rs 4,870 | Rs 4,870 |

### Q1. Which RANK column comes back for the seven invented members?

The seven are ranked with `rank() OVER (ORDER BY spend DESC)`. Which column comes back for G, H, J, K,
L, M and N, in that order?

a) 1, 2, 2, 3, 4, 4, 4

b) 1, 2, 3, 4, 5, 6, 7

c) 1, 2, 2, 4, 5, 5, 5

d) 1, 2, 2, 4, 5, 6, 7

### Q2. Which DENSE_RANK column comes back for the seven invented members?

The same seven are ranked with `dense_rank() OVER (ORDER BY spend DESC)`. Which column comes back?

a) 1, 2, 2, 4, 5, 5, 5

b) 1, 2, 2, 3, 4, 4, 4

c) 1, 2, 2, 3, 4, 5, 6

d) 1, 1, 1, 2, 3, 3, 3

### Q3. How many members do RANK and DENSE_RANK ship for a top four, and then for a top five?

Marketing asks for a top four from the seven, then widens it to a top five. How many members does RANK
ship each time, and how many does DENSE_RANK ship?

a) RANK 4 then 5, and DENSE_RANK 4 then 5

b) RANK 4 then 7, and DENSE_RANK 4 then 5

c) RANK 5 then 7, and DENSE_RANK 7 both times

d) RANK 4 then 7, and DENSE_RANK 7 both times

## Problem 2. Which of Marketing's asks need GROUP BY, which need a window, and which build fits the ask by city?

This comes up at work whenever a stakeholder's ask arrives and the first question is whether its answer is one
row per group or one row per row you started with.

Work alone for ten minutes. No city has two members tied at third place by Q2 revenue.

| Ask | What Marketing wants |
|---|---|
| Ask 1 | The three members who spent most in Q2 in each city |
| Ask 2 | The number of members who bought in Q2, segment by segment |
| Ask 3 | The segments with more than fifty members buying in Q2 |
| Ask 4 | Each month a member bought in, beside what the same member spent in the month they last bought before it |
| Ask 5 | Every Q2 buyer's Q2 revenue beside the Q2 total of the buyer's segment |
| Ask 6 | The average Q2 revenue per buying member, one line per segment |

### Q4. Which pattern of GROUP BY (G) and window (W) answers the six asks, in order?

Which pattern answers asks 1 to 6, in order?

a) W, G, G, W, W, G

b) W, G, G, G, W, G

c) G, G, G, W, W, G

d) W, G, W, W, G, G

### Q5. Which build fits ask 1, and how many queries and order reads does it take?

Which build fits ask 1, sized in the queries it takes and the Q2 order rows it reads?

a) Six sorted queries, one per city, each with LIMIT 3, glued with UNION ALL: six queries reading 2,772 order rows

b) One query ranking members in a window partitioned by city, places 1 to 3 kept outside: one query reading 462

c) `GROUP BY city` with `max(q2_revenue)`: one query reading 462 rows, returning each city's top figure alone

d) `GROUP BY city, customer_id` sorted by Q2 revenue with `LIMIT 18`: one query reading 462, the book's top 18

## Problem 3. What do eight invented members say about the list, the calls, the running total and its second route?

This comes up at work whenever a whole analysis has to be run end to end on data nobody has explained, with
every check in place before a line leaves.

Work in pairs for about forty minutes. Kavya Nair, the senior analyst on Kalpa Retail's data team, hands every
new analyst the same drill: the whole day on eight members, every number invented, small enough to
check by hand. Their monthly spend is below, with a blank where a member placed no order:

| Member (invented) | May | June | July | August | September |
|---|---|---|---|---|---|
| V-01 | | | Rs 2,700 | Rs 2,950 | Rs 2,150 |
| V-02 | Rs 4,500 | | Rs 3,900 | | Rs 3,000 |
| V-03 | | | Rs 4,100 | Rs 3,200 | Rs 2,300 |
| V-04 | | | Rs 2,050 | Rs 1,550 | Rs 1,100 |
| V-05 | | | Rs 2,300 | Rs 1,750 | Rs 1,350 |
| V-06 | | Rs 4,000 | Rs 3,500 | | Rs 4,300 |
| V-07 | | | Rs 2,100 | Rs 1,800 | |
| V-08 | | | Rs 1,500 | Rs 2,100 | Rs 1,800 |

Build it in one SQL file, as named steps on one `VALUES` list of (member, month, spend), a row only
for a month with an order, in four steps:

1. Rank each member's Q2 revenue, July to September, under the head of Retail-Plus's rule, and keep a
   top five.
2. Flag members with LAG over each member's own months, read at September, and check that the two rows
   before September are August and July.
3. List the calls, which are the members on the list whose checked flag holds.
4. Accumulate all eight members' Q2 revenue from the biggest down.

### Q6. How many members does the top five ship under the head of Retail-Plus's rule, and why?

How many members does the top five ship under the head of Retail-Plus's rule, and why?

a) Five: V-03, V-01, V-06, V-02 and V-05, with V-08 left off by their id

b) Four, since the tie at fifth straddles the line and both of its members drop

c) Six, since V-05 and V-08 tie at fifth on Rs 5,400 and both of them ship

d) Seven, since the ties at second and at fifth each save the list a number

### Q7. Which member on the hurried flag would a call wrongly accuse, and why?

A hurried flag, LAG over each member's own months with no calendar check, names four members: V-02,
V-03, V-04 and V-05. Which of them would a call wrongly accuse of falling two months running, and why?

a) V-02, since LAG compared their September with July and their July with May

b) V-04, since they stand off the top five and Marketing does not ring them

c) V-05, since their September fell by less than their August did

d) V-03, since their fall began in July, before the two months Marketing named

### Q8. Who does Marketing ring first: listed under the head's rule and flagged on calendar months?

Who does Marketing ring first, taking the members on the list whose calendar-checked flag holds?

a) V-02, V-03 and V-05

b) V-03, V-04 and V-05

c) V-03 alone

d) V-03 and V-05

### Q9. What do V-01's and V-06's rows of the running total show, and what makes each row its own step?

All eight members' Q2 revenue is accumulated from the biggest down with
`sum(q2_revenue) OVER (ORDER BY q2_revenue DESC)`. What do V-01's and V-06's rows show, and what makes
each row its own step?

a) Rs 17,400 and Rs 25,200, since each row adds its own Rs 7,800, so nothing needs changing

b) Rs 25,200 on both, since the two are peers on Rs 7,800; add the member id to the ORDER BY

c) Rs 7,800 on both, since a running total restarts at a tie; add `PARTITION BY q2_revenue`

d) Rs 25,200 on both, since the total belongs on every row; drop the ORDER BY from the window

### Q10. Which route reaches the head's count for a top two with no window, and what does it give?

Kavya changes the drill to a top two and asks for the head of Retail-Plus's count reached with no
window at all. Which route does that, and what does it give?

a) Count the different Q2 figures at or above the second member's Rs 7,800: 2

b) Count the members who booked more than the second member's Rs 7,800: 1

c) Count the members who booked at least the second member's Rs 7,800 in Q2: 3

d) Sort the eight by Q2 revenue, keep two rows with `LIMIT 2` and count them: 2

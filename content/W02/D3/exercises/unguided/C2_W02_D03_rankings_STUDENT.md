# Round 2 set: how many make the list when two members tie?

The head of Retail-Plus wrote: "Ties matter. If two members spent the same, I want them ranked the
same, and I want to know how many made the top fifty, not forty-nine because of a tie." Three
ranking functions treat a tie three ways, and each way ships a different number of members. This
set asks you to predict each function on paper, count what each rule ships, and choose the rule
you would defend to him.

Seven items, about fifteen minutes, worked in pairs and on paper before anything runs. Items 1 to 4
use six invented members, P to U, whose Q2 spend is below. The invented members exist only for
this set.

| Member (invented) | Q2 spend |
|---|---|
| P | Rs 9,200 |
| Q | Rs 7,600 |
| R | Rs 7,600 |
| S | Rs 7,600 |
| T | Rs 7,600 |
| U | Rs 5,300 |

Post one line in this shape, your seven letters in item order: `1x 2x 3x 4x 5x 6x 7x`

---

### Q1

Marketing ranks the six with `rank() OVER (ORDER BY spend DESC)`. Which column comes back for
P, Q, R, S, T and U?

a) 1, 2, 3, 4, 5, 6
b) 1, 2, 2, 2, 2, 3
c) 1, 2, 2, 2, 2, 6
d) 1, 2, 2, 2, 2, 5

### Q2

The same six ranked with `dense_rank() OVER (ORDER BY spend DESC)`. Which column comes back?

a) 1, 2, 2, 2, 2, 3
b) 1, 2, 2, 2, 2, 6
c) 1, 2, 3, 4, 5, 6
d) 1, 1, 1, 1, 1, 2

### Q3

The same six ranked with `row_number() OVER (ORDER BY spend DESC)` and nothing else in the order.
What can you say about Q, R, S and T?

a) All four share position 2, since equal spends share a number
b) They take 2 to 5 in alphabetical order, the same on every run
c) They take 2 to 5 in the order their first orders were placed
d) They take 2 to 5 in an order the database picks for that run

### Q4

Marketing wants a top three from these six. How many members does each rule ship, read in the
order ROW_NUMBER, RANK, DENSE_RANK?

a) 3, 3 and 3, since the cut-off is three
b) 3, 5 and 6
c) 3, 5 and 5
d) 3, 4 and 6

### Q5

On Kalpa's Retail-Core list, ROW_NUMBER at fifty or below ships 50 members, RANK ships 50, and
DENSE_RANK ships 52. The fiftieth member spent Rs 2,980 and the fifty-first Rs 2,950. What
explains the 52?

a) Two members tie at fiftieth, so both of them carry position 50 under every rule
b) DENSE_RANK counts members who bought in more than one month as two rows each
c) The fifty-first and fifty-second members tie with each other, and a tie always ships whole
d) Ties higher up each save a number, so the 51st and 52nd members carry dense 49 and 50

### Q6

A segment head tells you: "If two members spent the same, rank them the same, and tell me how many
made the top fifty." Which rule do you ship, and what goes in the report?

a) DENSE_RANK at fifty or below, since tied members share one number and no gap opens
b) ROW_NUMBER with customer_id as a tiebreaker, so the list holds fifty on every run
c) RANK at fifty or below, with the count stated, since a tie at the line ships whole
d) Whole ties only, dropping any tie that crosses the line, so the list never runs over

### Q7

Suppose a Student top ten is built with `row_number() OVER (ORDER BY q2_revenue DESC)`. A member
is on Monday's list and off Tuesday's, and no Student order changed between the two runs. What
happened?

a) The Tuesday run read a stale copy of the orders, so her revenue was lower there
b) She tied with another member at tenth, and ROW_NUMBER broke the tie a new way
c) One of her orders was refunded overnight, which moved her below the tenth member
d) RANK would have flipped her the same way, since every function must break a tie

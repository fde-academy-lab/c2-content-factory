# Which extra fits you tonight: the stretch on a Q2-only protect list, or the recovery drill on the grain?

Both are optional and neither is graded. Pick the one that matches where you are after today's six
chapters on Meera's chief of staff's three asks: the revenue tree by segment for both quarters, the
protect list of fifty Retail-Plus members with a lookup by id, and the front-page number, in a
workbook a director can change in the room.

---

## Stretch: which Retail-Plus members would a protect list built on Q2 alone pick, and where does it disagree with today's list?

This one is for you if you finished the escalated case early and the lookup felt easy.

**Who needs the answer.** The head of Retail-Plus, Kalpa Retail's paid membership tier, sends a
retention offer to each member on the protect list and will ask which list to act on: today's, which
ranks members by revenue across April to September 2026 from the customer table, or one that ranks
them by Q2 alone, July to September, the quarter in which members ordered less often.

**The questions on the way.**

1. How do you add up each member's Q2 revenue from the raw export without counting an order twice?
2. Which fifty members does a Q2 ranking pick, and what happens at the fiftieth place?
3. How many members sit on both lists, and how many on only one?
4. Which list answers which of the head of Retail-Plus's questions?

### How do you add up each member's Q2 revenue from the raw export without counting an order twice?

The raw export holds one row per payment, with the order's amount on every row of that order. Add a
column that carries `order_amount` only on the first row of each order, and only when the order falls
in Q2. Then, on a new tab, add each Retail-Plus member's Q2 revenue with `SUMIFS` over that column.
Before you trust the ranking, check your Retail-Plus Q2 total against the warehouse's Retail-Plus Q2,
Rs 4,13,380; 76 Retail-Plus members ordered in Q2.

### Which fifty members does a Q2 ranking pick, and what happens at the fiftieth place?

Rank the members with `COUNTIFS`, breaking ties by id, and keep fifty. Look at the fiftieth place and
the fifty-first, and say how many rows the list ships if ties rank the same, which is the question
Wednesday's tie rule settled.

### How many members sit on both lists, and how many on only one?

Put the top fifty by Q2 beside today's top fifty across both quarters, and count the members on one
list and not the other. You should find 36 members on both lists and 14 on only one side of each.
For every member on the Q2 list and not on today's, find where that member sits in the customer
table, and say why each one is missing from today's list.

### Which list answers which of the head of Retail-Plus's questions?

Write two sentences: which list answers "who is drifting now", and which answers "who has been worth
most across the half-year". Then say which one the retention offer should go to, and what fact would
change your answer.

---

## Recovery: what does a pivot add on thirteen rows, and which rows does each count keep?

If chapter 2 lost you, start here and do it on paper first.

**Who needs the answer.** You, before Saturday's paper. The grain is the first thing every later
chapter assumed, and a number built on the wrong grain is wrong whatever else is right.

**The questions on the way.**

1. How many rows does each order occupy, and what does a Sum of them add?
2. Which rows does Remove Duplicates take out?
3. What is the total when each order counts once?

### How many rows does each order occupy, and what does a Sum of them add?

An invented export from the app channel, one row per payment: seven orders paid once, worth Rs 20,000
together; two orders of Rs 40,000 and Rs 60,000, each paid in two instalments on different dates; and
one order of Rs 2,000, which the gateway posted twice. Every row carries its order's amount. Write the
rows out and add them up: you should reach 13 rows for 10 orders. Then add what each row carries: you
should reach Rs 2,24,000, which is what a pivot's Sum shows.

### Which rows does Remove Duplicates take out?

Cross out only the rows identical to another row in every column. Which one goes? You should keep 12
rows and Rs 2,22,000, because the two instalment rows of an order differ in their dates.

### What is the total when each order counts once?

Keep only the first row of each order: you should reach 10 rows and Rs 1,22,000. Say in one sentence
why crossing out duplicates did not reach this number. Then open the companion page,
`demos/C2_W02_D05_last_mile_STUDENT.html`, run its experiment on invented rows that counts each order
once, and rerun the chapter 2 set, `exercises/unguided/C2_W02_D05_ch2_both_quarters_STUDENT.md`.

# Can the table rebuild itself every Monday and refuse to ship when something breaks?

Chapter 6 set, five items, after chapter 6: items 1 and 2 run live in the chapter's last three
minutes; the rest are the practice lab's stretch or tonight's work.

> "We send the codes on Monday morning before anyone has looked at the run. If the table is wrong, I
> would rather it did not arrive at all."
>
> The growth team, Kalpa Retail

The growth team sends a win-back code to every customer the Monday table flags as lapsed: no order in
the 60 days before the table's as-of date, the last date the data covers. Recency is the number of
days from a customer's last order to that date, and the days from the as-of date to the run day are
the data's age. A customer who never ordered is not lapsed and gets the first-order nudge instead.
The warehouse's last order is dated 28 September 2026, and nothing after it has been loaded.

Chapter 6 made the table rebuild itself in one function, told only the warehouse connection and the
feed's path. It reads the orders, counts recency to the last order it read, carries that date as its
`as_of` column, and refuses to write a table that fails any of four guards: one row per customer, as
many rows as the customer list's 340, spend equal to the warehouse's Rs 19,84,00,000, and a guard on
the smallest recency. The honest win-back list holds 111 customers, and the warehouse, counting on
its own, agrees. Kavya Nair, the senior analyst on the team, lets the growth team act on a run
without her only when every guard has passed.

**Who needs the answer.** The growth team, which acts on Monday's table with nobody watching the run.
A refresh that counts from the wrong date sends codes to customers who bought weeks ago, and a broken
table that ships sends Monday's offers to the wrong people before anyone looks.

**The questions on the way.**

- What recency does the honest refresh write for a customer whose last order was 20 May?
- What does a smallest recency of 7 days say about this Monday's run?
- How should the refresh build the table as it would have stood on 31 August?
- Which guard is the only one to fire on each of three broken tables?
- Which fifth guard stops a run on stale data and still lets a normal Monday through?

Every store and date in item 1, and the loading schedule in item 5, are invented.

**What you post.** One line of five letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

### Q1. What recency does the honest refresh write for a customer whose last order was 20 May?

An invented Kalpa store's data ends on 30 June; its refresh runs on Monday 13 July. A customer last
ordered on 20 May, and the store's win-back line is 45 days. What recency does the honest refresh
write, and is the customer lapsed?

a) It writes 54 days, so the customer is lapsed on a 45-day line.
b) It writes 41 days, so the customer is not lapsed on a 45-day line.
c) It writes 13 days, the gap between the data's end and the run.
d) It writes 41 days, and the customer turns lapsed by the run day, 13 days later.

### Q2. What does a smallest recency of 7 days say about this Monday's run?

This Monday's refresh reports 340 rows, spend of Rs 19,84,00,000, an `as_of` of 28 September 2026
and a smallest recency of 7 days. What does the 7 say, and does any guard fire?

a) No guard fires, since rows, spend and the as-of date all agree with the warehouse.
b) No guard fires, since a 7 only says nobody happened to order in the data's last week.
c) The recency guard fires, since the days were counted to 5 October, a week past the data.
d) The recency guard fires, since the days were counted to 21 September, a week before the data's end.

### Q3. How should the refresh build the table as it would have stood on 31 August?

Finance's auditor asks for the growth team's table exactly as the refresh would have built it on
Monday 31 August 2026, from the orders placed before that day, with all four guards passing. Today
the refresh reads every order in the warehouse. Which change builds the auditor's table?

a) Read every order as now, and count recency to 31 August, the day it would have run.
b) Cut the orders and the spend guard's total at 31 August, and count recency to 31 August.
c) Cut the orders at 31 August, count recency to the last order kept, and keep the guards as they are.
d) Cut the orders and the spend guard's total at 31 August, and count recency to the last order kept.

### Q4. Which guard is the only one to fire on each of three broken tables?

Here are three broken copies of Monday's table:

1. The 39 customers who never ordered are dropped.
2. Recency is counted to the run day, 19 October.
3. One order's amount is added to its customer's spend twice.

The guards are the key guard (one row per customer), the count guard (as many rows as the customer
list), the spend guard (spend equal to the warehouse's) and the recency guard (a smallest recency of
0). Which guard is the only one to fire on copies 1, 2 and 3, in that order?

a) Count fires on copy 1, recency on copy 2 and spend on copy 3.
b) Key fires on copy 1, recency on copy 2 and spend on copy 3.
c) Count fires on copy 1, spend on copy 2 and recency on copy 3.
d) Count fires on copy 1, recency on copy 2 and key on copy 3.

### Q5. Which fifth guard stops a run on stale data and still lets a normal Monday through?

Invented: from November the warehouse loads each day's orders overnight, so on a normal Monday the
orders end on the Sunday before. One Monday the loads have been failing quietly for two weeks, so
the orders end 15 days before the run day; all four guards pass, and the codes go out. Which fifth
guard would have stopped that run and still let a normal Monday through?

a) The as-of date is the run day itself.
b) The as-of date is no more than seven days before the run day.
c) The win-back list holds no more customers than last Monday's list.
d) The spend still equals the warehouse's total when rechecked before the send.

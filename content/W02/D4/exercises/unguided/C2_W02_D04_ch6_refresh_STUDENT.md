# Can the table rebuild itself every Monday and refuse to ship when something breaks?

Chapter 6 set, five items, after chapter 6: items 1 and 2 run live in the chapter's last three
minutes; the rest are the practice lab's stretch or tonight's work.

> "We send the codes on Monday morning before anyone has looked at the run. If the table is wrong, I
> would rather it did not arrive at all."
>
> The growth team, Kalpa Retail

The growth team sends a win-back code to every customer the Monday table marks as lapsed: no order in
the 60 days before the table's as-of date, the last date the data covers. Recency is the number of
days from a customer's last order to that date. A customer who never ordered is not lapsed and gets
the first-order nudge instead. The warehouse's last order is dated 28 September 2026, and nothing
after it has been loaded.

Chapter 6 made the table rebuild itself in one function, told only the warehouse connection and the
feed's path. It counts recency to the data's own last date, carries that date as its `as_of` column,
and refuses to write a table that fails any of four guards: one row per customer, as many rows as the
customer list's 340, spend equal to the warehouse's Rs 19,84,00,000, and a smallest recency of 0.
The honest win-back list holds 111 customers, and the warehouse, counting on its own, agrees. Kavya
Nair, the senior analyst on the team, lets the growth team act on a run without her only when every
guard has passed.

**Who needs the answer.** The growth team, which acts on Monday's table with nobody watching the run.
A refresh that counts from the wrong date sends codes to customers who bought weeks ago, and a broken
table that ships sends Monday's offers to the wrong people before anyone looks.

**The questions on the way.**

- What recency does each refresh give a customer whose last order was 20 May?
- Which guard fires on a run whose smallest recency is 7 days?
- How should the refresh run once its only reader is a dashboard that queries the warehouse?
- Which guard is the only one to fire on each of three broken tables?
- What do the wall-clock refreshes cost in win-back codes nobody needed?

Every store, date and price in items 1 and 5 is invented.

**What you post.** One line of five letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

### Q1. What recency does each refresh give a customer whose last order was 20 May?

An invented Kalpa store's data ends on 30 June; its refresh runs on Monday 13 July. A customer last
ordered on 20 May, and the store's win-back line is 45 days. What recency does the honest refresh
write, and is the customer lapsed?

a) 54 days, lapsed on a 45-day line
b) 41 days, not lapsed on a 45-day line
c) 13 days, the gap between the data's end and the run
d) 41 days now, and lapsed by the run day, 13 days later

### Q2. Which guard fires on a run whose smallest recency is 7 days?

This Monday's refresh reports: 340 rows, spend Rs 19,84,00,000, `as_of` 28 September 2026, and a
smallest recency of 7 days. Which guard fires, and what does it say?

a) None, since rows, spend and the as-of date all agree with the warehouse
b) The spend guard, as recency counted wrongly moves spend between customers
c) The recency guard: recency was counted to a day after 28 September
d) The recency guard, since nobody can buy in a quarter's last 7 days

### Q3. How should the refresh run once its only reader is a dashboard that queries the warehouse?

Next quarter the growth team stops opening the table's CSV. Its only reader becomes a dashboard that
queries the warehouse directly. Which way should the Monday refresh run then?

a) The pandas function with guards, writing a CSV the dashboard imports weekly
b) A by-hand rerun of the notebooks before the dashboard's first viewer arrives
c) A function that prints PASS or FAIL beside each check and writes the table anyway
d) A SQL view the dashboard reads, with the four checks as the warehouse's own tests

### Q4. Which guard is the only one to fire on each of three broken tables?

Three broken copies of Monday's table:

1. The 39 customers who never ordered are dropped.
2. Recency is counted to the run day, 19 October.
3. One order's amount is added to its customer's spend twice.

The guards are the key guard (one row per customer), the count guard (as many rows as the customer
list), the spend guard (spend equal to the warehouse's) and the recency guard (a smallest recency of
0). Which guard is the only one to fire on copies 1, 2 and 3, in that order?

a) count, recency, spend
b) key, recency, spend
c) count, spend, recency
d) count, recency, key

### Q5. What do the wall-clock refreshes cost in win-back codes nobody needed?

Counted to the run day, the win-back list holds 166 customers on Monday 19 October and 187 on Monday
2 November, with no new data loaded; the honest list holds 111. Invented: each code sent costs Rs 150
in margin. What do the codes nobody needed cost on those two Mondays?

a) Rs 8,250 on 19 October, Rs 11,400 on 2 November
b) Rs 24,900 on 19 October, the whole list's codes
c) Rs 8,250 each Monday, since a sent list is fixed
d) Rs 16,650 on 19 October, the honest list's codes

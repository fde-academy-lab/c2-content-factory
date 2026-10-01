# Does the warehouse tell the same story as the file Meera's decision rested on?

Chapter 2 set, five items. Items 1 and 2 run live in chapter 2's last minutes if the chapter ran to
time; items 3 to 5 are the practice lab's stretch or tonight's work.

> "The warehouse holds the same orders and customers you cleaned last week, one thousand orders for
> the two quarters, already de-duplicated. Query it; do not export it."
>
> The data platform lead, Kalpa Retail

Last week the team answered Meera Raghavan, Kalpa Retail's CEO, from a file of 186 orders, and she
parked a Rs 12 crore acquisition budget on its story: customers held steady while each ordered less
often. This week Anand Iyer, the finance controller, wants the Monday numbers from the warehouse, whose
book holds 1,000 orders for the same two quarters, Q1 (April to June 2026) and Q2 (July to September
2026). The revenue tree splits a quarter's revenue into three branches that multiply back to it:
customers who bought, times orders per customer, times revenue per order. Each of these, with orders
and revenue themselves, is a leaf. A leaf read as a change is its Q2 value over its Q1 value, less
one, in percent. Customers who bought are counted once in a quarter however many orders they placed.
An order id names one order in the warehouse; a file kept elsewhere may number its orders its own way.

**Who needs the answer.** Anand wants to know which numbers his sheet signs for, and Meera's budget
stays parked on last week's story until someone says whether the book tells the same one. Two sources
that differ with nobody saying so leave a Rs 12 crore decision resting on a number the warehouse may
not support.

**The questions on the way.**

- Which comparison fits a store file that shares no ids with the warehouse, sized in the numbers it sets side by side?
- Which comparison finds three changed orders once Finance's file carries the warehouse's order ids?
- Which leaves disagree when two invented sources show the same revenue change?
- What most likely explains a regional file whose customers held flat while the book's fell?
- Which rebuild of the app's customers from each customer's history holds, and what does it show?

**What you post.** One line of five letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

## How should two sources be compared?

Used at work whenever a new system's numbers must be reconciled with the numbers a decision was
already taken on.

### Q1. Which comparison fits a store file that shares no ids with the warehouse, sized in the numbers it sets side by side?

The store operations team keeps its own file of 90 store orders across Q1 and Q2, numbered by its
tills, and neither its order numbers nor its customer numbers match anything in the warehouse. Its
revenue change from Q1 to Q2 matches the book's store change. Anand asks whether the file tells the
same story as the book. Which comparison fits?

a) The two sources' revenue in each quarter, four numbers, since the change already agrees
b) Twenty numbers: all five leaves for each quarter of each source, compared as Q2 over Q1
c) Order by order on the till number, 90 lookups against the book's store orders
d) The store team's spreadsheet rerun on an export of the book's 324 store orders

### Q2. Which comparison finds three changed orders once Finance's file carries the warehouse's order ids?

Finance's order file for Q2 comes from Finance's own system, carries the warehouse's order ids and
holds 462 orders, the same count as the book's Q2. The amounts in this item are invented: three of the
file's orders differ from the book, one by Rs 500 more, one by Rs 300 less and one by Rs 200 less.
Which comparison finds them, and what does the comparison of every leaf show?

a) The two totals, which agree to the rupee, so the file needs no further check
b) Every leaf as a change, which shows Q2 revenue Rs 1,000 apart and so flags the file
c) Order by order on the shared id, which names all three while every leaf agrees
d) Every leaf as a change, which names the three orders through the revenue per order leaf

## Do the leaves agree when the revenue does?

Used at work whenever two reports agree on a headline and someone has to say whether they agree on
the reasons.

### Q3. Which leaves disagree when two invented sources show the same revenue change?

The two sources below are invented. Both show revenue down 1.0 percent from Q1 to Q2.

| Source | Quarter | Orders | Customers who bought | Revenue |
|---|---|---|---|---|
| A | Q1 | 100 | 50 | Rs 10,00,000 |
| A | Q2 | 90 | 50 | Rs 9,90,000 |
| B | Q1 | 400 | 160 | Rs 40,00,000 |
| B | Q2 | 360 | 144 | Rs 39,60,000 |

Which leaves tell a different story from Q1 to Q2 in the two sources?

a) Customers and orders per customer, flat in one and down 10 percent in the other
b) Revenue per order alone, since B's orders are four times A's in each of the quarters
c) Orders alone, since B lost 40 orders between the quarters while A lost only 10
d) None, since both revenues fell by the same 1.0 percent from Q1 to Q2 in either source

### Q4. What most likely explains a regional file whose customers held flat while the book's fell?

Every number in this item is invented. The north region's manager keeps a file of 40 customers, which
shows customers who bought flat from Q1 to Q2 and orders per customer down 15 percent. The book shows
the region's customers down 12 percent, from 100 in Q1 to 88 in Q2, and orders per customer down 3
percent. In the manager's file, all 40 customers bought in both quarters; in the book, 70 of the
region's customers did. What most likely explains the gap?

a) The file was drawn from customers who bought in both quarters, so its customer leaf could not move
b) The book counts cancelled orders and the file does not, so the book's customers run lower
c) The manager's file is small, and on 40 customers every change is the usual wobble
d) The book counts a customer who bought in both quarters twice, once in each, so its fall is overstated

## How would you rebuild a change from each customer's history?

Used at work whenever a net movement goes on a sheet and someone asks who is behind it.

### Q5. Which rebuild of the app's customers from each customer's history holds, and what does it show?

On the book, the customers who bought through Kalpa's app fell from 133 in Q1 to 124 in Q2, a net fall
of 9. Kavya Nair, the team's senior analyst, wants both counts rebuilt a second way, from each app
customer's own history. Three filters over one row per app customer give their own counts: 52 bought
through the app in both quarters, 81 in Q1 only and 72 in Q2 only. Which rebuild holds, and what does
it show?

a) 133 less the net fall of 9 is 124, so 9 customers left the app and every other customer stayed
b) 52 plus 81 is 133 and 52 plus 72 is 124, so both quarters tie out and 153 customers moved
c) 52 plus 72 is 124, so the app kept 52 and added 72, and Q1's 133 cannot be rebuilt
d) 81 plus 72 plus 52 is 205, so 205 customers bought through the app in Q2

# How far did Retail-Plus members' spend fall from Q1 to Q2, month by month?

Chapter 3 set, five items, after chapter 3: items 1 and 2 run live in the chapter's last three
minutes; the rest are the practice lab's stretch or tonight's work.

> "I take one number to the growth review, and I use each member's months to decide whom we protect
> first. Give me both, and make sure they agree."
>
> The head of Retail-Plus, Kalpa Retail

Retail-Plus is Kalpa Retail's paid membership tier. A member's spend in a month is every order they
placed in it, at the prices charged, added up; Q1 is April to June 2026 and Q2 is July to
September. A long table holds one row per member per month that has orders. A wide table holds one
row per member and one column per month, and `pivot_table` builds it by turning the values of one
column into columns and putting one number in each cell; `melt` folds a wide table back into long.
A table's cells count every column, the member's id among them.

Chapter 3 found that Retail-Plus's 107 members who ordered bought in 266 member-months, and that the
tier took Rs 5,85,770 in Q1 and Rs 4,13,380 in Q2, a fall of 29.4 percent, or Rs 1,72,390. A query
in the warehouse that never pivots gave the same two quarters. Kavya Nair, the senior analyst on the
team, reviews every view before it reaches the head of Retail-Plus.

**Who needs the answer.** The head of Retail-Plus, who defends the tier at the growth review. A
number too small argues the problem away, and rows that stand for the wrong thing protect the wrong
members.

**The questions on the way.**

- What does a one-line pivot put in April's column for two invented members?
- What goes back to an analyst whose months view adds up to less than its orders?
- Which shape should carry the tier's twelve-month trend next year, sized on its rows and empty cells?
- What shape is the tier's pivot with months as the index and members as the columns?
- Which plan answers Finance's weekly months and the head's afternoon question together?

Every member, order and number in items 1, 2 and 3 is invented.

**What you post.** One line of five letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

### Q1. What does a one-line pivot put in April's column for two invented members?

Invented orders: member M1 ordered Rs 1,000 and Rs 3,000 in April and Rs 2,000 in May; member M2
ordered Rs 4,000 in April. The analyst runs

```python
orders.pivot_table(index="member", columns="month", values="amount")
```

with no other argument, then adds up April's column. What does the sum give?

a) It gives Rs 8,000.
b) It gives Rs 6,000.
c) It gives Rs 3,000.
d) It gives Rs 2,667.

### Q2. What goes back to an analyst whose months view adds up to less than its orders?

Invented: an analyst sends the head of a loyalty tier a months view, one row per member and one
column per month. Its Q1 columns add up to Rs 3,10,000 and its Q2 columns to Rs 2,90,000, a fall of
6.5 percent. The orders the view was built from total Rs 8,40,000. What goes back to the analyst
before anyone reads a month?

a) Ship it, since the fall of 6.5 percent comes from the view's own columns.
b) Rebuild it with `fill_value=0`, since the empty months pulled the sums down.
c) Rs 2,40,000 of orders is missing, so the index must have dropped members.
d) The cells add up to Rs 6,00,000 of Rs 8,40,000, so name the aggfunc.

### Q3. Which shape should carry the tier's twelve-month trend next year, sized on its rows and empty cells?

Invented projection: next year the tier has 150 members who order, in about 540 member-months
across 12 months. The head of Retail-Plus wants one slide: the tier's spend month by month, as a
line. Which shape fits, and what does it hold?

a) The wide table fits, at 150 rows by 13 columns, 1,950 cells, 1,260 of them empty, read along a row.
b) A query per month fits, with 12 columns written by hand, so a 13th month is an edit.
c) The long table fits, at 540 rows by 3 columns, 1,620 cells, none empty, one total a month by `groupby`.
d) The pivot indexed by order fits, with a row per order and 12 columns, nearly all of them empty.

### Q4. What shape is the tier's pivot with months as the index and members as the columns?

Retail-Plus's 355 orders came from 107 members across the six months from April to September 2026.
What shape does this call return, as rows by columns?

```python
plus.pivot_table(index="month", columns="customer_id", values="amount", aggfunc="sum")
```

a) It returns 6 rows by 107 columns.
b) It returns 107 rows by 6 columns.
c) It returns 355 rows by 6 columns.
d) It returns 6 rows by 355 columns.

### Q5. Which plan answers Finance's weekly months and the head's afternoon question together?

Next month two asks arrive on the same day. Finance wants Retail-Plus's spend month by month every
Monday, beside its revenue query, and Anand Iyer, the finance controller, has an analyst who reruns
it from the warehouse. The head of Retail-Plus wants to try three ways of ranking the members whose
spend fell, this afternoon, before the growth review. Which plan fits both?

a) Both stay in pandas, and the notebook with its long and wide tables goes to Finance each Monday.
b) Finance gets one query grouped by month, and the head's three tries run in pandas on the tables.
c) Finance gets a query per month, typed by hand, and the head's three tries run in pandas.
d) Both move to the warehouse, as Finance's query and a new query for each of the head's tries.

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
- Which fact would move the months view from pandas into the warehouse?

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

a) Rs 8,000
b) Rs 6,000
c) Rs 3,000
d) Rs 2,667

### Q2. What goes back to an analyst whose months view adds up to less than its orders?

Invented: an analyst sends the head of a loyalty tier a months view, one row per member and one
column per month. Its Q1 columns add up to Rs 3,10,000 and its Q2 columns to Rs 2,90,000, a fall of
6.5 percent. The orders the view was built from total Rs 8,40,000. What goes back to the analyst
before anyone reads a month?

a) Ship it, since the fall of 6.5 percent comes from the view's own columns
b) Rebuild it with `fill_value=0`, since the empty months pulled the sums down
c) Rs 2,40,000 of orders is missing, so the index must have dropped members
d) Its cells are not totals: Rs 6,00,000 against Rs 8,40,000; name the aggfunc

### Q3. Which shape should carry the tier's twelve-month trend next year, sized on its rows and empty cells?

Invented projection: next year the tier has 150 members who order, in about 540 member-months
across 12 months. The head of Retail-Plus wants one slide: the tier's spend month by month, as a
line. Which shape fits, and what does it hold?

a) The wide table: 1,800 cells, 1,260 of them empty, read along each member's row
b) A query per month: 12 columns written by hand, and a 13th month is an edit
c) The long table: 540 rows, none empty, one total a month by `groupby`
d) The pivot indexed by order: a row per order and 12 columns, nearly all empty

### Q4. What shape is the tier's pivot with months as the index and members as the columns?

Retail-Plus's 355 orders came from 107 members across the six months from April to September 2026.
What shape does this call return, as rows by columns?

```python
plus.pivot_table(index="month", columns="customer_id", values="amount", aggfunc="sum")
```

a) 6 by 107
b) 107 by 6
c) 355 by 6
d) 6 by 355

### Q5. Which fact would move the months view from pandas into the warehouse?

Chapter 3 built the months view in pandas, the long and wide tables together. Which of these facts
would move it into the warehouse as a query, with a table of months in place of hand-written
columns?

a) The head of Retail-Plus asks for October once its orders arrive
b) Finance asks to rerun the view every Monday beside its revenue query
c) The tier grows from 120 members to 400, so the wide table gets longer
d) Members place several orders a month, so each cell needs a sum

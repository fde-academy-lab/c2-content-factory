# How do ROW_NUMBER, RANK and DENSE_RANK treat a tie, and what does the head of Retail-Plus's rule ship for Retail-Core?

You build this one with the trainer in chapter 3, in about fifteen minutes. The trainer types each step on the
projector and says aloud what each function does to the tie; you type the same step in your own
query tab on the warehouse, or run the same block from `sql/C2_W02_D03_03_tie_rule_STUDENT.sql`, and
compare. Steps 1 and 2 run on invented members, labelled invented, so the mechanism fits on one
screen; step 3 runs on Kalpa's Retail-Core members; step 4 is the sentence the head of Retail-Plus
reads. Answer each item before you run its step, then run the step and look where it tells you.

> "Ties matter. If two members spent the same, I want them ranked the same, and I want to know how
> many made the top fifty, not forty-nine because of a tie."
>
> The head of Retail-Plus, Kalpa Retail

Q2 is July to September 2026, and a member's Q2 revenue is the booked amount of every Q2 order the
member placed, whatever its status. Two members tie when their Q2 revenue is the same to the rupee.
The line is the last place a list keeps, fourth on a top four and fiftieth on a top fifty, and a list
"ships" the members whose number is at or inside the line. Chapter 2 cut each segment's list with
`row_number()`, which breaks a tie by whatever else its ORDER BY names, there the customer id, or
arbitrarily if nothing does, and the head of Retail-Plus is asking whether that is fair. Three window
functions number a list: `ROW_NUMBER`, `RANK` and `DENSE_RANK`. A fourth rule, whole ties only, keeps a
tie only when all of it fits inside the line, using `tied_with = count(*) OVER (PARTITION BY q2_revenue)`,
the number of members who share a figure: a member ships when `rank + tied_with - 1` is at or inside
the line. Retail-Core, Kalpa's everyday shoppers, has 96 Q2 buyers.

**Who needs the answer.** The head of Retail-Plus needs it to defend every count to the tier's members,
and a count you cannot explain in one sentence is one the head cannot defend. You need to say, for any
list, which rule made its count and which members stand at its line.

**The questions on the way.**

- What does DENSE_RANK give the six invented members?
- How many members does each rule ship on an invented top four?
- How many Retail-Core members does DENSE_RANK put on a top fifty, and why?
- Which statement about Retail-Core's fiftieth place holds?
- Which sentence goes to the head of Retail-Plus about Retail-Core's list?

**What you post.** Five letters in item order, with no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

## How do three functions number one tie?

This comes up at work whenever a ranked report meets two equal values and its reader asks why two rows share a
number.

**Step 1, three functions on six invented members.** All six members are invented: A and B
spent Rs 7,500 each, C Rs 6,000, D and E Rs 5,200 each and F Rs 4,100. Said aloud: the same ORDER BY
feeds three functions, and only what they do at a tie differs.

```sql
WITH invented (member, spend) AS (
    VALUES ('A', 7500), ('B', 7500), ('C', 6000), ('D', 5200), ('E', 5200), ('F', 4100)
)
SELECT member, spend,
       row_number() OVER (ORDER BY spend DESC, member) AS row_number,
       rank()       OVER (ORDER BY spend DESC)         AS rank,
       dense_rank() OVER (ORDER BY spend DESC)         AS dense_rank
FROM   invented
ORDER  BY spend DESC, member;
```

### Q1. What does DENSE_RANK give the six invented members?

Before step 1 runs, what does the `dense_rank` column give A, B, C, D, E and F, in that order?

a) 1, 2, 3, 4, 5, 6

b) 1, 1, 3, 4, 4, 6

c) 1, 1, 1, 2, 2, 3

d) 1, 1, 2, 3, 3, 4

Then run step 1 and read the three columns side by side, member by member, against your answer.

## How many members does each rule ship when a tie sits on the line?

This comes up at work whenever a top-N list arrives longer or shorter than N and somebody has to say why.

**Step 2, a top four with a tie at the line, invented.** The invented members now spent Rs 9,100,
Rs 8,800, Rs 8,200, Rs 7,400, Rs 7,400 and Rs 6,900, so the fourth and fifth tie. Said aloud: each rule
keeps the members whose number is four or less, and whole ties only asks where a tie ends.

```sql
WITH invented (member, spend) AS (
    VALUES ('A', 9100), ('B', 8800), ('C', 8200), ('D', 7400), ('E', 7400), ('F', 6900)
),
r AS (
    SELECT member, spend,
           row_number() OVER (ORDER BY spend DESC, member) AS rn,
           rank()       OVER (ORDER BY spend DESC)         AS rk,
           dense_rank() OVER (ORDER BY spend DESC)         AS dr,
           count(*)     OVER (PARTITION BY spend)          AS tied_with
    FROM   invented
)
SELECT count(*) FILTER (WHERE rn <= 4)                 AS row_number_ships,
       count(*) FILTER (WHERE rk <= 4)                 AS rank_ships,
       count(*) FILTER (WHERE dr <= 4)                 AS dense_rank_ships,
       count(*) FILTER (WHERE rk + tied_with - 1 <= 4) AS whole_ties_only_ships
FROM   r;
```

### Q2. How many members does each rule ship on an invented top four?

Before step 2 runs, how many members does each rule ship, in the order ROW_NUMBER, RANK, DENSE_RANK
and whole ties only?

a) 4, 4, 4 and 4

b) 4, 5, 5 and 3

c) 4, 5, 6 and 3

d) 4, 5, 5 and 5

Then run step 2 and read its one row of four counts against your answer.

## How long is Retail-Core's list under each rule?

This comes up at work whenever a rule tried on a few invented rows has to hold on the real list.

**Step 3, the same four counts on Retail-Core.** Said aloud: the window now restarts in every segment,
and `tied_with` counts members who share a figure inside their own segment.

```sql
WITH q2 AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
),
r AS (
    SELECT segment, customer_id, q2_revenue,
           row_number() OVER (PARTITION BY segment ORDER BY q2_revenue DESC, customer_id) AS rn,
           rank()       OVER (PARTITION BY segment ORDER BY q2_revenue DESC)              AS rk,
           dense_rank() OVER (PARTITION BY segment ORDER BY q2_revenue DESC)              AS dr,
           count(*)     OVER (PARTITION BY segment, q2_revenue)                           AS tied_with
    FROM   q2
)
SELECT count(*) FILTER (WHERE rn <= 50)                 AS row_number_ships,
       count(*) FILTER (WHERE rk <= 50)                 AS rank_ships,
       count(*) FILTER (WHERE dr <= 50)                 AS dense_rank_ships,
       count(*) FILTER (WHERE rk + tied_with - 1 <= 50) AS whole_ties_only_ships
FROM   r
WHERE  segment = 'Retail-Core';
```

### Q3. How many Retail-Core members does DENSE_RANK put on a top fifty, and why?

Before step 3 runs, how many Retail-Core members does DENSE_RANK put on a top fifty, and why?

a) 52, since ties higher up the list each cost it a number

b) 50, since nobody ties at Retail-Core's fiftieth place

c) 51, since one tie inside the list costs it one number

d) 48, since each tie inside the list takes away one member

Then run step 3 and set its four counts beside your answer.

**Step 3, read the members at the line.** The trainer runs blocks `c3_core_line` and `c3_core_ties` of
the same file. The first prints places 46 to 54 of Retail-Core with ROW_NUMBER, RANK and DENSE_RANK side
by side; the second lists each member inside the first fifty who shares a Q2 figure with another
member, with their places. Read both before the next item.

### Q4. Which statement about Retail-Core's fiftieth place holds?

Reading what the two blocks print, which statement about Retail-Core's fiftieth place holds?

a) Two members tie at fiftieth, so RANK ships 51 and ROW_NUMBER drops one by id

b) Nobody ties at fiftieth, so DENSE_RANK ships the same fifty members as RANK

c) Nobody ties at fiftieth, so RANK and ROW_NUMBER ship the same fifty members

d) C-0092 ties with C-0005 at fiftieth, so whole ties only ships forty-nine

## What does the head of Retail-Plus's rule ship, and what goes in the sentence?

This comes up at work whenever a count leaves the team, since the sentence beside it is what its reader
repeats.

**Step 4, the sentence to the head.** The head asked for two things: members who spent the same ranked
the same, and the number that made the list. Nothing runs in this step; you choose the sentence the head
reads beside Retail-Core's list.

### Q5. Which sentence goes to the head of Retail-Plus about Retail-Core's list?

Which sentence goes to the head of Retail-Plus about Retail-Core's list?

a) "Retail-Core's list holds 52 under DENSE_RANK, which keeps every tie together, just as you asked."

b) "Retail-Core's list holds 50 under RANK; nobody ties at fiftieth, where C-0005 booked Rs 2,980."

c) "Retail-Core's list holds 50 under ROW_NUMBER, cut by customer id, so it is the same each run."

d) "Retail-Core's list holds 50 under whole ties only, so no tie anywhere on the list is ever split."

**Your turn, after the build.** Section 3 of `notebooks/C2_W02_D03_03_tie_rule_STUDENT.ipynb` ends on an
empty cell for the head's own segment, Retail-Plus. Run block `c3_retail_plus_rules` there, read the
members around fiftieth place if your four counts differ, and write the same kind of sentence for the
head's list. The TA reads the sentences in the practice lab.

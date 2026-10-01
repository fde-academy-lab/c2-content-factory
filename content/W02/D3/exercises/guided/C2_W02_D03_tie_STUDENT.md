# How do ROW_NUMBER, RANK and DENSE_RANK treat a tie, and what does the head of Retail-Plus's rule ship for Retail-Core, built together on one screen?

You build this one with the trainer in chapter 3, in about fifteen minutes. The trainer types each step on the
projector and says aloud what each function does to the tie; you type the same step in your own
query tab on the warehouse, or run the same block from `sql/C2_W02_D03_03_tie_rule_STUDENT.sql`, and
compare. Steps 1 and 2 run on invented members, labelled invented, so the mechanism fits on one
screen; step 3 runs on Kalpa's Retail-Core members; step 4 applies the head of Retail-Plus's rule.
Answer each item before you run its step.

> "Ties matter. If two members spent the same, I want them ranked the same, and I want to know how
> many made the top fifty, not forty-nine because of a tie."
>
> The head of Retail-Plus, Kalpa Retail

Q2 is July to September 2026, and a member's Q2 revenue is the booked amount of every Q2 order the
member placed, whatever its status. Two members tie when their Q2 revenue is the same to the rupee. A
list "ships" the members whose number is at or inside the line. Chapter 2 cut each segment's list with
`row_number()`, letting the customer id decide between two members who booked the same, and the head
of Retail-Plus is asking whether that is fair. Three window functions number a list: `ROW_NUMBER`,
`RANK` and `DENSE_RANK`. A fourth rule, whole ties only, keeps a tie only when all of it fits inside the
line, using `tied_with = count(*) OVER (PARTITION BY q2_revenue)`, the number of members who share a
figure: a member ships when `rank + tied_with - 1` is at or inside the line. Retail-Core, Kalpa's
everyday shoppers, has 96 Q2 buyers.

**Who needs the answer.** The head of Retail-Plus needs it to defend every count to the tier's members,
and a count you cannot explain in one sentence is one the head cannot defend. You need to say, for any
list, which rule made its count and which members stand at its line.

**The questions on the way.**

- What does DENSE_RANK give the six invented members?
- How many members does each rule ship at an invented line of four?
- How many Retail-Core members does DENSE_RANK put on a top fifty, and why?
- Which statement about Retail-Core's line holds?
- Which sentence goes to the head of Retail-Plus about Retail-Core's list?

**What you post.** One line of five letters in item order, no spaces, in this shape:

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

What you should see: `row_number` 1 to 6, with A ahead of B only because the member name sorts A
first; `rank` gives A and B 1 and skips 2, as a race reports a shared first place; `dense_rank` numbers
the different spend figures and never skips, so by F its number sits two below F's place among the
members.

## How many members does each rule ship at a line?

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

### Q2. How many members does each rule ship at an invented line of four?

Before step 2 runs, how many members does each rule ship, in the order ROW_NUMBER, RANK, DENSE_RANK
and whole ties only?

a) 4, 4, 4 and 4

b) 4, 5, 5 and 3

c) 4, 5, 6 and 3

d) 4, 5, 5 and 5

What you should see: one row reading 4, 5, 5 and 3. ROW_NUMBER keeps D and leaves E off by the name;
RANK keeps both; whole ties only drops both, which is the forty-nine the head of Retail-Plus warned
about, at a line of four.

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

What you should see: 50, 50, 52 and 50.

**Step 3, read the line.** The trainer runs blocks `c3_core_line` and `c3_core_ties` of the same file:
places 46 to 54 with all three functions side by side, then the ties inside the first fifty.

| Place | RANK | DENSE_RANK | Member | Q2 revenue |
|---|---|---|---|---|
| 46 | 46 | 44 | C-0007 | Rs 3,100 |
| 47 | 47 | 45 | C-0127 | Rs 3,030 |
| 48 | 48 | 46 | C-0054 | Rs 3,000 |
| 49 | 49 | 47 | C-0072 | Rs 2,990 |
| 50 | 50 | 48 | C-0005 | Rs 2,980 |
| 51 | 51 | 49 | C-0092 | Rs 2,950 |
| 52 | 52 | 50 | C-0094 | Rs 2,910 |
| 53 | 53 | 51 | C-0048 | Rs 2,870 |
| 54 | 54 | 52 | C-0074 | Rs 2,810 |

Two ties sit inside the first fifty: C-0044 and C-0132 on Rs 4,540 at places 31 and 32, and C-0060 and
C-0121 on Rs 4,120 at places 37 and 38.

### Q4. Which statement about Retail-Core's line holds?

Reading places 46 to 54 and the two ties inside the first fifty, which statement about Retail-Core's
line holds?

a) The two ties inside the list each push RANK one place further on, so RANK ships 52

b) DENSE_RANK's 50 falls on C-0092, the 51st member, so DENSE_RANK ships 51

c) Nobody ties at fiftieth, and DENSE_RANK's 50 falls on C-0094, the 52nd member

d) Nobody ties at fiftieth, so all four rules ship the same fifty members

## What does the head of Retail-Plus's rule ship, and what goes in the sentence?

This comes up at work whenever a count leaves the team, since the sentence beside it is what its reader
repeats.

**Step 4, the head's rule applied.** The head asked for two things: members who spent the same ranked
the same, and the number that made the list. RANK does the first, because tied members share a place
and everyone at or inside the line ships; the second is a sentence in the report, beside the list.
Said aloud: the rule, the count and the members at the line go in one sentence.

### Q5. Which sentence goes to the head of Retail-Plus about Retail-Core's list?

Which sentence goes to the head of Retail-Plus about Retail-Core's list?

a) "Retail-Core's list holds 52 under DENSE_RANK, which keeps every tie together, just as you asked."

b) "Retail-Core's list holds 50 under RANK; nobody ties at fiftieth, where C-0005 booked Rs 2,980."

c) "Retail-Core's list holds 50 under ROW_NUMBER, cut by customer id, so it is the same size on every run."

d) "Retail-Core's list holds 50 under whole ties only, so no tie anywhere on the list is ever split."

**Your turn, after the build.** Section 3 of `notebooks/C2_W02_D03_03_tie_rule_STUDENT.ipynb` ends on an
empty cell for the head's own segment, Retail-Plus. Run block `c3_your_segment` there, read the
members around fiftieth place if your four counts differ, and write the same kind of sentence for the
head's list. The TA reads the sentences in the practice lab.

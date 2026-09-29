# Round 3 set: two quarters as named steps

Seven items, about seven minutes, at the close of round 3. Each is a question the head of
Retail-Plus or the analyst asks about the two-quarter comparison. The blocks in
`sql/C2_W02_D01_03_quarters_STUDENT.sql` check most of them.

Post one line, seven letters in item order, no spaces:

```
Post exactly this shape: xxxxxxx
```

---

### Q1

In `WITH q1 AS (...), q2 AS (...) SELECT ... FROM q1 JOIN q2 USING (segment)`, what can the final
SELECT read?

a) Only q2, the step just before it
b) Only the base tables, since CTEs are temporary
c) Only q1, because q2 was defined after it
d) Both steps, and every table as well

### Q2

The head of Retail-Plus is told spend per member fell 15.5 percent. The member step used
`sum(CASE WHEN quarter = 'Q2' THEN amount END)` and then `avg()`. What went wrong?

a) The CASE counted Q1 orders into the Q2 column
b) Lapsed members became NULL and avg skipped them
c) avg rounded each member's spend before averaging it
d) The CTE ran twice, so each member appears twice

### Q3

The member step holds 107 Retail-Plus members, and `count(q2_spend)` returns 76. How many members
did the hurried Q2 average leave out?

a) 15, the members lost between Q1 and Q2
b) 13, the members who never bought (120 less 107)
c) 31, the members with no Q2 order
d) None, since avg divides by every row

### Q4

After `coalesce`, Retail-Plus spend per member reads Rs 5,474 in Q1 and Rs 3,863 in Q2, a 29.4
percent fall, exactly the segment's revenue fall. Why exactly?

a) Both averages divide by the same 107 members
b) coalesce rounds the averages to the revenue's precision
c) Both numbers come from one CTE, so they must agree
d) It is a coincidence of this quarter's data

### Q5

Anand asks what share of the two quarters' revenue Business carries. Which part of the query needs
a query of its own inside it?

a) The segment label on each output row
b) The GROUP BY that splits revenue by segment
c) The ORDER BY that puts Business first
d) The denominator: the total of both quarters

### Q6

Query 6 shows Retail-Plus customers down 16.5 percent, orders per customer down 22.0 percent and
order value up 8.4 percent. Which branch does the sentence to Anand lead with?

a) Customers, since losing members is worse than losing orders
b) Frequency, the branch that fell furthest
c) Order value, since it is the only branch that rose
d) Revenue, since it is the total the others explain

### Q7

The two-CTE query has to survive the analyst's audit. Which change makes it easier to audit
without changing a single number?

a) Merge q1 and q2 into one subquery to save lines
b) Drop the ORDER BY, since there are only four rows
c) Add a comment on what each step computes
d) Round every column to whole rupees inside each step

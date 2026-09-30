# Round 2 set: per segment and per quarter

Seven items, about seven minutes, at the close of round 2. Each is a question the analyst puts to
the eight-row table. Check any answer you can against a block of
`sql/C2_W02_D01_02_segments_STUDENT.sql`.

Post one line, seven letters in item order, no spaces:

```
Post exactly this shape: xxxxxxx
```

---

### Q1

```sql
SELECT c.segment, o.quarter, count(*)
FROM   orders o JOIN customers c USING (customer_id)
GROUP  BY c.segment, o.quarter;
```

Anand's analyst runs this on the warehouse, where every segment ordered in both quarters. How many
rows come back?

a) 4, one per segment across both quarters
b) 2, one per quarter for all segments
c) 8, one per segment and quarter
d) 1,000, since grouping keeps every order row

### Q2

A colleague's query prints Retail-Core orders per customer as 1 in Q1 and 2 in Q2, and proposes
moving loyalty budget to Retail-Core. What do you check first?

a) Whether the division ran on integers and dropped the fraction
b) Whether Retail-Core gained customers between the two quarters
c) Whether the GROUP BY lists the segment before the quarter
d) Whether the WHERE clause kept only delivered orders

### Q3

Retail-Plus had 140 Q2 orders from 76 customers. What does
`count(*) / count(DISTINCT customer_id)` print for that group?

a) 1.84
b) 2
c) 1.8421
d) 1

### Q4

Anand wants the segment-quarters with fewer than 30 orders flagged, because a rate on so few orders
cannot be trusted. Which clause keeps only those groups?

a) WHERE count(*) < 30
b) HAVING count(*) < 30
c) ORDER BY count(*) LIMIT 30
d) HAVING count(DISTINCT customer_id) < 30

### Q5

The analyst wants the same tree for delivered orders only. Where does `status = 'delivered'`
belong, and why?

a) In HAVING, because it filters the groups Anand reads
b) In SELECT, as a CASE inside every aggregate on the row
c) In WHERE, because it tests a row before any group forms
d) In ORDER BY, so delivered orders sort to the top of each group

### Q6

In the eight-row table, the orders add up to 1,000 and the revenue to Rs 19.84 crore. What does
that sum check prove?

a) No order was lost or doubled by the grouping
b) Every segment's rate is statistically reliable
c) The orders per customer are computed correctly
d) The segments come back in the right order

### Q7

The analyst reads the thin-cell query in the order Postgres runs it. Which order is that, for the
clauses SELECT, WHERE, GROUP BY, HAVING and FROM?

a) SELECT, FROM, WHERE, GROUP BY, HAVING
b) FROM, WHERE, SELECT, GROUP BY, HAVING
c) FROM, GROUP BY, WHERE, HAVING, SELECT
d) FROM, WHERE, GROUP BY, HAVING, SELECT

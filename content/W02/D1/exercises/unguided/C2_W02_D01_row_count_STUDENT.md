# Round 1 set: is the warehouse the book?

Seven items, about seven minutes, at the close of round 1. Every item is a question Anand's analyst
or Kavya would put to you about the first queries. Run a block of
`sql/C2_W02_D01_01_first_queries_STUDENT.sql` whenever an item lets you check your answer.

Post one line, seven letters in item order, no spaces:

```
Post exactly this shape: xxxxxxx
```

---

### Q1

Anand's analyst runs `SELECT count(*) FROM orders WHERE quarter = 'Q2';`. What does the number he
sees count?

a) 227, the customers who bought in Q2
b) 462, the order rows booked in Q2
c) 340, every member on the book
d) 1,000, because WHERE runs after the count

### Q2

The head of Retail-Plus asks how many members bought in Q2. Which aggregate over the Retail-Plus Q2
orders answers her?

a) count(*), since each row is a member's purchase
b) count(customer_id), since every row carries an id
c) count(*) over the Retail-Plus rows of the customers table
d) count(DISTINCT customer_id), each member once

### Q3

`count(DISTINCT customer_id)` over the orders returns 301, and the customers table holds 340 rows.
What is the gap of 39?

a) Members on the book who placed no order in Q1 or Q2
b) Duplicate customer ids that the warehouse load failed to remove
c) Orders whose customer id was left empty by the source system
d) Customers counted twice, once in each quarter

### Q4

Your audit sample of five delivered Q2 app orders, pulled with `LIMIT 5` and no `ORDER BY`, totals
Rs 3,900. After the overnight reload the analyst reruns the same query and gets Rs 4,590. What do
you conclude?

a) The reload changed two amounts, so the book no longer reconciles
b) The analyst edited the query, so he should send you his version
c) Nothing fixed which five came back, so order by order_id first
d) LIMIT samples at random, so either five is a fair audit sample

### Q5

Week 1's extract put Q1 at Rs 1.90 crore; the warehouse says Rs 10.00 crore. Which check tells
Kavya the warehouse tells the story Week 1 defended?

a) The two Q1 totals agree to the rupee
b) The Q1 to Q2 fall agrees, 1.6 percent in both
c) The order counts agree, quarter by quarter
d) None, until Finance reconciles the warehouse by hand again

### Q6

Anand's sheet needs "the typical order" across both quarters. The mean is Rs 1,98,400 and the
median is Rs 2,510. Which goes on the sheet?

a) The mean, because it uses every one of the 1,000 orders
b) The mean after removing the largest orders, to cure the skew
c) Both, averaged, so neither number dominates the sheet
d) The median, with the mean beside it for reconciliation

### Q7

The suite's comment line has to name its reading of revenue. Which reading does the Monday suite
use, and why?

a) Booked, every status, as Week 1 reconciled
b) Delivered, since it is the most conservative total
c) Not cancelled, since returns arrive later anyway
d) Whichever is largest, as long as the label says so

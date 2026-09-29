# Week 2 recap paper

Saturday 17 October 2026 · 120 minutes · 58 items · pen and paper, no assistant, no notes

Name: ____________________    Marked by: ____________________    Items right: ____ of 58

Answer every item in the space it gives you. Each section says how. After the break the papers are swapped and marked against the key, and the discussion starts with the items the room missed most.

---

## A. Fill in the blank (Q1 to Q9)

Write the missing word or number on the line.

#### Q1

WHERE filters rows before they are grouped, and ____ filters the groups after they are formed.

Answer: ____________________

#### Q2

Without ORDER BY, LIMIT 5 returns five rows in an order the database does not ____.

Answer: ____________________

#### Q3

A named query step introduced by the keyword WITH is called a ____.

Answer: ____________________

#### Q4

A LEFT JOIN keeps every row from the ____ table, whether it finds a match or not.

Answer: ____________________

#### Q5

Orders with no payment are found with a LEFT JOIN to payments and a filter where the payment key IS ____.

Answer: ____________________

#### Q6

On the first month of each customer, LAG(spend) returns ____.

Answer: ____________________

#### Q7

The clause that restarts a window calculation for each segment is ____ BY.

Answer: ____________________

#### Q8

In pandas, merge(..., validate='one_to_one') raises a ____ when a key repeats.

Answer: ____________________

#### Q9

pivot_table makes a table wider, and ____ makes it longer.

Answer: ____________________

---

## B. True or false (Q10 to Q17)

Write T or F on the line.

#### Q10

In the logical order of a query, SELECT is evaluated before WHERE.

Answer: ____________________

#### Q11

WHERE COUNT(*) > 5 is valid SQL for filtering groups.

Answer: ____________________

#### Q12

An INNER JOIN between orders and payments silently drops the orders that were never paid.

Answer: ____________________

#### Q13

A join can inflate a SUM while every individual row still looks plausible.

Answer: ____________________

#### Q14

RANK and DENSE_RANK give different results only when there are ties.

Answer: ____________________

#### Q15

A window function can be used directly inside a WHERE clause.

Answer: ____________________

#### Q16

groupby followed by agg returns one row for each group.

Answer: ____________________

#### Q17

A pivot table built on an export that still contains duplicate rows reports the correct total.

Answer: ____________________

---

## C. One correct option (Q18 to Q32)

Circle the one correct letter.

#### Q18

Which clause runs first in the logical order of a query?

a) SELECT
b) FROM
c) WHERE
d) ORDER BY

#### Q19

A query fails with: column "segment" must appear in the GROUP BY clause or be used in an aggregate function. What fixes it?

a) Add segment to GROUP BY, or wrap it in an aggregate.
b) Move the WHERE filter into a HAVING clause after GROUP BY.
c) Add LIMIT 1 so that only one segment returns.
d) Add ORDER BY segment at the end of the query.

#### Q20

Why should Finance's Monday number be computed in the warehouse and not in a notebook?

a) The warehouse hides the raw data from Finance, which keeps the number from being disputed.
b) A notebook cannot hold a full quarter of orders, so its totals are always approximate.
c) SQL is faster than Python on every task, so the number arrives sooner each Monday.
d) The query runs unchanged each week against the source, and every line can be audited.

#### Q21

Which join returns only the orders that have at least one payment?

a) LEFT JOIN
b) FULL OUTER JOIN
c) INNER JOIN
d) CROSS JOIN

#### Q22

After a LEFT JOIN from orders to payments, the row count rose from 1,000 to 1,050. What is the likeliest cause?

a) The payments table is empty.
b) Some orders have no payment.
c) The join kept the unpaid orders as extra rows.
d) Some orders have more than one payment row.

#### Q23

Which query lists the orders that were paid twice?

a) SELECT order_id FROM payments GROUP BY order_id HAVING COUNT(*) > 1
b) SELECT DISTINCT order_id FROM payments
c) SELECT order_id FROM payments ORDER BY order_id
d) SELECT order_id FROM payments WHERE COUNT(order_id) > 1 GROUP BY order_id

#### Q24

Collected revenue doubled after a join and every row looks fine. What is the first check?

a) Rerun the query at a quieter hour, in case the warehouse returned a partial result.
b) Round the amounts to whole rupees, because decimals accumulate across many rows.
c) Switch to an INNER JOIN, because a LEFT JOIN is what creates the extra rows.
d) Compare the row count before and after the join, and count payments per order.

#### Q25

Revenue values are 900, 850, 850 and 700. What does RANK() return in descending order?

a) 1, 2, 3, 4
b) 1, 2, 2, 3
c) 1, 2, 2, 4
d) 1, 1, 2, 3

#### Q26

For the same four values, what does DENSE_RANK() return?

a) 1, 2, 3, 4
b) 1, 2, 2, 3
c) 1, 2, 2, 4
d) 1, 1, 2, 3

#### Q27

Marketing wants the top three customers in each segment. Which approach answers it?

a) GROUP BY segment with LIMIT 3, because the limit is applied to each group in turn.
b) A window function ranked within PARTITION BY segment, filtered in an outer query.
c) ORDER BY revenue DESC with LIMIT 3, run once, since it returns the top of each segment.
d) HAVING COUNT(*) <= 3, because HAVING keeps only the three largest rows in a group.

#### Q28

A running total changes between two runs of the same query. What is the likeliest cause?

a) The ORDER BY inside the window has ties, so the row order is ambiguous.
b) The partition is too large, so the database samples the rows it adds.
c) The database cached an old result and served it for one of the runs.
d) SUM is approximate for large partitions, so its result drifts slightly.

#### Q29

Which sentence describes groupby correctly?

a) It sorts the rows by key, and then returns the first row of every key as the group's result.
b) It joins two tables on a key, and then keeps one row for every match.
c) It splits rows by key, applies a computation to each group and combines the results.
d) It removes duplicate keys, and then counts how many rows were removed.

#### Q30

A merge of 1,000 customers with the campaign exposure table returns 1,120 rows. What happened?

a) 120 customers had no exposure record, so pandas added an empty row for each of them.
b) Some customer keys repeat in the exposure table, so those customers were multiplied.
c) pandas appended its index as extra rows, which happens whenever how='left' is used.
d) The key columns had different names, so pandas fell back to matching on row position.

#### Q31

XLOOKUP returned a member's details for an id that does not exist. Which setting was wrong?

a) The return array was one row shorter than the lookup array it pairs with.
b) The lookup array was sorted in ascending order before the formula ran.
c) The sheet was protected, so the formula returned the last cached result.
d) The match mode asked for a nearest match when it should have been exact.

#### Q32

Which of these jobs belongs in Excel?

a) Letting a director slice a clean customer table and watch one number recalculate.
b) Joining payments to orders to find the orders that were never paid.
c) Computing the source-of-truth revenue figure that Finance will check its own books against.
d) De-duplicating the orders export before anyone computes revenue from it.

---

## D. More than one correct (Q33 to Q39)

Circle every correct letter.

#### Q33

Which statements about WHERE and HAVING are correct? Mark every correct option.

a) WHERE filters rows before grouping.
b) HAVING filters groups after aggregation.
c) HAVING can use COUNT(*).
d) WHERE can use COUNT(*).

#### Q34

A LEFT JOIN from 1,000 orders to payments returns 1,050 rows. Which checks belong in the validation? Mark every correct option.

a) the row count before and after the join
b) payments per order, with GROUP BY and HAVING COUNT(*) > 1
c) booked revenue before and after the join
d) the font of the report

#### Q35

Which rows can appear in a FULL OUTER JOIN of orders and payments and never in an INNER JOIN? Mark every correct option.

a) orders with no payment
b) payments with no order
c) orders with exactly one payment
d) orders with two payments

#### Q36

Which questions need a window function, because GROUP BY alone cannot answer them? Mark every correct option.

a) each customer's rank within a segment
b) total revenue per segment
c) each month's spend beside the same customer's previous month
d) a running total by date with every row kept

#### Q37

The head of Retail-Plus wants ties ranked the same and wants to know how many members made the top fifty. Which statements are true? Mark every correct option.

a) ROW_NUMBER breaks ties arbitrarily, so it does not meet the ask.
b) RANK gives tied members the same rank.
c) With RANK, a tie at position fifty can ship fifty-one rows.
d) ROW_NUMBER always ships more than fifty rows.

#### Q38

Which statements about pandas merge are true? Mark every correct option.

a) It is the pandas form of a SQL join.
b) validate= can make a fan-out fail loudly.
c) It always keeps the row count of the left table.
d) Checking the row count before and after is still worth doing.

#### Q39

A front-page number is misread unless it carries which of these? Mark every correct option.

a) its denominator
b) its period
c) its comparison
d) its cell colour

---

## E. Scenario set (Q40 to Q51)

Each set opens on one Kalpa situation. Answer each item the way it asks: circle a letter, write T or F, or write the number or the word.

### Set 1

**Situation.** The warehouse holds 1,000 Q2 orders. 920 orders have one payment row. 50 orders have two payment rows, because the gateway retried and recorded the same payment a second time. 30 delivered orders have no payment row.

#### Q40

A LEFT JOIN from orders to payments returns ____ rows.

Answer: ____________________

#### Q41

An INNER JOIN returns ____ rows.

Answer: ____________________

#### Q42

Anand asks for the unpaid orders. Which pattern finds them?

a) LEFT JOIN, then WHERE payments.order_id IS NULL
b) INNER JOIN, then WHERE payments.amount_paid IS NULL
c) GROUP BY order_id HAVING COUNT(*) > 1
d) ORDER BY paid_at

#### Q43

True or false: SUM(amount_paid) over the payments table overstates what was collected, because each retried payment is counted twice.

Answer: ____________________

### Set 2

**Situation.** Q2 revenue in Rs thousand for six Retail-Plus members: A 900, B 850, C 850, D 700, E 700, F 650. Ranks run from the highest revenue down.

#### Q44

Under RANK(), member D gets rank ____.

Answer: ____________________

#### Q45

Under DENSE_RANK(), member F gets rank ____.

Answer: ____________________

#### Q46

With DENSE_RANK(), how many members does WHERE dense_rnk <= 3 return?

a) 3
b) 4
c) 5
d) 6

#### Q47

Marketing wants exactly four members. Which function returns exactly four rows, and at what cost?

a) RANK, at no cost, because every rank above four is simply filtered out by the WHERE.
b) DENSE_RANK, at no cost, because it never leaves a gap in the ranks.
c) ROW_NUMBER, and the D-E tie is broken arbitrarily unless a tiebreaker is named.
d) LAG, at the cost of losing the first row of every partition.

### Set 3

**Situation.** Marketing's customer table has 1,000 rows. The campaign exposure table lists the same 1,000 customers, and 60 of them appear twice. An analyst merges the two on customer_id with how='left' and sends the result to Excel, where a pivot sums revenue.

#### Q48

The merged table holds ____ rows.

Answer: ____________________

#### Q49

What would validate='one_to_one' have done?

a) Removed the repeated keys silently and kept the first of each.
b) Nothing, because validate applies only to inner merges.
c) Sorted both tables by key so that the rows lined up.
d) Raised a MergeError before any number was produced.

#### Q50

True or false: The pivot's revenue total will be higher than the warehouse figure.

Answer: ____________________

#### Q51

Where does the fix belong?

a) In the pivot: type the warehouse total over the pivot's own total before the file is shared.
b) In the merge: de-duplicate the exposure table on a stated rule and validate the keys.
c) In the chart: plot revenue per customer, which is unaffected by the repeated rows.
d) Nowhere: a gap of this size is rounding, and the pivot can be shared as it stands.

---

## F. Applied maths (Q52 to Q56)

Show the working, then the answer.

#### Q52

A table has 4 segments and 2 quarters, and every combination has orders. How many rows does GROUP BY segment, quarter return?

Working:

Answer: ____________________

#### Q53

Every Q2 order was paid in full once, which makes Rs 20 lakh collected. Fifty payments of Rs 2,000 each were then recorded a second time by the gateway. What does a plain SUM of the payments table report?

Working:

Answer: ____________________

#### Q54

Two members tie exactly at position fifty and nobody else ties. How many rows does WHERE rnk <= 50 return under RANK(), and how many under ROW_NUMBER()?

Working:

Answer: ____________________

#### Q55

A member's monthly spend is Rs 5,000, then Rs 4,200, then Rs 3,900. Using LAG, give the two month-on-month changes and say whether the 'fell two months running' flag fires.

Working:

Answer: ____________________

#### Q56

1,000 orders belong to 400 customers. How many rows does the one-row-per-customer table hold, and what is the mean frequency?

Working:

Answer: ____________________

---

## G. Order the steps (Q57 to Q58)

Write the letters in the right order.

#### Q57

Put the clauses in their logical execution order.

a) SELECT
b) WHERE
c) FROM
d) ORDER BY
e) GROUP BY
f) HAVING

Order: ____________________

#### Q58

Put the week's tools in the order a number travels to the leadership deck.

a) Excel presents it and lets a director explore.
b) The warehouse computes the source of truth.
c) pandas carries the analyst's iteration.

Order: ____________________

# Does the Monday suite hold on Anand's definition, the orders that were delivered?

The escalated case, alone, in five parts. Parts 1 and 2 run in the afternoon, 20 minutes; parts 3 to
5 run in the practice lab. You work in `notebooks/C2_W02_D01_ex1_escalated_case_STUDENT.ipynb`, and
this brief carries everything the case needs, so it can be read with nothing else open. Items 1 to 10
are the notebook's ten lettered markers, with the same numbers and the same letters. Items 11 to 15
are this brief's own design items, one at the end of each part, answered here.

> "Finance counts the orders that reached the customer and stayed there. Run me the same suite on
> delivered orders, and tell me whether the story changes."
>
> Anand Iyer, finance controller, Kalpa Retail

The chapters built the Monday suite on booked revenue, every order at its amount whatever its status:
Rs 10,00,00,000 in Q1 (April to June 2026) and Rs 9,84,00,000 in Q2 (July to September 2026), 244
then 227 customers who bought, and Retail-Plus, Kalpa's paid membership tier, carrying the fall with
its revenue down 29.4 percent. Finance counts only delivered orders, the orders whose status is
delivered; cancelled and returned orders are not revenue on Anand's books. This case reruns the suite
on that definition, so its numbers are new and nothing from the chapters can be copied.

The book is Kalpa's Postgres warehouse. The segment lives on the customers table, and each order looks
it up with one line, `JOIN customers c USING (customer_id)`, which finds the order's one customer and
changes no row count. Kavya Nair, the team's senior analyst, flags on the sheet any rate that stands on
fewer than 30 customers. Customers who took delivery are counted once in a window, however many
delivered orders they received. Orders per customer is orders divided by those customers, and the
analyst multiplies every one of them back to its orders. The revenue tree splits revenue into
customers, orders per customer and revenue per order, which multiply back to it. Spend per member is
the rupees a member spent in a quarter, averaged over the tier's members. A fingerprint is a block of
numbers describing the book, printed beside the results so a reader can tell a changed book from a
changed query. The ERP is the system Finance books orders in.

| Table | Rows | Columns |
|---|---|---|
| orders | 1,000, one per order | order_id, customer_id, order_date, quarter, channel, amount, status |
| customers | 340, one per member | customer_id, segment, city, country, joined_date |

| Status on the book | Orders | Rupees |
|---|---|---|
| delivered | 653 | Rs 13,45,90,290 |
| returned | 184 | Rs 3,80,55,960 |
| cancelled | 163 | Rs 2,57,53,750 |
| The book | 1,000 | Rs 19,84,00,000 |

| Segment | Members on the customers table |
|---|---|
| Business, corporate buyers whose orders are worth lakhs | 40 |
| Retail-Core, everyday shoppers | 150 |
| Retail-Plus, the paid membership tier | 120 |
| Student | 30 |

**Who needs the answer.** Anand signs delivered revenue, and the head of Retail-Plus is deciding, on
the booked story, how hard to work to keep members. If the story changes on Finance's definition and
the sheet does not say so, her retention plan rests on orders that were returned or cancelled.

**The questions on the way.**

- What does the book say on Anand's definition?
- Which segment's frequency fell on delivered orders, and which groups are too thin?
- Which branch of Retail-Plus's tree moved furthest, and how much less did each member spend?
- Does the suite add up the way the analyst will add it?
- Will the analyst's rerun draw the same sample, and what does the run print beside it?

**What you post.** One line of fifteen letters in item order, no spaces, items 1 to 10 from the
notebook's markers and items 11 to 15 from this brief, in this shape:

```
Post exactly this shape: xxxxxxxxxxxxxxx
```

Beside the letters, post the three numbers the notebook asks for: Q2's delivered revenue, Retail-Plus's
Q2 orders per customer, and Retail-Plus's half-year customers.

---

## Part 1. What does the book say on Anand's definition?

Used at work whenever a finance number is built, since the filter that states the definition of
revenue is the first line an auditor reads.

In the afternoon, about 10 minutes: markers 1 and 2 in the notebook, then item 11 here.

### Q1. Which filter keeps the orders that reached the customer and stayed there?

Anand's books count the orders that reached the customer and stayed there. Which filter keeps exactly
those orders?

a) `WHERE status <> 'cancelled'`
b) `WHERE status IN ('delivered', 'returned')`
c) `HAVING status = 'delivered'`
d) `WHERE status = 'delivered'`

### Q2. Which expression counts the customers who took delivery in a quarter, each once?

Anand's customer line counts the customers who took delivery in a quarter, each once. Which expression
counts them?

a) `count(DISTINCT customer_id)`, one per customer id however many rows it has
b) `count(*)`, since each delivered row belongs to a customer who took delivery
c) `count(customer_id)`, since it counts the customer column rather than the rows
d) `sum(1)`, since adding one per delivered order counts everyone who received one

### Q11. How should the sheet set delivered revenue beside booked revenue, sized in queries and rows?

Anand asked whether the story changes, so his sheet will carry booked and delivered revenue for each
quarter side by side. Which way fits, sized in queries and rows?

a) Two queries, one per definition, whose two results of 2 rows the analyst lines up by hand
b) One query grouped by quarter with booked and delivered revenue as two columns, 2 rows
c) One query grouped by quarter and status, 6 rows, which the analyst adds up into the two definitions
d) The delivered query alone, 2 rows, since delivered revenue is the only one Finance signs

## Part 2. Which segment's frequency fell on delivered orders, and which groups are too thin?

Used at work whenever a business head reads a per-segment rate first, and a rate on too few customers
is the line most likely to mislead them.

In the afternoon, about 10 minutes: markers 3 to 5 in the notebook, then item 12 here.

### Q3. Which grouping gives Anand's sheet one line per segment and quarter?

Anand's sheet carries one line per segment and quarter. Which grouping gives the analyst exactly those
lines?

a) `GROUP BY o.quarter`, with the segment read from each quarter's rows
b) `GROUP BY c.segment`, with each quarter shown inside the segment's row
c) `GROUP BY c.segment, o.quarter`, one group per segment in each quarter
d) `GROUP BY o.customer_id`, so each customer's segment and quarter come through

### Q4. Which orders-per-customer figure survives the analyst's multiply-back check?

The analyst multiplies every orders-per-customer figure back to its orders before she reads it. Which
expression gives a figure that survives her check?

a) `round(count(*) / count(DISTINCT o.customer_id), 2)`
b) `round(count(*)::numeric / count(DISTINCT o.customer_id), 2)`
c) `count(*) / count(DISTINCT o.customer_id)`
d) `round(count(DISTINCT o.customer_id)::numeric / count(*), 2)`

### Q5. Which clause lists the segment-quarters Kavya flags as too thin?

Kavya flags any rate that stands on fewer than 30 customers. Which clause lists the segment-quarters to
flag?

a) `WHERE count(DISTINCT o.customer_id) < 30`, since WHERE decides which lines come back
b) `HAVING count(*) < 30`, since a thin group is one with few orders
c) `WHERE o.customer_id < 30`, which drops rows before the groups are counted
d) `HAVING count(DISTINCT o.customer_id) < 30`, since the bar is on customers per group

### Q12. How should the thin flag reach the sheet, sized in rows?

On delivered orders the eight segment-quarters stand on these customers, Q1 then Q2: Business 30 and
26, Retail-Core 86 and 73, Retail-Plus 77 and 57, Student 12 and 17. The sheet shows all eight lines.
Which way should the flag reach it, sized in rows?

a) A HAVING query that lists the thin groups on their own, three rows the analyst matches to the sheet by hand
b) A HAVING query that keeps only the groups with 30 or more customers, five rows, so no thin rate reaches the sheet
c) A flag column in the same eight rows, true where a group has fewer than 30 customers
d) A flag on the groups with fewer than 30 orders, which catches Student's two quarters and no other group

## Part 3. Which branch of Retail-Plus's tree moved furthest, and how much less did each member spend?

Used at work whenever the head of a customer tier asks what each member is worth now against last
quarter.

In the practice lab: markers 6 and 7 in the notebook, then item 13 here. The notebook builds a table
with one row per Retail-Plus member who took delivery in the half-year, holding each member's
`q1_spend` and `q2_spend`; a member with no delivered order in a quarter has NULL, an empty
value, for that quarter.

### Q6. Which expression gives the average member's Q2 spend over the same members as Q1's?

The head of Retail-Plus wants each member's average Q2 spend over the same members as Q1's, so the two
quarters compare like for like. Which expression gives it?

a) `avg(coalesce(q2_spend, 0))`
b) `avg(q2_spend)`
c) `sum(q2_spend) / count(q2_spend)`
d) `max(q2_spend)`

### Q7. Which pair of counts shows who is inside each quarter's average?

Kavya wants the sheet to show who is inside each quarter's average, so a reader can see both quarters
cover the same members. Which pair of counts shows it?

a) `sum(q1_spend)` and `sum(q2_spend)`
b) `count(DISTINCT q1_spend)` and `count(DISTINCT q2_spend)`
c) `count(q1_spend)` and `count(q2_spend)` beside `count(*)`
d) `avg(q1_spend)` and `avg(q2_spend)`

### Q13. Does the story change for Retail-Plus on delivered orders?

On booked orders, Retail-Plus's branches as Q2 over Q1 were customers 0.835, orders per customer 0.780
and revenue per order 1.084, with revenue at 0.706. On delivered orders the notebook prints 0.740,
0.835 and 1.049, with revenue at 0.648. Anand asked whether the story changes. Which line answers him
for Retail-Plus?

a) It holds: members ordering less often is still the branch that fell furthest, on both definitions
b) It shifts: on delivered orders fewer members buying is the larger fall, 0.740 against 0.835
c) It holds: revenue falls by 29 to 35 percent on either definition, the same story told twice
d) It reverses: revenue per order rose on both, so Retail-Plus is spending more where it counts

## Part 4. Does the suite add up the way the analyst will add it?

Used at work whenever a report shows a total beside its parts, since someone adds them before
believing it.

In the practice lab: marker 8 in the notebook, then item 14 here.

### Q8. Which count gives each segment's half-year customers on delivered orders?

The analyst checks that no segment's half-year customers exceed its members. Which count gives each
segment's half-year customers on delivered orders?

a) The segment's two quarter counts added together, one for Q1 and one for Q2
b) `count(DISTINCT o.customer_id)` over both quarters' delivered orders
c) The larger of the segment's two quarter counts, since most Q2 buyers also bought in Q1
d) `count(*)` over both quarters' delivered orders for the segment

### Q14. Which fact would let the analyst add Business's two quarter counts for its half-year?

Business took delivery from 30 customers in Q1 and 26 in Q2. Which fact, if it held, would let the
analyst add the two counts for Business's half-year?

a) No Business customer took delivery in both quarters
b) Both counts sit at or under Kavya's bar of 30 customers
c) The two quarters share no days, so the two counts cannot overlap
d) The analyst needs only Business's orders and rupees for the half-year

## Part 5. Will the analyst's rerun draw the same sample, and what does the run print beside it?

Used at work whenever an auditor traces a sample from a report back to the system Finance books
orders in.

In the practice lab: markers 9 and 10 in the notebook, then item 15 here. The analyst traces five
delivered Q2 web orders against the ERP every Monday, and reruns the query after the platform's
overnight reload, which rewrites rows of the book with the values they already had.

### Q9. Which ordering makes the five delivered Q2 web orders the same five on every run?

Which ordering, placed before `LIMIT 5`, makes the analyst's five delivered Q2 web orders the same five
on every run?

a) `ORDER BY customer_id`
b) no ORDER BY, only `LIMIT 5`
c) `ORDER BY quarter`
d) `ORDER BY order_id`

### Q10. What should the fingerprint printed beside the delivered suite hold?

Which numbers should the fingerprint printed beside the delivered suite hold?

a) The delivered book's rows, rupees and distinct customers
b) The count of order rows alone, the one number every reload changes
c) The time the query took to run, so a slow run stands out on the sheet
d) The date the suite was run, so each Monday's output carries its label

### Q15. Which route confirms the delivered book's rupees without reusing the delivered filter?

The delivered book's rupees come to Rs 13,45,90,290. The status table at the top of this brief gives
the book's rupees and the returned and cancelled rupees. Which route confirms the delivered rupees without
reusing the delivered filter?

a) Rerun the delivered fingerprint query and set the two results side by side
b) Add part 1's two quarters of delivered revenue, Rs 6,80,25,200 and Rs 6,65,65,090
c) The book's rupees less the returned and the cancelled rupees
d) Multiply the 653 delivered rows by the delivered book's revenue per order

## Which rules does the case keep?

- The data is the warehouse's orders and customers tables, read where they live; nothing is exported.
- Every customer count in your answer is a count of customers who took delivery, each once in its
  window, and every ratio goes on the sheet with its two counts beside it.
- A rate on fewer than 30 customers goes on the sheet with its flag.
- The support TA answers environment problems only.
- The debrief in the practice lab replays the room's wrong answers from all five parts, so post your
  letters before it starts.

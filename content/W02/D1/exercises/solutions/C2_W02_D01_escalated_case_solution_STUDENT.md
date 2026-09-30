# Which answers hold in the escalated case on the Monday suite over delivered orders, and why?

Answers: 1d 2a 3c 4b 5d 6a 7c 8b 9d 10a 11b 12c 13b 14a 15c

Anand Iyer, Kalpa Retail's finance controller, counts only the orders that reached the customer and
stayed there, and he asked for the Monday suite on that definition and whether the story changes. The
case asks each learner to rebuild the suite alone in five parts: items 1 to 10 are the ten markers of
`notebooks/C2_W02_D01_ex1_escalated_case_STUDENT.ipynb`, and items 11 to 15 are the brief's design
items, one per part. The executed solution, `C2_W02_D01_ex1_escalated_case_solution_STUDENT.ipynb` in
this folder, runs every marker. Five of the fifteen items are design items: 11 to 15.

**Who needs the answer.** You, before the debrief, checking your fifteen letters and your three
numbers. The debrief replays the room's wrong answers aloud, and a line you cannot defend here is the
one Anand's analyst sends back.

**The questions on the way.**

- Which idea does this case test?
- Which numbers should you have reached, part by part?
- Why is each key right, item by item?
- Which wrong answers does the debrief replay?
- Where does this show up at work?

## Which idea does this case test?

The case tests the whole day on a definition nobody has run yet. A revenue definition is a row filter
that runs before anything is grouped; every customer count names what it counts; every ratio is
divided in numeric and multiplied back; an average says who is inside it; a wider window counts its
customers again from the orders; and a sample is drawn in an order the rerun will repeat, beside a
fingerprint of the book it read. The design items ask how the sheet sets two definitions side by side,
how a thin flag reaches it, whether the tree's story changes, when two counts may be added, and how
to confirm a fingerprint by a route that avoids the filter it checks.

## Which numbers should you have reached, part by part?

| Part | Number | What it means |
|---|---|---|
| 1 | Delivered revenue Rs 6,80,25,200 in Q1 and Rs 6,65,65,090 in Q2, down 2.1 percent, from 355 then 298 orders; 205 then 173 customers who took delivery, down 15.6 percent | The revenue fall is a little deeper on Finance's definition, and the customer fall is more than twice the booked book's 7.0 percent. |
| 2 | Orders per customer, Q1 then Q2: Business 1.90 then 2.08, Retail-Core 1.57 then 1.74, Retail-Plus 1.87 then 1.56, Student 1.58 then 1.65; flagged thin: Business Q2 on 26 customers, Student Q1 on 12 and Q2 on 17 | Retail-Plus is the one segment whose customers ordered less often, and Business's Q2 rate goes on the sheet flagged. |
| 3 | Retail-Plus branches: customers 0.740, orders per customer 0.835, revenue per order 1.049, revenue 0.648; spend per member over the 93 who took delivery, with 77 of them buying in Q1 and 57 in Q2: Rs 4,356 then Rs 2,823, down 35.2 percent | On delivered orders, fewer members taking delivery is the larger branch of the fall. |
| 4 | Half-year customers on delivered orders: Business 36, Retail-Core 116, Retail-Plus 93, Student 23; adding the quarters would say Retail-Plus 134, since 41 members took delivery in both | Counted from the orders, no segment's half-year exceeds its members. |
| 5 | Five delivered Q2 web orders by order id: KR-00539 Rs 850, KR-00541 Rs 1,160, KR-00550 Rs 1,480, KR-00551 Rs 1,500 and KR-00552 Rs 880, Rs 5,870 in all; the delivered book's fingerprint: 653 rows, Rs 13,45,90,290, 268 customers | The same five come back after the reload, beside a fingerprint that says the delivered book did not move. |

The three numbers to post beside the letters are Q2's delivered revenue, Rs 6,65,65,090; Retail-Plus's
Q2 orders per customer, 1.56; and Retail-Plus's half-year customers, 93.

## Why is each key right, item by item?

### Q1. Which filter keeps the orders that reached the customer and stayed there?

Kind: choose the definition. The key is d, `WHERE status = 'delivered'`. A delivered order reached the
customer and stayed; the filter removes the other statuses row by row, before any group forms.

- a, `WHERE status <> 'cancelled'`: keeps the 184 returned orders, whose money went back.
- b, `WHERE status IN ('delivered', 'returned')`: counts a return as revenue.
- c, `HAVING status = 'delivered'`: HAVING judges groups after they form, and status belongs to a
  single order, so the filter has to act on rows.

### Q2. Which expression counts the customers who took delivery in a quarter, each once?

Kind: choose the count. The key is a, "`count(DISTINCT customer_id)`, one per customer id however many
rows it has". It gives 205 in Q1 and 173 in Q2, where the delivered orders number 355 and 298.

- b, "`count(*)`, since each delivered row belongs to a customer who took delivery": counts rows, 355
  and 298, so a customer with three deliveries counts three times.
- c, "`count(customer_id)`, since it counts the customer column rather than the rows": counts the rows
  whose customer id is filled in, which is every row again.
- d, "`sum(1)`, since adding one per delivered order counts everyone who received one": adds one per
  row, the same 355 and 298.

### Q11. How should the sheet set delivered revenue beside booked revenue, sized in queries and rows?

Kind: a design item, the best-fit way sized in queries and rows. The key is b, "One query grouped by
quarter with booked and delivered revenue as two columns, 2 rows". One pass puts Rs 10,00,00,000
beside Rs 6,80,25,200 for Q1 and Rs 9,84,00,000 beside Rs 6,65,65,090 for Q2, on the same row, for
example with `sum(amount)` and `sum(CASE WHEN status = 'delivered' THEN amount END)`, so the reader
compares the two definitions without moving between results.

- a, "Two queries, one per definition, whose two results of 2 rows the analyst lines up by hand":
  right numbers, and the lining up by hand is the step Anand ruled out.
- c, "One query grouped by quarter and status, 6 rows, which the analyst adds up into the two
  definitions": the delivered rows are there, and booked revenue has to be added by hand from three
  rows per quarter.
- d, "The delivered query alone, 2 rows, since delivered revenue is the only one Finance signs": Anand
  asked whether the story changes, which needs the booked number beside it.

### Q3. Which grouping gives Anand's sheet one line per segment and quarter?

Kind: choose the grouping. The key is c, "`GROUP BY c.segment, o.quarter`, one group per segment in
each quarter": eight groups, the eight lines of the sheet.

- a, "`GROUP BY o.quarter`, with the segment read from each quarter's rows": a quarter's row holds four
  segments, so the database has no single segment to print for it.
- b, "`GROUP BY c.segment`, with each quarter shown inside the segment's row": merges Q1 and Q2, so no
  change can be read.
- d, "`GROUP BY o.customer_id`, so each customer's segment and quarter come through": makes 268
  groups, one per customer, where the sheet wants eight, and a customer who took delivery in both
  quarters has no single quarter to print.

### Q4. Which orders-per-customer figure survives the analyst's multiply-back check?

Kind: fix the logic. The key is b, `round(count(*)::numeric / count(DISTINCT o.customer_id), 2)`.
Dividing in numeric keeps the decimals: Retail-Plus 144 over 77 is 1.87 and 89 over 57 is 1.56, and
1.56 times 57 is 88.9, within half an order of 89.

- a, `round(count(*) / count(DISTINCT o.customer_id), 2)`: the division of two whole numbers has
  already dropped the remainder before round sees it, so Retail-Plus reads 1.00 in both quarters.
- c, `count(*) / count(DISTINCT o.customer_id)`: the same whole-number division with no rounding at
  all.
- d, `round(count(DISTINCT o.customer_id)::numeric / count(*), 2)`: customers per order, the branch
  upside down.

### Q5. Which clause lists the segment-quarters Kavya flags as too thin?

Kind: choose the clause. The key is d, "`HAVING count(DISTINCT o.customer_id) < 30`, since the bar is
on customers per group". HAVING keeps whole groups after they form, and the bar counts customers, so it
returns Business Q2 on 26, Student Q1 on 12 and Student Q2 on 17.

- a, "`WHERE count(DISTINCT o.customer_id) < 30`, since WHERE decides which lines come back": WHERE
  runs before any group exists, so it has no count per group to test.
- b, "`HAVING count(*) < 30`, since a thin group is one with few orders": counts orders, flags Student
  Q1 (19) and Q2 (28), and misses Business Q2's 26 customers behind 54 orders.
- c, "`WHERE o.customer_id < 30`, which drops rows before the groups are counted": compares a customer
  id with a number, which says nothing about how many customers stand behind a group.

### Q12. How should the thin flag reach the sheet, sized in rows?

Kind: a design item, the best-fit way sized in rows. The key is c, "A flag column in the same eight
rows, true where a group has fewer than 30 customers". Each line carries its own flag, so the three
thin groups are marked where the reader meets their numbers, and no line is hidden.

- a, "A HAVING query that lists the thin groups on their own, three rows the analyst matches to the
  sheet by hand": right groups, and a second result to match by hand is how a flag lands on the wrong
  line.
- b, "A HAVING query that keeps only the groups with 30 or more customers, five rows, so no thin rate
  reaches the sheet": drops Business Q2, which books most of the quarter's delivered rupees; a thin
  rate is flagged, never hidden.
- d, "A flag on the groups with fewer than 30 orders, which catches Student's two quarters and no other
  group": counts orders, so Business Q2's 26 customers go unflagged.

### Q6. Which expression gives the average member's Q2 spend over the same members as Q1's?

Kind: choose the average. The key is a, `avg(coalesce(q2_spend, 0))`. A member with no delivered Q2
order spent Rs 0 in Q2, written in on purpose, so both quarters average over the same 93 members:
Rs 4,356 then Rs 2,823, down 35.2 percent, the same change as the tier's delivered revenue.

- b, `avg(q2_spend)`: averages only the 57 members who took delivery in Q2, Rs 4,607, against Q1's 77,
  Rs 5,261, two different groups.
- c, `sum(q2_spend) / count(q2_spend)`: the same average over the same 57, written out by hand.
- d, `max(q2_spend)`: one member's spend, the largest, which is no average at all.

### Q7. Which pair of counts shows who is inside each quarter's average?

Kind: choose the check. The key is c, `count(q1_spend)` and `count(q2_spend)` beside `count(*)`. They
read 77 and 57 beside 93, which shows a plain average would cover two different groups; after the zero
is written in, both averages cover all 93.

- a, `sum(q1_spend)` and `sum(q2_spend)`: rupees, which say nothing about who is inside.
- b, `count(DISTINCT q1_spend)` and `count(DISTINCT q2_spend)`: counts different spend values, 73 and
  54, so two members who spent the same amount count once.
- d, `avg(q1_spend)` and `avg(q2_spend)`: the averages themselves, with nothing to say whom they
  cover.

### Q13. Does the story change for Retail-Plus on delivered orders?

Kind: a design item that combines the two definitions' trees. The key is b, "It shifts: on delivered
orders fewer members buying is the larger fall, 0.740 against 0.835". On booked orders, members
ordering less often led (0.780 against 0.835 for customers); on delivered orders, 26.0 percent fewer
members took delivery and each did so 16.5 percent less often, and revenue fell 35.2 percent. The
line to Anand says the story shifts toward members who stopped taking delivery.

- a, "It holds: members ordering less often is still the branch that fell furthest, on both
  definitions": on delivered orders the customer branch, 0.740, fell further than frequency, 0.835.
- c, "It holds: revenue falls by 29 to 35 percent on either definition, the same story told twice":
  the revenue ratio matches in direction, and the branch that carries it changed.
- d, "It reverses: revenue per order rose on both, so Retail-Plus is spending more where it counts":
  a larger basket on fewer members and fewer orders still leaves revenue down by a third.

### Q8. Which count gives each segment's half-year customers on delivered orders?

Kind: choose the count. The key is b, `count(DISTINCT o.customer_id)` over both quarters' delivered
orders. Counted from the orders, Business has 36, Retail-Core 116, Retail-Plus 93 and Student 23, each
within its members.

- a, "The segment's two quarter counts added together, one for Q1 and one for Q2": counts every
  member who took delivery in both quarters twice; Retail-Plus would read 134.
- c, "The larger of the segment's two quarter counts, since most Q2 buyers also bought in Q1": misses
  everyone who took delivery only in the smaller quarter; Retail-Plus would read 77.
- d, "`count(*)` over both quarters' delivered orders for the segment": counts orders, 233 for
  Retail-Plus, which is more than the tier's 120 members.

### Q14. Which fact would let the analyst add Business's two quarter counts for its half-year?

Kind: a design item, the fact that would switch the method. The key is a, "No Business customer took
delivery in both quarters". Adding double-counts exactly the customers in both quarters, so with none
the sum would be exact. On the book, 20 Business customers took delivery in both, so 30 plus 26 gives
56 where the half-year is 36.

- b, "Both counts sit at or under Kavya's bar of 30 customers": the bar decides whether a rate is
  flagged, and has nothing to do with whether two counts may be added.
- c, "The two quarters share no days, so the two counts cannot overlap": the days never overlap, and
  the customers can, which is where the double count comes from.
- d, "The analyst needs only Business's orders and rupees for the half-year": orders and rupees add
  anyway, so this avoids the question and leaves the customer count unanswered.

### Q9. Which ordering makes the five delivered Q2 web orders the same five on every run?

Kind: choose the fix. The key is d, `ORDER BY order_id`. No two orders share an id, so the five are
fixed by the ids alone: KR-00539, KR-00541, KR-00550, KR-00551 and KR-00552, Rs 5,870, before and
after the reload.

- a, `ORDER BY customer_id`: a customer can have several of the 93 candidates, so the order among
  them is left to the database.
- b, "no ORDER BY, only `LIMIT 5`": returns whichever five the database reaches first, which a reload
  can change.
- c, `ORDER BY quarter`: every candidate is in Q2, so this orders nothing.

### Q10. What should the fingerprint printed beside the delivered suite hold?

Kind: choose the check. The key is a, "The delivered book's rows, rupees and distinct customers": 653
rows, Rs 13,45,90,290 and 268 customers. If next Monday's delivered numbers differ and these three do
not, the query moved; if these moved, the book did.

- b, "The count of order rows alone, the one number every reload changes": a rewrite with the same
  values changes no count, and a corrected amount changes the rupees while the rows stay put.
- c, "The time the query took to run, so a slow run stands out on the sheet": describes the run,
  never the book.
- d, "The date the suite was run, so each Monday's output carries its label": labels the output and
  says nothing about what it read.

### Q15. Which route confirms the delivered book's rupees without reusing the delivered filter?

Kind: a design item, the independent second route. The key is c, "The book's rupees less the returned
and the cancelled rupees". Rs 19,84,00,000 less Rs 3,80,55,960 less Rs 2,57,53,750 is Rs 13,45,90,290,
reached from the other two statuses, so a delivered filter that let a returned order in would show up
as a difference.

- a, "Rerun the delivered fingerprint query and set the two results side by side": the same filter
  twice repeats whatever it gets wrong.
- b, "Add part 1's two quarters of delivered revenue, Rs 6,80,25,200 and Rs 6,65,65,090": the sum is
  Rs 13,45,90,290, reached through the same delivered filter, so it cannot catch a fault in it.
- d, "Multiply the 653 delivered rows by the delivered book's revenue per order": revenue per order
  is the delivered rupees over the 653 rows, so the product gives back the number it started from.

## Which wrong answers does the debrief replay?

Item 5, option b, first: thin by orders is the reading a hurried analyst gives, and on delivered orders
it misses Business Q2, the group that carries most of the rupees. Then item 13, option a: the room
that learned this morning that frequency led the fall will carry that line into the afternoon, and on
Finance's definition it no longer holds. Then item 2, option b, if anyone chose it, since it turns 173
customers into 298. Last, item 15, option b: the sum of the two quarters is the right number by a
route that shares the filter it is meant to check.

## Where does this show up at work?

Every finance team keeps more than one definition of revenue, booked, shipped, delivered or net of
returns, and a suite that reruns cleanly on a second definition, with both side by side and the filter
stated on its first line, is the one a controller trusts when the definitions disagree. Tomorrow's
question, how much of what was booked was collected, is the next definition on that list.

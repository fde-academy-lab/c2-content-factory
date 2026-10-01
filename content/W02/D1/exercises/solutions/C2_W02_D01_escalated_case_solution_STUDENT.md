# Which answers hold in the escalated case on the Monday suite over Finance's book, and why?

Answers: 1b 2c 3a 4d 5a 6c 7d 8b 9b 10a 11b 12c 13b 14d 15a

Anand Iyer, Kalpa Retail's finance controller, signs revenue on Finance's definition, the orders that
reached the customer and stayed there, and he asked for the Monday suite on that definition and
whether the story changes. Those orders, Finance's book, are the ones whose status is delivered: a
cancelled order never reached the customer, and a returned one did not stay. The case asks each
learner to rebuild the suite alone in five parts: items 1 to 10 are the ten markers of
`notebooks/C2_W02_D01_ex1_escalated_case_STUDENT.ipynb`, and items 11 to 15 are the brief's own, one
per part. The executed solution,
`C2_W02_D01_ex1_escalated_case_solution_STUDENT.ipynb` in this folder, runs every marker. Four of the
fifteen items are design items: 11, 12, 14 and 15.

**Who needs the answer.** You do, when you check your fifteen letters and your three numbers before
the debrief. The debrief replays the room's wrong answers aloud, and a line you cannot defend here is
the one Anand's analyst sends back.

**The questions on the way.**

- Which idea does the escalated case test: the whole Monday suite rerun on a definition nobody has run yet?
- Which numbers should you have reached, from the delivered book to the five traced orders?
- Why does each of the fifteen keys hold, from the delivered filter to the route that catches it?
- Which four wrong answers does the debrief replay, from thin by orders to a route that shares the fault?
- Where does a second definition of revenue meet Anand next?

## Which idea does the escalated case test: the whole Monday suite rerun on a definition nobody has run yet?

A revenue definition is a row filter that runs before anything is grouped; every customer count names
what it counts; every ratio is divided in numeric and multiplied back; an average says who is inside
it; a wider window counts its customers again from the orders; and a sample is drawn in an order the
rerun will repeat, beside a fingerprint of the book it read. The design items size how the sheet sets
two definitions side by side and how a thin flag reaches it, name the fact that would let two counts
be added, and work out which route would catch a filter that let the cancelled orders in.

## Which numbers should you have reached, from the delivered book to the five traced orders?

| Part | Number | What it means |
|---|---|---|
| 1 | Delivered revenue Rs 6,80,25,200 in Q1 and Rs 6,65,65,090 in Q2, down 2.1 percent, from 355 then 298 orders; 205 then 173 customers who took delivery, down 15.6 percent | The revenue fall is a little deeper on Finance's definition, and the customer fall is more than twice the booked book's 7.0 percent. |
| 2 | Orders per customer, Q1 then Q2: Business 1.90 then 2.08, Retail-Core 1.57 then 1.74, Retail-Plus 1.87 then 1.56, Student 1.58 then 1.65; flagged thin: Business Q2 on 26 customers, Student Q1 on 12 and Q2 on 17 | Retail-Plus is the one segment whose customers ordered less often, and Business's Q2 rate goes on the sheet flagged. |
| 3 | Retail-Plus branches: customers 0.740, orders per customer 0.835, revenue per order 1.049, revenue 0.648; spend per member over the 93 who took delivery, with 77 of them buying in Q1 and 57 in Q2: Rs 4,356 then Rs 2,823, down 35.2 percent | On delivered orders, fewer members taking delivery is the larger branch of the fall. |
| 4 | Half-year customers on delivered orders: Business 36, Retail-Core 116, Retail-Plus 93, Student 23; adding the quarters would say Retail-Plus 134, since 41 members took delivery in both | Counted from the orders, no segment's half-year exceeds its members. |
| 5 | Five delivered Q2 web orders by order id: KR-00539 Rs 850, KR-00541 Rs 1,160, KR-00550 Rs 1,480, KR-00551 Rs 1,500 and KR-00552 Rs 880, Rs 5,870 in all; the delivered book's fingerprint: 653 rows, Rs 13,45,90,290, 268 customers | The same five come back after the reload, beside a fingerprint that says the delivered book did not move. |

The three numbers to post beside the letters are Q2's delivered revenue, Rs 6,65,65,090; Retail-Plus's
Q2 orders per customer, 1.56; and Retail-Plus's half-year customers, 93.

## Why does each of the fifteen keys hold, from the delivered filter to the route that catches it?

### Q1. Which filter keeps the orders that reached the customer and stayed there?

Kind: choose the definition. The key is b, `WHERE status = 'delivered'`. A delivered order reached the
customer and stayed; the filter removes the other statuses row by row, before any group forms, and
keeps 653 orders.

- a, `WHERE status <> 'cancelled'`: keeps the 184 returned orders, whose money went back, 837 orders
  in all.
- c, `WHERE amount > 0`: keeps all 1,000 orders, since no amount on the book is zero or below, so it
  is booked revenue under another name.
- d, `WHERE status <> 'returned'`: keeps the 163 cancelled orders, which never reached the customer,
  816 orders in all.

### Q2. Which expression counts a quarter's customers in Finance's book, each once?

Kind: choose the count. The key is c, "`count(DISTINCT customer_id)`, since every customer id stands
for one customer". It counts each id once however many rows carry it: 205 in Q1 and 173 in Q2, where the
delivered orders number 355 and 298.

- a, "`count(*)`, since each row in Finance's book belongs to a customer Finance counts": counts rows,
  355 and 298, so a customer with three orders counts three times.
- b, "`count(customer_id)`, since it counts the customer column rather than the rows": counts the rows
  whose customer id is filled in, which is every row again.
- d, "`sum(1)`, since adding one per order in Finance's book reaches every customer in it": adds one
  per row, the same 355 and 298.

### Q11. How should the sheet set Finance's revenue beside booked revenue, sized in queries and rows?

Kind: a design item, the best-fit way sized in queries and rows. The key is b, "One query grouped by
quarter, booked and Finance's revenue as two columns of the same 2 rows". One query puts
Rs 10,00,00,000 beside Rs 6,80,25,200 for Q1 and Rs 9,84,00,000 beside Rs 6,65,65,090 for Q2, on the
same row, for example with `sum(amount)` and `sum(CASE WHEN status = 'delivered' THEN amount END)`, so
the reader compares the two definitions without moving between results.

- a, "Two queries, one per definition, whose two results of 2 rows the analyst lines up by hand":
  right numbers, and the lining up by hand is the step Anand ruled out.
- c, "The query on Finance's book alone, 2 rows, since Finance's revenue is the only one Finance
  signs": Anand asked whether the story changes, which needs the booked number beside it.
- d, "One query grouped by quarter and status, 6 rows, which the analyst adds up into the two
  definitions": the delivered rows are there, and booked revenue has to be added by hand from three
  rows per quarter.

### Q3. How many rows will the segment query on Finance's book return?

Kind: predict the output. The key is a, "8, one for each segment in each quarter". Grouping by segment
and quarter makes one group for each pair that has rows, and every segment took delivery in both
quarters, so four segments times two quarters gives 8.

- b, "4, one for each segment over both quarters": the answer for a query grouped by segment alone.
- c, "2, one for each quarter over all segments": the answer for a query grouped by quarter alone.
- d, "One for each order the filter keeps": the 653 rows before grouping; grouping returns one row per
  group.

### Q4. Which orders-per-customer figure survives the analyst's multiply-back check?

Kind: fix the logic. The key is d, `round(count(*)::numeric / count(DISTINCT o.customer_id), 2)`.
Dividing in numeric keeps the decimals: Retail-Plus 144 over 77 is 1.87 and 89 over 57 is 1.56, and
1.56 times 57 is 88.9, within half an order of 89.

- a, `round(count(*) / count(DISTINCT o.customer_id), 2)`: the division of two whole numbers has
  already dropped the remainder before round sees it, so Retail-Plus reads 1.00 in both quarters.
- b, `count(*) / count(DISTINCT o.customer_id)`: the same whole-number division with no rounding at
  all.
- c, `round(count(DISTINCT o.customer_id)::numeric / count(*), 2)`: customers per order, the branch
  upside down.

### Q5. Which clause lists the segment-quarters Kavya flags as too thin?

Kind: choose the clause. The key is a, "`HAVING count(DISTINCT o.customer_id) < 30`, since HAVING tests
a group once formed". HAVING keeps whole groups after they form, and Kavya's bar counts customers, so
it returns Business Q2 on 26, Student Q1 on 12 and Student Q2 on 17.

- b, "`HAVING count(*) < 30`, since a thin group is one with few orders": counts orders, flags Student
  Q1 (19) and Q2 (28), and misses Business Q2's 26 customers behind 54 orders.
- c, "`HAVING count(DISTINCT o.customer_id) <= 30`, since a group on exactly 30 is thin too": also
  flags Business Q1, whose 30 customers meet Kavya's bar; the bar flags fewer than 30.
- d, "`HAVING count(o.customer_id) < 30`, since it counts the customer column": counts the rows that
  carry a customer id, which are the orders, so it flags the same two Student quarters as b.

### Q12. How should the thin flag reach the sheet, sized in rows?

Kind: a design item, the best-fit way sized in rows. The key is c, "A flag column on the sheet's own
eight rows, true where a group has fewer than 30 customers who took delivery". Each line carries its
own flag, so the three thin groups are marked where the reader meets their numbers, and no line is
hidden.

- a, "A HAVING query that lists the thin groups on their own, three rows the analyst matches to the
  sheet by hand": right groups, and a second result to match by hand is how a flag lands on the wrong
  line.
- b, "A HAVING query that keeps only the groups with 30 or more customers, five rows, so no thin rate
  reaches the sheet": drops Business Q2, which books most of the quarter's delivered rupees; a thin
  rate is flagged, never hidden.
- d, "A flag on the groups with fewer than 30 orders, which catches Student's two quarters and no other
  group": counts orders, so Business Q2's 26 customers go unflagged.

### Q6. Which expression averages each quarter's spend over every member in the step?

Kind: choose the average. The key is c, `avg(coalesce(q2_spend, 0))`. A member with no delivered Q2
order spent Rs 0 in Q2, written in on purpose, so both quarters average over every member in the step,
the 93 who took delivery in either quarter: Rs 4,356 then Rs 2,823, down 35.2 percent, the same change
as the tier's delivered revenue, and each average times 93 gives back its quarter's revenue.

- a, `avg(q2_spend)`: averages only the 57 members who took delivery in Q2, Rs 4,607, against Q1's 77,
  Rs 5,261, two different groups.
- b, `sum(q2_spend) / count(q2_spend)`: the same average over the same 57, written out by hand.
- d, `sum(q2_spend) / 120`: divides by the 120 members on the customers table, 27 of whom took no
  delivery in either quarter, so it reads Rs 2,188 and is no longer an average over the step.

### Q7. Which pair of counts shows who is inside each quarter's average?

Kind: choose the check. The key is d, `count(q1_spend)` and `count(q2_spend)` beside `count(*)`. They
read 77 and 57 beside 93, which shows a plain average would cover two different groups; after the zero
is written in, both averages cover all 93.

- a, `sum(q1_spend)` and `sum(q2_spend)`: rupees, which say nothing about who is inside.
- b, `count(DISTINCT q1_spend)` and `count(DISTINCT q2_spend)`: counts different spend values, 73 and
  54, so two members who spent the same amount count once.
- c, `avg(q1_spend)` and `avg(q2_spend)`: the averages themselves, with nothing to say whom they
  cover.

### Q13. Does the story change for Retail-Plus in Finance's book?

Kind: read the two trees side by side. The key is b, "It shifts: in Finance's book fewer members
buying is now the larger fall, 0.740 against 0.835". On booked orders, members ordering less often led
(orders per customer 0.780 against customers 0.835); on delivered orders, 26.0 percent fewer members
took delivery and each did so 16.5 percent less often, and revenue fell 35.2 percent. The line to Anand
says the story shifts toward members who stopped taking delivery.

- a, "It holds: members ordering less often is still the branch that fell furthest, on both
  definitions": on delivered orders the customer branch, 0.740, fell further than frequency, 0.835.
- c, "It holds: revenue falls by 29 to 35 percent on either definition, the same story told twice":
  the revenue ratio matches in direction, and the branch that carries it changed.
- d, "It reverses: revenue per order rose on both, so Retail-Plus is spending more where it counts":
  a larger basket on fewer members and fewer orders still leaves revenue down by a third.

### Q8. How many Business customers does Finance's book hold in the half-year?

Kind: predict the number. The key is b, "36, each of the customers counted once". The 20 who took
delivery in both quarters sit in both counts, so the half-year is 30 plus 26 less 20, which is 36, the
number the count from the orders prints.

- a, "56, the two quarters' customers added": counts the 20 two-quarter customers twice, and 56 is
  more than Business's 40 customers on the customers table.
- c, "30, the larger of the two quarters": leaves out the 6 who took delivery only in Q2.
- d, "10, the Q1 customers who did not return": that is one group of the three, the customers who
  took delivery in Q1 only.

### Q14. Which fact would let the analyst add Business's two quarter counts for its half-year?

Kind: a design item, the fact that would switch the method. The key is d, "No Business customer has an
order in Finance's book in both quarters". Adding double-counts exactly the customers in both
quarters, so with none the sum would be exact. On the book, 20 Business customers took delivery in
both, so 30 plus 26 gives 56 where the half-year is 36.

- a, "Both counts sit at or under Kavya's bar of 30 customers": the bar decides whether a rate is
  flagged, and has nothing to do with whether two counts may be added.
- b, "The two quarters share no days, so the two counts cannot overlap": the days never overlap, and
  the customers can, which is where the double count comes from.
- c, "The analyst needs only Business's orders and rupees for the half-year line": orders and rupees
  add anyway, so this avoids the question and leaves the customer count unanswered.

### Q9. Which way of writing the sample makes its five Q2 web orders the same five on every run?

Kind: choose the fix. The key is b, "`ORDER BY order_id`, then `LIMIT 5`". The sort comes before the
cut, and no two orders share an id, so the five are fixed by the ids alone: KR-00539, KR-00541,
KR-00550, KR-00551 and KR-00552, Rs 5,870, before and after the reload.

- a, "`LIMIT 5` first, then `ORDER BY order_id` in an outer query": the cut comes first, so the five
  are whichever the database reached first, now printed in order; after the reload four of them come
  back and one does not.
- c, "no ORDER BY, only `LIMIT 5`": returns whichever five the database reaches first, which a reload
  can change.
- d, "`ORDER BY quarter`, then `LIMIT 5`": every candidate is in Q2, so this orders nothing and the
  five come back as unordered as c.

### Q10. What should the fingerprint printed beside the suite on Finance's book hold?

Kind: choose the check. The key is a, "The rows, rupees and distinct customers of Finance's book, three
numbers": 653 rows, Rs 13,45,90,290 and 268 customers. If next Monday's numbers differ and
these three do not, the query moved; if these moved, the book did.

- b, "The count of order rows alone, the one number every reload changes": a rewrite with the same
  values changes no count, and a corrected amount changes the rupees while the rows stay put.
- c, "The rows and distinct customers of Finance's book, the suite's own two counts": an amount
  corrected overnight leaves both counts where they were, and moves every revenue line on the sheet.
- d, "The row count and the latest order date, so a late order shows up": catches a late order and
  misses a corrected amount for the same reason as c.

### Q15. Which route would catch a filter that let the cancelled orders in?

Kind: a design item, the independent second route, worked out from the amounts in the stem. The key is
a, "The book's rupees less those of every order Finance's definition leaves out". The definition
leaves out the returned and the cancelled orders, and Rs 19,84,00,000 less Rs 3,80,55,960 less
Rs 2,57,53,750 is Rs 13,45,90,290, which sits Rs 2,57,53,750 below the faulty Rs 16,03,44,040,
exactly the cancelled rupees the filter let in.

- b, "Part 1's two quarters of revenue added, through the same filter": Rs 8,05,93,520 plus
  Rs 7,97,50,520 is Rs 16,03,44,040, the faulty number again, since it shares the fault.
- c, "The book's rupees less the returned rupees, the orders sent back after delivery":
  Rs 19,84,00,000 less Rs 3,80,55,960 is Rs 16,03,44,040; the route avoids the filter and still
  agrees with the fault, because it writes down the same wrong definition.
- d, "The fingerprint's rows times its revenue per order, from the same query": revenue per order is
  the faulty rupees over the faulty 816 rows, so the product gives back Rs 16,03,44,040.

## Which four wrong answers does the debrief replay, from thin by orders to a route that shares the fault?

Item 5, option b, first: thin by orders is the reading a hurried analyst gives, and on delivered orders
it misses Business Q2, the group that carries most of the rupees. Then item 13, option a: the room
that learned this morning that frequency led the fall will carry that line into the afternoon, and on
Finance's definition it no longer holds. Then item 2, option a, if anyone chose it, since it turns 173
customers into 298. Last, item 15, option c: a route that never touches the filter can still agree
with a wrong number when it carries the same wrong definition, which is why the key subtracts every
status that is not delivered.

## Where does a second definition of revenue meet Anand next?

Anand's sheet now carries booked and delivered revenue side by side, each from a filter stated on its
first line. Tomorrow's question is collected revenue, what was actually paid against what was booked
in Q2, order by order, and it brings the payments table into the book. The same habits carry over: the
definition stated once, counts that say what they count, and a second route that does not share the
first one's filter.

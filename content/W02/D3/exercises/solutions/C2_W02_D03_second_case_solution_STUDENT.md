# Which answers hold in the second case on whether Retail-Core's list should rank members by how often they ordered, and why?

Answers: 1a 2b 3a 4b 5a 6a 7b 8d 9c 10d

The marketing lead wants Retail-Core's top fifty ranked by how often members ordered in Q2, under the
head of Retail-Plus's rule. A count ties far more often than a rupee amount, so the case asks each pair
to read the tie rule again on a new metric: items 1 to 7 are the seven markers of
`notebooks/C2_W02_D03_ex2_second_case_STUDENT.ipynb`, and items 8 to 10 are the brief's design items.
The executed solution, `C2_W02_D03_ex2_second_case_solution_STUDENT.ipynb` in this folder, runs every
marker. Three of the ten items are design items: 8, 9 and 10. The line, in a list, is the last place it
keeps, fiftieth on a top fifty.

**Who needs the answer.** You and your partner need it after the take-home, to check ten letters and
one sentence. The marketing lead decides on that sentence which members the member team protects, so
its count and its comparison with the revenue list have to hold on their own.

**The questions on the way.**

- What does the second case test about a tie rule read again on a count?
- Which numbers should the frequency list have reached, step by step?
- Why is each of the second case's ten keys right, and each other letter wrong?
- Why is item 7's option a, RANK on orders alone, worth arguing about?
- Where does a list ranked on a count meet the same crowd of ties?

## What does the second case test about a tie rule read again on a count?

A tie rule chosen for rupee amounts behaves differently on a count, where dozens of members share a
value. RANK keeps the head's promise and ships 51, a second key with a business reason brings the list
to fifty, and the change of metric is then measured before anyone argues over it. The design items
price the rule that lets the id decide, reach the shared count by a route with no join, and measure
whether frequency is falling in Retail-Core at all.

## Which numbers should the frequency list have reached, step by step?

| Step | Number | What it means |
|---|---|---|
| 1 | 96 members, 193 orders: 1 member with 8 orders, 2 with 7, 2 with 5, 5 with 4, 14 with 3, 27 with 2 and 45 with 1 | Seven different counts for 96 members, so ties are everywhere. |
| 2 | Ranked by orders alone: ROW_NUMBER 50, RANK 51, DENSE_RANK 96, whole ties only 24 | DENSE_RANK has only seven numbers to give, so every member is inside fifty. |
| 3 | 24 members with three or more orders, then the 27 with two all at place 25 | RANK ships 24 plus 27, one over fifty. |
| 4 | Orders first, Q2 revenue second: RANK ships 50, and the two-order member left off is C-0070, who booked Rs 2,730, the least of the 27 | The second key breaks the crowd with a reason. |
| 5 | 49 members on both lists: C-0092 (two orders, Rs 2,950) only on the frequency list, C-0072 (one order, Rs 2,990) only on the revenue list | One member swaps each way. |
| 6 | The frequency list carries Rs 2,78,700 and 146 orders, the revenue list Rs 2,78,740 and 145 orders | The change costs Rs 40 of covered revenue and buys one more order. |
| 6 | Retail-Core placed 199 orders from 102 buyers in Q1, 1.95 a buyer, and 193 from 96 in Q2, 2.01 a buyer; Retail-Plus went from 2.36 to 1.84 | Frequency has not started to fall in Retail-Core, so the frequency list is a precaution taken early. |

A sentence for the marketing lead that holds: "Rank by orders with Q2 revenue as the second key: fifty
ship, and the list is almost the revenue list, member for member and in rupees." In numbers, 49 of its
50 members are on the revenue list too, and the two lists differ by Rs 40.

## Why is each of the second case's ten keys right, and each other letter wrong?

### Q1. Which expression counts a member's Q2 orders?

This item asks you to choose the count. The key is a, "`count(*)`, which counts one for every order
row the member placed". Grouped by member over Q2's Retail-Core orders, each row is one order, so the
count is the member's orders: 193 across 96 members.

- b, "`count(DISTINCT o.customer_id)`, so no member is counted twice": inside one member's group there
  is one customer id, so every member reads 1.
- c, "`count(DISTINCT o.order_date)`, so a day with two orders counts once": three Retail-Core members
  placed two Q2 orders on the same day, so their counts fall by one and the counts no longer add back to
  the segment's 193 orders.
- d, "`count(DISTINCT date_trunc('month', o.order_date))`, months with orders": 1 to 3 for every
  member, a different measure that ties even more.

### Q2. Which window puts the head of Retail-Plus's rule on the orders count?

This item asks you to choose the rule. The key is b, `rank() OVER (ORDER BY q2_orders DESC)`. Members
with the same number of orders share a place and the next place skips the ones they used, which is the
head's rule: it ships 51.

- a, `row_number() OVER (ORDER BY q2_orders DESC, customer_id)`: ships 50 by giving members with the
  same orders different places, decided by their ids.
- c, `dense_rank() OVER (ORDER BY q2_orders DESC)`: shares the place and skips nothing, so its seven
  numbers put all 96 members inside fifty.
- d, `rank() OVER (ORDER BY q2_orders)`: the head's rule ascending, so place 1 goes to a member with one
  order and the list keeps the members who ordered least.

### Q3. Why does the head's rule, on orders alone, ship more than fifty members?

This item asks you to explain the count. The key is a, "24 members placed three or more orders, and the
27 members with two orders all share the 25th place". One, two, two, five and fourteen members fill
places 1 to 24, and the 27 two-order members share place 25, so RANK ships 24 plus 27, which is 51.

- b, "The rule skips a number after every tie, and those skipped numbers count as extra members on the
  list": skipped numbers are numbers nobody holds; the list counts members.
- c, "The rule numbers the 27 two-order members 25 to 51 by id, one place each, and keeps every one of
  them": that is ROW_NUMBER with the id as the tiebreaker, which would stop at fifty; under the head's
  rule all 27 hold place 25, which is why every one of them ships.
- d, "The 45 members with one order share a place, and the rule adds one of them to make the list
  even": the one-order members share place 52, past the line, and RANK never adds anyone to round a
  count.

### Q4. Which ORDER BY ranks by orders first, then lets revenue separate members with the same orders?

This item asks you to fix the logic. The key is b, `ORDER BY q2_orders DESC, q2_revenue DESC`. Orders decide first, and
among members with the same orders, the one who spent more ranks higher. RANK ships 50: of the 27
two-order members, the 26 who spent most stay and C-0070, on Rs 2,730, is left off.

- a, `ORDER BY q2_orders DESC, customer_id`: the id breaks every tie, so RANK behaves as ROW_NUMBER and
  the member left off is whoever has the highest id.
- c, `ORDER BY q2_revenue DESC, q2_orders DESC`: revenue first, which is the revenue list again.
- d, `ORDER BY q2_orders DESC`: orders alone, the 27 members tied at place 25 and 51 members.

### Q8. Which member does a rule that lets the id decide leave off, and what does it cost?

This is a design item: it asks you to size the alternative rule by what it costs.

The key is d, "C-0147, who booked Rs 4,780, while C-0070 on Rs 2,730 stays, because the highest id is
the one cut". Among the 27 two-order members the id rule keeps the 26 lowest ids, and the highest,
C-0147, goes, though they spent Rs 2,050 more than C-0070, who stays. The rule ships fifty and keeps a
member nobody would choose over the one it drops, and its only reason is the order the ids were
issued in.

- a, "C-0070, who booked Rs 2,730, the least of the 27, so the id rule cuts the member a spend rule would": that is what a spend key does; C-0070's id is low, so the id rule keeps them.
- b, "C-0092, who booked Rs 2,950, since they are the member a list ranked by revenue alone also leaves
  off": C-0092 is off the revenue list, a different list, and their id is lower than C-0147's, so the id
  rule keeps them.
- c, "Nobody who matters, since every two-order member booked within a few hundred rupees of the
  others": the 27 run from Rs 2,730 to Rs 5,750, more than double.

### Q5. Which query counts the members who are on both lists?

This item asks you to choose the query. The key is a, "An INNER JOIN of the two lists on customer_id, counting the rows
it returns". The join keeps a member only when their id is on both lists: 49.

- b, "A LEFT JOIN from the revenue list to the frequency list, counting every row": keeps
  every revenue-list row whether or not it matched, 50.
- c, "UNION ALL of the two lists, counting the rows": stacks the two lists, 100 rows.
- d, "The revenue list EXCEPT the frequency list, counting the rows it returns": EXCEPT keeps the
  members on the revenue list who are missing from the frequency list, one member, C-0072, which is the
  difference and never the overlap.

### Q9. Which route confirms the number of members on both lists a second way, and what does it give?

This is a design item: it asks for the independent second route.

The key is c, "A UNION of the two lists' ids, 51 different members, so 50 plus 50 less 51 gives 49".
UNION keeps each id once, so it counts the members on at least one list; the two lists' rows less that
count are the members counted twice, the shared ones. It reaches the join's 49 with set arithmetic
alone.

- a, "UNION ALL of the two lists' ids, 100 rows, less one list's 50, which gives 50 shared": taking
  one list away from the stack leaves the other list, whoever is on it.
- b, "A filter on the frequency list for members with two or more Q2 orders, which gives 50":
  every member on the frequency list has two or more orders by construction, so the filter returns 50
  whatever the overlap.
- d, "Retail-Core's 96 buyers less the 45 who are on neither list, which gives 51 shared": 51 is the
  union, the members on at least one list.

### Q6. How far apart are the two lists in the Q2 revenue they carry?

This item asks you to predict the number. The key is a, "Rs 40, the difference between the Q2 revenue
the two lists carry". The revenue list carries Rs 2,78,740 and the frequency list Rs 2,78,700: C-0072's
Rs 2,990 leaves and C-0092's Rs 2,950 comes in.

- b, "Rs 2,950, the Q2 revenue of the frequency list's fiftieth member": that is C-0092's own revenue,
  the member who comes in, read without the member who goes out.
- c, "Rs 1,09,900, the Q2 revenue of the 27 members with two orders": the revenue of the crowd at place
  25, most of whom are on both lists, so it measures no difference between the lists.
- d, "Rs 2,980, the Q2 revenue of the revenue list's fiftieth member": that is C-0005's figure, the
  revenue list's line, and C-0005 is on both lists.

### Q7. Which sentence goes to the marketing lead?

This item asks you to choose the sentence. The key is b, "Rank by orders with Q2 revenue as the second
key: fifty ship, and the list is almost the revenue list, member for member and in rupees." It gives
the rule, the count it ships and the size of the change in one sentence: 49 of the 50 members are on
the revenue list too, and the two lists differ by Rs 40.

- a, "Rank Retail-Core by orders alone under RANK: the list runs past fifty, which honours the tie rule
  and protects the frequency that fell.": the list does run past fifty, to 51, and it ends on 27
  members tied at place 25, more than half of it decided by nothing but a shared count; a second key
  with a reason ships fifty.
- c, "Rank Retail-Core with DENSE_RANK on orders, so that every member who ordered the same shares a
  place on the list.": DENSE_RANK on orders ships all 96 buyers, so the list leaves nobody off.
- d, "Keep the revenue list, since ranking by orders would drop the members whose quarters carry the
  most revenue.": the two lists differ by one member each way and Rs 40, so the frequency list drops
  nobody who carries much.

### Q10. Is frequency falling in Retail-Core too, and which measure says so?

This is a design item: it asks for the measure that answers the marketing lead's premise, computed on
two quarters.

The key is d, "Orders per buying member, Q1 against Q2: 1.95 then 2.01, so it has not started to fall
yet". Frequency is orders per member who bought, so it is the orders divided by the buyers in each
quarter: 199 orders from 102 buyers in Q1 and 193 from 96 in Q2. Retail-Plus's fell from 2.36 to 1.84
over the same two quarters. The frequency list in Retail-Core is a precaution taken before the fall
reaches it, and the sentence to the marketing lead can say so.

- a, "Total Retail-Core orders, Q1 against Q2: 199 then 193, so frequency is falling there too": total
  orders fell because six fewer members bought, and each buyer ordered slightly more often.
- b, "Orders per buying member, Q1 against Q2: 2.01 then 1.95, so it falls as Retail-Plus's did": the
  right measure read with the quarters swapped.
- c, "Members with one Q2 order, 45 of 96, nearly half, so frequency in Retail-Core is already low": a
  level in one quarter, with no quarter to compare it against, cannot say whether frequency is
  falling.

## Why is item 7's option a, RANK on orders alone, worth arguing about?

Item 7's option a keeps the head of Retail-Plus's promise to the letter, and a pair can defend it: nobody who ordered as often as a listed member is left off. The cost is that more
than half the list is one tie, 27 members at place 25, so the list says nothing about which of them
matter more. A second key with a reason Marketing can repeat, here what each member spent, keeps equal
members equal on both keys and ships fifty.

## Where does a list ranked on a count meet the same crowd of ties?

Any list ranked on visits, orders or logins meets it, because a count piles members onto the same few
values. Here the change of metric was measured before anyone argued over it: one member each way and
Rs 40 between the lists, with frequency not yet falling in Retail-Core.

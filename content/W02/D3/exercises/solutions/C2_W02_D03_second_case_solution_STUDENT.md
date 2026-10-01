# Which answers hold in the second case on whether Retail-Core's list should rank members by how often they ordered, and why?

Answers: 1a 2b 3a 4b 5a 6a 7b 8d 9c 10d

The marketing lead wants Retail-Core's top fifty ranked by how often members ordered in Q2, under the
head of Retail-Plus's rule. A count ties far more often than a rupee amount, so the case asks each pair
to read the tie rule again on a new metric: items 1 to 7 are the seven markers of
`notebooks/C2_W02_D03_ex2_second_case_STUDENT.ipynb`, and items 8 to 10 are the brief's design items.
The executed solution, `C2_W02_D03_ex2_second_case_solution_STUDENT.ipynb` in this folder, runs every
marker. Three of the ten items are design items: 8, 9 and 10.

**Who needs the answer.** You and your partner, after the take-home, checking ten letters and one
line. The marketing lead decides on that line which members the member team protects, so its count
and its comparison with the revenue list have to hold on their own.

**The questions on the way.**

- Which idea does this case test?
- Which numbers should you have reached, step by step?
- Why is each key right, item by item?
- Which wrong answer is worth arguing about?
- Where does this show up at work?

## Which idea does this case test?

A tie rule chosen for rupee amounts behaves differently on a count, where dozens of members share a
value. RANK keeps the head's promise and ships 51, a second key with a business reason brings the list
to fifty, and the change of metric is then measured before anyone argues over it. The design items
price the rule that lets the id decide, reach the shared count by a route with no join, and name the
fact that would send the team back to revenue.

## Which numbers should you have reached, step by step?

| Step | Number | What it means |
|---|---|---|
| 1 | 96 members, 193 orders: 1 member with 8 orders, 2 with 7, 2 with 5, 5 with 4, 14 with 3, 27 with 2 and 45 with 1 | Seven different counts for 96 members, so ties are everywhere. |
| 2 | Ranked by orders alone: ROW_NUMBER 50, RANK 51, DENSE_RANK 96, whole ties only 24 | DENSE_RANK has only seven numbers to give, so every member is inside fifty. |
| 3 | 24 members with three or more orders, then the 27 with two all at place 25 | RANK ships 24 plus 27, one over the line. |
| 4 | Orders first, Q2 revenue second: RANK ships 50, and the two-order member left off is C-0070, who booked Rs 2,730, the least of the 27 | The second key breaks the crowd with a reason. |
| 5 | 49 members on both lists: C-0092 (two orders, Rs 2,950) only on the frequency list, C-0072 (one order, Rs 2,990) only on the revenue list | One member swaps each way. |
| 6 | The frequency list carries Rs 2,78,700 and 146 orders, the revenue list Rs 2,78,740 and 145 orders | The change costs Rs 40 of covered revenue and buys one more order. |

A line for the marketing lead that holds: "Rank by orders with Q2 revenue as the second key: fifty
ship, 49 are on the revenue list too, and the lists differ by Rs 40."

## Why is each key right, item by item?

### Q1. Which expression counts a member's Q2 orders?

Kind: choose the count. The key is a, "`count(*)`, one per order row the member placed". Grouped by
member over Q2's Retail-Core orders, each row is one order, so the count is the member's orders: 193
across 96 members.

- b, `count(DISTINCT o.customer_id)`: inside one member's group there is one customer id, so every
  member reads 1.
- c, `sum(o.amount)`: the member's Q2 revenue, which is the list Marketing already has.
- d, `count(DISTINCT date_trunc('month', o.order_date))`: the months with an order, 1 to 3 for every
  member, a different measure that ties even more.

### Q2. Which window gives members with the same number of orders the same place, and skips the places they use up?

Kind: choose the rule. The key is b, `rank() OVER (ORDER BY q2_orders DESC)`. Members with the same
number of orders share a place and the next place skips the ones they used: it ships 51.

- a, `row_number() OVER (ORDER BY q2_orders DESC, customer_id)`: ships 50 by giving members with the
  same orders different places, decided by their ids.
- c, `dense_rank() OVER (ORDER BY q2_orders DESC)`: shares the place and skips nothing, so its seven
  numbers put all 96 members inside fifty.
- d, `rank() OVER (ORDER BY q2_revenue DESC)`: the head's rule on revenue, the list the marketing lead
  asked to replace.

### Q3. Why does RANK on orders alone ship 51 members?

Kind: explain the count. The key is a, "24 members placed three or more orders, and the 27 members
with two orders all share 25th place". One, two, two, five and fourteen members fill places 1 to 24,
and the 27 two-order members share place 25, so RANK ships 24 plus 27.

- b, "RANK skips a number after every tie, and those skipped numbers count as extra members on the
  list": skipped numbers are numbers nobody holds; the list counts members.
- c, "One member placed eight orders, so RANK counts that member several times on the list": the table
  holds one row per member, so nobody appears twice.
- d, "The 45 members with one order share a place, and RANK adds one of them to make the list even":
  the one-order members share place 52, past the line, and RANK never adds anyone to round a count.

### Q4. Which ORDER BY ranks by orders first, then lets revenue separate members with the same orders?

Kind: fix the logic. The key is b, `ORDER BY q2_orders DESC, q2_revenue DESC`. Orders decide first, and
among members with the same orders, the one who spent more ranks higher. RANK ships 50: of the 27
two-order members, the 26 who spent most stay and C-0070, on Rs 2,730, is left off.

- a, `ORDER BY q2_orders DESC, customer_id`: the id breaks every tie, so RANK behaves as ROW_NUMBER and
  the member left off is whoever has the highest id.
- c, `ORDER BY q2_revenue DESC, q2_orders DESC`: revenue first, which is the revenue list again.
- d, `ORDER BY q2_orders DESC`: orders alone, the crowd of 27 at place 25 and 51 members.

### Q8. Which member does a rule that lets the id decide leave off, and what does it cost?

Kind: a design item, the alternative rule sized by what it costs.

The key is d, "C-0147, who booked Rs 4,780, while C-0070 on Rs 2,730 stays, because the highest id is
the one cut". Among the 27 two-order members the id rule keeps the 26 lowest ids, and the highest,
C-0147, goes, though he spent Rs 2,050 more than C-0070, who stays. The rule ships fifty and keeps a
member nobody would choose over the one it drops, and its only reason is the order the ids were
issued in.

- a, "C-0070, who booked Rs 2,730, the least of the 27, so the id rule and a spend rule leave off the
  same member": that is what a spend key does; C-0070's id is low, so the id rule keeps him.
- b, "C-0092, who booked Rs 2,950, since he is the member a list ranked by revenue alone also leaves
  off": C-0092 is off the revenue list, a different list, and his id is lower than C-0147's, so the id
  rule keeps him.
- c, "Nobody who matters, since every two-order member booked within a few hundred rupees of the
  others": the 27 run from Rs 2,730 to Rs 5,750, more than double.

### Q5. Which query counts the members who are on both lists?

Kind: choose the query. The key is a, "An INNER JOIN of the two lists on customer_id, counting the rows
it returns". The join keeps a member only when his id is on both lists: 49.

- b, "A LEFT JOIN from the revenue list to the frequency list, counting all the rows it returns": keeps
  every revenue-list row whether or not it matched, 50.
- c, "UNION ALL of the two lists, counting the rows": stacks the two lists, 100 rows.
- d, "The two list counts subtracted, 50 less 50": two lists of the same length can hold different
  members, so the difference says nothing about the overlap.

### Q9. Which route confirms the number of members on both lists a second way, and what does it give?

Kind: a design item, the independent second route.

The key is c, "A UNION of the two lists' ids, 51 different members, so 50 plus 50 less 51 gives 49".
UNION keeps each id once, so it counts the members on at least one list; the two lists' rows less that
count are the members counted twice, the shared ones. It reaches the join's 49 with set arithmetic
alone.

- a, "UNION ALL of the two lists' ids, 100 rows, less one list's 50, which gives 50 shared": taking
  one list away from the stack leaves the other list, whoever is on it.
- b, "The frequency list's members with two or more Q2 orders, counted with a filter, which gives 50":
  every member on the frequency list has two or more orders by construction, so the filter returns 50
  whatever the overlap.
- d, "Retail-Core's 96 buyers less the 45 who are on neither list, which gives 51 shared": 51 is the
  union, the members on at least one list.

### Q6. How far apart are the two lists in the Q2 revenue they carry?

Kind: predict the number. The key is a, "Rs 40". The revenue list carries Rs 2,78,740 and the frequency
list Rs 2,78,700: C-0072's Rs 2,990 leaves and C-0092's Rs 2,950 comes in.

- b, "Rs 2,950": C-0092's own revenue, the member who comes in, without the member who goes out.
- c, "About Rs 1.2 lakh": a gap that size would mean lists with few members in common, and these share
  49.
- d, "Nothing, since both lists hold fifty members": the same length with one member swapped each way.

### Q7. Which line goes to the marketing lead?

Kind: choose the line. The key is b, "Rank by orders with Q2 revenue as the second key: fifty ship, 49
are on the revenue list too, and the lists differ by Rs 40." It gives the rule, the count it ships and
the size of the change in one sentence.

- a, "Rank Retail-Core by orders alone under RANK: 51 members ship, which honours the tie rule and
  protects the frequency that fell.": the count is right and the list ends on 27 members tied at place
  25, more than half of it decided by nothing but a shared count; a second key with a reason ships
  fifty.
- c, "Rank Retail-Core with DENSE_RANK on orders, so that every member who ordered the same shares a
  place on the list.": DENSE_RANK on orders ships all 96 buyers, which is no list at all.
- d, "Keep the revenue list, since ranking by orders would drop the members whose quarters carry the
  most revenue.": the two lists differ by one member each way and Rs 40, so the frequency list drops
  nobody who carries much.

### Q10. Which fact would send the team back to the list ranked by revenue alone?

Kind: a design item, the fact that would switch the call.

The key is d, "The frequency list carried a fifth less of Retail-Core's Q2 revenue, a real cost in
coverage". The call to rank by orders is cheap today because the two lists carry almost the same
rupees. Were the frequency list to carry a fifth less, protecting frequency would leave a fifth of the
segment's revenue off the list, and the revenue list would earn its place back.

- a, "Two two-order members, C-0060 and C-0121, booked the same Rs 4,120, so revenue cannot separate
  every pair": true, and both sit inside the list at place 38, so the count does not move; the revenue
  list holds the same pair tied.
- b, "RANK on orders alone shipped 51 members, one more than the fifty the marketing lead asked for":
  the second key already brings the list to fifty.
- c, "Retail-Core's orders per member fell from Q1 to Q2, the way Retail-Plus's did, so frequency is
  spreading": that would argue for the frequency list, the reason the marketing lead gave.

## Which wrong answer is worth arguing about?

Item 7, option a. RANK on orders alone keeps the head of Retail-Plus's promise to the letter, and a
pair can defend it: nobody who ordered as often as a listed member is left off. The cost is that more
than half the list is one tie, 27 members at place 25, so the list says nothing about which of them
matter more. A second key with a reason Marketing can repeat, here what each member spent, keeps equal
members equal on both keys and ships fifty.

## Where does this show up at work?

Every loyalty team that ranks on visits or orders meets this case, because counts pile up on the same
few values. The decision that holds is the one that measures how much the list changes before it
argues about which list is right: here one member each way and Rs 40, which makes the frequency list an
easy yes.

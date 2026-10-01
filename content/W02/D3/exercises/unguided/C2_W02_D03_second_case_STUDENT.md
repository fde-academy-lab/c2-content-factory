# Should Retail-Core's protect list rank members by how often they ordered in Q2, instead of by how much they spent?

The second case is part of the take-home and takes about forty minutes, in pairs or alone. You work in
`notebooks/C2_W02_D03_ex2_second_case_STUDENT.ipynb`, and this brief carries everything the case
needs. Items 1 to 7 are the notebook's seven lettered
markers, with the same numbers and the same letters. Items 8 to 10 are this brief's own design items,
answered here.

> "Frequency is what fell in Retail-Plus. Before it spreads, I want Retail-Core's top fifty ranked by
> how often members ordered in Q2. Same rule as the head of Retail-Plus: ties ranked the same, and
> tell me how many made it."
>
> The marketing lead, Kalpa Retail

Retail-Core is Kalpa Retail's everyday shoppers: 96 of them ordered in Q2 (July to September 2026, after Q1,
April to June),
193 orders worth Rs 3,66,250, every order booked at its amount whatever its status. Ranked by Q2
revenue under the head of Retail-Plus's rule, which gives members who spent the same one place and
skips the places they use up, Retail-Core's top fifty holds 50 members, because nobody ties at the
line, the last place the list keeps: the fiftieth, C-0005, booked Rs 2,980 and the 51st, C-0092,
Rs 2,950. Frequency is the number of
Q2 orders a member placed. `ROW_NUMBER` gives every member a number of their own, `RANK` gives tied
members one number and skips the numbers they use up, and `DENSE_RANK` gives them one number and skips
nothing, so it numbers the different values. A second key in a window's ORDER BY decides between members
the first key leaves tied. The book is Kalpa's Postgres warehouse: `orders` (1,000 rows: order_id,
customer_id, order_date, quarter, channel, amount, status) and `customers` (340 rows, one per member,
with the segment).

| Q2 orders placed | 8 | 7 | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|---|---|
| Retail-Core members | 1 | 2 | 2 | 5 | 14 | 27 | 45 |

The 27 Retail-Core members with two Q2 orders, by customer id, with their Q2 revenue:

| Member | Q2 revenue | Member | Q2 revenue | Member | Q2 revenue |
|---|---|---|---|---|---|
| C-0003 | Rs 3,440 | C-0047 | Rs 5,500 | C-0118 | Rs 3,590 |
| C-0004 | Rs 3,120 | C-0054 | Rs 3,000 | C-0121 | Rs 4,120 |
| C-0005 | Rs 2,980 | C-0060 | Rs 4,120 | C-0124 | Rs 4,150 |
| C-0007 | Rs 3,100 | C-0066 | Rs 3,960 | C-0127 | Rs 3,030 |
| C-0013 | Rs 4,270 | C-0070 | Rs 2,730 | C-0131 | Rs 4,700 |
| C-0018 | Rs 4,440 | C-0092 | Rs 2,950 | C-0132 | Rs 4,540 |
| C-0022 | Rs 3,520 | C-0095 | Rs 4,070 | C-0139 | Rs 5,020 |
| C-0031 | Rs 4,750 | C-0113 | Rs 4,300 | C-0142 | Rs 5,750 |
| C-0045 | Rs 5,200 | C-0116 | Rs 4,770 | C-0147 | Rs 4,780 |

**Who needs the answer.** The marketing lead needs it to decide which Retail-Core members the member
team protects, and the head of Retail-Plus needs to see the list keep their rule. A list with the wrong
count, or with members picked by nothing the business chose, spends the member team's calls on the
wrong people.

**The questions on the way.**

- How many Q2 orders did each Retail-Core member place, and where do the ties fall?
- How many members does each rule ship when the list is ranked by orders alone?
- Why does that rule ship the number it ships?
- Which second key decides between members with the same number of orders, and how many members does the list ship then?
- How many members do the two lists share, and how far apart are they in rupees?
- Is frequency falling in Retail-Core, and what do you tell the marketing lead?

**What you post.** One line of ten letters in item order, no spaces, items 1 to 7 from the notebook's
markers and items 8 to 10 from this brief, in this shape:

```
Post exactly this shape: xxxxxxxxxx
```

Beside the letters, post one sentence for the marketing lead in your own words: the rule, the count it
ships, and how far the frequency list sits from the list ranked by revenue.

---

## Step 1. How many Q2 orders did each Retail-Core member place, and where do the ties fall?

This comes up at work whenever a list is ranked on how often customers buy, in place of how much they
spend.

Marker 1 in the notebook.

### Q1. Which expression counts a member's Q2 orders?

Which expression counts a member's Q2 orders?

a) `count(*)`, which counts one for every order row the member placed

b) `count(DISTINCT o.customer_id)`, so no member is counted twice

c) `count(DISTINCT o.order_date)`, so a day with two orders counts once

d) `count(DISTINCT date_trunc('month', o.order_date))`, the months with an order

## Step 2. How many members does each rule ship when the list is ranked by orders alone?

This comes up at work whenever a rule written for one metric is applied to another, and its count has to
be read again.

Marker 2 in the notebook.

### Q2. Which window puts the head of Retail-Plus's rule on the orders count?

The marketing lead wants the same rule as the head of Retail-Plus, now on the number of Q2 orders.
Which window puts that rule on the orders count?

a) `row_number() OVER (ORDER BY q2_orders DESC, customer_id)`

b) `rank() OVER (ORDER BY q2_orders DESC)`

c) `dense_rank() OVER (ORDER BY q2_orders DESC)`

d) `rank() OVER (ORDER BY q2_orders)`

## Step 3. Why does that rule ship the number it ships?

This comes up at work whenever a stakeholder who asked for fifty receives more and wants the reason in one
sentence.

Marker 3 in the notebook.

### Q3. Why does the head's rule, on orders alone, ship more than fifty members?

Why does the head of Retail-Plus's rule, applied to the orders count alone, ship more than fifty
members?

a) 24 members placed three or more orders, and the 27 members with two orders all share the 25th place

b) The rule skips a number after every tie, and those skipped numbers count as extra members on the list

c) The rule numbers the 27 two-order members 25 to 51 by id, one place each, and keeps every one of them

d) The 45 members with one order share a place, and the rule adds one of them to make the list even

## Step 4. Which second key decides between members with the same number of orders, and how many members does the list ship then?

This comes up at work whenever a ranking needs a second key to decide between members level on the first,
which is a business choice with a reason.

Marker 4 in the notebook, then item 8 here.

### Q4. Which ORDER BY ranks by orders first, then lets revenue separate members with the same orders?

Which ORDER BY ranks by orders first, then lets revenue separate members with the same orders?

a) `ORDER BY q2_orders DESC, customer_id`

b) `ORDER BY q2_orders DESC, q2_revenue DESC`

c) `ORDER BY q2_revenue DESC, q2_orders DESC`

d) `ORDER BY q2_orders DESC`

### Q8. Which member does a rule that lets the id decide leave off, and what does it cost?

`row_number() OVER (ORDER BY q2_orders DESC, customer_id)` also ships fifty, and it lets the customer
id decide among members with the same number of orders. Using the table of two-order members, which
member does it leave off, and what does that cost?

a) C-0070, who booked Rs 2,730, the least of the 27, so the id rule and a spend rule leave off the same member

b) C-0092, who booked Rs 2,950, since they are the member a list ranked by revenue alone also leaves off

c) Nobody who matters, since every two-order member booked within a few hundred rupees of the others

d) C-0147, who booked Rs 4,780, while C-0070 on Rs 2,730 stays, because the highest id is the one cut

## Step 5. How many members do the two lists share, and how far apart are they in rupees?

This comes up at work whenever a team argues over two definitions and first measures how much the answer
changes.

Marker 5 in the notebook, then item 9 here.

### Q5. Which query counts the members who are on both lists?

Which query counts the members who are on both lists?

a) An INNER JOIN of the two lists on customer_id, counting the rows it returns

b) A LEFT JOIN from the revenue list to the frequency list, counting all the rows it returns

c) UNION ALL of the two lists, counting the rows

d) The revenue list EXCEPT the frequency list, counting the rows it returns

### Q9. Which route confirms the number of members on both lists a second way, and what does it give?

Kavya Nair, the senior analyst who checks every number before it leaves the team, wants the number of
members on both lists confirmed by a route that shares no code with marker 5's query. Which route does
that, and what does it give?

a) UNION ALL of the two lists' ids, 100 rows, less one list's 50, which gives 50 shared

b) The frequency list's members with two or more Q2 orders, counted with a filter, which gives 50

c) A UNION of the two lists' ids, 51 different members, so 50 plus 50 less 51 gives 49

d) Retail-Core's 96 buyers less the 45 who are on neither list, which gives 51 shared

## Step 6. What do you tell the marketing lead?

This comes up at work whenever an argument over a definition ends with someone saying what changes, by how
much, and which choice they recommend.

Markers 6 and 7 in the notebook, then item 10 here.

### Q6. How far apart are the two lists in the Q2 revenue they carry?

How far apart are the two lists in the Q2 revenue they carry?

a) Rs 40, the difference between the Q2 revenue the two lists carry

b) Rs 2,950, the Q2 revenue of the frequency list's fiftieth member

c) Rs 1,09,900, the Q2 revenue of the 27 members with two orders

d) Rs 2,980, the Q2 revenue of the revenue list's fiftieth member

### Q7. Which sentence goes to the marketing lead?

Which sentence goes to the marketing lead?

a) "Rank Retail-Core by orders alone under RANK: the list runs past fifty, which honours the tie rule and protects the frequency that fell."

b) "Rank by orders with Q2 revenue as the second key: fifty ship, and the list is almost the revenue list, member for member and in rupees."

c) "Rank Retail-Core with DENSE_RANK on orders, so that every member who ordered the same shares a place on the list."

d) "Keep the revenue list, since ranking by orders would drop the members whose quarters carry the most revenue."

### Q10. Is frequency falling in Retail-Core too, and which measure says so?

The marketing lead asked for the frequency list "before it spreads". Before the sentence goes out,
Kavya asks whether Retail-Core's frequency has started to fall from Q1 to Q2 the way Retail-Plus's did.
Which measure answers it, and what does it give?

a) Total Retail-Core orders, Q1 against Q2: 199 then 193, so frequency is falling there too

b) Orders per buying member, Q1 against Q2: 2.01 then 1.95, so it falls as Retail-Plus's did

c) Members with one Q2 order, 45 of 96, nearly half, so frequency in Retail-Core is already low

d) Orders per buying member, Q1 against Q2: 1.95 then 2.01, so it has not started to fall yet

## Which rules does the case keep?

- The data is the warehouse's orders and customers tables, read where they live; nothing is exported.
- Every count in your sentence says which rule produced it.
- Work in pairs or alone; if you pair, both names go on the post and each of you can explain every
  letter.

# Which answers hold in the escalated case on Monday's file, and why?

Answers: 1c 2b 3d 4a 5d 6a 7c 8b 9b 10a

Meera's chief of staff asked for the file Monday's growth review opens: the revenue tree by segment
for both quarters, the protect list of fifty Retail-Plus members with a lookup by id, and the
front-page number with its trend, which a director will change in the room. The warehouse holds one
row per order and books Rs 10,00,00,000 in Q1 (April to June 2026) and Rs 9,84,00,000 in Q2 (July to
September 2026). The customer table holds one row per customer who ordered in the half-year; the raw
export holds one row per payment, with the order's amount on every row of that order. Retail-Plus is
Kalpa's paid membership tier, and C-0195 is a Retail-Plus member with no orders in the two quarters.
The escalated case asks each learner to build all three deliverables alone in fifty minutes in
`notebooks/C2_W02_D05_ex1_escalated_case_STUDENT.ipynb`, ten lettered choices in five parts, and to
say what the file can be trusted for. The executed solution,
`C2_W02_D05_ex1_escalated_case_solution_STUDENT.ipynb` in this folder, runs every key. Four of the
ten items are design items: 6, 7, 8 and 10.

**Who needs the answer.** You, before the debrief, checking your ten letters and your two sentences.
The debrief replays the room's wrong numbers aloud, and a line you cannot defend here is the one a
director takes apart on Monday.

**The questions on the way.**

- Which idea does the escalated case test: every check of the day, with no trainer choosing the step?
- Which numbers should you have reached in each of the five parts?
- Why does each of the ten keys hold, from one row per order to the warehouse's own query?
- What do two good sentences to the chief of staff say?
- Which wrong numbers does the debrief replay, and what replaces each?
- Where does a release note like this one come up again at work?

## Which idea does the escalated case test: every check of the day, with no trainer choosing the step?

The case runs the whole day at once: say the grain and count each order once, rank inside the segment
the ask names, look up with an exact match that says when an id is missing, measure a change on the
earlier quarter and print its share, tie each part to a number from somewhere else, and ship only the
parts whose checks pass. No step is new; what is new is that nobody tells you which step comes next.

## Which numbers should you have reached in each of the five parts?

| Part | Number | What it means |
|---|---|---|
| 1 | Q1 Rs 10,00,00,000 on 538 orders and Q2 Rs 9,84,00,000 on 462, to the rupee; Retail-Plus customers who ordered, 91 in Q1 and 76 in Q2; Retail-Plus orders per customer 2.36 and 1.84 | The tree ties to Finance, and the Retail-Plus fall sits in how often members buy |
| 2 | Fifty members from C-0152 at Rs 25,840 down to Rs 8,580; the lookup returns Rs 25,840 for C-0152 and "not in the table" for C-0195 | The list is the right fifty, and the lookup fails visibly |
| 3 | All segments down 1.6 percent; all except Business down 17.3 percent, 0.8 percent of Q2 revenue; Retail-Plus down 29.4 percent, 0.4 percent of Q2 revenue | Each scope prints its own change and share, measured on Q1 |
| 4 | The tree and the front page ship; the protect list is held, because its source table does not match the raw export counted once | The list waits for a fresh export, with a note saying what does not tie |
| 5 | Filtered to Mumbai, the foot shows Rs 1,56,790 for eleven members; the warehouse's query gives both quarters to the rupee | Two second routes agree with the file |

## Why does each of the ten keys hold, from one row per order to the warehouse's own query?

### Q1. Which line leaves exactly one row per order?

The raw export holds one row per payment.

The key is c, `orders = raw.drop_duplicates("order_id")`. Naming the key keeps the first row of each
order and drops every repeat, instalment or gateway copy alike: 1,000 rows, one per order.

- a, `orders = raw.drop_duplicates()`: removes only rows identical in every column, so the 400
  instalment orders keep both rows, since their rows differ in the amount paid.
- b, `orders = raw.drop_duplicates("customer_id")`: keeps one order per customer and loses the rest.
- d, `orders = raw[raw["paid_amount"] > 0]`: drops nothing that repeats and keeps every payment row.

### Q2. How are customers counted in each segment and quarter?

The tree's first leaf is the customers who ordered.

The key is b, `("customer_id", "nunique")`. A customer with three orders in a quarter is one
customer, so the count is of distinct ids; Retail-Plus reads 91 in Q1 and 76 in Q2, as the warehouse
does.

- a, `("customer_id", "count")`: counts rows, so a customer with three orders counts three times.
- c, `("order_id", "nunique")`: counts orders, which is the tree's second number, not its first leaf.
- d, `("customer_id", "size")`: counts rows too, missing values included.

### Q3. Which line gives the fifty Retail-Plus members with the highest revenue?

The ask is the top fifty inside Retail-Plus.

The key is d, `protect = plus.nlargest(50, "revenue")`. It ranks inside the segment the ask names and
keeps the fifty largest, from C-0152 at Rs 25,840 to Rs 8,580.

- a, `protect = table.nlargest(50, "revenue")`: ranks every segment together, so the 39 Business
  buyers take most of the places.
- b, `protect = plus.nsmallest(50, "revenue")`: keeps the fifty members who spent least.
- c, `protect = plus.head(50)`: keeps the first fifty rows in id order, which is no ranking at all.

### Q4. Which lookup returns a member's revenue, or a sentence when the id is not in the table?

The lookup must answer for the member asked for, or say the id is missing.

The key is a, `lookup = lambda m: by_id["revenue"].get(m, "not in the table")`. An exact lookup by
id with a not-found value, the notebook's form of `=XLOOKUP(id, ids, revenue, "not in the table")`.

- b, `lookup = lambda m: by_id["revenue"].iloc[by_id.index.searchsorted(m, "right") - 1]`: finds the
  largest id not above the one asked for, which is VLOOKUP with its fourth argument left out, and
  returns C-0194's Rs 16,740 for C-0195.
- c, `lookup = lambda m: by_id["revenue"].iloc[0]`: returns the first member's revenue for every id.
- d, `lookup = lambda m: by_id["revenue"].asof(m)`: another approximate match, with the same
  neighbour for a missing id.

### Q5. Which is the change from Q1 to Q2?

The card measures the change on the earlier quarter.

The key is d, `(q2 - q1) / q1 * 100`. For all segments it reads down 1.6 percent; for Retail-Plus,
down 29.4 percent.

- a, `(q2 - q1) / q2 * 100`: divides by the current quarter, which reads Retail-Plus down 41.7
  percent where it fell 29.4.
- b, `(q1 - q2) / (q1 + q2) * 100`: measures the fall against both quarters together, a base no card
  names.
- c, `q2 / q1 * 100`: a ratio of about 98 that a card would misprint as a percentage change.

### Q6. Which share goes beside the number?

A design item. The share tells a director how much of the company the scope is.

The key is a, `q2 / company_q2 * 100`. The scope's Q2 as a share of the company's Q2: 0.4 percent for
Retail-Plus and 0.8 percent for all except Business, so a large percentage fall on a small base reads
as small in rupees.

- b, `q2 / (q1 + q2) * 100`: shares out the scope's own two quarters, which says nothing about its
  size in the company.
- c, `(q2 - q1) / company_q2 * 100`: the change's share of company revenue, a useful number that is
  not the scope's base.
- d, `q2 / q1 * 100`: the same ratio as item 5's option c.

### Q7. Which comparison says whether the list's source table ties?

A design item. The list comes from the customer table, a different export from the one part 1 tied.

The key is c, the customer table's orders and revenue against the raw export counted once. The raw
export counted once ties to the warehouse to the rupee, so comparing the customer table with it is
comparing the list's source with Finance. On the day's files the two do not match, so the list's
source does not tie.

- a, `source_ties = len(table) == 300`: counts the table's rows against a number the table itself
  gave, which cannot fail.
- b, comparing the list's total with the same fifty taken again: compares the list with itself.
- d, `source_ties = int(table["revenue"].sum()) > int(seg_q["Q2"].sum())`: compares a half-year with a
  quarter, which any half-year passes.

### Q8. Which rule turns the checks into Monday's release?

A design item. Each part sits on its own checks: the tree and the front page on the tree's tie, the
protect list on its source and its lookup.

The key is b, ship a part only when every check behind it passes. The tree and the front page ship,
and the protect list is held until its source ties.

- a, ship a part when two or more checks pass anywhere: a release is not a vote, since each check
  guards a different part.
- c, ship a part only when every check in the file passes: one failing source would hold the tree and
  the card, which tie.
- d, ship everything because every number is a formula: recalculating is not the same as being right.

### Q9. Which total is what SUBTOTAL(109) shows at the foot of the list filtered to Mumbai?

The foot must add only the rows on screen.

The key is b, the revenue of the protect-list rows whose city is Mumbai: Rs 1,56,790 for eleven
members. A SUMIFS on the city, which ignores the filter, agrees.

- a, the whole list's revenue: Rs 7,14,890, which is what a SUM at the foot shows.
- c, the rows the filter hid: the opposite of what is on screen.
- d, every Mumbai customer in every segment: the foot's range is the fifty list rows.

### Q10. Which query is the warehouse's own route to the two quarters of booked revenue?

A design item. The second route has to be able to disagree with the tree.

The key is a, `SELECT quarter, sum(amount) AS revenue FROM orders GROUP BY quarter`. The warehouse's
orders table never saw the export, and it gives Rs 10,00,00,000 and Rs 9,84,00,000, the tree's
numbers to the rupee.

- b, the payments joined to orders and summed: that is collected money, which differs from booked.
- c, `count(*)` by quarter: counts orders, a number the tree can match without its rupees being
  right.
- d, the same sum restricted to delivered orders: booked revenue counts every order at the price
  charged, returned and cancelled ones included.

## What do two good sentences to the chief of staff say?

"The tree and the front page tie to Finance to the rupee: Q2, July to September 2026, is Rs 9.84
crore, down 1.6 percent on Q1's Rs 10.00 crore, and the card prints its scope and base whenever a
director changes it. The protect list is held until the data platform lead sends a customer table
that ties to the warehouse, and its lookup says "not in the table" for any id it does not hold."

## Which wrong numbers does the debrief replay, and what replaces each?

| The wrong number | Where it came from | What replaces it |
|---|---|---|
| Rs 11,66,786 an order for Business | A per-customer column averaged in the pivot | Rs 10,45,740, revenue over orders |
| Rs 39.41 crore for the half-year | A Sum over payment rows | Rs 19.84 crore, each order once |
| Rs 39,40,57,740 | Remove Duplicates, then Sum | The same count by order id |
| C-0194's Rs 16,740 for C-0195 | An approximate match | "not in the table" |
| Rs 19.84 crore with no months | A card with no period | Rs 9.84 crore for Q2, down 1.6 percent on Q1 |
| Retail-Plus down 41.7 percent | The change divided by Q2 | Down 29.4 percent, measured on Q1 |
| Rs 7,14,890 for Mumbai | SUM under a filter | Rs 1,56,790 for eleven members |

## Where does a release note like this one come up again at work?

Every report that leaves the team for a meeting it cannot attend: a monthly pack for Finance, a
dashboard refresh, a model's scores sent to a business team. Each part carries its own checks, the
note ships what passed and names what waits and why, and the stakeholder learns which numbers to
quote before anyone quotes a wrong one.

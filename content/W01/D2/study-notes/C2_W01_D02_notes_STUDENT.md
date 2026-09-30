# Which branch moved from Q1 to Q2?

**Week 1, Tuesday. Study notes, read after the session.** Meera Raghavan, Kalpa Retail's CEO, asked
it in her own words: Q2 came in below Q1, so are we losing customers, or are the ones we have buying
less? The day climbs to her answer in six chapters, each asking the question the answer before it
raised. Every chapter weighs two to four ways of answering, sizes them, picks one, and reaches the
same number a second way. Reading time: about 40 minutes.

---

## What will you be able to do once you have read these notes?

1. You can check whether a drop is real before explaining it, and choose between closed quarters,
   the same weeks of each, a rate per week and last year's quarter, saying what would switch you.
2. You can split a change in revenue into customers, orders per customer and revenue per order, show
   that they multiply back, and put rupees on each branch with a bridge whose order you state.
3. You can decide between copying code, writing a function and grouping by a key, and roll a rate up
   from segments with its weights.
4. You can say how much of a blended rate's change came from the mix and how much from behaviour
   inside each segment.
5. You can test a stakeholder's claim in its own terms, catch a helper that drops a group, and judge
   a segment against the business it belongs to.
6. You can hand over a cause as a hypothesis with a ceiling, tested on timing, a comparison segment
   and the channel it predicts, and name the data that would settle it.

---

## Where does Tuesday sit in the week, and what does it lean on?

Kalpa Retail is the first business most of the room has worked in. How a retailer earns, who owns
which lever and why periods are compared like with like is told in Monday's domain dossier,
`content/W01/D1/study-notes/C2_W01_D01_domain_retail_STUDENT.md`. Today uses four of its parts: section 2 on Retail-Plus, the
paid tier, and why memberships buy frequency; section 5's revenue tree, average order value (whose
trap is today's chapter 4) and frequency; section 5's same-store sales, which is chapter 1's matched
windows; and section 4 on who asks for which number.

```mermaid
flowchart LR
    M["<b>Monday</b><br/>what is sales made of"] --> T["<b>Tuesday</b><br/>which branch moved"]
    T --> W["<b>Wednesday</b><br/>can the numbers be trusted"]
    W --> H["<b>Thursday</b><br/>is it real, what goes to Meera"]
    H --> F["<b>Friday</b><br/>the week rebuilt without an assistant"]
    classDef today fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class T today
```

Whether the export itself can be trusted waits for Wednesday, when Finance
compares its books with the dashboard; tomorrow's reconciliation may change tonight's numbers.
Whether the differences found today are real waits for Thursday.

---

## Which picture holds the whole day?

```mermaid
flowchart LR
    subgraph LAD["the six chapters"]
        direction TB
        R1["1 is the drop real?"] --> R2["2 which branch moved?"]
        R2 --> R3["3 which segment moved?"]
        R3 --> R4["4 did customers pay more?"]
        R4 --> R5["5 were customers lost?"]
        R5 --> R6["6 did the button do it?"]
    end
    subgraph TREE["the tree, Q1 to Q2"]
        direction LR
        V["<b>revenue</b><br/>Rs 2.10 to 1.87 cr"] --> C["<b>customers</b><br/>69 to 69"]
        V --> F["<b>orders per customer</b><br/>1.65 to 1.25"]
        V --> O["<b>revenue per order</b><br/>Rs 1.84 to 2.17 lakh"]
    end
    LAD --> TREE
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef moved fill:#FBE3EA,stroke:#D63A6A,color:#1A0F5C
    class R6 bet
    class F moved
```

Read the ladder from the top: each chapter answers a question that must be settled before the next
one is worth asking. The tree beside it is Monday's tree with Tuesday's numbers written in, and the
shaded branch is the one that moved. One sentence to Meera runs through every chapter: it starts as
"revenue fell" and ends as a claim with its evidence, its caveat and its ceiling.

The eight lines the day comes down to:

1. Confirm the drop on matched windows before you explain it.
2. A rate without its denominator is a rumour.
3. Decompose along the tree: customers, orders per customer, revenue per order.
4. Missing means unknown until someone chooses a default and writes down why.
5. Roll a rate up with its weights; never average the averages.
6. A blended rate can move while no segment moves; split mix from rate.
7. A function returns its answer; count the groups in and the groups out.
8. Name the cause as a hypothesis, with its ceiling and the evidence that would settle it.

---

## Chapter 1. Did revenue really fall from Q1 to Q2, and by how much, once both sides cover the same weeks?

**Who needs the answer.** Meera decides whether Marketing's Rs 12 crore acquisition request is
urgent, and the request rests on a slide saying revenue fell by a quarter. Overstate the fall and
crores move in a hurry on a lever nobody has checked; understate it and a real leak runs another
quarter.

**The questions on the way.**

1. Which of four ways should size the fall, and what does each leave out?
2. How far did revenue fall between the two closed quarters?
3. Why does Marketing's slide say 25.9 percent?
4. How far apart are the quarters per week, with the window stated?
5. What do the same eleven weeks of each quarter say?
6. Does adding revenue up by month give the same fall?

**The need.** The metric is the change in booked revenue, every order placed before any
cancellation or return, between two quarters. Kalpa's financial year opens in April, so Q1 is April
to June and Q2 July to September, and both have closed.

**Who else faces this.** Retailers compare like with like on purpose. DMart reports like-for-like
growth, sales growth counted only on stores open in both periods, and only on stores open at least 24
months, 8.1 percent in FY26. Target defines comparable sales, its own like-for-like measure, against a
prior period of equivalent length, and its 53-week fiscal 2023 carried an extra week worth
$1,715 million. The National Retail Federation's 4-5-4 calendar gives comparable months the same
weeks and weekends.

### Which of four ways should size the fall, and what does each leave out?

| Option | Rows read | Answer | What it leaves out |
|---|---|---|---|
| A. Closed quarters as totals | 200 | minus 11.0 percent | Nothing, once both quarters have closed |
| B. The same 11 weeks of each | 167 | minus 17.0 percent | The last two weeks of each quarter |
| C. A rate per day or per week | 200 | minus 11.9 percent per day | Where the weeks sit, once a quarter is cut |
| D. The same quarter last year | 0 | cannot run | Everything, until last year's export arrives |

What separates them is the question each answers and what each leaves out. The call is A, because
both quarters closed at 13 weeks each. Q2 still open would switch it to B, and a question about the
monsoon would switch it to D and a data request.

### How far did revenue fall between the two closed quarters?

A dictionary keyed by quarter adds revenue in one pass. Revenue fell from Rs 2,10,00,000 to
Rs 1,87,00,000, which is Rs 23,00,000 and 11.0 percent, on two windows of 13 weeks.

### Why does Marketing's slide say 25.9 percent?

Marketing's Q2 figure is a dashboard tile read on 15 September: Rs 1,55,59,950 against all of Q1
gives minus 25.9 percent, with correct arithmetic. The tile holds 11 weeks against 13, and the check
that catches it in a minute is the first and last order date of each window. The fix is the closed
quarters, and a bridge shows where the extra fall went: the last two weeks of Q2, which the tile had
not reached, held 16 orders and Rs 31,40,050. The fall Meera acts on shrank from Rs 54,40,050 to
Rs 23,00,000.

### How far apart are the quarters per week, with the window stated?

A rate per week puts unequal windows on one scale if it names its numerator, its denominator and its
window: Rs 16,15,385 a week in Q1 against Rs 14,14,541 on the tile, minus 12.4 percent. It fixes the
length of the two windows and leaves their position, so the tile's first eleven weeks still stand
against all of Q1. Per day on the closed quarters the fall is 11.9 percent, because Q2 has 92 days and
Q1 has 91.

### What do the same eleven weeks of each quarter say?

The first eleven weeks of each quarter, 1 April to 16 June against 1 July to 15 September, give
minus 17.0 percent. That differs from the per-week minus 12.4 because a few lakh-sized Business
orders make weeks lumpy, so which weeks a cut includes moves the answer. While a quarter is open, send
the same weeks of both with the cut date in the sentence; once it closes, compare closed quarters.

### Does adding revenue up by month give the same fall?

Key the accumulator by the month in the order date instead of the quarter field, and add the months
back: April to June give Rs 2,10,00,000 and July to September Rs 1,87,00,000, the same minus 11.0
percent. Agreement shows that the quarter field and the dates give each quarter the same total, in
aggregate only, since two mislabelled orders of equal value would cancel out. Use the month key once a
question moves inside a quarter.

So the drop is real: revenue fell 11.0 percent, Rs 23,00,000, between two closed quarters of 13
weeks each, and Marketing's 25.9 percent compared 11 weeks with 13.

---

## Chapter 2. Which branch of the revenue tree carries the Rs 23,00,000 fall: customers, how often they buy, or what each order is worth?

**Who needs the answer.** Meera decides which owner gets the problem. Customers belong to Marketing
and cost acquisition spend; orders per customer belong to the tier and product owners, working on
people already won; revenue per order belongs to merchandising, the team that chooses the range and
the pack sizes; price and discounts belong to Finance with Marketing. A wrong split sends crores to the
wrong owner for a quarter.

**The questions on the way.**

1. Which of four ways should split the fall between the branches?
2. Did the number of customers fall?
3. Which leaf of the tree moved against Kalpa?
4. How many rupees does each branch carry, one leaf at a time?
5. What share of orders carried a discount, once a missing discount counts as unknown?
6. Does a split that chooses no order put the fall on the same branch?

**The need.** Meera asks whether Kalpa is losing customers or whether the ones it has buy less. The
metric is the rupees each branch carries of the Rs 23,00,000 fall.

**Who else faces this.** Blinkit, the quick-commerce app, reports orders and net average order
value, the average order after discounts, side by side: 273.9 million orders at Rs 525 in the fourth
quarter of FY26, about Rs 14,386 crore of net order value. Walmart splits U.S. comparable sales into
transactions and average ticket, the average spend per transaction, every quarter: in the quarter to
31 July 2026, up 2.6 percent, made of transactions up 1.5 and ticket up 1.1.

### Which of four ways should split the fall between the branches?

| Option | Frequency is charged | Depends on order? |
|---|---|---|
| A. Leaf percentages only | no rupees, since percentages do not add | no |
| B. A bridge in the tree's order | minus Rs 51,57,895 | yes |
| B, with the order reversed | minus Rs 60,88,372 | yes |
| C. A symmetric logarithmic split | minus Rs 55,88,480 | no |
| D. Customer by customer | 69 rows to read before any total | no |

The call is B with its order written beside it, because it adds exactly and a CEO can follow it, and
in every order frequency carries the fall. A split that Finance rebuilds every month would go
symmetric, so nobody argues about order, and "which customers?" goes to D.

### Did the number of customers fall?

No. A dictionary of customer ids per quarter counts 69 customers in both, while orders fell from 114
to 86.

### Which leaf of the tree moved against Kalpa?

Orders per customer fell from 1.65 to 1.25, down 24.6 percent, while revenue per order rose from
Rs 1,84,211 to Rs 2,17,442, up 18.0 percent. The leaves multiply: 1.000 times 0.754 times 1.180 is
0.890, the revenue ratio. Adding the percentages would have said minus 6.6.

### How many rupees does each branch carry, one leaf at a time?

The bridge moves one leaf at a time to its Q2 value, customers first, holding the leaves not yet
moved at Q1: customers Rs 0, frequency minus Rs 51,57,895, order value plus Rs 28,57,895. Marketing's
branch carries no rupees on this file.

### What share of orders carried a discount, once a missing discount counts as unknown?

Meera's fourth branch is price, and Marketing's monsoon plan starts from the share of orders carrying
a discount. Indexing the missing field raises `KeyError`, a runtime error that takes two minutes. The
trap is what the quick fix decides: `order.get("discount", 0)` reads every blank as zero, and 50.0
percent of Q2's orders carry a discount, 43 of 86, so Marketing extends the discount to "the other
half". The check splits the 43 without one: 17 record Rs 0 and 26 carry no field at all. The fix
writes the rule down, "absent means not recorded; reported separately; never counted as zero",
reports 71.7 percent over the 60 orders that record the field, gives the range the blanks allow,
50.0 to 80.2 percent, and bounds the branch: at Rs 150 on every Q2 order, the largest recorded, it
holds at most Rs 12,900 of a Rs 23,00,000 fall. Discounts leave the list of causes.

### Does a split that chooses no order put the fall on the same branch?

Yes. Split the fall symmetrically, each leaf taking a share in proportion to its logarithmic change,
so that no order is chosen at all: frequency minus Rs 55,88,480, order value plus Rs 32,88,480,
customers nothing. The Rs 4,30,585 between the two frequency figures is the part where frequency and
order value moved together. Keep the bridge for Meera; go symmetric when someone rebuilds the split
every month.

So the branch that moved is orders per customer, 1.65 to 1.25, which carries Rs 51,57,895 of the
fall in the tree's order; customers held at 69, and discounts can carry at most Rs 12,900.

---

## Chapter 3. Which of the four customer segments carries the fall in orders per customer, measured the same way for every segment and quarter?

**Who needs the answer.** The head of Retail-Plus, the paid membership tier, decides whether his tier
needs rescuing; his renewals are the metric of his job, so orders per member is his number. A wrong
answer costs a tier nobody protects, or a quarter spent fixing one that was fine.

**The questions on the way.**

1. Which way should compute the same numbers for eight groups: copy the loop, write a function, or
   group by key?
2. Does the function reproduce chapter 2's numbers?
3. How did Retail-Core move?
4. What did Business orders look like in Q2?
5. How far did orders per customer fall with the segments rolled up?
6. Does one pass grouped by quarter and segment agree with the function for all eight groups?

**The need.** He forwards a member's complaint about the app's reorder button and asks whether his
tier is slipping. The same five numbers are needed for four segments in two quarters.

**Who else faces this.** Costco reports its renewal rate, the share of members who pay again for
another year, twice: 92.3 percent in the United States and Canada and 89.8 percent worldwide at the
end of fiscal 2025, because a blend would hide where renewals are weaker.

### Which way should compute the same numbers for eight groups: copy the loop, write a function, or group by key?

| Option | Lines | Places to edit | Rows read |
|---|---|---|---|
| A. Copy the loop per group | 72 | 8 | 1,600 |
| B. A function, `tree_for(rows)` | 21 | 1 | 200 |
| C. Group by a key in one pass | 14 | 1 | 200 |

The call is B, because the same numbers will be asked for a channel, a month and delivered orders
before the day ends, and a function answers each with one line. Millions of rows with every group
needed at once would switch it to C, which is `groupby` in Week 2.

### Does the function reproduce chapter 2's numbers?

Yes. `tree_for` returns a dictionary, so its answer can go into a table, a chart or a check, and it
earns trust by reproducing chapter 2: 114 orders, 69 customers and 1.65 in Q1; 86, 69 and 1.25 in Q2.

### How did Retail-Core move?

`describe` returns a group's median, smallest and largest values and range. Retail-Core's 34
customers slipped from 1.12 to 1.06 orders each, minus 5.3 percent, and its median order fell from
Rs 2,325 to Rs 2,080.

### What did Business orders look like in Q2?

Business's median barely moved, Rs 9,83,780 to Rs 9,52,000, while one order of Rs 29,45,460 widened
the range by about 73 percent. Its 11 customers fell 15.0 percent, on three orders.

### How far did orders per customer fall with the segments rolled up?

Averaging the four segments' orders per customer gives 1.94 then 1.82, minus 6.0 percent on the
unrounded figures, 1.9385 to 1.8215: "frequency
is not the branch, Marketing may be right". A 2-customer segment votes as much as a 34-customer one.
The check is that a roll-up must reproduce the company figure, 1.65 and 1.25, and this one does not.
The fix is total orders over total customers, 114 over 69 then 86 over 69, minus 24.6 percent,
counting four groups in and 69 customers back.

### Does one pass grouped by quarter and segment agree with the function for all eight groups?

Yes. One pass over the 200 orders, adding into `totals[(quarter, segment)]`, gives the same revenue,
orders and customers as `tree_for` for all eight groups. It prints agreement and no segment's
numbers. Keep the function while groups are asked for one at a time; switch to the pass by key when
every group is needed at once on a large file.

So Retail-Core fell 5.3 percent and Business 15.0, neither near the company's 24.6, and the weighted
roll-up puts the rest in the two segments your own run of all four opens; that run names where orders
per member fell furthest.

---

## Chapter 4. Revenue per order rose 18 percent while revenue fell: did customers pay more, or did the mix of orders change?

**Who needs the answer.** Meera and Finance decide whether a price rise goes into the plan, on
Marketing's reading of the 18 percent. A wrong reading raises prices on customers who never paid
more, and costs volume in the tier whose orders already halved.

**The questions on the way.**

1. Which of four readings can put rupees on "customers paid more" and on "the mix changed"?
2. How many of the 28 lost orders were Retail-Plus?
3. Did any segment's own revenue per order rise 18 percent?
4. Did customers pay 18 percent more, or did the mix move the blend?
5. What is the rate part made of?
6. Does a back-of-envelope split, Business against everyone else, put the same share of the rise on
   the mix?

**The need.** Your run showed Retail-Plus: the same 22 members placed 26 orders in Q2 against 51 in
Q1. Marketing reads the 18 percent rise in revenue per order as customers paying more. Revenue per
order is a blend across segments whose orders differ several hundredfold: a Q1 Business order averaged
Rs 10,38,559 and a consumer order Rs 2,434.

**Who else faces this.** Swiggy reported the average order value of Instamart, its quick-commerce
store, up 14 percent in a quarter to Rs 697 in the quarter to September 2025, and put it down to
non-grocery categories and large packs taking a larger share of gross order value, the value of
orders before discounts. The average order grew because the mix of what people bought moved.

### Which of four readings can put rupees on "customers paid more" and on "the mix changed"?

A, the blended change, gives the size and no cause; B, each segment's own revenue per order, says
whether any segment paid more; C, the split of the rise into mix and rate, puts rupees on each and
makes them add to the Rs 33,231 rise; D, each segment's median order, gives the typical order and no
rupees. The call is C, built on B. Segments of similar order size, or shares that held, would make
mix negligible and B enough.

### How many of the 28 lost orders were Retail-Plus?

Twenty-five. Retail-Plus lost 25 orders, Business 3 and Retail-Core 2, while Student gained 2. The
orders that vanished were about three thousand rupees each.

### Did any segment's own revenue per order rise 18 percent?

No. Retail-Core fell 4.9 percent, Retail-Plus rose 7.0, Business 5.0 and Student 14.8, so the blend
rose further than any segment in it.

### Did customers pay 18 percent more, or did the mix move the blend?

"Revenue per order rose 18.0 percent, so customers pay 18 percent more" would put a price rise on
the tier whose orders already halved. The check is the per-segment table: no segment rose 18
percent. The fix prices Q2's order mix at Q1's segment rates, which gives Rs 2,07,112, so the mix
explains Rs 22,902 of the rise, about 69 percent, and the rate inside segments Rs 10,330, which leaves
the price rise without the evidence it rested on. Retail-Plus fell from 44.7 to 30.2 percent of
orders.

### What is the rate part made of?

Almost all Business: Rs 10,302 of the Rs 10,330, from 17 orders that each grew about Rs 52,000 on
average, one large order driving it, as chapter 3's range showed. The consumer segments' own revenue
per order moved by a few hundred rupees at most.

### Does a back-of-envelope split, Business against everyone else, put the same share of the rise on the mix?

Yes. Business's share of orders rose from 17.5 to 19.8 percent, and a Q1 Business order was worth
Rs 10,36,125 more than a consumer order, so the mix is about Rs 23,000, 69.3 percent of the rise. The
envelope uses no consumer rate, so it could have disagreed with the four-segment split, and it lands
within one percent. Report the four-segment split, which names each segment.

So customers did not pay more in any way that matters: about 69 percent of the rise in revenue per
order is mix, the small member orders that left, and most of the rest is Business's lakh-sized
orders.

---

## Chapter 5. Marketing says the flat count hides customers lost and replaced: were any lost, who slowed instead, and which segment fell most?

**Who needs the answer.** Meera decides whether to release the Rs 12 crore acquisition budget, which
Marketing now rests on churn, customers who stop buying, hiding in a flat count. A wrong answer spends
crores replacing customers who never left, while the ones who slowed keep slowing.

**The questions on the way.**

1. Which of four tests can see customers lost and customers new?
2. How many of Q1's 69 customers are missing from Q2?
3. Who placed fewer orders in Q2?
4. Which segment's orders per customer fell most?
5. Is Retail-Plus too small to matter at Rs 65,250?
6. Do each customer's first and last order dates find anyone lost or new?

**The need.** Marketing pushes back three ways: a flat count can hide churn replaced by new
customers; Retail-Plus is Rs 65,250 of a Rs 23 lakh fall; and last quarter's summary script says
Business fell most. The metric is retention and its mirror, new customers.

**Who else faces this.** Harvard Business Review summarised the studies behind the retention
argument: acquiring a customer costs 5 to 25 times more than retaining one, and Bain's Frederick
Reichheld found a 5 percent rise in retention lifting profits 25 to 95 percent. Those are estimates
across industries and say nothing about Kalpa's own costs, so the reply asks Finance for Kalpa's own
acquisition cost. Swiggy
reports its users and their frequency apart: in the quarter to September 2025 its monthly transacting
users, the people who ordered at least once in a month, rose 34.0 percent to 22.9 million while orders
per user a month fell from 4.53 to 4.10, a growing count beside a falling frequency that new users
alone could produce.

### Which of four tests can see customers lost and customers new?

A, compare the counts, cannot see churn because a count is net; B, the overlap of ids as sets, names
lost and new; C, customer by customer, also names who slowed; D, sign-ups from Marketing's CRM, its
customer database, sees only new customers, from a second system. The call is B, then C. One person
holding a store id and an app id would make the overlap invent churn, and the ids would need joining
first.

### How many of Q1's 69 customers are missing from Q2?

None. The overlap is 69 in both quarters, none only in Q1, none only in Q2.

### Who placed fewer orders in Q2?

Customer by customer, 23 placed fewer orders in Q2 and 18 of them are Retail-Plus members; 44
ordered exactly as often as before.

### Which segment's orders per customer fell most?

Retail-Plus, 2.32 to 1.18, minus 49.0 percent. The summary script runs cleanly and prints
`{'Retail-Core': -5.3, 'Business': -15.0}`, "most in Business". Its helper prints a warning for any
change above 30 percent and returns nothing, so Python hands back `None`, and `if ch and ch < 0`
drops every `None` without a word. Retail-Plus is exactly the change the script was written to flag,
and it vanished. The check counts groups in and out: four in, two back. The fix returns the change
every time and puts the flag in its own column: Retail-Plus minus 49.0 percent, Business minus 15.0
on three orders, Student plus 40.0.

### Is Retail-Plus too small to matter at Rs 65,250?

No. Business orders run to lakhs, so a consumer segment is judged against the consumer business:
Rs 2,28,820 to Rs 1,58,540, a fall of Rs 70,280, of which Retail-Plus is Rs 65,250, 93 percent, and 25
of the 28 lost orders. The rupee fall in Business is three orders out of twenty, each worth lakhs, so
one account ordering early or late moves it by lakhs.

### Do each customer's first and last order dates find anyone lost or new?

No one. Every first order in the export falls in Q1 and every last order in Q2, so none is new and
none lost, from the dates alone and without the quarter field. The route could have disagreed with
the overlap, and it adds a warning the overlap cannot: a first order in this export is only the
first since 1 April.

So no customer was lost and none is new. Twenty-three existing customers bought less often, 18 of
them members, and Retail-Plus fell 49.0 percent per member while the broken script said Business.

---

## Chapter 6. How much of the Retail-Plus fall can the broken reorder button explain, and what evidence goes in Meera's memo?

**Who needs the answer.** The head of Retail-Plus and engineering decide what to fix first, and Meera
decides what the board hears as the cause. Blame the button for everything and the tier keeps falling
for a reason nobody looked for; dismiss it and members keep failing to reorder.

**The questions on the way.**

1. Which of four tests of a cause run today, and in which order?
2. When did Retail-Plus orders drop below every Q1 month?
3. How many orders can the button have cost the tier?
4. Could a season that hit every customer explain the fall?
5. Did only the app channel fall, as a broken app feature predicts?
6. Does a pace corrected by Retail-Core's own change stay inside the ceiling?

**The need.** The head of Retail-Plus says the broken reorder button, six weeks old, caused the fall;
Meera wants one page of what we know and what we guess. The metric is Retail-Plus orders per week
before and after the break, taken at the complaint's word as 25 August.

**Who else faces this.** Sonos rolled out a redesigned app in 2024; its chief executive said the
app's rollout had required it to reduce its fiscal 2024 guidance, the revenue it had told investors to
expect, and its annual report set out short-term costs of up to $30 million to fix it.

### Which of four tests of a cause run today, and in which order?

A, before and after the break, can rule out the button as the whole story; B, a comparison segment,
Retail-Core, can rule out a season that hit everyone; C, the channel the cause predicts, can rule out
an app-only cause; D, the app's reorder logs, is a data request that settles it later. The call is A,
B and C now, timing first, and D requested today. A break date earlier than the complaint says would
flip A's verdict.

### When did Retail-Plus orders drop below every Q1 month?

In July, before the break. A counting function that takes any key, `count_by(rows, key)`, is chapter
1's accumulator grown: by month, Retail-Plus placed 9 orders in July against at least 13 in every Q1
month, while Retail-Core held level.

### How many orders can the button have cost the tier?

The hurried memo charges the button with the tier's whole quarter: 51 orders to 26, so "the button
cost 25 orders and Rs 65,250". Engineering fixes it, recovers a handful, and the real problem runs
another quarter. The check splits Q2 at the break and gives each side its window: 3.92 orders a week
in Q1, 2.29 before the break, 1.51 after. The fix charges the button with no more than the fall after
the break beyond the pace already set: at 18 orders in the 55 days before the break, the 37 days after
would have carried about 12.1 orders, and the tier placed 8, so the button explains at most about 4
orders, about Rs 12,400.

The ceiling rests on its baseline. Over only the 37 days just before the break, 19 July to 24 August,
the tier placed 15 orders; at that pace the 37 days after would have carried 15, and the ceiling is
7.0. Either way it sits far below the 25 orders the hurried memo charges, so the call holds, and the
memo names the baseline it used, the 55 days.

### Could a season that hit every customer explain the fall?

Not one that hit every customer. Retail-Core kept 95 percent of its Q1 orders against Retail-Plus's 51, so a season that hit
everyone does not fit. A season that hit members harder still fits, and last year's Q2 by segment
tests it.

### Did only the app channel fall, as a broken app feature predicts?

No. Every Retail-Plus channel fell, web 24 to 9, store 14 to 9, app 13 to 8, so an app-only cause does
not fit; something touched members in every channel.

### Does a pace corrected by Retail-Core's own change stay inside the ceiling?

Yes. Retail-Core placed 22 orders in the 55 days before 25 August and 14 in the 37 after, a pace
0.946 of what it had been. Scaled by that, the tier's expected 12.1 becomes 11.5 against 8 placed,
about 3.5 orders, which lands inside the ceiling of about 4, as a ceiling should. Write the ceiling in
the memo; bring the corrected route when someone argues for the season.

### What goes in Meera's memo, and what settles each hypothesis?

The memo's claim, as it goes to Meera and the head of Retail-Plus: "Revenue fell 11.0 percent between two closed quarters, Rs 2.10 crore to Rs 1.87 crore
on the export as it stands. Customers held at 69, all of them buying in both quarters, so acquisition
is not the branch that moved; orders per customer fell from 1.65 to 1.25. In behaviour the fall sits
in Retail-Plus, where the same 22 members placed 26 orders against 51, and revenue per order rose
mainly because those small orders disappeared. In rupees most of the fall is three fewer Business
orders, each worth lakhs, so one account's timing moves it by lakhs. The fall began in July, before the
button broke, and hit every channel, so the button explains at most about 4 orders. Two hypotheses
remain: the button deepened the fall after 25 August, settled by the reorder logs by week and the
release date; and something changed for members in July, settled by the tier's change log, renewals
and support tickets. Last year's Q2 by segment rules the season in or out."

So the button can explain at most about 4 of the tier's 25 lost orders on the 55-day baseline, 7.0
on the shorter one. The fall began in July and hit every channel, and the memo hands over two
hypotheses with the data that settles each.

---

## Did the story survive delivered orders and Marketing's new deck?

**Who needs the answer.** Meera, whose board pack counts only the orders that reached customers and
stayed, needs to know whether the branch and the segment hold on that definition; the head of
Retail-Plus needs to know whom to call first, while Marketing's new deck asks him to call his tier
healthy. A wrong answer sends the board a story that changes with the definition, or spends the
tier's calls on the wrong members.

**The questions on the way.**

1. Does the story survive when revenue counts only delivered orders?
2. Does Marketing's new deck hold, and whom does the tier call first?

### Does the story survive when revenue counts only delivered orders?

The escalated case reruns the ladder alone on delivered orders, the board's definition: orders
that reached the customer and were not returned. The drop survives, minus 11.3 percent; frequency
still carries the most rupees; Retail-Plus falls 42.6 percent per member. One branch moves that held
on booked orders: customers with a delivered order fall from 54 to 50. All 19 who left the delivered
count booked again in Q2 and had those orders cancelled or returned, so the branch is cancellations
and returns, to be split by reason between the teams that deliver orders and the teams that own the
product, and acquisition still has nothing to replace. On delivered orders the mix explains 44
percent of the rise in revenue per order, with Business's larger delivered orders carrying the rate.

### Does Marketing's new deck hold, and whom does the tier call first?

The second case takes Marketing's new deck apart in pairs. The members' 7 percent more per order
is one leaf, and the tier's leaves multiply to 1.000 times 0.510 times 1.070, about 0.55, so its
revenue fell about 45 percent; counted directly, Q2's tier revenue is 0.545 of Q1's. The web claim
fails because Retail-Core's web orders held at 13 and 12 on the same website, and the tier's call list
starts with the 7 members who went from three orders a quarter to one.

---

## Can you answer six questions without writing?

Pick a letter for each, then check the key.

1. Q1 covers 13 weeks and the Q2 tile covers 11, and Q2 is still open. The fair comparison is: a) the
   two totals as they stand, since both are called quarters; b) the two totals, with Q2 scaled up by 13
   over 11; c) the same weeks of both, with a rate per week beside them; d) the two medians, since a
   median is moved by neither the calendar nor a large order.
2. Customers are flat and orders per customer fell 24.6 percent. Marketing's acquisition plan targets:
   a) the branch that moved, since frequency needs new customers; b) the branch that did not move,
   since customers held at 69; c) revenue per order, which rose 18 percent; d) discounts, which half
   the orders seemed to lack.
3. Four segments average 1.94 orders per customer, and the company figure is 1.65. The difference
   comes from: a) rounding, since each segment's rate is shown to two decimals; b) a missing field that
   drops some orders; c) a window cut short on one quarter; d) weights, since small segments count once
   each.
4. A function prints its result and has no `return`. A variable set to its call holds: a) the printed
   text, as a string; b) `None`, the value of no return; c) zero, the default for a number; d) an
   error, raised at the call.
5. Some orders carry no discount field. In the share of orders with a discount they count as: a) no
   discount, so zero rupees each; b) the average discount of the recorded orders; c) unknown, reported
   separately; d) the largest discount anyone recorded.
6. From Monday: the mean order doubled and the median did not move. The first check is: a) read the
   top of the sorted list; b) recount the customers, since the mean divides by them; c) change the
   window to the full quarter; d) drop the largest order and recompute.

Key: 1c 2b 3d 4b 5c 6a. If you missed 1, reread chapter 1; 2, chapter 2; 3, chapter 3's roll-up; 4,
chapter 5's summary script; 5, chapter 2's discount; 6, Monday's notes on the average that lies.

---

## How do interviewers ask about a sales drop, and what does a strong answer say?

The tags mark how often a question comes up: [S] a staple asked everywhere, [F] frequent in GCC and
product screens, [SV] a service-major screen opener, [D] a differentiator.

**1. [S] Sales dropped 15 percent last month; how would you investigate?** Tested: order before
opinion. Strong: confirm the drop on matched windows and one definition; decompose along the tree into
customers, orders per customer and revenue per order; split by segment and channel; separate mix from
rate; then state a hypothesis with the evidence that would settle it, timing first. Weak: a list of
possible causes before the drop has been confirmed.

**2. [S] Why is a rate without a denominator meaningless?** Tested: whether numbers are read as
claims. Strong: a rate is a numerator over a denominator in a window, and without the denominator no
one can tell whether the top rose or the bottom shrank; "orders per customer fell" means little until
it says 86 over 69 against 114 over 69. Weak: "because it could be misleading", with no example.

**3. [F] Why does a function that prints instead of returning break a pipeline?** Tested: the
difference between showing and handing back. Strong: printing sends text to the screen and returns
`None`, so every caller receives nothing; a later filter can drop `None` silently and a group vanishes
from the summary; return the value and let the caller decide what to print. Weak: "printing is slower".

**4. [F] What has to match before a quarter-on-quarter comparison is fair?** Tested: like with like.
Strong: the same weeks on both sides, which means closed quarters once both have closed and, while
one is open, the same weeks of each with a rate per week beside them; the same definition of revenue,
the same segments, and the same denominators; and say that a quarter-on-quarter comparison still
carries the season, which only the same quarter last year removes. Weak: comparing whatever totals the dashboard shows.

**5. [D] Marketing insists the answer is acquisition and your data says frequency; how do you make the
case in the room?** Tested: judgement under pressure. Strong: agree the goal, show the tree with
customers flat and the id overlap showing none lost and none new, show frequency falling in one
segment, and offer the cheaper next step of testing the frequency hypothesis before spending on
acquisition. Weak: winning the argument without naming what evidence would change your mind.

**6. [F] Revenue fell 11 percent; how do you split the change between customers, frequency and order
value?** Tested: decomposition. Strong: compute the three branches for both periods, check that their
ratios multiply back to the ratio of the totals, then build a bridge in rupees that moves one branch at
a time from the start value to the end value, saying which branch moved first, or use the symmetric
logarithmic split so the answer does not depend on the order. Weak: three percentage changes added
together.

**7. [F] Revenue per order rose 18 percent while revenue fell; did prices go up?** Tested: mix against
rate. Strong: not necessarily, since an average across segments moves when the mix of orders moves;
price the later period's mix at the earlier period's segment rates to separate the two, and here
about 69 percent of the rise came from small Retail-Plus orders disappearing. Weak: "yes, prices went
up".

**8. [S] A field is missing on some records; do you fill it with zero?** Tested: missing against zero.
Strong: only if absent truly means zero and someone has written that down; otherwise report the count
of absent records separately, compute averages over recorded values, and bound the effect with the
largest plausible value. Weak: "yes, `.get` with a default of zero".

**9. [F] You have orders per customer for four segments; why can't you average them for the company
figure?** Tested: weighted roll-ups. Strong: a plain average counts each segment once regardless of
size; the company figure is total orders over total customers, and the check is that the roll-up
reproduces the known total. Weak: "the average is close enough".

**10. [SV] The customer count is flat quarter on quarter; does that prove no customers were lost?**
Tested: counts against identities. Strong: no, since losses can be replaced by new customers at the
same count; compare the sets of customer ids to count lost, retained and new. Weak: "yes, the number
did not change".

**11. [D] The design question: the same metrics are needed for every segment and quarter; do you
copy the code, write a function or group by a key?** Tested: sizing a choice. Strong: a function when
groups are asked one at a time and the definition may change, since there is one place to edit and it
answers any subset; one pass by key when the file is large and every group is needed at once; copying
means eight edits and one forgotten. Weak: "a function, because it is cleaner", with no cost named.

**12. [D] A stakeholder hands you a cause; how do you test it with the data you have and name the data
you need?** Tested: hypothesis discipline, with an order of tests and a point to stop. Strong: restate
the cause as a hypothesis and test what the file can test, timing first because it is cheap and can
rule a cause out, then a comparison group and whether the channel the cause lives in fell first and
alone; stop when the export can only cap the cause, here at about 4 orders on the 55-day baseline and
7.0 on the 37 days before the break, and name the data that would settle it, such as event logs and
release dates. Weak: accepting or rejecting the cause on instinct, or running every test at once.

---

## What do the day's words mean?

| Term | What it means here | Where it appeared | Example |
|---|---|---|---|
| Matched windows | Two periods of the same length compared, or both turned into a rate | Chapter 1 | Two closed 13-week quarters, a fall of 11.0 percent |
| Rate | A numerator over a denominator in a stated window | Chapter 1 | Rs 16,15,385 a week in Q1 |
| Like-for-like | A comparison that holds the outlets, the weeks and the weekends equal | Chapter 1; DMart, Target, NRF | Two closed 13-week quarters |
| Decomposition | A change split along the tree into branches that multiply | Chapter 2 | 1.000 times 0.754 times 1.180 is 0.890 |
| Bridge | A change in rupees moved one branch at a time from start to end | Chapter 2 | Orders per customer took away Rs 51,57,895 |
| Range | The largest value less the smallest, set by two orders alone | Chapter 3; `describe` | Business, Rs 15,80,940 in Q1 |
| Mix | Each segment's share of orders | Chapter 4 | Retail-Plus, 44.7 to 30.2 percent of orders |
| Rate part | The change inside segments, mix held still | Chapter 4 | Rs 10,330 of the Rs 33,231 rise |
| Default | The value used when a field is absent, with its written reason | Chapter 2 | Absent discount reported separately, never counted as zero |
| Function | A named block that takes inputs and returns one answer | Chapter 3 | `tree_for(rows)` returns a dictionary of the tree |
| Weighted roll-up | A company rate built from totals, so each group counts by its size | Chapter 3 | 114 orders over 69 customers is 1.65 |
| Mix against rate | An overall rate split into a change of weights and a change inside groups | Chapter 4 | Mix explains about 69 percent of the rise in revenue per order |
| Hypothesis | A named cause stated with the evidence that would settle it | Chapter 6 | The reorder feature, settled by the app's reorder logs |
| Ceiling | The most a cause could explain, given what else was already moving | Chapter 6 | The button, at most about 4 orders on its stated baseline |
| Id overlap | Customer ids in both periods, only the first, only the second | Chapter 5 | 69, 0 and 0 |
| Second route | The same answer reached by an independent method, one that could have disagreed | Every chapter | The symmetric split puts the fall on frequency, as the bridge did |

---

## What should you read next, and in what order?

| Order | What | Time | Why this one |
|---|---|---|---|
| 1 | Brit Institute, analyst case study interview questions, https://britinstitute.uk/blog/data-analyst-case-study-interview-questions (verified 29 Sep 2026) | 15 minutes | The sales-drop question as interviewers ask it |
| 2 | Exponent, data analyst interview questions, https://www.tryexponent.com/blog/top-data-analyst-interview-questions (verified 29 Sep 2026) | 20 minutes | The metric questions that follow it |
| 3 | Khan Academy, summarizing quantitative data, https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data (verified 29 Sep 2026) | 25 minutes | A typical value and a spread |
| 4 | Khan Academy, mean, median and mode review, https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/mean-median-basics/a/mean-median-and-mode-review (verified 29 Sep 2026) | 10 minutes | The median by hand, as `describe` computes it |
| 5 | Corey Schafer, "Python Tutorial for Beginners 8: Functions", https://www.youtube.com/watch?v=9Os0o3wzS_I (verified 29 Sep 2026) | 25 minutes | Defining a function that returns |
| 6 | Python documentation, "More Control Flow Tools", the section on defining functions, https://docs.python.org/3/tutorial/controlflow.html (verified 29 Sep 2026) | 15 minutes | Where a function without `return` is shown to give `None` |
| 7 | Python documentation, built-in types, `dict.get`, https://docs.python.org/3/library/stdtypes.html (verified 29 Sep 2026) | 5 minutes | What a default supplies when a key is absent |
| 8 | Corey Schafer, "Python Tutorial: Using Try/Except Blocks for Error Handling", https://www.youtube.com/watch?v=NIWwJbo-9_8 (verified 29 Sep 2026) | 20 minutes | The other way to meet a `KeyError`, and the decision hidden in the `except` |
| 9 | Python documentation, the statistics module, `median`, https://docs.python.org/3/library/statistics.html (verified 29 Sep 2026) | 5 minutes | The library median to check your own against |
| 10 | Harvard Business Review, Amy Gallo, "The Value of Keeping the Right Customers", https://hbr.org/2014/10/the-value-of-keeping-the-right-customers (verified 29 Sep 2026) | 5 minutes | What each branch costs to move |
| 11 | National Retail Federation, the 4-5-4 calendar, https://nrf.com/resources/4-5-4-calendar (verified 29 Sep 2026) | 5 minutes | How retailers keep periods comparable |
| 12 | Costco, fourth quarter fiscal 2025 results (renewal rates), https://www.sec.gov/Archives/edgar/data/909832/000090983225000093/costex9928-k92525.htm (verified 30 Sep 2026) | 5 minutes | A blended rate reported beside its segment |
| 13 | Walmart, earnings release for the second quarter of fiscal 2027, https://stock.walmart.com/_assets/_921ff28c537145729fbc2553b7f43fac/walmart/db/938/9996/earnings_release/Earnings+Release+(FY27+Q2).pdf (verified 30 Sep 2026) | 10 minutes | Transactions and average ticket, the tree in a results table |
| 14 | Swiggy, Q2 FY2026 shareholder letter, https://www.swiggy.com/corporate/wp-content/uploads/2025/10/Q2-FY2026-Shareholder-letter.pdf (verified 30 Sep 2026) | 10 minutes | An order value that rose on its mix, said as a mix |
| 15 | Target, fourth quarter and full year 2023 results, https://corporate.target.com/press/release/2024/03/target-corporation-reports-fourth-quarter-and-full-year-2023-earnings (verified 30 Sep 2026) | 5 minutes | A 53-week year and comparable periods of equal length |
| 16 | Sonos, third quarter fiscal 2024 results, https://investors.sonos.com/news-and-events/investor-news/latest-news/2024/Sonos-Reports-Third-Quarter-Fiscal-2024-Results/ (verified 30 Sep 2026) | 5 minutes | A company tying its reduced guidance to a broken app, in its own results |

---

## So which branch moved from Q1 to Q2?

Orders per customer. Revenue fell 11.0 percent between two closed quarters, Rs 2,10,00,000 to
Rs 1,87,00,000. Customers held at 69, every one of them buying in both quarters, so acquisition has no
lost customer to replace; orders per customer fell from 1.65 to 1.25, which carries Rs 51,57,895 of
the fall in the tree's order. In behaviour the fall sits in Retail-Plus, where the same 22 members
placed 26 orders against 51; in rupees most of it is three fewer Business orders, each worth lakhs,
which one account's timing moves. Revenue per order rose mainly because those small member orders
left, about 69 percent of the rise being mix. The fall began in July, before the reorder button broke,
so the button explains at most about 4 orders on the 55 days before the break, or 7.0 on the 37 days
just before it, and the memo asks for the tier's July change log, the app's reorder logs and last
year's Q2 by segment.

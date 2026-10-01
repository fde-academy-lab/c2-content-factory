# Can you build the growth team's whole Monday table alone, with both flags, one view and a guarded run, and post four numbers that hold?

The escalated case: fifty minutes, alone, straight after chapter 6. You work in
`notebooks/C2_W02_D04_ex1_escalated_case_STUDENT.ipynb`, which loads the warehouse and the
campaign platform's feed, asks for thirteen lettered choices in five parts with a check after each
part, and ends on four numbers.

> "One table, one row per customer, refreshed every Monday: how recently, how often, how much, the
> segment, whether the monsoon sale reached them, and the two flags we act on. And one view of it by
> month that we can put on a slide."
>
> The growth team, Kalpa Retail

Kalpa Retail's warehouse, its Postgres database, holds 1,000 orders placed between April and
September 2026, Q1 (April to June) and Q2 (July to September), worth Rs 19,84,00,000 at the prices
charged, and a customer list of 340 customers in four segments: Retail-Core and Retail-Plus, the two
consumer tiers, of which Retail-Plus is the paid membership; Student; and Business, Kalpa's sales to
companies. Spend is the value of a customer's orders at the prices charged, whatever became of each
order afterwards. The campaign platform's feed, `data/C2_W02_D04_exposure_STUDENT.csv`, lists the
customers the monsoon sale reached in August 2026 and the date it reached each one.

The six chapters built this table one question at a time. Here you choose every step yourself, and
each part's check tells you whether the table still holds before you move on. Kavya Nair, the senior
analyst on the team, lets the table go to the growth team only when every check has passed.

**The growth team's rules.**

- One row per customer on the list.
- A customer the feed names more than once was reached once, on the first date the feed gives.
- *Lapsed* means no order in the 60 days to the table's as-of date, which part 3 asks you to choose.
  A customer who never ordered is not lapsed, since there is nothing to win back; they get the
  first-order nudge instead.
- *Falling* is Wednesday's rule: spend lower in August than in July, and lower again in September
  than in August, each reading a real calendar month after the one before, so a month with no order
  breaks the run.

**Who needs the answer.** The growth team, which sends Monday's win-back codes and first-order
nudges from this table with nobody watching the run, and the marketing lead, who takes the reached
customers to the November budget meeting. A customer missing from the table gets no offer, a
customer counted twice inflates the campaign's case, and a flag counted from the wrong day sends a
code to someone who bought last month.

**The questions on the way.**

- Does the table hold every customer, with the three numbers each?
- Which customers did the sale reach, one row each, and does a second count agree?
- Who has gone quiet, and whose monthly spend is falling?
- How does spend move month by month in each segment?
- Will the table rebuild itself next Monday, stop when something breaks, and still work when the
  orders run to crores?

## Part 1. Does the table hold every customer, with the three numbers each?

Used at work on every table a team acts on person by person.

Eight minutes, the notebook's markers 1 and 2: which frame the table starts from, and what goes in
the frequency of a customer who never ordered. The check compares the table's rows with the customer
list and its spend with the warehouse.

## Part 2. Which customers did the sale reach, one row each, and does a second count agree?

Used at work whenever another team's feed is joined to a table people act on.

Ten minutes, markers 3 to 5: which argument applies the growth team's rule to a customer the feed
names twice, which promise the merge should carry, and which count, sharing no code with the rule or
the merge, should equal the customers marked as reached.

## Part 3. Who has gone quiet, and whose monthly spend is falling?

Used at work in every retention team's weekly list, where each flag must mean the same thing every
week.

Fourteen minutes, markers 6 to 9: the table's as-of date, the condition that marks a customer
lapsed, the previous monthly reading of the same customer, and the test that keeps a fall only when
the readings are July and August. The checks compare the win-back list and the falling flag with the
warehouse's own queries.

## Part 4. How does spend move month by month in each segment?

Used at work on the slide a growth review opens on.

Six minutes, marker 10: the call that builds the slide's view, months down the side and one column
per segment. The check compares the view's total with the warehouse.

## Part 5. Will the table rebuild itself next Monday, stop when something breaks, and still work when the orders run to crores?

Used at work wherever a scheduled job feeds a campaign or a report.

Twelve minutes, markers 11 to 13: the guard that stops a table that is no longer one row per
customer, the guard that catches recency counted to the wrong day, and the query step 1 should read
once the orders table grows to 5 crore rows. The checks run the refresh twice, break a copy on
purpose, and compare the query's answer with step 1's numbers.

## Which rules does the escalated case keep?

- The data is the warehouse and the one feed file; nothing needs cleaning first.
- Every part's check must pass before the next part starts. A check that fails is information: read
  what it compared, find the marker that caused it, and choose again.
- Never edit a check to make it pass.
- The support TA answers environment problems only.

## How do you post your thirteen letters and four numbers?

One line of thirteen letters in the order of the notebook's markers, then the four numbers the last
cell prints: the customers, their spend, the customers reached and the win-back list.

```
Post exactly this shape: xxxxxxxxxxxxx
```

Bring the CSV the notebook writes to `output/` to Friday.

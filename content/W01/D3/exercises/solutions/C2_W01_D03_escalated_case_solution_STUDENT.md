# Which answers hold in the escalated case on running the whole pass alone, and why?

Answers: 1d 2b 3c 4c 5a 6d 7a 8c 9b 10a

Alone, each learner cleans Kalpa Retail's export of Q1 and Q2 orders from the ERP, the enterprise
resource planning system Finance books orders in, reconciles it to the books, Finance's own record of
Q1 at Rs 1,90,00,000, recomputes Monday's revenue tree, revenue = customers x orders per customer x
revenue per order, and writes the note that Anand Iyer, the finance controller, asked for. The team's
dashboard, reading the same export, puts Q1 at Rs 2.1 crore, Rs 20 lakh above the books, and Marketing
asks whether Tuesday's fall in orders per customer for Retail-Plus, Kalpa's paid membership tier,
survives the clean file.

The notebook's own letters, in order, are in its solution notebook,
`exercises/solutions/C2_W01_D03_ex1_escalated_case_solution_STUDENT.ipynb`: 1c 2a 3d 4c 5b 6d 7b 8a 9c.

Four of the ten items are design items: 3, 5, 6 and 8.

## What does the escalated case test?

It tests the whole pass, alone, in the order that makes each step safe: the profile's three counts for
every field, present, convertible and distinct; the identity rule, which decides when two rows are one
order, keeping the copy whose amount converts; conversion with a rejects log that stays empty on this
file; the two flags, on the order with no status and on the largest Q2 order, records kept with a
question on them; rows and rupees reconciled to the books; Monday's tree recomputed; and the note in
under 120 words. The brief's items are the questions that arrive once the numbers land, so each asks
for a judgement the notebook's code does not make for you.

## Part 1. What can you tell Anand from the profile and the feed?

### Q1. Which one line goes to Anand after the profile?

The profile shows order_id distinct on 186 of 201 rows, amount convertible on 200 and status present
on 200, and Anand asks for one line he can rely on before the pass goes further; his analyst ties out
every figure, matching it to the books line by line.

The key is d, "The export counts some orders twice; the rupees wait on the rule". 201 rows for 186 ids
proves that some orders sit on more than one row. How many rupees they carry, and which figure is
right, waits for the identity rule and the bridge, the walk from one total to the other one cause at a
time.

- a, "Your 1.9 crore is right; the export carries fifteen extra rows": calls the books right before a
  single row has been tied out.
- b, "The export is clean apart from one amount and one missing status": ignores the 15 rows beyond
  one per order.
- c, "The gap is fifteen orders at about Rs 1.3 lakh each, Rs 20 lakh": spreads the gap evenly over
  the extra rows, when two of them carry 98.5 percent of it.

### Q2. Which sentence about the JSON feed can the note carry?

The app's JSON feed, cut from the same extract as the CSV, one pull of rows out of the ERP, yields 119
complete records; 118 of their amounts convert and match the clean file, and the 119th is unreadable
in the feed as it is in the CSV.

The key is b, "The feed repeats the CSV's extract, so it cannot vouch for any amount". The feed was cut
from the same extract, so it witnesses what the extract held, never whether a value is right.

- a, "The feed confirms the export's amounts for 118 of its orders": agreement with a copy of the same
  extract confirms nothing about the value.
- c, "The feed covers 59 percent of the export, so it can stand in for it": its 119 complete records
  hold only 19 of Q2's 86 orders.
- d, "The feed and the CSV disagree on one amount, so one of them is corrupt": the two agree on that
  amount, which is unreadable in both.

## Part 2. How does the identity rule treat repeated orders, today and next month?

### Q3 (Design). Which identity rule fits once two systems number their own orders?
From next month the export stitches the app's and the stores' orders, each system numbering from
KR-00001, and in a test month 312 order ids appear in both systems.

The key is c, "The system and order_id together; today's rule drops 312 real orders". Two systems
issuing their own ids means an id no longer names one order. The source system plus the id does, and
today's rule would set aside 312 real orders as copies of each other.

- a, "order_id alone, as today, since the log records every row it sets aside": a log that records a
  wrong removal still removes it.
- b, "The whole record less the line, as real orders never fully match": finds only exact copies, and a
  real copy that differs in one field survives.
- d, "customer_id, amount and date, since a customer rarely repeats an order": merges two real orders a
  customer places for the same amount on one day.

### Q4. How many repeated orders go to the ERP team as a question?

The rule keeps the copy whose amount converts, then the first; of the 15 repeated orders, 13 have
identical copies and 2 have copies that differ.

The key is c, "1, for the pair whose valid copies disagree". Thirteen pairs are identical, and one
pair's unreadable copy has a readable twin, the other row of the same order, so the rule settles all
fourteen. The pair whose valid copies disagree on a field leaves a fact only the source can settle.

- a, "15, one for every repeated order": thirteen of those questions have nothing in them.
- b, "2, one for each pair whose copies differ": the unreadable pair needs no question, since its twin
  carries the value.
- d, "0, since the rule settles every pair itself": the rule keeps a copy of the disagreeing pair, and
  the field it keeps is still unconfirmed.

## Part 3. How do you decide on an unusual order and on amounts in new formats?

### Q5 (Design). What goes in the note about a large order the business says will not recur?
The head of the Business segment, Kalpa's sales to companies, says the largest Q2 order, Rs 29,45,460,
was a one-off; Anand wants Q2 as booked, every order at the price charged, and Marketing wants a base
for planning Q3.

The key is a, "Q2 as booked, with the order; the Q3 plan built from Q2 without it". The order
happened, so Q2 as booked keeps it. A plan for Q3 is a forecast, and an order the business says will
not recur comes out of its base, labelled, so each reader gets the figure for their use with a line
saying which is which.

- b, "Q2 without the order, since it will not recur and would mislead": removes booked revenue from the
  quarter Finance reconciles.
- c, "Q2 with it, and the Q3 plan built from Q2 as booked, order and all": plans on an order the
  business says will not come back.
- d, "Q2 with the order capped at the next largest, for both readers": writes an amount nobody booked
  into both numbers.

### Q6 (Design). Which change to convert() fits amounts with paise and separators?
Next month about 40 percent of amounts will carry paise, `2310.50`, and a few a thousands separator,
`1,150`, while the day's `convert()` accepts whole numbers only.

The key is d, "Read commas and paise by one rule; log whatever still fails". Rejecting what int()
refuses would leave about 40 percent of revenue in the log. A rule for a known format, stated and
tested, reads both forms exactly and logs only what is still unreadable.

- a, "Keep int(), and send every amount it refuses to the rejects log": leaves about 40 percent of
  revenue out.
- b, "Wrap int() in try, and return 0 for anything it refuses": turns about 40 percent of orders into
  Rs 0.
- c, "Cut every amount at the dot before int(), and log the rest": drops the paise from 40 percent of
  orders and still rejects every amount with a comma.

## Part 4. Where did every row go, and what proves a re-sent export?

### Q7. Where did the one amount that fails to convert go?

After the identity rule, converting the 186 kept amounts logs nothing, though chapter 1's profile
counted one amount that fails, and a colleague says the pass lost a reject.

The key is a, "To the set-aside log, as a copy, with its readable twin named". The unreadable amount
was one copy of a pair. The rule kept the readable twin and set the copy aside with its reason, so
conversion afterwards had nothing to reject.

- b, "Into the clean file as text, since conversion skips kept rows": conversion runs on every kept
  row, and every kept amount converts.
- c, "Nowhere, since the rule converted it while it compared copies": the rule tests whether an amount
  converts and changes none of them.
- d, "Out of the pass, since profile() drops a row once it fails": profile() counts values and removes
  nothing.

### Q8 (Design). What do you run on a Q1 export re-sent with the copies removed?
The ERP team offers to re-send the Q1 export tomorrow with the copies removed at source.

The key is c, "Every step again: 100 orders, nothing set aside, Q1 on the books". A new export is a new
file, and only the whole pass proves it: 100 Q1 orders on 100 rows, nothing set aside, and Q1 on the
books. Any other result is a finding about the fix at source.

- a, "Nothing new, since today's bridge already explains the whole gap": today's bridge proves today's
  file, and tomorrow's is another file.
- b, "Only a row count, expecting 100 rows, since the rupees follow": rows can tie while the rupees
  miss, as a colleague who kept the first copy and then converted showed, with 201 = 185 + 16 and Q1
  Rs 1,790 short of the books.
- d, "Only the bridge, since copies were the one cause found today": a bridge on a file nobody
  profiled can close on the wrong rows.

## Part 5. What does the clean file change in Monday's tree, and what does Anand read first?

### Q9. Which branch of Monday's tree moves furthest from Tuesday's reading?

Recomputed on the clean file, which branch of Monday's tree, revenue = customers x orders per customer
x revenue per order, moves furthest from the Q2 multiples of Q1 that the team read on Tuesday from the
export as delivered?

The key is b, "Orders per customer: x0.860 on the clean file against x0.754". The copies were Q1
orders, so orders per customer carries the correction, 1.449 to 1.246 against Tuesday's 1.65 to 1.25.
Revenue per order moves from x1.180 to x1.144, a smaller shift, and customers stay at 69.

- a, "Revenue per order: x1.144 on the clean file against x1.180": revenue per order moves by less, from
  x1.180 to x1.144.
- c, "Customers: the copies counted some of the 69 buyers twice": the copies repeated orders of the
  same 69 customers, so the customer count never moved.
- d, "Orders per customer: x0.763 on the clean file against x0.754": x0.763 is the export as delivered
  today, before any cleaning.

### Q10. In what order does the note to Finance run?

The note to Finance has 120 words, and its content has to follow Anand's question.

The key is a, "Which figure is right; both reconciliations; what was flagged; what changed
downstream". Anand asked which figure is right, so that leads, then the proof, then the judgement
calls, then what the change means for Tuesday's finding.

- b, "What changed downstream; which figure is right; both reconciliations; what was flagged": opens
  on what changed for Marketing's campaign before Anand's question.
- c, "Both reconciliations; what was flagged; which figure is right; what changed downstream": makes
  Anand read the proof before the answer.
- d, "What was flagged; both reconciliations; what changed downstream; which figure is right": leaves
  the answer to the last line.

## Which letters does the notebook take?

The notebook's nine letters: 1c 2a 3d 4c 5b 6d 7b 8a 9c. Each check cell recomputes its step by a
second route, so a wrong letter shows as a FAIL on the step it belongs to. The notebook logs a
replaced copy only as "replaced by a later copy of the same order"; a log an auditor reads also says
why, here that the kept copy's amount would not convert.

## Why is item 5 worth arguing about?

Most of the room will say "remove it" or "keep it", and each answer is half right. The same record
goes to two readers: Finance reconciles what was booked, and a plan forecasts what will recur. The
analyst says which number answers which decision and labels both.

## Where does this pass run at work?

This pass, with its logs and two reconciliations, is the month-end close between any sales system and
the ledger, the finance team's own books. Running the steps in this order lets somebody else repeat the
close, and the recompute redoes every number already reported from the raw file.

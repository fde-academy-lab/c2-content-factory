# Which answers hold in the chapter 5 set on where each of the week's steps belongs, and why?

Answers: 1b 2a 3d 4b 5a 6c

Kavya Nair, the senior analyst on Kalpa Retail's data team, asked which parts of the week's work belong
in Excel, which must never be done there, and how the two are kept from drifting apart. The warehouse
holds one row per order and one per payment and is the source of truth; booked revenue is the value
of the orders, collected is the money received against them, and Tuesday's report joined 1,000 orders
to 1,428 payments to set one against the other. Chapter 5 found what a lookup does when it stands in
for that join and wrote the team's rule in three lines: the warehouse owns the number and every join,
dedupe and rank Finance relies on; pandas owns the analyst's iteration until Finance relies on it; the
workbook owns the last mile, on an export that ties, with a drift check on every refresh. Three of the
six items are design items: 3, 4 and 6.

**Who needs the answer.** You, checking your six letters after the lab or tonight. Kavya signs the
rule, and Anand Iyer, the finance controller, acts on the numbers it protects: a wrong letter here is
a collections team chasing money customers have already paid.

**The questions on the way.**

- Which idea does the chapter 5 set test: that a step belongs where it can be rerun and audited?
- Why does each of the six keys hold, from the Rs 8 crore that was never owed to the second route?
- Why is option a in item 3, a SUMIFS per order in the workbook, the wrong answer worth arguing about?
- Where did Public Health England lose cases to a step that lived in a spreadsheet?

## Which idea does the chapter 5 set test: that a step belongs where it can be rerun and audited?

A number Finance relies on has to be reachable again by anyone with the query, so joins, dedupes and
ranks live in the warehouse, and a sheet only presents what ties to it. The live items show what a
lookup does when it stands in for a join; the design items ask which arrangement fits a report Finance
signs, which question may stay in a sheet, and which route can disagree with the workbook.

## Why does each of the six keys hold, from the Rs 8 crore that was never owed to the second route?

### Q1. What happened when a lookup put collected at Rs 11.84 crore against Rs 19.84 crore booked?

A lookup on the order id fetched paid_amount from the raw export, one row per payment.

The key is b, "It took the first payment of each order and ignored any second one". A lookup returns
the first matching row and stops. On Kalpa's export 450 orders have two payment rows, 400 paid in
instalments and 50 posted twice by the gateway, so the lookup read Rs 11,83,81,974 collected and
reported Rs 8.00 crore outstanding, 40.3 percent of booked. Adding every payment gives
Rs 19,66,82,820, Rs 17,17,180 short of booked, 0.9 percent.

- a, "The unpaid orders have no payment row, so they pulled the total down": the unpaid orders are
  part of the real Rs 17 lakh gap, and the lookup's Rs 8 crore is far larger than that.
- c, "The exact match failed on half the ids, which then returned zero": an exact match finds every
  order with a payment row; the trouble is the rows it never reads.
- d, "The refunds were netted off the payments before the export was sent": nothing in the export
  nets refunds, and Rs 8 crore is the size of the second instalments.

### Q2. What does a lookup say is outstanding on four invented orders, and what is?

Orders of Rs 10,000 (two instalments of Rs 5,000), Rs 6,000 (paid once), Rs 4,000 (two instalments of
Rs 2,000) and Rs 2,000 (unpaid); booked is Rs 22,000.

The key is a, "Rs 9,000 by the lookup, and Rs 2,000 in truth". The lookup collects Rs 5,000 plus
Rs 6,000 plus Rs 2,000 plus zero, Rs 13,000, so it says Rs 9,000 is outstanding. Every payment added
gives Rs 20,000, so Rs 2,000 is outstanding, the one unpaid order.

- b, "Rs 2,000 by the lookup, and Rs 2,000 in truth": the lookup misses both second instalments,
  Rs 7,000 between them.
- c, "Rs 13,000 by the lookup, and Rs 20,000 in truth": those are the two collected figures, and the
  question asks what is outstanding.
- d, "Rs 9,000 by the lookup, and Rs 9,000 in truth": the second instalments were paid, so they are
  not owed.

### Q3. Which arrangement fits the booked-against-collected report Anand signs every month?

A design item. Anand signs it monthly, and his analyst reruns any number before relying on it.

The key is d, "The join in the warehouse, with a SUMIFS in the workbook as a check on it". The join of
orders to payments is one order to several rows, the step a sheet gets wrong most quietly, and a query
can be rerun and audited by anyone. A SUMIFS in the workbook that adds every payment per order is a
cheap independent check against the warehouse's figure.

- a, "A SUMIFS per order in the workbook over the payment export, refreshed by hand": it gives the
  right total today, and a monthly hand refresh of a cleaning step with no record is what an audit
  cannot rerun.
- b, "An exact-match lookup per order in the workbook, so nobody needs a login": this is the lookup
  that reported Rs 8 crore outstanding.
- c, "A notebook that computes collected and pastes the figures in as values": the notebook can be
  rerun by the analyst who wrote it, and the pasted values cannot be traced by anyone else.

### Q4. Which question can live in a sheet alone, with no warehouse step behind it?

A design item. The rule gives the warehouse every number Finance relies on.

The key is b, "A one-off look at which cities the protect list sits in, for a meeting". Nobody audits
it, nobody reruns it, and it reads a list that already ties, so a sheet is the right size of tool.
This is the fact that would change the rule's call: a one-off question nobody relies on can live in a
sheet, and the moment Finance relies on it, it moves upstream.

- a, "Anand's monthly collected figure, since a SUMIFS adds every payment": Finance relies on it every
  month, so it belongs in the warehouse whatever the sheet computes.
- c, "The weekly revenue by segment that every growth review reads first": a number read every week is
  a number someone has to rerun, which the warehouse does.
- d, "Counting each order once in the payment export before Finance sees a total": a dedupe Finance relies
  on is the warehouse's, ideally as an export that arrives at the order grain.

### Q5. What does the drift check do when the workbook's Q2 falls short of the warehouse's?

On an invented Monday, the workbook's Q2 reads Rs 9.79 crore against the warehouse's Rs 9.84 crore,
and every row in the export is real.

The key is a, "Holds the deck until someone knows why, and asks for a fresh export". A drift check
exists to stop a number that does not tie, whatever the reason. Real rows can still fall short: an
export pulled a week early is missing the orders that arrived after it, which is the case chapter 5's
notebook caught.

- b, "Ships the deck with a footnote that the export may be incomplete": a footnote ships a number the
  team already knows is wrong.
- c, "Types the warehouse's figure over the workbook's total so the two agree": that hides the gap and
  leaves every number beneath the total still short.
- d, "Ships the deck, since every row in the export is a real order": real rows are not all the rows.

### Q6. Which check can disagree with the workbook's collected figure when the workbook is wrong?

A design item. The workbook adds every payment per order with SUMIFS and reaches Rs 19,66,82,820.

The key is c, "The warehouse's payments table joined to its orders and summed". The warehouse never
saw the export or the workbook, so a SUMIFS that missed a row would disagree with it. Chapter 5's
notebook ran this route, and collected and booked both tied to the rupee.

- a, "The same SUMIFS copied onto a second tab and compared cell by cell": a copy repeats any mistake
  the first one made.
- b, "The lookup's figure, with the second payments added back by hand": it rebuilds the workbook's
  figure from the same export, so the two share every step that could go wrong.
- d, "The share of orders with a payment row, set against the share collected": a count of orders and
  a share of rupees measure different things and need not agree even when both are right.

## Why is option a in item 3, a SUMIFS per order in the workbook, the wrong answer worth arguing about?

Because it computes the right number. A SUMIFS adds every payment, so it does not fall into the
lookup's trap, and on Kalpa's export it reaches the warehouse's Rs 19,66,82,820. What it lacks is a
record: each month somebody refreshes it by hand, nobody else can rerun it, and an export that arrives
short gives a short answer with no warning. Kept as a check against the warehouse's join, the same
formula is exactly what the rule asks for.

## Where did Public Health England lose cases to a step that lived in a spreadsheet?

In October 2020 Public Health England reported that "15,841 cases between 25 September and 2 October
were not included in the reported daily COVID-19 cases" (GOV.UK, PHE statement on delayed reporting
of COVID-19 cases, 4 October 2020, checked 30 September 2026). The BBC explained that the files passed
through templates in the old XLS format, so "each template could handle only about 65,000 rows of
data rather than the one million-plus rows that Excel is actually capable of" (BBC News, 5 October
2020, checked 30 September 2026). A step of a data pipeline ran in a spreadsheet, rows past its limit
were dropped without an error, and nothing upstream counted them back.

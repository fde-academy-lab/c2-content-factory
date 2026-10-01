# Which answers hold in the chapter 5 set on where each of the week's steps belongs, and why?

Answers: 1b 2a 3d 4b 5a 6c

Kavya Nair, the senior analyst on Kalpa Retail's data team, asked which parts of the week's work belong
in Excel, which must never be done there, and how the two are kept from drifting apart. The warehouse
holds one row per order and one per payment and is the source of truth; booked revenue is the value
of the orders, collected is the money received against them, and Tuesday's report joined 1,000
orders to 1,428 payment rows, eight of which match no order, to set one against the other. Chapter 5
found what a lookup does when it stands in for that join and wrote the team's rule in three lines:
the warehouse owns the number and every join, dedupe and rank Finance relies on; pandas owns the
analyst's iteration until Finance relies on it; the workbook owns the last mile, on an export that
ties, with a drift check on its Checks tab that compares the sheet's totals, live, with the
warehouse's control totals. Three of the six items are design items: 3, 4 and 6.

**Who needs the answer.** You, checking your six letters after the lab or tonight. Kavya signs the
rule, and Anand Iyer, the finance controller, acts on the numbers it protects: a wrong letter here is
a collections team chasing money customers have already paid.

**The questions on the way.**

- Which skill does the chapter 5 set test?
- Why does each of the six keys hold, from the Rs 8 crore a lookup called outstanding to the second route?
- Why is a SUMIFS per order in the workbook (item 3, a) the most tempting wrong answer?
- Where did Public Health England lose cases to a step that lived in a spreadsheet?

## Which skill does the chapter 5 set test?

The skill is placing each step where it can be rerun and audited. A number Finance relies on has to
be reachable again by anyone with the query, so joins, dedupes and ranks live in the warehouse, and a
sheet only presents what ties to it. The live items show what a lookup does when it stands in for a
join; the design items ask which arrangement fits a report Finance signs, which standing arrangements
break the rule, and which route can disagree with each of the workbook's figures.

## Why does each of the six keys hold, from the Rs 8 crore a lookup called outstanding to the second route?

### Q1. What happened when a lookup put collected at Rs 11.84 crore against Rs 19.84 crore booked?

A lookup on the order id fetched paid_amount from the raw export, one row per payment.

The key is b, "It took the first payment of each order and ignored any second one". A lookup returns
the first matching row and stops. On Kalpa's export 450 orders have two payment rows, 400 paid in
instalments and 50 posted twice by the gateway, so the lookup read Rs 11,83,81,974 collected and
reported Rs 8.00 crore outstanding, 40.3 percent of booked. Adding every payment once, after the
gateway's 50 copies are dropped, gives Rs 19,66,45,070, Rs 17,54,930 short of booked, 0.9 percent,
which is exactly the 30 orders nobody has paid for. The Rs 7,82,63,096 of "outstanding" that
disappears is the second instalments of the 400 instalment orders.

- a, "The unpaid orders have no payment row, so they pulled the total down": the unpaid orders are
  the real gap, Rs 17,54,930 on 30 orders, and the lookup's Rs 8.00 crore is far larger than that.
- c, "The exact match failed on half the ids, which then returned zero": an exact match finds every
  order with a payment row; the trouble is the rows it never reads.
- d, "The refunds were netted off the payments before the export was sent": nothing in the export
  nets refunds, and the Rs 7,82,63,096 the lookup missed is the second instalments.

### Q2. What does a lookup say is outstanding on four invented orders, and what is?

Orders of Rs 10,000 (two instalments of Rs 5,000), Rs 6,000 (paid once), Rs 4,000 (two instalments of
Rs 2,000) and Rs 2,000 (unpaid); booked is Rs 22,000.

The key is a, "Rs 9,000 by the lookup, and Rs 2,000 in truth". The lookup reads the first payment row
of each order and stops, so it collects Rs 5,000 plus Rs 6,000 plus Rs 2,000 plus zero, Rs 13,000,
and says Rs 9,000 is outstanding. Every payment added once gives Rs 20,000, so Rs 2,000 is
outstanding, the one unpaid order.

- b, "Rs 2,000 by the lookup, and Rs 2,000 in truth": the lookup misses both second instalments,
  Rs 7,000 between them.
- c, "Rs 13,000 by the lookup, and Rs 20,000 in truth": those are the two collected figures, and the
  question asks what is outstanding.
- d, "Rs 9,000 by the lookup, and Rs 9,000 in truth": the second instalments were paid, so they are
  not owed.

### Q3. Which arrangement fits the booked-against-collected report Anand signs every month?

A design item. Anand signs it monthly, his analyst reruns any number before relying on it, and the
workbook that carries the figure to the deck has no login to the warehouse.

The key is d, "The join in the warehouse, with a SUMIFS in the workbook as a check on it". The join of
orders to payments is one order to several rows, the step a sheet gets wrong with no error showing,
and a query in the warehouse can be rerun and audited by anyone. A SUMIFS in the workbook, adding
every payment once over the export with its gateway copies dropped, is a cheap check beside the
warehouse's figure, so a copy that stops matching is caught in the workbook itself.

- a, "A SUMIFS per order in the workbook over each month's payment export, refreshed by hand": it can
  give the right total, and a monthly hand refresh of a join with no record is what an audit cannot
  rerun.
- b, "The join in the warehouse, and the workbook shows its total with no check beside it": the
  number starts right, and once it sits in a workbook nothing says when the copy stops matching the
  warehouse, after an export pulled early or a figure typed over it.
- c, "A notebook that runs the join and pastes the figure in as a value": a notebook is the analyst's
  iteration, rerun by the analyst who wrote it, and a figure Finance signs every month belongs to the
  warehouse; the pasted value cannot be traced by anyone else.

### Q4. Which of three standing arrangements break the team's rule?

A design item. The three arrangements are the first-row flag every week under the growth review's
revenue, a one-off city count on the tied protect list, and a SUMIFS per order every month for
Anand's collected figure.

The key is b, "1 and 3, since each cleans or joins the rows a Finance number rests on". Arrangement 1
is a dedupe that the growth review's revenue, which must equal Finance's, rests on every week, so it
belongs in the warehouse as an export at the order grain; on about 145,000 rows next quarter the flag
would also cost about 10.5 billion comparisons. Arrangement 3 is the join behind a figure Finance
signs. Arrangement 2 reads a list that already ties, once, and nobody audits or reruns it, which is
the case the rule leaves to a sheet; the fact that would move it upstream is Finance starting to rely
on it.

- a, "Only 3, since the flag ties to the warehouse to the rupee every week": a tie proves each week's
  number, and the cleaning behind it is still a standing step with no record, in the one tool that
  cannot rerun it.
- c, "All three, since none of them has a query in the warehouse behind it": the city count reads a
  list that already ties, once, and nobody audits or reruns it, so the rule lets a sheet hold it.
- d, "2 and 3, since nothing ties the protect list's city count to the warehouse": the city count
  reads the tied list, and the weekly flag, which does break the rule, is left in place.

### Q5. What does the drift check do when the workbook's Q2 falls short of the warehouse's?

On an invented Monday, the workbook's own Q2 total reads Rs 9.79 crore against the warehouse's control
total of Rs 9.84 crore, and every row in the export is real.

The key is a, "Holds the deck until someone knows why, and asks for a fresh export". A drift check
exists to stop a number that does not tie, whatever the reason. Real rows can still fall short: an
export pulled a week early is missing the orders that arrived after it, which is the case chapter 5's
notebook caught.

- b, "Ships the deck with a footnote that the export may be incomplete": a footnote ships a number the
  team already knows is wrong.
- c, "Passes, since Rs 5 lakh is about half a percent of Q2, inside rounding": the workbook and the
  warehouse add the same orders, so they tie to the rupee or something is missing, and Rs 5 lakh is
  more than Retail-Plus booked in the whole of Q2, Rs 4,13,380.
- d, "Ships the deck, since every row in the export is a real order": real rows are not all the rows.

### Q6. Which route can disagree with each of two workbook figures when the figure is wrong?

A design item, set as a matching. Figure 1 is collected, Rs 19,66,45,070, every payment added once
after the gateway's 50 copies are dropped; figure 2 is Q2's booked revenue, Rs 9,84,00,000, from the
flagged rows. The warehouse's payments table carries the gateway's 50 double posts.

The key is c, "Figure 1 with P, and figure 2 with R". Route P never adds a payment: it starts from the
warehouse's booked Rs 19,84,00,000 and takes away the 30 orders with no payment at all, Rs 17,54,930,
which leaves Rs 19,66,45,070, so a workbook that kept a gateway copy or missed a second instalment
would disagree with it. Route R sums the warehouse's orders table, which never saw the export or the
flag, and gives Rs 9,84,00,000 for Q2. Chapter 5's notebook ran route P and chapter 2's ran route R,
and both tied to the rupee.

- a, "Figure 1 with Q, and figure 2 with R": route Q adds payment rows, and the payments table carries
  the same 50 double posts, so it reads Rs 37,750 above the true figure and would agree with a
  workbook that forgot to drop them.
- b, "Figure 1 with P, and figure 2 with S": route S pivots the same flagged rows again, so a flag that
  missed an order or kept a repeat gives the same wrong Q2 twice.
- d, "Figure 1 with Q, and figure 2 with S": each route repeats a step of the figure it checks, the
  double posts in one and the flag in the other.

## Why is a SUMIFS per order in the workbook (item 3, a) the most tempting wrong answer?

Option a can compute the right number. A SUMIFS adds every payment, so it does not fall into the
lookup's trap, and over the export with the gateway's 50 copies dropped it reaches Rs 19,66,45,070,
the warehouse's figure. What it lacks is a record: each month somebody refreshes it by hand, nobody
else can rerun it, and an export that arrives short gives a short answer with no warning. Kept as a
check beside Tuesday's join in the warehouse, which counts each instalment once, the same formula is
exactly what the rule asks for.

## Where did Public Health England lose cases to a step that lived in a spreadsheet?

In October 2020 Public Health England reported that "15,841 cases between 25 September and 2 October
were not included in the reported daily COVID-19 cases" (GOV.UK, PHE statement on delayed reporting
of COVID-19 cases, 4 October 2020, checked 30 September 2026). The BBC explained that the files passed
through templates in the old XLS format, so "each template could handle only about 65,000 rows of
data rather than the one million-plus rows that Excel is actually capable of" (BBC News, 5 October
2020, checked 30 September 2026). A step of a data pipeline ran in a spreadsheet, rows past its limit
were dropped without an error, and nothing upstream counted them back.

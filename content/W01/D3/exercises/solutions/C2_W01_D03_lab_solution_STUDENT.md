# Which answers hold in the practice lab on the ERP team's other files, and why?

Answers: 1b 2c 3b 4c 5a 6a 7d 8b 9d 10a 11b

Kavya Nair, the senior analyst on Kalpa Retail's data team, asked for the day's pass to be run on the
other files sent by the team that runs the ERP, the enterprise resource planning system Finance books
orders in, and for a verdict on which of them the team can trust.

## What does the lab test?

It runs the day's pass on files nobody demonstrated: a profile, the three counts for every field, read
as evidence, a second source read for what it can witness, and a reconciliation in rows and rupees
against a clean file you built yourself.

## Problem 1. Which of two profile printouts of one export would you trust?

Two analysts profiled the same 320-row export. Printout A shows 305 distinct order ids, 320 amounts
convertible, 4 amounts at Rs 0 and no failures logged; printout B shows 305 ids, 316 amounts
convertible, none at Rs 0 and 4 failures logged.

### Q1. Which printout goes to Anand's analyst?

The analyst works for Anand Iyer, the finance controller, and ties out every figure she receives,
matching it to the books, Finance's own record of Q1, line by line.

The key is b, "B, since its four failures are counted and named". B counts its failures and logs them,
while A turned four failures into orders at Rs 0.

- a, "A, since every amount in it converts": a perfect convertible count beside four zeros is the
  coercion trap, a helper turning each failure into Rs 0.
- c, "Either, since the rows and the ids agree across both": agreeing rows and ids say nothing about
  amounts.
- d, "Neither, since both show copies in the export": copies are a reason to reconcile, and they count
  against neither printout.

### Q2. How many rows sit beyond one per order?

The export holds 320 rows and 305 distinct order ids.

The key is c, "15". 320 rows less 305 distinct ids is 15.

- a, "4": the count of failed amounts.
- b, "11": 15 less 4 mixes two counts.
- d, "19": 15 plus 4 adds them.

### Q3. What does the same total on A and B tell you?

A's total and B's total over the amounts that convert are the same number.

The key is b, "A's zeros add nothing, which is how its total hides them". Adding zeros changes no
total, so A looks identical in rupees while hiding four orders.

- a, "The totals agree, so the two printouts are equally sound": four zeros leave a total unchanged, so
  equal totals say nothing about which printout is sound.
- c, "The four failures carried no rupees, so neither total is short": a failed amount can carry any
  value, and nobody has read these four.
- d, "The four failed amounts must all sit in one quarter": nothing in either printout places them in a
  quarter.

## Problem 2. What does the vendor copy hold once you profile it?

The vendor copy, `C2_W01_D03_vendor_STUDENT.csv`, which the ERP team says a vendor sent, copied from
the start of the export, is read with `read_orders()` and profiled with `profile()`.

### Q4. How many rows and convertible amounts does the profile show?

The day's `profile()` counts the vendor copy's rows and the amounts among them that convert.

The key is c, "40 rows, 39 convert". The profile counts every line after the first as a row, 40 of
them, and one of their amounts does not convert.

- a, "39 rows, 39 convert": the profile counts every line after the first, and there are 40.
- b, "40 rows, 40 convert": one amount does not convert.
- d, "39 rows, 38 convert": the profile counts every line after the first, and there are 40.

### Q5. What do you do first about a segment value the export never carries?

The segment field holds one more distinct value than the export's own rows carry.

The key is a, "Print the rows whose amount fails, and read each one". Read the rows that fail before
deciding anything, since the failed amount and the extra segment value sit on the same row.

- b, "Add the extra segment to the tree as a new branch": Monday's revenue tree splits revenue into
  customers x orders per customer x revenue per order, and a branch for a value nobody sold to is
  invented.
- c, "Drop the segment field, since one of its values cannot be trusted": the field is sound on every
  other row.
- d, "Ask the vendor for a new file before reading any further": read first, then ask.

### Q6. What does the vendor copy total over the amounts that convert?

The vendor copy's amounts that convert are added up.

The key is a, "Rs 81,890". The rows that convert total Rs 81,890.

- b, "Rs 18,890": the first two digits swapped, the kind of slip a hand copy makes.
- c, "Rs 8,18,900": a zero added.
- d, "Rs 81,980": the 8 and the 9 swapped.

## Problem 3. Does the app's JSON feed agree with the CSV, and what would that prove?

The app's JSON feed, `C2_W01_D03_orders_STUDENT.json`, was cut from the same extract as the CSV, one
pull of rows out of the ERP, and each complete record is compared with the CSV row on the same file
line.

### Q7. How many feed records are complete, and how many match the CSV's amount text?

Each complete feed record is set beside the CSV row on the same file line, amount text against amount
text.

The key is d, "119 and 119". 119 records are complete, and each carries the same amount text as its
CSV row.

- a, "120 and 119": counts a record that is not complete.
- b, "119 and 118": nothing differs among the complete records.
- c, "120 and 120": counts a record that is not complete.

### Q8. What can the feed prove about the CSV's amounts?

The feed and the CSV were cut from the same extract, and the complete records carry the same amount
text as the CSV.

The key is b, "What the extract held, and never whether a value is right". The feed was cut from the
same extract, so it witnesses what the extract held, never whether a value is right: a flaw in the
extract appears in both files.

- a, "That they are right wherever the two files agree": both files can carry the same wrong value.
- c, "That the CSV holds no copies among the rows the feed covers": agreement on amounts says nothing
  about repeated ids.
- d, "Nothing at all, since the feed is cut part way through": the complete records are real evidence
  of what was exported.

## Problem 4. Does the vendor copy reconcile to your clean file in rows and in rupees?

The vendor copy is reconciled against the clean file from the escalated case, 186 orders, in rows and
in rupees.

### Q9. What is the vendor copy's row reconciliation?

The vendor copy's 40 rows are reconciled against the 186 orders of the clean file.

The key is d, "40 rows in equal 39 orders kept plus 1 set aside". 40 rows come in, 39 orders are kept
and 1 line is set aside.

- a, "39 rows in equal 39 orders kept, nothing set aside": miscounts the rows read.
- b, "40 rows in equal 38 orders kept plus 2 set aside": the 39 orders are distinct, so only one line
  is set aside.
- c, "40 rows in equal 40 orders kept, nothing set aside": keeps as an order the line whose amount does
  not convert.

### Q10. What must hold for the vendor copy's rupees to reconcile?

Every vendor order_id is in the clean file.

The key is a, "The vendor total equals your clean total for the same ids". Rupees reconcile when the
same orders carry the same total.

- b, "The vendor total equals Q1 in the books": the copy holds only the orders it holds, a slice of the
  quarter against the books, Finance's own record of all of Q1.
- c, "The vendor total is within 1 percent of the clean total": a tolerance hides the gap an analyst
  ties out to.
- d, "The vendor total rounds to the same lakh as the clean total": a tolerance hides the gap an analyst
  ties out to.

### Q11. What do you tell Kavya about the vendor copy?

The vendor copy's rupees reconcile to the clean file over the same order ids.

The key is b, "It confirms the orders it holds to the rupee, and no more". A copy that agrees to the
rupee shows the orders it holds match your clean file and shows nothing past them, which is worth one
line in the note.

- a, "It is a clean second source and can replace the export for Q1": a slice of the export cannot
  replace the whole of it.
- c, "It proves the export held no copies among its first rows": it covers only the rows it holds, and
  a copy of one of those orders could sit later in the export.
- d, "It is too small to matter, so it stays out of the note": a small copy still checks the orders it
  holds.

## Why is item 8 worth arguing about?

When two sources agree, the agreement shows that they share an origin, and a defect in that origin sits
in both. The reconciliation to the books is the test for that reason, and the feed only witnesses what
the extract held.

## Where does a second source get read this way at work?

Every data team keeps a second source for its most important numbers: a gateway report against the
orders table, a ledger extract against the warehouse. The team reads it for what it can witness and
never lets it replace the first, so two copies of one mistake cannot pass as confirmation.

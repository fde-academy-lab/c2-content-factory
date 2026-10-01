# Which answers hold in the practice lab on the last mile in new cases, and why?

Answers: 1a 2c 3a 4b 5c 6a 7b 8c 9b 10c 11c 12a 13b 14a 15b 16a 17d 18b

Kavya Nair, the senior analyst on Kalpa Retail's data team, asked which parts of the week's work
belong in Excel, which must never be done there, and how the two stay in step. The team's rule gives
the warehouse the number and every join, dedupe and rank Finance relies on, gives pandas the analyst's
iteration until Finance relies on it, and gives the workbook the last mile, on an export that ties. A
front-page card prints its period, its comparison and its base, and measures a change on the earlier
period. The lab practised the day's checks on cases nobody had seen: eight requests, three draft
cards, an invented export and a colleague's sheet.

**Who needs the answer.** You, at the end of the lab, checking your eighteen letters. The four
problems are the four ways the day's traps reach you at work, and a letter you cannot explain here is
one you will repeat on a real deadline.

**The questions on the way.**

- Which skill does the practice lab test?
- How do the invented export's rows add up, three ways?
- Why does each of the eighteen keys hold, problem by problem?

## Which skill does the practice lab test?

The skill is carrying the day's checks to cases nobody has seen. Problem 1 is the operating rule
applied to requests the team really receives: whoever has to trust a number, and how often it is
rebuilt, decides where it lives. Problem 2 is three cards a director misreads: one with no period or
comparison, one with no base, and one whose comparison points the wrong way. Problem 3 runs chapter
2's grain and chapter 4's card on an export small enough to hold in your head. Problem 4 is the
day's checks on a sheet somebody else built, which is how the traps arrive in real work.

## How do the invented export's rows add up, three ways?

| Version | Q1 | Q2 | Change on Q1 |
|---|---|---|---|
| Every payment row, as exported | Rs 30,000 + 2 x 2 x Rs 20,000 = Rs 1,10,000 | Rs 17,000 + 2 x Rs 40,000 + 2 x Rs 3,000 = Rs 1,03,000 | Down 6.4 percent |
| After Remove Duplicates | Rs 1,10,000, since instalments on different dates are not copies | Rs 1,00,000, since the gateway's copy goes | Down 9.1 percent |
| Each order once | Rs 30,000 + Rs 40,000 = Rs 70,000 | Rs 17,000 + Rs 40,000 + Rs 3,000 = Rs 60,000 | Down 14.3 percent |

## Why does each of the eighteen keys hold, problem by problem?

### Q1. Anand's Monday revenue by segment, which his analyst audits line by line: which tool owns it?

The key is a, "SQL in the warehouse". An audited number is computed where anyone can rerun the query.

- b, "pandas in a notebook": a notebook is the analyst's iteration, and an audit needs a step anyone
  can rerun.
- c, "Excel on the export": a sheet holding an audited number has no record of how it was made.

### Q2. A director slices the reconciled tree by city during Monday's review: which tool owns it?

The key is c, "Excel on the export". Slicing a reconciled table in the room, without a login, is the
last mile.

- a, "SQL in the warehouse": a director in the room has no login and no query.
- b, "pandas in a notebook": a director does not run a notebook in a meeting.

### Q3. Counting each order once in the payment export every week, before any total is computed: which tool owns it?

The key is a, "SQL in the warehouse". A dedupe that runs every week under a number Finance relies on
is cleaning, and it belongs where it can be rerun and audited, ideally as an export that arrives at
the order grain.

- b, "pandas in a notebook": fine for a one-off look, and wrong for a step that runs every week under
  the deck's number.
- c, "Excel on the export": the first-row flag met Friday's deadline once, and as a weekly step it is a
  cleaning job with no record, which on next quarter's 145,000 rows also costs about 10.5 billion
  comparisons.

### Q4. Trying five definitions of an active member this afternoon, to see which one separates the members who stopped buying: which tool owns it?

The key is b, "pandas in a notebook". Five definitions in an afternoon is the analyst's iteration.

- a, "SQL in the warehouse": fixes a definition in the source of truth before anyone knows which one
  works.
- c, "Excel on the export": cannot rebuild a table five ways and keep the steps reproducible.

### Q5. The chief of staff looks one member up by id on a laptop before a call: which tool owns it?

The key is c, "Excel on the export". A lookup on a finished table, on a laptop, without a login.

- a, "SQL in the warehouse": needs a login and a query the chief of staff does not write.
- b, "pandas in a notebook": needs Python, which the chief of staff ruled out.

### Q6. The booked-against-collected report Finance signs every month: which tool owns it?

The key is a, "SQL in the warehouse". Finance signs it, and its join of one order to several payments
is the step a sheet gets wrong with no error showing.

- b, "pandas in a notebook": holds a signed number in a place nobody else reruns.
- c, "Excel on the export": a lookup there reported Rs 8 crore outstanding that customers had paid.

### Q7. A one-off look at whether returns cluster in one city, for a hypothesis nobody has funded yet, when returns sit in neither of the exports the workbook reads: which tool owns it?

The key is b, "pandas in a notebook". An unfunded hypothesis is the analyst's iteration, and since
returns sit in neither export, the look needs returns joined to cities, which a notebook keeps
reproducible.

- a, "SQL in the warehouse": the rule gives the warehouse what Finance relies on, and a hypothesis
  nobody has funded moves upstream only once someone relies on it.
- c, "Excel on the export": returns sit in neither export, so the sheet has nothing to count.

### Q8. A what-if on next quarter's Retail-Plus recovery, asked for in the growth review: which tool owns it?

The key is c, "Excel on the export". A what-if is a labelled input on the sheet, beside the actual,
which a director changes in the room.

- a, "SQL in the warehouse": puts an assumption into the source of truth.
- b, "pandas in a notebook": the director cannot change it in the room.

### Q9. The card reads "Revenue up 12 percent". What will a director misread?

The key is b, "Which months grew, and against which, since neither is named". With no period and no
comparison, the card is read against whatever the director remembers.

- a, "The rounding, since 12 percent could be anything from 11.5 to 12.4": half a point either way
  changes no decision, while the missing months change every reading of the card.
- c, "The size of the business, since there is no chart drawn beside it": a chart helps once the period is
  known, and does not supply it.
- d, "The segment, since the card does not say which one it means": "Revenue" with no segment reads as
  the company, which is the likely meaning.

### Q10. The card reads "Student orders, Q2: up 41 percent on Q1". What will a director misread?

Student placed 27 orders in Q1 and 38 in Q2, from 20 customers in Q2.

The key is c, "The size, since 41 percent sits on 27 orders and 20 customers". Eleven more orders read
as the fastest growth on the page; the card needs its counts beside the rate, the rule from Week 1
Thursday on a rate with few customers behind it.

- a, "The direction, since a rise in orders can come with falling revenue": true in general, and
  Student's revenue rose too, from Rs 26,720 to Rs 35,770.
- b, "The period, since orders are counted every day of the quarter": the card names its quarter and
  its comparison, so the period is not what is missing.
- d, "The segment, since Student is the smallest of the four": the card names the segment; what it
  hides is how few orders stand behind the rate.

### Q11. The card reads "Q2 orders 462, up from 538 in Q1". What will a director misread?

The key is c, "The direction, since 462 is 14.1 percent below 538". The word "up" is wrong: 462 less
538 is minus 76, a fall of 14.1 percent on Q1.

- a, "The base, since a count of orders needs a share of revenue beside it": a count is its own base,
  and the wrong word is the misreading.
- b, "The period, since Q2 is not spelled out in its months": worth fixing, and smaller than a card
  that says up for a fall.
- d, "Nothing, since both quarters and both counts are named": both are named, and the word between
  them points the wrong way.

### Q12. What does a pivot's Sum of order_amount print for Q1 and Q2, and what change does it show?

The key is a, "Rs 1,10,000 and Rs 1,03,000, down 6.4 percent". Every row adds its order's amount, so
the instalment orders count twice and the gateway's order twice; the change is Rs 7,000 over Q1's
Rs 1,10,000.

- b, "Rs 70,000 and Rs 60,000, down 14.3 percent": that is the honest count, which the pivot on the
  rows cannot show.
- c, "Rs 1,10,000 and Rs 1,00,000, down 9.1 percent": that is after Remove Duplicates.
- d, "Rs 1,10,000 and Rs 1,03,000, down 6.8 percent": the totals are right, and the change is divided
  by Q2.

### Q13. After Remove Duplicates on every column, what change does the pivot show?

The key is b, "Down 9.1 percent, Rs 1,00,000 against Rs 1,10,000". Only the gateway's identical copy
goes, Rs 3,000 from Q2; the instalments differ in date and stay, so Q1 is unchanged.

- a, "Down 6.4 percent, since nothing in the export is an exact copy": the gateway's two rows are exact
  copies.
- c, "Down 14.3 percent, Rs 60,000 against Rs 70,000": that is each order once, which Remove
  Duplicates does not give.
- d, "Down 10.0 percent, Rs 1,00,000 against Rs 1,10,000": the totals are right, and the change is
  divided by Q2.

### Q14. Counted once per order, which card goes on the front page?

The key is a, "App channel, Q2: Rs 60,000, down 14.3 percent on Q1 (Rs 70,000)". The quarter, its
change measured on Q1, and Q1's figure as the base.

- b, "App channel, Q2: Rs 60,000, down 16.7 percent on Q1 (Rs 70,000)": the fall of Rs 10,000 divided
  by Q2.
- c, "App channel: Rs 1,30,000 across the half-year, down Rs 10,000": two quarters added, with a
  change and no comparison a director can check.
- d, "App channel, Q2: Rs 60,000, down 9.1 percent on Q1 (Rs 70,000)": the change from the deduplicated
  pivot, printed beside the honest figures.

### Q15. Its grand total is Rs 4.10 crore for two quarters the warehouse books at Rs 2.05 crore, and its export has 2,900 rows for 2,000 orders. What do you fix?

The key is b, "The grain: count each order once before anything is summed". More rows than orders and
a total near twice the warehouse is chapter 2's trap.

- a, "The date filter, since two periods overlap inside the pivot": an overlap would not make rows
  outnumber orders.
- c, "The segment mapping, since one segment is counted twice over": a double-counted segment would
  not double every quarter.
- d, "Nothing, since a pivot's Sum is the export's own total": that is the problem, at the wrong grain.

### Q16. Its lookup returns a member's revenue for C-0888, an id the team says left last year. What do you fix?

The key is a, "The match type: exact, with a not-found path the room can see". An approximate match
returns the largest id below a missing one, a neighbour's revenue.

- b, "The sort order of the ids, so the lookup finds the right member": sorting is what makes an
  approximate match return a plausible neighbour, so it makes the defect harder to see.
- c, "The revenue column, which may still hold last year's figures": the row returned is somebody
  else's, whatever year its figures are.
- d, "Nothing, since a member who left keeps a row of history": a member with no row cannot have one
  returned for them.

### Q17. Filtered to Chennai, the foot of its list does not move. What do you fix?

The key is d, "The foot: SUBTOTAL(109) where it has SUM". SUM adds the rows a filter hides; SUBTOTAL
with 109 adds only the rows on screen, and also skips rows hidden by hand.

- a, "The filter, since Chennai may have no members on the list": an empty filter would leave nothing
  on screen, and the foot would still read the whole list under SUM.
- b, "The list size, since the filter cannot reach row fifty": a filter reaches every row of its range.
- c, "The city column, which may hold codes the filter misses": then the filter would show the wrong
  rows, and the foot would still not move.

### Q18. Its card says a segment fell 25 percent, from Rs 4.00 lakh to Rs 3.20 lakh. What do you fix?

The key is b, "The change: 20 percent, measured on the earlier quarter". Rs 80,000 over Rs 4.00 lakh
is 20 percent; 25 percent divides it by the later Rs 3.20 lakh.

- a, "Nothing, since Rs 80,000 is a quarter of the segment's revenue": it is a quarter of Rs 3.20 lakh,
  the later figure.
- c, "The period, since one quarter is too short to compare": quarter against quarter is the card's
  comparison; the arithmetic is what is wrong.
- d, "The rounding, since the change is 25.0 percent exactly": it is 25.0 percent only on the wrong
  base.

# Which answers hold in the chapter 3 set on the protect list and the member lookup, and why?

Answers: 1d 2b 3c 4b 5a 6c

Meera's chief of staff asked for the top-fifty protect list with a lookup that finds any member by
id. The list is the fifty Retail-Plus members, Kalpa's paid membership tier, with the highest revenue
from April to September 2026, taken from the customer table, which holds one row per customer who
ordered in those months; it runs from C-0152 at Rs 25,840 down to a cut-off of Rs 8,580, and the
fifty-first member spent Rs 8,520, so no tie crosses the boundary. A VLOOKUP with its fourth argument
left out is an approximate match, which returns the largest id not above the one asked for; an exact
match returns the member asked for or says the id is missing. Three of the six items are design
items: 3, 4 and 6.

**Who needs the answer.** You, checking your six letters after the lab or tonight. A lookup you
cannot defend is the one that tells a director, in front of the room, that a member who stopped
buying is one of Kalpa's best.

**The questions on the way.**

- Which idea does the chapter 3 set test: that a lookup has to fail visibly on an id it does not hold?
- Why does each of the six keys hold, from C-0195 to the second route?
- Why is option a in item 3, XLOOKUP for every laptop, the wrong answer worth arguing about?
- Where did TransAlta, the Canadian power company, pay for a row that answered for the wrong item?

## Which idea does the chapter 3 set test: that a lookup has to fail visibly on an id it does not hold?

A lookup is read aloud in rooms where nobody sees the formula, so its one unforgivable answer is
somebody else's row. An exact match with a not-found path says when an id is missing; an approximate
match never does, and returns a neighbour that looks plausible. The design items ask which exact
lookup fits the office's software, where an approximate match is the right tool, and which second
route can catch a lookup that is wrong.

## Why does each of the six keys hold, from C-0195 to the second route?

### Q1. What went wrong when C-0195 came back as Rs 16,740 at rank 15?

C-0195 placed no orders in the two quarters, so the table has no row for it, and the cell holds
`=VLOOKUP("C-0195", A2:F301, 5)`.

The key is d, "An approximate match returned the nearest id below the one asked for". With the
fourth argument left out, VLOOKUP matches approximately: Microsoft's page says "If you don't specify
anything, the default value will always be TRUE or approximate match" (Microsoft Support, VLOOKUP
function, checked 30 September 2026). It returned C-0194's row, a member at rank 15 who spent
Rs 16,740, and nothing on the screen turned red.

- a, "The member's orders were summed across both quarters instead of Q2 alone": C-0195 has no
  orders to sum, and the revenue shown is somebody else's.
- b, "The ids are text, so the lookup compared them in the wrong order": text ids sort the way the
  table is sorted here, and the trouble is the match type, which would return a neighbour for any key.
- c, "The list was ranked before the segment filter was applied to it": the rank belongs to the row
  the lookup returned, C-0194's, so ranking order is not what went wrong.

### Q2. Which formula returns a member's revenue or the words "not in the table", and nothing else?

Revenue sits in column E and ids in column A, rows 2 to 301.

The key is b, `=IFERROR(INDEX(E:E,MATCH("C-0195",A:A,0)),"not in the table")`. MATCH with 0 is an
exact match: it finds the id or returns #N/A, and IFERROR turns the #N/A into the words.

- a, `=VLOOKUP("C-0195",A:E,5)`: the fourth argument is left out, so this is the approximate match
  that returned C-0194's row.
- c, `=INDEX(E:E,MATCH("C-0195",A:A,1))`: MATCH with 1 is approximate too, and returns the largest id
  not above C-0195.
- d, `=IFERROR(VLOOKUP("C-0195",$A$2:$E$301,5,TRUE),"not in the table")`: TRUE asks for the
  approximate match, which finds a neighbour and raises no error, so IFERROR never fires.

### Q3. Which lookup ships to an office where two laptops run Excel 2019?

A design item. Any of the office's laptops may open the file in the meeting, and two run Excel 2019.

The key is c, "IFERROR around INDEX and MATCH with 0, which every version computes". It is exact,
says "not in the table" when an id is missing, and computes in Excel 2016, 2019 and Microsoft 365 and
in LibreOffice. The fact that decides it is the oldest Excel that will open the file; if every laptop
ran Microsoft 365, XLOOKUP with its fourth argument would be the cleaner formula.

- a, "XLOOKUP with its fourth argument, since it is exact by default and names a missing id": both
  are true, and Microsoft's page says XLOOKUP "is not available in Excel 2016 and Excel 2019"
  (Microsoft Support, XLOOKUP function, checked 30 September 2026), so two laptops show #NAME?.
- b, "VLOOKUP with FALSE, since #N/A is an honest answer for an id the table lacks": honest, and a
  director reads #N/A as a broken sheet, so the meeting stops on the error instead of the answer.
- d, "VLOOKUP with its fourth argument left out, since every version of Excel has it": every version
  has it, and every version gives the approximate match that answers with a neighbour.

### Q4. Which match type fits a discount tier, and which fits a member id?

A design item. Invented tiers start at Rs 0, Rs 1,000, Rs 2,500 and Rs 5,000; an order of Rs 2,700
needs its tier, and the same sheet looks members up by id.

The key is b, "Approximate for the tier, and exact for the member id". A tier table holds the lower
edge of each band, sorted, so "the largest value not above Rs 2,700" is exactly the band the order
falls in, the one starting at Rs 2,500. A member id is a name, so the largest id below a missing one
is a different member. The question to ask before typing a lookup is whether the key is a band edge
or a name.

- a, "Exact for the tier, and approximate for the member id": an exact match finds no tier starting
  at Rs 2,700 and fails, and the approximate id lookup is chapter 3's trap.
- c, "Approximate for both, since both columns are sorted": sorting is what an approximate match
  needs, and it does not make a neighbour's row the right member.
- d, "Exact for both, since an approximate match is never safe": bands are the case approximate
  match was built for, and an exact match cannot find an amount that sits between two edges.

### Q5. Which three ids test a lookup before a director uses it?

The list will be seen sorted by revenue in the meeting.

The key is a, "One known to be present, one known to be missing, and the first once re-sorted". The present id proves the found path, the missing id proves the not-found path, and the first
id on the list sorted by revenue proves the lookup does not depend on the order of the rows, which an
approximate match does.

- b, "The top member, a member from the middle of the list, and the last id in the table": three
  present ids prove the found path three times and never test the not-found path.
- c, "Three ids from the top of the list, so that the largest revenues are proved first": the same
  gap, with the largest numbers.
- d, "One typed in lower case, one with a trailing space, and one pasted from the export": worth
  testing once the two paths work, and none of the three is an id known to be missing, so a lookup
  that answers with a neighbour passes all three.

### Q6. Which check can disagree with the lookup when the lookup is wrong?

A design item. The second route shares none of the lookup's steps.

The key is c, "A COUNTIF of the id, which must read zero where the lookup says not found".
Counting is a different method from matching, so a lookup that returned a neighbour for a missing id
would meet a count of zero and disagree. In Excel, `=COUNTIF(A:A, "C-0195")` reads 0, and
`=SUMIFS(E:E, A:A, "C-0152")` reads Rs 25,840, the same as the lookup for a member who is there.

- a, "An XLOOKUP beside the INDEX and MATCH, compared with it cell by cell": two matches can share a
  mistake, such as both being given an approximate match type.
- b, "The lookup's answer compared with the rank column on the very row it returned": the rank sits on the
  row the lookup returned, so a wrong row brings its own consistent rank.
- d, "The table sorted by id, and the row for the id read off it by eye": a person reading fifty rows
  in a meeting is not a check that runs every time the sheet changes.

## Why is option a in item 3, XLOOKUP for every laptop, the wrong answer worth arguing about?

Because XLOOKUP is the better formula wherever it computes: exact by default, with the not-found words
built in. The mistake is assuming every laptop that opens the file has it. A lookup that shows #NAME?
on two laptops in the CEO's office has failed as surely as one that returns a neighbour, only more
loudly. The fact to ask for before choosing is the Excel version on the oldest laptop in the room.

## Where did TransAlta, the Canadian power company, pay for a row that answered for the wrong item?

In 2003 TransAlta lost 24 million US dollars on bids for electricity transmission contracts in New
York after "someone preparing the electronic file of bids ... misaligned the rows of information in
the spreadsheet". Its president, Steve Snyder, said: "It was literally a cut-and-paste error in an
Excel spreadsheet that we did not detect when we did our final sorting and ranking of bids prior to
submission" (The Globe and Mail, 4 June 2003, checked 30 September 2026). A ranked list read off by
row is Kalpa's protect list, and a row that answers for the wrong item costs money at any scale.

# Which answers hold in the chapter 6 set on the workbook a director takes in the room, and why?

Answers: 1c 2d 3b 4c 5a 6d

Meera's chief of staff will hand the workbook to a director mid-meeting, and the sheet has to
recalculate in front of the room without lying. The protect list holds the fifty Retail-Plus members,
Kalpa's paid membership tier, with the highest revenue from April to September 2026, in rows 2 to 51,
and its foot reads Rs 7,14,890. SUBTOTAL skips rows a filter hides whatever its first argument; 109
and 103 also skip rows hidden by hand, while 9 and 3 keep them. A yellow input cell holds an
assumption, every other cell a formula, and the Checks tab's release holds whatever a failing check
names. Three of the six items are design items: 4, 5 and 6.

**Who needs the answer.** You, checking your six letters after the lab or tonight. The workbook leaves
your hands on Monday, and every wrong letter here is a number a director reads in the room with
nobody beside them to say it is wrong.

**The questions on the way.**

- Which idea does the chapter 6 set test: that a sheet a director changes must never lie silently?
- Why does each of the six keys hold, from the Mumbai foot to the typed-over cell?
- Why is option b in item 6, holding only the typed-over cell, the wrong answer worth arguing about?
- Where did Barclays buy contracts that sat in hidden rows of a spreadsheet?

## Which idea does the chapter 6 set test: that a sheet a director changes must never lie silently?

A director will filter, sort, type and ask what-ifs, and three of those change what a number means
with no error on screen. The day's answer is a sheet built so that every change either moves a
number honestly or turns a check red: a foot that follows the filter, assumptions in yellow inputs
that formulas read, and a release that holds whatever does not tie. The design items ask when that
sheet is the wrong vehicle, how a what-if is built, and what a failing check holds.

## Why does each of the six keys hold, from the Mumbai foot to the typed-over cell?

### Q1. What is the foot doing when the list is filtered to Mumbai and still reads Rs 7,14,890?

Eleven Mumbai members show on screen, and the foot is `=SUM(E2:E51)`.

The key is c, "Adding all fifty members, whatever the filter hides". SUM adds every cell in its
range, hidden or not, so the foot still reads the whole list's Rs 7,14,890, while the eleven on screen
spent Rs 1,56,790. A Mumbai budget sized on the foot would be 4.6 times too big.

- a, "Adding the eleven Mumbai members at their half-year revenue": the eleven add to Rs 1,56,790, so
  a foot that read them would have moved.
- b, "Adding only the Mumbai members who placed an order in Q2": the foot knows nothing about
  quarters, and the list's revenue covers both.
- d, "Adding every Mumbai customer from every one of the segments": the foot's range is the fifty
  list rows, all Retail-Plus.

### Q2. Which foot adds only the rows on screen, however the others were hidden?

A filter or a hand may hide the rows.

The key is d, `=SUBTOTAL(109,E2:E51)`. Microsoft's page says SUBTOTAL "ignores any rows that are not
included in the result of a filter, no matter which function_num value you use", and the 101 to 111
values also ignore rows hidden by hand (Microsoft Support, SUBTOTAL function, checked 30 September
2026). Filtered to Mumbai it reads Rs 1,56,790, and `=SUBTOTAL(103,A2:A51)` beside it counts 11 of 50.

- a, `=SUM(E2:E51)`: adds every row, which is the trap in item 1.
- b, `=SUBTOTAL(9,E2:E51)`: skips filtered rows and keeps rows hidden by hand.
- c, `=SUMIFS(E2:E51,C2:C51,"Mumbai")`: it reads Rs 1,56,790 for Mumbai whatever is on screen, which
  makes it the second route for the visible foot, and it shows Mumbai even after the director filters
  to Pune.

### Q3. What do SUM, SUBTOTAL(9) and SUBTOTAL(109) read on five invented rows?

Rows of Rs 100 to Rs 500; the Rs 500 row is filtered out and the Rs 100 row hidden by hand.

The key is b, "Rs 1,500, Rs 1,000 and Rs 900". SUM adds all five, Rs 1,500. SUBTOTAL(9) skips the
filtered Rs 500 and keeps the hand-hidden Rs 100, Rs 1,000. SUBTOTAL(109) skips both, Rs 200 plus
Rs 300 plus Rs 400, Rs 900. On LibreOffice 24.2.7.2 the team checked the same rule: SUM over three
rows with one hidden by hand gave 60, and SUBTOTAL(109) gave 40.

- a, "Rs 1,500, Rs 1,500 and Rs 900": SUBTOTAL(9) does skip filtered rows.
- c, "Rs 1,000, Rs 1,000 and Rs 900": SUM skips nothing.
- d, "Rs 1,500, Rs 900 and Rs 900": SUBTOTAL(9) keeps a row hidden by hand.

### Q4. Which way does a board pack go when its readers will change nothing?

A design item. The audit committee will read the pack and change nothing.

The key is c, "A PDF of the checked sheet, since nothing in it has to recalculate". The workbook's
yellow inputs and Checks tab exist for readers who change things; for readers who only read, a PDF of
a sheet whose checks all passed carries every number and cannot be typed over. This is the fact that
switches chapter 6's choice.

- a, "The same workbook, since its Checks tab protects any reader of it": the Checks tab only helps a
  reader who opens it and understands it, and this reader needs neither.
- b, "The workbook with every cell protected, so nobody can type over one": it works, and a PDF does
  the same with nothing to unlock and no formulas to break when the file is opened elsewhere.
- d, "A copy of the workbook for each member, so each one can read alone": copies drift apart, and
  nobody can later say which one is right.

### Q5. Where does a director's voucher go, and what does the sheet show for Mumbai?

A design item. A Rs 600 voucher in yellow cell B1, ids in A2:A51, eleven Mumbai rows on screen.

The key is a, `=B1*SUBTOTAL(103,A2:A51)`, showing Rs 6,600. The formula reads the director's input
and counts only the rows on screen, Rs 600 times 11. Change B1 and the cost moves in front of the room;
change the filter and it follows. The list's own figures never change, because the assumption sits
beside them.

- b, `=B1*COUNTA(A2:A51)`, showing Rs 30,000: COUNTA counts all fifty rows, whatever the filter
  hides.
- c, "Rs 6,600 typed in, since the answer is right": right today, and dead the moment the director
  changes the voucher or the filter, with no trace of how it was made.
- d, `=600*SUBTOTAL(103,A2:A51)`, showing Rs 6,600: the number is right and the assumption is buried
  inside the formula, so the director cannot change it without editing a formula.

### Q6. What does the release say when the typed-over check holds?

A design item. Four lines pass; the ISFORMULA line holds, since one cell on the Tree tab holds a typed
figure.

The key is d, "Hold the whole workbook until the cell is restored from its formula". A typed figure
feeds every formula that reads it, so nobody can say which other numbers it has moved, and the
release holds everything until the formula is back. A failing source check holds only the part built
on that source; a typed-over formula holds the whole file.

- a, "Ship everything, since four of the five checks pass": a release is not a vote, since each check
  guards something different.
- b, "Hold the one cell that was typed over, and ship every other number": the cell's figure has
  already flowed into every number that reads it.
- c, "Ship everything, with the typed-over cell coloured red for the room": colour warns the reader of
  one cell and leaves the numbers it moved looking right.

## Why is option b in item 6, holding only the typed-over cell, the wrong answer worth arguing about?

Because it sounds precise. It holds exactly the cell that is wrong and ships the rest, which is the
right rule for a failing source check, where one part sits on one export. A typed-over formula is
different: the figure feeds the tree's totals, the card's change and anything else that reads it, so
the damage is not confined to the cell. The test is to ask which numbers read the failing thing, and
for a typed figure the honest answer is that nobody knows without tracing every formula.

## Where did Barclays buy contracts that sat in hidden rows of a spreadsheet?

In September 2008 Barclays bought parts of the bankrupt Lehman Brothers. A law firm reformatting a
spreadsheet of the contracts into a PDF for the court's website exposed rows that had been hidden, and
"contracts that had been marked as "hidden" in the spreadsheet when it was received by the law firm
were added to the purchase offer during the reformatting process"; Barclays then asked the court to
exclude 179 contracts it said were included by mistake (Computerworld, 14 October 2008, checked 30
September 2026). Rows nobody could see still counted, the same rule as a SUM under a filter.

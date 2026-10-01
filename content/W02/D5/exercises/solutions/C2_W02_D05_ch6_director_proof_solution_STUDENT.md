# Which answers hold in the chapter 6 set on the workbook a director takes in the room, and why?

Answers: 1c 2d 3b 4b 5a 6d

Meera's chief of staff will hand the workbook to a director mid-meeting, and the sheet has to
recalculate in front of the room without lying. The protect list holds the fifty Retail-Plus members,
Kalpa's paid membership tier, with the highest revenue from April to September 2026, in rows 2 to 51,
and its foot, the total at the bottom of the list, reads Rs 7,14,890. SUBTOTAL skips rows a filter
hides whatever its first argument; 109 and 103 also skip rows hidden by hand, while 9 and 3 keep
them. A yellow input cell holds an assumption, every other cell a formula, and the Checks tab's
release ships a part only when every check behind it passes. Three of the six items are design
items: 4, 5 and 6.

**Who needs the answer.** You, checking your six letters after the lab or tonight. The workbook leaves
your hands on Monday, and every wrong letter here is a number a director reads in the room with
nobody at the table to say it is wrong.

**The questions on the way.**

- Which skill does the chapter 6 set test?
- Why does each of the six keys hold, from the Mumbai foot to the typed-over cell?
- Why is holding the tree and the front-page card (item 6, c) the most tempting wrong answer?
- Where did Barclays buy contracts that sat in hidden rows of a spreadsheet?

## Which skill does the chapter 6 set test?

The skill is building a sheet a director can change without it lying. A director will filter, sort,
type and ask what-ifs, and three of those change what a number means with no error on screen. The
answer is a sheet in which every change either moves a number honestly or turns a check red: a foot
that follows the filter, assumptions in yellow inputs that formulas read, and a release that holds
whatever does not tie. The design items ask when that sheet is the wrong pack, how a what-if is
built, and what a failing check holds.

## Why does each of the six keys hold, from the Mumbai foot to the typed-over cell?

### Q1. What is the foot doing when the list is filtered to Mumbai and still reads Rs 7,14,890?

Eleven Mumbai members show on screen, and the foot is `=SUM(E2:E51)`.

The key is c, "Adding all fifty members, whatever the filter hides". SUM adds every cell in its
range, hidden or not, so the foot still reads the whole list's Rs 7,14,890, while the eleven on screen
spent Rs 1,56,790. A Mumbai budget sized on the foot would be 4.6 times too big.

- a, "Adding the eleven Mumbai members at their half-year revenue": the eleven add to Rs 1,56,790, so
  a foot that read them would have moved.
- b, "Waiting for a Refresh, since a filter changes no total until Refresh is pressed": Refresh is a
  PivotTable's step, and the foot is a formula that recalculates by itself; it reads Rs 7,14,890
  because SUM adds the hidden rows.
- d, "Adding the whole revenue column, since the foot's range runs past row 51": the range is E2:E51,
  the fifty list rows, and Rs 7,14,890 is exactly their total.

### Q2. Which foot adds only the rows on screen, however the others were hidden?

A filter or a hand may hide the rows.

The key is d, `=SUBTOTAL(109,E2:E51)`. Microsoft's page says SUBTOTAL "ignores any rows that are not
included in the result of a filter, no matter which function_num value you use", and the 101 to 111
values also ignore rows hidden by hand (Microsoft Support, SUBTOTAL function, checked 30 September
2026). Filtered to Mumbai it reads Rs 1,56,790, and `=SUBTOTAL(103,A2:A51)` beside it counts 11 of 50.

- a, `=SUM(E2:E51)`: adds every row, which is the trap in item 1.
- b, `=SUBTOTAL(9,E2:E51)`: skips filtered rows and keeps rows hidden by hand.
- c, `=SUMIFS(E2:E51,C2:C51,"Mumbai")`: it reads the city and never the screen, which makes it the
  second route for the visible foot, and it splits from the foot the moment a row is hidden by hand:
  hide one Mumbai row of Rs 9,390 and SUMIFS still reads Rs 1,56,790 while the rows on screen add to
  Rs 1,47,400. It also keeps showing Mumbai after the director filters to Pune.

### Q3. What do SUM, SUBTOTAL(9) and SUBTOTAL(109) read on five invented rows?

Rows of Rs 100 to Rs 500; the Rs 500 row is filtered out and the Rs 100 row hidden by hand.

The key is b, "Rs 1,500, Rs 1,000 and Rs 900". SUM adds all five, Rs 1,500. SUBTOTAL(9) skips the
filtered Rs 500 and keeps the hand-hidden Rs 100, Rs 1,000. SUBTOTAL(109) skips both, Rs 200 plus
Rs 300 plus Rs 400, Rs 900. On LibreOffice 24.2.7.2 the team checked the same rule: SUM over three
rows with one hidden by hand gave 60, and SUBTOTAL(109) gave 40.

- a, "Rs 1,500, Rs 1,500 and Rs 900": SUBTOTAL(9) does skip filtered rows.
- c, "Rs 1,000, Rs 1,000 and Rs 900": SUM skips nothing.
- d, "Rs 1,500, Rs 900 and Rs 900": SUBTOTAL(9) keeps a row hidden by hand.

### Q4. Which pack goes to the audit committee, and which fact would switch it?

A design item. The audit committee reads the pack and changes nothing. The workbook recalculates on
whatever laptop opens it and needs its checks run again on the day it is sent; a PDF printed once
every check reads PASS takes about two minutes, an invented estimate, and recalculates nothing.

The key is b, "The PDF, since nothing in it has to recalculate; a member who wants a what-if would switch it".
The workbook's yellow inputs and Checks tab exist for readers who change things. For readers who only
read, a PDF of a sheet whose checks all passed carries every number as it was checked, costs two
minutes, and cannot be typed over or recalculated on a laptop with another version of Excel. A member
who wants to change an assumption in the meeting is the fact that sends the workbook instead.

- a, "The workbook, since the committee should see the Checks tab; an older Excel on one laptop would switch it":
  the committee changes nothing, so it pays the workbook's costs for none of its uses, and the checks
  it would see have all passed before the PDF is printed.
- c, "The PDF, since a file nobody can change can never be wrong; a later export would switch it": a
  PDF of an unchecked sheet is as wrong as the sheet, which is why it is printed only after every
  check passes, and a later export means a new PDF after a fresh check, never the workbook.
- d, "The workbook, since one file is cheaper to keep than two; a committee with no Excel would switch it":
  the PDF is printed from the same workbook, so there is still one file to keep, and a committee that
  changes nothing gains nothing from a file that recalculates.

### Q5. Which formula prices a director's voucher for the members on screen?

A design item. The voucher, Rs 600 today, sits in yellow cell B1, the ids in A2:A51, and eleven Mumbai
rows are on screen; the cost must read Rs 6,600 now and move with the voucher and the filter.

The key is a, `=B1*SUBTOTAL(103,A2:A51)`. The formula reads the director's input and counts only the
rows on screen, Rs 600 times 11, Rs 6,600. Change B1 and the cost moves in front of the room; change
the filter and it follows. The list's own figures never change, because the assumption sits in its
own yellow cell.

- b, `=B1*COUNTA(A2:A51)`: COUNTA counts all fifty rows, whatever the filter hides, so it reads
  Rs 30,000.
- c, `=B1*11`: right today, and the count is typed in, so it stays at eleven when the director filters
  to another city.
- d, `=600*SUBTOTAL(103,A2:A51)`: right today, and the assumption is buried inside the formula, so the
  director cannot change the voucher without editing a formula.

### Q6. What does the release say when the typed-over check holds?

A design item. The release ships a part only when every check behind it passes. Four lines pass; the
ISFORMULA line holds, since one cell on the Tree tab holds a typed figure, and nobody has yet traced
which formulas on the other tabs read it.

The key is d, "Hold the whole workbook until the cell is restored from its formula". The typed-over
check reads every cell outside the yellow inputs, so it sits behind every part whose formulas could
read the typed figure, and until someone traces them that is every part. Once the formula is back,
the check reads PASS and each part ships on its own checks again. A failing source check holds only
the part built on that source; a typed-over formula holds the whole file.

- a, "Ship everything, since four of the five checks pass": a release is not a vote, since each check
  guards something different.
- b, "Hold the one cell that was typed over, and ship every other number": the cell's figure has
  already flowed into every number that reads it.
- c, "Hold the tree and the front-page card, which read the Tree tab, and ship the protect list": it
  applies the release rule as if the typed figure's reach were known, and nobody has traced whether a
  formula on the protect list's tab reads it.

## Why is holding the tree and the front-page card (item 6, c) the most tempting wrong answer?

Option c follows the release rule the item states: the typed cell sits on the Tree tab, the tree and
the card read it, so it holds those two and ships the list. The rule is right, and the step c skips is
asking which parts the typed-over check sits behind. That check reads every cell in the file, and a
typed figure feeds any formula that reads its cell, on any tab, so until someone traces those
formulas it sits behind every part. The test is to ask which numbers read the failing thing, and for
a typed figure nobody can answer without tracing every formula.

## Where did Barclays buy contracts that sat in hidden rows of a spreadsheet?

In September 2008 Barclays bought parts of the bankrupt Lehman Brothers. A law firm reformatting a
spreadsheet of the contracts into a PDF for the court's website exposed rows that had been hidden, and
"contracts that had been marked as "hidden" in the spreadsheet when it was received by the law firm
were added to the purchase offer during the reformatting process"; Barclays then asked the court to
exclude 179 contracts it said were included by mistake (Computerworld, 14 October 2008, checked 30
September 2026). Rows nobody could see still counted, the same rule as a SUM under a filter.

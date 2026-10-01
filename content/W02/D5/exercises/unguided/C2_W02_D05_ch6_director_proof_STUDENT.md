# When a director takes the workbook in the room, what can they break, and which checks catch it before anyone reads a wrong number?

Chapter 6 set, six items, after chapter 6: items 1 and 2 run live in the chapter's last three
minutes; the rest are the practice lab's stretch or tonight's work.

> "If a director changes an assumption in the room, the sheet must recalculate in front of them."
>
> Meera's chief of staff, Kalpa Retail

The protect list is the fifty Retail-Plus members, Kalpa Retail's paid membership tier, with the
highest revenue from April to September 2026; it sits in rows 2 to 51 of its tab, with member ids in
column A, cities in column C and revenue in column E, and the head of Retail-Plus sizes each city's
retention budget from it. The list's foot, the total at the bottom of the list, is `=SUM(E2:E51)` and
reads Rs 7,14,890. A filter hides the rows that fail a condition, and a director can also hide a row
by hand. `SUBTOTAL(function_num, range)` totals a range with the calculation its first argument
picks: 9 and 109 add, 3 and 103 count filled cells, and the two codes of each pair differ in which
hidden rows they leave out. A yellow input cell holds an assumption a director may change, and every
other cell holds a formula. The workbook's Tree tab holds the revenue tree by segment for both
quarters, and the front-page card reads its totals. The Checks tab has five lines, one for each way
the file can mislead: the tree may not tie to the warehouse, the protect list's source table may not
tie, the lookup may answer for an id the table does not hold, the foot may not follow a filter, and a
formula may have a figure typed over it. Each line compares a number on the sheet with one from
somewhere else and reads PASS or HOLD, and one release sentence reads all of them.

**Who needs the answer.** The chief of staff hands the laptop across the table mid-meeting, and the
head of Retail-Plus sizes each city's budget from the list. A total that keeps counting rows a filter
has hidden sizes a city's budget on the whole list, and a number typed over a formula becomes a
figure nobody can trace.

**The questions on the way.**

- What is the foot doing when the list is filtered to Mumbai and still reads Rs 7,14,890?
- Which foot adds only the rows on screen, however the others were hidden?
- What do SUM, SUBTOTAL(9) and SUBTOTAL(109) read on five invented rows?
- Which pack goes to the audit committee, and which fact would switch it?
- Which formula prices a director's voucher for the members on screen?
- What does the release say when the typed-over check holds?

Item 3's rows and item 4's two minutes are invented; the other items use Kalpa's own protect list.

Post one line of six letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxxx
```

---

### Q1. What is the foot doing when the list is filtered to Mumbai and still reads Rs 7,14,890?

The head of Retail-Plus asks to see the Mumbai members, and a director filters the city column to
Mumbai. Eleven members show on screen, and the foot still reads Rs 7,14,890. What is the foot doing?

a) Adding the eleven Mumbai members at their half-year revenue
b) Waiting for a Refresh, since a filter changes no total until Refresh is pressed
c) Adding all fifty members, whatever the filter hides
d) Adding the whole revenue column, since the foot's range runs past row 51

### Q2. Which foot adds only the rows on screen, however the others were hidden?

The list may be filtered by a director, or a row may be hidden by hand. Which foot adds only the rows
on screen in both cases?

a) `=SUM(E2:E51)`
b) `=SUBTOTAL(9,E2:E51)`
c) `=SUMIFS(E2:E51,C2:C51,"Mumbai")`
d) `=SUBTOTAL(109,E2:E51)`

### Q3. What do SUM, SUBTOTAL(9) and SUBTOTAL(109) read on five invented rows?

An invented list has five rows of Rs 100, Rs 200, Rs 300, Rs 400 and Rs 500. A director filters out
the Rs 500 row, then hides the Rs 100 row by hand. In that order, what do SUM, SUBTOTAL(9) and
SUBTOTAL(109) over the five rows read?

a) Rs 1,500, Rs 1,500 and Rs 900
b) Rs 1,500, Rs 1,000 and Rs 900
c) Rs 1,000, Rs 1,000 and Rs 900
d) Rs 1,500, Rs 900 and Rs 900

### Q4. Which pack goes to the audit committee, and which fact would switch it?

On Monday the deck pack also goes to the audit committee, whose members read it and change nothing.
Two packs are on the table, each with its cost. The workbook carries yellow inputs and a Checks tab,
recalculates on whatever laptop opens it, and needs its checks run again on the day it is sent. A
PDF printed from the workbook once every check reads PASS takes about two minutes, shows the numbers
exactly as they were checked, and recalculates nothing. Which pack goes to the committee, and which
fact would switch it?

a) The workbook, since the committee should see the Checks tab; an older Excel on one laptop would switch it
b) The PDF, since nothing in it has to recalculate; a member who wants a what-if would switch it
c) The PDF, since a file nobody can change can never be wrong; a later export would switch it
d) The workbook, since one file is cheaper to keep than two; a committee with no Excel would switch it

### Q5. Which formula prices a director's voucher for the members on screen?

A director asks what a voucher would cost for the members on screen. The voucher's value, Rs 600
today, sits in yellow cell B1, the ids sit in A2:A51, and the list is filtered to Mumbai, eleven of
the fifty rows. The cost cell must show Rs 6,600 now, and move when the director changes either the
voucher or the filter. Which formula goes in it?

a) `=B1*SUBTOTAL(103,A2:A51)`
b) `=B1*COUNTA(A2:A51)`
c) `=B1*11`
d) `=600*SUBTOTAL(103,A2:A51)`

### Q6. What does the release say when the typed-over check holds?

The release ships a part of the workbook only when every check behind it passes: the tree and the
front-page card sit on the tree's tie, and the protect list on its source tie and its lookup. On
Monday four lines read PASS, and the fifth, which tests with ISFORMULA that every cell outside the
yellow inputs still holds its formula, reads HOLD: one cell on the Tree tab holds a typed figure. The
check names the cell, and nobody has yet traced which formulas on the other tabs read it. What does
the release say?

a) Ship everything, since four of the five checks pass
b) Hold the one cell that was typed over, and ship every other number
c) Hold the tree and the front-page card, which read the Tree tab, and ship the protect list
d) Hold the whole workbook until the cell is restored from its formula

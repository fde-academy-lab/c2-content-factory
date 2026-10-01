# When a director takes the workbook in the room, what can they break, and which checks catch it before anyone reads a wrong number?

Chapter 6 set, six items, after chapter 6: items 1 and 2 run live in the chapter's last three
minutes; the rest are the practice lab's stretch or tonight's work.

> "If a director changes an assumption in the room, the sheet must recalculate in front of them."
>
> Meera's chief of staff, Kalpa Retail

The protect list is the fifty Retail-Plus members, Kalpa Retail's paid membership tier, with the
highest revenue from April to September 2026; it sits in rows 2 to 51 of its tab, with member ids in
column A, cities in column C and revenue in column E, and the head of Retail-Plus sizes each city's
retention budget from it. Its foot, `=SUM(E2:E51)`, reads Rs 7,14,890. A filter hides the rows that
fail a condition, and a director can also hide a row by hand. `SUBTOTAL(function_num, range)` adds or
counts a range in a way chosen by its first argument: 9 adds and 3 counts filled cells, and both skip
the rows a filter hides; 109 and 103 do the same and also skip rows hidden by hand. A yellow input
cell holds an assumption a director may change, and every other cell holds a formula. The Checks tab
turns each of the day's traps into a line that compares a number on the sheet with one from somewhere
else and reads PASS or HOLD, and one release sentence reads all of them.

**Who needs the answer.** The chief of staff hands the laptop across the table mid-meeting, and the
head of Retail-Plus sizes each city's budget from the list. A total that keeps counting rows a filter
has hidden sizes a city's budget on the whole list, and a number typed over a formula becomes a
figure nobody can trace.

**The questions on the way.**

- What is the foot doing when the list is filtered to Mumbai and still reads Rs 7,14,890?
- Which foot adds only the rows on screen, however the others were hidden?
- What do SUM, SUBTOTAL(9) and SUBTOTAL(109) read on five invented rows?
- Which way does a board pack go when its readers will change nothing?
- Where does a director's voucher go, and what does the sheet show for Mumbai?
- What does the release say when the typed-over check holds?

Item 3's rows are invented; the other items use Kalpa's own protect list.

**What you post.** One line of six letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxxx
```

---

### Q1. What is the foot doing when the list is filtered to Mumbai and still reads Rs 7,14,890?

The head of Retail-Plus asks to see the Mumbai members, and a director filters the city column to
Mumbai. Eleven members show on screen, and the foot still reads Rs 7,14,890. What is the foot doing?

a) Adding the eleven Mumbai members at their half-year revenue
b) Adding only the Mumbai members who placed an order in Q2
c) Adding all fifty members, whatever the filter hides
d) Adding every Mumbai customer from every one of the segments

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

### Q4. Which way does a board pack go when its readers will change nothing?

The team's default for Monday is a workbook with yellow inputs, every other cell a formula, and a
Checks tab. A second pack goes to the audit committee, who will read it and change nothing. Which way
does the second pack go?

a) The same workbook, since its Checks tab protects any reader of it
b) The workbook with every cell protected, so nobody can type over one
c) A PDF of the checked sheet, since nothing in it has to recalculate
d) A copy of the workbook for each member, so each one can read alone

### Q5. Where does a director's voucher go, and what does the sheet show for Mumbai?

A director asks what a Rs 600 voucher would cost for the members on screen. The voucher sits in yellow
cell B1, the ids in A2:A51, and the list is filtered to Mumbai, eleven of the fifty rows. What goes
in the cost cell, and what does it show?

a) `=B1*SUBTOTAL(103,A2:A51)`, showing Rs 6,600
b) `=B1*COUNTA(A2:A51)`, showing Rs 30,000
c) Rs 6,600 typed in, since the answer is right
d) `=600*SUBTOTAL(103,A2:A51)`, showing Rs 6,600

### Q6. What does the release say when the typed-over check holds?

The Checks tab reads PASS on four lines and HOLD on the line that tests, with ISFORMULA, that every
cell outside the yellow inputs still holds its formula: one cell on the Tree tab holds a typed figure.
What does the release say?

a) Ship everything, since four of the five checks pass
b) Hold the one cell that was typed over, and ship every other number
c) Ship everything, with the typed-over cell coloured red for the room
d) Hold the whole workbook until the cell is restored from its formula

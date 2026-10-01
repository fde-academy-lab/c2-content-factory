# Which answers hold in the second case on the director's five lakh, and why?

Answers: 1a 2c 3b 4d 5a

A director of Kalpa Retail asked, in the room, for Rs 5,00,000 to be typed into Retail-Plus's Q2 cell
so the front-page card would stop frightening people, and for the source to be fixed later.
Retail-Plus, the paid membership tier, booked Rs 5,85,770 in Q1 (April to June 2026) and Rs 4,13,380
in Q2 (July to September 2026), down 29.4 percent; counted once per order the export ties to the
warehouse, Rs 10,00,00,000 in Q1 and Rs 9,84,00,000 in Q2. The team's operating rule gives the number
to the warehouse and the last mile to the workbook, with what-ifs as labelled inputs and nobody
typing over the source. The pair worked the scene in
`notebooks/C2_W02_D05_ex2_second_case_STUDENT.ipynb`, five lettered choices, and the executed
solution, `C2_W02_D05_ex2_second_case_solution_STUDENT.ipynb` in this folder, runs every key. Two of
the five items are design items: 2 and 5.

**Who needs the answer.** You and your partner, checking your five letters and your three lines after
the case. The director will ask again on Monday, and the line that holds is the one you can say with
its number.

**The questions on the way.**

- Which idea does the second case test: that a what-if sits beside the actual and never over it?
- Which numbers stand behind the pair's three lines?
- Why does each of the five keys hold, from the moved card to the labelled scenario?
- What three lines held the line?
- Where did pairs go wrong in the role play, and why does each move fail?

## Which idea does the second case test: that a what-if sits beside the actual and never over it?

A director's assumption is a fair question, and a sheet is a good place to answer it, as long as the
assumption sits in its own labelled input beside the number Finance books. Typed over the source, the
same figure moves the card, fails the drift check, flags on the formula check and disappears at the
next refresh with nobody able to say why it was there.

## Which numbers stand behind the pair's three lines?

| Step | Number | What it means |
|---|---|---|
| 1 | The card moves from down 29.4 percent to down 14.6 percent | Rs 5,00,000 against Q1's Rs 5,85,770, a fall Finance's books do not show |
| 2 | The drift on Q2 is Rs 86,620 | The typed Rs 5,00,000 less the export's Rs 4,13,380, caught against the warehouse's Q2 |
| 3 | One cell flagged | The Q2 cell holds a typed figure where a formula should be |
| 4 | Monday's refresh restores Rs 4,13,380 | The typed figure, and any record of why it was there, is gone |
| 5 | Two lines on the card: actual down 29.4 percent, the director's scenario down 14.6 percent | The question is answered and the actual stays |

## Why does each of the five keys hold, from the moved card to the labelled scenario?

### Q1. Which line is the card the room now sees for Retail-Plus?

The director's Rs 5,00,000 sits in the Q2 cell, and the card reads the cell.

The key is a, `shown = change(export_q1, typed_q2)`. The card recalculates from whatever sits in its
cells, so it measures the typed Rs 5,00,000 against Q1's Rs 5,85,770: down 14.6 percent.

- b, `shown = change(export_q1, export_q2)`: the card before the edit; the sheet reads the cell, not
  the export.
- c, `shown = change(typed_q2, export_q2)`: measures the export's Q2 against the typed figure, which
  no card prints.
- d, `shown = typed_q2 / export_q2 * 100`: a ratio of two Q2 figures, which no card prints either.

### Q2. Which comparison catches a figure typed into the sheet?

A design item. The check has to stay quiet on the sheet as exported and fire on the edited one.

The key is c, `drift = lambda s: int(s["Q2"].sum()) - wq["Q2"]`. The sheet's Q2 total against the
warehouse's Q2: zero on the clean sheet, Rs 86,620 on the edited one.

- a, `drift = lambda s: len(s) - 4`: counts segments, which an edit never changes.
- b, `drift = lambda s: int(s["Q1"].sum()) - wq["Q1"]`: looks at the quarter nobody touched.
- d, `drift = lambda s: 0 if s is sheet else 1`: compares the sheet with itself by name, so it fires
  on any copy and says nothing about the numbers.

### Q3. Which rule flags a figure typed over a formula?

Outside the yellow inputs, every cell should hold a formula.

The key is b, the rule that flags a cell outside the inputs whose content is not a formula, which is
what ISFORMULA tests in a sheet. It flags nothing on the clean sheet and the one typed cell on the
edited sheet.

- a, flagging every cell that holds a number: it would flag every yellow input too, which a director
  is allowed to change.
- c, flagging every cell that differs from one saved copy: it breaks after any honest change, such as
  next week's refresh.
- d, flagging the input cells: those are the cells a director is meant to change.

### Q4. Which line is Monday's refresh?

A refresh rebuilds the sheet from a fresh export.

The key is d, `refreshed = orders.pivot_table(index="segment", columns="quarter", values="order_amount", aggfunc="sum")`.
The sheet is computed again from the export, so Q2 returns to Rs 4,13,380 and the drift check reads
zero; the typed figure and its reason are gone without a trace.

- a, `refreshed = edited.copy()`: keeps the typed figure, which is the drift the rule exists to stop.
- b, `refreshed = edited.fillna(0)`: keeps it too.
- c, `refreshed = sheet.where(edited == sheet, edited)`: keeps the edited value wherever the two
  differ, which is exactly the typed cell.

### Q5. Which card answers the director and keeps the number Finance signs?

A design item. The question is fair: what would the card say if Retail-Plus came back to Rs 5,00,000?

The key is a, a card with two labelled lines: the actual, down 29.4 percent, and the director's
scenario, down 14.6 percent, read from a yellow input. The room gets its answer, and the actual stays
the number Finance books.

- b, a card whose only line, labelled actual, reads the director's figure: the edit again under a new
  name.
- c, a card with the actual alone: it refuses a fair question and sends the director back to typing
  over cells.
- d, the two lines with their labels swapped: the page then calls the scenario the actual.

## What three lines held the line?

"Yes: here is the card with your assumption, Retail-Plus back to Rs 5.00 lakh, as a labelled scenario
line, down 14.6 percent on Q1. The actual stays at Rs 4.13 lakh, down 29.4 percent, because it is the
number Finance books and the one Anand's analyst will check next week. Every refresh compares the
sheet's quarters with the warehouse's, and a typed figure would have shown up as a Rs 86,620 drift
and disappeared on Monday with no record of why."

## Where did pairs go wrong in the role play, and why does each move fail?

| The move | Why it fails |
|---|---|
| "No, the sheet must match Finance" and nothing more | It refuses a fair question, and the director types the figure in anyway |
| Typing the figure with a comment saying who changed it | The comment is lost at the next refresh, and the card shows the scenario as the actual all week |
| A separate copy of the workbook for the director | Two files leave the meeting, and nobody can later say which one the deck came from |
| Arguing about whether Retail-Plus will recover | It is the director's assumption to make; the pair's job is where the assumption sits |

# Solution: the director who wants to edit the source

Answers: 1c 2d 3a 4b 5a 6c

Hands-on picks, the notebook's four letters in order: `badb`

## The idea being tested

The director's question is legitimate and the edit is not. A typed-over cell makes the card compute
from a hope: Retail-Plus reads down 14.6 percent where the export says 29.4. The sheet then disagrees
with Finance's books until Monday's refresh wipes the edit and nobody can say why the two differed.
A labelled input beside the source gives the director the number to discuss and keeps the number
Finance signs.

## The rule, in three lines

1. The warehouse owns the number: anything Finance audits, and anything that needs a join, a dedupe
   or a cleaning step.
2. pandas owns the iteration: the analyst's question that changes daily, until Finance relies on it.
3. Excel owns the last mile: it presents, slices and looks up an export, takes what-ifs as labelled
   inputs, and nobody types over the source.

## What a strong defence sounds like

"Yes, I will show five lakh as your scenario, on its own line beside the actual. The actual comes
from the export Finance ties to, and typing over it breaks that tie for a week, until the refresh
wipes it. Every refresh ties the sheet back to the warehouse, so a drift shows the same day."

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | c | It answers the question the director is asking and keeps the source intact. | a refuses a legitimate question, and the director types over the cell anyway. b is the edit. d turns a scenario into a sign-off process nobody needs. |
| 2 | d | A labelled input is a what-if; the actual line still ties to the warehouse. | a is the edit with a note on it. b edits the source of truth. c makes two versions of one deck that will drift apart. |
| 3 | a | The warehouse's Q2 is the control total; an edit moves the sheet's Q2 and nothing else. | b counts rows, which an edit never changes. c compares wording. d compares dates, which say nothing about numbers. |
| 4 | b | The refresh rebuilds the tree from the export, so the typed value and any record of why it was typed are gone. | a describes a protection Excel does not apply to a rebuilt range. c never happens. d describes a feature nobody built. |
| 5 | a | Removing rows is a cleaning step with no audit trail in a sheet, and the next export brings the rows back. | b, c and d are the last mile Excel owns. |
| 6 | c | Finance's audit decides the owner; the room decides only who presents. | a lets the room own an audited number. b is the iteration, which ends once Finance relies on it. d names a person where a system belongs. |

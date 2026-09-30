# Solution: the escalated case

Answers: 1d 2a 3b 4c 5d 6a 7c 8b

Hands-on picks, the notebook's seven letters in order: `cbcdabb`

## The idea being tested

The three deliverables are one piece of work, because they share a grain and a control total. The
tree has to come from the raw export, since only it carries order dates, and it has to count each
order once to tie to the warehouse. The protect list comes from the customer table, which must tie on
its own. The card inherits whatever the tree counted. A release that holds what does not reconcile is
the answer to "what can I trust it for".

## The solution workbook

`demos/C2_W02_D05_deck_pack_STUDENT.xlsx` is the reference build: a Raw tab and a Customers tab with
the exports as values; a Tree tab that is a pivot written as `SUMIFS` over a first-row flag; a Protect
tab with a rank column, a lookup with an exact match and its not-found path, and SUBTOTAL(109) at the
foot; a FrontPage tab whose card sentence and trend recompute from a yellow scope cell; and a Checks
tab whose release sentence reads: "Send the tree and the front page. Hold the protect list until the
customer table reconciles to the warehouse." Its numbers are proved by recalculating it through
LibreOffice.

| Part | What the reference build shows |
|---|---|
| 1 | Q1 Rs 10,00,00,000 and Q2 Rs 9,84,00,000, a fall of 1.6 percent; Retail-Plus customers 91 to 76 and orders per customer 2.36 to 1.84 |
| 2 | Fifty members, Rs 7,14,890 together, cut-off Rs 8,580; C-0152 at rank 1 with Rs 25,840; C-0195 not in the table |
| 3 | "All segments, Q2, July to September 2026: Rs 9.84 crore, down 1.6 percent on Q1, April to June 2026 (Rs 10.00 crore); 100.0 percent of company revenue in Q2." |
| 4 | The tree and the card ship; the protect list is held until the customer table ties |
| 5 | The seven letters above, and the checks all passing |

**The note to the data platform lead.** "The customer table exported for Monday does not tie to the
warehouse: its revenue and order count fall short of the Q1 and Q2 totals. Please rerun the export;
the protect list waits for it."

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | d | Only the raw export carries order dates, and only a count per order ties to the warehouse. | a and b invent a split the customer table cannot make. c counts per payment row and splits on when money arrived, which is a collections question. |
| 2 | a | The warehouse's two quarters are the control total. | b is the double count itself. c is a different export that has to tie on its own. d is collected money, which differs from booked. |
| 3 | b | A list built on a table that does not tie may be missing members, and the fix is upstream. | a confuses recalculating with being right. c ships a list nobody can act on safely. d cleans data in a sheet during a meeting, which the operating rule forbids. |
| 4 | c | One present id proves the found path, one missing id proves the not-found path. | a and b test only present ids, where an approximate match also looks right. d tests only the missing path. |
| 5 | d | Every part of the card is a function of the scope, and the sentence has to say which scope it shows. | a and b leave the comparison or the base pointing at the company while the number does not. c turns the scope into decoration. |
| 6 | a | The inputs are the assumptions; everything else is computed. | b and d type over computed cells, which is drift. c edits the source, the one thing that must never happen in a sheet. |
| 7 | c | SUBTOTAL(109) follows a filter, so an unchanged foot means SUM or no filter at all. | a and d read a defect as a coincidence. b contradicts itself: if a filter hid rows, SUBTOTAL(109) would move. |
| 8 | b | It says what ties, what is held and why, which is what "trust it for" asks. | a confuses recalculating with correctness. c undersells numbers that tie to the rupee. d forbids the assumptions the chief of staff asked to change. |

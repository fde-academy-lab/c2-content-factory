# The escalated case: Monday's deck pack, end to end

Sixty minutes, alone, at the start of the afternoon. No hints. The solution, the deck pack workbook in
`demos/` and the executed hands-on notebook, opens at the debrief.

> "Build me the file I open on Monday: the tree by segment for both quarters, the protect list with
> the lookup, and the front-page number with its trend. I will change things in the room. Tell me
> what I can trust it for."
>
> Meera's chief of staff, Kalpa Retail

You have the two exports in `data/`: `C2_W02_D05_customer_table_STUDENT.csv`, one row per customer,
and `C2_W02_D05_raw_export_STUDENT.csv`, one row per payment. Monday's warehouse numbers are Rs 10.00
crore for Q1 and Rs 9.84 crore for Q2. Build in one new Excel workbook, with the two exports pasted
in as values on their own tabs and every other number a formula.

---

## Part 1. The tree, fifteen minutes

The revenue tree by segment for Q1 and Q2: customers, orders per customer, revenue per order and
revenue. Count each order once. The tab's total ties to the warehouse to the rupee, and a cell on the
tab says whether it does.

## Part 2. The protect list and the lookup, twelve minutes

The fifty Retail-Plus members with the highest revenue across both quarters, from the customer table,
with the list size in a yellow cell. A lookup by member id that returns the member's revenue and
place on the list, or the words "not in the table", and test it before you trust it. The foot of
the list adds only the rows on screen.

## Part 3. The front-page card, twelve minutes

Q2 revenue with its period, its comparison with Q1 and its share of company revenue, as one sentence
built by formula, and a monthly trend beside it. The card's scope sits in a yellow cell with the
choices all segments, all except Business and each segment.

## Part 4. What ships, six minutes

A tab of checks, one per deliverable, each saying whether its numbers tie to the warehouse, and a
release sentence saying what goes into Monday's deck and what is held, with the reason. Write the
two-line note you would send the data platform lead about anything held.

## Part 5. The numbers a second way, fifteen minutes

Open `notebooks/C2_W02_D05_ex1_hands_on_STUDENT.ipynb`. Seven lettered `TODO` markers across six
steps reach your sheet's numbers in pandas, and each step ends on checks. Run it from the top; it
stops at the first placeholder until you fill it, which is intended. Post the seven letters in one
line.

---

## Eight items on the calls you made

Post exactly this shape, the letters in item order, no spaces: `xxxxxxxx`

### Q1. Which export does the tree by quarter have to come from?

a) The customer table, split on each customer's last order date
b) The customer table, with each customer's revenue halved per quarter
c) The raw export, filtered to rows with a payment date in the quarter
d) The raw export, counted once per order and split on the order date

### Q2. Before the Tree tab ships, what must its total equal?

a) Rs 19,84,00,000, the warehouse's two quarters
b) Rs 39,40,95,490, the export's column total
c) The customer table's revenue column total, both quarters
d) The paid_amount column's total in the export

### Q3. The customer table's revenue does not tie to the warehouse. What happens to the protect list on Monday?

a) It ships, since its ranking uses a formula that recalculates
b) It is held, and the data platform lead is asked to rerun the export
c) It ships with a footnote saying the table may be incomplete
d) It is rebuilt by hand from the raw export by the analyst in the meeting

### Q4. Which pair of ids tests the lookup before the chief of staff uses it?

a) C-0152 and C-0194, the top of the list and a mid-list member
b) C-0001 and C-0340, the first and the last ids in the customer table
c) C-0152 and C-0195, a member on the list and an id not in the table
d) C-0195 and C-0999, two ids nobody has ever looked up in a meeting

### Q5. A director changes the card's scope to all except Business. What else must change on the card, by formula?

a) Only the number, since the comparison and the base belong to the whole company
b) The number and the comparison, and the base stays at 100 percent
c) Nothing, since the scope is a label for the reader of the card
d) The number, the comparison, the base and the scope printed in the sentence

### Q6. Which cells may a director type into in the room?

a) The yellow input cells, and nothing else
b) Any cell on the Tree and FrontPage tabs
c) The Raw tab, to correct a row they know is wrong
d) The card sentence, to soften its wording

### Q7. The foot of the protect list reads the same with and without a city filter. What does that tell you?

a) The list has no members outside the chosen city
b) The foot is SUBTOTAL(109) and the filter hid no rows
c) The foot is SUM, or no filter was actually applied to it
d) The foot is correct, since the two totals agree with each other

### Q8. What is the one sentence to the chief of staff about what the file can be trusted for?

a) "Everything recalculates live, so every number is right whatever you change"
b) "The tree and the card tie to Finance; the list is held until its export ties"
c) "The numbers are approximate, so treat the whole file as a guide for discussion"
d) "The file is final; please do not change any cell before Monday's meeting"

# The second case, part two: pick the tool for five asks

Fifteen minutes in pairs, inside the second case. Each ask is one a Kalpa stakeholder has made
this week. Pick the tool, then write the reason in one line beside your letter: who has to trust,
rerun or audit the number decides it.

Post one line, five letters in item order, no spaces:

```
Post exactly this shape: xxxxx
```

---

### Q1

Anand Iyer, the finance controller: "Revenue by segment for both quarters, every Monday, computed
so my analyst can rerun it herself and get the same number." Which tool owns it?

a) Plain Python, a script whose loop shows each step to the reader
b) SQL, a view in the warehouse that anyone with access can rerun
c) pandas, a notebook the analyst refreshes by hand each Monday
d) Excel, a workbook Anand's analyst can open without a login

### Q2

The marketing lead: "This afternoon I want to see recency cut five different ways, 30, 45, 60,
90 days and by segment, before I decide the win-back threshold." Which tool fits?

a) Plain Python, since each cut is a short loop anyone can follow
b) SQL, a view per threshold so each cut is saved in the warehouse
c) pandas, on the customer table, one line per cut and a chart each
d) Excel, a pivot on last week's export with the thresholds typed in

### Q3

A new joiner on the team asks: "How exactly is orders per customer computed? Show me every
step, I want to check it by hand on ten orders." Which tool do you use to show them?

a) Plain Python, a loop over ten orders with the running totals printed
b) SQL, a GROUP BY with count and count distinct in one statement
c) pandas, a groupby chain with a named aggregation per measure
d) Excel, a pivot table with the order ids dragged into its values box by hand

### Q4

The campaign platform sends a CSV of this week's exposures, once, and the marketing lead wants
it matched to the customer table before lunch to see who was reached. Which tool fits?

a) Plain Python, reading the CSV row by row into a dictionary of customers
b) SQL, after the platform lead loads the file into a new warehouse table
c) pandas, reading the file and merging it with `validate="one_to_one"`
d) Excel, a lookup from the CSV into last Friday's exported customer table

### Q5

Kavya: "The count of orders per quarter that the auditor will rerun next month, from the same
source, and expect to match." Which tool owns it?

a) Plain Python, a script checked into the repository beside the notebook
b) SQL, a statement against the warehouse that the auditor can run again
c) pandas, a notebook with its outputs saved, so the auditor can read them
d) Excel, a sheet with the counts pasted in and the date on the tab

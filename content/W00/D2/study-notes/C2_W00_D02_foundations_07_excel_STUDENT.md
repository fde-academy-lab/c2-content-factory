# Chapter 7. A PivotTable is GROUP BY for people who will never see your code

Week 0 foundations guide, chapter 7 of 9. [Back to the map](C2_W00_D02_foundations_00_map_STUDENT.md).

Excel is secondary in Week 0 and unavoidable at work: every number you compute will be checked by
someone in a spreadsheet, and the fastest way to be trusted is to be able to rebuild your answer
where they can see it. Reading time: 5 minutes.

## What you can now do

You can turn a range into a Table so formulas stay correct as rows are added. You can build a
PivotTable that reproduces a `GROUP BY`. You can write `SUMIFS` and `COUNTIFS` for a filtered total.
You can look up a value from another table with `INDEX` and `MATCH`. You can say where Excel stops
and a notebook starts.

## Where this sits

**What this chapter covers.** Tables, PivotTables, conditional totals, lookups, and the limits. It
is short because the operations are Chapter 2's with different spelling, and the figure below is the
whole map.

**Placement.** Excel is the seventh cell of the bottom band and a floating slot in Week 0 if time
permits. It reappears whenever a stakeholder wants to check a number.

**Outcome tie.** The specific moment is the Build 1 presentation in Week 3, when a panel member
opens the group's numbers in a spreadsheet and asks why the pivot disagrees with the notebook. It
should not, and this chapter is how you make sure.

**What was left out.** Charts, Power Query and the Data Model are not needed in this programme's
first weeks.

## The picture to remember: one question, three tools

One question, three tools: the operation is the same; only the spelling changes

| Question | SQL | pandas | Excel |
|---|---|---|---|
| Revenue per tier | GROUP BY tier | groupby('tier').sum() | PivotTable, or SUMIFS |
| Paid orders only | WHERE status='paid' | df[df.status=='paid'] | filter, or SUMIFS criteria |
| Latest call per ticket | ROW_NUMBER() OVER | sort + drop_duplicates | sort, then remove duplicates |
| Attach city to orders | JOIN customers | merge(customers) | INDEX and MATCH, or XLOOKUP |

*Figure 27. Four questions from Meera's table, answered in SQL, pandas and Excel. The operation is identical; only the spelling changes.*

## Tables, not ranges

Select the data and press Ctrl+T, or Insert then Table. A Table has a name, its formulas fill every
row, and a PivotTable built on it grows with it. A range does none of that, and most "the total is
wrong" complaints in spreadsheets are a range that stopped one row short.

## The PivotTable is GROUP BY

Insert then PivotTable, put `tier` in Rows, `amount` in Values, `status` in Filters set to paid.
That is `SELECT tier, SUM(amount) FROM orders WHERE status = 'paid' GROUP BY tier`. Drag `quarter`
to Columns and you have the cross-tab Meera's table was drawn from.

**IN THE FIELD.** Microsoft's own guide to creating a PivotTable applies to Excel for Microsoft 365 through Excel 2016 and walks the same four steps: select the cells, Insert then PivotTable, choose the placement, tick the fields (source: [support.microsoft.com](https://support.microsoft.com/en-us/) (checked 30 September 2026), "Create a PivotTable to analyze worksheet data").

## SUMIFS and COUNTIFS

A pivot is a report; a formula is a single cell you can point at.
`=SUMIFS(amount, tier, "Plus", status, "paid")` is the Plus revenue, and
`=COUNTIFS(tier, "Plus", status, "paid")` is the order count; divide them for the average order
value. Column names in these formulas are the Table's column names, so they survive sorting and new
rows.

**WATCH OUT.** `SUMIF` with one criterion and `SUMIFS` with several take their arguments in a
different order. Use `SUMIFS` everywhere, even for one criterion, and the order is always range,
criteria range, criteria.

## INDEX and MATCH

To attach a customer's city to an order,
`=INDEX(customers[city], MATCH([@customer_id], customers[customer_id], 0))` finds the row in the
customers table and returns the city. `XLOOKUP` does the same in one function on current Excel;
`INDEX` and `MATCH` work everywhere, including the LibreOffice this programme's workbooks are
checked in. A lookup that finds two rows returns the first and says nothing, which is Chapter 2's
fan-out in a spreadsheet.

## Where Excel stops

Above about a million rows the sheet will not hold the data. Above about ten steps, a spreadsheet
cannot be reviewed, because the steps are hidden inside cells. And a spreadsheet cannot be rerun on
next month's file without hand-editing. Those three limits are where the notebook and the query
begin, and the programme's rule is simple: compute in the notebook or the database, then rebuild the
one headline number in the sheet so the stakeholder can see it agree.

## Try this yourself

**No-code self-check.** (1) Your `SUM` misses the last row; what did you skip? (2) The pivot's Plus
revenue disagrees with your notebook; name two causes. (3) Which lookup pattern works in both Excel
and LibreOffice? Key: (1) making the data a Table; (2) cancelled orders included in one and not the
other, or amounts stored as text in the sheet; (3) `INDEX` and `MATCH`. A miss on (1) sends you to
Tables, on (2) to the pivot, on (3) to lookups.

**Hands-on, forty-five minutes.** Paste mini project 1's rows into a sheet, make them a Table, build
the pivot for revenue by tier, write the `SUMIFS` for Plus, and check the two agree with your
notebook. Put a screenshot of the pivot in the `w00-diagnostic-pandas` README beside the pandas
result.

## Glossary

| Term | Plain meaning | Where it appeared | Example |
|---|---|---|---|
| Table | A named range whose formulas and pivots grow with it | Tables section | Ctrl+T on the orders range |
| PivotTable | A drag-and-drop `GROUP BY` | Pivot section | tier in Rows, amount in Values |
| SUMIFS | A sum with one or more conditions | Formulas section | Plus revenue, paid only |
| INDEX and MATCH | A lookup by position found by value | Lookup section | City for a customer id |

## Go deeper, in this order

| Step | Resource | Time | Why this one |
|---|---|---|---|
| 1 | Microsoft Support, "Create a PivotTable to analyze worksheet data", [support.microsoft.com/office/18fb0032-b01a-4c99-9a5f-7ab09edde05a](https://support.microsoft.com/en-us/excel/get-started/create-a-pivottable-to-analyze-worksheet-data) (checked 30 September 2026) | 15 min, with the embedded video | The vendor's own steps, platform by platform |
| 2 | The hands-on above | 45 min | The pivot that agrees with your notebook |

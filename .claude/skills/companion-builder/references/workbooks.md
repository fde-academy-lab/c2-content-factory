# The two workbook forms

An Excel tool is the part of a day a learner still has in month three, when the notebook has been closed and the deck is a file in a folder. It is built to be applied to their own work, so it holds a framework rather than the day's data.

## Form one: the decision tool

Every teaching day gets one.

**One tab per taught decision**, each ending in a computed verdict cell. The verdict is a string a person can read aloud, not a number: `ship it`, `investigate before you clean`, `escalate to the order book owner`.

**An export tab** that assembles a paste-ready brief by formula from the other tabs. A learner fills the yellow cells, opens the export tab, and copies a paragraph that already reads as something they wrote.

**Yellow cells are inputs.** Everything else is computed and locked in appearance if not in fact. A learner should be able to tell input from output without reading a legend.

**One planted defect per tab**, which the learner finds first. The defect is a plausible wrong value, not a broken formula: a denominator that counts the wrong population, a threshold set where the day said not to set it, a rate quoted without its count.

**An interior optimum.** Fixing one thing must not clear the release. If correcting the denominator on tab one still leaves the verdict blocked because tab three's threshold is wrong, the learner has to work the whole tool rather than the first cell they notice.

## Form two: the live miniature

Built where the day also carries a repeatable procedure a learner should run again.

**A run sheet** listing the procedure's moves in order, with an observed column the learner fills and a computed status per row. The status compares what they observed against what the row expects and says pass, differs, or not run.

**A symptom lookup**: symptom, first check, fix, evidence to keep, and who owns the decision. Five columns, one row per symptom the day actually produced.

## Formulas that survive LibreOffice

The recalc gate runs through LibreOffice headless, so the workbook has to compute there.

**Allowed:** `IF`, `AND`, `OR`, `NOT`, `INDEX`, `MATCH`, `COUNTIF`, `COUNTIFS`, `SUMIF`, `SUMIFS`, `SUMPRODUCT`, `ROUND`, `ABS`, `MIN`, `MAX`, `LEN`, `TEXT`, `CONCATENATE`, `&`, `IFERROR`.

**Not allowed:** `XLOOKUP`, `IFS` without a fallback, `LET`, `LAMBDA`, `TEXTJOIN` with arrays, dynamic array spills, structured table references.

`INDEX` and `MATCH` do everything `XLOOKUP` does and load everywhere.

## The recalc manifest

A small file beside each workbook, named to the stem rule with the `INTERNAL` audience, telling `xlsx_recalc.py` what to prove:

```yaml
workbook: C2_W01_D03_decision_tool_STUDENT.xlsx
verdicts:
  - sheet: Missingness
    cell: D14
    expect: "keep and flag, and write the reason"
  - sheet: Duplicates
    cell: D12
    expect: "escalate to the order book owner"
  - sheet: Export
    cell: B2
    contains: "44 of 50 rows"
flips:
  - name: absence stops meaning something
    set: [{sheet: Missingness, cell: B7, value: "no"}]
    verdicts:
      - {sheet: Missingness, cell: D14, expect: "drop the field"}
  - name: the identity rule becomes order_id alone
    set: [{sheet: Duplicates, cell: B6, value: "order_id"}]
    verdicts:
      - {sheet: Duplicates, cell: D12, expect: "one duplicate pair, resolve before you ship"}
```

Two things the manifest proves that a human reading the file cannot. First, that the verdict cells actually compute rather than holding a cached string typed by the builder. Second, that the decisions genuinely drive the verdicts, because flipping an input moves the verdict to a different stated value.

A workbook whose verdict does not move under any flip is a spreadsheet with words in it.

## Sizing

Three to five tabs plus the export tab. Under three and the day's decisions did not need a tool; over five and the learner never opens the last two.

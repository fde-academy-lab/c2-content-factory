# Recalc manifest: the decisions log

Read by `scripts/xlsx_recalc.py`, which `scripts/verify.py` runs. It proves the Reconcile sheet counts
removed rows from the Log sheet and says whether input equals clean plus removed.

```yaml
workbook: C2_W03_D01_decisions_log_STUDENT.xlsx
verdicts:
  - {sheet: Reconcile, cell: B18, expect: "No file counted yet: profile before you touch"}
  - {sheet: Reconcile, cell: F5, expect: "not counted yet"}
  - {sheet: Reconcile, cell: B5, expect: "6700"}
flips:
  - name: five patient rows removed and the clean file reconciles
    set:
      - {sheet: Log, cell: C5, value: "patients"}
      - {sheet: Log, cell: D5, value: "patient_id"}
      - {sheet: Log, cell: F5, value: 5}
      - {sheet: Log, cell: H5, value: "removes rows"}
      - {sheet: Reconcile, cell: D5, value: 6695}
    verdicts:
      - {sheet: Reconcile, cell: F5, expect: "reconciles"}
      - {sheet: Reconcile, cell: B18, expect: "1 of 1 counted files reconcile"}
  - name: the clean file is five rows short of the log
    set:
      - {sheet: Log, cell: C5, value: "patients"}
      - {sheet: Log, cell: D5, value: "patient_id"}
      - {sheet: Log, cell: F5, value: 5}
      - {sheet: Log, cell: H5, value: "removes rows"}
      - {sheet: Reconcile, cell: D5, value: 6690}
    verdicts:
      - {sheet: Reconcile, cell: F5, contains: "short by 5 rows"}
      - {sheet: Reconcile, cell: B18, expect: "1 counted files do not reconcile: stop and find the rows"}
  - name: a kept row does not count as removed
    set:
      - {sheet: Log, cell: C5, value: "patients"}
      - {sheet: Log, cell: D5, value: "employer_account"}
      - {sheet: Log, cell: F5, value: 1}
      - {sheet: Log, cell: H5, value: "keeps rows"}
      - {sheet: Reconcile, cell: D5, value: 6700}
    verdicts:
      - {sheet: Reconcile, cell: C5, expect: "0"}
      - {sheet: Reconcile, cell: F5, expect: "reconciles"}
```

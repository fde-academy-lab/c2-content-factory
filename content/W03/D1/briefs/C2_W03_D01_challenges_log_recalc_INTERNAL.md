# Recalc manifest: the challenges log

Read by `scripts/xlsx_recalc.py`, which `scripts/verify.py` runs. It proves the Summary sheet computes
from the Log sheet and moves when a group logs an entry.

```yaml
workbook: C2_W03_D01_challenges_log_STUDENT.xlsx
verdicts:
  - {sheet: Summary, cell: B11, expect: "No entries yet: write entry one before the close"}
  - {sheet: Summary, cell: B4, expect: "0"}
flips:
  - name: entry one logged and still open
    set:
      - {sheet: Log, cell: E5, value: "We could not say what an at-home collection is in the files"}
      - {sheet: Log, cell: I5, value: "open"}
      - {sheet: Log, cell: K5, value: 20}
    verdicts:
      - {sheet: Summary, cell: B11, expect: "1 open of 1: take the oldest open one to the checkpoint"}
      - {sheet: Summary, cell: B8, expect: "20"}
      - {sheet: Log, cell: A5, expect: "1"}
  - name: entry one resolved
    set:
      - {sheet: Log, cell: E5, value: "We could not say what an at-home collection is in the files"}
      - {sheet: Log, cell: I5, value: "resolved"}
    verdicts:
      - {sheet: Summary, cell: B11, expect: "All 1 resolved: the log is ready for the viva"}
```

# Provenance: Week 2, Friday

INTERNAL.

## Numbers

| Figure | Value | Asserted |
|---|---|---|
| Rows in the clean customer table export | 300 | Yes, by `--contract` |
| Rows in the raw export | 1,450 | Yes |
| Rows per customer in the raw export | about 4.83 | Derived |
| Ratio of the raw total to the clean total | close to 2 | Checked in the notebook |
| The absent member id | C-0170 | Yes |

The clean export holds 300 rows rather than 301: one customer who ordered is removed on purpose so
the lookup has something to fail on. That is the plant, and the trainer sheet says not to name it.

## A real constraint the build exposed

`scripts/xlsx_recalc.py` recalculates through LibreOffice, and this environment runs LibreOffice
24.2.7.2. XLOOKUP arrived in LibreOffice 24.8, so it returns `#NAME?` under the gate.

Rather than dropping XLOOKUP, which the curriculum row names, the workbook carries both: an
XLOOKUP for the Excel reader the chief of staff actually has, and an `INDEX`/`MATCH` pair that
computes in any reader. Cell B24 reports which of the two the opening application managed, and
cell B25 explains why both are there.

The recalculation manifest asserts the `INDEX`/`MATCH` verdicts. This is recorded because a
reviewer could reasonably read the XLOOKUP cell failing under the gate as a defect, and it is not.

The version fact was verified on 13 September 2026 by running `libreoffice --version`.

## The workbook

Every result cell is a formula, so the gate's flips move real values rather than re-reading cached
strings. Three input cells form the decision surface: the quarter, the segment, and whether the
figure comes from the clean table or the raw export.

Two flips are asserted. Switching the source to "raw" moves the verdict from "safe to send" to
"do not send". Changing the looked-up id from the absent one to a present one moves the lookup
verdict.

`demos/C2_W02_D05_build_pack_TRAINER.py` is the builder, shipped so the workbook can be rebuilt
from a fresh export rather than edited by hand, which is the take-home's whole point.

## Links, all verified 13 September 2026

| Link | Used in |
|---|---|
| Microsoft Support, create a PivotTable (verified 13 Sep 2026) | pre-read, study notes |
| Microsoft Support, XLOOKUP function (verified 13 Sep 2026) | study notes |
| <https://www.youtube.com/watch?v=OAd_K9RCBHo> (verified 13 Sep 2026) | pre-read, study notes |

The video was confirmed live by title and channel through the oEmbed endpoint: "XLOOKUP Function
and Pivot Tables", Resagratia.

## Open, for the reviewer

The take-home asks learners to regenerate the data and rebuild. That changes their local warehouse
and therefore every number in their own earlier work for the week. It is deliberate, since a
deliverable that cannot survive a refresh is the thing the day is about, and it will surprise
somebody. A reviewer who wants the rebuild done against a copy instead should say so.

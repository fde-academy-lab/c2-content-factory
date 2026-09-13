# Trainer day sheet: Week 2, Friday. Excel for analysts

TRAINER ONLY.

## The shape of the day

| Block | Minutes | What has to happen |
|---|---|---|
| The chief of staff's three asks | 15 | The room says which Excel should own and which it must not |
| The customer table in Excel, and the pivot | 50 | Built on the clean table, then on the raw export |
| Lookups | 35 | XLOOKUP, the not-found path, the nearest-match trap |
| Presenting one number | 35 | Denominator, period, comparison, the sentence beside it |
| The operating rule | 35 | Written as a team note |
| Unguided | 50 | The three deliverables for Monday's deck |
| Kahoot, close, Build 1 preview | 20 | Seven questions and the bridge |

Total 240 minutes.

## Before the room opens

Have both CSVs open in separate windows and the workbook ready. Check that
`content/W02/D5/data/` holds both exports; if not, regenerate with
`python3 data/generate_client_zero.py --version v4 --out content/W02/D1/data --stem C2_W02_D01`.

## What is planted

**Never name any of this.**

| Planted | Found by | Value |
|---|---|---|
| A raw export that still repeats the double-paid orders | Building the pivot on it and reading the total | 1,450 rows against 300 customers |
| One member id absent from the clean table | Typing it into the lookup | C-0170 |

The absent member is not a data defect and it is worth saying so if asked: the table is built from
orders, and that member placed none in the two quarters.

## The two failures to let happen

**One, the pivot.** Build it on the raw export in front of the room, thirty seconds of clicking,
and read the total out. It is roughly double the warehouse figure.

Ask what the pivot did wrong. Wait for it. The answer is that it did nothing wrong, and a room
that arrives at that sentence has learned the lesson rather than a rule about spreadsheets.

Then rebuild on the clean table with identical clicks and let them see the total land.

**Two, the lookup.** Have somebody type `C-0170` into the lookup with approximate match switched
on. It returns a neighbouring member: a real name, a real spend, a real segment.

The room catches it only because they know the id is missing, and saying that out loud is the
point. In a real sheet nobody knows.

## A portability fact that will come up

The recalculation gate runs LibreOffice 24.2, which predates XLOOKUP, so it returns `#NAME?` there.
The workbook carries both an XLOOKUP and an `INDEX`/`MATCH` pair and a cell that reports which one
the reader managed to compute.

That is deliberate and it is worth thirty seconds: "nothing that needs Python" does not mean
"opens identically everywhere".

## The moment the day turns

Not the pivot. The operating rule.

By this point the room has met the same underlying discipline four times in five days: count
before you total, name the denominator, say what one row means. Ask what all four have in common
before giving them the three lines.

Then add the fourth line, the reproducibility condition, and ask what breaks it first in a real
team. The answer is a deadline and a correction that exists in only one place.

## Timing pressure

Cut the number-card styling first, per the row. Never cut the pivot double-count or the operating
rule.

## Close-out and the bridge

Release both solution files. Set the take-home and say plainly that part one is a rebuild, not a
re-read: somebody in the room will report no change from a sheet they did not actually rebuild.

Then the bridge, and give it a full minute. Build 1 opens Monday in Kalpa Health with the
Programme Head's online introduction. Unfamiliar unit, unfamiliar data, unfamiliar stakeholders.

The last thing on the board:

```
The method transfers. The domain does not.
```

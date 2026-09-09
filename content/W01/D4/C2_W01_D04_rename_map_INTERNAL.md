# Rename map: what changes when client zero locks

Internal working file. Never given to a learner.

## The state this pack was built in

The client-zero scenario is frame locked and no more. `docs/07_Client_Zero.md` carries status PROPOSED with an empty lock line, and the Structure tab records that the company name and entity model still need the formal lock.

Nothing in this pack invents a company, a domain, a product or an entity. The field names are the five field roles carried forward from the shipped Day 2 pack, and the segment values are visibly placeholders. Thursday's payload is descriptive statistics and dictionary accumulation, so it survives the placeholder exactly as Tuesday's did.

## What changes at the lock, and where

| Placeholder | Replace with | Files touched |
|---|---|---|
| `id` | The scenario's own identifier name | both data files, both notebooks, both deck halves, activity, exercises, solutions, take-home, self-check, study notes, cheat sheets, day sheet |
| `segment` | The scenario's own grouping field | same |
| `amount` | The scenario's own money field | same |
| `outcome` | The scenario's own status field | same |
| `date` | The scenario's own date field | same |
| `segment_a` to `segment_d` | The scenario's four real segment values | both data files, and every artifact that names a segment in prose |
| `accepted`, `declined`, `pending` | The scenario's real status values | both data files, and the rate definition wherever it is stated |

The client-zero file names four segments (Retail-Core, Retail-Plus, Business and Student) and states that the small twelve-record segment is Student. At the lock, `segment_d` becomes Student, and the three others map by size and story rather than by letter. That mapping is a judgement call for whoever runs the lock, and it should be recorded here rather than made twice.

## What does not change

Every count, total, median and rate in this pack is independent of the naming. Renaming a column does not move a number, so these stay correct through the rename and should be re-checked afterwards rather than recalculated.

| Value | Where it appears |
|---|---|
| 47 records, total Rs 846,000, mean Rs 18,000.00, median Rs 7,500 | both deck halves, notebook 1, activity, exercises, solutions, study notes, cheat sheet, pre-read, day sheet |
| Whale Rs 480,000; highest ordinary record Rs 17,400; mean without the whale Rs 7,956.52; median without it Rs 7,300 | deck half one, notebook 1, activity, study notes |
| Mode Rs 4,500 at three occurrences | deck half one, notebook 1, study notes |
| Q1 Rs 4,800, Q3 Rs 10,900, IQR Rs 6,100, upper fence Rs 20,050, one record above it | deck half one, notebook 1, study notes, cheat sheet |
| Segment counts 20, 9, 6, 12 summing to 47 | both deck halves, notebook 2, activity, exercises, solutions, study notes, day sheet, tiered extras, pre-read |
| Segment medians Rs 7,950, Rs 8,000, Rs 6,800, Rs 6,750 | deck half two, notebook 2, activity, solutions, study notes |
| Rates 45.0, 44.4, 50.0, 58.3 percent; `segment_b` mean Rs 60,255.56 against median Rs 8,000 | deck half two, notebook 2, activity, solutions, study notes |
| Take-home file: 39 records, 4 months, smallest bucket 4, overall median Rs 9,400, the 2026-07 mean Rs 35,463.64 against median Rs 9,600 | take-home, self-check |

One value moves under the rename and it is the exception to this table.

| Value | What happens |
|---|---|
| `KeyError: 'segment_d'` in notebook 2, deck half two, exercises, solutions, day sheet and study notes | The exception type and the mechanism survive. The quoted key becomes whichever real segment value replaces `segment_d`, and it must be the segment that is *absent* from the hard-coded list in notebook 2's failing cell. Edit that cell's three hard-coded keys and the printed key together, or the break stops reproducing. |

## How to do it

Rename the two data files first, then edit notebook 2's hard-coded key list to match, then run `python3 scripts/verify.py content/W01/D4`, then execute both notebooks cold and confirm every number in the table above is unchanged.

A rename that moves a number means a value was hard-coded where it should have been computed, and the cold run will show it.

The activity HTML carries its own copy of the 47 records inside a `const DATA` array. It must be renamed alongside the CSV or the two will disagree silently, since nothing cross-checks them at build time. The build session verified them equal as multisets; repeat that check after the rename.

The decks, the exercises, the solutions and the study notes carry field names as prose and need reading rather than a blind find and replace.

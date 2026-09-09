# Rename map: what changes when client zero locks

Internal working file. Never given to a learner.

## The state this pack was built in

The client-zero scenario is frame locked and no more. The Structure tab records that the company name and entity model still need the formal lock, and the Week 1 Day 1 row says entity and field names slot in once the scenario locks.

Nothing in this pack invents a company, a domain, a product or an entity. The field names are the five field roles the Day 1 row states in its own words, and the segment values are visibly placeholders. That is why this day could be built while Day 1 could not: Day 1's core artifact is the company told as a story, and Tuesday's payload is functions, tracebacks and file input and output.

## What changes at the lock, and where

| Placeholder | Replace with | Files touched |
|---|---|---|
| `id` | The scenario's own identifier name | the four data files, both notebooks, the deck halves, exercises, solutions, take-home, self-check |
| `segment` | The scenario's own grouping field | same |
| `amount` | The scenario's own money field | same |
| `outcome` | The scenario's own status field | same |
| `date` | The scenario's own date field | same |
| `segment_a` to `segment_d` | The scenario's real segment values | the four data files only |
| `accepted`, `declined`, `pending` | The scenario's real status values | the four data files only |
| `feed_01` | The scenario's real upstream system name | the two JSON files |

## What does not change

Every count, total and error string in this pack is independent of the naming. Renaming a column does not move a number, so these stay correct through the rename and should be re-checked afterwards rather than recalculated:

| Value | Where it appears |
|---|---|
| 30 records in, 28 clean, 2 rejected, total 230380 | deck half one, deck half two, both notebooks, activity, solutions, study notes, day sheet, tiered extras |
| 24 in, 21 clean, 3 rejected, total 181950 | solutions holds all four; tiered extras holds 24, 21 and 3 without the total; the exercises name the lab file and withhold the counts on purpose |
| 30 in, and either 27 clean at 219050 or 26 clean at 223550 | take-home self-check |

One value does move under the rename, and it is the exception to this table.

| Value | What happens |
|---|---|
| `line 48 column 1 (char 841)`. The full string with the offset is in the exercises and the day sheet, and notebook 2 produces it at runtime. The solutions and the study notes name line 48 without the offset. | The line and column survive, since the truncated file's shape is unchanged. The character offset 841 counts bytes, so it shifts as soon as a field name changes length. Re-run the truncated load after renaming and paste the real offset back into the exercises and the day sheet. The files that name only the line need no edit. |

## How to do it

Rename in the four data files first, then run `python3 scripts/verify.py content/W01/D2`, then re-run both notebooks cold and confirm every number above is unchanged. A rename that moves a number means a value was hard-coded where it should have been computed, and the notebook run will show it.

The two decks, the exercises and the solutions carry the field names as prose and need reading rather than a blind find and replace.

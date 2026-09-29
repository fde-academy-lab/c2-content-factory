# Provenance: Week 3 Wednesday, Build 1, build days two and three

**INTERNAL.** Where every part of this pack came from, what it departs from, and what was invented.
Built on 29 September 2026.

---

## Sources, in the order they were read

| Source | What it gave the pack |
|---|---|
| `CLAUDE.md` | The build workflow, the hard rules, the folder and naming rules |
| `docs/detailing/W03_build1_spine.md` (approved 29 September 2026) | The day's shape (checkpoint 30, parallel build 60, build time, close 20), the five sub-problems by number and name, the plant table and its witness numbers |
| `docs/curriculum/W3_Build_1.md`, Monday's row and Wednesday's row | The scenario, the thinking trained, the trainer agenda, the learner outcome, the trainer notes, the after-class task and the interview angle ([F] and [D]) |
| `docs/programme/calendar.md`, line W03/D3 | Wed 21 Oct, build week, Module 1, no faculty block |
| `data/programme/facts.yaml` (as of 29 September 2026) | The campus day (two 180-minute blocks, then the TA time), the cohort (35 learners, nine groups, stated), the locked per-event marks (40, 30, 30), the `groups` conflict, the `build1-rubrics` decision (closed) |
| `docs/07_Client_Zero.md`, sections 1a and 1b and the Build 1 seeds | Dr Priya Menon as the one named Kalpa Health stakeholder, the GCC frame, Kavya Nair's review beat |
| `data/generate_kalpa_health.py`, its docstring and `--witness` | The ten files, what each system exports, the witness numbers |
| The ten files in `content/W03/D1/data/` | Every number in the pack, recomputed by `internal/C2_W03_D03_numbers_INTERNAL.py` |
| `.claude/skills/day-pack-builder/SKILL.md`, the manifest's build-week section, `references/the-standard.md` | The build-week folders, the day sheet's parts, the notebook's form |
| `content/W01/D3` and `content/W01/D4` | The decisions log shape (Field, Issue, Rows, Decision, Reason, with a kept row) and the note shape (claim, evidence, caveat, action) |

No link enters any file in this pack, so there is nothing to date.

---

## The data command, and how the pack reads the files

The data pack is Monday's, written by `python3 data/generate_kalpa_health.py --out content/W03/D1/data
--stem C2_W03_D01`. This day copies nothing. The notebook reads `../../D1/data/` from
`parallel-build/`, and the numbers script reads the same folder from the repository root.

Rebuild the notebook with `python3 content/W03/D3/internal/C2_W03_D03_build_parallel_build_INTERNAL.py`.
Recompute every quoted number with `python3 content/W03/D3/internal/C2_W03_D03_numbers_INTERNAL.py`,
which ends on PASS and asserts the spine's witness where the pack quotes it.

---

## The plants, and where each is used

| Plant | Where it appears | Audience |
|---|---|---|
| The headline (5.1, 7.8, 8.6 and 5.6 percent) | Day sheet, circulating section | TRAINER |
| 1. The corporate contract, packages as one line | Checkpoint guide, catch-up plan, run sheet (as what the slice avoids) | TRAINER |
| 2. The system switch, the repeated rows | Checkpoint guide, run sheet. The notebook shows Delhi's 33 repeated ids and handles them with an identity rule, never naming a cause. | TRAINER; the Delhi count only in the STUDENT notebook |
| 3. The reference formats, double posts, refunds, unpaid invoices | Checkpoint guide, day sheet interview answer | TRAINER |
| 4. The small clinic | Checkpoint guide | TRAINER |
| 5. The campaign reversal and pre-trend | Checkpoint guide, run sheet (as what the slice avoids) | TRAINER |

The STUDENT files are the checkpoint questions, the headline sheet and the notebook. They name no
plant and quote only Dr Menon's own figures (5 percent against 18, the 9 percent) and the Delhi
slice's numbers.

---

## Where the pack departs from the spine, the row or the brief, and why

| Departure | Reason |
|---|---|
| The parallel build splits Delhi by clinic, never by channel | The campaign file offers the free collection to 316 Delhi patients, and home-collection invoices in Delhi rise from 97 to 160 at a lower mean. A channel split would point at sub-problem 5. |
| The spine says the offer ran in three cities; the campaign file carries offers in all six | That is what the files hold (Delhi 316, Chennai 215, Pune 208). In Delhi, offered patients book 23.5 percent more than the rest. The checkpoint guide and day sheet tell the trainer how to handle a group that finds it. The orchestrating session should decide whether the spine or the generator changes. |
| The witness's `text_amounts: 60` against 35 comma-written amounts in the file | 60 amounts were written as text, but 25 of them are under Rs 1,000 and print with no comma, so a learner sees 35. The pack quotes 35 and 4 (Delhi). |
| The spine's "48,235 tests performed behind 22,152 invoice lines" | 48,235 counts tests on every non-corporate booking, cancelled ones included. On completed bookings, which are the ones invoiced, it is 46,867. The checkpoint guide gives both. |
| The rubrics were drafted and awaiting approval when the brief was written; the requester approved them on 29 September 2026 (main, #151) | The day sheet and the headline sheet carry the mini project's rubric through `sync:rubric:W03/mini-project`, and the day sheet names the mock and GD days, which facts.yaml now allows for Build 1. |
| The pack carries no deck | The brief's artifact table names none. The close uses the presentation format from the Saturday pack. |

---

## What was invented

| Invented | Where |
|---|---|
| The wording of Kavya Nair's review lines | The notebook, the headline sheet |
| The six tests a claim passes before it is pinned | The headline sheet, built on the Week 1 Thursday note and the week's own checks |
| The one nudge per checkpoint question, and the claim-type responses at the close | Checkpoint guide, day sheet |
| The smallest honest claim templates | Catch-up plan |

Dr Menon's quoted words are the row's ("test volumes grew 5 percent against a plan of 18"), and her
data team's two facts are the ones the brief allows.

---

## Tool versions the outputs came from

Python 3.11.15, pandas 3.0.6, numpy 2.4.6, nbclient 0.11.0, nbconvert 7.17.1. The notebook uses only
`read_csv`, boolean filters, `groupby`, `merge` with `validate` and `indicator`, and
`drop_duplicates`. It was also executed under pandas 2.3.3 on 29 September 2026, with the same
17 checks passing.

# Week 1 Saturday: provenance

INTERNAL. Where every part of the Week 1 Saturday pack came from, which items are waiting for the
tracker, and the decisions taken while building it. Checked on 29 September 2026.

## Sources

| Source | What it gave the pack | Checked |
|---|---|---|
| `docs/detailing/W01_W02_spine.md`, "The Saturdays" | The 300-minute shape (paper 120, break 20, marking 20, discussion 90, mock-interview round 30, doubts and the bridge 20), the rule that the bank is the floor and that Week 1 adds about 13 minutes of new timed items | 29 Sep 2026 |
| `docs/detailing/W01_W02_spine.md`, the Week 1 table | The week's traps the new items are built on: rows counted as customers, an average of segment averages, a whole-record dedupe, counts that reconcile while rupees do not | 29 Sep 2026 |
| `docs/curriculum/W1_Data_analysis_found.md`, the Saturday row | The ten interview anchors, the paper's format and status (ungraded, AI-free), the bridge into Week 2 | 29 Sep 2026 |
| `docs/curriculum/W1_Data_analysis_found.md`, the Monday to Friday rows | The daily interview angles each new item's anchor is taken from, and the client-zero plants the STUDENT paper must not name | 29 Sep 2026 |
| `docs/curriculum/source.xlsx`, Saturday papers tab, paper W1 | The 52 bank items, their keys, levels, tags, roles, days, minutes and anchors (107 minutes at the blueprint's pace) | 29 Sep 2026 |
| `data/programme/paper_edits.yaml` | The option rewordings already laid on the bank; none added by this pack | 29 Sep 2026 |
| `data/programme/facts.yaml`, `saturday_papers.paper_minutes` | The paper's 120 minutes | 29 Sep 2026 |
| `.claude/skills/exercise-builder/SKILL.md` and `references/distractor-discipline.md` | The blueprint's pace per item type, the level and tag rules, and the distractor discipline | 29 Sep 2026 |
| `scripts/build_saturday_paper.py`, docstring | The source file's four sections and block-style format | 29 Sep 2026 |
| `.claude/skills/day-pack-builder/references/artifact-manifest.md`, the Saturday paragraph | The Saturday folders and what each of the three files carries | 29 Sep 2026 |
| `content/W01/D4/trainer/C2_W01_D04_day_sheet_TRAINER.md` | The Thursday numbers the discussion guide's anchors 8 and 10 cite (the exposure mix, the Retail-Plus and Retail-Core falls, 0 of 5,000 shuffles) | 29 Sep 2026 |

No external link enters this pack. The row's two trainer resources stay in the row and were not
re-verified here.

## The new items, waiting for the tracker

All five sit in the scenario section after the bank's three sets, at 2.5 minutes each, which is
12.5 minutes and takes the paper from 107 to 119.5 minutes by the blueprint's pace.

| Q | Set | Level | Tag | Day | Key | The trap it stages | Anchor |
|---|---|---|---|---|---|---|---|
| Q46 | 4 | Easy | [S] | Mon | 2.00 (or 2) | Rows counted as customers, so orders per customer reads 1.00 | Marketing wants budget for acquisition; what would you check before agreeing it is the right branch? |
| Q47 | 4 | Medium | [S] | Tue | 4,000 (Rs 4,000) | An average of segment averages, Rs 7,000 | Why is a rate without a denominator meaningless? |
| Q48 | 4 | Hard | [D] | Tue | c | Marketing's "nobody comes back" read off the broken slide | Marketing insists the answer is acquisition and your data says frequency; how do you make the case in the room? |
| Q49 | 5 | Medium | [F] | Wed | d | A whole-record dedupe reporting zero duplicates | How do you find duplicates, and what makes two records the same? |
| Q50 | 5 | Hard | [D] | Wed | b | Counts that reconcile while Rs 3.0 lakh does not | Finance and your dashboard disagree; what do you do? |

Accept one by adding it to the tracker's Saturday papers tab, paper W1, and deleting it from the
source file. Until then the key lists them under "New items waiting for the tracker".

## Decisions

1. **Two new scenario sets and five items, 12.5 minutes.** The blueprint prices a scenario item at
   2.5 minutes, so five items land the paper at 119.5 minutes against 120, the same margin Week 2
   carries. A sixth item would run to 122.
2. **The new sets cover the traps the bank does not.** The bank already stages unequal windows (Q21),
   p = 0.03 misread (Q9, Q26, Q35) and the aggregate trusted while every segment fell (Set 3). Set 4
   takes Monday and Tuesday's rows counted as customers and average of averages; Set 5 takes
   Wednesday's whole-record dedupe and counts that reconcile while rupees do not.
3. **The new sets use their own numbers, not client zero's.** Set 4 is an April export of 500 rows
   and Set 5 a store-channel Q1 export of 1,200 rows, so no stem carries a planted figure from v0 to
   v3 and nothing a learner reads names a plant.
4. **Key positions.** The three new option items key on c, d and b, which keeps the paper's
   positions spread across a, b, c and d.
5. **Exhibits.** Sets 1, 2, 3 and 4 carry a small table and Set 5 a Mermaid flow, each drawn only
   from its situation's numbers. Set 2's exhibit was first drawn as a Mermaid flow and rendered a
   full page tall in the Word paper, so it became a table; no exhibit prints a number an item asks
   for.
6. **Notes on every bank item.** The fill-in, true-or-false, applied maths and ordering items carry
   their commonest wrong answers as the keys of `wrong`, so the key file prints each wrong answer in
   brackets beside the misconception behind it.
7. **The stretch page.** Four written follow-ups: acquisition's cost case, p = 0.03 for the board,
   the auditor's walk through removed rows, and the two-hour export. Stretch 2 names no segment, so
   it gives away no Thursday finding.
8. **The discussion guide.** Rewritten for the 300-minute Saturday. The most-missed list gains the
   five new items; the anchors keep their answers and their item lists move to the printed numbers
   (bank items 46 to 52 now print as Q51 to Q57); the mock-interview round assigns anchor pairs by
   counting round the room, so every anchor is asked and no pair picks its favourites.
9. **The Word files were rendered with a session shim for mermaid-cli.** The installed mermaid-cli
   12.0.0 has no `-w` option, which `scripts/build_cheatsheet.py` passes when rendering a PNG, so
   every Mermaid exhibit silently drops from the Word paper. This build ran with a shim outside the
   repository that maps `-w` to `-s 2`. The fix belongs in the builder, and the orchestrating session
   has it as a change request.

# Provenance: Week 0, Tuesday

INTERNAL.

## What the pack was built from

The Tuesday row of `docs/curriculum/W0_Baseline_week.md` (tracker v7, 21 September 2026) for the
content: four papers by topic and their subtopics, keys marked the same evening by the Academic TA
and the Support TA, the scores setting Wednesday's two tracks and feeding the baseline card, the
rule that nothing a learner sees carries a cut-off, a level label or another learner's score, and
the four interview questions. The student Week 0 sheet, `docs/journey/Week_0.md` (version 2, 27
September 2026), for the running order: one paper of about two hours on paper with no assistant,
then a ten-minute briefing for Wednesday's introductions. The spine was approved in session on 28
September 2026 with two decisions from the requester: follow the student sheet's two hours, and drop
the college project one-pager while keeping the track rule.

## Checked on 28 September 2026

| Source | What it settled |
|---|---|
| Python 3.11.15, run in session | The output of items 1 to 8, the two error lines in items 9 and 10, which fixes print the asked value, and every wrong answer the key names for items 9 to 11 |
| PostgreSQL 16.13, run in session on the eight-row `issues` table | The rows for items 12 to 15, the reference queries for items 16 to 18, the empty result for `'maths'` and the two error lines the key names |
| GitHub Docs, creating diagrams, https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams (checked 28 September 2026) | Mermaid fences render in GitHub markdown; the page names no Mermaid version |
| GitHub's Mermaid renderer, the bundle `mermaidMarkdown-035ded29910819bc6e5e.js` served by viewscreen.githubusercontent.com (checked 28 September 2026) | It registers the xychart diagram with a detector that accepts `xychart-beta`, so item 22's bar chart renders on GitHub |
| mermaid-cli 11.17.0 through the shared theme | Item 22 draws a tick for every cup from 95 to 106, with the two bars at 100 and 105 |
| `scripts/xlsx_recalc.py` through LibreOffice | The workbook computes, and the track follows the share, the attendance and the ticks |

## Conflicts, and what the pack did

- **The length of the paper.** The tracker runs four papers of 60, 45, 30 and 30 minutes and a
  40-minute project one-pager; the student sheet promises about two hours. The pack runs the four
  papers in 45, 30, 20 and 25 minutes and drops the one-pager, as agreed in session.
- **The one-pager's thinking.** The row asks for "my part" and "what broke" because project answers
  fall apart there. Both now sit in the briefing and the pre-read for Wednesday's introductions,
  which the student sheet gives the same shape.
- **The make-up.** The tracker puts it in Wednesday's practice lab, and the student sheet names lab
  time on Wednesday or Thursday for the one-to-ones. The pack runs the make-up in Wednesday's lab
  time.

## Changed outside the pack

`data/programme/facts.yaml` listed the Week 0 papers and the baseline card among the papers still to
build. The entry now names only the papers that remain, and the sync re-rendered what reads it.

## Own constructions

Every item and its key, built from the row's subtopics; the tick counts per paper; the six question
categories and the three-part hypothesis test, which the key labels as the programme's own; the
track rule, approved in session; the marking split, the calibration on three papers, and the
default track for a learner who missed the paper; and the baseline card's layout.

## Not verified, and left for the team

- Who invigilates: the row names the markers and no one else, so the day sheet gives the
  invigilation steps without naming a role.
- How much of the second half the institute's first half leaves: the student sheet shows half-day
  blocks and says the institute publishes the exact slots.
- Printing: the chart renders on GitHub's page, and a print from that page was not tested in
  session, so the day sheet asks for a check on the print preview.

# Provenance: Week 3 Friday, Build 1, expert day one

**INTERNAL.** Where every part of this pack came from, the numbers it quotes and their sources, what
it departs from, and what was invented. The pack was built on 29 September 2026 and reached main that
day with pull request #161. Its day sheet changed twice more with #177, in commit 1a879ee on 29
September 2026 and in the merge commit 59f336b on 30 September 2026, and commit f335887, of 30
September 2026, seated the cohort as 35 in the day sheet and in a rebuilt GD scoring sheet. This
record was written on 30 September 2026 from the repository alone: the day's files, the spine,
`data/programme/facts.yaml`, the generator and its witness, and `git log` on each file, with
`--follow` and across merges. Where the repository does not say something, this record says so.

---

## Sources

| Source | What it gave the pack |
|---|---|
| `CLAUDE.md` | The build workflow, the hard rules, the folder and naming rules |
| `docs/detailing/W03_build1_spine.md` (approved 29 September 2026) | Friday's line: expert day one, GD rounds at about 30 minutes per group on prompts that climb in complexity, a thread separate from the projects, the build freeze, two cold demo runs and the first presentations, with the GD prompts, facilitation notes and the demo rehearsal checklist as the pack; the plant table the expert's brief copies; the rule for a demo that fails; the rubrics block; the Saturday slot of 25 to 30 minutes |
| `docs/curriculum/W3_Build_1.md`, Friday's row and Monday's row | The scenario; the thinking trained (structured articulation under time pressure, unprepared by design); the agenda (the expert's rounds on a rolling roster, groups rehearsing the demo cold in parallel, a first tranche where the roster allows, Saturday's order drawn in 10 minutes); the trainer notes (fifteen groups at 30 minutes is about 7.5 hours of GD across both expert days, the Principal Advisor takes a share of the rounds online, the builds freeze tonight); GD topics at progressive complexity as a separate thread; two cold demo runs, logged; the `[F]` interview angle; Monday's structure note (groups of four, the expert on Friday and Saturday only) |
| `docs/programme/calendar.md`, line W03/D5 | Fri 23 Oct, build week, Module 1, no faculty block, rendered into the day sheet through `sync:module:W03/D5` and `sync:day-date:W03/D5` |
| `data/programme/facts.yaml` (as of 30 September 2026) | The campus day (two blocks of 180 minutes); the cohort (35 learners and nine groups, both stated; groups of four, locked); the marks per event (mini project 40, mock 30, GD 30, locked); the GD and mini project rubrics in `evaluation.rubrics.W03`, settled on 29 September 2026 and rendered through `sync:rubric:W03/gd` and `sync:rubric:W03/mini-project`; the GD's days; the `groups` conflict; the GCC addendum with Kavya Nair's review as a recurring beat |
| `docs/07_Client_Zero.md`, section 1a | Dr Priya Menon as Kalpa Health's COO, whose asks open every card |
| `data/generate_kalpa_health.py`, its `--witness`, and the ten files in `content/W03/D1/data/` | The expert's plant table, and every number a GD card attributes to Kalpa Health's files |
| Files of other days that the pack names | Monday's challenges log and decisions log (the checklist's deliverables) and Saturday's presentation format (the first tranche and the checklist) |

### The one link

| Link | Where | Checked |
|---|---|---|
| GitHub Docs, "Creating a codespace for a repository": https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository | The cold-demo checklist's step on opening a new Codespace | The checklist carries verified 29 September 2026. Checked again for this record on 30 September 2026: it returns 200 with the title "Creating a codespace for a repository - GitHub Docs", and the page still carries the "Create a codespace on BRANCH" wording the step quotes. |

---

## The data command, and how the numbers were rechecked

The pack copies no data. The expert's brief says its plant numbers are the generator's witness, run
on 29 September 2026, and the GD prompts file says every card number taken from Kalpa Health's files
was computed from `content/W03/D1/data/` that day. That folder is written by
`python3 data/generate_kalpa_health.py --out content/W03/D1/data --stem C2_W03_D01`. On 30 September
2026 that command, pointed at a scratch folder, wrote ten files that are byte-identical to the
committed ones; `--contract` printed PASS; `--witness` printed every figure in the plant table; and
the two kept witness scripts, `content/W03/D1/internal/C2_W03_D01_witness_check_INTERNAL.py` and
`content/W03/SAT/internal/C2_W03_SAT_witness_INTERNAL.py`, both ended on PASS against the spine. The
ten SHA-256 checksums in the cold-run script match the committed files. The card figures were counted
from the CSV files in this session with a scratch script that is not kept.

---

## The numbers each file quotes, and where each comes from

### The day sheet, TRAINER only

| The figure | Where it comes from |
|---|---|
| The plant table: 5.1, 7.8, 8.6 and 5.6 percent; Rs 18,00,000 and 16.2 percent; Rs 1,904, Rs 1,596 and Rs 1,499; 22,152 invoice lines, 46,867 tests on completed bookings and 48,235 counting cancelled ones; 23.0 and 12.2 percent; 180 repeated rows; 2.2 percent; 229 double posts, 102 refunds and 398 unpaid invoices; 19.2 against 8.7 and 20.0 against 15.2 percent, with a probability of 0.22; 9.0 percent overall and 10.8, 19.9 and 13.0 percent less in the campaign cities; within about 6 percent before the offer; 6.9 percent before it; Delhi's 23.5 percent | The spine's plant table as corrected in #169 and #177; the generator's witness and the Saturday witness print each, the witness giving Delhi's gap as 0.2349 under `campaign_lift_other_cities` |
| Block one as 15 minutes of opening, five rounds of 30 and 15 minutes of write-up | The roster: the row's 30-minute round and the pack's opening of 15 |
| Block two as 90 minutes of tranche (three presentations of 30), 20 of notes, 27 of roll call (three minutes for each of nine groups), 10 of draw and 33 of slack | The roster's "Friday block two" sheet, whose verdict reads "block two fits with 33 minutes of slack"; the row gives the 10-minute draw |
| 450 minutes of GD for fifteen groups | 15 times 30, the row's "about 7.5 hours" |
| Up to twelve groups with stream B running rounds 3 to 5, up to sixteen with up to three Saturday rounds a stream, a third chair past sixteen | The roster's Check sheet: five rounds a stream fit in Friday block one after the opening, and at most three a stream on Saturday morning |
| The marks per event and the two rubrics | `data/programme/facts.yaml`, through the sync blocks |
| The interview answer's 9 percent claim and its 7.6 percent break-even | Card 05's claim and its arithmetic, below; 9 percent overstated by a fifth is 7.2 percent, under the break-even |

### The GD cards, STUDENT, and the GD prompts, TRAINER

The cards take five kinds of figure from Kalpa Health's files, and a count on 30 September 2026
matched each one.

| On the card | How the prompts file says it was computed | The count on 30 September 2026 |
|---|---|---|
| List prices: Full body Rs 2,999, Diabetes care Rs 1,499, Senior citizen Rs 3,499, Corporate health check Rs 1,500, CBC Rs 350, Lipid Rs 600, HbA1c Rs 450, Vitamin D Rs 1,200 | The test catalogue's `list_price` | The same eight prices |
| 1,685 Full body checkups booked, April to September | Booking-tests rows with `line` package and `package_code` PKG-FB | 1,685 |
| 6,700 patients, 1,699 of them aged 60 and over (25.4 percent) | The patients file, its rows and `age_band` 60+ | 6,700 and 1,699 |
| Patients by city: Delhi 1,500, Bengaluru 1,250, Mumbai 1,200, Chennai 1,000, Pune 950, Hyderabad 800 | The patients file by `city` | The same six counts |
| Channel mix: walk-in 45, app 27, phone 15, home collection 13 percent | Both booking exports, the old one de-duplicated on `booking_id`, the new system's codes mapped, the one corporate booking left out, shares over the rows with a channel | 45.1, 26.9, 15.4 and 12.6 percent of 11,525 bookings; 176 rows carry no channel |

Every other figure on a card is marked on the card as the prompt's own assumption or as one
stakeholder's figure: 23,000 bookings a year, Rs 1,500 a booking, every cost, share, survey and
estimate, and the 9 percent the marketing head reports on card 05, which is the claim Monday's briefs
give sub-problem 5. The prompts file's arithmetic for all ten cards was rechecked on 30 September
2026 and holds. One figure sits on a rounding edge: card 05 breaks even at 1,759.5 extra bookings,
which is 7.65 percent of 23,000, and the files print it as 1,760 and 7.6 percent. The facilitation
notes round the same figures once more (Rs 1.5 lakh, Rs 8.6 lakh, Rs 10.6 lakh, near 42 and 33
percent).

### The cold-demo checklist and the cold-run script, STUDENT

| The figure | Where it comes from |
|---|---|
| A presentation slot of 25 to 30 minutes | The spine's Saturday line |
| About five minutes as the longest a cold run should take, and ten minutes of cost before a challenges log entry | The pack's own thresholds |
| Ten raw files and their SHA-256 checksums | The script's table, written on 29 September 2026; all ten match the committed files on 30 September 2026 |

### The roster and the scoring sheet

| The figure | Where it comes from |
|---|---|
| A round of 30 minutes | The row |
| An opening of 15 minutes, nine rounds (seven on Friday and two on Saturday morning), and at most three Saturday rounds a stream | The pack's own settings on the Inputs sheet, each with its reason beside it |
| Blocks of 180 minutes and nine groups | `data/programme/facts.yaml`, campus_day and cohort (stated) |
| 270 minutes of GD this build | Nine groups times 30, asserted by the recalc manifest |
| The sub-problem of each group on Inputs (G1 and G2 on 1, G3 and G4 on 2, G5 and G6 on 3, G7 and G8 on 4, G9 on 5) | An example, as the Read me says, "so the checks have something to check"; Monday's allocation replaces it |
| Four criteria with maximums of 8, 8, 8 and 6, adding to 30, over 35 seats | `evaluation.rubrics.W03` for the criteria; the cohort's 35 learners in nine groups, eight of four and G9 of three, from `data/programme/facts.yaml`, as Thursday's roster and Saturday's workbooks seat them |

The roster has no build script in the repository. Its metadata says openpyxl created it on 29
September 2026 and LibreOffice 24.2.7.2 saved it last, which is the recalculation
`scripts/xlsx_recalc.py` runs. Since commit f335887 the scoring sheet and its recalc manifest are
written by `internal/C2_W03_D05_build_gd_scoring_INTERNAL.py`, which reads the GD rubric and the
cohort from `data/programme/facts.yaml`.

---

## The plants, and where each is used

| Plant | Where it appears | Audience |
|---|---|---|
| The headline and all five sub-problems | The expert's brief in the day sheet, each with the question that tests whether a group found it | TRAINER |
| 5. The campaign | Card 05 quotes the marketing head's 9 percent and has the finance head ask for the cities that did not get the offer; it says nothing of what the files show, the facilitation notes tell the chair to say nothing either, and the roster keeps the card from sub-problem 5's groups | The card is STUDENT; the rest TRAINER |
| 4. The small clinic | Card 06's league table is invented and labelled so. The notes tell the chair to note, and leave unanswered, a question about whether every clinic counts a visit the same way, and the roster keeps the card from sub-problem 4's groups. | The card is STUDENT; the rest TRAINER |
| 1 and 3. The contract and the unpaid invoice | Card 07 prices a different, invented contract (2,000 checks, a client's Rs 1,100 against the list's Rs 1,500, payment at 90 days); the roster keeps it from sub-problem 1's and 3's groups | The card is STUDENT; the rest TRAINER |

The STUDENT files are the ten cards, the checklist and the cold-run script. On 30 September 2026 a
search of them for the plant words (the contract, the switch and the new system, walk-ins, retries and
double posts, the reference formats, the small clinic, the offer and its cities, the comma amounts)
found them only where a file uses them for its own purpose: the six cities in the exhibits of cards
03 and 08, the channel names on card 04, card 05's claim, card 07's own contract and the insurer's
offer on card 09, and in the checklist and the script a random sample, the comma in a slide number
and the campaign file's name among the checksums. None names a plant, and the data pack figures on
the cards are the five kinds above and nothing else.

---

## Decisions, and where the pack departs from the spine or the row

| Decision or departure | What the repository records |
|---|---|
| A second GD stream online | The Principal Advisor chairs stream B online, hosted by the Academic TA in a second room; the row gives the Principal Advisor a share of the rounds online, and without the second stream nine rounds take 270 minutes of the expert's Friday. #161 listed this among its departures to review. |
| Difficulty climbs with the slot | The card each slot carries is fixed on the roster, so the lot drawn at the opening decides who meets the harder cards (#161's departures). |
| No group meets its own sub-problem | Cards 05, 06 and 07 overlap sub-problems 5, 4, and 1 and 3; the roster's Check sheet flags a clash, and the fix is the other card of the level or card 08 (#161's departures). |
| A first tranche of three presentations in whole sub-problem clusters | The row says "where the roster allows"; the pack fixes three, drawn by cluster (#161's departures). |
| Checksums hard-coded in the cold-run script | They are the data pack's as of 29 September 2026, and `--reference` covers a re-issued pack (#161's departures). They still match on 30 September 2026. |
| Nine groups where the tracker plans fifteen | facts.yaml's stated nine; the day sheet names the conflict and the roster names the stretch. |
| 35 seats, as on Thursday and Saturday | The GD scoring sheet seated nine groups of four, 36 seats, and the day sheet called the plan nine groups of four from 35 learners, one seat more than the cohort. Commit f335887 (30 September 2026) made both agree with Thursday's roster and Saturday's workbooks: nine groups, eight of four and G9 of three, 35 seats. It rebuilt the scoring sheet from a new builder, with the summary's ranges and the recalc manifest's verdicts following the 35 seats, a Read me line on the seating, and blue text in the input cells, as the sheet's Read me already said. |
| The demo that fails in the room | The day sheet gives two minutes to recover, then the executed run, which is the spine's rule, set on 29 September 2026 by the orchestrating session on the requester's delegation and added to the spine with #169. On the Saturday branch, commit 045a746 changed this sheet to one run with no recovery and commit 1af434b restored it, and #164's merge message records that Friday's sheet went back to main's version. |
| The plant row brought in line with the spine | Commit 1a879ee (#177) gave the like-for-like test count and the offer outside the three campaign cities, and the merge commit 59f336b (#177) stopped the row calling the campaign cities' shortfall a drift. |
| The rubrics | Commit 813308d built the GD scoring sheet once the rubric locked (#151) and put the GD and mini project rubrics in sync blocks. |

---

## What was invented

| Invented | Where |
|---|---|
| Every figure marked as the prompt's assumption or a stakeholder's, the stakeholders' lines, and the league table of clinics A to F | The ten cards |
| The ladder of five levels, the overlap rule, and each card's tension, arithmetic and positions | The GD prompts |
| The opening instruction, each card's added line, the structure moves, the intervention lines, the panel's two questions per card, and the strongest and weakest discussions | The facilitation notes |
| The opening words, the freeze rule's wording and its four checks, the freeze table, the draw's steps, the table of what goes wrong and the interview answer in a trainee's voice | The day sheet |
| The table of what usually breaks a cold run, and the two thresholds above | The checklist |
| The example allocation on the roster's Inputs sheet | The roster |

Dr Menon's asks on the cards are the pack's wording; her figures elsewhere in the pack, 5 percent
against a plan of 18, are the row's and the spine's.

---

## What this record could not establish

- The session that built the pack kept no provenance, no numbers script and no workbook builder
  (the scoring sheet's builder dates from commit f335887), and its commit messages name no tool
  versions. #161's description shows `scripts/verify.py content/W03/D5
  --execute` passing on 29 September 2026; the versions behind that run are unknown.
- #161 lists five departures "to review"; the repository records their merge and no separate review
  of them.
- #161 says the cold-run script was tested on a clean run, a missing slide number, a crashing
  notebook, and an edited and a missing raw file. This record did not rerun those tests; it checked
  only the script's checksums against the committed files.

## Tool versions

The build's own versions are not recorded, apart from LibreOffice 24.2.7.2, which the roster's
metadata names. The scoring sheet was rebuilt on 30 September 2026 with openpyxl 3.1.5 and PyYAML
6.0.1. This record's checks ran on 30 September 2026 under Python 3.11.15, pandas 3.0.5 (for
the Saturday witness script), openpyxl 3.1.5, LibreOffice 24.2.7.2 (for the recalc that
`scripts/verify.py` runs) and git 2.43.0. The cold-run script calls `jupyter nbconvert`, which is
nbconvert 7.17.1 in this container; it was not run here. The generator, the D1 witness check and the
scratch counts use the standard library only.

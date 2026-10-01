# Provenance: Build 1 Monday, where every part of the pack came from

**INTERNAL.** Where every part of this pack came from, the numbers it quotes and their sources, what it
departs from, what was invented, and the depth loop. The pack was first built in the India setting on
29 and 30 September 2026 (#176); #202 moved the data and #204 the dossier, card and talk track to the
US setting. This record covers the rebuild of 1 October 2026 to standard v3 in the US setting, on
branch `w03-d1` from main at f21ce02. The dossier, the card, the talk track and their sources file,
`internal/C2_W03_D01_domain_sources_INTERNAL.md`, are #204's and are unchanged.

---

## Sources

| Source | What it gave the pack |
|---|---|
| The Build 1 day prompt and its Monday fill, `prompts/week_revamp_W02_W03.md`, section 4 | The day's parts: the introduction (60), the domain's story (45) after the introduction and before the allocation with its minutes from the translation block, the allocation (30), the translation and the close (15); the pack's eight parts; standard v3; the plant list; the depth loop; the boundaries and the proof |
| `CLAUDE.md` | The build workflow, the hard rules, the folder and naming rules |
| `.claude/skills/day-pack-builder/references/the-standard.md`, standard v3 | The question ladder, the self-contained rule, the decks in depth, the depth loop |
| `.claude/skills/day-pack-builder/references/artifact-manifest.md`, build-week variations | The build-week pack in place of the teaching manifest |
| `docs/detailing/W03_build1_spine.md`, approved 29 September 2026 and set in the US on 30 September | The week, Monday's line, the rule for a demo that fails, the three rubrics and their days, the data pack and its plants with the witness numbers |
| `docs/curriculum/W3_Build_1.md`, Monday's row and Wednesday's row | Monday: the scenario, the thinking trained (a booking is an order, a test is an item, a no-show is a cancellation; the cost of an error), the agenda, the trainer notes, the worksheet and entry one, the `[S]` and `[F]` interview angles. Wednesday: the two things the data team tells the room, which this pack no longer carries (see the departures) |
| `docs/programme/calendar.md`, lines W03/D1 and W03/TUE | Mon 19 Oct, build week, Module 1, no faculty block, rendered through `sync:module:W03/D1` and `sync:day-date:W03/D1`; Tue 20 Oct as Dussehra |
| `docs/07_Client_Zero.md`, sections 1a, 1b and 1c | Dr Priya Menon, Meera Raghavan, Anand Iyer and Kavya Nair; the GCC frame and Kavya's four checks; Kalpa Health in the US, its six metros, four payer kinds and seven denial categories |
| `data/programme/facts.yaml` (as of 30 September 2026) | The campus day; the cohort (35 learners and nine groups, stated; groups of four, locked); the `groups` conflict; the marks per event; the three Build 1 rubrics, rendered through `sync:rubric:W03` and its parts; decisions `four-domains`, `build1-us-data`, `question-ladder`, `self-contained`, `humanizer` |
| `study-notes/C2_W03_D01_domain_us_healthcare_STUDENT.md` and `trainer/C2_W03_D01_domain_story_TRAINER.md` (#204) | James Carter's claim ($135 billed, $70.20 allowed, $64.80 written off, $56.16 paid, $14.04 owed), the $100 journey, the charge-to-cash tree, the heads and what each asks, the rules and the ladder; the dossier's facts as checked on 30 September 2026 |
| `data/generate_kalpa_health.py` and its `--witness`, and `internal/C2_W03_D01_witness_check_INTERNAL.py` | Every planted number, recomputed from the CSV files |
| The Week 1 and 2 calendar lines and deck openers in `content/W01` and `content/W02` | The ten moves on the deck's S27 and the worksheet's method table, named by day and question, with no number quoted from a Week 2 pack |

---

## The data, and how every number was checked

The ten files in `data/` are the export of Friday 16 October 2026, written by
`python3 data/generate_kalpa_health.py --out content/W03/D1/data --stem C2_W03_D01` and last changed
on main by #211. On 1 October 2026 that command, pointed at a scratch folder, wrote ten files
byte-identical to the committed ones; `--contract` printed `PASS every plant holds`. This rebuild
did not touch them.

`internal/C2_W03_D01_witness_check_INTERNAL.py` reads only the committed CSV files. On 1 October 2026
it was widened to recompute every further number the day sheet quotes (the switch metros one by one,
the other four metros' change, the repeated rows' dates and differences, the contract claim's id,
date, metro, screenings and tests, Q2 billed and its mean, billed growth with and without the
contract, the three claim-key formats, the next-worst centre both ways, the three other metros'
lifts, the gaps before the offer, New York's permutation p with seed 20261019, and the denial
reconciliation), and it ended on `RESULT: PASS (0 drifts from the spine and the day sheet)`.

---

## The numbers each file quotes, and where each comes from

### The STUDENT files

| File | The figure | Source |
|---|---|---|
| Every brief, the note, the worksheet, the deck | 5 percent against a plan of 18, and the 13 points | The row and the spine; 18 less 5 |
| Every brief, the note, the deck | Six US metros, a laboratory and two patient service centres in each, eighteen sites | `sites` |
| Every brief, the note, the dictionary | Q2 as April to June 2026 and Q3 as July to September 2026 | Client zero 1c and the generator |
| The note, the dictionary, the briefs, the deck | The ten row counts: 6,700; 18; 16; 11,729; 153; 51,456; 11,356; 11,343; 7,133; 2,381; and the export of Friday 16 October 2026 | Counted on 1 October 2026; the export date is the spine's and #211's |
| The dictionary | Bookings dated 1 April to 30 September 2026; services dated the same; postings recorded 2 April to 16 October 2026; visits 1 July to 30 September 2026; offers sent 15 July to 4 August 2026; twelve tests and four panels; a panel's own price below the sum of its tests' prices | Counted on 1 October 2026 |
| Brief 1, the deck | About 81,000 rows across seven files (81,428) | The row counts |
| Brief 2 | About 18,600 rows (11,729 + 153 + 6,700 + 18) | The row counts |
| Brief 5, the deck notes | The offer's weeks, 15 July to 14 September 2026, and the 9 percent | The generator's campaign window and the witness's 9.0 percent; the 9 percent is the row's |
| Brief 3, the deck | James's claim: $135, $70.20, $64.80, $56.16, $14.04 | The dossier, from the test catalogue and a commercial posting |
| The deck, D11 | $100, $55, $45, $3, $42, $28, $14, $8, $6, illustrative; Quest's operating income at 14.1 percent | The dossier's section 3, and Quest's 10-K for 2025 as the dossier records it, checked on 30 September 2026 |
| The deck, S36 | 35 learners and nine groups, eight of four and one of three, as the plan | `cohort` in facts.yaml, status stated |
| The deck, S40, and the day sheet | 60, 45, 10, 30 and 35; 75, 30, 30, 30 and 15 | The row's 60, 30 and 15, the fill's 45, and the pack's split |
| The deck, S47 to S52, every brief, the note | 40, 30 and 30 marks; the rubrics; the days of Mock R1, the group discussions and the presentations; the rule for a demo that fails | facts.yaml through the sync blocks; the spine's rule |
| Every brief | Each way's rows, from the row counts, and its hours | The hours are the pack's estimates, labelled as estimates |
| Every brief, the deck's D10 | The real-company facts | See the links below |

### The trainer day sheet

| The figure | Source |
|---|---|
| The headline's four readings and the contract's 6,000 tests | The spine; the witness prints each count and rate |
| Sub-problem 1's $180,000, 14.6 percent of $1,231,001, $210.50, $179.75, $150, 22,152 lines, 46,867 and 48,235 tests, 60 text amounts | The spine and the witness |
| Sub-problem 1's claim KH-CLM-007802, account EMP-0007, Dallas, 6 August, 1,200 screenings of 5 tests; Q2's $970,098 and its $176.13 mean; growth of 26.9 percent with the contract and 8.3 without; "$265.00" as a text amount | The widened witness |
| Sub-problem 2's 23.0 and 12.2 percent, 1,415, 1,090 and 1,243 bookings, 11,729 rows over 11,549 ids, 153 new-system bookings | The spine and the witness |
| Sub-problem 2's Chicago 754, 571 and 656 (minus 24.3 and minus 13.0), Philadelphia 661, 519 and 587 (minus 21.5 and minus 11.2), the other four metros' 7.7, 13.0, 6.8 and 21.2 percent, the repeated ids' dates and their 30 and 6 differences, the 180 empty channels and the new system's first and last dates | The widened witness |
| Sub-problem 3's 216 exact matches of 11,343 (1.9 percent), 280 double posts worth $19,204.63, 105 reversals, 398 claims with no posting, $801,314 against $2,201,099 | The spine and the witness |
| Sub-problem 3's 2,269 CLM-numbers and 8,858 bare digits; 1,175 claims marked denied, 1,137 with a $0.00 denial posting and 38 with no posting; 36.4 percent paid of billed; the 398 spread across all six months | The widened witness; the monthly spread counted on 1 October 2026 |
| Sub-problem 4's 52 visits, 50 scheduled and 2 walk-in, 19.2 and 8.7 percent, 20.0 percent (10 of 50) and 15.2 percent, p of 0.22 | The spine and the witness |
| Sub-problem 4's next-worst centres, 9.6 percent on all visits and 16.8 on scheduled visits | The widened witness |
| Sub-problem 5's 2,381 offered and 948 taking it up, 9.0 percent, minus 10.8, 19.9 and 13.0, 50.5 and 21.4 percent offered, 6.9 percent before the offer | The spine and the witness |
| Sub-problem 5's gaps before the offer (plus 1.4, minus 5.2, minus 6.1), the other metros' lifts (minus 4.8, plus 0.6, plus 23.5) and New York's p of 0.03, two-sided over 10,000 shuffles | The widened witness |
| The payer mix of 53.9, 23.9, 14.5 and 7.7 percent | The spine and the witness |

---

## The plants, and where each is used

| Plant | Where it appears | Audience |
|---|---|---|
| The headline, the employer contract, the system switch with its re-export and date format, the claim-key formats with the double posts, the walk-ins and the campaign's targeting | The day sheet's plant table, with where each surfaces and the question to ask if nobody finds it by Wednesday | TRAINER |
| The same numbers, recomputed | `internal/C2_W03_D01_witness_check_INTERNAL.py` | INTERNAL |

No STUDENT file names a plant, hints at its size or reuses a planted value. The checks made on 1
October 2026:

- The data team's two notes, that two metros changed booking systems and that the posting system keys
  claims differently, are gone from the briefing note and the dictionary, since the prompt lists the
  system switch and the claim-key formats as plants.
- The dictionary gives no sample values and no observed code lists, so no sample shows the new
  system's metros, its dates or its date format, a claim reference's shape, or the employer payer.
  It describes each column's meaning and type as its system means to write it, and says the data
  team has not checked the files against the page.
- The bookings brief does not name the two metros, and the no-shows brief gives the report's rate as
  the report works it out without saying what a visit's kind does to it.
- The deck's files pictures name files and row counts only, and its notes say nothing a plant turns
  on.
- The one Kalpa Retail example on S45, Meera's scope, is Week 1's own.

---

## Real companies, and the links behind them

| # | Fact | Where it is used | Source | Checked |
|---|---|---|---|---|
| 1 | Quest: net revenues of $11,035 million in 2025; about 2,400 patient service centres, many inside large retail stores; mobile phlebotomy "so patients who prefer an in-home blood draw may access our services for a fee"; DIS performance assessed on "volume (measured by test requisitions) and revenue per requisition", used to understand "trends affecting number of requisitions, pricing and test mix"; requisition volume change reported each year; "reducing denials and patient concessions" among its areas of focus; DSO, "a measure of billing and collection efficiency", 48 days at the end of 2025; the patient app's appointment scheduling and reminders | Deck D10; briefs 1 to 5; the day sheet | Quest Diagnostics, Form 10-K for 2025, https://www.sec.gov/Archives/edgar/data/1022079/000102207926000015/dgx-20251231.htm | 1 October 2026, curl, text searched |
| 2 | Labcorp: revenues of $13,951.7 million in 2025; "more than 2,200 PSCs" | Deck D10; the day sheet | Labcorp Holdings, Form 10-K for 2025, https://www.sec.gov/Archives/edgar/data/920148/000092014826000111/lh-20251231.htm | 1 October 2026, WebFetch |
| 3 | Optum India: "Largest Global Capability Center for UnitedHealth Group", "providing healthcare operations, technology, analytics and support services" | Deck D10; the day sheet | UnitedHealth Group careers, India, https://www.unitedhealthgroup.com/careers/in/work.html | 1 October 2026, WebFetch |
| 4 | AGS Health: "more than 15,000 skilled RCM professionals worldwide"; delivery centres in Chennai, Vellore, Tirupati, Hyderabad, Ahmedabad, Bengaluru and Jaipur; billing, coding and analytics for "some of the nation's largest healthcare organizations", serving U.S. hospitals and health systems; "Denial Management and Prevention Services" | Deck D10; brief 3; the day sheet | AGS Health, company page, https://www.agshealth.com/company/ | 1 October 2026, WebFetch |

Every other fact about US healthcare in the pack is the dossier's, with its sources and dates in
`internal/C2_W03_D01_domain_sources_INTERNAL.md`.

---

## Decisions, and where the pack departs from the spine, the row or the prompt

| Decision or departure | Reason |
|---|---|
| The data team's two notes are gone | Wednesday's row has the data team tell the room that two cities changed booking systems and that the payment feed keys invoices differently, and the first wave carried both notes into Monday's dictionary. The day prompt makes the system switch and the claim-key formats TRAINER-only plants, and the prompt ranks first. |
| The domain's story runs after the introduction, with a 10-minute break after it | The fill places the story after the introduction and before the allocation, its 45 minutes from the translation block, which the day sheet names: block one's translation drops from 90 to 35 minutes. The break is the pack's own call after 105 minutes of listening, taken from the same block. The talk track's table still says the story runs before the introduction, as a proposal; it is #204's and unchanged, so the day sheet says how to end it today. |
| The spine's text-amount example | The spine gives "$1,050.00" as an example of the 60 text amounts; no billed amount in the claims file reaches $1,000 in text form, so the day sheet quotes "$265.00", which is in the file. |
| The spine's "1,137 denials, 10.4 percent of retail claims" | 1,137 is the count of denial postings and 10.4 percent is the claims file's rate, 1,175 of 11,355; 38 claims marked denied have no posting. The day sheet states both counts. |
| Nine groups where the tracker allocates fifteen | facts.yaml states nine groups as the plan, with the `groups` conflict open; the day sheet gives two ways to allocate nine, and the Programme Head chooses. The STUDENT deck states 35 learners and nine groups as the plan. |
| Option A's spare questions | The first wave's choice (1, 3 and 5 taken; 2 and 4 spare) is kept. The day sheet now notes that Wednesday's parallel build, New York's revenue tree, sits in a metro where neither the contract nor the switch is, which the data confirms. |
| The askers' words | The first wave's wording of the five questions is kept, with question 3 lightly reworded to "the posting system", so that the four parallel Build 1 sessions, which read these briefs, quote the same questions. |
| The ways in each brief | The fill asks for two to four ways sized on rows, hours and error with the move each needs. Each brief lists four and makes no call: choosing the way that leads, and the one that checks it, is the group's translation, which the row and the trainer notes forbid handing over. |
| The deck's build | `scripts/build_deck.py` prints an HTML comment line as slide text, so the three rubric sync markers showed on S49, S51 and S52. `internal/C2_W03_D01_build_deck_INTERNAL.py` builds from a copy with the marker lines removed, with `--out` into `slides/`. The shared fix is for the builder to drop whole-line HTML comments. |
| The row's India setting | The row's six Indian cities, invoices and payment feed, and "Q2" for the fall, are the India setting of v2.2; the spine and client zero 1c win, so the pack speaks of six US metros, claims, remittances and Q2 to Q3. |

---

## What was invented

| Invented | Where |
|---|---|
| The heads' wording of the five questions, each decision and its cost (the first wave's, kept) | The note, the briefs, the worksheet, the deck |
| The four ways per brief, their hours, and what each can get wrong | The briefs and the deck's D slides |
| Full marks per question against the rubric | The briefs |
| The data team's line that it checked only that each file opens with its row count | The dictionary |
| The worksheet's parts beyond the row's three seeded pairs, and its one-line method table | The worksheet |
| The deck's questions, answers and notes | The deck |
| The two allocation options (the first wave's), the sound translations, the words to say, the table of what goes wrong and the interview answers | The day sheet |
| The challenges log's Example entry (the first wave's) | The challenges log |

Dr Menon's 5 percent against a plan of 18 is the row's and the spine's; every number in the files is
synthetic.

---

## Tool versions

Python 3.11.15, openpyxl 3.1.5 (the two workbooks), python-pptx 1.0.2 and mermaid-cli 12.0.0 (the
deck), LibreOffice 24.2.7.2 with the Carlito font installed this session from
`fonts-crosextra-carlito` (the recalcs and the render), git 2.43.0. The generator and the witness use
the standard library only.

---

## The depth loop

| Pass | Who | What it asked | What it found | What changed |
|---|---|---|---|---|
| 1. Draft | The builder | Is every file built from the row, the spine and the dossier? | The first wave's day sheet and deck still read the India setting and "Q1 to Q2"; the briefs had no sized ways, no row counts and no question headings; the dictionary named two plants through the data team's notes | Every STUDENT and TRAINER file rebuilt to standard v3 in the US setting |
| 2. Domain | The builder | Could a learner who never worked in a business say who asks, why the metric matters, what a wrong number costs and which real company faces the same question, from each file alone? | The briefs named no real company | Each brief gained a real-company likeness from Quest's 10-K or AGS Health's page, checked on 1 October 2026 |
| 3. Problem first | The builder | Does every way arrive as an answer to a stated problem, sized, with the move it needs? | Each brief's ways were sized on rows, hours and error, but the call between them was not the brief's to make | Each brief says the call, and the fact that would switch it, is the group's Part 2 |
| Humanizer | The builder, file mode | Which patterns in the humanizer's list remain in each prose file? | One staged run-up ("So, in one line"), one slogan closer, one intensifier, one bold label that should be a question heading, a "you"-less "our estimate", and a saying-like note in the deck | Each rewritten; the tic scanner is clean on every markdown file |
| 4. Rigor | A fresh reviewer | | | |
| 5. Pedagogy and language | A fresh reviewer | | | |

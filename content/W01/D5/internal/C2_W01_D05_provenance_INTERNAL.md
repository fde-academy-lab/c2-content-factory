# Provenance: Week 1, Friday

**INTERNAL.** Where every fact, number and decision in this pack came from. The lab data is
`v3-lab`, **proposed for client zero v2.3** (tracker v7, 21 September 2026) and not yet locked.
Raised to the chapter standard on 30 September 2026, fixed the same day after the orchestrating
session's review, and rechecked the same day to standard v3 (decisions `question-ladder`,
`self-contained`, `humanizer` and `opus-max`); the fix pass and the recheck are logged at the end of
this file.

## Sources, in the order they bind

| Source | What it gave this pack |
|---|---|
| `docs/detailing/W01_W02_spine.md`, approved 29 September 2026 | The day's shape (lab 150, break 10, debrief 40, rehearsal in two rounds 100, timed cases 40, Kahoot and preview 20); the traps as "the week's traps in new places, and a reconciliation skipped under time pressure"; the practice lab as "rerun the step where the learner stalled" |
| `docs/curriculum/W1_Data_analysis_found.md`, Fri 09 Oct row | Kavya's words, the four questions on the table, the method's six steps, the observation rule with no scores on a wall, the client-zero column (v3-lab and its four defect families), the interview angle, the after-class tasks, the Kahoot plan, the references |
| `docs/programme/calendar.md` | Fri 09 Oct, teaching, Module 1, no faculty block |
| `docs/07_Client_Zero.md` v2.2 with the v2.3 note | The stakeholders and their roles; v3-lab named as proposed for v2.3 |
| `.claude/skills/day-pack-builder/references/the-standard.md` and `artifact-manifest.md` | Form; the three devices that keep plants out of learner files; the AI-free lab kept in its own kind |
| `content/W01/D3` and `content/W01/D4` | The week's conventions the lab reruns: the identity rule, the three-way decision, input equals clean plus rejected, the shuffle test and its p-value sentence, the four-part note. The unit each of Friday's tests shuffles comes from the orchestrating review's ruling in the next rows, never from Thursday's files |
| `docs/curriculum/Saturday_papers.md`, W1 paper | Saturday's format for the preview; no Kahoot item copies a paper item |
| The requester's raise of 30 September 2026 (decisions `chapter-standard` and `four-domains` in `data/programme/facts.yaml`) and the session brief for this day | The lab brief opening on the business situation; the debrief as three chapters paired with notebooks; the timed cases as design cases at Kalpa with a real company each; Marketing's sharpest push; design items in the Kahoot and the practice set; the depth loop |
| The orchestrating session's review of the raised pack, 30 September 2026 | Ruling 1: no learner file names a planted value, the debrief included. Ruling 2: the same members across two quarters are tested by flipping each member's own two quarters, and different customers by shuffling labels across whole customers; pooling paired data is the hurried mistake; both directions sit beside a verdict; the lab key lists every route with its number and verdict; nothing credits Thursday with Friday's design. Finding B2 (the lab's cost row), a should-fix list and a minor list. Each is logged with its fix at the end of this file |
| The standard v3 recheck prompt, `prompts/week_revamp_W02_W03.md` section 1, with this day's fills, 30 September 2026 | Every heading a question with who needs the answer and the questions on the way; every file standing alone; the debrief deck carrying each chapter in full; the humanizer's read of every prose file; and four specifics: no number computed from the lab export in any STUDENT file (the three wrong headline rates and notebook 3's corporate fall named), the value reader's comment naming no number form, the shuffle ruling, the nine routes and the sign test at p = 0.043 kept as merged, and Friday's shape kept (the AI-free lab, the debrief, pairs defending the note) |
| `data/programme/facts.yaml`, `saturday_papers.paper_minutes` | The Saturday paper at 120 minutes, which corrected a 110 on the rehearsal deck's S13 |
| The retail and e-commerce dossier, `content/W01/D1/study-notes/C2_W01_D01_domain_retail_STUDENT.md` | Linked by path from the day sheet and the study notes, never copied. Its branch, `w01-domain-retail`, was absent at the start of the build and fetched later on 30 September 2026 (`git show origin/w01-domain-retail:<path>`); the pack's stakeholders, their questions and the DMart likeness agree with its sections 2 and 4, and the day sheet and notes point at its sections 4 and 5. Its one-page card was not yet on the branch |

## The data

```
python3 data/generate_client_zero.py --version v3-lab --out content/W01/D5/data --stem C2_W01_D05
python3 data/generate_client_zero.py --contract
```

`v3-lab` was added to the generator as a new version only, seeded from `SEED + 30` (and `SEED + 31`
for the practice export), with customer ids C-7000 to C-7803 and order ids KR-07001 onward, so no
key from Monday to Thursday recurs. Versions v0 to v3 were written to a scratch folder after the
change and compared byte for byte with the committed day folders: every file identical. The
contract passes with the v3-lab block added.

| File | Rows | Carries |
|---|---|---|
| `C2_W01_D05_lab_orders_STUDENT.csv` | 207 | 197 distinct orders plus 10 repeated rows, one text amount, one empty segment |
| `C2_W01_D05_lab_control_STUDENT.csv` | 2 | Q1 98 orders Rs 60,48,000; Q2 99 orders Rs 43,25,480 |
| `C2_W01_D05_practice_orders_STUDENT.csv` | 79 | 75 distinct orders plus 4 repeated Q1 Retail-Plus rows, one amount "Rs 2,260", one empty customer_id |
| `C2_W01_D05_practice_control_STUDENT.csv` | 2 | Q1 39 orders Rs 23,21,000; Q2 36 orders Rs 23,39,340 |

## The plants, and where each is used

| Plant | Lab file | Used in (TRAINER and INTERNAL only) | Learner files |
|---|---|---|---|
| A batch posted twice, 10 rows in Q2 | KR-07143 (7 August) and nine Retail-Core orders (2 to 10 September) | Lab key, day sheet (its said-aloud table gives the numbers), reference notebook, observation sheet | None of its count, rupees, dates or ids. The debrief deck (S5 to S17), the notes and notebook 1 show the mechanism on the invented export (8 rows, Rs 12,16,420, labelled invented); the lab's rows, count and rupees appear only in notebook 1's empty your-turn cells |
| "9,85,000" stored as text | KR-07073 | Same | None of its value, form, quarter or id. The deck (S21 to S27), the notes and notebook 2 show the mechanism on the invented "850000.00"; the lab's gap, value and row are notebook 2's your-turn cells, and the value reader's comment names no number form |
| Empty segment | KR-07146 | Same | None of its quarter, segment, amount or id. D28, the notes and notebook 2's level 5 show the mechanism on the invented export's Q1 Retail-Core order; the lab's row is a your-turn cell |
| Business on 6 then 4 orders | 5 corporate customers: C-7304 did not reorder and C-7300 ordered once where it had ordered twice | Same | None of its counts, accounts, rate or rupees. The deck (S34 to S38), the notes and notebook 3 show the mechanism on the invented export (5 orders then 2, -36.3 percent, Rs 13,88,200, 99.2 percent of the fall); the lab's counts, rate and coin-flip share are notebook 3's your-turn cells |

The practice export's defects appear in its solution file, which opens only after the practice lab.

**The debrief's chapter notebooks and the plants.** The fix pass after the orchestrating review sized
the chapter notebooks' options on the lab export and printed four numbers computed from it: the three
wrong headline rates (+11.8, -14.6 and -29.2 percent) and notebook 3's corporate fall (Rs 17,10,000,
99.3 percent). The standard v3 recheck removed all of them, and with them every other number computed
from the lab export, plant or not: the control totals, the consumer tree, the Retail-Core lead and its
tests now sit only in TRAINER files. The three chapter notebooks load the invented export from `data/`,
written by `internal/C2_W01_D05_invented_export_INTERNAL.py`, label it invented in every caption,
print and paragraph that quotes it, stage each trap on it with its exact wrong number, and end every
step on an empty your-turn cell whose markdown gives the lines that rerun the step on the lab file. The
deck and the notes quote the same invented figures, so a learner meets one set of invented numbers in
every file and the lab's only on their own screen after the lab. The notebooks keep the names
`01_debrief_quarters`, `02_debrief_values` and `03_debrief_segments`, so a folder listing names no
trap, and the lab rules keep every other notebook in `notebooks/` closed during the lab. The trainer
says the morning's real numbers aloud from the day sheet's said-aloud table, slide by slide. The value
reader's comment says it reads a value "in the forms this week's exports used" and names none of them.

## Decisions that depart from a source

| Decision | Source it departs from | Why |
|---|---|---|
| The lab export is described to learners as "Kalpa-shaped and re-keyed for the drill, so nothing in it belongs in Monday's note" | The row says only "a fresh two-quarter export" | Any business identity for the export (a region, last year's quarters) would be a client-zero fact beyond the lock, and its totals differ from the Q1 and Q2 figures the week established |
| A control-totals file ships with the lab export | The row lists no control file | The reconciliation needs a figure outside the file to land on; Wednesday's Finance figure plays that role in the week |
| The clean finding is Retail-Core's basket, a branch the week never showed | The row says only that the defect families move | A lab that ends on Tuesday's answer measures memory; a new branch measures the method |
| The lab's 150 minutes are terms 10, clock 120, second look 20 | The row: terms 10, lab 120 | The spine's 150; the row's "inside two hours" kept as the clock |
| The debrief splits across lunch, chapter 1 (20) before it and chapters 2 and 3 (10 each) after | The spine lists debrief 40 after the break | The morning block is 180 minutes, so 150 + 10 + 40 does not fit; the reconciliation, the break most rooms fall into, runs before lunch |
| The debrief runs all three chapters every time, and the lunch tally chooses only which reserve slide replaces a self-study slide | The 29 September pack ran the reconciliation and then the two breaks the tally named | The raise sets three chapters, one per place most rooms break |
| In the debrief, the room's wrong number comes before the options, in the deck and in all three notebooks | The standard's chapter order (need, options, build, trap) | A debrief replays where the room broke, so each chapter opens on the number the room sent and then sizes what the step should have been |
| Each debrief chapter is one deck section and one STUDENT notebook, running on the invented export with the lab file behind empty your-turn cells | The standard's teaching-day chapter of about 30 minutes | A lab day's debrief is 40 minutes in all; the notebooks carry the full chapter order (need, options and sizing, build in levels, trap, second route, review, interview, depth) for self-study, and the deck runs the live minutes |
| The option sizings are on what separates the options: analyst minutes at the lab brief's pace, cells, what each needs from outside the file, what it can see, the headline it lets through and the points off the books; option D is run where the file allows it (chapter 3's four tests) and marked not run where it needs a ledger the lab lacks (chapter 1) | The standard asks for sizing in rows, minutes, rupees and error | The review found sizings that separated nothing, since every option computed in under a millisecond; the lab's own pace is the only sourced minute figure |
| The three design cases carry illustrative numbers (about 2,000 orders, 50,000 rows, 12 and 1,200 checkout visits, 1,200 visits a week) | The lock carries no Q3 export, no migrated-ERP quarter and no checkout traffic for Kalpa | Setting the cases at Kalpa, as the raise asks, needed figures the lock does not hold; each is marked illustrative in the STUDENT file |
| The Kahoot has eight items: three on the method (Q1, Q4, Q5), four design calls that take two ideas or a computed sizing (Q2, Q3, Q6, Q7) and Thursday's return (Q8) | The row's quiz plan (five plus the return) | The standard's eight and the review's call for at least a third genuine design items; the row's concepts stay tested, two of them inside the design calls Q2 and Q3 |
| The practice set has sixteen items, nine of them design items (3, 4, 6, 8, 10, 11, 12, 13, 16), six of those with a sizing the learner computes, and item 15 a find-the-defect item | The 29 September set's eleven | The review's call for at least a third genuine design items; every problem ends on one, so each stalled step has its design item |
| The debrief deck, the notes and the three chapter notebooks run every trap, sizing and test on an invented export, labelled invented, and the trainer says the lab's numbers aloud from the day sheet | The raise: the debrief's options sized on the lab data | Ruling 1, then the recheck's first specific: no STUDENT file carries a number computed from the lab export; the lab's sizing is each notebook's your-turn cells |
| In STUDENT files the lead is the invented Retail-Plus basket, tested with each member's two quarters flipped (p = 0.011) and by a sign test (13 of 16, p = 0.021), with pooling as trap 5b and single orders shuffled between segments as trap 5; the lab's Retail-Core lead, its paired test (p = 0.006), the nine routes and the sign test at p = 0.043 stay in the lab key, the reference run and the day sheet | The merged pack showed the Retail-Core lead and its tests in the deck, notebook 3 and the notes | The recheck's first specific removes them from learner files, and its third keeps the shuffle ruling, the nine routes and the sign test at 0.043 as merged, in the TRAINER files |
| Kahoot Q7's key is Retail-Plus's basket | The merged Kahoot keyed the lab's lead segment | No item echoes the lab's finding, so the quiz tests the count-before-rate call without replaying the lab |
| Each chapter map slide's title opens on "Answered in" | The standard: a map slide's title answers like any body slide | `scripts/deck_md_check.py` reads a SECTION title that ends in a question mark as a question slide and fails the deck unless the next title starts with "Answer"; the fix belongs in the shared tool and is named in the recheck's report |
| The note's test flips each Retail-Core customer's own two quarters, reported both ways; the segment label shuffled across whole customers stays as the fair test of a different question; pooling a customer's two quarters (per customer or order by order) and shuffling single orders are traps 5b and 5 | The 29 September key, which tested the note with a label shuffle across customers, accepted the quarter label dealt across single orders, and credited Thursday with the design | Ruling 2 |
| The three chapter notebooks are `01_debrief_quarters`, `02_debrief_values` and `03_debrief_segments` | The raise's names, which named each trap | Ruling 1: a folder listing names no trap |
| The rehearsal defends Thursday's final note | The row says "the note" | Thursday's note is the one going to Monday's review, which is what the rehearsal rehearses |
| Three decks named lab, debrief, rehearsal, where the standard names half1 and half2 | The standard | A lab day takes its week spine's shape; three decks follow the three moments a trainer switches files |
| No companion page, decision workbook, cheat sheet, take-home, whiteboard, tiered extras or per-chapter scenario sets | The standard's teaching-day volume | The raise for this day lists what it adds, and none of these is on it; the lab adds no idea, the chapter notebooks carry a predict item at every level, and the practice set carries the row's FIX task |
| The practice set is four problems of lettered items with a hands-on rerun | The standard: three or four problems | Four problems, each with three to five lettered items, so the audit can check it |

## Invented

**The invented export**, built record by record by `internal/C2_W01_D05_invented_export_INTERNAL.py`
at seed 2020 and written to `data/C2_W01_D05_invented_orders_STUDENT.csv` and
`data/C2_W01_D05_invented_control_STUDENT.csv`, which the three chapter notebooks load. The builder
reads both files back and asserts every figure the deck, the notes and the notebooks quote. It carries
the lab's four defect families in other places and sizes: 175 rows, 167 distinct orders, 130 distinct
amounts; control totals Q1 Rs 40,00,000 on 83 orders and Q2 Rs 26,00,000 on 84, a fall of 35.0
percent; the hurried run Q1 Rs 31,50,000 and Q2 Rs 38,16,420 on 92 rows, up 21.2 percent and 56.2
points off; the count check alone down 17.5 percent, 17.5 points off; 8 repeated rows worth Rs
12,16,420, a corporate Rs 12,00,000 and seven Retail-Plus rows; one Q1 corporate amount stored as
"850000.00", 21.25 percent of the quarter; the bridge Rs 69,66,420 less Rs 12,16,420 plus Rs 8,50,000
to Rs 66,00,000; value accounting 167 present, 166 convertible and 1 logged; one Q1 Retail-Core order
of Rs 2,350 with an empty segment, so Retail-Core reads Rs 73,250 and up 2.2 percent on named rows, Rs
75,600 and down 1.0 percent restored; Retail-Plus frequency 2.00 to 2.44 and revenue up 2.1 percent on
the hurried rows, its basket Rs 3,000 to Rs 2,550, down 15.0 percent, Rs 14,400, clean; the corporate
book down 36.3 percent on 5 orders then 2, Rs 13,88,200 of the Rs 14,00,000 fall (99.2 percent), with
seven orders split at least as unevenly by coin flips in 0.453 of worlds; the mean order Rs 39,521 and
the median Rs 2,350.

Retail-Plus's 16 members place one, two or three orders a quarter, the same number in both quarters
(four once, eight twice, four three times), dealt by `random.Random(36)` in Q1 and
`random.Random(1036)` in Q2. On the clean data, each member's two quarters flipped 2,000 times on
`random.Random(7)`: 22 as large either way, p = 0.011 (0.0015 one way); 0.0109 at 20,000 flips;
exact over all 2^16 flip patterns 704 of 65,536, 0.0107; seeds 1 to 20 between 0.0065 and 0.0165.
The sign test on 13 fell against 3 rose, 0.0213 both ways. Revenue per member Rs 6,000 to Rs 5,100:
flipped 0.0025, pooled and dealt as strangers 0.222 (0.1125 one way). The quarter label dealt across
Retail-Plus's 64 single orders, 0.003. Retail-Plus against Retail-Core, a gap of -14.0 points: the
label across whole customers 0.0385, across single orders 0.0945. Option D, one flipped test per
segment on revenue: Retail-Core -1.0 percent, 0.8275; Retail-Plus -15.0 percent, 0.011; Student +36.9
percent, 0.06; Business -36.3 percent, 0.3705; the chance one of four tests at 0.05 looks real by luck,
0.185.

The member-dealing seed was checked by this recheck over seeds 0 to 39 (Q2 at seed plus 1,000) for
the five properties chapter 3 needs: the paired test and the sign test under 0.05, the pooled deal
over 0.05, and between segments the whole-customer shuffle under 0.05 with the single-order shuffle
over it. Eighteen of the forty seeds have all five; seed 36 is one of them, and its figures are the
ones above. None of these numbers is a Kalpa record or the lab's.

**Elsewhere.** The Kahoot's exhibits (12,400 rows and 12,380 ids; Rs 50, 45 and 47 lakh; p = 0.04; the
four moves in Q7) and the practice set's items on other exports (the 1,240-row profile, "4.5k", "TBC"
and "TEST", 5 lakh rows, 6 "UNKNOWN" of 1,000 orders, Rs 30 and 27 lakh against Rs 28.2 and 29.4 lakh,
2,480 rows and Rs 14,600, the 120-minute read, p = 0.048) are invented, each set on an export the
stem names as another file. The rehearsal's Marketing pushes beyond the row's own facts are invented.
The three design cases' situations are marked illustrative in the STUDENT file: a Q3 export of about
2,000 orders two hours before the review; the migrated ERP's first full quarter of about 50,000 rows
and a Rs 20 lakh gap; a redesigned app checkout at 5 of 12 visits against 31 percent of 1,200, 1,200
visits a week, and about 300 visits per checkout as the case's given size. The 42 against 31 on 12
against 1,200 comes from Thursday's row. None is a Kalpa fact.

Computed here, from the case's own illustrative numbers and the lab file: about 300 visits per
checkout to tell 42 from 31 percent at a 5 percent false-alarm rate and 80 percent power (the
two-proportion formula gives 299.5); D's 240 visits beside 2,160 reach 0.91 power against C's 0.80, in
the TA block; 5 or more conversions in 12 visits at a true 31 percent, 0.303; ten orders split at
least as unevenly as six and four by coin flips, 0.754; the chance at least one of four tests at 0.05
looks real by luck, 0.185; the note's paired test exact over all 2^30 flips, 0.0035; the sign test on
21 against 9, 0.0428; the practice lead's paired test exact over 256 flips, 32 of 256, 0.125.

## The real companies, each fact checked on 30 September 2026

A research agent searched and fetched the sources; the Nykaa figures (from the press release PDF), the
IMDb wording and the DMart figures (across three outlets) were re-checked by the builder the same day.

| Where used | Fact as the pack states it | Source | Checked |
|---|---|---|---|
| Chapter 1 | Nykaa, April to June 2025: consolidated GMV Rs 4,182 crore; revenue from operations Rs 2,155 crore | FSN E-Commerce Ventures press release, 12 August 2025, https://www.nykaa.com/media/wysiwyg/uiTools/2025-8/press-release.pdf | verified 30 Sep 2026 |
| Chapter 1 | Public Health England: 15,841 positive cases from 25 September to 2 October 2020 left out of the reported daily figures because files exceeded a size limit | UK government, "PHE statement on delayed reporting of COVID-19 cases", 4 October 2020, https://gov.uk/government/news/phe-statement-on-delayed-reporting-of-covid-19-cases. The pack does not state the XLS row limit, which only secondary reporting carries | verified 30 Sep 2026 |
| Chapter 2 | JPMorgan's task force: the spreadsheet "divided by their sum instead of their average"; "likely had the effect of muting volatility by a factor of two and of lowering the VaR" | The task force report (January 2013) as quoted verbatim by The Baseline Scenario, 9 February 2013, https://baselinescenario.com/2013/02/09/the-importance-of-excel/. The report PDF itself could not be opened | verified 30 Sep 2026 |
| Chapter 2 | The trading losses of $6.2 billion from what became known as the "London Whale" trades in the Chief Investment Office's Synthetic Credit Portfolio, the FCA's own wording | FCA, JPMorgan Chase Bank N.A. fined £137,610,000, 19 September 2013, https://www.fca.org.uk/news/press-releases/jpmorgan-chase-bank-na-fined-%C2%A3137610000-serious-failings-relating-its-chief | verified 30 Sep 2026 |
| Chapter 3 | IMDb Top 250: at least 25,000 ratings; only regular voters; weighted rating pulls a low-vote title toward the mean of all titles | IMDb Help, ratings FAQ, updated 9 February 2026, https://help.imdb.com/article/imdb/track-movies-tv/ratings-faq/G67Y87TFYYP6TWAV | verified 30 Sep 2026 |
| Chapter 3 | Wainer: small schools over-represented at both tails; Gates Foundation education grants about $1.7 billion by 2001 | Howard Wainer, Picturing the Uncertain World, Princeton University Press, 2009, chapter 1, https://assets.press.princeton.edu/chapters/s8863.pdf. The American Scientist page (May to June 2007) returned 503, so the pack cites the book chapter | verified 30 Sep 2026 |
| Case 1 | DMart Q2 FY26 business update, 3 October 2025: standalone revenue Rs 16,218.79 crore; 432 stores at 30 September 2025; provisional, subject to limited review; the quarter's results reported in a regulatory filing on 11 October 2025 | For the filing date, Business Today, 11 October 2025, https://www.businesstoday.in/markets/stocks/story/dmart-q2-results-avenue-supermarts-profit-rises-4-to-rs-685-crore-revenue-up-15-497833-2025-10-11 (verified 30 Sep 2026, re-checked by the fix pass: the page names the regulatory filing of 11 October 2025). For the update, Bajaj Broking, https://www.bajajbroking.in/share-market-news/dmart-q2-fy2025-26-results-revenue-at-rs-16218-79-crore; IndiaCSR, https://indiacsr.in/dmart-q2-fy26-results-revenue-rises-15-4-to-rs-16218-79-cr-store-count-at-432/; Business Standard, 11 October 2025, https://www.business-standard.com/amp/companies/quarterly-results/avenue-supermarts-q2-net-profit-rises-4-to-685-crore-revenue-up-15-125101100643_1.html. The exchange filing could not be opened | verified 30 Sep 2026 |
| Case 2 | TSB: FCA and PRA fines totalling £48,650,000, 20 December 2022, for the April 2018 migration | FCA, https://www.fca.org.uk/news/press-releases/tsb-fined-48m-operational-resilience-failings | verified 30 Sep 2026 |
| Case 2 | TSB, called a loose likeness in every file: 1.9 million customers unable to view their accounts, attributed to The Register's report of the review; the move from Lloyds Banking Group's platform to Sabadell's Proteo4UK | The Slaughter and May review as reported by The Register, 19 November 2019, https://theregister.com/2019/11/19/tsb_slammed_for_big_bang_it_approach_behind_disastrous_migration | verified 30 Sep 2026 |
| Case 3 | Bing: a headline idea waited more than six months; a "too good to be true" alert; a 12 percent revenue lift worth more than $100 million a year in the US. The article says the result was analysed and confirmed, never re-run, and the pack says "checked" | Kohavi and Thomke, "The Surprising Power of Online Experiments", Harvard Business Review, September to October 2017, https://hbr.org/2017/09/the-surprising-power-of-online-experiments | verified 30 Sep 2026 |

## Links, each checked on 29 September 2026

- Aced (formerly Exponent), top data analyst interview questions, the rehearsal's challenge
  questions; page title "35+ Data Analyst Interview Questions & Answers (2026 Guide)":
  https://www.tryexponent.com/blog/top-data-analyst-interview-questions (verified 29 Sep 2026)
- Seeing Theory, frequentist inference, the student reference:
  https://seeing-theory.brown.edu/frequentist-inference/index.html (verified 29 Sep 2026)

## Tool versions the numbers and outputs came from

The chapter notebooks are built by `internal/C2_W01_D05_build_chapters_INTERNAL.py` and executed cold
in `notebooks/` through `scripts/nb_make.py`; the lab workspace and the reference run are still built
by `internal/C2_W01_D05_build_notebooks_INTERNAL.py`.


Python 3.11 kernel through nbclient; python-pptx 1.0.2; LibreOffice headless for the render check
with fonts-crosextra-carlito installed; mermaid-cli 11.17.0 for the deck diagrams (the session's
global mermaid-cli was 12.0.0, which rejects the `-w` flag `scripts/build_deck.py` passes, so an 11.x
copy was installed in the session's scratch folder and put first on PATH for the build). The 30
September raise used the same arrangement: mermaid-cli 11.17.0 from the scratchpad first on PATH,
fonts-crosextra-carlito installed, LibreOffice headless for the render check, python-pptx 1.0.2. The
fix pass ran Python 3.11.15 with nbclient 0.11.0, python-pptx 1.0.2, LibreOffice 24.2.7.2 headless
with Carlito, and mermaid-cli 11.17.0 on PATH at `/opt/node22/bin/mmdc`. The standard v3 recheck ran
Python 3.11.15 with nbclient 0.11.0, nbconvert 7.17.1, pandas 3.0.6, matplotlib 3.11.2 and
python-pptx 1.0.2; LibreOffice 24.2.7.2 headless with fonts-crosextra-carlito 20230309-2 for the
render check; and mermaid-cli 12.0.0, which `scripts/build_deck.py` now drives through the flags it
detects, so no 11.x copy was needed.

## The depth loop

| Pass | Who | The question | What it found | What changed |
|---|---|---|---|---|
| 1. Draft | The builder | Is every chapter built from the row, the spine and the domain, in the chapter order? | Every chapter traces to the row's four questions, the spine's Friday paragraph and trap line (the reconciliation skipped first), and the dossier's stakeholders; the chapter order holds, with the room's wrong number first in the debrief (see the departures) | The debrief rewritten as three chapters; notebooks 01 to 03 built |
| 2. Domain | The builder | Could a learner who has never worked in a business say, for every chapter, who asks, why the metric matters, what a wrong number costs and which real company faces the same question? | The likenesses sat on self-study slides (D2, D13, D22), so a live room could hear no company; the retail dossier landed mid-build | One sentence of likeness added to each chapter's opening notes; the day sheet and notes point at the dossier's sections 4 and 5 |
| 3. Problem first | The builder | Does every technique arrive as the answer to a stated problem, with options, a sizing and the call, and is the code its last mile? | Every chapter carries options, a sizing on the lab file and the call with its switch; the deck and notebooks 2 and 3 show the room's wrong number before the options, and notebook 1 showed the options first | Recorded as a departure for a debrief; notebook 1 reordered in round two to match its deck |
| 4. Rigor | A fresh reviewer agent, read-only | Do the notebooks run cold, does every trap show its exact wrong number and check, does every sizing hold, is every real-world fact sourced, would a strong interviewer accept every answer? | Round one FAIL. (1) Case 3 sized B and D as if the split were equal: D's 240 visits beside 2,160 give 0.91 power, and B needs about 14 weeks, not 25. (2) The wrong-unit mechanism was stated backwards as a rule. (3) The lab key's model note called the corporate fall noise. (4) The practice lead's test was never run, and it sits at p = 0.047 or 0.011 by the handling of the blank customer_id. (5) The chapter 3 lead's rupee size was not stated. (6) Practice stems named the practice plants. (7) Kahoot Q2's stem gave its key. (8) Three notebook checks could never fail. (9) Mean as read Rs 52,057.7; the practice solution's 'by luck' | (1) Key, STUDENT case, notes and day sheet re-sized. (2) Corrected in deck D29, notebook 3, notes, lab key and the reference notebook: the wrong unit moves p either way, most often too small; here it breaks each customer's Q1 to Q2 pairing. (3) Action now asks the account owner. (4) Test added to the reference notebook's practice section, stated in the solution and the TA note. (5) Rs 15,400, 0.9 percent, in notebook 3, S26 and notes. (6) and (7) Stems rewritten. (8) Checks rebuilt on independent lists and the walk-back headline; option D marked 'needs the ledger'. (9) Stands: `kit.rupees` truncates, and the figures quote the notebook's print; 'by luck' rewritten |
| 5. Pedagogy and language | A fresh reviewer agent, read-only | Does each chapter pair one deck chapter with one notebook that builds on the last, do the devices vary, does every diagram read at print size, is the language free of tics? | Round one FAIL. (1) Two decks older than their markdown. (2) Practice stems named the practice plants and a hands-on number. (3) Design share and one device only. (4) Banned contrast constructions the scanner missed, including two crux lines. (5) Aphorisms. (6) Kahoot Q2 stem. (7) Case 1's options drawn as a sequence, and the slide lit the answer. (8) Kavya's review before the second route. (9) S18 edge labels. (10) 'Break' in two senses. (11) Structure commentary in the notes and the Kahoot header. (12) 'A mix' unexplained | (1) All three decks rebuilt and re-rendered. (2) Stems made generic, hands-on number 3 changed to Retail-Plus's distinct Q2 orders. (3) Items 10 and 16 made design items, 16 an ordering item: seven of sixteen. (4) and (5) Rewritten in every file, crux lines identical in the deck and the notes. (6) Stem cut. (7) Fans from one question, no highlight. (8) Reviews moved to each chapter's last slide. (9) S18 redrawn left to right. (10) to (12) Fixed |

**Round two.** Pass 4 found every round-one fix in place and FAILED on one mislabel: the practice
test's second handling dropped the blank-customer order from the file, where the solution and the TA
note said it was only left out of the customer count; and three low points (two practice options that
still hinted at the practice plants, three checks that could not fail, the INTERNAL decisions row
still at fifteen items). Fixed: the handling relabelled "left out of the file entirely", item 3's own
handling added as a gap-only row (about -34 points, no customer to shuffle) in the reference notebook,
the solution and the TA note; the options made neutral; the reference check now asserts the two
p-values' positions; notebook 1's tautological walk-back check removed and option D labelled as
modelled on C; the decisions row corrected. Pass 5 FAILED on the chapter notebooks' opening cells,
which rendered as code because the builder joined a flush-left paragraph to an indented one, and on
practice items that cued each other's keys and still described the plants; with notebook 1's depth
cell after Kavya's review, one device across the practice set, two deck question keys that were the
longest option, remaining contrast lines, 8.5 point captions on S11 and three minor points. Fixed: the
builder's indentation, so every opener renders as prose; items 2 and 3 set on other exports, items 9,
11 and 14 made neutral, problem timings moved out of the headings; notebook 1 reordered to the deck's
order; item 17 added as a find-the-defect item; S4 and S24 keys shortened; every contrast line
rewritten; S11's captions dropped and their meaning moved into its subtitle; S14's subtitle and S27's
label fixed; the timed cases' links dated on the URL line.

**Round three.** Pass 4 FAILED on wording only: practice item 14's key said the test "says whether it
is chance"; item 15 let a rerun on another seed decide the claim, where p near 0.05 wobbles by about
0.005 at 2,000 shuffles; the notes' "sure it is not chance at the usual bar". Fixed: item 14's key now
says how often chance alone makes the gap; item 15's key is a test on new orders, and the solution and
the TA note say to run 20,000 shuffles before calling a p this close to 0.05; the notes say "below the
usual 0.05 bar". Stands: the reviewer put the one-in-ten split's 80 percent point at about 175
new-checkout visits; the key's own unpooled formula gives 0.802 at 170, so "about 170" stays. Pass 5
FAILED on practice items 2 and 3, whose solution rows answered them with this export's values, item 2's
stem repeating its key, items cueing each other (9 into 8, 17 into 6), debrief S15's key the longest
option with S12's quote giving it away (and S1 giving S4's), and four contrast lines. Fixed: items 2
and 3 set on other exports with other surfaces ("4.5k", "UNKNOWN") and solved generically; item 9 asks
for "the branch that moved"; item 6 rewritten as the second-route design item (value accounting), so
item 17 answers nothing else, and item 17 set on last month's export; S15's key shortened, S12's and
S1's client lines no longer state the key; the lab S7 lines, the rehearsal and notes caveat line and
notebook 1's depth line rewritten. The design share is now eight of seventeen.

**Round four.** Pass 4 PASSED: every number, sizing, trap and p-value statement held, and the notebooks
ran cold. Pass 5 FAILED on cues between keys (S12's subtitle giving S15's key, a regression from round
three; item 7's key echoing item 6's; item 12's key answering item 11) and ten contrast or aphorism
lines, with S1's title and item 1's option c as optional points. Fixed: S12 and S1 retitled and S14's
note made neutral; item 7 asks what the note says with no control total; item 12's key drops the
shuffle unit; item 1's option c made quarter-neutral; every flagged line restated positively,
including the chapter 2 review in the deck and notebook 2 and the "promising, still to be proven"
label.

**Round five.** Pass 5 PASSED, with three recommendations, all applied: S5 no longer states S15's
key, the chapter 3 promise became a question so it no longer states S24's key, and three contrast
lines in the notebooks and one pivot line on S21 and S23 were restated. Kept as a known point: the
chapter titles name where the room broke, so chapter 1's title sits beside S4's question by design;
items 1 and 4 of the practice set share a method and stay answerable on their own.

## The fix pass after the orchestrating review, 30 September 2026

The orchestrating session reviewed the raised pack before merge on branch `w01-d5-chapters` and
returned two binding rulings, one blocking finding, a should-fix list, a minor list and a list of
what to keep. Every item, and what changed for it:

| The review found | What changed |
|---|---|
| Ruling 1. Debrief slides named planted values: S3, S7, S9, S16, S17, D19 and S23 | Those slides, and every slide in the same chain (S5, S6, S8, D10, S14, S20 and S25's subtitle), show the mechanism on the invented export, labelled invented on the slide. S21 and S26 to S28 stay real, since the quarter's fall, the consumer lead and its tests are no plant. The speaker notes send the trainer to the day sheet's debrief table for the morning's own numbers |
| Ruling 1. Notebooks 01 to 03 printed plants; notebook 2's cell 8 said "One value in 207" | Rebuilt from `internal/C2_W01_D05_build_chapters_INTERNAL.py`: every planted count, value, form and place is an empty your-turn cell with the lines to type, the sentence is gone, the value reader names no single form, and notebook 2's segment-sum prediction offers four outcomes of one shape |
| Ruling 1. The notes' trap sections (lines 246 to 320) named plants | The worked case and the three chapters' traps run on the invented export, labelled invented; the Retail-Core lead stays real |
| Ruling 1. The TRAINER files carry the real values said aloud | The day sheet's new table, "The debrief's real numbers, said aloud", gives each slide's invented figure beside the morning's real one and says where the room sees it printed |
| Ruling 1. A folder listing named each trap | The chapter notebooks are `01_debrief_quarters`, `02_debrief_values` and `03_debrief_segments`; the index, the day sheet, the notes and the deck point at the new names |
| Ruling 1. The lab rules | The lab brief, lab deck S5, the lab notebook and the day sheet say no other notebook in `notebooks/` is open during the lab |
| Ruling 2. The unit of the note's test | Each Retail-Core customer's own two quarters flipped: 12 of 2,000, p = 0.006 both ways, 0.0035 exact over all 2^30 flips, 0.0005 to 0.006 on seeds 1 to 20. The segment label shuffled across whole customers, 0.0195, is named as the fair answer to a different question. Both directions sit beside every verdict; the one-way share appears only in TRAINER files, so a TA recognises it |
| Ruling 2. The lab key lists every route with its number and verdict | Nine routes, each with the question it answers, fair or unfair and why, printed and checked by the reference notebook: 0.006, 0.0015, 0.0428, 0.0195, 0.0230, 0.0345 fair; 0.0765, 0.0035 and 0.0755 the traps |
| Ruling 2. The accepted "quarter label shuffled across orders" | Moved into trap 5b with its number, 0.0035 both ways (0.001 one way): on this file it agrees with the fair verdict for the wrong reason, since it treats the same 30 customers' orders as unrelated |
| Ruling 2. The observation sheet coded a p window | It codes the unit read from the shuffle cell: T1 single orders, T1b a customer's two quarters pooled, per customer or order by order, T2 a test on Business, T3 the p-value sentence, T4 a one-way p after looking |
| Ruling 2. Claims that Thursday taught Friday's design: D29, notes line 171, notebook 3 cell 12, reference cell 24, this file's line 16 | Deleted. D29, crux line 4, rehearsal S14 and the notes state "keep each customer's own two quarters together"; the order shuffle between segments is named as trap 5's mistake, with no file or day credited for it |
| B2. The lab brief's cost row, lab deck S1 and S7, and lab notebook cell 13's label pointed at the answer | The cost row names three costs with no direction in them, S1 carries the same text, S7 shows step names and minutes only, and the lab notebook's segment check label is `__TODO__` |
| The practice lead stood uncaveated | Caveated with its paired test, 32 of 256, p = 0.125, in the solution, the TA note and the reference notebook, with the between-segment p (0.047 or 0.011 by handling) as a different question |
| Chapter 1's second route restated the bridge | It sums the set-aside list and the log on their own and checks each against its move in the bridge |
| Option sizings separated nothing; option D was never run | Sized on minutes, cells, what each needs and can see, the headline it lets through and the points off the books; D run in chapter 3 (0.006, 0.79, 0.27, 0.44, and a 0.19 chance one of four looks real by luck), marked not run in chapter 1, S6 and the notes, where it needs a ledger no export carries |
| Chapter 3's second route had no number | The sign test on 21 against 9 prints p = 0.043 in notebook 3, S28 and the notes |
| "Which two accounts" was wrong | C-7304 did not reorder and C-7300 ordered once where it had ordered twice, in the lab key, the reference notebook's per-account table and the day sheet |
| The key did not reach every number, and trap 7 contradicted the flagged-unknown handling | The key gives the flagged-unknown numbers (Retail-Plus Q2 34 orders, Rs 93,670, -1.6 percent; the between-segment test 0.0230), and trap 7 is the silence, never the handling |
| Too few genuine design items | The Kahoot has four of eight (Q2, Q3, Q6, Q7) and the practice set nine of sixteen (3, 4, 6, 8, 10, 11, 12, 13, 16); each takes two ideas or a computed sizing |
| Rehearsal timings; the monsoon push on pair one's list; "mostly" | Round one sums to 50 minutes with the modelled push inside it; the monsoon push is modelled once aloud and is off pair one's list, with its follow-ups in the key; the brief says "half" |
| Case 1's options apart in cost; case 3's power arithmetic in the room; "as good on evidence" | Case 1's plans cost 95 to 105 minutes, so the choice is the step each leaves out; case 3 gives about 300 visits as the case's size and keeps the power arithmetic in the TA block; D is stated as more evidence than C, 0.91 against 0.80, in four times the time |
| Terms left unexplained | GMV, revenue from operations, VaR, muting volatility, the London Whale, booked and ERP are each explained where they first appear |
| Minor: the timed cases key's lab-export line lacked its status | "proposed for client zero v2.3" added |
| Minor: lab S9's notes were stale; S12's design-call count; the afternoon debrief summed to 22 minutes | S9's notes rewritten; S12 names the Kahoot's four design calls; the afternoon debrief runs 10 and 10 |
| Minor: notebook 2's option D; the notes' "a finding, not a result" | D reads "provisional"; the sentence rewritten |
| Minor: TSB attribution and likeness; DMart's filing date | The 1.9 million is attributed to The Register's report of the review and TSB is called a loose likeness in every file; the filing date is cited to Business Today, 11 October 2025 |
| Minor: notebook 3's depth | A table of every route's p on this file (0.0015 against 0.0765 and 0.0325 one way; 0.0195 against 0.0755) with the mean and median |

**Kept, as the review asked.** The lab export's design; the "one export, four headlines" table in the
reference notebook; notebook 2's A-against-B contrast; Marketing's sharpest push; case 3's transparent
arithmetic, now in the TA block; the lab key's trap table, extended to 5b.

**Found by the fix pass itself.** Practice item 2's solution row tripped the marks-language warning and
was reworded; the day sheet's debrief rows were put in slide order; the reference notebook's seed band
was labelled "seeds 1 to 20" and its practice handling pointed at item 4.

**The proofs, run on the branch after the last change.** `python3 scripts/verify.py content/W01/D5
--execute`: PASS, 0 failures and 0 warnings; four notebooks cold-run clean, 58 checks passing and 0
failing, the distractor audit at a=4 b=4 c=4 d=4 on the practice set and a=2 b=2 c=2 d=2 on the
Kahoot, 66 slides rendered with no overflowing box. `python3 scripts/sync_programme.py --check`: every
output current. `python3 data/generate_client_zero.py --contract`: 41 checks passing, 0 failing. All
three decks rebuilt from their markdown and rendered through LibreOffice, and every changed slide
looked at. The tic scanner is clean on every changed markdown file. A grep of every STUDENT file
(markdown, notebook sources and outputs, deck slides and speaker notes) for the plants' values, ids,
dates, counts and give-away phrases finds none of the lab's; its only hits are other exports' own
figures, the invented export's labelled mechanism, and the value reader's list of four forms.

# Provenance: Week 1, Friday

**INTERNAL.** Where every fact, number and decision in this pack came from. The lab data is
`v3-lab`, **proposed for client zero v2.3** (tracker v7, 21 September 2026) and not yet locked.
Raised to the chapter standard on 30 September 2026.

## Sources, in the order they bind

| Source | What it gave this pack |
|---|---|
| `docs/detailing/W01_W02_spine.md`, approved 29 September 2026 | The day's shape (lab 150, break 10, debrief 40, rehearsal in two rounds 100, timed cases 40, Kahoot and preview 20); the traps as "the week's traps in new places, and a reconciliation skipped under time pressure"; the practice lab as "rerun the step where the learner stalled" |
| `docs/curriculum/W1_Data_analysis_found.md`, Fri 09 Oct row | Kavya's words, the four questions on the table, the method's six steps, the observation rule with no scores on a wall, the client-zero column (v3-lab and its four defect families), the interview angle, the after-class tasks, the Kahoot plan, the references |
| `docs/programme/calendar.md` | Fri 09 Oct, teaching, Module 1, no faculty block |
| `docs/07_Client_Zero.md` v2.2 with the v2.3 note | The stakeholders and their roles; v3-lab named as proposed for v2.3 |
| `.claude/skills/day-pack-builder/references/the-standard.md` and `artifact-manifest.md` | Form; the three devices that keep plants out of learner files; the AI-free lab kept in its own kind |
| `content/W01/D3` and `content/W01/D4` | The week's conventions the lab reruns: the identity rule, the three-way decision, input equals clean plus rejected, the shuffle on the customer, the four-part note |
| `docs/curriculum/Saturday_papers.md`, W1 paper | Saturday's format for the preview; the Kahoot avoids the paper's items |
| The requester's raise of 30 September 2026 (decisions `chapter-standard` and `four-domains` in `data/programme/facts.yaml`) and the session brief for this day | The lab brief opening on the business situation; the debrief as three chapters paired with notebooks; the timed cases as design cases at Kalpa with a real company each; Marketing's sharpest push; design items in the Kahoot and the practice set; the depth loop |
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
| A batch posted twice, 10 rows in Q2 | KR-07143 (7 August) and nine Retail-Core orders (2 to 10 September) | Lab key, day sheet, reference notebook, observation sheet | No id and no description; after the lab clock, the debrief deck (S5, S7) and notebook 1 print the Rs 13,35,410 the control total does not hold and Q2's 109 rows against 99 orders; the rows themselves are a your-turn cell |
| "9,85,000" stored as text | KR-07073 | Same | No id and no raw text; after the lab clock, the debrief deck (S16) and notebook 2 print Q1 Rs 9,85,000 short of its control total; the row is a your-turn cell |
| Empty segment | KR-07146 | Same | No id; after the lab clock, D19 and notebook 2's level 4 print the named segments one Q2 order short and Retail-Plus both ways |
| Business on 6 then 4 orders | 5 corporate customers | Same | After the lab clock, chapter 3 of the deck and notebook 3 print Business on 6 orders then 4, as the lesson's subject |

The practice export's defects appear in its solution file, which opens only after the practice lab.

**The debrief's chapter notebooks and the plants.** The requester asked for the debrief's options to
be sized on the lab data and for no learner file to name a plant, and the two collide: sizing on the
lab file prints the lab's totals, the rupee gaps and the tree, and those numbers point at the plants.
The call made here follows the week's own notebooks (Thursday's STUDENT notebooks print the Student
segment's twelve orders and the monsoon sale's segment split): the three chapter notebooks and the
debrief deck print aggregates only (quarter totals as summed and as booked, the Rs 13,35,410 and Rs
9,85,000 moves of the bridge, the Q2 order short in the named segments, Business on six orders then
four) and never an order id, a raw text value or a statement of what was planted. Every place a
learner needs the record itself is an empty your-turn cell with the lines to type. The notebooks and
the deck are released as the lab clock stops, never before, which the day sheet says. The
orchestrating review may prefer invented numbers for the plant-bearing slides; the chapter notebooks
are the only place the lab data could not be replaced without losing the sizing the raise asked for.

## Decisions that depart from a source

| Decision | Source it departs from | Why |
|---|---|---|
| The lab export is described to learners as "Kalpa-shaped and re-keyed for the drill, so nothing in it belongs in Monday's note" | The row says only "a fresh two-quarter export" | Any business identity for the export (a region, last year's quarters) would be a client-zero fact beyond the lock, and its totals differ from the Q1 and Q2 figures the week established |
| A control-totals file ships with the lab export | The row lists no control file | The reconciliation needs a figure outside the file to land on; Wednesday's Finance figure plays that role in the week |
| The clean finding is Retail-Core's basket, a branch the week never showed | The row says only that the defect families move | A lab that ends on Tuesday's answer measures memory; a new branch measures the method |
| The lab's 150 minutes are terms 10, clock 120, second look 20 | The row: terms 10, lab 120 | The spine's 150; the row's "inside two hours" kept as the clock |
| The debrief splits across lunch, chapter 1 (20) before it and chapters 2 and 3 (10 each) after | The spine lists debrief 40 after the break | The morning block is 180 minutes, so 150 + 10 + 40 does not fit; the reconciliation, the break most rooms fall into, runs before lunch |
| The debrief runs all three chapters every time, and the lunch tally chooses only which reserve slide replaces a self-study slide | The 29 September pack ran the reconciliation and then the two breaks the tally named | The raise sets three chapters, one per place most rooms break |
| Each debrief chapter is one deck section and one STUDENT notebook, running on the lab export | The standard's teaching-day chapter of about 30 minutes | A lab day's debrief is 40 minutes in all; the notebooks carry the full chapter order (need, options and sizing, build in levels, trap, second route, review, interview, depth) for self-study, and the deck runs the live minutes |
| The option sizings use the lab brief's pace for analyst minutes and label option D's minutes as an estimate; compute is measured in the notebook | The standard asks for sizing in rows, minutes, rupees and error | The lab's own pace is the only sourced minute figure; the measured compute (under a millisecond) is shown so the room sees the choice is about thought, never compute |
| The three design cases carry illustrative numbers (about 2,000 orders, 50,000 rows, 12 and 1,200 checkout visits, 1,200 visits a week) | The lock carries no Q3 export, no migrated-ERP quarter and no checkout traffic for Kalpa | Setting the cases at Kalpa, as the raise asks, needed figures the lock does not hold; each is marked illustrative in the STUDENT file |
| The Kahoot has eight items: the row's five, two design items and the return | The row's quiz plan (five plus the return) | The standard's eight and the raise's third of items as design items; Q2 was rewritten from "which check catches a duplicate" into the design call "which check first", so the row's concept stays tested |
| The practice set has fifteen items, five of them design items (4, 7, 11, 12, 15) | The 29 September set's eleven | The raise asks for at least a third design items, covering the step where a learner stalled; one per problem, so each stalled step has its design item |
| The rehearsal defends Thursday's final note | The row says "the note" | Thursday's note is the one going to Monday's review, which is what the rehearsal rehearses |
| Three decks named lab, debrief, rehearsal, where the standard names half1 and half2 | The standard | A lab day takes its week spine's shape; three decks follow the three moments a trainer switches files |
| No companion page, decision workbook, cheat sheet, take-home, whiteboard, tiered extras or per-chapter scenario sets | The standard's teaching-day volume | The raise for this day lists what it adds, and none of these is on it; the lab adds no idea, the chapter notebooks carry a predict item at every level, and the practice set carries the row's FIX task |
| The practice set is four problems of lettered items with a hands-on rerun | The standard: three or four problems | Four problems, each with three to five lettered items, so the audit can check it |

## Invented

The 29 September debrief's invented numbers are gone: the debrief now runs on the lab export. What is
still invented: the Kahoot's 180, 171 and 9 and its p = 0.04; the rehearsal's Marketing pushes beyond
the row's own facts; and the three design cases' situations, each marked illustrative in the STUDENT
file (a Q3 export of about 2,000 orders two hours before the review; the migrated ERP's first full
quarter of about 50,000 rows and a Rs 20 lakh gap; a redesigned app checkout at 5 of 12 visits against
31 percent of 1,200, and 1,200 visits a week). The 42 against 31 on 12 against 1,200 comes from
Thursday's row. The practice set's design item 4 uses an illustrative next-month export of about 5
lakh rows. None is a Kalpa fact.

Computed here, from the case's own illustrative numbers: about 300 visits per checkout to tell 42
from 31 percent at a 5 percent false-alarm rate and 80 percent power (the two-proportion formula gives
299.5); 5 or more conversions in 12 visits at a true 31 percent, 0.303; ten orders split at least as
unevenly as six and four by coin flips, 0.754; the chance at least one of four tests at 0.05 looks
real by luck, 0.185.

## The real companies, each fact checked on 30 September 2026

A research agent searched and fetched the sources; the Nykaa figures (from the press release PDF), the
IMDb wording and the DMart figures (across three outlets) were re-checked by the builder the same day.

| Where used | Fact as the pack states it | Source | Checked |
|---|---|---|---|
| Chapter 1 | Nykaa, April to June 2025: consolidated GMV Rs 4,182 crore; revenue from operations Rs 2,155 crore | FSN E-Commerce Ventures press release, 12 August 2025, https://www.nykaa.com/media/wysiwyg/uiTools/2025-8/press-release.pdf | verified 30 Sep 2026 |
| Chapter 1 | Public Health England: 15,841 positive cases from 25 September to 2 October 2020 left out of the reported daily figures because files exceeded a size limit | UK government, "PHE statement on delayed reporting of COVID-19 cases", 4 October 2020, https://gov.uk/government/news/phe-statement-on-delayed-reporting-of-covid-19-cases. The pack does not state the XLS row limit, which only secondary reporting carries | verified 30 Sep 2026 |
| Chapter 2 | JPMorgan's task force: the spreadsheet "divided by their sum instead of their average"; "likely had the effect of muting volatility by a factor of two and of lowering the VaR" | The task force report (January 2013) as quoted verbatim by The Baseline Scenario, 9 February 2013, https://baselinescenario.com/2013/02/09/the-importance-of-excel/. The report PDF itself could not be opened | verified 30 Sep 2026 |
| Chapter 2 | The London Whale trading losses, $6.2 billion | FCA, JPMorgan Chase Bank N.A. fined £137,610,000, 19 September 2013, https://www.fca.org.uk/news/press-releases/jpmorgan-chase-bank-na-fined-%C2%A3137610000-serious-failings-relating-its-chief | verified 30 Sep 2026 |
| Chapter 3 | IMDb Top 250: at least 25,000 ratings; only regular voters; weighted rating pulls a low-vote title toward the mean of all titles | IMDb Help, ratings FAQ, updated 9 February 2026, https://help.imdb.com/article/imdb/track-movies-tv/ratings-faq/G67Y87TFYYP6TWAV | verified 30 Sep 2026 |
| Chapter 3 | Wainer: small schools over-represented at both tails; Gates Foundation education grants about $1.7 billion by 2001 | Howard Wainer, Picturing the Uncertain World, Princeton University Press, 2009, chapter 1, https://assets.press.princeton.edu/chapters/s8863.pdf. The American Scientist page (May to June 2007) returned 503, so the pack cites the book chapter | verified 30 Sep 2026 |
| Case 1 | DMart Q2 FY26 business update, 3 October 2025: standalone revenue Rs 16,218.79 crore; 432 stores at 30 September 2025; provisional, subject to limited review; results approved 11 October 2025 | Bajaj Broking, https://www.bajajbroking.in/share-market-news/dmart-q2-fy2025-26-results-revenue-at-rs-16218-79-crore; IndiaCSR, https://indiacsr.in/dmart-q2-fy26-results-revenue-rises-15-4-to-rs-16218-79-cr-store-count-at-432/; Business Standard, 11 October 2025, https://www.business-standard.com/amp/companies/quarterly-results/avenue-supermarts-q2-net-profit-rises-4-to-685-crore-revenue-up-15-125101100643_1.html. The exchange filing could not be opened | verified 30 Sep 2026 |
| Case 2 | TSB: FCA and PRA fines totalling £48,650,000, 20 December 2022, for the April 2018 migration | FCA, https://www.fca.org.uk/news/press-releases/tsb-fined-48m-operational-resilience-failings | verified 30 Sep 2026 |
| Case 2 | TSB: 1.9 million customers unable to view their accounts; the move from Lloyds Banking Group's platform to Sabadell's Proteo4UK | The Slaughter and May review as reported by The Register, 19 November 2019, https://theregister.com/2019/11/19/tsb_slammed_for_big_bang_it_approach_behind_disastrous_migration | verified 30 Sep 2026 |
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
fonts-crosextra-carlito installed, LibreOffice headless for the render check, python-pptx 1.0.2.

## The depth loop

| Pass | Who | The question | What it found | What changed |
|---|---|---|---|---|
| 1. Draft | The builder | Is every chapter built from the row, the spine and the domain, in the chapter order? | PASS1 | |
| 2. Domain | The builder | Could a learner who has never worked in a business say, for every chapter, who asks, why the metric matters, what a wrong number costs and which real company faces the same question? | PASS2 | |
| 3. Problem first | The builder | Does every technique arrive as the answer to a stated problem, with options, a sizing and the call, and is the code its last mile? | PASS3 | |
| 4. Rigor | A fresh reviewer agent, read-only | Do the notebooks run cold, does every trap show its exact wrong number and check, does every sizing hold, is every real-world fact sourced, would a strong interviewer accept every answer? | PASS4 | |
| 5. Pedagogy and language | A fresh reviewer agent, read-only | Does each chapter pair one deck chapter with one notebook that builds on the last, do the devices vary, does every diagram read at print size, is the language free of tics? | PASS5 | |

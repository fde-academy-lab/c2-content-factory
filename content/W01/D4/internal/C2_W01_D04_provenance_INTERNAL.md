# Provenance: Week 1, Thursday

INTERNAL. Where every part of the Thursday pack came from, what was invented, and what departs from a
source. Rebuilt on 29 September 2026 to the standard of that date, and raised on 30 September 2026
to the chapter standard: the three 50-minute rounds became six chapters, each with its options sized,
its best-fit call, its trap and a second route, one notebook per chapter.

## Sources, in the order they were read

| Source | What it gave the pack |
|---|---|
| `docs/detailing/W01_W02_spine.md`, Thursday row, the campus day, the afternoon-and-lab table | The case, the five rungs, the four traps, the escalated case, the second case, the lab set, the 360-minute day |
| `.claude/skills/day-pack-builder/references/the-standard.md` | The bar, the volume per family, the form of each family |
| `docs/curriculum/W1_Data_analysis_found.md`, Thu 08 Oct row, all fifteen columns | Scenario, thinking, agenda, outcomes, trainer notes, plants, exercises, after-class tasks, interview angle, references, Kahoot plan |
| `docs/programme/calendar.md` | W01/D4, Thu 08 Oct 2026, teaching, M1, no faculty block |
| `docs/07_Client_Zero.md` (v2.2 locked), section 7, version v3 | The dataset and its three witnesses; the stakeholder table |
| `content/W01/D1` | The model for form: deck syntax, notebook helper and rhythm, companion build, workbook build, day sheet |
| `data/programme/facts.yaml`, decisions `chapter-standard` and `four-domains` | The six-chapter grid, the depth loop, and the retail domain linked from Monday's dossier |
| `content/W01/D1/study-notes/C2_W01_D01_domain_retail_STUDENT.md` | Linked by path from the notes, the day sheet and the morning deck's notes; read from `origin/w01-domain-retail` on 30 September 2026 once it was pushed: it calls Retail-Plus Kalpa's paid membership tier, which is how this pack describes it; nothing is copied |

## Data

```bash
python3 data/generate_client_zero.py --version v3 --out content/W01/D4/data --stem C2_W01_D04
python3 data/generate_client_zero.py --version v0 --out <scratch> --stem C2_W01_D04_monday
cp <scratch>/C2_W01_D04_monday_takehome_STUDENT.py content/W01/D4/data/C2_W01_D04_monday_sample_STUDENT.py
python3 data/generate_client_zero.py --version v2 --out <scratch> --stem C2_W01_D04
cp <scratch>/C2_W01_D04_takehome_STUDENT.csv content/W01/D4/data/C2_W01_D04_takehome_STUDENT.csv
```

`python3 data/generate_client_zero.py --contract` passed on 29 September 2026 (v3: Student orders 12
against 12; blended exposure lift +6.1 percent; within Retail-Plus and within Retail-Core -3.0
percent). The v3 files regenerate byte-identical to the ones the 9 September pack carried, checked
again on 30 September 2026 with the command above into a scratch folder and `cmp`.

The six chapter notebooks are written and executed cold by
`internal/C2_W01_D04_build_notebooks_INTERNAL.py` (all six, or any by number). The afternoon deck's
chapter numerals are set to 06 to 11 after each build by
`internal/C2_W01_D04_renumber_afternoon_INTERNAL.py`.

| File | Version | Read by |
|---|---|---|
| `C2_W01_D04_orders_STUDENT.csv` | v3, the 186 cleaned orders | Notebooks 01 to 06, ex1 |
| `C2_W01_D04_exposure_STUDENT.csv` | v3, 160 customers | Notebooks 04 to 06, ex1, ex2 |
| `C2_W01_D04_campaigns_STUDENT.csv` | v3, one campaign | Notebooks 04 to 06, ex1, ex2 |
| `C2_W01_D04_monday_sample_STUDENT.py` | v0, Monday's take-home sample | Practice lab problem 3 (ex3) |
| `C2_W01_D04_takehome_STUDENT.csv` | v2, Wednesday's take-home export | Tonight's take-home |

## Plants, and where each is used

| Plant | Where the room meets it | Kept out of |
|---|---|---|
| Student holds exactly 12 orders (5 then 7, from 2 customers) | Notebook 03, the empty your-turn cell; ex1 part 3 computes it into a variable and never prints it | Every slide, exercise stem, the Kahoot, the companion page and the study notes |
| The Retail-Plus gap is real but modest | Notebook 01, section 3 (135 of 5,000, 0.027), after a predict prompt; notebook 02 (Rs 24,420, 0.19 percent) | Slides show the share only from the room's run onward (S16 on), after the room has computed it |
| The monsoon sale lifts the blend 6.1 percent while each segment falls 3.0 percent | Notebook 04, section 3, after a predict prompt; ex1 part 4 and ex2 apply it | The morning slides show an invented two-store reversal (S51) before the room's split (S52); the Kalpa cells appear only on S54, after the run |
| Take-home plants: header row as body line 45, -2,400 on KR-02018, 12/05/2026 on KR-02030, empty status on KR-02052, six duplicated ids | The take-home | Named only in the day sheet; the self-check gives numbers and generic decisions |

## Decisions that depart from a source

| Decision | Source it departs from | Why |
|---|---|---|
| The shuffle permutes quarter labels on delivered revenue per member | The row says "shuffle the segment labels" | Meera's first question compares two quarters of one segment, so the labels that carry no meaning under chance are the quarters; the take-home keeps a segment comparison |
| The measure is delivered revenue per member | The row leaves the measure open | Monday settled delivered as the money kept, and a member exists in both quarters; on this measure the one-sided share is 0.027, which is the spine's 0.03 without forcing it |
| The morning demonstration runs on Retail-Core, and the room runs Retail-Plus | The spine's rung is "a shuffle test on the Retail-Plus gap" | The trainer shows the wobble first and the room finds the plant; the rung is unchanged |
| The p-value counts one direction (a fall at least as large) | None; the row says "at least as extreme" | Meera asked about a drop; the two-direction share (0.050) is taught as depth in notebook 01 and slide D39 |
| Chapter 3's chance reference is a coin flip per order | The row's shuffle is a label shuffle | Shuffling labels among a fixed set of orders keeps the 5 and 7 split, so it cannot test a count; one coin per order is the same chance-only idea for a count |
| Retail-Plus "beats the wobble" is presupposed by chapter 2's slides and by the Kahoot's return item | The row's plant list | Chapter 2's rung is the question that result raises, and the return question is the row's own; both follow the room's chapter 1 run |
| The monsoon split is a morning chapter (4), met guided, and the escalated case applies it alone | The 29 September pack met it unguided in the case | The chapter standard makes each spine rung a chapter; the case now escalates by combining all three questions alone in 50 minutes |
| Chapter 6 opens the orders file by month (July against August) and designs the hold-back | The row names no month comparison | The spine's sixth chapter is "who got it, who did not, and what else changed"; the orders file carries the months, and the before-and-after trap is the plausible readout a marketing team writes |
| The textbook two-sample test runs as one scipy call in chapter 1 | The row's stop-before names the t-test family | It appears only as the second route, one library call with no formula, named and deferred; scipy ships with scikit-learn in the Codespace's setup |
| The bootstrap range is drawn and named a confidence interval in chapter 2 | The row names the interval at recognition depth and stops before its construction | The resampling loop is the same idea as the shuffle; its construction proper stays later |
| Each chapter set's items 1 and 2 run live, and items 3 to 6 open the practice lab | The standard lists the volume without a slot | Thirty-minute chapters cannot hold a ten-minute set; the lab and the evening take the rest |
| The Kahoot's rate item uses 45 percent on 11 orders against 31 percent on 400 | The row's plan says 40 percent on 12 | The standard's third device: a quiz trap never echoes the planted value |
| The practice lab gives the "four p-value sentences" and "confounder in three vignettes" in new sentences and vignettes | The spine lists the same device names as the row's mid-session drills | The chapter sets use related items; the lab needs fresh ones |
| Tonight's take-home runs on Wednesday's take-home export (v2) with a discount question | The row's after-class task names the note and a shuffle on Monday's data | v3 has no second sample in the generator; v2's second export carries its own plants, spirals Wednesday's cleaning, and the Monday shuffle became practice problem 3 as the spine asks |
| A decision workbook ships beside the companion | The standard lists it; the prompt did not | D1's model pack carries one, and it gives early finishers the day's four decisions with a defect each |

## Invented, and labelled so wherever it appears

- The ten cards (Q1 3,400, 2,900, 4,100, 2,500, 3,800; Q2 2,200, 3,100, 1,900, 2,700, 2,400).
- The twenty no-change segments in notebook 01 (seeds 100 to 119, values Rs 1,500 to Rs 4,500).
- The Rs 20 gap at 100 to 20,000 orders (notebook 02 and morning S26).
- The retention offer at Rs 500 per member per quarter, and the 30 percent margin in notebook 02's depth.
- The one-order swing table, the 400-order segment, and the 42 percent on 12 simulation in notebook 03.
- The two stores in morning S51 (Rs 900 against Rs 1,000; Rs 180 against Rs 200; 8 and 2 of 10).
- The mix shift from 40 to 60 percent in notebook 04's depth, built from the real cells.
- Every number on the companion page and in the decision workbook.
- The numbers each chapter set's opening paragraph names as invented, the lab's vignettes and problem 4, and Kahoot items 1, 3 and 7.

## Links, each checked on the day it entered

| Link | Checked | Used in |
|---|---|---|
| Seeing Theory, frequentist inference: https://seeing-theory.brown.edu/frequentist-inference/index.html | Checked 29 Sep 2026, HTTP 200, title "Seeing Theory - Frequentist Inference" | Take-home, study notes |
| StatQuest video index: https://statquest.org/video_index.html | Checked 29 Sep 2026, HTTP 200, both named videos listed | Study notes |

| Booking.com, 25,000 tests a year: https://hbr.org/2020/03/building-a-culture-of-experimentation | Checked 30 Sep 2026, loads as a paywalled preview carrying the quoted sentence | Chapter 1: notebook, deck S7, notes |
| Booking.com, over 1,000 concurrent and about nine in ten experiments improving nothing: https://hbr.org/podcast/2019/09/at-booking-com-innovation-means-constant-failure | Checked 30 Sep 2026, transcript loads | Chapter 1 |
| Bing, 12 percent and over 100 million dollars: https://hbr.org/2017/09/the-surprising-power-of-online-experiments | Checked 30 Sep 2026, paywalled preview carries the sentence | Chapter 2 |
| Microsoft, about a third of experiments improve their metric: https://ai.stanford.edu/~ronnyk/ExPThinkWeek2009Public.pdf | Checked 30 Sep 2026, PDF | Chapter 2 |
| Wainer, small schools and 1.7 billion dollars: https://assets.press.princeton.edu/chapters/s8863.pdf | Checked 30 Sep 2026, PDF; the American Scientist page returned HTTP 503 three times | Chapter 3 |
| Berkeley 1973, 44 against 35 percent: https://www.refsmmat.com/posts/2016-05-08-simpsons-paradox-berkeley.html | Checked 30 Sep 2026; the Science DOI page returned HTTP 403, so the figures are as this page quotes Bickel and others | Chapter 4 |
| Flipkart Big Billion Days 2022: https://corporate.walmart.com/news/2022/10/25/ahead-of-the-u-s-holidays-indias-shoppers-and-sellers-go-big | Checked 30 Sep 2026 | Chapter 4 |
| Amazon's six-page memos: https://www.aboutamazon.com/news/company-news/2017-letter-to-shareholders | Checked 30 Sep 2026 | Chapter 5 |
| eBay paid search: https://www.nber.org/papers/w20171 | Checked 30 Sep 2026, abstract and PDF | Chapter 6 |

The row's trainer resources (Khan Academy, Exponent, GeeksforGeeks) are not carried into any pack file.
The real-company facts were gathered on 30 September 2026 by a research subagent with WebSearch and
WebFetch in this session, each quote read from the fetched page; a figure that did not load (Wainer in
American Scientist, Berkeley on Science) was taken from the reachable source named above instead.

## Citations in the study notes, each checked on 29 Sep 2026

| Citation | How it was checked |
|---|---|
| Fisher, The Design of Experiments, 1935, as an original reference for the permutation test | Crossref lists contemporary reviews dated December 1935; the Wikipedia article "Permutation test" lists it under original references |
| Simpson, "The Interpretation of Interaction in Contingency Tables", JRSS Series B 13, 1951 | Crossref record for DOI 10.1111/j.2517-6161.1951.tb00088.x |
| Bickel, Hammel and O'Connell, "Sex Bias in Graduate Admissions: Data from Berkeley", Science 187, 1975 | Crossref record and abstract for DOI 10.1126/science.187.4175.398; the notes' sentence follows the abstract ("about as many units appear to favor women as to favor men") |

## Tools the numbers and outputs came from

Python 3.11.15; nbclient 0.11.0 and nbformat 5.11.1 through `scripts/nb_make.py`; scipy 1.17.1 for the
textbook test in chapter 1; pandas is not used (Week 1 stays in plain Python). Every share comes from `random.seed(2026)`, except the invented
segments in notebook 01 (their own seeds) and the invented Rs 20 orders (seed 11). Decks built with
`scripts/build_deck.py` with mermaid-cli 12.0.0 and rendered through LibreOffice with Carlito
(installed in the session with `apt-get install fonts-crosextra-carlito`). The companion page's live numbers come from a seeded mulberry32 generator in
the browser, so they differ slightly from Python's (the walk's 1,000 shuffles give 0.029 there against
0.021 in notebook 01), and every such number on the page is labelled as computed on the page.

## The depth loop, 30 September 2026

| Pass | Who | What it asked | What it found | What changed |
|---|---|---|---|---|
| 1. Draft | The builder | Is every chapter built from the row, the spine and the domain, in the chapter order? | The three rounds held five rungs; the sixth chapter (the fair comparison) had no build, and no chapter had options, sizing or a second route | Six notebooks from one builder script, each: need, options table and sizing cell, best-fit call and switch fact, three or four levels, the trap, a second route, Kavya, interview with a design question, depth |
| 2. Domain | The builder | Could a learner who has never worked in a business say, for every chapter, who asks, why the metric matters, what a wrong number costs and which real company faces it? | Every notebook's first cell and every deck chapter's first two slides name who asks, the metric and the company; chapters 1 and 3 said what a wrong call costs in words only, and the morning deck had no link to Monday's retail story | Chapter 3's options now size waiting in quarters of orders; morning S5 and the day sheet point to the retail dossier by path; the costs stay qualitative where no Kalpa figure exists (no invented rupee cost) |
| 3. Problem first | The builder | Does every technique arrive as the answer to a stated problem, with two or more options, a sizing and the best-fit call with what would change it, and is the code the last mile? | Each chapter has four options, a sizing cell that times or counts them on Kalpa's files, a call and a switch fact before its first build level; chapter 5's first sizing padded the dashboard's word count with filler | Chapter 5's dashboard is now sized from the words chapters 1 to 4 actually printed (443); the deck's options slides carry the same figures as the notebooks |
| 4. Rigor, first run | A fresh reviewer agent | Do the notebooks run cold, does every trap show its exact wrong number and its check, does every sizing hold, is every fact sourced, would an interviewer accept every answer? | FAIL. All nine notebooks ran cold and every headline number recomputed. Six majors: 8 of 44 totals are zero, never 6; chapter 2's trap set a fall against Business's rise; chapter 6's chance reference dealt Retail-Plus orders to months (0.059) where the question is Retail-Plus against Retail-Core; a 14-customer hold-back cannot size a 6 percent lift; the exposure table does not reconcile with the order sample; the note priced a half-tier test at the full Rs 11,000. Minors: the mix called "mostly Retail-Plus", paired data tested unpaired, the bootstrap read too strongly, chapter 3's threshold wording, Booking.com overstated, the difference in differences' pre-period | 8 of 44 everywhere; chapter 2's harm restated as scale against the company and the offer's cost; chapter 6 now shuffles segment labels over both segments' Q2 orders (a 4-point gap either way in 0.82 of deals); the hold-back called its cost, with one line that power sizes it later; chapter 4 and the day sheet say what the exposure extract is; the note tests the offer on half the tier at Rs 5,500; the mix reads half against 40 percent; chapter 1's interview answer names the paired shuffle (the extras sheet runs it); the range is an approximate 95 percent range and its zero share a consistency check; "orders placed" said once and the wait option sized as a rate; Booking.com reads nine in ten experiments improving nothing; the depth section checks May to June |
| 5. Pedagogy and language, first run | A fresh reviewer agent | Does each chapter pair one deck chapter with one notebook that builds on the last, do the devices vary, does every diagram read at print size, is the language clean? | FAIL. Pairing, minutes, crux lines, slide ranges and the scrubber all passed, and 24 of 36 chapter items are design items. Four majors: an unlabelled two-line chart on half2 S8; every chapter item a four-option choice; Kahoot Q8 named Wednesday's duplicates; the cheat sheet's anchor labels near 5 points. Minors: S10 ran into the footer, trap-first order in chapters 3 and 5, no idea count, build commentary in half2 notes, decorative diagrams, Kahoot trap labels, long rationale distractors on numeric items, two stems with no stakeholder, a compressed Kavya line, the dossier link, two "however" adverbs | S8 is now a month table; an order item (chapter 5, Q7) and a match item (chapter 6, Q7) added; Kahoot Q8 says "cleaning"; the anchor redrawn top to bottom, which gains little because the builder fixes the anchor's width (a shared-tool ask); S10 left to right; build commentary removed; Kahoot trap labels aligned on Q2 and Q7; stems given to Kavya and Meera; Kavya's line rewritten; "however" replaced. Kept as they stand: the trap before the build in chapters 3 and 5, where the room must see the headline before counting what stands behind it; the dossier link, whose file is on `origin/w01-domain-retail` and lands with it; the morning's five ideas in 150 minutes, at the cap, with S31 cut first |
| 4. Rigor, second run | A fresh reviewer agent | The same question, on the fixed pack | FAIL on two fixes that had not reached every file (the chapter 1 set still said six zeros; the fall was still set against Business's rise in notebook 02, S26, the notes and the day sheet) and one new major: Retail-Core is chapter 6's comparison segment although Marketing's extract lists Retail-Core customers among those who got the sale. Minors: the day sheet's spread claim, the half-tier test's size, a check label reading no sign as no effect. All six notebooks re-ran cold and every touched number recomputed | Eight zeros in the set and its key; every Business comparison removed from the sizing of the fall; chapter 6's notebook, S8, S11, the notes and the day sheet now call Retail-Core an imperfect comparison and say why a coin is still needed; the spread stated as about two thirds of the mean; eleven a side named as able to show only a large recovery; the label reads "no sign". Checked by grep and a full verify with --execute after the fix |
| 5. Pedagogy and language, second run | A fresh reviewer agent | The same question, on the fixed pack | FAIL on one item: Kahoot Q8's option a still said "duplicates". S8, the order and match items, S9, S10 and S41 passed; the scrubber was clean on all 34 markdown files; the crux lines match; the anchor's small print is recorded as a builder limit | Option a now says "once the file was cleaned"; grep confirms no STUDENT file names Wednesday's duplicates or Student's count |

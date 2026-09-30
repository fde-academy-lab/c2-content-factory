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
`internal/C2_W01_D04_build_notebooks_INTERNAL.py` (all six, or any by number). The three case
notebooks, each a TODO twin and an executed solution, come from one source,
`internal/C2_W01_D04_build_case_notebooks_INTERNAL.py`, whose `--verify` swaps every wrong option
into the solution and confirms a check fails. The afternoon deck's chapter numerals come from
`scripts/build_deck.py` itself, which prints the numeral each SECTION heading carries, so the old
renumber script is gone.

| File | Version | Read by |
|---|---|---|
| `C2_W01_D04_orders_STUDENT.csv` | v3, the 186 cleaned orders | Notebooks 01 to 06, ex1 |
| `C2_W01_D04_exposure_STUDENT.csv` | v3, 160 customers | Notebooks 04 to 06, ex1, ex2 |
| `C2_W01_D04_campaigns_STUDENT.csv` | v3, one campaign | Notebooks 04 to 06, ex1, ex2 |
| `C2_W01_D04_monday_sample_STUDENT.py` | v0, Monday's take-home sample | Practice lab problem 3 (ex3) |
| `C2_W01_D04_takehome_STUDENT.csv` | v2, Wednesday's take-home export, byte-identical to `content/W01/D3/data/C2_W01_D03_takehome_STUDENT.csv` (checked with md5sum, 30 September 2026) | Tonight's take-home, which says so |

## Plants, and where each is used

| Plant | Where the room meets it | Kept out of |
|---|---|---|
| Student holds exactly 12 orders (5 then 7, from 2 customers) | Notebook 03, the empty your-turn cell in section 3 (morning S47 sends the room there); ex1 part 3 computes it into a variable and never prints it | Every slide, exercise stem, the Kahoot, the companion page and the study notes; where a file needs the finding, it states the rule the room drew (under thirty customers, so a lead) |
| The Retail-Plus gap is borderline and modest | Notebook 01, section 4 (145 of 5,000 flips counting falls, 0.029; 286 either way, 0.057), after a predict prompt; notebook 02 (Rs 24,420, 0.19 percent) | Slides show the share only from the room's run onward (morning S19 on), after the room has computed it; the chapter 1 map slide (S7) asks the question without a number |
| The monsoon sale lifts the blend 6.1 percent while each segment falls 3.0 percent | Notebook 04, section 4, after a predict prompt; ex1 part 4 and ex2 apply it | The morning slides show an invented two-store reversal (S61) before the room's split (S62); the Kalpa cells appear only from S63, after the run |
| Take-home plants: header row as body line 45, -2,400 on KR-02018, 12/05/2026 on KR-02030, empty status on KR-02052, six duplicated ids | The take-home | Named only in the day sheet; the self-check gives numbers and generic decisions |

## Decisions that depart from a source

| Decision | Source it departs from | Why |
|---|---|---|
| The chance reference flips each member's own two quarters (a paired sign-flip) on delivered revenue per member | The row says "shuffle the segment labels" | Meera's first question compares the same 22 members in two quarters, so the design is paired: a coin per member decides which of its quarters counts as Q1 (fix-pass ruling 1). The pooled label shuffle stays wherever the groups are different customers: chapter 6, practice problem 3 and the take-home |
| The measure is delivered revenue per member | The row leaves the measure open | Monday settled delivered as the money kept, and a member exists in both quarters; on this measure the flips' share counting falls is 0.029, the spine's 0.03 without forcing it |
| The morning demonstration runs on Retail-Core, and the room runs Retail-Plus | The spine's rung is "a shuffle test on the Retail-Plus gap" | The trainer shows the wobble first and the room finds the plant; the rung is unchanged |
| Both directions go beside every verdict: 0.029 counting falls and 0.057 either way, read as borderline and modest | None; the row says "at least as extreme" | Meera's question came after the fall was seen, so no direction was fixed in advance; the companion glossary's rule, the direction decided before the test is run, governs, and where it was not, both are reported (fix-pass ruling 2). The hard 0.05 checks are gone from notebook 01, the companion and the workbook, which now reads a share against bands agreed before the test |
| Chapter 3's chance reference is a coin flip per order | The row's shuffle is a label shuffle | Shuffling labels among a fixed set of orders keeps the 5 and 7 split, so it cannot test a count; one coin per order is the same chance-only idea for a count |
| Retail-Plus "borderline" is presupposed by chapter 2's slides and by the Kahoot's return item | The row's plant list | Chapter 2's rung is the question that result raises, and the return question is the row's own; both follow the room's chapter 1 run |
| The monsoon split is a morning chapter (4), met guided, and the escalated case applies it alone | The 29 September pack met it unguided in the case | The chapter standard makes each spine rung a chapter; the case now escalates by combining all three questions alone in 50 minutes |
| Chapter 6 opens the orders file by month (July against August) and designs the hold-back | The row names no month comparison | The spine's sixth chapter is "who got it, who did not, and what else changed"; the orders file carries the months, and the before-and-after trap is the plausible readout a marketing team writes |
| The textbook paired test runs as one scipy call (`ttest_rel`) in chapter 1's second route, beside the exact count of all 4,194,304 coin patterns; the pooled shuffle and Welch's test appear as the unpaired numbers | The row's stop-before names the t-test family | It appears only as a second route, one library call with no formula, named and deferred; scipy ships with scikit-learn in the Codespace's setup |
| The bootstrap range resamples the members' own Q1 less Q2 differences and is drawn and named a confidence interval in chapter 2 | The row names the interval at recognition depth and stops before its construction | The resampling loop is the same idea as the flips; its construction proper stays later |
| Each chapter set's items 1 and 2 run live; the lab's four problems are its core at about 60 minutes (10, 15, 20 and 15), and the sets' remaining 26 items are its stretch, for early finishers and tonight, with the TA note's cut order kept | The standard asks for about an hour of work, and facts.yaml gives the lab no length; the merged pack planned about 85 minutes | Thirty-minute chapters cannot hold a ten-minute set, and the requester's recheck fill of 30 September 2026 set the core at about an hour with the rest marked stretch; the cut order still sends the stretch home first, chapters 1 to 3's items before 4 to 6's, then shrinks problems 1 and 2, and never cuts problems 3 and 4 |
| The rule of thumb counts customers: thirty or more customers behind a rate | The row says "under thirty" | More orders from the same few customers add no new evidence, and Student's 12 orders come from 2 customers; the Week 1 Saturday paper's key says "until more customers buy" (coordinator, 30 September 2026). Stated in customers in the note, S39, notebook 03's depth, the workbook's Count tab, the sets and the notes |
| Chapter 2's trap orders the review by rupees moved, which puts Business first, while the fix sizes the fall only against the company and the offer's cost | Pass 4 removed every Business comparison from the fall's sizing | The fix-pass review asked for the trap's ranking to differ from the fix. The ranking now carries the scale point (by money, Business opens the review), and the fix says Business's rise does not shrink the fall, which is judged against the company's quarter and the offer's cost |
| The exposure table is read as a separate population: the campaign platform's August list | `docs/07_Client_Zero.md` v2.2 names the exposure table without saying where it comes from | Its ids (C-6000 to C-6159) never meet the order file's (C-2000 to C-5003), so the pack says what it is wherever it is read (fix-pass ruling 3) and sizes each decision on the list it acts on: the offer on Finance's 22 members, the hold-back on the platform's 70 |
| The Kahoot's rate item uses 45 percent on 11 orders against 31 percent on 400 | The row's plan says 40 percent on 12 | The standard's third device: a quiz trap never echoes the planted value |
| The practice lab gives the "four p-value sentences" and "confounder in three vignettes" in new sentences and vignettes | The spine lists the same device names as the row's mid-session drills | The chapter sets use related items; the lab needs fresh ones |
| Tonight's take-home runs on Wednesday's take-home export (v2) with a discount question | The row's after-class task names the note and a shuffle on Monday's data | v3 has no second sample in the generator; v2's second export spirals Wednesday's cleaning, and the Monday shuffle became practice problem 3 as the spine asks. The file is byte-identical to Wednesday's, so the brief says so and starts each learner from their Wednesday decisions log (fix-pass finding S9) |
| A decision workbook ships beside the companion | The standard lists it; the prompt did not | D1's model pack carries one, and it gives early finishers the day's four decisions with a defect each |

## Invented, and labelled so wherever it appears

- The ten cards, re-paired in the fix pass as five members with a Q1 and a Q2 card each (member order:
  Q1 3,400, 2,900, 4,100, 2,500, 3,800; Q2 2,400, 2,200, 3,100, 1,900, 2,700), in notebook 01, the
  guided sheet, the board work and the companion's walk.
- The heavy-buyer tier in the chapter 1 set's item 6 and the extras stretch: `random.Random(21)`, 30
  members, levels drawn from 2,000 to 7,700, each quarter within plus or minus 600 of the level, Q2 set
  Rs 400 lower; a fall of Rs 314, flips 0.004 counting falls and 0.007 either way, pooled shuffle 0.24
  and 0.49, correlation 0.95.
- The exposure table's story, the pack's own reading. `docs/07_Client_Zero.md` v2.2 and the generator
  give the exposure table no origin, and it disagrees with the campaigns table: `campaigns.csv`
  targets Retail-Plus only, while the exposure table marks 30 Retail-Core customers exposed. The pack
  reads the exposure table as the campaign platform's August list, under the platform's own ids
  (C-6000 to C-6159), a separate population from Finance's order file, which records who received
  the sale whatever the sale was aimed at: the campaigns table is the plan and the list is what the
  platform sent. For a client zero v2.3 note: the lock should name the exposure table as the
  platform's list keyed separately from the orders, and say that it records receipt, whatever the
  target.
- The invented campaigns, stores and limits in the chapter sets' design items (for example the
  northern and southern stores, the campaign month at 40 against 33 percent, the Rs 4,500 limit on
  the hold-back), each labelled invented in its set's opening paragraph.
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

| Booking.com, 25,000 tests a year: https://hbr.org/2020/03/building-a-culture-of-experimentation | Checked 30 Sep 2026, loads as a paywalled preview carrying the quoted sentence | Chapter 1: notebook, morning deck S9, notes |
| Booking.com, over 1,000 concurrent and about nine in ten experiments improving nothing: https://hbr.org/podcast/2019/09/at-booking-com-innovation-means-constant-failure | Checked 30 Sep 2026, transcript loads | Chapter 1 |
| Bing, 12 percent and over 100 million dollars: https://hbr.org/2017/09/the-surprising-power-of-online-experiments | Checked 30 Sep 2026, paywalled preview carries the sentence | Chapter 2 |
| Microsoft, about a third of experiments improve their metric: https://ai.stanford.edu/~ronnyk/ExPThinkWeek2009Public.pdf | Checked 30 Sep 2026, PDF | Chapter 2 |
| Wainer, small schools and 1.7 billion dollars: https://assets.press.princeton.edu/chapters/s8863.pdf | Checked 30 Sep 2026, PDF; the American Scientist page returned HTTP 503 three times | Chapter 3 |
| Berkeley 1973, 44 against 35 percent: https://www.refsmmat.com/posts/2016-05-08-simpsons-paradox-berkeley.html | Checked 30 Sep 2026; the Science DOI page returned HTTP 403, so the figures are as this page quotes Bickel and others | Chapter 4 |
| Flipkart Big Billion Days 2022: https://corporate.walmart.com/news/2022/10/25/ahead-of-the-u-s-holidays-indias-shoppers-and-sellers-go-big | Checked 30 Sep 2026; removed in the fix pass, since a visit count said nothing about a split by segment, and no pack file cites it now | None |
| Amazon's six-page memos: https://www.aboutamazon.com/news/company-news/2017-letter-to-shareholders | Checked 30 Sep 2026 | Chapter 5 |
| eBay paid search: https://www.nber.org/papers/w20171 | Checked 30 Sep 2026, abstract and PDF; re-read the same day in the fix pass for chapter 4's split by customer (new and infrequent users bought more after an ad, frequent users did not) | Chapters 4 and 6 |

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
textbook paired test (`ttest_rel`) and Welch's test in chapter 1, and an exact count of all 2^22 coin
patterns by a sum-by-sum tally in the same cell; pandas is not used (Week 1 stays in plain Python). Every share comes from `random.seed(2026)`, except the invented
segments in notebook 01 (their own seeds) and the invented Rs 20 orders (seed 11). Decks built with
`scripts/build_deck.py` with mermaid-cli 12.0.0 and rendered through LibreOffice with Carlito
(installed in the session with `apt-get install fonts-crosextra-carlito`). The companion page's live numbers come from a seeded mulberry32 generator in
the browser, so they differ slightly from Python's (the walk's 1,000 tosses give 0.037 there against
0.035 in notebook 01), and every such number on the page is labelled as computed on the page. The
workbook is recalculated through LibreOffice by `scripts/xlsx_recalc.py`; the cheat sheet is printed
by `scripts/build_cheatsheet.py` with `--verified "30 September 2026"`.

## The depth loop, 30 September 2026

| Pass | Who | What it asked | What it found | What changed |
|---|---|---|---|---|
| 1. Draft | The builder | Is every chapter built from the row, the spine and the domain, in the chapter order? | The three rounds held five rungs; the sixth chapter (the fair comparison) had no build, and no chapter had options, sizing or a second route | Six notebooks from one builder script, each: need, options table and sizing cell, best-fit call and switch fact, three or four levels, the trap, a second route, Kavya, interview with a design question, depth |
| 2. Domain | The builder | Could a learner who has never worked in a business say, for every chapter, who asks, why the metric matters, what a wrong number costs and which real company faces it? | Every notebook's first cell and every deck chapter's first two slides name who asks, the metric and the company; chapters 1 and 3 said what a wrong call costs in words only, and the morning deck had no link to Monday's retail story | Chapter 3's options now size waiting in quarters of orders; morning S5 and the day sheet point to the retail dossier by path; the costs stay qualitative where no Kalpa figure exists (no invented rupee cost) |
| 3. Problem first | The builder | Does every technique arrive as the answer to a stated problem, with two or more options, a sizing and the best-fit call with what would change it, and is the code the last mile? | Each chapter has four options, a sizing cell that times or counts them on Kalpa's files, a call and a switch fact before its first build level; chapter 5's first sizing padded the dashboard's word count with filler | Chapter 5's dashboard is now sized from the words chapters 1 to 4 actually printed (443); the deck's options slides carry the same figures as the notebooks |
| 4. Rigor, first run | A fresh reviewer agent | Do the notebooks run cold, does every trap show its exact wrong number and its check, does every sizing hold, is every fact sourced, would an interviewer accept every answer? | FAIL. All nine notebooks ran cold and every headline number recomputed. Six majors: 8 of 44 totals are zero, where the pack said 6; chapter 2's trap set a fall against Business's rise; chapter 6's chance reference dealt Retail-Plus orders to months (0.059) where the question is Retail-Plus against Retail-Core; a 14-customer hold-back cannot size a 6 percent lift; the exposure table does not reconcile with the order sample; the note priced a half-tier test at the full Rs 11,000. Minors: the mix called "mostly Retail-Plus", paired data tested unpaired, the bootstrap read too strongly, chapter 3's threshold wording, Booking.com overstated, the difference in differences' pre-period | 8 of 44 everywhere; chapter 2's harm restated as scale against the company and the offer's cost; chapter 6 now shuffles segment labels over both segments' Q2 orders (a 4-point gap either way in 0.82 of deals); the hold-back called its cost, with one line that power sizes it later; chapter 4 and the day sheet say what the exposure extract is; the note tests the offer on half the tier at Rs 5,500; the mix reads half against 40 percent; chapter 1's interview answer names the paired shuffle (the extras sheet runs it); the range is an approximate 95 percent range and its zero share a consistency check; "orders placed" said once and the wait option sized as a rate; Booking.com reads nine in ten experiments improving nothing; the depth section checks May to June |
| 5. Pedagogy and language, first run | A fresh reviewer agent | Does each chapter pair one deck chapter with one notebook that builds on the last, do the devices vary, does every diagram read at print size, is the language clean? | FAIL. Pairing, minutes, crux lines, slide ranges and the scrubber all passed, and 24 of 36 chapter items are design items. Four majors: an unlabelled two-line chart on half2 S8; every chapter item a four-option choice; Kahoot Q8 named Wednesday's duplicates; the cheat sheet's anchor labels near 5 points. Minors: S10 ran into the footer, trap-first order in chapters 3 and 5, no idea count, build commentary in half2 notes, decorative diagrams, Kahoot trap labels, long rationale distractors on numeric items, two stems with no stakeholder, a compressed Kavya line, the dossier link, two "however" adverbs | S8 is now a month table; an order item (chapter 5, Q7) and a match item (chapter 6, Q7) added; Kahoot Q8 says "cleaning"; the anchor redrawn top to bottom, which gains little because the builder fixes the anchor's width (a shared-tool ask); S10 left to right; build commentary removed; Kahoot trap labels aligned on Q2 and Q7; stems given to Kavya and Meera; Kavya's line rewritten; "however" replaced. Kept as they stand: the trap before the build in chapters 3 and 5, where the room must see the headline before counting what stands behind it; the dossier link, whose file is on `origin/w01-domain-retail` and lands with it; the morning's five ideas in 150 minutes, at the cap, with S31 cut first |
| 4. Rigor, second run | A fresh reviewer agent | The same question, on the fixed pack | FAIL on two fixes that had not reached every file (the chapter 1 set still said six zeros; the fall was still set against Business's rise in notebook 02, S26, the notes and the day sheet) and one new major: Retail-Core is chapter 6's comparison segment although Marketing's extract lists Retail-Core customers among those who got the sale. Minors: the day sheet's spread claim, the half-tier test's size, a check label reading no sign as no effect. All six notebooks re-ran cold and every touched number recomputed | Eight zeros in the set and its key; every Business comparison removed from the sizing of the fall; chapter 6's notebook, S8, S11, the notes and the day sheet now call Retail-Core an imperfect comparison and say why a coin is still needed; the spread stated as about two thirds of the mean; eleven a side named as able to show only a large recovery; the label reads "no sign". Checked by grep and a full verify with --execute after the fix |
| 5. Pedagogy and language, second run | A fresh reviewer agent | The same question, on the fixed pack | FAIL on one item: Kahoot Q8's option a still said "duplicates". S8, the order and match items, S9, S10 and S41 passed; the scrubber was clean on all 34 markdown files; the crux lines match; the anchor's small print is recorded as a builder limit | Option a now says "once the file was cleaned"; grep confirms no STUDENT file names Wednesday's duplicates or Student's count |

## The fix pass, 30 September 2026

The orchestrating session's review returned three rulings and eight findings before merge, and the
Week 1 Saturday paper's review added two points. Each is logged with what changed.

| Item | What it asked | What changed |
|---|---|---|
| Ruling 1, the paired design | Retail-Plus compares the same 22 members' Q1 and Q2, so the chance reference flips each member's pair | `flip_gaps` replaces the pooled shuffle in chapters 1, 2, 5 and the escalated case: 145 of 5,000 flips counting falls (0.029), 286 either way (0.057); Retail-Core 0.358 and 0.723. Chapter 1's options size the flips, the pooled shuffle (kept and rejected), the textbook paired test and waiting; its second route counts all 4,194,304 coin patterns (0.027 and 0.055) beside `ttest_rel` (0.0275 and 0.055, t = 2.03 on 21 degrees of freedom), with the pooled shuffle (0.027 and 0.050) and Welch (0.0265 and 0.053) as the unpaired numbers. Chapter 2's bootstrap resamples the members' own differences (Rs 81 to Rs 2,164, 0.016 at or below zero). The companion's walk tosses a coin per member, and its flip machine draws each member's two quarters together beside a pooled shuffle, with a slider for how much members differ. The extras stretch shows the two part on an invented tier where heavy buyers stay heavy (this file's correlation is 0.04). The cheat sheet's panel 3 shows both designs. The pooled label shuffle stays in chapter 6, practice problem 3 and the take-home. Every recurring count moved: S15 to S20, the notes, the day sheet, the escalated case's checks and chapter 1's item 6 |
| Ruling 2, both directions and a borderline verdict | Report both directions beside every verdict; read the fall as borderline and modest; at Rs 24,420 a quarter, worth watching and not worth acting on alone; drop the hard 0.05 checks; one convention | Every verdict now carries 0.029 and 0.057 (or "about 3 in 100, 6 either way"); notebook 01's checks assert the shares against the seeded counts, and its sentence reads borderline because the question came after the fall; the companion's experiments A and B lost their 0.05 line and its machine reads a direction chosen before the run against bands the page states; the workbook's Share tab reads both directions against a reading agreed before the test; chapters 1 and 6 both report the two directions for the same reason, stated in each |
| Ruling 3, the exposure table's population | Say what the exposure table is wherever it is read; settle the 22 against 70 and Rs 5,000 against about Rs 1,139 head-on | One sentence, the campaign platform's August list under its own ids that cannot be matched to Finance's order file, now opens S48, notebook 04, the escalated case's part 4, notebook 06, half2 S3 and S10, and the notes' chapter 4; notebook 04 no longer calls it an order sample; notebook 06, S10, the notes and the day sheet meet the two lists head-on (the offer priced on "the whole tier" of 22 and tested on half; the hold-back 14 of 70); logged in the invented list for a v2.3 note |
| S3, case checks | The case notebooks' checks printed their keys | The case builder writes each check in a later cell that tests the computed value against the number it should reach, and no check reads a key or a line of text; `--verify` swaps every wrong option in and a check fails for each, except ex3's TODO 2 option b, which crashes with Monday's TypeError on purpose |
| S4, cues and lengths | Later stems announced earlier keys; chapter 1's item 5 leaked; chapter 6's item 7 sat on the diagonal; the longest option was always wrong | All six sets rewritten: no stem gives away another item's key, chapter 6's match item keys off the diagonal (A3, B4, C1, D2), and across the 38 chapter items the key is tied longest seven times, shortest or tied shortest seven times and in the middle 24 times; the lab and the Kahoot rebalanced the same way; the distractor audit passes on all eight option files |
| S5, design items | At least a third genuinely design, including in the cases; remove the cheat sheet's C over F and 1/(1 - d) - 1 formulas | Three design items in every chapter set (18 of 38), each asking for a method, a set-up or a decision under a stated constraint rather than a sum (chapter 2's item 1 now asks which half gets a first test, and chapter 4's items 3 and 5 ask for a plan and a set-up), four in the escalated case (items 2, 6, 10, 12) and two in the second case (items 4 and 8); the solution files mark each item's kind; the cheat sheet states both facts in words |
| S6, chapter 3's item 6 | 300 orders called a finding | The item stands on 690 orders and reads "worth testing on its count"; the workbook's Count tab says the same, in customers |
| S7, options and routes | Options sized by what separates them, no unmeasured timings; a paired option in chapter 1; genuinely different approaches in chapter 2; chapter 3's wait sized after the your-turn cell; chapter 4's one-mix route said plainly; a real second route in chapter 5; a placebo in chapter 6; a route that checks the idea in chapter 3 | Each chapter's options table sizes by records, assumptions and seed spread, and none by timings; chapter 2's options are break-even, the range's low end, a half-tier test and a past rate; chapter 3's wait is sized once the count is found, and its second route adds Student-sized handfuls of Retail-Core's orders; chapter 4 says the one-mix route cannot catch an error in its four cells; chapter 5's route applies the day's rules to the numbers and reaches all three decisions; chapter 6's route runs the same test on Q1's months |
| S8, the day sheet and decks | Keys for the new seven-item sets; the escalated brief at 50 minutes after chapter 6; the pushback brief at 40; the renumber step gone; both decks rebuilt | Done; the renumber script is deleted, both decks rebuilt and their changed slides rendered through LibreOffice and read |
| S9, the take-home file | The take-home CSV is Wednesday's | The brief says it is Wednesday's export and starts from the learner's decisions log; the self-check adds customers and both directions |
| S10, counts that disagree | Figure counts and word counts must match everywhere | Notebook 05's note is 193 words with 11 figures, 11 traced, on S63 and in the day sheet; the escalated case's model note is 190 words in its notebook, its solution, the notes and the day sheet |
| Minor findings | Amazon's wording; Flipkart's visit count; thin "never" antitheses; S26's subtitle; S9's overclaim; notebook 04's 70-word sentence; notes opening on the scene; blend, mix and lift in the glossary; S51; one unit for the thirty rule; the lab's budget against the sets' 26 items; ex3's duplicate reasons; S27's speaker; chapter 2's trap ranking | Amazon quoted from the letter; Flipkart replaced by eBay's split by customer; the thin "never" lines rewritten pack-wide; S26, S9 and S51 reworded; the sentence split; the notes open on Meera's Monday; blend, mix, lift, the flip test, the label shuffle and the placebo in the companion's and the notes' glossaries; the thirty rule in customers everywhere; the TA note budgets the 26 items and gives a cut order; ex3's reasons deduplicated; S27 is Kavya's; chapter 2's trap ranks by rupees, logged above |
| Saturday review, point 1 | The thirty rule counts customers | Logged in the decisions above |
| Saturday review, point 2 | campaigns.csv against exposure.csv | Settled in the exposure sentence and logged in the invented list |

Kept as the review asked: notebook 01's twenty invented no-change segments (one at 0.003), notebook
02's Rs 20 gap falling to 0.002, chapter 3's empty your-turn cell with the coin flip, notebook 04
rebuilding 6.1 percent, notebook 05's audit, notebook 06's answer to the 170 percent jump, and the
day sheet's trap table.

Proof run before the push: `python3 scripts/verify.py content/W01/D4 --execute`,
`python3 scripts/build_companion.py content/W01/D4 --check`, `python3 scripts/sync_programme.py
--check`, `scripts/distractor_audit.py` on every option file, the case builder's `--verify`, both
decks rebuilt with `scripts/build_deck.py` and checked by `scripts/deck_check.py`, every changed
notebook executed cold, and the tic scanner on every changed markdown file. Every one passed on
30 September 2026: verify with `--execute` reported zero failures, with 116 notebook checks passing.

## The v3 recheck, 30 September 2026

The merged pack (pull request 201, commit bda418a) was rechecked to standard v3 (decisions
`question-ladder`, `self-contained`, `humanizer` and `opus-max`) from the recheck prompt in
`prompts/week_revamp_W02_W03.md`, section 1, on branch `w01-d4-v3`, restarted from main after a
first session stopped at the usage limit without pushing. The fills: Week 1 Thursday, Thu 8 Oct
2026; the later days' traps (Friday's traps in new places and a reconciliation skipped under time
pressure; Week 2's fan-out, INNER join, whole-table ranking, LAG without PARTITION, doubling merge and
double-counting pivot); and four specifics: keep the merged numbers and verdict exactly, keep the
exposure table's one sentence without spreading it, fit the practice lab's core to about 60 minutes
with the rest marked stretch and the TA note's cut order kept, and rebuild both decks on the cover's
chapter strip from pull request 200.

**Read first, in this order.** `CLAUDE.md`; `the-standard.md` (the question ladder, the self-contained
rule, the decks); `.claude/skills/humanizer/SKILL.md`; the Thursday row of the spine and of the
tracker; this provenance; and, for the form, the sibling rechecks in progress on `origin/w01-d3-v3`
and `origin/w01-d5-v3` (their ladder slide after the cover, their "Answered in six questions" map
slides, their question-titled afternoon sections and their notebooks' closing answer cells).

**The ladder.** The day's question, in Meera's words: is the Retail-Plus fall real, is Student's 40
percent worth budget, and did the monsoon sale work? The day sheet prints the whole ladder at its
top, and every family carries it word for word.

| Chapter, as its opener asks it | Its full question | Notebook | Deck | The spine's rung |
|---|---|---|---|---|
| 1. Real, or the wobble? | Is the Retail-Plus fall real, or the wobble Kalpa sees every quarter? | `01_real_or_wobble` | Morning, SECTION 1, S7 to S24 | A shuffle test on the Retail-Plus gap |
| 2. Worth acting on? | The fall edges past chance: is it big enough, in rupees against what a fix costs, to act on? | `02_worth_acting_on` | Morning, SECTION 2, S25 to S38 | Real against worth acting on |
| 3. How many behind 40%? | Student is up 40 percent, the fastest rise on the page: how many customers stand behind it, and should budget move there? | `03_count_behind_the_rate` | Morning, SECTION 3, S39 to S53 | 40 percent on twelve orders |
| 4. Did the discount work? | Marketing says the monsoon sale lifted revenue 6 percent: did the discount work, or did those customers buy anyway? | `04_discount_by_segment` | Morning, SECTION 4, S54 to S66 | The monsoon discount split by segment |
| 5. What goes on the page? | Three answers are in: what goes on Meera's one page, and when is "not yet" the honest answer? | `05_the_note` | Morning, SECTION 5, S67 to S79 | The one-page note that may say "not yet" |
| 6. What would settle it? | Marketing wants the sale again for more of the base: who got it, what else changed, and what would settle it at Diwali? | `06_fair_comparison` | Afternoon, SECTION 6, S2 to S15 | The sixth chapter: who got it, who did not, what else changed |

**What each family changed.**

| Family | What the recheck did |
|---|---|
| Chapter notebooks | Each title is `# n. <full question>`; the first cell restates what the chapters before found, with the numbers, and gives Who needs the answer and the six questions on the way; the six sections are numbered question headings (the options section is question 1, the second route question 6); the interview and depth headings ask; a closing markdown cell answers each question in one line with its number, before `kit.check_summary()`. The real-company lines carry their sources and check dates inline. Only markdown, the map cell's labels and chapter 3's section references changed, so every printed output is identical to the merged notebooks' (checked stream by stream), and chapter 5's dashboard still counts 506 words |
| Decks | Morning: the day's question and the six chapter questions on S1 after the cover; each SECTION title is the chapter's short question with the full question as its promise; a map slide per chapter ("Answered in six questions, ...") with Who needs the answer and a timeline; subtitles ask and titles answer throughout; a code slide or a code block per build step; the Retail-Plus flips (S19) and Student's coin-flip worlds (S49) drawn as results; closes that answer each smaller question beside Kavya's review. Afternoon: the morning's five answers on S1; chapter 6 in the same form; the case, debrief, second case, drill and close as question-titled sections, the close (S27) answering the day's question. Slides added per chapter: chapter 1 three (map, code, result), chapter 2 two (map, predict with code), chapter 3 three (map, predict with code, result), chapter 4 two (map, result), chapter 5 three (map, each number's partner, the audit's logic), chapter 6 three (recap, map, code), plus the ladder slide and a map for the second case. The morning deck runs to 86 slides and the afternoon deck to 37 |
| Exercises, lab, take-home, Kahoot | Every title and item heading asks; each file carries its scenario, terms and the earlier chapters' findings; solution files give each item its own section with the stem, the key quoted and why each other letter fails; the pushback case's "moves" became parts; the case notebooks' checks and helpers stopped announcing keys (ex1's `revenue()` over the learner's `kept(o)`, ex2's `like_for_like(s)`, ex3's `share_kept` and `plus_k`, and ex1 part 3's check against the exact count of every deal); strawman distractors replaced with plausible wrong answers, every key unchanged |
| Practice lab | The four problems are the core, about 60 minutes (10, 15, 20, 15); the chapter sets' remaining 26 items are the stretch; the TA note keeps the cut order |
| Day sheet | The ladder at its top with the day's answer; every heading a question; the new slide numbers; the escalated and second cases' part questions in the ladder |
| Study notes | The title is the day's question; each chapter is `## Chapter n.` with its full question, Who needs the answer, its six questions and a `###` subsection for each, word for word with the ladder (checked by script), closing on its answer; the last section answers the day's question with the model sentence to Meera; Meera's message, Kavya and every term are introduced where first used; Student's count appears only as "fewer than thirty customers"; the unsupported line "In Week 2 a hold-back becomes a SQL query" is gone. About 5,300 words of prose against 4,550 before, the growth being the ladder's questions and answers |
| Cheat sheet | Every panel heading asks; the crux lines stay word for word; panel 1 names Meera's three numbers. The anchor is now the notes' and deck's left-to-right picture with a per-diagram `wrappingWidth` so labels stay on one line: with the old top-to-bottom anchor, `scripts/build_cheatsheet.py` sized labels near its 5.2-point floor and dropped the vocabulary strip from the PDF while reporting one page, which the merged sheet also did |
| Board work, pre-read, extras | Question headings throughout; the pre-read opens on Kavya's terms for Friday and teaches none of Friday's traps; the extras' stretch carries `flip_gaps` and `shuffle_gaps` so it runs alone, and states the heavy-buyer tier's numbers as rerun (Rs 314; 0.004 and 0.007; 0.24 and 0.49; 0.95); the recovery drill points to notebook 1's sections by their questions |
| Companion page and workbook | The page's title, headings, walk steps and experiment cards ask their questions, its behaviour and library blocks unchanged; each workbook tab's A1 asks its question and the start tab lists them (sheet names cannot hold a question mark), with no input, check or verdict cell moved, so the recalc manifest's cells stand |

**Numbers the recheck corrected (no key changed).** Chapter 1 set, item 6: "about Rs 310" became Rs
314, and option a's "pooled 0.17" became 0.24, recomputed with `Random(21)` (fall 314.1; pooled 0.243
and 0.488; flips 0.004 and 0.007; correlation 0.9525); its solution's "Rs 430" and "about 0.9"
became Rs 314 and 0.95. Chapter 3 solution, item 2: the reasons for b (13 over 10) and c (4 over 11)
now name the arithmetic each wrong letter does. The ex1 and ex3 marker 3 reasons for option a say it
counts nearly every world. The ex3 close reads "five of eight cancelled or returned, averaging about
Rs 3,800", checked against the sample. The lab's model note is 94 words counted without its part
labels. Ex1 marker 6's option d carries its figure, Rs 1,025 apart. The chapter 4 set's Berkeley line
follows the abstract, the chapter 6 set's eBay line the notebook's sourced wording, and the chapter 1
set's Booking.com line this provenance's facts.

**New figures drawn on slides, and how they were computed.** Morning S19: the 5,000 Retail-Plus flips
(seed 2026) in bins of Rs 250 centred from -1,500 to 1,500, counts 26, 99, 205, 425, 585, 678, 854,
773, 598, 388, 225, 98 and 30, with 16 outside the axis; 145 at or above Rs 1,110 and 286 either way,
as in notebook 1. Morning S49: Student's orders dealt by coin 5,000 times (seed 2026): 1,882 worlds
fell, 1,133 rose under 40 percent and 1,985 rose 40 percent or more (0.397); Retail-Core's 73 orders
430 (0.086). Both recomputed from the notebook's own helpers on 30 September 2026. The morning
deck's Retail-Core chart (S17) recomputed to the same counts as the merged slide.

**Decisions this recheck made.**

| Decision | Why |
|---|---|
| Map slides are titled "Answered in six questions, ..." | `scripts/deck_md_check.py` treats a SECTION heading ending in a question mark as a question slide and wants the next slide's title to start with "Answer"; the sibling rechecks use the same form, and a shared-tool change would let a map slide carry any title |
| The code slides show the logic in short form | S16, S30, S48, S62 and S12 in the afternoon are the notebooks' steps cut to four or five lines; S48 leaves out the world with no Q1 orders, which its notes name, and S75's audit tests fewer words than notebook 5's, which the slide says |
| The chapter questions are the day's own wording | The spine names the rungs; the ladder turns each into a plain question in the stakeholder's words, and the day's question joins Meera's three |
| The afternoon deck opens on the morning's five answers | The self-contained rule: a learner who missed the morning follows chapter 6 from the afternoon deck alone |
| No Student count appears on any slide or map | The map slides ask their questions without numbers; results appear only after the room's run (S19, S49 and S63 on); chapter 3's close states the rule the room drew, under thirty customers |

**Tool versions for this recheck.** Python 3.11.15, nbclient 0.11.0, nbformat 5.11.1, scipy 1.17.1,
python-pptx 1.0.2, mermaid-cli 12.0.0, LibreOffice 24.2.7.2 with Carlito installed in the session
(`apt-get install fonts-crosextra-carlito`).

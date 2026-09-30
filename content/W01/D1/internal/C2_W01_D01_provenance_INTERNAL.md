# Provenance: Week 1 Day 1

**INTERNAL.** What this pack is built from, what was verified and when, and every decision that
departs from a source.

---

## The sources

Raised on 30 September 2026 to the chapter standard, from, in this order:

- `docs/detailing/W01_W02_spine.md`, approved on 29 September 2026 and raised on 30 September 2026
  (decisions `chapter-standard` and `four-domains`). It sets the case, the rungs that become
  chapters, the traps and the campus day.
- `.claude/skills/day-pack-builder/references/the-standard.md`, as raised on 30 September 2026,
  including the domain-first-day variant and the depth loop.
- `.claude/skills/day-pack-builder/references/domain-dossier.md`.
- The retail dossier, the domain card and the talk track on `w01-domain-retail`, which this pack
  links to and never edits.
- The Monday 5 October 2026 row of `docs/curriculum/W1_Data_analysis_found.md`, read in column
  order.
- The day's line in `docs/programme/calendar.md`.
- `docs/07_Client_Zero.md` at v2.2, locked 13 September 2026.

The 29 September build of this pack supplied the form: deck syntax, notebook helper and rhythm,
companion, workbook script and day sheet.

## The data

Every file in `data/` is written by `data/generate_client_zero.py`, version `v0`; nothing is
hand-edited, and a regeneration on 30 September 2026 produced byte-identical files.

```
python3 data/generate_client_zero.py --version v0 --out content/W01/D1/data --stem C2_W01_D01
```

| Planted | Where it is used |
|---|---|
| One Business order of Rs 4,80,000, KR-01031 | Chapter 4's trap (the mean of Rs 18,160 against the median of Rs 2,205), found by the learner's own sort in an empty cell; the second case, where it carries store's 91.6 percent |
| One amount stored as the text "4500", KR-01008 | Chapter 1's first sum, met as a TypeError in two minutes and fixed with `int()`; the record is found in an empty cell |
| The take-home's second sample: two Business orders (Rs 3,12,000 and Rs 2,05,000) and the text "1990" | The take-home; named only in the day sheet |

The plants appear by value only in `trainer/` and here. Chapter 6 counts the Business customer
among the 9 one-time buyers too recent to judge, since it ordered 43 days before the extract ends;
no learner file lists the 9 ids.

## The build: the story and six chapters

| Deck section | Notebook | Chapter | Trap and its exact wrong number |
|---|---|---|---|
| Morning, SECTION 0 | `00_retail_story` | The retail story, from the talk track and the dossier | None; the formulas on invented numbers, each with the trap the card names |
| Morning, SECTION 1 | `01_four_readings_of_sales` | Four readings of sales | Rs 5,44,810 as sales, 4 cancelled store orders inside |
| Morning, SECTION 2 | `02_the_tree_as_metrics` | The tree as metrics | AOV Rs 25,943, booked rupees over delivered orders; Rs 7,78,300 multiplied back |
| Morning, SECTION 3 | `03_the_leaves_counted` | The leaves, counted | 30 customers, 1.00 orders each |
| Morning, SECTION 4 | `04_the_typical_order` | The typical order | The mean of Rs 18,160 as typical, median Rs 2,205 |
| Afternoon, SECTION 5 | `05_which_branch_first` | Which branch first | Two 10 percent lifts called 20 percent, Rs 6,53,772 against Rs 6,59,220 |
| Afternoon, SECTION 6 | `06_the_sentence` | The sentence Meera acts on | "70 percent lost", when 9 of 16 one-time buyers are inside the 45-day repeat gap |

The notebooks are written by `internal/C2_W01_D01_build_notebooks_INTERNAL.py` and executed cold in
their own folder by `scripts/nb_make.py`. The decks are built by
`internal/C2_W01_D01_build_decks_INTERNAL.py`, which runs `scripts/build_deck.py`'s build and prints
each chapter opener's own numeral (see decision 1).

## Decisions that depart from a source

1. **Chapter opener numerals.** `scripts/build_deck.py` numbers openers by position, which would
   print chapter 5 as 01 in the afternoon deck. The day-folder wrapper prints the number written in
   the heading: 00 for the story, 01 to 06 for the chapters, and A to E for the afternoon's case
   blocks, which have no chapter notebook. A rebuild with `scripts/build_deck.py` alone gives the
   same slides with positional numerals.
2. **Two traps are this pack's, in chapters the spine gives no trap.** The spine lists four traps
   for Monday and the standard asks one per chapter. Chapter 2 stages a fraction from two
   definitions (Rs 25,943), and chapter 6 stages one-time buyers read as lost (70 percent). Both
   follow from the chapters' questions on this file.
3. **The escalated case moves to the delivered definition.** The spine's escalated case answers
   the leaves, the typical order, the branch and the window, and chapters 3 to 6 now teach all four
   on booked orders. Rebuilding the answer on Anand's delivered definition keeps the case a harder,
   unguided climb, with the odd-count median, the plan and discount on delivered revenue, and the
   window's edge.
4. **The afternoon's minutes.** Chapter 5 moves to the afternoon, and the case blocks give up the 30
   minutes: the escalated case runs 35 (from 50) and the second case 25 (from 40). The debrief,
   break, drill and Kahoot keep the standard's minutes. The morning runs the story 45, the ask 5,
   chapters 1 to 3, the break before chapter 4, and chapter 4.
5. **The row's environment block (25 minutes) is gone.** Week 0 set up the Codespace; the day
   carries the one TypeError in chapter 1, two minutes.
6. **The Kahoot departs from the row's plan in two items.** The row's Q3 ("'4500' > 3000") tests
   syntax, and its Q5 (cells run out of order) tests a kernel topic the chapter grid no longer
   teaches. They are replaced by chapter 2's mixed fraction and chapter 6's window edge. There is no
   return question on Day 1, as the row says.
7. **Anand Iyer is the finance controller.** The row calls him the CFO; `docs/07` says finance
   controller, and the pack follows `docs/07`.
8. **The second case groups revenue by segment and channel** with a dictionary, per the spine's
   afternoon table, although the row's stop-before line names grouping by segment; Tuesday still
   owns grouping as a technique.
9. **The plant rule, applied to the afternoon.** It holds as on 29 September. Aggregates that
   include the Business order are the trap numbers and are printed. Rupees without it appear only
   on consumer orders in afternoon files, introduced as "the order your chapter 4 sort put at the
   top".
10. **Interview questions.** The row's five anchors are kept. The pack adds seven case-style and
    design follow-ups, tagged on the row's scale by this pack.
11. **The workbook gains two tabs**, Fraction and Edge, so every chapter's decision has a tab; the
    recalc manifest proves both.

12. **The 15 percent plan is sized on the everyday orders.** The spine's chapter 5 asks which
    branch Meera opens first; sized on booked revenue, each extra order would carry the Rs 18,160
    mean, which the one Business order sets. Chapter 5 and the escalated case size the plan on the
    orders other than the one chapter 4's sort found, and say why. The two-lifts trap stays on booked
    revenue, since it is multiplication and holds on any base.

## Invented, and recorded as invented

1. Kalpa Retail sells to consumers and to businesses: consumer orders sit in the locked Rs 800 to
   Rs 3,000 band and the Business segment buys in bulk, as the generator's docstring sets it.
2. The Week 1 extract is Kalpa Retail India for one window, 1 July to 26 September 2026.
3. Marketing's Rs 12 crore is the acquisition line of the growth plan, not one quarter's spend.
4. The story notebook's numbers are the dossier's illustrative numbers, labelled invented in
   every cell that uses them: Rs 100 of GMV, the Saturday basket, the app's funnel, the month's
   tree, January's cohort, the CLV and CAC, inventory days, the two categories and the like-for-like
   stores.
5. Chapter 4's sizing and mechanism set: five invented orders of Rs 1,900 to Rs 2,600 and one of
   Rs 90,000.
6. Chapter 6's reading times for the four answer formats (2, 20 and 60 seconds) are this pack's
   estimates, labelled as the sizing of a choice.
7. The lab's orders W-01 to W-08 and IV-01 to IV-12, 50,000 registered users in lab item 14, and a
   Rs 1,500 cost per customer in the stretch task, each labelled invented where it appears.

## The real company in each chapter

All are from the dossier's likeness section and its sources file, checked on 30 September 2026.

| Chapter | Fact | Link | Checked |
|---|---|---|---|
| 1 | Reliance Retail: gross revenue Rs 90,408 crore and revenue from operations Rs 79,745 crore, quarter to June 2026 | https://www.ril.com/sites/default/files/2026-07/Media_Release_RIL_Q1_FY2026-27_Financial_and_Operational_Performance.pdf | checked 30 Sep 2026 |
| 2 | Jio: 533 million subscribers, revenue per user Rs 215.6 a month, churn 1.6 percent a month | The same release | checked 30 Sep 2026 |
| 3 | Reliance Retail: 396 million registered customers and 20,169 stores at 30 June 2026 | The same release | checked 30 Sep 2026 |
| 4 | Blinkit: net AOV Rs 518 and 2,443 dark stores, quarter to June 2026 | https://www.medianama.com/2026/07/223-takeaways-eternal-q1-fy27-earnings-call/ | checked 30 Sep 2026 |
| 5 | Flipkart Black at Rs 1,499 a year, 2025 | https://stories.flipkart.com/flipkart-black-loyalty-program-2025 | checked 30 Sep 2026 |
| 5 | Amazon Prime in India from Rs 399 to Rs 1,499 a year | https://www.aboutamazon.in/news/retail/new-amazon-prime-membership-plans-in-india | checked 30 Sep 2026 |
| 6 | Klarna: two-thirds of chats in the first month | https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/ | checked 30 Sep 2026 |
| 6 | Klarna's CEO on lower quality from a cost-first approach | https://fortune.com/2025/05/09/klarna-ai-humans-return-on-investment/ | checked 30 Sep 2026 |

## The row's references, with the date each was checked

Each link was requested on 29 September 2026 and returned HTTP 200, except where noted.

| Link | Role | Checked |
|---|---|---|
| https://www.hackingthecaseinterview.com/pages/profitability-case-interview | The profitability case, trainer preparation and the notes | checked 29 Sep 2026, 200 behind a bot challenge page |
| https://www.roadtooffer.com/blog/driver-tree | Driver trees, the notes | checked 29 Sep 2026, 200 |
| https://mconsultingprep.com/profitability-case-framework | The framework's revenue variants, the notes and the take-home | checked 29 Sep 2026, 200 |
| https://automatetheboringstuff.com/3e/ | Loops and dictionaries, the notes' reading path | checked 29 Sep 2026, 200 |
| https://docs.github.com/en/codespaces/developing-in-a-codespace/getting-started-with-github-codespaces-for-machine-learning | Codespaces with Jupyter, trainer preparation | checked 29 Sep 2026, 200 |
| https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7 | Corey Schafer, the beginner playlist | checked 29 Sep 2026, 200 |
| https://www.youtube.com/watch?v=daefaLgNkw0 | Corey Schafer, Dictionaries | checked 29 Sep 2026 through the oEmbed endpoint, since the page returned 429 |
| https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/mean-median-basics/v/mean-median-and-mode | Mean, median and mode | checked 29 Sep 2026, 200 |
| https://britinstitute.uk/blog/data-analyst-case-study-interview-questions | The sales-drop case, Tuesday's pre-read | checked 29 Sep 2026, 200 |

## Tools the numbers and outputs came from

Python 3.11.15 and nbclient 0.11.0 for every notebook output and error text; python-pptx through
`scripts/build_deck.py` for the decks, with mermaid-cli 12.0.0 as installed in the session;
LibreOffice for the workbook recalculation and the deck render check, with the Carlito font
installed from `fonts-crosextra-carlito` on 30 September 2026.

## The depth loop

| Pass | Asked | Found | Changed |
|---|---|---|---|
| 1. Draft | Is every chapter built from the row, the spine and the dossier, in the chapter order? | The spine's five rungs became six chapters, with the sixth the rung's hardest form, the sentence with its caveat. Every deck chapter and notebook runs need, options, build, trap, second route and review. | Nothing further. |
| 2. Domain | Could a learner who has never worked in a business say, for every chapter, who asks, why the metric matters, what a wrong number costs and which real company faces the same question? | Every chapter's first notebook cell and first two deck slides name the metric, who asks, the cost of a wrong number and a real company with its source. The chapters did not point to the dossier's sections by name, which the domain-dossier reference asks for. The escalated and second cases name no real company, since they are not chapters. | Each chapter notebook's need table gained an "In the dossier" row naming its section (3, 5, 5, 5, 2 and 5, 5 and 8); the study notes name the sections in their reading path. The cases stand as they are. |
| 3. Problem first | Does every technique arrive as the answer to a stated problem, with two or more options, a sizing and the best-fit call with what would change it, and is the code its last mile? | Every chapter has four options sized on the file (rows, passes, seconds, fields, rupees moved or reading time), a best-fit call and the fact that would switch it, and a second route asserted equal. Chapters 3, 4 and 6 staged the trap before the build, against the chapter order of need, options, build, trap, second route and review; every notebook put Kavya's closing review before the second route. | Chapters 3, 4 and 6 were reordered to build then trap in the notebooks, the decks and the study notes (chapter 6 now builds a first draft whose "16 bought once" the trap turns into "70 percent lost"; chapter 4 gained a fix slide). Kavya's closing review moved after the second route in all six notebooks. The day sheet's slide ranges were renumbered. |
| 4. Rigor, first run | Do the notebooks run cold, does every trap show its exact wrong number and its check, does every sizing's arithmetic hold, is every real-world fact sourced, and would a strong interviewer accept every answer? | FAIL. Every notebook ran cold and every recomputed number held, but: a chapter 4 distractor printed the plant's value (Rs 4,80,000 / 30); the second case's combined key was wrong for items 3, 7 and 9; chapter 5 sized the plan on booked revenue, so each extra order was silently worth the Rs 18,160 mean; chapter 2's identity table multiplied by the same denominator, so the trap row showed a real total; the payback answer priced a total on a median; Kahoot Q1's key used additive reasoning; notebook 00 counted acquisition marketing twice in the payback; `c2kit.rupees` truncates, so three outputs disagreed with the text by a rupee; afternoon files name the Business segment; the chapter 1 trap stem was ambiguous; several design items and distractors gave the key away. | The distractor is now the 16th order. The combined key reads 3c 4b 5a 7d 8b 9a 11c to 16b with the three numbers. Chapter 5 and the escalated case size the plan on the everyday orders, setting aside the order chapter 4's sort found: 29 orders, Rs 9,722 more, 3.3 customers or 4.35 orders, and 20 delivered orders, 3 more. The identity multiplies by the orders the revenue was summed over (30 x (Rs 5,44,810 / 21) = Rs 7,78,300). The payback answers now use the targeted segment's mean, with the median quoted as the typical order. Kahoot Q1's key names orders per customer or order value. Notebook 00 adds the double count and the 14-month reading. Non-integer rupees are rounded before `kit.rupees`. The chapter 1 stem reads "never left the shelf". Chapter 4 Q3 and Q4, chapter 5 Q1 and Q5, chapter 6 Q1 and escalated Q4 were rewritten; the lab set's keys were rotated in four items; the Kahoot's Tests lines no longer state answers. The Business segment naming in afternoon files stands: it follows the 29 September decision recorded above (decision 9), after the chapter 4 sort, and the segment name is a column value every record prints; a ruling that extends `plants-once-found` to same-day files would settle it. Anand stays the finance controller (decision 7). |
| 5. Pedagogy and language, first run | Does each chapter pair one deck chapter with one notebook that builds on the last, do the devices vary, does every diagram read at print size, and is the language free of the tics the scrubber finds? | FAIL. Pairing and the grid held, but: the escalated case had two post shapes and its key sat in a STUDENT deck's notes; slide minutes summed to 25 to 28 in four chapters and three section notes listed the old order; notebook 05's Predict letters disagreed with its table; the Kahoot had no chapter 1 item; four slide diagrams and the cheat sheet's anchor printed small, and the sheet ran to two pages; every item was one shape, with no matching or ordering item; traps arrived after the right answer; the cover numerals did not match the sections; one subtitle promised a chart it did not show; a list of antithesis lines, slogans and fragments; the chapter 1 budget scheduled the TypeError. | One post shape across the brief, notebook and deck, with the keys moved to the day sheet. Every chapter's slide minutes sum to 30 and the section notes follow build then trap. Notebook 05's options follow the table. The Kahoot's Q8 is a chapter 1 item. S1, S4, S5 and S29 were simplified and the cheat sheet fits one page with a wider anchor. Chapter 1 Q2 is an ordering item and chapter 3 Q1 a matching item. Each trap slide's notes stage the wrong number as the colleague's or marketing's figure. The deck wrapper prints the section numerals on the covers. The subtitle and every quoted line were rewritten. The TypeError reads "if it happens". Two points stand: the board's drawing 2 keeps the talk track's part name, "Kalpa's twins", and S5 keeps the shelf above revenue, both because the talk track and the dossier draw them so. |
| 4. Rigor, second run | The same question, asked by a fresh reviewer on the fixed pack. | FAIL. The identity row printed 30 x Rs 25,943 = Rs 7,78,300, which is Rs 10 out; notebook 00's check, Predict and summary still asserted 20 months as the payback while its text called 14 months the refined answer; four items cued their keys (chapter 2 Q4 printed the formula in every option, chapter 4 Q3's key alone said what would change it, chapter 6 Q5's stem echoed the answer, and the lab's diagram labelled each branch's cost); the escalated case claimed returning customers' second orders were the ones cancelled, when 4 of the 9 lost orders are second orders and 5 are first orders. | The identity reads 30 x (Rs 5,44,810 / 21) = Rs 7,78,300 wherever the multiplication is shown, and the board says about. Notebook 00 now asks the question with the marketing note in the stem, keys b, about 14 months, checks round(payback) == 14 and the cautious 20 separately, and the story's summary table reads about 14 months, 20 cautious. The four items were neutralised: bare figures in chapter 2 Q4, a what-would-change-it clause in every chapter 4 Q3 option, a neutral chapter 6 Q5 stem, and branch names alone in the lab diagram. The leak now reads: of the 7 customers who came back, 4 lost that second order to a cancellation or a return, against 5 of the 23 first orders, in the solution, the notebook, the notes and both decks. |
| 5. Pedagogy and language, second run | The same question, asked by a fresh reviewer on the fixed pack. | FAIL. The morning deck still carried a TypeError slide and a self-study delivered-leaves slide, and five transitions named a slide that did not come next; two wrong-answer slides were not staged as a colleague's figure and one trap slide's notes repeated their staging; the afternoon cover listed five of seven sections; a debrief self-study slide duplicated a trainer table and section B's minutes did not sum; chapter 3 Q4, chapter 4 Q5 and escalated Q7 and Q8 printed numbers the escalated case asks for; the notes' chapter 5 had no build paragraph; the cheat sheet's anchor printed small; eight lines read as slogans. | The TypeError's two minutes moved into the first question slide's notes and the delivered leaves into the set slide's notes; both slides were cut and the decks renumbered (morning S1 to S46, afternoon S1 to S32), with the day sheet's ranges following. Every transition names the next slide. Both wrong answers are a colleague's figures and the duplicate staging line is gone. The afternoon sections carry short names, so the cover lists all seven. The debrief table lives only in the day sheet and section B runs 3 and 12. Chapter 3 Q4 and chapter 4 Q5 moved to the not-cancelled definition (26 orders, 21 customers, 5 back; mean Rs 20,606, median Rs 2,100), and escalated Q7a and Q8b no longer print 2 of 19 or 1.11. The notes' chapter 5 gained its build. The anchor is a one-row chain across the band, labels about 9 points, and the sheet stays one page. The eight lines were rewritten as statements with their reason. Minutes on the covers: the rendered covers carry none; the cover notes keep durations as the notes format asks. |

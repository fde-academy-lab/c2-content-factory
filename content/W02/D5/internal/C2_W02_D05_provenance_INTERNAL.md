# Provenance: Week 2, Friday

**INTERNAL.** Where every part of the Friday pack came from, what was verified and when, every
decision that departs from a source, and everything invented. Built on 29 September 2026 in three
50-minute rounds, and raised on 30 September and 1 October 2026 to standard v3: six chapters, each
with its options sized, its best-fit call, its trap and a second route, one notebook per chapter,
every heading a question, every file readable alone, and every prose file through the humanizer's
read.

## Sources, in the order they were read

| Source | What it gave the pack |
|---|---|
| The requester's day prompt, `prompts/week_revamp_W02_W03.md` section 3 with the Week 2 Friday fills, and the resume notice of 1 October 2026 | The three asks as chapters, the sixth chapter on a workbook a director can break, the four traps, the second case as the operating rule defended against a director, LibreOffice-safe formulas, Week 4's traps kept untaught, and the instruction to re-execute every notebook that draws a strip once main's `c2kit.strip` fix (#213) was merged |
| `docs/detailing/W01_W02_spine.md`, Friday's row, the campus day and the afternoon-and-lab table | The case, the five rungs, the four traps, the escalated case, the second case and the lab set |
| `.claude/skills/day-pack-builder/references/the-standard.md` | The bar, the chapter, the question ladder, the volume per family, the depth loop |
| `docs/curriculum/W2_Data_manipulation.md`, the Fri 16 Oct 2026 row, all columns in order | Scenario, thinking, agenda, outcomes, trainer notes, plants, exercises, after-class tasks, interview angle, references and the Kahoot plan |
| `docs/programme/calendar.md` | W02/D5, Fri 16 Oct 2026, teaching, M1, no faculty block; W02/SAT the recap paper; W03/D1 Build 1, the online project introduction |
| `docs/07_Client_Zero.md` (v2.2, with the GCC addendum) | Version v4, the stakeholders (Meera Raghavan, Anand Iyer as finance controller, Kavya Nair), and Build 1's Kalpa Health |
| `data/programme/facts.yaml`, decisions `chapter-standard`, `four-domains`, `question-ladder`, `self-contained`, `humanizer`, `opus-max`, `plants-once-found`, `anand-finance-controller` | The grid, the retail domain linked from Monday's dossier, the forms every file follows |
| `content/W01/D4` on main, raised to standard v3 | The model for the chapter form, the scenario sets, the solutions, the day sheet and this file |
| `content/W03/D1/briefs/C2_W03_D01_briefing_note_STUDENT.md` on main | The pre-read's Build 1 setting: Kalpa Health in six US metros, Q2 against Q3 of 2026, volumes up 5 percent against a plan of 18 |

## Data

Every file in `data/` comes from `data/generate_client_zero.py`; nothing is hand-edited.

| File | How it was written | Read by |
|---|---|---|
| `C2_W02_D05_customer_table_STUDENT.csv`, `C2_W02_D05_raw_export_STUDENT.csv` | The class exports, version v4, as the generator writes them; in the folder since 29 September 2026 and not regenerated | Notebooks 01 to 06, ex1, ex2, the companion page, both workbooks |
| `C2_W02_D05_takehome_customer_table_STUDENT.csv`, `C2_W02_D05_takehome_raw_export_STUDENT.csv` | `demos/C2_W02_D05_build_takehome_data_TRAINER.py`, which loads the generator, sets its seed to 20261016 and calls its own `build_v4` and `_v4_exports`, because the generator has no take-home switch for v4 and a day session may not edit it | The take-home and its self-check, every number of which was recomputed from these files on 1 October 2026 |
| The warehouse | `bash .devcontainer/load_warehouse.sh`, which loads `content/W02/D1/data/C2_W02_D01_warehouse_v4_STUDENT.sql` into Postgres 16 (customers 340, orders 1,000, payments 1,428, refunds 12, campaign_exposure 136, plan_line 13 on 1 October 2026) | Every notebook's second route, both case notebooks |

The six chapter notebooks and the two case notebooks, each case a TODO twin and an executed
solution, are written and executed cold by `demos/C2_W02_D05_build_notebooks_TRAINER.py` (all, or any
by key: c1 to c6, ex1, ex2). On 1 October 2026, after `origin/main` was merged with main's #213 fix
to `scripts/c2kit.py`, all eight were rebuilt and executed cold; the strips in chapters 1 and 3 and in
the escalated case were looked at and draw every dot at its value.

## Plants, and where each is used

| Planted | Where the room meets it | Kept out of |
|---|---|---|
| The raw export at the payment grain: 450 orders on two rows, 400 instalment orders (186 Business, 174 Retail-Plus, 40 Retail-Core) and 50 gateway retries (30 Student, 20 Retail-Core, Rs 37,750) | Chapter 2: notebook 2 sections 2 to 4, morning S28 to S33, the guided sheet's steps 4 to 6, where the totals are blanks the room fills | Every file before chapter 2 states the grain of the customer table only; after chapter 2, files state the rule the room drew, count each order once |
| C-0170 absent from the customer table (Retail-Plus, 6 orders, all in Q2, Rs 21,740, rank 5 if present), so the table sums to Rs 19,83,78,260 and 994 orders | Chapter 3's empty your-turn cell (notebook 3, morning S43); the escalated case's TODO 7, whose check releases on the learner's own comparison; the debrief at afternoon S20; the extras' stretch, whose Q2 list holds C-0170 | Every STUDENT file: no file names the id, prints the table's grand total or its gap, or says which member is missing; the deck pack's Checks tab computes the gap and never the id |
| The approximate match on C-0170 returning C-0169 (rank 50, Rs 8,580) | Said aloud at the debrief only, from the day sheet | Every learner file; the lookup trap is taught on C-0195 returning C-0194 |
| Take-home: C-0172 absent (Retail-Plus, 6 orders, Rs 14,740, rank 20 if present); 311 customers, so ranges sized for Friday's 300 rows miss C-0327 to C-0340 | The take-home's self-check line of 311 customers, 994 orders and Rs 19,83,85,260, which the learner compares with the warehouse | The id is named only in the day sheet |

## Decisions that depart from a source

| Decision | The source says | Why |
|---|---|---|
| The six chapters are the spine's five rungs and a sixth on the workbook a director can break | The spine lists five rungs; the 29 September pack ran three rounds | The day prompt's Friday fill names the sixth chapter; it carries the row's "a director who changes an assumption in the room" and SUM under a filter, the spine's own trap |
| The tree for both quarters is built from the raw export counted once per order | The row: "the chief of staff's three asks are all buildable from the clean export" | The customer table has no quarter, and chapter 1 shows that a split on its last order date puts Rs 17.88 crore in Q2; only the raw export carries order dates |
| The double count is 450 orders, of which 50 are the double-paid retries | The row: "double-counts the fifty double-paid orders" | The raw export has one row per payment, so the 400 instalment orders also appear twice and carry most of the rupees; Remove Duplicates removes the 50 identical copies and leaves the total at Rs 39,40,57,740, which becomes chapter 2's second level |
| The protect list is the top fifty Retail-Plus members by two-quarter revenue | Wednesday's row ranks by Q2 revenue per segment | The customer table carries two-quarter revenue only; the two-quarter list has no tie at fifty (Rs 8,580 against Rs 8,520), so Wednesday's tie rule is referred to; the extras' stretch ranks on Q2 alone, where a tie at Rs 3,350 sits across the boundary |
| The lookup trap is taught on C-0195 | The row: the lookup trap fires on the one absent member | C-0195 is a Retail-Plus member with no orders in the two quarters, so an approximate match returns C-0194 (rank 15, Rs 16,740) on real data without naming the plant; the room's own tie in chapter 3 finds the absent member |
| The front-page number is Q2 revenue against Q1, with the trend and a scope a director picks | The row names "one number on the front page with its trend" and leaves the number open | The growth review asks what moved, and Monday's warehouse numbers are the quarters; which metric belongs on a front page is Week 4's metric design and stays untaught |
| Chapter 5's test case is booked against collected, with a lookup doing the join | The row's chapter 5 is the operating rule | Tuesday's join is the week's one step where one order meets several rows, which is the step a sheet gets wrong most quietly; the spine's traps for Friday do not include it, so it is chapter 5's own trap |
| XLOOKUP is taught; every workbook computes with INDEX and MATCH | The row: "XLOOKUP for find this member" | LibreOffice 24.2.7.2 returns #NAME? for XLOOKUP and `xlsx_recalc.py` proves workbooks there; Microsoft says XLOOKUP is not available in Excel 2016 and 2019, which chapter 3 turns into its version fact |
| The escalated case is the notebook's ten markers in five parts, with a workbook build as the early finishers' stretch | The row's unguided task: the three deliverables in Excel | The standard asks for the escalated case as a TODO twin with its executed solution; the take-home asks for the Excel build from fresh exports |
| The second case runs as the notebook's five markers, a role play and three lines | The 29 September brief added six operating-rule items | The operating rule is chapter 5's set; the second case keeps the director's edit and the defence of the rule, as the spine names it |
| The Kahoot's fifth item calls the tool for five asks in one option string | The row: "warehouse, pandas or Excel for five asks, called fast" | Kahoot answers are single options, so the five calls are one ordered string |
| The deck pack's Checks tab computes the source tie as a formula, so the release reads "Hold the protect list until the customer table reconciles to the warehouse" whenever the workbook is opened, and the companion page carries no member ids beyond the four its lookup answers (C-0152, C-0194, C-0195 and a typed id that is not in the table) | The row's plant list names the absent member as the room's own finding | The deck pack is the escalated case's Excel solution and the trainer opens its Checks tab only from chapter 6, after chapter 3's your-turn tie; neither file prints the absent id, and the companion builder refuses to write a page that contains it, its approximate-match neighbour, the table's grand total or its gap |
| Kalpa's chief of staff, the director and the head of Retail-Plus are unnamed, and the chief of staff takes no pronoun | The row names none of them | Roles only, since no locked source names them |

## Invented, and labelled so wherever it appears

| What | Where |
|---|---|
| Five records short of an invented control total by Rs 1,200, and a two-cell sheet with one figure typed over its formula | Notebook 6, the Checks tab's release; afternoon S13 and S14 |
| Discount tiers at Rs 0, Rs 1,000, Rs 2,500 and Rs 5,000, and an order of Rs 2,700 | Notebook 3's depth section; the chapter 3 set, item 4 |
| Three customers of one invented segment (Rs 9,00,000 once, Rs 3,00,000 once, ten orders of Rs 1,00,000) | The chapter 1 set, item 3 |
| A store's July export (20 single orders worth Rs 50,000, 5 instalment orders of Rs 10,000, 2 gateway orders of Rs 1,500) | The chapter 2 set, items 1 and 2 |
| An app channel's share moving from 20 to 25 percent | The chapter 4 set, item 3 |
| Four orders (Rs 10,000 in two instalments, Rs 6,000 once, Rs 4,000 in two instalments, Rs 2,000 unpaid), and a Monday on which the workbook's Q2 reads Rs 9.79 crore | The chapter 5 set, items 2 and 5 |
| Five rows of Rs 100 to Rs 500, one filtered and one hidden by hand | The chapter 6 set, item 3 |
| An app-channel export by quarter (Q1: six single orders worth Rs 30,000 and two instalment orders of Rs 20,000; Q2: five single orders worth Rs 17,000, one instalment order of Rs 40,000 and one gateway order of Rs 3,000) | The practice lab, problem 3 |
| A regional team's sheet, including C-0888, a Chennai filter, Rs 4.10 crore against Rs 2.05 crore and a segment from Rs 4.00 lakh to Rs 3.20 lakh | The practice lab, problem 4 |
| The app-channel export of the recovery drill (13 rows, 10 orders) | The extras' recovery |
| The director's Rs 5,00,000 | The second case, as the director's stated assumption |
| Eight experiment cards on invented records: A, three orders worth Rs 7,000 on five payment rows; B, three corporate buyers worth Rs 30,00,000 on 12 orders; C, members C-0401 to C-0409 with C-0405 missing; D, a segment falling from Rs 500 to Rs 400; E, three orders booked at Rs 10,000, Rs 20,000 and Rs 6,000; F, eight members worth Rs 60,000, three of them in Mumbai worth Rs 25,500 (C-0501 to C-0508); G, five records worth Rs 11,000 against a control total; H, a two-cell sheet of Rs 500 and Rs 400 | The companion page, each card labelled invented |
| Members C-0401 to C-0409 (C-0405 returning C-0404 under an approximate match), members C-0501 to C-0508 under a Mumbai filter, nine payment rows for six orders, and a collected column that takes the first payment only | The decision tool's Lookup, Director, Quarters and Rule tabs, each labelled invented; its Tree tab reads the real Business rows and its Card tab Retail-Plus's real quarters |

## Links, each with its check date

Every real-world fact in the notebooks was checked by the session that wrote them on 30 September
2026; this session fetched each source again on 1 October 2026 and matched the quote, except where the
row says otherwise.

| Source | Checked | Used for |
|---|---|---|
| Costco, Form 10-K for the fiscal year ended 31 August 2025: https://www.sec.gov/Archives/edgar/data/909832/000090983225000101/cost-20250831.htm | checked 1 October 2026 | Chapter 1: 81.0 million paid members, 38.7 million Executive, "approximately 73.6% of worldwide net sales in 2025" |
| Report of JPMorgan Chase & Co. Management Task Force Regarding 2012 CIO Losses, 16 January 2013, Yale Program on Financial Stability archive: https://ypfsresourcelibrary.blob.core.windows.net/fcic/YPFS/JPMorgan%20Management%20Task%20Force%20Regarding%202012%20CIO%20Losses%201-16-13.pdf | checked 1 October 2026, printed page 128 | Chapter 1's depth: "divided by their sum instead of their average" and "muting volatility by a factor of two" |
| Microsoft Support, Calculate values in a PivotTable: https://support.microsoft.com/en-us/excel/calculate-values-in-a-pivottable | checked 1 October 2026 | Chapter 1's fix: "Formulas for calculated fields operate on the sum of the underlying data for any fields in the formula" |
| Microsoft Support, Create a PivotTable: https://support.microsoft.com/en-us/office/create-a-pivottable-to-analyze-worksheet-data-a9a84538-bfe9-40a9-a8e9-f99134456576 | checked 1 October 2026 | The guided sheet's steps; "any PivotTables that were built on that data source need to be refreshed" |
| Razorpay documentation, About Orders: https://razorpay.com/docs/payments/orders/ | checked 1 October 2026 | Chapter 2: "Combines multiple payment attempts for a single order" |
| Razorpay documentation, Enable Partial Payments (Payment Links): https://razorpay.com/docs/payments/payment-links/partial-payments/ | checked 1 October 2026 | Chapter 2: "Each partial payment would have a unique payment_id, but will be tied to the same order_id" |
| Razorpay API reference, Create an Order: https://razorpay.com/docs/api/orders/create/ | checked 1 October 2026 | Chapter 2's depth: the `attempts` field, "The number of payment attempts, successful and failed, that have been made against this order", and `amount_paid` |
| The Globe and Mail on TransAlta, 4 June 2003: https://www.theglobeandmail.com/report-on-business/human-error-costs-transalta-24-million-on-contract-bids/article18285651/ | checked 1 October 2026 | Chapter 3: "misaligned the rows of information in the spreadsheet"; Steve Snyder's "cut-and-paste error in an Excel spreadsheet" |
| Microsoft Support, VLOOKUP function: https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1 | checked 1 October 2026 | Chapter 3: "If you don't specify anything, the default value will always be TRUE or approximate match"; the first column "needs to be sorted alphabetically or numerically" |
| Microsoft Support, Look up values with VLOOKUP, INDEX, or MATCH: https://support.microsoft.com/en-us/excel/look-up-values-with-vlookup-index-or-match | checked 1 October 2026 | Chapter 3: an approximate match "finds the largest value less than or equal to" the one asked for |
| Microsoft Support, XLOOKUP function: https://support.microsoft.com/en-au/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929 | checked 1 October 2026 | Chapter 3: "XLOOKUP is not available in Excel 2016 and Excel 2019"; the if_not_found argument |
| Avenue Supermarts, press release on results for the quarter ended 30 June 2025, 11 July 2025, as filed with BSE: https://www.bseindia.com/xml-data/corpfiling/AttachHis/a1df88b0-1e3c-4bf7-8336-51eabde7b953.pdf | checked 30 September 2026 by the session that wrote chapter 4; BSE refused this session's fetch on 1 October 2026 | Chapter 4's headline: "Standalone Total Revenue up by 16.2% at Rs.15,932 Crore", against Rs 13,712 crore |
| Avenue Supermarts, investor presentation for the quarter ended 30 June 2025: https://api.dmartindia.com/corporate/content/file/v1/2/n3r8YXSIV43th6Z7M9eaRyiX1752240093/Investor%20Presentation%20for%20the%20year%20ended%2030%20June,%202025.pdf | checked 1 October 2026 | The same two figures, Rs 15,932 crore and Rs 13,712 crore, in the company's own revenue chart |
| GOV.UK, PHE statement on delayed reporting of COVID-19 cases, 4 October 2020: https://www.gov.uk/government/news/phe-statement-on-delayed-reporting-of-covid-19-cases | checked 1 October 2026 | Chapter 5: "15,841 cases between 25 September and 2 October were not included in the reported daily COVID-19 cases" |
| BBC News, 5 October 2020, "Excel: Why using Microsoft's tool caused Covid-19 results to be lost" | checked 30 September 2026 by the session that wrote chapter 5; bbc.co.uk and bbc.com refuse this session's fetch, so no URL is recorded here and the files cite the article by name and date | Chapter 5: templates of "about 65,000 rows"; "about 1,400 cases" per template |
| Microsoft Learn, Work around the Excel 2003 row limitation: https://learn.microsoft.com/en-us/sql/reporting-services/report-builder/work-around-the-excel-2003-row-limitation?view=sql-server-ver17 | checked 1 October 2026 | Chapter 5's depth: "Excel 2003 supports a maximum of 65,536 rows per worksheet" |
| Microsoft Support, SUBTOTAL function: https://support.microsoft.com/en-us/office/subtotal-function-7b027003-f060-4ade-9040-e478765b9939 | checked 1 October 2026 | Chapter 6: SUBTOTAL "ignores any rows that are not included in the result of a filter, no matter which function_num value you use"; 101 to 111 also ignore rows hidden by hand |
| Computerworld on Barclays and Lehman Brothers, 14 October 2008: https://www.computerworld.com/article/1561181/excel-error-leaves-barclays-with-more-lehman-assets-than-it-bargained-for.html | checked 1 October 2026 | Chapter 6: contracts "marked as 'hidden'" added in reformatting; Barclays sought to exclude 179 contracts |
| Exponent, data analyst interview questions: https://www.tryexponent.com/blog/top-data-analyst-interview-questions | checked 1 October 2026 by the notes' builder | Interview calibration, from the row |
| Chandoo on YouTube, Complete Excel Tutorial for Data Analysis in 4 Hours (with FREE Files): https://www.youtube.com/watch?v=7QNgqq154gE | verified 1 October 2026 through YouTube's oEmbed endpoint, which returns the title and the author, Chandoo; the watch page answered with an automated-traffic check and chandoo.org with 403, so the video's chapter list was not read and the notes give its length as the title's four hours | The notes' reading path, the video on pivots and lookups |

## Checked in this session, and not verified in Excel

On LibreOffice 24.2.7.2, 29 September 2026: `SUM` over three rows with one hidden by hand returned 60
and `SUBTOTAL(109)` 40; `_xlfn.XLOOKUP` returned #NAME?; an approximate `VLOOKUP` for a missing
C-0120 among C-0118, C-0119 and C-0121 returned C-0119's value; `COUNTIFS` with a text criterion
compared text. Excel itself was not available, so these are not verified in Excel: the menu names in
the guided sheet beyond the PivotTable page, Excel reading the export's ISO dates as dates, the
`_xlfn.XLOOKUP` cell computing in Excel, and the charts in the deck pack rendering as drawn.

## Tool versions

Python 3.11.15; pandas 3.0.6; openpyxl 3.1.5; python-pptx 1.0.2; nbclient 0.11.0; psycopg2-binary
2.9.13, installed in the session on 1 October 2026 because the notebooks' warehouse route needs it;
PostgreSQL 16, started in the session; LibreOffice 24.2.7.2 with the Carlito font installed in the
session (`fonts-crosextra-carlito`); Playwright with Chromium from `/root/.cache/ms-playwright`;
mermaid-cli 11.17.0, installed in the session's scratch space and put first on `PATH` for the deck and
cheat-sheet builds, because `setup.sh` pins 11 and the container carries 12.0.0.

## The depth loop

Logged at the end of the build.

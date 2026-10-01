# Where did every source, number and decision in the Week 2 Thursday pack come from?

**INTERNAL.** The provenance of `content/W02/D4`, built to standard v3 (decisions `chapter-standard`,
`four-domains`, `question-ladder`, `self-contained`, `humanizer` and `opus-max` in
`data/programme/facts.yaml`) across three sessions on 30 September and 1 October 2026, on branch
`w02-d4-chapters`.

## Which sources was the pack built from, in the ground-truth order?

| Source | What it gave |
|---|---|
| `prompts/week_revamp_W02_W03.md`, section 3, the day prompt with the Week 2 Thursday fills | The six chapters, the four traps, the pandas 3 instruction, the second case as the three-tool re-expression and the tool-choice note, the later-day traps to keep out, and the full grid (not a faculty day) |
| `docs/detailing/W01_W02_spine.md`, approved 29 September 2026 and raised 30 September | The case, the rungs that became chapters, the traps, the afternoon cases and the lab set; the campus day of two 180-minute blocks and the lab |
| `docs/curriculum/W2_Data_manipulation.md`, Thursday 15 October, all columns | The scenario and Kavya's challenge, the thinking, the agenda, the outcomes, the stop-before line, the client-zero plants, the exercises, the interview angle, the references and the Kahoot plan; no IITGN block today |
| `docs/programme/calendar.md` | W02/D4, Thu 15 Oct 2026, teaching, Module 1, no faculty block |
| `docs/07_Client_Zero.md`, v2.2 locked, sections 1a, 1b and 7 | Kalpa, the GCC frame, the stakeholders, data version v4 and its witnesses |
| `.claude/skills/day-pack-builder/references/the-standard.md` on main | The bar, the question ladder, the self-contained rule, the decks in depth, the volume per family and the depth loop |
| `content/W01/D3` and `content/W01/D4` on main | The model for each family's form at standard v3 |
| `content/W01/D1/study-notes/C2_W01_D01_domain_retail_STUDENT.md` | The retail dossier the notebooks point to for GMV, frequency and Retail-Plus |

## Where did the data come from?

| File | How it was made |
|---|---|
| The v4 warehouse, `content/W02/D1/data/C2_W02_D01_warehouse_v4_STUDENT.sql` | Read only, loaded with `bash .devcontainer/load_warehouse.sh` on PostgreSQL 16.14: 1,000 orders, 340 customers, 1,428 payments, 136 exposure rows, 13 plan rows, 12 refunds |
| `data/C2_W02_D04_exposure_STUDENT.csv` | Written by `data/generate_client_zero.py --version v4`; equal to the warehouse's `campaign_exposure` row for row (checked 29 September 2026) |
| `data/C2_W02_D04_takehome_{orders,customers,exposure}_STUDENT.csv` | `internal/C2_W02_D04_build_takehome_data_INTERNAL.py`, which imports the generator, sets `SEED = 20261015` and calls `build_v4()`; nothing in `data/` is edited |
| Every notebook and its saved outputs | `internal/C2_W02_D04_build_notebooks_INTERNAL.py`, executing each notebook cold in its own folder through `scripts/nb_make.py` against the running warehouse; the six chapter notebooks and both case twins were rebuilt on 1 October 2026 |
| The `sql/` files | Written by the same script from the one copy of each query the notebooks run |

## Which plants does the pack use, and how do the student files stay clean?

| Plant | Used in | How the student files stay clean |
|---|---|---|
| 6 repeated customer keys in the exposure feed (C-0001, C-0002, C-0003, C-0006, C-0007, C-0009, re-sent on 11 August), 136 rows for 130 customers | Notebook 02's empty your-turn cell; the escalated case's markers 3 to 5; the day sheet | The fan-out is shown on four invented customers, C-9001 to C-9004, labelled invented; no saved output prints the feed's rows beside its distinct customers, and the escalated case's raw-feed check keeps only the error's kind, since pandas 3.0.6 lists the repeated keys in a `MergeError`'s message (every notebook's saved outputs searched for the ids on 1 October); the exercises use invented feeds (the Diwali email, the app team's push); the notes and solutions restate the rule the room drew, never the keys or the count |
| A customer whose months pivot wrongly by order index (the row's) | Chapter 3, S43 | The generator plants none by name, so the order-indexed pivot is taught on Retail-Plus as a whole |
| Wednesday's three falling Retail-Plus members | The escalated case's falling flag and notebook 06's depth section | The flag runs across all segments and is checked against Wednesday's query as a set; no student file gives a count or an id |
| The take-home snapshot's own repeated feed rows (153 customers, 159 rows) | The take-home | Named only in the day sheet; the self-check gives the numbers to reach and a conditional diagnosis |

## What is invented, and why?

- Customers C-9001 to C-9004 and their spends (Rs 12,400, Rs 8,600, Rs 5,100, Rs 1,900), and the
  companion's reached customers: the fan-out mechanism without naming the plant.
- In the chapter sets: next year's 2 crore orders from 9 lakh listed customers, 6 lakh of them ordering
  (chapter 1); the Diwali email's five customers C-8101 to C-8105, the app team's 2,000-row push feed
  naming 1,900 customers against 12,000 loyalty customers and Rs 5,100 a typical spend, and a combined
  feed carrying a Navratri email beside the monsoon sale (chapter 2); members M1 and M2, a loyalty
  tier's Rs 3,10,000 and Rs 2,90,000 against Rs 8,40,000, and next year's 150 members and 540
  member-months (chapter 3); customers A to E, a dashboard's 96 percent of 1,250 against a feed of
  1,480, and a festive-season SMS that reached 900 customers, 40 of them with no city after a data
  migration (chapter 4); 50 lakh orders and 2 lakh customers, and a hurried note's timings of 0.009,
  0.012 and 0.021 seconds (chapter 5); a store whose data ends 30 June with a run on 13 July, and
  nightly loads from November that fail quietly for two weeks (chapter 6). Every one is labelled
  invented in its file, and none echoes a planted value.
- The run day of Monday 19 October 2026 for recency from the wall clock: the first Monday refresh after
  the session, pinned so the wrong number is exact.
- The escalated case's two broken copies in step 5's check: one customer's id written over another
  customer's row, and recency counted to 21 September 2026; and step 2's table with one reached
  customer removed. Each exists so that only the right letter passes its check.
- The Kahoot's item 6: a left merge of 1,000 customers that returns 1,120 rows; the Kahoot says so
  beside the item.
- The chief of staff's words in the pre-read and on the last slide are Friday's row, quoted.

## Which decisions depart from a source, and why?

| Decision | Why |
|---|---|
| The spine's trap "groupby dropping customers with no segment" is staged where a reach table takes the segment from the order rows | Every customer in the v4 warehouse has a segment, so the trap needs a table where it can be missing; this one leaves 23 reached non-buyers out and gives the trap a business cost, 100 against 82 percent |
| "Last week's flags" are lapsed (60 days to the as-of date) and falling (Wednesday's rule, all segments) | The row names the flags without defining them; these are the week's |
| Spend counts every booked order, all statuses | Monday's warehouse tree and Friday's exported table both sum every order |
| The escalated case's opening gives the data and the growth team's rules and no longer states `validate`, `aggfunc` or the as-of rule | The 30 September build's opening answered six of its markers, the case-opening failure the Week 1 reviews named |
| The escalated case gains marker 5 (a count that shares no code with the merge) and marker 13 (the query step 1 reads at 5 crore orders, checked against step 1), and the second case gains marker 5 (which size tells the routes apart) | The day prompt's lesson 3 asks for design items in both cases |
| Every case check tests the learner's own choice: marker 3 holds the whole call, marker 4's promise is run against the raw feed, marker 5's count is a function rerun on a table that lost a customer, marker 8 chooses the grouping that feeds spend and month alike, markers 11 and 12 face copies only the right guard stops, and the second case's marker 6 is tied to the size chosen in marker 5 | Pass 4 ran all 39 wrong letters of the escalated case and found 13 passing every check, and marker 3 with two right answers; after the change, all 39 and all 18 of the second case's wrong letters fail a check or stop the run (run on 1 October 2026) |
| Chapter 5 states speed as measured: 30 timed runs on 1 October 2026 gave SQL 0.004 s, pandas 0.010 s and plain Python 0.017 s as medians, SQL first in all 30 | Pass 4 timed 30 runs and found the claim that the ranking changes from run to run false; the chapter now says the gap is real and too small to decide a weekly number |
| Chapter 6 reports the data's age beside the table and does not stop on it | The course's warehouse is a fixed extract ending 28 September, so a freshness guard that stopped would stop every run on the course's data; the interview answers carry the production rule, report a stale load before the send |
| Chapter 3's sizing counts the key column as a cell in every shape: long 798, wide 749, the query 749 | Pass 4 found the long table and the query counted their keys while the wide table did not |
| The decks' chapters run 14, 13, 14, 13, 11 and 14 slides | Pass 5 found chapters 1 and 6 over the standard's 10 to 14; two slide pairs merged in each, one predict pair split in chapter 4, and chapter 4 gained its thinking picture |
| The second case's first marker counts members from lists of ids, so each wrong pick gives a plausible wrong rate | The 30 September version's wrong picks raised `AttributeError`, a runtime error in an item slot |
| The guided set is a carve the room mirrors, not a lettered set | The exercise-builder skill keeps a guided carve in its kind |
| The practice lab gives asks an owner among plain Python, SQL and pandas only | Friday's lab sets warehouse, pandas or Excel for eight asks; Excel stays out today |
| The pre-read drops the front-page number's denominator and period, the lookup's not-found framing and the operating rule | Each pre-empts a Friday trap or chapter |
| The study notes run to about 7,300 words of prose, 8,500 with their tables and code, over the standard's 4,000 to 5,000 | The model pack's notes run to 6,900 words of prose and Week 1 Tuesday's to 7,200; each chapter carries its options, sizing, trap and second route, and the interview answers are in full. The depth loop's fixes added about 550 words (the data's age, the guards' two kinds, Week 1's numbers); cutting to the standard's length would drop the second routes or the answers, a call for the requester |
| Chapter 6's item 3 rebuilds the table as of 31 August from the warehouse, whose last August order is dated 28 August | The generator draws order days 1 to 28 (`data/generate_client_zero.py`), so no order falls on 29 to 31 August; option b's smallest recency of 3 rests on that gap, which is the generator's, not a plant |
| The practice lab's problem 4 compares members who bought in Q1: 33 of the 44 reached, 75 percent, against 34 of the 47 others, 72 percent | Pass 4 found the model sentence compared 33 of 60 with 34 of 60, where 13 of the 120 members never ordered and 16 more bought only in Q2, so neither group could spend less in Q2 |
| The cheat sheet drops a numbers panel to fit one landscape page | Every number on it already sat in panels 1, 5 and 7 |
| Twelve interview questions in the notes: the row's five and eight case-style follow-ups, tagged | The standard's ten to twelve plus one |

## Which real companies does each chapter name, and where was each fact checked?

Each fact was first checked on 30 September 2026 and checked again on 1 October 2026 by a research
agent fetching each page; the wording in the pack follows the second check.

| Chapter | Company and fact | Source, as fetched on 1 October 2026 |
|---|---|---|
| 1 | Shopify scores customers 1 to 5 on recency, frequency and monetary value, in 11 RFM groups, one of them Prospects, "Customers with no orders yet"; the sentence quoted in notebook 01 and on S8, "RFM analysis applies a 3-digit score to each customer, where each digit ranges from 1 to 5, and relates to the days from a customer's most recent purchase (recency), the total number of orders (frequency), and the total amount spent (monetary value)", read from the page again on 1 October | https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/customers-reports, "Customers reports" (verified 1 October 2026) |
| 2 | Meta: an advertiser sending events from the Pixel and the Conversions API "must set up a deduplication method"; under the recommended method, the same event ID and event name reaching the same Pixel within 48 hours are deduplicated, the first kept | https://developers.facebook.com/docs/marketing-api/conversions-api/deduplicate-pixel-and-server-events/, "Handling Duplicate Pixel and Conversions API Events"; the check found a second method (external ID or fbp), so "only when" became "under the method Meta recommends" (verified 1 October 2026) |
| 3 | Costco, fourth quarter of fiscal 2026: "traffic or shopping frequency increased 3.3% worldwide", "our average transaction or ticket was up 5.9% worldwide", US and Canada renewal rate 92.3 percent | The call of 24 September 2026, transcript at https://www.theglobeandmail.com/investing/markets/stocks/COST/pressreleases/4846871/costco-cost-q4-2026-earnings-call-transcript/ (a Motley Fool transcript, posted 29 September); the figures in Costco's Exhibit 99.2 to its Form 8-K, https://www.sec.gov/Archives/edgar/data/0000909832/000090983226000084/costex9928-k92426.htm (verified 1 October 2026) |
| 4 | Uber: Operations computed completed trips in Presto/Hive SQL for dashboards while Pricing Engineering built its own from a Cassandra table; the goal, "a strictly ONE to ONE mapping" | https://www.uber.com/blog/umetric/, "The Journey Towards Metric Standardization", 12 January 2021 (verified 1 October 2026) |
| 5 | LinkedIn: "multiple stakeholders come up with different ways to calculate the same metric arriving at slightly different results"; the platform "serves as the single source of truth for all business metrics at Linkedin" | https://engineering.linkedin.com/teams/data/analytics-platform-apps/analytics-platforms/ump, "Unified Metrics Platform (UMP)" (verified 1 October 2026) |
| 6 | Public Health England: "15,841 cases between 25 September and 2 October were not included in the reported daily COVID-19 cases"; the cause, results "automatically fetched in CSV format" stored in the .XLS format "that limited the number of rows to 65,536 per spreadsheet" | https://www.gov.uk/government/news/phe-statement-on-delayed-reporting-of-covid-19-cases (4 October 2020); https://www.theregister.com/2020/10/05/excel_england_coronavirus_contact_error/, 5 October 2020 (verified 1 October 2026) |

## Which links does the pack cite, and when was each checked?

| Link | Check on 1 October 2026 |
|---|---|
| https://pandas.pydata.org/docs/user_guide/10min.html | 200, "10 minutes to pandas, pandas 3.0.6 documentation" (verified 1 October 2026) |
| https://pandas.pydata.org/docs/user_guide/index.html | 200, "User Guide, pandas 3.0.6 documentation" (verified 1 October 2026) |
| https://pandas.pydata.org/docs/user_guide/groupby.html | 200, "Group by: split-apply-combine" (verified 1 October 2026) |
| https://pandas.pydata.org/docs/user_guide/merging.html | 200, "Merge, join, concatenate and compare"; its sections include "Merge types" and "Merge key uniqueness" (verified 1 October 2026) |
| https://pandas.pydata.org/docs/user_guide/reshaping.html | 200, "Reshaping and pivot tables" (verified 1 October 2026) |
| https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html | The `validate` text quoted in the take-home's self-check, read from the pandas 3.0.6 page (verified 1 October 2026) |
| https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html | The sentence on null join keys, "different from usual SQL join behaviour", read from the pandas 3.0.6 page (verified 1 October 2026) |
| https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html | 200, pandas 3.0.6 documentation; the `dropna` text quoted on S56's notes, "NA values together with row/column will be dropped" (verified 1 October 2026) |
| https://pandas.pydata.org/docs/whatsnew/v3.0.0.html | 200, "What's new in 3.0.0 (January 21, 2026)" (verified 1 October 2026) |
| https://pgexercises.com/ | 200, "PostgreSQL Exercises", the row's trainer link (verified 1 October 2026) |
| https://www.youtube.com/watch?v=txMdrV1Ut64 | oEmbed title "Python Pandas Tutorial (Part 8): Grouping and Aggregating - Analyzing and Exploring Your Data", channel Corey Schafer; the watch page redirected to a captcha, so the upload date and the content were not checked, and the take-home says the notebooks are current where a call differs (verified 1 October 2026) |

## Which tool versions did the numbers and outputs come from?

| Tool | Version |
|---|---|
| pandas | 3.0.6. On it, `pivot_table`'s `aggfunc` defaults to the mean, `groupby`'s `dropna` to `True`, `merge`'s `how` to `"inner"` and `validate` to `None`; `validate="one_to_one"` raises `pandas.errors.MergeError`; text reads as `str`; `idxmax(axis=1)` on an all-missing row raises `ValueError: Encountered all NA values` |
| Python | 3.11.15 |
| PostgreSQL | 16.14 |
| SQLAlchemy and psycopg2 | 2.1.1 and 2.9.13, installed in the session |
| nbconvert | 7.17.1 |
| mermaid-cli | 11.17.0, the version `setup.sh` pins, installed in a scratch prefix and put first on the path for the decks and the sheet; the session's own 12.0.0 draws at other sizes |
| LibreOffice with Carlito | 24.2.7.2, with `fonts-crosextra-carlito` installed, for the deck renders |

## How many items does the day carry, and which are design items?

| File | Items | Design items |
|---|---|---|
| Chapter 1 set | 5 | 1, 4, 5 |
| Chapter 2 set | 5 | 3, 5 |
| Chapter 3 set | 5 | 3, 5 |
| Chapter 4 set | 5 | 3, 4, 5 |
| Chapter 5 set | 5 | 1, 2, 4, 5 |
| Chapter 6 set | 5 | 3, 5 |
| Escalated case | 13 | 5, 13 |
| Second case | 6 | 5, 6 |
| The day | 49 | 20, which is 41 percent |

The practice lab adds nine lettered items and two build problems, and the Kahoot eight items.

## What did each pass of the depth loop ask, find and change?

| Pass | Who | What it asked | What it found | What changed |
|---|---|---|---|---|
| 1. Draft | The builder | Is every chapter built from the row, the spine and the dossier, in the chapter order? | The six chapters follow the spine's rungs; the 30 September build left the exercises, notes, sheet, Kahoot, pre-read, take-home and board work at the earlier form | Every family listed rebuilt on 1 October |
| 2. Domain | The builder | Could a learner who has never worked in a business say, per chapter, who asks, why the metric matters, what a wrong number costs and which real company faces it, from the chapter's own files? | Each notebook opens on the four beats; the chapter sets lacked them | Each chapter set and solution now names the stakeholder, the cost of a wrong answer and the chapter's company with its check date |
| 3. Problem first | The builder | Does every technique arrive as the answer to a stated problem, with options, a sizing and the call with what would change it? | The notebooks and decks hold the options tables; the escalated case had no design item and its opening answered its markers | Two design markers added to the escalated case and one to the second case; the opening rewritten |
| 4. Rigor | A fresh reviewer agent, read-only, on 1 October 2026 at 9c1a72f | Do the notebooks run cold; is every number, key and source right; does any check or item pass a wrong answer; does anything teach a later day's trap or name a plant? | No wrong trap number and no plant or later trap in a student file. One blocker: escalated marker 3 had two right answers. Majors: 13 of the escalated case's 39 wrong letters passed every check, and the second case's last check passed any string; chapter 5 said the speed ranking changes from run to run, which 30 timed runs refuted; the recency answers hid the data's age and called every guard independent of the table; 13 of 20 design items were answered in one step; six items were cued; the lab's problem 4 compared counts on the wrong base. Minors on chapter 3's cell counts, chapter 4's rows moved, the int64 wording, GROUP BY rows at scale, NaN keys in a merge, strawmen and error-raising distractors, the take-home's claims and two unrecorded quotes | Marker 3 holds the whole call, and every case check now tests the learner's choice (all 39 and all 18 wrong letters fail, run on 1 October); speed stated as measured; the refresh reports the data's age and the guards are described as two against the warehouse and two on the table's shape, with the control totals read on every call; ten design items rebuilt in changed situations and the cues removed; problem 4 compares Q1 buyers, 33 of 44 against 34 of 47; every minor fixed, the quotes re-read and recorded |
| 5. Pedagogy and language | A fresh reviewer agent, read-only, on 1 October 2026 at 9c1a72f | Does each deck section pair with its notebook; do the headings read as a ladder alone; does each file stand alone; do the decks carry each chapter in full; are the devices varied; is the language the house's? | Half one's .pptx was stale; two notebook charts and four more SVGs clipped; the speed slide's bar argued against its own answer; predicts sat only in speaker notes on six slides; chapters 1 and 6 ran over 14 slides and chapter 4 had no thinking picture; six map slides shared one title and subtitle; labels that did not match their text; humanizer patterns (staged closers, aphorisms, "made loud" six times, bold lead-ins, "It does" openings, fragment stems); the second case brief left terms and tables unnamed; the cheat sheet's foot cut two definitions | Both decks rebuilt and every changed slide rendered and read; every SVG measured inside its frame; every predict on its slide with its answer next; chapters run 14, 13, 14, 13, 11 and 14 slides; map slides name their stakeholder; labels, titles and the language list rewritten across notebooks, decks, notes, solutions and briefs; the brief names the tables and explains its terms; the glossary meanings fit the foot strip |
| 6. Second round, narrow | A fresh reviewer agent, read-only, on 1 October 2026 at ae545a4, because passes 4 and 5 changed keys, methods and repeated numbers | Does each changed key hold, does every wrong letter fail, does any check or stem give a key away, and does any file still state an old number? | One blocker: the escalated solution saved pandas' full `MergeError` text, which lists five of the six repeated feed keys. Majors: two case check cells spelled out keys (the warehouse queries inline, a dtype test, two labels naming the tool), the notes kept 1,000 rows for plain Python, and the second case brief cited Week 1 Tuesday's raw 1.65 to 1.25. Minors: a step 1 gap in the second case, the falling flag's count in a solution, three cues, three defensible distractors, fragment options in the lab, two closers, the lab's old title in the index and a label over the wrong sentence. Its blind letters matched every key; every number recomputed | The raw-feed test keeps only the error's kind; the step 3 check reads chapter 6's queries from `sql/`, step 1 checks that every frequency is present and adds to the orders, and the second case's labels name no tool; the notes say 1,340; the brief cites the clean file's 1.449 to 1.246 and Retail-Plus's 1.82 to 1.18; the cues, distractors, lab options, closers, title and label fixed. Kept, with reasons: the Kahoot's options stay short clauses, since Kahoot caps an answer at 75 characters; the second case's misspelt label stays as 3b, since it runs and returns no rows, which the row-count check catches |

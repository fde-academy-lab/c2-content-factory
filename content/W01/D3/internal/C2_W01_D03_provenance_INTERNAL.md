# Provenance: Week 1 Day 3

INTERNAL. Where every number, decision and link in the Wednesday pack came from. Built on
29 September 2026 to the round standard, raised on 30 September 2026 to the chapter standard in
`.claude/skills/day-pack-builder/references/the-standard.md` (decisions `chapter-standard` and
`four-domains` in `data/programme/facts.yaml`), merged in pull request 196, and rechecked the same day
to standard v3 (decisions `question-ladder`, `self-contained`, `humanizer` and `opus-max`) from the
recheck prompt in `prompts/week_revamp_W02_W03.md`, section 1, on branch `w01-d3-v3`.

## The sources

| Source | What it fixed |
|---|---|
| `docs/detailing/W01_W02_spine.md`, approved 29 September 2026, raised 30 September 2026 | The case, the rungs that became the chapters, the four spine traps, the afternoon cases and the lab set |
| `docs/curriculum/W1_Data_analysis_found.md`, the Wednesday row | Scenario, thinking, outcomes, plants, interview anchors, references, Kahoot plan |
| `docs/07_Client_Zero.md`, v2.2, section 7 | Data version v2 and its witnesses |
| `docs/programme/calendar.md` | Wed 07 Oct 2026, W01/D3, teaching, module M1, no faculty block |
| `content/W01/D1/study-notes/C2_W01_D01_domain_retail_STUDENT.md` on branch `w01-domain-retail`, read with `git show` on 30 September 2026 | The domain story the pack links to; Anand's row in the org chart; GMV, every order at the price charged before cancellations and returns come out, which is what both of Anand's figures count |
| `content/W01/D2/trainer/C2_W01_D02_day_sheet_TRAINER.md` | Tuesday's reported numbers: Retail-Plus 2.32 to 1.18, down 49.0 percent; the tree as Tuesday read it, customers x1.000, orders per customer 1.65 to 1.25 (x0.754), revenue per order x1.180, revenue x0.890 |
| `.claude/skills/day-pack-builder/references/the-standard.md`, standard v3 of 30 September 2026 | The question ladder, every artifact standing on its own, decks carrying each chapter in full, and the humanizer's read on every prose file |
| `prompts/week_revamp_W02_W03.md`, section 1, with the orchestrating session's fills | The recheck's five steps, the later days' traps to keep out, and three specifics: the review's two rulings stay with every file explaining its own terms, the notes do not grow past about 6,650 words, and the recomputed tree's numbers stay exactly as merged |
| `.claude/skills/humanizer/SKILL.md` (blader/humanizer at 225a6f3, MIT) | The read in file mode over every prose file |

## The data

```
python3 data/generate_client_zero.py --version v2 --out content/W01/D3/data --stem C2_W01_D03
```

Rerun on 30 September 2026 into a scratch folder; all four files came out byte-identical to the
committed ones. The CSV holds 201 rows (the contract's 200 plus the near-duplicate), the JSON feed the
first 120 rows cut inside the 120th record, the vendor copy the header twice and the first 39 data
rows, and the take-home file the v2b sample.

## The chapters, and where each came from

| Chapter, as its opener asks it | Notebook | Deck | The spine's rung |
|---|---|---|---|
| 1. What did the ERP send? | `01_profile` | Half one, SECTION 1, S7 to S21 | The profile |
| 2. Which rows repeat? | `02_duplicates` | Half one, SECTION 2, S22 to S34 | The migration's duplicates |
| 3. Which copy stays? | `03_identity_rule` | Half one, SECTION 3, S35 to S48 | The identity rule |
| 4. Drop, fill or flag? | `04_missing_malformed` | Half one, SECTION 4, S49 to S63 | Missing and malformed values |
| 5. Can we prove the 1.9? | `05_bridge` | Half one, SECTION 5, S64 to S78 | The revenue bridge with Tuesday recomputed |
| 6. Can the analyst replay it? | `06_audit_logs` | Half two, SECTION 6, S2 to S15 | The sixth chapter the brief names: the rejects and decisions logs Anand's analyst audits |

The full questions, who needs each answer and the six smaller questions per chapter are printed at
the top of the day sheet, and every family carries them word for word.

## The plants, and where each is used

| Plant | Student files meet it as | Named only in |
|---|---|---|
| 14 duplicated Q1 rows | Aggregate counts and rupees (186 of 201, 14 in Q1, Rs 19,98,210); the rows found in empty cells | Day sheet |
| The amount `twelve` | "One amount does not convert"; the error read live in an empty cell; its effect as Rs 1,790 in chapters 3, 4 and 6 | Day sheet, lab note |
| The missing status | "Status present on 200"; the decision sized in totals | Day sheet |
| The near-duplicate pair | Invented pairs INV-11 to INV-13 for the mechanism; its effect as "Q2 Rs 3,710 high" in chapter 3's trap; the real pair found in an empty cell | Day sheet |
| The truncated JSON line | The error read live in an empty cell; 119 records recovered | Day sheet, lab note |
| The duplicated header | "40 rows, 39 convert, three segments"; found in an empty cell | Lab note |

The Rs 1,790 and Rs 3,710 appear in STUDENT files as the size of a wrong pass, never beside the order
or its line. The existing 29 September build already showed Rs 1,790 this way.

## Decisions that depart from a source, and why

1. **Chapters 1 and 3 carry traps the spine does not list.** The standard asks for a trap in every
   chapter and the spine names four. Chapter 1's is the text sort that names Rs 970 as the largest Q2
   order (the row's "everything read is text", made into a wrong number). Chapter 3's is the whole
   record less the line, which ties Q1 to the books while keeping 188 rows for 186 orders and Q2
   Rs 3,710 high.
2. **The coerce-to-zero trap moved from the profile to chapter 4**, where the brief puts coerce,
   reject or repair. Its wrong number is now the whole pass: 201 of 201 convert, 0 rejects, and after
   the first-copy dedupe Q1 Rs 1,89,98,210 with an order at Rs 0.
3. **The whole-record trap still reports zero because the file line is in the key.** On the v2 file a
   plain whole-record dedupe finds 13 exact copies, not zero; zero arises honestly because chapter 1's
   rejects log attaches each row's file line. The 13 is shown in chapter 2's options table.
4. **"Counts reconcile while rupees do not" is chapter 6's colleague**, dedupe first keeping the first
   copy, then convert: 201 = 185 + 16, Rs 20,00,000 set aside, Q1 Rs 1,89,98,210. The spine ties it to
   the bridge rung; it sits with the logs because the analyst's audit is where a row-only
   reconciliation fails.
5. **The bulk order is Q2's largest order, KR-02186 at Rs 29,45,460**, as in the 29 September build.
   v2 lists no bulk-order plant; the spine added this trap. It sits in chapter 5 with Tuesday's
   recompute, since removing it is what turns 1.6 percent into 17.1.
6. **Anand's books are Rs 1,90,00,000 to the rupee**, the generator's `Q1_CLEAN`. The row quotes "1.9".
7. **Revenue is booked value, every status, which the retail dossier calls GMV.** Both 2.1 and 1.9
   total all statuses in the generator's contract. By the orchestrating session's ruling of
   30 September 2026, the notes and the day sheet say once that booked value is the dossier's GMV,
   every order at the price charged before cancellations and returns come out, and that the export
   does not state whether GST is inside, a question an analyst asks Anand. Nothing more is said about
   GST, since the client-zero lock is silent on it. S1's notes no longer claim that Monday set the
   definition.
8. **Percentages are from unrounded ratios.** Retail-Plus falls 35.0 percent (26/22 against 40/22);
   Tuesday's -49.0 percent is quoted from Tuesday's day sheet, since Tuesday ran on v1.
9. **The afternoon deck's chapter opener shows 06.** Main's deck builder now prints the number each
   `## SECTION n:` heading carries, so chapter 6 opens the afternoon deck as 06, and the notes no
   longer explain an 01.
10. **Chapter titles are statements.** `scripts/deck_md_check.py` reads a SECTION title ending in a
    question mark as a question slide, so the six titles drop the mark in the decks and notebooks alike.
11. **The study notes run to about 6,650 words, about 5,550 outside the tables,** against the
    standard's 4,000 to 5,000, because six chapters as worked cases with options and sizing, the
    recomputed tree and twelve full interview answers do not fit the lower figure without cutting
    what the standard requires.
12. **The practice lab's "second export with new defects" is the vendor copy**, since the take-home
    file is the second sample the standard assigns to the take-home.
14. **The cut-first list departs from the row.** The row cuts `json.dump`, then the outlier fence. The
    day sheet cuts `json.dump`, then the JSON feed in chapter 1, because the outlier fence is chapter
    5's trap, the bulk order removed as an outlier, which the spine added, and cutting it would leave
    chapter 5 without its trap; the feed's point returns in chapter 4's repair and chapter 5's options,
    so chapter 1 loses the least by dropping it.
15. **One shape for the final pass.** Every file states the pass as notebook 06's `clean_pass()` runs
    it: the identity rule first, keeping the copy whose amount converts (the first when both do), then
    conversion with a rejects log, which is empty on this export because the one unreadable amount is a
    copy, set aside with its twin named. Rows: 201 = 186 + 15. Chapter 1's rejects log of one is the
    profile's log on the raw export, before the rule.
16. **The day carries 40 lettered items, 20 of them design,** against the standard's about 35 and a
    third: six chapter sets of four or five, the escalated brief's ten and the second case's five. The
    lab's eleven and the Kahoot's eight are counted apart. A design item passes the house test: the
    learner combines two ideas or takes several dependent steps, and nothing else in the pack answers it.
17. **One set of twelve interview questions** runs through the notes, the day sheet, the drill and the
    notebooks: the row's five, two follow-ups (row counts reconcile; the largest order) and five design
    questions, one for each of chapters 1 to 5. Dropped from the earlier fifteen: a dedupe that returns
    zero, a JSON file that fails to parse, cleaning a file never seen, cleaning shrinking yesterday's
    finding, and whose number is right; chapter 6's design question on the log's contents folded into
    the auditor answer.
18. **The escalated case escalates.** The learner writes the identity rule's key and survivor line and
    recomputes Monday's tree, and every TODO is code whose check recomputes the step by a second route;
    D13 no longer prints the case's answers.
19. **Files replaced.** The three round notebooks became six chapter notebooks
    (`03_bridge` removed; `03_identity_rule`, `04_missing_malformed`, `05_bridge`, `06_audit_logs`
    added); `hands_on` and its solution became `ex1_escalated_case`; the three round sets and their
    solutions became six chapter sets. All removals by `git rm`.

## Invented, and recorded as invented

- Every record in the mechanism cells: INV-01 to INV-03 (chapter 2; INV-01 moved from Rs 2,400 to
  Rs 2,500 so no class number echoes the take-home's refund), INV-11 to INV-13 (chapter 3), INV-21
  (chapter 4); the amount `" 950"` in notebook 01's Depth, which replaced the take-home's `"-2400"`;
  the companion's four experiments, whose experiment A moved its first amount from Rs 2,400 to
  Rs 2,500 for the same reason; the decision workbook; the recovery extra.
- Every number in the chapter sets, the case briefs' distractors, the lab's problem 1 and the Kahoot,
  except where an item says it is the day's: among them the 1.2 crore and 4 crore row exports, 20 lakh
  values and 50 lakh pairs a minute, 100 bytes an id and 2 GB free, the two apps' 30,000 customers in 6
  cities, the fuzzy key's 40, 38 and 36 rows, the May re-run, the 1,800 orders without a status and 2
  minutes a lookup, the Q3 warehouse record, the 312 ids two systems share, the paise and separator
  formats, and the 900-row hand-over at 30 seconds a line.
- The minutes in the sizing tables: half a second a cell, half a minute a row tied out, 30 seconds a
  log line. Each is labelled illustrative where it appears.
- The auditor as a person; the section 1a table names no auditor, so the role is unnamed.
- The companion's simulator holds no records; its outcomes are totals computed from the v2 export by
  `internal/C2_W01_D03_companion_totals_INTERNAL.py` and embedded as numbers.

## Real companies, each fact with its source

Every page below was fetched on 30 September 2026 by a research agent in this session, and the
figures used are the ones it confirmed.

| Chapter | Fact used | Source |
|---|---|---|
| 1 | Target Canada launched March 2013, lost almost $1 billion in year one, and announced on 15 January 2015 it would close all 133 stores | https://www.cbc.ca/news/business/target-closes-all-133-stores-in-canada-gets-creditor-protection-1.2901618 (checked 30 Sep 2026) |
| 1 | Product data about 30 percent accurate against 98 to 99 percent in the US, attributed to Castaldo's Canadian Business article | https://www.salsify.com/blog/product-content-lesson-target-canada-collapse-taught-us (checked 30 Sep 2026; a secondary summary, since the Canadian Business page returned 403) |
| 2 | Starbucks billed some card customers twice on 22 and 23 May 2009, at about 7,800 company-owned stores in the US and Canada, and repaid about one million customers | https://www.nbcnews.com/id/wbna31208561 (checked 30 Sep 2026) |
| 3 | The IRP rejects an invoice already reported under the same supplier GSTIN, invoice number, document type and financial year, the combination also used to generate the IRN, a 64-character hash (FAQ questions 64 and 65) | https://www.gstn.org.in/assets/mainDashboard/Pdf/GST%20e-invoice%20System%20-%20FAQs%20-%20Version%201.4%20Dt.%2030-3-2021.pdf (checked 30 Sep 2026, and again in the fix pass the same day) |
| 3 | E-invoicing covers supplies to registered persons (B2B), SEZ supplies and exports, never B2C (FAQ questions 9 and 10); exempt: SEZ units, insurers, banks and NBFCs, goods transport agencies, passenger transport, multiplex cinemas and OIDAR (FAQ question 17) | The same FAQ PDF (checked 30 Sep 2026 in the fix pass) |
| 3 | Notification 10/2023-Central Tax of 10 May 2023 moves the threshold in notification 13/2020 from Rs 10 crore to Rs 5 crore of aggregate turnover from 1 August 2023 | https://www.gstcouncil.gov.in/node/4365 and its English PDF, https://www.gstcouncil.gov.in/sites/default/files/2024-05/10ct_eng.pdf (both checked 30 Sep 2026 in the fix pass) |
| 4 | A glitch in the repricing tool Repricer Express set hundreds of items on Amazon to 1p between 19:00 and 20:00 GMT on Friday 12 December 2014; the orders were placed on Amazon's Marketplace, "which allows third-party companies to trade on Amazon", and the firms affected used the tool; Amazon said most orders were cancelled | https://www.bbc.co.uk/news/uk-northern-ireland-foyle-west-30475542 (checked 30 Sep 2026, and again in the fix pass for the third-party sellers) |
| 5 | Tesco overstated half-year profit guidance by about GBP 250 million, "principally due to the accelerated recognition of commercial income and delayed accrual of costs"; the chief executive said expected revenue from suppliers had been "reported in the wrong time period", 22 September 2014 | https://www.bbc.co.uk/news/business-29306444 (checked 30 Sep 2026, and again in the fix pass for the supplier income wording) |
| 5 | Confirmed as GBP 263 million: GBP 118 million first half, about GBP 70 million 2013/14, about GBP 75 million before | https://www.tescoplc.com/media/hm2hnfbe/interim_2014-15_results_statement.pdf (checked 30 Sep 2026) |
| 6 | Patisserie Valerie's hole put at GBP 94 million, March 2019 | https://www.bbc.co.uk/news/business-47591082 (checked 30 Sep 2026) |
| 6 | FRC fined the auditor GBP 4 million, reduced to GBP 2.34 million, for three years of audits, 27 September 2021 | https://www.frc.org.uk/news-and-events/news/2021/09/sanctions-against-grant-thornton-uk-llp-and-david-newstead/ (checked 30 Sep 2026) |

Left out as unverified: a count of Amazon items or sellers affected; Target Canada's total loss
beyond CBC's figures; any retailer's own statement on deduplicating by order id; any statement about
Patisserie Valerie's criminal proceedings, since none was sourced, so S2's notes say only to name no
person. No verified public case was found of an export stitched from two extracts inflating reported
sales, so chapter 2 uses the Starbucks double charge and says what it is.

## Links, each with the date it was checked

| Link | Checked | Where used |
|---|---|---|
| https://docs.python.org/3/library/json.html | checked 30 Sep 2026, page title confirmed | Study notes |
| https://automatetheboringstuff.com/3e/ | checked 30 Sep 2026, page title confirmed | Study notes |
| https://www.youtube.com/watch?v=9N6a-VLBa2I | checked 30 Sep 2026, title confirmed by oEmbed | Study notes |
| https://www.youtube.com/watch?v=q5uM4VKywbA | checked 30 Sep 2026, title confirmed by oEmbed | The row's trainer resource |
| https://realpython.com/python-csv/ | verified 03 Sep 2026 per the row; the 30 Sep fetch met a Cloudflare check | Study notes, take-home |
| https://realpython.com/python-lbyl-vs-eafp/ | verified 03 Sep 2026 per the row; the 30 Sep fetch met a Cloudflare check | Study notes, notebook 01 |

## How the files were built, and the tool versions

| Family | Command |
|---|---|
| Notebooks | `python3 content/W01/D3/internal/C2_W01_D03_build_notebooks_INTERNAL.py` |
| Chapter sets | `python3 content/W01/D3/internal/C2_W01_D03_build_sets_INTERNAL.py` |
| Decks | `python3 scripts/build_deck.py <md> --footer "Week 1 Day 3: which Q1 figure is right"`, rendered with `soffice --headless --convert-to pdf` and read slide by slide |
| Companion | The page, then `python3 scripts/build_companion.py`; the simulator totals from `internal/C2_W01_D03_companion_totals_INTERNAL.py` |
| Workbook | `python3 content/W01/D3/demos/C2_W01_D03_build_decision_tool_TRAINER.py` |
| Cheat sheet | `python3 scripts/build_cheatsheet.py <md> --verified "30 Sep 2026"` |

Python 3.11.15, nbclient 0.11.0, nbformat 5.11.1, IPython 9.17.1, openpyxl 3.1.5, python-pptx 1.0.2,
LibreOffice 24.2.7.2, Chromium 141.0.7390.37, mermaid-cli 12.0.0, with fonts-crosextra-carlito
installed in this session.

## The depth loop

| Pass | Who | What it asked | What it found | What changed |
|---|---|---|---|---|
| 1. Draft | The builder | Is every chapter built from the row, the spine and the dossier, in the chapter order? | Six chapters from the spine's five rungs and the brief's sixth; each notebook and deck section runs need, company, options, build, trap, fix, second route, review. The dossier landed mid-session and was linked, never copied. | Chapter titles made statements so the deck gate does not read them as questions; two titles shortened so the section openers do not wrap |
| 2. Domain | The builder | Could a learner who has never worked in a business say who asks, why the metric matters, what a wrong number costs and which real company faces it? | The need slides for chapters 2, 3 and 4 named who asks and the metric but not the cost of a wrong number | A "What breaks" line with the cost in rupees or customers added to S18, S27 and S38 |
| 3. Problem first | The builder | Does every technique arrive as the answer to a stated problem, with options, sizing and the call? | Chapter 1's first sizing chart plotted an assumed score, not a measure | Replaced by the values each option reads, computed from the file |
| 4. Rigor, round 1 | A fresh reviewer agent | Cold runs, exact wrong numbers, sizing arithmetic, sources, interview answers | FAIL. Pair count on 2 crore rows off by 100 times; the "fuzzy key" was an exact composite key priced as all pairs; the sampling chance measured drawing one copy, which cannot reveal a repeat; the missing-data answer contradicted chapter 4; lab Q7 ambiguous; "twelve" in a STUDENT notebook's word table; openers rendering as code; Target wording overreached; smaller items (wording of "second copies", ch6 Q3 order, two distractor rationales, cheat sheet drop row, GBP glyph, empty loop log) | Option d is now a true fuzzy match (same customer and amount within 60 days) compared pairwise, 20,100 pairs, same 15 rows; 200 lakh crore; sampling restated as 13 percent to draw both copies of a pair; the answer rewritten; lab stems pinned to the file line; "twelve" removed; opener dedented; Target wording to "announced it would close"; every smaller item fixed; the Tuesday Rs 1,790 difference explained in the day sheet |
| 5. Pedagogy and language, round 1 | A fresh reviewer agent | Chapter pairing, device variety, print legibility, tics | FAIL. Openers as code; ch1 Q4 and ch4 Q3 tested runtime behaviour; chapter 6 drawn as 01; briefs all one device; chapter 2's trap slides used question labels; chapter 5's fix had no slide; control totals, fence, GSTIN and booked value used before defined; cheat sheet panel one labels across arrows; S35 line over categories; minutes drifting; notebooks 05 and 06 missing Depth and predictions; meta lines on slides; "Kavya's review" on options slides | Both items replaced (match the question to the method; fix the logic); escalated brief Q4, Q7 and Q9 now fix the logic, design and match; S21 and S22 relabelled; S56 carries the fix; the four terms defined at first use and added to the glossary; panel one reshaped; S35 a table; minutes balanced to 30 per chapter; Depth and predictions added; meta lines removed; options slides close on "The call". Chapter 6's numeral 01 stands, since the fix is in shared `scripts/build_deck.py`, and is raised in the report |
| 4. Rigor, round 2 | A fresh reviewer agent | The same question, with round one's findings to confirm | FAIL, narrowly. Every number recomputed and every notebook cold-run clean; left: the notes still said Target Canada opened 133 stores in 2013 (it opened about 124 then), the day sheet and provenance said the stores closed in January 2015, and notebook 04 cited Week 5 imputation, which the tracker does not carry. Minor: the 387-line hand-over unexplained, the lab intro matched by order id, a brief item mislabelled as a match, thin scope in three interview answers, a cheat sheet run-on | All wording now says "launched in March 2013 ... announced in January 2015 it would close all 133"; the Week 5 reference replaced by what imputation is for; the hand-over read "against the raw", the diff ties rupees "by hand"; the lab pinned to the file line; Q9 relabelled; imputation, model-side outlier treatment and blocking sized in the answers; the sheet's sentence fixed |
| 5. Pedagogy and language, round 2 | A fresh reviewer agent | The same question, with round one's findings to confirm | FAIL on one item: the new chapter 4 fix-the-logic item named the take-home's planted refund. Should fix: S56 text-only; S40 sized one decision; the sheet's glossary cut and missing fence; the escalated Q4 key longest; double numerals in the notebooks' ladders. Minor: design tags on three predict or match items, keys leaning to c, "Kavya's review" off its beat on three slides, clumsy subtitles, one minute over in the ask | The item now uses an invented refund of -1150; S56 carries the fix in stats; S40 carries both tables; the glossary reordered so fence and control totals print; keys and distractors rebalanced on Q4 and two slide questions; ladders fixed; tags now honest (17 design of 47 items, 36 percent); ch6 Q2's key moved to a; "The call" and "The rule" replace off-beat reviews; subtitles rewritten; S3 trimmed to 4 minutes |
| 4. Rigor, round 3 | A fresh reviewer agent | The same question, targeted at round two's items | Every gate question held: cold runs identical, every edited slide's numbers recomputed, sources rechecked live (Starbucks, FRC, Tesco), no plant named. Should fix: the amount's "what would switch it" named a fact that switches nothing; the bulk order was "kept and flagged" in the decisions and the note but absent from the flags log. Minor: the notes' outlier answer lacked the model side; "two rows can carry more than a hundred" was unclear; blocking's recall cost unstated; company wording beyond the provenance table (Starbucks company-owned, Tesco's cause, Amazon's repricing tool, the IRN hash); S8's and S49's titles and the Tesco Depth line interpretive | The switch fact now names an independent source that turns the reject into a repair; `clean_pass()` flags the bulk order, so the hand-over is 24 lines; the answers carry the model-side treatment, the Rs 19,67,560 of Rs 19,98,210, and the recall cost of blocking; the table carries every company fact the pages use; S8 retitled "Target Canada's new system ran on bad data", S49 "Tesco's gap grew from GBP 250m to 263m", the Amazon line and the Tesco Depth line reworded to what the sources say. No finding left open, so the loop closes here |
| 5. Pedagogy and language, round 3 | A fresh reviewer agent | The same question, targeted at round two's items | PASS. Should fix: the glossary still cut the fence entry; the S40 switch fact read the wrong way round. Minor: the escalated Q4 missed by the shared audit script; half2 S17's key the longest option; S40's two tables at different sizes; notebook 05's ladder subtitle; the non-chapter sets carry no kind tags; chapter 4's logic item rehearsed the take-home's defect type | Fence shortened so the glossary prints whole; the switch fact rewritten in the deck, notebook 04, the notes and the day sheet; S17's options rebalanced; the ladder subtitle reads "Rs 2.1 crore to Rs 1.9 crore"; chapter 4's item now uses a thousands separator. S40's table sizes are set by `scripts/deck_layout.py` and stand; the brief tags are left as the brief's own format |

## The orchestrating session's review, 30 September 2026

The orchestrating session held the pack on four blocking findings and eight should-fix findings and
ruled on two questions. This pass fixed every finding; nothing was left open.

### The rulings

1. **The definition of revenue.** Both of Anand's figures are booked value across every order status.
   The notes and the day sheet say once that booked value is what the retail dossier calls GMV, every
   order at the price charged before cancellations and returns come out, and that the export does not
   state whether GST is inside, a question an analyst asks Anand. S1's notes lose the claim that
   Monday set the definition (decision 7).
2. **Jargon.** ERP, tie out, extract, migration and Tesco's supplier income are each explained in one
   clause where they first appear in each STUDENT family: the decks (S1 and S49), the notebooks
   (notebook 01's need and notebook 05's company), the exercises (the index, the chapter 1 and 3 sets,
   both case briefs and the lab), the reading (the notes' opening and chapter 5, with rows at the foot
   of the glossary), the take-home brief and the companion.

### What the review found, and what changed

| Finding | What changed |
|---|---|
| B1. The pre-read spent Thursday's small-base trap on Thursday's own segment | Tonight's check is the delivered share by quarter over orders with a status, 67 of 100 and 57 of 85; the vocabulary row points at a field, never a segment |
| B2. Week 2 Tuesday's fan-out was taught in three STUDENT files | Deleted from D24's notes, the notes' "where this shows up" (now an audits bullet) and notebook 02's Depth; the .pptx rebuilt |
| B3. Notebook 01's Depth named the take-home's refund | An invented `" 950"` with a stray space, which isdigit refuses and int() reads; INV-01 moved off Rs 2,400 as well |
| B4. Chapter 6's Q3 key contradicted notebook 06, and the pass had two shapes | Q3 re-keyed to notebook 06's order; every file states the one shape (decision 15); the escalated twin no longer logs the unreadable row twice, and the auditor solution says the rejects log is empty |
| S1. Two stories about the JSON feed | One sentence everywhere: it witnesses what the extract held, never whether a value is right (notebooks 01 and 04, S16, S45, the notes, the escalated Q2, the chapter 4 set, the lab's Problem 3 and Q8, the TA note) |
| S2. Design items mislabelled, and too few of them | 40 items, 20 design by the house test (decision 16), each with a one-line case in the session report |
| S3. Every item answerable cold | Distractors rewritten as the answers a hurried analyst gives; no key leads with a chapter's slogan; across the 59 lettered and Kahoot items no key is the lone longest or lone shortest option, keys sitting tied at the top in 16 and tied at the bottom in 8; the set builder refuses a lone extreme |
| S4. Leaks and cues between items | The lab's intro and Q6, Q8, Q10 and Q11 no longer answer other items; the auditor brief asks five new questions; both TODO twins carry code options only, each check recomputing its step another way, including ex2's TODOs 3 and 5; ch1 Q1 and ex1 TODO 1 are business questions; chapter 5 tests the bulk order once |
| S5. Token second routes in chapters 1, 2 and 4 | Chapter 1: sorted ids counted at each change, and a digit pattern with no int(); chapter 2: every row against every later row; chapter 4: counts read from the flags, rejects and discount logs; chapter 6's replay from disk kept |
| S6. The escalated case did not escalate, and the tree was never recomputed | The learner writes the rule's key and survivor line and the tree's customers branch and multiples; the tree, x1.000, x0.860, x1.144 and x0.984 against Tuesday's x1.000, x0.754, x1.180 and x0.890, is in notebook 05, S53, the notes, the board work, the cheat sheet and the escalated case |
| S7. Weak switch facts in chapters 1 and 5 | Chapter 1 switches on a profile too slow for the deadline, chapter 5 on a second source independent of the export and complete for the quarter, each as the chapter's own interview answer names it, in the notebook, the slide, the notes and the day sheet |
| S8. Minor | S17 rebalanced; "at the end of the file" and "twin carries the value" left to their your-turn cells; chapter 4's and 6's traps, D13, S14 and the cheat sheet show 186 orders, Rs 20,00,000 set aside or Q1 rounding to 1.90 crore where four places showed Rs 1,89,98,210; S20 and the notes no longer size chapter 3's trap; the 13 percent and ch1 Q6 cut; one set of twelve interview questions (decision 17); S39, the e-invoice scope and the Business segment's direction corrected to their sources; the conviction line removed; the take-home says three defects are today's kinds and two are new; the cut-first departure recorded (decision 14); notebook 04 computes the imputed status from the customer's earlier order |

Kept as the review asked: notebook 02's four keys, each sized on this file, and "same count, other
rows"; chapter 3's trap paired with chapter 6's; notebook 05's bulk-order trap and its note to Finance;
chapter 6's replay; the S14 and S15 debrief, whose chapter 6 row now shows that trap's own headline;
and the day sheet's tables. Also corrected on the way: the companion's glossary, which pointed at the
slides and sections of an earlier build and defined the rejects log as the set-aside log.

### The proofs

- Every wrong option of every TODO in both case twins was run against the checks and fails at least
  one; every keyed option passes with no error.
- `scripts/distractor_audit.py` passes on all ten option files, and a stricter pass over the same items
  finds no key at a lone length extreme.
- Every changed notebook was executed cold by `scripts/nb_make.py`; both decks rebuilt with
  `scripts/build_deck.py`, rendered through LibreOffice with Carlito installed and read slide by slide
  on every changed slide; the cheat sheet PDF rebuilt; the companion swept in Chromium.
- Every STUDENT file, markdown, notebook sources and outputs, the companion page and the built decks
  with their notes, was searched for Thursday's and Week 2's trap mechanisms, every take-home plant
  and today's plant words, with no hit; the take-home self-check lists its own target numbers by
  design. The word "twelve" left the notes and the afternoon deck, where it had counted questions and
  minutes.
- `python3 scripts/verify.py content/W01/D3 --execute`, `python3 scripts/build_companion.py
  content/W01/D3 --check` and `python3 scripts/sync_programme.py --check` pass; their output is in the
  session report.


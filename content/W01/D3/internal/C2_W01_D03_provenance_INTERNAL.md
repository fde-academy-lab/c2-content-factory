# Provenance: Week 1 Day 3

INTERNAL. Where every number, decision and link in the Wednesday pack came from. Built on
29 September 2026 to the round standard and raised on 30 September 2026 to the chapter standard in
`.claude/skills/day-pack-builder/references/the-standard.md` (decisions `chapter-standard` and
`four-domains` in `data/programme/facts.yaml`).

## The sources

| Source | What it fixed |
|---|---|
| `docs/detailing/W01_W02_spine.md`, approved 29 September 2026, raised 30 September 2026 | The case, the rungs that became the chapters, the four spine traps, the afternoon cases and the lab set |
| `docs/curriculum/W1_Data_analysis_found.md`, the Wednesday row | Scenario, thinking, outcomes, plants, interview anchors, references, Kahoot plan |
| `docs/07_Client_Zero.md`, v2.2, section 7 | Data version v2 and its witnesses |
| `docs/programme/calendar.md` | Wed 07 Oct 2026, W01/D3, teaching, module M1, no faculty block |
| `content/W01/D1/study-notes/C2_W01_D01_domain_retail_STUDENT.md` on branch `w01-domain-retail`, read with `git show` on 30 September 2026 | The domain story the pack links to; Anand's row in the org chart; the dossier's net revenue definition |
| `content/W01/D2/trainer/C2_W01_D02_day_sheet_TRAINER.md` | Tuesday's reported numbers: Retail-Plus 2.32 to 1.18, down 49.0 percent |

## The data

```
python3 data/generate_client_zero.py --version v2 --out content/W01/D3/data --stem C2_W01_D03
```

Rerun on 30 September 2026 into a scratch folder; all four files came out byte-identical to the
committed ones. The CSV holds 201 rows (the contract's 200 plus the near-duplicate), the JSON feed the
first 120 rows cut inside the 120th record, the vendor copy the header twice and the first 39 data
rows, and the take-home file the v2b sample.

## The chapters, and where each came from

| Chapter | Notebook | Deck | The spine's rung |
|---|---|---|---|
| 1. What the ERP actually sent | `01_profile` | Half one, SECTION 1, S7 to S17 | The profile |
| 2. The rows that repeat | `02_duplicates` | Half one, SECTION 2, S18 to S26 | The migration's duplicates |
| 3. The copy that stays | `03_identity_rule` | Half one, SECTION 3, S27 to S37 | The identity rule |
| 4. What is missing or malformed | `04_missing_malformed` | Half one, SECTION 4, S38 to S47 | Missing and malformed values |
| 5. The bridge to the books | `05_bridge` | Half one, SECTION 5, S48 to S57 | The revenue bridge with Tuesday recomputed |
| 6. The log the analyst audits | `06_audit_logs` | Half two, SECTION 6, S1 to S11 | The sixth chapter the brief names: the rejects and decisions logs Anand's analyst audits |

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
7. **Revenue is booked value, every status.** Both 2.1 and 1.9 total all statuses in the generator's
   contract. The retail dossier defines net revenue after cancellations and returns and says Finance
   reconciles to net revenue; this case keeps both figures on booked value, and the notes and the day
   sheet say so once. This is a tension between the dossier and the client-zero contract, raised in
   the session report.
8. **Percentages are from unrounded ratios.** Retail-Plus falls 35.0 percent (26/22 against 40/22);
   Tuesday's -49.0 percent is quoted from Tuesday's day sheet, since Tuesday ran on v1.
9. **The afternoon deck's chapter opener shows the numeral 01.** `scripts/build_deck.py` numbers
   sections by their order in the file, so chapter 6, which opens the afternoon deck, is drawn as 01.
   The title and the notes say chapter 6.
10. **Chapter titles are statements.** `scripts/deck_md_check.py` reads a SECTION title ending in a
    question mark as a question slide, so the six titles drop the mark in the decks and notebooks alike.
11. **The study notes run to about 6,300 words** against the standard's 4,000 to 5,000, because six
    chapters as worked cases with options and sizing plus fifteen full interview answers do not fit the
    lower figure without cutting what the standard requires.
12. **The practice lab's "second export with new defects" is the vendor copy**, since the take-home
    file is the second sample the standard assigns to the take-home.
13. **Files replaced.** The three round notebooks became six chapter notebooks
    (`03_bridge` removed; `03_identity_rule`, `04_missing_malformed`, `05_bridge`, `06_audit_logs`
    added); `hands_on` and its solution became `ex1_escalated_case`; the three round sets and their
    solutions became six chapter sets. All removals by `git rm`.

## Invented, and recorded as invented

- Every record in the mechanism cells: INV-01 to INV-03 (chapter 2), INV-11 to INV-13 (chapter 3),
  INV-21 (chapter 4); the companion's four experiments; the decision workbook; the recovery extra.
- Every number in the chapter sets, the case briefs' distractors, the lab's problem 1 and the Kahoot,
  except where an item says it is the day's.
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
| 2 | Starbucks billed some card customers twice on 22 and 23 May 2009, about 7,800 stores, about one million customers repaid | https://www.nbcnews.com/id/wbna31208561 (checked 30 Sep 2026) |
| 3 | The IRP rejects an invoice already reported under the same supplier GSTIN, invoice number, document type and financial year | https://www.gstn.org.in/assets/mainDashboard/Pdf/GST%20e-invoice%20System%20-%20FAQs%20-%20Version%201.4%20Dt.%2030-3-2021.pdf (checked 30 Sep 2026) |
| 3 | E-invoicing for aggregate turnover above Rs 5 crore from 1 August 2023 | https://www.gstcouncil.gov.in/node/4365 (checked 30 Sep 2026) |
| 4 | Hundreds of Amazon UK items at 1p for about an hour on 12 December 2014; most orders cancelled | https://www.bbc.co.uk/news/uk-northern-ireland-foyle-west-30475542 (checked 30 Sep 2026) |
| 5 | Tesco overstated half-year profit guidance by about GBP 250 million, 22 September 2014 | https://www.bbc.co.uk/news/business-29306444 (checked 30 Sep 2026) |
| 5 | Confirmed as GBP 263 million: GBP 118 million first half, about GBP 70 million 2013/14, about GBP 75 million before | https://www.tescoplc.com/media/hm2hnfbe/interim_2014-15_results_statement.pdf (checked 30 Sep 2026) |
| 6 | Patisserie Valerie's hole put at GBP 94 million, March 2019 | https://www.bbc.co.uk/news/business-47591082 (checked 30 Sep 2026) |
| 6 | FRC fined the auditor GBP 4 million, reduced to GBP 2.34 million, for three years of audits, 27 September 2021 | https://www.frc.org.uk/news-and-events/news/2021/09/sanctions-against-grant-thornton-uk-llp-and-david-newstead/ (checked 30 Sep 2026) |

Left out as unverified: a count of Amazon items or sellers affected; Target Canada's total loss
beyond CBC's figures; any retailer's own statement on deduplicating by order id. No verified public
case was found of an export stitched from two extracts inflating reported sales, so chapter 2 uses the
Starbucks double charge and says what it is. Patisserie Valerie's criminal case is unresolved; the
pack names no individual.

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

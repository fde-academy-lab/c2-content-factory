# Provenance: Week 2, Wednesday

**INTERNAL.** What this pack is built from, what was verified and when, and every decision that
departs from a source.

---

## The sources

Raised on 1 October 2026 to standard v3, from, in this order:

- The requester's day prompt, `prompts/week_revamp_W02_W03.md` section 3, with the Week 2 Wednesday
  fills: the six chapters (top fifty overall, per segment, the tie at fifty, falling spend with LAG,
  the running total against plan, and the protect list Marketing acts on), the four traps, the
  options to weigh (ROW_NUMBER, RANK and DENSE_RANK against the business rule; a calendar against
  LAG), queries shipped as `.sql` files in `sql/`, and the faculty-day shape.
- `docs/detailing/W01_W02_spine.md`, approved on 29 September 2026 and raised on 30 September 2026,
  for the case, the rungs, the traps and the faculty-day paragraph.
- `.claude/skills/day-pack-builder/references/the-standard.md` at standard v3 (decisions
  `chapter-standard`, `four-domains`, `question-ladder`, `self-contained`, `humanizer` and
  `opus-max` in `data/programme/facts.yaml`), whose model pack is `content/W01/D1`.
- The Wednesday 14 October 2026 row of `docs/curriculum/W2_Data_manipulation.md` (tracker v7), read in
  column order, with the violet column for the IITGN faculty session W2-3, which is tentative.
- The W02/D3 line of `docs/programme/calendar.md`: Wed 14 Oct 2026, a teaching day, Module 1, faculty
  block W2-3 tentative. The day sheet carries both through the `sync:module:W02/D3` and
  `sync:faculty-day:W02/D3` blocks, filled by `scripts/sync_programme.py`.
- `docs/07_Client_Zero.md` at v2.2, locked 13 September 2026, for the stakeholders and the v4 row of
  the dataset ladder.
- The retail dossier, `content/W01/D1/study-notes/C2_W01_D01_domain_retail_STUDENT.md`, for the
  segments, the membership tier and the plan line's place in Meera's quarter.

The 29 September build of this pack, in three 50-minute rounds, supplied the take-home's second
sample and its generator, the companion page and the plan line's trap. Everything else was rebuilt.

---

## The data

The warehouse is the v4 file Monday's pack ships,
`content/W02/D1/data/C2_W02_D01_warehouse_v4_STUDENT.sql`, written by `data/generate_client_zero.py`
and loaded into the database `kalpa` by the Codespace's own script. Nothing in it is hand-edited.
On 1 October 2026 the loaded tables held orders 1,000, customers 340, payments 1,428, refunds 12,
campaign_exposure 136 and plan_line 13.

```
python3 data/generate_client_zero.py --version v4 --out content/W02/D1/data --stem C2_W02_D01
bash .devcontainer/load_warehouse.sh
```

Every query the pack shows lives in one of the six chapter files in `sql/`, under a `-- name:` line,
and the notebooks read their blocks from those files, so a notebook and its `.sql` file cannot
disagree. All six files ran against PostgreSQL 16.14 on 1 October 2026; the one block that errors on
purpose, `c2_where_error`, prints `ERROR:  window functions are not allowed in WHERE`.

The take-home's second sample is written by `internal/C2_W02_D03_takehome_data_INTERNAL.py`, which
imports the generator, sets its seed to 20261014, its own quarter totals (Rs 9,61,20,000 and
Rs 9,23,60,000), 454 Q2 orders and a plan line of Rs 72,40,000 a week, reruns `build_v4`, and adds one
three-way tie. It loads into its own schema, `takehome`, and leaves the day's warehouse untouched.
The file was regenerated on 1 October 2026 and is byte-identical to the 29 September file (md5
0e19d6d71ebac061c1f844993a8d0fe2); every self-check value was recomputed on it the same day.

```
python3 content/W02/D3/internal/C2_W02_D03_takehome_data_INTERNAL.py
psql -d kalpa -f content/W02/D3/data/C2_W02_D03_takehome_STUDENT.sql
```

---

## The plants, and where each is used

Every plant appears by name only in `trainer/` and here. The notebook script keeps a list of the
planted ids and values (`FORBIDDEN`) and stops the build if any saved output prints one.

| Planted | Where it is used |
|---|---|
| The exact Q2 tie at fiftieth in Retail-Plus, C-0185 and C-0242 on Rs 3,350, so RANK ships 51, ROW_NUMBER 50, DENSE_RANK 52 and whole ties only 49 | Chapter 3's your-turn, an empty cell in notebook 03 and morning slide S46, where each learner runs Retail-Plus and reads its own count; the escalated case, part 1, whose solution prints Business, Retail-Core and Student and leaves Retail-Plus to the learner's own run; the day sheet's debrief. No STUDENT file, solution included, prints a Retail-Plus count or a total that reveals it (decision 6). |
| The natural tie at 48th in Retail-Plus, C-0189 and C-0206 on Rs 3,480, which nobody planted and which pushes DENSE_RANK to 52 | The day sheet's plant table, for the trainer reading a learner's boundary rows. |
| Three Retail-Plus members whose spend fell in each Q2 month, C-0161, C-0171 and C-0175 | Inside chapter 4's 16 and chapter 6's 9, which no STUDENT file splits by segment or lists; the nine are printed only in an empty your-turn cell (block `c6_call_list`); the escalated case, part 2. |
| The plan line as a small table, 13 weeks from Monday 6 July at Rs 75,69,230 | Chapter 5, where the plan-first join drops the 25 orders of 1 to 5 July; the escalated case, part 4. |
| The bulk Business order KR-00667 (Rs 1,98,57,600), Monday's plant | Nowhere by name. Business's lists hold every Business buyer, so no file needs the order. |
| The take-home's three-way Retail-Core tie at places 19 to 21, C-0017, C-0033 and C-0144 on Rs 5,170, added by the builder | The take-home, sections 2 and 3, and the self-check's 20, 21, 22 and 18. |
| The take-home's falling ladder, C-0154, C-0165 and C-0170, which the generator places under the new seed | The take-home's flag counts, 21, 13 and 6. |
| The take-home's tie at fiftieth in Retail-Plus, C-0175 and C-0247 on Rs 3,680, from the generator's own tie step | Nowhere in the brief; the day sheet names it in case a learner meets it. |

---

## The build: six chapters

| Deck section | Notebook and `.sql` file | Chapter question | Trap and its exact wrong number |
|---|---|---|---|
| Morning, SECTION 1, S7 to S20 | `01_top_fifty` | Which fifty members spent the most in Q2? | The fifty biggest Q2 orders sent as the top fifty members: 50 rows naming 28 members, all Business |
| Morning, SECTION 2, S21 to S34 | `02_each_segment` | Which fifty members lead each of the four segments? | The whole book numbered once and split by segment: Business 35, Retail-Core 4, Retail-Plus 11, Student 0 |
| Morning, SECTION 3, S35 to S48 | `03_tie_rule` | When two members tie at fiftieth place, how many does a list ship, and which rule did the head of Retail-Plus ask for? | DENSE_RANK's Retail-Core top fifty shipped as 52 members, two of them past the line with no tie at it |
| Morning, SECTION 4, S49 to S61 | `04_falling_spend` | Whose monthly spend fell two months running? | LAG with no PARTITION BY flags 20 members, 4 of them compared with another member's month |
| Morning, SECTION 5, S62 to S76 | `05_against_plan` | Has Q2 revenue kept pace with the plan line week by week, and where did it stand at mid-quarter? | The plan-first join closes at Rs 9,68,60,180, reported as Rs 15,39,810 short of plan |
| Afternoon, SECTION 6, S2 to S16 | `06_call_first` | Which listed members does Marketing call first, and does each flag hold up when a member says they were on holiday? | Chapter 4's 16 flags shipped as calls, 7 of them reading a skipped month as last month |

The morning deck holds 82 slides and the afternoon deck 30: chapter 6, the escalated case's first two
parts, the close with the day's answer and the Kahoot, and self-study slides for the interview drill
(D22 and D23), the second case (D24) and the day's wrong numbers (D25). The notebooks are written by
`internal/C2_W02_D03_build_notebooks_INTERNAL.py` and executed cold in their own folder by
`scripts/nb_make.py`; the same script writes the two case twins
(`ex1_escalated_case`, `ex2_second_case`) and their executed solutions. The decks are built by
`scripts/build_deck.py` from the markdown in `slides/`.

---

## Decisions that depart from a source

1. **Chapter 1's trap is this pack's.** The spine lists four traps for Wednesday and the standard asks
   one per chapter. Chapter 1 stages the fifty biggest orders sent as the top fifty members (50 rows,
   28 members), the row's question GROUP BY answers before a window is needed, and Monday's "rows
   counted as customers" one level up.
2. **Chapter 3 meets the tie twice.** The spine's "a tie that ships 49 or 51 rows" is the planted
   Retail-Plus tie, which the room finds in its own run, so the chapter cannot stage it with its
   number. The chapter shows the four rules on an invented top four (4, 5, 5 and 3), and its trap on
   real data is DENSE_RANK's 52 in Retail-Core, where nobody ties at the line. The row's "Never cut
   the tie demonstration" is kept by the your-turn on Retail-Plus.
3. **Chapter 5's trap moved from the case.** The 29 September build staged the plan-first join in the
   escalated case. It is chapter 5's trap now, since it is the running total's own wrong number, and
   the case reuses the fix as a marker.
4. **Chapter 6 is the protect list Marketing acts on.** The fill names it; the spine's rungs stop at
   the running total. Its trap is the spine's "a skipped month counted as a fall", met on chapter 4's
   16 (7 of them across a gap), with the calendar against LAG as its options.
5. **A second case exists on a faculty day.** The spine's afternoon table says none on a faculty day;
   the requester's fill moves the second case to the practice lab and the take-home. It asks whether
   Retail-Core's list should rank by orders, which the row's "Retail-Plus frequency is the problem"
   raises, and it runs in the take-home, forty minutes in pairs or alone.
6. **The Retail-Plus count is printed in no STUDENT file, solutions included.** The row says the room
   meets the tie in its own output. The escalated case's solution prints the other three segments and
   leaves Retail-Plus to the learner's run, and the day's answer on afternoon S19 says "the count your
   own run gave". Morning S46, the your-turn, withholds its answer for the same reason, so it carries
   no Answer slide and is titled as a statement.
7. **The escalated case climbs past the chapters.** Its five parts reuse the chapters' methods on
   harder asks: each segment's list with its count, the members rung first, the share of each
   segment's revenue the lists carry (100, 76.1, the learner's own Retail-Plus share and 100), Q2
   against plan by total and by weekly run rate, and the lines for Meera and Marketing. Parts 1 and 2
   run in the trainer's afternoon (20 minutes); parts 3 to 5, its debrief and the interview drill run
   in the TA-led practice lab.
8. **The day's afternoon follows the fill.** The trainer keeps 60 minutes: chapter 6 (30), the
   escalated case's first two parts (20) and the Kahoot (10). The IITGN block W2-3 takes the last 120
   minutes, tentative, and every STUDENT file that mentions it carries the word tentative.
9. **The window function in WHERE is a two-minute aside, never an item.** The row's "what the data
   reveals" and its Kahoot Q5 name the error. The requester's rule says a syntax or runtime error gets
   two minutes when it happens and never a trap slot, a chapter or an exercise item, and the requester
   outranks the row. The error lives in chapter 2's aside (block `c2_where_error`) and the [F]
   interview question stays, since it is the row's anchor. Kahoot Q5 tests ROW_NUMBER's cut at a tie.
10. **Monday's row says v4 carries exact amount ties in the top ten for today's RANK demonstration.**
    Neither the order amounts nor the Q2 member totals in v4 tie in the top ten; the tie the row and
    `docs/07` name for today sits at fiftieth in Retail-Plus, and the pack follows today's row. The
    mechanism is shown on six invented members.
11. **Q2 revenue is booked revenue in every status.** Monday's suite defines Q2 at Rs 9,84,00,000 on
    that basis, and the tie at fiftieth exists only on that definition, so every file that shows a
    revenue figure says which definition it uses.
12. **"PostgreSQL Exercises, window functions category, first three" becomes three named pages.** The
    site has no separate window functions category; its window questions sit in the Aggregation
    category. The first three there are countmembers, nummembers and fachours4.
13. **Chapter 4's company is American.** No Indian company's own page on a customer's falling
    activity could be verified on 1 October 2026: the Medium-hosted engineering blogs of Swiggy,
    Flipkart, Razorpay and Meesho refused the session, and Airtel's integrated report names churn
    prediction without a signal read against a customer's own history. Square's "Lapsed" group stands.
14. **The take-home's ask is Marketing's, on Retail-Core, with the head of Retail-Plus's tie rule.**
    `docs/07_Client_Zero.md` has no head of Retail-Core, so the brief invents none.
15. **The interview drill prints on two slides, D22 and D23.** The angle runs to thirteen questions,
    the row's five anchors and eight follow-ups from the day's traps. A table of a header and
    thirteen rows needs 5.04 inches at the deck builder's smallest row, against 4.94 on a slide, so
    the three [D] questions sit on D23 and the later self-study slides renumber to D24, D25 and S26.
16. **They for every member and every stakeholder whose pronouns no source states.** `docs/07` writes
    Meera Raghavan as "she", and nobody else's pronouns are stated, so members, the head of
    Retail-Plus, the marketing lead, Kavya and Anand are "they" in every file. The head of
    Retail-Plus's chapter 6 quote, invented for this pack, reads "they were travelling in August and
    have not stopped buying. Is your flag wrong about them".
17. **The cheat sheet's anchor is S5's drawing reshaped.** S5's exact shape printed its labels at 5.2
    points and pushed the sheet to two pages, so the sheet carries the same two branches with the
    labels on the arrows. The notes and the board's first drawing carry S5's exact source, and
    notebook 01 draws the same two branches with the helper's tree.
18. **Chapter 2 stages its trap before its build.** The trap is chapter 1's list reused per segment,
    which is the first thing a hurried analyst sends, and PARTITION BY is both the build and the fix,
    so the chapter shows the wrong list, its check, then the window that replaces it. Chapter 6 runs
    its second route before the call list, since the call list needs the nine the route confirms.
19. **The escalated case's monthly table carries the segment.** Marker 3's option a, PARTITION BY
    segment, would otherwise stop with an error, and an error is never an exercise item; with the
    segment on every row, the option runs and its check counts more than 700 rows that cross members.
20. **Chapter 1's live pair is items 2 and 3.** Item 1 now sizes the four per-segment builds, and its
    key prints 155 rows, which chapter 2's S30 asks the room to predict. Items 1, 4 and 5 run in the
    practice lab or tonight, after chapter 2; every other set keeps items 1 and 2 live.
21. **A key ties for the longest option in about a quarter of items.** The rigor reviewer asked for
    the key to be the lone longest option in about a quarter of items, so length points neither way;
    `scripts/distractor_audit.py` fails any item whose key is the lone longest, and CLAUDE.md requires
    the audit to pass, so the key ties exactly for the longest in about a quarter of each file's items
    and is never the lone longest or the lone shortest.
22. **"The line" means the cut-off, defined where each file first uses it.** The pedagogy reviewer
    found the word in three senses: the cut-off of a list, the plan line and a line of code. Every
    file that uses the cut-off defines it at first use as the last place a list keeps, fiftieth on a
    top fifty, and the plan line keeps its full name.
23. **The running total's interview answer names two failures.** Ordered by date alone under
    PostgreSQL's default frame, a running total repeats on every run and gives peers one figure; with
    a ROWS frame over the date alone, tied rows can come in a different order on each run. The order
    id after the date fixes both. The row's word "deterministic" stays in the [F] question.
24. **Chapter 4 switches to a lookup per row.** A self-join that matches each September to the same
    member's rows dated one and two months earlier keeps 9 members on this book, which is chapter 6's
    calendar answer, so the build that reproduces LAG's 16 without window functions is a correlated
    subquery for each member's previous month with an order.
25. **The overlap of flags and lists is stated without a place.** The 16 flagged members all sit on a
    protect list, and two of them sit in their list's last three places: C-0054 at Retail-Core's 48th
    and C-0185 at Retail-Plus's 50th, the planted tie. STUDENT files say "two of them in the last three
    places of their list", which names neither the plant nor its place.

---

## Invented, and recorded as invented

1. The quotes beyond the row's two: the head of Retail-Plus on C-0216's August (chapter 6), the
   marketing lead's Monday message (the escalated case) and the frequency ask (the second case), each
   written in the row's voice for this pack.
2. The six invented members A to F (Rs 7,500, 7,500, 6,000, 5,200, 5,200 and 4,100), which show the
   three functions side by side and whose own top four ships 4, 5, 6 and 3 on the cheat sheet, and
   the invented top four with a tie at fourth (Rs 9,100, 8,800, 8,200, 7,400, 7,400 and 6,900),
   which ships 4, 5, 5 and 3. Both are labelled invented wherever they appear.
3. The members on the companion page, `demos/C2_W02_D03_tie_STUDENT.html`, labelled invented there.
4. The take-home's three-way Retail-Core tie, added to the second sample by the builder.
5. The members and amounts in Kahoot items 1, 5 and 7, labelled invented in the quiz.
6. Each chapter's sizing in rows read (1,848, 16,617, 1,504, 6,006 and 1,806) is this pack's
   arithmetic on the warehouse, shown with its working.
7. The invented members of the chapter sets, the guided build and the practice lab (letters such as
   A to F, P to R and R to X, and ids such as V-01 to V-08, X-01 and Y-01 that the warehouse does
   not hold), each labelled invented where it appears.
8. The chapter sets' numbers added in passes 4 and 5, each recomputed on the warehouse on 1 October
   2026. Chapter 1: fifty orders per segment ship 188 rows (50, 50, 50 and Student's 38) naming 131
   members, fifty members or every buyer per segment ship 155, and four glued queries read 4 x 462 =
   1,848 order rows; the fifty biggest Q2 orders carry Rs 7,90,08,600, 80.3 percent of Q2, and leave
   off a Business member on Rs 15,91,000, above the Rs 11,27,000 of the smallest member they name.
   Chapter 2: ten per city and segment ship 171 rows, ten per city alone 60, and 24 queries read 24 x
   462 = 11,088 order rows; one sorted query over Retail-Core and Student with LIMIT 70 returns 65 and
   5. Chapter 3: on Retail-Core a top thirty-one ships 31, 32, 32 and 30 under ROW_NUMBER, RANK,
   DENSE_RANK and whole ties only, and a top forty 40, 40, 42 and 40. Chapters 4 to 6: 84 of Q2's 92
   calendar days carry an order; the 16 flagged members hold 68 member-months; 50 of the 118 members
   with a September order also ordered in August; a calendar self-join reads 118 September, 122
   August and 119 July rows, 359 in all; 27 members bought in July and August and not in September.

---

## The real company in each chapter

Each fact was fetched on 1 October 2026; quotes are copied from the fetched text.

| Chapter | Fact | Link | Checked |
|---|---|---|---|
| 1 | Starbucks Rewards members made 59 percent of money tendered at US company-operated stores in Q3 FY26, and 35.8 million US members were active in the 90 days to 28 June 2026 | https://s203.q4cdn.com/326826266/files/doc_financials/2026/q3/Q3-FY26-Digital-IR-Dashboard.pdf | checked 1 Oct 2026, 200 |
| 1 | Q3 FY26 is the 13 weeks ended 28 June 2026 | https://www.sec.gov/Archives/edgar/data/829224/000082922426000129/sbux-06282026xearningsrele.htm | checked 1 Oct 2026, 200 |
| 2 | Amazon's overall Best Sellers Rank "doesn't always indicate how well an item is selling in relation to similar items", so Amazon keeps category and subcategory lists | https://www.amazon.com/gp/help/customer/display.html?nodeId=GGGMZK378RQPATDJ | checked 1 Oct 2026, 200 |
| 2 | One product can hold a different rank in each category it sits in | https://sell.amazon.com/blog/amazon-best-sellers-rank | checked 1 Oct 2026, 200 |
| 2 | JEE Advanced 2026 keeps category rank lists beside the common rank list; the OBC-NCL rank 1 held CRL 3 and the GEN-EWS rank 1 held CRL 6 | https://jeeadv.ac.in/documents/Result2026PressRelease.pdf and https://jeeadv.ac.in/documents/IBEnglish_2026.pdf | checked 1 Oct 2026, 200 |
| 3 | American Airlines ranks upgrade requests by status tier, type of upgrade and Loyalty Points in the last 12 months, then booking code and the time of the request | https://www.aa.com/web/i18n/aadvantage-program/answers-support/upgrades-for-status-members.html | checked 1 Oct 2026, 200 with a Safari user agent |
| 3 | Tokyo 2020 men's high jump final, 1 August 2021: Barshim and Tamberi placed 1 and 1 on 2.37 m and Nedasekau placed 3, with no silver | https://worldathletics.org/competitions/olympic-games/the-xxxii-olympic-games-athletics-7132391/results/men/high-jump/final/result | checked 1 Oct 2026, 200 |
| 4 | Square's "Lapsed" group holds "customers who were regulars, but haven't visited in the last six weeks"; a regular visited three times in six months | https://squareup.com/help/us/en/article/6245-manage-customer-groups-and-filters | checked 1 Oct 2026, 200 |
| 5 | Target cut its Q2 2022 operating margin guidance to around 2 percent on 7 June 2022, from a range centred on Q1's 5.3 percent, and closed the quarter at 1.2 percent | https://corporate.target.com/getmedia/c217afb7-0af0-4956-8179-abfabd71ddd5/Target-Corporation-Announces-Updated-2022-Plan-Focused-on-Inventory-Optimization.pdf, https://www.sec.gov/Archives/edgar/data/27419/000002741922000011/a2022q1ex-99.htm and https://www.sec.gov/Archives/edgar/data/27419/000002741922000023/a2022q2ex-99.htm | checked 1 Oct 2026, 200 |
| 6 | Shopify Engineering: "Far too often businesses define churn as no purchases after N days" (Cam Davidson-Pilon, 14 November 2017) | https://shopify.engineering/how-shopify-merchants-can-measure-retention | checked 1 Oct 2026, 200 |
| 6 | Marriott extended elite status earned in 2019 until February 2022 (14 April 2020) | https://www.sec.gov/Archives/edgar/data/1048286/000162828020004943/mar-2020covidx19ex991.htm | checked 1 Oct 2026, 200 |
| 6 | Hilton extended status to 31 March 2022 for Silver, Gold and Diamond members set to downgrade in 2020 or 2021 (27 October 2020) | https://stories.hilton.com/releases/hilton-honors-adds-flexibility-value-for-members | checked 1 Oct 2026, 200 |
| 2, 4 | MySQL first shipped window functions in 8.0.2 (17 July 2017), and 8.0.11 (19 April 2018) is the first GA release of 8.0 | https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-2.html and https://dev.mysql.com/blog-archive/whats-new-in-mysql-8-0-generally-available/ | checked 1 Oct 2026 |

Not verified, and so not in any file: a live "Best Sellers Rank" line on an amazon.in product page
(bot interstitial), the phrase "updated hourly", the World Athletics rule edition in force in August
2021, Marriott's first announcement of 8 April 2020, and Hilton's first extension of March 2020.

---

## The row's references, with the date each was checked

Each link was requested on 1 October 2026 and returned HTTP 200, except where noted.

| Link | Role | Checked |
|---|---|---|
| https://www.postgresql.org/docs/16/tutorial-window.html | PostgreSQL 16, 3.5 Window Functions: why WHERE cannot see a window, and peers in a running sum; the notes' reading path | checked 1 Oct 2026, 200 |
| https://www.postgresql.org/docs/16/functions-window.html | PostgreSQL 16, 9.22 Window Functions: row_number, rank, dense_rank and lag as documented; the notes' reading path | checked 1 Oct 2026, 200 |
| https://www.youtube.com/watch?v=Ww71knvhQ-s | techTFQ, "SQL Window Function, How to write SQL Query using RANK, DENSE RANK, LEAD/LAG", the one video for the new topic | checked 1 Oct 2026 through YouTube's oEmbed endpoint, which returned the title and channel; the watch page sent the session to a bot check, so the running time is not verified and the notes say so |
| https://pgexercises.com/questions/aggregates/ | PostgreSQL Exercises, Aggregation, where the site keeps its window questions | checked 1 Oct 2026, 200 |
| https://pgexercises.com/questions/aggregates/countmembers.html | The first window question, a total on every row; the take-home and the notes | checked 1 Oct 2026, 200; the site's answer uses count(*) over () |
| https://pgexercises.com/questions/aggregates/nummembers.html | The second, a numbered list of members | checked 1 Oct 2026, 200; the site's answer uses row_number() |
| https://pgexercises.com/questions/aggregates/fachours4.html | The third, the facility with the most slots, every tied result output | checked 1 Oct 2026, 200; the site's answer uses rank() |
| https://neon.com/postgresql/window-function | The PostgreSQL Tutorial's window functions page, the row's postgresqltutorial.com resource, which now redirects here | checked 1 Oct 2026, 200 after the redirect from https://www.postgresqltutorial.com/postgresql-window-function/ |
| https://www.pgtutorial.com/postgresql-window-functions/ | pgtutorial.com, clause syntax cross-checks | checked 1 Oct 2026, 200 |
| https://sqlbolt.com/ | SQLBolt, for anyone still shaky on joins | checked 1 Oct 2026, 200 |

The row carried pgexercises.com, postgresqltutorial.com, pgtutorial.com and sqlbolt.com as verified 05
Sep 2026; each was checked again on 1 October 2026 before it entered this pack.

---

## Tools the numbers and outputs came from

PostgreSQL 16.14 for every query and error text; Python 3.11.15, pandas 3.0.6, psycopg2 2.9.13,
SQLAlchemy 2.1.1, nbformat 5.11.1 and nbclient 0.11.0 for every notebook output; python-pptx 1.0.2
through `scripts/build_deck.py` for the decks; LibreOffice 24.2.7.2 with Carlito for the render
check. The first deck builds drew their mermaid with the container's mermaid-cli 12.0.0; the shipped
decks and the cheat sheet are drawn by mermaid-cli 11.17.0, the major version `setup.sh` pins,
installed in the session's scratch space on 1 October 2026.

---

## The depth loop

| Pass | Asked | Found | Changed |
|---|---|---|---|
| 1. Draft | Is every chapter built from the row, the spine and the fill, in the chapter order? | The spine's five rungs and the fill's sixth became six chapters; each notebook runs need, options with sizing and the call, build with each step predicted, trap, second route and Kavya's review, and each deck section follows it in 13 to 15 slides. | Nothing further. |
| Exercise review | Do the exercise sets, cases and lab hold their keys, plants and numbers before any reviewer sees them? | Seventy items, 26 of them design items; no plant in any STUDENT file; every key matches its notebook. Four notebook markers (escalated 7, 9 and 10, second case 7) kept options the briefs had lengthened, so the key was the only longest option in the notebook; escalated marker 3's option a stopped with an error; escalated item 13 printed the 76.1 and 92.6 percent shares that part 3 asks the learner to compute; the saved case solution charted Retail-Plus's share under RANK, 86.3 percent, which set beside notebook 02's 85.5 shows RANK keeping an extra member. | The notebook options now match the briefs word for word; the monthly table carries the segment (decision 19); item 13 sizes per call in rupees; the solution charts Business, Retail-Core and Student and leaves Retail-Plus to the learner's run. The marker test catches every wrong letter on the eight computed markers. |
| 2. Domain | Could a learner who has never worked in a business say, for every chapter, who asks, why the metric matters, what a wrong number costs and which real company faces the same question? | Every chapter names its stakeholder, metric, cost and company with a dated source. Chapters 3, 5 and 6 named no section of the retail dossier, and chapter 1 sent the reader to section 4 for what a paid tier buys, which section 2 holds. | Each chapter notebook's metric paragraph names its dossier section: sections 2 and 4, 4, 4, 5, 4 and 5, and 8 (a wrong retention flag spends offers on the wrong members). |
| 3. Problem first | Does every technique answer a stated problem, with two to four options sized, a best-fit call and the fact that would switch it, and is the code its last mile? | Every chapter sizes its options in rows, reads, pairs or lookups (462, 1,848, 16,617, 752, 1,504, 6,006, 1,806), makes its call, names the switch and reaches the same answer a second, independent way. Chapter 2 stages its trap before its build, and chapter 6 runs its second route before the call list. | Kept, with the reasons recorded as decision 18. |
| Humanizer read, decks, notebook script, day sheet, lab note, SQL comments | Which of the humanizer's patterns survive? | 22 edits on the morning deck, 17 on the afternoon's, about 58 in the notebook script's markdown, 7 on the day sheet, 6 on the lab note and 4 in SQL comments: lines with no verb under **Who needs the answer.**, closers and slogans, a staged run-up, "every analyst" and "most people" lines, "actually", and "he" for members and unnamed stakeholders. A line claiming half the buyers hold three quarters of the rupees "in both" segments was false for Retail-Plus, 50 of 76 buyers. Deck notes and the day sheet cited notebook 03's "section 4" and "section 5", which the notebook numbers steps 2 and 3. | Rewritten in place, the false line cut, the step numbers fixed; notebooks re-executed cold, decks rebuilt on mermaid-cli 11.17.0 and every slide rendered through LibreOffice with Carlito and looked at. |
| Humanizer read, reading and exercise files | Which of the humanizer's patterns survive in the notes, the sheet, the board work, the extras, every exercise and solution file, the take-home, the Kahoot and the companion page? | 28 of 30 files edited, the pre-read and self-check clean: lines with no verb under **Who needs the answer.** ("You, planning the day."), forty subjectless "Used at work whenever" lines, fragment openers, sayings ("a fall is a fall", "RANK's rule is older than any database", which its own 2021 example did not support), closers, unsourced "every interview" lines, and he, him or she for members, the head of Retail-Plus and Kavya. The companion page sent the Retail-Plus run to notebook 02 and dated its figures 29 September; the afternoon cover's quote dropped C-0216; the notes linked a tutorial address that redirects twice. | Rewritten in place with every heading, number, option and key unchanged except the five pronoun phrases; the companion points at notebook 03 and dates its figures 1 October 2026, after its two real figures (Rs 9,600 and Rs 9,630) were checked again; the cover quote carries C-0216; the notes link https://neon.com/postgresql/window-function (checked 1 October 2026); the sheet rebuilt, one page. Distractor audit, tic scan, html sweep and deck check pass. |
| 4. Rigor, one fresh reviewer, read-only, once, at 167f5d8 | Sit the day's seventy exercise items blind from the STUDENT files alone, recompute every number a file quotes on the warehouse, and check every STUDENT file for a plant and for Thursday's and Friday's traps. | One blocker: the companion page, which chapter 3 puts on the projector, named chapters 4 to 6's traps and the plan line's plant on load. Eleven majors: running-total answers that called a date-only total non-deterministic, when the default frame repeats it on every run and a ROWS frame is what can change; an eleven-rows interview answer that assumed a tie; Kahoot keys the lone shortest option in six of eight items; across 70 items, a lone longest option that was never the key; a guided build that printed answers under its predictions; set openings, stems and options that cued keys or echoed a slide's check line; design items that were recall or one step; case notebook checks that spelled a key or passed any letter; case openings that named a trap; strawman distractors; a lab ask GROUP BY could answer. Fifteen minors, among them chapter 5's sizing units, chapter 1's sizing column scoring three options at 50, "92 daily rows" against 84 dates with an order, a run rate "below plan since 10 August" when the week of 14 September beat plan, ROW_NUMBER's arbitrary order at a tie, LAG's other first-month causes, Tokyo 2020's third jumper on 2.37 m, and no learner file saying why booked revenue counts cancelled and returned orders. | The companion's chapter 4 to 6 parts fold closed and its walk holds at step 3. Every case check tests the learner's value against a second count, so all 51 wrong letters fail and no check spells a key. The chapter 1 to 6 sets, the guided build, both cases, the lab and the Kahoot were rebuilt or rebalanced with every key letter kept except escalated item 12, rebuilt on the 752-row monthly table (a to b). Keys tie for the longest option in about a quarter of items (decision 21). The drill answers, notes, day sheet, cheat sheet and notebook 05 name both running-total failures (decision 23); the run rate reads six of the seven full weeks from 10 August; chapter 4 switches to a lookup per row (decision 24); the notes give the booked-revenue reason, Rs 3,18,34,910 cancelled or returned and 38 of Retail-Core's 50 kept on delivered orders. Two helpers rebuilt the chapter sets under the builder's rules and recomputed every new number, recorded under invented item 8. |
| 5. Pedagogy and language, one fresh reviewer, read-only, once, at 167f5d8 | Run the headings-only read on every file, open three files at random alone (seed 20261014: the chapter 2 set, the second case notebook and its solution), look at every rendered slide of both decks, and list every humanizer pattern still present. | Eight majors: "line" in three senses with the cut-off undefined; "your own segment" where Retail-Plus was meant; template headings in eleven solution files and a generic closing heading in six notebooks; case notebooks without the two beats; S4 and S5's subtitles; four notebook charts; humanizer patterns in the decks, the notes, the board work, the Kahoot, the companion page, the lab note, the escalated brief and five solution files; fragments in "Kind:" lines, option openers and SQL comments. Twenty-four minors, among them afternoon notes timed at 66 minutes against 60, self-study slides with no minutes, trainer instructions inside client strips, titles that did not answer their subtitles, chapter 1's question 5 and chapter 4's question 2 with no slide, labels crossed by edges, close-slide tables at about 9 points, notebook charts 1,657 px wide, and no "order the analysis" item in the day. | "The line" is defined where each file first uses it (decision 22). Every solution heading names its set, every notebook closes on its chapter's question, and the case notebooks open on both beats. The afternoon notes total 60 minutes and chapter 3's 30. Chapter 1 asks five questions in the deck, notebook 01, the notes and the day sheet, its segment count folded into question 3, and S53 answers chapter 4's question 2. Diagrams were reshaped where an edge crossed a label, charts redrawn at their natural width, every listed humanizer pattern rewritten, and every fragment written as a sentence. Chapter 6's item 3 now orders the call list's four build steps, key c kept. The notes carry both beats under all eight non-chapter sections. The close-slide tables stay at the size `scripts/deck_layout.py` gives them, a shared file this pack does not edit. |
| Fix audit, one fresh helper, read-only | Which of the two reviews' findings are still open after the fixes, by file and line? | Eighteen open in the decks, the notes and the chapter 1 to 3 sets. One was new and made by a fix: S10 and notebook 01 sized the four segment lists in members and printed the 155 that chapter 2's S30 asks the room to predict, S26 offered "155, fifty or every buyer per segment" as a wrong option, and chapter 1's item 1 repeated S10 option for option. The others: five slips of "line" in the notes and index, two glossary rows, chapter 5's option C sized in pairs alone, the notes' switch to a "went quiet" flag, S3's title, the block name `c3_your_segment`, eight notes sections without beats, and render checks. | Chapter 1 sizes its options in order rows read (1,848 against 462 once) and S31 is the first place 155 appears; S26's option b is "227, one per member who bought"; item 1 asks for a top twenty-five per segment (100 order rows naming 85 members against 95 member rows); the rest fixed in place, the block renamed `c3_retail_plus_rules`. The builder checked every item the audit did not reach: the plant scan, key lengths in every set and the Kahoot (nine lone long distractors trimmed, two of them in the Kahoot), the escalated key strings in the day sheet and lab note (item 12 corrected to b), and every flagged slide in a fresh render. |

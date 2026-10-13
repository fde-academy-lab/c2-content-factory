# W04 D4 sources: every public fact with its check, every correction, every open item

INTERNAL. One page for the reviewer. Every link below was fetched on 12 October 2026 in the finishing
session; R2 ids are the case file's (`docs/detailing/W04_case_file.md`, "Public facts allowed on
Thursday").

## Which public facts does the pack use, and what did the check confirm?

| R2 | Fact as the pack states it | Source, checked 12 October 2026 | What the fetch confirmed |
|---|---|---|---|
| Th4 | Gold at 1.8 million members in Q4 FY23; members' orders about 30 percent of food delivery GOV in March 2023; order frequency up about 60 percent after joining; Gold members get free delivery | https://www.bseindia.com/xml-data/corpfiling/AttachHis/42b3bf3b-1edb-4da7-849a-87ca9da27ff8.pdf (checked 12 October 2026) | All four from the PDF's text, page 4 and the Q4 answer: "orders from Zomato Gold members (with free delivery benefit) now comprise as much as ~30% of our total GOV (Mar-23) ... increased by ~60% post becoming members" |
| Th1 | Blinkit: 46 percent of a cohort's customers order in the fourth quarter after acquisition, on average; NOV retention 150 percent at Q4 and 279 percent at Q12; a cohort spends nearly 3x three years on | https://drive.google.com/file/d/1jb9KWd4Ap4RTKHFHxzEOO7jgQqVZEGcd/view (checked 12 October 2026), linked from https://www.eternal.com/blog/q1fy27/ (checked 12 October 2026) | The results page that links the letter is dated 22 July 2026 (re-checked 13 October 2026); the letter's Blinkit section, re-read in the fix pass: "Q4 retention (% of customers placing at least 1 order in the 4th quarter after acquisition): average across all cohorts is 46%" and "a cohort of customers is spending nearly 3x with us three years after acquisition than they did in their first quarter" |
| Th2 | Instamart: every cohort's spend is indexed to the Q4 FY24 cohort's spend in its acquisition quarter, and that cohort spends 4.14x in its sixth quarter; Swiggy "weaned away certain users from the platform with low potential Lifetime values"; Instamart's average order value up about 40 percent year on year, to INR 697; the table states no denominator | https://www.swiggy.com/corporate/wp-content/uploads/2025/10/Q2-FY2026-Shareholder-letter.pdf (checked 12 October 2026) | The quotes and the 4.14x, from the PDF's text; the base quarter is Q0, the quarter of acquisition |
| Th3 | Platform MTU up 27.4 percent year on year; platform frequency, "completed orders per user in a month", 4.13 to 3.87, Q1 FY26 to Q1 FY27 (6.3 percent, our arithmetic); more than 4 million unprofitable Instamart users weaned over three quarters; Instamart's one-month retention of its transacting user base 61 percent from 55 | https://nsearchives.nseindia.com/corporate/SWIGGY_30072026154100_Covering_Letter_Letter_to_Shareholders_-_signed.pdf (checked 12 October 2026) | All four, from the PDF's text; the 61 sits in the letter's Instamart answer |
| Th5 | Amplitude: 7 percent of a cohort back on day seven puts a product in the top 25 percent for activation, from more than 2,600 companies; the blog gives no method | https://www.amplitude.com/blog/7-percent-retention-rule (checked 12 October 2026, re-read 13 October 2026) | "analysis of over 2,600 companies ... you've crossed into the top 25% for activation performance"; the page points to the company's 2025 Product Benchmark Report and states no method |
| M6, T3 | DMRC: 64.06 lakh journeys a day "currently", all days; the record 82,44,903 boardings on 17 September 2026, a bus-strike day; the earlier record of more than 81 lakh passenger journeys on 8 August 2025; journeys count each line a rider uses | The Tribune, https://www.tribuneindia.com/news/delhi/delhi-metro-records-99-95-train-punctuality-in-2026-dmrc/ (checked 12 October 2026); Republic World quoting DMRC's post, https://www.republicworld.com/india/delhi-metro-breaks-all-time-record-with-8244-lakh-footfall-as-dtc-strike-sends-rush-soaring-2026-09-18-137241 (checked 12 October 2026); Deccan Herald (PTI), 30 August 2023, https://www.deccanherald.com/india/delhi/delhi-metro-records-highest-ever-footfall-on-aug-29-2666561 (checked 12 October 2026); PTI via LatestLY, https://www.latestly.com/agency-news/dmrc-uses-new-count-metric-on-traffic-flow-doesnt-share-ridership-190870.html/amp (checked 12 October 2026) | "Journey or line utilisation is calculated by the number of corridors passengers use to reach their destinations"; the 82.44 lakh boardings beat the 81 lakh passenger-journeys record, so both are one line-use count |
| T2 | Aced: on its sample metric drop, define the metric, rule out a data issue first, segment before a root cause, and in its commentary keep fewer users apart from fewer views each; the page is undated | https://www.aced.io/blog/top-data-analyst-interview-questions (checked 12 October 2026) | The sample answer to "a 10% drop in Facebook's daily post views" and its commentary; byline "Aced Team", no date |
| New | Simpson's 1951 paper, its journal, volume and pages; the label about twenty years later | https://doi.org/10.1111/j.2517-6161.1951.tb00088.x (checked 12 October 2026, through its Crossref record; the publisher's page returns 403 to a script); https://en.wikipedia.org/wiki/Edward_H._Simpson (checked 12 October 2026) for the name's date | Title, journal, volume 13, issue 2, pages 238 to 241, July 1951 |
| Reading | Mixpanel cohorts; Amplitude funnels; pandas 10 minutes | https://mixpanel.com/blog/cohort-analysis/, https://amplitude.com/blog/funnel-analysis, https://pandas.pydata.org/docs/user_guide/10min.html (each checked 12 October 2026) | Each returned HTTP 200 |
| Video | IBM Technology, panel data; root cause analysis | https://www.youtube.com/watch?v=LoMgvSfKp6Y, https://www.youtube.com/watch?v=7t3lTYEd_PM (each checked 12 October 2026) | Titles and channel through oEmbed; lengths 11:39 and 8:32 from R3 of the same day |

## Which corrections to the case file does the pack carry?

Each is also in the facts file's `corrections` block, with the arithmetic or the source.

| Case file | The pack | Why |
|---|---|---|
| The dashboard blends everyone who joined before the month | Month-two retention: members two or more months past joining | With every cohort falling and August at 31, a blend that counts August cannot hold at 38 |
| 60,000 members | 53,089 | Seven cohorts of about 5,000, August's 13,000 and September's 5,089 |
| Twelve rows: August 2 of 5; September 6 of 12 | 0 of 5; 2 of 12 | 6 of 12 needs members to return, which breaks every cohort falling; 2 of 5 sits a point from Kalpa's 41; 1 of 5 equals the sale-week members' own 19.8 percent, and 3 of 12 sits within a point of Kalpa's per-member checkout, 24.5 |
| `events.member_id` | `user_id` with `is_member` | The ticket compares non-members on Android |
| Kalpa retention on orders | On app activity, the spine's fallback | 37 of the 120 Retail-Plus customers ordered in September in v4 |
| The funnel toy: 100 visits; checkout 10 of 50 per session against 10 of 20 per member | 100 sessions; 10 of 100 sessions against 10 of 20 people | 100 visits then 50 sessions mixes units, and 10 of 50 is no step over the step before (the first cold read's blocker) |
| The guesstimate's catch: journeys and boardings are different units | Trips against DMRC's line-use count, of which journeys and boardings are two names | Deccan Herald (PTI) defines the journey count by line used, and the boardings record beat the journeys record |
| Aced: tracking first | The hypothesis board's order, with Aced cited only for what its page says | Aced's sample answer defines the metric first and rules out data issues first |
| The tracking check: the mapping and the cut moved a week | The order records against the event log; the moved cut dates the fall | The rename shipped with the release, so a logging fault would also start on 14 September |

## Which items did the orchestrator close, and how?

Each was checked on `main` on 13 October 2026.

- Wednesday's pre-read for Thursday now prints the 53,089 members who joined from January to
  September and says the August group was grown by a sale week, so it agrees with Thursday's data.
- Monday's lab and Thursday's lab share the window of 10 to 30 September, and the shared constants
  agree in both facts files.
- Monday's Kalpa lab was rebuilt on Thursday's table (pull request 246): `C2_W04_D01_kalpa_members`
  is a byte copy of `C2_W04_D04_kalpa_memberships`, with v4's customer ids, and every order id in
  Monday's reorder log is a v4 order with the same customer, date, amount and status, so the two
  days' Kalpa tables join.
- The DMRC catch reads trips against line uses in the case file, Monday's deck and Tuesday's
  solutions, and the Aced line "tracking first" appears only in Thursday's and Saturday's sources,
  each of which cites Aced only for what its page says.

## Which cold-read findings were not fixed, and why?

Every other finding of both reads is fixed in the pack; `internal/C2_W04_D04_cold_reads_INTERNAL.md`
says where.

| Read, finding | What stayed | Why |
|---|---|---|
| Graduate 37 | The three reveals stay in the STUDENT cards file, and the Kahoot file marks its keys | The deck's answer slides print every reveal's numbers, so the cards spoil nothing the deck does not; the model pack's Kahoot file marks its keys the same way, since it is the file loaded into Kahoot; the staff printing line moved to the trainer's run sheet |
| Graduate 40, the posting place | No file names where letters are posted | The programme's facts name no posting channel, so the trainer names it in the room |
| Graduate 32, the handoff line | Superseded by the fix pass of 13 October 2026: S81 now says the table leaves a young cohort's later ages empty, and that treating a member who has not left yet as retained for ever would flatter every curve | Two rebuild cold reads found the spine's wording false for the table taught (its unlived cells are empty); the pack departs from `docs/detailing/W04_analyst_craft_spine.md`, section 8, which still carries the old line and sits outside this folder |
| Graduate 75, Gold's price | The pack names Gold's free delivery and no price | No source checked in the session states a price; the benefit comes from Zomato's own letter |
| Graduate 76, sections against chapters | Superseded on 13 October 2026 | The concept-first rebuild numbers every chapter as a SECTION in deck order, and the afternoon now opens on the fifth topic, SECTION 8 |
| Interviewer, sourcing 9 | The Eternal citation is the company's results page and the letter's copy it links | The exchange filing of the letter could not be found in the session; the quoted lines were re-read from that copy |
| Interviewer, sourcing 7 | The DMRC unit rests on PTI's report of DMRC's definition and on the record's framing | No DMRC release was fetched in the session |
| Interviewer 25, the supply-side cross-check | Named in the guesstimate, never computed | Train counts and capacities were not verified in the session, so no number is given |
| Interviewer 14, cost per retained user | Named in the AI variant without a number | The variant is invented; a cost figure would be a fabricated fact |
| Interviewer, round two, sourcing | No second copy of Swiggy's Q1 FY27 letter, and no DMRC post fetched directly | The NSE copy returned the full letter in this session; DMRC's post is quoted as Republic World carries it, and the "same count" reading is labelled the pack's inference |

## What did the concept-first rebuild of 13 October 2026 lock, and what did it change?

The requester's direction of 13 October 2026: teach the row's five subtopics first, as named concept
chapters and notebooks, then the case. The plan is `docs/detailing/W04_concept_first/D4_plan.md`;
where this pack departs from it, the departure is in the table of decisions below. Every link was
fetched on 13 October 2026 in the build session.

### Which written reference does each topic's rule or formula rest on?

| Topic | The rule or formula as the pack states it | Reference, checked 13 October 2026 | What the fetch confirmed |
|---|---|---|---|
| Cohort construction | Rows by joining month, columns by age, a cohort compared down a column at the same age | Mixpanel, "Cohort analysis", https://mixpanel.com/blog/cohort-analysis/ (checked 13 October 2026; the page says it was last edited 15 June 2026) | Rows are when users started, columns the time since they started, and a column compares cohorts at the same age |
| Cohort construction, in code | `melt` to one row per member per month, then one `pivot_table` with values, index and columns | pandas, "10 minutes to pandas", https://pandas.pydata.org/docs/user_guide/10min.html (checked 13 October 2026; the page documents pandas 3.0.6, and the session executed the notebooks on pandas 3.0.5) | `pivot_table` pivots by values, index and columns |
| Retention curves: shape and floor | A curve's floor is the level it stops falling at, the users who kept the habit | The same Mixpanel page (checked 13 October 2026) | "A healthy product shows the curve flattening rather than falling to zero; that plateau is the group of users who found lasting value" |
| Retention curves: the two-ages rule | A floor is called once two ages in a row read within a point of each other (exact equality until the fix pass of 13 October 2026) | None: the programme's own rule of thumb, labelled so on S17, in notebook 02, the notes and drill c2 | Not a sourced claim |
| Blended numbers against cohort truth | A rate over subgroups is their average weighted by each subgroup's share, and a total can run against its parts when the weights differ | Stanford Encyclopedia of Philosophy, "Simpson's Paradox", https://plato.stanford.edu/entries/paradox-simpson/ (checked 13 October 2026; first published 24 March 2021, substantive revision 6 June 2026); Wikipedia, "Weighted arithmetic mean", https://en.wikipedia.org/wiki/Weighted_arithmetic_mean (checked 13 October 2026) | The overall rate is a weighted average of the subpopulation rates; the weighted-mean formula, with a class example whose plain mean differs from its weighted mean |
| Blended numbers: the origin | E. H. Simpson, 1951, Journal of the Royal Statistical Society, Series B | Crossref record, https://doi.org/10.1111/j.2517-6161.1951.tb00088.x (checked 13 October 2026); Wikipedia, "Simpson's paradox", https://en.wikipedia.org/wiki/Simpson%27s_paradox (checked 13 October 2026) | Volume 13, issue 2, pages 238 to 241, 1 July 1951; the paradox needs group sizes that differ |
| Funnel stages, drop-off, denominators | Step rate over the step before; overall over the first step; drop-off 100 less the step rate | HockeyStack, "Funnels Reports", https://docs.hockeystack.com/documentation/funnels (checked 13 October 2026) | Step Conversion Rate from the previous step, Funnel Conversion Rate from the first step, Dropoff as 100 less the Step Conversion Rate |
| Funnel stages: drop-off in practice | Where users drop off between steps | Amplitude, "What is funnel analysis?", https://amplitude.com/blog/funnel-analysis (checked 13 October 2026) | Drop-off language; the page gives no step formula, so the formula rests on HockeyStack |
| The fix-first decision and its evidence | Rule out data issues first, segment, and keep fewer users apart from less use, before the call | Aced, https://www.aced.io/blog/top-data-analyst-interview-questions (checked 13 October 2026; the Exponent address the row names redirects there) | "Rule out data issues first"; segments by platform and geography; fewer users against fewer views per user; its cohort question has no worked answer |
| The fix-first decision: the five-line page | Call, evidence, cost, objection, what would change it | None: the programme's own form, built on Week 1's claim, evidence, caveat and action and Tuesday's four moves | Not a sourced claim |
| Videos | IBM Technology, panel data; root cause analysis | https://www.youtube.com/watch?v=LoMgvSfKp6Y, https://www.youtube.com/watch?v=7t3lTYEd_PM (each checked 13 October 2026 through oEmbed) | Titles "Understanding Data Structures: Time Series, Cross-Sectional, and Panel Data Explained" and "What is Root Cause Analysis (RCA)?", channel IBM Technology |
| The row's interview resource | GeeksforGeeks' data analyst interview questions | The page (last updated 24 July 2026) carries no cohort or funnel item: not verified on 13 October 2026, so no learner file cites it | |

### Which decisions did the rebuild make where the plan or the rules left a choice?

| Decision | What the pack does | Why |
|---|---|---|
| Notebook numbers | Concept notebooks 01 to 04 and 08, case notebooks 05 to 07, the lab 12 | The build brief and the gate's rule that a notebook takes its chapter's SECTION number; the plan's 01 to 09 predates that rule |
| The opening | S1 the day's topic, S2 the week map, S3 the five topics, S4 the concept map, S5 the ticket | The brief's order; the plan opened on the ticket |
| Teaching order | Subtopics 1, 3, 4 and 2 in the morning, 5 opening the afternoon | The spine and the plan: cohorts before the curves and the blend read from them, then the funnel |
| The toy guard | Read kind by kind: no toy blend within five points of a planted blend, no toy artefact near 118 and 89, no toy skip share near 31, no toy count equal to the bank's funnel | The plan fixes toy values (24, 80, 26.7) within five points of unrelated plants of another kind; the contract asserts each kind-wise guard |
| The cost on the college | 48 joiners at an assumed Rs 1 to 1.5 lakh, Rs 48 to 72 lakh | Fees come from students who join; the plan's 60 acceptances at Rs 1.2 lakh counts students who would not have joined (facts `corrections`) |
| Applicants | 900 | The plan's 850 gives 28.2 per applicant against the 26.7 its own line uses (facts `corrections`) |
| The gym's dashboard months | January counts the older members only; February adds the January joiners at month one | The dashboard counts from the month after joining (facts `corrections`) |
| The register | One row per member with a column per month, as a register is kept | The plan's long form is the notebook's first step, `melt`, so the file is kept wide (facts `corrections`) |
| SECTIONs 9 to 11 | No notebook; the gate warns three times | SECTION 9 writes a page from notebooks 06 and 07, SECTION 10 is the interview room and SECTION 11 the Kahoot and close; the brief allows none |
| The Week 1 callback | Names the reversal, never its numbers | Week 1 Thursday's finding is a plant; decision `plants-once-found` lets only that week's Saturday paper name it |
| The cheat sheet's concept map | Five topics in two rows, cohort to curve to blend to the call, with the funnel feeding the call | S4's map prints its labels under five points on a sheet; this drawing keeps the same five topics and their order of use |
| The cheat sheet's causes chain | A line of text in panel 5 | The sheet must fit one page with the concept map added |
| Drill timing | Drills c1 to c4 sit inside their chapters (4, 3, 3 and 4 minutes, taken from named slides, each SECTION's notes summing to its allowance); drill c5 and the case drill run in the lab | The plan put each drill in its chapter; the trainer's cold read showed the chapters' slide minutes already filled them, so the fix pass trimmed slides for c1 to c4 and moved the afternoon's two drills to the lab |

### What did the fix pass of 13 October 2026 decide, and which rebuild findings did it leave?

The three rebuild cold reads and the one fix pass are in `internal/C2_W04_D04_cold_reads_INTERNAL.md`.
Each choice the fix pass made where the findings or the rules left one:

| Decision | What the pack does | Why |
|---|---|---|
| The floor rule | Two ages in a row within a point; `floor_of(row, within=0.01)` | Exact equality never fires on a large cohort's shares, so Gold's floor had to be called "one that erodes" against the day's own rule; a batch of ten moves in steps of ten points, so the gym's floors are unchanged |
| Gold's floor | Reached at month two for January to June, eroding about 0.3 points a month; July has not lived month three | `floor_of` on notebook 06's table returns 38.3 to 38.6 for those six rows and nothing for July and August |
| What the floor means | "In any month, about 38 in 100 order, though not always the same 38" (Kahoot Q4's key) | Members come back after a month with no order, so a month-active plateau is not a fixed group of regulars; S18's rule 2 is scoped to members who never return |
| Why Gold's 38 is flat | A slide of 0.3 points a month, refilled by a new cohort near 38.5, which props September by about half a point; the count never sees month one | Held to June's four cohorts, September reads 37.3 against 37.8 (facts `dashboard_sep_june_cohorts_only`, `mix_prop_points_sep`) |
| The per-person funnel | Only the overall is sure to read higher per person, and only when each person converts once; the middle steps' direction is read from the data | One member with many converting sessions pulls a per-member rate below the per-session one; in this data every Gold step but search to menu view, and every college step, reads at least as high per person |
| The low-step rule | "When the overall falls, the step that moved against its own past owns the fall; a low, steady step is how the process runs, and where to invest is a separate question" | The old rule mixed diagnosing a change with choosing where to invest; the no-show is now sized at about 30 joiners if half sat (facts `toy_college_by_group`) |
| The handoff line | S81 and the day sheet carry a corrected line; the spine keeps the old one | See the Graduate 32 row above; the departure is the requester's to ratify |
| Predictions the ticket answered | The ticket drops the 61; S48 asks why the dashboard holds, S61 asks when the Android rate broke; S37 prints blanks | The trainer's read found three predictions answered before they were asked |
| Reveal 2 and the tracking strike | Reveal 2 is handed at S53; tracking is struck at S64 on the order records | Reveal 2 prints S53's split; a moved cut dates the fall and cannot test tracking |
| The cohort table in SQL | The notes' part two carry a `GROUP BY` query and the sparse-table trap | The interviewer's read found no SQL; the query ran on Postgres 16 and on SQLite in the session and printed notebook 06's rows |
| The fallback deck | SECTIONs 12 to 15, 120 minutes, no Kahoot line | Its SECTIONs 7 to 10 collided with the day's; S9 runs 18 minutes so the parts sum to 120 |
| The notes' length | Outside the five topic sections the notes run 2,965 words by a prose count (code, pictures and links left out), the topic sections 2,588 more | The spine caps the notes at 3,000 words and the brief lets the topic sections exceed it; the fixes had pushed the rest to 3,262, so the head's picture paragraph, the two-row "where does this show up" table and the Zomato field note (now a cell of the doubts table) went, and part two was tightened |

| Read, finding | What stayed | Why |
|---|---|---|
| Graduate 20, interviewer 19 (part) | The transcript's "Users or use" row holds cohorts to members who joined before July; notebook 07 holds to before August | Both keep the same members in both months, and both are true; the transcript's stricter hold keeps every cohort out of its first month in both months, and its numbers are in the facts file (`held_july_*`) |
| Graduate 24 | S80's table keeps the blended row under the cohort columns | The row says what each cohort does to the blended count; the diagram beneath draws both cohorts feeding the blend |
| Graduate 31 | The deck's slide titles stay statements, with the question in the italic line | The deck convention sets an action title over each slide's question; learner files' headings are questions |

### Which items stay open for the week read?

- `content/W04/D1/demos/C2_W04_D01_week_explorer_STUDENT.html` draws Thursday's Th2 scene as "a
  coaching centre's batches A and B" (100 at 50 then 40, and 400 at 52.5); Thursday's SECTION 3 now
  teaches the same numbers on the gym's dashboard, and the explorer's day nodes do not yet name
  Thursday's five topics. Both sit outside this folder.
- The spine's Thursday handoff line (`docs/detailing/W04_analyst_craft_spine.md`, section 8) still reads
  "treats a member who has not left yet as if she were retained for ever"; S81 and the day sheet
  carry the corrected line, and the spine sits outside this folder.
- No other day's file names a Thursday slide or notebook by number; a search of `content/W04` for
  `C2_W04_D04_0` and `W04/D4` outside this folder found the Wednesday pre-read's link to Thursday's
  data and the explorer's facts read, neither of which names a slide or a notebook number.

# Where does every Monday fact come from, and what departs from a source?

**INTERNAL.** One page: the written reference that locks each concept chapter's rule, the public facts
with their check dates, the data and the invented examples, the case-file sharpenings, the decisions
the concept-first rebuild of 13 October 2026 took, what was left out, and the cold-read findings that
carry a reason in place of a fix.

## Which written reference locks each concept chapter's rule, and when was it checked?

The row's own references came first, as the rebuild's brief asks. Exponent's address now redirects
to Aced's page, which loads on 13 October 2026 and carries the question "measure whether a new
feature launch was successful" with no north star, guardrail or definition lines; GeeksforGeeks loads
on 13 October 2026 and its metric items are general; Interview Query answered 429 on 13 October 2026,
so it is **not verified on 13 October 2026**. None of the three states a rule a chapter names, so each
rule is locked to the written reference below, and where a rule is the programme's own summary the
table says so.

| Chapter | The rule it names last | Reference | Checked |
|---|---|---|---|
| 1. What to measure and why; the proxy test | A proxy stands in for the thing wanted; the proxy test asks whether a team could hit the number while what it stands for got worse | The row's own words ("if a department could hit the number while the business got worse, the number is a proxy that has drifted"); Chou, "Blending Proxy Metrics with a North Star", arXiv 2606.21745, June 2026, whose abstract describes proxies as metrics used in place of outcomes the experimenter does not observe: https://arxiv.org/abs/2606.21745 | 13 October 2026 |
| 2. North-star and guardrail metrics | A north star best captures the value the people served get; a guardrail is watched so that hitting it does no hidden harm | Amplitude, "What Makes a Good vs Bad North Star Metric" (Julia Sholtz, 15 August 2024): https://www.amplitude.com/blog/good-bad-north-star-metric.md; Spotify Confidence's glossary entry for a guardrail metric: https://confidence.spotify.com/glossary/guardrail-metric | 13 October 2026 |
| 3. Leading against lagging indicators | A leading number moves before the north star while a team can act; a lagging one confirms it | The same Amplitude article: "these are lagging indicators", "Revenue is a lagging indicator", and a good north star as "a leading indicator of revenue" | 13 October 2026 |
| 4. Definitions: numerator, denominator, window, exclusions | Four lines make a number computable | The US Centers for Medicare and Medicaid Services' Measures Management System, "Develop Specifications" (last updated Jun 2026, listing the numerator, denominator and denominator exclusions, with a step to define any time intervals) and "Define the Denominator Exclusions" (last updated Jun 2025, "Denominator exclusions refer to criteria that result in removal of patients or cases from the denominator before calculating the numerator"): https://mmshub.cms.gov/measure-lifecycle/measure-specification/develop-specification and https://mmshub.cms.gov/measure-lifecycle/measure-specification/develop-specification/denominator-exclusions, which redirect to the pages' current addresses | 13 October 2026 |
| 5. Gaming, and definitions that resist it | A definition resists gaming when its numerator needs a receipt, its denominator is set by someone other than the people paid, its clock starts at a system time, its exclusions are dated, and it says what it does not reward | The programme's own summary of four failures, each from a written record: the SEC's 2020 order against Wells Fargo (Release 34-88257) and the VA inspector general's report 14-02603-267, both in the table below | 13 October 2026 |
| 6. The metric definition artifact | The seven-line page: four lines that make the number computable and three that make it safe to pay for | The row's own words, which name the numerator, the denominator, the window, the exclusions, what it deliberately does not reward, the guardrails and the gaming note; the CMS pages above for a measure specified on one written page | 13 October 2026 |

## Which public facts does the pack use, and when was each checked?

Every URL below was first fetched on 12 October 2026 and fetched again on 13 October 2026 for the concept-first rebuild; the ids are the case file's. The rebuild quotes the Q1 FY26 letter's own words, "over 28% of our MTUs" and "a slightly lower number of orders by the same user", and the SEC release's "combined $3 billion settlement with the SEC and the Department of Justice".

| Id | Fact, as used | URL |
|---|---|---|
| M8 | CFPB: USD 100 million, with the OCC's USD 35 million and Los Angeles's USD 50 million, USD 185 million in all, 8 September 2016; roughly 1.5 million deposit and 565,000 credit card accounts that may not have been authorised; the director's words, employees "secretly opened unauthorized accounts to hit sales targets and receive bonuses", which S13's notes quote | https://www.consumerfinance.gov/about-us/newsroom/consumer-financial-protection-bureau-fines-wells-fargo-100-million-widespread-illegal-practice-secretly-opening-unauthorized-accounts/ (checked 13 October 2026) |
| M8 | SEC: USD 3 billion settlement with the DOJ and the SEC, USD 500 million of it the SEC's penalty, February 2020 | https://www.sec.gov/newsroom/press-releases/2020-38 (checked 13 October 2026) |
| M8 | SEC order 34-88257: no usage condition; debit cards counted up to four years unused; the 2013 remittance addition (0.04 of 0.11); simulated funding; surveys dodged; paragraph 17, the cross-sell metric published as "the ratio of the number of accounts and products per retail bank household" and touted to investors; paragraph 18, some executives' pay moved with cross-sell growth; paragraph 20, "the number of products sold continued to be a significant criterion" for judging employees from tellers up, which is why S13 says staff were judged on products sold while investors read the cross-sell number | https://www.sec.gov/files/litigation/admin/2020/34-88257.pdf (checked 13 October 2026) |
| M8 | VA OIG 14-02603-267, page 49: of 40 primary-care schedulers and supervisors asked how they set the desired date, 10 used the date the veteran wanted and "the remaining 30" used the provider's availability or the next available appointment, giving false zero-day waits; 79 staff were interviewed in all, so the earlier "30 of 79" mixed two bases and is gone; the 14-day goal left performance contracts | https://www.vaoig.gov/sites/default/files/reports/2014-08/VAOIG-14-02603-267.pdf (checked 13 October 2026) |
| M1 | Swiggy Q2 FY25 letter: MTU and platform frequency defined; frequency 4.53, MTU 17.1 million | https://www.bseindia.com/xml-data/corpfiling/AttachHis/2495f39b-e1d1-4018-8f69-6ff250345e98.pdf (checked 13 October 2026) |
| M9 | Swiggy Q1 FY26 letter: Maxxsaver used by "over 28% of our MTUs"; AOV up 16 percent quarter on quarter to Rs 612, credited to "a higher non-grocery mix" and Maxxsaver; "Some cart-consolidation led by Maxxsaver and letting go of some low AOV orders and unprofitable users drove a lower order growth"; "the Maxxsaver ramp-up happened entirely during Q1. This kept our absolute Contribution flat QoQ" | https://www.swiggy.com/corporate/wp-content/uploads/2025/07/Q1-FY2026-Shareholder-letter.pdf (checked 13 October 2026) |
| M2 | Eternal Q1 FY26 letter: NOV = GOV minus discounts | https://drive.google.com/file/d/1VtoiLsA2OpKauFnkKIlhXRmnbvxL-6ha/view (checked 13 October 2026) |
| M2 | Eternal Q1 FY27 letter: GOV disclosure sunset, "NOV more accurately reflects underlying performance", said inside the food delivery line, the letter's only GOV mention; the blog page links it and lists Zomato, Blinkit, District and Hyperpure | https://drive.google.com/file/d/1jb9KWd4Ap4RTKHFHxzEOO7jgQqVZEGcd/view ; https://www.eternal.com/blog/q1fy27/ (checked 13 October 2026) |
| M6 | Delhi Metro: 45,35,932 line utilisation on 29 May 2018, a single day, against "nearly 27 lakh commuters taking the rapid transit network daily in February this year", a month's average, so the two differ in window as well as unit; DMRC "did not share the daily average ridership figures" after the new section opened, ridership having "taken a hit after two fare hikes in 2017" (PTI, 30 May 2018); 64.06 lakh journeys on an average day now and the record of more than 81 lakh passenger journeys on 8 August 2025 (The Tribune); 82,44,903 passenger boardings on 17 September 2026, the highest ever, during a bus strike (Republic World carrying DMRC's post); a journey counts each line used (Deccan Herald, PTI, 30 August 2023); that journeys and boardings are one count is the pack's reading, labelled so on S21 | https://www.latestly.com/agency-news/dmrc-uses-new-count-metric-on-traffic-flow-doesnt-share-ridership-190870.html/amp ; https://www.tribuneindia.com/news/delhi/delhi-metro-records-99-95-train-punctuality-in-2026-dmrc/ ; https://www.republicworld.com/india/delhi-metro-breaks-all-time-record-with-8244-lakh-footfall-as-dtc-strike-sends-rush-soaring-2026-09-18-137241 ; https://www.deccanherald.com/india/delhi/delhi-metro-records-highest-ever-footfall-on-aug-29-2666561 (checked 13 October 2026) |
| M5 | Uber 10-K for 2025: a trip counted per paying consumer (an UberX Share ride with three paying riders is three trips); monthly active platform consumers need a completed ride or delivery | https://www.sec.gov/Archives/edgar/data/1543151/000154315126000015/uber-20251231.htm (checked 13 October 2026) |
| M4 | Airbnb S-1: nights booked net of cancellations, minus 4.1 million in March 2020 | https://www.sec.gov/Archives/edgar/data/1559720/000119312520294801/d81668ds1.htm (checked 13 October 2026) |
| M5 | Spotify 20-F for 2025: an MAU has more than zero milliseconds of consumption in thirty days | https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm (checked 13 October 2026) |
| T2 | Aced: interviewers score structure, assumptions and scope before the method | https://www.aced.io/blog/top-data-analyst-interview-questions (checked 13 October 2026) |
| Added | Ziegler and others, "Productivity Assessment of Neural Code Completion", 13 May 2022: the acceptance rate, more than persistence in the code, drives perceived productivity | https://arxiv.org/abs/2205.06537 (checked 13 October 2026) |

Not used, because unverified: Wells Fargo firing counts, the "3.5 million accounts" figure, Goodhart's
wording, the NHS examples.

## Where does the data come from?

`python3 content/W04/D1/internal/C2_W04_D01_generate_INTERNAL.py`, seed 20261026, writes the five
case CSVs, the six invented tables of the concept chapters, the contract (79 lines) and the facts
file; a second run is byte-identical. The invented tables draw nothing from the case's random streams,
and the contract compares `drivers`, `driver_weeks` and `zone_weeks` byte for byte with
`git show origin/main`, so Tuesday's and Thursday's readers of Monday's facts get what they read
before. It reads Thursday's
`data/C2_W04_D04_kalpa_memberships_STUDENT.csv` and v4's orders from
`content/W02/D1/data/C2_W02_D01_warehouse_v4_STUDENT.sql`, and asserts the three case tables against
their checksums on origin/main of 13 October 2026. The Kalpa rebuild of 13 October 2026 rebuilt the
sheet and the morning deck with mermaid-cli 11.17.0 installed in the session, because this
container's default 12.0.0 lays the sheet's anchor out at 744 by 646 and prints its labels at 2.5pt. Tools: Python 3.13.16, pandas
3.0.5, matplotlib 3.11.2, numpy 2.5.3, nbclient 0.11.0, python-pptx 1.0.2, mermaid-cli 11.17.0,
weasyprint 70.0, LibreOffice 24.2.7.2.

## Which invented numbers do the concept chapters use, and where does each live?

Every number of the six invented examples sits in `internal/C2_W04_D01_facts_INTERNAL.yaml` under a
`toy_` id, with `how: invented for the concept chapter on <subtopic>` and the files that print it;
`internal/C2_W04_D01_build_notebooks_INTERNAL.py` stops the build when a number it writes differs
from its id.

| Chapter | The example (invented) | Its numbers, by id prefix |
|---|---|---|
| 1 | A school canteen's ten days: plates 200 a day, tokens 200 then 400 once servers are paid per token; 150 g of rice a plate at Rs 50 a kg; the school bus, 40 then 55 km a day for 30 children, as the your-turn | `toy_canteen_*`, `toy_bus_*` |
| 2 | A driving school of four instructors and 100 learners a year: 100 took the test and 60 passed in 2025; 40 took it and 36 passed in 2026 | `toy_driving_*` |
| 3 | A T20 chase of 160 against 159: 6 an over for ten overs (60 for 3), then 7 to 11, ending on 147 for 7, lost by 12 | `toy_chase_*` |
| 4 | One student's 60-day term: 10 holidays, 40 present, 8 absent, 2 medical; the last 20 working days 14, 4 and 2; a scholarship at 75 percent | `toy_register_*` |
| 5 and 6 | Balaji Kirana, a corner shop in Hyderabad: 50 orders in four weeks (12, 13, 12, 13), all marked done, 40 OTP-confirmed, 35 within 30 minutes of the bill, 6 complaints on the 10 orders with no OTP, Rs 20 a delivery; the weak page "Deliveries, monthly, plus 20 percent" | `toy_kirana_*`, `toy_artifact_*` |

## What does the pack sharpen from the case file?

- The guarantee's window drops "weekday": with weekday windows only, the idle tail's top-up per
  driver-week would exceed the floor's own maximum.
- `driver_weeks` counts `peak_offers` (every showing of a request) and gains `peak_hours_no_trip`;
  the ticket's row reads "offers accepted over offers shown", since a declined request is offered
  again, which is why `zone_weeks` requests and `driver_weeks` offers differ.
- The twelve rows keep the draft's 114 to 88 trips and 1.90 to 1.19 (the case file had 110 and
  1.49), on the orchestrator's instruction, with the reason said on the slide.
- The Kalpa lab runs on Thursday's membership table (the requester's decision of 13 October 2026):
  `kalpa_members` is a byte copy of Thursday's `kalpa_memberships`, v4's own ids C-0151 to C-0270, and
  every placement in `app_reorders` that became an order is one of v4's ten Retail-Plus app orders of
  20 August to 9 September, with v4's id in a new `order_id` column and v4's status; the rest of that
  window is members' presses merged into an open basket, and 10 to 30 September holds only the app's
  own placements. `product_id` is dropped, since a press re-places a past basket and Wednesday's
  order items list several products per order. The per-member comparison counts the 107 who joined by
  19 August. No warehouse SQL file is written; `order_id` joins to the Week 2 warehouse as it stands.
- The cheat sheet's ticket sits in its top band, the six topics' map in panel one and the finished
  case board in panel two, since the brief asks for a topic panel printing the concept map and the
  spine for the board; the sheet now runs to two pages, as Friday's does.
- S70's invented pair (S19 before the renumbering) is rebuilt (X at 2.0 trips an hour for 10 hours,
  Y at 0.5 for 40) so its average errs high, as the city's 1.71 does against 1.58; notebook 08 and the
  board work carry the same pair.

## Which decisions did the concept-first rebuild of 13 October 2026 take?

| Decision | Why |
|---|---|
| Chapter 2's coaching batch became a driving school, every number and step of the plan kept | The brief: Thursday's deck opens its cohort chapter on two coaching batches |
| Monday's kirana is Balaji Kirana, in Hyderabad | The brief: Tuesday's is Ramesh's and Wednesday's is Sharma Kirana in Pune |
| The chase ends on 147 and loses by 12 to the other side's 159 | The plan printed 148 in one place and "lost by 12" in another; the spine's "lost by 12" is kept |
| Chapter 4's window is the term's last 20 working days, read 14 / 20 = 70.0 | The plan read 14 / 20 as "the second month alone", and this register's second month holds 25 working days |
| Chapter 1's opener carries the row's words with no quotation marks | The first build quoted them, because `scripts/build_deck.py` read a topic opening on "What" as a question; pull request 254 fixed that rule on main (80d0952), which this branch merged, so the quotes came off |
| The fallback deck's sections became 13 to 16 | 6 to 9 collided with the new concept chapters, and 12 is the lab's notebook number |
| The lab notebook was renamed to 12 and not executed again | The brief keeps the lab as merged; the build script rebuilds it only when asked for by number |
| Notebook 07 lost its canteen cells and gained a picture of the offers each driver accepted, counts only | The canteen belongs to chapter 1; the picture keeps three pictures and adds no new case figure |
| SECTIONs 10 and 11 each pair with a notebook numbered as the chapter: 10 `gaming_page_three_roles` and 11 `new_feature_definition_page` | The orchestrating session's review of 13 October 2026 asked for it, since the gate warns on a case chapter with no notebook; notebook 10 tests each line of the page against the way of gaming it must resist and each role's objection on the tables, and notebook 11 checks the hire-grade answer's numbers and drafts the coding assistant's page with `missing_lines`. Five numbers they print are new ids read from the same tables (`north_star_after_idle_off` 36.88, `online_driver_weeks_after_idle_off` 5,354, `idle_online_driver_weeks_after` 1,080, `idle_tph_before` 1.90 and `idle_tph_after` 0.80), so the data files are unchanged |
| Notebook 03 carries no case cell | The two-examples rule: the chase is the concept chapter's example, and notebook 09 reads which of Uber's numbers moved first |
| Complaints are counted per 100 orders billed | "Per 100 deliveries" divided by orders billed, which include the 10 parcels never delivered |
| Chapter 4 names four lines that make a number computable, and leaves "complete" to the seven-line page | The row calls a definition complete only when it also says what it does not reward |
| The definition-lines set is `four_definition_lines_set` | The plan's `definition_lines_set` shares its prefix with the guided `definition`, and the distractor audit keyed the guided file from the wrong solution |
| The slide minutes were re-cut to the spine's envelope | Chapter 5's prediction (S39) gained 30 seconds; round 1 (S58) gave two minutes to the hand count (S60, S62), so chapter 7 runs 12 and 20; S87 and S90 gained the minute and a half chapter 10's opener already counted, so it runs 25 |
| The saving moved from notebook 09 to notebook 10 | The trainer's read (T10): notebook 09 runs in the morning and printed Rs 92.7 lakh and Rs 58.0 lakh, the answer round 3 asks groups to choose after lunch; notebook 09 now stops at the top-up split |
| "The acceptance floor" is named apart from "the Rs 300 floor" everywhere | The graduate's read (G47): one word named both the hourly earnings guarantee and the least share of offers a driver-week must accept to earn it; the scheme is judged by completed trips, and the Rs 300 floor is paid only for weeks that clear the acceptance floor |
| A guardrail is defined as sitting beside the number being chased | The graduate's read (G11) and the interviewer's (I20): chapter 2's guardrail watched the pass rate, the number the school chased, while the north star it names fell |
| The four-lines set's Q1 pair is 80.0 against 84.0 | The interviewer's read (I11): 80.0 against 66.7 differed in the denominator and in the days counted, so two keys could be argued; 84.0 differs from 80.0 in the numerator alone |
| Kahoot Q7's key is the numerator's receipt condition, kept text at the next commit | The interviewer's read (I23): the D1 plan keyed the line on what the number does not reward, and that line only names a behaviour and cannot stop a numerator that still counts it; S95's note and chapter 5's receipt rule both say the numerator does the work |
| The north-star set's option b and the artifact set's option a were rewritten | The interviewer's read (I20, I21): option b could also catch the move, and option a was a guardrail in name only; option a is now a growth target, the second north star the stem warns against |
| The kirana table's typed dispatch is capped at 3 minutes after the bill, with no new random draw | The graduate's read (G38): 12 of 50 rows put the typed dispatch before the bill existed; the cap changes only `minutes_from_typed_dispatch` in `data/C2_W04_D01_kirana_deliveries_STUDENT.csv`, a contract line now checks it (80 of 80 pass), and the case CSVs are byte-identical |
| The cost per extra trip keeps Rs 2,836 and adds near Rs 7,400 net of the rise in requests | The interviewer's read (I4): requests rose 1.8 percent, so at the old fulfilment rate of 0.89 the new requests alone give 228,335 trips and about 2,565 of the 6,700 came from the scheme; the four numbers are new ids (`fulfil_rate_before`, `trips_expected_after_old_rate`, `extra_trips_net_of_demand`, `topup_per_net_extra_trip_rs`) read from the same tables |
| The handoff line names no company | The trainer's read (T14): the faculty brief, a sync block, ties the test to Kalpa's tree while the spine says the redesign; the line says "the redesign", which both readings fit, and the day sheet tells the trainer to park "is the fall real?" for the block |
| The lab note is kept as merged | The brief keeps the Kalpa lab as it is; the day sheet schedules the concept sets' Q2 and Q3 after the lab note's four parts (T17) |
| The clinic's S6 prints the lead-and-lag handout's Q1, in its order and with its letters | The trainer's read (T20): S6 and the handout numbered the same eight numbers differently, so a trainer reading S6's key to a room holding the handout would mark right answers wrong; matching S6 to the handout keeps the lab note's rule that a room which sat the drill in the clinic skips it in the lab (the TA's read of 13 October 2026, finding 27) |
| The fallback clinic's sections 15 and 16 were re-timed to their totals | The trainer's read (T18): the slide notes summed to 109 of 120 minutes; S6 runs 12, S7 6, S9 13 and S10's close 2, and S4's note says why the clinic's finance and marketing readers argue numbers other than their round 1 cards (T19) |
| The test's unit is named, and the deck does not choose it | The interviewer's read (I5) and the graduate's (G51): zones leak when drivers cross zone lines, and 835 of the 1,200 drivers have more than one busiest zone (`zone_mode`) across the twelve weeks; S92 lists zones, single drivers and the whole city switched window by window and leaves the choice to the tentative faculty block, while the transcript's candidate picks the city switched window by window and says why |
| The public cases were re-read against their sources and tightened | The interviewer's read (I16, I17, I18, I28): Wells Fargo judged staff on products sold while investors read the cross-sell number (CFPB; SEC order paragraphs 17, 18 and 20); the VA count is 30 of 40 schedulers and supervisors (page 49); Swiggy's slower order growth is credited to cart consolidation and dropped low-value orders and users, with contribution held flat; Eternal's GOV sunset sits in its food delivery line; Delhi Metro's two figures differ in window as well as unit |
| The board work follows the deck's order and labels | The trainer's read (T2, T7, T21): the question and the room's headline go up at S5, the topic map mirrors S4 with chapter 2 feeding chapter 6 and the case node in the known colour, and round 3's defence runs 6.5 minutes |
| The pre-read defines AI-free | The graduate's read (G48): the row's agenda reads "The AI-free business case, individual and written: one page on a short Kalpa brief, handed in"; the pre-read says only that, and nothing about marks |

## Which cold-read findings carry a reason in place of a fix?

G numbers are the fresh graduate's findings and I numbers the hiring interviewer's, in
`internal/C2_W04_D01_cold_reads_INTERNAL.md`. The slide numbers in this table are the merged pack's of
12 October 2026, before the concept chapters; `internal/C2_W04_D01_renumber_INTERNAL.py` prints where
each went.

| Finding | Why it carries a reason in place of a fix |
|---|---|
| G7 | S2's later-day words are the spine's week map, and each day defines its own words when it reaches them. |
| G8 | S2's Kalpa labels follow the spine, whose Monday node now reads "Kalpa Retail: reorders per member" (pull request 233), so no morning slide names the window the lab finds. |
| G10, in part | Anchor, drift, crux, baseline, tail, segment, test accounts and diagnostic are said aloud with their meaning, and glossing all eight would crowd the slides. |
| G14, in part | What a group hands in for round 1 and how it is scored is the trainer's to say from the war-game run sheet. |
| G18 | The 880 hold 1.90 together (186,200 trips over 98,000 hours, then 193,800 over 102,000); A to D are four of them and vary week to week. |
| G30 | S24 states the check and notebook 02 runs it, which is where a proof belongs. |
| G34, in part | Crore in prose, lakh on a chart's axis and the Indian grouping in an option a learner types are each the form that place reads best in. |
| G35, I7, in part | `topup_rs` keeps the case file's totals (Rs 1.9 crore, Rs 1.159 crore, Rs 82.3 a trip), which the data was settled to hit; regenerating it from a per-window rule is the orchestrator's call, and the report names it. |
| G61 | "That lead" points at the driver-operations lead named earlier in the same sentence. |
| G64 | E's and F's 21 September weeks are in the picture at 0.29 and 0.25, each a bar one driver-week high beside bars near 300. |
| G69 | Inline `<- correct` keys are the Kahoot pack format the model pack set (W01 D1 and W02 D5 carry eight each), and the distractor audit reads them there. |
| G71 | Week 2 Friday taught the grain, and its lab and take-home use the word; the warehouse is a distractor. |
| G75 | The section opener's subtitle says what happens in it. |
| G90 | The week's explorer is the orchestrating session's to build at `demos/C2_W04_D01_week_explorer_STUDENT.html`; the notes name its scenes. |
| I1, I24, in part | The north star and the AI variant's kept-text outcome are the spine's; the candidate owns the north star's weakness aloud and reads time to merge beside kept text. |
| I2, in part | S30's two inputs are the spine's tree, and the transcript, S47 and the notes lead with requests per online hour by zone. |
| I4, I12, in part | The tables hold zone-week medians and no trip earnings, so a ride-weighted p90 wait and a driver-earnings guardrail cannot be computed from them. |
| I15, in part | The afternoon's interview room runs [S] and the AI variant; [D] runs in the clinic's section 9, as the spine places it. |
| I21 | PTI's copy, republished by LatestLY on 30 May 2018, reads "nearly 27 lakh commuters ... daily in February this year"; the page answered a plain fetch on 12 October 2026. |
| I28, in part | "[S] a staple asked everywhere" in the exercise index is the curriculum schema's own tag definition (docs/05_Curriculum_Map_Schema.md). |
| I30, in part | Kahoot Q7 follows the spine's AI variant, where kept text is the outcome. |

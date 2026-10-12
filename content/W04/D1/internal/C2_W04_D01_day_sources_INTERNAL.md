# Where does every Monday fact come from, and what departs from a source?

**INTERNAL.** One page: the public facts with their check dates, the data, the case-file sharpenings,
what was left out, and the cold-read findings that carry a reason in place of a fix.

## Which public facts does the pack use, and when was each checked?

Every URL below was fetched on 12 October 2026; the ids are the case file's.

| Id | Fact, as used | URL |
|---|---|---|
| M8 | CFPB: USD 100 million, with the OCC's USD 35 million and Los Angeles's USD 50 million, USD 185 million in all, 8 September 2016; roughly 1.5 million deposit and 565,000 credit card accounts that may not have been authorised | https://www.consumerfinance.gov/about-us/newsroom/consumer-financial-protection-bureau-fines-wells-fargo-100-million-widespread-illegal-practice-secretly-opening-unauthorized-accounts/ (checked 12 October 2026) |
| M8 | SEC: USD 3 billion settlement with the DOJ and the SEC, USD 500 million of it the SEC's penalty, February 2020 | https://www.sec.gov/newsroom/press-releases/2020-38 (checked 12 October 2026) |
| M8 | SEC order 34-88257: no usage condition; debit cards counted up to four years unused; the 2013 remittance addition (0.04 of 0.11); simulated funding; surveys dodged | https://www.sec.gov/files/litigation/admin/2020/34-88257.pdf (checked 12 October 2026) |
| M8 | VA OIG 14-02603-267: 30 of 79 Phoenix staff used a wrong desired date; the 14-day goal left performance contracts | https://www.vaoig.gov/sites/default/files/reports/2014-08/VAOIG-14-02603-267.pdf (checked 12 October 2026) |
| M1 | Swiggy Q2 FY25 letter: MTU and platform frequency defined; frequency 4.53, MTU 17.1 million | https://www.bseindia.com/xml-data/corpfiling/AttachHis/2495f39b-e1d1-4018-8f69-6ff250345e98.pdf (checked 12 October 2026) |
| M9 | Swiggy Q1 FY26 letter: Maxxsaver over 28 percent of MTUs; AOV up 16 percent to Rs 612, which Maxxsaver helped raise; cart consolidation and dropped low-value orders slowed order growth | https://www.swiggy.com/corporate/wp-content/uploads/2025/07/Q1-FY2026-Shareholder-letter.pdf (checked 12 October 2026) |
| M2 | Eternal Q1 FY26 letter: NOV = GOV minus discounts | https://drive.google.com/file/d/1VtoiLsA2OpKauFnkKIlhXRmnbvxL-6ha/view (checked 12 October 2026) |
| M2 | Eternal Q1 FY27 letter: GOV disclosure sunset, "NOV more accurately reflects underlying performance"; the blog page links it and lists Zomato, Blinkit, District and Hyperpure | https://drive.google.com/file/d/1jb9KWd4Ap4RTKHFHxzEOO7jgQqVZEGcd/view ; https://www.eternal.com/blog/q1fy27/ (checked 12 October 2026) |
| M6 | Delhi Metro: 45,35,932 line utilisation on 29 May 2018 against nearly 27 lakh riders a day in February 2018 (PTI, 30 May 2018); 64.06 lakh journeys; 82,44,903 boardings on 17 September 2026 | https://www.latestly.com/agency-news/dmrc-uses-new-count-metric-on-traffic-flow-doesnt-share-ridership-190870.html/amp ; https://www.tribuneindia.com/news/delhi/delhi-metro-records-99-95-train-punctuality-in-2026-dmrc/ ; https://www.republicworld.com/india/delhi-metro-breaks-all-time-record-with-8244-lakh-footfall-as-dtc-strike-sends-rush-soaring-2026-09-18-137241 (checked 12 October 2026) |
| M5 | Uber 10-K for 2025: a trip counted per paying consumer (an UberX Share ride with three paying riders is three trips); monthly active platform consumers need a completed ride or delivery | https://www.sec.gov/Archives/edgar/data/1543151/000154315126000015/uber-20251231.htm (checked 12 October 2026) |
| M4 | Airbnb S-1: nights booked net of cancellations, minus 4.1 million in March 2020 | https://www.sec.gov/Archives/edgar/data/1559720/000119312520294801/d81668ds1.htm (checked 12 October 2026) |
| M5 | Spotify 20-F for 2025: an MAU has more than zero milliseconds of consumption in thirty days | https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm (checked 12 October 2026) |
| T2 | Aced: interviewers score structure, assumptions and scope before the method | https://www.aced.io/blog/top-data-analyst-interview-questions (checked 12 October 2026) |
| Added | Ziegler and others, "Productivity Assessment of Neural Code Completion", 13 May 2022: the acceptance rate, more than persistence in the code, drives perceived productivity | https://arxiv.org/abs/2205.06537 (checked 12 October 2026) |

Not used, because unverified: Wells Fargo firing counts, the "3.5 million accounts" figure, Goodhart's
wording, the NHS examples.

## Where does the data come from?

`python3 content/W04/D1/internal/C2_W04_D01_generate_INTERNAL.py`, seed 20261026, writes the five
CSVs, the contract and the facts file; a second run is byte-identical. Tools: Python 3.13.16, pandas
3.0.5, matplotlib 3.11.2, numpy 2.5.3, nbclient 0.11.0, python-pptx 1.0.2, mermaid-cli 11.17.0,
weasyprint 70.0, LibreOffice 24.2.7.2.

## What does the pack sharpen from the case file?

- The guarantee's window drops "weekday": with weekday windows only, the idle tail's top-up per
  driver-week would exceed the floor's own maximum.
- `driver_weeks` counts `peak_offers` (every showing of a request) and gains `peak_hours_no_trip`;
  the ticket's row reads "offers accepted over offers shown", since a declined request is offered
  again, which is why `zone_weeks` requests and `driver_weeks` offers differ.
- The twelve rows keep the draft's 114 to 88 trips and 1.90 to 1.19 (the case file had 110 and
  1.49), on the orchestrator's instruction, with the reason said on the slide.
- The Kalpa tables are held byte-identical to the draft: `RP-` member ids, booked value from
  `app_reorders`, no manual reorders in the window, and no warehouse SQL file.
- The cheat sheet's ticket sits in its top band and the concept board in panel one, since the spine
  asks for both in first position.
- S19's invented pair is rebuilt (X at 2.0 trips an hour for 10 hours, Y at 0.5 for 40) so its
  average errs high, as the city's 1.71 does against 1.58; notebook 02, the notes and the board work
  carry the same pair.

## Which cold-read findings carry a reason in place of a fix?

G numbers are the fresh graduate's findings and I numbers the hiring interviewer's, in
`internal/C2_W04_D01_cold_reads_INTERNAL.md`.

| Finding | Why it carries a reason in place of a fix |
|---|---|
| G7 | S2's later-day words are the spine's week map, and each day defines its own words when it reaches them. |
| G8 | S2's Kalpa labels are the spine's, and tying S37 to the auto-reorder window in the morning would point at the lab's plant. |
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

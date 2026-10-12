# W04 D4 sources: every public fact with its check, every correction, every open item

INTERNAL. One page for the reviewer. Every link below was fetched on 12 October 2026 in the finishing
session; R2 ids are the case file's (`docs/detailing/W04_case_file.md`, "Public facts allowed on
Thursday").

## Which public facts does the pack use, and what did the check confirm?

| R2 | Fact as the pack states it | Source, checked 12 October 2026 | What the fetch confirmed |
|---|---|---|---|
| Th4 | Gold at 1.8 million members in Q4 FY23; members' orders about 30 percent of food delivery GOV in March 2023; order frequency up about 60 percent after joining; Gold members get free delivery | https://www.bseindia.com/xml-data/corpfiling/AttachHis/42b3bf3b-1edb-4da7-849a-87ca9da27ff8.pdf (checked 12 October 2026) | All four from the PDF's text, page 4 and the Q4 answer: "orders from Zomato Gold members (with free delivery benefit) now comprise as much as ~30% of our total GOV (Mar-23) ... increased by ~60% post becoming members" |
| Th1 | Blinkit: 46 percent of a cohort's customers order in the fourth quarter after acquisition, on average; NOV retention 150 percent at Q4 and 279 percent at Q12; a cohort spends nearly 3x three years on | https://drive.google.com/file/d/1jb9KWd4Ap4RTKHFHxzEOO7jgQqVZEGcd/view (checked 12 October 2026), linked from https://www.eternal.com/blog/q1fy27/ (checked 12 October 2026) | The letter's Blinkit section, re-read in the fix pass: "Q4 retention (% of customers placing at least 1 order in the 4th quarter after acquisition): average across all cohorts is 46%" and "a cohort of customers is spending nearly 3x with us three years after acquisition than they did in their first quarter" |
| Th2 | Instamart: the cohort acquired in Q4 FY24 spends 4.14x in its sixth quarter what it spent in its acquisition quarter; Swiggy "weaned away certain users from the platform with low potential Lifetime values"; average order value up about 40 percent year on year; the table states no denominator | https://www.swiggy.com/corporate/wp-content/uploads/2025/10/Q2-FY2026-Shareholder-letter.pdf (checked 12 October 2026) | The quotes and the 4.14x, from the PDF's text; the base quarter is Q0, the quarter of acquisition |
| Th3 | Platform MTU up 27.4 percent year on year; platform frequency 4.13 to 3.87, Q1 FY26 to Q1 FY27 (6.3 percent, our arithmetic); more than 4 million unprofitable Instamart users weaned over three quarters; Instamart's one-month retention of its transacting user base 61 percent from 55 | https://nsearchives.nseindia.com/corporate/SWIGGY_30072026154100_Covering_Letter_Letter_to_Shareholders_-_signed.pdf (checked 12 October 2026) | All four, from the PDF's text; the 61 sits in the letter's Instamart answer |
| Th5 | Amplitude: 7 percent of a cohort back on day seven puts a product in the top 25 percent for activation, from more than 2,600 companies; the blog gives no method | https://www.amplitude.com/blog/7-percent-retention-rule (checked 12 October 2026) | "analysis of over 2,600 companies ... you've crossed into the top 25% for activation performance"; no method on the page |
| M6, T3 | DMRC: 64.06 lakh journeys a day "currently", all days; the record 82,44,903 boardings on 17 September 2026, a bus-strike day; the earlier record of more than 81 lakh passenger journeys on 8 August 2025; journeys count each line a rider uses | The Tribune, https://www.tribuneindia.com/news/delhi/delhi-metro-records-99-95-train-punctuality-in-2026-dmrc/ (checked 12 October 2026); Republic World quoting DMRC's post, https://www.republicworld.com/india/delhi-metro-breaks-all-time-record-with-8244-lakh-footfall-as-dtc-strike-sends-rush-soaring-2026-09-18-137241 (checked 12 October 2026); Deccan Herald (PTI), 30 August 2023, https://www.deccanherald.com/india/delhi/delhi-metro-records-highest-ever-footfall-on-aug-29-2666561 (checked 12 October 2026); PTI via LatestLY, https://www.latestly.com/agency-news/dmrc-uses-new-count-metric-on-traffic-flow-doesnt-share-ridership-190870.html/amp (checked 12 October 2026) | "Journey or line utilisation is calculated by the number of corridors passengers use to reach their destinations"; the 82.44 lakh boardings beat the 81 lakh passenger-journeys record, so both are one line-use count |
| T2 | Aced: on its sample metric drop, define the metric, rule out a data issue first, segment before a root cause, keep fewer users apart from fewer views each | https://www.aced.io/blog/top-data-analyst-interview-questions (checked 12 October 2026) | The sample answer to "a 10% drop in Facebook's daily post views" and its commentary; byline "Aced Team", no date |
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

## Which items stay open for the orchestrator?

- Wednesday's pre-read for Thursday (`origin/w04-d3`) prints "60,000 members" and "the August group
  signed up in a sale week"; Thursday's data holds 53,089 members, and 8,027 of August's 13,000 joined
  in the sale week.
- Monday's lab (`origin/w04-d1`) and Thursday's lab share the window of 10 to 30 September; the
  shared constants are checked in the generator against Monday's facts file and agree.
- Monday's `kalpa_members` names the 120 Retail-Plus members `RP-0001` to `RP-0120` with its own
  `member_since` dates; Thursday's `kalpa_memberships` uses v4's own customer ids (`C-0151` and on),
  which join to the Week 2 warehouse, with Thursday's dates. The two days' Kalpa tables do not join.
- The case file's DMRC catch and its Aced line (R2 M6, T3 and T2) want the same corrections in any
  other day that uses them.

## Which cold-read findings were not fixed, and why?

Every other finding of both reads is fixed in the pack; `internal/C2_W04_D04_cold_reads_INTERNAL.md`
says where.

| Read, finding | What stayed | Why |
|---|---|---|
| Graduate 37 | The three reveals stay in the STUDENT cards file, and the Kahoot file marks its keys | The deck's answer slides print every reveal's numbers, so the cards spoil nothing the deck does not; the model pack's Kahoot file marks its keys the same way, since it is the file loaded into Kahoot; the staff printing line moved to the trainer's run sheet |
| Graduate 40, the posting place | No file names where letters are posted | The programme's facts name no posting channel, so the trainer names it in the room |
| Graduate 32, the handoff line | S45 keeps "treats a member who has not left yet as if she were retained for ever" | It is the spine's handoff line, said word for word; S36 and the notes now say what the table does with young cohorts |
| Graduate 75, Gold's price | The pack names Gold's free delivery and no price | No source checked in the session states a price; the benefit comes from Zomato's own letter |
| Graduate 76, sections against chapters | Sections 4 to 6 stay sections | The spine sets three chapters for the morning; the section 4 subtitle now says the afternoon adds no new idea |
| Interviewer, sourcing 9 | The Eternal citation is the company's results page and the letter's copy it links | The exchange filing of the letter could not be found in the session; the quoted lines were re-read from that copy |
| Interviewer, sourcing 7 | The DMRC unit rests on PTI's report of DMRC's definition and on the record's framing | No DMRC release was fetched in the session |
| Interviewer 25, the supply-side cross-check | Named in the guesstimate, never computed | Train counts and capacities were not verified in the session, so no number is given |
| Interviewer 14, cost per retained user | Named in the AI variant without a number | The variant is invented; a cost figure would be a fabricated fact |

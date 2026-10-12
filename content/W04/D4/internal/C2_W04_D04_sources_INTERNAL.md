# W04 D4 sources: every public fact with its check, every correction, every open item

INTERNAL. One page for the reviewer. Every link below was fetched on 12 October 2026 in the finishing
session; R2 ids are the case file's (`docs/detailing/W04_case_file.md`, "Public facts allowed on
Thursday").

## Which public facts does the pack use, and what did the check confirm?

| R2 | Fact as the pack states it | Source, checked 12 October 2026 | What the fetch confirmed |
|---|---|---|---|
| Th4 | Gold at 1.8 million members in Q4 FY23; members' orders about 30 percent of food delivery GOV in March 2023; order frequency up about 60 percent after joining | https://www.bseindia.com/xml-data/corpfiling/AttachHis/42b3bf3b-1edb-4da7-849a-87ca9da27ff8.pdf (checked 12 October 2026) | All three sentences, page 4 and the Q4 answer, from the PDF's text |
| Th1 | Blinkit: Q4 retention 46 percent on average across cohorts; NOV retention 150 percent at Q4 and 279 percent at Q12 | https://drive.google.com/file/d/1jb9KWd4Ap4RTKHFHxzEOO7jgQqVZEGcd/view (checked 12 October 2026), linked from https://www.eternal.com/blog/q1fy27/ (checked 12 October 2026) | The letter's Blinkit section, quoted; the blog page itself carries only the headline results |
| Th2 | Instamart cohorts indexed to the Q4 FY24 cohort's first quarter (414 percent at Q6); users with low lifetime value weaned away; "retained user cohorts" | https://www.swiggy.com/corporate/wp-content/uploads/2025/10/Q2-FY2026-Shareholder-letter.pdf (checked 12 October 2026) | The table and both phrases, from the PDF's text |
| Th3 | MTU up 27.4 percent; platform frequency 4.13 to 3.87 (6.3 percent, our arithmetic); more than 4 million unprofitable Instamart users weaned over three quarters; one-month retention 61 percent from 55 | https://nsearchives.nseindia.com/corporate/SWIGGY_30072026154100_Covering_Letter_Letter_to_Shareholders_-_signed.pdf (checked 12 October 2026) | All four, from the PDF's text; downloaded with a browser user agent |
| Th5 | Amplitude's 7 percent on day seven as a top-quarter mark, method unpublished | https://www.amplitude.com/blog/7-percent-retention-rule (checked 12 October 2026) | Michele Morales, 30 September 2025, a benchmark of more than 2,600 companies, no method given |
| M6, T3 | 64.06 lakh average daily journeys (2026); 82,44,903 boardings on 17 September 2026; the 2018 line count | The Tribune, Republic World and LatestLY URLs in `trainer/C2_W04_D04_guesstimate_TRAINER.md` (each checked 12 October 2026) | As R2 records them |
| T2 | Aced: tracking first, segments before a root cause, fewer users apart from less use | https://www.aced.io/blog/top-data-analyst-interview-questions (checked 12 October 2026) | Page live; the order as R2 records it |
| New | Simpson's 1951 paper; the label about twenty years later | https://en.wikipedia.org/wiki/Edward_H._Simpson (checked 12 October 2026) | Title, journal and "twenty years later" on the page |
| Reading | Mixpanel cohorts; Amplitude funnels; pandas 10 minutes | https://mixpanel.com/blog/cohort-analysis/, https://amplitude.com/blog/funnel-analysis, https://pandas.pydata.org/docs/user_guide/10min.html (each checked 12 October 2026) | Each returned HTTP 200 |
| Video | IBM Technology, panel data; root cause analysis | https://www.youtube.com/watch?v=LoMgvSfKp6Y, https://www.youtube.com/watch?v=7t3lTYEd_PM (each checked 12 October 2026) | Titles and channel through oEmbed; lengths 11:39 and 8:32 from R3 of the same day |

## Which corrections to the case file does the pack carry?

Each is also in the facts file's `corrections` block, with the arithmetic.

| Case file | The pack | Why |
|---|---|---|
| The dashboard blends everyone who joined before the month | Month-two retention: members two or more months past joining | With every cohort falling and August at 31, a blend that counts August cannot hold at 38 |
| 60,000 members | 53,089 | Seven cohorts of about 5,000, August's 13,000 and September's 5,089 |
| Twelve rows: August 2 of 5; September 6 of 12 | 1 of 5; 3 of 12 | 6 of 12 needs members to return, which breaks every cohort falling; 2 of 5 sits a point from Kalpa's 41 |
| `events.member_id` | `user_id` with `is_member` | The ticket compares non-members on Android |
| Kalpa retention on orders | On app activity, the spine's fallback | 37 of the 120 Retail-Plus customers ordered in September in v4 |

## Which items stay open for the orchestrator?

- Wednesday's pre-read for Thursday (`origin/w04-d3`) prints "60,000 members" and "the August group
  signed up in a sale week"; Thursday's data holds 53,089 members, and 8,027 of August's 13,000 joined
  in the sale week.
- Monday's lab (`origin/w04-d1`) and Thursday's lab share the window of 10 to 30 September; the
  shared constants are checked in the generator against Monday's facts file and agree.
- Monday's `kalpa_members` names the 120 Retail-Plus members `RP-0001` to `RP-0120` with its own
  `member_since` dates; Thursday's `kalpa_memberships` uses v4's own customer ids (`C-0151` and on),
  which join to the Week 2 warehouse, with Thursday's dates. The two days' Kalpa tables do not join.

## Which cold-read findings were not fixed, and why?

Filled after the fix pass; every finding not fixed in the pack carries its one-line reason here.

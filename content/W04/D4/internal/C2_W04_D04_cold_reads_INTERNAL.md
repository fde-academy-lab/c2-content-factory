# Week 4 Thursday: the two cold reads

INTERNAL. Two separate agents read the pack cold on 12 October 2026, each on the opus model, each
told to report findings only and never to edit. Their reports are below as they returned them; what
the fix pass did with each finding is in the last section of this file, and every finding not fixed
carries its one-line reason in `internal/C2_W04_D04_sources_INTERNAL.md`.

## Read 1: a fresh graduate who opens only the STUDENT files, in a learner's order

The reader: 23, never worked in a company, not strong in maths, met `pivot_table` last week. The
files, in order: half one, the case-file cards, notebook 01, the guided set, notebook 02, the chapter
2 drill, notebook 03, the chapter 3 drill, half two, the fix-first set, the interview transcript, the
Kahoot, notebook 04, the Kalpa set, the practice set, the six solutions, the take-home and its
self-check, the study notes, the cheat sheet, Friday's pre-read, the fallback deck and the exercise
index.

**Overall impression (as returned).** Some of the day was clear: the hand count on the twelve-member
card, the coaching-batch toy, rebuilding September's 37.8 as 13,218 of 35,000, the carousel
explanation of the 118 percent, the release-split chart, and the fix-first set (whose "numbers you
need" box finally let me work out 1,317 myself). The invented drills (Kaapi, Dabba Club) were the
easiest to do alone. My answers: ch2 "bcad", ch3 "acbd", fix-first "bdacba", Kalpa "dacb" and lab set
"cabadb" all matched their keys. On the guided set I posted "cabb" against the key "cabd", so I got
Q4 wrong. I got lost in five places. (1) Words: "month-two retention" against the "month two" column;
"sale" naming three different groups; "everyone problem", "mix" and "artefact" never defined;
"session" never defined; "leaving" meaning "did not order this month". (2) Numbers with no working or
no source: 72.5 to 55 next to 58 to 44, 20.5 and 33 for October, 0.23 and 0.61, 1.36 and 1.20, 0.9
points, and the 47 and 43 from moving the cut. (3) The toy funnel where 100 visits become 50
sessions. (4) The evening lab, which leans on a monsoon sale and an auto-reorder window I could not
place, builds a calendar-month table the morning told me not to read, asks for a "baseline", and
leaves five overlapping write-ups with no order. (5) The take-home, which stopped me at the week
arithmetic.

**Counts.** 77 findings: 2 blockers, 30 majors, 45 minors.

The findings, as returned, numbered 1 to 77:

1. half1 S1 rows 1 and 2 (also S2, S12): month-two retention, cohort and blend are used nine slides
   before they are defined. Major.
2. half1 S1, data line: 53,089 members; the cohorts on S23 and August add to 48,000, and no file says
   the other 5,089 joined in September. Minor.
3. half1 S1 data and caveats (and chapter 3): session, event, stage, mapped, release and home
   carousel are never defined; checkout version is listed and never used. Major.
4. half1 S1 row 4 against S3 (and the cards, notebook 03, S35): two before-and-after pairs (58 to 44,
   72.5 to 55) with no line showing 0.80 x 72.5 = 58 and 0.80 x 55 = 44. Major.
5. half1 S1, S3, S5, the notebooks' tickets: "everyone problem" is never defined, and "it is both"
   cannot be read when the second problem is members on Android only. Major.
6. half1 S3 and S37: the 1,317 shows neither the 44 percent nor the divide by 17, times 7. Minor.
7. half1 S2: the Monday and Tuesday slogans mean nothing read cold; Wednesday's box leads nowhere.
   Minor.
8. half1 S4, S34, S36, S42, the notes, the chapter 3 drill: why a fall that survives a moved cut
   rules out a tracking change is never said; 47, 56 and 43 are computed in no notebook; the drill's
   billing-record test is never used in the morning. Major.
9. half1 S4 cause 4: "every cohort in the same calendar month" against the sheet's and the notes'
   "never in the same calendar month". Major.
10. half1 S5, S7, the cards, the guided set: "twelve real members" reads as real Zomato customers.
    Minor.
11. half1 S7: "ZG40539 to ZG42328" reads as a range of about 1,800 ids. Minor.
12. half1 S9 against S18: 75 and 67 on the card against 52 and 50 on the full table, with nothing
    saying the twelve were chosen to show the pattern. Minor.
13. half1 S10, S18, notebook 02 cell 8, Kahoot Q4: "month-two retention" (the dashboard) and "month
    two" (a cohort's column) are two numbers near 38; notebook 02's curves draw "dashboard 38" across
    an age axis. Major.
14. half1 S13 subtitle, notebook 01 cell 12: "every batch shrinks" when batch B is new. Minor.
15. half1 S13 against S20 and S23, the notes' interview table, Kahoot Q3: the toy's mechanism (a big
    young batch) is given as the case's, where the counted cohorts are all about 5,000 and the big
    one, August, is low and not counted. Major.
16. half1 S14, fallback S1 and S3, the transcript: Q4, NOV, indexed, FY24, weaned and lifetime value
    unexplained; 150 and 279 percent make no sense; Eternal is never named as Zomato's parent; S5
    promised a chart and S14 shows two cards. Major.
17. half1 S15, the transcript, the Kalpa solution: "[F]" and "mix" never defined, yet "split mix from
    rate" is a scored line. Major.
18. half1 S17, notebook 02 cells 2 to 5: why the year is times 12, why the mean of True and False is a
    share, and what `mm` is, none shown. Major.
19. half1 S18 and the triangle: every cohort lands near 38.5 in month two whatever its month one, so
    what the flat 38 hides, apart from August, is unclear. Major.
20. half1 S18, S26, the sheet, the transcript: "points" against "percent" never explained. Minor.
21. The triangle and the GIF: "Aug (sale) 13,000" calls the whole August cohort sale; the light cells
    change shade with no key. Minor.
22. half1 S20 against notebook 02 cell 14: 38.05 printed as 38.0. Minor.
23. half1 S23: "the newest cohorts sit highest" when July, 38.5, sits below June, 38.6. Minor.
24. half1 S25, notebook 02 cell 18, the notes: "falls as July's did" read as a ratio gives 24, not
    20.5; no cell computes October's 33 or the 32 to 34. Major.
25. "Sale" across files names the August cohort (13,000), the sale-week members (8,027) and the week
    of 17 August (9,108). Major.
26. half1 S28: the stem already says per session, so key d's condition is met; option c names the
    step the day later blames. Minor.
27. half1 S29, notebook 03 cell 2, the notes, the guided set Q4: 100 visits then 50 sessions; "10 of
    50" is not a step over the step before; Q4's "membership lead's chart" pushed to b. Blocker.
28. half1 S30: "menu views with no search" in a table of sessions; the 89 percent's working is not
    shown. Minor.
29. half1 S32, notebook 03 cell 10, Kahoot Q5, the practice set Q3: "artefact" never defined. Major.
30. The two-unit funnel picture: three per-member numbers never discussed; 64 against 84 at the
    broken step with no word on which shows the loss; two purples unexplained. Minor.
31. The release-split picture: "1 Aug" and "3 Aug" two days apart; the release line drawn between 7
    and 14 September; "cart to order" against "add-to-cart to order". Minor.
32. half1 S36 censoring row, half2 S45, the notes: the check cell holds a statement; how the table
    treats anyone as retained for ever is not shown. Major.
33. half1 S36 seasonality row: a hypothetical cause with a reported result no notebook computes.
    Minor.
34. half1 S36 last row: "before and after is not cause" beside the release split reads as saying the
    release finding is not causal either. Major.
35. half1 S36 selection row: "its organic members" after "the sale-week members". Minor.
36. half1 S37: Amplitude's day seven, "vendor" and "top-quarter" unexplained; "survivors mistaken for
    growth" tied to nothing. Minor.
37. The case-file cards and the Kahoot: staff printing lines in a learner file; the reveals and the
    quiz keys printed for anyone reading ahead. Minor.
38. Notebooks 01, 03 and 04: melt, the -1 for May, a two-function pivot, shift, sets, a double
    unstack, a cross merge and fillna each with one comment line. Major.
39. Notebook 01 cell 11 chart: rows labelled by month and channel, with no member ids. Minor.
40. Every exercise file: L1 to L6, "screens", "GCC", "design call" and where to post the letters
    explained only in the index, read last. Minor.
41. Notebook 02 cell 8 chart: no legend; January darker; August a single dot. Minor.
42. The chapter 2 drill Q2 and Q3: 36.9 is both January's September rate and the plain average.
    Minor.
43. Notebook 03 cell 9: two close purples; each table row names one stage for a step between two.
    Minor.
44. Notebook 03 cell 13: a web platform the ticket never mentions. Minor.
45. half2 S38, the fix-first page, notebook 04 cell 10, the Kalpa set, the practice set: five
    overlapping write-ups with no order and no owner. Major.
46. half2 S40: 0.23 and 0.61 orders per member, computed in no notebook. Major.
47. The transcript, the solutions, the notes, S43: 1.36 and 1.20, computed in no notebook, and
    `member_months` has no platform column. Major.
48. half2 S41, S42, S3, the notes: "judge the next sale on its own cohort curve before buying it",
    when a sale's cohort has no curve until it runs. Major.
49. half2 S43 against S4 and the sheet: two ladders with different names and lengths. Minor.
50. half2 S44 and the transcript's AI section: "look like recovery" when actives never fell; "keep
    arriving" said of one cohort. Major.
51. half2 S46 against the Kahoot: the item numbers on the slide do not match the quiz; "floor" never
    taught. Minor.
52. Business words: "already bought", "friction", "hire-grade", "refill the top of the funnel",
    "sprint", "monthly transacting users", "cohort-level levers". Minor.
53. The fix-first set Q5: S39 says "bring the split", which is option c's wording. Minor.
54. The transcript: Aced is unexplained and unlinked. Minor.
55. Kahoot Q4 with the deck title, the notes and the sheet: "leaving" has meant not ordering all day,
    and nothing says a member who skips a month is still a member. Major.
56. Notebook 04 cell 0, the Kalpa set: no channel column and no sale dates, so the monsoon-sale
    members are guessed to be the August joiners. Major.
57. Notebook 04 cells 0 and 6, the Kalpa set: what auto-reorder does, and whether it is the suspect or
    the fix, is never said. Major.
58. Notebook 04 cell 0: "active" and "blended" change meaning from the morning; the head asks about
    frequency and the lab measures app opens. Minor.
59. Notebook 04 cell 4: the typed lines build cohorts by calendar month, the layout the morning
    warned against, and give 48 raw counts with no check. Major.
60. Notebook 04 cell 8, the Kalpa table: checkouts over all sessions is not a step over the step
    before. Minor.
61. Notebook 04 cell 10, the Kalpa second page: "baseline" is a Friday word; no cell builds the second
    route and nothing gives an expected output. Major.
62. The Kalpa set Q4 and its solution: a looks stronger than b on about 2 checkouts, and the solution
    calls a defensible. Major.
63. The Kalpa set Q2 key: the August cohort has one month, so it cannot have fallen. Minor.
64. The practice set Q6: cohort C new in June sits in June's blend, when June is its month zero.
    Minor.
65. The practice set Q5: renewals never defined for Dabba Club. Minor.
66. The take-home brief and fallback S4: no way shown to get a week gap from two dates; nothing says
    `member_id` and `user_id` are one person; "W-SUN" beside "weeks start on Monday". Blocker.
67. The self-check: "wobble a few points" beside a 21-point drop. Minor.
68. The self-check against fallback S6: "the last month leaves the count" against "the last month
    counts". Minor.
69. The notes: the Delhi Metro guesstimate appears in no other learner file; DMRC is not spelled out.
    Minor.
70. The notes' glossary leaves out the words the reader struggled with; ORIGIN never says "Simpson's
    paradox". Minor.
71. The sheet's panels 1 and 3: "panel" means two things; the "Over" column says "All of them" twice.
    Minor.
72. The pre-read's checks: notebook 04 ends on empty cells, not checks; "cohort channel". Minor.
73. Fallback S5 picture: the five non-sale weeks share one colour. Major.
74. Fallback S1, S7, S8: Q6, GOV unexplained; "holdout" against Friday's "hold-out". Minor.
75. All files: what Gold costs and gives a member is never said. Minor.
76. The section and chapter headers: sections 1 to 3 are chapters, section 4 is not a chapter 4.
    Minor.
77. The GIF's first frame: at the end of February it already shows later cohorts' sizes. Minor.

## Read 2: a hiring interviewer who runs analyst screens at Uber, Swiggy, Google and an AI startup

The reader scored the hire-grade answers of both transcripts on the scorecard, re-checked the
disputed numbers against the pack's data files and every public source live, and edited nothing.

**Verdict (as returned).** The [S] hire-grade answer as written: Swiggy a lean hire for up to two
years' experience, Uber borderline, Google a lean no, an AI startup a no. The [D] answer's stakeholder
moves would score anywhere; its evidence lines fail the second push. The order of the walk is above
the bar; what fails is the rigour behind the lines a hard interviewer probes first: a count check
that cannot tell a renamed event from a broken checkout, comparators quoted on another step, a
users-or-use ratio that is itself a blend, a 35.9 with no comparator, a cost in order value with no
range, and nothing on app version, sample size or noise. A candidate reciting twenty case numbers the
interviewer never supplied would sound rehearsed everywhere.

**Scores.** [S] hire-grade: 10 of 14 against the file's 14, because the file's "what earned the 2"
column credits four lines the transcript does not contain (the renamed event, 13,218 of 35,000 outside
a follow-up, Rs 5.3 lakh at Rs 400, the six-move roadmap). [D] hire-grade: 9 of 14 against the file's
12.

**Counts.** 25 findings: 1 blocker, 14 majors, 10 minors; and 10 sourcing items.

The findings, as returned, numbered 1 to 25:

1. The AI variant (the transcript, half2 S44, the trainer file, the day sheet): "launched three
   weeks ago" and then judged at week four, which no cohort has reached. Blocker.
2. The transcript's step row, follow-up 2, the trainer's [D] follow-up 1 and the fix-first solution:
   the comparators 57 to 56 and 52 to 51 are add-to-cart to order, on another step from the one
   blamed; on checkout start to order, iOS members ran 71.25 to 70.0 and non-members on Android 65.0
   to 63.75, so "nobody else fell" is loose. Major.
3. The step row, the [D] follow-up 2 and the scorecard: moving the cut a week cannot separate a
   renamed event that shipped with the release from a broken checkout; the [S] answer never reports
   the mapping; "the orders table agrees" proves nothing independent when member_months equals the
   event log; the weekly series (58 to 59 for seven weeks, then 45, 43, 44) dates the break better.
   Major.
4. The users-or-use row (also the trainer's push 1, the notes, S40's notes, the solution's Q4): 1.36
   to 1.20 against 1.34 to 1.40 is itself a cohort blend; among members who joined before August,
   iOS holds at 1.45 and Android falls from 1.45 to 1.24. Major.
5. The cohorts row and follow-up 1: every cohort lands at 38.5 to 38.9 in month two and slides 0.3
   points a month, a plateau; the propping is worth about half a point; the hard push is "so is there
   a cohort problem?", and the answer is that month one fell (58 to 49), which the dashboard excludes
   by design, and August sits at 31. Major.
6. The number row and the close: the drop is never shown; counted over everyone who joined before the
   month, the series reads 40.9, 40.0, 39.5 and then 35.9. Major.
7. The close and the scorecard's cost row: no range, no upper-bound caveat, no reversal fact; Rs 5.3
   lakh is order value, of which Zomato keeps its take; netting the comparators gives about 1,220 to
   1,290 a week; the loss is about a quarter of Android members' orders (5,064 a week before). Major.
8. The step row and the [D] answer: no split by checkout version; every Android session moved to v2
   on 14 September, so date and version are confounded, and the answer should say so. Major.
9. The step row, follow-up 2 and [D]: no sample size; 55 rests on 18,273 starts (under a point
   either way), the non-member comparator on about 1,600 (about 2.4 points). Major.
10. The close, half2 S41 and S42: whether the sale paid back is never asked; the sale is judged on
    each member's contribution over months against the discount. Major.
11. The trainer's [D] follow-up 1: "members on iOS joined in the same sale and held at 57 to 56" is
    all iOS members; sale-week members on iOS fell from 62.7 to 43.5; the clean test is members who
    joined before August (Android completion 70.3 to 53.6, iOS 68.6 to 69.3), with the sale cohort as
    Android-heavy as every cohort. Major.
12. The trainer's upper-bound answer: it leans on the blended ratio; "most" is unquantified; the 17
    days in the log already answer it: after a failed checkout the member ordered within a day 36.5
    percent of the time before and 35.1 after, so retries did not rise. Major.
13. The whole hire-grade column and the rubric: the interviewer never answers the clarifying
    questions or hands over data, yet the candidate recites about twenty numbers; "named with the
    day's number" rewards recitation. Major.
14. The AI section and S44: nothing on what active means for a writing assistant, output quality,
    cost per retained user or the launch channel; "never the blended count" overreaches; "looks like
    recovery" contradicts the record. Major.
15. The guesstimate's validate and catch rows: DMRC's "passenger journeys" counts each line used, and
    the 82.44 lakh record beat an earlier 81 lakh "passenger journeys", so the two are likely one
    series under two names; "average daily" is not weekdays; the page commits the error it was built
    to catch. Major.
16. The number row: "month-two retention counts members from their second month" reads as one
    cohort's month-two rate. Minor.
17. The clarifying questions: none asks whether retained means renewed or ordered. Minor.
18. The structure: no external or supply-side branch (delivery time and fees, restaurants, a Gold
    price change, a competitor, a festival week). Minor.
19. The close: no forward warning that October reads about 33. Minor.
20. Follow-up 3: the Swiggy letter says "low potential Lifetime values", its table states no
    denominator, and weaning in one quarter lifts a diagonal of the table rather than every column.
    Minor.
21. The [D] "what would change it" row: non-members falling changes who owns the step, and "I'll
    rerun it on your mapping" hands the check to the disputing team. Minor.
22. The [D] concession: the question as spoken never raises the sale members; the next step names no
    member-only code path. Minor.
23. The [D] rank follow-up and push 2: the lever is the loss's size and a cheap reversible test.
    Minor.
24. The pain-point table: Swiggy's row is "more users, less use each", its frequency platform-wide
    and year on year; the synthetic row sits under a heading that promises real cases. Minor.
25. The guesstimate: the 15 percent riding share is unanchored, "about 6 percent low" is false
    precision, and there is no supply-side cross-check. Minor.

The sourcing items, as returned:

1. Aced: no URL; the page's lines come from commentary on a drop in Facebook's daily post views; its
   stated order starts with the metric's definition; the byline is "Aced Team", undated.
2. Swiggy Q2 FY26: misquoted ("low potential Lifetime values", page 12); "per retained" is inference;
   no URL in the transcript.
3. Swiggy Q1 FY27: verified; needs "year on year" and "platform"; the 61 percent is Instamart's base;
   no URL in the transcript.
4. Amplitude: the blog says "top 25% for activation performance" and gives no method; "method
   unpublished" overstates.
5. Zomato, 19 May 2023: verified word for word; no URL in the transcript.
6. The AI variant's "week four or later" is a rule of thumb stated as fact.
7. DMRC 64.06 lakh: The Tribune says "currently", so "in 2026" is the pack's gloss; the unit is open
   in the week's research file.
8. DMRC 2018 line count: the LatestLY page returned 403; cite DMRC's post as quoted.
9. Eternal and Blinkit: a Google Drive copy is unstable for a listed company's letter; "spend" renders
   NOV retention; "since those who stay spend more" is inference.
10. Simpson 1951: cite the paper itself.

## What did the fix pass do with each finding?

Every finding was fixed in the pack, or fixed in part with the rest given its one-line reason in the
sources list. Decks were rebuilt, every changed notebook re-executed, the cheat sheet reprinted.

**Read 1, the fresh graduate (77): 72 fixed, 5 fixed in part.**

| Finding | What changed |
|---|---|
| 1 | Fixed: S1's table names month one; S3 carries month-two retention, cohort problem and everyone problem; S12 names the blend in its stem. |
| 2 | Fixed: S1 says 53,089 joined January to September; S25 and notebook 02 place September's 5,089 in month zero. |
| 3 | Fixed: S1 defines a session and the event rows and names v1 and v2; S30 and the notes define the carousel; notebook 03 defines session, stage, step and release and uses `checkout_version` in a check. |
| 4 | Fixed: S3, S35, notebook 03 (a printed product and a check) and the notes show 0.80 x 72.5 = 58 and 0.80 x 55 = 44. |
| 5 | Fixed: S1's ask and S3 define both problems; S3 now says the order loss hits every signup month on one platform. |
| 6 | Fixed: S37 and notebook 03 show 0.14 x 22,841 = 3,198 in 17 days, 188 a day, 1,317 a week. |
| 7 | Fixed: S2's nodes say each day's question in plain words, and every day now leads to Saturday. |
| 8 | Fixed: S34 says the moved cut dates the fall and cannot test tracking; S36, notebook 03 and the notes test tracking on the order records, which is the chapter 3 drill's billing-record test; notebook 03 computes 47, 43 and 56. |
| 9 | Fixed: S4 row 4, the sheet's crux and the notes say cohorts are compared at one age and one calendar month is read across them only to look for a shock that hit everyone. |
| 10 | Fixed: S5, S7, the cards, the guided set and notebook 01 say members of the case data, which is synthetic. |
| 11 | Fixed: S7, the sheet's panel 2 and the cards name the four members one by one. |
| 12 | Fixed: S9 and notebook 01 say the twelve were picked to show the pattern, with the full data's 52 and 50. |
| 13 | Fixed: S20, notebook 02 and the notes say the dashboard is no cohort's month-two column; the curves lost the dashboard line. |
| 14 | Fixed: S13 and notebook 01 say the old batch shrinks. |
| 15 | Fixed: S13, notebook 01, the notes' interview table and the transcript keep the toy's big batch apart from the case's gentler prop and name month one and August as what the flat number hides. |
| 16 | Fixed: S14, fallback S1 and S3 and the transcript open Q4, NOV, Q0 and Q6, FY, weaned and lifetime value, and name Eternal as the company behind Zomato and Blinkit; S5 promises reports. |
| 17 | Fixed: S15 and the transcript define [F] and mix; the scorer line defines mix. |
| 18 | Fixed: S17's code comments and notebook 02 explain `mm`, year x 12 and the mean of True and False. |
| 19 | Fixed: S18, S3, notebook 02 and the notes say every cohort lands near 38.5 and the flat number hides month one and August. |
| 20 | Fixed: S18, notebook 02 and the notes define a point. |
| 21 | Fixed: the triangle and the GIF say Aug with no sale label, use one tint after month one and carry a key. |
| 22 | Fixed: notebook 02 prints one decimal, 38.0. |
| 23 | Fixed: S23 says the rates rise with youth, July 38.5 beside June 38.6. |
| 24 | Fixed: S25, notebook 02 and the notes say July's 10.5 points; notebook 02 computes October's 33 and the 32 to 34. |
| 25 | Fixed: the sweep leaves the August cohort (13,000), the sale-week members (8,027) and the sale week's cohort (9,108) as three names, each one meaning. |
| 26 | Fixed: S28's key now asks for the split against the weeks before, and option c names the first step. |
| 27 | Fixed (blocker): S29, notebook 03, the notes and the guided set count the toy in sessions, read 10 of 100 sessions against 10 of 20 people, and Q4 asks what the chart needs. |
| 28 | Fixed: S30's table counts sessions only and shows 116,797 of 131,974. |
| 29 | Fixed: S30, notebook 03, Kahoot Q5, the practice set and the notes define artefact. |
| 30 | Fixed: S32 and notebook 03 read the per-member panel and say why neither panel shows the ticket's loss; one colour and a key. |
| 31 | Fixed: the release split sits on a date axis with the release line on 14 September and says add-to-cart to order. |
| 32 | Partly: S36 and the notes say what the table does with young cohorts; S45's spine line stays (sources list). |
| 33 | Fixed: notebook 02 computes September by zone, 0.9 points. |
| 34 | Fixed: S36's last row and the notes say the release split has comparison groups and Gold's 60 percent has none. |
| 35 | Fixed: S36 says the August cohort's organic members. |
| 36 | Fixed: S37's notes and the notes say who Amplitude is and what its 7 percent means; the pitfall reads a rate over stayers read as growth. |
| 37 | Partly: the staff line moved to the trainer; the reveals and the Kahoot keys stay (sources list). |
| 38 | Fixed: notebooks 01, 03 and 04 explain melt, the -1, the two-function pivot, shift, sets, unstack, the cross merge and fillna. |
| 39 | Fixed: notebook 01's chart labels each row with its member id. |
| 40 | Partly: every set now opens its levels, design calls, screens and GCC; no posting place is named (sources list). |
| 41 | Fixed: notebook 02's curves carry a legend and say August has one month on record. |
| 42 | Fixed: the chapter 2 drill's Q2 no longer prints 36.9; its solution gives the three September rates. |
| 43 | Fixed: notebook 03 uses violet and amber and labels each row as a step between two stages. |
| 44 | Fixed: S1 and notebook 03 name android, ios and web. |
| 45 | Fixed: S38, the index, notebook 04 and the Kalpa set name two pages and their order, with notebook 04's three sentences as the second page's first lines. |
| 46 | Fixed: notebook 02 computes 0.23 and 0.61. |
| 47 | Fixed: notebook 03 joins each member's platform from the events and computes the ratio, and the transcript, the notes, S40 and the solution now use the cohorts held fixed. |
| 48 | Fixed: S3, S41, S42, the notes, the solutions and the trainer files say work out whether the sale's members pay back their discount. |
| 49 | Fixed: S43 uses the board's five names plus the call. |
| 50 | Fixed: S44 and the transcript say the blended count stays near the record as each week's cohort joins. |
| 51 | Fixed: S46's cards match the quiz's items; floor is gone from the slide. |
| 52 | Fixed: already bought, friction, sprint, refill the top of the funnel, monthly transacting users and cohort-level levers replaced; hire-grade defined where used. |
| 53 | Fixed: the fix-first set's option c no longer borrows S39's words. |
| 54 | Fixed: the transcript names Aced and links it with its date. |
| 55 | Fixed: S3, the Kahoot, the notes and the notebooks' ticket say a member with no order in a month is not retained that month and is still a member. |
| 56 | Fixed: notebook 04 and the Kalpa set say the August joiners are the monsoon-sale members. |
| 57 | Fixed: notebook 04, the Kalpa set and the lab note say what auto-reorder did and that it is the window's suspect. |
| 58 | Fixed: notebook 04 and the Kalpa set say active and blended change meaning and frequency is read through app opens. |
| 59 | Fixed: notebook 04's typed lines build the table by age, print rates with each cohort's size, and carry a check. |
| 60 | Fixed: notebook 04 says September's two checkout rates run end to end, from opening the app. |
| 61 | Fixed: notebook 04 says the rate before the window, adds the second route's lines, its empty cell and what it must print. |
| 62 | Fixed: the Kalpa set's Q4 rests on the monsoon cohort holding September's blend up (26 of 32; 23 of 88 without it), and the solution no longer calls a defensible. |
| 63 | Fixed: the Kalpa key says older cohorts fell. |
| 64 | Fixed: the practice set's Q6 says cohort C joined in May and June is its month one. |
| 65 | Fixed: the practice set defines Dabba Club's plan and a renewal. |
| 66 | Fixed (blocker): the take-home shows how to get a week from two dates with a worked example and says user_id is the member_id; fallback S4's comments explain W-SUN and the week gap. |
| 67 | Fixed: the self-check separates a one-point tick from the large falls. |
| 68 | Fixed: the self-check and fallback S6 say September is whole and counted and the week of 28 September is left out. |
| 69 | Fixed: the notes spell out DMRC and say what its count counts. |
| 70 | Fixed: the notes' glossary adds blend, session and artefact, and ORIGIN names Simpson's paradox. |
| 71 | Fixed: the sheet says the grid and drops the repeated column. |
| 72 | Fixed: the pre-read says notebook 04 stops at the lab's cells and sends errors to the TA. |
| 73 | Fixed: the weekly picture gives each signup week its own colour and marker. |
| 74 | Fixed: fallback S1, S7 and S8 open Q6 and GOV and spell hold-out as Friday does. |
| 75 | Partly: the pack names Gold's free delivery from Zomato's letter; no price (sources list). |
| 76 | Partly: section 4's subtitle says the afternoon adds no new idea; sections stay sections (sources list). |
| 77 | Fixed: the GIF shows a cohort's size only once it has joined. |

**Read 2, the hiring interviewer (25 findings and 10 sourcing items): 23 and 8 fixed, 2 and 2 fixed in part.**

| Finding | What changed |
|---|---|
| 1 | Fixed (blocker): S44, the transcript, the trainer file and the day sheet put the AI question two months after launch. |
| 2 | Fixed: the transcript, S35, S42, fallback S9, the role card, the fix-first set and solution, the cards and the notes put the comparators on the step blamed (iOS members 71 to 70, non-members on Android 65 to 64). |
| 3 | Fixed: the tracking check is the order records against the event log in S36, notebook 03, the transcript and the trainer files; the moved cut is said to date the fall only; the weekly series is quoted. |
| 4 | Fixed: notebook 03 holds the cohorts fixed (1.45 to 1.24 on Android, 1.44 and 1.45 on iOS) and shows the blended ratio's false iOS rise; every file that used 1.36 to 1.20 now uses the held-fixed reading. |
| 5 | Fixed: S3, S18, the transcript and the notes say the base is steady near 38.5 and what fell is month one and August. |
| 6 | Fixed: the transcript hands over the series and the hire-grade answer reads 40.9, 40.0, 39.5 and 35.9; S25 and the notes carry it. |
| 7 | Fixed: the cost is 1,223 to 1,317 orders a week, a quarter of 5,064, Rs 3.7 to 6.6 lakh of order value of which Zomato keeps its fees, in the transcript, S37, S40, S42, the fix-first set and the notes. |
| 8 | Fixed: notebook 03 checks every Android session from 14 September ran v2; S34's notes and the transcript say date and version are one split. |
| 9 | Fixed: notebook 03, S35's notes and the transcript size the 55 on 18,273 starts and the comparator on 1,600. |
| 10 | Fixed: the transcript, S41, S42 and the notes judge the sale on payback against the discount. |
| 11 | Fixed: the [D] follow-up uses members who joined before August (70.3 to 53.6 against 68.6 to 69.3) and states the 70 percent Android mix. |
| 12 | Fixed: the upper-bound push uses retries (36.5 then 35.1 percent within a day) and the 1,223 to 1,317 range; notebook 03 computes both. |
| 13 | Fixed: the transcript's interviewer answers every clarifying question with the numbers the candidate then uses, and the rubric scores asked-then-used. |
| 14 | Partly: the variant defines active on a kept draft, adds the share of drafts kept and the cost per retained user, and keeps the blend for load and spend; no cost number (sources list). |
| 15 | Fixed: the guesstimate validates trips against DMRC's line-use count, says all days, and treats the record as the same count on a strike day. |
| 16 | Fixed: the transcript says the label misleads and what it counts. |
| 17 | Fixed: the transcript asks whether retained means ordered or renewed. |
| 18 | Fixed: the transcript names the outside causes and the check that clears them. |
| 19 | Fixed: the transcript's close warns that October reads about 33. |
| 20 | Fixed: the transcript, S14 and the fallback quote 'low potential Lifetime values', say the table states no denominator and that weaning lifts that quarter's cells and later ones. |
| 21 | Fixed: the [D] answer's what-would-change line uses the order records and retries. |
| 22 | Fixed: the [D] question raises the sale members, and the next step names a member-only path to check. |
| 23 | Fixed: the rank follow-up and push 2 use the loss's size and a two-day reversible test. |
| 24 | Fixed: the pain-point table relabels Swiggy's row, says platform-wide and year on year, and marks the synthetic row. |
| 25 | Partly: the riding share carries the widest range and is named as the least sure input; the false precision is gone; the supply-side check is named, never computed (sources list). |

| Sourcing item | What changed |
|---|---|
| 1 | Fixed: the transcript and S43's notes cite what Aced's page says, with its link and date. |
| 2 | Fixed: the quote is the letter's; the link is in the transcript. |
| 3 | Fixed: year on year, platform and Instamart's base are named; the link is in the transcript. |
| 4 | Fixed: top 25 percent of more than 2,600 companies, no method given. |
| 5 | Fixed: the link is in the transcript. |
| 6 | Fixed: week four is labelled the programme's rule of thumb. |
| 7 | Partly: 'currently' and all days now; the unit rests on PTI's report (sources list). |
| 8 | Fixed: the LatestLY page returned HTTP 200 in the fix pass; DMRC's post is quoted as Republic World carries it. |
| 9 | Partly: the letter's own words replace 'spend'; the exchange copy was not found (sources list). |
| 10 | Fixed: the notes cite the paper's DOI. |

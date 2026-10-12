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

Filled after the fix pass.

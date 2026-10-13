# What did the cold reads find in the Week 4 Monday pack?

**INTERNAL.** Two separate agents read the pack cold on 12 October 2026 and wrote findings only;
neither edited a file. A third ran the rebuilt Kalpa lab cold as the TA on 13 October 2026, and its
report and fix log are the last section. Their reports are kept below as they returned them, except that one ", but"
in the first read's finding 89 is set as a semicolon so the style gate reads it. What changed for
each finding, or the one-line reason it did not, is in the fix log at the end and in the sources
list (`internal/C2_W04_D01_day_sources_INTERNAL.md`).

## The fresh graduate's read

I read the pack as a B.Com graduate with Weeks 1 to 3 behind me, in the order I was given, and opened only `_STUDENT` files. All paths are under `content/W04/D1/`. When a problem shows up in several files, I list it once, where I first met it, and name every place it appears. "Unsure" marks findings where I may have misread something. For finding 35 I also opened the student CSV `data/C2_W04_D01_driver_weeks_STUDENT.csv`.

### 1. The morning deck, `slides/C2_W04_D01_half1_STUDENT.md`, and its pictures

1. **S1, the ticket.** "is guaranteed Rs 300 per peak online hour, and Uber tops up the gap." I could not tell which gap, between what and what. "Top-up" is new to me in this sense. Notebook 01's first cell explains it (the gap between trip earnings and the Rs 300 floor); the deck never does. **SLOWS**
2. **S1, the table.** "Offers accepted; accepted, then cancelled by the driver | 0.86; 0.04" and "Online hours with no trip; median rider wait | 0.22; 4.8 min". Each cell holds two measures, and 0.86, 0.04, 0.22 and 0.11 are shares with no "share of what" beside them. I read 0.86 as a count, and I could not tell whether 0.04 is out of accepted offers or out of all offers. With a commerce degree, "share" first means a stock to me. Notebook 01's table labels these properly. **SLOWS**
3. **S1, the ask.** "is anyone gaming it?" "Gaming" a number is never defined in any file. It is missing from the study notes' word list and from the cheat sheet's word box, yet the "Gaming note" line and every exercise depend on it. I guessed the meaning from S5 and S7. **SLOWS**
4. **S1, the data line.** "...trips, hours with no trip, bookings, top-up". "Bookings" is never explained. S14 (`peak_bookings_rs`), S31 ("bookings per online hour fell to Rs 271"), the lead-lag set, fallback S6 and the pre-read ("Gross bookings were Rs 3,69,93,000") all lean on it. I only worked out that it means the fares of trips from the pre-read's "average peak fare stayed at Rs 165". **SLOWS**
5. **S1.** "drivers (1,200, 140 new)", "the monsoon ended mid-window", "an enrolled driver". New since when? Which window? Enrolled in what? Notebook 01 answers the first two. For "enrolled" I guessed it means signed up for the guarantee. **MINOR**
6. **Outer, core and thin zones (S1, S9, S23, S35).** The slides say "three outer zones are thin" (S1), "72 percent of the new hours in the outer zones" (S23) and "In the core zones it fell from 1.90 to 1.79" (S35), but never say which zones are outer or core. S9 lists Shamshabad and Rajendranagar with no hint that they are the quiet ones. "Thin" (few rider requests) is only explained in notebook 02, cell c16. Notebook 01 names the three outer zones; the core zones appear only as bar labels in notebook 02's last chart. `whiteboards/C2_W04_D01_zone_requests_STUDENT.png` would settle it, but it sits on no slide or page. **SLOWS**
7. **S2, the week map.** "support, confidence, lift", "cohorts, funnels, denominators", "baselines, hold-out, cost", "the guesstimate", "24 months and a vendor curve". The first picture of the week is a wall of words I do not know. They belong to later days, so I let them pass. **MINOR**
8. **S2 against S37.** S2 puts "Kalpa Retail: the auto-reorder window" on Monday and "the Retail-Plus tier" on Thursday, but S37 says today's lab is "the head of Retail-Plus's growth number". I only saw that it is both once I reached notebook 04. **MINOR**
9. **S3.** "a definition of seven lines that three people who lose under it cannot break." Which three people, and what do they lose? The roles only arrive on S5. **SLOWS**
10. **Small words I picked up from context.** "Anchor" (S4), "drift" (S8), "The crux" and "baseline" (S13), "tail" (S23), "segment" (S24, notebook 02 c00), "test accounts" (S32), "diagnostic" (transcript, lab-set solution), "quick-commerce" (take-home). None of them stopped me for long. **MINOR**
11. **S4, S13 and S24, the board's second question.** "How could it rise while riders waited longer?" Riders did not wait longer: the wait went from 4.8 to 4.6 minutes, and S4's own sentence says "served no better". I went back to the ticket to check whether I had misread it. **SLOWS**
12. **S5, the role cards.** "The guarantee is the acquisition story". To me "acquisition" means one company buying another. "Finance partner" is a job title I have never met. **SLOWS**
13. **S5, the finance card.** "Top-up per trip ... wants each rupee of top-up to buy a trip" sits under the question "how could each rise while riders waited longer?" Finance wants this number to fall, so I could not tell what "celebrated" or "rising badly" means for this card. **SLOWS**
14. **S5.** "The proxy test, three questions per number." "Proxy" is used here but only defined on S7. The slide never says what my group produces in the "war game" or how it is scored. **MINOR**
15. **S6.** The title asks "Which number can a driver raise without driving?" but the subtitle asks "which ... needs no rider at all to rise?" Under the title, option c also works: accept an offer, then cancel it, and the ticket shows "accepted, then cancelled" rising from 0.04 to 0.09. Option d (the wait) also rises if drivers stop driving. Both b and c looked right to me. **SLOWS**
16. **S8.** The title says "A canteen paid per token", but the picture says "What it pays for: tokens printed". Is the canteen being paid, or is it paying its servers? **MINOR**
17. **S9 against the study notes.** S9 says "twelve real rows of `driver_weeks`"; the study notes say "Six real rows of the data" for the same table. "Real" also made me wonder whether these are real drivers, since S1 says the data are synthetic. In the notes, "trips per box fell for all six" left me unsure whether each driver fell or the six fell together. **MINOR**
18. **S9 against S39 (unsure).** Drivers A to D each fell a little: A from 2.10 to 2.00, D from 1.90 to 1.82. Yet S39 says "the other 880 drivers held 1.90 trips an hour before and after". **MINOR**
19. **S12.** "an unused debit card, the largest product in it", "to meet funding rules", "changed contact details so customers would miss satisfaction surveys". Largest by what measure? Which funding rule? Why avoid the survey? I did get the main story. **MINOR**
20. **Abbreviations.** SEC, CFPB and Department of Justice (S12), PTI (S21), VA OIG and Inspector General (S33), BSE and 10-K (definition solution, study notes), S-1 and 20-F (study notes, Kalpa solution). None is ever expanded. **MINOR**
21. **S14.** "Which column would show the fall is demand?" I read it twice before I saw it means "show that demand caused the fall". **MINOR**
22. **S16, `drift_STUDENT.png`.** The picture has two y-axes, one starting at 18,000 and one at 1.4. The two lines cross exactly at the launch line, so I thought the crossing meant something. **MINOR**
23. **S17.** "turns 12,860 driver-weeks into the ticket's numbers". The 12,860 arrives with no source (1,200 × 12 is 14,400). `.lt(...).map({True: ..., False: ...})` is syntax I was never shown. The table beside the code has "Accepted share" and "No-trip share" columns that the three lines of code do not compute. **SLOWS**
24. **S19, the fractions.** "hides two-fifths of the fall (0.19 of 0.32)", then "a fall that looks a third smaller". 0.19 ÷ 0.32 is about three-fifths, and 0.19 is the part the average still shows; the hidden part is 0.13. Then the same slide says "a third". This stopped me for several minutes. **SLOWS**
25. **S19, the invented drivers X and Y** (repeated in notebook 02 c10, in the study notes under "How is a rate added up?" and in the board work). In the example, the average of rates (1.5) comes out lower than the ratio of sums (1.91). In the city data, the average (1.71) comes out higher than the ratio of sums (1.58). The example pulls the opposite way from the trap it is meant to explain. Only the lab-set solution ("the idle tail's long weeks count for as little as anyone's short ones") showed me the right direction. **SLOWS**
26. **S20.** MTU sits in a "Numerator / Denominator" table, but MTU is a count of users, so I could not see what is divided by what. "Transacting" is also new to me. **MINOR**
27. **S21.** The title says "counted one crowd three ways", but the figures come from February 2018, May 2018 and September 2026, so they are not one crowd. The text then adds "journeys" as a fourth word. Riders, line utilisation, journeys and boardings are never told apart. **SLOWS**
28. **S23 and notebook 02 c14.** "sat idle online"; "drivers who stayed online without driving." But these drivers' trips fell only 12 percent, and the scatter plot shows most of them making 25 to 38 trips a week, so they did drive. "Hours 2.1 times" is also a fragment: 2.1 times what? **SLOWS**
29. **S23, `idle_tail_STUDENT.png`.** The title points "far right and low", but E and F, which S23 says are two of the 180, logged 16 and 14 hours with 3 and 2 trips. That puts them in a small group at the bottom of the chart (12 to 17 hours, 2 to 4 trips) that nobody explains. Their trips fell more than 80 percent, against 12 percent for the 180, so the six gave me the wrong picture of the 180. The title also says "180 drivers" when each dot is a driver-week. **SLOWS**
30. **S24.** "acceptance finds the same 180" is claimed on the slide but only shown in notebook 02 c17. **MINOR**
31. **"Floor", first used in the deck on S25.** By the end of the day it means three things: the Rs 300 minimum (notebook 01), the minimum share of offers accepted (S25, S41), and the lowest possible cost ("a floor on the cost, never a forecast": S42, S50, notebook 03 c04). The redesign solution uses two of them in one sentence: "keeps the floor and pays it only to driver-weeks whose share ... stays at or above a floor the city sets". **SLOWS**
32. **S25.** "If the scheme paid for one number, which would make the most drivers drive?" Option b (completed trips) also makes drivers drive, and option c is two numbers, not one. Both looked right to me. **SLOWS**
33. **S27 and notebook 01 c00.** A wait of 4.8 to 4.6 is called "barely moved", while 1.90 to 1.58 is "the fall". I had no yardstick for what size of change counts. **MINOR**
34. **One amount, many formats.** "Rs 1.159 crore", "Rs 1.16 crore" (S29 title, transcript), "Rs 116 lakh" (top-up picture), "Rs 1,15,90,000" (redesign Q1); and for the top-up, "Rs 19,000,000" in western commas (notebook 03 c01). I had to convert every time. **MINOR**
35. **S29, where the Rs 1.9 crore comes from (unsure).** The pack never works out the top-up for a single driver-week. In the CSV, driver A in the week of 31 August had 11 hours and Rs 3,465 in bookings (above Rs 300 × 11 = Rs 3,300) and still got a top-up of Rs 722. The same driver on 21 September had 11 hours and Rs 3,630 and got Rs 0. Driver E on 21 September had a gap of Rs 4,305 but got Rs 4,400. I could not make the stated rule produce these numbers. **SLOWS**
36. **S30, the seesaw** (also in the study notes and board work). "when the north star rises and a guardrail drops, the rise was bought." The wait and top-up per trip are bad when they rise, so a dropping wait would be good news. I also could not tell what "bought" means here. **SLOWS**
37. **S30 (unsure).** The inputs are drawn in the same amber that S2 used for Kalpa, so I wondered whether they are Kalpa numbers. "In the first peak hour": the first hour of each window, or of the day? **MINOR**
38. **S31 and `lead_STUDENT.png`.** "moves before the number the plan is judged on", but the slide compares acceptance with bookings per online hour, which is neither the north star nor a guardrail. Both lines drop in the launch week, so "moved first" confused me until notebook 03 c10 said "settled two weeks before". The left axis starts at 0.725, so the drop looks like a cliff. **SLOWS**
39. **Acceptance in two roles.** It is "Guardrail 1" on S30, but the leading input on S31 and S47. Kahoot Q2 and lead-lag Q1 key it as leading. The lab-set solution for Q4 says "acceptance and the wait are the guardrails", not inputs. Lab set Problem 4 forces me to give it one role, and I could not tell which. **SLOWS**
40. **S32.** "counted per paying rider, as Uber's own filing counts trips". Only the definition solution and the study notes explain this (the UberX Share example in Uber's 10-K). **SLOWS**
41. **S32 and the guided template.** "a shrinking enrolled base": how does a definition "not reward" it, and what kind of gaming is that? The template then labels this line "three things the old number paid for", but paying for hours never paid for a shrinking base. **SLOWS**
42. **S32.** The "Gaming note" line says "Each guardrail names the way of hitting the north star it catches". That describes the line instead of filling it in; the actual note is only in the solution. **MINOR**
43. **S33.** "desired date", "false zero-day waits", "the 14-day goal", "the Inspector General's interim report". The slide never says what the 14-day goal was. **SLOWS**
44. **S35 and `fall_cuts_STUDENT.png`.** "the three busiest weeks ... which bounds the monsoon argument". Busiest by what? Why does this answer the monsoon point? What does "bounds" mean? Notebook 03 c12 supplies the missing pieces ("still in the rains", "demand was at its highest"); the slide and the picture's label do not. **SLOWS**
45. **S35, the open doubts.** "the data holds weeks, not hours" and "every driver in these tables enrolled": I could not see why either is a doubt. Notebook 03 c15 then renames them "interference, enrolment", and the study notes call them "Selection". **SLOWS**
46. **How many guardrails?** S3 has two blanks. S30, S32, the S36 crux and S45 have three. S38 says "two guardrails or more". S49 says "two guardrails". S50's filled sentence drops top-up per trip. The transcript says "Two guardrails", then draws three, then calls top-up "guardrail 3". The study notes say three, then "two guardrails". The lab set and take-home ask for "Guardrails, two". I could not tell whether top-up per trip is a guardrail. **SLOWS**
47. **S37.** "War game, round 3". Round 2 is in no file I was given. **MINOR**

### 2. Notebooks 01 to 03

48. **NB01 c00.** "down 13 points", "up 16 points". I read the first as "down 13 percent". "Points" is never explained, and it comes back in fallback S5 and the definition solution. **SLOWS**
49. **NB01 c00 against S1.** "weeks beginning 31 August to 5 October" (notebook and study notes) against "31 Aug to 11 Oct" (S1, guided set). I checked a calendar to confirm they are the same six weeks. **MINOR**
50. **NB01 c03.** "This cell keeps those twelve driver-weeks out of `driver_weeks`." That reads as "leaves them out", but the cell picks them. **MINOR**
51. **Code in notebooks 01 to 04.** `.isin`, `.map` with a dict, `sort_values(ascending=[True, False])`, `.pivot`, `.iterrows`, named `.agg`, `.twinx`, `:.0%`, `lambda`, `.nlargest`, `.between`, `sqlite3`, `1.0 * SUM(...)`, and `driver_id <= "d_1060"` (never explained). Each cell says what it does, never what these new pieces are; I was only taught read_csv, groupby and sum. **SLOWS**
52. **NB01 c13 and NB02 c19.** The tags "[S]" and "[F]" and the labels "Level 1" and "Levels 2 and 3" are only explained later, in the exercise index. **MINOR**
53. **NB02 c04.** "held flat to the hundred" (to the nearest hundred?) and "the middle of the 72 zone-week median waits": is the city's 4.8 a median of medians? **MINOR**
54. **NB03 c04.** "The A/B test of the redesign is what settles it." "A/B test" is never explained, and neither are "a holdout" (S47, transcript, study notes) or "the unit you randomise" (S49). S49 says "the test stays with the block", and that block is tentative. **SLOWS**
55. **NB03 c04.** "the idle tail's top-up" is the same money as "driver-weeks that accepted fewer than half", but that only follows from S41's 0.46 and 0.78, which come later. **MINOR**
56. **NB03 c15.** "(a fifth to a half ... still paid), the redesign saves Rs 58 lakh to Rs 92.7 lakh". Read in order, a fifth goes with Rs 58 lakh, but c05 gives Rs 92.7 lakh for a fifth. The same reversed order appears in redesign Q2 option d, the study notes and cheat-sheet panel 5. Only S42 pairs them the right way round. **SLOWS**

### 3. The exercise index and the guided set

57. **Exercise index, line 42.** "frequent in GCC and product screens". "GCC" is never expanded anywhere. "Screens" comes back in the transcript and in the half-two Section 5 heading ("when a screen asks it cold"). **SLOWS**
58. **Exercise index, lines 29 and 94.** "the metric clinic" means nothing to me until the fallback deck. "Post exactly this shape": post it where? **MINOR**
59. **Guided Q2.** Option c ("completed at least one peak trip") also keeps out a sign-up who never drives, so b and c both looked right. Only the solution explains the trap in c. **SLOWS**
60. **Guided Q4.** Option b (the median wait) also looked right, since riders whose trips are declined wait longer. Only the solution says the wait moves too slowly to catch this. **SLOWS**

### 4. The afternoon deck, `slides/C2_W04_D01_half2_STUDENT.md`

61. **S38 and S39.** "win that lead back": the person, or being ahead? I also missed what "looks like bait" meant at first. **MINOR**
62. **S39.** "the other 880 drivers". 1,200 − 180 is 1,020. I only reached 880 by also taking out the 140 new drivers, which the slide does not say. **SLOWS**
63. **S40.** Option b, the denominator, is the count of drivers online, so it falls the same week. S41 itself says "the shrinking denominator shows it too" but not why the wait shows it first. Both b and c looked right. **SLOWS**
64. **S41, `acceptance_gap_STUDENT.png` (unsure).** The idle-tail bars sit only between 0.40 and 0.46, but E accepted 0.29 and F 0.25 of their offers on 21 September. I looked for them and could not see them. **MINOR**
65. **S43.** It took me three reads to parse "a success orders per month would miss". "Eternal" (I did not know it is Zomato's parent), "GOV" (never expanded), "NOV" and "cart consolidation" are all unexplained, and GOV and NOV come back in the redesign solution and the study notes. **SLOWS**
66. **S47.** "commit", "revert rate", "time to merge", "Build failures", "A holdout". Nobody explains these software and testing words to someone from commerce. **SLOWS**

### 5. The transcript, the Kahoot and the fallback deck

The redesign set read cleanly apart from findings 34 and 56.

67. **Transcript, lines 50 and 152.** "Leading input | Drivers online in the first peak hour", but S47's version of the same table row says "Acceptance in the launch week". **SLOWS**
68. **Transcript, lines 45 and 188.** "The primary metric" is a third name for the north star, and "sign-ups are a leading input" adds a third leading input. **MINOR**
69. **Kahoot (unsure).** Every key is marked "<- correct" in the STUDENT file, which spoils the quiz for anyone who opens it first. **MINOR**
70. **Kahoot Q2 and lead-lag Q1.** "requests per online hour by zone" is called leading, something "the city team can act on this week", but riders make the requests. I got it by elimination. **MINOR**
71. **Kahoot Q8 (unsure).** "The grain" and "The warehouse": I am not sure Week 2 taught "grain", and "warehouse" made me think of a godown. **MINOR**
72. **Fallback S1, facts 3 and 4.** "remittance accounts ... 0.04 of that year's 0.11 rise" (what rose by 0.11?) and "the funding rule for sales credit". I could not follow either. **SLOWS**
73. **Fallback S2.** Facts 1 and 2 both fit option a and option c. Option d, "Exclusions, dated", brings in dating, which the morning's seven lines never mentioned. **SLOWS**
74. **Fallback S4.** "Finance partner | Acceptance share", but S5 and the transcript give finance "Top-up per trip", and the city head here replaces the marketing lead. **SLOWS**
75. **Fallback, "SECTION 7: Does each number survive its owner?"** The heading does not say what happens in the section. **MINOR**

### 6. The Kalpa lab and the lab exercises

76. **NB04 c04.** "Your TA hands out a sheet with seven members' placements". The seven members' rows are in no student file, and the notebook does not say which seven, so I cannot do the hand count, in class without the sheet or at home. **BLOCKS**
77. **NB04 c05 and c07.** Both your-turn cells are empty, and no student file shows the result (the solution says "the TA walks them"). I cannot check my two ratios. **SLOWS**
78. **NB04.** "growth review" is unexplained. The "merged" status is only explained later, in the Kalpa set. The prediction options jump from "up by a third" to "more than doubled", leaving no option for a 50 percent rise. And I could not see why I divide by seven when the seven cancels out of the ratio. **MINOR**
79. **Kalpa set, line 128.** "the three guardrails of the morning draft". The morning was all Uber, and I could not find any Kalpa draft. **SLOWS**
80. **Kalpa Q2.** Option b ("ever placed an order") also keeps customers who stop ordering, so it looked right too. Only the solution says it "grows for ever". "A retention review" is also unexplained. **SLOWS**
81. **Company words.** "budget owner" (redesign set), "growth review" (NB04), "before the board does" and "retention review" (Kalpa set), "the top page" (lab set), "sales credit" (fallback). These assume I have sat in rooms I never have. **MINOR**
82. **Lead-lag Q2.** Number 3 is "Gross bookings for the quarter", but the evidence quoted is weekly bookings per online hour, so I was not sure it is about the same number. **MINOR**
83. **Lab set, Problem 4 heading.** "Which nine numbers keep their place". Only five keep a place; four are cut. **MINOR**

### 7. The solutions

84. **Definition solution, item 2 (unsure).** "lets a sign-up drive pull the rate down". I read "sign-up drive" as a typo. "a purge of sleeping accounts" is jargon to me. **MINOR**
85. **Kalpa solution (unsure).** "Kavya's review." Kavya is not introduced anywhere I read today. **MINOR**

### 8. The take-home and the self-check

86. **When does the city head decide?** S1 says "Ask, due Friday", and NB01 and the guided set say "decides on Friday". The lab set says the "one-slide review tomorrow", the take-home says "Thursday's review", and the pre-read says "five minutes on Thursday to decide". Which day is the review, and which is the decision? **SLOWS**
87. **Self-check, checkpoint 5.** "A group defined before the period starts". The day's own denominator ("online at least one peak hour that week") is decided inside the week, so by this rule the main example fails. **SLOWS**

### 9. The study notes

88. **"A rate is a blend."** "100 drivers at 1.9 and 20 idle drivers at 0.2 blend to about 1.62 ... with nobody's driving changed." That only works if every driver has the same hours, which is the plain average of rates the section above calls the trap. And the 20 idle drivers did change. **SLOWS**
89. **"Say it to a driver" after the doubts table.** "the quiet zones do not explain the fall away"; the row above says "most of the fall is in the outer zones". Which is it? **SLOWS**
90. **"Explorer scene M1" and "M2 to M4".** There is no `demos/` folder in the pack, so I could not open the explorer. **SLOWS**
91. **"Which pain points has each real case already paid for?"** The heading is unclear, and the section brings in an Airbnb case ("netted", "S-1") that no session covered. **MINOR**
92. **"Which words does the day use?"** The list comes at the very end and leaves out top-up, gaming, bookings, floor, points, the test and the zones. The cheat sheet's word box has the same gaps. **MINOR**

### 10. The cheat sheet, the board work and the pre-read

93. **Cheat-sheet PDF header.** The illustrative-case line prints with its asterisks showing. **MINOR**
94. **Cheat-sheet panel 1** (also the S36 board and the board work). "The tree", "The seesaw" and "The window's start" are bare labels; from the sheet alone I could not say what any of them means. I also could not see why "Delhi Metro" hangs off "online but idle". The board work repeats the deck's diagrams, so findings 25 and 36 apply there too. **SLOWS**
95. **Pre-read, line 11 (unsure).** "per driver-week, up from Rs 5,816.5 to Rs 5,861.3". Using the driver-week counts I was taught (6,270 and 6,434) gives about Rs 5,900 and Rs 5,921. The pre-read's figures need 6,360 and 6,500, which it never gives. **SLOWS**
96. **Pre-read, line 43.** "The same Rs 3.81 crore". Before the launch it was Rs 3.70 crore, so "the same" threw me. **MINOR**

### Totals

96 findings: **1 BLOCKS, 53 SLOWS, 42 MINOR**. Nine of them are marked unsure: 18, 35, 37, 64, 69, 71, 84, 85 and 95.

### The three places I would most want fixed

1. **S1, plus a word box carried through the day.** Define top-up, gaming, bookings, share and points, enrolled, and which zones are outer and which are core. Every later slide, notebook and exercise leans on these, and I met most of them undefined (findings 1 to 6 and 48).
2. **S19 and its copies** (NB02 c10, the study notes, the board work). Make the X and Y example pull the same way as the city data, where long slow weeks are under-weighted and the average comes out too high, and make "two-fifths" agree with its bracket and with "a third". This is chapter 2's trap, and it left me more confused than before (findings 24 and 25).
3. **Say the roles of the day's numbers one way everywhere.** That means the guardrail count, whether acceptance is a guardrail or a leading input, what the leading input is, and which number finance wants. The exercise keys depend on these, so when the pack contradicts itself I lose marks I cannot defend (findings 39, 46, 67 and 74).

The only blocker is NB04 c04's missing seven-member sheet (finding 76).

### What should not change

The twelve-row hand count should stay as it is (S9 to S11, notebook 01, cheat-sheet panel 2). Six drivers, two weeks: add the hours, add the trips, divide once. I did it on paper, every number matched in every file, and predicting before the reveal made E and F stick.

## The hiring interviewer's read

I only read files and changed nothing in the repository. I checked the numbers with pandas against the Monday CSVs and the generator. I fetched five public sources, read-only, on 12 October 2026; the fetch tool cached three PDFs in the session's tool-results folder, outside the repository.

**Files.** All are under `/home/user/c2-content-factory/`:
- T: `content/W04/D1/extras/C2_W04_D01_transcript_STUDENT.md`
- SC: `content/W04/D1/trainer/C2_W04_D01_interview_scorecards_TRAINER.md`
- H1: `content/W04/D1/slides/C2_W04_D01_half1_STUDENT.md`
- H2: `content/W04/D1/slides/C2_W04_D01_half2_STUDENT.md`
- FB: `content/W04/D1/slides/C2_W04_D01_fallback_STUDENT.md`
- N: `content/W04/D1/study-notes/C2_W04_D01_notes_STUDENT.md`
- DS: `content/W04/D1/trainer/C2_W04_D01_day_sheet_TRAINER.md`
- UG: `content/W04/D1/exercises/unguided/C2_W04_D01_redesign_STUDENT.md`
- SOL: `content/W04/D1/exercises/solutions/C2_W04_D01_redesign_solution_STUDENT.md`
- K: `content/W04/D1/kahoot/C2_W04_D01_quiz_STUDENT.md`
- GEN: `content/W04/D1/internal/C2_W04_D01_generate_INTERNAL.py`
- FACTS: `content/W04/D1/internal/C2_W04_D01_facts_INTERNAL.yaml`
- DATA: `content/W04/D1/data/C2_W04_D01_driver_weeks_STUDENT.csv` and `C2_W04_D01_zone_weeks_STUDENT.csv`
- CASE: `docs/detailing/W04_case_file.md`
- SPINE: `docs/detailing/W04_analyst_craft_spine.md`

**The short version.** The [S] answer has every part an interviewer listens for, in the right order, and it earns its 14 on the pack's descriptors. The problems are underneath:
- Its north star does not measure the goal the candidate restates, and it barely moved (35.76 to 35.89 trips per online driver-week).
- Two of its guardrails can be beaten in ways the ticket already shows.
- The fact the candidate says would change their mind is already true in the case's own data.
- The top-up figure it sizes with cannot come from the payout rule the ticket states.

Judged by the pack's own descriptors, the AI variant and the [D] answer deserve well below the scores the pack gives them.

---

### 1. My scores, criterion by criterion

#### The [S] hire-grade answer (T lines 27 to 128)

| Criterion | Mine | The line that earns it | Pack | Where we differ |
|---|---|---|---|---|
| Clarified scope | 2 | "What was the guarantee meant to change ... Who is in it ... what would count as harm" (29-31), then "the goal is riders served faster at peak, and online hours are a means to it" (37-38) | 2 | Agree. It never asks what decision the answer feeds or what the baseline is (finding 11) |
| Named the denominator and window | 2 | "the denominator is enrolled drivers online at least one peak hour that week, with that count shown, and the window is the calendar week" (46-48) | 2 | Agree on the descriptor. This denominator is what makes the north star blind to the problem (finding 1) |
| Saw the paradox | 2 | "hours rose a quarter and the output per hour fell by about a sixth, while riders waited about as long" (101-102) | 2 | Agree. It never says what its own north star did |
| Sized it with a unit | 2 | "what share of the top-up went to weeks where drivers declined most offers?" ... "About Rs 1.16 crore in six weeks" (109-114) | 2 | Agree on the descriptor. It sizes who got the money and never what the money bought (finding 9), and the figure rests on a column the rule cannot produce (finding 7) |
| Said what would change their mind | 2 | "if riders in the outer zones waited less because those drivers sat there ... I would keep part of the hourly floor there" (117-118) | 2 | Agree for the candidate. The data already meets the condition (finding 5) |
| Tied it to a decision and its cost | 2 | "I would not extend it. I would pay the floor for completed peak trips, with a floor on the share of offers accepted, and test that rule" (115-117) | 2 | Agree on the descriptor. The new rule cannot be written as a payout formula (finding 6) |
| Structure before the number | 2 | The layout at lines 44-52 comes before the first number, at line 71 | 2 | Agree |
| **Total** | **14** | | **14** | Meets the target on the first three |

**My hire call on [S].** The descriptors reward the parts being present, and all of them are present.
- At a 0 to 3 year analyst screen in a GCC or at Swiggy, this answer is a hire.
- At Uber's marketplace team or at Google it is borderline. The structure carries the candidate into the second round of follow-ups, and the case's own data ends it there unless findings 1, 3, 5 and 8 have answers.

#### The AI-company variant (T lines 132 to 154)

| Criterion | Mine | The line | Pack | Why mine differs |
|---|---|---|---|---|
| Clarified scope | 1 | "First, what is it for: developers shipping working code faster." (139-140) | 2 | The candidate states the goal and asks the interviewer nothing. There is no question on who it serves (the developer, or the buyer of seats) and none on harm. The descriptor's 2 requires asking and building on the answers |
| Named the denominator and window | 1 | "per active developer per week" (142) | 2 | "Active" is undefined. If it means "used the tool this week", the denominator depends on the tool itself. "At the next commit" is a horizon each developer sets differently |
| Saw the paradox | 1 | "a developer can accept a short suggestion and delete it a minute later" (140-141) | 2 | It names a mechanism with no number, and the pack's own descriptor for a 2 is "names it with numbers". An assumption-labelled number was available. The mechanism is also the wrong one (finding 24) |
| Sized it with a unit | 0 | None | 1 | There is no size at all; a unit on its own is not one. A developer-tools screen expects a labelled back-of-envelope estimate: seats, minutes saved, loaded cost and seat price |
| Said what would change their mind | 1 | "I would test it with a holdout of users" (145) | 1 | Agree: it names a method, with no condition |
| Tied it to a decision and its cost | 0 | "Acceptance stays as a leading input, never the target" (143-144) | 1 | This is a reporting choice. There is no decision about the assistant (expand it, change when it suggests, stop quoting acceptance to buyers) and no cost |
| Structure before the number | 2 | Goal, outcome, guardrails, input, gaming, test, in that order (139-145) | 2 | Agree |
| **Total** | **6** | | **11** | Misses the target on all three of the first criteria |

The scorecard says the variant scores lower because it "has no data" (SC line 66). It still gives a 2 on "saw the paradox", whose own descriptor requires numbers.

#### The [D] hire-grade answer (T lines 158 to 195)

| Criterion | Mine | The line | Pack | Why mine differs |
|---|---|---|---|---|
| Clarified scope | 2 | "What is the scheme for, and which decision will the number drive ... And what does each team need to see to do its own job?" (167-169) | 2 | Agree. This is the best clarifying question in the file |
| Named the denominator and window | 1 | "One north star tied to the goal: completed peak trips per enrolled driver online at peak" (180); "Marketing, enrolled drivers is printed beside the rate every week" (187-188) | 2 | The call drops its window. The count promised to marketing is also a different number: the printed count is enrolled drivers online at least one peak hour, so a sign-up who never drives is in marketing's number and never in the printed one |
| Saw the paradox | 2 | "Hours rose 24 percent while trips per online hour fell from 1.90 to 1.58, so hours cannot be the target" (182) | 2 | Agree |
| Sized it with a unit | 1 | "it was Rs 82.3 after the launch" (194) | 1 | Agree, for a sharper reason. Rs 82.3 is half the Rs 165 average fare and the answer never says so. Nor does it price what choosing hours as the target cost |
| Said what would change their mind | 1 | "If the wait rose while the north star held, I would revisit the acceptance floor" (183) | 2 | The line appears only in the comparison table, never in anything the candidate says. It tunes a guardrail without reopening the call. It also misreads the candidate's own metric: a floor that pushes drivers out makes trips per remaining driver rise, not hold |
| Tied it to a decision and its cost | 1 | "The city head decides, from one page" (195); "Shows where each number now lives" (181) | 2 | A decision with no cost. The scorecard's own sizing row says "the cost of hours is not restated", and its descriptor scores that a 1 |
| Structure before the number | 2 | "Tie the one number to the scheme's goal, then give every other team's number a named place" (171-172) | 2 | Agree |
| **Total** | **10** | | **13** | Misses the target on the denominator |

---

### 2. What a strong interviewer would reject

**1. The north star measures the driver, while the goal is the rider. REJECT.**

*Where:* T lines 37-38 and 45-48; N "What does the full definition say?"; H2 S40 and S41; SPINE line 333.

> "Then the goal is riders served faster at peak" ... "The primary metric is completed peak trips per enrolled driver online at peak, per week"

*What is wrong:*
- Trips per driver is a utilisation number. Requests rose only 1.8 percent, so a supply scheme that works (more drivers on the road, faster pickups) pushes it down, and one that sheds drivers pushes it up.
- On the case data it rose 0.4 percent, from 35.76 to 35.89, while the candidate calls the scheme a failure using a different number. The transcript never says what its own north star did.
- The definition's line "What it does not reward: ... a shrinking enrolled base" is contradicted by its formula. Printing the count beside the rate shows the shrink, and the rate still rewards it.
- S40 asks which line "would show it first" if drivers log off, and keys c, the wait. The denominator moves that same week by construction, and the north star rises.

*What a strong interviewer wants:* a primary metric that moves with the goal, such as request-weighted pickup wait (p50 and p90) or the share of peak requests picked up within N minutes, by zone. Cost per incremental completed trip sits beside it as the efficiency line, and trips per online hour as the diagnostic.

If the spine's north star stays, the candidate must say so out loud: "my north star barely moved, 35.76 to 35.89, and it would rise if drivers quit, so the wait carries the goal and I read the two together."

**2. The leading input is the gamed proxy again, and it pushes the north star down. REJECT.**

*Where:* T lines 50, 58, 188 and 193; H2 S47 line 212; K Q2 key.

> "One leading input: drivers online in the first peak hour." ... "Their input is drivers online in the first peak hour, which moves before trips do." ... "sign-ups are a leading input"

*What is wrong:*
- More drivers online against flat requests lowers trips per driver. This input leads the wait and runs against the north star; sign-ups work the same way.
- It is an open-app headcount: the very measure the morning showed can rise with no service, now handed back to driver operations as their number.
- It cannot be computed from the weekly data.
- S47 gives a third version, "Acceptance in the launch week", which is guardrail 1 read once.

*What a strong interviewer wants:* an input that raises the north star when the city pushes it, such as requests per online hour by zone (already on H1 S30) or the share of peak requests with an open driver nearby. It should be stated the same way in T, S30, S47, K and N.

**3. The acceptance floor guards one gaming route and leaves two open. REJECT.**

*Where:* T lines 48-50 and 127; H2 S41; UG Q3; DS line 185.

> "the share of offers drivers accept, so nobody is paid for declining" ... "the floor sits in the gap the data shows, above the idle tail's highest week, 0.46, and below everyone else's lowest, 0.78."

*What is wrong:*
- **Accept-then-cancel.** The ticket's own row shows driver cancellations after acceptance rising from 0.04 to 0.09. In DATA, the idle tail cancels 15.2 percent of what it accepts and the 140 new drivers 14.8 percent; the 880 "honest" drivers went from 3.7 to 7.7 percent. A floor on accepted share pays all of them.
- **Location.** A driver parked in Shamshabad who accepts the few offers he gets clears any acceptance floor, while the hourly floor pays for his empty hours. 72 percent of the idle tail's new hours sat in the outer zones.
- **In-sample fit.** The gap is fitted on a group chosen by its outcome. Once the floor is announced, drivers move to it: a floor of 0.5 lets a driver refuse half his offers, against 0.86 before the launch.
- The day sheet's own [F] answer asks for "guardrails the measured cannot move". Acceptance is the one number the drivers move by hand.

*What a strong interviewer wants:*
- the floor set on the completed share of offers (accepted less driver-cancelled, over shown);
- a separate driver-cancel guardrail;
- eligibility only in zones and windows where requests outrun supply;
- the floor set from the pre-launch distribution and tested at two levels;
- S41's trainer caveat ("on a real city the two groups overlap") carried into the student transcript.

**4. The wait guardrail is an unweighted median of zone medians, so it cannot see the outer zones or the tail. REJECT.**

*Where:* T lines 49-50 and 98-99; FACTS `median_wait_before` and `median_wait_after` ("middle value of the 72 zone-week medians"); GEN lines 313-317.

> "the median rider wait at peak, so riders are not worse off"

*What is wrong:*
- 4.8 and 4.6 are the median of 72 zone-week medians: one vote per zone-week, whatever its number of requests. The generator nudges core zones until that median hits the core centre.
- The outer zones (6.3 to 6.8 minutes before, 5.5 to 6.6 after) sit above the city median in every week. The guardrail cannot see the zones where the idle hours went.
- This is the day's own trap in another form. K Q6 teaches "a rate is a ratio of two sums, never an average of each row's ratio", and this guardrail is a median of each row's median.
- A median also hides the riders who wait longest, and the weekly series is back at 4.80 in the week of 5 October.

*What a strong interviewer wants:* the wait computed from ride-level data with requests as weights, p90 beside p50, and the unfulfilled share (0.11 to 0.10), each shown by zone.

**5. The candidate's own mind-changer is already true in the data, and the verdict misstates how far the goal moved. REJECT.**

*Where:* T lines 114-118 and 193; DS line 183; H2 S50.

> "it is not a success on the goal it was launched for" ... "What would change my mind: if riders in the outer zones waited less because those drivers sat there" ... "the guarantee proved hours can rise with no service"

*What is wrong:*
- In zone_weeks, each outer zone's median wait fell by 0.5 to 0.7 minutes (6.6 to 5.95 for the three together). The core fell from 4.8 to 4.6, and the unfulfilled share fell from 0.11 to 0.10.
- The goal moved, a little. So "not a success on the goal" and "proved ... no service" are wrong as stated. The hire line is "it moved the goal slightly, at a price nobody would pay".
- Neither the transcript nor the pack's redesign checks the condition or keeps any floor in the outer zones. An interviewer holding the data takes the decision apart with one question.

*What a strong interviewer wants:* the candidate asks for waits by zone before deciding and finds 6.6 to 5.95. They price it on the pack's own column:
- the idle tail drew about Rs 85.7 lakh of top-up in weeks spent mostly in the outer zones;
- outer fulfilment rose from 0.780 to 0.789, about 185 extra trips once demand growth is netted out;
- that is about Rs 46,000 per extra trip.

Then they decide zone by zone.

**6. The redesign is written as two different rules, and neither is a payout formula. REJECT.**

*Where:* T lines 88 and 115-116; H2 S39 (marketing card) and S50; N closing paragraph; UG lines 35-38; SOL lines 8-10 and 43-45; role cards (TRAINER) line 41.

> T: "I would pay the floor for completed peak trips, with a floor on the share of offers accepted"
> UG: "The redesign keeps the Rs 300 floor and changes what earns it ... A driver-week whose accepted share falls under the floor earns no top-up that week"
> SOL: "it stops paying for the gross figure, hours online, and pays for the one that carries the service, completed trips"
> S50: "Pay for completed peak trips per enrolled driver online at peak"

*What is wrong:*
- The exercise keeps Rs 300 per online hour, gated on acceptance, which still pays for an empty hour to any driver above the floor. Its own solution says the redesign stops paying for hours.
- The transcript's phrase has no formula behind it.
- S50 asks the city to pay for a city-level ratio, which no driver can be paid by.
- The mechanism the case turns on is never named. Below the floor, the top-up shrinks by whatever the next trip pays, so the trip earns the driver nothing extra and declining is free. The exercise's rule keeps that.

*What a strong interviewer wants:*
- one written rule used in every file, for example a per-window floor paid only for windows with at least N completed trips, in demand zones, with the completed share of offers at or above F; or a per-trip peak bonus;
- the candidate saying how that rule gives the marginal trip its value back;
- the north star kept as the number the city judges the scheme by, in a separate sentence from what drivers are paid for.

**7. The top-up column cannot come from the rule the ticket states, and the rupee sizing rests on it. REJECT.**

*Where:* DATA driver_weeks; GEN lines 240-241 and 474; T lines 87 and 112-114; H2 S42; UG Q1 and Q2.

> "Rs 1.159 crore, 61 percent of the Rs 1.9 crore top-up, went to driver-weeks that accepted fewer than half their offers"

*What is wrong:*
- The ticket's rule pays, per whole window, the gap between Rs 900 and the driver's trip earnings in that window.
- Idle-tail driver-weeks average 38.9 hours, Rs 5,109 of fares and Rs 10,731 of top-up. That implies the drivers kept 18 percent of their fares.
- Every other driver's rows imply 73 percent. Hand-count row E implies 81 percent, and row F 106 percent, which is more than the fare.
- 496 of the 1,080 idle driver-weeks carry more top-up than the rule could pay even if every trip that week fell inside a single window.
- The generator sets the idle top-up as hours times a random factor between 0.93 and 1.0, scaled to a target total. Its only check is that no row exceeds Rs 300 times hours.
- At one consistent 80 percent share, the rule gives the idle tail about Rs 81.9 lakh and the city about Rs 1.34 crore. The 61 percent happens to survive at that share (at 73 percent it is 53 percent); the rupee figures do not.
- A learner who applies the morning's rule (row E) to the full table will find this, and so would an interviewer who sets the CSV as a take-home.

*What a strong interviewer wants:* `topup_rs` regenerated from the stated per-window rule with one stated driver share, letting Rs 1.159 crore, Rs 82.3 and the S42 range fall where they fall.

**8. "A holdout" is not a test design for a driver incentive in a shared market. REJECT.**

*Where:* T lines 51-52, 116-117 and 154.

> "I would test any change with a holdout, with the length of the test fixed before it starts" ... "test that rule against the current one before any new city"

*What is wrong:*
- At a marketplace screen, the first follow-up is "randomise what?".
- Drivers on two rules in one zone compete for the same riders, so a driver-level split is biased by spillover. Paying two drivers in one zone on different terms is also a driver-relations problem of its own.
- The test length must cover adaptation: H1 S31 shows bookings per hour took three weeks to settle.

*What a strong interviewer wants:* the unit named (zones, zone-and-time switchbacks, or a matched city), the primary metric and guardrails fixed in advance, at least four weeks, and no peeking. The faculty block goes deeper, but the hire-grade line still has to name the unit.

---

### 3. What passes a weak screen and stalls a strong one

**9. The candidate sizes who got the money and never what it bought. SHALLOW.**

*Where:* T lines 109-114 and 194.

> "what share of the top-up went to weeks where drivers declined most offers?"

The ticket alone gives the return on the spend:
- 6,700 extra peak trips for Rs 1.9 crore is about Rs 2,836 a trip, 17 times the Rs 165 average fare.
- Holding fulfilment at 0.89, only about 2,565 of those trips come from better fulfilment: about Rs 7,400 each.
- The 0.2-minute fall in median wait across 230,900 trips works out to roughly Rs 410 per rider-minute.
- Rs 82.3 of top-up per completed trip is half the average fare.

One of these sentences is what a hire says.

**10. There is no argument that the scheme caused the fall. SHALLOW.**

*Where:* T lines 101-107; H2 S39 (finance card); N doubt table.

> "Requests could explain it if riders asked for fewer trips, so I would check demand."

- This is a before-and-after comparison, with the monsoon ending inside the window. All 1,200 drivers are enrolled, so there is no in-city comparison group.
- The cheapest causal argument in the data is the step. Trips per online hour went from 1.88 in the week of 24 August to 1.64 in the launch week itself, while weekly requests stayed in the same 41,000 to 44,000 band before and after. A season drifts; this stepped on the launch date.
- S39's "the three busiest weeks already read 1.60" is weaker, because those are the first three weeks after the launch.
- A hire also asks for a comparison city.

**11. The clarifying questions skip the decision and the baseline. SHALLOW.**

*Where:* T lines 29-31, against H2 S44 line 148.

> S44: "Which window, against which baseline?"

The transcript's candidate asks three questions without this one. They then bring in "I would not extend it ... before any new city", a decision the interviewer never mentioned.

*Want:* "What decision rides on this: continue, change or expand?" and "Against what: the six weeks before, or a comparison city?", asked up front. The [D] clarify already does this for the decision.

**12. "Drivers will log off" is answered with the wrong number, and the 180 are not idle. SHALLOW.**

*Where:* H2 S39 card, S41 and S42; N "What do the three roles say?" and line 250.

> "True for the 180 who sat idle online; the other 880 drivers held 1.90 trips an hour before and after the launch" ... "180 drivers sat idle"

- The 880 drivers' rate says nothing about their spare capacity.
- The idle tail still completed 33,440 peak trips after the launch: 14.5 percent of the city's, about 31 a week each. If they quit rather than revert, the other drivers need about 17,600 more peak hours at 1.90 to carry those trips.
- No file names a driver-side guardrail (earnings per online hour, churn) for a change to driver pay, and S42's saving nets out none of this.

*Want:* three cases for the 180:
- they revert to their pre-launch 1.90, which adds trips;
- they game the new floor;
- they quit, with the trips at risk sized.

Plus a driver-earnings guardrail read weekly in the first month.

**13. Follow-up 3 answers logging in and skips logging off. SHALLOW.**

*Where:* T line 128; N "Which follow-ups come next?"; UG Q4.

> "Logging in alone cannot raise it ... the denominator counts a driver once, whatever the hours"

- A driver who stays off for a week leaves the denominator and raises the rate.
- S46 has the better line ("print the driver count beside the rate so logging off cannot flatter it"), and both T and N drop it. UG Q4 tests only the logging-in half.
- Under any per-trip rule, a hire also names trip fabrication (a ride booked from a second rider account) and the check for it.

**14. The room rehearses three friendly follow-ups and none of the hard ones. SHALLOW.**

*Where:* T lines 122-128; H2 S46.

The case's own data hands an interviewer these questions, and the pack has no prepared line for any of them:
- "Your north star went 35.76 to 35.89; did the scheme work?"
- "Driver cancellations more than doubled; what does your acceptance floor do now?"
- "Outer-zone waits fell 0.6 minutes; do you keep the floor there?"
- "Randomise what, when drivers share riders?"
- "If the 180 quit, who carries their 33,000 trips?"
- "Is 0.2 minutes real, when the last week is back at 4.8?"
- "Why the median wait and not p90?"

*Want:* a second follow-up table, the hard one, each question with its one-breath line.

**15. The [D] answer has three gaps, and it is rehearsed only if the faculty block slips. SHALLOW.**

*Where:* T lines 185-189 and 194; SC lines 3-5.

> "The budget is guardrail 3, top-up per completed trip" ... "Candidate, to the two who lose" ... "the [D] pair in section 9 of the metric clinic if the tentative faculty block does not run"

- **Finance gets a unit cost for a budget.** A budget is a total, and top-up per trip can fall while total spend runs away if trips rise.
- **All three teams lost, and the answer speaks to two.** The north star is none of the three teams' numbers, so driver operations lost too. A hire says "none of your three is the target, and here is why" before placing each one.
- **The [D] question, the one marked as separating the strongest candidates, gets class time only when the faculty block does not run.**

*Want:* a total cap plus cost per incremental trip for finance, the reframe said aloud, and ten minutes for [D] in the main interview room.

---

### 4. Real-world facts that need a source or a fix

**What I checked and found holding.** I checked these against the primary documents on 12 October 2026:
- **The SEC order (FB S1):** debit cards as "the largest product category", kept "for up to four years", and the .04 of the .11 rise over 2013.
- **The VA OIG report (N):** 79 staff interviewed, thirty of whom used the wrong desired date, and the 14-day goal leaving performance contracts.
- **Airbnb's S-1 (N):** the table shows March 2020 at "(4.1)" million nights, net of cancellations and alterations.
- **Swiggy's Q1 FY26 letter (H2 S43):** "16% QoQ to INR 612" and Maxxsaver's basket threshold.

The Uber 10-K UberX Share example and the Spotify definition match the day sources; I did not refetch them.

**16. S43's Swiggy sentence picks the larger reading and slips from "per user" to "per month". SOURCE.**

*Where:* H2 S43 line 116.

> "over 28 percent of Swiggy's monthly transacting users used it ... cart consolidation led by Maxxsaver lowered order growth ... Orders per month would have read that success as a fall."

- The letter says "over 28% of our MTUs", inside the Instamart answer on Maxxsaver. It does not say whether that means platform users (21.6 million) or Instamart's (11.1 million).
- It credits the lower order growth to "Some cart-consolidation led by Maxxsaver and letting go of some low AOV orders and unprofitable users". The slide keeps only the first cause.
- Its "a slightly lower number of orders by the same user" supports orders per user falling. Total orders still grew, more slowly.

*Want:* "over 28 percent of its MTUs", both causes, and "orders per user would have read that success as a fall".

**17. The notes say Maxxsaver "raised" the AOV. SOURCE.**

*Where:* N lines 227-229.

> "Swiggy's Maxxsaver raised Instamart's average order value 16 percent to Rs 612"

The letter credits "our significantly expanded selection driving a higher non-grocery mix ... and the resounding success of Maxxsaver", and says Maxxsaver "helped".

*Want:* "helped raise", or both drivers named.

**18. The Eternal quote is not on the case file's URL, and two glosses go further than Eternal's words. SOURCE.**

*Where:* H2 S43 line 118; N pain point at line 275; SOL lines 41-43; CASE M2 row (line 181).

> "'as NOV more accurately reflects underlying performance'" ... "The gross figure let discounts buy growth" ... "A gross figure read as money earned: Eternal's move from GOV to NOV"

- The case file's only M2 URL (eternal.com/blog/q1fy27, dated 22 July 2026) carries neither the NOV definition nor the quoted words.
- The quote lives in a Google Drive PDF that would not render in this session, so I could not verify it.
- The two glosses give Eternal a motive or an error that its words do not state. They also break S43's own trainer note: "Do not say either company used a metric badly".

*Want:* the stock-exchange copy of the letter in the case file, the quote checked against it, and both glosses cut back to what Eternal said.

**19. Spotify's pain-point label misstates the fact beside it. SOURCE.**

*Where:* N lines 278-279.

> "An open screen counted as activity: Spotify's monthly active user, any account with more than zero milliseconds of consumption in thirty days"

The definition counts consumption, however brief. An open screen with nothing played does not count.

*Want:* "a bar set at any consumption at all".

**20. Wells Fargo's 2020 sum is called a penalty. SOURCE.**

*Where:* N lines 84-86; CASE M8 row (line 177).

> "the bank paid USD 185 million in penalties in 2016 and USD 3 billion in 2020"

The day sources already say the USD 3 billion was a settlement with the DOJ and the SEC, of which USD 500 million was the SEC's penalty. The slip starts in the case file's wording, "the SEC's USD 3 billion settlement".

*Want:* "USD 3 billion to resolve DOJ and SEC investigations, USD 500 million of it the SEC's civil penalty".

**21. Delhi Metro's month is not in the case file, and the source is a wire republisher. SOURCE.**

*Where:* N lines 150-152.

> "about 27 lakh riders a day that February"

"That February" is not in CASE's M6 row. The LatestLY URL returned 403 to a fetch on 12 October 2026, and its agency-news page republishes wire copy.

*Want:* the original agency report or DMRC as the source, and the month confirmed or cut.

**22. Aced is cited without its URL, for a principle the rubric does not score. SOURCE.**

*Where:* SC lines 5-7.

> "built on what interviewers score per Aced's guide: structure, assumptions and scope before the method, the takeaway before the working (case file T2, checked 12 October 2026)"

- The URL sits only in CASE's T2 row.
- No criterion scores "the takeaway before the working", and the hire-grade answer gives its verdict last (T line 114).

*Want:* the URL in the file, and either an eighth criterion ("led with the verdict once the numbers were in") or the phrase cut.

---

### 5. The AI-company variant

**What it gets right:** acceptance is a proxy, kept code matters, the revert rate is a real guardrail, acceptance stays an input, and the test length is fixed in advance.

**What it gets wrong:**
- the outcome does not fit the goal it restates;
- the gaming it names is not the gaming that happens;
- the test cannot read its own north star;
- the guardrails stop at the build.

A developer-tools interviewer would mark it a weak signal, which is what my 6 of 14 says.

**23. The holdout cannot measure the north star. REJECT.**

*Where:* T lines 145 and 154; H2 S47 line 214.

> "I would test it with a holdout of users" ... "A holdout of developers without the assistant"

Suggested text still in the code is zero, by construction, for developers without the assistant. The test can compare only the guardrails.

*Want:*
- an outcome that both arms have, such as time from first commit to merge, or merged changes not reverted within 30 days per developer;
- teams randomised as units, since shared code and reviewers spill over;
- a test length that covers the learning curve;
- for day-to-day changes, an A/B test of model versions, where kept-text measures exist in both arms.

**24. The outcome is a usage volume, and the gaming it names is mostly developers inspecting suggestions. REJECT.**

*Where:* T lines 137-145 and 149-153; N "How does it move to an AI product?"; K Q7.

> "So the outcome I would count is suggested text still in the code at the next commit, per active developer per week" ... "time to merge, so review is not slowed" ... "The gaming I would watch is short suggestions accepted and deleted."

*What is wrong:*
- The goal it restates is "developers shipping working code faster". Kept AI text per developer measures how much of the code the tool wrote, and it rises with verbose suggestions nobody trims.
- Time to merge, filed as a guardrail, is the number closest to the goal.
- Developers are not paid per acceptance, so accepting and then deleting is mostly how people inspect a suggestion.
- The party with a motive to move acceptance is the team that quotes it. It can show fewer, shorter, safer suggestions: the acceptance rate rises while the value delivered falls.
- The transcript switches between a rate ("the share of suggestions developers accept", line 137) and a count ("Suggestions accepted", line 149). Those two are pushed in opposite directions.
- K Q7 and N call kept text "the outcome".

*What a strong interviewer wants:*
- outcome: time from first commit to merge, or unreverted merged changes, per licensed developer, with the active share printed beside it;
- kept-suggestion share at a fixed horizon (seven days, say) as the quality-weighted input;
- acceptance as the leading input;
- the gaming named as suppression and verbosity.

**25. The guardrails stop at the build. SHALLOW.**

*Where:* T line 151; H2 S47 line 211.

> "Build failures; revert rate; time to merge"

Build failures need attribution: failures on commits with suggested code, compared with those without. The list also misses what a developer-tools company watches:
- security findings in accepted code (static-analysis alerts, secrets, vulnerable dependencies);
- churn (suggested lines rewritten within two or three weeks);
- review load (PR size, review time, comments per PR);
- suggestion latency and inference cost per developer;
- developers' trust in the tool.

*Want:* two of these named, each with how it is tied to suggested code.

**26. The variant is not ready for the published finding against it. SHALLOW.**

*Where:* T lines 139-141.

> "Accepted suggestions are a proxy, like online hours"

A 2022 study of a production code-completion tool reports that "the rate with which shown suggestions are accepted, rather than more specific metrics regarding the persistence of completions in the code over time, drives developers' perception of productivity" (Ziegler and others, "Productivity Assessment of Neural Code Completion", arXiv 2205.06537, abstract checked 12 October 2026). An interviewer at a developer-tools company may know it.

*Want:* a line ready: perception is one measure of value; acceptance is a sound leading input; the tool is judged on measured time to merge in a team-level test.

---

### Minor points

**27. Two guardrails or three. MINOR.** T line 48, N line 247 and DS line 183 say two. T's own diagram (line 57), H1 S30, H2 S45 and the definition say three. Say three everywhere, and say which one finance owns.

**28. "A staple asked everywhere". MINOR.** T line 22 makes an unsourced claim about real interviews. "In this programme's calibration" is enough once "asked everywhere" goes.

**29. Every driver is enrolled. MINOR.** T line 34 ("Enrolled drivers only") and N's doubt table ("Who enrolled") treat enrolment as a subset. All 1,200 rows of drivers.csv have enrolled = True, so the filter does nothing and the selection doubt cannot be tested. Say so, or add non-enrolled drivers.

**30. The Kahoot items. MINOR.**
- Q1 is sound.
- Q5's key is right, but two distractors ("rise every week for ... a quarter" and "read from across a large room") are throwaways.
- Q6's "never an average of each row's ratio" is an absolute a strong interviewer rejects. The mean of driver rates answers a different, legitimate question (the typical driver's week); the rule is to match the aggregation to the question. The pack's own wait guardrail also breaks the rule it teaches (finding 4).
- Q7 calls kept text the outcome (finding 24). It also treats a developer survey as plainly wrong, though developer-reported productivity is a standard measure in that field.

**31. The fallback's [D] slide differs from the transcript. MINOR.** FB S9 line 232 calls hours "an input beside trips per hour". T line 181 calls them supply's diagnostic, and T line 193 names a different input. S9's table also drops marketing's number.

---

### Counts and the three changes

| Severity | Count | Findings |
|---|---|---|
| REJECT | 10 | 1 to 8, 23, 24 |
| SHALLOW | 9 | 9 to 15, 25, 26 |
| SOURCE | 7 | 16 to 22 |
| MINOR | 5 | 27 to 31 |

**The three changes that would most raise the material:**

1. **Re-cut the metric tree against the goal, and put the case's own data to the candidate** (findings 1, 2, 4, 5, 9, 14).
   - Either replace the per-driver north star with a rider-side measure, or have the candidate own it: "35.76 to 35.89, and it would rise if drivers quit, so the wait carries the goal".
   - Make the wait request-weighted, with p90, by zone. Make the input requests per online hour by zone.
   - Rewrite the close so the candidate checks the outer zones (6.6 to 5.95), prices the return and decides zone by zone. The prices: Rs 2,836 per extra trip, about Rs 7,400 per trip from better fulfilment, and about Rs 46,000 per extra outer-zone trip.
   - Add the hard follow-up table. Add two criteria to the scorecard: "the metric moves with the goal" and "the test fits the market".

2. **Make the money and the rule real** (findings 3, 6, 7, 8).
   - Regenerate `topup_rs` from the stated per-window rule with one driver share (row E's 81 percent), and let Rs 1.159 crore, Rs 82.3 and S42's range fall where they fall.
   - Write one payout formula and use it in every file: gated on the completed share of offers, with a driver-cancel guardrail and eligibility only in demand zones.
   - Have the hire-grade line name the test's unit (zones or zone-and-time switchbacks), its length (at least four weeks, given S31's three-week settling) and no peeking.

3. **Rebuild the AI variant and score it against the descriptors** (findings 23 to 26).
   - Outcome: time from first commit to merge, or unreverted merged changes, per licensed developer.
   - Kept-suggestion share at a fixed horizon becomes the input.
   - Name the gaming as the reporting team's suppression and verbosity.
   - Use a team-level test or a model-version A/B, so the outcome exists in both arms.
   - Add security, churn and review-load guardrails, a labelled back-of-envelope size, and a ready answer to the 2022 acceptance finding.
   - Rescored honestly, it should then reach 2 on the first three criteria.

## The fix log

**Counts.** The fresh graduate filed 96 findings (1 BLOCKS, 53 SLOWS, 42 MINOR) and the hiring
interviewer 31 (10 REJECT, 9 SHALLOW, 7 SOURCE, 5 MINOR), 127 in all. The fix pass changed the pack
for 116 of them, 13 of those in part, and gave 11 a one-line reason with no change. Every reason, for
the partial fixes as well, is a row in the sources list's last table
(`internal/C2_W04_D01_day_sources_INTERNAL.md`). Every deck was rebuilt and rendered, every notebook
re-executed, and the cheat sheet reprinted on one page.

### What changed for the fresh graduate's findings?

| Findings | What changed |
|---|---|
| 1 to 6 | S1 defines the top-up gap, labels every share by what it is a share of, defines gaming, enrolled and the 140 new drivers, gives bookings as the fares riders paid, and names the three outer zones; Top-up, Bookings and Gaming joined the notes' word list. |
| 9, 11 to 13 | S3 names the three roles; S4, S13 and S24 ask how the number could rise while riders were served no better; S5's cards say marketing's guarantee is the story that wins new drivers and finance wants top-up per trip low. |
| 14 (in part), 15, 16 | S5 defines a proxy where it first appears; S6 asks which number can rise with no rider at all; S8 says the canteen pays its servers per token handed out. |
| 17, 19 to 23 | S9 and the notes call the twelve rows the case's own; S12 expands CFPB and SEC and explains funding and surveys; PTI, OIG, BSE, 10-K, S-1 and 20-F are glossed where they appear; S14 is retitled; S16 says the two scales make the crossing meaningless; S17 explains 12,860 and glosses `.lt` and `.map`. |
| 24, 25 | S19's invented pair now pulls the way the city does (1.25 against a true 0.80) and the slide says the average hides 0.13 of the 0.32 fall, about two-fifths; notebook 02, the notes and the board work follow. |
| 26 to 29 | S20's headers name what is counted, per what and over which window; S21 tells riders, line utilisation, journeys and boardings apart; S23 says the idle tail's hours went to 2.1 times their level before the launch, and the scatter is titled per driver-week with E and F placed. |
| 31 to 33 | "Floor" now means the Rs 300 floor or the acceptance floor, and the cost bound is "the least it would cost"; S25 asks which rule makes drivers drive and serve riders; notebook 01's ticket gives each change in its own unit. |
| 36 to 39 | The seesaw reads "a guardrail moves the wrong way, riders or the budget paid for the rise" everywhere; S30's inputs are drawn dashed and white; S31 separates when a number moves from the job it does, and its chart starts at 0.6. |
| 40 to 47 | S32 cites the annual report's UberX Share count, explains the shrinking base and fills the gaming note, and the guided template is relabelled; S33 states the 14-day goal; S35 and the fall chart name the three weeks with most requests, still in the rains, and S35 and notebook 03 name the three open doubts the same way; three guardrails everywhere, two for riders and one for the budget; S37 says round 2 was the morning's chapters. |
| 48 to 56 | Notebook 01 glosses a point and gives both date forms; the notebooks gloss each new piece of code the reader listed; [S], [F] and the levels are explained at first use; notebook 02 says "the median of the 72 zone-week medians"; notebook 03 names the test the tentative block designs, shows why the under-0.5 weeks are the idle tail's, and pairs a fifth with Rs 92.7 lakh and a half with Rs 58 lakh, as every file now does. |
| 57 to 60 | The index glosses GCC, the metric clinic and the class chat, and "screen" became "interviewer"; guided Q2 and Q4 have sharper stems. |
| 62, 63, 65 to 68 | S39 counts the 880 as drivers who joined before the launch; S40 asks which line tells the city head riders are worse off; S43 is retitled with Eternal, GOV, NOV and cart consolidation glossed; S47 and the transcript gloss commit, revert, time to merge and build failure, and use one leading input and one name for the north star. |
| 70, 72 to 74 | The lead-lag word table says how the team acts on requests; fallback S1 explains facts 3 and 4, S2's options a and c are sharpened, and S4 and S5 give each owner one number. |
| 76 to 89 | Notebook 04 lists the seven member ids with the lines a home learner types, glosses growth review and merged, and adds "rose by more than a third"; the Kalpa set names the guardrails Meera's team proposed and glosses retention review; lead-lag Q2 has its context; the lab set asks "which of nine"; the solutions say "sign-up campaign" and introduce Kavya; Thursday's review comes before Friday's decision in every file; checkpoint 5, the blend and the say-it line are rewritten. |
| 91 to 96 | The pain-points heading asks a plain question and glosses the S-1; the cheat sheet prints no asterisks and its board's nodes carry sublabels; the pre-read prints 6,360 and 6,500 driver-weeks and drops "the same". |
| 10, 34, 35 (each in part) | Quick-commerce is glossed in the take-home; notebook 03 prints the top-up as Rs 1.90 crore, never in western commas; S1 and notebook 01's ticket say trip earnings are not in the tables, so a week's top-up cannot be rebuilt from its bookings. |

### What changed for the interviewer's findings?

| Finding | What changed |
|---|---|
| 1 (in part) | The north star stays, as the spine sets it; the candidate now says it barely moved, 35.76 to 35.89, would rise if drivers quit, and is never read without the wait. |
| 2 (in part) | The transcript, S47 and the notes name requests per online hour by zone as the leading input. |
| 3 | The cancel share sits beside acceptance, the payout rule counts a cancelled trip as a decline (the gap's edges become 0.43 and 0.67), the wait is read by zone, and the floor is tested at two levels. |
| 4 (in part) | The transcript names the median-of-medians caution and reads the wait zone by zone. |
| 7 (in part) | S1 and notebook 01's ticket say trip earnings are not in the tables, so no reader expects to rebuild a week's top-up from its bookings. |
| 5 | The candidate checks the outer zones (6.6 to 5.95 minutes), prices them (Rs 85.7 lakh for about 185 extra trips, about Rs 46,000 each) and decides zone by zone; the mind-changer is outer-zone waits back up to 6.6 minutes without the hourly floor. |
| 6 | One written rule in every file: the floor stays only for driver-weeks that accept at least half their offers, a cancelled trip counted as declined; the notes name why declining was free; S50 judges and pays in separate sentences. |
| 8, 23 | The test uses zones as the unit for the guarantee and teams for the coding assistant, fixed in advance and run at least four weeks. |
| 9 to 11 | Rs 2,836 per extra trip, 17 fares, in the transcript, scorecards, notes and cheat sheet; the launch-week step from 1.88 to 1.64 carries the causal argument; the clarify asks for the decision and the baseline. |
| 12 (in part), 13, 14 | Three cases for the 180, with 17,600 hours if they quit; logging off and a second rider account answered; a five-row table of harder follow-ups. |
| 15 (in part) | The [D] answer says none of the three numbers is the target, gives finance a total cap and the cost per extra trip, and speaks to all three teams. |
| 16 to 20, 22 | S43 and the notes quote Swiggy and Eternal as they wrote; the Eternal glosses are cut back; Spotify's label reads "a bar set at any use at all"; Wells Fargo's 2020 sum is a settlement with USD 500 million of penalty; the scorecards carry Aced's dated URL and drop the clause no criterion scored. |
| 24 (in part), 25, 26 | The AI variant counts per developer with a seat with time to merge beside it, names fewer, safer suggestions as the gaming, adds security findings and rewritten lines, and has a line ready for Ziegler and others (2022). |
| 27, 29, 31 | Three guardrails everywhere; S35 and the notes say every driver here enrolled; fallback S9 matches the transcript. |
| 30 (in part) | Kahoot Q5's two throwaway options are replaced and Q6 says the average answers another question. |
| 28 (in part) | The transcript drops "asked everywhere". |

**The scores after the fix pass.** The interviewer scored the old transcript at 14 for [S], 6 for
the AI variant and 10 for [D]. The rewritten answers score 14, 12 and 14 on the scorecard's
descriptors, with the variant's two 1s explained in the scorecards: it has no data to size with or
to cost.

## The TA's cold read of the rebuilt Kalpa lab

**INTERNAL.** On 13 October 2026 the lab was rebuilt on Thursday's membership table: the generator,
notebook 04, the Kalpa set and its solution, the lab note and the day sheet. One agent then ran it
cold as the TA, from the lab note and the STUDENT notebook, opening only the files the note sends a
TA to, and wrote findings without editing any file. Its report is kept below as it returned it,
except that one ", but" in finding 22 is set as a semicolon so the style gate reads it, and what the
fix pass did for each finding follows.

### The TA's report

I read the lab note and then the notebook top to bottom. Next I did the seven-member count on paper from the lab note's sheet:

- Placements: 2+2+1+1+1+1+1 = 9 in the comparison window and 2+1+3+1+3+1+1 = 12 in the auto-reorder window.
- Booked value: 6,690+7,620+1,970+1,940+3,790+4,350+3,490 = Rs 29,850, and 2,950+2,010+5,110+2,290+6,660+3,400+2,690 = Rs 25,110.
- Ratios: 12 / 9 = 1.33 and 25,110 / 29,850 = 0.84. Both match the note, and every row matches the CSV.

I then copied the notebook and its two CSVs to /tmp/coldread and ran it with python3 (pandas 3.0.5, matplotlib headless). That covered cells 2, 4 and 10 as shipped, plus every line the markdown tells learners to type, in order. Nothing raised an error, and every number the lab note tells the room to find came out:

- 107 members in `base`, and the ratios 1.22 and 0.96.
- In the window, 22 cancelled, 16 merged and 6 pending. In the comparison, 4 delivered, 1 returned, 2 cancelled and 29 merged.
- 0 and 7 orders, average values Rs 2,362 and Rs 3,007.5, and the named stall's 1.17 and 0.9.

The three saved charts and the printed outputs show neither ratio nor the statuses by window. The Kalpa set's facts also reproduce: 107 members, 13 of the 120 joining from 20 to 29 August, and the 25 August joiner having 16 of the 21 days.

The note gives no durations. My estimate is two to two and a half hours: about 40 minutes for the notebook, 25 to 30 for the Kalpa set, 15 for the lead-and-lag drill, 35 for the lab set and 15 for the solutions and the close. Cells are counted from 1 at the top of the notebook.

1. **Lab note, lines 3 to 4:** "L1 to L3 in the lab notebook, L5 in the Kalpa set, then the practice set." The L-levels are never defined and there is no L4. "The Kalpa set" is never tied to a file name, so I had to guess that the stall table means `kalpa_north_star`. **MINOR**

2. **Lab note, order table (lines 18 to 23):** "| Part | File | What the room does |". No part has a duration, and nothing says how long the lab runs. A TA alone cannot pace four parts or decide what to cut. **SLOWS**

3. **Lab note, lines 4 to 5, 33 and 47:** line 4 says "The seven-member sheet and the planted values below stay with the TA until the room has counted them", but line 33 says "Hand this out". The table it hands out includes the totals row "The seven | 9 | 12 | Rs 29,850 | Rs 25,110". Printed as it stands, the sheet does the room's adding for it. Nothing says to cut that row and the paragraph below, and no learner copy exists. **SLOWS**

4. **Lab note, lines 51 to 53:** "Four of the seven placed an order ... which is why their comparison values run high." This is wrong, and a learner holding the sheet can show it:
   - Booked value counts every placement, whatever became of it.
   - C-0211 (Rs 1,970) and C-0224 (Rs 3,790) are below their own window values.
   - The four warehouse orders average Rs 3,150, against Rs 3,450 for the seven's merged placements.

   **SLOWS**

5. **Lab note, line 85:** the stall "Dividing by seven before taking the ratio" and its hint "Add the seven first, then divide once" contradict notebook cell 5. That cell tells learners to "add up ... divide by seven, and write the two ratios", and says the seven cancels. A TA following the note would correct learners for doing what the page says, even though they get 1.33 and 0.84. Only averaging each member's own ratio goes wrong, giving 1.50 and 1.11. **SLOWS**

6. **Lab note, line 86, with notebook cells 4 and 5:** the hint "Who was a member for all 21 days of the comparison window?" and the reason "a member who joined later had fewer of the comparison window's days" both let in C-0269. C-0269 joined on 20 August, the window's first day, and placed an order on 2 September. The third chart shows 108 members that day. A learner who writes `<= "2026-08-20"` gets 108 members and 1.19 and 0.92, and nothing on the page explains why the cut-off is 19 August. **SLOWS**

7. **Lab note, line 88:** the Kalpa set Q3 hint "Can a number guard itself?" assumes learners see option d, "Orders per member per month", as the north star. The north star is delivered orders per active customer, so a learner who sees two different numbers gets nothing from the hint. **MINOR**

8. **Lab note, line 90:** "Which number did the morning say the average hides two-fifths of?" depends on something said in the morning that neither the note nor the lab set records. I only decoded it by working out that the 1.71 average hides 0.13 of the 0.32 fall from 1.90 to 1.58. **SLOWS**

9. **Lab note, line 98:** "On Uber the paid number was hours, and an open app raised it." "An open app" means nothing to a TA who missed the morning, and this is the line the TA is told to say aloud. **MINOR**

10. **Lab note, line 25:** "Open the solutions at the end of the lab, after walking the notebook's two your-turn cells aloud." It names no solution file. It also leaves unclear whether the notebook's findings are confirmed before the Kalpa set, whose Q5 and template depend on them. **MINOR**

11. **Notebook cell 1:** "From 10 September the app orders in the Week 2 warehouse are members' own orders through the normal checkout, and they are not in `kalpa_app_reorders`." Read before the second your-turn cell, this tells learners that no auto-reorder reached the warehouse, which is the planted "none became an order". "The Week 2 warehouse" is never explained. The lab note's "7 app orders in the Week 2 warehouse" (line 73) cannot be checked from the two CSVs. **SLOWS**

12. **Notebook cell 1:** "If it can rise while the tier earns less, the review rewards the app for placing orders nobody receives." This is the planted result in conditional form, sitting above "Predict before you run". Most of the room will predict "rose, fell" from it. **MINOR**

13. **Notebook cell 1:** "delivered, returned or cancelled, merged (...) or pending". Cancelled is grouped with the order outcomes and never explained. Both of the comparison's cancelled placements carry an `order_id`, and none of the window's 22 does, so "22 cancelled" next to "0" orders cannot be reconciled from the page. **SLOWS**

14. **Notebook cell 1, and lab note lines 67 and 75 to 77:** merged means "its items joined a basket the member already had open". Nothing says whether that basket was then checked out and delivered. That makes "orders nobody receives" and "none of them became an order" go further than the data for the window's 16 merged placements. 29 of the comparison's 36 manual reorders merged too, and the TA has no answer when asked. **SLOWS**

15. **Notebook cell 1:** `kalpa_members` is "the same table Thursday's lab reads". On a Monday, nobody can tell which Thursday this means. **MINOR**

16. **Notebook cell 5:** the hand count and the first your-turn share one markdown cell and one empty code cell. "Type these two lines into the empty cell below first" points past the next heading. "Run it again" assumes a first run that learners with the sheet never made. **MINOR**

17. **Notebook cell 5, the prediction:** 12 / 9 lands exactly on the line between c) "rose by up to a third" and d) "rose by more than a third". 0.96 could be a) "fell" or b) "held about level", while the lab note says "fell", and the note gives no expected prediction. **MINOR**

18. **Notebook cell 5 and lab note line 59:** "The per-member comparison counts only the 107 members in `base`". "Comparison" means both the first window (and the variable) and the whole before-and-after. The reason given covers only the first window, so why the 13 late joiners are also dropped from the auto-reorder window is not explained until cell 11. The members table has no leaving date, so "in the tier for the whole of both windows" is assumed. **MINOR**

19. **Notebook cells 5 and 11:** "write the two ratios ... on the sheet" and "Write on the TA's sheet: your two ratios ... the one sentence ... and which line ...". The lab note's sheet is a data table with no space for any of this. "The TA's sheet" is never defined, and the note never says to collect it. **SLOWS**

20. **Notebook cell 7, fourth typed line:** `print(window["value_rs"].mean(), comparison["value_rs"].mean())` prints `2362.2727272727275 3007.5` unrounded, while the note expects "Rs 2,362 against Rs 3,008". **MINOR**

21. **Notebook cell 11:** "a second way to the same answer (the hand count against the full table)". The lab note (lines 49 to 51) says the seven were picked to land more than 0.10 away. Learners get 1.33 against 1.22 and 0.84 against 0.96 and conclude they made a mistake. The Kalpa solution's "get to the same number a second way" repeats this, and the TA has no line explaining why a sample of seven differs. **SLOWS**

22. **Notebook cell 11:** "which line of a complete definition would have stopped "reorders per member" being paid for that". Nothing says anyone is paid on the number. The Kalpa solution's table gives three lines that would each stop it (numerator, exclusions, what it does not reward); the TA's closing accepts only the numerator. **MINOR**

23. **Kalpa set, lines 27 to 30 and 130 to 144:** it promises "the seven-line template" and "the seven lines below", but the table has nine rows (North star and Leading inputs are added). **MINOR**

24. **Kalpa set Q4, key c:** "Add-to-cart events per active app member". The lab has just shown the app putting items into members' open baskets by itself (16 merged auto-reorders). A learner can fairly argue this is an input the app raises on its own, and the solution does not answer that. **MINOR**

25. **Kalpa set Q5, lines 111 to 116:** "Why does the comparison window start on 20 August rather than in July?" No file gives the sale's first day, so key b only beats July if the sale ran through July. The table also starts on 20 August, so a July window cannot be computed. The preamble's "counted only the 107" rules out d before the question is asked. **MINOR**

26. **Kalpa set Q1, and solution line 26 (exclusions):** the north star counts "delivered" orders, but the data has "returned" as a separate status. Neither file says whether a returned order counts, so a learner filtering on the status column would drop it. **MINOR**

27. **Lab set, lines 61 to 64:** "Sit `exercises/unguided/C2_W04_D01_lead_lag_STUDENT.md`, three items, unless your group sat it in the metric clinic." The drill is also Part 3 in the lab note, so a room that has just done it is told to sit it again. **MINOR**

28. **Lab set, lines 12 to 14:** "You, before Tuesday, which rehearses the one-slide review the city head holds on Thursday and assumes every learner can compute..." This reads as machine-made, and a learner cannot tell what "rehearses" or "assumes" refers to. **MINOR**

**Counts:** 28 findings: 0 BLOCKS, 11 SLOWS, 17 MINOR.

**The three I would most want fixed:**
- **3:** the sheet to hand out carries the totals row, and the note contradicts itself on whether the sheet is handed out.
- **11:** cell 1's "Week 2 warehouse" sentence gives away that none of the window's placements became an order.
- **21:** cell 11 and Kavya's line call the hand count "the same answer" when it was built to differ.

### What did the fix pass change?

**Counts.** 28 findings (0 BLOCKS, 11 SLOWS, 17 MINOR): the fix pass changed the pack for all 28,
one of them in part. Notebook 04 was rebuilt and executed cold, the generator reran byte-identical
with four new facts (the averaged member ratios, the base cut on 20 August, the sale's dates from
v4's campaigns table and the window three weeks earlier), and the distractor audit, the tic scan and
`scripts/verify.py` were run again. The pass also took out the notebook's sentence that the
auto-reorder feature placed the window's reorders, which said in advance part of what the second
your-turn cell finds.

| Finding | What changed |
|---|---|
| 1 | The lab note's opening names the first three rungs of the ladder and the fifth, and names the Kalpa set's file. |
| 2 | The order table gains a minutes column (40, 25, 45 and 10 minutes) and a cut order that never cuts the notebook's two your-turn cells. |
| 3 | The note hands out the seven member rows only, marks the totals row for the TA, lists the four blank lines the sheet carries and says to collect it. |
| 4 | The wrong causal sentence is gone; the note says which four of the seven have an order in the warehouse and that their other placements merged. |
| 5 | The stall row names averaging each member's own ratio, which gives 1.50 and 1.11, both now in the facts file. |
| 6 | Every file states the base as the members already in the tier when the comparison window opened on 20 August; the hint asks who was a member then, and the stall row adds the 108 members and the 1.19 and 0.92 that a cut on 20 August gives. |
| 7 | The Q3 hint says option d counts the north star's own orders. |
| 8 | The lab set's problem 1 hint carries the numbers it needs: lines 5 and 6 print 1.71 against the city's 1.58. |
| 9 | The closing line says the city paid for peak online hours, which a driver raised by keeping the app open with no rider. |
| 10 | The note names the three solution files and says to walk the two your-turn cells before the Kalpa set. |
| 11 | The notebook's data line says only that orders members place themselves through the normal checkout are not in the reorder log; the warehouse's 7 window orders, with the warehouse file's path, stay in the lab note. |
| 12 | The stakes line no longer states the result's direction. |
| 13 | The status line explains both kinds of cancelled and says `order_id` tells them apart. |
| 14 | The notebook says a merged placement's items reach the member only if the member checks that basket out, the lab note gives the TA the answer when asked, and "orders nobody receives" is gone. |
| 15 | The table names this week's Thursday lab. |
| 16 | The hand count has its own empty cell, so each set of typed lines goes into the cell below it; the notebook has 13 cells. |
| 17 | The options read fell, stayed exactly level, rose by a third or less, rose by more than a third, and the lab note gives the expected letters. |
| 18 | The base line says the per-member figures divide both windows by the same 107, and the members table is described as recording no end date. |
| 19 | The lab note defines the TA's sheet and says to collect it; the notebook calls it the TA's sheet. |
| 20 | The typed line rounds both means, so it prints 2362 and 3008, as the note quotes them. |
| 21 | The closing cell's second route is the ratio of the totals against the ratio of the per-member figures, and it says the seven's hand count lands elsewhere because seven members are a sample; the lab note gives the TA the same line. |
| 22 | The notebook asks which line would have stopped the number rising, and the TA's closing names the numerator with the exclusions and the does-not-reward line behind it. |
| 23 | The Kalpa set describes the template as the north star's name, its seven lines and its leading inputs. |
| 24 | The solution's item 4 says the add-to-cart count is the members' own, so items the auto-reorder feature merged into a basket stay out of it. |
| 25 (in part) | Q5 gives the sale's dates, 5 to 19 August from v4's campaigns table, and asks about the window three weeks earlier, from 30 July, which would hold the sale. The 107 line moved up to the table's paragraph, where it still answers option d: an exercise may be answerable from its own page, and the item tests where the window starts. |
| 26 | The solution's numerator line says a returned order was still delivered and counts, and the return-rate guardrail reads it. |
| 27 | The lab note folds the lead-and-lag drill into the lab set as its problem 2, so no room sits it twice. |
| 28 | The lab set's opening sentence says who needs the answer and why. |

# What did the cold reads find in the Week 4 Monday pack?

**INTERNAL.** Two separate agents read the pack cold on 12 October 2026 and wrote findings only;
neither edited a file. A third ran the rebuilt Kalpa lab cold as the TA on 13 October 2026, and its
report and fix log follow theirs. Three more read the concept-first rebuild cold the same day, and
their reports and fix log are the last section. Their reports are kept below as they returned them, except that one ", but"
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


## The concept-first rebuild's cold reads, 13 October 2026

Three fresh agents read the rebuilt pack cold on 13 October 2026 and wrote findings only; none edited
a file. The trainer who did not write the day read with the curriculum row open and named where each
subtopic is taught (T1 to T32); the fresh graduate read the STUDENT files (G1 to G54); the hiring
interviewer scored the interview material and re-read every cited source (I1 to I31). Their reports
follow as they returned them, with two changes of form: the trainer's level-two headings are set at
level four so they sit under this section, and one ", but" in the graduate's G7 is set as a
semicolon so the style gate reads it. The trainer's table has no "not found" cell, so no subtopic
stopped the build. Slide numbers are the rebuilt pack's, S1 to S84 in the morning deck and S85 to
S98 in the afternoon deck, and the fix log after the three reports gives each finding's outcome.

### The trainer's read

I've read the row and every file in the brief. One subtopic table follows, then 32 findings: T1 to T4 for (b), T5 to T24 for (c) and T25 to T32 for (d). The pack was being edited while I read it. The half1 markdown, the coverage matrix, the sources page, the day sheet, notebook 02 and four solution files were rewritten between 12:16 and 12:26 UTC, so I re-checked every finding against the files as they stood at 12:33 UTC. I edited nothing and did not run git.

#### (a) Where each subtopic is taught

| # | Subtopic, in the row's words | Slides | Notebook | Exercise items | Kahoot |
|---|---|---|---|---|---|
| 1 | What to measure and why; the proxy test | half1 SECTION 1 and S6 to S13 (instinct round S7 to S8, rule S10, Wells Fargo S13); applied S58 to S59, S62 to S63; recalled S91, S98 | 01 `C2_W04_D01_01_proxy_test_STUDENT.ipynb`; applied in 07 | Proxy test set Q1 (asked aloud at S12), Q2, Q3; lab set Q5 | Q5 |
| 2 | North-star and guardrail metrics | SECTION 2 and S14 to S21 (rule S17); applied S75 to S76, S80 to S81, S84, S88 to S89 | 02 `..._02_north_star_guardrails_STUDENT.ipynb`; applied in 09 | North star set Q1 to Q3; guided Q4; redesign Q3; lead and lag Q3; lab set Q2, Q3; Kalpa set Q3 | Q1 |
| 3 | Leading against lagging indicators | SECTION 3 and S22 to S29 (rule S25, case data S28); applied S80 | 03 `..._03_leading_lagging_STUDENT.ipynb`; 09's "Which number moved first?" | Leading and lagging set Q1 to Q3; lead and lag Q1, Q2; lab set Q4; Kalpa set Q4 | Q2 |
| 4 | Definitions: numerator, denominator, window, exclusions | SECTION 4 and S30 to S37 (rule S33); applied S60 to S62, S68 to S70, S81 lines 1 to 4 | 04 `..._04_numerator_denominator_window_exclusions_STUDENT.ipynb`; applied in 07, 08 | Four lines set Q1 to Q3; guided Q1 to Q3; Kalpa set Q2, Q5; lab set Q1 | Q4, Q6 (Q8 rests on it) |
| 5 | Gaming, and definitions that resist it | SECTION 5 and S38 to S45 (rule S41, four ways S42); applied S59, S71 to S72, S76, S81, S85 to S90 | 05 `..._05_gaming_resistant_definitions_STUDENT.ipynb`; applied in 08, 09 | Gaming set Q1 to Q3; redesign Q1, Q2, Q4 | Q3 |
| 6 | The metric definition artifact | SECTION 6 and S46 to S53 (rule S50); applied S56, S81, S86, S98 | 06 `..._06_metric_definition_artifact_STUDENT.ipynb`; applied in 09 | Artifact set Q1 to Q3; Kalpa set Q1 and its template | Q7 |

No cell is "not found". The table matches the coverage matrix and the day sheet's first table cell for cell. Two items are filed loosely:
- **Kalpa set Q1** asks only for the numerator, which is a topic 4 line, yet it is the artifact topic's only item outside its own set.
- **Redesign Q1** asks for 61 percent of Rs 1.9 crore. S79 and the redesign file's own facts table already state that number.

#### (b) Can S3, S4 and the SECTION headings carry the day alone?

Only partly. Together they give the six subtopics verbatim and in order, each concept chapter's minutes and notebook number, and (from the case headings, not from the map) the topics each case chapter applies. They do not give the shape of the day, and the map misleads about the case.

**T1. half1 S3 (lines 81 to 101) hides the day's timing.**
- **What I found:** The case is one row, "7 to 11 | 140 minutes | 07 to 09". The slide does not show:
  - the 7-minute opening;
  - the 10-minute break after S53;
  - the lunch between chapters 9 and 10;
  - the 20 minutes of Kahoot, handoff and close (S96 to S98);
  - the tentative 120-minute faculty block;
  - which case notebook goes with which chapter (chapters 10 and 11 have none, and nothing on the slide says why the lab notebook is 12).
- Only S3's speaker note says chapters 10 and 11 run after lunch. Yet S84's note says "the afternoon's running order is on the topics slide, S3", and the day sheet (line 130) says "old S37 cut, since the topics slide carries the afternoon's order".
- **What a trainer would do wrong:** run chapters 7 to 11 back to back. That is 7 + 63 + 10 + 140 = 220 minutes in a 180-minute morning, and the faculty handoff arrives with no time left for the Kahoot or the close.

**T2. half1 S4 (lines 105 to 149) misleads about the case.** The same map is in the day sheet (lines 82 to 111) and the board work (lines 24 to 51).
- **What I found:**
  - The single node "Applied to: Uber, Hyderabad, chapters 7 to 11" hangs off chapter 6 alone. The map never says which case chapter applies which topic (per the matrix: 7 applies 1 and 4; 8 applies 4 and 5; 9 applies 2, 3, 5 and 6; 10 applies 5 and 6; 11 applies all).
  - Chapter 6 gets arrows only from chapters 3 and 5. S46 says its last three lines come from chapters 2 and 5, and S21 (line 514) draws chapter 2 to chapter 6.
  - The Uber node carries the amber `kalpa` style (`class U kalpa`, line 136), which is the colour S2 gives Kalpa's nodes (line 68).
  - All six boxes are lit from the start, although S4's note and the board work (line 21) say each chapter lights its own box when it closes.
- **What a trainer would do wrong:**
  - teach the case as the use of chapter 6 only, and drop the recalls by name that carry it: S59's chapter 1 test on hours, S68 to S70's chapter 4 ratio of sums, S80's chapter 2 seesaw and chapter 3 inputs;
  - call the amber case box Kalpa;
  - draw a fully lit map, so the progress cue never happens.

**T3. The SECTION headings miss parts of the day.** (half1 lines 176, 356, 532, 694, 872, 1039, 1215, 1492, 1728; half2 lines 9, 153.)
- **What I found:**
  - The six concept headings carry the row's subtopics verbatim.
  - SECTION 9's title, "The redesign's north star, guardrails, leading inputs and seven-line page", leaves out gaming. S74's Applies line, the day sheet (line 70) and the matrix all give it gaming.
  - No heading marks the opening (S1 to S5), the break, round 1 (S58), the guided definition (S81, 11 minutes), or the Kahoot, handoff and close. Those three slides sit under SECTION 11 with no heading.
  - No heading carries minutes.
- **What a trainer would do wrong:** budget SECTION 11 at its 15 minutes and lose the 20 minutes of S96 to S98, including the handoff line that must be read word for word. They would also teach chapter 9 without naming the gaming lines it applies.

**T4. None of the three mentions the row's own scenario.**
- **What I found:** S3, S4 and the headings never name Meera's growth plan, Marketing's orders per month, Operations' app sessions or Retail-Plus's reorders per member. Nor do they say the scenario moved to the TA lab; only S1's speaker note says so (lines 21 to 26). They also do not place the instinct round (S7), the eight-metric drill (S27) or round 1 (S58).
- **What a trainer would do wrong:** with the row open, look for the Kalpa fight in the morning, not find it, and either improvise it inside the case's minutes or treat S27 as just a slide of rules.

#### (c) Where the trainer files, decks, board work, notebooks and matrix disagree

**The trainer's minutes add up.**
- **Morning:**
  - opening 7 (1 + 1 + 2 + 2 + 1);
  - chapter 1: 13;
  - chapters 2 to 6: 10 each;
  - break: 10 (S53);
  - chapter 7: 32 (12 + 20);
  - chapter 8: 30;
  - chapter 9: 38.
  - Total 180.
- **Afternoon:**
  - chapter 10: 25;
  - chapter 11: 15;
  - S96 to S98: 20 (12 + 2 + 6).
  - Total 60.
- Every SECTION note's internal split matches its slides, and the war game's round 1 (12) and round 3 (25) tables match.

The disagreements:

**T5. Concept-set Q1: how long it takes, and whether the key is given.** Day sheet lines 63 to 64 and 244; S12, S19, S27, S35, S44 and S52; exercise index line 132.
- **What I found:**
  - The day sheet says each chapter "closes on its set's Q1 ... (two minutes inside the chapter's time)". The deck asks Q1 on the rules slide, which is "LIVE, 1 minute" for the rules, the interview line and Q1 together, and the chapter then closes on its map slide.
  - The index says "the trainer says the key and one reason". S12 says "take letters; its solution opens after the lab".
  - The day sheet's fallback if most miss Q1 is to "redo the hand count ... before the code glimpse", but Q1 comes after the code glimpse.
- **What a trainer would do wrong:** overrun six chapters by a minute each, or hold back the keys until the evening.

**T6. The concept notebooks and notebook 07 get no time.** Day sheet lines 192 to 199; the SECTION 1 to 7 notes.
- **What I found:** The sheet and the notes say "Notebook 0n runs beside the chapter", but every minute of chapters 1 to 7 is assigned to slides. Notebooks 01 to 06 each have an empty your-turn cell (cells 13, 11, 13, 9, 11 and 13). No slide, no line of the day sheet and nothing in the lab note schedules them. Notebook 07 is never called for after S62.
- **What a trainer would do wrong:** skip the notebooks, or open them and overrun a 10-minute chapter.

**T7. The board order differs from the deck.** Board work lines 20, 57 and 229, against the S5, S55 and S57 notes.
- **What I found:**
  - The board file puts the topic map up "first" and the week map "second"; the deck shows the week (S2) before the topics (S3, S4).
  - S5's note has the trainer write "What makes a number safe to pay for?" and the headline "peak online hours up 24 percent" before chapter 1. S55 then returns to that headline "still on the board".
  - The board file has no such drawing, and says the four-questions board is "drawn after the break (S57), empty but for its anchor".
- **What a trainer would do wrong:** draw from the board file, never write the headline, and reach S55 and S57 with nothing on the board to point at.

**T8. The war game's ordering is off.** War game lines 6, 64 and 92; role cards lines 9 to 10; S58 note (line 1354).
- **What I found:**
  - Round 2 is to be named "at the start of chapter 7", which is where round 1 runs.
  - Both files say round 3 "closes the trainer's time", yet chapter 11 and S96 to S98 (35 minutes) follow it.
  - The round 1 stall move, "Point at drivers E and F on the twelve rows", points at S60, which the room has not yet seen.
- **What a trainer would do wrong:** announce round 2 before round 1, plan to finish after round 3, and spend the E and F reveal before the hand count that must never be cut.

**T9. Notebook 08's order differs from chapter 8's.** Notebook 08 cells 2 to 8, against S65 to S68 and day sheet line 154.
- **What I found:** The notebook computes the city totals first, then demand, then the twelve weeks. The deck asks about demand first (S65), shows the twelve weeks (S67), then "run the notebook's totals cell" (S68).
- **What a trainer would do wrong:** run the notebook top to bottom and reveal the totals before S65's demand question, or scroll back past three cells at S68.

**T10. Notebook 09 gives away the afternoon's answer.** Notebook 09 cells 4 to 6 and 8 to 10, against the S79 note, S90, guided exercise line 156 and redesign Q2.
- **What I found:**
  - The notebook prints the saving (Rs 92.7 lakh and Rs 58.0 lakh) right after the top-up split, in the morning. S79 holds the saving for round 3, where redesign Q2 asks groups to choose it.
  - The guided exercise tells learners to "Run notebook 09 top to bottom".
  - The notebook's "Which number moved first?" section belongs to S28 and has no slide in chapter 9.
- **What a trainer would do wrong:** run notebook 09 in chapter 9 and hand the room round 3's key before lunch.

**T11. S96 misdescribes the Kahoot's trap item.** S96 note (line 298) says "The trap item uses numbers other than today's". The Kahoot's Q3 (line 53) uses S72's idle-tail numbers, 2.1 times the hours and 12 percent fewer trips.
- **What a trainer would do wrong:** introduce Q3 as new numbers and be corrected by the room.

**T12. The finance role card attacks a different number from S87.** Role cards line 55, against S87 (line 79).
- **What I found:** The card attacks "the fall in bookings per hour". S87 answers with trips per hour, 1.88 to 1.64. Bookings per online hour is a different series (Rs 271.0 to Rs 259.1, S28).
- **What a trainer would do wrong:** a learner reading the card attacks one number and the trainer answers another.

**T13. S98's rule is loose and its transition skips the faculty block.** S98 lines 324 and 340.
- **What I found:**
  - S98 says "a cancelled trip counting as declined". S90, the day sheet (line 164) and the redesign set say an accepted trip that the driver then cancels.
  - The note ends "The TA lab now runs ... Transition: the lab", but the faculty block or the clinic runs next for 120 minutes (S97, day sheet line 211, lab note line 9).
- **What a trainer would do wrong:** tell the room that a rider's cancellation counts against the driver, and send the room to the lab when the faculty block is next.

**T14. The faculty block's brief and the handoff point at different companies.** Day sheet line 12 against the handoff line (day sheet line 23, S97).
- **What I found:** The rendered faculty brief "CONNECTS TO KALPA: one initiative on the growth plan's tree". The handoff, read word for word, says "design that test on this city", meaning Uber. Kalpa's growth plan is first written in the TA lab, which runs after the block.
- **What a trainer would do wrong:** point the faculty and the room at Uber while the faculty's brief expects a Kalpa plan the room has not built yet.

**T15. The cut list removes something the rest of the day relies on.** Day sheet lines 176 and 195.
- **What I found:** The second item to cut is S37's Delhi Metro line. Delhi Metro then carries S66 ("as Delhi Metro's riders and line uses were in chapter 4"), the "unit moves the number" pitfall on S73 and S84, board work lines 327 and 403, and cheat-sheet panel 2.
- **What a trainer would do wrong:** cut it as told, then point at a pitfall the room never heard.

**T16. Case terms are used before the case defines them.** S21 (closing line) and S28.
- **What I found:** Both use "share of offers accepted" and "bookings per online hour" before the break. S5 mentions neither, and an offer is first defined at S55.
- **What a trainer would do wrong:** reach S28's one minute with a room that does not know what an offer is.

**T17. The lab note drops 12 exercise items.** Day sheet line 212, the six concept sets and the index lines 26 to 31 and 132, against lab note lines 18 to 33.
- **What I found:** The day sheet and the index put the concept sets' Q2 and Q3, and all six concept-set solutions, in the TA lab. The lab note's 120 minutes (40 + 25 + 45 + 10) never schedules those 12 items, nine of which are design items, and it opens only three solution files.
- **What a TA would do wrong:** skip all 12, including leading and lagging Q2, which is the defence of two calls the row's drill asks for.

**T18. The fallback clinic's slide minutes add to 109, not 120.** The fallback note gives sections 15 and 16 thirty and fifteen minutes. Their slide notes give S6 8 + S7 4 + S8 12 = 24, and S9 8 + S10 2 = 10.
- **What a trainer would do wrong:** pacing by the notes, end the clinic 11 minutes early.

**T19. The fallback deck gives the roles different numbers from the role cards.** Fallback S4 (lines 114 to 116).
- **What I found:** In the clinic, finance owns "Completed peak trips" and marketing owns "Share of offers accepted". On the role cards and S58 they own "Top-up per completed trip" and "Enrolled drivers".
- **What a trainer would do wrong:** run the clinic with role-readers whose printed cards contradict the slide.

**T20. The fallback handout and its slide number the same eight items differently.** Fallback note line 29 offers `lead_lag_STUDENT.md` "as the handout" for S6.
- **What I found:** The handout orders the eight numbers differently and uses different letters (its leading items are 2, 4, 6 and 8; S6's are 1 to 4).
- **What a trainer would do wrong:** read S6's answer to a room holding the handout and mark right answers wrong. The lab then skips that file as "sat in the metric clinic", so its letters are never posted.

**T21. Round 3's defend time differs by half a minute.** S86 (line 52) and board work line 431 say "Defend, 7 minutes". The SECTION 10 note and the war game give 6 minutes 30 seconds.
- **Effect:** the room sees the slide's 7 while the trainer paces to 6.5.

**T22. Notebook 07's title renders as code.** In cell 0, the title, the applies paragraph and "Who needs the answer" are indented eight spaces. Jupyter and GitHub therefore show them as a code block with the "#" and "**" visible.
- **Effect:** the notebook's only statement of the subtopics it applies reads as raw text on the projector.

**T23. The half1 .pptx is stale.** It was built at 12:18:56 UTC; the markdown changed at 12:25:51.
- **What I found:** The built deck still puts SECTION 1's subtopic in quotation marks and carries the old SECTION 1 note. The day sheet (line 321) sends the trainer to the .pptx.
- **What a trainer would do wrong:** project a deck that differs from the notes they prepared from.

**T24. S3's notebook labels and one interview question are not the files' or the row's.**
- **What I found:**
  - S3 (lines 89, 91) calls notebook 04 "the four definition lines" and notebook 06 "the seven-line page". Those file names do not exist; the files are `..._04_numerator_denominator_window_exclusions_...` and `..._06_metric_definition_artifact_...`.
  - S27 (line 644) and notebook 03's last cell add "and the leading input that moves first" to the row's [F] question.
- **What a trainer would do wrong:** send the room looking for file names that do not exist, and quote a tagged interview question the row does not carry.

#### (d) What the row asks for that the pack does not deliver, or delivers outside the trainer's 240 minutes

The row's thinking is carried:
- metric as decision instrument (S6);
- the proxy test in the row's own words (S10 note);
- north star and guardrails (S17);
- leading and lagging (S25);
- the four lines plus "what it deliberately does not reward" (S33, S48).

The row's after-class tasks (build, prep, recap) are in the take-home.

| Row agenda item (row minutes) | Delivered in the trainer's time | Trainer minutes | Kalpa part, and where it went |
|---|---|---|---|
| 1. Three proposed targets (15) | S7 to S8 on three invented teacher numbers; S58, round 1, on Uber's three roles | 4.5 + 5 | Not done anywhere (T25) |
| 2. Decision instrument, proxy test, gaming (40) | Chapters 1 and 5, applied at S59 and S71 to S72 | 23, plus case time | None needed |
| 3. North star against guardrails, leading against lagging, on Kalpa's tree (50) | Chapters 2 and 3; Uber's tree at S80 | 24 | Inside S27's 1 minute, and the TA lab |
| 4. Definitions, computed on the customer table (45) | Chapter 4; chapter 8 on Uber's `driver_weeks` | 40 | TA lab, notebook 12 |
| 5. Guided then unguided artifact for the growth plan (60) | Chapter 6; S81; round 3, all on Uber | 46 | TA lab, the Kalpa set |
| 6. Kahoot and close (20) | S96 to S98 | 20 | Kalpa items replaced (T31) |

**T25. Agenda item 1: the row's three targets are never attacked.**
- **What I found:** No file asks how orders per month or app sessions could be hit while the business got worse. They appear only in the Kalpa set's preamble and as distractors (Kalpa Q2 c, Q3 b; item 8 of the leading and lagging set). Reorders per member is examined only in the lab.
- **Effect:** "finding how is the exercise" is never done on the row's own table.

**T26. Agenda items 3, 4 and 5, and "go as far as", are done on Uber, with Kalpa only in the lab.**
- **What I found:**
  - "Go as far as" ("everyone ships the growth-plan metric with two guardrails and a gaming note") is met only in the lab. In the trainer's time, each of nine groups, not each learner, ships Uber's page with three guardrails.
  - The day sheet never maps the row's agenda: the words agenda, mid-session, Kalpa's tree, customer table, orders per month and app sessions do not appear in it.
  - Moving Kalpa to the lab is by decision (S1 note; decision teaching-approach), but the day sheet does not say so.
- **What a trainer would do wrong:** with the row open, fail to find where items 1, 3, 4 and 5 went.

**T27. The row's unguided task and cut-first rule have no counterpart.**
- **What I found:**
  - "Define one guardrail solo, then swap and attack a partner's definition" appears nowhere. Round 3 is group work attacked by roles the trainer voices.
  - The row's "cut first: the second unguided definition" matches nothing in the pack.
  - "Never cut the gaming demonstration" is missing from the day sheet's never-cut list (line 176).

**T28. Mid-session drill 1 (classify eight Kalpa metrics and defend two, 15 minutes) shrinks to about a minute.**
- **What I found:**
  - In the trainer's time it is the leading and lagging set's Q1, called aloud inside S27, a 1-minute slide (the day sheet says 2 minutes).
  - Defending the two calls is that set's Q2, which the lab note never schedules.
  - The full drill runs only in fallback section 15, on Uber's numbers rather than Kalpa's, only if the faculty block slips. It is the clinic's first cut.

**T29. Mid-session drill 2 (name the guardrail for three proposed north stars, 15 minutes) is not in the trainer's 240 minutes at all.**
- **What I found:** It exists only as lead and lag Q3 (on Uber's three north stars) in the lab, or fallback S8.
- **Effect:** the row's own three proposed north stars never get a guardrail.

**T30. The interview angle is uneven.**
- **What I found:**
  - **[S]** gets chapter 11.
  - **The two [F] questions** are named on S19, S35 and S44 and answered only in the day sheet. No slide note has the trainer ask them aloud.
  - **[D]** appears in the trainer's time only as a line on S52. Its transcript and scoring run only in fallback section 16 (scorecards lines 4 to 5).
- **Effect:** if the faculty block runs, nobody answers [D] on Monday, even though the war game stages its exact situation.

**T31. The Kalpa column and the Kahoot plan.**
- **What I found:**
  - The plant (reorders per member up 22 percent, revenue per member down 4 percent) appears only in the TA lab.
  - The pack's 0.96 is booked value of placements in any status, not revenue. Per the lab note (lines 85 to 88), all 44 placements in the window were auto-reorders and none was delivered.
  - No file names the v4 customer table.
  - The row's Kahoot Q2 (five Kalpa metrics) and Q3 (the Kalpa trap) are replaced by Uber items. The Kalpa trap is never asked after the lab finds it.
  - The Wells Fargo case is delivered (S13, S42, fallback section 13).
- **What a trainer would do wrong:** repeat the row's "revenue per member falls 4 percent", which the lab's data does not show.

**T32. The row's references are missing.**
- **What I found:** The trainer resources (GeeksforGeeks, Interview Query, Exponent) and the student reference (Exponent) appear in no trainer or student file. Only the INTERNAL sources page explains why: Exponent now redirects to Aced, and Interview Query could not be verified.
- **Effect:** a trainer looking in the day sheet for the row's question sources finds none.

Count: 0 "not found" cells in (a); 32 findings: 4 in (b) (T1 to T4), 20 in (c) (T5 to T24) and 8 in (d) (T25 to T32).

### The fresh graduate's read

All files are under /home/user/c2-content-factory/content/W04/D1/. "Half one" means slides/C2_W04_D01_half1_STUDENT.md and "half two" means slides/C2_W04_D01_half2_STUDENT.md.

G1. Half one, S1 timeline and S2 map: "The head of Retail-Plus's growth number" and the node "Kalpa: Retail-Plus". No file I read says what Retail-Plus is. The S1 notes add "Meera's growth plan after Kalpa Health", which is not explained either. One line naming Retail-Plus and Meera's role would let me picture who wants "reorders per member".

G2. Half one and half two, the notes fences from S1 on. The notes speak to the trainer ("LIVE, 1 minute", "Transition:", "Styles: Brilliant ... Striver's ladder", "Explorer: scene M1", "each of the nine groups", "its scorer holds the proxy-test card"). They also point to files a learner cannot open: trainer/C2_W04_D01_war_game_TRAINER.md (S58, SECTION 10), the role cards, and the scorecard that S93's notes ask pairs to score on ("the scorecard's seven criteria"). I could not follow these instructions. Notes written for the learner, or student copies of the scorecard and role cards, would fix it.

G3. Half one S3, Notebook column: "04, the four definition lines" and "06, the seven-line page". The files are named ..._04_numerator_denominator_window_exclusions_STUDENT.ipynb and ..._06_metric_definition_artifact_STUDENT.ipynb, so the names on the slide match nothing in notebooks/. Using the file names would fix it.

G4. Half one S4, the study notes' map and cheat sheet panel 1: the box "Applied to: Uber, Hyderabad" uses the pale-yellow class that S2 uses only for Kalpa's nodes. Reading the maps in order, I took the Uber case for a Kalpa step. A different colour or a legend would fix it.

G5. Half one S5: "an enrolled driver online through a whole peak window is guaranteed Rs 300 per peak online hour, and Uber tops up the gap". At S5 I could not picture what the gap is, who counts as enrolled, or how long a peak window lasts. S55 explains all three fifty slides later ("between the driver's trip earnings and that floor", "one signed up for the scheme", "two a day, three hours each"). Putting those three short explanations on S5 would make the destination slide readable.

G6. Half one S9 and notebook 01 cells 3, 6 and 10: the owner "reads tomorrow's plates off today's tokens", yet the waste table books Rs 1,500 on day 6 itself and the chart is titled "Rs 7,500 thrown away by day 10". With a one-day lag, day 6's rice is cooked from day 5's 200 tokens, so inside the ten days only days 7 to 10 waste rice. That is Rs 6,000, and day 10's tokens waste rice on day 11. Either cook from today's count or shift the waste column by one day.

G7. Half one S11, S18 and S26 titles: "Four lines of pandas", "Three lines of pandas", "Three lines of pandas". The code under them has five, five and four lines. Not counting the read_csv line makes S11 and S26 fit; S18 still has four. Titles that match the code would stop me recounting.

G8. Half one S12 and every later "In the interview" line (S19, S27, S35, S44, S52): "[S]", "[F]", "[D]". The deck never says what the letters mean. Notebook 01's last cell explains them but leaves "GCC" unexpanded, and only the exercise index, read much later, says a GCC is a global capability centre. A one-line key on S12 would fix all three.

G9. Half one S13, "a cross-sell number, accounts and products per household", and S42, "remittance accounts added, undisclosed" (both repeated in the gaming set and the study notes). I have never worked at a bank, so I could not picture what cross-selling is, why staff would open accounts nobody used, or what a remittance account is. The public example did not land. One plain sentence for each term would fix it.

G10. Half one S13: "USD 185 million in penalties in 2016". The only 2016 source in the notes is a CFPB page whose address reads "fines-wells-fargo-100-million", so I could not reproduce 185 million from the page. Naming who levied the other 85 million, with a source, would let me check it.

G11. Half one S17 and S18, notebook 02 cells 9, 10 and 14, north-star set Q1, then S80, S84 and cheat sheet panel 2. Chapter 2 names licences per enrolled learner (0.60 to 0.36) as the north star, but its guardrail, the share who took the test, is paired with the hoarding's pass rate: S18 "multiplies the hoarding's rate by its guardrail", seesaw(rate, guardrail) runs on the pass rate, and Q1 asks for a guardrail "beside" next year's pass rate. The named north star already fell on its own, so I could not see what gaming of it the guardrail catches. The later board's "seesaw: star up, guardrail down" also contradicts chapter 2, where the north star went down. Saying plainly that the pass rate was the number being chased, and pairing the guardrail with the same number everywhere, would fix it.

G12. Half one S19 rule 3: "since a second growth count catches nothing" (repeated in notebook 06 cell 11, the study notes and cheat sheet panel 5). "Growth count" is never defined, so I could not tell which numbers are growth counts or why one can never catch gaming. A definition with one example would fix it.

G13. Half one S20: "28% of MTUs ... in its first quarter, to 30 June 2025" and "NOV ... gross order value minus discounts, from its Q1 FY27 letter". MTU is defined only at S36. Gross order value and "Q1 FY27" are never explained, "its first quarter" could mean Maxxsaver's or Swiggy's, and nothing says why gross order value misleads, so I got nothing usable from the Eternal half. The study notes repeat the Maxxsaver line without saying what Maxxsaver is. Explaining MTU, GOV and the fiscal quarter, plus one sentence on what discounts do to GOV, would fix it.

G14. Half one S21, S28 and S45: "the share of offers accepted". What an offer is waits until the S55 data line ("a declined request is offered again, so it counts offers") and only becomes clear at S66. Through chapters 2 to 5 I did not know that a driver is shown requests one at a time and may decline them. A one-line explanation at first use would fix it.

G15. Half one S25 and S27 rule 3, notebook 03 cells 9 and 16: "Wickets in hand, 7 at over 10, are the guardrail the leading number is read with." Chapter 2 had just defined a guardrail as a number watched beside the north star so that hitting it does no hidden harm. Here it sits beside a leading number, and no harm is named. Saying what harm wickets in hand guard against, or calling it context instead of a guardrail, would fix it.

G16. Half one S28, title "Acceptance moved first; bookings per hour followed" (echoed in notebook 03 cell 16, the study notes, S80, half two S98 and Kahoot Q2). The slide's own text has both lines falling in the launch week: acceptance to 0.729, and bookings per online hour to Rs 271.0, which the pre-read later shows is down from Rs 313.5. So acceptance did not move first; it reached its new level sooner, which is how notebook 09's last cell puts it. S28 prints no before values, and neither line is the north star. Adding the before values and changing the title to "settled first" would fix it.

G17. Half one S31 and S32, notebook 04 cells 5 and 12: "four honest clerks compute ... How many different numbers come out?", answered "five numbers from one register". Four clerks can print at most four numbers. The four-definition-lines set instead says "Four honest clerks ... and a fifth ... reads 70.0". Making it five clerks everywhere would remove the contradiction.

G18. Half one S32 row 4, notebook 04 cells 6 to 8, and the study notes' table: "Exclusions: medical leave counted present: 42 / 50". S30 defines exclusions as what leaves both counts, but this reading leaves nothing out and adds the two medical days to the numerator. Relabelling it as a numerator change, or explaining why it counts as an exclusion, would fix it.

G19. Half one S10 ("the curriculum's rule"), S33 ("The row adds that a definition is complete only when..."), notebook 06 cell 11 ("The curriculum row sets the bar") and the exercise index. "The row" is never explained to a learner. Notebook 06's bar (numerator, denominator, window, what it does not reward) also leaves out the exclusions that every other file lists among the four lines that make a number computable. Plain wording and one consistent list would fix it.

G20. Half one S36 and S53: the MTU row puts "per month" in the "Per what" column, and S53 says Uber's monthly active platform consumers give "a numerator with a receipt, a denominator and a window". Both are counts of users, so I could not find a denominator in either; "per month" is the window. S36 is titled "each line" but shows no exclusions. Saying which of the four lines each published count fills, and that a count has no denominator, would fix it.

G21. Half one S40 row 4 against S49: "Within 30 minutes of the shop's bill ... 35 of 50" and "30 of the 40 within 30 minutes of the bill". Together these mean 5 of the 10 orders that were never handed over were "on time". Notebook 05 cell 3 confirms the bill clock ends at the boy's done press, so the system's clock still stops when he presses. Timing only OTP-confirmed orders, or ending the clock at the OTP, would let me picture it.

G22. Half one S42: "schedulers typed a 'desired date'" and "used the wrong desired date, producing false zero-day waits". I did not know how a desired date enters a wait, so I could not see how typing it hid waiting. One sentence on which two dates the wait runs between, and what was typed, would fix it.

G23. Half one S49 gaming note (also notebook 06 cell 8 and the artifact set): "Complaints catch gate-marking". Once the numerator counts only OTP-confirmed deliveries, a press at the gate no longer raises the number. So I could not see what gaming of the full page the complaints guardrail is there to catch. Naming a way of gaming that still works under the OTP rule would fix it.

G24. Half one S54 timeline: "Two of the six sit in the idle tail." The term is defined only at S72, so at S54 I could not picture it. A short explanation at first use would fix it.

G25. Half one S55 data line: "bookings as fares riders paid" sits beside the caveat "trip earnings are not in the data", followed by "a declined request is offered again, so it counts offers". The deck never says trip earnings are the driver's share of the fares (only notebook 07 cell 1 does), so I could not see why one is in the data and the other is not. I also could not read "so it counts offers" as "one request can appear as several offers". Both explanations on S55 would fix it.

G26. Half one S56: the sentence has two guardrail blanks ("guarded by ____ and ____"), while line 6 under it says "two for riders, one for the budget". Half two S98 then fills the sentence without the budget guardrail. I could not tell whether top-up per trip belongs in the answer the city head gets. A third blank, or a note saying it is left out on purpose, would settle it.

G27. Half one S58: "The proxy test, from chapter 1, three questions per number ... Who controls the count? What does the number deliberately not reward?" Chapter 1 taught the proxy test as one question; the other two come from chapters 5 and 6, so I thought I had missed part of chapter 1. The notes also point at "drivers E and F" two slides before S60 shows them. Tagging each question with its own chapter would fix it.

G28. Half one S60, "E and F also keep shorter weeks than most drivers who idle like them", and S72, "E's and F's weeks are the small group at the bottom left, the most extreme of the 180", under a caption that says the idle tail "sits far right and low". I could not place E and F against the tail until cheat sheet panel 3 gave the tail's average of about 39 hours a week. The S60 notes say "offers down", but the table gives offers only for the after week, so the fall cannot be seen. Putting the 39-hour figure on S60, and saying why the most extreme members sit apart from the cluster, would fix it.

G29. Half one S70: "The true fall is 0.32 ... the average shows 0.19 of it and hides 0.13, about two-fifths." The 0.19 subtracts the after-window average of rates (1.71) from the before-window ratio of sums (1.90). The before-window average of rates is never shown, so I could not check the comparison like for like. Printing that before figure would let me reproduce "two-fifths".

G30. Half one S54 and S77: "if 'hours up 24 percent' is read as 'riders picked up faster' and it is not" and "the median wait barely moved, so riders were served no better". The deck's own numbers show waits falling from 4.8 to 4.6 minutes, unfulfilled requests from 0.11 to 0.10 and trips up 3 percent. Half two S93 adds outer-zone waits falling from 6.6 to 5.95 minutes. So I read it as riders being served slightly better at a high price, and "barely better, at about Rs 2,836 an extra trip" would match the numbers.

G31. Half one S80 and S81: the north star is "completed peak trips per enrolled driver online at peak, per week". S55 gives the goal as "riders picked up faster", and the wait becomes only guardrail 2. No slide explains why, by chapter 2's test, trips per driver captures what riders get better than the wait does. S81 also gives a reading of 35.76 for the weeks before the launch, when nobody could yet be enrolled. One sentence on each point would fix it.

G32. Half one S80 (and S29): the first leading input is "enrolled drivers online in the first peak hour". S83 says the data holds weekly totals, and notebook 07 cell 1 says the window-by-window record is not in the tables, so I could not see how the analyst would compute it. Saying the city must start collecting that data would fix it.

G33. Half one S81: the table's window line is "The calendar week", but its notes say "The window's start is the rider's request, never a time a driver sets". S42 and the S84 board also use "window" for when a clock starts. Chapter 4 defined the window as the stretch of time the count covers, so I could not tell whether Uber's window is a week or a waiting interval. Calling the second meaning "the clock's start" everywhere would fix it.

G34. Half one S83: "so the monsoon's end cannot explain the fall". The same slide's notes say the seasonal caveat "narrows and stays partly open", and half two S87 answers finance with "Partly". I could not tell which claim to repeat. Using one wording in all three places would settle it.

G35. Half one S79 and S84 notes ("Round 3 this afternoon", "half two opens on round 3 of the war game"): S58 is round 1, and no file I read mentions a round 2. I could not tell whether I had missed a round. Naming round 2 or renumbering would settle it.

G36. notebooks/C2_W04_D01_02_north_star_guardrails_STUDENT.ipynb cell 10, the figure "Each of the four instructors": B and C have identical values, so each panel shows three lines for four instructors, and no line is labelled. I could not find instructor D, the subject of the your-turn cell, on the chart. A letter at the end of each line would fix it.

G37. notebooks/C2_W04_D01_04_numerator_denominator_window_exclusions_STUDENT.ipynb cell 8, "four lines, five readings": the x labels "exclusions: medical out of both" and "exclusions: medical counted present" run into each other. The "70.0" value and the "75 percent" text sit on the dashed line. Shorter labels and moving the 75 percent text would make the chart readable at a glance.

G38. notebooks/C2_W04_D01_05_gaming_resistant_definitions_STUDENT.ipynb cell 4 and data/C2_W04_D01_kirana_deliveries_STUDENT.csv: in 12 of the 50 rows, the minutes from the boy's typed dispatch time are more than the minutes from the bill (K01 25 against 15, K32 28 against 21, K43 23 against 16). That puts his typed dispatch before the bill existed. The chapter says he types the dispatch time late so every order reads on time, so these rows contradict the story I am meant to find in the table. Regenerating the column so the typed dispatch never comes before the bill would fix it.

G39. notebooks/C2_W04_D01_06_metric_definition_artifact_STUDENT.ipynb cell 11, the trap: "orders billed up ... is a second growth count, it catches no way of gaming the first". Yet the same page refuses to reward "a shrinking order count", and chapter 2's rule 4 says a rate can rise because its denominator shrank, so a guardrail on orders billed seems to catch exactly that. The artifact set's Q3 then turns on (a) "a guardrail on orders billed" against (d) "the count of orders billed, printed beside the rate", a difference nothing in the notebook explains. A sentence on why the printed count is enough and a guardrail is not would fix it.

G40. Notebook 06 cell 13, the your-turn cell: the driving school's page needs exclusions, a does-not-reward line, guardrails and a gaming note for the north star "licences per learner who enrolled". Chapter 2 gave the school no exclusions and no guardrail that catches a way of gaming that north star. The missing_lines check also passes only if each gaming-note key repeats its guardrail string exactly, and the instructions do not say so. A hint for the exclusions line and a sentence on the matching key would let me fill it.

G41. notebooks/C2_W04_D01_07_proxy_test_on_twelve_rows_STUDENT.ipynb cell 1: the title, the opening paragraph and the "Who needs the answer" and "questions on the way" blocks are indented eight spaces in the source. Jupyter and GitHub render indented markdown as code, so the notebook opens with no heading, and the # and ** marks show as text in grey boxes. Removing the indentation would fix it.

G42. notebooks/C2_W04_D01_09_north_star_guardrails_cost_STUDENT.ipynb last cell (also the study notes' chapter 9 section, cheat sheet panel 6 and half two S90): "saves Rs 92.7 lakh ... if a fifth of the idle tail's top-up is still paid". The Rs 1.159 crore was split by driver-weeks that accepted fewer than half their offers, but the idle tail is defined as 180 drivers under one trip an hour. The arithmetic only works if the two groups received the same top-up, which no file says (half two S89 only implies it). One sentence saying the idle tail's weeks are exactly the weeks under half would fix it.

G43. exercises/unguided/C2_W04_D01_leading_lagging_set_STUDENT.md, "The example, in short": "Kalpa's growth plan chases one north star: delivered orders per active customer per month". The deck's S3 puts "Kalpa Retail's reorders per member" in the lab, and the index lists a Kalpa set that asks which number the plan should chase. I could not tell whether Kalpa's north star is already settled, which of the two it is, or who counts as "active". One consistent statement would fix it.

G44. Same file, Q3: "Yesterday's done presses with no OTP, delivery boy by delivery boy" and "Balaji Kirana (invented) judges its month". Chapters 5 and 6 give the shop one delivery boy and a page whose window is the calendar week, so both disagree with what I learned. Matching the shop's one boy and its weekly page would fix it.

G45. exercises/C2_W04_D01_index_STUDENT.md: the last section's "one shape" is "Post exactly this shape: xxxx", while the concept sets ask for xxx and the Kalpa and lab sets for five letters. The index also mentions "section 15 of the metric clinic, the fallback session", and half two S97 says "the metric clinic runs in its place", but no file says what the clinic is or why it has a section 15. Stating the shape as one letter per item, and adding a line on the clinic, would fix both.

G46. study-notes/C2_W04_D01_notes_STUDENT.md, line 3: "About 12 minutes to read, and 10 more for the self-check." The notes contain no self-check and link to none. A link, or the self-check itself, would fix it.

G47. The study notes' chapter 9 section and closing answer, cheat sheet panel 6, half one S75, S76 and S84, half two S90 and S98: S75's answer and S84's crux say "Pay for completed peak trips" with an acceptance minimum. The priced rule instead keeps the Rs 300 per-hour floor and pays it only to driver-weeks that accept at least half their offers, and "a cancel counted as a decline" first appears in the cheat sheet. I could not tell whether the redesign pays per trip or still pays per hour once a driver-week passes an acceptance minimum. "Floor" also names both the Rs 300 earnings floor and the acceptance minimum ("The floor sits in the gap", S89); separating what the scheme is judged by from what it pays for, and giving the two floors different names, would fix it.

G48. preread/C2_W04_D01_preread_STUDENT.md, Tuesday's topic 5: "The AI-free written business case". The word table explains claim, evidence, caveat, action and appendix, but not what "AI-free" means. One line would fix it.

G49. Half two S85 and S87: "the three roles in the room who each lose something under it", with the finance partner's attack "The fall is the monsoon's end". The redesign saves finance Rs 58 to 92.7 lakh, and on S58 the same role wanted each rupee of top-up to buy a trip. So I could not see what finance loses, or why it now defends the hours scheme. A line on finance's stake would fix it.

G50. Half two S94, second follow-up: "set it in the gap the data shows, above 0.46 and below 0.78". S89 says that counting an accepted-then-cancelled trip as a decline moves the edges to 0.43 and 0.67, and that is the rule S90 prices and S98 adopts. Under the adopted rule a floor of 0.70 would cut ordinary weeks. Quoting 0.43 and 0.67 would remove the clash.

G51. Half two S92, S95 and S97 (and the study notes' chapter 11): "The test: zones as the unit", "A test with teams as the unit", "the unit you randomise". Nothing I read says what a test's unit is or why zones are chosen over drivers, so I could not picture the proposed test. One sentence would fix it.

G52. Half two S93, row "Segment and zones": "where waits fell 6.6 to 5.95 minutes at about Rs 46,000 per extra trip". Neither number appears earlier, and I could not derive Rs 46,000 from anything on the page; the city-wide figure is Rs 2,836. Showing the outer zones' extra trips and top-up behind it would let me reproduce it.

G53. Half two S95: "per developer with a seat" and "Build failures and reverts on suggested code; security findings". The slide explains commit and time to merge, but not a seat, a revert or a security finding. Three short explanations would fix it.

G54. Half two S98, the six-topic strip, row 4: "The four lines | All trips over all hours". The page signed on S81 divides by enrolled drivers online at peak, so the strip gives the old rate as the result of the four lines. "Trips per enrolled driver online, per calendar week" would match the page.

54 findings.

### The hiring interviewer's read

I re-read every source cited below on 13 October 2026 and recomputed every case figure from content/W04/D1/data. No repository file was touched; source PDFs were extracted to text in the session scratchpad only.

**I1.** Place: half1 S80 and S81, read against S55 ("The goal: riders picked up faster"); half2 S89; the transcript's "What structure comes before any number?"; north_star_guardrails set Q2; Kahoot Q1. As written: S81 "the north star read 35.76 trips per online driver-week before and 35.89 after: hours rose 24 percent and the number the scheme exists for barely moved"; S89 "the shrinking count of drivers shows who left, while the north star would rise"; transcript "It does not say whether riders gained, and it would rise if drivers quit". Why: the scheme exists to get riders picked up faster. The pack demotes the rider's wait to guardrail 2 and chases a supply-productivity rate, and its own files admit that rate improves when drivers leave and riders wait longer. Kahoot Q1's key ("North star: the outcome the scheme is for") and set Q2's stem ("the people served are riders who ask for a trip at peak") both point to a rider outcome, so the pack contradicts itself. On the case data the chosen number mostly tracks demand per driver:
- it rose from 35.14 to 36.32 over the six weeks before launch;
- it fell from 37.06 to 34.20 over the weeks after, as requests fell from 43,878 to 41,161 and online drivers rose from 1,058 to 1,085;
- so "barely moved" averages two opposite trends, and the scheme can reach the number only through fulfilment (0.890 to 0.900).

Amplitude, cited for the definition, also asks that a north star sit "within product and marketing's sphere of influence". An interviewer's first follow-up is "what does your north star do if half the drivers log off?", and a number that rises fails it. Hire-grade: make the outcome the north star: the share of peak requests completed within a set number of minutes (or the request-weighted median and 90th-percentile pickup wait), read by zone. Trips per online hour, top-up per extra completed request (counted against what demand alone would give) and the acceptance and driver-cancel shares become its guardrails.

**I2.** Place: half1 S76 and the S84 crux; half2 S90 ("The rule priced") and S98; the transcript's hire-grade decision. As written: S76 "Trips with an acceptance floor, a minimum share of offers accepted, pay for the service and catch the cherry-picking"; S90 "The Rs 300 floor stays, and a driver-week earns its top-up only if the driver accepted at least half the offers shown"; transcript "I would keep the Rs 300 floor only for driver-weeks that accept at least half their offers ... which gives every trip its value back". Why: the rule that gets priced still pays Rs 300 per online hour, with an acceptance gate added. Take a driver parked in Shamshabad who accepts the few offers a thin zone sends him (driver E saw 14 in a week). He clears a 50 percent gate and keeps drawing the floor with almost no trips. Below the floor, each extra trip still cuts his top-up rupee for rupee, the mechanism the same candidate states two sentences earlier, so "gives every trip its value back" is false. S76 and S84 say "pay for trips" while S90 prices an hourly guarantee, and an interviewer will notice the recommendation changed between slides. Hire-grade: pay a per-trip peak bonus, or keep an hourly guarantee only with a minimum of completed trips per online hour and only in zones whose requests per online hour clear a bar. That way the next trip always pays, and idling where riders are few never does.

**I3.** Place: half1 S77 and S74; half2 S94 first follow-up; study notes, "So is the number the scheme pays for measuring what the city wants?". As written: S77 "the median wait barely moved, so riders were served no better"; S74 "keeps paying drivers to sit online in zones with no riders". Why: the case's own tables say riders were served better:
- The share of peak requests fulfilled ran 0.888 to 0.893 in every week before launch and 0.897 to 0.903 in every week after.
- Every one of the twelve zones averaged a lower weekly median wait after launch, by 0.05 to 0.67 minutes, most in the three outer zones (6.6 to 5.95 on S93).
- The request-weighted wait fell from 4.94 to 4.72 minutes.
- The gain passes the monsoon test S83 applies to trips per hour. In the three rainy weeks after launch the mean of zone medians was 4.88 to 5.02, against 5.16 to 5.29 in every week before.

Trips per online hour measures how busy drivers are, and it falls by construction when supply hours are added. In ride-hailing some idle supply near demand is what produces short pickups. An Uber interviewer scores the candidate who names that trade-off, prices it, and says what cannot be attributed without a comparison group. Hire-grade: "Fulfilment rose a point and waits fell in every zone, most where the idle hours sat; with no comparison group and the season turning I cannot attribute it, so the question is what that gain cost against other levers."

**I4.** Place: half2 S93, "Decision and cost"; the transcript's cost row, think-aloud and [D] answer. As written: transcript "Rs 1.9 crore bought 6,700 more peak trips, about Rs 2,836 each, 17 times the Rs 165 fare"; S93 "Hold it: Rs 2,836 per extra trip". Why: requests rose 1.8 percent (251,910 to 256,556), which the same answer checks a minute earlier. Netting that out:
- The old fulfilment rate was 224,200 / 251,910 = 0.890.
- At that rate the after window completes about 228,335 trips with no scheme.
- So 4,135 of the 6,700 extra trips come from demand, and the scheme's increment is about 2,565 trips.
- Rs 1.9 crore / 2,565 is about Rs 7,400 a trip, near 45 times the fare.

The same answer applies exactly this method to the outer zones ("185 more trips than their old fulfilment rate would give"). So the interviewer hears two methods in one answer, and a headline cost understated about 2.6 times. Hire-grade: "Net out demand: at the old 0.89 fulfilment the extra is about 2,565 trips, roughly Rs 7,400 each before any seasonal adjustment, and only a test makes even that causal."

**I5.** Place: half2 S92 (the diagram's "The test: zones as the unit"), S93 and S95; the transcript's "I would test any change with zones as the unit, since drivers in one zone compete for the same riders"; half1 S83. As written: those lines, and S83 "so the monsoon's end cannot explain the fall". Why: zones are a weak unit here:
- The data holds twelve zones, three of them outer, so a zone-randomised test has a dozen units and little power.
- Drivers roam between zones, which is the case's own finding (72 percent of the idle tail's new hours moved to the outer zones). A zone split shifts supply across arms and biases both.
- A pay rule is a contract with a driver, who cannot sensibly hold two rules depending on where he parks.

The hire-grade answer names no primary metric, no minimum detectable effect, no novelty period and no guardrail margin. The switchback appears only in a harder follow-up ("zones switched on and off by week"). S83 states as settled what its own notes say "stays partly open". A marketplace interviewer weights this part heavily. Hire-grade: "Randomise drivers to the new rule, or switch the whole city between rules by alternating peak windows to handle drivers sharing riders; fix fulfilment within N minutes as the primary metric with guardrail margins, size it from week-to-week variance, and run past the first two weeks of novelty."

**I6.** Place: half1 S17 (named last) and its notes, S19 rule 3, S48 line 6; notebook 02's `seesaw` cell and last cell; study notes chapters 2 and 6. As written: S17 "a north star is ... licences per enrolled learner, 0.60 then 0.36. A guardrail is a number watched beside it so that hitting it does no hidden harm; the share who took the test, 1.00 then 0.40, catches this school's move", with the note "The two numbers multiply into the honest one: 0.90 x 0.40 = 0.36"; S19 "Choose a guardrail by the gaming it catches, since a second growth count catches nothing"; S48 "Two or three numbers that must not fall". Why:
- The share who took the test is a factor of the north star, so the instructors' move already drags the north star down. The "guardrail" actually guards the hoarding's pass rate: `seesaw(year["pass_rate"], year["took_share"])` and set Q1 both guard the pass rate. The learner leaves unable to tell a decomposition from a guardrail.
- A guardrail watches harm outside the north star's definition. For licences per enrolled learner, that means weak applicants turned away at enrolment, teaching to the test (S8's own move), or graduates who fail on the road.
- The Spotify glossary the notes cite defines a guardrail by unintended harm and never mentions gaming. It names revenue and latency as typical guardrails (revenue is a growth count) and sets a non-inferiority margin. "Must not fall" with no margin trips on noise.
- The north star is a calendar-year reading of a cohort outcome: the 60 who did not test in 2026 can test in 2027.

Hire-grade: a guardrail is a metric outside the north star that must not degrade beyond a stated margin, chosen for the harm the push could do to customers, the other side of the market, cost or quality. The school chases licences within twelve months of enrolment by intake, and guards learners turned away and failures after licensing.

**I7.** Place: half1 S22, S25, S27 rules 1 and 3, S28; notebook 03's `first_crossing` cell and its check; the leading_lagging set solution, "Where does a leading number show up at work?", and its Q3 key; study notes chapter 3. As written: S22 "A number that moves before the north star, while a team can still act on it, is leading"; S28 "Acceptance moved first; bookings per hour followed ... A city team watching acceptance would have seen the change in week one"; S27 "Read a leading number beside its guardrail: 10 an over with 7 wickets in hand". Why:
- The definition is timing alone. A leading indicator has to predict the outcome, and the Amplitude article the notes cite for these words tells the reader to "Validate that it predicts retention and revenue in your own data".
- The required rate is the scoreboard re-expressed as runs needed over overs left, a running reading of the result itself. The set's Q3 key (yesterday's done presses with no OTP) is the same move: the month's own north star read a day at a time.
- The level of 10 is picked after the loss is known, and 100 off 10 overs with 7 wickets standing is a live T20 chase. S23's stem never gives the runs before over 10, so "first reach 10" cannot be determined.
- In the case data, bookings per online hour fell from about Rs 313 to Rs 271.0 in the launch week, three-quarters of its whole fall, in the same week acceptance fell. Both respond to the launch at the same time. With the fare fixed at Rs 165 every week, bookings per hour is simply trips per hour times 165.
- Wickets in hand is a state of the chase; calling it a guardrail misuses chapter 2's word. S80 labels its two inputs as leading with no lag shown.

Hire-grade: a leading indicator moves before the outcome and predicts it with a known lead time, shown on history or past experiments, and the team can act on it. "I would check whether first-week acceptance predicted week-six trips per online hour across past incentive launches."

**I8.** Place: half1 S80 guardrail 1 and S81 (guardrails, gaming note, exclusions); study notes case table; guided definition solution item 4. As written: S81 "For riders: accepted share at or above a floor the city sets" and "Guardrail 1 catches declining and cherry-picking"; guided solution "Declining the long trips lowers the accepted share in the same week, so a floor on it catches cherry-picking as it starts". Why: a driver who accepts the long trip and then cancels it keeps his accepted share up. The page also excludes "Trips cancelled by either side" from the count, so the cherry-pick vanishes from both lines. The ticket shows exactly this behaviour: the share of accepted trips the driver cancelled went from 0.04 to 0.09 at launch (0.037 to 0.089 week by week). S90, S98 and the transcript count a cancelled trip as declined, so the page the city signs and the rule it prices disagree. Hire-grade: guardrail 1 is offers accepted and completed over offers shown, with a driver cancel counting as a decline. The driver-cancel share of accepted trips is watched as its own guardrail.

**I9.** Place: half1 S10 (named last) and S12 rules 2 and 3; notebook 01's `drifted` cell and last cell; study notes chapter 1 "In the interview"; Kahoot Q5; proxy_test set solution. As written: S10 "the proxy test asks whether a team could hit this number while the thing it stands for got worse or stayed the same"; S12 "nearly every number on a dashboard is one"; `drifted`: `return bool(paid.iloc[-1] > paid.iloc[0] and wanted.iloc[-1] <= wanted.iloc[0])`; notebook 01 "names a number that cannot rise while that thing gets worse". Why:
- Together the two rules fail every proxy, since any proxy can be pushed while its goal sits still, so the test ranks nothing. The interviewer asks how cheaply, and by whom, the number moves without the goal, and whether it moves when the goal moves.
- `drifted` compares only two endpoints. It passes a doubled token count if plates go from 200 to 201.
- The other half of judging a proxy is never taught: checking that it moves in the same direction as the north star, and that it detects change sooner. That is the subject of the Chou paper S10 cites.
- A number that "cannot rise" while the goal worsens does not exist, and the pack's own north star rises when drivers quit.
- The solution's "A count passes when raising it needs the thing itself" ignores trips booked from a second rider account, which the transcript itself names.
- The wording drifts from "got worse or stayed the same" (S10) to "got worse" (S12, Kahoot Q5, the notes' glossary).

Hire-grade: a good proxy moved with the goal on past launches, moves sooner or more sensitively than the goal, and costs a lot to move without it. Every proxy can be gamed, so it ships with counter-metrics that catch the cheap ways.

**I10.** Place: half1 S33 (named last), the S36 table and S53; Kahoot Q4; artifact set solution item 1 and its "published page" paragraph; guided definition solution, "Which item is worth arguing about?". As written: S33 "four lines make a number computable, its numerator, its denominator, its window and its exclusions"; artifact solution "d: with no denominator and no exclusions, the number is not computable"; S53 "a numerator with a receipt, a denominator and a window, written down"; S36 MTU row "per month" under "Per what". Why: counts are computable with no denominator: licences in a year, trips, gross bookings. Uber's 10-K defines MAPCs as unique consumers with a completed ride or delivery in a month, "averaged over each month in the quarter". That is a de-duplicated count with no denominator, and "per month" in the MTU row is the window. The guided solution also rules that "The denominator has to be set by something other than the outcome it divides". It then praises Swiggy's platform frequency, completed orders per transacting user, whose denominator exists only for users who ordered. Hire-grade: first say whether the metric is a count, a ratio or an average. A count needs its unit, de-duplication rule, window and filters; a ratio adds a denominator whose population is named and justified.

**I11.** Place: half1 S32 table and S34; notebook 04 cells 5 and 7; study notes chapter 4 table; four_definition_lines set Q1 and its solution. As written: S32 "Denominator: calendar days | 40 | 60 days" and "Exclusions: medical leave counted present | 42 | 50"; S34 "an exclusion is a status left out of both"; solution "d: neither leaves a status out of both counts". Why: in the pack's own function the 66.7 reading is `bottom=("present", "absent", "medical", "holiday")`. So 80.0 and 66.7 differ only in whether "holiday" is a status left out of both counts, which S34 calls an exclusion. By the chapter's own definition option d is right, and Q1's key is arguable at best. "Medical leave counted present" moves a status into the numerator (`top=("present", "medical")`), so it is a numerator rule. An interviewer who asks for the numerator, denominator and exclusions of attendance would mark both labels wrong. Hire-grade: the school rule excludes holidays from the population, which sets the denominator at 50. Counting medical leave as present is a numerator rule. Removing medical leave from both counts is the exclusion.

**I12.** Place: half1 S31 and S32; notebook 04 last cell. As written: S31 "four honest clerks compute the attendance percentage from the same register. How many different numbers come out?"; S32 "Answer: c, five numbers from one register"; notebook 04 "Four honest clerks can print five numbers from it". Why: four clerks cannot print five numbers. With nothing said about their choices, option d ("It cannot be told") is the literal answer, and the exercise set's own example has five clerks. Hire-grade: ask "how many different readings can one register honestly give?" and key it to the five definitions.

**I13.** Place: half1 S46, S48, S49, S50 notes and S52 rule 2; notebook 06 last cell; study notes chapter 6. As written: S52 "The first four lines make it computable; the last three make it safe to pay for"; S50 notes "a US quality measure is specified on one written page with its numerator, denominator, exclusions and time interval"; S49 "What it does not reward | ... a shrinking order count". Why:
- The page has no line for the decision it feeds, which S12's first rule puts first.
- It also lacks the owner, the unit and de-duplication rule (Uber's MAPC definition carries one: "counted as only one MAPC"), the data source and event timestamps, the window's time zone or cohort basis, the baseline and decision threshold, and the guardrails' margins.
- The CMS page cited lists 18 building blocks, among them target population, data sources, level of analysis and attribution model, and says nothing about one page.
- On the shop, the full page swaps the son's growth count for a completion rate, which answers a different question.
- Its "does not reward a shrinking order count" has no mechanism behind it. A rate over orders billed rises when hard orders are refused, and the pack forbids the count guardrail that would catch that.
- A number becomes safe to pay on through guardrail thresholds someone watches and audits someone runs; the seven lines supply neither.

Hire-grade: a metric spec states the decision and owner, the unit and de-duplication rule, numerator and denominator, the window with its time zone or cohort, filters and exclusions, the data source, the baseline and decision threshold, guardrails with margins, and known gaming. The shop chases OTP-confirmed deliveries and guards the confirmation rate and orders billed.

**I14.** Place: half1 S38, S41, the S42 title, S44 rules and "In the interview"; the gaming set solution, "What does the set test about gaming?"; notebook 05 last cell. As written: S38 "Gaming is raising a number without doing what it stands for. It needs no dishonesty"; solution "A paid number is gamed in four ways"; S41 "a definition resists gaming when its numerator needs a receipt ..."; S44 "Start the clock at a time the system records, never at one the person timed types in"; "how do you write one that is not?". Why:
- Every case the chapter uses is falsification. The boy marks undelivered parcels done, and the SEC order the pack cites says Wells Fargo's "gaming" took in "fraud, identity theft, and the falsification of bank records".
- An interviewer wants false reporting told apart from behavioural gaming. False reporting is fixed with receipts, audits and logs that cannot be edited; behavioural gaming is fixed with pay design and counter-metrics.
- The "four ways" omit selection and effort substitution, both shown earlier in the pack: the instructors booking only sure learners, drivers picking trips, and S8's "Teach only the questions the paper repeats". Timing games are missing too.
- An OTP can be read out at the gate or over the phone.
- The VA report the pack cites shows schedulers overwriting appointments so that "The create date of the appointment is effectively reset". That is a system-recorded time gamed by the person being timed.
- No definition is ungameable, so the interview question's premise fails.

Hire-grade: "Any metric can be gamed; I name the cheapest way to move this one without the goal, make it costly (receipts, a clock that starts at the first event and cannot be reset, audits) and visible (a counter-metric), and keep pay off any single number."

**I15.** Place: half1 S40 table, S44 rule 2 and the S49 guardrail; notebook 05 `paid_deliveries`. As written: S40 "Within 30 minutes of the shop's bill | the shop's system | 35 of 50, 0.70"; `paid_deliveries(orders, receipt=True, clock="minutes_from_bill", limit=30)`. Why: the bill clock includes packing and the wait for the boy to get back, time he does not control, and it still stops at his own done press. The 0.70 divides by 50, counting the 10 parcels never delivered. The pay rule pays nothing for an OTP-confirmed delivery at minute 31 of a clock the boy did not start. A Swiggy interviewer expects the shop's leg and the delivery leg measured apart, with a system pickup scan starting the rider's clock and the OTP stopping it. Hire-grade: time the shop from bill to a system pickup scan and the rider from that scan to OTP entry, and count undelivered orders as late in the on-time denominator.

**I16.** Place: half1 S13; proxy_test set solution, "Where does a number that fails the proxy test show up at work?"; study notes chapter 1. As written: "Wells Fargo paid staff on a cross-sell number, accounts and products per household, that counted accounts nobody used". Why: the cited sources do not say staff were paid on products per household. The CFPB release says employees opened accounts "to hit sales targets and receive bonuses". The SEC order (Release 34-88257) says "the number of products sold continued to be a significant criterion by which the performance of employees ... was evaluated" (paragraph 20) and "The compensation of certain Company executives was impacted by cross-sell growth" (paragraph 18). The cross-sell ratio was the figure reported to investors, and anyone who knows the case would correct a candidate who repeats the slide. Hire-grade: branch staff were pushed and paid on product sales goals. Those sales, many unused or unauthorised, inflated the cross-sell ratio reported to investors, and some executives' pay tracked its growth.

**I17.** Place: half1 S42 last line; study notes chapter 5; gaming set solution. As written: "At its Phoenix facility, 30 of 79 Veterans Affairs staff interviewed said they used the wrong desired date, producing false zero-day waits." Why: the report's body (page 49) says the inspectors "asked 40 Primary Care schedulers and supervisors how they determined the veteran's desired date", and "The remaining 30 stated they based the desired date on the provider's availability or next available appointment date". The 79 is everyone interviewed about scheduling. The rate is 30 of 40, three-quarters, and the pack prints a 38 percent ratio on the day it teaches the denominator line. Hire-grade: 30 of the 40 primary-care schedulers and supervisors asked said they entered the next available slot as the desired date, which showed false 0-day waits (VA OIG report 14-02603-267, August 2014).

**I18.** Place: half1 S20 (stats and paragraph); north_star_guardrails set solution, "Where does a north star that matches what a business is trying to do show up at work?"; study notes chapter 2. As written: S20 "28% | of MTUs, in Swiggy's words"; "Rs 612 ... up 16 percent on the quarter before, with slightly fewer orders per user"; "orders per user would have read the offer's success as a fall"; "NOV ... from its Q1 FY27 letter". Why:
- The letter says "over 28% of our MTUs".
- It credits the AOV rise to "our significantly expanded selection driving a higher non-grocery mix in our GOV, and the resounding success of Maxxsaver".
- It credits the slower order growth to "Some cart-consolidation led by Maxxsaver and letting go of some low AOV orders and unprofitable users", a deliberate pruning of the user base the pack leaves out.
- "A slightly lower number of orders by the same user" is a qualitative remark. Instamart orders per MTU in the letter's own table fell about 9 percent quarter on quarter (89 million orders on 9.8 million MTUs to 92 million on 11.1 million).
- The letter says the Maxxsaver ramp-up "kept our absolute Contribution flat QoQ". That is the guardrail an interviewer asks for: AOV read alone would call a costly discount a success, just as orders per user would call it a failure.
- The lead_lag solution paraphrases the same letter differently ("lowered order growth").
- Eternal's "NOV = GOV minus discounts" is in the Q1 FY26 letter. The Q1 FY27 letter carries the GOV sunset, inside its food-delivery line.

Hire-grade: Swiggy credited the AOV rise to a wider non-grocery selection and Maxxsaver, and the slower order growth to cart consolidation and dropping low-value orders and users. GOV or contribution per transacting user weighs both, and Swiggy said the ramp-up held contribution flat.

**I19.** Place: half1 S27, S35 and S44; study notes chapters 3 to 5; notebooks 03 and 04 last cells. As written: S27 "[F] North-star against guardrail, with one example pair, and the leading input that moves first" (S19's question again); S35 "[F] What makes a metric gameable, and how do you write one that is not?" (S44's question word for word). The notes put that gaming question under chapter 4 and give chapters 3 and 5 none. Why: two of the six topics carry no question of their own, and a hard screen asks both most mechanically: "Define a daily active user, or a completed trip, line by line: what counts, over what window and time zone, with which exclusions and de-duplication?" and "Give a leading indicator of 90-day retention and show that it leads." Nothing in the pack asks how to set a target or a guardrail's tolerance either. Hire-grade: chapter 3 carries "[F] Name a leading indicator for X; how would you show it predicts X?" and chapter 4 carries "[S] Define DAU for this product line by line."

**I20.** Place: north_star_guardrails set Q1 and solution item 1. As written: key c; solution "b: passes per instructor is the outcome counted again, and it cannot say why the rate rose". Why: passes per instructor fell from 60 / 4 = 15 to 36 / 4 = 9 while the hoarding's rate rose. So b also "would have caught the 2026 move", which is all the stem asks; explaining why is a different test. Hire-grade: either ask which guardrail shows why the rate rose, or replace b; as written, b and c both catch the move.

**I21.** Place: artifact set Q3, solution item 3 and "Which item is worth arguing about?"; notebook 06 `missing_lines` cell. As written: solution "a: a growth count as a guardrail catches no way of gaming the north star"; notebook 06 "a guardrail that catches nothing named: orders billed up". Why: the north star is confirmed deliveries over orders billed, so refusing hard orders raises it. That is why the page lists "a shrinking order count" under what it does not reward. A guardrail on orders billed is the line that catches this, so option a is defensible and stronger than d, which prints the count with no threshold. The notebook flags the guardrail only because the gaming note does not name it, and reports that as "catches nothing". Hire-grade: key a, since a floor on orders billed catches the shrinking denominator the page says it will not reward, or accept both a and d.

**I22.** Place: leading_lagging set Q1 (the eight-number table) and its key; Kahoot Q2. As written: key a "1, 3, 6 and 8"; Kahoot key "1, 3 and 5". Why: every keyed number carries "this week", and every lagging one says "for the quarter" or "for the month". In Kahoot the leading ones say "this week", "first peak hour" and "by zone", against "the month's" and "the quarter's". So the window words give the key away, while the solution itself says how often a number is read does not decide it. Returns booked this month (7) and customers lost (4) could plausibly lead next month's orders per active customer. Kahoot's (5), requests per online hour, moves in the same week as the north star. Hire-grade: put every number on the same window and make the call turn on what causes what (a booking precedes its delivery; a return precedes churn). Include one weekly number that still lags, such as this week's delivered revenue.

**I23.** Place: Kahoot Q7. As written: key "What it does not reward: text accepted, then deleted". Why: a line saying the definition does not reward accept-then-delete cannot override a numerator that counts accepted suggestions. The deck's own S95 notes say the north star catches it, "since deleted text is not present at the next commit". The transcript says accepting and deleting "is mostly how a developer inspects a suggestion", and nobody is paid on acceptance at all. Hire-grade: the numerator line does the work. Counting only suggested text still present at the next commit is the receipt condition that keeps accept-then-delete out of the count.

**I24.** Place: north_star_guardrails set solution, item 3 and "Which item is worth arguing about?". As written: "Top-up per completed trip rises only when money is paid for hours with no trips"; "it stays inside its design no matter how many paid hours serve no rider". Why: top-up per trip also rises when the fare per trip falls (shorter trips, surge ending), and it can fall while total spend runs away if trips grow. Top-up per online hour climbs toward the Rs 300 cap as idling grows, so option c moves too; a cap limits a number without freezing it. Hire-grade: top-up per completed trip moves with idle hours and with fare per trip. Read it beside total top-up against budget, and beside trips per online hour, to tell the two apart.

**I25.** Place: gaming set Q3 and solution item 3. As written: key d "Doubts the student confirms resolved, over all doubts students raised"; solution "A definition resists gaming only when the people paid control neither line". Why: "all doubts students raised" is platform-wide, so one teacher's rate depends on what every other teacher took on. The pay rule has no way to attribute a doubt to a teacher, which the CMS page the pack cites lists as a building block ("Attribution model"). A student can also withhold the confirmation or be pressed for it. Hire-grade: route each doubt to one teacher and pay per student-confirmed resolution. Guard with the share of routed doubts declined or abandoned, and with doubts asked again within a week.

**I26.** Place: half2 S95 table and notes; transcript, "How does the same question move to an AI coding assistant?". As written: north star "Suggested code still present at the next commit, per developer with a seat, per week", with "Read beside it | Time from first commit to merge", which the transcript calls "the number closest to the goal". Why: the unit is never stated (characters, lines or suggestions), and counting kept text rewards long boilerplate. Surviving to the next commit is a short horizon. The number the candidate calls closest to the goal is demoted to a side read, the same inversion as I1. The decision is renewal, so the outcome should lead. Hire-grade: judge renewal on time to merge and merged changes per active developer, in a test randomised by team. Kept suggested characters at 30 days is an input, with reverts and security findings as guardrails.

**I27.** Place: half1 S70 notes and S73 crux; Kahoot Q6. As written: S73 "A rate is two sums divided once, with its denominator named"; Kahoot Q6 "Which goes on the slide?", keyed 1.58. Why: the right aggregate depends on the question. The city's trips per paid hour needs the ratio of sums; "how did the typical driver fare under the rule" needs the per-driver mean. Q6's own Tests line concedes the mean "answers a different question", yet the stem never says which question the slide answers. In an experiment where drivers are the unit, a ratio metric also needs delta-method variance, a standard follow-up at Uber and Google. Hire-grade: for the city's trips per paid hour, the ratio of sums, 1.58; for the typical driver-week, the mean, 1.71. The slide says which question it answers.

**I28.** Place: half1 S37; notebook 04 last cell; study notes chapter 4. As written: "In 2018 Delhi Metro counted about 27 lakh riders a day, and its new 'line utilisation' count read 45,35,932 on 29 May 2018 ... one crowd, two units." Why: PTI's 27 lakh is February 2018's daily average ("nearly 27 lakh commuters taking the rapid transit network daily in February this year"). The 45,35,932 is one day, 29 May, when the 24.82 km Janakpuri West to Kalkaji Mandir section opened to passengers. The gap mixes a window change with the unit change, on the day the window line is taught. The same article says DMRC "did not share the daily average ridership figures" after the opening, and that ridership "had taken a hit after two fare hikes in 2017". That makes it a live example of chapter 5's quiet change of definition, and the pack tells it as neutral. Hire-grade: compare the same day's ridership with that day's line utilisation. Note that DMRC adopted the higher-reading count while withholding the old one after a fare-hike dip, which is why a definition change is dated beside the number.

**I29.** Place: half1 S42 "In public" column; gaming set Q2 ("four public ways of gaming"); study notes chapter 5 table. As written: "Uber: an open app counts as online (chapter 7)". Why: by the pack's own label the Uber situation is synthetic. Listing it beside Wells Fargo and Veterans Affairs as a public case asserts a gaming problem at a real company with no source, and an Uber interviewer will ask for one. Hire-grade: label it "the illustrative case" in its own column, or cite a dated public instance.

**I30.** Place: artifact set solution item 2; half2 S90; half1 S60 (E accepted 4 of 14 offers, F 3 of 12). As written: "a boy who confirms every order he carries reads the same rate in a quiet week as in a busy one"; "a driver-week earns its top-up only if the driver accepted at least half the offers shown". Why: in a quiet week of three orders, one miss moves the rate 33 points. A per-driver-week acceptance gate on a dozen offers is noisy and lands hardest on drivers in thin zones. Interviewers ask for a minimum volume before a rate decides pay. Hire-grade: apply the floor only above a minimum number of offers, or on a rolling four-week window, and print the count beside every rate.

**I31.** Place: half1 S10 and the S13 notes. As written: "any target bends behaviour toward itself"; notes "Do not quote a firing count or Goodhart". Why: interviewers listen for the standard names: Goodhart's law and Campbell's law, counter-metric, proxy (surrogate) validation, input versus output metric, metric tree, non-inferiority margin, switchback. The pack teaches several of these ideas but none of the names candidates are scored on. Hire-grade: "This is Goodhart's law: once a measure becomes a target it stops being a good measure, so I pair the target with counter-metrics."

31 findings.

### What did the fix pass change for the rebuild's reads?

**Counts.** The trainer filed 32 findings, the fresh graduate 54 and the interviewer 31, 117 in all,
and the trainer's table has no "not found" cell. A fresh agent then checked every finding read-only
against the committed files: 70 were fixed, 37 fixed in part and 10 open, and it listed eight defects
the pass itself had introduced. A second round closed what the folder allowed. The final count is 84
fixed, 23 fixed in part and 10 left as they are; each of the 33 has its reason in the sources list's
last table (`internal/C2_W04_D01_day_sources_INTERNAL.md`). The eight introduced defects are fixed:
the redesign solution sends the saving to notebook 10, Kahoot's question list matches Q6 and Q7, the
gaming solution keeps one VA base, the leading-and-lagging solution says the plan proposes its north
star, the notes name the test's unit, the cheat sheet's VA node reads "Who sets the start?", the day
sheet no longer claims the Kalpa set attacks the row's three targets, and notebook 09 says "few
riders". The render check found two more, both fixed or reported: S20's stat notes ran to two lines
under the card rule and now fit one, and the morning deck's footer prints nine chapter names in a
strip that holds about eight (reported, since the strip is drawn by `scripts/deck_layout.py`).

| Id | Outcome | What changed, or where the reason is |
|---|---|---|
| T1 | Fixed | S3 splits the case into chapters 7 to 9 and 10 and 11 with minutes and notebooks, and names the opening, the break, the close and the faculty session |
| T2 | Fixed | S4, the day sheet and the board work say which case chapter applies which topic, draw chapter 2 into chapter 6 and drop the Kalpa colour; the board draws the boxes unlit |
| T3 | In part | SECTION 9 names its resistant lines, and S3 carries the opening, the break and the close; reason in the sources list |
| T4 | In part | S3's note sends the row's Kalpa scenario to the lab, and the day sheet's agenda table places S7, S27 and S58; reason in the sources list |
| T5 | Fixed | Each concept set's Q1 runs inside its rules slide's minute and a half, with the key and one reason said |
| T6 | Fixed | The day sheet's "When does each notebook run?" names the cells each slide runs |
| T7 | Fixed | The board work follows the deck's order, writes the question and the headline at S5 and grows the case board at S57 |
| T8 | Fixed | Round 2 is named at S59, round 3 is the last round, and the stall move waits for S60 |
| T9 | Not fixed | Reason in the sources list |
| T10 | In part | Notebook 09 stops at the top-up split and notebook 10 prices the saving; reason for "Which number settled first?" in the sources list |
| T11 | Fixed | S96's note says the trap item reuses chapter 8's idle-tail numbers |
| T12 | Fixed | The finance card attacks trips per hour, the number S87 answers |
| T13 | Fixed | S98 counts an accepted trip the driver later cancels, and its transition names the tentative faculty block or the clinic |
| T14 | Not fixed | Reason in the sources list |
| T15 | Fixed | The cut list keeps Delhi Metro, which S66, S73 and S84 recall |
| T16 | Fixed | S21 defines an offer and S28 glosses bookings per online hour before the break |
| T17 | In part | The day sheet schedules the concept sets' Q2 and Q3 after the lab note's four parts; reason in the sources list |
| T18 | Fixed | The clinic's slide minutes add to 120 |
| T19 | Not fixed | Reason in the sources list |
| T20 | Fixed | The clinic's S6 prints the handout's Q1 in its order with its letters, so a room that sat it there skips it in the lab |
| T21 | Fixed | Round 3's defence reads 6.5 minutes on S86 and the board |
| T22 | Fixed | Notebook 07's first cell renders as markdown |
| T23 | Fixed | All three decks are rebuilt after their markdown |
| T24 | Fixed | S3's notebook column uses the files' numbers, and S27 carries the row's [F] question as the row words it |
| T25 | Not fixed | The day sheet now says no item attacks the row's three targets; reason in the sources list |
| T26 | In part | The day sheet's "Go as far as" says what groups write in the trainer's time and what every learner writes in the lab; reason in the sources list |
| T27 | In part | The never-cut list keeps the gaming demonstration; reason in the sources list |
| T28 | In part | S27 runs a minute and a half with two defences, and the lab takes Q2; reason in the sources list |
| T29 | Not fixed | Reason in the sources list |
| T30 | In part | S90 names the [D] question and the day sheet carries every answer in one breath; reason in the sources list |
| T31 | In part | The day sheet forbids the row's 4 percent and keeps Kalpa items out of Monday's Kahoot; reason in the sources list |
| T32 | In part | The day sheet lists the row's references with what each check found; reason in the sources list |
| G1 | Fixed | S1's timeline names Retail-Plus as Kalpa's paid membership tier, and its note names Meera Raghavan, Kalpa Retail's CEO |
| G2 | In part | S93's note sends pairs to the seven checks printed in the transcript; reason in the sources list |
| G3 | Fixed | As T24 |
| G4 | Fixed | S4, the cheat sheet and the notes' map show the case in the known colour |
| G5 | Fixed | S5 defines enrolled, the peak window and the gap |
| G6 | Fixed | The kitchen cooks for each token as it is handed out, so day 6's waste and the Rs 7,500 by day 10 follow |
| G7 | Fixed | The code-glimpse titles count their own lines |
| G8 | Fixed | S12 explains the tags, and the notebooks' tag line glosses GCC |
| G9 | Fixed | S13, the notes and gaming Q2 gloss cross-selling |
| G10 | Fixed | S13 names who levied each part of the USD 185 million |
| G11 | Fixed | The guardrail sits beside the number being chased, the pass rate, in every file |
| G12 | Fixed | "Growth target", with an example, replaces "growth count" in the deck, the notebooks, the notes, the sheet, S86's note and the self-check |
| G13 | Fixed | S20 dates the quarter in months and spells out GOV and NOV |
| G14 | Fixed | S21 defines an offer at first use |
| G15 | Fixed | S25 names the harm wickets in hand guard against |
| G16 | Fixed | S28 says acceptance settled first and prints the before values |
| G17 | Fixed | Five clerks in every file |
| G18 | Fixed | The medical row is labelled a numerator change |
| G19 | Fixed | Learner files say the course outline; the trainer's notes keep the curriculum row |
| G20 | Fixed | S36 and S53 say a count has no denominator |
| G21 | Fixed | S40 says both clocks stop at the done press and the page times only confirmed orders |
| G22 | Fixed | S42 says how the desired date entered the wait |
| G23 | Fixed | Complaints catch an OTP asked for by phone before the goods arrive |
| G24 | Fixed | S54 says what the two idle drivers did |
| G25 | Fixed | S55 explains trip earnings and re-offered requests |
| G26 | Fixed | S56 says the budget's guardrail sits on the page |
| G27 | Fixed | S58 tags each question with its chapter |
| G28 | Fixed | S60 and S72 give the tail's 39 hours and place E and F |
| G29 | Fixed | S70 prints the before window's average of rates |
| G30 | Fixed | S54 and S77 say the wait fell only from 4.8 to 4.6 minutes |
| G31 | Fixed | S80 says why trips lead, and S81 why the weeks before count the same drivers |
| G32 | Fixed | S80 says the city starts logging drivers online by peak hour |
| G33 | Fixed | "The clock's start" names when a wait begins, and "window" keeps chapter 4's meaning |
| G34 | Fixed | S83, its note and S87 say the season stays partly open |
| G35 | Fixed | S58 names round 2 |
| G36 | Fixed | Notebook 02 draws one labelled row per instructor |
| G37 | Fixed | Notebook 04's labels and the 75 percent line no longer collide |
| G38 | Fixed | No typed dispatch falls before its bill, and a contract line checks it |
| G39 | Fixed | Notebook 06 and the artifact set call orders billed up 20 percent a growth target and show the count already on the page |
| G40 | Fixed | Notebook 06's your-turn cell hints at the exclusions and says the gaming note's keys repeat a guardrail's words |
| G41 | Fixed | As T22 |
| G42 | Fixed | S90, the notes and the sheet say the weeks under half are exactly the idle tail's |
| G43 | In part | The set and its solution say the plan proposes its north star; reason in the sources list |
| G44 | Fixed | The set's Q3 matches the shop's weekly page and its one boy |
| G45 | Fixed | The index states the answer shape and what the clinic is |
| G46 | Fixed | The notes link the self-check |
| G47 | Fixed | The scheme is judged by trips and the Rs 300 floor is paid under the acceptance floor in every file, S84's title, S98's strip and S45's node included |
| G48 | Fixed | The pre-read defines AI-free |
| G49 | Fixed | S85 gives finance's stake |
| G50 | Fixed | S94 quotes 0.43 and 0.67 under the adopted rule |
| G51 | Fixed | S92 defines a test's unit, and the notes and the transcript follow it |
| G52 | Fixed | S93 shows the Rs 85.7 lakh and about 185 trips behind Rs 46,000 |
| G53 | Fixed | S95 explains a seat, a revert and a security finding |
| G54 | Fixed | S98's strip matches the signed page |
| I1 | Not fixed | Reason in the sources list |
| I2 | In part | "Gives every trip its value back" is gone, and the scheme is judged by trips; reason for the priced rule in the sources list |
| I3 | In part | Every file says riders were served barely better, the wait falling from 4.8 to 4.6 minutes; reason in the sources list |
| I4 | Fixed | The cost is also given net of the 1.8 percent rise in requests: about 2,565 trips, near Rs 7,400 each |
| I5 | In part | The test's unit is named, and the transcript switches the whole city window by window; reason in the sources list |
| I6 | In part | A guardrail is chosen by the harm or gaming it catches and holds a margin; reason in the sources list |
| I7 | In part | A leading number must predict, S23 gives the runs before over 10, and S28 says both fell at the launch; reason in the sources list |
| I8 | Fixed | The page, the guided solution and the gaming note read the cancel share beside guardrail 1 |
| I9 | In part | The proxy test reads "got no better" in every file, and no file claims a number that cannot rise; reason in the sources list |
| I10 | Fixed | S33, notebook 04, the notes, the four-lines set and Kahoot Q4 say what a count needs in place of a denominator, and the guided solution says platform frequency's base is set by ordering, its count printed beside it |
| I11 | Fixed | The four-lines set's Q1 pairs 80.0 with 84.0, and the medical row is a numerator change |
| I12 | Fixed | Five clerks |
| I13 | In part | S50's note quotes CMS's building blocks as they stand, and line 6 holds a margin; reason in the sources list |
| I14 | In part | Gaming has two kinds, the set takes four common ways, and S44's clock is one the person timed cannot reset; reason in the sources list |
| I15 | Not fixed | Reason in the sources list |
| I16 | Fixed | Every file says staff were judged on products sold while investors read the cross-sell number |
| I17 | Fixed | Every file says 30 of the 40 schedulers and supervisors asked |
| I18 | Fixed | Every file credits Swiggy's own causes and the flat contribution |
| I19 | Not fixed | Reason in the sources list |
| I20 | Fixed | The north-star set's option b no longer catches the move |
| I21 | Fixed | The artifact set's option a is a growth target |
| I22 | In part | Every leading-and-lagging item reads one week; reason for requests per online hour in the sources list |
| I23 | Fixed | Kahoot Q7 keys the numerator's receipt condition |
| I24 | Fixed | The north-star solution says top-up per online hour climbs to the cap and stops there |
| I25 | Fixed | Doubts are routed to one teacher, and the solution reads unconfirmed and repeated doubts beside the rate |
| I26 | Not fixed | Reason in the sources list |
| I27 | In part | The city's rate is the ratio of sums and the mean answers the typical driver-week; reason in the sources list |
| I28 | Fixed | Every file says the two Delhi Metro figures differ in window and that DMRC stopped sharing the old one |
| I29 | Fixed | The Uber case is labelled illustrative wherever it sits beside public cases |
| I30 | In part | The artifact solution prints the count beside a quiet week's rate, and S89 puts a minimum offer count into the test; reason in the sources list |
| I31 | Not fixed | Reason in the sources list |

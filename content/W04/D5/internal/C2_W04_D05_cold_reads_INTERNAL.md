# W04 D5 cold reads: what a fresh graduate and a hiring interviewer could not accept

**INTERNAL.** Two cold reads of the Friday pack, each by a separate agent on the Opus model, each
given the pack frozen at commit 65d645b and told to write findings only and never edit. The first
read as a 23-year-old fresh graduate who has never worked and has weak maths, every STUDENT file in
learner order. The second read as a hiring interviewer from Uber, Swiggy, Google and an AI startup,
the interview material and its scorecard. Both reports are kept below as they were returned, with a
third read by a fresh interviewer agent after the fix pass, frozen at commit 478a643. What the fixes
changed for each finding is in the last section; a finding left as it is has its one-line reason in
`internal/C2_W04_D05_sources_INTERNAL.md`.

---

## Read 1: what stopped a weak learner in Week 4 Friday's learner files?

I read every STUDENT file in the order given, as a 23-year-old fresh graduate with weak maths and a little pandas. That covered both day decks and the fallback deck, the four notebooks' cells and printed outputs, the nine exercise and solution files and the index, the transcripts, the Kahoot answer sheet, the take-home brief and self-check, the study notes, the cheat sheet, the Saturday preview, and every picture these pages point at. I skimmed the speaker notes and mention them only where a slide depends on them.

In the Kalpa lab I ran the two "your turn" cells the notebook asks me to type, saving nothing. I also opened the calendar data file once to see when the sale opens, though no page asked me to. I edited nothing.

Each finding gives its number, the file and place, the kind, what stopped me, and how badly.

### Which places in the morning deck (half one) stopped me?

**1. half1 title and S1 ("festive forecasts 18 points apart"); notebooks 01 to 03 cell 1 ("eighteen points apart"); preview table.** Kind: word. How badly: minor. No page says "points" means percentage points; I only understood it after subtracting 4 from 22.

**2. half1 "Who" line and S4 ("the FC planner"); S1 and S33 speaker notes.** Kind: word. How badly: minor. "FC" is never expanded on screen. "Packer-shift" is defined only in the speaker notes, so on the slides I had to guess both.

**3. half1 S1, row "The two forecasts" ("promises the window 22 percent above last year's; finance's rule is last year's window plus 4 percent").** Kind: word. How badly: slows. "Window" is not defined. Which weeks of last year it means is only settled at S31 and in notebook 03 cell 7, and the whole vendor-against-finance argument turns on it.

**4. half1 S1, row "The data" ("kind: fitted, holdout or forecast"); S16 caption "104 weeks with the hold-out shaded"; S16 "test set"; notebook 02 cell 2 output "training weeks: 91".** Kind: word. How badly: slows. These four terms arrive before any sentence explains them. "Fit" is defined only inside S20's vote option c ("A fit is drawn through weeks it has seen"), which is that vote's right answer.

**5. half1 S1, row "The data" (`calendar` with diwali_week and sale_week; `costs`).** Kind: instruction. How badly: minor. No notebook or exercise opens these two tables, because the Diwali dates and the costs are typed into the code. The sale weeks the ticket says I hold appear on no page.

**6. half1 S1 ("the three weeks before it run at 1.5, 1.9 and 1.7 times an ordinary week, its own week at 1.4"); S18 option d; S19 picture; S28 option a.** Kind: step. How badly: minor. S1 already puts the peak two weeks before Diwali, so the S5 vote is answered before it is asked. Likewise, S18's option d announces the tie, S19's picture shows the vendor's 16,400 before S20 asks me to predict it, and S28's option a carries its own reasoning.

**7. half1 S29 ("all book their biggest week on 5 October") against the plan weeks "12 October to 30 November" (S1); repeated on S36, half2 S3 and S4, and in the staffing note table.** Kind: contradiction. How badly: slows. 5 October lies outside the eight weeks to staff, so I could not see how a plan for those weeks "books" its peak there. No page says why the weeks of 28 September and 5 October are left out of the plan.

**8. half1 S2 map.** Kind: picture. How badly: minor. Arrows run from "One number" to four days, a dotted line joins Monday and Tuesday, and only Tuesday and the Kalpa lab lead to Saturday. I could not tell what an arrow means or why Wednesday and Thursday never reach Saturday.

**9. half1 S3 and S33 ("Rs 35,832 of idle shifts if high, Rs 1.7 lakh of late shipments if low").** Kind: number. How badly: minor. No slide shows this arithmetic. With the deck's own Rs 5.42, 6,615 x 5.42 gives Rs 35,853, so I could not reach 35,832; the Rs 1.7 lakh needs 6,615 x 25 = Rs 1.65 lakh rounded up.

**10. half1 S3 ("The error bar", title "a bar in rupees"), S33, half2 title and S1, notes, cheat sheet; fallback S12 ("error band").** Kind: word. How badly: slows. "Error bar" names "how wrong the plan could be" without a definition, and I know an error bar only as a whisker on a chart. "Error band" in the fallback deck is a third name.

**11. half1 S7 picture ("Cycle: payday weeks") against S8 ("The same point one cycle back, here 52 weeks"), notebook 01 cell 15 ("the same point in the last cycle (seasonal)"), the chapter 1 set ("Season is a pattern that repeats on a fixed beat; here the beat is four weeks"; option b "the 8 a cycle adds") and its solution ("rising 8 every cycle of four weeks").** Kind: contradiction. How badly: slows. On S7 a four-week repeat is a cycle and a season is a yearly peak. In the chapter 1 set the same four-week repeat is a season and a cycle is one turn of it, so I could not decide whether series B is a season or a cycle.

**12. half1 S8, row "Drift" ("The straight line through the first and last values | The average change added on").** Kind: step. How badly: slows. Drift is the only rule with no worked number on the canteen example (on 50, 52, 49, 51 it would be 51 and a third). No slide shows the line being extended one week at a time.

**13. half1 S8 ("plus the year's growth"), S9 card c ("add 4 percent"), S36 ("Your 4 percent is the growth two years show"), half2 S4 ("the two years grew 4.0 percent").** Kind: number. How badly: slows. On screen the 4 percent looks borrowed from finance. The only place it is measured is notebook 02 cell 6, in code (`y.iloc[52:91].sum() / y.iloc[0:39].sum() - 1`), and no sentence says which weeks those slices compare.

**14. The copy of last year goes by many names: "same week last year" and "house bot" (S3, S8), "the bot", "the house rule" (notebook 02 cell 1, guided set), "the copy of last year", "calendar copy", "seasonal copy" (notebook 01 cell 3, S26, notebook 02 cell 17, chapter 1 set), "same-period copy" (S14, notes) and "month-aligned copy" (notebook 04).** Kind: word. How badly: slows. For a while I thought "seasonal copy" and "house bot" were two different rules.

**15. Source tags "(F6, ...)" on S13, "(F2 ...)" on S14, "F1" on S26, "F5" on S35, "(F3)" on half2 S7, "(T3 ...)" on half2 S9, "F3" and "F4" on fallback S10 and S11; study notes last line ("F1 builds a series, F2 slides the hidden weeks, F3 moves Diwali, F4 moves the two costs").** Kind: contradiction. How badly: slows. No learner page says what the F and T tags point to. In the notes the same labels F1 to F4 then name explorer scenes, so F1 is a research paper on S26 and a slider in the notes.

**16. half1 S13 ("Ekart", "The Big Billion Days"); S35 and half2 S9 ("FADA", "SIAM", "GST cuts", "two-wheeler retail").** Kind: word. How badly: minor. No page says Ekart is Flipkart's delivery arm, and FADA and SIAM are never expanded. I did not see why two-wheeler sales belong in a Flipkart shipments case until a speaker note explained it.

**17. half1 S14 ("On Walmart's M5 data the same-period copy scored 0.847 against 1.752 for the naive, lower being better"); notes add "the random forest benchmark's 1.010".** Kind: number. How badly: slows. I do not know what M5 is or what measure gives 0.847, so the comparison only told me that lower wins. "Random forest" is never taught here.

**18. half1 S15 ("Rs 25 short, Rs 5.42 spare") and S22 ("a spare one Rs 5.42").** Kind: step. How badly: minor. Rs 5.42 is used twice before S32 shows Rs 650 / 120 on screen.

**19. Names for the cost of spare capacity: "an idle packer-shift" (S1), "a spare one" (S22), "a shipment of spare capacity" (S32), "being long" (S32 title), "a shipment planned and not shipped" (notebook 03 cell 9, notes, take-home), "a planned shipment that never comes" (Kahoot Q7), "an idle one Rs 5" (notes self-test 4).** Kind: word. How badly: slows. "A spare one" first read to me as an extra parcel. "Short" and "long" read like trading slang until S32.

**20. "Horizon" (S16, half2 S8 "Hide the horizon", notes and transcripts "at every horizon", Kahoot Q5 tag, self-check, fallback S5) and "origin" (notebook 02 cell 6 output "origin 2026-06-22", cell 17 "forecast them from one origin", notes "Rolling the origin", take-home, self-check, fallback title and S4); S15 "forecast from one week".** Kind: word. How badly: slows. "Horizon" is never defined on any page. "Origin" is defined only in the glossary at the very end of the notes, after the take-home has already used it. "Forecast from one week" first read to me as "using one week of data".

**21. MAPE (half2 S7 "MAE or MAPE, and when?", Kahoot Q2, transcripts).** Kind: word. How badly: slows. MAPE is never expanded on any learner page; in half one it appears only in the S17 speaker note. The follow-up asks me to choose a measure I was never shown.

**22. half1 S8 ("The week at the same distance from last year's Diwali") against S19 ("no hidden week lies within five weeks of a Diwali, so both rules copy the same week of 2025") and notebook 02 cell 5 ("for the weeks from five before Diwali to four after, the same calendar week otherwise").** Kind: contradiction. How badly: slows. Read literally, S8's rule copies 16 June 2025 into 29 June 2026, yet S19 says festival-aligned copies the same calendar week there. The switch-over rule is stated only in notebook 02, and S19 words its edge differently ("within five weeks").

**23. half1 S20 ("within 2 percent of every week it was fitted to") and the fit_vs_forecast picture ("within 2 percent") against S21 and S36 ("within 1.4 percent").** Kind: contradiction. How badly: minor. The same fit gets two sizes one slide apart. Only the study notes later explain that 2 is the claim and 1.4 the worst week.

**24. half1 S23 and the scoreboard picture.** Kind: picture. How badly: slows. The left panel shows MAE "a week", but the right panel's rupee axis has no unit and nothing says these are totals over thirteen weeks. S3 and S33 give rupees for a single week, so I mixed up the two until notebook 02 cell 14.

**25. half1 S24 ("3.6 percent too high in the first six hidden weeks, 11.5 percent in the last six"); also notebook 02 cell 15, notes, transcripts, chapter 2 solution.** Kind: number. How badly: slows. No cell prints either number. "First six" and "last six" of thirteen weeks leave the middle week unaccounted for.

**26. half1 S25 ("The same 6,615 from a table anyone can add up").** Kind: instruction. How badly: minor. The table of thirteen misses is in notebook 02 cell 16 and not on the slide, so the slide alone gives me nothing to add up.

**27. half1 S26 ("a seasonal copy beat half the machine-learning methods") against the transcripts and notes ("statistical methods beat machine-learning ones at every horizon").** Kind: contradiction. How badly: minor. The same 2018 paper is summarised two different ways, and I could not tell which is its finding.

**28. half1 S30 ("missed 2025's eight festive weeks"; "Rs 69.6 lakh of it late shipments").** Kind: number. How badly: minor. The slide does not name the eight weeks; only the picture's axis shows 29 September to 17 November 2025. Notebook 03 cell 4 prints only the Rs 79.8 lakh total, never the Rs 69.6 lakh part.

**29. half1 S30 and notebook 03 cell 4 (the 2025 back-test adds "plus 4 percent"); S16 ("as a planner standing there would have").** Kind: question. How badly: minor. A planner standing in September 2025 holds only one year of weeks. I could not see how they would know a growth rate that notebook 02 measured on weeks up to June 2026.

**30. "Back-test" (half1 S35 "the 2025 back-test", notes "back-tested", transcripts "I back-test the 2025 festival").** Kind: word. How badly: slows. It is never defined; I guessed it means standing in an earlier year and forecasting it.

**31. "Level" (S31 "level" meaning the same as; S27 "Level | How far above?"; S32 picture "against its level"; exercises "Level L1" to "L5"; lab set Q2 "Treat this year as level with last year"; fallback S8 "Level: one week ahead, both are close").** Kind: word. How badly: minor. One word carries three meanings: the same as, the height of the plan, and a difficulty grade.

**32. half1 S32 ("The cheapest plan covers demand in 25 / (25 + 5.42), about 0.82, of weeks"); notebook 03 cell 9 ("the share of weeks that balances the two"), notes, cheat sheet panel 6, half2 S1, Kahoot Q7.** Kind: step. How badly: blocks. The formula is stated and used everywhere but never derived. No small example shows why "short costs 4.6 times long" turns into covering 82 weeks in 100, so I could only memorise it.

**33. half1 S32 ("Festival-aligned's hidden-week misses put that at 2.6 percent above the forecast: demand beat the forecast by more in 18 percent of the hidden weeks"); notebook 03 cell 10 output; notes ("put the 0.82 point 2.6 percent above"); cheat sheet panel 6.** Kind: step. How badly: blocks. No page shows how to read "the 0.82 point" off thirteen misses, and 18 percent of thirteen weeks is 2.3 weeks. When I turned notebook 02 cell 16's printed misses into percents, three of thirteen weeks (about 23 percent) beat the forecast by more than 2.6 percent, so I could not reproduce the cushion every later number rests on.

**34. cost_curve picture (S32, notes).** Kind: picture. How badly: slows. Its labels "expected cost, Rs lakh" and "plan at the 0.82 quantile" use two words the pack never explains. The axis covers one week only (19 October 2026), and no text says how the curves were drawn from the thirteen misses.

**35. half1 S34 ("If demand follows the festival-aligned forecast, what does each other plan cost?").** Kind: question. How badly: minor. Every plan is priced against festival-aligned's own weeks, so festival-aligned wins by construction. The slide says "A scenario, never a measurement", and I still could not tell what the table proves.

**36. half1 S35 and the notes' doubts table (header "What would settle it").** Kind: contradiction. How badly: minor. The header promises the fact that would settle each doubt. Most rows give evidence already in hand instead ("Tested on one festival only: the 2025 back-test", the overtime count).

**37. half1 S35 ("Overtime reached 1,638 shifts in the week of 6 October 2025 against 5 in an ordinary week"); notebook 03 cell 15 ("an ordinary November week").** Kind: number. How badly: minor. No notebook prints the overtime column, so I could find neither number. The two pages also describe the ordinary week differently.

**38. half1 S35, half2 S9 and notes ("31,49,846", "12,87,735", "2,17,05,974") beside "2,370,680" and "1,983,300".** Kind: number. How badly: slows. The pack switches between Indian and international digit grouping, sometimes on one slide, and I misread 31,49,846 at first.

**39. half1 S36 ("plan at the 0.82 share"; "To the vendor's sponsor").** Kind: word. How badly: minor. "Share" is a new name for the 0.82, which S32 called a fraction "of weeks". The vendor's sponsor appears here for the first time with no introduction.

**40. festival_calendar picture (S12).** Kind: picture. How badly: slows. The columns carry 2025's Mondays, so 2024's Diwali week sits under "27 Oct" though the slides say 28 October. In 2026, Diwali's week sits under "3 Nov" and the bot's copy under "20 Oct", while S12 says 2 November and 19 October; the small subtitle "the nearest Monday each year" only made sense after I had found the mismatch.

**41. baselines_panel picture ("Drift: the line through it", "Festival-aligned (finance's ties)"); actual_series and fit_vs_forecast axes ("2024-10", "2025-01").** Kind: picture. How badly: minor. In the drift label, "it" has nothing to point to, and "finance's ties" reads oddly. The year-month axis style also differs from the day-month-year dates everywhere else.

### Which places in notebooks 01 to 03 stopped me?

**42. notebook 01 cell 10 (`copy51 = pd.Series({d: round(s[d - pd.Timedelta(weeks=51)] * 1.04) ...})`, printed as "festival-aligned").** Kind: code. How badly: slows. No sentence says why festival-aligned reaches 51 weeks back here (Diwali 2025's week came 51 weeks after 2024's). The 54 weeks the rule needs in 2026 is mentioned only once, in the notes.

**43. notebook 01 cells 6 and 8 (`rows.groupby(rows.week_start.dt.year).shipments.idxmax()`, `strftime("%d %b %y")`, `week = pd.Timestamp`, `f"{name:22s} {f:>9,} ..."`).** Kind: code. How badly: slows. I could not have typed these from what earlier weeks taught. Naming the Timestamp class `week` also made `week("2025-10-20")` look like a function I had missed.

**44. notebook 02 cell 6 (`h = pd.Series(range(1, 14), index=hold.index)`, `last_year = y.shift(52).loc[hold.index]`, `(last_year * 1.04)`).** Kind: code. How badly: slows. The markdown never explains `shift` or the letter `h`. The rules use a typed 1.04 right after the cell computes `growth`, so I wondered whether `growth` was used at all.

**45. notebook 02 cell 14 and notebook 03 cell 14 (`rules.sub(hold, axis=0).clip(lower=0).sum()`, `rules.rsub(hold, axis=0)`, `/ 1e5`).** Kind: code. How badly: slows. `sub`, `rsub`, `axis=0`, `clip` and `1e5` are all new. I worked out that `rsub` means actual minus forecast only by comparing with the printed table.

**46. notebook 02 cell 2 check ("the vendor's hold-out rows are forecasts, never fits", which tests `kind == "holdout"`) against the Kalpa vendor file, whose hidden months print as `['forecast']` when I run notebook 04's typed cell.** Kind: contradiction. How badly: minor. The same idea is labelled "holdout" in one file and "forecast" in the other, and the check's name calls the "holdout" rows "forecasts". No sentence tells me what the printed kind should prove.

**47. half1 S24 ("Its lean was never chosen"); notebook 02 cell 15 ("its high bias was never sized").** Kind: word. How badly: minor. "Lean" and "bias" are new words for erring one way, used without a definition.

**48. notebook 03 cell 2 (`aligned_source`, with `min(diwali.values(), key=lambda w: ...)` and `if -5 <= gap <= 4 and near.year - 1 in diwali`).** Kind: code. How badly: slows. `lambda` and `key=` were never taught. No markdown cell in notebook 03 restates the five-before, four-after window that the `if` line uses.

**49. notebook 03 cell 10 (`misses = (hold - fa_hold) / fa_hold  # positive: demand above the forecast`).** Kind: contradiction. How badly: slows. In notebook 01, notebook 02 cell 16 and the guided set, a miss is "the forecast minus what shipped: positive is too high". Here a miss is actual minus forecast, as a percent, so the same word flips sign.

**50. notebook 03 cell 10 (`cushion = round(misses.quantile(q), 3)`, `grid = [i / 1000 for i in range(-80, 101, 2)]`, the nested `cost = [sum(... max(0, ...) ...) / 13 / 1e5 for g in grid]`).** Kind: code. How badly: blocks. This cell sets the plan, and it is the hardest code of the day. No words walk through `quantile`, the grid, the two `max` terms or the division by 13.

**51. notebook 03 cell 15 ("how much inference capacity does a launch need?", "set capacity above the median"); half2 S8, transcripts, notes, cheat sheet panel 7.** Kind: word. How badly: slows. "Inference" is never explained. "Median" appears here for the first time, with no link to the 0.82 share.

### Which places in the three chapter exercises stopped me?

**52. Every set ("What you post. Three letters in item order ... Post exactly this shape: xxx").** Kind: instruction. How badly: minor. No set says where to post the letters.

**53. Guided Q1 ("Level L1 · asked in e-commerce and quick-commerce analytics screens"), chapter 2 Q2 ("GCC screens"), fallback S13 ("[D]").** Kind: word. How badly: minor. The levels are explained only in the index, which I read last. "Screens", "GCC" and the [S] and [D] tags are explained only in the transcripts, which come after these sets.

**54. Guided Q2 ("Hide the weeks of 13, 20 and 27 October 2025").** Kind: instruction. How badly: minor. The item says "hide" but names no week to forecast from. The copy of last year does not change whatever I hide, so I was unsure what hiding adds here.

**55. Chapter 2 Q1 (`naive = y.shift(1).loc[hold.index]`).** Kind: code. How badly: slows. The item turns on what `shift(1)` does, which no notebook explained in words. The solution explains it afterwards.

**56. Chapter 2 Q2 ("only by enough to change a decision"; key c "Skip A, rescore B, use C for ordinary weeks").** Kind: question. How badly: slows. No page says how much better than the bot counts as "enough" (A is 3 percent better). Neither the item nor its solution says why C is kept for ordinary weeks only.

**57. One-off terms: "RMSE" (chapter 2 Q1 option c), "R-squared" (transcripts), "overfitted" (Kahoot Q3), "baseline", "autocorrelation" and "smoothing or ARIMA" (half2 S10), "newsvendor rule" (practice-set solution).** Kind: word. How badly: minor. Each appears once with no explanation. The name "newsvendor rule" for the 0.82 idea appears only in the last solution file of the day.

### Which places in the afternoon deck, the staffing note, the transcripts and the Kahoot stopped me?

**58. half2 S7 ("A guardrail of plus or minus 200 basis points swung about 1,200; a write-down of about USD 304 million"); the transcripts' Zillow follow-up; notes; fallback S10.** Kind: word. How badly: blocks. "Basis points", "breakeven", "unit economics", "write-down" and "swung about 1,200" (1,200 of what?) are never explained. After three readings I still could not say what went wrong at Zillow.

**59. half2 S11 ("eight calls in twenty seconds each") against the Kahoot page ("twenty seconds each and forty for the plan share in item 7").** Kind: contradiction. How badly: minor. The deck promises twenty seconds for every call, but the answer sheet gives item 7 forty.

**60. Staffing note Q3 ("this year's sale opens four weeks before Diwali instead of three"; key b "Copy by distance from the sale, which the peak follows").** Kind: question. How badly: blocks. No page before this item says the festive sale opens three weeks before Diwali's week; only the calendar file shows it. The morning explained the peak by Diwali ("Parcels leave the centre before the festival", notebook 01 cell 7; S1 "the sale weeks move with it"), so the pack's own reasoning led me to option a. "The peak follows the sale" first appears in the transcripts, which come after this set.

**61. Staffing note Q3 against half1 S13 ("Before the sale opened on 9 October 2026").** Kind: contradiction. How badly: slows. 9 October 2026 falls in the week of 5 October, four weeks before Diwali's week of 2 November. Q3's "hypothetical" therefore reads like what S13 says really happened, and I could not tell whether the plan should already be lined up by the sale.

**62. Transcripts, Transcript 2 follow-ups ("finance's rule missed by 60,488 a week"; "price at Rs 8.8 lakh").** Kind: number. How badly: slows. No notebook prints either number. Notebook 03 cell 4 scores only the house bot and festival-aligned on 2025's festival, and no cell prices the plan raised 2.6 percent on the hidden weeks.

**63. Transcripts, Transcript 2 clarifying question 2 ("Finance's rule has, by the hold-out; the vendor's promise for the festive window has not").** Kind: contradiction. How badly: minor. The vendor was also scored on the hold-out (16,400). "Has not" confused me until I read it as "its festive weeks have not".

**64. Kahoot Q4 ("'This forecast is good enough': what is that sentence a claim about?").** Kind: question. How badly: slows. No deck, notebook, note or exercise teaches "good enough" as a claim about the decision. The nearest line is the chapter 2 set's "only by enough to change a decision".

### Which places in the Kalpa lab, the board set and the practice set stopped me?

**65. Notebook 04 cell 1 ("the monthly sums of the 1,000 orders in the Week 2 warehouse").** Kind: word. How badly: minor. On a day about a physical fulfilment centre, "warehouse" here seems to mean a data warehouse, and the page does not say so.

**66. Notebook 04 cell 6 (`drift = rev["2026-03"] + months_ahead * (rev["2026-03"] - rev["2024-10"]) / 17`).** Kind: code. How badly: slows. Nothing says that 17 is the number of months from October 2024 to March 2026.

**67. Notebook 04 cell 9, the code I am asked to type (`last = [rev[f"{int(m[:4]) - 1}{m[4:]}"] for m in months]`).** Kind: code. How badly: slows. I could type it but not understand it: the f-string slices a month label and subtracts a year in one line.

**68. Notebook 04 cells 1, 9 and 11 against the board set's second table.** Kind: contradiction. How badly: slows. The ask says "Finance's forecast is last year plus 4 percent", yet the table my typed cell prints has a "month-aligned" column with no 4 percent and no finance column. Cell 11 prints "the second year grew 3.7% on the first" while every Kalpa copy adds 4 percent, so I could not tell which column was finance's, or why 4 and not 3.7.

**69. Notebook 04 cell 9 and the board solution ("festival-aligned puts Diwali's spike in November, where the festival falls").** Kind: contradiction. How badly: slows. The morning taught that the busiest week comes two weeks before Diwali's week. With Diwali on Sunday 8 November 2026 that is the week of 19 October, still in October, so I could not see why the spike moves to November.

**70. Board set Q1 (option b "against the vendor's Rs 38.8"; option c "against naive's Rs 59.4 lakh").** Kind: question. How badly: slows. Both statements are true, and the stem does not say which comparison it wants. The solution rejects c because naive is something "nobody proposed for the board", which the stem never says.

**71. Board set Q3 key a and its solution ("The chosen forecast's own miss on the hidden months, Rs 11.7 lakh a month").** Kind: contradiction. How badly: slows. The set's own table gives 11.7 as the miss of "Same month of 2025 (the seasonal copy)", which has no 4 percent, while the board number is festival-aligned with 4 percent. When I added 4 percent to the copy's six months, the miss came to about Rs 3.5 lakh a month, which no option offers.

**72. Notebook 04 cell 4 chart ("Kalpa Retail revenue, Rs lakh a month").** Kind: picture. How badly: minor. The chart shows tall months in April and July of both years that no text mentions. I did not know whether they matter for the board number.

**73. Notebook 04 cell 3 ("Predict before you run. Which month is the biggest of each winter?") and cell 12 ("its error bar in Rs lakh from the six hidden months").** Kind: instruction. How badly: slows. Cell 3 offers no options to choose from. No cell scores festival-aligned on the six hidden months, so I did not know which number to bring as my error bar.

**74. Practice set Q2 ("what do naive, the same week last year and festival-aligned forecast for this year's week 5?" followed by "Which value is festival-aligned's?").** Kind: question. How badly: minor. The stem asks for three forecasts, but the options test only one.

### Which places in the take-home, the notes, the cheat sheet, the preview and the self-check stopped me?

**75. Take-home brief ("Move the split: the last week every rule may see is 24 August 2026, the 100th row (position 99)").** Kind: instruction. How badly: slows. Notebook 02 has 13 and 91 typed into several cells (`h = pd.Series(range(1, 14), ...)`, `ax.plot(range(1, 14), ...)`, `/ 13` in cell 16, the check "91 training weeks and 13 hidden ones"). Moving the split alone makes cell 6 stop with a length-mismatch error and cell 16 give a wrong hand count, and the brief does not warn me.

**76. Study notes formulas (`\hat{y}_{T+h} = y_T`, `\hat{y}_t = y_{t-52}`, `\text{MAE} = \frac{1}{n}\sum_{t} |y_t - \hat{y}_t|`) and cheat sheet panel 3 (`y[T]`, `y[t - 52]`, `y[T] + h x weekly change`).** Kind: word. How badly: slows. The hat, the small t, n and the summation sign are never explained; only T and h are. The cheat sheet repeats the notation with no key at all.

**77. Study notes, "Four ways to judge a forecast" ("Rolling the origin a week at a time gives many small tests, more work than a morning holds ... a third year of data would make rolling worth it").** Kind: step. How badly: slows. Rolling origin is named with no picture or example. Only the fallback deck shows one, and it runs only if the faculty session is cancelled; the notes also do not say why a third year would make rolling worth doing.

**78. Study notes GIF ("The thirteen hidden weeks revealed one at a time, each rule's misses adding up").** Kind: picture. How badly: slows. The animation shows only the house bot and the vendor, and its bars are the average so far rather than a running sum. Opened as one picture it shows the first frame, where the vendor leads 3,700 to 12,300 (the opposite of the day's message), and the notes do not place the last-frame still beside it.

**79. Study notes, "Two windows" ("finance's rule 9.5 below, 308,048 shipments short").** Kind: number. How badly: slows. In that sentence, 9.5 percent is measured against 2025's weeks counted from Diwali (2,279,500), but 308,048 is the gap to festival-aligned's 2026 forecast. Against 2,279,500 the shortfall would be 216,868, so I could not make the two numbers agree.

**80. Study notes ("That is 20,275 shifts, 515 above the forecast alone").** Kind: number. How badly: minor. The 515 needs the forecast's own shifts, rounded up week by week (19,760), which no page prints.

**81. Study notes last line ("The week's explorer replays the day").** Kind: instruction. How badly: slows. No page gives the explorer's file or link, so I could not open it.

**82. Study notes glossary ("Which words did Friday use?").** Kind: word. How badly: minor. It defines six words but leaves out the ones that stopped me most (horizon, quantile, back-test, error bar, drift, MAPE, fit). It also sits at the very end of the last reading of the day.

**83. Self-check ("The bot, finance's rule and festival-aligned barely moved") against its own scoreboard (6,615 to 8,104; 9,831 to 8,500) and the fallback picture title ("A four-week test moves every number; the order barely moves").** Kind: contradiction. How badly: minor. A 22 percent rise did not look like "barely moved" until I read that the forecasts stayed put and only the scores moved. "The order barely moves" also puzzled me, since the vendor climbs from last to third.

**84. Self-check scoreboard ("Vendor's curve ... Rs 5.8 lakh", "Naive ... Rs 37.0 lakh").** Kind: number. How badly: minor. By hand, 108,000 x 650 / 120 is Rs 5.85 lakh and 148,200 x 25 is Rs 37.05 lakh. My rounding gave 5.9 and 37.1, and I thought my notebook was wrong.

### Which places in the solutions and the index stopped me?

**85. Staffing note solution, Q2 row ("c sizes the bot's 19 October week, a post-festival copy").** Kind: contradiction. How badly: minor. The bot's 19 October 2026 copies 20 October 2025, which S12 calls Diwali 2025's own week, so "post-festival" did not match the morning.

**86. Index ("an interview question at an AI company (L6)", the staffing row "L4 to L6", "Eight of the fifteen exercise items", "a solutions file of the same name").** Kind: contradiction. How badly: minor. No item anywhere is marked L6 (the staffing items are L5, L5 and L4), and the six sets hold 21 items, not fifteen. Every solution file also has "_solution" in its name, so the names do not match.

### Which places in the fallback deck stopped me?

**87. Fallback S2 to S4 (the four-week test run in class, with 37,050 and the four misses on screen) against the self-check ("Open this after your notebook runs, never before").** Kind: contradiction. How badly: minor. If the fallback hour runs, tonight's take-home answers are already on the board.

**88. Fallback S8 options ("Naive, by about ten times", "Naive, by about thirty times") against S9 ("Answer: naive, by about thirty-five times").** Kind: contradiction. How badly: minor. The answer names a figure no option offered. Only the speaker note says b was the closest.

### Which sentences did I have to read three times?

These are listed apart from the 88 findings and are not in the counts below.

- half1 S17: "A percentage error would hide the size of a miss: the same percent is twice the shipments in a peak week."
- half1 S30: "Rs 69.6 lakh of it late shipments in the weeks the rush came early."
- half1 S32: "Festival-aligned's hidden-week misses put that at 2.6 percent above the forecast: demand beat the forecast by more in 18 percent of the hidden weeks."
- half2 S2, card 3: "Shipments a week, priced in each direction, and the festival's own record."
- notebook 03 cell 15: "One spike a year is two spikes in two years."
- notebook 03 cell 15: "A vendor model with no Lucknow festival in its forecast record is an assumption, like a forecast with no history behind it."
- notebook 04 cell 9: "the festival-aligned copy moves last year's Diwali month to this year's and puts last year's November in October's place, then adds 4 percent."
- transcripts, Zillow follow-up: "In 2021 its unit economics swung about 1,200 basis points toward minus 500 to minus 700, it wrote down about USD 304 million and cut about 25 percent of its workforce."
- transcripts, Transcript 2: "Raised by 2.6 percent on purpose, festival-aligned's misses on the same weeks price at Rs 8.8 lakh, a figure flattered a little because the 2.6 was read from those weeks."
- take-home brief: "It says which rules never looked at the origin, and so barely moved."
- study notes, "Say it to a shift supervisor": "so its busiest week comes two weeks before the real one."
- study notes, CALLBACK: "Thursday gave the week a time axis; today it runs forward."
- study notes: "Rolling the origin a week at a time gives many small tests, more work than a morning holds."
- same-week-rule solution: "each calendar copy carried a week that sat closer to the 2024 festival."

### How do the findings count up?

| Kind | Blocks | Slows | Minor | Total |
|---|---|---|---|---|
| Word | 1 | 10 | 10 | 21 |
| Step | 2 | 2 | 2 | 6 |
| Number | 0 | 6 | 5 | 11 |
| Picture | 0 | 4 | 3 | 7 |
| Code | 1 | 8 | 0 | 9 |
| Instruction | 0 | 3 | 4 | 7 |
| Contradiction | 0 | 9 | 11 | 20 |
| Question | 1 | 3 | 3 | 7 |
| All | 5 | 45 | 38 | 88 |

### Where is a weak learner most likely to give up?

The first place is the plan's level in chapter 3 (findings 32, 33, 34 and 50). The 0.82 share is never derived, and the step from 0.82 to the 2.6 percent cushion happens inside a pandas `quantile` call that no sentence explains. The printed "18 percent of the hidden weeks" does not match a count of the thirteen printed misses, and the cost-curve cell is the hardest code of the day; yet the 20,275 shifts and every rupee figure after them rest on that cushion.

The second is the Kalpa lab (findings 66 to 73), which comes at the end of a long day. The typed cells use code the learner has not seen, and the printed table has no finance column. The growth printed is 3.7 percent while every copy adds 4, and the spike moves to a month the morning's own rule would not choose. The keyed error bar also belongs to a different forecast from the one sent to the board, so the careful learner is the one who ends up confused.

The third is the Zillow material (finding 58), repeated on the afternoon deck, in the transcripts, in the notes and on the fallback deck. Basis points, breakeven and write-downs arrive with no explanation, so a learner preparing for an interview would memorise a line they cannot explain. That comes on top of a steady pile of undefined words (horizon, origin, back-test, error bar, MAPE) and nine names for one copying rule.

---

## Read 2: what would a hiring interviewer reject?

### What does a forecasting interviewer make of Friday's interview material?

This is a cold read of the frozen snapshot of `content/W04/D5`, read as a hiring interviewer for 0 to 3 year analytics, data-science and forecasting roles. Short names are used below. **Transcripts** is `extras/C2_W04_D05_interview_transcripts_STUDENT.md` and **Scorecards** is `trainer/C2_W04_D05_interview_scorecards_TRAINER.md`. **Half one**, **Half two** and **Fallback** are the three decks in `slides/`. **Notes** is `study-notes/C2_W04_D05_notes_STUDENT.md`, **Sheet** is `cheatsheets/C2_W04_D05_beat_the_bot_STUDENT.md`, **Card** is `trainer/C2_W04_D05_guesstimate_TRAINER.md` and **Facts** is `internal/C2_W04_D05_facts_INTERNAL.yaml`.

Every figure I recomputed comes from the pack's own `data/` files, using small scripts in the session scratchpad. I changed nothing in the repository or the snapshot. Every outside source below was opened on 12 October 2026.

#### How do the three hire-grade answers score?

##### How does transcript 1's hire-grade answer score?

| Criterion | Mine | Programme | The line that earns or loses the point |
|---|---|---|---|
| Clarified the scope | 2 | 2, agree | Four clarifiers; the sharpest is "Has any of the three been scored on weeks it never saw?" The reply to the first one gives the plan's length (eight weeks) where the question asked how far ahead the plan is booked, which feeds finding 1. |
| Named the hidden weeks and the unit | 1 | 2, disagree | Earned by "I hide the latest thirteen weeks, 29 June to 21 September 2026 ... forecast them from 22 June" and "MAE ... in shipments". Lost because the obvious follow-up (why a symmetric measure when a short week costs 4.6 times a long one?) has no answer (finding 2), and because "longer than the eight-week plan" counts the wrong horizon (finding 1). |
| Saw the paradox | 2 | 2, agree | "too high in 12 of 13 weeks, though it fits its 91 past weeks within 1.4 percent", then "Priced, the vendor's misses cost least". |
| Sized it with a unit | 2 | 2, agree | 9,831, 6,615 and 16,400 shipments a week; Rs 11.9 lakh against Rs 13.5 lakh; 0.82 and 2.6 percent. |
| Said what would change their mind | 1 | 2, disagree | "A third year of data, or a sale that opens a different distance before Diwali; either would move the plan's peak." A third year cannot arrive before Friday, and it would refine the estimate rather than move the peak. The sale is the real trigger, but the answer gives no date to check it against and no threshold. |
| Tied it to a decision and its cost | 2 | 2, agree | "So I lean high on purpose: the plan covers demand in 0.82 of weeks, festival-aligned plus 2.6 percent." |
| Gave the structure before the number | 2 | 2, agree | The five-step structure comes before any figure. |
| **Total, of 14** | **12** | **14** | |

**Would I hire?** Lean hire, for an analyst or junior data-science screen. The answer has the skeleton I listen for at this level:
- a test that respects time order;
- naive and seasonal baselines;
- the error in the business's unit;
- an asymmetric cost;
- a separate test of what the hold-out cannot see.

Many candidates at this level miss two of those five. It is short of a clear hire for two reasons. Three of its lines break under the next follow-up (findings 2, 3 and 4). "The house bot" and more than a dozen exact case figures would also make me probe whether the candidate understands the method or has rehearsed this case (finding 20).

##### How does the AI-company variant score?

| Criterion | Mine | Programme | The line that earns or loses the point |
|---|---|---|---|
| Clarified the scope | 2 | 2, agree | "How long does it take to add capacity? What does a timeout cost us against an idle machine for an hour?" Lead time and the cost asymmetry are the two clarifiers that matter. |
| Named the hidden weeks and the unit | 1 | 2, disagree | "Hide the last launch's own days as the test" leaves nothing to copy from unless an earlier launch exists, and the answer never says one does (finding 13). "Requests a minute" is also a weak unit for model serving (finding 12). |
| Saw the paradox | 0 | 2, disagree | The rubric's paradox (a close fit, or cheap misses, that do not earn the plan) never appears. The programme credits the calendar-alignment point instead, which is a different idea. |
| Sized it with a unit | 0 | 1, disagree | The answer gives no figure at all, and the rubric's own scale calls that absent. |
| Said what would change their mind | 1 | 2, disagree | "A model that cannot beat the last launch's shape on those hidden days does not size the launch" is a gate on models. It names no signal that would move the capacity booked, such as waitlist sign-ups or first-hour traffic. |
| Tied it to a decision and its cost | 1 | 2, disagree | "Plan above the forecast, since a timeout loses a user and an idle machine loses an hour of rent" ties capacity to cost. But the share-of-minutes rule accepts timeouts in about one minute in five, and the two costs are in units the answer never converts (finding 12). |
| Gave the structure before the number | 2 | 2, agree | Clarify, line up by launch day, the copy to beat, the test, the plan's level. The missing number is already charged under sizing. |
| **Total, of 14** | **7** | **13** | |

**Would I hire?** No, not on this answer at an AI startup. Carrying the festival idea over to a launch earns credit. But an inference-capacity question is a sizing question, and this answer sizes nothing. It plans in a unit the serving team does not use, and it has no plan for a first launch with no history (finding 42).

##### How does transcript 2's hire-grade answer score?

| Criterion | Mine | Programme | The line that earns or loses the point |
|---|---|---|---|
| Clarified the scope | 2 | 2, agree | "Plus 4 and plus 22 against which weeks of last year?" is the best clarifier in the pack. It shows that both numbers sit on calendar weeks holding only the festival's tail. |
| Named the hidden weeks and the unit | 2 | 2, agree | "Scored on thirteen hidden weeks ... 6,615 a week", with the 2025 festival back-test named as a separate test. |
| Saw the paradox | 2 | 2, agree | "your rule ties ours on the hidden weeks" and "its misses on the hidden weeks are the cheap kind", each with its reason. |
| Sized it with a unit | 2 | 2, agree | 20,275 packer shifts, 3,719 at the peak, 6,615 shipments a week, and rupees in each direction. |
| Said what would change their mind | 2 | 2, agree | "the curve beating the house bot on a festival it never saw" can be tested before Friday: ask the vendor to forecast 2025's festival from data to September 2025. |
| Tied it to a decision and its cost | 1 | 2, disagree | "Rs 35,832 of idle shifts if a week lands high, Rs 1.7 lakh of late shipments if it lands low" prices the unraised forecast rather than the plan being recommended (finding 5). Finance also never hears what the plan costs over its own rule (finding 27). |
| Gave the structure before the number | 2 | 2, agree | Restate, answer, concede, what would change it, then the plan. |
| **Total, of 14** | **13** | **14** | |

**Would I hire?** Yes, at 0 to 3 years. The answer settles a two-stakeholder dispute from evidence, concedes the true half of each position and ends on a plan with a number, which few juniors manage. I would still push on the error bar and on averaging (findings 5 and 14), and on how the candidate brings two senior people along (finding 28).

##### What about the weak answers and their scores?

I agree that both weak answers score close to nothing. I disagree with the sizing point given to transcript 1's weak answer: "R-squared, or maybe MAPE" carries no figure, and percent is not one of the rubric's units (shipments, shifts or rupees), so it scores 0. Transcript 2's "13 percent" earns its 1 only on a generous reading of the same rule. Both weak answers are straw men (finding 19).

#### What would a strong interviewer reject or mark down?

1. **Transcripts, transcript 1: structure step 2, and the "The test" row ("longer than the eight-week plan"). Also Scorecards push-back ("Thirteen covers the eight-week horizon"), Fallback S5 ("The plan books eight weeks, so the test hides at least eight"), Notes interview table row 1 and Sheet panel 7.** The data end with the week of 21 September and the plan's last week begins 30 November, so the farthest week ahead is ten, and FPP3's rule is a test "at least as large as the maximum forecast horizon required" (Facts records `horizon_weeks: 10`). Thirteen weeks still covers ten, but every version of the reason confuses the plan's length with its lead time, and a forecasting interviewer would correct it on the spot.

2. **Transcripts, transcript 1: the "The measure" row ("MAE ... fixed before anyone scores") against the "The price" row, and follow-up 1 ("MAE in shipments when the cost is per shipment").** The answer fixes a symmetric measure, then sets the plan with an asymmetric priced loss under which the order flips and the vendor wins, so it reads as changing the measure once the first one crowns the wrong forecast. MAE fits a cost that is per shipment and equal in both directions; this decision's loss is the quantile (pinball) score at 0.82 from FPP3 section 5.9, and comparing each forecast's plan under that loss, with each cushion set the same way, would fix this finding and the next.

3. **Transcripts, transcript 2, follow-up 3 ("Raised by 2.6 percent on purpose ... Rs 8.8 lakh, a figure flattered a little"); Scorecards push-back ("Yes, a little").** The cushion is read from the same thirteen weeks it is scored on, the vendor gets no such tuning, and the 0.82 point of thirteen errors moves from 2.1 to 4.1 percent with the choice of quantile method alone (linear interpolation gives the 2.6). The fair comparison exists and still favours festival-aligned: scaled to its own 0.82 point on the same weeks, the vendor's misses price at about Rs 10.0 lakh against Rs 8.8 lakh, so the candidate should offer that instead of "flattered a little".

4. **Transcripts: transcript 1's "What the test cannot see" row and transcript 2's "Answer" row (festival-aligned "by 4,034"); Scorecards ("checked against 2025's festival").** On the hidden weeks festival-aligned is identical to finance's rule, so the whole case for lining up by Diwali rests on this one back-test, and at its origin, 22 September 2025, the history is exactly 52 weeks, too short to measure the 4 percent growth the rule multiplies by (the pack calls it "the growth two years show"). Without that growth the same copy misses by about 10,575 a week, and the raised plan covers 2 of the 8 festive weeks instead of 7; the verdict against the calendar copy (58,250) survives, but a festive error of about 1.4 percent of a festive week, half the 3.0 percent the same rule missed by on the July to September hidden weeks, would make me ask why the busiest weeks are the easiest to forecast.

5. **Transcripts, transcript 2, "The error" row ("6,615 shipments a week: Rs 35,832 ... Rs 1.7 lakh").** The rupees price the unraised forecast: the plan actually recommended sits 5,100 to 11,308 shipments above the forecast each week, so a week landing 6,615 above the forecast costs Rs 9,400 to Rs 37,900 (late shipments only in the four November weeks, where the cushion is under 6,615), and a week landing 6,615 below costs Rs 63,000 to Rs 97,000 of idle shifts. The bar also mixes two error models (the cushion in percent, the bar in fixed shipments, which is 1.5 percent of the peak week and 3.4 percent of the week of 9 November), and an MAE is an average miss, while "how do you present the error?" asks for a range, such as an 80 percent interval in shifts for the peak week.

6. **Transcripts, transcript 1, follow-up 1 ("MAPE when I compare series of different sizes ... section 5.8"); Half two S7; Notes interview table row 2.** MAPE can compare centres of different sizes, but the answer misses the two measures I would expect: MASE, which the cited section offers "as an alternative to using percentage errors when comparing forecast accuracy across series with different units", and WAPE (total absolute error over total actuals). The same section warns that percentage errors "put a heavier penalty on negative errors", which here means over-forecasts, so picking by MAPE leans toward the short side that costs Rs 25, and a strong candidate says so.

7. **Transcripts, transcript 1, follow-up 3 ("The guardrail bounded the forecast, and the forecast was what failed"), and pain-point row 3. Also Half two S7 ("A guardrail ... swung about 1,200"), Notes ("A 200-basis-point band swung about 1,200") and Fallback S10 notes ("nobody watching the band").** Zillow's letter set "unit economic target guardrails publicly of +/- 200 basis points of breakeven economics", a margin target on results, and it was the unit economics that swung about 1,200 basis points. The same letter names "renovation and resale capacity constraints" and conversion "higher-than-anticipated" alongside price-forecast volatility, and Zillow did stop (it suspended new contracts), so "stop when it is breached" and "nobody watching the band" are not what the source shows, and an interviewer who knows the case would stop the candidate here.

8. **Transcripts, pain-point row 1 ("statistical methods beat machine-learning ones at every horizon"); Notes, chapter 2 field note.** This is true of the 2018 paper on 1,045 M3 monthly series, but as a 2026 lesson it is out of date: the M5 accuracy paper reports that "in the M5 all 50 top-performing methods were ML", LightGBM-based and "significantly better than all statistical benchmarks and their combinations", and the winner's 0.520 beat the seasonal naive's 0.847 in the very workbook the pack cites. Told to an AI startup or Google as "statistics beat ML" it sounds cherry-picked; the defensible lesson is the paper's other line, that the best fits "did not necessarily" forecast best, and the transcript drops the word "necessarily".

9. **Transcripts, pain-point row 5 (Amazon Science, "a plain bestseller list beat a deep-learning recommender"); Notes, pain-points paragraph.** The article says the bestseller list won the first test, and that once the team retrained the autoencoder "on movie-viewing data that had been sorted chronologically" and tested on the two weeks after the cutoff, the autoencoder beat the bestseller list and beat item-to-item filtering two to one. Quoting only the first half reverses the outcome; the full story teaches Friday's own lesson (test on weeks after the training cutoff) and should be told that way.

10. **Transcripts, pain-point row 2 (Target Canada, cited to "Target's release of 15 January 2015"); Notes, pain-points paragraph.** The release gives 133 stores, about 17,600 people and a profitability reason and says nothing about forecasting, which comes from Canadian Business (Joe Castaldo, "The Last Days of Target"), the same article that puts item data accuracy at "about 30%" and describes a much wider supply-chain failure. A one-cause line ("could not forecast new stores ... and Target closed all 133 stores") would be challenged, and the row's check (score the model on a festival it did not see) suits a model with history, while this is a cold-start case that belongs beside the AI launch variant.

11. **Transcripts, AI variant ("Line the last launch up by days from launch day ... because a weekday launch and a weekend launch peak on different dates"); Half two S8; Sheet panel 7.** Counting days from launch lines up the launch curve but scrambles the weekly cycle, which stays on the calendar: day 4 of a Tuesday launch is a Saturday, and day 4 of a Saturday launch is a Wednesday. The forecast needs both a days-since-launch effect and a day-of-week effect, and the reason given argues for the half that does not fix the problem it names.

12. **Transcripts, AI variant ("requests a minute"; "the share of minutes to cover is the cost of a timeout over the two costs added, the same arithmetic as the packer shifts").** Serving load for a model runs on tokens and concurrent requests, so requests a minute misstates capacity, and the 0.82 arithmetic carried over would accept timeouts in roughly one minute in five, while serving is planned to a latency target with headroom because queueing delay climbs steeply near saturation. The costs are per request and per machine-hour with no conversion between them, and the clarified target, "requests a minute at the peak", is one number where the share-of-minutes rule needs the spread across minutes.

13. **Transcripts, AI variant ("Hide the last launch's own days as the test" beside "The copy to beat is the last launch's shape"); Half two S8 ("Hide the horizon").** Testing the last launch's shape as a forecast needs a launch before it, so a startup with one prior launch has no out-of-sample test of this method at all. The answer should say so and move to an analogue or a bottom-up model, plus capacity that can stretch.

14. **Transcripts, transcript 2, follow-up 1 ("Both are copies of the calendar ... Averaging two forecasts with the same error keeps the error").** This holds for a shared placement error, but said flatly it contradicts the steadiest finding in the field, which the M5 paper puts as "combining improves forecasting accuracy" across all five M competitions; the candidate should say why this case is the exception, and that averaging with an independently placed forecast would help. "Copies of the calendar" also asserts the vendor's internals from its output, about a curve that fitted two festivals a week apart within 1.4 percent; what was observed is that its 2026 peak lands on 5 October.

15. **Scorecards, push-back ("13 of 104 is an eighth, which is the honest limit of two years").** A same-week or festival-aligned copy needs only 52 weeks of history, so those copies could be scored on much longer tests, and 21 weeks would meet the "about a fifth" the same reply quotes; the real limit is the vendor's need for training data, which the reply should name. A hold-out starting in late September 2025 would put the 2025 festival inside the test, the very gap the answer has to close with a separate back-test.

16. **Notes, "Four ways to judge a forecast" ("Rolling the origin ... more work than a morning holds ... a third year of data would make rolling worth it").** A rolling origin needs no third year for the seasonal copies: dozens of origins from late September 2025 onward have a full year behind them, and Fallback part 2 rolls five origins through 2025 itself. A candidate who repeats "rolling needs a third year" would be marked down in any data-science screen.

17. **Half two S10 ("earn its place above the festival-aligned baseline on the thirteen held-out weeks").** The same thirteen weeks have already picked the rule and set the cushion, so judging further models on them turns the test set into a validation set, and those weeks hold no festival, which is where the baseline differs from finance's rule. A strong interviewer would ask for a fresh hold-out or a rolling-origin back-test before any smoothing or ARIMA model is compared.

18. **Fallback S13, hire-grade column ("Concedes what is true in each: finance's growth, the vendor's fit").** The vendor's fit is the part that misleads, so conceding it hands the sponsor the wrong point; transcript 2's own concede line names the true part, that its misses run to the cheap side. The slide summarises the transcript more weakly than the transcript itself.

19. **Transcripts, both "Weak answer" columns ("I would check how well each model fits the history", "R-squared, or maybe MAPE", four rows of "Not reached"; "I would average them: 13 percent", "Nothing conceded", "Not said"); Scorecards, "Where the weak answer scores its point".** These are straw men: the weak answers I hear most often from 0 to 3 year candidates are a random 80/20 split scored by RMSE or MAPE with no baseline (a failure the Notes name), or "use the vendor's model, it is proper ML with a 2 percent fit". Contrasting with those would teach what separates candidates, and the scorecard's sizing point for "maybe MAPE" breaks its own unit rule.

20. **Transcripts and Notes, the hire-grade lines generally ("the house bot", "festival-aligned", "hidden weeks", "forecast them from one week").** The standard terms never appear (seasonal naive baseline, hold-out or test set, forecast origin, rolling-origin back-test, newsvendor critical ratio, quantile loss), so the answers sound like this programme rather than the field, and the aphorisms ("The guardrail bounded the forecast...") and more than a dozen exact case figures would sound memorised. The candidate also never says the Flipkart Lucknow numbers come from a synthetic class case, which in a real screen can sound like a claim to real company data.

21. **Scorecards, all three tables.** None of the seven criteria checks technical soundness (a test with no leakage, a measure that matches the decision's loss, an honest statement of uncertainty), so a 14 out of 14 here can still carry findings 2 to 5. A rubric used to train interview answers needs an eighth line: "the method survives a technical follow-up".

#### Where do the answers stop short of a strong candidate?

22. **Transcripts, transcript 1, structure step 2 ("forecast them from one week").** A strong candidate at Uber, Google or Swiggy runs a rolling-origin back-test and reports the error by weeks ahead, because one origin is one draw, as the Fallback shows with naive scoring 14,923 on thirteen weeks from 22 June and 37,050 on four weeks from 24 August. This is the single addition that matters most: run through autumn 2025 for the copies, it puts a festival inside the test, gives enough errors to set the cushion away from the scored weeks, and answers findings 3, 4, 15 and 16 at once.

23. **Transcripts, both answers.** The plan is a quantile, yet nothing checks a quantile: there is no prediction interval, no quantile score and no coverage figure (the raised plan covered 10 of 13 hidden weeks, and 7 of 8 festive weeks only with the 4 percent questioned in finding 4). The line "my 0.82 plan covered about four weeks in five on weeks it never saw" would lift both answers.

24. **Transcripts, transcript 1, "What the test cannot see" row.** Shipments are what the centre packed, and in the week of 6 October 2025, 1,638 of the 3,485 shifts worked were overtime, so the peak may have been capped by capacity with demand above what shipped, which makes any copy of last year's peak run low on the expensive side. A strong candidate names censored demand before trusting the history; the Notes list it as a doubt, but the transcripts never mention it.

25. **Transcripts, transcript 1, structure step 4 ("set the plan's level from the two costs").** The two-cost rule treats each week alone with no recourse, while a short week can be met with overtime, temporary staff or orders routed to another centre, and its backlog spills into the next week. Strong operations candidates also plan the sale weeks by day, since the opening days spike, and ask whether new festive hires reach 120 shipments a shift.

26. **Transcripts, transcript 1, "The bar to beat" row.** "Too high in 12 of 13 weeks" points toward the sharper diagnosis: the vendor's error is almost all bias (mean error +16,108 a week against an MAE of 16,400), growing with the weeks ahead, which often means a wrong trend. A strong candidate separates bias from noise and says what a bias-corrected vendor curve would score.

27. **Transcripts, transcript 2, the "Answer" and "The error" rows.** Finance hears no budget figure: finance's rule books about 17,193 shifts against the plan's 20,275, about 3,082 more, or roughly Rs 20 lakh at Rs 650 a shift, and that is the number the finance stakeholder will ask for first. The answer also books once and walks away, where a strong candidate agrees an in-season trigger in advance (re-plan if the first sale week lands outside the band) and keeps part of the capacity flexible.

28. **Transcripts, transcript 2, the question ("Both are senior to you").** The answer handles the evidence and says nothing about the people: sharing the back-test with each stakeholder before the meeting, and putting the options with their costs in front of the operations head. A differentiator answer needs one sentence on this.

29. **Transcripts, AI variant.** A strong candidate sizes from the bottom up (users, adoption, requests per user, tokens per request, the ratio of peak to average) against a latency target, and buys stretch (burst capacity, rate limits, a waitlist) for what the forecast cannot know. One worked figure would earn the sizing point the variant now loses.

**The single addition that matters most** is finding 22, a rolling-origin back-test with errors by weeks ahead. For transcript 2 alone it would be the budget figure plus an in-season trigger (finding 27). For the AI variant it would be a bottom-up figure in tokens against a latency target (finding 29).

#### Which facts need a source, and which look wrong?

30. **Zillow (transcripts follow-up 3 and pain-point row 3; Half two S7; Notes; Fallback S10).** The pages name the source with a check date (the Q3 2021 shareholder letter, checked 12 October 2026) but give no URL. The figures hold against the letter (https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/exhibit993.htm, checked 12 October 2026): "+/- 200 basis points of breakeven economics"; "approximately 1,200 basis points from Q2 to an expected -500 to -700 basis points in Q4 2021"; "a $304 million write-down on inventory"; a workforce reduction of "approximately 25%" over the next few quarters; and forecasting "three to six months into the future". The reading of these figures is wrong (finding 7).

31. **PLOS ONE 2018 (transcripts pain-point row 1; Notes; Half one S26).** The pages name the paper with a check date but give no DOI. The paper (https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0194889, checked 12 October 2026) does use 1,045 monthly M3 series and says the ML methods were "dominated ... for all forecasting horizons examined". Half one S26's "a seasonal copy beat half the machine-learning methods" needs correcting: the paper's benchmark is Naive 2, "a random walk model adjusted for seasonality", and its "half of the ML methods" comparison is for one-step-ahead forecasts only.

32. **Target Canada (transcripts pain-point row 2; Notes; Fallback S11).** The release confirms 133 stores and "approximately 17,600 people" on 15 January 2015 (https://corporate.target.com/press/release/2015/01/target-corporation-announces-plans-to-discontinue-canadian-operations, checked 12 October 2026). The forecasting clause needs its own source on the student pages. It is Canadian Business's account, read through the gwern.net mirror listed in the INTERNAL sources page. The Fallback notes say so; the Transcripts and Notes do not.

33. **FADA (transcripts pain-point row 4; Notes; Half one S35; Half two S9).** Right, and sourced with its date, so nothing needs correcting. The release of 7 November 2025 (https://fada.in/images/press-release/1690d68d7a2e6cFADA%20releases%20October%202025%20&%2042-Days%20Festive%20Vehicle%20Retail%20Data.pdf, checked 12 October 2026) gives two-wheeler retail of 31,49,846 in October 2025 and 12,87,735 in September. It credits GST 2.0 and defines the window as running "from 1st day of Navratri to 15 days post Dhanteras due to time lag for vehicle registration".

34. **Amazon Science (transcripts pain-point row 5; Notes).** The pages give a check date but not the article's author and date: Larry Hardesty, 22 November 2019 (https://www.amazon.science/the-history-of-amazons-recommendation-algorithm, checked 12 October 2026). The claim also reverses the article's outcome (finding 9).

35. **M5 (Notes, chapter 1 field note; Half one S14).** The workbook figures are right: naive 1.752, seasonal naive 0.847, random forest 1.010, MLP 0.977 and winner 0.520 (https://raw.githubusercontent.com/Mcompetitions/M5-methods/master/Scores%20and%20Ranks.xlsx, checked 12 October 2026). The "same-period copy" needs correcting. The M5 paper (Makridakis, Spiliotis and Assimakopoulos, International Journal of Forecasting, 2022; preprint at https://statmodeling.stat.columbia.edu/wp-content/uploads/2021/10/M5_accuracy_competition.pdf, checked 12 October 2026) sets the seasonal naive's period "equal to 7 since the series are daily". That is a copy of the same weekday one week back, so it is no evidence for copying the same week last year. The pack also leaves out the paper's headline result, that ML methods took the top places (finding 8).

36. **SIAM (Half two S9; Card; Notes).** Right, and sourced with its date. SIAM's release (https://www.siam.in/news-&-updates/press-releases/x/605, checked 12 October 2026) gives two-wheeler sales of 2,17,05,974 for April 2025 to March 2026, with growth of 10.7 percent. These are domestic sales reported by manufacturers, meaning dispatches to dealers, which the guesstimate's own definition does not match (finding 44).

37. **Flipkart, 6 October 2026 (Notes chapter 3; Half one S13).** The 14 million cubic feet and the 9 October sale date are right (https://stories.flipkart.com/announcement/flipkarts-big-billion-days-returns-for-its-13th-edition, checked 12 October 2026; early access opened on 8 October). Two problems remain:
- The Notes' "created more than 2.5 lakh festive jobs" overstates the source, which says "More than 2.5 lakh direct and indirect employment opportunities".
- The real 9 October opening falls in the week of 5 October. The synthetic calendar puts the 2026 sale weeks at 12 and 19 October, and the plan peaks on 19 October. The pack never reconciles the two (finding 41).

38. **FPP3 (transcripts follow-up 1; Half one S16; Fallback S5 and S6).** Section numbers and wording are right (https://otexts.com/fpp3/accuracy.html, checked 12 October 2026). The sections are 5.2, 5.8, 5.9 and 5.10, and the quoted rules read "at least as large as the maximum forecast horizon required" and "A model which fits the training data well will not necessarily forecast well". The fault lies in applying the horizon rule (finding 1).

39. **Diwali dates (Notes opening; Half one S1).** 31 October 2024, 20 October 2025 and 8 November 2026 look right, but the Notes state them with no source on the page. The trainer calendar card sources them to staffnews.in copies of the DoPT lists and says DoPT's own site refused the connection. The DoPT order itself should replace those links once it can be reached.

#### Which follow-ups would I ask that the transcripts do not prepare for?

40. **Overtime and censored demand.** "In your 2025 peak week, 1,638 of the 3,485 shifts were overtime. Did that week ship all its demand, and what does an overtime shift cost?" If overtime can absorb a short week, the cost of being short is the overtime premium, not Rs 25. At one and a half times the ordinary rate the share to cover falls from 0.82 to about 0.33, and at twice the rate it falls to 0.5. The plan's whole cushion therefore depends on a question the transcripts never ask.

41. **The real sale date.** "Flipkart opened The Big Billion Days on 9 October this year, with early access on 8 October, in the week of 5 October, four weeks before Diwali's week. Your data's 2026 sale weeks are 12 and 19 October and your plan peaks on 19 October. What do you change?" This tests the candidate's own "what would change my mind", using a date the pack itself cites (Half one S13).

42. **A first launch.** "This feature has never launched, so there is no last launch. What is your forecast, and what capacity do you commit before you know?" The answer I want has three parts: a bottom-up range in tokens, an analogue from a nearby feature, and capacity that can stretch (burst, rate limits, a waitlist). That is the Target Canada lesson in AI form.

#### How good is the two-wheeler guesstimate?

43. **Card, "How does a strong candidate run it?", and Half two S9.** The structure is right and in the right order: clarify, map, assume with ranges, calculate, validate, then the catch, with "Every input is an assumption, said as one" as the habit. At 0 to 3 years this passes a guesstimate round.

44. **Card, the Clarify row against the Validate row.** "New vehicles sold to buyers in India" defines retail sales, but SIAM's 2,17,05,974 counts manufacturers' domestic sales, so "I am within 1 percent" compares across two definitions. The card's last paragraph knows the difference, but the candidate's line never says it, and a registrations count for the same year would match the definition.

45. **Card, the "Assume, with ranges" row.** Thirty crore households and half of them owning a two-wheeler are defensible and labelled, but the map counts one vehicle per owning household and leaves out commercial riders (delivery fleets and bike taxis), the first gap an interviewer at Swiggy or Uber would raise. The eight-year cycle is how long a first owner keeps a vehicle, while new-vehicle demand also depends on scrappage and the used market.

46. **Card, the Calculate row ("about 1.2 crore to about 3.8 crore across the ranges, every extreme multiplied together").** Putting every input at its extreme at once gives a band too wide to tell the candidate anything, since the extremes rarely coincide. Swinging one input at a time shows that the replacement years (plus 33 to minus 20 percent) and the ownership share (plus or minus 20 percent) dominate, which supports the card's conclusion with a method a candidate can say aloud.

47. **Card, the Calculate row, and Half two S9 ("about 1.9 crore ... about 2.16 crore").** 1.9 times 1.15 is about 2.19, so the spoken arithmetic does not follow; the 2.16 comes from the unrounded 1.875. Quoting 2.16 crore from inputs this loose is false precision where "about 2 crore" is the honest output, and the card's own "luck as much as method" is the right reflex.

48. **Card, "The catch" row, and Half two S9 ("never annualise a festive month").** This is the right lesson for the day, but October 2025 was more than a festive month. FADA's release says the first 21 days of September were muted ahead of GST 2.0, so that demand landed in October, and FADA counts registrations, which lag sales. The 74 percent also sets a month of registrations against a year of dispatches, which the candidate should say.

The guesstimate is the strongest item in the interview set. Once its definition matches its anchor and commercial riders are added, it is hire-grade for a 0 to 3 year candidate.

#### What are the counts?

- Rejections: 21 (findings 1 to 21).
- Shallow parts: 8 (findings 22 to 29). Finding 22 is the single addition that matters most.
- Facts needing a source or a correction: 7 of the 10 checked (findings 31, 32, 34, 35, 36, 37 and 39). Findings 30, 33 and 38 hold; the misreading in finding 30 is counted under finding 7.
- Missing follow-ups: 3 (findings 40 to 42).
- Guesstimate findings: 6 (findings 43 to 48).

---

## Read 2, again: what does a fresh interviewer make of the revised material?

A third agent, on the Opus model, read the interview material after the fix pass, frozen at commit 478a643, with the same brief and no sight of the earlier reads. Its report is kept below as it was returned; what the last round changed for it is in the final section.

### How would a hiring interviewer judge Friday's interview material?

Snapshot read: `/tmp/claude-0/-home-user-c2-content-factory/03a440af-2d67-5a4f-b57a-4df77f69f80c/scratchpad/coldread2/content/W04/D5`. File names below are relative to it. Nothing in the repository or the snapshot was edited.

#### What did I read, and how did I check it?

I read all eight items in the brief:

- the transcripts
- the scorecards
- half2 S6 to S10
- the notes' interview section and the chapters it draws on
- cheat sheet panel 7
- the guesstimate card with S9
- fallback S10 to S13

I recomputed every case figure the answers quote from the four data files, using the rule definitions in `internal/C2_W04_D05_make_data_INTERNAL.py`. My scripts are `/tmp/claude-0/-home-user-c2-content-factory/03a440af-2d67-5a4f-b57a-4df77f69f80c/scratchpad/cr2check/recompute.py` and `extra.py`. Every quoted figure reproduced to the unit:

- the six hold-out MAEs
- the vendor's 1.4 percent fit and its 16,108 bias
- the priced costs, and the costs once each forecast is moved to its own 0.82 point
- the 2025 back-test
- the plan
- the peak-week range
- the 0.33 and 0.50 overtime shares
- the guesstimate arithmetic

I opened every outside source on 12 October 2026.

#### How do the answers score?

##### How does transcript 1's hire-grade answer score?

| Criterion | Mine | Programme | Agree? | The line that earns or loses it |
|---|---|---|---|---|
| Clarified the scope | 2 | 2 | Yes | Four clarifiers, each tied to what it sets: the ten-week reach, Rs 25 and Rs 5.42, Diwali's move, and "Has any of the three been scored on weeks it never saw?" |
| Named the hidden weeks and the unit | 2 | 2 | Yes | "I hold out the latest thirteen weeks, 29 June to 21 September 2026 ... from one origin, 22 June", with MAE in shipments and the priced loss "fixed before anyone scores" |
| Saw the paradox | 2 | 2 | Yes | "though it fits its 91 past weeks within 1.4 percent" beside a 16,400 miss that is "almost all bias", and "the vendor's misses cost least ... only because it runs high" |
| Sized it with a unit | 2 | 2 | Yes | 9,831, 6,615 and 16,400 shipments a week; Rs 8.8 lakh against Rs 10.0 lakh |
| Said what would change their mind | 2 | 2 | Yes | The sale's distance from Diwali, a first sale week outside "5.9 percent below to 7.8 percent above", and overtime that absorbs a short week |
| Tied it to a decision and its cost | 2 | 2 | Yes | "the plan is festival-aligned plus 2.6 percent, and it covered 10 of the 13 hidden weeks" |
| Gave the structure before the number | 1 | 2 | No | The first words spoken are "I hold out the latest thirteen weeks, 29 June to 21 September 2026". The five-step structure sits under a heading the candidate never says aloud. |
| Total | 13 | 14 | | |

**Would I hire?** Yes, for an analyst or data-science seat at any of the four companies. The answer does what most 0 to 3 year candidates never reach; they usually stop at a time-ordered split and MAPE. It:

- tests only on weeks after a fixed origin, and sets the test's length from the decision's horizon
- puts the seasonal naive on the board
- prices misses by direction, and compares forecasts at their own 0.82 points
- checks coverage and admits the circularity
- back-tests the one festival and names censored demand

Two things would cost the candidate in the room. One is reciting thirty-odd figures (finding 4). The other is having no answer to "on these weeks, isn't your rule the copy of last year plus 4 percent?" (finding 5).

##### How does the AI-company variant score?

| Criterion | Mine | Programme | Agree? | The line that earns or loses it |
|---|---|---|---|---|
| Clarified the scope | 2 | 2 | Yes | Unit, latency target, lead time, what stretches within minutes, the cost each way, and whether anything like it has launched |
| Named the hidden weeks and the unit | 1 | 2 | No | "a method can be tested only on a launch it did not see" earns half. "1,500 tokens a request, prompt and answer together" lumps two kinds of token that load a GPU very differently, and no measure of the forecast's quality is named. |
| Saw the paradox | 1 | 2 | No | No fit-versus-forecast or cheap-miss paradox is stated. Keeping both days from launch and the weekday is a sound design point. The scorecard credits a line the answer never says (finding 2). |
| Sized it with a unit | 2 | 2 | Yes | "20,000 requests and 3 crore tokens a minute, about 5 lakh tokens a second", with the inputs labelled invented. It stops before machines (finding 26). |
| Said what would change their mind | 2 | 2 | Yes | "Waitlist sign-ups before launch and the first hour's tokens a second after it" |
| Tied it to a decision and its cost | 1 | 2 | No | "sits above the forecast when a timeout costs more than an idle GPU hour" compares a per-request cost with a per-machine-hour cost. Neither cost is sized, so the rule never yields a number (finding 8). |
| Gave the structure before the number | 2 | 2 | Yes | "Then four steps", each named before its content |
| Total | 11 | 14 | | |

**Would I hire?** A lean hire for an analytics or data-science seat at an AI startup. No hire for an inference or platform seat as written.

The shape is right: a ground-up size, the last launch as the baseline, an honest "untested", stretch capacity and leading indicators. But it never reaches a machine count or a priced decision. An infrastructure interviewer's first two questions have no answer on the page: prompt tokens or output tokens, and how many requests are open at once.

##### How does transcript 2's hire-grade answer score?

| Criterion | Mine | Programme | Agree? | The line that earns or loses it |
|---|---|---|---|---|
| Clarified the scope | 2 | 2 | Yes | "Plus 4 and plus 22 against which weeks of last year?" is the best clarifier in the pack |
| Named the hidden weeks and the unit | 2 | 2 | Yes | Thirteen hidden weeks in shipments, and 2025's festival back-tested from 22 September 2025 |
| Saw the paradox | 1 | 2 | No | It sees why finance ties and why the vendor's misses are cheap. It misses the one the sponsor will raise: the plan books more in total than the vendor's own curve (finding 25 has the figures), and no line answers "your plan is bigger than mine". |
| Sized it with a unit | 2 | 2 | Yes | 20,275 shifts with 3,719 at the peak; 3,082 shifts and Rs 20.0 lakh over finance's rule; 3,413 to 3,906 shifts at the peak week's extremes |
| Said what would change their mind | 2 | 2 | Yes | "I would ask the vendor to forecast 2025's festival from data to September 2025, which can be done before Friday" |
| Tied it to a decision and its cost | 2 | 2 | Yes | The peak week priced at both ends (Rs 2.0 lakh idle or Rs 5.6 lakh late), plus the cost to finance |
| Gave the structure before the number | 2 | 2 | Yes | It opens on the restate and the headline "Neither goes to the plan as it stands" before any figure |
| Total | 13 | 14 | | |

**Would I hire?** Yes. The candidate:

- refuses the midpoint and answers from out-of-sample evidence
- concedes the true part of each side
- prices the plan's cost to finance and its range at the peak
- proposes a test the vendor can run before the deadline
- briefs both stakeholders before the meeting

That is senior behaviour at 0 to 3 years. The lost point is the sponsor's best reply, which the answer cannot meet (finding 25).

##### Do the scorecards hold up against the transcripts?

1. **trainer/C2_W04_D05_interview_scorecards_TRAINER.md, [S] table, "Gave the structure before the number".** The line "Measures, test set and origin, the baselines, ... in that order" does not match the answer table, which gives the test before the measure. That order holds only for the structure list, which the candidate never says aloud.
2. **Same file, AI table, "Saw the paradox".** "The last launch's curve looks like a forecast but cannot be tested on itself" is the scorer's paraphrase and appears nowhere in the variant. That breaks the page's own rule: "Every hire-grade 2 below rests on a line the answer says."
3. **Same file, "Why thirteen weeks?".** Citing FPP3's "about a fifth of the sample" invites the reply "a fifth of 104 is about 21, so why 13?". The real reason, that the vendor's file holds one origin, should come first.

#### What would a strong interviewer reject or mark down?

##### Which lines would sound memorised?

4. **extras/C2_W04_D05_interview_transcripts_STUDENT.md, all six rows of transcript 1's hire-grade column, and transcript 2's "Answer" row.** The [S] answer carries about thirty-five figures, and the [D] answer row carries eight in one breath. The page's own advice rules this out: "Carry four numbers into a real screen ... A string of exact figures sounds rehearsed." Delivered as written, I would start probing for memorisation by the third row.

##### Which claims overreach?

5. **Transcripts, [S] rows "The bar to beat" and "The price".** "Festival-aligned and finance's rule beat it at 6,615", and the "fair comparison" sets festival-aligned against the vendor only. On the hidden weeks, festival-aligned is the seasonal naive times 1.04, so the whole MAE gap is the growth term. Moved to its own 0.82 point, the seasonal naive also costs Rs 8.8 lakh (882,420 against 882,269 in `internal/C2_W04_D05_facts_INTERNAL.yaml`). The trainer page says "only the festival separates them"; the student page never does.
6. **Transcripts, pain-point row "A close fit taken for a good forecast".** The row says the paper "found eight machine-learning methods beaten by eight statistical ones at every horizon it examined". The paper compared eight statistical methods with ten machine-learning ones (eight plus RNN and LSTM), and its finding is about the two groups. It says the MLP's sMAPE was "only 0.19% more accurate than Naive 2", which is one of the eight statistical methods. The notes' wording ("statistical methods beat machine learning at every horizon tested") is the accurate one.
7. **Transcripts, last sentence of the Zillow follow-up; half2 S7 "Follow-up 3"; notes interview row 4.** "The price forecast's error at a six-month horizon was wider than the whole band" is the candidate's inference. The letter gives no error at any horizon; it says forecasts "three to six months into the future" missed "by much more than we modeled as possible". S7 and the notes shorten this to "price forecasts six months out" and "the margin swung about 12", with the unit gone. Keep "three to six months", "12 percentage points" and "which suggests".

##### Which methods or terms are wrong or stated loosely?

8. **Transcripts, AI variant step 3, and half2 S8 notes.** The notes ask the room "which cost is the Rs 25 and which the Rs 5.42 here: a timeout and an idle GPU hour". Rs 25 and Rs 5.42 are both per shipment, so the AI pair must also be per unit of demand: the cost of one timed-out request against the idle capacity one request would have used. As written, the comparison uses unlike units and can point the plan the wrong way. The same step's "the target sets the headroom within a minute" also reads unclearly.
9. **Transcripts, AI variant step 1.** "10 percent of them sending a request in the peak minute" is labelled invented, but it implies heavy use. If the peak minute runs three to ten times the average minute, each user averages about 14 to 48 requests a day. A sharp interviewer will ask where one user in ten in a single minute comes from, so the candidate should run that check on the placeholder.
10. **Transcripts, follow-up "MAE in shipments or MAPE"; half2 S7 "Follow-up 1"; notes row 2.** The answer says MASE is "scaled by the naive's average miss in training". FPP3 section 5.8 scales a seasonal series by the in-sample seasonal naive instead. For weekly data with a yearly cycle, the candidate should name which scale they mean.
11. **Same three places, on MAPE.** "Punishes a forecast that lands above the actual harder than one below" is FPP3's own sentence and survives. "Which here would tilt the pick" is never checked. On these thirteen weeks no actual is near zero, and MAPE ranks the rules exactly as MAE does (in my recomputation: festival-aligned 3.05 percent, seasonal naive 4.49, drift 6.80, naive 6.82, vendor 7.47). The stronger line is "here it changes nothing; at a store with near-zero days it would".
12. **study-notes/C2_W04_D05_notes_STUDENT.md ("The **error bar**, how wrong the forecast could be, is its average miss" and the words table); half2 S1; cheat sheet panel 6.** An error bar is an interval; MAE is the typical miss, and 5 of the 13 hidden weeks missed by more than 6,615. Pricing it as "Rs 35,800 if it runs high, Rs 1.65 lakh if low" treats the average miss as a band. Call it the typical miss, and keep transcript 2's lowest-to-highest range as the error bar.
13. **Transcripts, words table ("kept out of every rule and used only to score"); notes ("1.04 is the growth two years show"); transcript 2's concession ("your 4 percent is the growth two years show").** The thirteen hidden weeks also set the 2.6 percent cushion, and the two years of growth include them. Training weeks alone give 3.96 percent (`growth_train` in the facts file), which rounds to the same 4, so the scores stand. The candidate should still say so before an interviewer asks whether the test saw the future.
14. **slides/C2_W04_D05_half2_STUDENT.md, S10.** The handoff line promises a model judged "above the festival-aligned baseline on the thirteen held-out weeks". The table's last row on the same slide says those weeks "have already picked the rule and set the cushion". The table row is right; the handoff line should point at the rolling origin.

##### Do any numbers fail to follow from the data?

No case figure fails; everything quoted reproduces to the unit. One figure sits awkwardly beside the case:

15. **Transcripts, follow-up "The festival moves by three weeks this year. What breaks?".** The case's own move is two weeks: Diwali's week in 2026 comes 54 weeks after 2025's. A candidate who carries "three weeks off" back to the case says something false. One line marking the follow-up as hypothetical prevents it.

##### Are any follow-ups answered evasively?

None outright. The circularity reply opens with "A little, and for every forecast alike", which softens before it concedes. The rest of the line (4.1 against 2.6 percent, then a rolling origin) carries it.

##### Are the weak answers straw men?

16. **Transcripts, both "Weak answer" columns (scored 1 and 0 of 14).** The random 80 to 20 split and "whichever comes out lowest" are real junior errors, so each cell is credible. But the column fails every row. The answer most real candidates give is missing: a time-ordered hold-out, MAPE, pick the lowest, with no cost asymmetry and no festival check. That is where a hire decision is actually made, and showing it with a score of about 6 would teach more.

#### Where does a hire-grade answer stop short?

17. **Transcript 1. This is the single addition that matters most, here and across all three answers.** The candidate should say: "On these weeks festival-aligned is the seasonal naive plus 4 percent, and at each one's own 0.82 point they cost the same Rs 8.8 lakh. So the hidden weeks rule out the vendor and cannot rank my rule above the copy of last year. The 2025 back-test does that, on one festival, so I would roll the origin through it before trusting the festive error." That closes the gap between what the hold-out shows and what the plan claims.
18. **Transcript 1, "The test" row: no error by horizon.** The plan books 12 October from data ending 21 September, so horizons 3 to 10 are the ones that matter. Over those weeks, festival-aligned misses by 5,842, the seasonal naive by 9,838 and the vendor by 15,150. The vendor's miss climbs from 1.8 percent at one week ahead to 14.7 percent at thirteen.
19. **Transcript 1, structure step 2 and the circularity follow-up.** The rolling origin is named as the cure but never run. The copies can be forecast from every week since 29 September 2025, as the trainer page admits; only the vendor is limited to one origin.
20. **Transcript 1, clarifier 2 and "The measure" row.** The 0.82 share assumes a late shipment is still packed later, so Rs 25 is pure penalty. If a short week loses the order, the shift cost is saved and the share becomes (25 minus 5.42) over 25, about 0.78. One clause stating the assumption closes the follow-up.
21. **Transcript 1, the overtime follow-up.** It is answered as a condition, though the candidate's own file shows overtime carried the 2025 peak: 1,638 overtime shifts on a roster of about 1,847, and in every week the shifts worked equal shipments over 120, rounded up. A strong answer leads with what the data shows, then asks for the overtime rate and any orders that missed dispatch before keeping Rs 25.
22. **Transcripts 1 and 2: carry-over is never mentioned.** A short festive week pushes work into the next week, which is still heavy (383,760 forecast for 26 October, after 434,928). A one-week newsvendor prices each week as if it stood alone.
23. **Transcript 2, "The error" row, and transcript 1's trigger band.** The lowest-to-highest range of thirteen misses would cover a new week about 12 times in 14 if the misses were independent draws. Misses from one origin are correlated, so the band is looser than it looks. "Roughly an 85 percent band, and narrower than the truth" is the honest framing.
24. **Transcript 1, "What would change it" row.** The trigger (a first sale week outside the range) comes with no lever. It should say which weeks' shifts can still change after 12 October, and at what lead time.
25. **Transcript 2: the single addition that matters most for this answer is the volume concession.** Over the eight weeks the plan books 2,432,319 shipments, 22.6 percent above last year's same calendar weeks and 12,819 more than the vendor's curve (20,275 shifts against about 20,165). The line to add: "Over the eight weeks your curve and our plan book within 1 percent of each other; we differ on which weeks. Yours books its biggest week on 5 October, and about 2.6 lakh shipments too few across 19 October to 2 November." That moves the dispute from how much to which weeks, which is the case the rest of the answer makes.
26. **AI variant: the single addition that matters most for this answer is turning tokens a second into machines.** Split prompt tokens from output tokens. Convert requests to concurrency: 20,000 a minute is about 333 a second, and at an assumed 10 seconds a reply that is about 3,300 open streams. Size GPUs from a load test at the latency target, and price both costs per request. Without that, the two-cost rule has nothing to act on.
27. **AI variant, step 3: staged rollout is missing.** Releasing to a share of users first, and raising it as the first hours come in, is the cheapest demand lever at launch. It belongs beside the waitlist and rate limits.
28. **Transcript 1, Zillow follow-up: the answer stops at the band.** The letter itself names the deeper lesson: conversion rose "as a result of unintentionally purchasing homes at higher prices than our current estimates of future selling prices". A forecast used to bid wins exactly where it overestimates, so the homes Zillow held carried its errors in one direction. That selection effect is the interview-grade point.
29. **Transcripts, pain-point row 1.** The PLOS ONE and M5 findings sit side by side without the reason they differ. PLOS used single monthly M3 series of 81 to 126 months. M5 had tens of thousands of related daily series with explanatory variables, which the M5 paper says LightGBM could "effectively process". "The data decides which family wins" is the line an interviewer wants.
30. **Notes interview row 1, and cheat sheet panel 7.** The one-line answer quotes 6,615 against 9,831 and stops. It leaves out that the hidden weeks hold no festival, which is the first follow-up anyone asks of a Diwali plan. Add "and I back-test the festival, since the hidden weeks hold none".

#### Which real-world facts check out, and which need a source or correction?

All sources were opened on 12 October 2026.

| # | Fact as stated | Where | Source and date on the page | Matches when opened? |
|---|---|---|---|---|
| 31 | Zillow: forecasts three to six months ahead; guardrail of plus or minus 200 basis points of breakeven; misses in both directions; about 1,200 basis points of swing from Q2 to an expected minus 500 to minus 700 in Q4 2021; more homes bought (9,680 in Q3); renovation capacity short; USD 304 million write-down; wind-down; about 25 percent of the workforce cut | Transcript 1 follow-up, pain points, fallback S10, half2 S7 | Q3 2021 shareholder letter, SEC link, checked date | Yes, every figure. Needs correction where S7 and the notes shorten the horizon and drop the unit (finding 7). |
| 32 | FPP3: test set about 20 percent of the sample, ideally at least as long as the horizon; MAPE undefined at zero and heavier on negative errors; MASE | Follow-up 1, scorecard | Sections 5.8 and 5.9, link, checked date | Yes. The source list should add section 5.10, where rolling origin lives (fallback S6 cites it correctly). MASE needs the seasonal scale (finding 10). |
| 33 | PLOS ONE 2018: 1,045 monthly series; best-fitting models "did not necessarily" forecast better; eight ML methods beaten by eight statistical ones | Pain point 1, notes | Link, checked date | The quote and series count match. The method count and the wording need correction (finding 6). |
| 34 | M5: all 50 top methods machine learning and ahead of every statistical benchmark; seasonal naive 0.847, naive 1.752, winner 0.520; 35.8 percent of teams beat the seasonal naive; 3,049 Walmart products | Pain point 1, notes | Preprint link, checked date | Yes. All top 50 beat the best benchmark (ES_bu) by more than 14 percent, and 1,972 teams (35.8 percent) beat the seasonal naive. The link is a preprint copy on a blog host; cite the journal version. |
| 35 | Target Canada: forecasting system needed years of history; optimistic projections from headquarters; item data accurate about 30 percent of the time; distribution centres overflowing while shelves sat bare; 133 stores; about 17,600 staff | Pain point 2, fallback S11 | Canadian Business (archived) and Target's release of 15 January 2015, checked date | Yes. The Canadian Business article carries no publication date and is cited through a third-party mirror; add its date. |
| 36 | FADA: 42-day festive window from the first day of Navratri; October 2025 two-wheeler retail 31,49,846; September 12,87,735; September's first 21 days almost quiet ahead of GST 2.0; GST cuts credited | Pain point 4, S9, notes, guesstimate card | Release of 7 November 2025, link, checked date | Yes. FADA defines the window as "1st day of Navratri to 15 days post Dhanteras due to time lag for vehicle registration", which supports the card's point that registrations lag sales. Its counts exclude Telangana and come from 1,400 of 1,458 RTOs, a footnote worth carrying. |
| 37 | Amazon Science (Larry Hardesty, 22 November 2019): the Prime Video model lost to a bestseller list, was retrained on time-ordered data, was tested on the two weeks after its cutoff, and beat both the list and item-to-item "two to one" | Pain point 5 | Link, author and date, checked date | Yes. "Deep-learning recommender" is a fair gloss of the article's autoencoder. |
| 38 | SIAM: 2,17,05,974 domestic two-wheeler sales in FY 2025-26, up 10.7 percent, makers' sales to dealers | S9, notes, guesstimate card | The card gives the link; S9 and the notes give only "checked 12 October 2026" | Yes (release dated 14 April 2026). S9 and the notes need the link or the release's name. |
| 39 | Diwali on Thursday 31 October 2024, Monday 20 October 2025 and Sunday 8 November 2026 | Notes opening | "DoPT's holiday lists, checked 12 October 2026", no link | Yes, all three, checked through reproductions of the DoPT orders. Needs a link. |
| 40 | "On 6 October 2026 Flipkart said Ekart ... had added 14 million cubic feet of warehousing ... and more than 2.5 lakh direct and indirect festive employment opportunities" | Notes, chapter 3 "IN THE FIELD" | Date only, no source | The figures match; the date does not. The 14 million cubic feet came in a statement of 29 September, reported on 30 September 2026 (Business Today, Maritime Gateway). The 2.5 lakh roles appear in coverage dated 15 and 16 September 2026 (UNI, Outlook Business, seen through search results). I found no 6 October release. Correct the date and add the source. |
| 41 | Not on any page: The Big Billion Days 2026 opened on 9 October 2026 (Business Today, 30 September 2026) | Bears on the whole case | None | The real sale opened in the week of 5 October, four weeks before Diwali's week; the synthetic calendar puts the sale in the weeks of 12 and 19 October. The case is labelled synthetic, so nothing on the page is wrong. A Flipkart interviewer will still know the date, so the candidate should have it ready alongside the line "a sale that opens a different distance before Diwali moves the peak". |

#### How good is the two-wheeler guesstimate?

42. **trainer/C2_W04_D05_guesstimate_TRAINER.md, structure: strong.** The Clarify step separates buyers from dealer dispatches and says why the two differ only by dealer stock over a year. The Map step names the logic: the household fleet divided by the replacement cycle. The one-at-a-time sensitivity names the two inputs worth arguing about. That is better than most guesstimates I hear.
43. **Same table, "Assume, with ranges": the weak input is "first-time and commercial buyers add 15 percent".** Thirty crore households, half owning one, and an eight-year cycle are defensible. But the model assumes a steady state, and SIAM's own release says FY 2025-26 set a record above the FY 2018-19 peak, with the second half up about 21.5 percent. The fleet is growing, so first-time demand is no small add-on. The close match comes partly from offsetting errors, which the card's "luck as much as method" half-admits.
44. **Same table, "Calculate", with S9 and the notes: no page states the output range.** The swings are right: minus 20 to plus 33 percent for the replacement years, 20 percent either way for ownership, about 7 for households and about 4 for first-time buyers. The facts file holds 1.2 to 3.8 crore with every input at an extreme. S9's title and the notes give "about 2.2 crore" alone, which is the "Gives one number with no range" wrong turn the card's own table names.
45. **Same table, "Validate".** The anchor matches SIAM exactly, but in a real screen nobody has SIAM's figure to hand. The candidate's own check should be a second route, such as a large maker's yearly volume divided by its market share, and the card teaches none. Its "Calls a match with SIAM proof" row is a good guard.
46. **Same table, "The catch", and S9: good, and correctly caveated on the card.** The card's caveats are a festive month, September's deferred buying, registrations lagging sales, and a month of registrations set against a year of dispatches. S9 and the notes drop the last caveat and say "74 percent above the year" and "74 percent too high". The like-for-like check sets October's annualised registrations against FADA's own full-year retail count.

#### What are the counts?

- **Rejections or mark-downs:** 13 (findings 4 to 16). None is a case number that fails the data, and no follow-up is evasive.
- **Shallow parts:** 14 (findings 17 to 30). The single addition that matters most is finding 17.
- **Facts needing a source or correction:** 8 of the 11 checked (findings 31, 32, 33, 34, 35, 38, 39 and 40). Finding 41 is a real-world date the case should be ready for.
- **Scorecard notes:** 3 (findings 1 to 3).
- **Guesstimate mark-downs:** 3 (findings 43 to 45).

---

## What did the fix pass change for each finding?

Each row says what the pack does now. A separate agent audited Read 1's findings against the pack
after the first round of fixes, and the rows below take its evidence plus the later fixes. "Partly"
and "Kept" rows have their one-line reason in `internal/C2_W04_D05_sources_INTERNAL.md`.

### Read 1, the fresh graduate

| # | Status | What the pack does now |
|---|---|---|
| 1 | Fixed | S1 and notebooks 01 to 03 say "eighteen percentage points apart"; the preview says "18 percentage points apart". |
| 2 | Fixed | S1 expands FC and defines a packer-shift on screen. |
| 3 | Fixed | S1 defines the window as the eight weeks to staff, against the same weeks last year. |
| 4 | Fixed | S1 defines the vendor file's three kinds of row; S16 defines hidden weeks, hold-out, test set, training weeks and origin on the slide that first shows them. |
| 5 | Fixed | Notebook 01 opens the calendar and prints the sale weeks; notebook 03 reads the costs table. |
| 6 | Partly | S1's multipliers are gone, S19's picture no longer shows the vendor and S28's option a no longer argues for itself; S18's option d still names the tie. |
| 7 | Partly | Every page now says the calendar copies put the peak on 5 October, before the plan's first week; why the window opens on 12 October stays with the ticket. |
| 8 | Fixed | S2 is one chain of days ending in the Kalpa lab and Saturday, with a caption saying what each node carries. |
| 9 | Fixed | The notes show 6,615 x Rs 650 / 120 and 6,615 x Rs 25; every page prints about Rs 35,800. |
| 10 | Fixed | S3 defines the error bar as the forecast's average miss on unseen weeks; "error band" is gone; every page prices it at the forecast. |
| 11 | Fixed | S7 and its picture use FPP3's terms (a season has a fixed period, a cycle does not); the chapter 1 set and its solution say "repeat". |
| 12 | Fixed | S8 works drift on the canteen (about 51.3); notebook 01 works it on the series. |
| 13 | Fixed | Notebook 02 says which 39 weeks the growth compares; S8's table says the 4 percent is the growth the two years show. |
| 14 | Fixed | S8 and notebook 01 tie "house bot" to "seasonal copy"; "same-period copy" and "house rule" are gone; the transcripts add the field's word, "seasonal naive", in a word table. |
| 15 | Fixed | No F or T tag remains on a learner page. |
| 16 | Fixed | Ekart, The Big Billion Days, FADA, SIAM and GST are expanded where they first appear. |
| 17 | Fixed | S14 and the notes say what M5 is, that its seasonal copy is the same weekday a week earlier, which measure scored it, and that 35.8 percent of teams beat it. |
| 18 | Fixed | S1 and S15 show Rs 650 / 120 before Rs 5.42 is used. |
| 19 | Fixed | "A spare shipment, planned for and never shipped" from S1 on; "short" and "long" are gone from half two, the chapter 2 solution and the day sheet. |
| 20 | Fixed | S16 defines origin and the ten-week horizon on screen; S15, half two S6 and the transcripts say "one origin". |
| 21 | Fixed | S17 and notebook 02 expand MAPE. |
| 22 | Fixed | S8 and S19 state the stretch from five weeks before Diwali's week to four after. |
| 23 | Fixed | S20 calls 2 percent the sponsor's claim; S21 gives 1.4 percent as the worst fitted week. |
| 24 | Fixed | The scoreboard picture labels its totals over 13 weeks and its rupee axis. |
| 25 | Fixed | Notebook 02 prints both figures; every page says weeks 1 to 6 and 8 to 13; the cell's halves follow the test's length. |
| 26 | Fixed | S25 points to notebook 02's printed misses, which add to 85,996. |
| 27 | Fixed | One wording everywhere, checked against the paper, with M5's reversal beside it. |
| 28 | Fixed | S30 names the eight weeks; notebook 03 prints the late part, Rs 69.6 lakh. |
| 29 | Fixed | Notebook 03 runs festival-aligned with no growth (10,575); S30 and the transcripts quote both figures. |
| 30 | Fixed | S30 defines a back-test on screen. |
| 31 | Fixed | "Level" means a difficulty grade only; the plan's height is the cushion, and "the same" replaces the other use. |
| 32 | Fixed | The 100-week derivation sits on S32, in notebook 03 after a predict step, in the notes and on cheat sheet panel 6. |
| 33 | Fixed | New S33 and the cushion strip sort the thirteen misses; notebook 03 prints them and reads the 0.82 point between the 10th and 11th. |
| 34 | Fixed | The cost curve has plain labels; notebook 03 says how it is drawn and what its two terms are. |
| 35 | Fixed | S35 says the table is a scenario resting on the back-test's placement. |
| 36 | Fixed | S36 and the notes' table give what the pack has and what would settle each doubt. |
| 37 | Fixed | Notebook 03 prints 1,638 and 5 with their weeks. |
| 38 | Fixed | Learner pages print lakh and crore with decimals; exact Indian-grouped figures stay in TRAINER files. |
| 39 | Fixed | S37 says "cover demand in 0.82 of weeks"; S1 introduces the vendor's sponsor. |
| 40 | Fixed | The festival calendar labels each year's boxes by that year's own Monday. |
| 41 | Fixed | The baselines panel and the axes are relabelled. |
| 42 | Fixed | Notebook 01 explains the 51 weeks; notebook 01 and S12 give the 54. |
| 43 | Fixed | Notebook 01's cells use commented loops; the date line says what it prints. |
| 44 | Fixed | Notebook 02 explains `shift(52)`, `h` and the measured growth. |
| 45 | Fixed | Notebooks 02 and 03 use plain loops and 100_000; notebook 04 says what 1e5 and 1e7 are at first use. |
| 46 | Fixed | Kalpa's vendor file labels its hidden months `holdout`; notebook 04 says what the column shows. |
| 47 | Fixed | "Nobody chose how high it runs" replaces "lean" and "bias". |
| 48 | Fixed | Notebook 03 builds the source map in a commented loop, defines only `check`, and drops `min(key=)`. |
| 49 | Fixed | Notebook 03 names the reversed measure `above` and says so. |
| 50 | Fixed | Notebook 03 gives words for `quantile`, the grid, the two `max` terms and the averaging. |
| 51 | Fixed | Inference is defined; "median" is gone. |
| 52 | Fixed | Every set names its thread in the cohort channel. |
| 53 | Fixed | The guided set explains the levels, a screen and a GCC; fallback S13 explains [D]. |
| 54 | Fixed | Guided Q2 names the origin week and what hiding stops. |
| 55 | Fixed | Chapter 2 Q1 explains `shift(1)`. |
| 56 | Fixed | The set defines "enough" by packer-shifts; team A now beats the bot by 31 shipments a week, which changes no shift, and the solution says why C has earned the ordinary weeks only. |
| 57 | Fixed | RMSE, R-squared, overfitted, the newsvendor rule, baseline, autocorrelation, smoothing and ARIMA are each glossed where they first appear. |
| 58 | Fixed | Basis points, breakeven, unit economics and the write-down are explained, and the reading is corrected against Zillow's letter. |
| 59 | Fixed | Half two S11 gives item 7 forty seconds. |
| 60 | Fixed | The staffing note, S6 and notebook 01 say the sale runs in the third and second weeks before Diwali's week. |
| 61 | Fixed | S13 gives no date; the real sale date stays off learner pages. |
| 62 | Fixed | Notebook 03 prints 60,488 and Rs 8.8 lakh. |
| 63 | Fixed | Transcript 2 says the vendor's file holds no forecast of any festival. |
| 64 | Fixed | S26, notebook 02 and the notes teach "good enough" as a claim about the decision. |
| 65 | Fixed | Notebook 04 says "data warehouse". |
| 66 | Fixed | Notebook 04 explains the 17. |
| 67 | Fixed | Notebook 04's typed cell uses spelled-out month lists. |
| 68 | Fixed | The typed table has a finance column; notebook 04 says why 4 percent stands beside the measured 3.7. |
| 69 | Fixed | Notebook 04 and the board set explain that revenue is booked in Diwali's own month. |
| 70 | Fixed | Board Q1 asks for the vendor comparison only. |
| 71 | Fixed | Board Q3's key is festival-aligned's own miss, Rs 3.5 lakh a month, which notebook 04 prints. |
| 72 | Fixed | Notebook 04 explains the tall Aprils and Julys. |
| 73 | Fixed | Notebook 04's predict step has options; its last cells print and name the error bar. |
| 74 | Fixed | Practice Q2's stem asks for festival-aligned only. |
| 75 | Fixed | The brief changes one line; notebook 02 counts the hidden weeks itself, and the one FAIL is announced. |
| 76 | Fixed | The notes key every symbol; cheat sheet panel 3 has a key. |
| 77 | Partly | The notes say what rolling the origin does and why the morning used one origin; the worked example stays in the fallback. |
| 78 | Fixed | The notes place the last-frame still and give both weeks' numbers. |
| 79 | Fixed | The notes separate the 9.5 percent from the 308,048. |
| 80 | Fixed | Notebook 03 and S34 print the 19,760. |
| 81 | Partly | The notes give the explorer's path; the file lives on branch `w04-explorer` until it merges. |
| 82 | Partly | The glossary adds origin and horizon, back-test, MAE and MAPE, error bar and plan share; drift and fit are defined where they first appear, and the notes do not use "quantile"; the glossary stays last. |
| 83 | Fixed | The self-check gives the copies' moves, 1,331 and 1,489; the fallback picture and S2 say which ranks hold. |
| 84 | Fixed | The self-check prints two places and says how the notebook rounds. |
| 85 | Fixed | The staffing solution calls the copied week Diwali 2025's own week. |
| 86 | Fixed | The index counts 21 items, nine of them design calls, names the solution files, and the transcripts carry the L6 label. |
| 87 | Partly | The brief says what to do if the fallback ran; the fallback still shows the four-week numbers. |
| 88 | Fixed | Fallback S8's option b matches S9's answer. |

| Sentence read three times | Status | What the pack says now |
|---|---|---|
| half1 S17, "A percentage error would hide..." | Fixed | MAPE is defined and the peak-week comparison worked. |
| half1 S30, "Rs 69.6 lakh of it late shipments..." | Fixed | "where the rush came before the copy expected it". |
| half1 S32, "Festival-aligned's hidden-week misses..." | Fixed | Moved to S33 and rewritten around the sorted thirteen. |
| half2 S2 card 3 | Fixed | "The miss a week in shipments, its cost if high and if low, and the rule's record on 2025's festival." |
| Notebook 03, "One spike a year..." | Fixed | "Two years hold only two festivals". |
| Notebook 03, "A vendor model with no Lucknow festival..." | Fixed | "an untested assumption". |
| Notebook 04, "the festival-aligned copy moves..." | Fixed | "swaps two months", each named. |
| Transcripts, Zillow | Fixed | Rewritten against the letter. |
| Transcript 2, "Raised by 2.6 percent..." | Fixed | Replaced by the comparison at each forecast's own 0.82 point. |
| Take-home, "never looked at the origin" | Fixed | "the rules that never use the origin week, the copies of last year". |
| Notes, "two weeks before the real one" | Fixed | "books the most packers two weeks before the real rush". |
| Notes, CALLBACK | Fixed | "today forecasts weeks not yet seen". |
| Notes, "Rolling the origin..." | Fixed | Says what is rolled and why the morning used one origin. |
| Same-week solution, "each calendar copy carried a week..." | Fixed | "one step earlier in the 2024 festival, nearer its peak". |

Read 1 totals: 82 fixed and 6 partly fixed of 88 findings; all 14 sentences fixed.

### Read 2, the hiring interviewer

| # | Status | What the pack does now |
|---|---|---|
| 1 | Fixed | Every page names the ten-week horizon, 21 September to the week of 30 November: S16, fallback S5, the transcripts, notes, cheat sheet, Kahoot Q5, the self-check, notebook 02, the day sheet and the scorecards. |
| 2 | Fixed | Two measures are fixed together before scoring: MAE in shipments and the misses priced by direction, named as the quantile loss at 0.82 (FPP3 5.9). |
| 3 | Fixed | Each forecast is compared at its own 0.82 point (Rs 8.8 lakh against the vendor's Rs 10.0 lakh); the 4.1 percent reading is named; the cost curve is shown flat from 2 to 4 percent; a rolling origin is named as the cure. |
| 4 | Fixed | Both transcripts and the scorecard give 4,034 with the growth and 10,575 without it, and the festive coverage, 7 of 8 against 2 of 8. |
| 5 | Fixed | Transcript 2 gives the peak week's range in shifts, 3,413 to 3,906 against 3,719 booked, priced at its ends; everywhere else the error bar is the forecast's average miss, priced at the forecast. |
| 6 | Fixed | The MAPE follow-up names MASE and WAPE and MAPE's heavier penalty on forecasts that land high. |
| 7 | Fixed | Zillow is retold from the letter: a margin guardrail, price forecasts that missed by more than modelled, the purchases and renovation capacity, the write-down and the wind-down. |
| 8 | Fixed | The PLOS ONE row keeps "did not necessarily" and adds M5's reversal. |
| 9 | Fixed | The Amazon row tells the whole story, with the retrained recommender's win. |
| 10 | Fixed | The forecasting clause is sourced to Canadian Business, with the item-data accuracy and the stock failure; the check moved to sizing from the ground up. |
| 11 | Fixed | The AI variant keeps days from launch and the day of the week. |
| 12 | Fixed | The variant sizes in tokens a second to a latency target with headroom; the two-cost share applies to capacity booked ahead. |
| 13 | Fixed | The variant says a method is untested with one earlier launch or none. |
| 14 | Fixed | The averaging follow-up says when combining helps and why it fails here, from the observed peak week only. |
| 15 | Fixed | The scorecard names the vendor's single-origin file as the real limit. |
| 16 | Fixed | The third-year line is gone; the notes say the copies could roll through 2025's festival. |
| 17 | Partly | The handoff line stays as the spine wrote it; S10's table adds that a new model is fairest judged on weeks no choice has used. |
| 18 | Fixed | Fallback S13 concedes the vendor's tilt to the cheap side. |
| 19 | Fixed | The weak answers are a random split scored by RMSE or MAPE with the vendor taken on its fit, and "go with the vendor, trimmed to plus 13"; the scorecard states its unit rule and rescores them. |
| 20 | Fixed | A word table maps the class's words to the field's; the scorer section says to carry four numbers; the intro says to name the exercise as synthetic. |
| 21 | Fixed | A 2 now requires surviving the technical follow-up, inside the spine's seven criteria. |
| 22 | Partly | Rolling the origin is in the structure, a follow-up, the notes and the scorecard; no rolling results are quoted. |
| 23 | Fixed | Coverage is quoted, 10 of 13 with its caveat and 7 of 8 on 2025's festival. |
| 24 | Fixed | "What the test cannot see" names the 1,638 of 3,485 overtime shifts and the capped peak. |
| 25 | Partly | Overtime is a follow-up with the 0.33 and 0.50 shares; routing, backlog, day-level planning and new hires' pace are not added. |
| 26 | Fixed | The vendor's bias, 16,108 a week against an MAE of 16,400, is in transcript 1 and the scorecard. |
| 27 | Fixed | Transcript 2 gives finance 3,082 shifts, about Rs 20.0 lakh, and an in-season trigger. |
| 28 | Fixed | Transcript 2 has a row for the people. |
| 29 | Fixed | The variant works 2 lakh users, 10 percent and 1,500 tokens (invented) into about 5 lakh tokens a second. |
| 30 | Fixed | The transcripts list the letter's link with its check date. |
| 31 | Fixed | S26 names Naive 2 and the one-step-ahead comparison; the paper's link is listed. |
| 32 | Fixed | The forecasting clause cites Canadian Business on every page that uses it. |
| 33 | No change | The FADA figures held. |
| 34 | Fixed | The Amazon row gives author and date. |
| 35 | Fixed | S14 and the notes say M5's seasonal copy is the same weekday a week earlier. |
| 36 | Fixed | The guesstimate and S9 say SIAM counts makers' sales to dealers. |
| 37 | Partly | "Direct and indirect employment opportunities" replaces "jobs"; the real sale date stays off learner pages. |
| 38 | No change | The FPP3 wording held. |
| 39 | Partly | The notes cite DoPT's holiday lists; the links stay the staffnews.in copies. |
| 40 | Fixed | Transcript 1 has the overtime follow-up. |
| 41 | Partly | A moving sale is answered as a hypothetical; the real date is not used. |
| 42 | Fixed | The variant and the Target row cover a first launch. |
| 43 | No change | The structure held. |
| 44 | Fixed | The clarify and validate lines match SIAM's definition. |
| 45 | Fixed | Commercial riders are in the map and the 15 percent; the cycle is the years a household keeps one before buying new. |
| 46 | Fixed | The card swings one input at a time. |
| 47 | Fixed | The estimate is about 2.2 crore. |
| 48 | Fixed | The catch names September's quiet weeks and registrations against dispatches. |

Read 2 totals: 39 fixed, 6 partly fixed and 3 needing no change, of 48 findings.

### Read 2, again: the fresh interviewer, after the fix pass

| # | Status | What the pack does now |
|---|---|---|
| 1 | Fixed | Transcript 1 opens on a "Said first" row naming the five steps; the scorecard cites it. |
| 2 | Fixed | The variant now says "That curve looks like a forecast, and it is not one until it has predicted a launch it never saw"; the scorecard quotes it. |
| 3 | Fixed | The scorecard's reply leads with the vendor's single-origin file. |
| 4 | Fixed | Transcript 1's rows carry about twenty figures instead of thirty-five, and transcript 2's answer row five instead of eight. |
| 5 | Fixed | The bar and price rows say festival-aligned is the seasonal naive plus 4 percent on these weeks and that both cost Rs 8.8 lakh at their own 0.82 points. |
| 6 | Fixed | The PLOS ONE row states the finding for the two groups, with no method count. |
| 7 | Fixed | The Zillow line is framed as inference ("which suggests"); S7 and the notes keep "three to six months" and "12 percentage points". |
| 8 | Fixed | The variant's two costs are per unit of demand: a timed-out request against the idle capacity one request would use; S8's notes match. |
| 9 | Fixed | The placeholder is 1 percent in the peak minute, checked at about 3 requests a user a day. |
| 10 | Fixed | MASE is scaled by the seasonal naive's training miss. |
| 11 | Fixed | The MAPE line says it ranks the rules as MAE does on these weeks. |
| 12 | Fixed | The error bar is called the typical miss everywhere it is defined, with 5 of 13 weeks missing by more; the range is the answer to "how wrong could it be". |
| 13 | Fixed | The concession and the notes say the training weeks show the 4 percent; the word table says the hidden weeks also set the cushion. |
| 14 | Kept | The handoff line stays as the spine wrote it; S10's table carries the caution. |
| 15 | Fixed | The three-week follow-up notes the case's own move is two weeks. |
| 16 | Fixed | A typical answer sits between the columns, scored 3 of 14 on the card. |
| 17 | Fixed | Transcript 1's price row carries the concession and what only the back-test can rank. |
| 18 | Kept | Error by weeks ahead is not quoted. |
| 19 | Kept | The rolling origin is named, not run. |
| 20 | Kept | The lost-order case is not added. |
| 21 | Fixed | The overtime follow-up leads with what the data show. |
| 22 | Kept | Carry-over between weeks is not added. |
| 23 | Fixed | Transcript 2 says the range covers roughly six weeks in seven and that one origin's misses move together. |
| 24 | Kept | The trigger names no lever. |
| 25 | Fixed | Transcript 2 concedes the totals sit within 1 percent, 12,819 shipments apart, and moves the dispute to which weeks (291,183 more across 19 October to 2 November). |
| 26 | Fixed | The variant splits prompt and answer tokens and turns requests into about 330 open at once, then machines by load test. |
| 27 | Fixed | A staged rollout joins the stretch options. |
| 28 | Fixed | The Zillow line adds the selection effect with the letter's words. |
| 29 | Fixed | The PLOS ONE row says why the two findings differ: single monthly series against tens of thousands of related daily ones. |
| 30 | Fixed | The notes' and cheat sheet's one-line answers add the festival back-test. |
| 31 | Fixed | See 7. |
| 32 | Fixed | The transcripts' sources add sections 5.9 and 5.10. |
| 33 | Fixed | See 6. |
| 34 | Kept | The M5 paper stays cited as the preprint that was opened. |
| 35 | Kept | The Canadian Business article stays undated. |
| 36 | No change | The FADA figures held; the footnote is not carried. |
| 37 | No change | The Amazon row held. |
| 38 | Partly | S9's notes link SIAM's release; the notes keep its name and check date. |
| 39 | Kept | The notes name DoPT's lists without a link. |
| 40 | No change | The announcement's own page metadata gives 6 October 2026; the notes now name it. |
| 41 | Kept | The real sale date stays off learner pages. |
| 42 | No change | The structure held. |
| 43 | Fixed | The card says the market grew 10.7 percent, so part of the match is errors that cancel. |
| 44 | Fixed | S9, the notes, the card and the day sheet give the range, about 1.7 to 2.9 crore. |
| 45 | Kept | No second validation route is added. |
| 46 | Fixed | S9 sets a month of registrations against a year of dealer sales; the notes say "above SIAM's year". |

Read 2, again, totals: 30 fixed, 1 partly fixed, 11 kept with a reason and 4 needing no change, of 46 findings.

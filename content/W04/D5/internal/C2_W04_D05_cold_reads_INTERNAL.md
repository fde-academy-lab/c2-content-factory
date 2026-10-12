# W04 D5 cold reads: what a fresh graduate and a hiring interviewer could not accept

**INTERNAL.** Two cold reads of the Friday pack, each by a separate agent on the Opus model, each
given the pack frozen at commit 65d645b and told to write findings only and never edit. The first
read as a 23-year-old fresh graduate who has never worked and has weak maths, every STUDENT file in
learner order. The second read as a hiring interviewer from Uber, Swiggy, Google and an AI startup,
the interview material and its scorecard. Both reports are kept below as they were returned. What
the fix pass changed for each finding is in the last section; a finding left as it is has its
one-line reason in `internal/C2_W04_D05_sources_INTERNAL.md`.

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

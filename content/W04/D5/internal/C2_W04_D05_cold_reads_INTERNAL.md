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

Pending: the second agent's report is pasted here when it returns.

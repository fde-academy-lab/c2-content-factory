# Cold reads, W04 D2: what a fresh graduate could not follow and what a hiring interviewer would reject

Two separate reviewers read the pack on 12 October 2026 and wrote findings only; neither edited a file. Read 1 read the STUDENT files in learner order; read 2 scored the transcripts' hire-grade answers on the S52 scorecard. Their findings are reproduced as written. What changed in answer, and the reason for each finding not fixed, are in `C2_W04_D02_sources_INTERNAL.md`.

---

## Read 1: the fresh graduate (23, no work experience, not strong in maths)

**How I read.** I read only the STUDENT files under `content/W04/D2/`, in the order I was given. Paths below are relative to that folder. For the two decks I judged what is on each slide; I read the `notes` fences only to know what I would have heard in class, and I say so wherever a slide leans on them. Notebook cells are counted from 1, markdown and code together, in the order they appear (cell 1 is the title, cell 2 loads the data). I answered every lettered item before opening its solution, and I looked at every picture the files name, plus the three figures saved in the notebook and the cheat-sheet PDF rendered at print size.

**My letters before the solutions.**

| Set | My letters | Key | Right? | What gave it away |
|---|---|---|---|---|
| guided/slide_and_estimate | dca | 1d 2c 3a | all | Q1: the only option carrying the claim's own "Rs 1.16 crore". Q2: the stem's "pays drivers for each peak hour online" is repeated in c. Q3: the row under the blank back-solves it (8,300 / blank x 1.15 = 5,700), and notebook cell 13 prints "1.68 ... (2.4 x 0.70)" first. |
| unguided/mid_cut_to_two | ca | 1c 2a | all | Q1: S9 and S10 already answered it. Q2: the stem's "what happens to the drivers who accept?" matches a's "still accept". |
| unguided/studio_brief | d | 1d | yes | S20's marketing row, nearly word for word. |
| unguided/mid_check_against | bcda | 1b 2c 3d 4a | all | Q1: S44 and notebook cell 13 print 802 million a day. Q2: the stem's words match c. Q4: S34. Q3 is the one I had to reason out, and I was unsure. |
| unguided/interview_rungs | bd | 1b 2d | both | Q1: the sentence repeated all day. Q2: I matched "leading input" from S51 without knowing what it means. |
| unguided/kalpa_store | cb | 1c 2b | both | Q1: Q2's option a prints "about Rs 146 crore a store". |

Fourteen of fourteen right, and twelve of the fourteen could be answered by matching words or reading the answer off another page (finding 38). After reading the solutions I could say why my answer was right for every item except interview_rungs Q2, where the solution also never says what a "leading input" is. My eight Kahoot answers matched the keys, which were printed in my copy (finding 60).

---

### The morning deck: slides/C2_W04_D02_half1_STUDENT.md

**1. CONFUSING. S1, table, lines 26 and 28.** "Gross bookings per peak online hour"; "Gross bookings per active driver-week". The first table on the first slide uses two terms the slide never explains. I heard in class (speaker notes) that gross bookings are what riders paid before Uber's share and any top-up, and that an active driver-week is one driver with a row that week, but the slide does not say it. The definitions sit in notebook cells 3 and 5 and in the guided exercise. Reading the deck on its own, I cannot read its first table.

**2. CONFUSING. "Top-up": S1 line 31 ("topup_rs"), S4 line 101, and S9, S10, S11, S22, S29.** "Top-up per trip becomes a guardrail". The word is on many slides and defined on none. The guarantee itself (Rs 300 for every peak hour online, with the gap paid as a top-up) first appears in `exercises/guided/C2_W04_D02_slide_and_estimate_STUDENT.md` lines 3 to 5, and even there "paying the gap above their trip earnings" took me two reads. Neither the notes' word table nor the cheat sheet's word list includes it.

**3. CONFUSING. S1 line 26 against S4 line 100 and the guided exercise line 4.** "Rs 314" an hour before the launch; "Rs 300 an hour, guaranteed". An hour online brought in Rs 314 before the launch, more than the Rs 300 guarantee, and Rs 260 after, only Rs 40 short of it. So I could not see how Rs 1.9 crore of top-up was paid (about Rs 130 for every one of the 1,46,300 online hours). I guessed the driver keeps less than the rider pays, but no file gives Uber's share, so I could not connect gross bookings to what the guarantee tops up.

**4. CONFUSING. S1, line 31.** "to keep the median rider wait under five minutes, in fifteen minutes, without a dataset"; "no published figure exists for the number a sanity check on the afternoon ask would want"; "Each objection is partly right". On first read "in fifteen minutes" looked like part of the wait. The sentence about the published figure I read three times before I understood it. "Each objection" points at objections the deck has not introduced yet (they arrive on S19).

**5. MINOR. S2, lines 50, 55 and 56.** "trips per online hour 1.9 to 1.6"; "does it transfer"; "the north-star slide, Anand's new store". Every other file says 1.90 to 1.58, so 1.6 made me wonder whether it was a different number. "Does it transfer" (Saturday) and "Anand" (not introduced until the Kalpa store set) meant nothing to me here.

**6. CONFUSING. The saving range: S3 line 81, and the same line on the S10 picture, S49, S56, cheat sheet panel 1 and `extras/C2_W04_D02_interview_room_STUDENT.md` line 41.** "that returns Rs 58 lakh to Rs 93 lakh over six weeks if a fifth to a half of the idle drivers start accepting". I could not trace either number on any slide; the working is only in the speaker notes. The guided exercise (lines 47 to 49) says it in words ("If a fifth to a half of that is still paid ... the rest comes back") but never shows the sums: Rs 1.16 crore x 1/2 = Rs 58 lakh, Rs 1.16 crore x 4/5 = Rs 92.8 lakh, and 1 crore = 100 lakh. The sentence also pairs the ranges in reverse: read left to right, "Rs 58 lakh" lines up with "a fifth" and "Rs 93 lakh" with "a half", when it is the other way round (more drivers accepting means less money back). "Returns" sounded like profit to me.

**7. CONFUSING. Who the saving is about: S3 line 81, the S10 picture, S49, S56, guided line 45 and interview room line 41, against S9 line 219, S12 line 288, `exercises/unguided/C2_W04_D02_studio_brief_STUDENT.md` line 73 and the written-case solution line 23.** "if a fifth to a half of the idle drivers start accepting" against "driver-weeks that accepted fewer than half their offers" against "the 180 drivers whose trips per online hour fell under 1.0". The saving is worked from the Rs 1.16 crore paid to low-acceptance driver-weeks, yet the action line calls them "idle drivers", and S12 defines the idle tail as 180 drivers picked by trips per hour, a different test. The studio brief's option b calls the Rs 1.16 crore "paid to idle drivers"; the written-case model page says "low-acceptance drivers". No file says whether these are one group.

**8. CONFUSING. "Acceptance floor" and "the floor": S3 line 81, the S10 picture (subtitle and box 4), studio brief line 6, written case lines 6 to 7, S49, S56, cheat sheet panel 1; and S4 line 100, S20 line 452.** The phrase "acceptance floor" is used all day and its plain meaning arrives only in the written-case solution (line 22, "a floor on how many offered rides a driver accepts"), the last file I read. On S4 and S20, "the floor" means the Rs 300 an hour the hoarding promised, so the same word names two different minimums. I could not tell which floor the action was about.

**9. CONFUSING. "Guardrail": S4, lines 101 and 104.** "Top-up per trip becomes a guardrail"; "with three guardrails". The word is never explained in any Tuesday file, and it comes back in the Kalpa template, S51, S55, the interview room and Kahoot Q7. From the list I guessed "a number you watch so the main number cannot be gamed", but that is a guess.

**10. CONFUSING. "Acceptance share": S4 line 104, the S8 picture, S9 line 217, S12 line 281.** The term is defined only in Kahoot Q7 ("requests accepted over requests offered"), at the end of the day. S9 defines "low acceptance" but not the share itself.

**11. MINOR. Shares written as decimals: the S8 picture, S9, S12 lines 281, 282 and 286.** "Acceptance share 0.86 to 0.73"; "Online hours with no trip 0.22 to 0.38"; "Driver cancels after accepting 0.04 to 0.09"; "Unfulfilled requests 0.11 to 0.10". These sit beside "61 percent" and "+24 percent" on the same slides, and I had to stop to work out that 0.86 means 86 percent. "Online hours with no trip 0.22 to 0.38" appears only in the S8 picture and is never explained in the morning; it returns in the afternoon as the idle share.

**12. MINOR. S6, line 153.** "the number that rose while riders were served no better". The S8 picture and S9 show the median wait falling from 4.8 to 4.6 minutes, and S12 shows unfulfilled requests falling from 0.11 to 0.10, so riders were served a little better. No file says 0.2 minutes is too small to count.

**13. CONFUSING. S7, line 185.** "A slide that opens on its evidence has already given away its title, and a slide whose caveat sits off the page invites its owner to call it dishonest." I read this three times. "Given away" could mean "revealed" or "lost". "Its owner" reads as the slide's owner, who would not call their own slide dishonest; it only made sense at S27, where a caveat turns out to have an owner (a role).

**14. CONFUSING. One piece of evidence or two: S7 line 171, S9 to S10, the S10 picture, `study-notes/C2_W04_D02_notes_STUDENT.md` line 137, `exercises/unguided/C2_W04_D02_mid_cut_to_two_STUDENT.md` lines 70 to 71 and its solution line 37.** S7 says the evidence is "one chart or one number". S9 asks which two numbers carry the claim, and S10 answers trips per hour plus "the 61 percent". The notes say "Nine numbers become two: the chart ... and the 61 percent". The mid_cut solution says "The morning deck's rebuilt slide A keeps the chart and the split, and its appendix drawer heads one page per role". The rebuilt slide A picture (S10, the notes' "one picture to remember", cheat sheet panel 1) shows the chart, the caveat and the action, with no 61 percent and no drawer. The mid_cut set sends me to the deck to check my letters against something the picture does not show.

**15. MINOR. The S10 picture, the S15 picture and the notebook's clear chart (cell 10).** "launch, 31 Aug". The red launch line sits halfway between the 24 August point and the tick labelled 31 August. I could not tell whether the 31 August week counts as before or after.

**16. CONFUSING. S12, lines 278 and 280.** "Drivers | 1,200 (140 new) |". The figure is in the Before column with After blank, but S16 and S20 say the 140 joined after the launch, so there were 1,060 before. Separately, "Offers shown to drivers 2,69,773" is more than the 2,51,910 rider requests on S11; nothing says one request can be offered to several drivers, so the two tables looked inconsistent to me.

**17. CONFUSING. S13, lines 299 to 312.** "The twelve rows, read in rupees three ways". The table shows six rows. That "before" is the week of 10 August and "after" the week of 21 September is only in the speaker notes, so on the slide "Hours before 10" could be ten hours over six weeks. Notebook cell 2 is where I learned these were twelve driver-weeks. A second point: these six drivers bring in Rs 3,135 per driver-week and the city Rs 5,817 (S1); nothing says why the six are about half the city, so I wondered whether they are typical.

**18. MINOR. Predictions answered before they are asked.** S5's answer (c) is the sentence on S3. S14's answer (b) is in S1's table (per hour down 17 percent, per driver-week up 0.8 percent), and the bold line under S14's own options ("the city's count of active driver-weeks moves") points at it. S19's answer (d) is S1's caveat "Each objection is partly right". S26's answer (b) repeats S16's fix word for word ("with one line each on what moved them"). In the notebook, cell 3's prediction was worked on S13 minutes before, cell 5's was on S1 and S15, and cell 11's (the share who ride moves the answer most) answers the afternoon's S39 vote before I reached it.

**19. CONFUSING. S15, the picture (line 345) and line 347.** "index, before window = 100"; "Each line is divided by its own before-window value, so all three start near 100". Dividing a number by itself gives 1, not 100; the step "then multiply by 100" is missing and "index" is not explained. In the picture the amber line (per active driver-week) ends near 96, below 100, which looks like a fall, while the slide says it rose 0.8 percent. Why both are true is only in the speaker notes.

**20. CONFUSING. S16 line 364, notebook cells 7 and 8.** "the 140 drivers who joined after the launch added 140 driver-weeks between them"; "Bookings rose 3.0 percent ... active driver-weeks rose 2.2 percent ... The ratio rose 0.8 percent". 140 drivers over six weeks adding 140 driver-weeks means one week each on average; it read like a typo until notebook cell 7 added "driving only some of the six weeks". The slide makes 3.0 minus 2.2 look like the rule for 0.8, while the notebook's check (cell 8) divides 1.030 by 1.022. I did not know which rule is right or why.

**21. CONFUSING. S17 lines 380 to 381, notebook cell 8 (printed output), cells 9 and 15, notes lines 84 to 85.** "Rs 260.4 | Rs 165 x 1.58 trips per hour". 165 x 1.58 = 260.7, not 260.4. The slide's point is that the two routes "land on the same rupees", and my calculator said they do not. The 1.58 is rounded from 1.578, but no file says so.

**22. CONFUSING. S17 and notebook cell 7.** "A second route reaches rupees per hour without dividing bookings by hours ... If the two routes agree, the fall is all trips." The second route is (bookings / trips) x (trips / hours), which is bookings / hours again, so it has to agree. What shows the fall is all trips is the flat fare. I could not see what the agreement proves.

**23. MINOR. Tags and levels: S18 line 410, S25, S30, S46, notebook cell 15, every exercise, `exercises/C2_W04_D02_index_STUDENT.md` lines 7 and 24.** "[S]", "[F]", "[D]"; "Level L1 ... L6"; "the day's ladder"; "the dojo"; "studio"; "lettered set". None is explained in a student file; the ladder and the dojo are named only in speaker notes.

**24. MINOR. S20, line 451.** "The other 1,020 drivers held at 1.90 to 1.89 trips per online hour". The 1,020 (1,200 less 180) include the 140 who joined after the launch and have no before figure, so I could not see how all 1,020 "held".

**25. CONFUSING. S23 line 507, notes line 119, interview room line 47, studio-brief solution line 29.** "the three busiest weeks after the launch still ran at 1.60 trips per online hour". This is a new number with no source on any page, and no file says why it answers the monsoon objection. My best guess: if the season had cut demand, the busiest weeks should have recovered towards 1.90. That step is never written down.

**26. MINOR. S23, line 511.** "or the test of the redesign showing no change". "The test" has not been mentioned before. That it means a trial in a few zones I learned later, from the interview room (line 41) and the written-case solution.

**27. CONFUSING. S24 line 530 against S31 line 681, and the studio brief lines 20 to 22.** "every member of a group presents once, objects once and scores once"; "The round-one presenter now objects ... the round-one scorer presents, with the appendix pages built in chapter 3". In round one everyone held every seat, so "the round-one presenter" picks out nobody. "Round" means both the studio round and each seven-minute turn. Chapter 3 drew the drawer and ran the cut-to-two drill; I built no appendix pages, so I did not know what to present with.

**28. CONFUSING. S27 line 592, mid_cut lines 7 and 64.** "does the sign-up story survive?" "Sign-up story" is never explained. I guessed it means the 140 drivers who joined after the hoarding went up.

**29. MINOR. Everyday words used in a special sense, across both decks.** "Window" means the six-week before or after period ("the monsoon ended inside the window", S3) and also the three-hour peak ("the peak window is three hours long", S1). "Read" is a noun ("three reads", "the per-driver-week read"). "Appendix" is used on S16 before chapter 3 explains it. "Sized" means estimated (S3). Each cost me a pause.

### The notebook: notebooks/C2_W04_D02_01_makeover_and_ledger_STUDENT.ipynb

**30. CONFUSING. Enrolled, active, or all drivers: notebook cells 5 and 13, S4 line 104, S12 line 278, the guided-exercise solution line 24, the mid_check solution line 26.** Cell 5: an active driver-week counts a driver "whether or not the driver is enrolled in the guarantee, so it counts drivers who used the app, never sign-ups". S4: Monday's redesign pays "per enrolled driver per week". The guided solution: enrolment "was never the scheme's" unit. The mid_check solution: "Monday's 1,200 drivers are the enrolled drivers in the case data". Cell 13: the data covers "the twelve zones the enrolled drivers work". So I could not tell whether the table holds only enrolled drivers or everyone, whether "enrolled" is the redesign's denominator or never the scheme's, and what "sign-ups" means (to the guarantee, or new drivers).

**31. CONFUSING. Cells 11 and 12.** "Drivers online = rider requests an hour / trips one online driver completes an hour x a buffer"; "Requests an hour walk from a crowd to a count"; "1e7, 9e6, 1.1e7". In words I could not tell whether to divide by (trips x buffer) or divide and then multiply; only the code shows the second. "Walk from a crowd to a count" is a picture I could not turn into a step. The ledger is written in scientific notation, and no value or range has a reason beside it (the 2.4 trips an hour is explained only on afternoon S38: about 25 minutes a trip).

**32. MINOR. The swing charts: notebook cell 12 output and the S40 picture.** In the notebook chart the red vertical line has no label (the whiteboard version says "central: about 5,700"). On the S40 picture the labels "trips a busy driver fits in" and "share in the evening" are cut short, and "people who ride on a weekday" differs from "share who ride on a weekday" on S39 and in the notebook.

**33. CONFUSING. Cells 13 and 15, S41 lines 228 to 234, S56 line 531.** "online driver-hours behind each rider request"; "1 / 1.68, about a quarter above 0.47". I could not see why trips per driver-hour is turned upside down, what "behind" means, or whether a request is the same as a trip (Monday's tables show 10 to 11 percent of requests unfulfilled). S41 gives three numbers and no conclusion; "the chain errs on the generous side, so the buffer is the first factor to trim" is only in the speaker notes and the notebook. The day still closes on "about 5,700" (S56), so I did not know whether the check was meant to change the answer.

**34. CONFUSING. Cell 13 and S41 line 234, against S1 line 31 and S37 line 133.** "Monday's data counts peak hours on all seven days, two three-hour windows a day, 42 hours a week". The morning said "the peak window is three hours long", and the afternoon's clarify step says "The weekday evening peak, three hours long". I had understood the guarantee and the data to cover one evening peak; learning in the afternoon that the data holds two windows a day, every day, left me unsure what the morning's totals cover.

**35. CONFUSING. Cells 13 to 15, S44, S45 line 306.** "about 35 crore active UPI users ... set against NPCI's average of 802 million"; "24.07 billion"; "A city of two million people ... about 5 lakh households". Crore, lakh, million and billion are mixed without the conversion shown (35 crore x 2 = 70 crore = 700 million; 2 million = 20 lakh, and 20 lakh / 4 = 5 lakh). S44's diagram shows "70 crore, 700 million" once; the notebook does not.

**36. CONFUSING. The UPI drill was spoiled before it began: notebook cells 13 to 15 (opened in the morning) and `exercises/unguided/C2_W04_D02_mid_check_against_STUDENT.md` line 33, against `exercises/unguided/C2_W04_D02_paired_estimate_STUDENT.md` lines 3 to 4 and 41.** The notebook works the full UPI chain (35 crore x 2 = 700 million) and prints NPCI's 802 million; the mid_check table prints it too. The paired drill then asks me to "size a number neither of you has looked up" and says "The trainer reveals the published figure after the swap". I already knew the chain and the answer.

**37. MINOR. Wording and layout in the notebook.** Cell 13: "is to be found; no source holds it" (will it be found, or does it not exist?). Cell 14's check says "within a third" while cell 15 says "about a quarter more". Cell 15: "a wrong 3 percent", "the same order" (of magnitude, I guessed) and "which points at payments a day" (a jump I could not follow). Cell 4's printed table wraps into two blocks with a "\" between them. Cell 7 says "The next cell checks the three growth rates", but the next cell sits under a new heading about the second route.

### The morning exercises

**38. CONFUSING. Twelve of the fourteen lettered items can be answered without the idea (the table at the top).** guided Q1, Q2, Q3; mid_cut Q1, Q2; studio Q1; mid_check Q1, Q2, Q4; interview_rungs Q1, Q2; kalpa_store Q1. In each, the key repeats the stem's words, carries the claim's own number, can be back-solved from the next line, or was printed earlier in the deck or the notebook. I got all fourteen right and still could not tell, for several, whether I had understood the idea or only matched words.

**39. MINOR. Guided Q1, lines 75 to 82, and S11 line 262.** "Which one number from finance's tab proves the drafted claim?" The claim is "Rs 1.16 crore of the top-up went to ...", and the key is "Top-up to low acceptance, Rs 1.16 crore". Proving a claim with the number it already states felt circular, and the solution calls it "the claim's own number". S11 also asked for "the caveat that sits beside it", but finance's tab holds no caveat and the exercise drops that half.

**40. CONFUSING. Guided Q2, lines 96 to 103.** "The scheme pays drivers for each peak hour online. Which denominator should slide C's evidence name?" Monday's redesign pays per completed trip (S4), so "per completed trip" (b) also looked right for "the scheme". Nothing says the question means the scheme running now, before the redesign.

**41. MINOR. Guided line 127, S37 line 136, S39 line 192.** "1 crore people x 1 percent who ride on a weekday x a quarter of the day's trips"; "Rider requests, each one a trip to serve"; "1 lakh trips a day". People who ride become trips, and trips become requests, with no line saying each rider takes one trip a day, while Monday's tables show some requests never become trips.

**42. MINOR. Studio brief line 83 and its solution line 27.** "The final number is never scored" (the final number of what?). The solution's driver-operations concession, "the outer zones are thin", uses a fact and a word ("thin") I had not met.

### The afternoon deck: slides/C2_W04_D02_half2_STUDENT.md

**43. CONFUSING. S33 lines 33 to 39 and S34 line 52.** "Which of these numbers checks it?"; "The answer is c, and nobody publishes it ... d checks one link in the chain ... and that is the check the afternoon uses." The right answer is a number that does not exist, and the check the afternoon goes on to use (d) is marked wrong. I picked d and still do not know whether d was wrong.

**44. CONFUSING. Which test a trap breaks: S34 line 52 and its diagram (line 60), S45 lines 306 to 308, cheat sheet panel 5 (lines 47 to 49), the mid_check solution line 24, the paired-estimate solution lines 21 to 22.** S34's text says sign-ups are "a different definition", while its diagram puts "drivers signed up" on the "same unit? no" branch. S45 files Delhi Metro boardings under "A different unit" and Flipkart under "Read the source's text"; the cheat sheet files both under "Definition" and puts the day's-trips error under "Unit". The cheat sheet calls the 31-day error "Period"; the paired solution calls it "the wrong unit". I could not learn the three tests when the files sort the same traps differently.

**45. MINOR. Names and places I could not look up: S6 line 153, S36 line 118, S54 line 501, notes lines 102 and 176.** "Barbara Minto's Pyramid Principle"; "Aced's analyst guide"; "the Big Idea from Storytelling with Data"; "(Explorer scenes T1 and T2.)"; "(Explorer scene T3.)". None is introduced on the slide. The notes send me to explorer scenes but give no path, and the day folder has no student explorer file.

**46. CONFUSING. S39, line 199.** "Which assumption moves the answer most across its range". No range is on the slide; the ranges appear only after the vote (S40) and in notebook cell 12. I could only guess.

**47. MINOR. S39 line 196, interview room lines 69 and 74.** "8,300 / 1.68 | about 4,960 drivers"; "about 6,250 an hour, so about 4,300 drivers". 8,300 / 1.68 = 4,940; the 4,960 comes from 8,333, not the 8,300 on the slide. The four-hour answer skips the "/ 1.68 x 1.15" step.

**48. MINOR. S43, line 262.** "split between paying shops and paying people". I could not see how the split enters the chain: another factor, or two chains added together?

**49. CONFUSING. S44 line 277, S45 lines 307 to 308.** "NPCI"; "DMRC"; "64.06 lakh journeys a day ... 82,44,903 boardings"; "the 63 is in its URL". NPCI and DMRC are never spelled out. Why journeys and boardings differ is only in the speaker notes and in the mid_check table's 2018 row. I could not picture how a web address holds a wrong number.

**50. CONFUSING. S45 line 306 and Kahoot Q5 (lines 57 to 60).** "A city of two million people has nine million households"; "People were counted as households". If people were counted as households the error would give two million households, not nine million, so the stated cause does not produce the number. I later guessed someone multiplied by about 4.5 people a household instead of dividing, but no file says so.

**51. CONFUSING. S50, line 428.** "Requests an hour times the trips one online driver completes, times a buffer: about 8,300 / 1.68 x 1.15". The words say "times" and the sum divides. Weak in maths, I need the words and the sum to agree.

**52. CONFUSING. "North star" and "leading input", never defined: S2 line 56, S51 lines 445 and 447, notebook cell 15, `exercises/guided/C2_W04_D02_kalpa_slide_template_STUDENT.md` lines 1 to 7, the lab set, notes lines 183, 214 and 216, interview_rungs Q2.** Both terms carry the Kalpa lab and the AI variant. I answered interview_rungs Q2 by matching the phrase, and its solution never says what a leading input is or how it differs from a north star.

**53. CONFUSING. The AI variant's other terms: S51, interview room lines 81 to 103, notebook cell 15.** "commit"; "build failures and revert rate as guardrails"; "vanity metric"; "pays the team for text that survives"; follow-up 1, "the guardrails tell us whether it fell because suggestions got worse or because developers write more themselves". I got the gist (count text that is kept, not text that is accepted), but I could not follow how revert rate tells those two cases apart, or which team is "paid".

**54. MINOR. S52, line 463.** "Named the denominator and the window" is a criterion for scoring both transcripts, but transcript 2 is an estimate with no denominator. I did not know how to score it.

**55. MINOR. S47 line 367 and the written case lines 43 to 44.** "Words a non-technical reader would not know (denominator, ratio of sums, regression) stay off the page ... Say what they mean instead." "Ratio of sums" is never defined, so I cannot say what it means instead.

### The afternoon exercises

**56. MINOR. mid_check Q3, lines 64 to 71, and its solution lines 30 to 33.** "DMart's revenue divided by the 415 stores open at the start of the year". This file never shows that 415 is 500 less 85 (the Kalpa store set does). "Standalone total revenue" is not explained. The solution's item worth arguing about discusses the year-end count (about Rs 134 crore), which is not one of Q3's options.

**57. BLOCKER. `exercises/unguided/C2_W04_D02_written_case_STUDENT.md`, lines 27 to 28 against lines 36 to 41 and 50 to 58.** "No laptop, no phone, no notes beyond this brief"; "The action, its saving in rupees over a stated number of weeks with the assumption behind it, and who signs". The brief gives Rs 1.16 crore of Rs 1.9 crore but not the saving range (Rs 58 lakh to Rs 93 lakh), not the assumption (a fifth to a half start accepting) and not who signs. I never saw the working for the range (finding 6), so with no notes I could not rebuild it, and the checklist marks the action on exactly this. I could not finish the last part of the handed-in page as asked.

**58. MINOR. The written-case solution, lines 22 to 25, against the S10 picture and guided line 45.** The model page's action is "The city head signs off a test in a few zones first"; slide A's action is to pay per completed trip, with the city head signing. These are two different actions for the same case, and I did not know which one the checklist wants.

**59. MINOR. `exercises/unguided/C2_W04_D02_interview_rungs_STUDENT.md`, line 9.** "Illustrative case: the company is real ... The coding-assistant company is invented." The same box says the company is real and that it is invented.

### The Kahoot: kahoot/C2_W04_D02_quiz_STUDENT.md

**60. MINOR. Lines 21, 32, 42, 53, 60, 71, 82 and 90, and Q2 lines 27 to 33.** "<- correct" is printed beside every key in my copy, and nothing says to open the file only after the quiz. Q2 asks which element should take "one more" slot and the key is the caveat, which the morning said is one of the four parts that must already be on the slide; I was unsure whether this slide was missing it.

### The Kalpa lab

**61. CONFUSING. Kalpa slide template, lines 1 to 9.** "one of the three Kalpa heads who lose something under it: the marketing lead, Operations, or the head of Retail-Plus". The Uber case spelled out what each role loses (S4); the Kalpa template does not, so I could not prepare for the objection. "Retail-Plus" is not explained in this file; the Kalpa store set explains it, after this file in the index.

**62. CONFUSING. Kalpa slide template, lines 34 to 36, and the lab-set solution line 11.** "these warehouse totals: 1,000 orders from 340 customers, Rs 10.00 crore booked in April to June 2026 and Rs 9.84 crore in July to September 2026". I did not know whether "warehouse" means a building or a database, or which months the 1,000 orders cover. Rs 10 crore from 1,000 orders is at least Rs 1 lakh an order, which seemed huge for a shop. These totals cannot give "delivered orders per active customer per month" (no delivered count, no monthly active customers). The solution's "strong version" of the evidence repeats the totals with no number, so I could not check mine.

**63. CONFUSING. Kalpa's size, across three files: the Kalpa template line 35, the Kalpa store set line 59, the lab-set solution line 27.** The template says Kalpa booked about Rs 10 crore a quarter. The Kalpa store set imagines one new store selling Rs 150 crore in its first year, and the lab solution's worked store sells Rs 72 crore a year. One store selling several times the company's quarterly bookings made me doubt which figures describe Kalpa.

**64. CONFUSING. The Kalpa store set, lines 3 to 7 and 59 to 69, and the lab set line 42.** Anand asks how many customers a new store could sign up to Retail-Plus (a count of members), but the check is a year of store sales in rupees against DMart's revenue per store. The afternoon taught me a check counts only in "the same unit, period and definition" (S34), and here the unit (rupees against members) and the definition (all shoppers against paid members) both differ. The step from members to sales appears only in the lab set.

**65. CONFUSING. Which DMart figure: the mid_check solution lines 25 and 30 to 33 and the Kalpa store solution line 20, against the lab-set solution line 27.** Two solutions say the average store count (about Rs 146 crore) is the right check and that the year-end count (about Rs 134 crore) "understates a mature store". The lab solution's worked estimate validates against "DMart's about Rs 134 crore a store on the year-end count". I did not know which one to use in the lab.

**66. MINOR. The lab set lines 60 to 62 and its solution lines 45 to 51.** "using the numbers from the morning's answer slide": the morning has five answer slides (S6, S10, S15, S20, S27), and I guessed S20. In the solution, P4 says "one guardrail that answers the CEO's question" and "the page of the head who owns each" without naming either, so I could not mark my answer. P5's model reads "Fund the store if it can sign about 1,000 members ...: our estimate is 1,000", which sounds circular, and "the case rests on year two" is not explained.

### The notes, the cheat sheet and the take-home

**67. CONFUSING. Notes word table, lines 224 to 233, and the cheat sheet's word list.** The tables define claim, denominator, gross bookings, active driver-week, caveat, appendix page, idle share and sanity check. They leave out the words I needed most: top-up, guardrail, north star, leading input, acceptance share, acceptance floor, low acceptance, idle tail, enrolled driver, buffer, index and driver-hour.

**68. CONFUSING. Notes, lines 142 to 145.** "A familiar number that leaves the report draws the question it was hiding from." I read it three times, and I could not see how the 2018 Delhi Metro story shows what should leave a slide.

**69. MINOR. Notes line 119 against S20 line 453.** Finance's objection is answered by "the busiest after weeks still ran at 1.60" in the notes and by "drivers who joined before the launch fell from 1.90 to 1.58" on S20. Two different second lines of evidence for the same row.

**70. MINOR. Cheat sheet panel 4, lines 34 to 39.** The table lists Clarify, Map, Calculate, Range. Its crux says "four steps", and the deck's four steps end on Validate, which the panel leaves out. "(2.4 x 0.70)" appears without the idle share it comes from.

**71. CONFUSING. Cheat sheet panel 5, line 48.** "24.07 billion over 31 days, 776 million, against NPCI's 802 million a day". The sheet never says the month is September or that September has 30 days, so on its own I cannot see why 31 is wrong.

**72. MINOR. The cheat sheet PDF, panel 1.** The rebuilt-slide picture is printed small. I measured its caveat and action text: lines about 26 px tall in a 1,376 px picture placed 268 points wide, so about 5 point on paper. In the rendered sheet I could read the two boxes only by zooming in.

**73. MINOR. Take-home brief lines 4 and 30, self-check line 23.** "Kalpa Health's question"; "what it costs in dollars or weeks". Every other file says Kalpa Retail and rupees. I guessed Build 1 was a US business, but neither file says so, and neither says when or where to hand in.

**74. MINOR. Other business words never explained, across the pack.** "finance partner" (title slide line 6; I first read it as an outside partner company), "city review", "supply at peak" (S19), "standalone total revenue" (mid_check), "finance controller" (Kalpa store set), "dark store" (lab set line 33, take-home line 48), "quick-commerce", "listed company" and "shareholder letter" (take-home line 48), "capstone defence" and "market-sizing theory" (notes lines 50 to 51), "incident review" (notes line 185), "sales base", "catchment", "ramp" and "the Week 5 handover" (Kalpa store solution), "proxy" (interview_rungs solution). Each one stopped me briefly; none stopped me completely.

---

### Where the categories you asked about sit

- **Two files giving different numbers or reasons for the same thing:** 5, 7, 8, 14, 16, 20, 21, 30, 34, 44, 50, 58, 63, 65, 69, 73.
- **A file sending me elsewhere for something I needed:** 1 and 2 (definitions only in the notebook or the guided set), 14 (mid_cut sends me to a picture that lacks the split and the drawer), 17 (the week dates only in speaker notes), 33, 45 (explorer scenes with no path), 61 (Retail-Plus explained in a later file), 64.
- **Pictures too small, crowded or misleading:** 14, 15, 19, 32, 72.
- **Business words used before they are explained:** 1, 2, 8, 9, 10, 28, 52, 53, 67, 74, plus "idle drivers" before the idle tail is defined (7) and "appendix" before chapter 3 (29).
- **Items whose answer a cue gave away:** 18 (deck and notebook predictions), 38 and 39, and the table at the top.

### Counts

- Total findings: 74
- BLOCKER: 1 (finding 57)
- CONFUSING: 44
- MINOR: 29

---

## Read 2: the hiring interviewer (analyst screens at Uber, Swiggy, Google and an AI startup)

Read cold on 12 October 2026 by the interviewer who runs the screen. Files read, all under
content/W04/D2/: extras/C2_W04_D02_interview_room_STUDENT.md; slides/C2_W04_D02_half2_STUDENT.md,
S33 to S52; exercises/unguided/C2_W04_D02_interview_rungs_STUDENT.md and its solution;
study-notes/C2_W04_D02_notes_STUDENT.md, "Where does this get tested?";
trainer/C2_W04_D02_guesstimate_TRAINER.md; trainer/C2_W04_D02_day_sheet_TRAINER.md, "What are the
interview answers, in one breath?"; internal/C2_W04_D02_facts_INTERNAL.yaml. I recomputed every case
number below from Monday's three CSVs (content/W04/D1/data/) with a read-only script in my
scratchpad. Public figures marked "verified" were fetched on 12 October 2026. I opened the trainer
scorecards only after section A was written.

Another session changed the pack while I was reading: commit 1975ae0 (19:42, the saving now reads
"Rs 58 lakh to Rs 92.7 lakh ... depending on whether half or a fifth", and the notes now cite "the
other 880"), commit c8d6b57 (19:44, half two's cover replaced by an "AN ILLUSTRATIVE CASE" header),
and uncommitted edits to the notes, half one and the facts file. At 19:55 I re-checked every
quotation below against the files as they then stood, and findings 2, 28, 36 and 40 are written
against the current text.

### A. Scores (0, 1 or 2 on the S52 rubric)

**Transcript 1, hire-grade answer** ("The scheme is paying for online hours that carry no trips...")

| # | Criterion | Score | Evidence |
|---|---|---|---|
| 1 | Clarified the scope first | 1 | The three questions (which decision, who else hears it, how long the slot is) are the right ones. But the transcript never records the answers, and the answer never says which decision it serves; "test before extending" first appears in follow-up 1. The structure line promises "who signs", and the answer names no signer. |
| 2 | Named the denominator and the window | 2 | "an hour a driver spends online at peak" and "the six weeks after the launch on 31 August, against the six weeks before". |
| 3 | Saw the trap or paradox | 1 | It names the per-driver-week read ("You will hear that bookings per driver-week rose"). But the check it offers ("that is 140 new drivers joining part-way") is wrong on the case's own data (finding 1). Named, then checked wrongly. |
| 4 | Sized it with a unit | 2 | Rs per peak online hour, Rs crore of top-up and Rs lakh over six weeks, carried through. |
| 5 | Said what would change their mind | 1 | "a test in a few zones settles it" names a method, never the result that would reverse the call. The named fact only comes in follow-up 3 ("If last year's same weeks fell as far"), and the candidate has just said that fact does not exist. |
| 6 | Tied it to a decision and its cost | 2 | "paying per completed peak trip with an acceptance floor: Rs 58 lakh to Rs 92.7 lakh back over six weeks". |
| 7 | Gave the structure before the number | 2 | It opens on the claim, and the first number comes in the second sentence. |
| | **Total** | **11 of 14** | |

**Transcript 2, hire-grade answer** ("I will take drivers online at one moment...")

| # | Criterion | Score | Evidence |
|---|---|---|---|
| 1 | Clarified the scope first | 2 | "drivers online at one moment of the three-hour weekday evening peak, Uber only, median wait under five minutes": the unit, the window and the target are all pinned. Finding 21 covers the gaps (products, multi-homing, which median). |
| 2 | Named the denominator and the window | 2 | "about 8,300 requests an hour" over the three-hour weekday window, divided by "about 1.68" trips per online driver-hour. |
| 3 | Saw the trap or paradox | 1 | It avoids dividing a day by an hour but never names that trap, and the check meant to catch such slips compares unlike quantities (finding 7). The trap is avoided without a word, which is short of "named and checked". |
| 4 | Sized it with a unit | 1 | "1 percent ride on a weekday, a quarter of those trips": riders turn into trips with no trips-per-rider factor. That is exactly the "unit that changes between factors without anyone saying so" the notes warn about (finding 10). |
| 5 | Said what would change their mind | 1 | The check finds the chain "on the generous side", and the candidate keeps 5,700. No fact that would move the number is named until follow-up 3. |
| 6 | Tied it to a decision and its cost | 0 | 5,700 is never tied to a decision or a rupee: no incentive budget, no cap on enrolment, nothing the city head does with it. S42 shows the material knows the decision exists ("asks for incentives for about seven times the drivers"). |
| 7 | Gave the structure before the number | 1 | Scope comes first, but the formula listed under "The structure" is never said before the multiplying starts. The S50 version does say it, with the wrong operator (finding 12). |
| | **Total** | **8 of 14** | |

**The AI-company variant, hire-grade answer** ("Acceptance counts a suggestion as a win...")

| # | Criterion | Score | Evidence |
|---|---|---|---|
| 1 | Clarified the scope first | 1 | The listed questions are good, but the answer never pins the unit of "suggested text" (characters, lines or tokens), the window, or the outcome the north star serves (renewals, seats, time saved). |
| 2 | Named the denominator and the window | 1 | "per active developer-week" leaves "active" undefined, and "present at the next commit" is a different window for every developer (finding 16). A lenient marker gives 2 because both words appear. |
| 3 | Saw the trap or paradox | 1 | The trap is named in the first sentence and never checked: no share of accepted text later deleted, no number of any kind. |
| 4 | Sized it with a unit | 0 | No number and no unit. The invented 32 percent in the question is never used. |
| 5 | Said what would change their mind | 0 | "We report both for a quarter", with no result that would make the team keep acceptance or drop retained text. |
| 6 | Tied it to a decision and its cost | 1 | A decision (a new north star, with pay tied to retained text) and no cost: no revenue at risk, no instrumentation cost, no serving cost. |
| 7 | Gave the structure before the number | 2 | Claim, proposal, guardrails, concession, transition, in that order. There is no number to put first. |
| | **Total** | **6 of 14** | |

**The weak answers, quickly**

| Answer | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Total | Why |
|---|---|---|---|---|---|---|---|---|---|
| Transcript 1, weak | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 3 | It starts on method ("So I looked at the dashboard"), names per hour but no window, falls into the trap ("Bookings per driver-week is actually up, so the picture is mixed"), and offers "maybe pay per trip" with no rupees |
| Transcript 2, weak | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 2 | No scope; a day's trips divided by an hour's rate; no idle share, no range, no check, no decision |
| AI variant, weak | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 2 | It drops the number customers see, which is the first half of the trap; a decision with no measure |

The weak answers are fair contrasts.

**Do the hire-grade answers score 2 on the first three criteria?** No, none of them does. Transcript
1 scores 1, 2, 1; transcript 2 scores 2, 2, 1; the AI variant scores 1, 1, 1. The spine sets the
gate for this read (docs/detailing/W04_analyst_craft_spine.md, acceptance item 14: "the interviewer
read scores each transcript's hire-grade answer at 2 on the first three criteria and names nothing a
strong interviewer would reject"). The pack meets neither half of that sentence.

### B. What a strong interviewer would reject

**1. REJECT. Transcript 1's pre-emption line gives the wrong cause, and the case's own data contradicts it.**
Quote: "You will hear that bookings per driver-week rose; that is 140 new drivers joining part-way,
and it is not what the scheme pays for." The 140 joiners logged 140 driver-weeks at Rs 4,314 each,
which is below the average, so they pulled bookings per driver-week down. The 1,060 drivers who were
there before the launch went from Rs 5,816.5 to Rs 5,895.4 a driver-week, up 1.4 percent. Adding
the joiners brings the rise down to 0.8 percent. The rise comes from hours: a pre-launch driver-week
carried 22.6 peak online hours after the launch against 18.6 before, and Rs 260.4 x 22.5 hours =
Rs 5,861 against Rs 313.5 x 18.55 = Rs 5,816. The next follow-up: "New drivers add driver-weeks to
the bottom of that ratio. How do they push it up?" The line that survives it: "It rose because each
driver stayed online four more hours a week at 17 percent less per hour; the scheme bought hours."
The same error sits in three more places: the notes' WATCH OUT ("because 140 joiners drove only some
weeks); hours never enter it"), the day sheet's S16 row, and the facts file's first correction
("hours do not enter that ratio"). The ratio's formula has no hours in it, but it splits exactly into
rupees per hour times hours per driver-week.

**2. REJECT. The saving is restated as a different assumption and priced without the per-trip rate.**
Quote, as it now reads: "Rs 58 lakh to Rs 92.7 lakh back over six weeks depending on whether half
or a fifth of the idle drivers start accepting." (When I began reading it said "Rs 93 lakh ... if a
fifth to a half", which mapped the range backwards; commit 1975ae0 fixed the order.) Monday's facts
define the range as the share of the Rs 1.159 crore that is still paid: a fifth still paid gives
Rs 92.7 lakh, a half gives Rs 58 lakh. The transcript turns that into the share of idle drivers who
start accepting. The two match only if a driver who starts accepting is paid per trip exactly what
the hourly floor paid him to sit idle. And "back" is spend avoided, not money returned. The saving
also assumes the per-trip scheme costs the accepting drivers what the hourly
top-up did (Monday's Rs 74 lakh), yet no per-trip rate appears anywhere in the day. The missing depth
is interference between drivers. Requests rose only 1.8 percent, so most trips the newly accepting
drivers complete are trips the 1,020 would otherwise have done. Under pay per completed trip, the
payout is the rate times trips, and demand caps the trips. So the uncertain number is the rate, not
the uptake. The next follow-up, from the finance partner: "What is the per-trip rate, what does it
cost on the 1,020 who already accept, and why does a fifth of the drivers accepting mean a fifth of
the money?"

**3. REJECT. A supply incentive is judged with no rider outcome, and the money's geography is missing.**
The answer treats every idle hour as waste ("The scheme is paying for online hours that carry no
trips"). In a two-sided market some idle supply is what buys short waits, and the first question an
Uber interviewer asks of a supply incentive is what riders got. The case data answers it:
- The median wait went from 4.8 to 4.6 minutes.
- The served share of requests went from 0.890 to 0.900. That is about 2,600 more requests served
  than the before rate would give on the after window's demand.
- 74 percent of the Rs 1.16 crore paid to low-acceptance driver-weeks went to the three outer zones.
  Those zones' zone-week medians sat at 6.6 minutes before and about 6.0 after, above the five-minute
  target in every outer zone-week of both windows.

Monday's own hire-grade line said "waits barely moved; 180 drivers sat idle, mostly in the outer
zones", and Tuesday's drops both points. The next follow-up: "What did riders get for Rs 1.9 crore,
and where are the idle hours? If they sit in the zones that already miss five minutes, what happens
there when you stop paying for them?" A line that survives: "Three-quarters of the idle money is in
the outer zones, which already run at six minutes, so the redesign keeps median wait by zone as its
guardrail."

**4. REJECT. "A test in a few zones settles it" overclaims, and the action is left ambiguous.**
The case has twelve zones, and drivers work across them. A few treated zones give only a handful of
units, drivers move toward the better-paying zones, and core and outer zones behave differently (4.6
against about 6.0 minutes). So "settles" promises more than the design can give. It is also unclear
whether the city head is being asked to roll out the redesign or to sign off a test. The Rs 58 lakh
to Rs 93 lakh is the city-wide six-week figure, which a test in a few zones does not deliver. The
structure line promises "the action with its cost and who signs", and the answer names no signer;
the day sheet's version does ("the city head signs a test first"). The next follow-up: "Test or
rollout? If it is a test: which zones, how many weeks, which number decides it, and how do you stop
drivers moving into the treated zones?" The missing depth: randomise drivers within zones, or switch
the rule by zone and time block; name the deciding metric (trips per enrolled driver) and the
guardrail (median wait by zone) before the start; and say how many weeks it runs.

**5. REJECT. The monsoon rebuttal leans on a six-week average that hides a falling trend, and compares the weakest weeks.**
Quote (follow-up 3): "Requests rose 1.8 percent, so demand did not fall, and the busiest three
weeks after the launch still ran at 1.60 trips an hour." Weekly requests in the after window fell
four weeks running, from 43,878 in the week of 7 September to 41,161 in the week of 5 October. A
finance partner holding the weekly series will say demand is falling as the rains end. The "busiest
three weeks" are also the first three weeks after the launch (31 August, 7 and 14 September), so
busiest and earliest cannot be told apart. The rebuttal also answers only the demand side, while a
change of season can bring more drivers online, which lowers trips per hour by itself. The data
allows a stronger line: "In the last three weeks requests were back at the before window's level
(41,161 to 42,602 a week against 41,155 to 42,719), and trips per hour still ran at 1.56." Without
last year's weeks, the comparison that settles the season is a city where the rains ended and no
scheme launched, read as a difference in differences. No file mentions it. The next follow-up:
"Requests have fallen four weeks running. Isn't that the monsoon?"

**6. REJECT. Follow-up 2's alternative denominator is the fare.**
Quote: "If the scheme paid per trip I would read per trip, which is flat at Rs 165." Bookings per
trip is the average fare, and it says nothing about any incentive. Under a per-trip scheme, the
reads are top-up per completed trip (Monday's guardrail, Rs 82.3 after the launch) and completed
trips per enrolled driver (Monday's north star). The next follow-up: "Rs 165 is the average fare.
What would tell you a per-trip scheme was working?"

**7. REJECT. Transcript 2's validation breaks the rule the day teaches (same unit, period and definition), and the candidate ignores what it says.**
Quote: "the case's own zones had 0.47 online driver-hours behind each request before the launch,
against my 0.60, so I am on the generous side." It fails on four counts:
- **Definition.** The chain treats every request as a trip ("Rider requests, each one a trip to
  serve", S37), but 0.47 divides by requests, and 11 percent of those went unserved. Per completed
  trip the case reads 0.526, so the chain is 13 percent generous, not "about a quarter".
- **Period.** The case's ratio pools all seven days and both peak windows (S41 says so), while the
  estimate is for weekday evenings. The facts file calls it "a ratio no window definition changes",
  which holds only if utilisation is the same in every window.
- **Independence.** The idle share's range came from the same twelve zones, so the check partly
  re-reads its own input.
- **No update.** Having found the chain generous, the candidate keeps 5,700. The case's per-trip
  ratio gives about 5,000 with the buffer.

The S41 trainer note makes it worse: "the chain errs on the generous side, so the buffer is the
first factor to trim". The 0.60 was taken before the buffer, so the buffer is not part of the gap.
The next follow-up: "Your chain counts every request as a trip and your check doesn't. What is the
like-for-like number, and do you move your answer?"

**8. REJECT. Follow-up 1 checks an idle share at a moment against an hourly count.**
Quote: "The share of online hours with no completed trip: 0.22 before the launch and 0.38 after, so
my 0.30 sits between them." An hour with no completed trip is not a moment with no rider. A driver
who drops a rider at minute 10 and then waits 50 minutes has an hour with a completed trip that was
mostly idle. Like-for-like, from the case and the chain's own 25-minute trip: 1.90 trips x 25
minutes means drivers were 79 percent occupied before the launch (idle 0.21), and 1.58 x 25 means 66
percent after (idle 0.34). The numbers happen to sit close here, but the answer makes exactly the
definition swap the day tells the room to refuse. "Sits between them" also misses which end matters:
the before value is the one that held the median wait at 4.8 minutes, under the target, and an idle
share of 0.21 gives about 5,050 drivers. The next follow-up: "Which of your two idle shares
delivered a wait under five minutes, and what does it do to your answer?"

**9. REJECT. The four-hour window answer changes the requirement by redrawing the clock.**
Quote: "The evening's 25,000 trips spread over four hours, about 6,250 an hour, so about 4,300
drivers, unless the fourth hour brings trips of its own." The question asks for drivers online at
the busiest moment, and the riders at that moment do not change because the window got longer. The
answer's own buffer is "for the busiest half hour". A longer window lowers the average hour and
raises the buffer (from 1.15 to about 1.53 for the same busiest half hour), which leaves about 5,700.
A fourth hour also does bring trips, so the 25,000 cannot hold. The next follow-up: "Did the city's
riders change because you redrew the window?" A line that survives: "Nothing changes at the peak
moment. The average hour falls and the peak-to-average ratio rises, so the busiest half hour sets
the number, not the window." The same wrong line is printed as the hire-grade answer in S50's notes
and in the facts file (four_hour_drivers).

**10. REJECT. The hire-grade estimate hides its biggest assumption: one trip per rider.**
Quote: "About 1 crore people, 1 percent ride on a weekday, a quarter of those trips in the evening
window". Riders become trips with no trips-per-rider factor, and evening riders are often commuters
who also rode in the morning. At two trips per rider the answer is about 11,400. That swing is
bigger than the whole range the answer gives for the factor it says "sets the range" (2,900 to
8,600). The next follow-up: "Is your 1 percent riders or trips? How many trips does a rider take in
a day?"

**11. REJECT. The five-minute target is pinned and then never used.**
Nothing in the chain responds to the wait: it sizes throughput at an assumed idle share. The next
follow-up: "Where did five minutes enter your arithmetic? What changes at three minutes?" A strong
answer ties the target to how densely idle drivers are spread. At an assumed 15 km an hour, four
minutes of driving covers about a kilometre, so the city's area divided by that catchment gives the
idle drivers needed. Or it uses the case directly: an idle share near 0.21 held a 4.8-minute median,
so that is the share the target needs. "Median wait" also needs a where. The case's core zones ran
at 4.8 and 4.6 minutes and the outer zones at 6.6 and about 6.0, so a city-wide median can pass
while whole zones fail.

**12. REJECT. S50's model answer says "times" where it divides.**
Quote: "Requests an hour times the trips one online driver completes, times a buffer: about 8,300 /
1.68 x 1.15". Requests an hour times trips per driver-hour means nothing. The lesson of the day is
"write the unit beside every factor", and on its projected slide the model answer gets the operator
wrong in words. S38 now states the formula correctly ("Drivers online = requests an hour / trips
per online driver-hour x buffer"), so the deck also contradicts itself. An interviewer would stop the
candidate at that sentence.

**13. MINOR. The range is one factor's swing, said as if it were the whole range.**
Quote: "between about 2,900 and 8,600; the share of people who ride sets the range." S40 says every
other factor is held at its central value; the transcript drops that. It happens to land near a
combined band. With each factor's range treated as a triangle, a 90 percent band is about 3,500 to
8,100. Combining the six end-of-range swings in log terms gives about 2,600 to 9,500. Every factor at
its bad end at once gives 1,400 to 16,600. The candidate should be able to say which of these the
stated range is. The next follow-up: "Is that with everything else fixed?"

**14. REJECT. AI variant: the guardrails cannot catch what the answer says they catch.**
Quote (follow-up 2): "It can be padded with long suggestions, which is why revert rate and build
failures sit beside it." Long boilerplate that compiles and is never reverted passes both checks.
What catches padding is a ratio: retained characters per accepted character, the suggested share of
all committed code, or edits per accepted suggestion. Quote (follow-up 1): "the guardrails tell us
whether it fell because suggestions got worse or because developers write more themselves". Neither
build failures nor revert rate measures how much developers write themselves. The day's own method
gives the answer, which is a decomposition: retained text per developer-week = suggestions shown x
share accepted x size accepted x share retained. That names the factor that moved. Add an A/B test
of the model change, which is how AI companies ship models. The next follow-up: "Which of your
guardrails moves if suggestions get longer and no better?"

**15. REJECT. AI variant: no evidence the new north star tracks value, no test, and the best-known study points the other way.**
Ziegler and colleagues at GitHub, "Productivity Assessment of Neural Code Completion" (arXiv
2205.06537, 13 May 2022, MAPS '22; verified 12 October 2026), found that the rate at which shown
suggestions are accepted, rather than measures of whether completions persist in the code, drives
developers' perception of productivity. A head of product at a coding-assistant company knows that
paper. The answer asserts "it can rise while the product helps less" with no number, and proposes
paying the team on retained text without a test. Monday's version of the same variant had "the test
is a holdout of users"; Tuesday's dropped it. The question also hands over the conclusion ("You want
the team to optimise something else"), so the answer never has to argue the part a head of product
would dispute. The missing depth: tie both measures to an outcome the business is paid on, such as
renewals, seat expansion, or task time in a holdout. METR's randomised study (10 July 2025, 16
developers, 246 tasks; verified 12 October 2026) found tasks took 19 percent longer with AI tools
while the developers believed they were about 20 percent faster. The page now points to a February
2026 follow-up. Either way, it shows that neither a proxy nor self-report is the outcome. The next
follow-up: "GitHub's own study found acceptance tracks perceived productivity better than retention.
Why would I pay my team on retention?"

**16. REJECT. AI variant: the window, the denominator and the unit are undefined.**
"present at the next commit" is a different window for every developer. Someone who commits every
ten minutes keeps more suggested text at the next commit than someone who commits nightly, for the
same suggestions. "per active developer-week" leaves "active" undefined, and if active means
"accepted at least one suggestion", the denominator selects on the outcome. "suggested text" has no
unit. This is criterion 2 failing on the day that teaches criterion 2. The next follow-up: "Two
teams use the tool identically; one commits hourly, one daily. Do they get the same north star?"

**17. SHALLOW. AI variant: the deck keeps a number the analyst has just called inflatable, and nothing is priced.**
Quote (follow-up 3): "Acceptance, with its definition printed, while the team's target is the
retained text." Quoting to customers a number you have argued "can rise while the product helps
less" is a credibility risk, and the answer never names it. Once the team optimises retained text,
acceptance can move either way, and nobody owns the deck number when it falls. Paying the team on a
measure the answer admits can be padded invites the padding. The answer also never mentions serving
cost, an AI company's main variable cost; a north star that counts retained text rewards showing
more suggestions. The next follow-up: "When the team optimises retained text and acceptance falls
from 32 to 26 percent, what does sales tell customers, and what did the extra suggestions cost to
serve?"

### C. Too shallow for a hire

**18. SHALLOW. Transcript 1 never says what the Rs 1.9 crore bought, so the obvious alternative goes unanswered.**
The city head's decision is whether the spend was worth it, and the case gives the answer. Trips
rose by 6,700 (224,200 to 230,900), so the top-up cost at least Rs 2,836 per extra trip worth
Rs 165, and more if some of those trips came from the 1.8 percent rise in requests. Gross bookings
rose about Rs 11 lakh. A hire at Uber puts the cost per extra trip (or per extra request served,
about Rs 7,400) beside the options: end the scheme, keep it, or redesign it. The next follow-up:
"Why not end it and save the whole Rs 1.9 crore?" The answer has no line for that.

**19. MINOR. Transcript 1's claim and its number measure different things, and one word is jargon for this listener.**
The claim is about "online hours that carry no trips", but the number offered is the top-up paid to
"driver-weeks that accepted fewer than half their offers". The direct evidence exists and goes
unused: the no-trip share of online hours rose from 0.22 to 0.38, and 72 percent of the
low-acceptance driver-weeks' online hours had no trip. "Driver-weeks" is also an analyst's unit, out
of place in a two-minute pitch to a non-technical city head.

**20. SHALLOW. The acceptance floor has no level and no check against gaming.**
"an acceptance floor" at what share? Drivers clear a floor by the minimum, and they can accept and
then cancel: driver cancels after accepting already rose from 0.04 to 0.09. Some outer-zone declines
are fair (long pickups), which Monday conceded ("some declines are fair; the floor sits in the gap
the data shows"). The next follow-up: "Where do you set the floor, and what stops drivers accepting
and then cancelling?"

**21. SHALLOW. Transcript 2's clarifications miss what an Indian ride-hailing screen expects.**
Three are missing. Which products: cars, autos and bikes have different trip times and different
driver pools. Multi-homing: a driver online on Uber may be on another platform's trip, so the idle
share overstates who is free. And whether the five-minute median is for the city or for every zone
(finding 11).

**22. SHALLOW. The [D] answer is one move used for every conflict.**
The notes' "Where does this get tested?" and the day sheet both give: "Concede their true part
first, keep their visible number as a leading input". The day also uses that move for marketing's
objection and for the AI variant. A strong candidate adds how adoption actually happens: meet each
owner before the meeting, agree the test and its decision rule in advance, and set a date when the
old target retires.

**23. SHALLOW. Rung Q1 is a recognition item labelled L6.**
Only option b opens on a claim; a, c and d are method or numbers. So the item tests whether a learner
can spot a claim sentence, not their judgment. An interview-grade version would add a claim-first
distractor that uses the flattering denominator ("The guarantee works: bookings per driver-week rose
0.8 percent"), or one that overclaims ("The scheme caused a 17 percent fall in earnings per hour").

**24. MINOR. Rung Q2's solution reasons loosely.**
The line "two equal north stars let each team quote the one that flatters it, which is the
per-driver-week trap again" stretches the analogy. The hire-grade answer's own plan ("We report both
for a quarter") also sits close to option c. The solution should say what separates them: which of
the two numbers the team is paid on.

### D. The guesstimates, step by step

| Step | Arithmetic | Logic |
|---|---|---|
| Requests an hour: 1 crore x 1 percent = 1 lakh; x a quarter = 25,000; / 3 = 8,333 | Right | Riders become trips with no trips-per-rider factor (finding 10). The "requests" are completed trips, while 11 percent of the case's requests went unserved, so the chain sizes for demand that was already being met |
| Trips per online driver-hour: 2.4 x 0.70 = 1.68 | Right | 25 minutes from accepting to dropping is a fair stated assumption. The check on the idle share uses a different definition (finding 8) |
| Buffer: 8,333 / 1.68 = 4,960; x 1.15 = 5,704 | Right | The buffer is defined for the busiest half hour, so it must change with the window (finding 9) |
| Range: a ride share of 0.5 to 1.5 percent gives 2,852 to 8,557; the other five swings as stated | Right | Among the stated factors the ride share does set the range, but the unstated trips per rider moves it more (finding 10). One factor's swing is given as the range (finding 13) |
| Validation: 0.595 / 0.468 = 1.27 | Right | It compares per request with per trip, and seven days of both windows with weekday evenings (finding 7). The trim then lands on the buffer, which is outside the comparison |
| 256,556 / 252 = about 1,018 requests an hour | Right | Fine as stated |
| UPI: 35 crore x 2 = 70 crore = 700 million, 13 percent below 802 million; swings of 50 to 90 crore and 35 to 105 crore | Right | Finding 25 |
| UPI catch: 24.07 billion / 30 = 802.3 million; / 31 = 776.5 million, 3.2 percent low | Right | Correct, but immaterial at guesstimate precision (finding 25) |
| Kalpa: 50,000 x 0.4 = 20,000; x 0.05 = 1,000; 20,000 x 2 x Rs 1,500 x 12 = Rs 72 crore; Rs 66,968 crore / 500 = Rs 133.9 crore; / 457.5 = Rs 146.4 crore, 9.3 percent apart; 72 / 133.9 = 0.54 | Right | Finding 26 |

Nothing is double-counted now. The facts file records that a draft once divided by an idle share on
top of trips per online hour, and that this was corrected.

**25. SHALLOW. The UPI catch is real arithmetic with nothing at stake, and a sharper check sits in the same source.**
A 3 percent slip in the divisor, against an estimate whose own range spans a factor of three (35 to
105 crore), changes no decision. Yet the day sheet stages it as a trap ("A pair's estimate judged
against a figure 3 percent low"). The same report gives a check that teaches something.
Rs 29.37 lakh crore over 24.07 billion is about Rs 1,220 a transaction, and the report's daily value
(Rs 97,913 crore over 802 million) agrees. That is far above "a tea, a recharge or a transfer", so
the count holds large person-to-person transfers. The "about 2 a day" factor therefore needs the
split S43 asks for ("split between paying shops and paying people"), and the worked chain never
makes it. The figure of 35 crore active users has no anchor at all.

**26. SHALLOW. The Kalpa check tests the link it can reach rather than the one that sets the range, and it cannot fail.**
The chain's widest factor is the sign-up share: 0.02 to 0.08 gives 400 to 1,600 sign-ups, against
600 to 1,600 from households and 625 to 1,250 from the share who shop. The DMart comparison checks
only households times the share who shop. The note gives no range for sign-ups and names no driving
factor, although the day sheet's answer says "give the range and its factor". "About half a mature
store passes for a first-year store" sets no band that would fail, so it is not yet a check. DMart's
revenue per store is a hypermarket average across store sizes. A like-for-like comparison needs
sales per square foot or a matched format, and the right anchor for sign-ups is the Retail-Plus
sign-up rate at Kalpa's existing stores.

### E. Real-world facts and their sources

| Fact | Where | Source and date beside it? |
|---|---|---|
| Uber's Hyderabad peak-hour guarantee and its numbers | extras, notes, half two | The extras and notes carry the illustrative label. Half two's cover has carried it since 19:44 today (finding 28) |
| "About 1 crore people" in Hyderabad | extras T2, S38, guesstimate note | No. The note calls it "A round number said aloud, to be checked", and no check is recorded |
| The monsoon ending inside the after window | extras T1 and its follow-ups | No date or IMD source; covered only by the illustrative label |
| No published count of Uber drivers online at Hyderabad's peak | extras, S34, S41, note | Yes: a dated search on 12 October 2026, in the note |
| Aced: interviewers evaluate the framework, not a precise number | S36 | Yes, "checked 12 October 2026", but the slide says more than the source (finding 27) |
| NPCI: 802 million a day, 24.07 billion in September 2026 | S44, notes, note | Yes: Outlook Money, 2 October 2026, citing NPCI, checked 12 October 2026. Verified today. It is a secondary source; NPCI publishes its own monthly figures |
| India about 140 crore people; 35 crore active UPI users | S44, note | No; labelled as assumptions and never anchored |
| DMRC: 64.06 lakh journeys a day; 82,44,903 boardings on 17 September 2026 | S45 | Only in the notes fence (The Tribune, 9 August 2026; Republic World, 18 September 2026; checked 12 October 2026), not beside the claim. Not re-verified here (finding 29) |
| Flipkart: 6.3 million concurrent users in a minute, 9 October 2026 | S45 | The date is on the slide and the source is named. Verified today (finding 30) |
| DMRC line utilisation, 2018 | S45 notes | Yes: PTI, 30 May 2018 |
| DMart: Rs 66,968 crore, 500 stores, 85 added, 10.8 percent growth for older stores in Q4 FY26 | guesstimate note, day sheet | Yes in the note (Avenue Supermarts, 2 May 2026, checked 12 October 2026). The day sheet's "Rs 134 crore to Rs 146 crore" has no source beside it. Not re-verified: the NSE archive returned 503 on 12 October 2026 (finding 31) |
| "asked in every screen, product companies most of all"; "asked in AI-startup and product-company screens"; the [S], [F] and [D] tags | rungs, notes | No (finding 32) |
| Acceptance rate of 32 percent | extras, S51 | Labelled as invented |
| Outside S33 to S52: Amazon's memo line on S53 | half two | No date on the slide; the notes give the letter's filing date |

**27. FACT. S36 attributes to Aced what Aced does not say, and S43 goes further.**
S36 reads: "Interviewers score the structure and the sanity check, and hardly ever the final number.
Aced's analyst guide says the interviewer is evaluating the estimation framework and wants each
assumption stated so it can be challenged (checked 12 October 2026)." The page, fetched on 12 October
2026, says "The interviewer isn't looking for a precise number" and "They're evaluating your
estimation framework". It never mentions a sanity check, and it never says the final number is
hardly ever scored. S43 adds "The final number scores nothing on its own." A real interviewer marks
down an answer of 41,700 however good its structure, which is exactly the day's own S42 trap. The
sentence comes from the curriculum row (W4_Analyst_craft.md, Tuesday's "Thinking we train"), so the
fix starts there.

**28. MINOR. Half two's label arrived during this read; S41's note still describes a label its slide does not carry.**
When I began reading, half two's cover named "The Hyderabad city head, Uber" with no illustrative
line anywhere in the deck. Commit c8d6b57 (19:44) replaced the cover with "Header: WEEK 4 · DAY 2 ·
UBER, HYDERABAD, AN ILLUSTRATIVE CASE", which settles the deck. What is left is small. S41's note
reads "Synthetic, labelled: these are the case's numbers, not Uber's", but S41 itself carries no
label, and neither do S50 and S56, the slides a learner is most likely to lift and quote alone.

**29. FACT. The Delhi Metro row has no source on the slide and may not show a difference of unit.**
"DMRC reports 64.06 lakh journeys a day and, separately, a record 82,44,903 boardings on 17
September 2026": the sources sit only in the notes fence. The row is labelled "A different unit",
but as written it compares an average day with a record day, which is a difference of period. No
file says whether DMRC counts an interchange once in "journeys" and twice in "boardings". An
interviewer who knows how DMRC counts will ask.

**30. FACT. Flipkart's own figure mixes a moment with a minute, and the day quotes it as the clean number.**
The verified wording is "Flipkart recorded 6.3 million concurrent users in a minute". "Concurrent"
is a count at one moment, and "in a minute" is a count over a window: the distinction this day
teaches with drivers online. The decimal trap stands, but the deck should also say that the unit is
muddled.

**31. FACT. DMart's older-store growth is misquoted, and a motive is invented.**
The guesstimate note says "two-year-old stores ... grew 10.8 percent", while its own facts file
records "two years and older". And "which is why DMart reports its two-year-old stores separately"
gives a reason no source states; reporting like-for-like growth on mature stores is standard
practice.

**32. FACT. What gets "asked" is stated as market fact.**
"Level L6 · asked in every screen, product companies most of all" and "asked in AI-startup and
product-company screens" carry no source. The tags are the programme's own calibration, as the
curriculum row says ("This programme's own calibration for 0-3 year Indian-market candidates"). The
notes' "Where does this get tested?" uses [S], [F] and [D] without saying what they mean.

### F. What would embarrass the programme in front of a real interviewer

**33. MINOR. A candidate says "The published count for the city is to be found."**
That is the house placeholder in a candidate's mouth. In a screen it would be: "I don't know a
public count; I'd check Uber's supply dashboard for drivers online at peak."

The rest, most embarrassing first: the S50 operator (finding 12); the explanation that blames the
joiners (1); the four-hour window that shrinks the city's need (9); the validation that breaks the
day's own three-word rule (7 and 8); the guardrails that cannot catch padding (14); and the Aced
line (27). Each is the kind of slip a hiring interviewer takes a screenshot of.

### Other minor items

**34. MINOR. The day sheet's one-breath answers leave out the drivers estimate the learners rehearse.**
It carries the row's "[S] A guesstimate: how many customers could a new store sign up to a loyalty
tier", while the spine, the transcript, the deck and the notes all use drivers at the evening peak.
Its presentation answer also names a signer ("the city head signs a test first") that the student
hire-grade answer leaves out.

**35. MINOR. The notes' weak-answer column names the wrong failure for the drivers question.**
It gives "One confident number with no range", but the transcript's weak answer fails on the unit (a
day's trips divided by an hour's rate), which is the day's staged trap.

**36. MINOR. The idle tail is defined by the outcome.**
The notes' objection table now answers driver operations with "The other 880, there before the
launch, held at 1.90 trips per online hour" (it read "The other 1,020 held at 1.90 to 1.89" before
commit 1975ae0). The tail is defined as the drivers whose trips per hour fell under 1.0 after the
launch, so the rest holding up is partly built in. The data holds the line that helps, since the
tail also ran at 1.90 before the launch, and no file says it. This feeds the [F] answer on
objections.

**37. MINOR. Transcript 1's trap line is worded backwards.**
"quoting the read that flatters the claim": the per-driver-week read flatters the scheme and cuts
against the claim.

### Where I disagree with the trainer scorecards (opened after section A was written)

| Answer | Scorecard | Mine | Where we differ |
|---|---|---|---|
| Transcript 1, hire-grade | 14 | 11 | Scope (2 against my 1), trap (2 against 1), what would change their mind (2 against 1) |
| Transcript 2, hire-grade | 13 | 8 | Trap (2 against 1), unit (2 against 1), what would change their mind (2 against 1), decision (1 against 0), structure (2 against 1) |
| AI variant, hire-grade | 13 | 6 | Scope, denominator and window, and trap (2 against 1 each); unit (1 against 0); what would change their mind (2 against 0); decision (2 against 1) |
| Transcript 1, weak | 2 | 3 | Denominator (0 against 1: "trips per hour fell from 1.90 to 1.58" names one) |
| Transcript 2, weak | 1 | 2 | Denominator (0 against 1: "2.4 trips an hour" names one) |
| AI variant, weak | 1 | 2 | Trap (1 against 0: the answer falls into the trap's first half), decision (0 against 1), structure (0 against 1) |

**38. REJECT. The scorecard marks up what a strong interviewer marks down.**
It credits lines from the follow-ups to the main answer. For criterion 5 it cites "last year's weeks"
from transcript 1's follow-up 3 (weeks the candidate says do not exist), "Uber's own peak requests"
from transcript 2's follow-up 3, and "The guardrails read first if retained text falls" from the AI
variant's follow-up 1, which is also not a fact that would change anyone's mind (finding 14). It
applies the rupee rule unevenly on criterion 6. Transcript 2 is held at 1 for want of a named cost,
while the AI variant gets 2 with no cost at all. The sentence the key offers to earn transcript 2's
2 ("so the peak incentive should be sized for about 5,700 drivers, not 41,700") names a decision
without rupees, which S52 scores 1. On criterion 3 it accepts a wrong reason (transcript 1's "said
why it is not what the scheme pays for"; see finding 1). If pairs compare their scores with this key,
the room learns that these answers are flawless.

**39. REJECT. The scorecard's follow-up table scores the sound four-hour-window answer as the weak one.**
The table reads: "The window is three hours. What does a four-hour window do? | Changes nothing,
because the window never entered the chain". At the busiest moment the requirement does not change
(finding 9). A trainer holding this key would mark down the candidate who says so, and would mark up
the 4,300.

**40. MINOR. Smaller errors in the key.**
The AI variant's unit criterion gets 1 although there is no unit; S52's 0 is "no unit". Transcript
1's unit criterion cites "Rs 58 lakh to Rs 92.7 lakh over six weeks with its assumption", but the
assumption the transcript states (half or a fifth of the drivers start accepting) is not Monday's
(half or a fifth of the money is still paid; finding 2). For transcript 2's trap,
"did not count idle time twice" credits the candidate with a correction from the build history,
not with anything the candidate said. The seven criteria are attributed to "Aced's account of what
interviewers listen for". Aced's page covers structure over a precise number, stated assumptions and
scoping questions. Denominator and window, decision and cost, and what would change your mind are
the programme's own criteria.

### Counts by mark

| Mark | Count | Findings |
|---|---|---|
| REJECT | 17 | 1 to 12, 14, 15, 16, 38, 39 |
| SHALLOW | 8 | 17, 18, 20, 21, 22, 23, 25, 26 |
| FACT | 5 | 27, 29, 30, 31, 32 |
| MINOR | 10 | 13, 19, 24, 28, 33 to 37, 40 |
| **Total** | **40** | |

Sources fetched for this read, all on 12 October 2026: arXiv 2205.06537 (Ziegler and colleagues,
2022); metr.org, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer
Productivity" (10 July 2025); the Outlook Money UPI report (2 October 2026); Flipkart Stories (9
October 2026); and the Aced guide. The Avenue Supermarts release at the NSE archive returned 503, so
the DMart figures were not re-verified.

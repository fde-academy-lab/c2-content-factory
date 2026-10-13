# Sources, W04 D2 (Tuesday 27 October 2026): what the pack rests on, what it changed, and why

Built by the W04 D2 finishing session on 12 October 2026 from `docs/detailing/W04_analyst_craft_spine.md`
(section 6), `docs/detailing/W04_case_file.md` (Tuesday) and Monday's tables, and rebuilt concept first
on 13 October 2026 on branch `w04-d2`. Data command:
`python3 content/W04/D2/internal/C2_W04_D02_make_data_INTERNAL.py`, then the figures, notebooks and
audit scripts beside it (`C2_W04_D02_figures_INTERNAL.py`, `C2_W04_D02_build_notebooks_INTERNAL.py`,
`C2_W04_D02_facts_audit_INTERNAL.py`), and `C2_W04_D02_renumber_INTERNAL.py` once after the decks were
assembled. Tools on 13 October 2026: Python 3.13.16, pandas 3.0.5, matplotlib 3.11.2, PyYAML 6.0.1,
nbclient 0.11.0, nbformat 5.11.1, python-pptx 1.0.2, mermaid-cli 12.0.0, WeasyPrint 70.0, LibreOffice
24.2.7.2.

## What did the concept-first rebuild of 13 October 2026 change, and what does it rest on?

The row's five subtopics now lead, each as its own chapter on an invented example, in the row's
order: SECTIONs 1 to 3 in the morning, 4 and 5 applying them to Uber, 6 and 7 after studio round two,
then 8 to 10 applying them. The case's numbers, traps, transcripts and Kalpa lab are unchanged except
where a beat moved; `C2_W04_D02_slide_map_INTERNAL.md` maps every merged slide number to its new one.

### Which references lock each topic, and when were they checked?

| Topic | Written reference, checked 13 October 2026 | Video, checked 13 October 2026 (title and channel read through YouTube's oembed endpoint) |
|---|---|---|
| 1. The one-slide answer: claim, evidence, caveat, action | Management Consulted, "The Pyramid Principle" (page updated 2 September 2026): it "starts with the conclusion first, then organizes supporting points underneath it"; WebFetch returned 403 and curl with a browser user agent returned the page. https://managementconsulted.com/pyramid-principle/ (checked 13 October 2026) ; Barbara Minto's own site, https://www.barbaraminto.com/ (checked 13 October 2026) | Analyst Academy, "Consulting Slide Structure: How McKinsey, Bain, and BCG create slides", https://www.youtube.com/watch?v=ZXslsi3jK6Y (checked 13 October 2026) |
| 2. What to leave out, and the appendix | Storytelling with Data, "a new year's resolution: declutter your graphics" (4 January 2011): "Is it adding any informative value? If the answer is no, then take it out!" https://www.storytellingwithdata.com/blog/2011/01/new-years-resolution-declutter-your (checked 13 October 2026) | storytelling with data, "How to eliminate clutter from Excel graphs", https://www.youtube.com/watch?v=XgY1-BsZSzM (checked 13 October 2026) ; it covers what leaves a chart and says nothing about an appendix, so the appendix half's video is to be found |
| 3. Defending under challenge: restate, answer, concede, what would change your mind | The Marginalian, "How to Criticize with Kindness: Philosopher Daniel Dennett on the Four Steps to Arguing Intelligently" (dated 6 October 2026 on the page), quoting Rapoport's rules from Dennett's Intuition Pumps: re-express the target's position "so clearly, vividly, and fairly" that the target says "Thanks, I wish I'd thought of putting it that way". https://www.themarginalian.org/2026/10/06/daniel-dennett-rapoport-rules-criticism/ (checked 13 October 2026) | Stanford Graduate School of Business, "Answering Tough Questions", https://www.youtube.com/watch?v=hSeAGSPDG4w (checked 13 October 2026) |
| 4. The guesstimate: clarify, map, calculate, validate | Think Insights, "Guesstimates" (3 December 2018), the row's own reference, whose four steps are the row's: the interviewer "is interested in your thought process; not the final result", and "the best candidates validate their results & try to spot their own mistake before telling their interviewer they are done". https://thinkinsights.net/strategy/guesstimates (checked 13 October 2026) ; Aced, "The interviewer isn't looking for a precise number", https://www.aced.io/blog/top-data-analyst-interview-questions (checked 13 October 2026) | Hacking the Case Interview, "Market Sizing: Full Tutorial for Beginners", https://www.youtube.com/watch?v=8_9I8XMFNfs (checked 13 October 2026) |
| 5. The AI-free written business case | Amazon's 2017 letter to shareholders, filed 18 April 2018: "We don't do PowerPoint (or any other slide-oriented) presentations at Amazon"; memos read silently at the start of each meeting; a great memo "probably should take a week or more". https://www.sec.gov/Archives/edgar/data/1018724/000119312518121161/d456916dex991.htm (checked 13 October 2026) | ProjectManager, "How to Write a Business Case - Project Managment Training" (the title's spelling), https://www.youtube.com/watch?v=UQP5MmCAQ3Y (checked 13 October 2026) ; for why Amazon writes memos, Lex Clips, "Jeff Bezos on banning Powerpoint in meetings at Amazon", https://www.youtube.com/watch?v=e47wAgIhZ7o (checked 13 October 2026) |

The case file marks the Think Insights and Management Consulted pages "not to be used" because both
returned 403 on 12 October 2026. Both loaded on 13 October 2026, so the rebuild uses them with that
date; the requester's direction to use the row's references first decides it. IGotAnOffer's
market-sizing page returned 403 again on 13 October 2026: not verified on 13 October 2026, and not
used.

### Which decisions did the rebuild take, and why?

- **Notebook numbers follow SECTION numbers.** Notebooks 01, 02, 03, 06 and 07 are the concept notebooks; 04, 05, 08, 09 and 10 the case notebooks; the lab notebook takes 11, the number after the day's last SECTION. Chapter 9's page stays handwritten with laptops closed, so notebook 09 is opened after hand-in, recounting the brief's numbers and running the page rules on a typed copy; notebook 10 recomputes every number the hire-grade answers speak. The orchestrating session's note of 13 October asked that every chapter keep its notebook, so the coverage gate shows no WARN.
- **Every notebook defines only `check`.** The spine's acceptance line 13 and its rule of no helper layer allow no other definition, so the sort, the four moves, the swing, the validate step, the page's five rules and the spoken-order test run as plain loops, tables and `check` lines. The your-turn cells of notebooks 07 and 09 type the five rules as five `check` lines, and the lab's your-turn pastes the canteen cell's chain and swing lines under the learner's own `ledger`; each snippet was run with its blanks filled before the push.
- **SECTION 2's heading uses the row's words plain.** While `scripts/build_deck.py` kept a topic that opens on a question word whole, the unsplit cover overflowed (deck_check failed slide 15 by 25 px), so the heading quoted the Name for a while; pull request 254 on main fixed the builder, the branch merged it, and the quotes are gone.
- **The canteen has new invented numbers.** The merged pack's 2,000 x 0.6 x 2 = 2,400 became 3,000 x 0.45 x 2 = 2,700 with a till of five weekdays averaging 2,340, so the validate step meets a counted number; the guided set and the trainer files use the new ones.
- **The Kahoot.** Every item names the topic it tests; Q8 now tests the written case, and the old Q8 (31 billion in a 31-day month) moved to the chapter 6 set as Q6.
- **Minutes.** The concept chapters' 112 minutes came from studio round two (40 to 20, two turns and a rebuild), the interview room's live minutes (25 to 12, transcripts 2 and 3 now the evening's reading), the close (40 to 20, the gallery staying cut), the opening (15 to 5, the roles' losses moving into chapter 4) and the case chapters' own trims; the morning's S30 activity runs 5 minutes so the morning holds 180. The day sheet carries the before and after table.
- **The written case runs 35 minutes**, as chapter 9 does; its brief had said forty.
- **The facts audit** now homes a number a notebook prints from one of the day's own data tables, since a concept notebook prints its invented table in full; prose numbers still need a facts id.
- **The facts file's `used_by` slide numbers predate the rebuild.** Most are the merged pack's numbers, which the slide map translates; 38 come from an older numbering that restarted in half2. The `toy_` ids added on 13 October name SECTIONs instead of slides.
- **Sizes.** The decks run 59 and 44 slides against the artefact row's "about 48" and "about 38", inside its caps: half1 carries 30 case slides of at most 35, half2 28 of at most 30, and each concept chapter 7 to 9 slides with its opener, within 6 to 12. The notes run 2,970 words after the humanizer read (prose and tables, without diagrams, image lines, table rules or URLs), under the acceptance line's 3,000 and above the row's "about 2,000"; the fix pass added about 300 and the same pass cut them back by tightening chapters 1, 2 and 7 and the case section.
- **The Kalpa lab notebook** sets up the tools and the anchor and leaves the sizing to two empty cells, so the worked answer (about 1,000 sign-ups) stays in the TRAINER note and the lab set's solution.
- **The DMart table** `data/C2_W04_D02_kalpa_dmart_anchor_STUDENT.csv` carries both per-store figures, which answer the Kalpa store set's Q1; it stays byte-identical to the merged pack, as the brief requires of the case tables, and notebook 11 prints only its first four rows.

- **Ramesh's shop sells Rs 11,900 to Rs 12,600 a day** where the spine's table wrote Rs 12,000 to Rs 13,000: the lab set's food stall already takes Rs 12,000 in a day, so the shop's numbers moved to stay apart, and they were chosen so that sales per customer hold at Rs 100 and sales per hour land on Rs 1,190 and Rs 1,050.
- **The two mid-session drills keep the spine's minutes**, which give way to the row's 15 each: drill 1 runs 6 minutes inside SECTION 5's 12 for the drawer (spine section 6), and drill 2, the four estimates, stays in `exercises/unguided/` for the lab when chapter 8 runs short.
- **The Kahoot keeps two departures from the row.** Q5's city of two million holds eight million households, the merged pack's figure the brief keeps, where the row and the spine's L5 say nine; Q2's "keep or cut" offers four candidates, since a Kahoot item carries four answers, where the row lists six elements.
- **Anand's store question in STUDENT files** (the Kalpa store set, the lab set, the slide template and notebook 11) carries no status, while the row marks it proposed for client zero v2.3 and trainer only; the merged pack stated it the same way, so the rebuild kept it and leaves the ruling to the orchestrating session.

### What did the rebuild invent, and where is it recorded?

Ramesh's kirana shop (56 days, eight draft elements, the draft and the page), the auto driver's two
days, Gulmohar Secondary School's sixteen weeks and its board exam, the campus canteen's ledger and
till, the town of 24,000 people and the phone pack. Each is written by the generator to `data/` where
a notebook loads it, and each number sits under a `toy_` id in `C2_W04_D02_facts_INTERNAL.yaml` with
what it was invented for and where it is used; every file that shows one says invented.

### What did the rebuild's three cold reads change, and what stays?

The trainer's read (15 findings), the fresh graduate's (27: 10 confusing, 17 minor) and the hiring
interviewer's (21: 11 reject, 6 shallow, 1 fact, 3 minor) are in `C2_W04_D02_cold_reads_INTERNAL.md`,
each with what became of every finding. No read returned "not found" against a subtopic. The one fix
pass took these decisions.

- **Chapter 1 reads the extra hours on their own.** A falling average per hour does not show that added hours fail to pay, so the evidence divides by what the decision buys: the two added hours sold at most Rs 350 each (`toy_kirana_extra_hour_rs`), against Rs 1,190 in an old hour. The shop's records hold no cost of goods, so the claim keeps its action, counting the evening on its own; no margin was invented to settle it.
- **The shop's rain days are two in each month.** Five against two was a second seasonal cause of the same Rs 700, which chapter 2 then cut as irrelevant. The generator moved three September rain days and rebalanced their customers, so every monthly total, rate and toy value except the rain count is unchanged; every October day still sells less an hour than every dry September day.
- **The written page has five rules, in the same words everywhere.** S69 gained the method-word rule that S84, the brief and the checklist already asked; the rules cell in notebooks 07 and 09 now checks exactly those five, typed one part a line. The 250-word ceiling and the four-to-six-sentence check left it: the model page and real handwritten pages run past 250 words while still one page, and the plan's guard only asked that a ceiling, where stated, be labelled the pack's own. The generator still asserts that Ramesh's page runs under 250 words.
- **The saving keeps Monday's figures and says what they rest on.** Rs 58 lakh to Rs 92.7 lakh stays Monday's arithmetic, so the two days agree; every spoken use now names the enrolled drivers, the six weeks, the half-to-a-fifth assumption and the per-trip rate that decides where it lands, fixed before the test. "City-wide" is gone.
- **The test keeps Monday's design and names its bias.** Half the enrolled drivers, picked at random, as Monday set it; the transcript, the model page and the scorecard add that both halves serve the same riders, read the city's totals beside the comparison, and offer a whole-city alternation week by week as the cleaner design. The zone waits guard the city, with a stop line at any zone's median above its level before the launch.
- **The AI variant counts suggestions, per paid seat, against renewals.** Both shares are now of suggestions; the denominator is the paid seat; padding is caught by characters per accepted suggestion and a monthly reviewed sample; a check across last year's renewals replaces the holdout of users, since accounts renew yearly; METR is cited for the perception gap alone, re-read on 13 October 2026.
- **Two-app drivers push the idle share up.** S73's earlier "lean it low" ran the wrong way; S73, the scorecard and the guesstimate note now lean it high, which raises the answer.
- **Who quotes per driver-week** is the driver-operations lead, as notebook 04's table had it; S40's notes said marketing.
- **New and changed facts ids.** Added: `toy_kirana_extra_hour_rs`, `idle_hours_per_week_before`, `idle_hours_per_week_after`, `idle_trips_fall_pct`, `others_hours_per_week_rise`, and Monday's `idle_hours_per_driver_week_after` reused. Changed: `toy_kirana_rain_sep` from 5 to 2; `pre_launch_rs_per_dw_after` kept to one decimal (5,895.4) so notebook 04's hand division gives its printed 1.4 percent. Removed: `idle_topup_per_hour_rs` (about Rs 276 an hour), whose only use was the S30 note that cold read 4 could not reconcile.
- **Kept, with reasons.** "North star" stays undecoded on S65, since the draft's method words are the problem the slide shows; the "Styles:" lines stay in SECTION notes, the pattern of every Week 4 deck; the cover title stays the row's Day focus; the sheet's "Panel n:" prefixes are its builder's format.
- **For the orchestrating session, outside this day's files.** Monday's idle tail drew Rs 1.159 crore of top-up over 42,000 hours, about Rs 276 an hour, while its fares came to about Rs 131 an hour; under a floor of Rs 300 an hour checked window by window on the driver's share of the fares, the floor over 42,000 hours is Rs 1.26 crore, so the top-up can reach Rs 1.159 crore only if the driver keeps at most about 18 percent of the fare (Rs 1.26 crore less the share times Rs 55.2 lakh of fares), a share a sharp learner can question. Tuesday quotes Monday's caveat that the top-up cannot be rebuilt from bookings and no longer prints the per-hour figure; the data is Monday's to settle.

### What did the check of the fix pass find, and what changed after it?

A fresh agent checked the files against all 48 findings of the graduate's and the interviewer's
reads: 38 resolved, 9 partly, none open, and 8 problems the pass had made. The largest was that the
pass credited the per-driver-week rise to the idle tail, whose own weeks earned 12 percent less; the
rise sits with the other 880, who drove about 4 percent more hours at an unchanged Rs 313.5 an hour.
Every item it left open is fixed, as the cold reads file records item by item. Ramesh's page now
carries the added hours' Rs 350 (118 words, 7 numbers); the saving's rate can move it within the range
or beyond it, and its rule pays the drivers who already accept what the floor paid them; the drill's
table carries the bus strike and the 2023 line rule from the sources recorded on 12 October 2026.
Two fresh re-scores of transcript 1 followed: the first held scope at 1 and asked for a shorter answer,
a margin on the stop rule and the before-launch control in the monsoon answer; the second scored 2 on
each of S90's first three criteria and asked for the rate to be priced. The answer now fixes the
rate at what keeps the drivers who already accept whole, about Rs 38 a completed trip, at which the
whole scheme costs at most about Rs 87 lakh over six weeks, and stops the test early only on a zone's
median wait more than half a minute above its last six weeks' level, two weeks running.

### Which house reads ran on the rebuilt pack, and what did they change?

Two fresh agents ran the humanizer read in file mode on 13 October 2026 and edited nothing: one over
the decks, the notes, the cheat sheet, the pre-read, the board work and the transcripts (10 findings),
the other over the exercises, the Kahoot, the take-home, the trainer files and the notebooks' prose in
the build script (12 findings). All 22 are applied. Three of them corrected facts as well as wording:
the chapter 6 set said three checks where its items hold two, the rungs solution said three openings
lead with a claim or a method where all four do, and notebook 08's trap question read as an hour's
cost. The tic scanner then read all 53 files clean.

### What did the acceptance test find at the end, and what changed?

The spine's acceptance lines 0 to 17 were read against the pack after the house reads, and four
lines needed a change before they held.

- **Line 13.** Ten notebooks defined functions beside `check`; every one now defines only `check`, as
  the decision above records, with 127 checks still passing.
- **Line 11.** The cheat sheet had lost the twelve rows when its panels moved to the five topics;
  panel 7 now reads them beside all driver-weeks, and the sheet still prints on one page.
- **Line 12.** Chapters 5, 9 and 10 closed without a map node; S54, S85 and S90 now add theirs, as
  every other chapter close does, with every diagram label at 9 points or more.
- **Line 2.** Chapter 7 showed its counts as a picture; S68's notes now open on a hand count of the
  draft's method words. The twelve rows' Rs 165 a trip matches the full data by the spine's own L1
  and L2 design, since the fare is the ticket's stated constant.
- **Line 14.** The second re-score gave transcript 1 a 2 on each of S90's first three criteria and
  the check of the fix pass gave transcripts 2 and 3 the same; the second re-score's four
  rejections are fixed, and a third read was started and then stopped unread at the orchestrating
  session's request, so no read has followed those fixes.
- **Merge of 13 October.** Monday's concept-first rebuild came in from main; Tuesday's generator
  re-ran with its 108 checks passing and no data or facts changed, and Monday's kirana is Balaji
  Kirana, apart from Ramesh's shop.

## Which public sources were fetched, and when?

All fetched and read on 12 October 2026.

| R2 id | Source and what it supports | URL |
|---|---|---|
| T3 | Outlook Money, 2 October 2026, citing NPCI: 802 million UPI transactions a day in September 2026; 24.07 billion worth Rs 29.37 lakh crore | https://www.outlookmoney.com/banking/upi-processes-2407-billion-transactions-worth-rs-2937-lakh-crore-in-september (checked 12 October 2026) |
| T3 | Flipkart Stories, 9 October 2026: "6.3 million concurrent users in a minute"; the slug reads 63 million | https://stories.flipkart.com/announcement/india-logs-on-for-the-big-billion-days-flipkart-records-63-million-concurrent-users-as-the-festive-season-opens (checked 12 October 2026) |
| T3 | Avenue Supermarts release, 2 May 2026: FY26 standalone total revenue Rs 66,968 crore; 85 stores added; 500 stores; two-year-old stores up 10.8 percent in Q4 FY26 (fetched with curl, WebFetch returned 503) | https://nsearchives.nseindia.com/corporate/DMART_02052026173007_ASLPressRelease02052026.pdf (checked 12 October 2026) |
| T1 | Amazon's 2017 letter, filed 18 April 2018: no slide presentations; six-page memos read silently at the start of meetings; a great memo "should take a week or more" | https://www.sec.gov/Archives/edgar/data/1018724/000119312518121161/d456916dex991.htm (checked 12 October 2026) |
| T1 | Barbara Minto: ideas "organized as a pyramid under a single point"; the SCQ frame | https://www.barbaraminto.com/ (checked 12 October 2026) |
| T1 | Storytelling with Data: the declutter makeover (4 January 2011); the wordy slide makeover; the makeover index | https://www.storytellingwithdata.com/blog/2011/01/new-years-resolution-declutter-your ; https://www.storytellingwithdata.com/blog/a-wordy-slide-makeover ; https://www.storytellingwithdata.com/blog-summary-page-for-makeovers (checked 12 October 2026) |
| R1 | Storytelling with Data: the Big Idea (6 February 2014) and the 3-minute story (4 February 2014) | https://www.storytellingwithdata.com/blog/2014/02/whats-big-idea ; https://www.storytellingwithdata.com/blog/2014/02/the-3-minute-story (checked 12 October 2026) |
| T2 | Aced: the interviewer "isn't looking for a precise number"; each assumption stated "so the interviewer can push back"; scope first | https://www.aced.io/blog/top-data-analyst-interview-questions (checked 12 October 2026) |
| fresh check | Ziegler and colleagues, "Productivity Assessment of Neural Code Completion", arXiv 2205.06537, submitted 13 May 2022, a study of GitHub Copilot's users: the acceptance rate of shown suggestions, rather than the persistence of completions, drives developers' perception of productivity (the page lists no affiliations, so no file says GitHub wrote it) | https://arxiv.org/abs/2205.06537 (checked 12 October 2026) |
| fresh check | METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity", 10 July 2025: 16 experienced developers, 246 issues of about two hours each, timed as whole tasks; with AI tools allowed they took 19 percent longer, expected a 24 percent speed-up and afterwards believed 20 percent; the page now says "These results are out of date" and points to a February 2026 update. Re-read on 13 October 2026 for the rewritten transcript 3 | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ (checked 13 October 2026) |
| M6 | The Tribune, 9 August 2026: 64.06 lakh journeys a day; Republic World, 18 September 2026: 82,44,903 boardings on 17 September 2026; PTI via LatestLY, 30 May 2018: line utilisation 45,35,932, a trip across three lines counted three times (fetched with curl, WebFetch returned 403); Deccan Herald (PTI), 30 August 2023: a journey counts each line a rider uses, which the mid-check key's item 2 now says | https://www.tribuneindia.com/news/delhi/delhi-metro-records-99-95-train-punctuality-in-2026-dmrc/ ; https://www.republicworld.com/india/delhi-metro-breaks-all-time-record-with-8244-lakh-footfall-as-dtc-strike-sends-rush-soaring-2026-09-18-137241 ; https://www.latestly.com/agency-news/dmrc-uses-new-count-metric-on-traffic-flow-doesnt-share-ridership-190870.html/amp ; https://www.deccanherald.com/india/delhi/delhi-metro-records-highest-ever-footfall-on-aug-29-2666561 (checked 12 October 2026) |

Drivers online at Hyderabad's evening peak: R2 holds no figure, and a web search on 12 October 2026
found only undated or decade-old counts of Uber drivers signed up in the city, a different unit. A
second search on 13 October 2026 found rider-side figures only (Uber's 2025 usage data naming
Hyderabad among its busiest cities) and no count of drivers online at any hour. The slot reads "to be
found" in every file, and the room's check stays the case data's own ratio.

## Where does the pack depart from its sources, and why?

- **The per-driver-week read** is per active driver-week (a driver with a row that week), never per enrolled driver-week. Its 0.8 percent rise keeps the review's arithmetic (bookings up 3.0 percent over active driver-weeks up 2.2 percent) and adds the mechanism the interviewer read found in Monday's data: the ratio is rupees per hour times hours per driver-week, hours went from 18.6 to 22.5 a driver-week, and the 140 joiners (Rs 4,314 a driver-week) pulled it down while the drivers there before the launch rose 1.4 percent. Every file that blamed the joiners now says so.
- **The answer to driver operations** uses Monday's settled 880 drivers who were there before the launch, at 1.90 trips an hour in both windows, copied by id from Monday's facts file after the merge; Tuesday's own 1,020 count is gone.
- **The validate step** compares like with like, online driver-hours per completed trip (0.53 before the launch), since the chain counts trips; the chain runs an eighth high and the checked answer is about 5,000 to 5,700. The first factor is counted in trips per 100 people, so a commuter who rides twice counts twice.
- **A four-hour window** leaves the busiest half hour where it was (buffer about 1.53, answer about 5,700); the draft's 4,300 is now the scorecard's weak answer.
- **The monsoon answer** uses the last three weeks after the launch (requests back inside the before range, 1.56 trips an hour), since the busiest three weeks are also the first three.
- **The action** is a six-week test on half the enrolled drivers, picked at random, which the city head signs; the saving keeps Monday's own words, a half to a fifth of the Rs 1.16 crore still paid, and Monday's print, Rs 92.7 lakh.
- **The decks open on the ticket**, as the spine's first acceptance line asks; the quote covers were removed and the morning deck sits at the spine's 35 slides.
- **Case counts take Monday's grouping** (118,000, 146,300); published figures keep the source's own (82,44,903).
- **The fall in rupees per hour** is 16.9 percent, printed as 17; the draft's facts file carried 17.1.
- **The saving range**, Rs 58 lakh to Rs 92.7 lakh, is Monday's `saving_low_rs` and `saving_high_rs`, copied by id and re-derived by assertion (Rs 1.159 crore times one less Monday's uptake assumption of a fifth to a half).
- **Monday's data definition** counts peak windows on all seven days (42 hours a week, Monday's `max_peak_hours_per_week`), while the case file's guarantee names weekday windows; the validate step says so and treats the case's ratio as a check on size only.
- **The drivers-at-peak chain** walks requests from a crowd (the spine's L5) and uses trips per busy driver-hour, since the draft divided by an idle share on top of trips per online hour, which already carries idle time. With that walk, the share who ride moves the answer most; the case file's catch names the idle share, so the decks and notes say which factor moves it and why, and the guesstimate note records the change.
- **The UPI worked chain** uses round numbers a candidate would reach without the anchor (35 crore users, 2 a day) and lands 13 percent below NPCI; the draft's assumptions landed 0.4 percent from it.
- **No GIF**: the spine ships none on Tuesday, so the draft's GIF and its still were removed. The four moves are a timeline fence and the guesstimate tree a mermaid fence, per the visuals rule.
- **The notebook** is fifteen cells (the spine's 12 to 15) and defines its own `check`; the draft's 25 cells and `c2kit` helpers were replaced.
- **Amazon**: the draft's "fifteen minutes" of silent reading is not in the letter and was removed.
- **DMart** is quoted as "standalone total revenue", the release's wording.
- **Three cluttered slides** (A, B, C) carry nine Monday numbers each, by id, as the run sheet asks; the draft had one.
- **The gallery** runs in the afternoon (S54), where the spine's envelope places it.

## What is invented, and where is it labelled?

The hostel notice board, the canteen's tea, the city of two million people, the acceptance rate of 32
percent, the food stall, the Rs 150 crore store, and the Kahoot's two invented items, each labelled
invented where it appears and listed under `toys` in the facts file. Every guesstimate value is an
assumption said aloud with its range, under `assumptions` and in the guesstimate note.

## Which cold-read findings were not fixed, and why?

Both reads are in `C2_W04_D02_cold_reads_INTERNAL.md`. The fresh-graduate read found 74 (1 blocker, 44
confusing, 29 minor); the hiring-interviewer read found 40 (17 reject, 8 shallow, 5 fact, 10 minor) and
scored the three hire-grade answers 11, 8 and 6 of 14. The fix pass rewrote the three transcripts, the
scorecards, chapters 1 to 4 of the decks, the notebook, nine exercise files with their solutions, the
notes, the sheet, the Kahoot, the take-home and every trainer file; the rescored hire-grade answers
reach 2 on the first three criteria. Every finding is fixed except the lines below, each with its
reason.

- **Graduate 18, in part.** S19 keeps the spine's prediction (the Veritasium row of section 6's styles table), though S1's caveat says each objection is partly right: the question asks whose side the city head is on, which the caveat does not settle. The code-along's cells confirm in code what the deck counted by hand; their predictions now ask for what no slide shows (which drivers explain the fall, how many more hours a driver-week carried, what doubling a factor does).
- **Graduate 5, the week map.** The spine's styles table quotes Monday's node as "1.9 to 1.6"; the node prints 1.90 to 1.58, the two decimals every other file uses.
- **Graduate 29, "read" as a noun.** It stays, used only beside its three examples (per hour, per driver-week, per trip), which define it where it first appears.
- **Graduate 38, two items.** Drill 2's item 4 re-asks S33 minutes after it, by the design of a mid-session retrieval drill; the Kalpa store's item 1 is a computation the stem sets up, and item 2 no longer prints its answer.
- **Graduate 53, "vanity metric".** It sits in the weak answer on purpose: it is the jargon a weak candidate reaches for.
- **Graduate 60, the keys in the Kahoot file.** The house format marks keys inline, as Monday's pack does; the room answers in Kahoot, and the file now says it is for review after the quiz.
- **Graduate 67, the sheet's word strip.** The builder reads the strip from the notes' table and keeps the terms the sheet itself uses; the notes' table now carries all eighteen.
- **Graduate 74, three words.** "Finance controller" is Anand Iyer's locked title (decision `anand-finance-controller`); "city review" and "proxy" are defined by the sentence they sit in.
- **Interviewer 17, the deck number's credibility.** The transcript keeps acceptance in the deck with its definition printed, the head of product's true part; the scorecard leaves the decision criterion at 1 and asks the room for the rupee sentence.
- **Interviewer 18, "why not end it?"** The hire-grade answer opens on the three options (keep, end, change) and recommends a test as the cheaper way to learn whether the change beats ending the scheme.
- **Interviewer 19, the 72 percent.** The slide's evidence stays the rupees-per-hour chart with the 61 percent beside it; the 72 percent of low-acceptance hours with no trip is in the facts file for a trainer who wants it.
- **Interviewer 27, the curriculum row.** The row's wording about scoring the final number stays in the tracker, which a day session does not edit; every Tuesday file now quotes only what the Aced page says.
- **Interviewer 28, the label on S41, S50 and S56.** Every slide carries the header line "UBER, HYDERABAD, AN ILLUSTRATIVE CASE", so a slide lifted alone keeps its label.

## Which house reads ran after the fix pass, and what did they change?

The humanizer read ran in file mode over every STUDENT and TRAINER file and the notebook's markdown
cells, by four reviewer agents that wrote findings and edited nothing. They found 94: 14 in the
morning deck, the sheet and the pre-read, 19 in the afternoon deck and the notes, 39 in the exercises,
the Kahoot and the take-home, and 22 in the transcripts, the trainer files and the notebook. All 94 are
applied, 83 as proposed and 11 reworded so that each keeps its numbers and reads as one sentence. The
same pass names explorer scenes T1 to T3 in the notes of S9, S10, S14 and S40, puts the day sheet's
handoff line in S56's notes, and runs the notebook's ledger as a table of versions, so the notebook
defines only `check`. The tic scanner then read all 38 markdown files and the notebook's prose clean.

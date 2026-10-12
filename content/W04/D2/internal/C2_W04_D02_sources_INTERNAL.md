# Sources, W04 D2 (Tuesday 27 October 2026): what the pack rests on, what it changed, and why

Built by the W04 D2 finishing session on 12 October 2026 from `docs/detailing/W04_analyst_craft_spine.md`
(section 6), `docs/detailing/W04_case_file.md` (Tuesday) and Monday's tables. Data command:
`python3 content/W04/D2/internal/C2_W04_D02_make_data_INTERNAL.py`, then the figures, notebook and
audit scripts beside it. Tools: Python 3.13.16, pandas 3.0.5, matplotlib 3.11.2, PyYAML 6.0.1,
python-pptx 1.0.2, mermaid-cli 12.0.0, nbconvert 7.17.2, LibreOffice 24.2.7.2.

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
| fresh check | METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity", 10 July 2025: 16 experienced developers, 246 issues; with AI tools allowed they took 19 percent longer, expected a 24 percent speed-up and afterwards believed 20 percent; the page now says the results are out of date | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ (checked 12 October 2026) |
| M6 | The Tribune, 9 August 2026: 64.06 lakh journeys a day; Republic World, 18 September 2026: 82,44,903 boardings on 17 September 2026; PTI via LatestLY, 30 May 2018: line utilisation 45,35,932, a trip across three lines counted three times (fetched with curl, WebFetch returned 403) | https://www.tribuneindia.com/news/delhi/delhi-metro-records-99-95-train-punctuality-in-2026-dmrc/ ; https://www.republicworld.com/india/delhi-metro-breaks-all-time-record-with-8244-lakh-footfall-as-dtc-strike-sends-rush-soaring-2026-09-18-137241 ; https://www.latestly.com/agency-news/dmrc-uses-new-count-metric-on-traffic-flow-doesnt-share-ridership-190870.html/amp (checked 12 October 2026) |

Drivers online at Hyderabad's evening peak: R2 holds no figure, and a web search on 12 October 2026
found only undated or decade-old counts of Uber drivers signed up in the city, a different unit. The
slot reads "to be found" in every file.

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

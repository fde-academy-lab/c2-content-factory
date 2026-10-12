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
| M6 | The Tribune, 9 August 2026: 64.06 lakh journeys a day; Republic World, 18 September 2026: 82,44,903 boardings on 17 September 2026; PTI via LatestLY, 30 May 2018: line utilisation 45,35,932, a trip across three lines counted three times (fetched with curl, WebFetch returned 403) | https://www.tribuneindia.com/news/delhi/delhi-metro-records-99-95-train-punctuality-in-2026-dmrc/ ; https://www.republicworld.com/india/delhi-metro-breaks-all-time-record-with-8244-lakh-footfall-as-dtc-strike-sends-rush-soaring-2026-09-18-137241 ; https://www.latestly.com/agency-news/dmrc-uses-new-count-metric-on-traffic-flow-doesnt-share-ridership-190870.html/amp (checked 12 October 2026) |

Drivers online at Hyderabad's evening peak: R2 holds no figure, and a web search on 12 October 2026
found only undated or decade-old counts of Uber drivers signed up in the city, a different unit. The
slot reads "to be found" in every file.

## Where does the pack depart from its sources, and why?

- **The per-driver-week read** is per active driver-week (a driver with a row that week), never per enrolled driver-week, and its 0.8 percent rise is explained as bookings up 3.0 percent over active driver-weeks up 2.2 percent, as the orchestrator's review set out; the case file's "because hours rose" is replaced.
- **The fall in rupees per hour** is 16.9 percent, printed as 17; the draft's facts file carried 17.1.
- **The saving range**, Rs 58 lakh to Rs 93 lakh, is Monday's `saving_low_rs` and `saving_high_rs`, copied by id and re-derived by assertion (Rs 1.159 crore times one less Monday's uptake assumption of a fifth to a half).
- **The validate step** states Monday's data definition, peak windows on all seven days (42 hours a week, Monday's `max_peak_hours_per_week`), while the case file's guarantee names weekday windows; the check leans on online driver-hours per rider request, which no window definition changes.
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

Filled after the two cold reads and the fix pass; see the section below.

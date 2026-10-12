# W04 D3 sources: every public fact with its check, every correction, every open item

INTERNAL. One page for the reviewer. Every link below was fetched on 12 October 2026 in the build
session; R2 ids are the case file's (`docs/detailing/W04_case_file.md`, "Public facts allowed on
Wednesday").

## Which public facts does the pack use, and what did the check confirm?

| R2 | Fact as the pack states it | Source, checked 12 October 2026 | What the fetch confirmed |
|---|---|---|---|
| W1 | Counting co-purchases would make a few bestsellers, such as Harry Potter books and trash bags, the top recommendations for every customer; the team then measured the increased likelihood of buying B "with any given purchase", scaling heavy buyers down; Prime Video's first autoencoder trailed a list of the past two weeks' most popular rentals until it was trained on viewing before a cutoff and scored on the two weeks after it | https://www.amazon.science/the-history-of-amazons-recommendation-algorithm (checked 12 October 2026) | All three passages, the Prime Video one refetched on 12 October 2026 for its baseline ("the most popular movie rentals of the previous two weeks") and its test ("the two-week period after the cutoff time"); the article is Larry Hardesty's, 22 November 2019, so the pack says "Amazon Science's history" and never quotes the team |
| W1 | Linden, Smith and York, item-to-item collaborative filtering | https://www.cs.umd.edu/~samir/498/Amazon-Recommendations.pdf (checked 12 October 2026) | Title, authors, IEEE Internet Computing, January and February 2003, from the PDF's own text |
| W2 | 1992, about 1.2 million baskets from Osco Drug stores, early evening, and the chain does not appear to have moved any shelf | https://www.theregister.com/2006/08/15/beer_diapers/ (checked 12 October 2026) | 1992 and Teradata's team under Thomas Blischok; "between 5pm and 7pm", written as early evening by the case file's rule; the shelf move hedged in the source ("does not appear to have exploited the information") |
| W4 | Maxxsaver: over 28 percent of MTUs; AOV up 16 percent quarter on quarter to Rs 612; part of the larger basket's margin funnelled back to the user; it sometimes consolidates carts into fewer orders | https://www.swiggy.com/corporate/wp-content/uploads/2025/07/Q1-FY2026-Shareholder-letter.pdf (checked 12 October 2026) | Question 9 of the letter's Q&A, page 13, quoted; the letter never says the discount is paid on adds that would have happened anyway, so the pack states that as the analyst's reading |
| T3 | 1,089 completed orders per active dark store-day; 1,171 active stores at the quarter's end, across 131 cities | https://nsearchives.nseindia.com/corporate/SWIGGY_30072026154100_Covering_Letter_Letter_to_Shareholders_-_signed.pdf (checked 12 October 2026) | The key metrics table, its footnote and the definitions page (orders are completed orders; an active store has at least one completed order on the period's last day), and the letter's own sentence "1,171 darkstores across 131 cities"; the fetch tool met HTTP 503, and a plain download with a browser user agent returned the PDF |
| W4 | In the three months ended 31 December 2025, in countries offering both, consumers using rides and delivery generated over three times the gross bookings of single-product consumers; about one in five eligible consumers active monthly in both | https://www.sec.gov/Archives/edgar/data/1543151/000154315126000015/uber-20251231.htm (checked 12 October 2026) | Both sentences, in Item 1's platform synergies passage; the pack says "the last quarter of 2025" |
| W3 | Strawberry Pop-Tarts sales rose about seven times before Hurricane Charley; Walmart shipped extra ahead of Frances in 2004 | https://openstax.org/books/principles-data-science/pages/1-2-data-science-in-practice (checked 12 October 2026) | The account and the sevenfold figure |
| W5 | Agrawal, Imielinski and Swami (SIGMOD 1993); Brin, Motwani, Ullman and Tsur (SIGMOD 1997) | https://api.crossref.org/works/10.1145/170035.170072 and https://api.crossref.org/works/10.1145/253260.253325 (checked 12 October 2026) | Metadata only; neither record carries an abstract, so the notes cite the 1993 title and nothing about either paper's content beyond it |
| R1 3.2 | Lift as observed over expected | https://pbpython.com/market-basket-analysis.html (checked 12 October 2026) | Chris Moffitt, 3 July 2017; "the ratio of the observed support to that expected if the two rules were independent" |
| R1 3.2 | IBM's lift divides by the antecedent's support (trainer audit item) | https://www.ibm.com/think/topics/apriori-algorithm (checked 12 October 2026) | 0.6 / 0.125 = 4.8 and 0.3 / 0.25 = 1.2 on the page |
| Video | StatQuest, "Conditional Probabilities, Clearly Explained!!!" | https://www.youtube.com/watch?v=_IgyaD7vOOA (checked 12 October 2026) | Title and channel through oEmbed; the watch page returned HTTP 429, so its length is printed as not verified |
| Video | IBM Technology, "What is an AI Recommendation Engine?" | https://www.youtube.com/watch?v=gEdePRsDACc (checked 12 October 2026) | Title and channel through oEmbed; 10:53 from the research note of the same day |

## Which sources failed, and what replaced them?

- The case file's second W3 source, https://www.newsweek.com/survival-turn-tart-138555 (checked 12 October 2026), is a 2003 article about Hurricane Isabel with no Pop-Tarts figure. The pack cites OpenStax alone; the fallback deck's S8 is corrected to say so.

## Which corrections to the case file does the pack carry?

| Case file | The pack | Why |
|---|---|---|
| Milk's share of slot impressions, 44 percent | 50 percent | 44 percent beside 1.2 and 6.4 blends to 4.1 percent, and the ticket's after rate is 3.8 |
| Twelve carts: bread to milk 0.75 | 1.00 and lift 1.50 | 0.75 sits 0.01 from the full data's 0.74; the spine asks for five points between them |
| Rs 12.6 lakh a month over three slots | Rs 6.3 lakh recovered, Rs 12.6 lakh kept only as the ceiling and a distractor | Rs 12.6 lakh held only if every slot showed milk; `strip_log` shows milk on half the impressions |
| Causal testing "taken up in Week 5" (the draft's own wording) | Monday's faculty session on A/B testing (tentative) | `docs/faculty/Sessions.md` puts experiment design in W4-1; Week 5 is regression and classification |

## Which items stay open?

- The StatQuest video's length is not verified.
- The cohort's group count is not in the programme facts; the run sheet says groups of about four, as
  the build weeks use, and the decks no longer name a number of groups.

## Which cold-read findings were not fixed, and why?

Four findings were not fixed in full, each for the reason below; every other finding of the two
reads, all seven of the interviewer re-check and all eight of the confirmation read, was fixed, and
`internal/C2_W04_D03_cold_reads_INTERNAL.md` maps each one to its change.

- Graduate 59: the lab's your-turn cells carry sanity checks but no expected values, because the plants must be found in an empty cell (decision `w4-finding-once-found`); the TA lab note holds the numbers.
- Graduate 69: the pre-read stays terms only, as the spine sets it, so the line showing how 38 percent can be a mix waits for Thursday.
- Graduate 55: the quiz keeps the counts and gives item 2 sixty seconds, since computing lift from three counts is the skill tested.
- Interviewer 12, in part: the watch-list trial stays in two zones, as the spine's fallback protocol sets it, with shoppers randomised inside them.

# W04 D3 sources: every public fact with its check, every correction, every open item

INTERNAL. One page for the reviewer. The case-first build fetched every link below on 12 October
2026; the concept-first rebuild re-checked, on 13 October 2026, every reference a concept chapter
names, and each row says which date holds. R2 ids are the case file's
(`docs/detailing/W04_case_file.md`, "Public facts allowed on Wednesday").

## Which written reference checks each rule a concept chapter names?

| Chapter | The rule as the pack states it | Reference and its check date | What the fetch confirmed |
|---|---|---|---|
| 1, support | Support is the baskets holding both over all baskets | https://365datascience.com/tutorials/python-tutorials/market-basket-analysis/ (checked 13 October 2026) and https://pbpython.com/market-basket-analysis.html (checked 13 October 2026) | 365 Data Science: "Support(item) = Transactions comprising the item / Total transactions"; Practical Business Python: support "is the relative frequency that the rules show up" |
| 2, confidence | Confidence from A to B is both over A, so it has a direction | https://365datascience.com/tutorials/python-tutorials/market-basket-analysis/ (checked 13 October 2026) | "Confidence (Bread -> Milk) = Transactions comprising bread and milk / Transactions comprising bread"; the page's own lift line computes 0.75 / 1 and reports 1.3, so the pack cites it for support and confidence only |
| 3, chance and lift | Lift is seen over what chance gives; near one means chance | https://pbpython.com/market-basket-analysis.html (checked 13 October 2026) | Chris Moffitt, 3 July 2017: "the ratio of the observed support to that expected if the two rules were independent"; "a lift value close to 1 means the rules were completely independent" |
| 4, the confidence trap; lift near one | An item in most baskets earns high confidence toward everything; lift divides its base rate out | https://www.amazon.science/the-history-of-amazons-recommendation-algorithm (checked 13 October 2026) and https://pbpython.com/market-basket-analysis.html (checked 13 October 2026) | Amazon Science: counting how often buyers of A also bought B would put a few bestsellers beside everything; relatedness is scored against "the average Amazon customer"; heavy buyers were scaled down. The sweep's rule (confidence toward an ignoring partner equals the item's share) is taught from the example's arithmetic |
| 5, basket analysis on the order items | Group lines by order into a set, then count `combinations` of the sorted set once per basket | https://pandas.pydata.org/docs/user_guide/groupby.html (checked 13 October 2026) and https://docs.python.org/3/library/itertools.html (checked 13 October 2026) | pandas 3.0.6: group by as split, apply, combine; Python 3.15.0: combinations "are emitted in lexicographic order", sorted input gives sorted tuples, length `math.comb` |
| 6, the support floor and the watch list | A lift is read only above a floor of baskets set first | https://pbpython.com/market-basket-analysis.html (checked 13 October 2026) | Frequent itemsets "that have a support of at least 7%", a number "chosen so that I could get enough useful examples". The watch list, a trial with a pass rule set first, is not verified on 13 October 2026 against a written reference and is taught from the invented month's arithmetic and Week 1 Thursday's rule of thirty |
| 9, cross-sell and upsell | Cross-sell suggests a second item; upsell a dearer version of the same item | https://en.wikipedia.org/wiki/Cross-selling (checked 13 October 2026) and https://en.wikipedia.org/wiki/Upselling (checked 13 October 2026) | "selling of an additional product or service to an existing customer"; upselling "invites the customer to purchase more expensive items, upgrades", and "is distinct from cross-selling, in which a seller tries to sell something else" |
| 9, expected value in rupees | Expected value is each outcome times its probability, added up | https://en.wikipedia.org/wiki/Expected_value (checked 13 October 2026) | "a generalization of the weighted average"; for finitely many outcomes, x1p1 + x2p2 + ... + xkpk. The promotion line (margin on the purchases a card changes, less the discount on every bill that takes it, less the fixed cost) is not verified on 13 October 2026 against a written reference, since the search returned vendor and agency pages only, and is taught from the kirana's arithmetic |

One video per topic: StatQuest's conditional-probability video carries confidence, and IBM
Technology's recommendation-engine video the popular-partner trap; for basket analysis, the floor
and expected value no video was verified in the session, so those slots read "to be found".

## Which public facts does the pack use, and what did the check confirm?

| R2 | Fact as the pack states it | Source and its check date | What the fetch confirmed |
|---|---|---|---|
| W1 | Counting co-purchases would make a few bestsellers, such as Harry Potter books and trash bags, the top recommendations for every customer; the team then measured the increased likelihood of buying B "with any given purchase", scaling heavy buyers down; Prime Video's first autoencoder trailed a list of the past two weeks' most popular rentals until it was trained on viewing before a cutoff and scored on the two weeks after it | https://www.amazon.science/the-history-of-amazons-recommendation-algorithm (checked 13 October 2026 for the bestseller, base-rate and heavy-buyer passages; 12 October 2026 for Prime Video) | All three passages, the Prime Video one refetched on 12 October 2026 for its baseline ("the most popular movie rentals of the previous two weeks") and its test ("the two-week period after the cutoff time"); the article is Larry Hardesty's, 22 November 2019, so the pack says "Amazon Science's history" and never quotes the team |
| W1 | Linden, Smith and York, item-to-item collaborative filtering | https://www.cs.umd.edu/~samir/498/Amazon-Recommendations.pdf (checked 12 October 2026) | Title, authors, IEEE Internet Computing, January and February 2003, from the PDF's own text |
| W2 | 1992, about 1.2 million baskets from Osco Drug stores, early evening, and the chain does not appear to have moved any shelf | https://www.theregister.com/2006/08/15/beer_diapers/ (checked 12 October 2026) | 1992 and Teradata's team under Thomas Blischok; "between 5pm and 7pm", written as early evening by the case file's rule; the shelf move hedged in the source ("does not appear to have exploited the information") |
| W4 | Maxxsaver: over 28 percent of MTUs; AOV up 16 percent quarter on quarter to Rs 612; part of the larger basket's margin funnelled back to the user; it sometimes consolidates carts into fewer orders | https://www.swiggy.com/corporate/wp-content/uploads/2025/07/Q1-FY2026-Shareholder-letter.pdf (checked 12 October 2026) | Question 9 of the letter's Q&A, page 13, quoted; the letter never says the discount is paid on adds that would have happened anyway, so the pack states that as the analyst's reading |
| T3 | 1,089 completed orders per active dark store-day; 1,171 active stores at the quarter's end, across 131 cities | https://nsearchives.nseindia.com/corporate/SWIGGY_30072026154100_Covering_Letter_Letter_to_Shareholders_-_signed.pdf (checked 12 October 2026) | The key metrics table, its footnote and the definitions page (orders are completed orders; an active store has at least one completed order on the period's last day), and the letter's own sentence "1,171 darkstores across 131 cities"; the fetch tool met HTTP 503, and a plain download with a browser user agent returned the PDF |
| W4 | In the three months ended 31 December 2025, in countries offering both, consumers using rides and delivery generated over three times the gross bookings of single-product consumers; about one in five eligible consumers active monthly in both | https://www.sec.gov/Archives/edgar/data/1543151/000154315126000015/uber-20251231.htm (checked 12 October 2026) | Both sentences, in Item 1's platform synergies passage; the pack says "the last quarter of 2025" |
| W3 | Strawberry Pop-Tarts sales rose about seven times before Hurricane Charley; Walmart shipped extra ahead of Frances in 2004 | https://openstax.org/books/principles-data-science/pages/1-2-data-science-in-practice (checked 12 October 2026) | The account and the sevenfold figure |
| W5 | Agrawal, Imielinski and Swami (SIGMOD 1993); Brin, Motwani, Ullman and Tsur (SIGMOD 1997) | https://api.crossref.org/works/10.1145/170035.170072 and https://api.crossref.org/works/10.1145/253260.253325 (checked 12 October 2026) | Metadata only; neither record carries an abstract, so the notes cite the 1993 title and nothing about either paper's content beyond it |
| R1 3.2 | Lift as observed over expected | https://pbpython.com/market-basket-analysis.html (checked 13 October 2026) | Chris Moffitt, 3 July 2017; "the ratio of the observed support to that expected if the two rules were independent" |
| R1 3.2 | IBM's lift divides by the antecedent's support (trainer audit item) | https://www.ibm.com/think/topics/apriori-algorithm (checked 13 October 2026) | 0.6 / 0.125 = 4.8 and 0.3 / 0.25 = 1.2 on the page, re-checked on the build day as the spine asks |
| Video | StatQuest, "Conditional Probabilities, Clearly Explained!!!" | https://www.youtube.com/watch?v=_IgyaD7vOOA (checked 13 October 2026) | Title and channel through oEmbed; the watch page returned HTTP 429, so its length is printed as not verified |
| Video | IBM Technology, "What is an AI Recommendation Engine?" | https://www.youtube.com/watch?v=gEdePRsDACc (checked 13 October 2026) | Title and channel through oEmbed; 10:53 from the research note of 12 October 2026 |

## Which sources failed, and what replaced them?

- The case file's second W3 source, https://www.newsweek.com/survival-turn-tart-138555 (checked 12 October 2026), is a 2003 article about Hurricane Isabel with no Pop-Tarts figure. The pack cites OpenStax alone; the fallback deck's S8 is corrected to say so.

## Which corrections to the case file does the pack carry?

| Case file | The pack | Why |
|---|---|---|
| Milk's share of slot impressions, 44 percent | 50 percent | 44 percent beside 1.2 and 6.4 blends to 4.1 percent, and the ticket's after rate is 3.8 |
| Twelve carts: bread to milk 0.75 | 1.00 and lift 1.50 | 0.75 sits 0.01 from the full data's 0.74; the spine asks for five points between them |
| Rs 12.6 lakh a month over three slots | Rs 6.3 lakh recovered, Rs 12.6 lakh kept only as the ceiling and a distractor | Rs 12.6 lakh held only if every slot showed milk; `strip_log` shows milk on half the impressions |
| Causal testing "taken up in Week 5" (the draft's own wording) | Monday's faculty session on A/B testing (tentative) | `docs/faculty/Sessions.md` puts experiment design in W4-1; Week 5 is regression and classification |

## Which items were left open, and how did each close?

- The StatQuest video's length stays unverified. On 13 October 2026 YouTube answered automated reads
  with a rate limit on the watch page (HTTP 429) and a sign-in wall from its player endpoint
  (LOGIN_REQUIRED), and the only listing that names a length is an unofficial aggregator, so the
  notes keep "length not verified" and print no length.
- The group count closed on 13 October 2026. The programme facts state 35 learners in nine build
  groups (`cohort.students`, `cohort.build_groups`), so the run sheet names nine groups, eight of four
  and one of three, and counts every print run from them; the learner files keep "groups of about
  four", which is true of all nine.

## Which cold-read findings were not fixed, and why?

Four findings were not fixed in full, each for the reason below; every other finding of the two
reads, all seven of the interviewer re-check and all eight of the confirmation read, was fixed, and
`internal/C2_W04_D03_cold_reads_INTERNAL.md` maps each one to its change.

- Graduate 59: the lab's your-turn cells carry sanity checks but no expected values, because the plants must be found in an empty cell (decision `w4-finding-once-found`); the TA lab note holds the numbers.
- Graduate 69: the pre-read stays terms only, as the spine sets it, so the line showing how 38 percent can be a mix waits for Thursday.
- Graduate 55: superseded in the concept-first rebuild, whose item 2 computes lift from the twelve carts' counts, which divide in the head.
- Interviewer 12, in part: the watch-list trial stays in two zones, as the spine's fallback protocol sets it, with shoppers randomised inside them.

## Which decisions did the concept-first rebuild take?

- Slide one is the topic slide, with no quote cover, so slides two to five carry the week map, the
  five topics, the concept map and the ticket (acceptance line 1). Each concept chapter runs to six
  slides with its opener; half one holds 63 slides and half two 22.
- Four numbers in the plan were corrected in the deck and in the generator's assertions: the support
  trap adds 4 and 4 to 8, not 7; unsorted keys count 60 pairs, not 66; the top lift on the twelve
  orders is gulab jamun and curd at 6.0; the chaas band (confidence 0.60 to 1.00, lift 0.80 to 1.33)
  holds for the four items in four or more orders.
- The Kahoot's item 2 computes lift from the twelve carts' counts (4, 8 and 4 give 1.50), keeping
  the spine's "case's numbers" and the plan's numbers that divide in the head; item 8 asks how many
  pairs cart C033861 adds; item 7 keeps the blended click-through, the case's own finding, so the
  confidence direction is tested in canteen_concepts Q2 and the notes' self-check, and the
  heavy-buyer item lives in the strip set's Q2 and slide D69.
- The lab's practice set moved off a Pune kirana whose shares and lift (0.15, 0.60, 0.20, 1.25)
  repeated Sharma Kirana's, to an invented Nagpur hardware shop (paint, brushes, sandpaper; lift 1.24
  and a pair at exactly 1.00), clear of Kalpa's catalogue and of Instamart's items.
- Chapter 9 holds the second concept drill, items 5 to 7, inside its 18 minutes; chapter 10 opens on
  ch3_four_pairs as a four-minute paper check, and the pair-card sort runs inside S63.
- The decks drop the stock-out picture slide, the morning's-answer slide, the follow-ups slide and
  the AI-variant slide (read in the lab from extras), and the stock-out and actual-against-expected
  pictures retire from the figure script; the tea stall's two pictures are deleted.
- The Gold pre-read's facts follow the case file: 53,089 members and an August cohort of 13,000,
  2.6 times the 5,000 a month of January to July.
- The cheat sheet states how the topics join in words: a mermaid map either printed its labels under
  the 5.2-point floor or pushed the sheet onto a second page; the map stays on S4, in the notes and on
  the board.
- A loss prints as "-Rs 71", and the facts audit matches a loss by its size. A toy fact's `used_by`
  keeps its new chapter numbers, after a renumbering pass had sent notebook 04 to 11.
- The study notes run to 3,696 prose words against about 3,500, after a pass that cut repeated
  sentences rather than whole sections.

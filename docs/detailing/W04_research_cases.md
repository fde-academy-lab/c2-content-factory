# R2. Week 4 case bank and interview material

Every source below was opened on 12 October 2026 and carries that date beside its URL. Primary documents (exchange filings, SEC filings, regulator releases, company letters, peer-reviewed papers, competition data) were read directly, mostly as downloaded PDFs. Where only a newspaper or a reproduction could be reached, the entry says so. Figures we computed ourselves from sourced inputs are labelled "our arithmetic". Anything that could not be verified today sits at the end under "Unverified, do not use" or "Not yet verified".

Reuse note from Weeks 1 to 3: Target Canada was already taught in W01 D3 as a data-quality case (bad item data), Blinkit's net AOV and 2,443 dark stores appear in earlier packs, and Airbnb's metric-consistency post appears in an earlier trainer sheet. Week 4 should use Target Canada only for its forecasting angle and say it returns from Week 1.

One house-rule catch: the beer-and-diapers record names a clock window. A learner file should say "early evening" to keep the durations-only rule.

---

## Monday: metric design

### M1. Swiggy writes its metrics down to the denominator

Swiggy's shareholder letters end with a glossary that is a ready-made "complete definition" exhibit. From the Q2 FY25 letter dated 3 December 2024, filed with the exchanges:

| Swiggy term | Definition as filed (paraphrased closely) | Numerator | Denominator or unit | Window |
|---|---|---|---|---|
| Average Monthly Transacting Users (MTU) | Unique users who completed at least one order on the app or website in a month, averaged over the months in the period | unique users with one or more completed orders | per month, then averaged | calendar month |
| Platform Frequency | Completed orders per user in a month, averaged over the months in the period | completed orders | transacting users | month, averaged |
| Food delivery GOV | Value of completed orders gross of discounts, plus delivery charges (net of discounts, including Swiggy One free delivery), packaging charges, user fees and taxes, excluding tips | rupees | none (a total) | quarter |
| Quick commerce GOV | Same, but goods are valued at MRP (final selling price for fruit and vegetables), gross of discounts | rupees at MRP | none | quarter |
| AOV | GOV divided by total orders | GOV | completed orders | quarter |

Figures in that letter (quarter to 30 September 2024): platform MTU 17.1 million; B2C orders 230 million in the quarter; platform frequency 4.53 orders per user per month; food delivery GOV Rs 7,191 crore; Instamart AOV Rs 499 per order.

Why it teaches: the quick-commerce GOV is booked at MRP and before discounts, so the same basket shows a bigger GOV than the customer paid. In Swiggy's Q1 FY27 letter (30 July 2026), quick-commerce GOV was Rs 7,907 crore and NOV Rs 5,817 crore, NOV being 74 percent of GOV for the quarter. Swiggy's Q4 FY26 letter says its NOV to GOV ratio rose 330 basis points, from a low of 68.7 percent to 72.0 percent, after it halved the share of low-AOV orders.

Sources: https://www.bseindia.com/xml-data/corpfiling/AttachHis/2495f39b-e1d1-4018-8f69-6ff250345e98.pdf (checked 12 October 2026); https://nsearchives.nseindia.com/corporate/SWIGGY_30072026154100_Covering_Letter_Letter_to_Shareholders_-_signed.pdf (checked 12 October 2026); https://www.swiggy.com/corporate/wp-content/uploads/2026/05/Q4-FY2026-Shareholder-letter.pdf (checked 12 October 2026).

### M2. Eternal drops GOV for NOV, and says why

Eternal's Q1 FY26 letter (21 July 2025) states the formula plainly, NOV = GOV minus discounts, and explains that restaurant-funded discounts rose as a share of GOV in the quarter, so NOV grew more slowly than GOV. In the same letter the CFO says Eternal will disclose only NOV from then on because NOV is a better measure of growth. The Q1 FY27 letter (22 July 2026) reports food delivery NOV of Rs 10,769 crore, up more than 20 percent, notes that GOV growth was a few points higher, and closes the matter in one line: "sunsetting this metric disclosure from this quarter onwards as NOV more accurately reflects underlying performance". B2C NOV that quarter was Rs 31,120 crore, up 54 percent year on year; Blinkit NOV was Rs 17,132 crore, up 86 percent, from 2,443 stores.

Teaching use: a gross metric lets a team buy growth with discounts; the company itself moved its headline to the net figure. This is the "what the definition deliberately does not reward" line in a real filing.

Sources: https://www.eternal.com/blog/q1fy26/ (checked 12 October 2026), letter PDF linked there at https://drive.google.com/file/d/1VtoiLsA2OpKauFnkKIlhXRmnbvxL-6ha/view (checked 12 October 2026); https://www.eternal.com/blog/q1fy27/ (checked 12 October 2026), letter PDF at https://drive.google.com/file/d/1jb9KWd4Ap4RTKHFHxzEOO7jgQqVZEGcd/view (checked 12 October 2026).

### M3. Netflix stops reporting subscribers

Netflix's Q1 2024 letter (18 April 2024) says revenue and operating margin are its primary financial metrics and engagement, meaning time spent, is its "best proxy for customer satisfaction". It explains that membership growth mattered when the company had little revenue, that new revenue streams (advertising, extra members) make memberships one component of growth, and that with tiered prices each new membership has a different business impact. It announced it would stop reporting quarterly membership numbers and average revenue per membership (ARM) from Q1 2025. Paid memberships at the end of Q1 2024 were 269.60 million. ARM is defined in the letter as streaming revenue divided by average paid memberships divided by months in the period.

Source: https://s22.q4cdn.com/959853165/files/doc_financials/2024/q1/FINAL-Q1-24-Shareholder-Letter.pdf (checked 12 October 2026).

### M4. Airbnb's "nights booked" went negative

Airbnb's S-1 (filed 16 November 2020) defines Nights and Experiences Booked as nights booked for stays plus seats booked for experiences, net of cancellations and alterations that occurred in the period, and calls it a key measure of the platform's scale. A cancellation reduces the metric in the quarter in which it happens, even when the booking was made in an earlier quarter. In March 2020 gross nights booked were 19.0 million and cancellations 23.1 million (122 percent of gross), so the reported metric was minus 4.1 million; April 2020 was minus 0.7 million. The filing also warns that no uniform standard exists for such metrics, which limits comparison across companies. 2019 figures: 326.9 million nights and experiences booked, gross booking value USD 38.0 billion.

Source: https://www.sec.gov/Archives/edgar/data/1559720/000119312520294801/d81668ds1.htm (checked 12 October 2026).

### M5. Windows that hide in footnotes: Uber and Spotify

Uber's Form 10-K for 2025 (filed 13 February 2026) defines Monthly Active Platform Consumers as unique consumers who completed a ride or received a delivery at least once in a month, averaged over the months in the quarter, and a footnote says the annual MAPC figure is the fourth quarter's. Q4 2025 MAPCs were 202 million (up 18 percent). Trips are counted per paying consumer: an UberX Share ride with three paying consumers is three trips, an UberX ride with three passengers is one. Uber One had 46 million members at 31 December 2025.

Spotify's Form 20-F for 2025 (filed 10 February 2026) counts a monthly active user as an account that consumed content for more than zero milliseconds in the thirty days before period end, and itself warns the figure may overstate unique people (one person, several accounts) and may include non-genuine accounts. Premium Subscribers include every Family and Duo sub-account (up to six per Family plan) and subscribers in a grace period of up to 30 days after a failed payment. At 31 December 2025: 751 million MAUs, 290 million Premium Subscribers.

Sources: https://www.sec.gov/Archives/edgar/data/1543151/000154315126000015/uber-20251231.htm (checked 12 October 2026); https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm (checked 12 October 2026).

### M6. The same Delhi Metro crowd, counted three ways

A PTI report of 30 May 2018 explains that DMRC moved to a "line utilisation" count that tallies every line a passenger uses, so a trip from Noida City Centre to HUDA City Centre with two interchanges counts as three, where the older ridership count (entry and exit at the gates) counted it once. Line utilisation on 29 May 2018 was 45,35,932, while gate-based ridership had been close to 27 lakh a day by February 2018. In 2026 the figures appear in two more units: average daily ridership of 64.06 lakh "passenger journeys" (The Tribune, updated 9 August 2026, citing DMRC), and a record 82,44,903 "passenger boardings" on 17 September 2026 during a bus strike (Republic World, 18 September 2026, quoting DMRC's post).

Teaching use on Monday (a definition changes the number without changing the crowd) and again on Tuesday (check a published number's definition before you validate a guesstimate against it).

Sources: https://www.latestly.com/agency-news/dmrc-uses-new-count-metric-on-traffic-flow-doesnt-share-ridership-190870.html/amp (checked 12 October 2026); https://www.tribuneindia.com/news/delhi/delhi-metro-records-99-95-train-punctuality-in-2026-dmrc/ (checked 12 October 2026); https://www.republicworld.com/india/delhi-metro-breaks-all-time-record-with-8244-lakh-footfall-as-dtc-strike-sends-rush-soaring-2026-09-18-137241 (checked 12 October 2026).

### M7. North-star examples, with the right attribution

Amplitude's article on good and bad North Star metrics (Julia Sholtz, first published 15 August 2024, updated 15 July 2026) gives illustrative examples: Airbnb, nights booked; Spotify, time spent listening; Meta, active users; Amazon, purchases per month; Uber, rides per week; Slack, teams passing a message threshold. It defines a North Star as one metric that reflects the value customers get, that teams can influence, and that predicts future revenue. These are Amplitude's illustrations, and none of them is a statement by the company named. The company-sourced versions are Airbnb's S-1 (M4) and Netflix's engagement proxy (M3).

Source: https://www.amplitude.com/blog/good-bad-north-star-metric (checked 12 October 2026).

### M8. Gaming cases

**Wells Fargo (primary: CFPB 2016, SEC 2020).** The CFPB release of 8 September 2016 announced a USD 100 million CFPB penalty, USD 35 million to the OCC and USD 50 million to the City and County of Los Angeles (USD 185 million in all, our arithmetic), after the bank's own review found roughly 1.5 million deposit accounts and roughly 565,000 credit card accounts that may not have been authorised; refunds of at least USD 2.5 million. Director Cordray: "Wells Fargo employees secretly opened unauthorized accounts to hit sales targets and receive bonuses". The SEC's press release of 21 February 2020 sets a USD 500 million penalty within a combined USD 3 billion settlement with the SEC and the Department of Justice, and says the published cross-sell metric was inflated by unused, unneeded or unauthorised accounts.

The SEC order (Release 34-88257) is the best Monday exhibit we found:
- The metric was the ratio of accounts and products per retail bank household, published from at least 2000 to Q3 2016; it flattened in Q2 2014.
- It had no usage condition: unused accounts stayed in it until closed, which for debit cards, its largest product category, could take up to four years.
- The definition changed silently: in 2013 the bank added global remittance accounts. Of the metric's 0.11 rise that year, 0.04 came from the addition and the rest from accounts inactive for at least 365 days.
- Every guardrail was gamed. Sales credit needed a funded account, so staff moved customers' money into new accounts ("simulated funding"); bill-pay credit needed a payment, so staff prompted token payments; staff changed contact details so customers would not be reached by satisfaction surveys.
- Product sales goals for employees were eliminated in 2016.

Sources: https://www.consumerfinance.gov/about-us/newsroom/consumer-financial-protection-bureau-fines-wells-fargo-100-million-widespread-illegal-practice-secretly-opening-unauthorized-accounts/ (checked 12 October 2026); https://www.sec.gov/newsroom/press-releases/2020-38 (checked 12 October 2026); https://www.sec.gov/files/litigation/admin/2020/34-88257.pdf (checked 12 October 2026).

**US Veterans Affairs, Phoenix wait times (primary: VA Office of Inspector General, 26 August 2014, report 14-02603-267).** Wait time was measured from a "desired date". Thirty of 79 interviewed staff said they entered the wrong desired date, producing false zero-day waits; eleven said they "fixed" waits over 14 days by rebooking the same slot with a later desired date. About 1,400 veterans were on the official electronic wait list on 22 April 2014, and investigators found over 3,500 more waiting off it, many on unofficial lists. Investigations ran at 93 sites; the 14-day goal was removed from employee performance contracts. A clean Monday lesson: the start of a window is part of the definition, and whoever controls it controls the number.

Source: https://www.vaoig.gov/sites/default/files/reports/2014-08/VAOIG-14-02603-267.pdf (checked 12 October 2026).

**English NHS targets (peer-reviewed).** Bevan and Hood, "What's measured is what matters: targets and gaming in the English public health care system", Public Administration 84(3), 517 to 538, August 2006. The abstract describes governance by "targets and terror", argues it rests on taking a part to stand for the whole and on assuming that measurement problems and gaming do not matter, and examines evidence of gaming. Use the abstract only; the specific examples in the body were not read today.

Source: https://api.crossref.org/works/10.1111/j.1467-9299.2006.00600.x (checked 12 October 2026); DOI 10.1111/j.1467-9299.2006.00600.x.

### M9. Guardrail examples

- **Zillow** publicly set "unit economic target guardrails" of plus or minus 200 basis points around breakeven for Zillow Offers (Q3 2021 letter, 2 November 2021). See F3 for how it broke.
- **Swiggy Instamart's Maxxsaver** shows why orders per month is a poor north star. The Q1 FY26 letter (quarter to 30 June 2025) describes a basket-building offer that unlocks extra discounts once a cart passes a threshold; over 28 percent of MTUs used it, AOV rose 16 percent quarter on quarter to Rs 612, and Swiggy notes it sometimes consolidates carts, so the same user places slightly fewer orders. The Q3 FY26 letter (January 2026) attributes weak order growth partly to Maxxsaver-led cannibalisation as customers built larger carts. Kalpa's marketing head proposes orders per month; this is the real-world answer to "how could that number fall while the business improves".
- **DMart** reports growth of stores two years and older (10.8 percent in Q4 FY26) beside total revenue growth (19.0 percent), which separates new-store openings from like-for-like performance (press release, 2 May 2026).

Sources: https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/exhibit993.htm (checked 12 October 2026); https://www.swiggy.com/corporate/wp-content/uploads/2025/07/Q1-FY2026-Shareholder-letter.pdf (checked 12 October 2026); https://www.swiggy.com/corporate/wp-content/uploads/2026/01/Q3-FY2026-Shareholder-letter.pdf (checked 12 October 2026); https://nsearchives.nseindia.com/corporate/DMART_02052026173007_ASLPressRelease02052026.pdf (checked 12 October 2026).

---

## Tuesday: stakeholder communication and guesstimates

### T1. Answer first, and what to leave off

- **Pyramid Principle.** Barbara Minto's site describes the method as organising ideas as a pyramid under a single point so the reader follows the thinking, names the textbook *The Minto Pyramid Principle: Logic in Writing, Thinking and Problem Solving* (1996 edition, replacing the 1987 *Pyramid Principle*), and teaches the SCQ framework for finding the reader's question. https://www.barbaraminto.com/ (checked 12 October 2026).
- **Before-and-after makeovers.** Cole Nussbaumer, "a new year's resolution: declutter your graphics", Storytelling with Data, 4 January 2011: a shopping-habits line chart stripped of borders, gridlines, background tint and most markers, with direct labels replacing a distant legend. https://www.storytellingwithdata.com/blog/2011/01/new-years-resolution-declutter-your (checked 12 October 2026). Alex Velez, "a wordy slide makeover" (hypothetical Mowers Realty survey slide; title rewritten as a takeaway, bullets grouped under headings, key words emphasised; year not shown on the page). https://www.storytellingwithdata.com/blog/a-wordy-slide-makeover (checked 12 October 2026). Index of 30 makeover posts: https://www.storytellingwithdata.com/blog-summary-page-for-makeovers (checked 12 October 2026).
- **The opposite house rule, for debate.** In his 2017 letter (filed 18 April 2018), Bezos writes that Amazon does no slide presentations; meetings open with a silently read, narratively structured six-page memo, and a great memo takes a week or more to write. This pairs with Tuesday's AI-free written business case and makes a good "one slide or six pages" discussion. https://www.sec.gov/Archives/edgar/data/1018724/000119312518121161/d456916dex991.htm (checked 12 October 2026).

### T2. What interviewers score in a guesstimate

Aced (the former Exponent blog; page "35+ Data Analyst Interview Questions & Answers (2026 Guide)", Aced Team, undated) says interviewers want structured reasoning over one correct number, every assumption stated so it can be challenged, scope pinned first (definition, period, context), and the takeaway before the method. https://www.aced.io/blog/top-data-analyst-interview-questions (checked 12 October 2026). The row's Think Insights page (clarify, map, calculate, validate) returned HTTP 403 today; the four steps stay as the row's established method.

### T3. Indian guesstimates with a published number to validate against

Each structure below is a programme sketch; only the check numbers are facts.

| Question | Structure sketch (clarify, map, calculate, validate) | Published check number | Source and date | Catch for the validate step |
|---|---|---|---|---|
| How many smartphones are sold in India in a year? | Clarify units (shipments or sales, new only). Map: adult population, smartphone users, replacement cycle. | 152 million units shipped in 2025, up 0.5 percent; Q4 2025 34 million; record average price USD 282 | IDC press release, 16 February 2026 | IDC counts shipments into the sales channel, which can differ from purchases in any one year. |
| How many UPI transactions happen per day? | Clarify volume versus value. Map: active users times payments per user per day, split person-to-merchant and person-to-person. | 802 million per day on average in September 2026; 24.07 billion in the month, worth Rs 29.37 lakh crore | Outlook Money, 2 October 2026, citing NPCI data | A 30-day month against a 31-day month moves the monthly total; compare per-day figures. |
| How many people ride the Delhi Metro on a weekday? | Clarify journey, boarding or line use. Map: lines times trains times load, or population times share using metro. | 64.06 lakh average daily passenger journeys (2026); record 82,44,903 boardings on 17 September 2026 | The Tribune, 9 August 2026; Republic World, 18 September 2026 (both citing DMRC) | Boardings and journeys are different units (M6). |
| How many two-wheelers are sold in India in a year? | Map: households, ownership, replacement years, first-time buyers. | 2.17 crore domestic sales in FY 2025-26, up 10.7 percent; 20,34,698 in August 2026 | SIAM, 14 April 2026 and 15 September 2026 | October 2025 retail alone was 31.5 lakh (FADA, F5); never annualise a festive month. |
| How many orders does a dark store handle in a day? | Map: catchment households times share ordering times orders per week. | Swiggy Instamart: 1,089 orders per dark store per day in Q1 FY27, across 1,171 stores. Blinkit steady-state assumption: NOV of Rs 11 lakh per store per day | Swiggy letter, 30 July 2026; Eternal letter, 22 July 2026 | Swiggy computes per active store-day; check the denominator. |
| How much does one large-format grocery store sell in a year? (closest to Anand's new-store question) | Map: footfall per day times conversion times basket, times days open. | DMart FY26 standalone revenue Rs 66,968 crore; 85 stores added in FY26 to reach 500. Our arithmetic: about Rs 134 crore per store on the year-end count, about Rs 146 crore on the average of 415 and 500 stores | DMart press release, 2 May 2026 | The denominator choice moves the answer by about 9 percent; a first-year store sells less than a mature one, which is why DMart reports two-year-old stores separately. |

A decimal trap worth using: Flipkart's 9 October 2026 announcement reports 6.3 million concurrent users in a minute at the start of The Big Billion Days, while its URL slug reads "63-million". https://stories.flipkart.com/announcement/india-logs-on-for-the-big-billion-days-flipkart-records-63-million-concurrent-users-as-the-festive-season-opens (checked 12 October 2026).

Sources for the table: https://www.idc.com/resource-center/press-releases/india-smartphone-market-2025-2026/ (checked 12 October 2026); https://www.outlookmoney.com/banking/upi-processes-2407-billion-transactions-worth-rs-2937-lakh-crore-in-september (checked 12 October 2026); https://www.siam.in/news-&-updates/press-releases/x/605 (checked 12 October 2026), which SIAM's site resolves by the trailing number, release title "Auto Industry Performance of Q4 (Jan- March 2026) & FY 2025-26"; https://www.siam.in/news-&-updates/press-releases/auto-industry-performance-of-august-2026/620 (checked 12 October 2026); the Swiggy, Eternal, DMart, DMRC and Tribune URLs given above.

---

## Wednesday: market basket, lift and cross-sell

### W1. Amazon's own account of the confidence trap

Amazon Science, "The history of Amazon's recommendation algorithm" (Larry Hardesty, 22 November 2019), gives three Wednesday lessons in Amazon's words:
- The popularity trap: "Simply counting how often purchasers of item A also bought item B wouldn't do; that would make a few bestsellers like Harry Potter books and trash bags the top recommendations for every customer on every purchase."
- The fix is lift in spirit: item B is related to A if buyers of A are more likely to buy B than the average customer is.
- A second trap, years later: heavy buyers are more likely to buy anything, so the baseline had to be measured per purchase, and moving to that denominator improved quality.
- A bonus for Friday: in a Prime Video test, a plain bestseller list beat a deep-learning autoencoder. The simplest baseline is the one to beat.

The article also records that in 2017 the IEEE Internet Computing editorial board named the 2003 paper the one in its history that best stood the test of time, and that the algorithm had been in use for six years when the paper appeared. The paper itself (Linden, Smith and York, IEEE Internet Computing 7(1), 76 to 80, January 2003) reports more than 29 million customers and several million catalogue items, recommendations returned within half a second from an offline similar-items table, and click-through and conversion rates far above untargeted content such as banner ads and top-seller lists (no figures given). The 2017 follow-up is Smith and Linden, "Two Decades of Recommender Systems at Amazon.com", IEEE Internet Computing 21(3), 12 to 18.

Sources: https://www.amazon.science/the-history-of-amazons-recommendation-algorithm (checked 12 October 2026); https://www.cs.umd.edu/~samir/498/Amazon-Recommendations.pdf (checked 12 October 2026); https://api.crossref.org/works/10.1109/MIC.2003.1167344 (checked 12 October 2026); https://api.crossref.org/works/10.1109/MIC.2017.72 (checked 12 October 2026).

### W2. Beer and diapers: what is documented

Mark Whitehorn, The Register, 15 August 2006: in 1992 a team led by Thomas Blischok at Teradata analysed about 1.2 million transactions from Osco Drug stores and found beer and diapers often bought together in the early evening, with no link to age, gender or day of week; Osco does not appear to have moved any products, and the popular Wal-Mart shelf version is largely invented. Whitehorn's verdict is that almost all the vivid detail is probably fabrication, while the story has real roots. Tell it as a legend with a true core, then put the weight on the arithmetic, as the row asks.

Source: https://www.theregister.com/2006/08/15/beer_diapers/ (checked 12 October 2026).

### W3. Walmart's strawberry Pop-Tarts

OpenStax, *Principles of Data Science*, section 1.2 (CC BY-NC-SA 4.0): ahead of Hurricane Frances in 2004, Walmart staff studied sales from Hurricane Charley a few weeks earlier, found strawberry Pop-Tart sales rose about sevenfold, and shipped extra stock to stores in Frances's path; the analysis also informed cashier scheduling and product placement. It cites Hays (2004). Newsweek (Jason McLure, 12 October 2003) shows the earlier pattern before Hurricane Isabel, naming Wal-Mart among retailers with a Pop-Tart surge and BJ's Wholesale Club at over 20 percent.

Teaching note: this is event-driven demand, a forecasting story more than a pair rule. It makes a good bridge from Wednesday to Friday.

Sources: https://openstax.org/books/principles-data-science/pages/1-2-data-science-in-practice (checked 12 October 2026); https://www.newsweek.com/survival-turn-tart-138555 (checked 12 October 2026).

### W4. Indian basket-building and cross-sell, from filings

- **Swiggy Maxxsaver** (M9): a cart-threshold discount, used by over 28 percent of Instamart MTUs in its launch quarter, lifted AOV 16 percent to Rs 612 while cutting order counts through cart consolidation. Swiggy describes it as returning part of the larger basket's margin to the user, which is the cost line in an expected-value calculation.
- **Swiggy megapods** (Q2 FY25 letter, 3 December 2024): 8,000 to 10,000 sq ft stores with over 50,000 SKUs let a customer get frequent items in 10 minutes and the extended range in 10 to 30 minutes in one basket; Swiggy expects a larger selection to raise share of spend and AOV, which grew 7.3 percent in H1 FY25. By Q1 FY27 net AOV was Rs 508 (from Rs 453), attributed to non-grocery mix and larger baskets.
- **Uber cross-use** (10-K for 2025): in Q4 2025 consumers who used both rides and delivery generated over three times the gross bookings of single-product consumers, and only about one in five eligible consumers was active monthly in both.

Teaching use: these are cross-sell outcomes; none of them proves causation, which is a fair question for the room.

Sources: the Swiggy Q1 FY26, Q2 FY25 and Q1 FY27 letters and the Uber 10-K, URLs above.

### W5. Where the measures come from

Agrawal, Imielinski and Swami (1993), "Mining association rules between sets of items in large databases", SIGMOD, 207 to 216, introduced association rules. Brin, Motwani, Ullman and Tsur (1997), SIGMOD, 255 to 264, DOI 10.1145/253260.253325, is the paper usually credited with the interest (lift) measure; only its metadata was verified today. Sources: https://api.crossref.org/works/10.1145/170035.170072 (checked 12 October 2026); https://api.crossref.org/works/10.1145/253260.253325 (checked 12 October 2026).

### W6. Public data for basket work, with licences

| Dataset | What it holds | Licence | Source |
|---|---|---|---|
| UCI Online Retail II (Daqing Chen) | 1,067,371 invoice lines of a UK online gift retailer, 1 December 2009 to 9 December 2011; invoice, stock code, quantity, date, price, customer ID, country; cancellations marked | CC BY 4.0; cite DOI 10.24432/C5CG6D | https://archive.ics.uci.edu/dataset/502/online+retail+ii (checked 12 October 2026) |
| UCI Online Retail | 541,909 lines, 1 December 2010 to 9 December 2011 | CC BY 4.0; DOI 10.24432/C5BW33 | https://archive.ics.uci.edu/dataset/352/online+retail (checked 12 October 2026) |
| Instacart 2017 | about 3 million grocery orders | Non-commercial, as-is, subject to Instacart's terms, per a search snippet of Instacart's 2017 post; the post returned 403 and the dataset page 404 today | not verified, see the end |

Online Retail II carries customer IDs and two full years of dates, so it also works for Thursday's cohorts and as a public twin of Kalpa's 24 months on Friday.

---

## Thursday: cohort and funnel

### Th1. Blinkit publishes its cohort retention

In Eternal's Q1 FY27 letter (22 July 2026), in the Blinkit section, the CFO calls customer retention the key signal against competitors: Q4 retention (share of customers placing at least one order in the fourth quarter after acquisition) averaged 46 percent across cohorts, every successive cohort improved, and the latest (Q1 FY26) was at 50 percent; Q8 retention was 48 percent and Q12 49 percent. NOV retention averaged 150 percent at Q4, 215 percent at Q8 and 279 percent at Q12, so a cohort spends nearly three times its first-quarter amount three years on. A ready question: how can spend retention pass 100 percent while user retention stays under 50 percent? Survivors spend more.

### Th2. Swiggy publishes a cohort triangle

Swiggy's Q2 FY26 letter (October 2025) prints Instamart cohort spend indexed to the Q4 FY24 cohort's first quarter (Q0 = 100 percent):

| Cohort | Q0 | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 |
|---|---|---|---|---|---|---|---|
| Q4 FY24 | 100% | 240% | 303% | 322% | 304% | 346% | 414% |
| Q1 FY25 | 105% | 287% | 308% | 292% | 333% | 401% | |
| Q2 FY25 | 121% | 289% | 280% | 320% | 387% | | |
| Q3 FY25 | 124% | 261% | 297% | 361% | | | |
| Q4 FY25 | 126% | 261% | 316% | | | | |
| Q1 FY26 | 140% | 311% | | | | | |
| Q2 FY26 | 161% | | | | | | |

The same passage says Swiggy used cohort-level acquisition and retention levers (minimum order thresholds, free deliveries, new-user coupons) and actively weaned away users with low expected lifetime value, and calls these "retained user cohorts". The denominator is the lesson: is this spend per acquired user, per retained user, or the cohort total? Removing weak users lifts every later column.

Source: https://www.swiggy.com/corporate/wp-content/uploads/2025/10/Q2-FY2026-Shareholder-letter.pdf (checked 12 October 2026).

### Th3. A blended number moved by mix, in Swiggy's own tables

- Platform MTU rose from 21.6 million (Q1 FY26) to 27.5 million (Q1 FY27), up 27.4 percent, while platform frequency fell from 4.13 to 3.87 orders per user per month (down 6.3 percent, our arithmetic). Whether existing users ordered less or new, lighter users diluted the average cannot be told from the blend; it needs cohorts.
- The same letter says Swiggy weaned away more than 4 million unprofitable Instamart users over three quarters and that one-month retention of the transacting base rose to 61 percent from 55 percent in Q1 FY26. Part of such a rise can come from the changed mix of who remains, separate from any change in how each cohort behaves.
- Customers who bought the "Switch" own-brand and partner SKUs showed 30 percent higher retention than benchmark cohorts, a selection question for the room.

This is the closest verified real analogue of "blended flat while every cohort declines". No public case of exactly that shape was verified today (see the end).

Source: Swiggy Q1 FY27 letter, URL in M1.

### Th4. Memberships

- **Zomato Gold** (letter dated 19 May 2023): Gold reached 1.8 million members in Q4 FY23; Gold members' orders (with free delivery) were about 30 percent of food delivery GOV in March 2023; and Zomato says these customers' order frequency rose about 60 percent on average after joining. This maps onto Kalpa's Retail-Plus tier and is a clean self-selection question: members choose to join when they expect to order more. https://www.bseindia.com/xml-data/corpfiling/AttachHis/42b3bf3b-1edb-4da7-849a-87ca9da27ff8.pdf (checked 12 October 2026).
- **Amazon Prime**: Bezos's 2017 letter reports more than 100 million paid Prime members globally, 13 years after launch, and more new members joining in 2017 than in any earlier year. URL in T1.
- **Uber One**: 46 million members at 31 December 2025 (M5).

### Th5. Retention benchmark, with caveats

Amplitude, "the 7% retention rule" (Michele Morales, 30 September 2025), drawing on its 2025 Product Benchmark Report of more than 2,600 companies: 7 percent of a new-user cohort returning on day seven puts a product in roughly the top quarter; for enterprise products the day-7 median is 2.1 percent and the top 10 percent reach 12.4 percent; 69 percent of top day-7 performers were also top-tier at three months. These are vendor figures without published method, and the day-7 definition is loose. https://www.amplitude.com/blog/7-percent-retention-rule (checked 12 October 2026).

### Th6. Public data for a cohort exercise

UCI Online Retail II (W6) has customer ID and invoice date across 24 months under CC BY 4.0, enough to build monthly acquisition cohorts and a retention triangle.

---

## Friday: forecasting

### F1. The M competitions on simple methods

Makridakis, Spiliotis and Assimakopoulos, "Statistical and Machine Learning forecasting methods: Concerns and ways forward", PLOS ONE 13(3), 27 March 2018, CC BY 4.0. Its history section states two findings from the forecasting competitions: models that best fit past data did not necessarily forecast the future more accurately, and simple statistical methods were at least as accurate as sophisticated ones. On 1,045 monthly M3 series, scored with sMAPE and MASE, the statistical methods beat every machine-learning method across horizons, and Naive 2 (a seasonally adjusted random walk) was more accurate than half of the machine-learning methods. The paper also criticises studies that report accuracy without comparing to naive benchmarks. Its Figure 3 shows that better in-sample fit did not mean better post-sample accuracy, which is the vendor-curve trap.

Rob Hyndman's post of 19 November 2017 gives the series: M1 with 1,001 series (1982), M3 with 3,003 series (results in IJF 2000). The M4 page at the University of Nicosia: 100,000 series, run January to May 2018, results in IJF 36(1), 2020. Citations verified through Crossref: M3 (IJF 16(4), 451 to 476, 2000), M4 (IJF 36(1), 54 to 74, 2020), M5 (IJF 38(4), 1346 to 1364, 2022).

Sources: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0194889 (checked 12 October 2026); https://robjhyndman.com/hyndsight/m4comp/ (checked 12 October 2026); https://mofc.unic.ac.cy/m4/ (checked 12 October 2026); Crossref records https://api.crossref.org/works/10.1016/S0169-2070(00)00057-1 (checked 12 October 2026); https://api.crossref.org/works/10.1016/j.ijforecast.2019.04.014 (checked 12 October 2026); https://api.crossref.org/works/10.1016/j.ijforecast.2021.11.013 (checked 12 October 2026).

### F2. M5 on Walmart data: the seasonal naive in numbers

The competition (2 March to 30 June 2020, on Kaggle, close to 6,000 participants and about 100,000 submissions) used Walmart unit sales of 3,049 products in 3 categories and 7 departments across 10 stores in California, Texas and Wisconsin, from 29 January 2011 to 19 June 2016 (1,941 days), forecasting 28 days ahead, with price, promotion and event data (Super Bowl, Valentine's Day, Orthodox Easter). Errors were weighted by each series' recent dollar sales, so mistakes on valuable series cost more: an error judged in the business's money, as Friday teaches. The seasonal naive in the guide repeats the same weekday of the previous week.

From the official "Scores and Ranks" workbook (accuracy track, WRMSSE averaged over 12 levels, lower is better):

| Method | Average WRMSSE |
|---|---|
| Winner (team YJ_STU) | 0.520 |
| Best benchmark: exponential smoothing, bottom-up | 0.671 |
| Seasonal naive | 0.847 |
| Moving average | 0.956 |
| Simple exponential smoothing | 0.969 |
| Multilayer perceptron benchmark | 0.977 |
| Random forest benchmark | 1.010 |
| Naive | 1.752 |

Our arithmetic: the seasonal naive's error is 52 percent below the plain naive's and beat both machine-learning benchmarks; the winner was 39 percent below the seasonal naive. The seasonal naive did well on aggregates (0.560 at total level) and badly at item-store level (1.176), where sales are sparse.

Sources: https://mofc.unic.ac.cy/m5-competition/ (checked 12 October 2026); https://raw.githubusercontent.com/Mcompetitions/M5-methods/master/README.md (checked 12 October 2026); https://raw.githubusercontent.com/Mcompetitions/M5-methods/master/M5-Competitors-Guide.pdf (checked 12 October 2026); https://raw.githubusercontent.com/Mcompetitions/M5-methods/master/Scores%20and%20Ranks.xlsx (checked 12 October 2026).

### F3. Zillow Offers, 2021

From Zillow's Q3 2021 shareholder letter and press release (2 November 2021): the business depended on forecasting home prices accurately three to six months ahead; Zillow had set public guardrails of plus or minus 200 basis points of breakeven unit economics; it could not forecast prices within what it had modelled, and unit economics swung about 1,200 basis points from Q2 to an expected minus 500 to minus 700 basis points in Q4 2021. In Q3 it bought 9,680 homes and sold 3,032, ended with 9,790 in inventory and 8,172 under contract, recorded an inventory write-down of about USD 304 million for buying above its current estimates of resale prices, and expected a further USD 240 to 265 million of losses in Q4. Zillow Offers gross profit was a loss of USD 245 million (average minus USD 80,771 per home sold). Homes segment adjusted EBITDA was minus USD 381 million. Inventory rose from USD 491 million (31 December 2020) to USD 3,758 million (30 September 2021). Zillow wound the business down and cut about 25 percent of its workforce.

Sources: https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/exhibit993.htm (checked 12 October 2026); https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/q32021991.htm (checked 12 October 2026); https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/q32021992.htm (checked 12 October 2026).

### F4. Target Canada, the forecasting angle (returns from W01 D3)

Target's release of 15 January 2015: 133 stores, about 17,600 employees, about USD 5.4 billion of Q4 2014 losses on discontinued operations, cash exit costs of USD 500 to 600 million, and no realistic route to profit before at least 2021. Joe Castaldo's Canadian Business account (archived copy; Advisor.ca linked it on 21 January 2016) adds the forecasting failure: the JDA forecasting and replenishment system needed years of history and could not forecast new stores, so buyers used optimistic projections from US headquarters; a former buyer recalls vendors saying Target would sell double what Zellers had, and that going into the first forecast. Target over-ordered, distribution centres overflowed while shelves were empty. A forecast with no history is an assumption, and Kalpa's vendor curve is the same species.

Sources: https://corporate.target.com/press/release/2015/01/target-corporation-announces-plans-to-discontinue-canadian-operations (checked 12 October 2026); https://www.gwern.net/docs/www/archive.canadianbusiness.com/edd0ae069905e7df1b073ae02516993a2bf4a1b9.html (checked 12 October 2026); https://advisor.ca/industry-news/industry/why-target-failed-in-canada/ (checked 12 October 2026).

### F5. Diwali moves, and a calendar-month seasonal naive misses it

Diwali dates from the DoPT holiday memoranda (as reproduced on staffnews.in; DoPT's own site refused the connection today): Thursday 31 October 2024; Monday 20 October 2025; Sunday 8 November 2026. The repository's facts file already locks 9 November 2026 as "the Monday after Diwali". A seasonal naive that copies October 2025 into October 2026 carries a Diwali month into a month that has none this year.

FADA, the dealers' federation, aligns its festive window to the festival dates each year: 42 days from the first day of Navratri to 15 days after Dhanteras, which was 22 September to 2 November 2025 against 3 October to 13 November 2024. Its release of 7 November 2025 reports festive-window retail of 52,38,401 vehicles against 43,25,632 (up 21.10 percent), two-wheelers 40,52,503 against 33,27,198, and October 2025 two-wheeler retail of 31,49,846 against 12,87,735 in September (up 144.60 percent month on month). FADA itself attributes part of the jump to GST rate cuts that coincided with the festivals, so this is also a confounding lesson. Registrations lag sales, which is why the window runs past Diwali.

Sources: https://www.staffnews.in/2023/07/list-of-holidays-2024-dopt-order-reg-gazetted-and-restricted-holidays.html (checked 12 October 2026); https://www.staffnews.in/2024/07/holidays-to-be-observed-in-central-government-offices-year-2025.html (checked 12 October 2026); https://www.staffnews.in/2025/07/list-of-holidays-2026-dopt-order-reg-closed-and-restricted-holidays.html (checked 12 October 2026); https://fada.in/images/press-release/1690d68d7a2e6cFADA%20releases%20October%202025%20&%2042-Days%20Festive%20Vehicle%20Retail%20Data.pdf (checked 12 October 2026).

### F6. Festive demand from company statements

- **Flipkart, The Big Billion Days 2026** (13th edition; early access from 8 October, main sale 9 October 2026): 14 million cubic feet of warehouse space added (50 percent more storage), more than 2.5 lakh festive jobs, transacting sellers up over 60 percent on last year (announcement of 6 October 2026); 6.3 million concurrent users in a minute in the opening hour and over six times the shoppers of a typical hour (announcement of 9 October 2026). Capacity and hiring are forecast-driven decisions made weeks earlier. https://stories.flipkart.com/announcement/flipkarts-big-billion-days-returns-for-its-13th-edition (checked 12 October 2026) and the 9 October URL in T3.
- **Amazon Great Indian Festival 2025**: over 276 crore customer visits, 70 percent from tier 2 and 3 cities; more than 4 crore Prime products delivered. The page shows no publication date. https://www.aboutamazon.in/news/retail/amazon-great-indian-festival-2025-highlights-results (checked 12 October 2026).
- **One-off spikes**: DMart's MD notes a burst of consumer buying in March 2026 linked to geopolitical tensions that normalised by month end (2 May 2026 release); Blinkit's 19 percent quarter-on-quarter NOV growth in Q1 FY27 was "largely seasonality" per its CEO, and Blinkit's inventory losses were about 1.8 percent of NOV, mostly perishables (Eternal letter, 22 July 2026).

---

## Interview preparation across the week

What interviewers say they listen for, from Aced's 2026 analyst guide (URL in T2): structure over the final number; stated assumptions; scope first (definition, period, context); data and tracking checked before behaviour is blamed; segmentation before root cause; separating fewer users from less use per user; correlation kept apart from causation; and for A/B tests, significance treated as necessary but not sufficient, with effect size, planned duration and sample checked and the result tied to a decision. Evan Miller, "How Not To Run an A/B Test" (18 April 2010): stopping a test when it first looks significant inflates false positives; in his example a change with no effect, checked after every observation at a nominal 5 percent level, is declared significant 26.1 percent of the time; the fix is to fix the sample size in advance. https://www.evanmiller.org/how-not-to-run-an-ab-test.html (checked 12 October 2026).

The questions below are written for this programme in the style of product-company and GCC screens; tags follow the row's calibration ([S] staple, [F] frequent, [D] differentiator). Company-specific interview reports for Walmart Global Tech India, Target in India, Flipkart and Swiggy were not verified today.

| # | Question | Tag | Rubric points the interviewer listens for | Common failure | Source for the pattern |
|---|---|---|---|---|---|
| 1 | How would you measure the success of a new feature? | S | Goal and user first; one primary metric with numerator, denominator, window; two guardrails; a leading indicator; how it will be tested | Ten metrics, no primary, no definitions | Aced guide |
| 2 | Write Swiggy's MTU definition and say what it leaves out | F | Unique users with at least one completed order per month, averaged; excludes browsers and cancelled orders | Confuses with registered users | Swiggy letter, M1 |
| 3 | Why would Eternal drop GOV for NOV, and what did GOV reward? | F | GOV counts discounted value, so growth can be bought; NOV = GOV minus discounts | Calls them synonyms | Eternal letters, M2 |
| 4 | Give a north-star and guardrail pair for a quick-commerce app | F | Value outcome as north star; guardrail that catches harmful ways of hitting it, such as discount share of GOV | A guardrail that is another growth count | Amplitude article; Zillow guardrail |
| 5 | What makes a metric gameable, and how do you write one that is not? | F | Counts actions without a quality or usage condition; measured person controls inputs; silent definition changes | "Just audit it" | SEC order on Wells Fargo |
| 6 | A metric improved while the service got worse. Give an example and the check | F | Window start controlled by staff (VA desired date); independent audit of the start point | No mechanism named | VA OIG 2014 |
| 7 | How can a booking count be negative? | D | Net of cancellations recognised when they occur; timing of recognition | Assumes a data error | Airbnb S-1 |
| 8 | Orders per month or value per member as the north star, given a basket-threshold offer? | D | Threshold offers raise AOV and cut order counts; pick value, keep frequency as a leading signal | Picks orders per month | Swiggy Maxxsaver letters |
| 9 | Classify sessions, add-to-cart, month-3 retention and revenue as leading or lagging | S | Order along the causal chain; lead time; what moves first | Treats revenue as leading | Amplitude (north star predicts revenue) |
| 10 | Present a recommendation to a non-technical leader in two minutes | S | Claim first, one number with its denominator, caveat, action with cost | Method first, nine numbers | Minto; Aced |
| 11 | A stakeholder's objection is partly right. How do you answer? | F | Restate until they agree, concede the true part, answer from evidence, say what would change your mind | Retreats or overclaims | Row method (programme) |
| 12 | Estimate smartphones sold in India per year | S | Units clarified; population to users to replacement; validate near IDC's 152 million (2025) | No stated assumptions | Aced; IDC |
| 13 | Estimate UPI transactions per day | S | Volume versus value; users times frequency; validate near 802 million per day (September 2026) | Mixes count and rupees | Outlook Money citing NPCI |
| 14 | Estimate Delhi Metro riders on a weekday | F | Defines journey versus boarding; validates in the same unit | Compares with the wrong unit | PTI 2018; Tribune; Republic World |
| 15 | Estimate two-wheelers sold per year in India | F | Households, ownership, replacement; validate near 2.17 crore (FY26); seasonality | Annualises a festive month | SIAM; FADA |
| 16 | How many orders does a dark store handle per day? | D | Catchment times frequency; validate near Swiggy's 1,089 per store-day | Ignores store-day denominator | Swiggy letter |
| 17 | What will a new store sell in its first year? | D | Footfall, conversion, basket; mature versus new; denominator choice moves a DMart-based check from about Rs 134 to 146 crore | Uses mature-store averages for year one | DMart release, our arithmetic |
| 18 | What do you leave off the slide, and where does it go? | F | One exhibit, the rest to an appendix kept for a named question | Everything on the slide | SWD makeovers; Amazon memo |
| 19 | Support, confidence, lift: which cannot be fooled by popularity? | S | Lift compares with the base rate; Amazon's bestseller example | Picks confidence | Amazon Science |
| 20 | A pair has lift 4 and support 0.3 percent. Act or not? | F | Expected value with support times baskets times margin; watch list or small test | Acts on lift alone | Row method (programme) |
| 21 | Turn a basket analysis into a rupee recommendation | F | Incremental orders times margin minus promotion cost, including margin returned to the user and lost orders | Gross sales as the benefit | Swiggy Maxxsaver letters |
| 22 | Why would heavy buyers inflate lift, and what is the fix? | D | Heavy buyers buy everything; measure the base rate per purchase | Never asks about denominators | Amazon Science |
| 23 | Tell the beer-and-diapers story accurately | S | 1992, Osco Drug, about 1.2 million transactions, evening pattern, no documented shelf move | Repeats the legend as fact | The Register 2006 |
| 24 | Why did Walmart ship strawberry Pop-Tarts before Frances? Is it a basket rule? | F | Event-conditioned demand from Charley's sales, about sevenfold; a forecast | Calls it an association rule | OpenStax |
| 25 | A bestseller list beat a deep model. What does that teach? | D | Always benchmark against the simplest method | Assumes complexity wins | Amazon Science; PLOS ONE |
| 26 | Retention dropped. Walk me through your investigation | S | Tracking first; definition; segment by cohort, platform, region; fewer users versus less use; funnel stage | Jumps to a cause | Aced guide |
| 27 | Blended retention is flat while every cohort declines. How? | F | Mix shift: cohort sizes and ages change the blend; decompose | "Impossible" | Swiggy frequency and retention, Th3 |
| 28 | Zomato says Gold members order about 60 percent more after joining. Does Gold cause it? | F | Self-selection; matched non-joiners, pre-trends or a holdout | Accepts before-after as causal | Zomato letter, Th4 |
| 29 | How can spend retention be 150 percent when user retention is 46 percent? | F | Survivors spend more; different numerators | Thinks one figure is wrong | Eternal letter, Th1 |
| 30 | What denominator do you ask for before trusting a company's cohort chart? | D | Per acquired, per retained or total; removed users | Reads the curve at face value | Swiggy letter, Th2 |
| 31 | A funnel stage drops 40 percent. Loss or artefact? | F | Each stage's denominator; sessions versus users; tracking change | Blames the stage owner | Aced guide (tracking first) |
| 32 | What is good day-7 retention? | S | Depends on category; Amplitude's 7 percent top-quartile line, 2.1 percent enterprise median; vendor caveat | Quotes one universal number | Amplitude 2025 |
| 33 | p = 0.04 after three days. Do you launch? | S | Planned sample and duration; peeking inflates false positives; effect size and cost; guardrails | Launches on the p-value | Evan Miller; Aced |
| 34 | How do you evaluate a forecast? | S | Hold out the latest periods; error in business units; compare with naive and seasonal naive | Judges by in-sample fit | PLOS ONE; M5 guide |
| 35 | What baseline must any forecast beat? | F | Seasonal naive for seasonal data; M5: 0.847 against 1.752 for naive, ahead of the ML benchmarks | Names only "last value" | M5 scores |
| 36 | A vendor curve fits the past perfectly and promises 22 percent. Test it | F | Out-of-sample test; check for an extrapolated spike; ask what history it rests on | Trusts the fit | PLOS ONE; Target Canada |
| 37 | Diwali moves from 20 October 2025 to 8 November 2026. What breaks? | D | Calendar-month seasonal naive misplaces the spike; align to the festival | Copies last October | DoPT dates; FADA windows |
| 38 | What did forecast error cost Zillow, and which guardrail failed? | D | 3 to 6 month price forecasts; plus or minus 200 bps guardrail; about 1,200 bps swing; USD 304 million write-down | Calls it bad luck only | Zillow letter |
| 39 | MAE in rupees or MAPE in percent? | F | MAE when the decision is in rupees; MAPE fails near zero sales | One metric for all | M5 dollar weighting; FPP3 (not re-fetched today) |
| 40 | Finance and Marketing each want their forecast in front of the board. How do you choose and present the error? | D | Same hold-out, same error measure, decided before scoring; typical error in rupees; what would make it wrong | Splits the difference | Row method; PLOS ONE |

---

## Unverified, do not use

- The New York Times article of 14 November 2004 by Constance L. Hays, including Linda Dillman's exact quote, the "seven times" wording tied to Frances, and beer as the top pre-hurricane seller: the NYT refused the fetch and the web archive was unreachable. Use the OpenStax wording in W3.
- Wells Fargo firing counts (often given as about 5,300) and the later "3.5 million accounts" figure: not fetched.
- Goodhart's 1975 wording and Strathern's 1997 phrasing of the law: not fetched.
- Specific NHS gaming examples inside Bevan and Hood (for example ambulance response times): only the abstract was read.
- Call-centre handle-time gaming and app-install vanity-metric cases: no primary source found today.
- Spotify naming "time spent listening" as its own north star: only Amplitude's illustration exists in our sources.
- Flipkart Big Billion Days 2025 totals: no official statement found; third-party figures seen are not usable.
- Reliance Retail Q1 FY27 store count, registered customers and transactions: only secondary write-ups seen.
- Instacart 2017 licence wording: the Instacart pages returned 403 and 404; the non-commercial term comes from a search snippet only.
- M4 findings beyond scale (combinations, the hybrid winner, machine-learning results) and the M5 paper's conclusions: ScienceDirect blocked the fetch.
- Kaggle's data-use terms for M5: not fetched.
- The content of Brin et al. 1997 and Fabijan et al. 2019 (sample ratio mismatch): only their metadata was verified.

## Not yet verified (open items for a follow-up pass)

- FPP3 sections 5.2 and 5.8 (otexts.com returned 403 today); the Management Consulted Pyramid Principle page and the Think Insights guesstimates page in the row (both 403 today); IGotAnOffer market sizing (not fetched).
- NPCI's own UPI statistics page (403); the figure rests on Outlook Money's report of NPCI data.
- A public case where a blended retention figure stayed flat while cohorts declined (for example the cohort charts in Groupon's 2011 S-1).
- Current Zomato Gold and Swiggy One member counts (not in the 2026 letters read).
- Interview reports specific to Walmart Global Tech India, Target in India, Flipkart and Swiggy (Glassdoor, AmbitionBox).
- DMRC's own definition of "passenger journeys" versus "boardings" in 2026.

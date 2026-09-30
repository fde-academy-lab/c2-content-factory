# Sources: the retail domain dossier, the domain card and the domain story

**INTERNAL.** Every source behind `study-notes/C2_W01_D01_domain_retail_STUDENT.md` (the dossier), `cheatsheets/C2_W01_D01_retail_domain_card_STUDENT.md` and its PDF (the card), and `trainer/C2_W01_D01_domain_story_TRAINER.md` (the talk track), with the date each was checked, how it was reached, and a line per fact on where it came from.

---

## What the files are built from

| Source in the repository | What it supplied |
|---|---|
| The requester's brief of 30 September 2026, relayed by the orchestrating session | The four deliverables, the dossier's twelve sections, the likeness framing, and Kalpa Health's repositioning as a US-facing diagnostics and revenue-cycle business |
| `main` after this branch was cut (commits f788634, faf5c8e and db185d8, read on 30 September 2026) | Client zero section 1c and addendum `health-us-facing` (Kalpa Health serves the US); decision `four-domains`; `.claude/skills/day-pack-builder/references/domain-dossier.md`, which names this dossier as the model; the spine's line that Monday's domain story takes 45 minutes in place of the 20-minute ask |
| `CLAUDE.md` | The truth order, the writing rules, the plant rule, the diagram rule, durations only, role labels |
| `docs/07_Client_Zero.md`, v2.2 locked 13 September 2026, with the GCC addendum of 28 September 2026 | Kalpa Group's headquarters and five units, the Bengaluru centre as the GCC, the people in section 1a, 4 percent growth against a 15 percent plan, the Build 1, 2 and 3 seeds |
| `docs/curriculum/W1_Data_analysis_found.md` and `W2_Data_manipulation.md`, tracker v7 | Kalpa Retail selling through app, website and stores across India and South-East Asia; marketing's Rs 12 crore; the chief of staff's Week 2 Friday ask; the week's scenarios, which the dossier never pre-empts |
| `docs/detailing/W01_W02_spine.md`, approved 29 September 2026 | The traps each day stages, checked so the dossier's generic traps use different numbers from the staged ones |
| `data/programme/facts.yaml`, as of 30 September 2026 | Decision `anand-finance-controller` (Anand Iyer is the finance controller); decision `plants-once-found`; the Kalpa Logistics stakeholder's name listed as open; the holiday on Monday 9 November 2026, the day after Diwali |
| `content/W01/D1/` as it stood on 30 September 2026 | The house form of notes, sheet, day sheet and provenance, and the mermaid palette |

## Kalpa facts, and where each comes from

| Kalpa fact as the files state it | Where it comes from |
|---|---|
| Kalpa Group is headquartered in Singapore, with Retail, Financial Services, Logistics, Health and Connect | `docs/07_Client_Zero.md`, section 1 |
| The Bengaluru engineering and data centre is Kalpa's GCC, and the cohort are trainee engineers in its data and AI team | `docs/07_Client_Zero.md`, section 1b |
| Kalpa Retail sells consumer goods through its app, website and stores across India and South-East Asia | Week 1 Monday row, business scenario |
| Revenue grew 4 percent last year against a plan of 15; marketing wants Rs 12 crore to acquire customers | `docs/07_Client_Zero.md`, section 1; Week 1 Monday row |
| Meera Raghavan, CEO; Anand Iyer, finance controller; the head of Retail-Plus; the marketing lead; the data platform lead; Kavya Nair, senior analyst | `docs/07_Client_Zero.md`, section 1a; `facts.yaml` decision `anand-finance-controller` |
| Farhan Sheikh, head of customer support, from Week 8, two thousand tickets a day | `docs/07_Client_Zero.md`, section 1a |
| Rohan Desai from Week 5; a default costs twenty times a wrongful rejection | `docs/07_Client_Zero.md`, section 1a and the Build 2 seeds |
| Dr Priya Menon, COO of Kalpa Health, the Build 1 stakeholder; Ananya Bose, COO of Kalpa Connect, Build 3 | `docs/07_Client_Zero.md`, section 1a and the Build seeds |
| Kalpa Health tests US patients and bills US payers, with its analytics and revenue-cycle work run from the GCC in Bengaluru | The requester's brief, 30 September 2026, and on `main` client zero section 1c with addendum `health-us-facing` |
| The programme's four domains and when each enters: retail and e-commerce now, US healthcare on Build 1 Monday, financial services from Week 5, SaaS and enterprise AI from Week 8 | Decision `four-domains`, on `main` |
| The Kalpa Logistics stakeholder is not yet named | `facts.yaml`, `client_zero.proposed.open` |
| Meera's chief of staff asks for the leadership deck's numbers | Week 2 Friday row |

## External sources, checked on 30 September 2026

Every source below was opened on 30 September 2026 unless the note says otherwise. "WebFetch" is the session's page reader; "curl" means the file was downloaded and read as text, because the page reader was refused.

| # | Source | URL | Checked | How |
|---|---|---|---|---|
| 1 | Reliance Industries, media release on the quarter to 30 June 2026, dated 17 July 2026 | https://www.ril.com/sites/default/files/2026-07/Media_Release_RIL_Q1_FY2026-27_Financial_and_Operational_Performance.pdf | checked 30 Sep 2026 | curl, 200, PDF read in full |
| 2 | Tata group, business overview | https://www.tata.com/business/overview | checked 30 Sep 2026 | WebFetch |
| 3 | Tata group, Tata Capital company page | https://www.tata.com/business/tata-capital | checked 30 Sep 2026 | curl, 200 |
| 4 | Walmart corporate, "Walmart in India" | https://corporate.walmart.com/about/international/markets/india | checked 30 Sep 2026 | WebFetch |
| 5 | Walmart corporate news, completion of the Flipkart investment, 18 August 2018 | https://corporate.walmart.com/news/2018/08/18/walmart-and-flipkart-announce-completion-of-walmart-investment-in-flipkart-indias-leading-marketplace-ecommerce-platform | checked 30 Sep 2026 | WebFetch |
| 6 | Analytics India Magazine, "Target Expands Bengaluru GCC With New Campus in Manyata", 29 September 2026 | https://analyticsindiamag.com/ai-news/target-expands-bengaluru-gcc-with-new-campus-in-manyata | checked 30 Sep 2026 | WebFetch |
| 7 | Tesco Bengaluru, home page | https://www.tescobengaluru.com/ | checked 30 Sep 2026 | WebFetch |
| 8 | Lowe's India, About page and "Lowe's India marks 10-year milestone", 29 October 2024 | https://lowes.co.in/about/ and https://lowes.co.in/news/lowes-india-marks-10-year-milestone-in-country/ | checked 30 Sep 2026 | WebFetch, both |
| 9 | Avenue Supermarts (DMart), press release on results for the year to 31 March 2026, dated 2 May 2026 | https://api.dmartindia.com/corporate/content/file/v1/2/R2aWBiIpiuD39xgfm4wrqQKc1777723315/Press%20release%20dated%202nd%20May,%202026 | checked 30 Sep 2026 | curl, 200, PDF read in full |
| 10 | Business Standard, "Trent posts 19% YoY rise in Q1 revenue; store count rises to 1,312", 7 July 2026 | https://www.business-standard.com/markets/capital-market-news/trent-posts-19-yoy-rise-in-q1-revenue-store-count-rises-to-1-312-126070700484_1.html | checked 30 Sep 2026 | curl, 200 (WebFetch refused) |
| 11 | Trent Limited, home page | https://www.trentlimited.com/ | checked 30 Sep 2026 | WebFetch; brands Westside, Zudio and Star Bazaar |
| 12 | Amazon, "Sell on Amazon" terms of use | https://sell.amazon.in/standards/terms-of-use | checked 30 Sep 2026 | WebFetch |
| 13 | MediaNama, "7 key takeaways from Eternal Q1 FY27 earnings call", 24 July 2026 | https://www.medianama.com/2026/07/223-takeaways-eternal-q1-fy27-earnings-call/ | checked 30 Sep 2026 | WebFetch |
| 14 | All India Radio News, "Delivery aggregators agree to drop 10-minute delivery deadline after government intervention", 13 January 2026 | https://www.newsonair.gov.in/delivery-aggregators-agree-to-drop-10-minute-delivery-deadline-after-government-intervention-sources | checked 30 Sep 2026 | WebFetch |
| 15 | The Quint, on the Labour Ministry's memo to Blinkit, Swiggy Instamart and Zepto, 15 January 2026 | https://www.thequint.com/jobs/10-minute-delivery-blinkit-swiggy-instamart-zepto-order-stop-promoting-what-changes-for-partners-latest-news | checked 30 Sep 2026 | WebFetch |
| 16 | About Amazon India, "A guide to Amazon Prime membership plans, price and benefits in India" | https://www.aboutamazon.in/news/retail/new-amazon-prime-membership-plans-in-india | checked 30 Sep 2026 | curl, 200 |
| 17 | About Amazon India, Great Indian Festival 2025 and Prime early access | https://www.aboutamazon.in/news/amazon-prime/amazon-great-indian-festival-2025-prime-members-early-access-benefit | checked 30 Sep 2026 | WebFetch |
| 18 | Flipkart Stories, "Access a premium digital lifestyle with Flipkart Black", 12 September 2025 | https://stories.flipkart.com/flipkart-black-loyalty-program-2025 | checked 30 Sep 2026 | WebFetch |
| 19 | NBC Select, "Walmart Plus: What to Know and How to Save", updated 25 September 2026 | https://www.nbcnews.com/select/shopping/what-walmart-plus-rcna263677 | checked 30 Sep 2026 | WebFetch; walmart.com served a robot check |
| 20 | Quest Diagnostics, About us | https://www.questdiagnostics.com/our-company/about-us | checked 30 Sep 2026 | WebFetch |
| 21 | Labcorp, About us | https://www.labcorp.com/about-us | checked 30 Sep 2026 | WebFetch |
| 22 | Omega Healthcare, Revenue cycle management | https://www.omegahms.com/solution/revenue-cycle-management/ | checked 30 Sep 2026 | WebFetch |
| 23 | Business Standard, "Flipkart's Ekart opens nationwide logistics network to third-party biz", 28 July 2026 | https://www.business-standard.com/amp/companies/start-ups/flipkart-s-ekart-opens-nationwide-logistics-network-to-third-party-biz-126072801174_1.html | checked 30 Sep 2026 | curl, 200 |
| 24 | Andreessen Horowitz, "16 Startup Metrics", 21 August 2015 | https://a16z.com/16-startup-metrics/ | checked 30 Sep 2026 | WebFetch |
| 25 | DPIIT, Press Note No. 2 (2018 Series), dated 26 December 2018, effective 1 February 2019 | https://www.dpiit.gov.in/static/uploads/2025/07/2959b696766693441f5eb45d3eb49f97.pdf | checked 30 Sep 2026 | curl, 200, PDF read (WebFetch refused) |
| 26 | EY India tax alert on Press Note 3 (2026 Series), September 2026 | https://www.ey.com/en_in/technical/alerts-hub/2026/09/dpiit-permits-foreign-investment-in-export-oriented | checked 30 Sep 2026 | WebFetch |
| 27 | DPIIT, Consolidated FDI Policy Circular of 2020 | https://www.dpiit.gov.in/static/uploads/2025/07/3ab2ec2a3bdb91c69653b7c34618c14a.pdf | checked 30 Sep 2026 | curl, 200, PDF searched |
| 28 | DPIIT, Press Note No. 5 (2012 Series), 20 September 2012, background only | https://www.dpiit.gov.in/static/uploads/2025/07/384fbc020758137b3622fd8dd7bbf016.pdf | checked 30 Sep 2026 | curl, 200 |
| 29 | GST Council, press release on the 56th meeting, PIB, 3 September 2025 | https://gstcouncil.gov.in/sites/default/files/2025-09/press_release_press_information_bureau_0.pdf | checked 30 Sep 2026 | curl, 200, PDF read |
| 30 | GST Council, Notification 10/2023-Central Tax, 10 May 2023 | https://www.gstcouncil.gov.in/node/4365 | checked 30 Sep 2026 | WebFetch |
| 31 | TaxGuru, on Notification 15/2024-Central Tax, 10 July 2024 | https://taxguru.in/goods-and-service-tax/cgst-e-commerce-operator-tcs-collection-rate-reduced-0-25-percent.html | checked 30 Sep 2026 | WebFetch |
| 32 | TaxGuru, tax invoice requirements under section 31 and Rule 46, 8 February 2025 | https://taxguru.in/goods-and-service-tax/tax-invoice-requirements-section-31-cgst-act-gst-rule-46.html | checked 30 Sep 2026 | WebFetch; the CBIC rules page could not be reached |
| 33 | Indian Kanoon, Legal Metrology (Packaged Commodities) Rules 2011, rule 6 | https://indiankanoon.org/doc/38209662/ | checked 30 Sep 2026 | WebFetch |
| 34 | Indian Kanoon, Legal Metrology (Packaged Commodities) Rules 2011, rule 18 | https://indiankanoon.org/doc/82453918/ | checked 30 Sep 2026 | WebFetch |
| 35 | Mondaq, "E-Commerce Entities: Legal Metrology (Packaged Commodities) Amendment Rules, 2017" | https://www.mondaq.com/india/commoditiesderivativesstock-exchanges/662702/e-commerce-entities---legal-metrology-packaged-commodities-amendment-rules-2017 | checked 30 Sep 2026 | WebFetch |
| 36 | SCC Online, "Legal Metrology (Packaged Commodities) Amendment Rules, 2021", 8 November 2021 | https://www.scconline.com/blog/post/2021/11/08/legal-metrology-packaged-commodities-amendment-rules-2021/ | checked 30 Sep 2026 | WebFetch |
| 37 | IBC Laws, full text of the Consumer Protection (E-Commerce) Rules 2020, G.S.R. 462(E) of 23 July 2020 | https://ibclaw.in/consumer-protection-e-commerce-rules-2020/ | checked 30 Sep 2026 | WebFetch, twice; consumeraffairs.nic.in could not be reached |
| 38 | PIB, "Central Consumer Protection Authority issues Guidelines for Prevention and Regulation of Dark Patterns, 2023", 8 December 2023 | https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=1983994 | checked 30 Sep 2026 | curl, 200 (WebFetch refused) |
| 39 | PIB explainer, "DPDP Rules, 2025 Notified", 17 November 2025 | https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf | checked 30 Sep 2026 | curl, 200, PDF read |
| 40 | RBI circular RBI/2021-22/96, "Tokenisation: Card Transactions, Permitting Card-on-File Tokenisation (CoFT) Services", 7 September 2021 | https://rbi.org.in/Scripts/NotificationUser.aspx?Id=12159&Mode=0 | checked 30 Sep 2026 | curl, 200 |
| 41 | BusinessToday, "RBI extends card tokenisation deadline till September 30", 24 June 2022 | https://www.businesstoday.in/latest/policy/story/rbi-extends-card-tokenisation-deadline-till-september-30-339120-2022-06-24 | checked 30 Sep 2026 | WebFetch |
| 42 | PCI Security Standards Council blog, "Just Published: PCI DSS v4.0.1", 11 June 2024 | https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1 | checked 30 Sep 2026 | WebFetch |
| 43 | California Attorney General, CCPA page | https://www.oag.ca.gov/privacy/ccpa | checked 30 Sep 2026 | WebFetch |
| 44 | California Privacy Protection Agency, announcement of 23 September 2025 | https://cppa.ca.gov/announcements/2025/20250923.html | checked 30 Sep 2026 | WebFetch |
| 45 | Klarna, "Klarna AI assistant handles two-thirds of customer service chats in its first month", 27 February 2024 | https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/ | checked 30 Sep 2026 | curl, 200 |
| 46 | Fortune, "As Klarna flips from AI-first to hiring people again...", 9 May 2025 | https://fortune.com/2025/05/09/klarna-ai-humans-return-on-investment/ | checked 30 Sep 2026 | WebFetch |
| 47 | McCarthy Tétrault, "Moffatt v. Air Canada: A Misrepresentation by an AI Chatbot" | https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot | checked 30 Sep 2026 | WebFetch; CanLII refused the page reader |
| 48 | About Amazon India, launch of Rufus in India, published 20 November 2024 | https://www.aboutamazon.in/news/retail/rufus-ai-shopping-assistant-launch-in-india | checked 30 Sep 2026 | curl, 200; date from the page's datePublished |
| 49 | OfficeHolidays, Diwali 2025 in India | https://www.officeholidays.com/byday/diwali/2025 | checked 30 Sep 2026 | WebFetch |
| 50 | Wikipedia, Diwali (the 2026 dates) | https://en.wikipedia.org/wiki/Diwali | checked 30 Sep 2026 | WebFetch |
| 51 | YouTube oEmbed for Think School's DMart video | https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=B5txS_lC1yY&format=json | checked 30 Sep 2026 | curl, 200; title and channel only |

## Fact by fact

Where: D is the dossier and its section, C is the card and its panel, T is the talk track and its part.

| Fact as the files state it | Where | Source |
|---|---|---|
| Reliance: Jio's 533 million subscribers (533.3 million), Reliance Retail's 20,169 stores, JioMart serving about 5,500 pin codes, and the oil-to-chemicals segment, in the quarter to 30 June 2026. Jio-bp was left out of the opening scene because it is a joint venture with bp | D2, T2 | 1 |
| Reliance Retail: gross revenue Rs 90,408 crore and revenue from operations Rs 79,745 crore in the quarter; the consolidated statement's step is "Less: GST Recovered" | D3 | 1 |
| Reliance Retail: EBITDA margin 7.9 percent, calculated on revenue from operations | D3 | 1 |
| Reliance Retail: grocery like-for-like growth of 7 percent; 396 million registered customers | D5, T facts | 1 |
| Jio: revenue per user Rs 215.6 per subscriber per month; monthly churn 1.6 percent | D2, T facts | 1 |
| Tata: founded in 1868; 31 companies; ten verticals including consumer and retail, financial services, telecom and media; Tata Sons the principal investment holding company and promoter | D2, T2 | 2 |
| Tata Capital: a Tata company engaged in lending | D2 | 3 |
| Walmart Global Tech teams in Bengaluru, Chennai and Gurugram | D2, T2 | 4 |
| PhonePe: more than 520 million registered users, 38 million merchants, more than 230 million transactions a day, as Walmart describes it | D2 | 4 |
| Walmart has held about 77 percent of Flipkart since August 2018 | D2, T facts | 5 |
| Target in India: an integrated headquarters of the Minneapolis company, operating in India for more than 21 years, its expanded Bengaluru campus to bring together more than 5,700 team members | D2, T2 | 6 |
| Tesco Bengaluru: since 2004, more than 4,000 colleagues | D2, T2 | 7 |
| Lowe's India: established 2014, more than 5,000 associates across technology, analytics, finance and shared services | D2, T2 | 8 |
| DMart: 500 stores at 31 March 2026; "everyday low cost, everyday low price"; FY26 standalone revenue Rs 66,968 crore, EBITDA margin 7.8 percent, profit-after-tax margin 4.8 percent; stores two years and older grew 10.8 percent in the quarter to March 2026 | D2, D3, D5, T3, T5 | 9 |
| DMart Ready, DMart's online grocery business, operated in 18 cities at 31 March 2026 | D3 | 9 |
| Trent: 301 Westside and 982 Zudio stores at 30 June 2026 | D2, T facts | 10, 11 |
| Amazon's seller terms call amazon.in the "Marketplace" on which registered sellers sell | D2 | 12 |
| Blinkit: 2,443 dark stores at the end of the quarter to June 2026; net average order value Rs 518 | D2, D3, D10, T facts | 13 |
| Blinkit, Swiggy Instamart and Zepto as the quick-commerce platforms; Blinkit dropped the "10-minute" promise from its branding in January 2026 after a government intervention, and the aggregators agreed to drop the deadline | D2, D10, T facts | 14, 15 |
| Amazon Prime in India: plans from Rs 399 to Rs 1,499 a year | D2 | 16 |
| Amazon Great Indian Festival 2025 from 23 September, with 24-hour early access for Prime members on 22 September | D2, D10 | 17 |
| Flipkart Black: Rs 1,499 a year, evolved from the VIP programme, announced in 2025 | D2 | 18 |
| Walmart+: $98 a year or $12.95 a month | D2 | 19 |
| Quest Diagnostics serves one in three adult Americans each year | D2 | 20 |
| Labcorp: more than 71,000 employees | D2 | 21 |
| Omega Healthcare verifies insurance, codes, bills, manages denials and collects for US providers | D2 | 22 |
| Ekart: the Flipkart group's logistics arm, reaching more than 95 percent of Indian pin codes, opening to other businesses | D2 | 23 |
| GMV defined as "the total sales dollar volume of merchandise transacting through the marketplace in a specific period"; blended against paid CAC; retention by cohort | D3, D5, D12 | 24 |
| FDI permitted up to 100 percent in marketplace e-commerce and not in the inventory model; no ownership or control of inventory; a seller deemed controlled above 25 percent of purchases from the marketplace group; no influence on sale prices; effective 1 February 2019 | D3, D7, T3, C5 | 25 |
| Press Note 3 of 2026, dated 23 July 2026: an inventory model only for exporting goods made in India; the domestic restriction stands; effective 3 September 2026 | D3 | 26 |
| Multi-brand retail: FDI capped at 51 percent, government route; no retail trading by e-commerce for such companies (paragraph 5.2.15.4) | D3 | 27, with 28 as its origin |
| GST: two rates of 5 and 18 percent and a 40 percent rate from 22 September 2025; shampoo and toilet soap moved to 5 percent | D5, D7, C5 | 29 |
| E-invoicing above Rs 5 crore of aggregate turnover from 1 August 2023 | D7 | 30 |
| Tax collected at source by e-commerce operators at 0.5 percent from 10 July 2024 | D7 | 31 |
| A tax invoice carries the supplier's GSTIN, a serial number unique for the financial year, HSN, taxable value, tax rate and amount, place of supply | D7 | 32 |
| Rule 6: maker's name and address, MRP "inclusive of all taxes", consumer-complaint contact | D7 | 33 |
| Rule 18(2): no sale above the retail sale price | D6, D7, D8, T6, C5 | 34 |
| E-commerce entities display the declarations, except the date of manufacture, from 1 January 2018 | D7 | 35 |
| Unit sale price declared under the 2021 amendment | D7 | 36 |
| E-commerce rules: 48 hours to acknowledge and one month to redress (4(5)); cancellation charges (4(8)); explicit consent and no pre-ticked boxes (4(9)); refunds (4(10)); no price manipulation, no discrimination between consumers of the same class (4(11)); ranking parameters explained (5(3)(f)); country of origin (6(5)(d)) | D7, D8, T6, C5 | 37 |
| Dark patterns guidelines issued 30 November 2023, 13 specified patterns including false urgency, basket sneaking, drip pricing, bait and switch | D7, C5 | 38 |
| DPDP Rules notified 14 November 2025; eighteen-month phased compliance; consent notice naming the purpose; breach notice; verifiable parental consent; penalties up to Rs 250 crore and Rs 200 crore | D7, C5 | 39 |
| Card-on-file: only issuers and networks store actual card data; last four digits and issuer name may be kept for tracking and reconciliation | D7, T6, C5 | 40 |
| The storage deadline extended to 30 September 2022, so tokenisation applied from 1 October 2022 | D7 | 41 |
| PCI DSS v4.0.1 published 11 June 2024; v4.0 retired 31 December 2024; new requirements effective 31 March 2025 | D7, C5 | 42 |
| CCPA rights: know, delete, opt out of sale or sharing including through the global privacy control, correct, limit sensitive personal information | D7, C5 | 43 |
| CPPA rules on automated decision-making technology effective 1 January 2026, with ADMT compliance from 1 January 2027 | D7 | 44 |
| Klarna's assistant: 2.3 million conversations, two-thirds of chats, the work of 700 full-time agents, resolution from 11 minutes to under 2 | D8, D12, T6 | 45 |
| Klarna's chief executive on lower quality from a cost-first approach, and a human always available | D8, D12, T6 | 46 |
| Moffatt v. Air Canada, 2024 BCCRT 149: "it makes no difference whether the information comes from a static page or a chatbot" | D8, T6 | 47 |
| Rufus: a generative-AI shopping assistant trained on Amazon's catalogue and information from across the web, available to all India customers | D8 | 48 |
| Diwali on 20 and 21 October 2025 by state; on 8 November 2026 | D5 | 49, 50, and `facts.yaml` (the Monday after Diwali, 9 November 2026) |
| Think School's video title and channel | D12 | 51 |

## Illustrative and invented numbers

Every number below is illustrative, chosen for easy arithmetic, labelled illustrative where it appears, and neither Kalpa's data nor any real company's. The dossier plants them in section 1 and reuses them.

| Number | What it is | Where |
|---|---|---|
| 1,200 people, 480 bills, Rs 1,250 across 5 items | The store's Saturday | D1, D5, D6, T1 |
| 80,000 sessions, 50,000 visitors, 8,000 carts, 2,000 orders at Rs 1,600 across 4 items | The app's Saturday | D1, D5, C2, T1 |
| Rs 2,000 of goods, Rs 200 discount, Rs 1,800 charged, Rs 200 GST, Rs 1,200 cost, Rs 120, 20, 50 and 60 of variable costs, Rs 150 contribution | The Saturday basket | D1, D3, D5, T1, T3 |
| Rs 100 of GMV: 4 cancelled, 6 returned, 10 GST, 60 cost, 12.5 variable, 5 fixed, leaving 80, 20, 7.5 and 2.5 | The P&L waterfall | D3, C6, T3 |
| 4 percent stock-outs, shrinkage of half a percent of sales, 900 of 1,000 cases | The store manager's morning | D1, D5, D6 |
| 45 days of inventory, Rs 45 lakh against Rs 1 lakh a day, 60 days of supplier credit, 2 days of receivables, minus 13 days | Working capital | D1, D3, D5, D6 |
| 620 of 1,000 festive lights in four weeks | Sell-through | D1, D5, D6 |
| 7 in 100 delivered orders returned; 3,360 of 48,000 | Returns | D1, D5 |
| 40,000 customers, 50,000 orders, 4 items, Rs 450, 10 percent discount, Rs 8.1 crore | The app's month | D1, D5 |
| 1,00,000 customers, 1,50,000 orders, 30,000 repeaters | The quarter | D5, C2 |
| 1,000, 380, 300 and 260 | January's cohort | D5, T5 |
| 80,000 new customers from Rs 12 crore, CAC Rs 1,500, Rs 75 a month, 20 months; CLV Rs 150 x 6 x 2 = Rs 1,800 | Acquisition arithmetic; the Rs 12 crore is the story's, the 80,000 is illustrative | D5, C2 |
| Ten orders of Rs 1,600 and one of Rs 40,000: mean Rs 5,091, median Rs 1,600 | Invented, to show the mean against the median without echoing the Monday file | D5, T5 |
| Staples 10 percent on Rs 90 lakh, fashion 40 percent on Rs 10 lakh: 25 against 13 percent | Averaging margin percentages | D5 |
| 100 stores, Rs 500 crore to Rs 510 crore, 20 new stores adding Rs 65 crore | Like-for-like | D5, C2, T5 |
| 50 stores x 5,000 products x 730 days, about 18 crore rows | Forecast sizing | D9 |
| 1.2 x 5/6 = 1 | A flat total hiding two branches | D5 |
| The Saturday basket's operating profit of about Rs 45 | 2.5 percent of Rs 1,800, for the talk track's show of hands | T3 |

## Not verified, or verified only through a secondary source

- The length of Think School's video: YouTube returned a rate-limit page, so the dossier says "Length not verified".
- Flipkart's Big Billion Days is named from Flipkart's own sale page title in search results; the page itself returned 529 to the page reader. No date for it is stated.
- Press Note 3 of 2026 was read through EY India's alert (26); DPIIT's press-note page is script-rendered and returned no text.
- Rule 46's particulars come from TaxGuru (32) and the TCS rate from TaxGuru's report of the notification (31), since the CBIC tax information portal and consumeraffairs.nic.in closed the connection through this session's proxy; so did the Legal Metrology rule PDFs on state government sites.
- The Consumer Protection (E-Commerce) Rules were read from IBC Laws' copy of the notification (37). Rule 4(5)'s wording was confirmed in a second read.
- The Air Canada decision was read through McCarthy Tétrault's summary (47); CanLII refused the page reader. The decision's date is given only as 2024.
- The Walmart+ price is from NBC Select (19), because walmart.com served a robot check.
- Trent's store counts are from Business Standard (10), and Blinkit's from MediaNama (13), both reporting the companies' own results.
- That PCI DSS v4.0.1 is still the current version on 30 September 2026 rests on the Council's June 2024 post (42) and a search that found no newer published version, only a request for comments opened in June 2026.
- The DPDP phase-in dates rest on the PIB explainer (39). A January 2026 proposal to shorten the timeline for significant data fiduciaries was reported by law firms; whether it was notified was not verified, so no file states a changed date.

## Decisions and open points for the orchestrating session

1. **Kalpa Health's repositioning.** Settled on `main` after this branch was cut: client zero section 1c and addendum `health-us-facing`. The dossier's wording follows section 1c. This branch does not carry those files, so they arrive with the merge.
2. **A question the story leaves open.** A Singapore-headquartered group owning an Indian store chain that sells its own stock through an app would, in the real world, meet the FDI limits in section 3. The dossier names the rule and the question and says the story does not settle it. If the requester wants it settled, the likely lines are an Indian-owned Kalpa Retail India or a marketplace app; either would be a client-zero decision.
3. **The 45-minute domain story.** Settled on `main`: the spine now says Week 1 Monday's domain story takes 45 minutes in place of the 20-minute ask, and the domain-dossier reference says the morning deck's first chapter carries it. The talk track ends on Meera's ask, so the day's first chapter can open on it.
4. **The sheet builder.** `scripts/build_cheatsheet.py` read the foot strip's glossary from whichever notes file the filesystem listed first, and with the dossier added it would have printed retail terms on the Monday revenue-tree sheet's next rebuild. It now prefers the notes whose topic shares a word with the sheet's name, and otherwise the day's own `_notes_` file (commit on this branch). The revenue-tree PDF was not rebuilt.
5. **Length.** After two compression passes the dossier runs to about 8,560 words without its URLs and dated citations (about 8,800 by a plain count, diagram source excluded), against the brief's 6,000 to 8,000. Its twelve sections carry 29 tables. Section word counts are in the session report.
6. **The depth loop.** `CLAUDE.md` on `main` now asks every pack for a rigor pass and a pedagogy-and-language pass by fresh reviewer agents. This session had no tool to start another agent, so those two reviews were not run on these files; the orchestrating session can run them.

## The plant check

The dossier and card are STUDENT files read on Week 1 Monday, before the room has found anything, so neither names a plant. Checked against `docs/07_Client_Zero.md` section 7, the Week 1 and Week 2 rows, and the spine:

- No Kalpa dataset value appears: not the Monday file's largest order or its text amount, the export's duplicates, the Student segment's order count, the monsoon sale's result, the double-posted or unpaid payments, the ties at the fiftieth rank, the exposure table's duplicate keys, the Week 4 basket figures or the Week 5 leak.
- The generic traps use invented numbers that differ from the staged ones: a Rs 40,000 office order among Rs 1,600 orders, a cohort of 1,000, 100 stores. The revenue tree's trap is a flat total hiding two branches, chosen so it does not rehearse Monday's added-lifts trap.
- The Q1 and Q2 revenue figures of the Tuesday and Wednesday scenarios are not used, and nothing says which branch, tier or segment moved.
- The talk track names what must not be previewed only as a warning to the trainer, without values.

## Tools

Python 3 for extraction and word counts; pdftotext for the PDFs; mermaid-cli 11.17.0 and weasyprint 70.0 through `scripts/build_cheatsheet.py`, run as `python3 scripts/build_cheatsheet.py content/W01/D1/cheatsheets/C2_W01_D01_retail_domain_card_STUDENT.md --verified "30 Sep 2026" --max-pages 1`, which chose three columns and its tight layout and reported one page; the llm-tic-scrubber scanner on every markdown file.

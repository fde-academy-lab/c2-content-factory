# Sources: the financial services dossier, its card and the domain story

**INTERNAL.** Every source behind `3_study_material_for_students/C2_W05_D02_domain_financial_services_STUDENT.md` (the dossier) and its PDF, `3_study_material_for_students/C2_W05_D02_financial_services_card_STUDENT.md` (the card) and its PDF, and `4_trainer_only/C2_W05_D02_domain_story_TRAINER.md` (the talk track), with the date each was checked, how it was reached, a line per fact, the decisions taken in the build session and what could not be verified.

---

## What were the files built from inside the repository?

| Source in the repository | What it supplied |
|---|---|
| `docs/detailing/W05_briefs/W05_D2_domain_brief.md` | The four files, the lean dossier of about 3,500 words, the three visuals, the card's contents, the 15-minute story told before Tuesday's transfer chapter, the rules |
| `docs/detailing/W05_briefs/W05_D2_brief.md` | The slot just before chapter 6, *Same model, opposite threshold*; Rohan's threshold worked by hand in chapter 6, which the story must leave alone |
| `CLAUDE.md` and `docs/11_Artifact_Set_W05.md` | The Week 5 folders and names, the writing rules, the plant rule, durations only, role labels, the diagram rule |
| `.claude/skills/day-pack-builder/references/domain-dossier.md` | The twelve sections, the card and the talk track's shape, the truth rule |
| `content/W01/D1/study-notes/C2_W01_D01_domain_retail_STUDENT.md` and its card, talk track and sources | The house form, the mermaid palette, the likeness wording, the retail dossier's line that Kalpa Financial is like PhonePe in payments and Tata Capital in lending |
| `docs/07_Client_Zero.md`, v2.2 locked 13 September 2026 | Kalpa Group, its five units and its Bengaluru GCC; Rohan Desai, head of risk, entering in Week 5 with the cost asymmetry; the Build 2 seeds |
| `docs/curriculum/W5_ML_core_ME1.md`, Tuesday and Friday rows | Rohan's costs (Rs 60,000 for approving a defaulter, Rs 3,000 of lost interest for rejecting a good borrower); the transfer subtopic; Friday's question on the feature that would leak in lending, which no file answers |
| `docs/curriculum/W6_Build_2.md` | Kalpa Financial runs a payments app and a consumer lending book across India; the five Build 2 sub-problems; the data Rohan holds; the planted details the files must not name |
| `docs/detailing/W05_ml_core_plan.md` and `docs/detailing/W05_research/W05_cases.md` | The week's thread into lending; the PhonePe and Razorpay cases, re-fetched in this session |
| `data/programme/facts.yaml`, decision `four-domains` | Financial services enters in Week 5 and carries Build 2 |

## Which Kalpa facts do the files state, and where does each come from?

| Kalpa fact as the files state it | Where it comes from |
|---|---|
| Kalpa Group, Kalpa Financial Services and Rohan Desai are fictional | `docs/07_Client_Zero.md`, section 1 |
| Kalpa Financial runs a payments app and a consumer lending book across India | `docs/curriculum/W6_Build_2.md`, Tuesday row |
| Rohan Desai is head of risk at Kalpa Financial | `docs/07_Client_Zero.md`, section 1a |
| Approving a defaulter costs Rs 60,000; rejecting a good borrower costs Rs 3,000 of lost interest | Week 5 Tuesday row, business scenario |
| Rohan hears about Retail's model and asks whether the same machinery could score loan applicants | Week 5 Tuesday row, business scenario |
| Fraud is about half a percent of payments | `docs/curriculum/W6_Build_2.md`, sub-problem 2, which learners receive in Rohan's brief |
| Collections works with a fixed team | `docs/curriculum/W6_Build_2.md`, sub-problem 3 |
| Kavya Nair checks the data team's numbers | `docs/07_Client_Zero.md`, section 1a |
| The GCC in Bengaluru serves all five units | `docs/07_Client_Zero.md`, section 1 |
| Kalpa Financial's licence | Not in the lock; the files say the story does not say |

## Which external sources were read, and when?

Every source was read on 28 October 2026 in this session. WebFetch is the session's page reader; curl means the file was downloaded and read as text.

| # | Source | URL | Checked | How |
|---|---|---|---|---|
| 1 | RBI, Non-Banking Financial Companies (Credit Facilities) Directions, 2025, RBI/DOR/2025-26/347, 28 November 2025, updated as on 15 July 2026 | https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12957 | checked 28 October 2026 | WebFetch, chapter III read |
| 2 | RBI, Digital Lending Directions, 2025, RBI/2025-26/36, 8 May 2025 | https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12848 | checked 28 October 2026 | WebFetch, twice; no repeal note on the page |
| 3 | RBI, Non-Banking Financial Companies (Responsible Business Conduct) Directions, 2025, RBI/DOR/2025-26/362, 28 November 2025, updated as on 1 July 2026 | https://rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12942 | checked 28 October 2026 | WebFetch |
| 4 | RBI, Non-Banking Financial Companies (Income Recognition, Asset Classification and Provisioning) Directions, 2025, RBI/DOR/2025-26/356, 28 November 2025, updated as on 1 October 2026 | https://www.rbi.org.in/scripts/BS_ViewMasDirections.aspx?id=12948 | checked 28 October 2026 | WebFetch |
| 5 | RBI, Non-Banking Financial Companies (Know Your Customer) Directions, 2025, RBI/DOR/2025-26/361, 28 November 2025, updated as on 29 December 2025 | https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12943 | checked 28 October 2026 | WebFetch, first 100,000 characters |
| 6 | RBI press release, "RBI issues Amendment Directions to amend Credit Information Reporting Directions, 2025", 4 December 2025 | https://rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=61742 | checked 28 October 2026 | WebFetch |
| 7 | RBI, list of credit information companies, as on 18 August 2026 | https://www.rbi.org.in/scripts/bs_viewcontent.aspx?Id=4921 | checked 28 October 2026 | WebFetch |
| 8 | Vinod Kothari Consultants, table of RBI's consolidated NBFC directions, December 2025 | https://vinodkothari.com/wp-content/uploads/2025/12/RBI-Consolidation-of-Circulars-NBFCs-Final-1-1-1.pdf | checked 28 October 2026 | PDF saved and read with pdftotext |
| 9 | PIB, "DPDP Rules, 2025 Notified", 17 November 2025 | https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf | checked 28 October 2026 | PDF saved and read with pdftotext |
| 10 | Department of Financial Services, account aggregator framework page | https://financialservices.gov.in/account-aggregator-framework | checked 28 October 2026 | WebFetch |
| 11 | PhonePe, secured-loans page, disclaimer | https://www.phonepe.com/secured-loans/ | checked 28 October 2026 | curl, 200, disclaimer text extracted |
| 12 | Outlook Business, "PhonePe, Google Pay combined UPI market share drops below 80% for first time", 17 June 2026 | https://www.outlookbusiness.com/economy-and-policy/phonepe-google-pay-combined-upi-market-share-drops-below-80-for-first-time | checked 28 October 2026 | WebFetch |
| 13 | FinTech BizNews, "UPI TXN Volume & Value Fell In Sept '26", 1 October 2026 | https://fintechbiznews.com/fintech-digital-payment-/upi-txn-volume-value-fell-in-sept26-aeps-imps-volume-too-down | checked 28 October 2026 | WebFetch |
| 14 | Kotak Neo, "Bajaj Finance Q2 FY27 Results", 19 October 2026 | https://www.kotakneo.com/news/stocks/bajaj-finance-share-price-and-q2-fy-27-results/ | checked 28 October 2026 | WebFetch |
| 15 | Tata Capital, Q1 FY27 results media conference call transcript, 28 July 2026 | https://www.tatacapital.com/hindi/content/dam/tata-capital/pdf/investors-and-financial-reports/financials/tcl/media-conference-call-transcript-q1-fy-27-v2.pdf | checked 28 October 2026 | curl, 200, read with pdftotext |
| 16 | JPMorganChase, "At work in India" | https://jpmorganchase.com/communities/india | checked 28 October 2026 | WebFetch |
| 17 | PhonePe engineering, "Building PhonePe's Real-Time Transaction Model to prevent Frauds: A Journey", Nipun VK, 28 July 2022 | https://tech.phonepe.com/building-phonepes-real-time-transaction-model-to-prevent-frauds-a-journey/ | checked 28 October 2026 | WebFetch |
| 18 | Razorpay, "Vulcan: how Razorpay built a foundation model for payment decisions", 10 September 2026 | https://razorpay.com/blog/vulcan-how-razorpay-built-a-foundation-model-for-payment-decisions | checked 28 October 2026 | WebFetch |

## Where does each real fact in the files come from?

| Fact as the files state it | Files | Source |
|---|---|---|
| PhonePe is "a platform facilitating loan transactions between borrowers and RBI-registered NBFCs or Banks" and "does not lend directly" | Dossier s2, talk track part 2 | 11 |
| PhonePe and Google Pay together carried 79 percent of UPI transactions in May 2026, from NPCI data | Dossier s2 | 12 |
| UPI carried 2,407 crore transactions worth Rs 29.37 lakh crore in September 2026, from NPCI data | Dossier s2, talk track | 13 |
| Bajaj Finance, quarter to 30 September 2026: 13.45 million new loans, AUM Rs 5,84,624 crore, gross NPA 1.06 percent, net NPA 0.42 percent | Dossier s2, talk track part 2 | 14 |
| Tata Capital, quarter to 30 June 2026: AUM Rs 2.91 lakh crore, credit costs 1 percent, cost of funds 7.28 percent, consolidated ROA 2.3 percent, about 8.8 million customers | Dossier s2 and s3, talk track parts 2 and 3 | 15 |
| Four CICs: CRIF, Equifax, Experian, TransUnion CIBIL, as on 18 August 2026 | Dossier s2 and s7, card, talk track | 7 |
| JPMorganChase's corporate centres in Mumbai, Bengaluru and Hyderabad support its technology and business operations globally | Dossier s2 | 16 |
| KFS with APR before signing (para 9(1)); cooling-off at least one day (para 11(1)); age, occupation and income before lending (para 8(1)); need-based data with prior explicit consent and an audit trail, no files, media, contacts, call logs or telephony, one-time camera, microphone or location for KYC (para 13(1)); data only on servers in India (para 14(4)); disbursal and repayment only between the borrower's and the NBFC's accounts (paras 10(1) and 10(2)); DLG within 5 percent of the amount disbursed (para 24(1)); every digital loan reported to CICs (para 17(1)); escalation to RBI's complaint portal after 30 days without reply (para 12(4)); unbiased multi-lender view (para 7) | Dossier s1, s7, s9, s10; card; talk track part 5 | 1, and the same paragraphs in 2 |
| For NBFCs, the Credit Facilities Directions consolidate the Digital Lending Directions, 2025 | Dossier s7 | 8, cross-read against 1 and 2 |
| Every application acknowledged (para 12); communications and sanction terms in the vernacular or a language the borrower understands (paras 10 and 13); KFS in a language the borrower understands (para 29(1)); changes to rates and charges only prospectively, after notice (para 15); no undue harassment in recovery (para 20); NBFC or its agents call only inside the window para 100 fixes, with a narrower window for microfinance in para 91(2); penal charges not capitalised (para 30(1)) | Dossier s7, card, talk track part 5 | 3 |
| NPA when overdue more than 90 days (para 51(1), and para 44's glide path for base-layer NBFCs, completed by 31 March 2026); SMA-1 after 30 days and SMA-2 at about 60 (illustration I, para 19); upgrade only when all arrears are paid (para 24) | Dossier s5, s6, s7; card; talk track part 4 | 4 |
| Due diligence before any account-based relationship (paras 17(3), 21(1)); V-CIP on par with face to face (paras 26, 27); KYC refresh every two, eight or ten years by risk (para 42(1)); records kept at least five years after the relationship ends (para 47) | Dossier s7, card | 5 |
| Credit information reported fortnightly or more often, with RBI moving to weekly incremental reporting | Dossier s7, card | 6 |
| DPDP Rules notified 14 November 2025; Act enacted 11 August 2023; 18-month phased compliance; purpose-specific consent notice, withdrawable consent; requests answered within 90 days; breach notice to affected people without delay; penalties up to Rs 250 crore (security safeguards), Rs 200 crore (breach notice, children), Rs 50 crore (other) | Dossier s7, card, talk track part 5 | 9 |
| Account aggregators are NBFCs retrieving financial information, moved only with the customer's explicit consent to regulated users | Dossier s6, s9 | 10 |
| PhonePe's fraud system was designed "at very high precision"; operations reviewed samples and called senders; fraud rate on consumer-to-consumer transactions down 40 percent | Dossier s8 | 17 |
| Fraud may be confirmed only when a dispute appears weeks later and some is never reported; models are compared at the same alert volume | Dossier s5, s9 | 18 |

## Which numbers are illustrative, and whose construction are they?

Every number below is this build's own round number, labelled illustrative in the files: the rider's Rs 50,000 loan, 1,000 applications and 400 approvals; the Rs 100 journey (yield 16, cost of funds 8, fees 1, operating cost 4, credit cost 2, profit before tax 3, about 2.2 after tax); every worked number in the dossier's metric table; and the "about 8" and "about 16" on the board drawing. The DPD bands of 1 to 30, 31 to 60, 61 to 90 and over 90 are the usual industry bands, stated as a definition. The metric formulas for approval rate, bounce rate, collection efficiency, roll rate, default rate by vintage, cost of risk and net interest margin are standard definitions written for the course; collection efficiency carries its own caveat because lenders define it differently.

## Which decisions did the build take, with nobody to ask?

1. **Length.** The dossier runs to about 4,300 words: about 2,000 of prose and 2,300 inside its nine tables, against the brief's "about 3,500". The tables carry the card's metrics, terms and rules and each of the twelve sections' content; cutting them further would have dropped a section's substance, so the cut was made in prose and in duplicated rows (early warning, four terms) instead.
2. **Which digital lending instrument to cite.** The 8 May 2025 Digital Lending Directions page carried no repeal note, while the consolidated NBFC Credit Facilities Directions of 28 November 2025 carry the same provisions in chapter III and a law firm's consolidation table maps the one into the other for NBFCs. The files cite chapter III of the Credit Facilities Directions and name the May 2025 directions it carries.
3. **Kalpa Financial's licence.** The lock does not say, so the files use an NBFC lender's rules as the likeness and say so.
4. **Rohan's threshold.** No file divides Rs 60,000 by Rs 3,000 or says which way the threshold moves; the dossier and the talk track show only which line of the P&L each cost lands on and hand over to chapter 6.
5. **Build 2's plants.** No file names the application column written after the decision or says whether the campaign's lift is cause or mix; the campaign is left out, and the leakage problem is left to Wednesday and Friday.
6. **The card's "metric tree" and "one picture".** Read as one drawing, the tree rooted at return on assets, whose branches are the money flow's lines (margin, fees, operating cost, cost of risk), because one A4 page holds one picture legibly.
7. **The recovery calling window.** The files say "a daytime window the directions fix" without the hours, to keep lesson files to durations; para 100 of source 3 holds the hours.
8. **A voice bot and the recovery rules.** Para 100 binds the NBFC "or its agents"; the files read that as covering a voice bot calling for the lender, worded as the lender's duty.
9. **US rules.** Left out: Kalpa Financial lends in India, and no US lending rule was verified in this session.
10. **Fitting the card on one page.** The card carries a print style inside an HTML comment, which WeasyPrint applies and GitHub does not show, so `scripts/build_doc.py` stays untouched.
11. **Printing.** `scripts/build_cheatsheet.py` looks for Chromium under `chrome-linux/`, and this session's browser sits under `chrome-linux64/`, so both PDFs were printed with `PUPPETEER_EXECUTABLE_PATH=/opt/pw-browsers/chromium`. The script is outside this build's four files and was not changed.
12. **Diagram sizes.** The dossier's money flow was redrawn three times until it printed beside its section with labels near 14 points; the dossier's tree prints near 10 points and the card's near 7, against the five-point floor.

## What could not be verified, and what was left out?

| Item | What happened | What the files do |
|---|---|---|
| NPCI's own UPI statistics page | curl returned 403 and WebFetch returned only the page title | UPI totals come from FinTech BizNews and the market share from Outlook Business, each quoting NPCI |
| PhonePe's own UPI share | Only the PhonePe and Google Pay combined 79 percent was confirmed from a fetched page | The files give the combined figure only |
| PhonePe user and merchant counts | Not on its about page | Left out |
| Bajaj Finance's own results release | The investor page URL returned 404 | Figures from Kotak Neo's report of the results, labelled as such |
| Tata Capital's quarter to September 2026 | Not found | The quarter to June 2026, from its own call |
| RBI documents on rbidocs.rbi.org.in | Served a human-verification page | The same directions read on rbi.org.in instead |
| The date weekly CIC reporting starts | The press release does not give it | The files say RBI "moved towards" weekly reporting |
| Any change to the DPDP timeline after 17 November 2025 | Not checked beyond the PIB explainer | The files say most duties apply 18 months after notification |
| A requirement to give written reasons for rejecting a loan | Not found in the fair practices section of source 3 | Left out |
| JPMorganChase's India headcount | Not on its India page | Left out |
| How Rohan's Rs 60,000 and Rs 3,000 are built | Not in the lock | Not explained; the files show only where each lands |

## Which checks ran on the files?

| Check | Result |
|---|---|
| `.claude/skills/llm-tic-scrubber/scripts/tic_scan.py` on the three prose files | Clean on each |
| The humanizer's read, file mode, prose only | Done in the build: a staged opener, two slogan lines in the talk track, one overstated claim about PhonePe's aim and the gendered pronouns for the fictional rider were rewritten |
| `scripts/build_doc.py` on the two STUDENT files | The dossier prints to 13 A4 pages, the card to one |
| `python3 scripts/verify.py content/W05/D2` | PASS, 0 failures and no warnings, on the six files of this build before the last push |

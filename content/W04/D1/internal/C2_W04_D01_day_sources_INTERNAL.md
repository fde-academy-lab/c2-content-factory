# Where does every Monday fact come from, and what departs from a source?

**INTERNAL.** One page: the public facts with their check dates, the data, the case-file sharpenings,
what was left out, and the cold-read findings that carry a reason in place of a fix.

## Which public facts does the pack use, and when was each checked?

Every URL below was fetched on 12 October 2026; the ids are the case file's.

| Id | Fact, as used | URL |
|---|---|---|
| M8 | CFPB: USD 100 million, with the OCC's USD 35 million and Los Angeles's USD 50 million, USD 185 million in all, 8 September 2016 | https://www.consumerfinance.gov/about-us/newsroom/consumer-financial-protection-bureau-fines-wells-fargo-100-million-widespread-illegal-practice-secretly-opening-unauthorized-accounts/ (checked 12 October 2026) |
| M8 | SEC: USD 3 billion settlement with the DOJ and the SEC, USD 500 million of it the SEC's penalty, February 2020 | https://www.sec.gov/newsroom/press-releases/2020-38 (checked 12 October 2026) |
| M8 | SEC order 34-88257: no usage condition; debit cards counted up to four years unused; the 2013 remittance addition (0.04 of 0.11); simulated funding; surveys dodged | https://www.sec.gov/files/litigation/admin/2020/34-88257.pdf (checked 12 October 2026) |
| M8 | VA OIG 14-02603-267: 30 of 79 Phoenix staff used a wrong desired date; the 14-day goal left performance contracts | https://www.vaoig.gov/sites/default/files/reports/2014-08/VAOIG-14-02603-267.pdf (checked 12 October 2026) |
| M1 | Swiggy Q2 FY25 letter: MTU and platform frequency defined; frequency 4.53, MTU 17.1 million | https://www.bseindia.com/xml-data/corpfiling/AttachHis/2495f39b-e1d1-4018-8f69-6ff250345e98.pdf (checked 12 October 2026) |
| M9 | Swiggy Q1 FY26 letter: Maxxsaver over 28 percent of MTUs; AOV up 16 percent to Rs 612; cart consolidation lowered order growth | https://www.swiggy.com/corporate/wp-content/uploads/2025/07/Q1-FY2026-Shareholder-letter.pdf (checked 12 October 2026) |
| M2 | Eternal Q1 FY26 letter: NOV = GOV minus discounts | https://drive.google.com/file/d/1VtoiLsA2OpKauFnkKIlhXRmnbvxL-6ha/view (checked 12 October 2026) |
| M2 | Eternal Q1 FY27 letter: GOV disclosure sunset, "NOV more accurately reflects underlying performance"; linked from the blog page | https://drive.google.com/file/d/1jb9KWd4Ap4RTKHFHxzEOO7jgQqVZEGcd/view ; https://www.eternal.com/blog/q1fy27/ (checked 12 October 2026) |
| M6 | Delhi Metro: 45,35,932 line utilisation on 29 May 2018 against about 27 lakh riders; 64.06 lakh journeys; 82,44,903 boardings on 17 September 2026 | https://www.latestly.com/agency-news/dmrc-uses-new-count-metric-on-traffic-flow-doesnt-share-ridership-190870.html/amp ; https://www.tribuneindia.com/news/delhi/delhi-metro-records-99-95-train-punctuality-in-2026-dmrc/ ; https://www.republicworld.com/india/delhi-metro-breaks-all-time-record-with-8244-lakh-footfall-as-dtc-strike-sends-rush-soaring-2026-09-18-137241 (checked 12 October 2026) |
| M5 | Uber 10-K for 2025: a trip counted per paying consumer (an UberX Share ride with three paying riders is three trips); monthly active platform consumers need a completed ride or delivery | https://www.sec.gov/Archives/edgar/data/1543151/000154315126000015/uber-20251231.htm (checked 12 October 2026) |
| M4 | Airbnb S-1: nights booked net of cancellations, minus 4.1 million in March 2020 | https://www.sec.gov/Archives/edgar/data/1559720/000119312520294801/d81668ds1.htm (checked 12 October 2026) |
| M5 | Spotify 20-F for 2025: an MAU has more than zero milliseconds of consumption in thirty days | https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm (checked 12 October 2026) |
| T2 | Aced: interviewers score structure, assumptions and scope before the method | https://www.aced.io/blog/top-data-analyst-interview-questions (checked 12 October 2026) |

Not used, because unverified: Wells Fargo firing counts, the "3.5 million accounts" figure, Goodhart's
wording, the NHS examples.

## Where does the data come from?

`python3 content/W04/D1/internal/C2_W04_D01_generate_INTERNAL.py`, seed 20261026, writes the five
CSVs, the contract and the facts file; a second run is byte-identical. Tools: Python 3.13.16, pandas
3.0.5, matplotlib 3.11.2, numpy 2.5.3, nbclient 0.11.0, python-pptx 1.0.2, mermaid-cli 11.17.0,
weasyprint 70.0, LibreOffice 24.2.7.2.

## What does the pack sharpen from the case file?

- The guarantee's window drops "weekday": with weekday windows only, the idle tail's top-up per
  driver-week would exceed the floor's own maximum.
- `driver_weeks` counts `peak_offers` (every showing of a request) and gains `peak_hours_no_trip`;
  the ticket's row reads "offers accepted over offers shown", since a declined request is offered
  again, which is why `zone_weeks` requests and `driver_weeks` offers differ.
- The twelve rows keep the draft's 114 to 88 trips and 1.90 to 1.19 (the case file had 110 and
  1.49), on the orchestrator's instruction, with the reason said on the slide.
- The Kalpa tables are held byte-identical to the draft: `RP-` member ids, booked value from
  `app_reorders`, no manual reorders in the window, and no warehouse SQL file.
- The cheat sheet's ticket sits in its top band and the concept board in panel one, since the spine
  asks for both in first position.

## Which cold-read findings carry a reason in place of a fix?

Filled after the two cold reads.

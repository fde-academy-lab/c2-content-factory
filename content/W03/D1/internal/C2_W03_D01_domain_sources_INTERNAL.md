# Sources: the US healthcare domain dossier, the domain card and the domain story

**INTERNAL.** Every source behind `study-notes/C2_W03_D01_domain_us_healthcare_STUDENT.md` (the dossier), `cheatsheets/C2_W03_D01_us_healthcare_domain_card_STUDENT.md` and its PDF (the card), and `trainer/C2_W03_D01_domain_story_TRAINER.md` (the talk track), with the date each was checked, how it was reached, and a line per fact on where it came from. The files were built on 30 September 2026 and raised to standard v3 the same day, after the merge of `origin/main`.

---

## What the files are built from

| Source in the repository or the session | What it supplied |
|---|---|
| The requester's brief of 30 September 2026, relayed by the orchestrating session, and the orchestrating session's review of the same day | The four deliverables, the rule that no file teaches Build 1's answers or traps, the five review points (Kalpa Health against the data, no plant, exact compliance, ten company facts re-checked, length), standard v3, the humanizer read and the one-page card |
| `CLAUDE.md` | The truth order, the writing rules, the plant rule, the diagram rule, durations only, role labels |
| `.claude/skills/day-pack-builder/references/the-standard.md`, standard v3 from pull request 195 | The question ladder: every heading a question, **Who needs the answer.** and **The questions on the way.** under each section, the section closing on its answer; the self-contained rule; the humanizer read |
| `.claude/skills/day-pack-builder/references/domain-dossier.md` | The twelve section questions, the four files, the diagram set, 6,000 to 8,000 words, and the proof |
| `.claude/skills/humanizer/SKILL.md` | The file-mode read of all four files |
| `docs/07_Client_Zero.md`, v2.2 locked 13 September 2026, with the addenda of 28 and 30 September 2026 | Section 1c: Kalpa Health serves the US, six metros, four payer kinds, dollars, seven denial categories, calendar Q2 and Q3 of 2026, synthetic records; Dr Menon, Kavya Nair and the data platform lead |
| `data/programme/facts.yaml`, decisions `four-domains`, `health-us-facing` and `build1-us-data` | US healthcare enters on Build 1 Monday with its dossier, card and talk track; Build 1's data in the US setting |
| `docs/detailing/W03_build1_spine.md`, rewritten by pull request 202 | The five sub-problems, the plant table and its numbers, read so that no file names, previews or teaches any of them |
| The Build 1 briefing note, the Wednesday checkpoint questions, the Wednesday parallel build's run sheet and the Saturday panel's question bank | The heads Dr Menon names by role, and every trap the week stages, read for the plant check |
| The Build 1 data pack in `content/W03/D1/data/` (source 84) | The six metros with a laboratory and two patient service centres each, the four payer kinds and six state Medicaid ids, the seven denial categories, the service dates, the list prices of James's two tests and his plan's terms |
| `docs/curriculum/W3_Build_1.md`, the Monday row | The interview angle's two questions, carried as items 1 and 5 of section 11 with their tags |
| `docs/05_Curriculum_Map_Schema.md` | The interview tags and the rule that the tagging is labelled as the programme's own calibration |
| The retail dossier, card, talk track and sources file in `content/W01/D1/` on main (pull request 194) | The house form of all four files and the mermaid palette |

## Kalpa facts, and where each comes from

| Kalpa fact as the files state it | Where it comes from |
|---|---|
| Kalpa Health is a diagnostics and revenue-cycle business serving the US market; its laboratories and patient service centres test US patients and bill US payers | Client zero section 1c; addendum `health-us-facing` |
| Its analytics and revenue-cycle work runs from Kalpa's GCC in Bengaluru | Client zero section 1c |
| Six US metro areas: Dallas, Phoenix, New York, Chicago, Atlanta and Philadelphia | Client zero section 1c; decision `build1-us-data` |
| A laboratory and two patient service centres in each metro | The data pack's `sites` file (one laboratory and two patient service centers per metro) and the Build 1 briefing note, which says the same |
| Four kinds of payer: commercial plans, Medicare, Medicaid and self-pay | Client zero section 1c; decision `build1-us-data`; the claims file's `payer_type` |
| Medicaid in the six metros' states: Texas, Arizona, New York, Illinois, Georgia and Pennsylvania | The metros' states, and the claims file's `payer_id` values `MEDICAID-TX`, `-AZ`, `-NY`, `-IL`, `-GA` and `-PA` |
| Claims and remittances in dollars; seven denial categories modelled on the X12 claim adjustment reason codes, named as the claims file names them | Client zero section 1c; decision `build1-us-data`; the claims file's `denial_category` |
| Calendar Q2 (April to June) and Q3 (July to September) of 2026 | Client zero section 1c; decision `build1-us-data`; the claims file's service dates run from 1 April to 30 September 2026 |
| Dr Menon's page: test volumes grew 5 percent from Q2 to Q3 against a plan of 18, and she asks which branch is short | Client zero's Build 1 seeds; the spine's week paragraph; the briefing note. The files state it as her dashboard's reading, with no word on how it is counted |
| James's list prices: the HbA1c at $60 and the cholesterol panel at $75, $135 in all | The data pack's `test_catalogue` (`T-HBA` 60, `T-LIP` 75) |
| James's plan: $70.20 allowed on $135, $64.80 adjusted under group CO, $56.16 paid and $14.04 of 20 percent coinsurance | The remittances file's commercial postings on $135 claims, which carry exactly these amounts; the CARC numbers 45 and 2 are the real 835 codes for a contractual reduction and coinsurance, which the posting system keys in its own words |
| A few weeks from claim to remittance | The remittances file's payer postings, which arrive 14 to 45 days after the service date |
| Dr Priya Menon is the COO; Kavya Nair is the trainees' senior; the data platform lead owns the warehouse | Client zero sections 1a, 1b and 1c |
| The finance head, the patient service centres' operations head and the marketing head, unnamed | The Build 1 briefing note, which names them by role |
| Kalpa Group is headquartered in Singapore | Client zero section 1 |

Every other number about Kalpa Health's business is absent from the files: no count of tests, bookings, claims, visits or denials, no allowed share for any payer but James's plan, no cost, no turnaround and no daily volume. The illustrative lab of sections 3, 5, 8 and 9 is labelled made-up wherever it appears.

## External sources, checked on 30 September 2026

Every source below was opened on 30 September 2026. "WebFetch" is the session's page reader; "curl" means the page or file was downloaded and read as text because the page reader was refused (hhs.gov and sec.gov) or redirected (ecfr.gov, read through its official API); "Wayback" means a Wayback Machine capture was read because the site refused both readers that day. Sources marked "not cited now" were checked and are no longer cited in the files.

| # | Source | URL | Checked | How |
|---|---|---|---|---|
| 1 | Quest Diagnostics, Form 10-K for 2025, filed 26 February 2026 | https://www.sec.gov/Archives/edgar/data/1022079/000102207926000015/dgx-20251231.htm | checked 30 Sep 2026 | curl with a declared user agent, text searched |
| 2 | Quest Diagnostics, 8-K exhibit 99.1, results for the quarter to 30 June 2026, 23 July 2026 | https://www.sec.gov/Archives/edgar/data/1022079/000102207926000067/dgx063020268-kex991.htm | checked 30 Sep 2026 | curl; not cited now |
| 3 | Labcorp Holdings, Form 10-K for 2025, filed 24 February 2026 | https://www.sec.gov/Archives/edgar/data/920148/000092014826000111/lh-20251231.htm | checked 30 Sep 2026 | curl with a declared user agent |
| 4 | Quest newsroom, launch of mobile phlebotomy, 9 November 2023 | https://newsroom.questdiagnostics.com/2023-11-09-Quest-Diagnostics-Launches-Mobile-Phlebotomy-Service,-Enabling-Convenient-At-Home-Specimen-Collection-in-the-United-States | checked 30 Sep 2026 | WebFetch |
| 5 | UnitedHealth Group careers, India | https://www.unitedhealthgroup.com/careers/in/work.html | checked 30 Sep 2026 | WebFetch |
| 6 | Carelon Global Solutions, About us | https://www.carelonglobal.in/about-us | checked 30 Sep 2026 | WebFetch |
| 7 | The Cigna Group careers, Evernorth India | https://jobs.thecignagroup.com/us/en/evernorth-india | checked 30 Sep 2026 | WebFetch; not cited now |
| 8 | AGS Health, company page | https://www.agshealth.com/company/ | checked 30 Sep 2026 | WebFetch |
| 9 | Access Healthcare, locations | https://www.accesshealthcare.com/about/locations | checked 30 Sep 2026 | WebFetch |
| 10 | Omega Healthcare, revenue cycle management | https://www.omegahms.com/solution/revenue-cycle-management/ | checked 30 Sep 2026 | WebFetch; not cited now |
| 11 | EQT, agreement to acquire GeBBS Healthcare Solutions, 9 September 2024 | https://eqtgroup.com/news/eqt-to-acquire-gebbs-healthcare-solutions-a-leading-healthcare-technology-solutions-provider-2024-09-09 | checked 30 Sep 2026 | WebFetch; not cited now |
| 12 | Great Place to Work India, R1 RCM Global | https://www.greatplacetowork.in/great/company/r1-rcm-global-private-limited/ | checked 30 Sep 2026 | WebFetch; not cited now, since r1rcm.com refused both readers |
| 13 | CMS, National Health Expenditure fact sheet, modified 24 June 2026 | https://www.cms.gov/data-research/statistics-trends-and-reports/national-health-expenditure-data/nhe-fact-sheet | checked 30 Sep 2026 | WebFetch |
| 14 | US Census Bureau, press release on income, poverty and health insurance coverage, 15 September 2026 | https://www.census.gov/newsroom/press-releases/2026/income-poverty-health-insurance-coverage.html | checked 30 Sep 2026 | WebFetch |
| 15 | KFF, "Medicare Advantage in 2026: Enrollment Update and Key Trends", 5 June 2026 | https://www.kff.org/medicare/medicare-advantage-in-2026-enrollment-update-and-key-trends/ | checked 30 Sep 2026 | WebFetch; not cited now |
| 16 | Medicaid.gov, Medicaid and CHIP enrollment report highlights | https://www.medicaid.gov/medicaid/program-information/medicaid-and-chip-enrollment-data/report-highlights | checked 30 Sep 2026 | WebFetch; not cited now |
| 17 | KFF, "Claims Denials and Appeals in ACA Marketplace Plans in 2024", 24 March 2026 | https://www.kff.org/patient-consumer-protections/claims-denials-and-appeals-in-aca-marketplace-plans-in-2024/ | checked 30 Sep 2026 | WebFetch, and curl for the title |
| 18 | X12, transaction sets | https://x12.org/products/transaction-sets | checked 30 Sep 2026 | WebFetch |
| 19 | X12, claim adjustment reason codes, list dated 1 November 2025 | https://x12.org/codes/claim-adjustment-reason-codes | checked 30 Sep 2026 | WebFetch, and curl for the title; re-read on 30 Sep 2026 by the raising session for 18, 27, 45 and 96, page last reviewed 1 August 2026 |
| 20 | X12, claim adjustment group codes | https://x12.org/codes/claim-adjustment-group-codes | checked 30 Sep 2026 | WebFetch |
| 21 | CMS, Medicare Claims Processing Manual, chapter 22 | https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/downloads/clm104c22.pdf | checked 30 Sep 2026 | curl, PDF read |
| 22 | CMS, HIPAA adopted standards and operating rules, modified 16 March 2026 | https://www.cms.gov/priorities/key-initiatives/burden-reduction/administrative-simplification/hipaa/adopted-standards-operating-rules | checked 30 Sep 2026 | WebFetch |
| 23 | CMS, 5010 basics fact sheet | https://www.cms.gov/medicare/coding/icd10/downloads/w5010BasicsFctSht.pdf | checked 30 Sep 2026 | curl, PDF read |
| 24 | CMS, health care payment and remittance advice | https://www.cms.gov/medicare/coding-billing/electronic-billing/health-care-payment-remittance-advice | checked 30 Sep 2026 | WebFetch |
| 25 | CMS, MLN006976, Medicare billing, CMS-1500 and 837P, December 2025 | https://www.cms.gov/files/document/mln006976-medicare-billing-cms-1500-837p.pdf | checked 30 Sep 2026 | curl, PDF read |
| 26 | CMS, NCCI policy manual for Medicare services, 2026, chapter 10 | https://www.cms.gov/files/document/10-chapter10-ncci-medicare-policy-manual-2026-final.pdf | checked 30 Sep 2026 | curl, PDF read |
| 27 | AMA, "CPT overview and code approval", updated 23 January 2026 | https://www.ama-assn.org/practice-management/cpt/cpt-overview-and-code-approval | checked 30 Sep 2026 | WebFetch |
| 28 | CDC, ICD-10-CM | https://www.cdc.gov/nchs/icd/icd-10-cm/index.html | checked 30 Sep 2026 | WebFetch |
| 29 | CDC, ICD-10-CM files | https://www.cdc.gov/nchs/icd/icd-10-cm/files.html | checked 30 Sep 2026 | WebFetch |
| 30 | CMS, ICD-10 page, modified 8 September 2026, and the 2027 code descriptions file | https://www.cms.gov/medicare/coding-billing/icd-10-codes | checked 30 Sep 2026 | WebFetch; the file at https://www.cms.gov/files/zip/2027-code-descriptions-tabular-order.zip downloaded and searched for E11.9 |
| 31 | CMS, Healthcare Common Procedure Coding System | https://www.cms.gov/medicare/coding-billing/healthcare-common-procedure-system | checked 30 Sep 2026 | WebFetch |
| 32 | CMS, National Provider Identifiers, modified 16 March 2026 | https://www.cms.gov/priorities/key-initiatives/burden-reduction/administrative-simplification/unique-identifiers/npis | checked 30 Sep 2026 | WebFetch |
| 33 | CMS, Clinical Laboratory Fee Schedule, modified 24 September 2026, and the 2026 fourth-quarter file | https://www.cms.gov/medicare/payment/fee-schedules/clinical-laboratory-fee-schedule-clfs | checked 30 Sep 2026 | WebFetch; the file at https://www.cms.gov/files/zip/26clabq4.zip downloaded and read for 85025, 80053, 83036 and 80061; cited now for the fee schedule itself, with no fee printed |
| 34 | Medicare.gov, diagnostic laboratory tests | https://www.medicare.gov/coverage/diagnostic-laboratory-tests | checked 30 Sep 2026 | curl |
| 35 | HFMA, MAP Keys | https://www.hfma.org/data-and-insights/map-initiative/map-keys/ | checked 30 Sep 2026 | WebFetch |
| 36 | HFMA, "Standardizing denial metrics", Claim Integrity Task Force | https://www.hfma.org/guidance/standardizing-denial-metrics-revenue-cycle-benchmarking-process-improvement/ | checked 30 Sep 2026 | WebFetch |
| 37 | HFMA, "Healthcare Revenue Cycle Management (RCM): What It Is and How It Works", updated 25 September 2026 | https://www.hfma.org/reference/revenue-cycle-management/ | checked 30 Sep 2026 | WebFetch |
| 38 | MGMA, cost and revenue glossary | https://www.mgma.com/cost-rev-charges-and-revenue | checked 30 Sep 2026 | WebFetch |
| 39 | AAPC, "Revenue cycle challenges and opportunities", video, 7 minutes 59 seconds | https://www.aapc.com/video/revenue-cycle-challenges-and-opportunities | checked 30 Sep 2026 | WebFetch; the full video needs a free sign-up |
| 40 | HealthCare.gov glossary: allowed amount, deductible, coinsurance, copayment, plan year | https://www.healthcare.gov/glossary/allowed-amount/ | checked 30 Sep 2026 | WebFetch, one page per term under https://www.healthcare.gov/glossary/ |
| 41 | eCFR, 45 CFR 160.103 | https://www.ecfr.gov/current/title-45/section-160.103 | checked 30 Sep 2026 | eCFR API, curl |
| 42 | eCFR, 45 CFR 164.502 | https://www.ecfr.gov/current/title-45/section-164.502 | checked 30 Sep 2026 | eCFR API, curl |
| 43 | eCFR, 45 CFR 164.504 | https://www.ecfr.gov/current/title-45/section-164.504 | checked 30 Sep 2026 | eCFR API, curl |
| 44 | eCFR, 45 CFR 164.514 | https://www.ecfr.gov/current/title-45/section-164.514 | checked 30 Sep 2026 | eCFR API, curl |
| 45 | eCFR, 45 CFR 164.530 | https://www.ecfr.gov/current/title-45/section-164.530 | checked 30 Sep 2026 | eCFR versioner API, curl with compression; not cited now |
| 46 | eCFR, 45 CFR part 164, subparts C and D | https://www.ecfr.gov/current/title-45/part-164/subpart-C | checked 30 Sep 2026 | eCFR API, curl; subpart D at https://www.ecfr.gov/current/title-45/part-164/subpart-D (checked 30 Sep 2026) |
| 47 | eCFR, 45 CFR 102.3, last amended 28 January 2026 | https://www.ecfr.gov/current/title-45/section-102.3 | checked 30 Sep 2026 | eCFR API, curl; not cited now |
| 48 | eCFR, 42 CFR 424.44 | https://www.ecfr.gov/current/title-42/section-424.44 | checked 30 Sep 2026 | eCFR API, curl |
| 49 | HHS, "Summary of the HIPAA Privacy Rule" | https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html | checked 30 Sep 2026 | curl with browser headers |
| 50 | HHS, guidance on de-identification | https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html | checked 30 Sep 2026 | curl with browser headers |
| 51 | HHS, "Direct Liability of Business Associates", last reviewed 16 July 2021 | https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/business-associates/factsheet/index.html | checked 30 Sep 2026 | curl with browser headers; re-read on 30 Sep 2026 through the Wayback capture of 19 September 2026 |
| 52 | HHS, guidance on cloud computing | https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html | checked 30 Sep 2026 | curl with browser headers |
| 53 | HHS, breach notification rule | https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html | checked 30 Sep 2026 | curl with browser headers |
| 54 | HHS, Change Healthcare cybersecurity incident FAQ, last reviewed 13 August 2025 | https://www.hhs.gov/hipaa/for-professionals/special-topics/change-healthcare-cybersecurity-incident-frequently-asked-questions/index.html | checked 30 Sep 2026 | curl with browser headers |
| 55 | Federal Register, the proposed Security Rule, 6 January 2025 | https://www.federalregister.gov/documents/2025/01/06/2024-30983/hipaa-security-rule-to-strengthen-the-cybersecurity-of-electronic-protected-health-information | checked 30 Sep 2026 | Federal Register API; not cited now |
| 56 | reginfo.gov, RIN 0945-AA22 in the regulatory agenda | https://www.reginfo.gov/public/do/eAgendaViewRule?pubId=202510&RIN=0945-AA22 | checked 30 Sep 2026 | curl; not cited now |
| 57 | CMS, CLIA page, modified 9 September 2026 | https://www.cms.gov/medicare/quality/clinical-laboratory-improvement-amendments | checked 30 Sep 2026 | curl |
| 58 | Social Security Act, section 1862 | https://www.ssa.gov/OP_Home/ssact/title18/1862.htm | checked 30 Sep 2026 | curl |
| 59 | CMS, FFS ABN page, modified 17 July 2026 | https://www.cms.gov/medicare/forms-notices/beneficiary-notices-initiative/ffs-abn | checked 30 Sep 2026 | curl |
| 60 | CMS, fact sheet on the Interoperability and Prior Authorization Final Rule (CMS-0057-F), 17 January 2024 | https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-and-prior-authorization-final-rule-cms-0057-f | checked 30 Sep 2026 | curl; the URL now redirects to https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f, which the dossier cites (checked 30 Sep 2026) |
| 61 | CMS memo of 6 February 2024, frequently asked questions on coverage criteria and utilisation management, as hosted by the AHA | https://www.aha.org/system/files/media/file/2024/02/faqs-related-to-coverage-criteria-and-utilization-management-requirements-in-cms-final-rule-cms-4201-f.pdf | checked 30 Sep 2026 | curl, PDF read |
| 62 | California Legislature, SB 1120, chaptered, approved 28 September 2024 | https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240SB1120 | checked 30 Sep 2026 | curl; not cited now |
| 63 | CMS, Medicare Advantage Part C application for 2024, section 3.17 | https://www.cms.gov/files/document/cy-2024-medicare-advantage-part-c-application.pdf-1 | checked 30 Sep 2026 | curl, PDF read; not cited now, replaced by 78 |
| 64 | Texas HHSC, Managed Care Uniform Terms and Conditions, version 1.3, section 4.10 | https://www.hhs.texas.gov/sites/default/files/documents/amended-star-health-2.pdf | checked 30 Sep 2026 | curl, PDF read; re-read on 30 Sep 2026 through the Wayback capture of 31 October 2025, the latest, for sections 4.10(1) to (6) |
| 65 | MeitY, the Digital Personal Data Protection Act 2023 as published in the Gazette, 11 August 2023 | https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf | checked 30 Sep 2026 | curl, PDF read for sections 8 and 17 |
| 66 | American Hospital Association, on the Change Healthcare cyberattack | https://www.aha.org/change-healthcare-cyberattack-underscores-urgent-need-strengthen-cyber-preparedness-individual-health-care-organizations-and | checked 30 Sep 2026 | WebFetch |
| 67 | CBS News, the UnitedHealth Senate hearing, 1 May 2024 | https://www.cbsnews.com/news/unitedhealth-senate-hearing-cyberattack-change-healthcare/ | checked 30 Sep 2026 | WebFetch; not cited now |
| 68 | UnitedHealth Group, cyberattack status update, 18 March 2024 | https://www.unitedhealthgroup.com/newsroom/2024/2024-03-18-uhg-cyberattack-status-update.html | checked 30 Sep 2026 | WebFetch; not cited now |
| 69 | Skilled Nursing News, the nH Predict lawsuit, 14 February 2025 | https://skillednursingnews.com/2025/02/lawsuit-against-unitedhealth-over-ai-based-denials-of-post-acute-care-moves-ahead/ | checked 30 Sep 2026 | WebFetch |
| 70 | Courthouse News, the Cigna PxDx class claims | https://www.courthousenews.com/judge-advances-class-claims-over-cigna-use-of-automated-algorithm-to-deny-benefits/ | checked 30 Sep 2026 | WebFetch; not cited now |
| 71 | Experian Health, third annual State of Claims survey, 22 September 2025 | https://www.experianplc.com/newsroom/press-releases/2025/experian-health-s-3rd-annual-state-of-claims-survey-finds-denial | checked 30 Sep 2026 | WebFetch; not cited now |
| 72 | JAMIA rapid review citing Dantas et al. on no-show rates | https://pmc.ncbi.nlm.nih.gov/articles/PMC9933067/ | checked 30 Sep 2026 | WebFetch; not cited now, since its range is global and the files give no no-show figure |
| 73 | CMS, 835 flat file, version 5010A1 | https://www.cms.gov/medicare/billing/electronicbillingeditrans/downloads/835-flatfile.pdf | checked 30 Sep 2026 | curl; not cited now |
| 74 | CDC, the A1C test page under diabetes testing | https://www.cdc.gov/diabetes/diabetes-testing/prediabetes-a1c-test.html | checked 30 Sep 2026 | WebFetch |
| 75 | eCFR, 42 CFR 438.602 | https://www.ecfr.gov/current/title-42/section-438.602 | checked 30 Sep 2026 | eCFR API, curl, by the rigor reviewer; not cited now |
| 76 | eCFR, 45 CFR 164.314 | https://www.ecfr.gov/current/title-45/section-164.314 | checked 30 Sep 2026 | eCFR API renderer, curl |
| 77 | eCFR, 42 CFR 493.1445 | https://www.ecfr.gov/current/title-42/section-493.1445 | checked 30 Sep 2026 | eCFR API renderer, curl |
| 78 | CMS, CY 2027 Part C Medicare Advantage and 1876 Cost Plan Expansion Application, section 3.17 | https://www.cms.gov/files/document/cy2027-medicare-advantage-part-c-application.pdf | checked 30 Sep 2026 | curl, PDF read |
| 79 | CMS, 2027 Part D application | https://www.cms.gov/files/document/2027-part-d-application-final.pdf | checked 30 Sep 2026 | curl, PDF read |
| 80 | CMS, CY 2024 Readiness Checklist for MA organizations and Part D sponsors, section II | https://www.cms.gov/files/document/partscdreadinesschecklistcy2024.pdf | checked 30 Sep 2026 | curl, PDF read; not cited now, since the 2025 to 2027 checklists were not found at the same address |
| 81 | MeitY, Digital Personal Data Protection Rules 2025, G.S.R. 846(E), 13 November 2025 | https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf | checked 30 Sep 2026 | curl, PDF read for rule 1(4) and rule 6 |
| 82 | Quest Diagnostics, 10-K for 2025, exhibit 21.1, subsidiaries | https://www.sec.gov/Archives/edgar/data/1022079/000102207926000015/dgx12312025ex211.htm | checked 30 Sep 2026 | curl with a declared user agent |
| 83 | US Senate Committee on Finance, written testimony of Andrew Witty, 1 May 2024 | https://www.finance.senate.gov/imo/media/doc/0501_witty_testimony.pdf | checked 30 Sep 2026 | curl, PDF read; not cited now |
| 84 | The Build 1 data pack: `sites`, `test_catalogue`, `claims`, `remittances` and `booking_tests` in `content/W03/D1/data/`, written by `data/generate_kalpa_health.py` | the repository, after the merge of origin/main | read 30 Sep 2026 | pandas, for the metros, payers, denial categories, dates, list prices, the commercial terms on a $135 claim, the posting lag and the plant check |

## Compliance, checked on 30 September 2026 against the official text

A research agent read each rule on 30 September 2026 and quoted it; the eCFR text was current to 28 September 2026. eCFR's own pages redirect to a bot check, so its API renderer (`https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-45?part=164&section=164.502` and the same pattern for each section) was read; hhs.gov refused both readers with a 403, so its pages were read through Wayback Machine captures of 19 to 29 September 2026, each named below. The right-hand column is what the files say the rule requires, and no more.

| Rule | The text, quoted | Citation, URL and route | What the files say it requires |
|---|---|---|---|
| Minimum necessary | "a covered entity or business associate must make reasonable efforts to limit protected health information to the minimum necessary to accomplish the intended purpose of the use, disclosure, or request." | 45 CFR 164.502(b)(1), https://www.ecfr.gov/current/title-45/section-164.502, eCFR API | Whoever uses, discloses or requests PHI makes reasonable efforts to keep it to what the purpose needs |
| Its exceptions | "This requirement does not apply to: (i) Disclosures to or requests by a health care provider for treatment; (ii) Uses or disclosures made to the individual ...; (iii) ... pursuant to an authorization ...; (iv) Disclosures made to the Secretary ...; (v) ... required by law ...; (vi) ... required for compliance with applicable requirements of this subchapter." | 45 CFR 164.502(b)(2), same | Six cases fall outside it, among them treatment and the patient |
| Access by role | A covered entity must identify "Those persons or classes of persons ... in its workforce who need access to protected health information to carry out their duties" and "the category or categories of protected health information to which access is needed", and "must make reasonable efforts to limit the access of such persons or classes" | 45 CFR 164.514(d)(2), https://www.ecfr.gov/current/title-45/section-164.514, eCFR API | A covered entity limits each role to the categories of PHI it needs |
| Minimum necessary and business associates | HHS lists among the violations for which "Business associates are directly liable": "Failure to make reasonable efforts to limit PHI to the minimum necessary to accomplish the intended purpose of the use, disclosure, or request." | HHS, "Direct Liability of Business Associates", https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/business-associates/factsheet/index.html, Wayback capture 19 Sep 2026, last reviewed 16 Jul 2021 | The standard binds a business associate directly |
| De-identification, the standard | "Health information that does not identify an individual and with respect to which there is no reasonable basis to believe that the information can be used to identify an individual is not individually identifiable health information." | 45 CFR 164.514(a), eCFR API | De-identified data is not PHI |
| Expert determination | An expert "determines that the risk is very small that the information could be used, alone or in combination with other reasonably available information, by an anticipated recipient to identify an individual" and "Documents the methods and results of the analysis" | 45 CFR 164.514(b)(1), eCFR API | A qualified expert finds, and documents, a very small risk |
| Safe harbor, the list | "The following identifiers of the individual or of relatives, employers, or household members of the individual, are removed", (A) to (R), eighteen kinds, ending "(R) Any other unique identifying number, characteristic, or code, except as permitted by paragraph (c)" | 45 CFR 164.514(b)(2)(i), eCFR API | Eighteen kinds of identifier go, for the patient and for relatives, employers and household members; any unique number or code is one of them |
| Safe harbor, geography | "All geographic subdivisions smaller than a State ... except for the initial three digits of a zip code if ... The geographic unit formed by combining all zip codes with the same three initial digits contains more than 20,000 people", and the three digits of smaller units become 000 | 45 CFR 164.514(b)(2)(i)(B), eCFR API | Geography below a state goes, except a three-digit ZIP whose area holds more than 20,000 people |
| Safe harbor, dates and ages | "All elements of dates (except year) for dates directly related to an individual ...; and all ages over 89 and all elements of dates (including year) indicative of such age, except that such ages and elements may be aggregated into a single category of age 90 or older" | 45 CFR 164.514(b)(2)(i)(C), eCFR API | Only the year of a date tied to the patient stays; ages over 89 are grouped as 90 or older |
| Safe harbor, the second condition | "(ii) The covered entity does not have actual knowledge that the information could be used alone or in combination with other information to identify an individual who is a subject of the information." | 45 CFR 164.514(b)(2)(ii), eCFR API | The covered entity has no actual knowledge that what is left could identify the person |
| Lab dates | "Dates associated with test measures, such as those derived from a laboratory report, are directly related to a specific individual and relate to the provision of health care. Such dates are protected health information." | HHS de-identification guidance, FAQ 3.4, https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html, Wayback capture 26 Sep 2026, last reviewed 3 Feb 2025 | Under safe harbor a draw or result date keeps only its year |
| Business associate, the definition | "other than in the capacity of a member of the workforce ... creates, receives, maintains, or transmits protected health information for a function or activity regulated by this subchapter, including claims processing or administration, data analysis, processing or administration, ... billing, ..." and "(iii) A subcontractor that creates, receives, maintains, or transmits protected health information on behalf of the business associate" | 45 CFR 160.103, https://www.ecfr.gov/current/title-45/section-160.103, eCFR API | Anyone outside the workforce handling PHI for a covered entity's regulated work is a business associate, and so is a subcontractor handling that PHI on its behalf |
| The agreement | "(i) Establish the permitted and required uses and disclosures"; "(B) Use appropriate safeguards and comply, where applicable, with subpart C"; "(C) Report to the covered entity any use or disclosure of the information not provided for by its contract ..., including breaches of unsecured protected health information"; "(D) ... ensure that any subcontractors ... agree to the same restrictions and conditions"; "(J) At termination of the contract, if feasible, return or destroy all protected health information"; and 164.314(a)(2)(i)(C), "Report to the covered entity any security incident of which it becomes aware" | 45 CFR 164.504(e)(2), eCFR API; 45 CFR 164.314(a), source 76 | The agreement sets permitted uses, requires Security Rule safeguards, requires reports of misuse, security incidents and breaches, binds subcontractors to the same restrictions, and returns or destroys the PHI at the end where feasible |
| Written assurance first | A covered entity may disclose PHI to a business associate "if the covered entity obtains satisfactory assurance that the business associate will appropriately safeguard the information", documented "through a written contract or other written agreement or arrangement" | 45 CFR 164.502(e) and 164.308(b), eCFR API | PHI reaches an associate only on written assurances |
| Direct liability | "In 2009, Congress enacted the Health Information Technology for Economic and Clinical Health (HITECH) Act, making business associates of covered entities directly liable for compliance with certain requirements of the HIPAA Rules"; OCR may act against business associates "only for those requirements and prohibitions" listed, ten in all, among them "Failure to comply with the requirements of the Security Rule" and "Impermissible uses and disclosures of PHI" | HHS, direct liability fact sheet, as above | HHS can act against a business associate directly for ten listed failures |
| Offshore storage | Q: "Do the HIPAA Rules allow a covered entity or business associate to use a CSP that stores ePHI on servers outside of the United States?" A: "Yes, provided the covered entity (or business associate) enters into a business associate agreement (BAA) with the CSP and otherwise complies with the applicable requirements of the HIPAA Rules"; the rules "do not include requirements specific to protection of electronic protected health information (ePHI) processed or stored by a CSP or any other business associate outside of the United States"; entities "should take these risks into account when conducting the risk analysis" | HHS, guidance on HIPAA and cloud computing, https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html, Wayback capture 27 Sep 2026, last reviewed 23 Dec 2022 | HIPAA itself sets no border; data abroad is allowed under an agreement and the rest of HIPAA, with the location weighed in the risk analysis |
| Medicare Advantage offshore attestation | "Applicant agrees to submit the Offshore Subcontract Information and Attestation for each offshore subcontractor (first tier, downstream, and related entities) that receives, processes, transfers, handles, stores, or accesses Medicare beneficiary PHI by the last Friday in September for the upcoming contract year." | CMS, CY 2027 Part C application, section 3.17, source 78 | A Medicare Advantage plan gives CMS information and an attestation for each offshore subcontractor that touches beneficiaries' PHI |
| Part D | "provide names of the first tier, downstream and related entities you will use to carry out each of the functions listed in this chart and whether the first tier, downstream and related entities are off-shore." | CMS, 2027 Part D application, source 79 | A Part D sponsor names which of its contractors are offshore |
| Texas Medicaid managed care | "The MCO and all Subcontractors, vendors, agents, and service Providers of or for the MCO must not allow any Confidential Information that the MCO receives from or on behalf of HHSC to be moved outside the United States by any means (physical or electronic) at any time, for any period of time, for any reason"; they "must not permit any person to have remote access to HHSC information, systems, or Deliverables from a location outside of the United States"; and "Unless otherwise approved in advance by HHSC in writing", they "must perform all services under the Agreement ... within the United States", which "includes all services, including information technology services, processing, transmission, storage, archiving, data center services, disaster recovery sites and services, customer support), medical, dental, laboratory, and clinical services" | Texas HHSC, Managed Care Uniform Terms and Conditions, version 1.3, section 4.10(3) and (4), source 64, Wayback capture 31 Oct 2025 | The plan and its subcontractors, vendors, agents and service providers keep the contract's work and the state's confidential information inside the US, with no remote access from outside, unless the state approves in writing |
| India's DPDP Act, the exemption | "The provisions of Chapter II, except sub-sections (1) and (5) of section 8, and those of Chapter III and section 16 shall not apply where ... (d) personal data of Data Principals not within the territory of India is processed pursuant to any contract entered into with any person outside the territory of India by any person based in India" | Digital Personal Data Protection Act 2023, section 17(1)(d), source 65 | For foreigners' data processed in India under a contract with a person abroad, Chapter II except 8(1) and 8(5), Chapter III and section 16 do not apply |
| What survives | 8(1): a Data Fiduciary shall "be responsible for complying with the provisions of this Act and the rules made thereunder in respect of any processing undertaken by it or on its behalf by a Data Processor"; 8(5): it "shall protect personal data in its possession or under its control ... by taking reasonable security safeguards to prevent personal data breach" | Same | The responsibility for processing on one's behalf and the duty of reasonable security safeguards remain |
| When it applies | DPDP Rules 2025, G.S.R. 846(E), 13 November 2025, rule 1(4): "Rules 3, 5 to 16, 22 and 23 shall come into force eighteen months after the date of publication"; rule 6 is "Reasonable security safeguards". The Act's own commencement notification for sections 8 and 17 could not be read on an official page (India Code's files and the eGazette were unreachable) | Source 81 | The dossier says the date these sections take effect was not verified, and gives none |
| Breach notice | "without unreasonable delay and in no case later than 60 calendar days after discovery of a breach" of "unsecured protected health information"; HHS "contemporaneously" for 500 or more and within 60 days of the year's end for fewer; media for "more than 500 residents of a State or jurisdiction" | 45 CFR 164.404, 164.408, 164.406, eCFR API | As the dossier states |
| Medicare timely filing | "the claim must be filed no later than the close of the period ending 1 calendar year after the date of service", "Except as provided in paragraphs (b) and (e)" | 42 CFR 424.44(a)(1), eCFR API | One calendar year from the date of service, with listed exceptions |
| Prior authorisation | "send prior authorization decisions within 72 hours for expedited (i.e., urgent) requests and seven calendar days for standard (i.e., non-urgent) requests"; "Beginning in 2026, impacted payers must provide a specific reason for denied prior authorization decisions"; "generally beginning January 1, 2026" | CMS fact sheet on CMS-0057-F, source 60, at its new URL | As the dossier states |
| CLIA and the lab director | "all laboratories must be properly certified to receive Medicare or Medicaid payments"; the director "is responsible for the overall operation and administration of the laboratory" | CMS CLIA page, modified 9 Sep 2026, source 57; 42 CFR 493.1445, source 77 | As the dossier states |

## Ten company facts re-checked at random

The research agent numbered every fact the files gave about a named company or publisher before this session's rewrite, 52 in all, and drew ten with Python 3.11.15: `random.seed(20261019); random.sample(list(range(1, 53)), 10)` gives items 38, 21, 47, 8, 14, 31, 35, 19, 18 and 2. Each was re-read on 30 September 2026 against its source.

| Item | Fact as the files stated it | The source line, read today | Verdict, and what changed |
|---|---|---|---|
| 2 | Quest: $10,785 million of 2025 net revenues from diagnostic testing | "DIS revenues $10,785" (dollars in millions), source 1 | Confirmed |
| 8 | Quest: 2025 net revenue shares by payer, 39, 16, 31 and 12 | "Healthcare insurers 43% 39%", "Government payers 17 16", "Client payers 37 31", "Patients * 1 12", source 1 | Confirmed |
| 14 | Quest: operating income $1,556 million, 14.1 percent of net revenues | "Operating income $1,556"; "Operating income 14.1 %", source 1 | Confirmed |
| 18 | Quest's 10-K names sites in Canada, Finland, Puerto Rico and Mexico and does not mention India | "including in Canada, Finland, Puerto Rico and Mexico", source 1; exhibit 21.1 lists "Quest Diagnostics HTAS India Private Limited (India)" and "Quest Diagnostics India Private Limited (India)", source 82 | Corrected: the talk track now says the list is not exhaustive and that two Indian subsidiaries appear, with their work undescribed |
| 19 | Quest launched mobile phlebotomy in November 2023 | "Nov. 9, 2023 ... today announced the launch of Quest Mobile", source 4 | Confirmed |
| 21 | Labcorp: revenue of $13,951.7 million for 2025, 10-K filed 24 February 2026 | "During 2025, the Company's revenues of $13,951.7 million"; EDGAR "Filing Date 2026-02-24", source 3 | Confirmed |
| 31 | AGS Health: more than 15,000 revenue-cycle staff worldwide | "growing its workforce to more than 15,000 skilled RCM professionals worldwide", source 8 | Confirmed, as the company's undated page says |
| 35 | Omega Healthcare: coding, billing, accounts receivable follow-up, denials and appeals management | "Medical Records Coding", "Claims Management & Billing", "A/R Management & Collections", "Denials & Appeals Management", source 10 | Confirmed; Omega is no longer named in the files |
| 38 | CMS: US health spending was 18.0 percent of GDP in 2024 | "NHE grew 7.2% to $5.3 trillion in 2024, or $15,474 per person, and accounted for 18.0% of Gross Domestic Product (GDP)", page last modified 24 June 2026, source 13 | Confirmed |
| 47 | UnitedHealth's chief executive told a Senate committee the server "did not have MFA on it" | CBS places the words at "a congressional hearing" and names "the House Energy and Commerce Committee", source 67; the Senate Finance written testimony says "The portal did not have multi-factor authentication", source 83 | Corrected by removal: the quote is no longer in the files |

Eight confirmed and two corrected. Whatever the sample, Quest's net revenues of $11,035 million and its 2,400 patient service centres "located inside large retail stores or in convenient retail settings", and Labcorp's $13,951.7 million and "more than 2,200 PSCs", were re-read and confirmed the same day. Quest's AI sentence (item 16 of the agent's list) was reworded to what the 10-K says: in 2025 Quest "initiated or expanded our use of AI and automation in several areas", and "Other areas of focus include reducing denials and patient concessions".

## Fact by fact

Where: D is the dossier and its section, C is the card and its panel, T is the talk track and its part, and Tf is the talk track's facts table. Sources are numbered as in the table above.

| Fact as the files state it | Where | Source |
|---|---|---|
| E11.9 is "Type 2 diabetes mellitus without complications" | D1, D6, T1 | 30 |
| The HbA1c shows average blood sugar over about three months | D1 | 74 |
| Traditional Medicare is federal insurance for people 65 and older, and some younger people with disabilities | D1, D3, C4, T4 | 34 |
| The advance notice a Medicare patient signs before a service Medicare may refuse | D1, D6, D7 | 59 |
| US health spending of $5.3 trillion in 2024, 18.0 percent of GDP | D2 | 13 |
| Quest: net revenues of $11,035 million in 2025; about 244 million requisitions; about 2,400 patient service centres, many inside large retail stores | D2, T2, Tf | 1 |
| Quest launched mobile phlebotomy in November 2023 on a network of 5,000 mobile phlebotomists | D2 | 4 |
| Labcorp: revenue of $13,951.7 million, $10,876.5 million from diagnostics; more than 2,200 patient service centres; more than 7,000 phlebotomists in customers' offices; a leased Bangalore facility for its biopharma laboratory business | D2, T2, Tf | 3 |
| Quest's requisition "indicating the test(s) to be performed and the party to be billed for the test(s)" | D2 | 1 |
| Quest: requisitions billed to patients alone 1 percent of volume; patients 12 percent of net revenues and 20 percent of receivables; insured patients' deductibles and coinsurance counted as patient revenue while their requisitions count under insurers | D2, T4, Tf | 1 |
| Optum India is UnitedHealth Group's largest Global Capability Centre | D2, T2, Tf | 5 |
| Carelon Global Solutions, "born out of one of the largest health plans in the U.S.", in Bengaluru, Hyderabad and Gurugram | D2 | 6 |
| AGS Health: more than 15,000 revenue-cycle staff worldwide; Indian centres including Chennai, Hyderabad and Bengaluru | D2, T2, Tf | 8 |
| Access Healthcare: Indian centres including Chennai, Bengaluru and Hyderabad | D2, T2 | 9 |
| Quest's 10-K names sites outside the US "including in Canada, Finland, Puerto Rico and Mexico", and its exhibit 21.1 names two Indian subsidiaries without describing their work | T2, Tf | 1, 82 |
| Traditional Medicare pays lab tests mostly from its Clinical Laboratory Fee Schedule; its patients "usually pay nothing for Medicare-covered diagnostic laboratory tests" | D3, T3, T4, Tf | 33, 34 |
| Employment-based insurance covered 53.5 percent of Americans for some or all of 2025; 7.9 percent had no coverage all year | D3 | 14 |
| Quest's revenue estimate includes "the impact of contractual allowances (including payer denials), and patient price concessions" | D3 | 1 |
| Quest: cost of services 66.8 percent, selling, general and administrative 17.8 percent, operating income 14.1 percent, $1,556 million, of 2025 net revenues | D3, T3, Tf | 1 |
| Quest: days sales outstanding, "a measure of billing and collection efficiency", 48 at the end of 2025 and 2024 | D3, Tf | 1 |
| The initial denial rate, clean claim rate and days in AR as HFMA defines them | D5, C2 | 35, 36 |
| HealthCare.gov insurers denied 19 percent of in-network claims in 2024, from 3 to 36 percent by insurer | D5 | 17 |
| Allowed amount, deductible, coinsurance and copay | D3, D5, D6, C2, C4 | 40 |
| Pathology and laboratory CPT codes run from 80000 to 89999 | D6 | 26 |
| CPT is kept by the AMA | D6, C4 | 27 |
| ICD-10-CM is kept by NCHS at CDC, each year's set in force from 1 October | D6 | 28, 29, 30 |
| NPI: "a unique 10-digit number used to identify health care providers", through NPPES | D6 | 32 |
| 270 and 271, 276 and 277, 278, 837 and 835 are X12 transactions; version 5010 since 1 January 2012 | D6, C4, T1 | 18, 22, 23 |
| CARCs are maintained by a committee under X12 | D6 | CMS MLN article MM12478, https://www.cms.gov/files/document/mm12478-remittance-advice-remark-code-rarc-claims-adjustment-reason-code-carc-medicare-remit-easy.pdf (checked 30 Sep 2026) |
| Group codes CO, PR, OA and PI | D6, T3 | 20, 21 |
| CARC descriptions for 2, 16, 18, 27, 29, 45, 50, 96 and 197, quoted exactly | D6, T3 | 19 |
| The seven denial categories as Kalpa Health's claims file names them | D6 | The data pack; decision `build1-us-data` |
| Minimum necessary, de-identification, business associates, breach notice, timely filing, offshore | D7, D9, C5, T6, Tf | The compliance table above |
| Covered entities are health plans, clearinghouses and providers transmitting in the standard transactions | D7, T6 | 41 |
| PHI in "any form or media, whether electronic, paper, or oral" | D7 | 49 |
| Security Rule safeguards and the risk analysis, 45 CFR 164.308 to 164.312 | D7 | 46 |
| "all laboratories must be properly certified to receive Medicare or Medicaid payments"; the lab director answers for the lab's overall operation | D7, T2 | 57, 77 |
| Medicare pays nothing for services "not reasonable and necessary for the diagnosis or treatment of illness or injury" | D7 | 58 |
| Prior-authorisation decisions within 72 hours urgent and 7 calendar days standard, with a specific denial reason, generally from 1 January 2026, for Medicare Advantage, Medicaid and CHIP and their managed-care plans | D7 | 60 |
| CMS on algorithms in Medicare Advantage coverage decisions, 6 February 2024 | D7, T6, Tf | 61 |
| The Medicare Advantage and Part D offshore attestation, quoted | D7 | The compliance table above |
| Texas's Medicaid managed-care contract, quoted | D7, T6, Tf | The compliance table above |
| DPDP Act section 17(1)(d), with sections 8(1) and 8(5) still applying | D7 | The compliance table above |
| Change Healthcare: attacked 21 February 2024; by the AHA's count its network processes 15 billion health care transactions a year, eligibility checks, claims and payments among them | D7 | 66 |
| About 192.7 million individuals, reported to HHS on 31 July 2025 | D7 | 54 |
| Quest started or widened its use of AI and automation in several areas in 2025, names reducing "denials and patient concessions" among its other areas of focus, and continues to broaden AI in customer service | D8 | 1 |
| nH Predict: allegations; breach-of-contract and good-faith claims allowed to proceed in February 2025 | D8, T6, Tf | 69 |
| The reading path's nine URLs | D12 | 1, 37, 39, 19, 49, 50, 52, 60, 17 |

## Illustrative and invented numbers

Every number below is illustrative, chosen for easy arithmetic, labelled so where it appears, and neither Kalpa Health's data nor any real company's.

| Number | What it is | Where |
|---|---|---|
| $100 gross, $55 contractual, $45 allowed, $3 never collected, $42 net revenue, $28 cost, $14 gross profit, $8 other costs, $6 operating income | The waterfall; 6 of 42 is 14.3 percent against Quest's 14.1; 28 of 42 is 66.7 percent against 66.8; 8 of 42 is 19.0 percent against 17.8, since Quest also reports amortisation and other operating costs below its SG&A line | D3, C6, T3 |
| $1 of $45 is 2.2 percent; $1 of $6 is a sixth | The leak arithmetic | D3, C6, T3 |
| $46.80 to perform James's tests, $5 to bill and collect; contributions of $18.40, $4.36 and minus $51.80 | James's claim at the waterfall's cost share: 28 of 42 is two thirds, and two thirds of $70.20 is $46.80; 70.20 less 51.80 is 18.40; 56.16 less 51.80 is 4.36 | D3, D4 |
| 10,000 claims; $2,000,000 gross, $200 a claim; $900,000 allowed; $1,100,000 contractual; $60,000 never collected; $840,000 net revenue; $135,000 patient responsibility, 15 percent | The month at a made-up lab | D5, T5 |
| An 8 percent list-price rise, $2,160,000 | The gross charges trap | D5, C3, T5 |
| $1,160,000 in one write-offs line, hiding $60,000 | The contractual adjustment trap | D5, C3 |
| 500 denied of 10,000, 5 percent; $70,000 of $2,000,000, 3.5 percent | Denial rate by count and by dollars | D5, T5 |
| 8,800 of 10,000 clean, 88 percent | Clean claim rate | D5 |
| $1,260,000 over $28,000 a day, 45 days; 45 to 38 after a write-off | Days in AR | D5, T5 |
| $840,000 of $900,000, 93.3 percent; $540,000 before the window closes, 60 percent | Net collection rate and its trap | D5 |
| A median of 18 hours, 92 percent within 24 | Turnaround time | D5 |
| About 120,000 rows; 730 rows a lab | Section 9's sizing, at 10,000 claims a month | D9 |
| 3,000 checks a day at six minutes, 300 staff-hours; 400 misread a week for four weeks, 1,600 claims at $90 allowed, $144,000 | The claim-status agent; $90 is 45 percent of the $200 average charge | D8 |
| "Days in AR are up to 52", and the glossary's sentences | Section 6's meeting lines | D6 |

## Definitions held the same in every file

| Term | The one definition | Where it appears |
|---|---|---|
| Gross charges | Tests billed at the lab's chargemaster prices | D1, D3, D5, D6, C2, T3 |
| Allowed amount | The most the payer's contract or fee schedule permits for a covered test, which is the payer's share plus the patient's responsibility | D1, D3, D5, D6, C1, C2, T3 |
| Contractual adjustment | Gross charges less the allowed amount | D1, D3, D5, D6, C2, T3 |
| Net revenue | Gross charges less contractual adjustments, less what the lab expects never to collect | D3, D5, C2, T3 |
| Patient responsibility | Deductible plus coinsurance plus copay | D1, D3, D5, C2 |
| Initial denial rate | Claims denied in full or part on first answer over claims submitted, on one stated basis | D5, D10, C2, T5 |
| Clean claim rate | Claims passing every edit untouched over claims entered for billing, counted before any claim leaves | D5, C2, T5 |
| Days in AR | Net receivable over average net revenue per day | D3, D5, D10, C2, T5 |
| Net collection rate | Payments over gross charges less contractual adjustments, which is the allowed amount, on the same claims once the window closes | D5, C2 |

## Not verified, or verified only through a secondary source

- The date on which sections 8 and 17 of India's Digital Personal Data Protection Act 2023 take effect: the commencement notification could not be read on an official page, and law-firm summaries found by search say 13 May 2027. The dossier says the date was not verified and gives none.
- The net collection rate's formula is the industry's common one, payments over charges less contractual adjustments; HFMA has no key by that name, and the files state the formula without attributing it.
- The CMS memo of 6 February 2024 was read from the AHA's hosted copy; the original was not found on cms.gov.
- What Quest's two Indian subsidiaries do is not stated in the 10-K, so the talk track says only that they are listed.
- Headcounts for Optum India and Carelon were not found on a primary page, so the files state none.
- AGS Health's and Access Healthcare's figures and locations are what each company says of itself on an undated page.
- The Change Healthcare transaction count is the AHA's figure.
- No industry-wide initial denial rate for labs was found in a primary source; the files use KFF's marketplace figure only.
- The CMS readiness checklists for 2025 to 2027 were not found at the 2024 checklist's address, so the files cite the 2027 applications only.
- The AAPC video's content was read from its trailer page; the full video needs a free sign-up.
- HHS adopted HIPAA standards for claims attachments on 24 March 2026 (91 FR 14350); the section 6 file list does not name them, and their compliance date was not checked.

## Decisions and open points for the orchestrating session

1. **The build-day folders.** `scripts/verify.py` allows `study-notes/` and `cheatsheets/` on a build day, with a comment naming decision `four-domains`, and `content/README.md` says so. The change survived the merge of `origin/main` on 30 September 2026 unchanged.
2. **The 45-minute slot.** The rewritten spine still gives Monday's minutes to the introduction, the allocation, the translation and the close, so the talk track marks its placement before the Programme Head's introduction as proposed; the requester or the session rebuilding the Monday pack takes the 45 minutes from a named block.
3. **Length.** The dossier runs to the word count in the depth loop below by the section counter, fences and URLs excluded, against the reference's 6,000 to 8,000.
4. **The domain's volume tree.** The dossier teaches the charge-to-cash tree and leaves the lab's volume tree to the groups, since it is sub-problem 1.
5. **No-show rate.** The files neither define nor compute a no-show rate, since sub-problem 4's trap sits in its denominator; the earlier section 8 row on no-show prediction is removed.
6. **The India-setting data.** Resolved: pull request 202 regenerated the data pack in the US setting, and the talk track's line for a room that noticed rupee columns is removed.
7. **The billed-against-collected watch item.** Resolved by removal: the net collection rate's trap is now the collection window, the card's "collections over gross charges" row is gone, and the talk track's question of $888,000 on $2,400,000 is replaced by a days-in-AR question, since dividing collections by charges walked the gap sub-problem 3 asks groups to reconcile.
8. **James's claim is data, not illustration.** His $135, $64.80, $70.20, $56.16 and $14.04 are the data pack's own values for a commercial claim of that size, so a learner who finds such a row in the remittances file sees the dossier agree with it. If the generator's list prices or commercial terms change, these five numbers and the card's panel 1 change with them.

## The plant check

The dossier and the card are STUDENT files read on Build 1 Monday, before any group has found anything. Checked on 30 September 2026 against the rewritten `docs/detailing/W03_build1_spine.md` (its plant table and its five sub-problems), the Wednesday checkpoint questions, the Wednesday parallel build's run sheet and the Saturday panel's trap lines, which together list every trap Build 1 stages:

| What the week plants or stages | What the files say about it |
|---|---|
| The headline: the dashboard counts old-system retail tests, a panel as its component tests, and the reading moves with the counting unit | Nothing. The files give Dr Menon's 5 against 18 as her dashboard's reading and never say how any count is made; "panel" is defined as tests ordered by one name, with no word on how a panel is counted or billed |
| Sub-problem 1: one employer wellness contract in Q3, the mean claim against the median, panels billed as one claim line, billed amounts stored as text | Nothing. No employer, contract, account or large order appears; no mean, median or claim-line count; the payer table lists the four payer kinds of section 1c only |
| Sub-problem 2: two metros moved to a new booking system, the old export carries only its own bookings, repeated rows, month-first dates | Nothing. No system, export, migration, repeat or date format appears, and no metro is singled out |
| Sub-problem 3: the posting system's own claim keys, double posts from repeated ERA loads, an unpaid invoice, denials posted with nothing paid, reversals, and which rows count as money received | Nothing. The files define the claim, the remittance and a denial, and never say how a posting is keyed, repeated, reversed or counted. The earlier version's trap of dividing collections by gross charges, and the talk track's question of $888,000 on $2,400,000, are removed, since they walked the gap between billed and collected dollars that sub-problem 3 asks groups to reconcile |
| Sub-problem 4: one centre runs by appointment while the others count walk-ins; a small base; chance | Nothing. No no-show rate is defined or computed, no denominator is discussed, and the earlier no-show prediction row in section 8 is removed |
| Sub-problem 5: an offer targeted at rising metros, a within-metro reversal, a false positive at p of about 0.03 | Nothing. Home collection appears as a service (section 1's draw and Quest's mobile phlebotomy) and never as an offer, a campaign or a comparison |
| Wednesday's parallel build: rows against distinct ids, amounts that coerce to blanks, a fanned join, quarters of unequal length | Nothing. No row, id, join, coercion or per-day comparison appears |

The traps the files do teach, one per metric card, stage none of the above: a list-price rise read as growth, last year's allowed share applied to this year's claims, contractual adjustments and unpaid balances reported in one line, net revenue as a revised estimate, deductibles resetting each plan year, denial counts heard as dollars, a clean claim that is still denied, days in AR cut by write-offs, collections read before the window closes, and turnaround timed from the lab's door. Checked in the data pack the same day: one list price per test across both quarters, no deductible (a commercial posting's patient share is 0 or 20 percent of the allowed amount), no write-off posting, and payer postings running to 14 November 2026, so none of these traps can be met in the Build 1 files.

## The depth loop

| Pass | Who | What it did |
|---|---|---|
| 1 | The builder | Read the brief, the reference, client zero, the spine, the revamp prompt and the retail model; three research agents checked the regulation, the codes and transactions, and the companies and market against primary sources |
| 2 | The builder, domain pass | Every section opened on a scene before any term; the payer mix, the codes, the offshore limits and the real companies added from the research; definitions set to HFMA's where HFMA has one |
| 3 | The builder, problem-first pass | Section 9's six problems each with options, sizes, the best fit and the fact that would change it; sub-problem material removed or never written |
| 4 | A fresh rigor reviewer, read-only, on 30 September 2026 | Rechecked more than 30 facts against their sources and every chain of arithmetic. One blocking finding: Quest's payer table was misread, since the 1 percent is requisitions billed to patients alone and insured patients' requisitions count under insurers; fixed in the dossier's table and its reading, the talk track's question, correction and facts. Should-fix, all fixed: the GCC sentence now says the coders and AR team handle patient details within the agreement and only the analytics tables carry no names; the "safe default" line and the glossary's PHI line no longer state a rule stricter than HIPAA; Quest's "requisitions and revenue per requisition" line removed as the first split of sub-problem 1's tree; the panel no longer described as billed under one code; days in AR says the receivable is net; the causal link from the lawsuits to CMS's memo removed; four unsourced claims reworded (commercial plans deny more, patients who know pay more, coders scarce, most denials repeat); the talk track's placement marked proposed; "five code sets" corrected; the agent example's claim value set to the month's $80. Minor, all fixed: the NCR worked line, allowed-amount and patient-share wording, one cost label, CARC as "adjusted", Quest Mobile's network, AGS worldwide, Census "some or all", Labcorp's phlebotomists, CLFS "national limits", the CARC citation, traditional Medicare and "her doctor", the banned word, Kavya's role, the talk track's lab correction and drawing note, and the fact rows above. Kept as watch items: the net collection rate trap and the allowed-amount and net-revenue lag traps sit near sub-problems 3 and 2 without teaching them |
| 5 | A fresh pedagogy and language reviewer, read-only, on 30 September 2026 | Mechanical sweeps clean. Two blocking items outside the files' text, both left to the orchestrating session (open points 3 and 7 below). Should-fix, all fixed: Medicare, in network, medical coders, CMS, HHS, HIPAA, CFR, CHIP, MFA and the ABN defined at first use; the codes and CARC tables moved from section 3 to a reference at the end of section 6, with a short paragraph left in section 3; the header's read time and table count; the payer table's clients row and patient reading; the lab's certificate planted in section 1; the tension sentence names the right rows; the builder's client-zero citations and design note removed from the STUDENT file; three antitheses rewritten; the talk track's part 3 wrong answer made realistic, the two kinds of twin set up before "the first kind", part 6 cut to fewer ideas with its acronyms spoken, and the "names only Dr Menon" line fixed; the card's panel 6 shows what is taken and what is left, and its necessity, CARC, trap and pointer lines clarified; the panel example neutralised. Minor, all fixed: James's age, Kavya's role, "cost to collect" removed from section 10, section 9's self-reference, the closing slogan, the banned word, James's tests priced at Medicare's $23.10, the part 2 drawing reduced to four boxes, the part 4 question moved next to the payers, the question "comes back" wording, semicolon fragments in section 9, "Not named" removed with its column, the car-claim scene made a denial, one repeated triad varied, and the pointer to the card removed from section 5 |
| 6 | The raising session, on 30 September 2026 | Merged `origin/main` (standard v3, the retail model, Build 1's US data). Rewrote the dossier to the question ladder: every heading a question, the twelve section questions of the reference, each metric card, term group and problem headed by its own question, and **Who needs the answer.** and **The questions on the way.** under every section, each section closing on its answer. Set James's claim on the data pack's own values and moved every other worked number to a made-up lab; named the six metros, the four payer kinds and the six state Medicaid programmes; tied the seven denial categories to X12 codes read that day. Removed the billed-against-collected trap from the dossier, card and talk track, the employer and client payer row, the payer-split meeting line, the no-show row and the Medicare fee comparison that disagreed with the synthetic prices. A research agent re-read every compliance point against eCFR, HHS, CMS, Texas HHSC and MeitY texts and re-checked ten company facts at random (tables above); section 7 and the talk track were rewritten to the verified text. The humanizer read in file mode on all four files (repeated closers and openings varied, one-line closers merged), the tic scanner on every markdown file, and the card rebuilt on one page |
| 7 | A fresh reviewer, read-only, on 30 September 2026 | See the review log below |

## Tools

Python 3 and pandas for the data checks and word counts; the eCFR API renderer, the Federal Register API and Wayback captures for the rules; pdftotext for PDFs; WebFetch for x12.org and aha.org; mermaid-cli and weasyprint through `scripts/build_cheatsheet.py`, run as `python3 scripts/build_cheatsheet.py content/W03/D1/cheatsheets/C2_W03_D01_us_healthcare_domain_card_STUDENT.md --max-pages 1`, which chose three columns, one page and an anchor sized for 7pt labels; the llm-tic-scrubber scanner on every markdown file; `python3 scripts/verify.py content/W03/D1`.

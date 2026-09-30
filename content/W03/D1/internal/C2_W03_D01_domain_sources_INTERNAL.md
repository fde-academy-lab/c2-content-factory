# Sources: the US healthcare domain dossier, the domain card and the domain story

**INTERNAL.** Every source behind `study-notes/C2_W03_D01_domain_us_healthcare_STUDENT.md` (the dossier), `cheatsheets/C2_W03_D01_us_healthcare_domain_card_STUDENT.md` and its PDF (the card), and `trainer/C2_W03_D01_domain_story_TRAINER.md` (the talk track), with the date each was checked, how it was reached, and a line per fact on where it came from.

---

## What the files are built from

| Source in the repository or the session | What it supplied |
|---|---|
| The requester's brief of 30 September 2026, relayed by the orchestrating session | The four deliverables, the rule that no file teaches Build 1's answers or traps, the nine metrics that must read the same everywhere, the primary sources to use, the offshore question, and the depth loop |
| `CLAUDE.md` | The truth order, the writing rules, the plant rule, the diagram rule, durations only, role labels |
| `.claude/skills/day-pack-builder/references/domain-dossier.md` | The twelve sections, the four files, the diagram set and the proof |
| `docs/07_Client_Zero.md`, v2.2 locked 13 September 2026, with the addenda of 28 and 30 September 2026 | Section 1c: Kalpa Health serves the US market, its labs and patient service centres test US patients and bill US payers, its analytics and revenue-cycle work runs from the GCC in Bengaluru, dollars, US metro areas, the payer, the claim, the denial and prior authorisation, synthetic records; section 1a: Dr Priya Menon, COO, and Kavya Nair; section 1b: the GCC frame; the Build 1 seeds: 5 percent growth against a plan of 18 |
| `data/programme/facts.yaml`, decisions `four-domains` and `health-us-facing` | US healthcare enters on Build 1 Monday with its dossier, card and talk track |
| `docs/detailing/W03_build1_spine.md`, approved 29 September 2026 | The five sub-problems and their plants, read so that no file names, previews or teaches any of them |
| `prompts/week_revamp_W02_W03.md`, section 4, step 1 | The topics the dossier covers: the order, draw, result, claim, remittance and denial with CARC and RARC; the payers; the codes; medical necessity and prior authorisation; HIPAA and business associates; offshore limits; the real companies; the uses of analytics, ML, NLP and agents |
| `docs/curriculum/W3_Build_1.md`, the Monday row | The interview angle's two questions, carried as items 1 and 5 of section 11 with their tags |
| `docs/05_Curriculum_Map_Schema.md` | The interview tags and the rule that the tagging is labelled as the programme's own calibration |
| The retail dossier, card, talk track and sources file on branch `w01-domain-retail` (commit 1d9b823), read on 30 September 2026 | The house form of all four files, the mermaid palette, and the lessons its two reviews left |

## Kalpa facts, and where each comes from

| Kalpa fact as the files state it | Where it comes from |
|---|---|
| Kalpa Health is a diagnostics business serving the US market; its laboratories and patient service centres test US patients and bill US payers | Client zero section 1c; addendum `health-us-facing` |
| Its analytics and revenue-cycle work runs from Kalpa's GCC in Bengaluru | Client zero section 1c |
| Dollars, US metro areas, payers, claims, denials and prior authorisation | Client zero section 1c |
| Every Kalpa Health record is synthetic, so no protected health information exists in the programme | Client zero section 1c; addendum `health-us-facing` |
| Dr Priya Menon is the COO of Kalpa Health | Client zero sections 1a and 1c |
| The business grew 5 percent against a plan of 18 | Client zero, Build 1 seeds; the files state it as growth, without saying how it is counted |
| Kavya Nair is the trainees' senior on the GCC's data and AI team | Client zero sections 1a and 1b |
| The data platform lead owns the warehouse | Client zero section 1a |
| Kalpa Health offers draws at home as well as at centres | The Build 1 seeds name a home-collection campaign; the files mention home draws as a service and never the campaign |
| Kalpa Group is headquartered in Singapore with five units | Client zero section 1 |

Everything else about Kalpa Health in the files is illustrative and labelled so: James Carter, the day's 90 patients and 8 home visits, the $400 deductible, the 18-hour turnaround, the $180, $60 and $120, the month of 12,000 claims, and every sizing in section 9. None comes from the Build 1 data, which is being regenerated in parallel, and none was checked against it. The story names no Kalpa Health metro area.

## External sources, checked on 30 September 2026

Every source below was opened on 30 September 2026. "WebFetch" is the session's page reader; "curl" means the page or file was downloaded and read as text, because the page reader was refused (hhs.gov and sec.gov) or redirected (ecfr.gov, read through its official API). Sources marked "not cited now" were checked and left out of the files.

| # | Source | URL | Checked | How |
|---|---|---|---|---|
| 1 | Quest Diagnostics, Form 10-K for 2025, filed 26 February 2026 | https://www.sec.gov/Archives/edgar/data/1022079/000102207926000015/dgx-20251231.htm | checked 30 Sep 2026 | curl with a declared user agent, text searched |
| 2 | Quest Diagnostics, 8-K exhibit 99.1, results for the quarter to 30 June 2026, 23 July 2026 | https://www.sec.gov/Archives/edgar/data/1022079/000102207926000067/dgx063020268-kex991.htm | checked 30 Sep 2026 | curl; not cited now |
| 3 | Labcorp Holdings, Form 10-K for 2025, filed 24 February 2026 | https://www.sec.gov/Archives/edgar/data/920148/000092014826000111/lh-20251231.htm | checked 30 Sep 2026 | curl with a declared user agent |
| 4 | Quest newsroom, launch of mobile phlebotomy, 9 November 2023 | https://newsroom.questdiagnostics.com/2023-11-09-Quest-Diagnostics-Launches-Mobile-Phlebotomy-Service,-Enabling-Convenient-At-Home-Specimen-Collection-in-the-United-States | checked 30 Sep 2026 | WebFetch |
| 5 | UnitedHealth Group careers, India | https://www.unitedhealthgroup.com/careers/in/work.html | checked 30 Sep 2026 | WebFetch |
| 6 | Carelon Global Solutions, About us | https://www.carelonglobal.in/about-us | checked 30 Sep 2026 | WebFetch |
| 7 | The Cigna Group careers, Evernorth India | https://jobs.thecignagroup.com/us/en/evernorth-india | checked 30 Sep 2026 | WebFetch |
| 8 | AGS Health, company page | https://www.agshealth.com/company/ | checked 30 Sep 2026 | WebFetch |
| 9 | Access Healthcare, locations | https://www.accesshealthcare.com/about/locations | checked 30 Sep 2026 | WebFetch |
| 10 | Omega Healthcare, revenue cycle management | https://www.omegahms.com/solution/revenue-cycle-management/ | checked 30 Sep 2026 | WebFetch |
| 11 | EQT, agreement to acquire GeBBS Healthcare Solutions, 9 September 2024 | https://eqtgroup.com/news/eqt-to-acquire-gebbs-healthcare-solutions-a-leading-healthcare-technology-solutions-provider-2024-09-09 | checked 30 Sep 2026 | WebFetch; not cited now |
| 12 | Great Place to Work India, R1 RCM Global | https://www.greatplacetowork.in/great/company/r1-rcm-global-private-limited/ | checked 30 Sep 2026 | WebFetch; not cited now, since r1rcm.com refused both readers |
| 13 | CMS, National Health Expenditure fact sheet, modified 24 June 2026 | https://www.cms.gov/data-research/statistics-trends-and-reports/national-health-expenditure-data/nhe-fact-sheet | checked 30 Sep 2026 | WebFetch |
| 14 | US Census Bureau, press release on income, poverty and health insurance coverage, 15 September 2026 | https://www.census.gov/newsroom/press-releases/2026/income-poverty-health-insurance-coverage.html | checked 30 Sep 2026 | WebFetch |
| 15 | KFF, "Medicare Advantage in 2026: Enrollment Update and Key Trends", 5 June 2026 | https://www.kff.org/medicare/medicare-advantage-in-2026-enrollment-update-and-key-trends/ | checked 30 Sep 2026 | WebFetch |
| 16 | Medicaid.gov, Medicaid and CHIP enrollment report highlights | https://www.medicaid.gov/medicaid/program-information/medicaid-and-chip-enrollment-data/report-highlights | checked 30 Sep 2026 | WebFetch; not cited now |
| 17 | KFF, "Claims Denials and Appeals in ACA Marketplace Plans in 2024", 24 March 2026 | https://www.kff.org/patient-consumer-protections/claims-denials-and-appeals-in-aca-marketplace-plans-in-2024/ | checked 30 Sep 2026 | WebFetch, and curl for the title |
| 18 | X12, transaction sets | https://x12.org/products/transaction-sets | checked 30 Sep 2026 | WebFetch |
| 19 | X12, claim adjustment reason codes, list dated 1 November 2025 | https://x12.org/codes/claim-adjustment-reason-codes | checked 30 Sep 2026 | WebFetch, and curl for the title |
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
| 33 | CMS, Clinical Laboratory Fee Schedule, modified 24 September 2026, and the 2026 fourth-quarter file | https://www.cms.gov/medicare/payment/fee-schedules/clinical-laboratory-fee-schedule-clfs | checked 30 Sep 2026 | WebFetch; the file at https://www.cms.gov/files/zip/26clabq4.zip downloaded and read for 85025, 80053, 83036 and 80061 |
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
| 45 | eCFR, 45 CFR 164.530 | https://www.ecfr.gov/current/title-45/section-164.530 | checked 30 Sep 2026 | eCFR versioner API, curl with compression |
| 46 | eCFR, 45 CFR part 164, subparts C and D | https://www.ecfr.gov/current/title-45/part-164/subpart-C | checked 30 Sep 2026 | eCFR API, curl; subpart D at https://www.ecfr.gov/current/title-45/part-164/subpart-D (checked 30 Sep 2026) |
| 47 | eCFR, 45 CFR 102.3, last amended 28 January 2026 | https://www.ecfr.gov/current/title-45/section-102.3 | checked 30 Sep 2026 | eCFR API, curl |
| 48 | eCFR, 42 CFR 424.44 | https://www.ecfr.gov/current/title-42/section-424.44 | checked 30 Sep 2026 | eCFR API, curl |
| 49 | HHS, "Summary of the HIPAA Privacy Rule" | https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html | checked 30 Sep 2026 | curl with browser headers |
| 50 | HHS, guidance on de-identification | https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html | checked 30 Sep 2026 | curl with browser headers |
| 51 | HHS, business associate fact sheet | https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/business-associates/factsheet/index.html | checked 30 Sep 2026 | curl with browser headers |
| 52 | HHS, guidance on cloud computing | https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html | checked 30 Sep 2026 | curl with browser headers |
| 53 | HHS, breach notification rule | https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html | checked 30 Sep 2026 | curl with browser headers |
| 54 | HHS, Change Healthcare cybersecurity incident FAQ, last reviewed 13 August 2025 | https://www.hhs.gov/hipaa/for-professionals/special-topics/change-healthcare-cybersecurity-incident-frequently-asked-questions/index.html | checked 30 Sep 2026 | curl with browser headers |
| 55 | Federal Register, the proposed Security Rule, 6 January 2025 | https://www.federalregister.gov/documents/2025/01/06/2024-30983/hipaa-security-rule-to-strengthen-the-cybersecurity-of-electronic-protected-health-information | checked 30 Sep 2026 | Federal Register API |
| 56 | reginfo.gov, RIN 0945-AA22 in the regulatory agenda | https://www.reginfo.gov/public/do/eAgendaViewRule?pubId=202510&RIN=0945-AA22 | checked 30 Sep 2026 | curl |
| 57 | CMS, CLIA page, modified 9 September 2026 | https://www.cms.gov/medicare/quality/clinical-laboratory-improvement-amendments | checked 30 Sep 2026 | curl |
| 58 | Social Security Act, section 1862 | https://www.ssa.gov/OP_Home/ssact/title18/1862.htm | checked 30 Sep 2026 | curl |
| 59 | CMS, FFS ABN page, modified 17 July 2026 | https://www.cms.gov/medicare/forms-notices/beneficiary-notices-initiative/ffs-abn | checked 30 Sep 2026 | curl |
| 60 | CMS, fact sheet on the Interoperability and Prior Authorization Final Rule (CMS-0057-F), 17 January 2024 | https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-and-prior-authorization-final-rule-cms-0057-f | checked 30 Sep 2026 | curl |
| 61 | CMS memo of 6 February 2024, frequently asked questions on coverage criteria and utilisation management, as hosted by the AHA | https://www.aha.org/system/files/media/file/2024/02/faqs-related-to-coverage-criteria-and-utilization-management-requirements-in-cms-final-rule-cms-4201-f.pdf | checked 30 Sep 2026 | curl, PDF read |
| 62 | California Legislature, SB 1120, chaptered, approved 28 September 2024 | https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240SB1120 | checked 30 Sep 2026 | curl |
| 63 | CMS, Medicare Advantage Part C application for 2024, section 3.17 | https://www.cms.gov/files/document/cy-2024-medicare-advantage-part-c-application.pdf-1 | checked 30 Sep 2026 | curl, PDF read |
| 64 | Texas HHSC, Managed Care Uniform Terms and Conditions, version 1.3, section 4.10 | https://www.hhs.texas.gov/sites/default/files/documents/amended-star-health-2.pdf | checked 30 Sep 2026 | curl, PDF read |
| 65 | MeitY, the Digital Personal Data Protection Act 2023 as published in the Gazette, 11 August 2023 | https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf | checked 30 Sep 2026 | curl, PDF read for sections 8 and 17 |
| 66 | American Hospital Association, on the Change Healthcare cyberattack | https://www.aha.org/change-healthcare-cyberattack-underscores-urgent-need-strengthen-cyber-preparedness-individual-health-care-organizations-and | checked 30 Sep 2026 | WebFetch |
| 67 | CBS News, the UnitedHealth Senate hearing, 1 May 2024 | https://www.cbsnews.com/news/unitedhealth-senate-hearing-cyberattack-change-healthcare/ | checked 30 Sep 2026 | WebFetch |
| 68 | UnitedHealth Group, cyberattack status update, 18 March 2024 | https://www.unitedhealthgroup.com/newsroom/2024/2024-03-18-uhg-cyberattack-status-update.html | checked 30 Sep 2026 | WebFetch; not cited now |
| 69 | Skilled Nursing News, the nH Predict lawsuit, 14 February 2025 | https://skillednursingnews.com/2025/02/lawsuit-against-unitedhealth-over-ai-based-denials-of-post-acute-care-moves-ahead/ | checked 30 Sep 2026 | WebFetch |
| 70 | Courthouse News, the Cigna PxDx class claims | https://www.courthousenews.com/judge-advances-class-claims-over-cigna-use-of-automated-algorithm-to-deny-benefits/ | checked 30 Sep 2026 | WebFetch; not cited now |
| 71 | Experian Health, third annual State of Claims survey, 22 September 2025 | https://www.experianplc.com/newsroom/press-releases/2025/experian-health-s-3rd-annual-state-of-claims-survey-finds-denial | checked 30 Sep 2026 | WebFetch; not cited now |
| 72 | JAMIA rapid review citing Dantas et al. on no-show rates | https://pmc.ncbi.nlm.nih.gov/articles/PMC9933067/ | checked 30 Sep 2026 | WebFetch; not cited now, since its range is global and the files give no no-show figure |
| 73 | CMS, 835 flat file, version 5010A1 | https://www.cms.gov/medicare/billing/electronicbillingeditrans/downloads/835-flatfile.pdf | checked 30 Sep 2026 | curl; not cited now |
| 74 | CDC, the A1C test page under diabetes testing | https://www.cdc.gov/diabetes/diabetes-testing/prediabetes-a1c-test.html | checked 30 Sep 2026 | WebFetch |

## Fact by fact

Where: D is the dossier and its section, C is the card and its panel, T is the talk track and its part.

| Fact as the files state it | Where | Source |
|---|---|---|
| US health spending of $5.3 trillion in 2024, $15,474 a person, 18.0 percent of GDP | D2, T facts | 13 |
| Quest: net revenues $11,035 million in 2025, $10,785 million from diagnostic testing; about 244 million requisitions; about 2,400 patient service centres, many inside large retail stores | D2, T2, T facts | 1 |
| Quest's requisition "indicating the test(s) to be performed and the party to be billed for the test(s)" | D2 | 1 |
| Quest: payer shares of 2025 testing volume, revenue and receivables (insurers 43, 39, 27; government 17, 16, 8; clients 37, 31, 43; patients 1, 12, 20); the patient line includes coinsurance and deductibles | D3, T4, T facts | 1 |
| Quest records revenue at the amount it expects to receive, including "the impact of contractual allowances (including payer denials), and patient price concessions" | D3 | 1 |
| Quest: cost of services 66.8 percent, selling, general and administrative 17.8 percent, operating income 14.1 percent ($1,556 million) of 2025 net revenues | D3, T3, T facts | 1 |
| Quest: days sales outstanding "a measure of billing and collection efficiency", 48 days at the end of 2025 and 2024 | D3, T facts | 1 |
| Quest uses AI and automation among its efforts to reduce "denials and patient concessions" and has broadened AI in customer service | D8 | 1 |
| Quest's 10-K names sites in Canada, Finland, Puerto Rico and Mexico and does not mention India | T2, T facts | 1 |
| Quest launched mobile phlebotomy in November 2023 with 5,000 phlebotomists | D2, T facts | 4 |
| Labcorp: revenue $13,951.7 million, diagnostics $10,876.5 million, more than 2,200 patient service centres, more than 7,000 in-office phlebotomists; a leased Bangalore facility for its biopharma laboratory services | D2, T2, T facts | 3 |
| Optum India is UnitedHealth Group's largest Global Capability Centre, with hubs in Gurugram, Noida, Bengaluru, Hyderabad, Pune and Chennai | D2, T2, T facts | 5 |
| Carelon Global Solutions, "born out of one of the largest health plans in the U.S.", in Bengaluru, Hyderabad and Gurugram | D2 | 6 |
| Evernorth, part of The Cigna Group, opened a Hyderabad hub in 2024 | D2 | 7 |
| AGS Health: more than 15,000 revenue-cycle staff; Indian centres including Chennai, Hyderabad and Bengaluru | D2, T2, T facts | 8 |
| Access Healthcare: coding, accounts receivable and denial management; Indian centres including Chennai, Bengaluru and Hyderabad | D2, T2 | 9 |
| Omega Healthcare: coding, billing, accounts receivable follow-up, denials and appeals management | D2 | 10 |
| Employment-based insurance covered 53.5 percent of Americans in 2025; 7.9 percent uninsured all year | D3 | 14 |
| 55 percent of Medicare beneficiaries able to choose were in Medicare Advantage in March 2026 (35.2 of 64.2 million with Parts A and B) | D3 | 15 |
| HealthCare.gov insurers denied 19 percent of in-network claims in 2024, from 3 to 36 percent by insurer | D5, T facts | 17 |
| 837P and 837I, 835, 270 and 271, 276 and 277, 278; version 5010 since 1 January 2012; Medicare sends every electronic remittance as an 835 in 5010 | D3, D6, C4, T1 | 18, 22, 23, 24, 25 |
| CARC descriptions for 1, 2, 16, 29, 50 and 197, quoted exactly; CARC 3, 18, 27, 45 and 97 checked and not printed | D3, T3 | 19 |
| Group codes CO, PR, OA and PI | D3, T3 | 20, 21 |
| CARCs maintained by a committee, RARCs by CMS, both published by X12 and updated three times a year | D3 | 21 |
| Pathology and laboratory CPT codes run from 80000 to 89999 | D3 | 26 |
| CPT maintained by the AMA; its Editorial Panel appointed by the AMA Board of Trustees; Category I, II and III; the descriptions are AMA copyright and none is reproduced | D3, D6, C4 | 27, 33 |
| ICD-10-CM kept by NCHS at CDC; each year's set effective 1 October; the 2027 set published and effective 1 October 2026; E11.9 is "Type 2 diabetes mellitus without complications" | D1, D3, D6, C4, T1 | 28, 29, 30 |
| HCPCS Level II kept by CMS, one letter and four digits, quarterly files; Level I is CPT | D3 | 31 |
| NPI: "a unique 10-digit number used to identify health care providers", through NPPES | D3, D6, C4, T1 | 32 |
| Medicare's 2026 fourth-quarter fee schedule: 85025 $7.77, 80053 $10.56, 83036 $9.71, 80061 $13.39; the file's descriptions are AMA copyright and are not printed; most lab tests paid at the weighted median of private payer rates | D3, D7, T3, T facts | 33 |
| Medicare patients "usually pay nothing for Medicare-covered diagnostic laboratory tests" | D3, D7, T3, T facts | 34 |
| HFMA: net days in AR is net AR over average daily net patient service revenue; initial denial rate is initial denials over claims submitted; clean claim rate counts claims passing edits with no manual intervention over claims accepted into the billing tool; cost to collect is revenue-cycle cost over cash collected | D5, D10, C2 | 35, 36 |
| Revenue cycle management tracks revenue from the first encounter to the final payment of a balance | D12 | 37 |
| Gross charges at the practice's undiscounted rates | D5 | 38 |
| Allowed amount: "The maximum amount a plan will pay for a covered health care service"; deductible: "The amount you pay for covered health care services before your insurance plan starts to pay"; coinsurance and copayment as the patient's share after the deductible; a plan year is "A 12-month period of benefits coverage", which "may not be the same as the calendar year" | D5, D6, C4 | 40 |
| Covered entities are health plans, clearinghouses and providers transmitting in the standard transactions | D7, T6 | 41 |
| PHI in "any form or media, whether electronic, paper, or oral" | D7 | 49 |
| A covered entity designates a privacy official | D7 | 45 |
| Minimum necessary, quoted, with the treatment exception | D7, C5 | 42 |
| De-identification: expert determination or safe harbour, 18 identifiers, dates to the year, three-digit ZIP where the area has more than 20,000 people, ages over 89 grouped | D7, D9, C5, T6 | 44, 50 |
| Business associates include data analysis and billing; subcontractors are business associates; the agreement's terms; direct liability since 2013 | D7, C5, T6 | 41, 43, 51 |
| Security Rule safeguards and required risk analysis; the January 2025 proposal not final on 30 September 2026 | D7 | 46, 55, 56 |
| Breach notice within 60 calendar days; media when more than 500 residents of a state | D7, C5 | 46, 53 |
| At least $73,011 per violation for uncorrected willful neglect, 2025 amounts | D7 | 47 |
| CLIA covers about 320,000 laboratory entities; certification needed for Medicare or Medicaid payment | D7, T2 | 57 |
| Medicare pays nothing for services "not reasonable and necessary for the diagnosis or treatment of illness or injury" | D7 | 58 |
| The ABN, form CMS-R-131, used by providers including independent labs when Medicare payment is expected to be denied | D1, D7 | 59 |
| Medicare claims filed within one calendar year of the date of service | D7, C5 | 48 |
| Prior authorisation within 72 hours urgent and 7 calendar days standard, with a specific denial reason, generally from 1 January 2026, APIs generally from 1 January 2027, for Medicare Advantage, Medicaid and CHIP and their managed-care plans | D7, T facts | 60 |
| CMS on algorithms in Medicare Advantage coverage decisions, 6 February 2024 | D7, D8, T6, T facts | 61 |
| SB 1120's quoted text and its approval on 28 September 2024 | D7 | 62 |
| HHS: "Yes, provided the covered entity (or business associate) enters into a business associate agreement", no requirements specific to data abroad, location in the risk analysis | D7, T6, T facts | 52 |
| The Medicare Advantage and Part D offshore attestation, quoted | D7 | 63 |
| Texas's Medicaid managed-care contract, quoted | D7, T6, T facts | 64 |
| DPDP Act section 17(1)(d), with sections 8(1) and 8(5) still applying | D7 | 65 |
| Change Healthcare: attacked 21 February 2024; 15 billion transactions a year by the AHA's count | D7 | 66 |
| "This particular server did not have MFA on it" | D7 | 67 |
| About 192.7 million individuals, reported to HHS on 31 July 2025 | D7, T facts | 54 |
| nH Predict: allegations; breach-of-contract and good-faith claims allowed to proceed in February 2025 | D8, T6, T facts | 69 |
| HbA1c shows average blood sugar over about three months: "Your red blood cells regenerate roughly every 3 months. That's why the A1C test measures your blood sugar levels from that time period." | D1 | 74 |

## Illustrative and invented numbers

Every number below is illustrative, chosen for easy arithmetic, labelled illustrative where it appears, and neither Kalpa Health's data nor any real company's.

| Number | What it is | Where |
|---|---|---|
| James Carter, 58; $400 of deductible left; 18 hours; 90 patients and 8 home visits; one rejection in 90 claims; three weeks to the remittance | The day in the life | D1, T1 |
| $180 gross charges, $60 allowed, $120 contractual adjustment, $0 from the plan, $60 patient responsibility under group PR and CARC 1 | James's claim | D1, D3, D5, T1, T3 |
| $40 to perform, $5 to bill and collect, $15 contribution, minus $45 if unpaid | James's claim, set at the same shares as the $100 waterfall: 25 of 37 is 67.6 percent and 40 of 60 is 66.7 | D3 |
| $100 gross, $60 contractual, $40 allowed, $3 never collected, $37 net revenue, $25 cost, $12 gross profit, $6.50 other costs, $5.50 operating income | The waterfall; 5.50 of 37 is 14.9 percent against Quest's reported 14.1; 25 of 37 is 67.6 percent against 66.8; 6.50 of 37 is 17.6 percent against 17.8 | D3, C6, T3 |
| $1 of $40 is 2.5 percent; $1 of $5.50 is 18 percent | The leak arithmetic | D3, C6, T3 |
| 12,000 claims; $2,400,000 gross; $960,000 allowed; $1,440,000 contractual; $72,000 expected never collected; $888,000 net revenue; $144,000 patient responsibility | The month at one lab | D5, T5 |
| 1,080 denied of 12,000, 9 percent; $96,000 of $2,400,000, 4 percent | Denial rate by count and by dollars | D5, T5 |
| 10,560 of 12,000 clean, 88 percent | Clean claim rate | D5 |
| $1,332,000 receivable over $29,600 a day, 45 days; 45 to 38 after a write-off | Days in AR | D5, T5 |
| $888,000 over $960,000, 92.5 percent; over $2,400,000, 37 percent | Net collection rate and its trap | D5, T5 |
| An 8 percent chargemaster rise | The gross charges trap | D5, T5 |
| About 144,000 rows, 730 rows a lab | Section 9's sizing | D9 |
| 3,000 claim checks a day at six minutes, 300 staff-hours; 400 a week misread for a month, 1,600 claims at $150, $240,000 | The claim-status agent paragraph | D8 |
| "Days in AR are up to 52" and the glossary's sentences | Section 6's meeting lines | D6 |

## Definitions held the same in every file

| Term | The one definition | Where it appears |
|---|---|---|
| Gross charges | Tests billed at the lab's chargemaster prices | D3, D5, D6, C2, T3 |
| Allowed amount | The most the payer's contract or fee schedule permits for a covered test, which is the payer's share plus the patient's responsibility | D3, D5, D6, C1, C2, T3 |
| Contractual adjustment | Gross charges less the allowed amount | D3, D5, D6, C2, T3 |
| Net revenue | Gross charges less contractual adjustments, less what the lab expects never to collect | D3, D5, C2, T3 |
| Patient responsibility | Deductible plus coinsurance plus copay | D5, D6, C2, T3 |
| Denial rate | Claims denied in full or part on first answer over claims submitted, on one stated basis | D5, C2, T5 |
| Clean claim rate | Claims passing every edit with no manual intervention over claims entered for billing, counted before any claim leaves | D5, D10, C2, T5 |
| Days in AR | Accounts receivable over average net revenue per day | D5, D6, D10, C2, T5 |
| Net collection rate | Payments over gross charges less contractual adjustments, on the same claims once the window closes | D5, C2, T5 |

## Not verified, or verified only through a secondary source

- The net collection rate's formula is the industry's common one, payments over charges less contractual adjustments, as billing firms and practice-management writers publish it; HFMA has no key by that name, and MGMA's glossary page defines gross charges and adjustments but not the rate. The files state the formula without attributing it.
- The CMS memo of 6 February 2024 was read from the AHA's hosted copy; the original was not found on cms.gov.
- SB 1120's effective date and short title were not seen on any source, so the files give only its approval date and quoted text.
- The offshore attestation was read in the Part C application for 2024; the application for 2027 was not read.
- The HHS cloud computing guidance is the only HHS statement found on data held outside the US; it speaks of cloud providers "or any other business associate".
- The final action date of July 2027 for the Security Rule is the agency's projection in the regulatory agenda; the files say only that it was not final on 30 September 2026.
- Whether HHS still applies the lower annual caps it announced for the lower penalty tiers in 2019 was not checked; the files state only the regulation's minimum for uncorrected willful neglect.
- Headcounts for Optum India, Carelon and Evernorth India, R1's Indian cities, Omega's Indian cities and Access Healthcare's current headcount were not found on a primary page, so the files state none of them.
- AGS Health's and Access Healthcare's figures and locations are what each company says of itself on an undated page.
- The Change Healthcare transaction count is the AHA's figure, not UnitedHealth's.
- No industry-wide initial denial rate for hospitals or labs was found in a primary source; the files use KFF's marketplace figure only.
- No US-specific no-show rate was found, and the files give none.
- No Indian operation of Quest was found; the files say only what its 10-K names.
- The AAPC video's content was read from its trailer page; the full video needs a free sign-up.

## Decisions and open points for the orchestrating session

1. **The build-day folders.** `scripts/verify.py` did not allow `study-notes/` or `cheatsheets/` on a build day, and the brief puts the dossier and the card there. Both were added to the build-day set, with a comment naming decision `four-domains`, and `content/README.md` says so.
2. **The sheet builder.** `scripts/build_cheatsheet.py` is the file from branch `w01-domain-retail` unchanged, since main had not touched it since that branch was cut; the two branches merge cleanly on it. Without it the card printed its glossary twice, once as panel 4 and once as the foot strip.
3. **The 45-minute slot.** The Monday day sheet in `trainer/` still runs the India-setting day and has no minutes for the domain story. The talk track says it opens the day before the Programme Head's introduction and that the day sheet sets its minutes; the parallel session rebuilding the Monday pack has to place it.
4. **Length.** The dossier runs to about 10,000 words by the section counter, fences and table rules excluded, against the reference's 6,000 to 8,000 and the retail dossier's 9,062 by the same counter. Section 3 carries the codes and transactions the brief lists, and section 7 the offshore question, which retail had no equivalent of.
5. **The domain's volume tree.** The dossier teaches the charge-to-cash tree and leaves the lab's volume tree, the transfer of the Week 1 revenue tree, to the groups, since it is sub-problem 1.
6. **No-show rate.** The files define a no-show as a term only in passing and give no formula for its rate, since sub-problem 4's trap sits in its denominator.

## The plant check

The dossier and card are STUDENT files read on Build 1 Monday, before any group has found anything. Checked against `docs/detailing/W03_build1_spine.md` and client zero's Build 1 seeds:

- No Kalpa Health dataset value appears: no growth reading other than the story's 5 against 18, no count of tests, bookings or visits, no invoice or payment figure, no clinic, city or metro, no campaign figure.
- None of the five sub-problems is walked through, and no file draws Kalpa Health's volume tree.
- None of the Build 1 traps is taught or staged in any file: no system migration or export difference, no feed keyed in its own format, no duplicate or double posting, no denominator for a no-show rate or anything about walk-ins, no offer or campaign compared across groups or cities, no corporate contract and no package counted as components.
- Section 9's problems are ones the five sub-problems do not pose: denial prediction, work-queue ranking, coding assistance, patient estimates, de-identification and volume forecasting. Section 8's no-show row describes prediction only.
- The glossary's one sentence about 837s and 835s says nothing about matching them.
- The talk track names what must not be previewed only as a warning to the trainer, without values or mechanisms.

## The depth loop

| Pass | Who | What it did |
|---|---|---|
| 1 | The builder | Read the brief, the reference, client zero, the spine, the revamp prompt and the retail model; three research agents checked the regulation, the codes and transactions, and the companies and market against primary sources |
| 2 | The builder, domain pass | Every section opened on a scene before any term; the payer mix, the codes, the offshore limits and the real companies added from the research; definitions set to HFMA's where HFMA has one |
| 3 | The builder, problem-first pass | Section 9's six problems each with options, sizes, the best fit and the fact that would change it; sub-problem material removed or never written |
| 4 | A fresh rigor reviewer, read-only | Recorded below once run |
| 5 | A fresh pedagogy and language reviewer, read-only | Recorded below once run |

## Tools

Python 3 for extraction and word counts; pdftotext for PDFs; curl with a declared or browser user agent where the page reader was refused, and the eCFR and Federal Register APIs; mermaid-cli and weasyprint through `scripts/build_cheatsheet.py`, run as `python3 scripts/build_cheatsheet.py content/W03/D1/cheatsheets/C2_W03_D01_us_healthcare_domain_card_STUDENT.md --verified "30 Sep 2026" --max-pages 1`, which chose three columns, one page and an anchor sized for 7pt labels; the llm-tic-scrubber scanner on every markdown file.

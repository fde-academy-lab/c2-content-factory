# Data dictionary: the ten Kalpa Health files

Written by Dr Menon's data team for the GCC's data and AI team. Each file is described the way its
exporting system describes it: what the system says the file holds, how many rows came out, and what
each column is meant to carry. Row counts exclude the header line. Sample values are copied from the
files.

Kalpa Health and everyone in it are fictional, and every name, price and number in these files is
synthetic.

---

## Two things the data team already knows

1. **Two metros changed booking systems in Q3.**
2. **The posting system has a different id format from the claims export.**

The team has not checked anything beyond these two. What else the files hold is yours to find.

---

## The files at a glance

Every file is a comma-separated text file with a header row, in `data/`, named
`C2_W03_D01_{file}_STUDENT.csv`.

| File | Exporting system | What the system says it holds | Rows |
|---|---|---|---|
| `patients` | The patient register | One row per registered patient | 6,700 |
| `sites` | The site list | One row per site | 18 |
| `test_catalogue` | The price list | One row per test or panel on sale | 16 |
| `bookings_legacy` | The booking system in use since before Q2 | One row per booking, Q2 and Q3, every metro | 11,729 |
| `bookings_newsys` | The new booking system | One row per booking taken in the new system | 153 |
| `booking_tests` | The booking system's line table | One row per test, panel or panel component on a booking | 51,456 |
| `claims` | The billing export | One row per claim billed, Q2 and Q3 | 11,356 |
| `remittances` | The posting system: payers' remittances and the cash desks | One row per posting recorded | 11,343 |
| `appointments` | The patient service centres' visit register | One row per visit to a patient service centre, Q3 | 7,133 |
| `campaign` | The marketing team's offer list | One row per patient offered free at-home collection | 2,381 |

Q2 is April to June 2026 and Q3 is July to September 2026, the calendar quarters Kalpa Health
reports in.

---

## patients

The patient register. One row per patient.

| Column | Type | What it carries | Sample values |
|---|---|---|---|
| `patient_id` | text | The patient's id in the register | `P-000001`, `P-002450` |
| `metro` | text | The metro the patient is registered in | `Dallas`, `New York` |
| `age_band` | text | The patient's age band | `18-34`, `50-64`, `65+` |
| `sex` | text | Sex as recorded at registration | `F`, `M` |
| `payer_type` | text | Who pays for the patient's tests | `commercial`, `Medicare`, `Medicaid`, `self-pay` |
| `employer_account` | text | The employer account that books this patient, where one does; empty otherwise | empty |

## sites

The site list. One row per site.

| Column | Type | What it carries | Sample values |
|---|---|---|---|
| `site_code` | text | The site's code, as the booking system in use since before Q2 writes it | `KH-DAL-01`, `KH-PHX-02` |
| `metro` | text | The metro the site is in | `Phoenix`, `Philadelphia` |
| `kind` | text | `laboratory` or `patient service center` | `laboratory`, `patient service center` |
| `new_system_code` | text | The site's code in the new booking system, for sites that use it; empty otherwise | `ORD-01`, `PHL-02` |

## test_catalogue

The price list. Twelve single tests and four panels.

| Column | Type | What it carries | Sample values |
|---|---|---|---|
| `code` | text | The test or panel code | `T-CBC`, `PNL-WEL` |
| `name` | text | The name on the price list | `Complete blood count`, `Whole-body wellness panel` |
| `list_price_usd` | number, dollars | The list price of one test or one panel | `45`, `299` |
| `kind` | text | `test` or `panel` | `test`, `panel` |

## bookings_legacy

The booking system Kalpa Health has used since before Q2. The export covers bookings dated from
1 April to 30 September 2026.

| Column | Type | What it carries | Sample values |
|---|---|---|---|
| `booking_id` | text | The booking's id in this system | `KB0000001`, `KB0003502` |
| `patient_id` | text | The patient, as the register writes the id | `P-001368`, `P-005866` |
| `site_code` | text | The site that took the booking | `KH-PHX-01`, `KH-NYC-02` |
| `metro` | text | The site's metro | `Phoenix`, `New York` |
| `booking_date` | date, `YYYY-MM-DD` | The day the booking was made | `2026-05-27`, `2026-07-14` |
| `channel` | text | How the patient booked | `walk-in`, `online`, `phone`, `at-home` |
| `status` | text | Where the booking stands | `completed`, `cancelled` |
| `updated_at` | date and time, `YYYY-MM-DD HH:MM` | When the row was last changed | `2026-05-27 18:40` |

## bookings_newsys

The new booking system. It writes its own ids, its own site codes, its own channel and status codes,
and dates month first.

| Column | Type | What it carries | Sample values |
|---|---|---|---|
| `bkg_ref` | text | The booking's id in the new system | `NB/ORD/000001`, `NB/PHL/000012` |
| `patient` | text | The patient's number, without the register's prefix | `004857`, `004699` |
| `site` | text | The site, in the new system's codes (see `sites.new_system_code`) | `ORD-01`, `PHL-03` |
| `metro` | text | The site's metro | `Chicago`, `Philadelphia` |
| `created` | date, `MM/DD/YYYY` | The day the booking was made | `09/21/2026`, `09/20/2026` |
| `channel` | text | How the patient booked | `WALKIN`, `WEB`, `CALL`, `MOBILEDRAW` |
| `state` | text | Where the booking stands | `DONE`, `CXL` |

## booking_tests

The booking system's line table: what was booked on each booking, in both systems. A test booked on
its own is one `test` row. A panel is one `panel` row carrying the panel price, followed by one
`component` row for each test inside it, priced at zero.

| Column | Type | What it carries | Sample values |
|---|---|---|---|
| `booking_id` | text | The booking, as either system writes its id | `KB0000001`, `NB/ORD/000001` |
| `test_code` | text | The test, or the panel on a `panel` row | `T-URN`, `PNL-DB` |
| `panel_code` | text | The panel this row belongs to; empty for a test booked on its own | `PNL-WEL`, `PNL-AGE` |
| `quantity` | number | How many of this test or panel were booked | `1` |
| `price_each` | number, dollars | The price charged for one | `30`, `299`, `0` |
| `line` | text | `test`, `panel` or `component` | `test`, `panel`, `component` |

## claims

The billing export. One claim per completed booking, billed to a payer at list price.

| Column | Type | What it carries | Sample values |
|---|---|---|---|
| `claim_id` | text | The claim's id | `KH-CLM-000001`, `KH-CLM-000002` |
| `booking_id` | text | The booking billed, as either system writes its id | `KB0000001`, `NB/PHL/000001` |
| `service_date` | date, `YYYY-MM-DD` | The day of the service billed | `2026-04-01` |
| `metro` | text | The metro of the site that did the work | `Dallas`, `Philadelphia` |
| `payer_type` | text | The kind of payer billed | `commercial`, `Medicare`, `Medicaid`, `self-pay` |
| `payer_id` | text | The payer billed, in Kalpa's own ids | `COM-C`, `MEDICARE`, `MEDICAID-TX`, `SELF` |
| `billed_amount` | number, dollars | The claim total at list price | `85`, `299`, `149` |
| `line_items` | number | How many lines the claim carries | `1`, `3` |
| `employer_account` | text | The employer account billed, where the claim goes to one; empty otherwise | empty |
| `denial_category` | text | The payer's reason, once a denial has been posted back; empty otherwise | `medical necessity`, `timely filing` |

## remittances

The posting system. Payers' remittances arrive as electronic remittance files (ERA); card and cash
payments come from the patient service centres' desks. Every posting is recorded as its own row
against the claim it is for.

| Column | Type | What it carries | Sample values |
|---|---|---|---|
| `posting_id` | text | The posting's id in the system | `PST0000001`, `PST0000002` |
| `claim_ref` | text | The claim the posting is for, as the payer or the desk recorded it | `000002`, `000003` |
| `payer_id` | text | Who sent the money, in Kalpa's own ids | `COM-C`, `MEDICARE`, `SELF` |
| `channel` | text | How the posting arrived | `ERA`, `card`, `cash` |
| `billed_amount` | number, dollars | The claim's billed amount, as the payer or the desk recorded it | `85`, `299` |
| `posting` | text | `payment` for money received, `denial` for a claim the payer refused, `reversal` for money taken back | `payment`, `denial`, `reversal` |
| `allowed_amount` | number, dollars | What the payer allows for the claim | `23.80`, `140.53` |
| `paid_amount` | number, dollars | The amount this posting moved | `23.80`, `112.42` |
| `patient_responsibility` | number, dollars | What the patient owes on the claim | `0.00`, `28.11` |
| `adjustment_amount` | number, dollars | The part of the billed amount neither paid nor owed | `61.20`, `158.47` |
| `adjustment_group` | text | The adjustment's group code, as the remittance carries it | `CO`, `OA` |
| `reason_category` | text | The adjustment's reason | `contractual adjustment`, `medical necessity` |
| `posted_at` | date and time, `YYYY-MM-DD HH:MM` | When the system recorded the posting | `2026-05-07 17:18` |

## appointments

The patient service centres' visit register for Q3, all twelve patient service centres. Laboratories
do not keep one.

| Column | Type | What it carries | Sample values |
|---|---|---|---|
| `appointment_id` | text | The visit's id in the register | `AP000001`, `AP000002` |
| `site_code` | text | The patient service centre | `KH-DAL-02`, `KH-PHI-03` |
| `visit_date` | date, `YYYY-MM-DD` | The day of the visit, or of the booked slot | `2026-07-01` |
| `kind` | text | `scheduled` for a booked slot, `walk-in` for a patient who came without one | `scheduled`, `walk-in` |
| `attended` | text | `Y` if the patient was seen, `N` if not | `Y`, `N` |

## campaign

The marketing team's list for the free at-home collection offer. One row per patient the offer was
sent to.

| Column | Type | What it carries | Sample values |
|---|---|---|---|
| `patient_id` | text | The patient, as the register writes the id | `P-000002`, `P-000003` |
| `metro` | text | The patient's registered metro | `Dallas`, `Phoenix` |
| `offered_on` | date, `YYYY-MM-DD` | The day the offer was sent | `2026-07-22`, `2026-08-04` |
| `took_up` | text | `Y` if the patient used a free collection, `N` if not | `Y`, `N` |

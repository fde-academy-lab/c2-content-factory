# Data dictionary: the ten Kalpa Health files

Written by Dr Menon's data team for the GCC's data and AI team. Each file is described the way its
exporting system describes it: what the system says the file holds, how many rows came out, and what
each column is meant to carry. Row counts exclude the header line. Sample values are copied from the
files.

Kalpa Health and everyone in it are fictional, and every name, price and number in these files is
synthetic.

---

## Two things the data team already knows

1. **Two cities changed booking systems in Q2.**
2. **The payment feed has a different id format from the invoice export.**

The team has not checked anything beyond these two. What else the files hold is yours to find.

---

## The files at a glance

Every file is a comma-separated text file with a header row, in `data/`, named
`C2_W03_D01_{file}_STUDENT.csv`.

| File | Exporting system | What the system says it holds | Rows |
|---|---|---|---|
| `patients` | The patient register | One row per registered patient | 6,700 |
| `clinics` | The site list | One row per site | 18 |
| `test_catalogue` | The price list | One row per test or package on sale | 16 |
| `bookings_legacy` | The booking system in use since before Q1 | One row per booking, Q1 and Q2, every city | 11,729 |
| `bookings_newsys` | The new booking system | One row per booking taken in the new system | 153 |
| `booking_tests` | The booking system's line table | One row per test, package or package component on a booking | 51,456 |
| `invoices` | The billing export | One row per invoice raised, Q1 and Q2 | 11,356 |
| `payments` | The payment feed: gateway and cash desks | One row per payment or refund recorded | 11,289 |
| `appointments` | The walk-in clinics' visit register | One row per visit to a walk-in clinic, Q2 | 7,133 |
| `campaign` | The marketing team's offer list | One row per patient offered free home collection | 2,381 |

Q1 is April to June 2026 and Q2 is July to September 2026, the first two quarters of Kalpa Health's
financial year.

---

## patients

The patient register. One row per patient.

| Column | Type | What it carries | Sample values |
|---|---|---|---|
| `patient_id` | text | The patient's id in the register | `P-000001`, `P-002450` |
| `city` | text | The city the patient is registered in | `Bengaluru`, `Delhi` |
| `age_band` | text | The patient's age band | `18-29`, `45-59`, `60+` |
| `sex` | text | Sex as recorded at registration | `F`, `M` |
| `corporate_account` | text | The corporate account that books this patient, where one does; empty otherwise | empty |

## clinics

The site list. One row per site.

| Column | Type | What it carries | Sample values |
|---|---|---|---|
| `clinic_code` | text | The site's code, as the booking system in use since before Q1 writes it | `KH-BLR-01`, `KH-MUM-02` |
| `city` | text | The city the site is in | `Mumbai`, `Pune` |
| `kind` | text | `laboratory` or `walk-in clinic` | `laboratory`, `walk-in clinic` |
| `new_system_code` | text | The site's code in the new booking system, for sites that use it; empty otherwise | `MAA-01`, `PNQ-02` |

## test_catalogue

The price list. Twelve single tests and four packages.

| Column | Type | What it carries | Sample values |
|---|---|---|---|
| `code` | text | The test or package code | `T-CBC`, `PKG-FB` |
| `name` | text | The name on the price list | `Complete blood count`, `Full body checkup` |
| `list_price` | number, rupees | The list price of one test or one package | `350`, `2999` |
| `kind` | text | `test` or `package` | `test`, `package` |

## bookings_legacy

The booking system Kalpa Health has used since before Q1. The export covers bookings dated from
1 April to 30 September 2026.

| Column | Type | What it carries | Sample values |
|---|---|---|---|
| `booking_id` | text | The booking's id in this system | `KB0000001`, `KB0003502` |
| `patient_id` | text | The patient, as the register writes the id | `P-001368`, `P-005866` |
| `clinic_code` | text | The site that took the booking | `KH-MUM-01`, `KH-DEL-02` |
| `city` | text | The site's city | `Mumbai`, `Delhi` |
| `booking_date` | date, `YYYY-MM-DD` | The day the booking was made | `2026-05-27`, `2026-07-14` |
| `channel` | text | How the patient booked | `walk-in`, `app`, `phone`, `home-collection` |
| `status` | text | Where the booking stands | `completed`, `cancelled` |
| `updated_at` | date and time, `YYYY-MM-DD HH:MM` | When the row was last changed | `2026-05-27 18:40` |

## bookings_newsys

The new booking system. It writes its own ids, its own site codes, its own channel and status codes,
and dates day first.

| Column | Type | What it carries | Sample values |
|---|---|---|---|
| `bkg_ref` | text | The booking's id in the new system | `NB/MAA/000001`, `NB/PNQ/000012` |
| `patient` | text | The patient's number, without the register's prefix | `004857`, `004699` |
| `centre` | text | The site, in the new system's codes (see `clinics.new_system_code`) | `MAA-01`, `PNQ-02` |
| `city` | text | The site's city | `Chennai`, `Pune` |
| `created` | date, `DD/MM/YYYY` | The day the booking was made | `21/09/2026`, `26/09/2026` |
| `channel` | text | How the patient booked | `WALKIN`, `APP`, `CALL`, `HOMEVISIT` |
| `state` | text | Where the booking stands | `DONE`, `CXL` |

## booking_tests

The booking system's line table: what was booked on each booking, in both systems. A test booked on
its own is one `test` row. A package is one `package` row carrying the package price, followed by one
`component` row for each test inside it, priced at zero.

| Column | Type | What it carries | Sample values |
|---|---|---|---|
| `booking_id` | text | The booking, as either system writes its id | `KB0000001`, `NB/MAA/000001` |
| `test_code` | text | The test, or the package on a `package` row | `T-URN`, `PKG-DB` |
| `package_code` | text | The package this row belongs to; empty for a test booked on its own | `PKG-FB`, `PKG-SC` |
| `quantity` | number | How many of this test or package were booked | `1` |
| `price_each` | number, rupees | The price charged for one | `200`, `2999`, `0` |
| `line` | text | `test`, `package` or `component` | `test`, `package`, `component` |

## invoices

The billing export. One invoice per completed booking, numbered in the financial year's series.

| Column | Type | What it carries | Sample values |
|---|---|---|---|
| `invoice_no` | text | The invoice number | `KH/26-27/000001`, `KH/26-27/000002` |
| `booking_id` | text | The booking invoiced, as either system writes its id | `KB0000001`, `NB/PNQ/000001` |
| `invoice_date` | date, `YYYY-MM-DD` | The day the invoice was raised | `2026-04-01` |
| `city` | text | The city of the site that did the work | `Bengaluru`, `Hyderabad` |
| `amount` | number, rupees | The invoice total | `470`, `2999`, `1550` |
| `line_items` | number | How many lines the invoice carries | `1`, `3` |
| `corporate_account` | text | The corporate account billed, where the invoice goes to one; empty otherwise | empty |

## payments

The payment feed. Card and UPI payments come from the gateway; cash comes from the clinics' cash
desks. A refund is recorded as its own row.

| Column | Type | What it carries | Sample values |
|---|---|---|---|
| `payment_id` | text | The payment's id in the feed | `PAY0000001`, `PAY0000002` |
| `invoice_ref` | text | The invoice the payment is for, as the gateway or the cash desk recorded it | `000001`, `000002` |
| `method` | text | How the patient paid | `UPI`, `card`, `cash` |
| `amount` | number, rupees | The amount moved | `470`, `2999` |
| `paid_at` | date and time, `YYYY-MM-DD HH:MM` | When the feed recorded the payment | `2026-04-05 12:54` |
| `status` | text | `success` for a payment, `refund` for money returned | `success`, `refund` |

## appointments

The walk-in clinics' visit register for Q2, all twelve walk-in clinics. Laboratories do not keep one.

| Column | Type | What it carries | Sample values |
|---|---|---|---|
| `appointment_id` | text | The visit's id in the register | `AP000001`, `AP000002` |
| `clinic_code` | text | The walk-in clinic | `KH-BLR-02`, `KH-PUN-03` |
| `visit_date` | date, `YYYY-MM-DD` | The day of the visit, or of the booked slot | `2026-07-01` |
| `kind` | text | `scheduled` for a booked slot, `walk-in` for a patient who came without one | `scheduled`, `walk-in` |
| `attended` | text | `Y` if the patient was seen, `N` if not | `Y`, `N` |

## campaign

The marketing team's list for the free home-collection offer. One row per patient the offer was sent
to.

| Column | Type | What it carries | Sample values |
|---|---|---|---|
| `patient_id` | text | The patient, as the register writes the id | `P-000002`, `P-000003` |
| `city` | text | The patient's registered city | `Bengaluru`, `Mumbai` |
| `offered_on` | date, `YYYY-MM-DD` | The day the offer was sent | `2026-07-22`, `2026-08-04` |
| `took_up` | text | `Y` if the patient used a free collection, `N` if not | `Y`, `N` |

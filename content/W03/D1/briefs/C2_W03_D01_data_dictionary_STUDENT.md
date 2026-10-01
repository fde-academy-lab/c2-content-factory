# What does each of the ten Kalpa Health files hold, row by row and column by column?

Written by Dr Priya Menon's data team at Kalpa Health for the data and AI team at Kalpa's Global
Capability Centre (GCC) in Bengaluru. Kalpa Health is a US diagnostics business: a laboratory and
two patient service centres, where patients have blood drawn, in each of six US metro areas, with
bookings taken at all eighteen sites, billing patients' payers in dollars. It is fictional, and every name, price and number in these files is
synthetic, so no real patient's information is in them.

Every file is the export taken on Friday 16 October 2026, and nothing in any file is dated after
that day. Q2 means April to June 2026 and Q3 means July to September 2026, the calendar quarters
Kalpa Health reports in.

**Who needs the answer.** Every group, before it counts anything. A group that mistakes what one row
of a file stands for counts the wrong thing all week, and Dr Menon carries the wrong number to her
board.

**The questions on the way.** Which system wrote each file, and what period does it cover? What is
one row of each file? What does each column carry, and in what unit? Which columns point from one
file to another? What has the data team not checked?

---

## Which system wrote each file, and what does one row of it stand for?

**Who needs the answer.** Every group, at its first move. The grain of a file, what one row stands
for, decides what a count of its rows means, and a count of the wrong grain reaches Dr Menon as a
count of patients, bookings or tests that it is not.

**The questions on the way.** Which system exported each file? What does that system say one row
is? How many rows came out, and over which dates?

Every file is a comma-separated text file with a header row, in `data/`, named
`C2_W03_D01_{file}_STUDENT.csv`. Row counts exclude the header line. The middle column says what
each system says one row is, and the data team has not checked that the files keep to it.

| File | The system that wrote it | One row, as the system describes it | Rows | What it covers |
|---|---|---|---|---|
| `patients` | The patient register | One registered patient | 6,700 | Everyone registered when the file was exported |
| `sites` | The site list | One site, a laboratory or a patient service centre | 18 | Every Kalpa Health site |
| `test_catalogue` | The price list | One test or panel on sale | 16 | Twelve single tests and four panels |
| `bookings_legacy` | The booking system in use since before Q2 | One booking | 11,729 | Bookings dated 1 April to 30 September 2026 |
| `bookings_newsys` | The new booking system | One booking taken in the new system | 153 | Every booking the new system held at the export |
| `booking_tests` | The booking systems' line table | One test, one panel, or one test inside a panel, on a booking | 51,456 | The bookings in both booking files |
| `claims` | The billing system | One claim, the bill for one completed booking | 11,356 | Services dated 1 April to 30 September 2026 |
| `remittances` | The posting system | One posting: money received, a denial, or money taken back | 11,343 | Postings recorded from 2 April to 16 October 2026 |
| `appointments` | The patient service centres' visit register | One entry in a centre's visit register | 7,133 | Visits dated 1 July to 30 September 2026, Q3 only |
| `campaign` | Marketing's offer list | One patient sent the free at-home collection offer | 2,381 | Offers sent from 15 July to 4 August 2026 |

Laboratories keep no visit register, so `appointments` covers the twelve patient service centres
only.

---

## What does each column carry, and in what unit?

**Who needs the answer.** Every group, before it sums or compares a column. A column read in the
wrong unit or with the wrong meaning moves every number built on it, and nobody downstream can see
the mistake.

**The questions on the way.** What does each column of each file mean? Which columns are money, and
in which currency? Which columns are dates? Which codes need a word of explanation before they can be
read?

Each table below gives a column's name, its type as the system means to write it, and what it
carries. Every money column is in US dollars.

### What does the patient register hold for each patient?

| Column | Type | What it carries |
|---|---|---|
| `patient_id` | text | The patient's id in the register |
| `metro` | text | The metro area the patient is registered in |
| `age_band` | text | The patient's age band |
| `sex` | text | Sex as recorded at registration |
| `payer_type` | text | Who pays for the patient's tests: a commercial plan, Medicare, Medicaid or the patient (self-pay) |
| `employer_account` | text | The employer account that books for this patient, where there is one; empty otherwise |

### What does the site list say about each site?

| Column | Type | What it carries |
|---|---|---|
| `site_code` | text | The site's code in the booking system in use since before Q2, written `KH-` then a three-letter metro code then a two-digit number |
| `metro` | text | The metro area the site is in |
| `kind` | text | Whether the site is a laboratory or a patient service centre |
| `new_system_code` | text | The site's code in the new booking system, for a site that has one; empty otherwise |

### What does the price list charge for each test and panel?

| Column | Type | What it carries |
|---|---|---|
| `code` | text | The test or panel code, Kalpa Health's own; a code starting `T-` is a single test and one starting `PNL-` a panel |
| `name` | text | The name on the price list |
| `list_price_usd` | dollars | The list price of one test or one panel |
| `kind` | text | Whether the line is a single test or a panel |

A panel is several tests ordered and priced under one name. Its list price is the panel's own price,
which is not the sum of its tests' prices.

### What does the older booking system record for each booking?

| Column | Type | What it carries |
|---|---|---|
| `booking_id` | text | The booking's id in this system |
| `patient_id` | text | The patient, as the register writes the id |
| `site_code` | text | The site that took the booking |
| `metro` | text | The site's metro area |
| `booking_date` | date | The day the booking was made |
| `channel` | text | How the patient booked: walking in, online, by phone, or for a collection at home |
| `status` | text | Whether the booking was completed or cancelled |
| `updated_at` | date and time | When the row was last changed |

### What does the new booking system record for each booking?

The new system writes its own ids, its own site codes and its own channel and status codes.

| Column | Type | What it carries |
|---|---|---|
| `bkg_ref` | text | The booking's id in the new system |
| `patient` | text | The patient's register number, as the new system writes it |
| `site` | text | The site, in the new system's codes; the site list's `new_system_code` column carries the same codes |
| `metro` | text | The site's metro area |
| `created` | date | The day the booking was made |
| `channel` | text | How the patient booked, in the new system's codes for walking in, online, by phone and a collection at home |
| `state` | text | Whether the booking was completed or cancelled, in the new system's codes |

### Which tests and panels sit on each booking?

The line table serves both booking systems. A test booked on its own is one row whose `line` is
`test`. A panel is one row whose `line` is `panel`, carrying the panel's price, followed by one row
whose `line` is `component` for each test inside it, priced at zero.

| Column | Type | What it carries |
|---|---|---|
| `booking_id` | text | The booking, as either booking system writes its id |
| `test_code` | text | The test on a `test` or `component` row, or the panel on a `panel` row |
| `panel_code` | text | The panel a `panel` or `component` row belongs to; empty for a test booked on its own |
| `quantity` | whole number | How many of this test or panel were booked |
| `price_each` | dollars | The price charged for one |
| `line` | text | `test`, `panel` or `component`, as described above |

### What does each claim bill, and to whom?

A claim is the bill Kalpa Health sends to whoever pays for a completed booking: list prices, plus a
collection fee where a phlebotomist drew the blood at home and the fee was charged. The payer
answers with a remittance, which the posting system records.

| Column | Type | What it carries |
|---|---|---|
| `claim_id` | text | The claim's id in the billing system |
| `booking_id` | text | The booking billed, as either booking system writes its id |
| `service_date` | date | The day of the service billed |
| `metro` | text | The metro area of the site that did the work |
| `payer_type` | text | The kind of payer billed |
| `payer_id` | text | The payer billed, in Kalpa Health's own payer ids, since no real payer is named |
| `billed_amount` | dollars | The claim's total: the list prices of what was booked, plus any collection fee |
| `line_items` | whole number | How many lines the claim carries, a collection fee line among them where one was charged |
| `employer_account` | text | The employer account billed, where the claim goes to one; empty otherwise |
| `denial_category` | text | The payer's reason, once a denial has been posted back; empty otherwise |

### What does each posting record, and against which claim?

Payers' remittances arrive as electronic remittance files, which the posting system calls ERA; card
and cash payments come from the patient service centres' desks. The system records every posting as
a row of its own against the claim it is for.

| Column | Type | What it carries |
|---|---|---|
| `posting_id` | text | The posting's id in the posting system |
| `claim_ref` | text | The claim the posting is for |
| `payer_id` | text | Who sent the money or the decision, in Kalpa Health's own payer ids |
| `channel` | text | How the posting arrived: an electronic remittance, a card payment or a cash payment |
| `billed_amount` | dollars | The claim's billed amount, as the posting carries it |
| `posting` | text | `payment` for money received, `denial` for a claim the payer refused, `reversal` for money taken back |
| `allowed_amount` | dollars | What the payer's contract allows for the claim, its share and the patient's together |
| `paid_amount` | dollars | The money this posting moved; a reversal moves money back, so it is negative |
| `patient_responsibility` | dollars | What the patient owes on the claim |
| `adjustment_amount` | dollars | The part of the billed amount that neither the payer pays nor the patient owes |
| `adjustment_group` | text | The remittance's group code for that part: `CO`, a contractual obligation Kalpa Health absorbs; `PR`, the patient's responsibility; `OA`, another adjustment; `PI`, a reduction the payer made |
| `reason_category` | text | The adjustment's reason in words: a contractual adjustment, or one of the seven denial categories below |
| `posted_at` | date and time | When the posting system recorded the posting |

### What does the visit register record for each visit to a centre?

| Column | Type | What it carries |
|---|---|---|
| `appointment_id` | text | The visit's id in the register |
| `site_code` | text | The patient service centre |
| `visit_date` | date | The day of the visit, or of the booked slot |
| `kind` | text | `scheduled` for a slot booked ahead, `walk-in` for a patient who came without one |
| `attended` | Y or N | `Y` if the patient was seen, `N` if not |

### Whom did marketing send the at-home offer to, and who used it?

The offer was a free collection at home: a phlebotomist visits the patient and draws the sample
there, with the visit's fee waived.

| Column | Type | What it carries |
|---|---|---|
| `patient_id` | text | The patient, as the register writes the id |
| `metro` | text | The patient's registered metro area |
| `offered_on` | date | The day the offer was sent |
| `took_up` | Y or N | `Y` if the patient accepted the offer, `N` if not |

### What do the seven denial categories mean?

Kalpa Health's systems name every denial by one of seven categories, modelled on the claim
adjustment reason codes that US payers put on a remittance. The domain dossier's section 6 gives a
typical code for each and what the lab does next.

| Category | What the payer is saying |
|---|---|
| eligibility or coverage | The patient was not covered by this payer for this service on that day |
| missing or invalid information | The claim lacks information or carries an error |
| medical necessity | The payer does not consider the test necessary for the patient's condition |
| prior authorization | The payer requires approval before the service, and none was obtained |
| non-covered service | The patient's plan does not cover this service |
| duplicate claim | The payer has already received this claim |
| timely filing | The claim reached the payer after its filing deadline |

---

## Which columns point from one file to another?

**Who needs the answer.** Every group that combines two files, since almost every question does. A
group that joins on the wrong pair of columns, or never checks what its join kept and dropped, puts a
number in front of Dr Menon that no file supports.

**The questions on the way.** Which column in each file names a patient, a site, a booking, a claim
or a test? Which pairs of columns are meant to refer to the same thing?

Each row below pairs columns that the systems mean to refer to the same thing. Whether every value
in one finds its partner in the other is not something the data team has checked.

| The thing | Where it is defined | Where other files point to it |
|---|---|---|
| A patient | `patients.patient_id` | `bookings_legacy.patient_id`, `bookings_newsys.patient`, `campaign.patient_id` |
| A site | `sites.site_code`, and `sites.new_system_code` for the new system | `bookings_legacy.site_code`, `appointments.site_code`, and `bookings_newsys.site` |
| A booking | `bookings_legacy.booking_id` and `bookings_newsys.bkg_ref` | `booking_tests.booking_id`, `claims.booking_id` |
| A claim | `claims.claim_id` | `remittances.claim_ref` |
| A test or panel | `test_catalogue.code` | `booking_tests.test_code`, `booking_tests.panel_code` |
| A payer | `claims.payer_id` | `remittances.payer_id` |

---

## What has the data team not checked?

**Who needs the answer.** Every group, before it relies on these descriptions. The data team wrote down what
each system says it exports, and Dr Menon's heads have already been given different numbers from
these same systems.

**The questions on the way.** What did the data team check? What is left for your group?

The data team checked one thing: that each file opens and its row count is the one in the first
table. It has not checked any file against this page. Whether every row is what its system says it
is, whether every value is in the type its column says, and whether every pointer finds its partner,
are yours to find, and profiling each file before you count from it, the Week 1 Wednesday move, is
how a group finds them. Every cleaning or matching call your group makes goes in the decisions log,
`briefs/C2_W03_D01_decisions_log_STUDENT.xlsx`, with the rows it touched and its reason.

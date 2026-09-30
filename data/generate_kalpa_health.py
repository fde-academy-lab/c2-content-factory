"""Write Build 1's Kalpa Health data pack, deterministically, from one seed.

    python3 data/generate_kalpa_health.py --out content/W03/D1/data --stem C2_W03_D01
    python3 data/generate_kalpa_health.py --contract     # generate in memory and assert every plant
    python3 data/generate_kalpa_health.py --witness      # print the numbers the TRAINER files quote

Kalpa Health is a US diagnostics business (client zero section 1c, addendum health-us-facing, set by
the requester on 30 September 2026): its laboratories and patient service centres test US patients
in six US metro areas and bill US payers in dollars, and its analytics and revenue-cycle work runs
from Kalpa's GCC in Bengaluru. Its COO, Dr Priya Menon, wants to know why test volumes grew 5
percent against a plan of 18. The tracker row names a re-labelled public source for Build 1's data
without naming which; on 29 September 2026 the requester chose a synthetic pack instead, so the
files are safe in a public repository and every learner holds the same bytes.

Everything here is synthetic. Every list price is a synthetic Kalpa list price in the range a US
lab's price list carries, and no real payer's rate or fee schedule is used; payers are named by type
with Kalpa's own ids. Test codes are Kalpa's internal codes with plain names, and no CPT code or
descriptor text appears. A patient is a synthetic id with a metro, an age band, a sex and a payer
type, and carries no name, date of birth, address or anything else that reads as protected health
information.

The two quarters are calendar Q2 2026 (April to June) and calendar Q3 2026 (July to September), the
way a US business reports, and every file, key and message says Q2 and Q3 in that sense.

Ten files, one per system Dr Menon's team exports, each messy in the way that system is:

  patients         one row per patient: metro, age band, sex, payer type, and any employer account
  sites            one row per site, laboratory or patient service centre, with each system's code
  test_catalogue   every test and panel with its synthetic list price in dollars
  bookings_legacy  the old booking system, every metro, ISO dates; re-exported once mid-quarter
  bookings_newsys  the new system two metros moved to in Q3, with its own ids, codes and US dates
  booking_tests    one row per test on a booking; a panel is a header row and its component tests
  claims           the billing system's export: one claim per completed booking, billed to a payer
                   at list price, with the denial category once a denial has been posted back
  remittances      the posting system: payer remittances (ERA) and patient payments at the desk,
                   keyed by a claim reference in its own format, each with the allowed and paid
                   amounts, the patient's share, and an adjustment with its group code (CO, OA or
                   PR) and a reason category
  appointments     the patient service centres' visits, scheduled and walk-in, with attendance
  campaign         the at-home collection (mobile draw) offer: who was offered it, who took it up

Payers are commercial plans, Medicare, Medicaid (one programme per state) and self-pay; one
employer wellness contract is billed to the employer directly. Denials carry one of seven reason
categories modelled on the X12 claim adjustment reason codes (x12.org/codes/claim-adjustment-reason-
codes, checked 30 September 2026): eligibility or coverage, missing or invalid information, medical
necessity, prior authorization, non-covered service, duplicate claim, and timely filing. Every
payment posting balances: paid plus patient responsibility plus adjustment equals the billed amount.

The planted traps are the approved Build 1 spine's (docs/detailing/W03_build1_spine.md). Each is
asserted after generation, so a change that breaks one fails loudly, and none is named in a STUDENT
file: the room finds them by reconciling, splitting and asking what the denominator was.

  0 headline   Dr Menon's 5 percent is her dashboard's count of retail tests booked in the old system;
               across both systems, tests booked grew about 8 percent
  1 revenue    one employer wellness contract in Q3 moves every average; a panel is one claim line
               and many tests
  2 bookings   Chicago and Philadelphia moved to the new system late in Q3, so the old system's
               export shows about twice their real fall
  3 billing    the posting system keys claims in its own format, so an exact join matches almost
               nothing; duplicate ERA loads double-post; the employer invoice is unpaid; and denials
               sit beside the payments with nothing paid
  4 no-shows   one small patient service centre's rate looks double the others' because the others
               count walk-ins, and on its base the remaining gap is within chance
  5 campaign   the offer went at random to half the patients in three metros where bookings were
               already rising and to a fifth of patients elsewhere; offered patients out-book the rest
               overall while booking less than the rest, during the offer, inside each of the three
               campaign metros, and outside them any gap is chance (New York's draw happens to show one)

The bookings, patients, offer and appointments are drawn from the same random stream the India pack
of 29 September used, so every count behind plants 0, 2, 4 and 5 is the count that pack had; payers,
denials, dollar amounts and postings come from their own seeded streams.
"""
import argparse
import csv
import datetime as dt
import math
import pathlib
import random
import sys

SEED = 20261019
METROS = [("Dallas", "DAL"), ("Phoenix", "PHX"), ("New York", "NYC"),
          ("Chicago", "CHI"), ("Atlanta", "ATL"), ("Philadelphia", "PHI")]
NEW_CODES = {"Chicago": "ORD", "Philadelphia": "PHL"}
Q2 = (dt.date(2026, 4, 1), dt.date(2026, 6, 30))
Q3 = (dt.date(2026, 7, 1), dt.date(2026, 9, 30))
SWITCH_METROS = ("Chicago", "Philadelphia")
SWITCH_DATE = dt.date(2026, 9, 18)
CAMPAIGN_METROS = ("Dallas", "Atlanta", "Phoenix")
CAMPAIGN = (dt.date(2026, 7, 15), dt.date(2026, 9, 14))
PRE_CAMPAIGN = (dt.date(2026, 5, 14), dt.date(2026, 7, 14))
SMALL_SITE = "KH-ATL-03"
EMPLOYER = {"account": "EMP-0007", "metro": "Dallas", "site": "KH-DAL-01",
            "date": dt.date(2026, 8, 6), "heads": 1200, "unit": 150}

# Daily bookings per metro at the start of Q2, and the monthly trend. The campaign metros were
# already rising before the offer; Chicago and Philadelphia were really falling, by less than the
# old system's export makes it look.
BASE = {"Dallas": 14.0, "Phoenix": 13.0, "New York": 12.0, "Chicago": 9.5, "Atlanta": 9.0,
        "Philadelphia": 8.5}
TREND = {"Dallas": 0.045, "Phoenix": 0.045, "New York": 0.005, "Chicago": -0.042,
         "Atlanta": 0.045, "Philadelphia": -0.042}
PATIENTS = {"Dallas": 1250, "Phoenix": 1200, "New York": 1500, "Chicago": 1000, "Atlanta": 800,
            "Philadelphia": 950}
STATE = {"Dallas": "TX", "Phoenix": "AZ", "New York": "NY", "Chicago": "IL", "Atlanta": "GA",
         "Philadelphia": "PA"}
AGE_BANDS = ["18-34", "35-49", "50-64", "65+"]

# Synthetic Kalpa list prices in dollars. The names are plain words, never CPT descriptor text.
TESTS = [("T-CBC", "Complete blood count", 45), ("T-LIP", "Cholesterol panel", 75),
         ("T-HBA", "Hemoglobin A1c", 60), ("T-THY", "Thyroid screen", 95),
         ("T-LFT", "Liver health panel", 70), ("T-KFT", "Kidney health panel", 65),
         ("T-VTD", "Vitamin D", 150), ("T-B12", "Vitamin B12", 85),
         ("T-URN", "Urine test", 30), ("T-FBS", "Fasting glucose", 25),
         ("T-CRP", "Inflammation marker (CRP)", 55), ("T-ESR", "Sed rate (ESR)", 30)]
PRICE = {code: price for code, _, price in TESTS}
PANELS = {
    "PNL-WEL": ("Whole-body wellness panel", 299, ["T-CBC", "T-LIP", "T-HBA", "T-THY", "T-LFT",
                                                   "T-KFT", "T-VTD", "T-B12", "T-URN", "T-FBS",
                                                   "T-CRP", "T-ESR"]),
    "PNL-DB": ("Diabetes monitoring panel", 149, ["T-HBA", "T-FBS", "T-KFT", "T-URN"]),
    "PNL-AGE": ("Healthy aging panel", 349, ["T-CBC", "T-LIP", "T-HBA", "T-THY", "T-LFT",
                                             "T-KFT", "T-VTD", "T-B12", "T-URN", "T-FBS"]),
    "PNL-EMP": ("Employer wellness screening", 150, ["T-CBC", "T-LIP", "T-FBS", "T-URN", "T-LFT"]),
}
MOBILE_DRAW_FEE = 20
# Who was offered the free at-home collection, at random within each metro, and how much less an
# offered patient in a campaign metro books while the offer runs than a patient who was not offered.
OFFER_CHANCE = {"campaign": 0.50, "other": 0.20}
OFFER_SKIP = 0.06
CHANNELS = ("walk-in", "online", "phone", "at-home")
NEW_CHANNEL = {"walk-in": "WALKIN", "online": "WEB", "phone": "CALL", "at-home": "MOBILEDRAW"}

# Payers. Under 65 a patient is on a commercial plan, Medicaid or self-pay; at 65 and over, mostly
# Medicare. Each payer allows a share of the billed list price; the shares are synthetic and are no
# payer's real rate. Commercial members sometimes owe a deductible or coinsurance.
PAYER_UNDER_65 = (("commercial", 0.70), ("Medicaid", 0.20), ("self-pay", 0.10))
PAYER_65_PLUS = (("Medicare", 0.93), ("commercial", 0.05), ("self-pay", 0.02))
COMMERCIAL_PLANS = {"COM-A": 0.58, "COM-B": 0.52, "COM-C": 0.47}
ALLOWED_SHARE = {"Medicare": 0.34, "Medicaid": 0.28}
DENIAL_RATE = {"commercial": 0.09, "Medicare": 0.07, "Medicaid": 0.11, "self-pay": 0.0}
PANEL_DENIAL_FACTOR = 2.0   # a wellness panel billed to insurance is screening, and denied more often
DENIAL_CATEGORIES = ("eligibility or coverage", "missing or invalid information", "medical necessity",
                     "prior authorization", "non-covered service", "duplicate claim", "timely filing")
DENIAL_WEIGHTS = {"commercial": (25, 30, 10, 10, 15, 5, 5),
                  "Medicare": (10, 25, 40, 0, 15, 5, 5),
                  "Medicaid": (40, 25, 10, 10, 5, 5, 5)}


def days(a, b):
    d = a
    while d <= b:
        yield d
        d += dt.timedelta(days=1)


def months_in(d):
    return (d - Q2[0]).days / 30.4


def cents(x):
    return f"{x:.2f}"


def sites():
    out = []
    for metro, code in METROS:
        for n, kind in ((1, "laboratory"), (2, "patient service center"), (3, "patient service center")):
            new = f"{NEW_CODES[metro]}-{n:02d}" if metro in NEW_CODES else ""
            out.append({"site_code": f"KH-{code}-{n:02d}", "metro": metro, "kind": kind,
                        "new_system_code": new})
    return out


def patients(rng):
    out, n = [], 0
    for metro, _ in METROS:
        for _ in range(PATIENTS[metro]):
            n += 1
            frequent = rng.random() < 0.18
            out.append({"patient_id": f"P-{n:06d}", "metro": metro,
                        "age_band": rng.choice(AGE_BANDS),
                        "sex": rng.choice(["F", "M"]),
                        "payer_type": "", "employer_account": "",
                        "_weight": 5.0 if frequent else 1.0})
    return out


def assign_payers(people):
    """Each patient's payer type and payer id, from its own stream so the bookings are untouched."""
    rng = random.Random(SEED + 5)
    for p in people:
        mix = PAYER_65_PLUS if p["age_band"] == "65+" else PAYER_UNDER_65
        p["payer_type"] = rng.choices([t for t, _ in mix], weights=[w for _, w in mix])[0]
        if p["payer_type"] == "commercial":
            p["_payer_id"] = rng.choice(sorted(COMMERCIAL_PLANS))
        elif p["payer_type"] == "Medicare":
            p["_payer_id"] = "MEDICARE"
        elif p["payer_type"] == "Medicaid":
            p["_payer_id"] = f"MEDICAID-{STATE[p['metro']]}"
        else:
            p["_payer_id"] = "SELF"


def pick_tests(rng):
    """(panel or None, [test codes]) for one ordinary booking."""
    r = rng.random()
    if r < 0.14:
        return "PNL-WEL", None
    if r < 0.22:
        return "PNL-DB", None
    if r < 0.27:
        return "PNL-AGE", None
    k = rng.choice([1, 1, 2, 2, 3, 4])
    return None, rng.sample([t for t, _, _ in TESTS], k)


def generate():
    rng = random.Random(SEED)
    site_rows = sites()
    people = patients(rng)
    by_metro = {m: [p for p in people if p["metro"] == m] for m, _ in METROS}
    weights = {m: [p["_weight"] for p in by_metro[m]] for m in by_metro}
    site_codes = {m: [s["site_code"] for s in site_rows if s["metro"] == m] for m, _ in METROS}

    # The campaign offer is decided up front, at random within each metro: half the patients in the
    # campaign metros and a fifth elsewhere. The shortfall that makes offered patients book less
    # comes later, from OFFER_SKIP, only inside the campaign metros and only while the offer runs,
    # so any other gap is chance.
    offered, took_up = {}, set()
    for p in people:
        chance = OFFER_CHANCE["campaign"] if p["metro"] in CAMPAIGN_METROS else OFFER_CHANCE["other"]
        if rng.random() < chance:
            offered[p["patient_id"]] = CAMPAIGN[0] + dt.timedelta(days=rng.randint(0, 20))
            if rng.random() < 0.4:
                took_up.add(p["patient_id"])

    bookings = []
    serial = 0
    for metro, _ in METROS:
        for d in days(Q2[0], Q3[1]):
            weekday = 0.72 if d.weekday() == 6 else 1.0
            lam = BASE[metro] * (1 + TREND[metro] * months_in(d)) * weekday
            count = sum(1 for _ in range(int(lam * 2)) if rng.random() < 0.5)
            for _ in range(count):
                serial += 1
                p = rng.choices(by_metro[metro], weights=weights[metro])[0]
                pid = p["patient_id"]
                # Within the campaign metros, a patient who was offered the free collection books a
                # little less often while the offer runs than a patient who was not; before the
                # offer the two groups book alike, so nothing in the files shows who was targeted.
                if (pid in offered and metro in CAMPAIGN_METROS and CAMPAIGN[0] <= d <= CAMPAIGN[1]
                        and rng.random() < OFFER_SKIP):
                    continue
                in_window = pid in took_up and offered[pid] <= d <= CAMPAIGN[1]
                channel = ("at-home" if in_window and rng.random() < 0.6 else
                           rng.choices(CHANNELS, weights=[46, 28, 16, 10])[0])
                panel, tests = pick_tests(rng)
                bookings.append({
                    "serial": serial, "patient_id": pid, "metro": metro,
                    "site_code": rng.choice(site_codes[metro]), "date": d,
                    "channel": channel, "panel": panel, "tests": tests,
                    "status": "cancelled" if rng.random() < 0.03 else "completed",
                    "fee_waived": in_window,
                })
    # The employer wellness contract: one booking, one invoice, twelve hundred screenings.
    serial += 1
    emp_patient = next(p for p in people if p["metro"] == EMPLOYER["metro"])
    emp_patient["employer_account"] = EMPLOYER["account"]
    bookings.append({"serial": serial, "patient_id": emp_patient["patient_id"],
                     "metro": EMPLOYER["metro"], "site_code": EMPLOYER["site"],
                     "date": EMPLOYER["date"], "channel": "employer", "panel": "PNL-EMP",
                     "tests": None, "status": "completed", "fee_waived": True,
                     "quantity": EMPLOYER["heads"]})
    bookings.sort(key=lambda b: (b["date"], b["serial"]))
    assign_payers(people)
    payer_of = {p["patient_id"]: p for p in people}

    # Ids, and which system each booking lives in.
    new_serial = {}
    for n, b in enumerate(bookings, 1):
        b["booking_id"] = f"KB{n:07d}"
        b["system"] = "legacy"
        if b["metro"] in SWITCH_METROS and b["date"] >= SWITCH_DATE:
            key = NEW_CODES[b["metro"]]
            new_serial[key] = new_serial.get(key, 0) + 1
            b["system"] = "new"
            b["booking_id"] = f"NB/{key}/{new_serial[key]:06d}"

    legacy_rows, new_rows = [], []
    for b in bookings:
        if b["system"] == "legacy":
            legacy_rows.append({
                "booking_id": b["booking_id"], "patient_id": b["patient_id"],
                "site_code": b["site_code"], "metro": b["metro"],
                "booking_date": b["date"].isoformat(), "channel": b["channel"],
                "status": b["status"],
                "updated_at": f"{b['date'].isoformat()} {rng.randint(8, 19):02d}:{rng.randint(0, 59):02d}"})
        else:
            site = next(s for s in site_rows if s["site_code"] == b["site_code"])
            new_rows.append({
                "bkg_ref": b["booking_id"], "patient": b["patient_id"].replace("P-", ""),
                "site": site["new_system_code"], "metro": b["metro"],
                "created": b["date"].strftime("%m/%d/%Y"),
                "channel": NEW_CHANNEL.get(b["channel"], b["channel"].upper()),
                "state": "DONE" if b["status"] == "completed" else "CXL"})
    # The mid-quarter re-export repeated a stretch of rows exactly, and a handful of bookings edited
    # after the first export came back with a later updated_at.
    dup_rng = random.Random(SEED + 1)
    repeated = dup_rng.sample(legacy_rows[len(legacy_rows) // 3: len(legacy_rows) // 2], 150)
    edited = dup_rng.sample(legacy_rows[len(legacy_rows) // 2:], 30)
    legacy_out = legacy_rows + [dict(r) for r in repeated]
    for r in edited:
        again = dict(r)
        again["updated_at"] = again["updated_at"][:11] + "21:45"
        legacy_out.append(again)
    dup_rng.shuffle(legacy_out)
    for r in dup_rng.sample(legacy_out, 180):
        r["channel"] = ""

    test_rows = []
    for b in bookings:
        qty = b.get("quantity", 1)
        if b["panel"]:
            name, price, parts = PANELS[b["panel"]]
            test_rows.append({"booking_id": b["booking_id"], "test_code": b["panel"],
                              "panel_code": b["panel"], "quantity": qty,
                              "price_each": price, "line": "panel"})
            for t in parts:
                test_rows.append({"booking_id": b["booking_id"], "test_code": t,
                                  "panel_code": b["panel"], "quantity": qty,
                                  "price_each": 0, "line": "component"})
        else:
            for t in b["tests"]:
                test_rows.append({"booking_id": b["booking_id"], "test_code": t,
                                  "panel_code": "", "quantity": 1,
                                  "price_each": PRICE[t], "line": "test"})

    # Claims: one per completed booking, billed at list price to the patient's payer, or to the
    # employer for the wellness contract. Whether a payer denies it is drawn here, from its own
    # stream, and the billing system shows the category once the denial is posted back.
    deny_rng = random.Random(SEED + 6)
    claims, n_clm = [], 0
    for b in bookings:
        if b["status"] != "completed":
            continue
        n_clm += 1
        qty = b.get("quantity", 1)
        if b["panel"]:
            amount, items = PANELS[b["panel"]][1] * qty, 1
        else:
            amount, items = sum(PRICE[t] for t in b["tests"]), len(b["tests"])
        if b["channel"] == "at-home" and not b["fee_waived"]:
            amount += MOBILE_DRAW_FEE
            items += 1
        p = payer_of[b["patient_id"]]
        employer = b["channel"] == "employer"
        payer_type = "employer" if employer else p["payer_type"]
        denial = ""
        if not employer:
            rate = DENIAL_RATE[payer_type] * (PANEL_DENIAL_FACTOR if b["panel"] else 1.0)
            if deny_rng.random() < rate:
                w = list(DENIAL_WEIGHTS[payer_type])
                if b["panel"]:
                    w[4] *= 3          # a screening panel is the non-covered service a payer refuses
                denial = deny_rng.choices(DENIAL_CATEGORIES, weights=w)[0]
        claims.append({"claim_id": f"KH-CLM-{n_clm:06d}", "booking_id": b["booking_id"],
                       "service_date": b["date"].isoformat(), "metro": b["metro"],
                       "payer_type": payer_type,
                       "payer_id": EMPLOYER["account"] if employer else p["_payer_id"],
                       "billed_amount": amount, "line_items": items,
                       "employer_account": EMPLOYER["account"] if employer else "",
                       "denial_category": denial})
    # Sixty billed amounts left the billing system as formatted text.
    clm_rng = random.Random(SEED + 2)
    for c in clm_rng.sample(claims, 60):
        c["billed_amount"] = f"${c['billed_amount']:,}.00"

    # Postings: a payer's remittance (ERA) some weeks after service, or the patient's own payment
    # at the desk. The posting system keys the claim as the payer echoed it: bare digits from most
    # payers, CLM-number from the Medicaid programmes and the desk, and the full claim id only for
    # a few desk payments. A few ERA files were loaded twice, and a few payments were reversed.
    pay_rng = random.Random(SEED + 3)
    postings, n_post = [], 0
    unpaid = set(clm_rng.sample([c["claim_id"] for c in claims if not c["employer_account"]],
                                int(len(claims) * 0.035)))
    unpaid.add(next(c["claim_id"] for c in claims if c["employer_account"]))
    for c in claims:
        if c["claim_id"] in unpaid:
            continue
        billed = int(str(c["billed_amount"]).replace("$", "").replace(",", "").replace(".00", ""))
        digits = c["claim_id"].split("-")[-1]
        payer = c["payer_type"]
        if payer == "self-pay":
            channel = pay_rng.choices(["card", "cash"], weights=[80, 20])[0]
            ref = c["claim_id"] if pay_rng.random() < 0.25 else f"CLM-{int(digits)}"
            posted = dt.date.fromisoformat(c["service_date"]) + dt.timedelta(days=pay_rng.randint(0, 6))
        else:
            channel = "ERA"
            ref = f"CLM-{int(digits)}" if payer == "Medicaid" else digits
            posted = dt.date.fromisoformat(c["service_date"]) + dt.timedelta(days=pay_rng.randint(14, 45))
        stamp = f"{posted.isoformat()} {pay_rng.randint(8, 21):02d}:{pay_rng.randint(0, 59):02d}"
        n_post += 1
        base = {"posting_id": f"PST{n_post:07d}", "claim_ref": ref, "payer_id": c["payer_id"],
                "channel": channel, "billed_amount": billed}
        if c["denial_category"]:
            group = "OA" if c["denial_category"] == "duplicate claim" else "CO"
            postings.append(dict(base, posting="denial", allowed_amount=cents(0), paid_amount=cents(0),
                                 patient_responsibility=cents(0), adjustment_amount=cents(billed),
                                 adjustment_group=group, reason_category=c["denial_category"],
                                 posted_at=stamp))
            continue
        if payer == "self-pay":
            allowed, owed = float(billed), 0.0
            group, reason = "", ""
        else:
            share = COMMERCIAL_PLANS[c["payer_id"]] if payer == "commercial" else ALLOWED_SHARE[payer]
            allowed = round(billed * share, 2)
            owed = round(allowed * 0.20, 2) if payer == "commercial" and pay_rng.random() < 0.35 else 0.0
            group, reason = "CO", "contractual adjustment"
        paid = round(allowed - owed, 2)
        row = dict(base, posting="payment", allowed_amount=cents(allowed), paid_amount=cents(paid),
                   patient_responsibility=cents(owed), adjustment_amount=cents(billed - allowed),
                   adjustment_group=group, reason_category=reason, posted_at=stamp)
        postings.append(row)
        if channel == "ERA" and pay_rng.random() < 0.03:
            n_post += 1
            postings.append(dict(row, posting_id=f"PST{n_post:07d}",
                                 posted_at=stamp[:-2] + f"{min(59, int(stamp[-2:]) + 2):02d}"))
        if pay_rng.random() < 0.01:
            n_post += 1
            postings.append(dict(base, posting_id=f"PST{n_post:07d}", posting="reversal",
                                 allowed_amount=cents(0), paid_amount=cents(-paid),
                                 patient_responsibility=cents(0), adjustment_amount=cents(0),
                                 adjustment_group="", reason_category="", posted_at=stamp))

    # Appointments at the patient service centres in Q3: scheduled visits with attendance, and
    # walk-ins, who by definition came. The small centre runs almost entirely by appointment.
    appt_rng = random.Random(SEED + 4)
    appointments, n_app = [], 0
    for site in site_rows:
        if site["kind"] != "patient service center":
            continue
        small = site["site_code"] == SMALL_SITE
        for d in days(*Q3):
            scheduled = (1 if appt_rng.random() < 0.52 else 0) if small else appt_rng.randint(2, 6)
            walkins = (1 if appt_rng.random() < 0.02 else 0) if small else appt_rng.randint(1, 5)
            for _ in range(scheduled):
                n_app += 1
                appointments.append({"appointment_id": f"AP{n_app:06d}",
                                     "site_code": site["site_code"], "visit_date": d.isoformat(),
                                     "kind": "scheduled",
                                     "attended": "N" if appt_rng.random() < 0.15 else "Y"})
            for _ in range(walkins):
                n_app += 1
                appointments.append({"appointment_id": f"AP{n_app:06d}",
                                     "site_code": site["site_code"], "visit_date": d.isoformat(),
                                     "kind": "walk-in", "attended": "Y"})
    # Pin the small centre's no-shows at ten, so the witness numbers hold whatever the draw.
    small_rows = [a for a in appointments if a["site_code"] == SMALL_SITE and a["kind"] == "scheduled"]
    step = max(1, len(small_rows) // 10)
    for k, a in enumerate(sorted(small_rows, key=lambda a: a["appointment_id"])):
        a["attended"] = "N" if k % step == 0 and k // step < 10 else "Y"

    campaign = [{"patient_id": pid, "metro": payer_of[pid]["metro"],
                 "offered_on": day.isoformat(), "took_up": "Y" if pid in took_up else "N"}
                for pid, day in sorted(offered.items())]

    tables = {
        "patients": [{k: v for k, v in p.items() if not k.startswith("_")} for p in people],
        "sites": site_rows,
        "test_catalogue": ([{"code": c, "name": n, "list_price_usd": pr, "kind": "test"}
                            for c, n, pr in TESTS]
                           + [{"code": c, "name": v[0], "list_price_usd": v[1], "kind": "panel"}
                              for c, v in PANELS.items()]),
        "bookings_legacy": legacy_out,
        "bookings_newsys": new_rows,
        "booking_tests": test_rows,
        "claims": claims,
        "remittances": postings,
        "appointments": appointments,
        "campaign": campaign,
    }
    return tables, bookings


def dollars(value):
    """A billed amount as a number, whether the export wrote 299 or "$1,050.00"."""
    return int(str(value).replace("$", "").replace(",", "").replace(".00", ""))


# ------------------------------------------------------------------------------------ the witness
def witness(tables, bookings):
    """The numbers the TRAINER files quote, computed from the tables as a learner would."""
    w = {}
    real = {m: {"Q2": 0, "Q3": 0} for m, _ in METROS}
    for b in bookings:
        q = "Q2" if b["date"] <= Q2[1] else "Q3"
        real[b["metro"]][q] += 1
    legacy_q3 = {m: 0 for m, _ in METROS}
    seen = set()
    for r in tables["bookings_legacy"]:
        if r["booking_id"] in seen:
            continue
        seen.add(r["booking_id"])
        if r["booking_date"] >= Q3[0].isoformat():
            legacy_q3[r["metro"]] += 1
    sw_q2 = sum(real[m]["Q2"] for m in SWITCH_METROS)
    sw_q3_real = sum(real[m]["Q3"] for m in SWITCH_METROS)
    sw_q3_legacy = sum(legacy_q3[m] for m in SWITCH_METROS)
    w["switch_metros_q2"] = sw_q2
    w["switch_metros_q3_real"] = sw_q3_real
    w["switch_metros_q3_legacy_only"] = sw_q3_legacy
    w["switch_real_change"] = sw_q3_real / sw_q2 - 1
    w["switch_apparent_change"] = sw_q3_legacy / sw_q2 - 1
    w["legacy_rows"] = len(tables["bookings_legacy"])
    w["legacy_distinct_ids"] = len(seen)
    w["newsys_rows"] = len(tables["bookings_newsys"])

    # Dr Menon's 5 percent is her dashboard's: retail tests booked in the old system only, a panel
    # counted as its component tests. The whole business moved faster than that.
    def tests_in(b):
        return len(PANELS[b["panel"]][2]) if b["panel"] else len(b["tests"])
    moved = {k: {"Q2": 0, "Q3": 0} for k in ("dashboard", "booked", "performed", "bookings")}
    for b in bookings:
        if b["channel"] == "employer":
            continue
        q = "Q2" if b["date"] <= Q2[1] else "Q3"
        moved["booked"][q] += tests_in(b)
        moved["bookings"][q] += 1
        if b["system"] == "legacy":
            moved["dashboard"][q] += tests_in(b)
        if b["status"] == "completed":
            moved["performed"][q] += tests_in(b)
    for k, v in moved.items():
        w[f"{k}_q2_to_q3"] = v["Q3"] / v["Q2"] - 1

    cl = tables["claims"]
    amounts = [dollars(c["billed_amount"]) for c in cl]
    q3 = [a for c, a in zip(cl, amounts) if c["service_date"] >= Q3[0].isoformat()]
    q3_retail = [a for c, a in zip(cl, amounts)
                 if c["service_date"] >= Q3[0].isoformat() and not c["employer_account"]]
    w["q3_billed"] = sum(q3)
    w["q3_billed_without_contract"] = sum(q3_retail)
    w["q2_billed"] = sum(a for c, a in zip(cl, amounts) if c["service_date"] <= Q2[1].isoformat())
    w["contract_amount"] = EMPLOYER["heads"] * EMPLOYER["unit"]
    w["contract_share_of_q3"] = w["contract_amount"] / sum(q3)
    w["q3_mean_claim"] = sum(q3) / len(q3)
    w["q3_mean_without_contract"] = sum(q3_retail) / len(q3_retail)
    s = sorted(q3)
    w["q3_median_claim"] = (s[len(s) // 2 - 1] + s[len(s) // 2]) / 2 if len(s) % 2 == 0 else s[len(s) // 2]
    w["text_amounts"] = sum(1 for c in cl if isinstance(c["billed_amount"], str))
    lines = sum(c["line_items"] for c in cl if not c["employer_account"])
    completed = {b["booking_id"] for b in bookings if b["status"] == "completed"}
    tests = [t for t in tables["booking_tests"] if t["line"] in ("test", "component")
             and not t["panel_code"] == "PNL-EMP"]
    w["claim_lines_non_employer"] = lines
    # Tests on every booking, cancelled ones included, and on the completed bookings, which are the
    # ones the claim lines bill: the second is the like-for-like count behind the lines.
    w["tests_booked_non_employer"] = len(tests)
    w["tests_on_claimed_bookings_non_employer"] = sum(1 for t in tests if t["booking_id"] in completed)

    # The payer mix and the denial rates, over the retail claims (the employer bill is neither).
    retail = [c for c in cl if not c["employer_account"]]
    w["retail_claims"] = len(retail)
    w["payer_mix"] = {t: sum(1 for c in retail if c["payer_type"] == t) / len(retail)
                      for t in ("commercial", "Medicare", "Medicaid", "self-pay")}
    w["denial_rate_overall"] = sum(1 for c in retail if c["denial_category"]) / len(retail)
    w["denial_rate_by_payer"] = {t: sum(1 for c in retail if c["payer_type"] == t and c["denial_category"])
                                 / max(1, sum(1 for c in retail if c["payer_type"] == t))
                                 for t in ("commercial", "Medicare", "Medicaid", "self-pay")}
    denied = [c for c in retail if c["denial_category"]]
    w["denials_by_category"] = {k: sum(1 for c in denied if c["denial_category"] == k)
                                for k in DENIAL_CATEGORIES}
    w["denied_billed"] = sum(dollars(c["billed_amount"]) for c in denied)

    ids = {c["claim_id"] for c in cl}
    posts = tables["remittances"]
    w["remittance_rows"] = len(posts)
    w["exact_join_matches"] = sum(1 for p in posts if p["claim_ref"] in ids)
    w["exact_join_share"] = w["exact_join_matches"] / len(posts)
    by_digits = {c["claim_id"].split("-")[-1]: c["claim_id"] for c in cl}

    def normalise(ref):
        if ref in ids:
            return ref
        if ref.startswith("CLM-"):
            return by_digits.get(f"{int(ref[4:]):06d}")
        return by_digits.get(ref)
    matched = [normalise(p["claim_ref"]) for p in posts]
    w["normalised_join_unmatched"] = sum(1 for m in matched if m is None)
    keys = {}
    for p in posts:
        if p["posting"] == "payment":
            keys.setdefault((p["claim_ref"], p["paid_amount"]), []).append(p)
    doubles = [p for v in keys.values() if len(v) > 1 for p in v[1:]]
    w["double_posts"] = len(doubles)
    w["double_posted_dollars"] = round(sum(float(p["paid_amount"]) for p in doubles), 2)
    w["reversals"] = sum(1 for p in posts if p["posting"] == "reversal")
    w["denial_postings"] = sum(1 for p in posts if p["posting"] == "denial")
    claim_of = {c["claim_id"]: c for c in cl}
    w["denials_matching_claims"] = sum(1 for p, m in zip(posts, matched) if p["posting"] == "denial"
                                       and m and claim_of[m]["denial_category"] == p["reason_category"])
    w["unbalanced_postings"] = sum(1 for p in posts if p["posting"] in ("payment", "denial") and abs(
        float(p["paid_amount"]) + float(p["patient_responsibility"]) + float(p["adjustment_amount"])
        - p["billed_amount"]) > 0.005)
    posted = {m for m in matched if m}
    w["denied_claims_posted"] = sum(1 for c in denied if c["claim_id"] in posted)
    w["claims_without_posting"] = len(ids - posted)
    w["employer_invoice_unpaid"] = any(c["employer_account"] and c["claim_id"] not in posted for c in cl)
    w["paid_raw_sum"] = round(sum(float(p["paid_amount"]) for p in posts), 2)
    w["paid_net_of_double_posts"] = round(w["paid_raw_sum"] - w["double_posted_dollars"], 2)
    w["billed_all"] = sum(amounts)
    w["net_collection_ratio"] = w["paid_net_of_double_posts"] / w["billed_all"]

    appts = tables["appointments"]
    small_sched = [a for a in appts if a["site_code"] == SMALL_SITE and a["kind"] == "scheduled"]
    small_all = [a for a in appts if a["site_code"] == SMALL_SITE]
    other_sched = [a for a in appts if a["site_code"] != SMALL_SITE and a["kind"] == "scheduled"]
    other_all = [a for a in appts if a["site_code"] != SMALL_SITE]
    w["small_site_scheduled"] = len(small_sched)
    w["small_site_no_shows"] = sum(1 for a in small_sched if a["attended"] == "N")
    w["small_site_rate_all_visits"] = sum(1 for a in small_all if a["attended"] == "N") / len(small_all)
    w["others_rate_all_visits"] = sum(1 for a in other_all if a["attended"] == "N") / len(other_all)
    w["small_site_rate_scheduled"] = w["small_site_no_shows"] / len(small_sched)
    w["others_rate_scheduled"] = sum(1 for a in other_sched if a["attended"] == "N") / len(other_sched)
    n, k, p = len(small_sched), w["small_site_no_shows"], w["others_rate_scheduled"]
    w["small_site_tail_probability"] = sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j)
                                           for j in range(k, n + 1))

    offered = {c["patient_id"] for c in tables["campaign"]}
    in_window = {}
    for b in bookings:
        if CAMPAIGN[0] <= b["date"] <= CAMPAIGN[1] and b["channel"] != "employer":
            in_window[b["patient_id"]] = in_window.get(b["patient_id"], 0) + 1
    people = tables["patients"]

    def rate(group):
        return sum(in_window.get(p["patient_id"], 0) for p in group) / max(1, len(group))
    off = [p for p in people if p["patient_id"] in offered]
    rest = [p for p in people if p["patient_id"] not in offered]
    w["offered_patients"] = len(off)
    w["campaign_lift_aggregate"] = rate(off) / rate(rest) - 1
    w["campaign_lift_by_metro"] = {m: rate([p for p in off if p["metro"] == m])
                                   / rate([p for p in rest if p["metro"] == m]) - 1
                                   for m in CAMPAIGN_METROS}
    # Outside the campaign metros the offer carries no shortfall, so these gaps are chance.
    w["campaign_lift_other_metros"] = {m: rate([p for p in off if p["metro"] == m])
                                       / rate([p for p in rest if p["metro"] == m]) - 1
                                       for m, _ in METROS if m not in CAMPAIGN_METROS}
    w["offered_share"] = {group: sum(1 for p in off if (p["metro"] in CAMPAIGN_METROS) == inside)
                          / sum(1 for p in people if (p["metro"] in CAMPAIGN_METROS) == inside)
                          for group, inside in (("campaign_metros", True), ("other_metros", False))}
    before = {}
    for b in bookings:
        if Q2[0] <= b["date"] < CAMPAIGN[0] and b["channel"] != "employer":
            before[b["patient_id"]] = before.get(b["patient_id"], 0) + 1

    def rate_before(group):
        return sum(before.get(p["patient_id"], 0) for p in group) / max(1, len(group))
    w["campaign_gap_before_offer_by_metro"] = {m: rate_before([p for p in off if p["metro"] == m])
                                               / rate_before([p for p in rest if p["metro"] == m]) - 1
                                               for m in CAMPAIGN_METROS}

    def window_count(metro_set, lo, hi):
        return sum(1 for b in bookings if b["metro"] in metro_set and lo <= b["date"] <= hi
                   and b["channel"] != "employer")
    camp = set(CAMPAIGN_METROS)
    rest_metros = {m for m, _ in METROS} - camp - set(SWITCH_METROS)
    w["campaign_metros_window_change"] = (window_count(camp, *CAMPAIGN)
                                          / window_count(camp, *PRE_CAMPAIGN) - 1)
    w["campaign_metros_prior_change"] = (window_count(camp, *PRE_CAMPAIGN)
                                         / window_count(camp, Q2[0], PRE_CAMPAIGN[0] - dt.timedelta(days=1))
                                         * ((PRE_CAMPAIGN[0] - Q2[0]).days / 62) - 1)
    w["other_metros_window_change"] = (window_count(rest_metros, *CAMPAIGN)
                                       / window_count(rest_metros, *PRE_CAMPAIGN) - 1)
    return w


def check(w):
    """Every plant the spine promises, and every US element, asserted. Returns the failures."""
    fails = []

    def want(ok, text):
        if not ok:
            fails.append(text)
    # 0 and 2: the headline and the system switch.
    want(-0.30 <= w["switch_apparent_change"] <= -0.20,
         f"apparent fall in the switch metros {w['switch_apparent_change']:.3f}, wanted -0.30 to -0.20")
    want(-0.16 <= w["switch_real_change"] <= -0.08,
         f"real fall in the switch metros {w['switch_real_change']:.3f}, wanted -0.16 to -0.08")
    share = w["switch_real_change"] / w["switch_apparent_change"]
    want(0.35 <= share <= 0.65, f"the real fall is {share:.2f} of the apparent one, wanted about half")
    want(0.045 <= w["dashboard_q2_to_q3"] <= 0.055,
         f"the dashboard's growth is {w['dashboard_q2_to_q3']:.3f}, and Dr Menon says 5 percent")
    want(w["booked_q2_to_q3"] >= w["dashboard_q2_to_q3"] + 0.02,
         "the old system alone does not understate the growth in tests booked")
    want(w["legacy_rows"] - w["legacy_distinct_ids"] == 180,
         f"legacy duplicates {w['legacy_rows'] - w['legacy_distinct_ids']}, wanted 180")
    # 1: the employer contract and the panels.
    want(0.10 <= w["contract_share_of_q3"] <= 0.25,
         f"contract share of Q3 billed {w['contract_share_of_q3']:.3f}, wanted 0.10 to 0.25")
    want(w["q3_mean_claim"] >= 1.08 * w["q3_mean_without_contract"],
         "the contract does not move the Q3 mean claim by 8 percent or more")
    want(w["tests_on_claimed_bookings_non_employer"] >= 1.5 * w["claim_lines_non_employer"],
         "panels do not hide at least half again as many tests as claim lines show")
    # 3: the claims against the postings.
    want(w["exact_join_share"] <= 0.04, f"exact join matches {w['exact_join_share']:.3f} of postings")
    want(w["exact_join_matches"] > 0, "no posting matches exactly, so the room never sees a join half-work")
    want(w["normalised_join_unmatched"] == 0, f"{w['normalised_join_unmatched']} postings unmatched after normalising")
    want(w["double_posts"] >= 150, f"only {w['double_posts']} double posts")
    want(w["employer_invoice_unpaid"], "the employer invoice has a posting")
    want(w["unbalanced_postings"] == 0,
         f"{w['unbalanced_postings']} postings where paid, patient share and adjustment miss the billed amount")
    want(w["denial_postings"] == w["denied_claims_posted"],
         f"{w['denied_claims_posted'] - w['denial_postings']} denied claims came back with no denial posting")
    want(w["denials_matching_claims"] == w["denial_postings"],
         f"{w['denial_postings'] - w['denials_matching_claims']} denial postings disagree with the claim's category")
    # The payer mix, a plausible outpatient lab's, over retail claims.
    mix = w["payer_mix"]
    for payer, lo, hi in (("commercial", 0.45, 0.62), ("Medicare", 0.18, 0.30),
                          ("Medicaid", 0.10, 0.20), ("self-pay", 0.04, 0.12)):
        want(lo <= mix[payer] <= hi, f"{payer} is {mix[payer]:.3f} of retail claims, wanted {lo} to {hi}")
    # The denial rates: about one retail claim in ten, Medicaid highest, self-pay never.
    rates = w["denial_rate_by_payer"]
    want(0.07 <= w["denial_rate_overall"] <= 0.14,
         f"overall denial rate {w['denial_rate_overall']:.3f}, wanted 0.07 to 0.14")
    want(rates["Medicaid"] > rates["commercial"] > rates["Medicare"] > 0,
         f"denial rates out of order: {rates}")
    want(rates["self-pay"] == 0, "a self-pay claim was denied, and there is no payer to deny it")
    want(all(n > 0 for k, n in w["denials_by_category"].items() if k != "prior authorization")
         and w["denials_by_category"]["medical necessity"] >= 30,
         f"a denial category is empty or medical necessity is thin: {w['denials_by_category']}")
    # The dollar totals.
    want(900_000 <= w["q3_billed_without_contract"] <= 1_300_000,
         f"Q3 retail billed ${w['q3_billed_without_contract']:,}, wanted $0.9m to $1.3m")
    want(w["contract_amount"] == 180_000, f"the employer contract is ${w['contract_amount']:,}, wanted $180,000")
    want(120 <= w["q3_mean_without_contract"] <= 220,
         f"Q3 mean retail claim ${w['q3_mean_without_contract']:.0f}, wanted $120 to $220")
    want(0.35 <= w["net_collection_ratio"] <= 0.60,
         f"paid is {w['net_collection_ratio']:.3f} of billed, wanted 0.35 to 0.60 for a US lab's list prices")
    want(w["text_amounts"] == 60 and w["double_posted_dollars"] > 0,
         "the sixty text amounts or the double-posted dollars are missing")
    # 4: the small centre's no-shows.
    want(40 <= w["small_site_scheduled"] <= 60, f"small centre scheduled {w['small_site_scheduled']}")
    want(w["small_site_no_shows"] == 10, f"small centre no-shows {w['small_site_no_shows']}")
    want(w["small_site_rate_all_visits"] >= 1.8 * w["others_rate_all_visits"],
         "the small centre's all-visit rate is not about double the others'")
    want(w["small_site_tail_probability"] >= 0.10,
         f"the small centre's gap is not within chance: tail {w['small_site_tail_probability']:.3f}")
    # 5: the at-home offer.
    want(0.06 <= w["campaign_lift_aggregate"] <= 0.12,
         f"aggregate campaign lift {w['campaign_lift_aggregate']:.3f}, wanted 0.06 to 0.12")
    for metro, lift in w["campaign_lift_by_metro"].items():
        want(lift < 0, f"{metro}: offered patients out-book the rest ({lift:.3f}); the reversal is lost")
    for metro, gap in w["campaign_gap_before_offer_by_metro"].items():
        want(abs(gap) <= 0.08, f"{metro}: offered patients already booked {gap:+.3f} apart before the offer")
    return fails


def write(tables, out, stem):
    out.mkdir(parents=True, exist_ok=True)
    for name, rows in tables.items():
        path = out / f"{stem}_{name}_STUDENT.csv"
        with path.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            for r in rows:
                writer.writerow({k: r.get(k, "") for k in rows[0].keys()})
        print(f"wrote {path} ({len(rows)} rows)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=pathlib.Path)
    ap.add_argument("--stem", default="C2_W03_D01")
    ap.add_argument("--contract", action="store_true", help="assert every plant, write nothing")
    ap.add_argument("--witness", action="store_true", help="print the numbers the TRAINER files quote")
    a = ap.parse_args()
    tables, bookings = generate()
    w = witness(tables, bookings)
    fails = check(w)
    if a.witness or a.contract:
        for k, v in w.items():
            if isinstance(v, dict):
                v = {kk: round(vv, 4) if isinstance(vv, float) else vv for kk, vv in v.items()}
            print(f"{k}: {v:.4f}" if isinstance(v, float) else f"{k}: {v}")
    if fails:
        for f in fails:
            print(f"FAIL  {f}")
        sys.exit(1)
    if a.out:
        write(tables, a.out, a.stem)
    print("PASS  every plant holds")


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# python3 data/generate_kalpa_health.py --contract
#     Prints the witness numbers and "PASS  every plant holds"; writes nothing.
# python3 data/generate_kalpa_health.py --out content/W03/D1/data
#     Writes ten CSV files named C2_W03_D01_{table}_STUDENT.csv and prints each row count.
# Running either twice
#     Byte-identical output, because every draw comes from the fixed seed.
# A change to TREND that makes Chicago and Philadelphia rise
#     FAIL on the apparent and real falls, and nothing is written.
# Starting the offered patients' shortfall on 1 April instead of on the offer's first day
#     FAIL on the gap before the offer in all three campaign metros (among other plants), because
#     the files would then show the offer reaching patients who were already booking less.
# Setting DENIAL_RATE["Medicaid"] to 0.05
#     FAIL on the order of the denial rates, since Medicaid no longer denies most.
# Setting the employer unit price to 400
#     FAIL on the contract's share of Q3 billed and on the contract amount.

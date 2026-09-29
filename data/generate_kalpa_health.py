"""Write Build 1's Kalpa Health data pack, deterministically, from one seed.

    python3 data/generate_kalpa_health.py --out content/W03/D1/data --stem C2_W03_D01
    python3 data/generate_kalpa_health.py --contract     # generate in memory and assert every plant
    python3 data/generate_kalpa_health.py --witness      # print the numbers the TRAINER files quote

Kalpa Health runs diagnostic laboratories and walk-in clinics in six Indian cities, and its COO,
Dr Priya Menon, wants to know why test volumes grew 5 percent against a plan of 18. The tracker row
names a re-labelled public source for Build 1's data without naming which; on 29 September 2026 the
requester chose a synthetic pack instead, so the files are safe in a public repository and every
learner holds the same bytes. Every price, name and number here is synthetic.

Ten files, one per system Dr Menon's team exports, each messy in the way that system is:

  patients         one row per patient, with the city and whether a corporate account books them
  clinics          one row per site, with the code each booking system uses for it
  test_catalogue   every test and package with its list price
  bookings_legacy  the old booking system, every city, ISO dates; re-exported once mid-quarter
  bookings_newsys  the new system two cities moved to in Q2, with its own ids, codes and date format
  booking_tests    one row per test on a booking; a package is a header row and its component tests
  invoices         the billing export, one invoice per completed booking
  payments         the gateway and clinic cash feed, keyed by an invoice reference in its own format
  appointments     the walk-in clinics' visits, scheduled and walk-in, with attendance
  campaign         the free home-collection offer: who was offered it, and who took it up

The planted traps are the approved Build 1 spine's (docs/detailing/W03_build1_spine.md). Each is
asserted after generation, so a change that breaks one fails loudly, and none is named in a STUDENT
file: the room finds them by reconciling, splitting and asking what the denominator was.

  0 headline   Dr Menon's 5 percent is her dashboard's count of retail tests booked in the old system;
               across both systems, tests booked grew about 8 percent
  1 revenue    one corporate health-check contract of Rs 18 lakh in Q2 moves every average; a package
               is one invoice line and many tests
  2 bookings   Chennai and Pune moved to the new system late in Q2, so the old system's export shows
               about twice their real fall
  3 billing    the payment feed keys invoices in its own format, so an exact join matches almost
               nothing; gateway retries double-post; the corporate invoice is still unpaid
  4 no-shows   one small clinic's rate looks double the others' because the others count walk-ins,
               and on its base the remaining gap is within chance
  5 campaign   the offer ran where bookings were already rising, and offered patients out-book the
               rest overall while booking less than the rest inside every city that ran it
"""
import argparse
import csv
import datetime as dt
import math
import pathlib
import random
import sys

SEED = 20261019
CITIES = [("Bengaluru", "BLR"), ("Mumbai", "MUM"), ("Delhi", "DEL"),
          ("Chennai", "CHE"), ("Hyderabad", "HYD"), ("Pune", "PUN")]
NEW_CODES = {"Chennai": "MAA", "Pune": "PNQ"}
Q1 = (dt.date(2026, 4, 1), dt.date(2026, 6, 30))
Q2 = (dt.date(2026, 7, 1), dt.date(2026, 9, 30))
SWITCH_CITIES = ("Chennai", "Pune")
SWITCH_DATE = dt.date(2026, 9, 18)
CAMPAIGN_CITIES = ("Bengaluru", "Hyderabad", "Mumbai")
CAMPAIGN = (dt.date(2026, 7, 15), dt.date(2026, 9, 14))
PRE_CAMPAIGN = (dt.date(2026, 5, 14), dt.date(2026, 7, 14))
SMALL_CLINIC = "KH-HYD-03"
CORPORATE = {"account": "CORP-0007", "city": "Bengaluru", "clinic": "KH-BLR-01",
             "date": dt.date(2026, 8, 6), "heads": 1200, "unit": 1500}

# Daily bookings per city at the start of Q1, and the monthly trend. The campaign cities were
# already rising before the offer; Chennai and Pune were really falling, by less than the old
# system's export makes it look.
BASE = {"Bengaluru": 14.0, "Mumbai": 13.0, "Delhi": 12.0, "Chennai": 9.5, "Hyderabad": 9.0,
        "Pune": 8.5}
TREND = {"Bengaluru": 0.045, "Mumbai": 0.045, "Delhi": 0.005, "Chennai": -0.042,
         "Hyderabad": 0.045, "Pune": -0.042}
PATIENTS = {"Bengaluru": 1250, "Mumbai": 1200, "Delhi": 1500, "Chennai": 1000, "Hyderabad": 800,
            "Pune": 950}

TESTS = [("T-CBC", "Complete blood count", 350), ("T-LIP", "Lipid profile", 600),
         ("T-HBA", "HbA1c", 450), ("T-THY", "Thyroid profile", 500),
         ("T-LFT", "Liver function test", 650), ("T-KFT", "Kidney function test", 700),
         ("T-VTD", "Vitamin D", 1200), ("T-B12", "Vitamin B12", 900),
         ("T-URN", "Urine routine", 200), ("T-FBS", "Fasting blood sugar", 120),
         ("T-CRP", "C-reactive protein", 550), ("T-ESR", "Erythrocyte sedimentation rate", 150)]
PRICE = {code: price for code, _, price in TESTS}
PACKAGES = {
    "PKG-FB": ("Full body checkup", 2999, ["T-CBC", "T-LIP", "T-HBA", "T-THY", "T-LFT", "T-KFT",
                                           "T-VTD", "T-B12", "T-URN", "T-FBS", "T-CRP", "T-ESR"]),
    "PKG-DB": ("Diabetes care", 1499, ["T-HBA", "T-FBS", "T-KFT", "T-URN"]),
    "PKG-SC": ("Senior citizen checkup", 3499, ["T-CBC", "T-LIP", "T-HBA", "T-THY", "T-LFT",
                                                "T-KFT", "T-VTD", "T-B12", "T-URN", "T-FBS"]),
    "PKG-CORP": ("Corporate health check", 1500, ["T-CBC", "T-LIP", "T-FBS", "T-URN", "T-LFT"]),
}
HOME_FEE = 100
# Who was offered the free collection, and how much less an offered patient in a campaign city
# books than a like-for-like one: the offer reached patients who had started to drift.
OFFER_CHANCE = {"campaign": 0.50, "other": 0.20}
OFFER_SKIP = 0.06
CHANNELS = ("walk-in", "app", "phone", "home-collection")
NEW_CHANNEL = {"walk-in": "WALKIN", "app": "APP", "phone": "CALL", "home-collection": "HOMEVISIT"}


def days(a, b):
    d = a
    while d <= b:
        yield d
        d += dt.timedelta(days=1)


def months_in(d):
    return (d - Q1[0]).days / 30.4


def clinics():
    out = []
    for city, code in CITIES:
        for n, kind in ((1, "laboratory"), (2, "walk-in clinic"), (3, "walk-in clinic")):
            new = f"{NEW_CODES[city]}-{n:02d}" if city in NEW_CODES else ""
            out.append({"clinic_code": f"KH-{code}-{n:02d}", "city": city, "kind": kind,
                        "new_system_code": new})
    return out


def patients(rng):
    out, n = [], 0
    for city, _ in CITIES:
        for _ in range(PATIENTS[city]):
            n += 1
            frequent = rng.random() < 0.18
            out.append({"patient_id": f"P-{n:06d}", "city": city,
                        "age_band": rng.choice(["18-29", "30-44", "45-59", "60+"]),
                        "sex": rng.choice(["F", "M"]),
                        "corporate_account": "", "_weight": 5.0 if frequent else 1.0})
    return out


def pick_tests(rng):
    """(package or None, [test codes]) for one ordinary booking."""
    r = rng.random()
    if r < 0.14:
        return "PKG-FB", None
    if r < 0.22:
        return "PKG-DB", None
    if r < 0.27:
        return "PKG-SC", None
    k = rng.choice([1, 1, 2, 2, 3, 4])
    return None, rng.sample([t for t, _, _ in TESTS], k)


def generate():
    rng = random.Random(SEED)
    sites = clinics()
    people = patients(rng)
    by_city = {city: [p for p in people if p["city"] == city] for city, _ in CITIES}
    weights = {city: [p["_weight"] for p in by_city[city]] for city in by_city}
    site_codes = {city: [c["clinic_code"] for c in sites if c["city"] == city] for city, _ in CITIES}

    # The campaign offer is decided up front. In the campaign cities it went to lapsed patients far
    # more than to frequent ones, and it barely reached the other cities at all.
    offered, took_up = {}, set()
    for p in people:
        chance = OFFER_CHANCE["campaign"] if p["city"] in CAMPAIGN_CITIES else OFFER_CHANCE["other"]
        if rng.random() < chance:
            offered[p["patient_id"]] = CAMPAIGN[0] + dt.timedelta(days=rng.randint(0, 20))
            if rng.random() < 0.4:
                took_up.add(p["patient_id"])

    bookings = []
    serial = 0
    for city, _ in CITIES:
        for d in days(Q1[0], Q2[1]):
            weekday = 0.72 if d.weekday() == 6 else 1.0
            lam = BASE[city] * (1 + TREND[city] * months_in(d)) * weekday
            count = sum(1 for _ in range(int(lam * 2)) if rng.random() < 0.5)
            for _ in range(count):
                serial += 1
                p = rng.choices(by_city[city], weights=weights[city])[0]
                pid = p["patient_id"]
                # Within the campaign cities, a patient who was offered the free collection books
                # a little less often than a like-for-like patient who was not: the offer went to
                # patients who had already drifted.
                if (pid in offered and city in CAMPAIGN_CITIES and CAMPAIGN[0] <= d <= CAMPAIGN[1]
                        and rng.random() < OFFER_SKIP):
                    continue
                in_window = pid in took_up and offered[pid] <= d <= CAMPAIGN[1]
                channel = ("home-collection" if in_window and rng.random() < 0.6 else
                           rng.choices(CHANNELS, weights=[46, 28, 16, 10])[0])
                package, tests = pick_tests(rng)
                bookings.append({
                    "serial": serial, "patient_id": pid, "city": city,
                    "clinic_code": rng.choice(site_codes[city]), "date": d,
                    "channel": channel, "package": package, "tests": tests,
                    "status": "cancelled" if rng.random() < 0.03 else "completed",
                    "fee_waived": in_window,
                })
    # The corporate contract: one booking, one invoice, twelve hundred health checks.
    serial += 1
    corp_patient = next(p for p in people if p["city"] == CORPORATE["city"])
    corp_patient["corporate_account"] = CORPORATE["account"]
    bookings.append({"serial": serial, "patient_id": corp_patient["patient_id"],
                     "city": CORPORATE["city"], "clinic_code": CORPORATE["clinic"],
                     "date": CORPORATE["date"], "channel": "corporate", "package": "PKG-CORP",
                     "tests": None, "status": "completed", "fee_waived": True,
                     "quantity": CORPORATE["heads"]})
    bookings.sort(key=lambda b: (b["date"], b["serial"]))

    # Ids, and which system each booking lives in.
    new_serial = {}
    for n, b in enumerate(bookings, 1):
        b["booking_id"] = f"KB{n:07d}"
        b["system"] = "legacy"
        if b["city"] in SWITCH_CITIES and b["date"] >= SWITCH_DATE:
            key = NEW_CODES[b["city"]]
            new_serial[key] = new_serial.get(key, 0) + 1
            b["system"] = "new"
            b["booking_id"] = f"NB/{key}/{new_serial[key]:06d}"

    legacy_rows, new_rows = [], []
    for b in bookings:
        if b["system"] == "legacy":
            legacy_rows.append({
                "booking_id": b["booking_id"], "patient_id": b["patient_id"],
                "clinic_code": b["clinic_code"], "city": b["city"],
                "booking_date": b["date"].isoformat(), "channel": b["channel"],
                "status": b["status"],
                "updated_at": f"{b['date'].isoformat()} {rng.randint(8, 19):02d}:{rng.randint(0, 59):02d}"})
        else:
            site = next(c for c in sites if c["clinic_code"] == b["clinic_code"])
            new_rows.append({
                "bkg_ref": b["booking_id"], "patient": b["patient_id"].replace("P-", ""),
                "centre": site["new_system_code"], "city": b["city"],
                "created": b["date"].strftime("%d/%m/%Y"),
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
        if b["package"]:
            name, price, parts = PACKAGES[b["package"]]
            test_rows.append({"booking_id": b["booking_id"], "test_code": b["package"],
                              "package_code": b["package"], "quantity": qty,
                              "price_each": price, "line": "package"})
            for t in parts:
                test_rows.append({"booking_id": b["booking_id"], "test_code": t,
                                  "package_code": b["package"], "quantity": qty,
                                  "price_each": 0, "line": "component"})
        else:
            for t in b["tests"]:
                test_rows.append({"booking_id": b["booking_id"], "test_code": t,
                                  "package_code": "", "quantity": 1,
                                  "price_each": PRICE[t], "line": "test"})

    invoices, n_inv = [], 0
    for b in bookings:
        if b["status"] != "completed":
            continue
        n_inv += 1
        qty = b.get("quantity", 1)
        if b["package"]:
            amount, items = PACKAGES[b["package"]][1] * qty, 1
        else:
            amount, items = sum(PRICE[t] for t in b["tests"]), len(b["tests"])
        if b["channel"] == "home-collection" and not b["fee_waived"]:
            amount += HOME_FEE
            items += 1
        inv = {"invoice_no": f"KH/26-27/{n_inv:06d}", "booking_id": b["booking_id"],
               "invoice_date": b["date"].isoformat(), "city": b["city"],
               "amount": amount, "line_items": items,
               "corporate_account": CORPORATE["account"] if b["channel"] == "corporate" else ""}
        invoices.append(inv)
    inv_rng = random.Random(SEED + 2)
    for inv in inv_rng.sample(invoices, 60):
        inv["amount"] = f"{inv['amount']:,}"

    payments, n_pay = [], 0
    pay_rng = random.Random(SEED + 3)
    unpaid = set(inv_rng.sample([i["invoice_no"] for i in invoices if not i["corporate_account"]],
                                int(len(invoices) * 0.035)))
    unpaid.add(next(i["invoice_no"] for i in invoices if i["corporate_account"]))
    for inv in invoices:
        if inv["invoice_no"] in unpaid:
            continue
        amount = int(str(inv["amount"]).replace(",", ""))
        digits = inv["invoice_no"].split("/")[-1]
        method = pay_rng.choices(["UPI", "card", "cash"], weights=[55, 25, 20])[0]
        if method == "cash":
            ref = inv["invoice_no"] if pay_rng.random() < 0.10 else f"INV-{int(digits)}"
        else:
            ref = digits
        paid = dt.date.fromisoformat(inv["invoice_date"]) + dt.timedelta(days=pay_rng.randint(0, 6))
        n_pay += 1
        stamp = f"{paid.isoformat()} {pay_rng.randint(8, 21):02d}:{pay_rng.randint(0, 59):02d}"
        row = {"payment_id": f"PAY{n_pay:07d}", "invoice_ref": ref, "method": method,
               "amount": amount, "paid_at": stamp, "status": "success"}
        payments.append(row)
        if method != "cash" and pay_rng.random() < 0.03:
            n_pay += 1
            payments.append(dict(row, payment_id=f"PAY{n_pay:07d}",
                                 paid_at=stamp[:-2] + f"{min(59, int(stamp[-2:]) + 2):02d}"))
        if pay_rng.random() < 0.01:
            n_pay += 1
            payments.append({"payment_id": f"PAY{n_pay:07d}", "invoice_ref": ref, "method": method,
                             "amount": -amount, "paid_at": stamp, "status": "refund"})

    # Appointments at the walk-in clinics in Q2: scheduled visits with attendance, and walk-ins,
    # who by definition came. The small clinic runs almost entirely by appointment.
    appt_rng = random.Random(SEED + 4)
    appointments, n_app = [], 0
    for site in sites:
        if site["kind"] != "walk-in clinic":
            continue
        small = site["clinic_code"] == SMALL_CLINIC
        for d in days(*Q2):
            scheduled = (1 if appt_rng.random() < 0.52 else 0) if small else appt_rng.randint(2, 6)
            walkins = (1 if appt_rng.random() < 0.02 else 0) if small else appt_rng.randint(1, 5)
            for _ in range(scheduled):
                n_app += 1
                p_no = 0.15
                appointments.append({"appointment_id": f"AP{n_app:06d}",
                                     "clinic_code": site["clinic_code"], "visit_date": d.isoformat(),
                                     "kind": "scheduled",
                                     "attended": "N" if appt_rng.random() < p_no else "Y"})
            for _ in range(walkins):
                n_app += 1
                appointments.append({"appointment_id": f"AP{n_app:06d}",
                                     "clinic_code": site["clinic_code"], "visit_date": d.isoformat(),
                                     "kind": "walk-in", "attended": "Y"})
    # Pin the small clinic's no-shows at ten, so the witness numbers hold whatever the draw.
    small_rows = [a for a in appointments if a["clinic_code"] == SMALL_CLINIC and a["kind"] == "scheduled"]
    for k, a in enumerate(sorted(small_rows, key=lambda a: a["appointment_id"])):
        a["attended"] = "N" if k % max(1, len(small_rows) // 10) == 0 and k // max(1, len(small_rows) // 10) < 10 else "Y"

    campaign = [{"patient_id": pid, "city": next(p["city"] for p in people if p["patient_id"] == pid),
                 "offered_on": day.isoformat(), "took_up": "Y" if pid in took_up else "N"}
                for pid, day in sorted(offered.items())]

    tables = {
        "patients": [{k: v for k, v in p.items() if not k.startswith("_")} for p in people],
        "clinics": sites,
        "test_catalogue": ([{"code": c, "name": n, "list_price": pr, "kind": "test"} for c, n, pr in TESTS]
                           + [{"code": c, "name": v[0], "list_price": v[1], "kind": "package"}
                              for c, v in PACKAGES.items()]),
        "bookings_legacy": legacy_out,
        "bookings_newsys": new_rows,
        "booking_tests": test_rows,
        "invoices": invoices,
        "payments": payments,
        "appointments": appointments,
        "campaign": campaign,
    }
    return tables, bookings


# ------------------------------------------------------------------------------------ the witness
def witness(tables, bookings):
    """The numbers the TRAINER files quote, computed from the tables as a learner would."""
    w = {}
    real = {c: {"Q1": 0, "Q2": 0} for c, _ in CITIES}
    for b in bookings:
        q = "Q1" if b["date"] <= Q1[1] else "Q2"
        real[b["city"]][q] += 1
    legacy_q2 = {c: 0 for c, _ in CITIES}
    seen = set()
    for r in tables["bookings_legacy"]:
        if r["booking_id"] in seen:
            continue
        seen.add(r["booking_id"])
        if r["booking_date"] >= Q2[0].isoformat():
            legacy_q2[r["city"]] += 1
    sw_q1 = sum(real[c]["Q1"] for c in SWITCH_CITIES)
    sw_q2_real = sum(real[c]["Q2"] for c in SWITCH_CITIES)
    sw_q2_legacy = sum(legacy_q2[c] for c in SWITCH_CITIES)
    w["switch_cities_q1"] = sw_q1
    w["switch_cities_q2_real"] = sw_q2_real
    w["switch_cities_q2_legacy_only"] = sw_q2_legacy
    w["switch_real_change"] = sw_q2_real / sw_q1 - 1
    w["switch_apparent_change"] = sw_q2_legacy / sw_q1 - 1
    w["legacy_rows"] = len(tables["bookings_legacy"])
    w["legacy_distinct_ids"] = len(seen)
    w["newsys_rows"] = len(tables["bookings_newsys"])

    # Dr Menon's 5 percent is her dashboard's: retail tests booked in the old system only, a
    # package counted as its component tests. The whole business moved faster than that.
    def tests_in(b):
        return len(PACKAGES[b["package"]][2]) if b["package"] else len(b["tests"])
    moved = {k: {"Q1": 0, "Q2": 0} for k in ("dashboard", "booked", "performed", "bookings")}
    for b in bookings:
        if b["channel"] == "corporate":
            continue
        q = "Q1" if b["date"] <= Q1[1] else "Q2"
        moved["booked"][q] += tests_in(b)
        moved["bookings"][q] += 1
        if b["system"] == "legacy":
            moved["dashboard"][q] += tests_in(b)
        if b["status"] == "completed":
            moved["performed"][q] += tests_in(b)
    for k, v in moved.items():
        w[f"{k}_q1_to_q2"] = v["Q2"] / v["Q1"] - 1

    inv = tables["invoices"]
    amounts = [int(str(i["amount"]).replace(",", "")) for i in inv]
    q2 = [a for i, a in zip(inv, amounts) if i["invoice_date"] >= Q2[0].isoformat()]
    q2_no_corp = [a for i, a in zip(inv, amounts)
                  if i["invoice_date"] >= Q2[0].isoformat() and not i["corporate_account"]]
    w["q2_revenue"] = sum(q2)
    w["q2_revenue_without_contract"] = sum(q2_no_corp)
    w["contract_amount"] = CORPORATE["heads"] * CORPORATE["unit"]
    w["contract_share_of_q2"] = w["contract_amount"] / sum(q2)
    w["q2_mean_invoice"] = sum(q2) / len(q2)
    w["q2_mean_without_contract"] = sum(q2_no_corp) / len(q2_no_corp)
    s = sorted(q2)
    w["q2_median_invoice"] = (s[len(s) // 2 - 1] + s[len(s) // 2]) / 2 if len(s) % 2 == 0 else s[len(s) // 2]
    w["text_amounts"] = sum(1 for i in inv if isinstance(i["amount"], str))
    lines = sum(i["line_items"] for i in inv if not i["corporate_account"])
    tests = sum(1 for t in tables["booking_tests"] if t["line"] in ("test", "component")
                and not t["package_code"] == "PKG-CORP")
    w["invoice_lines_non_corporate"] = lines
    w["tests_performed_non_corporate"] = tests

    inv_nos = {i["invoice_no"] for i in inv}
    pays = tables["payments"]
    w["payments_rows"] = len(pays)
    w["exact_join_matches"] = sum(1 for p in pays if p["invoice_ref"] in inv_nos)
    w["exact_join_share"] = w["exact_join_matches"] / len(pays)
    by_digits = {i["invoice_no"].split("/")[-1]: i["invoice_no"] for i in inv}

    def normalise(ref):
        if ref in inv_nos:
            return ref
        if ref.startswith("INV-"):
            return by_digits.get(f"{int(ref[4:]):06d}")
        return by_digits.get(ref)
    matched = [normalise(p["invoice_ref"]) for p in pays]
    w["normalised_join_unmatched"] = sum(1 for m in matched if m is None)
    keys = {}
    for p in pays:
        if p["status"] == "success":
            keys.setdefault((p["invoice_ref"], p["amount"]), []).append(p)
    w["double_posts"] = sum(len(v) - 1 for v in keys.values() if len(v) > 1)
    w["refunds"] = sum(1 for p in pays if p["status"] == "refund")
    paid_invoices = {m for m in matched if m}
    w["unpaid_invoices"] = len(inv_nos - paid_invoices)
    w["corporate_invoice_unpaid"] = any(i["corporate_account"] and i["invoice_no"] not in paid_invoices
                                        for i in inv)

    appts = tables["appointments"]
    small_sched = [a for a in appts if a["clinic_code"] == SMALL_CLINIC and a["kind"] == "scheduled"]
    small_all = [a for a in appts if a["clinic_code"] == SMALL_CLINIC]
    other_sched = [a for a in appts if a["clinic_code"] != SMALL_CLINIC and a["kind"] == "scheduled"]
    other_all = [a for a in appts if a["clinic_code"] != SMALL_CLINIC]
    w["small_clinic_scheduled"] = len(small_sched)
    w["small_clinic_no_shows"] = sum(1 for a in small_sched if a["attended"] == "N")
    w["small_clinic_rate_all_visits"] = sum(1 for a in small_all if a["attended"] == "N") / len(small_all)
    w["others_rate_all_visits"] = sum(1 for a in other_all if a["attended"] == "N") / len(other_all)
    w["small_clinic_rate_scheduled"] = w["small_clinic_no_shows"] / len(small_sched)
    w["others_rate_scheduled"] = sum(1 for a in other_sched if a["attended"] == "N") / len(other_sched)
    n, k, p = len(small_sched), w["small_clinic_no_shows"], w["others_rate_scheduled"]
    w["small_clinic_tail_probability"] = sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j)
                                             for j in range(k, n + 1))

    offered = {c["patient_id"] for c in tables["campaign"]}
    in_window = {}
    for b in bookings:
        if CAMPAIGN[0] <= b["date"] <= CAMPAIGN[1] and b["channel"] != "corporate":
            in_window[b["patient_id"]] = in_window.get(b["patient_id"], 0) + 1
    people = tables["patients"]

    def rate(group):
        return sum(in_window.get(p["patient_id"], 0) for p in group) / max(1, len(group))
    off = [p for p in people if p["patient_id"] in offered]
    rest = [p for p in people if p["patient_id"] not in offered]
    w["offered_patients"] = len(off)
    w["campaign_lift_aggregate"] = rate(off) / rate(rest) - 1
    w["campaign_lift_by_city"] = {c: rate([p for p in off if p["city"] == c])
                                  / rate([p for p in rest if p["city"] == c]) - 1
                                  for c in CAMPAIGN_CITIES}

    def window_count(city_set, lo, hi):
        return sum(1 for b in bookings if b["city"] in city_set and lo <= b["date"] <= hi
                   and b["channel"] != "corporate")
    camp = set(CAMPAIGN_CITIES)
    rest_cities = {c for c, _ in CITIES} - camp - set(SWITCH_CITIES)
    w["campaign_cities_window_change"] = (window_count(camp, *CAMPAIGN)
                                          / window_count(camp, *PRE_CAMPAIGN) - 1)
    w["campaign_cities_prior_change"] = (window_count(camp, *PRE_CAMPAIGN)
                                         / window_count(camp, Q1[0], PRE_CAMPAIGN[0] - dt.timedelta(days=1))
                                         * ((PRE_CAMPAIGN[0] - Q1[0]).days / 62) - 1)
    w["other_cities_window_change"] = (window_count(rest_cities, *CAMPAIGN)
                                       / window_count(rest_cities, *PRE_CAMPAIGN) - 1)
    return w


def check(w):
    """Every plant the spine promises, asserted. Returns the list of failures."""
    fails = []

    def want(ok, text):
        if not ok:
            fails.append(text)
    want(-0.30 <= w["switch_apparent_change"] <= -0.20,
         f"apparent fall in the switch cities {w['switch_apparent_change']:.3f}, wanted -0.30 to -0.20")
    want(-0.16 <= w["switch_real_change"] <= -0.08,
         f"real fall in the switch cities {w['switch_real_change']:.3f}, wanted -0.16 to -0.08")
    share = w["switch_real_change"] / w["switch_apparent_change"]
    want(0.35 <= share <= 0.65, f"the real fall is {share:.2f} of the apparent one, wanted about half")
    want(0.045 <= w["dashboard_q1_to_q2"] <= 0.055,
         f"the dashboard's growth is {w['dashboard_q1_to_q2']:.3f}, and Dr Menon says 5 percent")
    want(w["booked_q1_to_q2"] >= w["dashboard_q1_to_q2"] + 0.02,
         "the old system alone does not understate the growth in tests booked")
    want(w["legacy_rows"] - w["legacy_distinct_ids"] == 180,
         f"legacy duplicates {w['legacy_rows'] - w['legacy_distinct_ids']}, wanted 180")
    want(0.10 <= w["contract_share_of_q2"] <= 0.25,
         f"contract share of Q2 revenue {w['contract_share_of_q2']:.3f}, wanted 0.10 to 0.25")
    want(w["q2_mean_invoice"] >= 1.08 * w["q2_mean_without_contract"],
         "the contract does not move the Q2 mean invoice by 8 percent or more")
    want(w["tests_performed_non_corporate"] >= 1.5 * w["invoice_lines_non_corporate"],
         "packages do not hide at least half again as many tests as invoice lines show")
    want(w["exact_join_share"] <= 0.04, f"exact join matches {w['exact_join_share']:.3f} of payments")
    want(w["normalised_join_unmatched"] == 0, f"{w['normalised_join_unmatched']} payments unmatched after normalising")
    want(w["double_posts"] >= 150, f"only {w['double_posts']} double posts")
    want(w["corporate_invoice_unpaid"], "the corporate invoice has a payment")
    want(40 <= w["small_clinic_scheduled"] <= 60, f"small clinic scheduled {w['small_clinic_scheduled']}")
    want(w["small_clinic_no_shows"] == 10, f"small clinic no-shows {w['small_clinic_no_shows']}")
    want(w["small_clinic_rate_all_visits"] >= 1.8 * w["others_rate_all_visits"],
         "the small clinic's all-visit rate is not about double the others'")
    want(w["small_clinic_tail_probability"] >= 0.10,
         f"the small clinic's gap is not within chance: tail {w['small_clinic_tail_probability']:.3f}")
    want(0.06 <= w["campaign_lift_aggregate"] <= 0.12,
         f"aggregate campaign lift {w['campaign_lift_aggregate']:.3f}, wanted 0.06 to 0.12")
    for city, lift in w["campaign_lift_by_city"].items():
        want(lift < 0, f"{city}: offered patients out-book the rest ({lift:.3f}); the reversal is lost")
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
# A change to TREND that makes Chennai and Pune rise
#     FAIL on the apparent and real falls, and nothing is written.

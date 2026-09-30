"""Recompute the Build 1 witness from the ten CSV files, the way a learner would reach it.

The generator's --witness reads its own tables in memory. The trainer day sheet quotes numbers a
group has to reach from the files it was given, so this script reads only content/W03/D1/data/ and
prints each number beside the spine's figure. Run it from the repository root:

    python3 content/W03/D1/internal/C2_W03_D01_witness_check_INTERNAL.py

It exits 1 if any recomputed number drifts from the spine by more than rounding.
"""
import csv
import datetime as dt
import math
import pathlib
import sys

DATA = pathlib.Path(__file__).resolve().parent.parent / "data"
STEM = "C2_W03_D01_"


def load(name):
    with open(DATA / f"{STEM}{name}_STUDENT.csv", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def iso(d):
    """Both systems' dates as a date: ISO in the old export, day/month/year in the new one."""
    if "/" in d:
        day, month, year = d.split("/")
        return dt.date(int(year), int(month), int(day))
    return dt.date.fromisoformat(d[:10])


def quarter(d):
    return "Q1" if d <= dt.date(2026, 6, 30) else "Q2"


def rupees(text):
    return int(str(text).replace(",", ""))


legacy = load("bookings_legacy")
newsys = load("bookings_newsys")
lines = load("booking_tests")
invoices = load("invoices")
payments = load("payments")
appointments = load("appointments")
campaign = load("campaign")
patients = load("patients")

# One row per booking across both systems, the old export's repeats dropped on the booking id.
bookings, seen = [], set()
for r in legacy:
    if r["booking_id"] in seen:
        continue
    seen.add(r["booking_id"])
    bookings.append({"id": r["booking_id"], "patient": r["patient_id"], "city": r["city"],
                     "date": iso(r["booking_date"]), "channel": r["channel"],
                     "done": r["status"] == "completed", "system": "legacy"})
for r in newsys:
    channel = {"WALKIN": "walk-in", "APP": "app", "CALL": "phone",
               "HOMEVISIT": "home-collection"}[r["channel"]]
    bookings.append({"id": r["bkg_ref"], "patient": "P-" + r["patient"], "city": r["city"],
                     "date": iso(r["created"]), "channel": channel,
                     "done": r["state"] == "DONE", "system": "new"})

tests_on = {}
for t in lines:
    if t["line"] in ("test", "component"):
        tests_on[t["booking_id"]] = tests_on.get(t["booking_id"], 0) + int(t["quantity"])

W = {}
W["legacy_rows"] = len(legacy)
W["legacy_distinct_ids"] = len(seen)
W["newsys_rows"] = len(newsys)

# The headline: four readings of "volume", every one without the corporate contract.
moved = {k: {"Q1": 0, "Q2": 0} for k in ("dashboard", "booked", "performed", "bookings")}
for b in bookings:
    if b["channel"] == "corporate":
        continue
    q = quarter(b["date"])
    n = tests_on.get(b["id"], 0)
    moved["booked"][q] += n
    moved["bookings"][q] += 1
    if b["system"] == "legacy":
        moved["dashboard"][q] += n
    if b["done"]:
        moved["performed"][q] += n
for k, v in moved.items():
    W[f"{k}_Q1"], W[f"{k}_Q2"] = v["Q1"], v["Q2"]
    W[f"{k}_q1_to_q2"] = v["Q2"] / v["Q1"] - 1
corporate_ids = {b["id"] for b in bookings if b["channel"] == "corporate"}
W["corporate_tests"] = sum(tests_on.get(i, 0) for i in corporate_ids)

# 2 Bookings: the two cities that changed systems, as the old export shows them and in truth.
sw = ("Chennai", "Pune")
W["switch_q1"] = sum(1 for b in bookings if b["city"] in sw and quarter(b["date"]) == "Q1")
W["switch_q2_real"] = sum(1 for b in bookings if b["city"] in sw and quarter(b["date"]) == "Q2")
W["switch_q2_legacy_only"] = sum(1 for b in bookings if b["city"] in sw and b["system"] == "legacy"
                                 and quarter(b["date"]) == "Q2")
W["switch_real_change"] = W["switch_q2_real"] / W["switch_q1"] - 1
W["switch_apparent_change"] = W["switch_q2_legacy_only"] / W["switch_q1"] - 1
W["first_new_system_date"] = min(iso(r["created"]) for r in newsys).isoformat()

# 1 Revenue.
q2 = [(i, rupees(i["amount"])) for i in invoices if iso(i["invoice_date"]) >= dt.date(2026, 7, 1)]
amounts = sorted(a for _, a in q2)
no_corp = [a for i, a in q2 if not i["corporate_account"]]
W["q2_revenue"] = sum(amounts)
W["q2_revenue_without_contract"] = sum(no_corp)
W["contract_amount"] = sum(a for i, a in q2 if i["corporate_account"])
W["contract_share_of_q2"] = W["contract_amount"] / W["q2_revenue"]
W["q2_invoices"] = len(amounts)
W["q2_mean_invoice"] = W["q2_revenue"] / len(amounts)
W["q2_mean_without_contract"] = sum(no_corp) / len(no_corp)
mid = len(amounts) // 2
W["q2_median_invoice"] = (amounts[mid] if len(amounts) % 2
                          else (amounts[mid - 1] + amounts[mid]) / 2)
W["text_amounts"] = sum(1 for i in invoices if "," in i["amount"])
W["invoice_lines_non_corporate"] = sum(int(i["line_items"]) for i in invoices
                                       if not i["corporate_account"])
W["tests_performed_non_corporate"] = sum(1 for t in lines if t["line"] in ("test", "component")
                                         and t["package_code"] != "PKG-CORP")

# 3 Billing.
inv_nos = {i["invoice_no"] for i in invoices}
by_digits = {i["invoice_no"].split("/")[-1]: i["invoice_no"] for i in invoices}


def normalise(ref):
    if ref in inv_nos:
        return ref
    if ref.startswith("INV-"):
        return by_digits.get(f"{int(ref[4:]):06d}")
    return by_digits.get(ref)


W["payments_rows"] = len(payments)
W["exact_join_matches"] = sum(1 for p in payments if p["invoice_ref"] in inv_nos)
W["exact_join_share"] = W["exact_join_matches"] / len(payments)
matched = [normalise(p["invoice_ref"]) for p in payments]
W["normalised_join_unmatched"] = sum(1 for m in matched if m is None)
keys = {}
for p in payments:
    if p["status"] == "success":
        keys.setdefault((p["invoice_ref"], p["amount"]), []).append(p)
W["double_posts"] = sum(len(v) - 1 for v in keys.values() if len(v) > 1)
W["refunds"] = sum(1 for p in payments if p["status"] == "refund")
W["unpaid_invoices"] = len(inv_nos - {m for m in matched if m})
corp = [i["invoice_no"] for i in invoices if i["corporate_account"]]
W["corporate_invoice_unpaid"] = all(c not in set(matched) for c in corp)

# 4 No-shows.
small = "KH-HYD-03"


def no_show_rate(rows):
    return sum(1 for a in rows if a["attended"] == "N") / len(rows)


small_all = [a for a in appointments if a["clinic_code"] == small]
other_all = [a for a in appointments if a["clinic_code"] != small]
small_sched = [a for a in small_all if a["kind"] == "scheduled"]
other_sched = [a for a in other_all if a["kind"] == "scheduled"]
W["small_clinic_visits"] = len(small_all)
W["small_clinic_walk_ins"] = sum(1 for a in small_all if a["kind"] == "walk-in")
W["small_clinic_scheduled"] = len(small_sched)
W["small_clinic_no_shows"] = sum(1 for a in small_sched if a["attended"] == "N")
W["small_clinic_rate_all_visits"] = no_show_rate(small_all)
W["others_rate_all_visits"] = no_show_rate(other_all)
W["small_clinic_rate_scheduled"] = no_show_rate(small_sched)
W["others_rate_scheduled"] = no_show_rate(other_sched)
n, k, p = len(small_sched), W["small_clinic_no_shows"], W["others_rate_scheduled"]
W["small_clinic_tail_probability"] = sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j)
                                         for j in range(k, n + 1))

# 5 Campaign: bookings per patient inside the offer's window, offered against not offered.
lo, hi = dt.date(2026, 7, 15), dt.date(2026, 9, 14)
pre_lo, pre_hi = dt.date(2026, 5, 14), dt.date(2026, 7, 14)
in_window = {}
for b in bookings:
    if lo <= b["date"] <= hi and b["channel"] != "corporate":
        in_window[b["patient"]] = in_window.get(b["patient"], 0) + 1
offered = {c["patient_id"] for c in campaign}


def per_patient(group):
    return sum(in_window.get(x["patient_id"], 0) for x in group) / len(group)


off = [x for x in patients if x["patient_id"] in offered]
rest = [x for x in patients if x["patient_id"] not in offered]
W["offered_patients"] = len(off)
W["took_up"] = sum(1 for c in campaign if c["took_up"] == "Y")
W["campaign_lift_aggregate"] = per_patient(off) / per_patient(rest) - 1
camp_cities = ("Bengaluru", "Hyderabad", "Mumbai")
for c in camp_cities:
    W[f"lift_{c}"] = (per_patient([x for x in off if x["city"] == c])
                      / per_patient([x for x in rest if x["city"] == c]) - 1)
W["offered_share_campaign_cities"] = (sum(1 for x in off if x["city"] in camp_cities)
                                      / sum(1 for x in patients if x["city"] in camp_cities))
W["offered_share_other_cities"] = (sum(1 for x in off if x["city"] not in camp_cities)
                                   / sum(1 for x in patients if x["city"] not in camp_cities))


def count(cities, a, b):
    return sum(1 for x in bookings if x["city"] in cities and a <= x["date"] <= b
               and x["channel"] != "corporate")


before_lo = dt.date(2026, 4, 1)
days_before = (pre_lo - before_lo).days
W["campaign_cities_prior_change"] = (count(camp_cities, pre_lo, pre_hi) / 62
                                     / (count(camp_cities, before_lo, pre_lo - dt.timedelta(days=1))
                                        / days_before) - 1)
W["campaign_cities_window_change"] = count(camp_cities, lo, hi) / count(camp_cities, pre_lo, pre_hi) - 1
W["other_cities_window_change"] = (count(("Delhi",), lo, hi) / count(("Delhi",), pre_lo, pre_hi) - 1)

# The spine's figures, rounded as the spine prints them.
SPINE = {
    "dashboard_q1_to_q2": 0.051, "booked_q1_to_q2": 0.078, "performed_q1_to_q2": 0.086,
    "bookings_q1_to_q2": 0.056, "corporate_tests": 6000,
    "contract_amount": 1800000, "contract_share_of_q2": 0.162, "q2_mean_invoice": 1904,
    "q2_mean_without_contract": 1596, "q2_median_invoice": 1499,
    "tests_performed_non_corporate": 48235, "invoice_lines_non_corporate": 22152,
    "switch_apparent_change": -0.230, "switch_real_change": -0.122,
    "legacy_rows": 11729, "legacy_distinct_ids": 11549,
    "exact_join_share": 0.022, "normalised_join_unmatched": 0, "double_posts": 229,
    "refunds": 102, "unpaid_invoices": 398,
    "small_clinic_rate_all_visits": 0.192, "others_rate_all_visits": 0.087,
    "small_clinic_rate_scheduled": 0.200, "small_clinic_no_shows": 10,
    "small_clinic_scheduled": 50, "others_rate_scheduled": 0.152,
    "small_clinic_tail_probability": 0.22, "campaign_lift_aggregate": 0.090,
    "lift_Bengaluru": -0.108, "lift_Hyderabad": -0.199, "lift_Mumbai": -0.130,
    "campaign_cities_prior_change": 0.069,
}

fails = 0
for key, value in W.items():
    want = SPINE.get(key)
    shown = f"{value:.4f}" if isinstance(value, float) else str(value)
    if want is None:
        print(f"      {key}: {shown}")
        continue
    tol = 0.0006 if isinstance(want, float) and abs(want) < 1 else 0.6
    if key == "small_clinic_tail_probability":
        tol = 0.006
    ok = abs(float(value) - want) <= tol
    fails += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {key}: {shown} (spine {want})")
print("RESULT:", "FAIL" if fails else "PASS", f"({fails} drifts from the spine)")
sys.exit(1 if fails else 0)

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W03/D1/internal/C2_W03_D01_witness_check_INTERNAL.py
#     Reads the ten CSV files, prints every number with the spine's figure beside it, and ends on
#     "RESULT: PASS (0 drifts from the spine)" with exit 0 while the data pack is unchanged.
# The same command after the data pack is regenerated with a different seed
#     One FAIL line per number that moved, and exit 1, which means the day sheet's numbers need
#     rewriting before the pack ships again.

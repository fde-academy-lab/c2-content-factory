"""Recompute the Build 1 witness from the ten CSV files, the way a learner would reach it.

The generator's --witness reads its own tables in memory. The trainer day sheet quotes numbers a
group has to reach from the files it was given, so this script reads only content/W03/D1/data/ and
prints each number beside the spine's figure. Run it from the repository root:

    python3 content/W03/D1/internal/C2_W03_D01_witness_check_INTERNAL.py

It exits 1 if any recomputed number drifts from the spine by more than rounding. The files are the
US pack of decision build1-us-data: six metros, claims billed in dollars, remittance postings keyed
in the posting system's own format, and the two quarters as calendar Q2 and Q3 of 2026.
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
    """Both systems' dates as a date: ISO in the old export, month/day/year in the new one."""
    if "/" in d:
        month, day, year = d.split("/")
        return dt.date(int(year), int(month), int(day))
    return dt.date.fromisoformat(d[:10])


def quarter(d):
    return "Q2" if d <= dt.date(2026, 6, 30) else "Q3"


def dollars(text):
    """A billed amount as a number, whether the export wrote 299 or $265.00."""
    return float(str(text).replace("$", "").replace(",", ""))


legacy = load("bookings_legacy")
newsys = load("bookings_newsys")
lines = load("booking_tests")
claims = load("claims")
postings = load("remittances")
appointments = load("appointments")
campaign = load("campaign")
patients = load("patients")

# One row per booking across both systems, the old export's repeats dropped on the booking id.
bookings, seen = [], set()
for r in legacy:
    if r["booking_id"] in seen:
        continue
    seen.add(r["booking_id"])
    bookings.append({"id": r["booking_id"], "patient": r["patient_id"], "metro": r["metro"],
                     "date": iso(r["booking_date"]), "channel": r["channel"],
                     "done": r["status"] == "completed", "system": "legacy"})
for r in newsys:
    channel = {"WALKIN": "walk-in", "WEB": "online", "CALL": "phone",
               "MOBILEDRAW": "at-home"}[r["channel"]]
    bookings.append({"id": r["bkg_ref"], "patient": "P-" + r["patient"], "metro": r["metro"],
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

# The headline: four readings of "volume", every one without the employer contract.
moved = {k: {"Q2": 0, "Q3": 0} for k in ("dashboard", "booked", "performed", "bookings")}
for b in bookings:
    if b["channel"] == "employer":
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
    W[f"{k}_Q2"], W[f"{k}_Q3"] = v["Q2"], v["Q3"]
    W[f"{k}_q2_to_q3"] = v["Q3"] / v["Q2"] - 1
employer_ids = {b["id"] for b in bookings if b["channel"] == "employer"}
W["employer_tests"] = sum(tests_on.get(i, 0) for i in employer_ids)

# 2 Bookings: the two metros that changed systems, as the old export shows them and in truth.
sw = ("Chicago", "Philadelphia")
W["switch_q2"] = sum(1 for b in bookings if b["metro"] in sw and quarter(b["date"]) == "Q2")
W["switch_q3_real"] = sum(1 for b in bookings if b["metro"] in sw and quarter(b["date"]) == "Q3")
W["switch_q3_legacy_only"] = sum(1 for b in bookings if b["metro"] in sw and b["system"] == "legacy"
                                 and quarter(b["date"]) == "Q3")
W["switch_real_change"] = W["switch_q3_real"] / W["switch_q2"] - 1
W["switch_apparent_change"] = W["switch_q3_legacy_only"] / W["switch_q2"] - 1
W["first_new_system_date"] = min(iso(r["created"]) for r in newsys).isoformat()

# 1 Revenue, as billed charges on the claims.
q3 = [(c, dollars(c["billed_amount"])) for c in claims if iso(c["service_date"]) >= dt.date(2026, 7, 1)]
amounts = sorted(a for _, a in q3)
no_emp = [a for c, a in q3 if not c["employer_account"]]
W["q3_billed"] = sum(amounts)
W["q3_billed_without_contract"] = sum(no_emp)
W["contract_amount"] = sum(a for c, a in q3 if c["employer_account"])
W["contract_share_of_q3"] = W["contract_amount"] / W["q3_billed"]
W["q3_claims"] = len(amounts)
W["q3_mean_claim"] = W["q3_billed"] / len(amounts)
W["q3_mean_without_contract"] = sum(no_emp) / len(no_emp)
mid = len(amounts) // 2
W["q3_median_claim"] = (amounts[mid] if len(amounts) % 2
                        else (amounts[mid - 1] + amounts[mid]) / 2)
W["text_amounts"] = sum(1 for c in claims if not c["billed_amount"].isdigit())
W["claim_lines_non_employer"] = sum(int(c["line_items"]) for c in claims if not c["employer_account"])
completed = {b["id"] for b in bookings if b["done"]}
test_rows = [t for t in lines if t["line"] in ("test", "component") and t["panel_code"] != "PNL-EMP"]
W["tests_booked_non_employer"] = len(test_rows)
W["tests_on_claimed_bookings_non_employer"] = sum(1 for t in test_rows if t["booking_id"] in completed)

# The payer mix and the denials, over the retail claims (the employer bill is neither).
retail = [c for c in claims if not c["employer_account"]]
for payer in ("commercial", "Medicare", "Medicaid", "self-pay"):
    of_payer = [c for c in retail if c["payer_type"] == payer]
    W[f"payer_share_{payer}"] = len(of_payer) / len(retail)
    W[f"denial_rate_{payer}"] = sum(1 for c in of_payer if c["denial_category"]) / len(of_payer)
denied = [c for c in retail if c["denial_category"]]
W["denial_rate_retail"] = len(denied) / len(retail)
W["denied_billed"] = sum(dollars(c["billed_amount"]) for c in denied)
W["denial_categories"] = len({c["denial_category"] for c in denied})

# 3 Billing: the claims against the posting system.
claim_ids = {c["claim_id"] for c in claims}
by_digits = {c["claim_id"].split("-")[-1]: c["claim_id"] for c in claims}


def normalise(ref):
    if ref in claim_ids:
        return ref
    if ref.startswith("CLM-"):
        return by_digits.get(f"{int(ref[4:]):06d}")
    return by_digits.get(ref)


W["remittance_rows"] = len(postings)
W["exact_join_matches"] = sum(1 for p in postings if p["claim_ref"] in claim_ids)
W["exact_join_share"] = W["exact_join_matches"] / len(postings)
matched = [normalise(p["claim_ref"]) for p in postings]
W["normalised_join_unmatched"] = sum(1 for m in matched if m is None)
keys = {}
for p in postings:
    if p["posting"] == "payment":
        keys.setdefault((p["claim_ref"], p["paid_amount"]), []).append(p)
doubles = [p for v in keys.values() if len(v) > 1 for p in v[1:]]
W["double_posts"] = len(doubles)
W["double_posted_dollars"] = sum(float(p["paid_amount"]) for p in doubles)
W["reversals"] = sum(1 for p in postings if p["posting"] == "reversal")
W["denial_postings"] = sum(1 for p in postings if p["posting"] == "denial")
W["claims_without_posting"] = len(claim_ids - {m for m in matched if m})
employer = [c["claim_id"] for c in claims if c["employer_account"]]
W["employer_invoice_unpaid"] = all(c not in set(matched) for c in employer)
W["paid_net_of_double_posts"] = sum(float(p["paid_amount"]) for p in postings) - W["double_posted_dollars"]
W["billed_all"] = sum(dollars(c["billed_amount"]) for c in claims)

# 4 No-shows.
small = "KH-ATL-03"


def no_show_rate(rows):
    return sum(1 for a in rows if a["attended"] == "N") / len(rows)


small_all = [a for a in appointments if a["site_code"] == small]
other_all = [a for a in appointments if a["site_code"] != small]
small_sched = [a for a in small_all if a["kind"] == "scheduled"]
other_sched = [a for a in other_all if a["kind"] == "scheduled"]
W["small_site_visits"] = len(small_all)
W["small_site_walk_ins"] = sum(1 for a in small_all if a["kind"] == "walk-in")
W["small_site_scheduled"] = len(small_sched)
W["small_site_no_shows"] = sum(1 for a in small_sched if a["attended"] == "N")
W["small_site_rate_all_visits"] = no_show_rate(small_all)
W["others_rate_all_visits"] = no_show_rate(other_all)
W["small_site_rate_scheduled"] = no_show_rate(small_sched)
W["others_rate_scheduled"] = no_show_rate(other_sched)
n, k, p = len(small_sched), W["small_site_no_shows"], W["others_rate_scheduled"]
W["small_site_tail_probability"] = sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j)
                                       for j in range(k, n + 1))

# 5 Campaign: bookings per patient inside the offer's window, offered against not offered.
lo, hi = dt.date(2026, 7, 15), dt.date(2026, 9, 14)
pre_lo, pre_hi = dt.date(2026, 5, 14), dt.date(2026, 7, 14)
in_window = {}
for b in bookings:
    if lo <= b["date"] <= hi and b["channel"] != "employer":
        in_window[b["patient"]] = in_window.get(b["patient"], 0) + 1
offered = {c["patient_id"] for c in campaign}


def per_patient(group):
    return sum(in_window.get(x["patient_id"], 0) for x in group) / len(group)


off = [x for x in patients if x["patient_id"] in offered]
rest = [x for x in patients if x["patient_id"] not in offered]
W["offered_patients"] = len(off)
W["took_up"] = sum(1 for c in campaign if c["took_up"] == "Y")
W["campaign_lift_aggregate"] = per_patient(off) / per_patient(rest) - 1
camp_metros = ("Dallas", "Atlanta", "Phoenix")
for m in camp_metros:
    W[f"lift_{m}"] = (per_patient([x for x in off if x["metro"] == m])
                      / per_patient([x for x in rest if x["metro"] == m]) - 1)
W["offered_share_campaign_metros"] = (sum(1 for x in off if x["metro"] in camp_metros)
                                      / sum(1 for x in patients if x["metro"] in camp_metros))
W["offered_share_other_metros"] = (sum(1 for x in off if x["metro"] not in camp_metros)
                                   / sum(1 for x in patients if x["metro"] not in camp_metros))


def count(metros, a, b):
    return sum(1 for x in bookings if x["metro"] in metros and a <= x["date"] <= b
               and x["channel"] != "employer")


before_lo = dt.date(2026, 4, 1)
days_before = (pre_lo - before_lo).days
W["campaign_metros_prior_change"] = (count(camp_metros, pre_lo, pre_hi) / 62
                                     / (count(camp_metros, before_lo, pre_lo - dt.timedelta(days=1))
                                        / days_before) - 1)
W["campaign_metros_window_change"] = count(camp_metros, lo, hi) / count(camp_metros, pre_lo, pre_hi) - 1
W["other_metros_window_change"] = (count(("New York",), lo, hi) / count(("New York",), pre_lo, pre_hi) - 1)

# The spine's figures, rounded as the spine prints them.
SPINE = {
    "dashboard_q2_to_q3": 0.051, "booked_q2_to_q3": 0.078, "performed_q2_to_q3": 0.086,
    "bookings_q2_to_q3": 0.056, "employer_tests": 6000,
    "contract_amount": 180000, "contract_share_of_q3": 0.146, "q3_billed": 1231001,
    "q3_mean_claim": 210.50, "q3_mean_without_contract": 179.75, "q3_median_claim": 150,
    "text_amounts": 60, "tests_booked_non_employer": 48235,
    "tests_on_claimed_bookings_non_employer": 46867, "claim_lines_non_employer": 22152,
    "payer_share_commercial": 0.539, "payer_share_Medicare": 0.239, "payer_share_Medicaid": 0.145,
    "payer_share_self-pay": 0.077,
    "switch_apparent_change": -0.230, "switch_real_change": -0.122,
    "legacy_rows": 11729, "legacy_distinct_ids": 11549,
    "exact_join_share": 0.019, "normalised_join_unmatched": 0, "double_posts": 280,
    "double_posted_dollars": 19204.63, "reversals": 105, "claims_without_posting": 398,
    "denial_postings": 1137, "denial_rate_retail": 0.104, "denial_rate_Medicaid": 0.149,
    "denial_rate_commercial": 0.113, "denial_rate_Medicare": 0.088, "denial_rate_self-pay": 0.0,
    "denied_billed": 230132, "paid_net_of_double_posts": 801314, "billed_all": 2201099,
    "small_site_rate_all_visits": 0.192, "others_rate_all_visits": 0.087,
    "small_site_rate_scheduled": 0.200, "small_site_no_shows": 10,
    "small_site_scheduled": 50, "others_rate_scheduled": 0.152,
    "small_site_tail_probability": 0.22, "campaign_lift_aggregate": 0.090,
    "lift_Dallas": -0.108, "lift_Atlanta": -0.199, "lift_Phoenix": -0.130,
    "campaign_metros_prior_change": 0.069,
}

fails = 0
for key, value in W.items():
    want = SPINE.get(key)
    shown = f"{value:.4f}" if isinstance(value, float) else str(value)
    if want is None:
        print(f"      {key}: {shown}")
        continue
    tol = 0.0006 if isinstance(want, float) and abs(want) < 1 else 0.6
    if key == "small_site_tail_probability":
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

"""Recompute, from the ten Kalpa Health CSV files alone, every number the Saturday TRAINER files quote.

    python3 content/W03/SAT/internal/C2_W03_SAT_witness_INTERNAL.py
    python3 content/W03/SAT/internal/C2_W03_SAT_witness_INTERNAL.py --data content/W03/D1/data

The generator's --witness reads its own in-memory tables. This script reads only the files a group
holds, the way a group would, so the panel's numbers are the numbers a careful group can reach. The
last lines compare each figure against the approved spine's witness and print PASS or FAIL.
"""
import math
import pathlib
import sys

import pandas as pd

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent.parent / "D1" / "data"
if "--data" in sys.argv:
    DATA = pathlib.Path(sys.argv[sys.argv.index("--data") + 1])
STEM = "C2_W03_D01_"


def load(name, **kw):
    return pd.read_csv(DATA / f"{STEM}{name}_STUDENT.csv", **kw)


Q1 = ("2026-04-01", "2026-06-30")
Q2 = ("2026-07-01", "2026-09-30")
CAMPAIGN = ("2026-07-15", "2026-09-14")
PRE = ("2026-05-14", "2026-07-14")
SWITCH = ["Chennai", "Pune"]
CAMPAIGN_CITIES = ["Bengaluru", "Hyderabad", "Mumbai"]


def quarter(d):
    return "Q1" if d <= Q1[1] else "Q2"


def pct(x):
    return f"{x * 100:+.1f} percent"


out = {}

# ---- Bookings: the old export de-duplicated, plus the new system mapped onto the old codes ----
legacy_raw = load("bookings_legacy")
legacy = legacy_raw.drop_duplicates("booking_id")
out["legacy_rows"] = len(legacy_raw)
out["legacy_repeated_rows"] = len(legacy_raw) - len(legacy)
dups = legacy_raw[legacy_raw.booking_id.duplicated()]
out["repeated_rows_first_date"] = dups.booking_date.min()
out["repeated_rows_last_date"] = dups.booking_date.max()
exact_dup_rows = legacy_raw.duplicated().sum()
out["repeated_rows_identical_on_every_field"] = int(exact_dup_rows)

clinics = load("clinics", dtype=str)
new_to_old = dict(zip(clinics.new_system_code.dropna(), clinics.dropna(subset=["new_system_code"]).clinic_code))
newsys = load("bookings_newsys", dtype=str)
out["newsys_rows"] = len(newsys)
out["newsys_first_date"] = pd.to_datetime(newsys.created, format="%d/%m/%Y").min().date().isoformat()
out["switch_cities_last_legacy_date"] = legacy[legacy.city.isin(SWITCH)].booking_date.max()
new = pd.DataFrame({
    "booking_id": newsys.bkg_ref,
    "patient_id": "P-" + newsys.patient,
    "clinic_code": newsys.centre.map(new_to_old),
    "city": newsys.city,
    "booking_date": pd.to_datetime(newsys.created, format="%d/%m/%Y").dt.strftime("%Y-%m-%d"),
    "channel": newsys.channel.map({"WALKIN": "walk-in", "APP": "app", "CALL": "phone", "HOMEVISIT": "home-collection"}),
    "status": newsys.state.map({"DONE": "completed", "CXL": "cancelled"}),
    "system": "new",
})
legacy = legacy.assign(system="legacy")
bookings = pd.concat([legacy[new.columns], new], ignore_index=True)
bookings["q"] = bookings.booking_date.map(quarter)

# ---- Sub-problem 2: the two cities that moved systems ----
by_city = bookings.groupby(["city", "q"]).size().unstack()
legacy_city = legacy.assign(q=legacy.booking_date.map(quarter)).groupby(["city", "q"]).size().unstack()
sw_q1 = int(by_city.loc[SWITCH, "Q1"].sum())
sw_q2_true = int(by_city.loc[SWITCH, "Q2"].sum())
sw_q2_old = int(legacy_city.loc[SWITCH, "Q2"].sum())
out["switch_q1"] = sw_q1
out["switch_q2_old_export"] = sw_q2_old
out["switch_q2_both_systems"] = sw_q2_true
out["switch_change_old_export"] = sw_q2_old / sw_q1 - 1
out["switch_change_both_systems"] = sw_q2_true / sw_q1 - 1
for c in SWITCH:
    out[f"{c}_q1"] = int(by_city.loc[c, "Q1"])
    out[f"{c}_q2_old_export"] = int(legacy_city.loc[c, "Q2"])
    out[f"{c}_q2_both_systems"] = int(by_city.loc[c, "Q2"])
    out[f"{c}_change_old_export"] = legacy_city.loc[c, "Q2"] / by_city.loc[c, "Q1"] - 1
    out[f"{c}_change_both_systems"] = by_city.loc[c, "Q2"] / by_city.loc[c, "Q1"] - 1
for c in ["Bengaluru", "Mumbai", "Delhi", "Hyderabad"]:
    out[f"{c}_bookings_change"] = by_city.loc[c, "Q2"] / by_city.loc[c, "Q1"] - 1

# ---- The headline: four honest readings of "test volumes" ----
bt = load("booking_tests")
tests_rows = bt[bt.line.isin(["test", "component"])]
tests_per_booking = tests_rows.groupby("booking_id").quantity.sum()
b = bookings.assign(tests=bookings.booking_id.map(tests_per_booking).fillna(0))
retail = b[b.channel != "corporate"]


def growth(frame, col=None):
    g = frame.groupby("q")[col].sum() if col else frame.groupby("q").size()
    return g["Q2"] / g["Q1"] - 1, int(g["Q1"]), int(g["Q2"])


out["dashboard_tests_change"], out["dashboard_q1"], out["dashboard_q2"] = growth(retail[retail.system == "legacy"], "tests")
out["booked_tests_change"], out["booked_q1"], out["booked_q2"] = growth(retail, "tests")
out["performed_tests_change"], out["performed_q1"], out["performed_q2"] = growth(retail[retail.status == "completed"], "tests")
out["bookings_change"], out["bookings_q1"], out["bookings_q2"] = growth(retail)
corp = b[b.channel == "corporate"]
out["corporate_bookings"] = len(corp)
out["corporate_tests"] = int(corp.tests.sum())
out["corporate_date"] = corp.booking_date.iloc[0]
out["corporate_clinic"] = corp.clinic_code.iloc[0]
perf = b[b.status == "completed"].groupby("q").tests.sum()
out["performed_tests_change_with_contract"] = perf["Q2"] / perf["Q1"] - 1

# ---- Sub-problem 1: revenue ----
inv = load("invoices", dtype=str)
inv["amt"] = inv.amount.str.replace(",", "", regex=False).astype(int)
out["amounts_written_with_commas"] = int(inv.amount.str.contains(",").sum())
inv["q"] = inv.invoice_date.map(quarter)
rev = inv.groupby("q").amt.sum()
q2 = inv[inv.q == "Q2"]
q2_nc = q2[q2.corporate_account.isna()]
out["q1_revenue"] = int(rev["Q1"])
out["q2_revenue"] = int(rev["Q2"])
out["q2_revenue_without_contract"] = int(q2_nc.amt.sum())
out["contract_amount"] = int(q2[q2.corporate_account.notna()].amt.sum())
out["contract_share_of_q2"] = out["contract_amount"] / out["q2_revenue"]
out["revenue_change"] = rev["Q2"] / rev["Q1"] - 1
out["revenue_change_without_contract"] = out["q2_revenue_without_contract"] / rev["Q1"] - 1
out["q2_invoices"] = len(q2)
out["q2_mean_invoice"] = q2.amt.mean()
out["q2_mean_without_contract"] = q2_nc.amt.mean()
out["q2_median_invoice"] = q2.amt.median()
out["q2_median_without_contract"] = q2_nc.amt.median()
out["invoice_lines_non_corporate"] = int(inv[inv.corporate_account.isna()].line_items.astype(int).sum())
out["test_rows_non_corporate"] = int(len(tests_rows[tests_rows.package_code != "PKG-CORP"]))
city_rev = inv[inv.corporate_account.isna()].groupby(["city", "q"]).amt.sum().unstack()
for c in city_rev.index:
    out[f"{c}_revenue_change_without_contract"] = city_rev.loc[c, "Q2"] / city_rev.loc[c, "Q1"] - 1

# ---- Sub-problem 3: invoices against the payment feed ----
pay = load("payments", dtype=str)
inv_nos = set(inv.invoice_no)
by_digits = {n.split("/")[-1]: n for n in inv.invoice_no}


def normalise(ref):
    if ref in inv_nos:
        return ref
    if ref.startswith("INV-"):
        return by_digits.get(f"{int(ref[4:]):06d}")
    return by_digits.get(ref)


pay["inv"] = pay.invoice_ref.map(normalise)
out["payment_rows"] = len(pay)
out["refs_in_invoice_format"] = int(pay.invoice_ref.isin(inv_nos).sum())
out["refs_inv_prefixed"] = int(pay.invoice_ref.str.startswith("INV-").sum())
out["refs_bare_digits"] = int(pay.invoice_ref.str.fullmatch(r"\d+").sum())
out["exact_join_share"] = out["refs_in_invoice_format"] / len(pay)
out["unmatched_after_normalising"] = int(pay.inv.isna().sum())
ok = pay[pay.status == "success"]
out["double_posts"] = int(ok.duplicated(["invoice_ref", "amount"]).sum())
out["double_post_value"] = int(ok[ok.duplicated(["invoice_ref", "amount"])].amount.astype(int).sum())
out["refunds"] = int((pay.status == "refund").sum())
out["refund_value"] = int(pay[pay.status == "refund"].amount.astype(int).abs().sum())
unpaid = inv[~inv.invoice_no.isin(set(pay.inv.dropna()))]
out["unpaid_invoices"] = len(unpaid)
out["unpaid_value"] = int(unpaid.amt.sum())
out["unpaid_value_without_contract"] = int(unpaid[unpaid.corporate_account.isna()].amt.sum())
out["corporate_invoice_unpaid"] = bool(unpaid.corporate_account.notna().any())
out["collected_success_total"] = int(ok.amount.astype(int).sum())
out["invoiced_total"] = int(inv.amt.sum())

# ---- Sub-problem 4: no-shows ----
ap = load("appointments")
ap["ns"] = ap.attended.eq("N")
all_rate = ap.groupby("clinic_code").ns.mean()
sched = ap[ap.kind == "scheduled"]
small = "KH-HYD-03"
out["small_clinic"] = small
out["small_clinic_visits"] = int((ap.clinic_code == small).sum())
out["small_clinic_walk_ins"] = int(((ap.clinic_code == small) & (ap.kind == "walk-in")).sum())
out["small_rate_all_visits"] = ap[ap.clinic_code == small].ns.mean()
out["others_rate_all_visits"] = ap[ap.clinic_code != small].ns.mean()
n = int((sched.clinic_code == small).sum())
k = int(sched[sched.clinic_code == small].ns.sum())
p = sched[sched.clinic_code != small].ns.mean()
out["small_scheduled"] = n
out["small_no_shows"] = k
out["small_rate_scheduled"] = k / n
out["others_rate_scheduled"] = p
out["walk_in_no_shows"] = int(ap[ap.kind == "walk-in"].ns.sum())
out["tail_probability"] = sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k, n + 1))
out["highest_other_clinic_rate_all_visits"] = all_rate.drop(small).max()

# ---- Sub-problem 5: the free home-collection offer ----
camp = load("campaign")
patients = load("patients")
offered = set(camp.patient_id)
win = retail[(retail.booking_date >= CAMPAIGN[0]) & (retail.booking_date <= CAMPAIGN[1])]
per_patient = win.groupby("patient_id").size()
patients["n"] = patients.patient_id.map(per_patient).fillna(0)
patients["offered"] = patients.patient_id.isin(offered)
r = patients.groupby("offered").n.mean()
out["offered_patients"] = len(offered)
out["offered_took_up"] = int(camp.took_up.eq("Y").sum())
out["offer_dates"] = f"{camp.offered_on.min()} to {camp.offered_on.max()}"
out["campaign_lift_aggregate"] = r[True] / r[False] - 1
for c in ["Bengaluru", "Hyderabad", "Mumbai", "Delhi", "Chennai", "Pune"]:
    s = patients[patients.city == c].groupby("offered").n.mean()
    out[f"{c}_offered_share"] = patients[patients.city == c].offered.mean()
    out[f"{c}_lift"] = s[True] / s[False] - 1


def window(cities, lo, hi):
    return len(retail[retail.city.isin(cities) & (retail.booking_date >= lo) & (retail.booking_date <= hi)])


before = window(CAMPAIGN_CITIES, *PRE)
during = window(CAMPAIGN_CITIES, *CAMPAIGN)
earlier = window(CAMPAIGN_CITIES, Q1[0], "2026-05-13")
out["campaign_cities_window_change"] = during / before - 1
out["campaign_cities_prior_change"] = before / earlier * (43 / 62) - 1
out["delhi_window_change"] = window(["Delhi"], *CAMPAIGN) / window(["Delhi"], *PRE) - 1

# ---- Supporting figures the question bank quotes beyond the spine's table ----
sw_raw = legacy_raw[(legacy_raw.booking_date >= Q2[0]) & legacy_raw.city.isin(SWITCH)]
out["switch_q2_old_export_with_repeats"] = len(sw_raw)
pay["t"] = pd.to_datetime(pay.paid_at)
ok_t = pay[pay.status == "success"]
groups = ok_t.groupby(["invoice_ref", "amount"]).t
spread = (groups.max() - groups.min()).dt.total_seconds() / 60
out["double_post_max_gap_minutes"] = float(spread[groups.size() > 1].max())
out["paid_invoice_value"] = out["invoiced_total"] - out["unpaid_value"]
out["net_collected"] = out["collected_success_total"] - out["double_post_value"] - out["refund_value"]
delhi = patients[patients.city == "Delhi"]
out["delhi_offered"] = int(delhi.offered.sum())
out["delhi_not_offered"] = int((~delhi.offered).sum())
z_a, z_b, p0, p1 = 1.96, 0.8416, out["others_rate_scheduled"], out["small_rate_scheduled"]
out["appointments_to_detect_gap"] = ((z_a * math.sqrt(p0 * (1 - p0)) + z_b * math.sqrt(p1 * (1 - p1)))
                                     / (p1 - p0)) ** 2

for key, value in out.items():
    if isinstance(value, float):
        print(f"{key}: {value:.4f}")
    else:
        print(f"{key}: {value}")

SPINE = {
    "dashboard_tests_change": 0.051, "booked_tests_change": 0.078, "performed_tests_change": 0.086,
    "bookings_change": 0.056, "contract_amount": 1800000, "contract_share_of_q2": 0.162,
    "q2_mean_invoice": 1904, "q2_mean_without_contract": 1596, "q2_median_invoice": 1499,
    "test_rows_non_corporate": 48235, "invoice_lines_non_corporate": 22152,
    "switch_change_old_export": -0.230, "switch_change_both_systems": -0.122, "legacy_repeated_rows": 180,
    "exact_join_share": 0.022, "unmatched_after_normalising": 0, "double_posts": 229, "refunds": 102,
    "unpaid_invoices": 398, "small_rate_all_visits": 0.192, "others_rate_all_visits": 0.087,
    "small_rate_scheduled": 0.200, "others_rate_scheduled": 0.152, "tail_probability": 0.224,
    "campaign_lift_aggregate": 0.090, "Bengaluru_lift": -0.108, "Hyderabad_lift": -0.199,
    "Mumbai_lift": -0.130, "campaign_cities_prior_change": 0.069, "corporate_tests": 6000,
}
fails = 0
print()
for key, want in SPINE.items():
    got = out[key]
    tol = 0.5 if want > 2 else 0.0006
    good = abs(got - want) <= tol
    fails += not good
    print(f"{'PASS' if good else 'FAIL'}  {key}: files {got:.4f}, spine {want}")
print(f"\nRESULT: {'PASS' if not fails else 'FAIL'} ({fails} disagreements with the spine)")
sys.exit(1 if fails else 0)

# Test inputs and expected outcomes.
# 1. No arguments, run from anywhere: reads content/W03/D1/data beside this day, prints every figure
#    and ends "RESULT: PASS (0 disagreements with the spine)".
# 2. --data content/W03/D1/data: the same output, from the path given.
# 3. --data pointing at a folder without the files: FileNotFoundError naming the first missing CSV.
# 4. After the generator's seed changes, the comparison lines turn to FAIL for every moved plant and
#    the exit code is 1, which is the signal to re-read every TRAINER number in this day.

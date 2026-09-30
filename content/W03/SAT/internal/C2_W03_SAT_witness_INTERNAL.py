"""Recompute, from the ten Kalpa Health CSV files alone, every number the Saturday TRAINER files quote.

    python3 content/W03/SAT/internal/C2_W03_SAT_witness_INTERNAL.py
    python3 content/W03/SAT/internal/C2_W03_SAT_witness_INTERNAL.py --data content/W03/D1/data

The generator's --witness reads its own in-memory tables. This script reads only the files a group
holds, the way a group would, so the panel's numbers are the numbers a careful group can reach. The
last lines compare each figure against the approved spine's witness and print PASS or FAIL. The files
are the US pack of decision build1-us-data: six metros, claims billed in dollars, remittance
postings, and the quarters as calendar Q2 (April to June) and Q3 (July to September) of 2026.
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


Q2 = ("2026-04-01", "2026-06-30")
Q3 = ("2026-07-01", "2026-09-30")
CAMPAIGN = ("2026-07-15", "2026-09-14")
PRE = ("2026-05-14", "2026-07-14")
SWITCH = ["Chicago", "Philadelphia"]
CAMPAIGN_METROS = ["Dallas", "Atlanta", "Phoenix"]


def quarter(d):
    return "Q2" if d <= Q2[1] else "Q3"


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

sites = load("sites", dtype=str)
new_to_old = dict(zip(sites.new_system_code.dropna(), sites.dropna(subset=["new_system_code"]).site_code))
newsys = load("bookings_newsys", dtype=str)
out["newsys_rows"] = len(newsys)
out["newsys_first_date"] = pd.to_datetime(newsys.created, format="%m/%d/%Y").min().date().isoformat()
out["switch_metros_last_legacy_date"] = legacy[legacy.metro.isin(SWITCH)].booking_date.max()
new = pd.DataFrame({
    "booking_id": newsys.bkg_ref,
    "patient_id": "P-" + newsys.patient,
    "site_code": newsys.site.map(new_to_old),
    "metro": newsys.metro,
    "booking_date": pd.to_datetime(newsys.created, format="%m/%d/%Y").dt.strftime("%Y-%m-%d"),
    "channel": newsys.channel.map({"WALKIN": "walk-in", "WEB": "online", "CALL": "phone", "MOBILEDRAW": "at-home"}),
    "status": newsys.state.map({"DONE": "completed", "CXL": "cancelled"}),
    "system": "new",
})
legacy = legacy.assign(system="legacy")
bookings = pd.concat([legacy[new.columns], new], ignore_index=True)
bookings["q"] = bookings.booking_date.map(quarter)

# ---- Sub-problem 2: the two metros that moved systems ----
by_metro = bookings.groupby(["metro", "q"]).size().unstack()
legacy_metro = legacy.assign(q=legacy.booking_date.map(quarter)).groupby(["metro", "q"]).size().unstack()
sw_q2 = int(by_metro.loc[SWITCH, "Q2"].sum())
sw_q3_true = int(by_metro.loc[SWITCH, "Q3"].sum())
sw_q3_old = int(legacy_metro.loc[SWITCH, "Q3"].sum())
out["switch_q2"] = sw_q2
out["switch_q3_old_export"] = sw_q3_old
out["switch_q3_both_systems"] = sw_q3_true
out["switch_change_old_export"] = sw_q3_old / sw_q2 - 1
out["switch_change_both_systems"] = sw_q3_true / sw_q2 - 1
for c in SWITCH:
    out[f"{c}_q2"] = int(by_metro.loc[c, "Q2"])
    out[f"{c}_q3_old_export"] = int(legacy_metro.loc[c, "Q3"])
    out[f"{c}_q3_both_systems"] = int(by_metro.loc[c, "Q3"])
    out[f"{c}_change_old_export"] = legacy_metro.loc[c, "Q3"] / by_metro.loc[c, "Q2"] - 1
    out[f"{c}_change_both_systems"] = by_metro.loc[c, "Q3"] / by_metro.loc[c, "Q2"] - 1
for c in ["Dallas", "Phoenix", "New York", "Atlanta"]:
    out[f"{c}_bookings_change"] = by_metro.loc[c, "Q3"] / by_metro.loc[c, "Q2"] - 1

# ---- The headline: four honest readings of "test volumes" ----
bt = load("booking_tests")
tests_rows = bt[bt.line.isin(["test", "component"])]
tests_per_booking = tests_rows.groupby("booking_id").quantity.sum()
b = bookings.assign(tests=bookings.booking_id.map(tests_per_booking).fillna(0))
retail = b[b.channel != "employer"]


def growth(frame, col=None):
    g = frame.groupby("q")[col].sum() if col else frame.groupby("q").size()
    return g["Q3"] / g["Q2"] - 1, int(g["Q2"]), int(g["Q3"])


out["dashboard_tests_change"], out["dashboard_q2"], out["dashboard_q3"] = growth(retail[retail.system == "legacy"], "tests")
out["booked_tests_change"], out["booked_q2"], out["booked_q3"] = growth(retail, "tests")
out["performed_tests_change"], out["performed_q2"], out["performed_q3"] = growth(retail[retail.status == "completed"], "tests")
out["bookings_change"], out["bookings_q2"], out["bookings_q3"] = growth(retail)
emp = b[b.channel == "employer"]
out["employer_bookings"] = len(emp)
out["employer_tests"] = int(emp.tests.sum())
out["employer_date"] = emp.booking_date.iloc[0]
out["employer_site"] = emp.site_code.iloc[0]
perf = b[b.status == "completed"].groupby("q").tests.sum()
out["performed_tests_change_with_contract"] = perf["Q3"] / perf["Q2"] - 1

# ---- Sub-problem 1: revenue, as billed charges on the claims ----
cl = load("claims", dtype=str)
cl["amt"] = cl.billed_amount.str.replace("$", "", regex=False).str.replace(",", "", regex=False).astype(float)
out["amounts_written_as_text"] = int((~cl.billed_amount.str.fullmatch(r"\d+")).sum())
cl["q"] = cl.service_date.map(quarter)
rev = cl.groupby("q").amt.sum()
q3 = cl[cl.q == "Q3"]
q3_nc = q3[q3.employer_account.isna()]
out["q2_billed"] = int(rev["Q2"])
out["q3_billed"] = int(rev["Q3"])
out["q3_billed_without_contract"] = int(q3_nc.amt.sum())
out["contract_amount"] = int(q3[q3.employer_account.notna()].amt.sum())
out["contract_share_of_q3"] = out["contract_amount"] / out["q3_billed"]
out["billed_change"] = rev["Q3"] / rev["Q2"] - 1
out["billed_change_without_contract"] = out["q3_billed_without_contract"] / rev["Q2"] - 1
out["q3_claims"] = len(q3)
out["q3_mean_claim"] = q3.amt.mean()
out["q3_mean_without_contract"] = q3_nc.amt.mean()
out["q3_median_claim"] = q3.amt.median()
out["q3_median_without_contract"] = q3_nc.amt.median()
out["claim_lines_non_employer"] = int(cl[cl.employer_account.isna()].line_items.astype(int).sum())
out["test_rows_non_employer"] = int(len(tests_rows[tests_rows.panel_code != "PNL-EMP"]))
metro_rev = cl[cl.employer_account.isna()].groupby(["metro", "q"]).amt.sum().unstack()
for c in metro_rev.index:
    out[f"{c}_billed_change_without_contract"] = metro_rev.loc[c, "Q3"] / metro_rev.loc[c, "Q2"] - 1
retail_claims = cl[cl.employer_account.isna()]
out["denial_rate_retail"] = retail_claims.denial_category.notna().mean()
for payer in ["commercial", "Medicare", "Medicaid", "self-pay"]:
    of_payer = retail_claims[retail_claims.payer_type == payer]
    out[f"payer_share_{payer}"] = len(of_payer) / len(retail_claims)
    out[f"denial_rate_{payer}"] = of_payer.denial_category.notna().mean()

# ---- Sub-problem 3: the claims against the posting system ----
pay = load("remittances", dtype=str)
claim_ids = set(cl.claim_id)
by_digits = {n.split("-")[-1]: n for n in cl.claim_id}


def normalise(ref):
    if ref in claim_ids:
        return ref
    if ref.startswith("CLM-"):
        return by_digits.get(f"{int(ref[4:]):06d}")
    return by_digits.get(ref)


pay["claim"] = pay.claim_ref.map(normalise)
pay["paid"] = pay.paid_amount.astype(float)
out["remittance_rows"] = len(pay)
out["refs_in_claim_format"] = int(pay.claim_ref.isin(claim_ids).sum())
out["refs_clm_prefixed"] = int(pay.claim_ref.str.startswith("CLM-").sum())
out["refs_bare_digits"] = int(pay.claim_ref.str.fullmatch(r"\d+").sum())
out["exact_join_share"] = out["refs_in_claim_format"] / len(pay)
out["unmatched_after_normalising"] = int(pay.claim.isna().sum())
ok = pay[pay.posting == "payment"]
out["double_posts"] = int(ok.duplicated(["claim_ref", "paid_amount"]).sum())
out["double_post_value"] = round(float(ok[ok.duplicated(["claim_ref", "paid_amount"])].paid.sum()), 2)
out["reversals"] = int((pay.posting == "reversal").sum())
out["reversal_value"] = round(float(pay[pay.posting == "reversal"].paid.abs().sum()), 2)
out["denial_postings"] = int((pay.posting == "denial").sum())
unpaid = cl[~cl.claim_id.isin(set(pay.claim.dropna()))]
out["claims_without_posting"] = len(unpaid)
out["unposted_value"] = int(unpaid.amt.sum())
out["unposted_value_without_contract"] = int(unpaid[unpaid.employer_account.isna()].amt.sum())
out["employer_invoice_unpaid"] = bool(unpaid.employer_account.notna().any())
out["paid_on_payment_postings"] = round(float(ok.paid.sum()), 2)
out["billed_total"] = int(cl.amt.sum())

# ---- Sub-problem 4: no-shows ----
ap = load("appointments")
ap["ns"] = ap.attended.eq("N")
all_rate = ap.groupby("site_code").ns.mean()
sched = ap[ap.kind == "scheduled"]
small = "KH-ATL-03"
out["small_site"] = small
out["small_site_visits"] = int((ap.site_code == small).sum())
out["small_site_walk_ins"] = int(((ap.site_code == small) & (ap.kind == "walk-in")).sum())
out["small_rate_all_visits"] = ap[ap.site_code == small].ns.mean()
out["others_rate_all_visits"] = ap[ap.site_code != small].ns.mean()
n = int((sched.site_code == small).sum())
k = int(sched[sched.site_code == small].ns.sum())
p = sched[sched.site_code != small].ns.mean()
out["small_scheduled"] = n
out["small_no_shows"] = k
out["small_rate_scheduled"] = k / n
out["others_rate_scheduled"] = p
out["walk_in_no_shows"] = int(ap[ap.kind == "walk-in"].ns.sum())
out["tail_probability"] = sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k, n + 1))
out["highest_other_site_rate_all_visits"] = all_rate.drop(small).max()

# ---- Sub-problem 5: the free at-home collection offer ----
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
for c in ["Dallas", "Atlanta", "Phoenix", "New York", "Chicago", "Philadelphia"]:
    s = patients[patients.metro == c].groupby("offered").n.mean()
    out[f"{c}_offered_share"] = patients[patients.metro == c].offered.mean()
    out[f"{c}_lift"] = s[True] / s[False] - 1


def window(metros, lo, hi):
    return len(retail[retail.metro.isin(metros) & (retail.booking_date >= lo) & (retail.booking_date <= hi)])


before = window(CAMPAIGN_METROS, *PRE)
during = window(CAMPAIGN_METROS, *CAMPAIGN)
earlier = window(CAMPAIGN_METROS, Q2[0], "2026-05-13")
out["campaign_metros_window_change"] = during / before - 1
out["campaign_metros_prior_change"] = before / earlier * (43 / 62) - 1
out["new_york_window_change"] = window(["New York"], *CAMPAIGN) / window(["New York"], *PRE) - 1

# ---- Supporting figures the question bank quotes beyond the spine's table ----
sw_raw = legacy_raw[(legacy_raw.booking_date >= Q3[0]) & legacy_raw.metro.isin(SWITCH)]
out["switch_q3_old_export_with_repeats"] = len(sw_raw)
pay["t"] = pd.to_datetime(pay.posted_at)
ok_t = pay[pay.posting == "payment"]
groups = ok_t.groupby(["claim_ref", "paid_amount"]).t
spread = (groups.max() - groups.min()).dt.total_seconds() / 60
out["double_post_max_gap_minutes"] = float(spread[groups.size() > 1].max())
out["posted_claim_value"] = out["billed_total"] - out["unposted_value"]
out["net_collected"] = round(out["paid_on_payment_postings"] - out["double_post_value"] - out["reversal_value"], 2)
new_york = patients[patients.metro == "New York"]
out["new_york_offered"] = int(new_york.offered.sum())
out["new_york_not_offered"] = int((~new_york.offered).sum())
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
    "bookings_change": 0.056, "contract_amount": 180000, "contract_share_of_q3": 0.146,
    "q3_billed": 1231001, "q3_mean_claim": 210.50, "q3_mean_without_contract": 179.75,
    "q3_median_claim": 150, "amounts_written_as_text": 60,
    "test_rows_non_employer": 48235, "claim_lines_non_employer": 22152,
    "switch_change_old_export": -0.230, "switch_change_both_systems": -0.122, "legacy_repeated_rows": 180,
    "exact_join_share": 0.019, "unmatched_after_normalising": 0, "double_posts": 280,
    "double_post_value": 19204.63, "reversals": 105, "denial_postings": 1137,
    "claims_without_posting": 398, "net_collected": 801314, "billed_total": 2201099,
    "denial_rate_retail": 0.104, "denial_rate_Medicaid": 0.149, "denial_rate_commercial": 0.113,
    "denial_rate_Medicare": 0.088, "payer_share_commercial": 0.539, "payer_share_Medicare": 0.239,
    "payer_share_Medicaid": 0.145, "payer_share_self-pay": 0.077,
    "small_rate_all_visits": 0.192, "others_rate_all_visits": 0.087,
    "small_rate_scheduled": 0.200, "others_rate_scheduled": 0.152, "tail_probability": 0.224,
    "campaign_lift_aggregate": 0.090, "Dallas_lift": -0.108, "Atlanta_lift": -0.199,
    "Phoenix_lift": -0.130, "campaign_metros_prior_change": 0.069, "employer_tests": 6000,
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

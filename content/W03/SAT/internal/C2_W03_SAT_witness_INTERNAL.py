"""Recompute, from the ten Kalpa Health CSV files alone, every number the Saturday TRAINER files quote.

    python3 content/W03/SAT/internal/C2_W03_SAT_witness_INTERNAL.py
    python3 content/W03/SAT/internal/C2_W03_SAT_witness_INTERNAL.py --data content/W03/D1/data

The generator's --witness reads its own tables in memory. This script reads only the files a group
holds, the way a group would, so the panel's numbers are numbers a careful group can reach. The files
are the US pack of decision build1-us-data: six metros, claims billed in dollars, remittance postings
keyed in the posting system's own format, and calendar Q2 (April to June) and Q3 (July to September)
of 2026. The visit register is drawn from the bookings (decision build1-register-from-bookings,
1 October 2026), so sub-problem 4's numbers are the spine's re-planted row.

Three tables close the run. SPINE holds the figures of the approved spine,
docs/detailing/W03_build1_spine.md, rounded as the spine prints them. BANK holds every further figure
the panel's question bank, the closure run sheet and the week-close notes quote, rounded as those
files print them. FACTS holds the dates, ids and yes-or-no findings those files state. A figure
passes when it agrees to the last place the table prints, so $19,204.63 must match to the cent and
0.146 to the third decimal; the chance checks, which shuffle, carry the wider tolerance in LOOSE.
Each line prints PASS or FAIL beside the files' value, and the last line reads RESULT: PASS only
when every one agrees.
"""
import math
import pathlib
import sys

import numpy as np
import pandas as pd

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent.parent / "D1" / "data"
if "--data" in sys.argv:
    DATA = pathlib.Path(sys.argv[sys.argv.index("--data") + 1])
STEM = "C2_W03_D01_"


def load(name):
    return pd.read_csv(DATA / f"{STEM}{name}_STUDENT.csv", dtype=str, keep_default_na=False)


Q2_END = "2026-06-30"
OFFER = ("2026-07-15", "2026-09-14")
PRE = ("2026-05-14", "2026-07-14")
SWITCH = ["Chicago", "Philadelphia"]
CAMPAIGN_METROS = ["Dallas", "Atlanta", "Phoenix"]
METROS = ["Dallas", "Phoenix", "New York", "Chicago", "Atlanta", "Philadelphia"]
SMALL = "KH-ATL-03"


def quarter(day):
    return "Q2" if day <= Q2_END else "Q3"


def dollars(text):
    """A billed amount as a number, whether the export wrote 299 or $265.00."""
    return float(str(text).replace("$", "").replace(",", ""))


def tail(n, k, p):
    """The chance of k or more events in n tries at rate p, the binomial check of Week 1 Thursday."""
    return sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k, n + 1))


W, B = {}, {}

# ---- The bookings: the old export once per booking id, plus the new system mapped onto old codes ----
legacy_raw = load("bookings_legacy")
legacy = legacy_raw.drop_duplicates("booking_id").assign(system="legacy")
sites = load("sites")
new_to_old = dict(zip(sites.new_system_code[sites.new_system_code != ""],
                      sites.site_code[sites.new_system_code != ""]))
newsys = load("bookings_newsys")
new = pd.DataFrame({
    "booking_id": newsys.bkg_ref,
    "patient_id": "P-" + newsys.patient,
    "site_code": newsys.site.map(new_to_old),
    "metro": newsys.metro,
    "booking_date": pd.to_datetime(newsys.created, format="%m/%d/%Y").dt.strftime("%Y-%m-%d"),
    "channel": newsys.channel.map({"WALKIN": "walk-in", "WEB": "online", "CALL": "phone",
                                   "MOBILEDRAW": "at-home"}),
    "status": newsys.state.map({"DONE": "completed", "CXL": "cancelled"}),
    "system": "new",
})
cols = list(new.columns)
bookings = pd.concat([legacy[cols], new], ignore_index=True)
bookings["q"] = bookings.booking_date.map(quarter)
retail = bookings[bookings.channel != "employer"]

B["legacy_rows"] = len(legacy_raw)
B["legacy_distinct_ids"] = legacy_raw.booking_id.nunique()
copies = legacy_raw[legacy_raw.booking_id.duplicated(keep=False)].groupby("booking_id")
B["repeated_ids"] = copies.ngroups
B["repeated_first_date"] = legacy_raw[legacy_raw.booking_id.duplicated()].booking_date.min()
B["repeated_last_date"] = legacy_raw[legacy_raw.booking_id.duplicated()].booking_date.max()
B["repeated_pairs_identical"] = int(legacy_raw.duplicated().sum())
B["repeated_pairs_differing_in_updated_at"] = int((copies.updated_at.nunique() > 1).sum())
B["repeated_pairs_differing_in_channel"] = int((copies.channel.nunique() > 1).sum())
B["repeated_pairs_differing_in_both"] = int(((copies.updated_at.nunique() > 1)
                                            & (copies.channel.nunique() > 1)).sum())
B["legacy_rows_with_no_channel"] = int((legacy_raw.channel == "").sum())
B["newsys_rows"] = len(newsys)
B["newsys_Chicago"] = int((newsys.metro == "Chicago").sum())
B["newsys_Philadelphia"] = int((newsys.metro == "Philadelphia").sum())
B["newsys_first_date"] = newsys.created.min()
B["newsys_last_date"] = newsys.created.max()
B["switch_metros_last_old_export_date"] = legacy[legacy.metro.isin(SWITCH)].booking_date.max()
# The caveat check a group can run: does any booking sit in both systems, by id or by patient and date?
B["ids_in_both_systems"] = len(set(new.booking_id) & set(legacy.booking_id))
B["patient_and_date_in_both_systems"] = len(new.merge(legacy, on=["patient_id", "booking_date"]))

# ---- The headline: four readings of "test volumes", every one without the employer contract ----
lines = load("booking_tests")
lines["quantity"] = lines.quantity.astype(int)
test_lines = lines[lines.line.isin(["test", "component"])]
tests_on = test_lines.groupby("booking_id").quantity.sum()
b = bookings.assign(tests=bookings.booking_id.map(tests_on).fillna(0).astype(int))
rb = b[b.channel != "employer"]


def two_quarters(frame, col=None):
    g = frame.groupby("q")[col].sum() if col else frame.groupby("q").size()
    return int(g["Q2"]), int(g["Q3"]), g["Q3"] / g["Q2"] - 1


B["dashboard_Q2"], B["dashboard_Q3"], W["dashboard_change"] = two_quarters(rb[rb.system == "legacy"], "tests")
B["booked_Q2"], B["booked_Q3"], W["booked_change"] = two_quarters(rb, "tests")
B["performed_Q2"], B["performed_Q3"], W["performed_change"] = two_quarters(rb[rb.status == "completed"], "tests")
B["bookings_Q2"], B["bookings_Q3"], W["bookings_change"] = two_quarters(rb)
raw = legacy_raw[legacy_raw.channel != "employer"].assign(
    q=lambda f: f.booking_date.map(quarter), tests=lambda f: f.booking_id.map(tests_on).fillna(0))
raw_q = raw.groupby("q").tests.sum()
B["dashboard_raw_rows_Q2"], B["dashboard_raw_rows_Q3"] = int(raw_q["Q2"]), int(raw_q["Q3"])
B["dashboard_raw_rows_change"] = raw_q["Q3"] / raw_q["Q2"] - 1
emp = b[b.channel == "employer"]
W["employer_tests"] = int(emp.tests.sum())
B["employer_screenings"] = int(lines[lines.panel_code == "PNL-EMP"].quantity.max())
B["employer_tests_per_screening"] = int(((lines.panel_code == "PNL-EMP") & (lines.line == "component")).sum())
B["employer_booking_date"] = emp.booking_date.iloc[0]
B["employer_site"] = emp.site_code.iloc[0]
B["booked_change_with_contract"] = (B["booked_Q3"] + W["employer_tests"]) / B["booked_Q2"] - 1
B["performed_change_with_contract"] = (B["performed_Q3"] + W["employer_tests"]) / B["performed_Q2"] - 1

# ---- Sub-problem 1: billed charges on the claims ----
claims = load("claims")
claims["amt"] = claims.billed_amount.map(dollars)
claims["q"] = claims.service_date.map(quarter)
contract = claims[claims.employer_account != ""]
retail_claims = claims[claims.employer_account == ""]
B["contract_claim"] = contract.claim_id.iloc[0]
B["contract_account"] = contract.employer_account.iloc[0]
B["contract_metro"] = contract.metro.iloc[0]
B["contract_service_date"] = contract.service_date.iloc[0]
W["contract_amount"] = contract.amt.sum()
by_q = claims.groupby("q").amt
W["q3_billed"] = by_q.sum()["Q3"]
B["q2_billed"] = by_q.sum()["Q2"]
B["q3_billed_without_contract"] = retail_claims[retail_claims.q == "Q3"].amt.sum()
W["contract_share_of_q3"] = W["contract_amount"] / W["q3_billed"]
B["billed_change_with_contract"] = W["q3_billed"] / B["q2_billed"] - 1
B["billed_change_without_contract"] = B["q3_billed_without_contract"] / B["q2_billed"] - 1
W["q3_mean_claim"] = by_q.mean()["Q3"]
W["q3_mean_without_contract"] = retail_claims[retail_claims.q == "Q3"].amt.mean()
W["q3_median_claim"] = by_q.median()["Q3"]
B["q2_median_claim"] = by_q.median()["Q2"]
B["second_largest_claim"] = claims.amt.nlargest(2).iloc[-1]
B["q2_mean_claim"] = by_q.mean()["Q2"]
B["q2_claims"] = int(by_q.size()["Q2"])
B["q3_retail_claims"] = int((retail_claims.q == "Q3").sum())
B["retail_claims_change"] = B["q3_retail_claims"] / B["q2_claims"] - 1
B["billed_per_retail_claim_change"] = W["q3_mean_without_contract"] / B["q2_mean_claim"] - 1
W["text_amounts"] = int((~claims.billed_amount.str.fullmatch(r"\d+")).sum())
text = claims[~claims.billed_amount.str.fullmatch(r"\d+")]
B["text_amount_dollars"] = text.amt.sum()
B["text_amounts_Q2"], B["text_amounts_Q3"] = int((text.q == "Q2").sum()), int((text.q == "Q3").sum())
W["claim_lines_non_employer"] = int(retail_claims.line_items.astype(int).sum())
non_emp_tests = test_lines[test_lines.panel_code != "PNL-EMP"]
W["tests_booked_non_employer"] = int(non_emp_tests.quantity.sum())
completed = set(b[b.status == "completed"].booking_id)
W["tests_on_claimed_bookings_non_employer"] = int(non_emp_tests[non_emp_tests.booking_id.isin(completed)]
                                                  .quantity.sum())
priced = lines[lines.line.isin(["test", "panel"])].assign(
    d=lambda f: f.price_each.astype(float) * f.quantity).groupby("booking_id").d.sum()
fee = claims[(claims.amt - claims.booking_id.map(priced).fillna(0) - 20).abs() < 1e-6]
B["fee_lines"] = len(fee)
B["fee_dollars_Q2"] = 20 * int((fee.q == "Q2").sum())
B["fee_dollars_Q3"] = 20 * int((fee.q == "Q3").sum())
B["claim_lines_tests_or_panels"] = W["claim_lines_non_employer"] - B["fee_lines"]
metro_rev = retail_claims.groupby(["metro", "q"]).amt.sum().unstack()
for m in METROS:
    B[f"billed_change_{m}"] = metro_rev.loc[m, "Q3"] / metro_rev.loc[m, "Q2"] - 1
payer_rev = retail_claims.groupby(["payer_type", "q"]).amt.sum().unstack()
for p in ["commercial", "Medicare", "Medicaid", "self-pay"]:
    B[f"billed_change_{p}"] = payer_rev.loc[p, "Q3"] / payer_rev.loc[p, "Q2"] - 1
    of_payer = retail_claims[retail_claims.payer_type == p]
    W[f"payer_share_{p}"] = len(of_payer) / len(retail_claims)
    W[f"denial_rate_{p}"] = (of_payer.denial_category != "").mean()
B["retail_claims"] = len(retail_claims)

# How much of the shortfall against the plan of 18 each branch explains: what Q3 would have been at 18
# percent above Q2, less what Q3 was, in billed dollars on retail claims and in tests performed.
patients = load("patients")
B["patients_with_no_payer"] = int((patients.payer_type == "").sum())


def shortfall(frame, by, col):
    g = frame.groupby([by, "q"])[col].sum().unstack()
    short = g["Q2"] * 1.18 - g["Q3"]
    return short, short.sum()


short, B["shortfall_dollars"] = shortfall(retail_claims, "metro", "amt")
for k, v in short.items():
    B[f"shortfall_dollars_{k}"] = round(float(v))
    B[f"shortfall_share_{k}"] = v / B["shortfall_dollars"]
B["shortfall_share_Chicago_and_Philadelphia"] = B["shortfall_share_Chicago"] + B["shortfall_share_Philadelphia"]
short, _ = shortfall(retail_claims, "payer_type", "amt")
for k, v in short.items():
    B[f"shortfall_dollars_{k}"] = round(float(v))
    B[f"shortfall_share_{k}"] = v / B["shortfall_dollars"]
B["shortfall_share_Medicaid_and_self-pay"] = B["shortfall_share_Medicaid"] + B["shortfall_share_self-pay"]
done = rb[rb.status == "completed"].merge(patients[["patient_id", "payer_type"]], on="patient_id", how="left")
for by in ("metro", "payer_type"):
    short, total = shortfall(done, by, "tests")
    B["shortfall_tests"] = total
    for k, v in short.items():
        B[f"shortfall_tests_share_{k}"] = v / total

# ---- Sub-problem 2: the two metros that moved booking systems ----
old_q = legacy.assign(q=legacy.booking_date.map(quarter))
old_q = old_q[old_q.channel != "employer"]
for m in METROS:
    q2 = int(((rb.metro == m) & (rb.q == "Q2")).sum())
    q3_both = int(((rb.metro == m) & (rb.q == "Q3")).sum())
    q3_old = int(((old_q.metro == m) & (old_q.q == "Q3")).sum())
    B[f"bookings_{m}_Q2"], B[f"bookings_{m}_Q3_both"], B[f"bookings_{m}_Q3_old"] = q2, q3_both, q3_old
    B[f"bookings_{m}_change_both"] = q3_both / q2 - 1
    B[f"bookings_{m}_change_old"] = q3_old / q2 - 1
B["switch_Q2"] = B["bookings_Chicago_Q2"] + B["bookings_Philadelphia_Q2"]
B["switch_Q3_old"] = B["bookings_Chicago_Q3_old"] + B["bookings_Philadelphia_Q3_old"]
B["switch_Q3_both"] = B["bookings_Chicago_Q3_both"] + B["bookings_Philadelphia_Q3_both"]
W["switch_change_old"] = B["switch_Q3_old"] / B["switch_Q2"] - 1
W["switch_change_both"] = B["switch_Q3_both"] / B["switch_Q2"] - 1
W["repeated_ids"] = B["repeated_ids"]
sw_raw = legacy_raw[legacy_raw.metro.isin(SWITCH)].assign(q=lambda f: f.booking_date.map(quarter))
B["switch_Q2_old_rows_with_repeats"] = int((sw_raw.q == "Q2").sum())
B["switch_Q3_old_rows_with_repeats"] = int((sw_raw.q == "Q3").sum())
B["switch_change_old_rows_with_repeats"] = B["switch_Q3_old_rows_with_repeats"] / B["switch_Q2_old_rows_with_repeats"] - 1

# ---- Sub-problem 3: the claims against the posting system ----
post = load("remittances")
post["paid"] = post.paid_amount.astype(float)
claim_ids = set(claims.claim_id)
by_digits = {c.split("-")[-1]: c for c in claims.claim_id}


def normalise(ref):
    if ref in claim_ids:
        return ref
    if ref.startswith("CLM-"):
        return by_digits.get(f"{int(ref[4:]):06d}")
    return by_digits.get(ref)


post["claim"] = post.claim_ref.map(normalise)
B["postings"] = len(post)
B["refs_as_claim_ids"] = int(post.claim_ref.isin(claim_ids).sum())
B["refs_as_CLM_numbers"] = int(post.claim_ref.str.startswith("CLM-").sum())
B["refs_as_bare_digits"] = int(post.claim_ref.str.fullmatch(r"\d+").sum())
W["exact_join_share"] = B["refs_as_claim_ids"] / len(post)
W["unmatched_after_normalising"] = int(post.claim.isna().sum())
pay = post[post.posting == "payment"]
dup_mask = pay.duplicated(["claim_ref", "paid_amount"])
W["double_posts"] = int(dup_mask.sum())
W["double_posted_dollars"] = round(float(pay[dup_mask].paid.sum()), 2)
pairs = pay[pay.duplicated(["claim_ref", "paid_amount"], keep=False)].assign(
    t=lambda f: pd.to_datetime(f.posted_at)).groupby(["claim_ref", "paid_amount"]).t
gap_minutes = (pairs.max() - pairs.min()).dt.total_seconds() / 60
B["double_post_gap_minutes_max"] = float(gap_minutes.max())
B["double_post_gap_minutes_min"] = float(gap_minutes.min())
for gap in (0, 1, 2):
    B[f"double_posts_{gap}_minutes_apart"] = int((gap_minutes == gap).sum())
B["double_posts_same_channel_ERA"] = int((pay[dup_mask].channel == "ERA").sum())
W["reversals"] = int((post.posting == "reversal").sum())
B["reversal_dollars"] = round(float(-post[post.posting == "reversal"].paid.sum()), 2)
W["denial_postings"] = int((post.posting == "denial").sum())
B["denial_postings_paying_nothing"] = int(((post.posting == "denial") & (post.paid == 0)).sum())
posted = set(post.claim.dropna())
unposted = claims[~claims.claim_id.isin(posted)]
W["claims_without_posting"] = len(unposted)
B["unposted_dollars"] = unposted.amt.sum()
B["unposted_without_contract"] = len(unposted[unposted.employer_account == ""])
B["unposted_dollars_without_contract"] = unposted[unposted.employer_account == ""].amt.sum()
B["unposted_months"] = unposted.service_date.str[:7].nunique()
B["employer_claim_unposted"] = bool((unposted.employer_account != "").any())
denied = retail_claims[retail_claims.denial_category != ""]
B["claims_marked_denied"] = len(denied)
W["denial_rate_retail"] = len(denied) / len(retail_claims)
W["denied_billed"] = denied.amt.sum()
B["denied_claims_with_no_posting"] = int((~denied.claim_id.isin(posted)).sum())
for cat, n in denied.denial_category.value_counts().items():
    B[f"denials_{cat}"] = int(n)
B["denial_rate_retail_printed"] = W["denial_rate_retail"]
B["paid_raw_sum"] = round(float(post.paid.sum()), 2)
B["paid_on_payment_postings"] = round(float(pay.paid.sum()), 2)
W["paid_net_of_double_posts"] = round(B["paid_raw_sum"] - W["double_posted_dollars"], 2)
W["billed_all"] = claims.amt.sum()
B["paid_share_of_billed"] = W["paid_net_of_double_posts"] / W["billed_all"]
kept = post[~((post.posting == "payment") & post.duplicated(["claim_ref", "paid_amount"]))]
kept_pay = kept[kept.posting == "payment"]
B["gap_billed_less_paid"] = round(W["billed_all"] - W["paid_net_of_double_posts"], 2)
B["gap_contractual"] = round(float(kept_pay[kept_pay.reason_category == "contractual adjustment"]
                                   .adjustment_amount.astype(float).sum()), 2)
B["gap_no_posting"] = B["unposted_dollars"]
denial_claims = set(post[post.posting == "denial"].claim)
B["gap_denied_with_posting"] = claims[claims.claim_id.isin(denial_claims)].amt.sum()
B["gap_patient_shares"] = round(float(kept_pay.patient_responsibility.astype(float).sum()), 2)
B["gap_reversals"] = B["reversal_dollars"]
B["gap_parts_sum"] = round(B["gap_contractual"] + B["gap_no_posting"] + B["gap_denied_with_posting"]
                           + B["gap_patient_shares"] + B["gap_reversals"], 2)

# The money to chase, at what the payers' contracts allow: each payer's allowed amount over billed
# on the claims it paid, applied to the claims still unpaid. The employer invoice counts in full.
paid_claims = kept_pay.merge(claims[["claim_id", "payer_type", "amt"]], left_on="claim", right_on="claim_id")
allowed = (paid_claims.groupby("payer_type").allowed_amount.apply(lambda c: c.astype(float).sum())
           / paid_claims.groupby("payer_type").amt.sum())
for p, r in allowed.items():
    B[f"allowed_share_of_billed_{p}"] = r
unposted_retail = unposted[unposted.employer_account == ""]
B["unposted_retail_at_contract"] = round(float((unposted_retail.amt * unposted_retail.payer_type.map(allowed)).sum()), 2)
denied_posted = claims[claims.claim_id.isin(denial_claims)]
B["denied_with_posting_at_contract"] = round(float((denied_posted.amt * denied_posted.payer_type.map(allowed)).sum()), 2)
shares = kept_pay.assign(pr=kept_pay.patient_responsibility.astype(float))
shares = shares[shares.pr > 0].merge(claims[["claim_id", "payer_type"]], left_on="claim", right_on="claim_id")
B["patient_balance_claims"] = len(shares)
B["patient_balances_commercial_share"] = shares[shares.payer_type == "commercial"].pr.sum() / shares.pr.sum()
reversed_claims = set(post[post.posting == "reversal"].claim)
B["reversed_claims"] = len(reversed_claims)
B["reversed_claims_billed"] = claims[claims.claim_id.isin(reversed_claims)].amt.sum()
net_paid = kept.groupby("claim").paid.sum()
B["reversed_claims_largest_net_paid"] = round(float(net_paid.reindex(list(reversed_claims)).abs().max()), 2)
B["unposted_at_contract_with_employer"] = round(B["unposted_retail_at_contract"] + W["contract_amount"], 2)
B["chase_at_contract_before_denials"] = round(B["unposted_retail_at_contract"] + W["contract_amount"]
                                              + B["gap_patient_shares"] + B["reversal_dollars"], 2)
co = kept[kept.adjustment_group == "CO"].assign(adj=lambda f: f.adjustment_amount.astype(float))
B["co_adjustments_on_kept_postings"] = round(float(co.adj.sum()), 2)
B["co_adjustments_on_denials"] = round(float(co[co.posting == "denial"].adj.sum()), 2)

# ---- Sub-problem 4: no-shows, on the register drawn from the bookings ----
ap = load("appointments")
ap["ns"] = ap.attended.eq("N")
small_all, other_all = ap[ap.site_code == SMALL], ap[ap.site_code != SMALL]
sched = ap[ap.kind == "scheduled"]
small_s, other_s = sched[sched.site_code == SMALL], sched[sched.site_code != SMALL]
B["register_rows"] = len(ap)
B["register_centres"] = ap.site_code.nunique()
W["small_site_visits"] = len(small_all)
W["small_site_walk_ins"] = int((small_all.kind == "walk-in").sum())
W["small_site_scheduled"] = len(small_s)
W["small_site_no_shows"] = int(small_s.ns.sum())
W["small_rate_all_visits"] = small_all.ns.mean()
W["others_rate_all_visits"] = other_all.ns.mean()
W["small_rate_scheduled"] = small_s.ns.mean()
W["others_rate_scheduled"] = other_s.ns.mean()
W["tail_probability"] = tail(len(small_s), W["small_site_no_shows"], W["others_rate_scheduled"])
B["tail_probability_all_visits"] = tail(len(small_all), int(small_all.ns.sum()), W["others_rate_all_visits"])
B["walk_in_rows"] = int((ap.kind == "walk-in").sum())
B["walk_in_rows_other_centres"] = int(((ap.kind == "walk-in") & (ap.site_code != SMALL)).sum())
B["no_shows_all"] = int(ap.ns.sum())
B["walk_in_no_shows"] = int(ap[ap.kind == "walk-in"].ns.sum())
B["next_worst_rate_all_visits"] = other_all.groupby("site_code").ns.mean().max()
B["next_worst_rate_scheduled"] = other_s.groupby("site_code").ns.mean().max()
slots = sched.groupby("booking_id")
B["bookings_with_two_slots"] = int((slots.size() == 2).sum())
two_slot = slots.size()[slots.size() == 2].index
B["no_shows_on_rebooked_bookings"] = int(sched[sched.booking_id.isin(two_slot)].ns.sum())
per_booking = slots.agg(site=("site_code", "first"), missed=("ns", "any"))
small_bk, other_bk = per_booking[per_booking.site == SMALL], per_booking[per_booking.site != SMALL]
B["small_scheduled_bookings"] = len(small_bk)
B["small_bookings_missing_a_slot"] = int(small_bk.missed.sum())
B["others_share_missing_a_slot"] = other_bk.missed.mean()
B["tail_probability_per_booking"] = tail(len(small_bk), B["small_bookings_missing_a_slot"],
                                         B["others_share_missing_a_slot"])
# Scheduled visits a centre would need before a gap this size reads as real at the usual 5 percent
# two-sided level with 80 percent power: the normal approximation to the one-sample binomial test.
p0, p1 = W["others_rate_scheduled"], W["small_rate_scheduled"]
B["visits_to_detect_gap"] = ((1.96 * math.sqrt(p0 * (1 - p0)) + 0.8416 * math.sqrt(p1 * (1 - p1)))
                             / (p1 - p0)) ** 2
B["quarters_to_detect_gap"] = B["visits_to_detect_gap"] / W["small_site_scheduled"]


def at_least(n, k, p):
    """The binomial tail on a log scale, for the large n of the power check."""
    return sum(math.exp(math.lgamma(n + 1) - math.lgamma(j + 1) - math.lgamma(n - j + 1)
                        + j * math.log(p) + (n - j) * math.log(1 - p)) for j in range(k, n + 1))


# The same 712 slots under the exact binomial test at 2.5 percent in the upper tail: its power.
n712 = round(B["visits_to_detect_gap"])
cut = next(k for k in range(n712 + 1) if at_least(n712, k, p0) <= 0.025)
B["exact_power_at_712"] = at_least(n712, cut, p1)
# With the other centres' own rate counted as an estimate, as they keep adding slots at their pace.
r = len(other_s) / len(small_s)
pooled = (p1 + r * p0) / (1 + r)
B["visits_to_detect_gap_two_sample"] = ((1.96 * math.sqrt(pooled * (1 - pooled) * (1 + 1 / r))
                                         + 0.8416 * math.sqrt(p1 * (1 - p1) + p0 * (1 - p0) / r))
                                        / (p1 - p0)) ** 2
B["other_centres_scheduled_slots"] = len(other_s)

# ---- Sub-problem 5: the free at-home collection offer ----
camp = load("campaign")
offered = set(camp.patient_id)
win = rb[(rb.booking_date >= OFFER[0]) & (rb.booking_date <= OFFER[1])]
patients["n"] = patients.patient_id.map(win.groupby("patient_id").size()).fillna(0)
before = rb[(rb.booking_date >= "2026-04-01") & (rb.booking_date < OFFER[0])]
patients["before"] = patients.patient_id.map(before.groupby("patient_id").size()).fillna(0)
patients["offered"] = patients.patient_id.isin(offered)


def lift(frame, col="n"):
    r = frame.groupby("offered")[col].mean()
    return r[True] / r[False] - 1


B["offered_patients"] = len(offered)
B["offered_first_date"], B["offered_last_date"] = camp.offered_on.min(), camp.offered_on.max()
B["accepted"] = int((camp.took_up == "Y").sum())
W["campaign_lift_aggregate"] = lift(patients)
for m in METROS:
    of_metro = patients[patients.metro == m]
    W[f"lift_{m}"] = lift(of_metro)
    B[f"offered_share_{m}"] = of_metro.offered.mean()
    B[f"offered_{m}"], B[f"not_offered_{m}"] = int(of_metro.offered.sum()), int((~of_metro.offered).sum())
for m in CAMPAIGN_METROS:
    B[f"gap_before_offer_{m}"] = lift(patients[patients.metro == m], "before")
B["offered_share_campaign_metros"] = patients[patients.metro.isin(CAMPAIGN_METROS)].offered.mean()
B["offered_share_other_metros"] = patients[~patients.metro.isin(CAMPAIGN_METROS)].offered.mean()


def per_day(metros, lo, hi):
    n = ((rb.metro.isin(metros)) & (rb.booking_date >= lo) & (rb.booking_date <= hi)).sum()
    return n / ((pd.Timestamp(hi) - pd.Timestamp(lo)).days + 1)


W["campaign_metros_prior_change"] = per_day(CAMPAIGN_METROS, *PRE) / per_day(CAMPAIGN_METROS, "2026-04-01", "2026-05-13") - 1
B["campaign_metros_window_change"] = per_day(CAMPAIGN_METROS, *OFFER) / per_day(CAMPAIGN_METROS, *PRE) - 1
others = [m for m in METROS if m not in CAMPAIGN_METROS]
B["other_metros_window_change"] = per_day(others, *OFFER) / per_day(others, *PRE) - 1
B["other_metros_prior_change"] = per_day(others, *PRE) / per_day(others, "2026-04-01", "2026-05-13") - 1
B["window_change_New York"] = per_day(["New York"], *OFFER) / per_day(["New York"], *PRE) - 1
# The chance checks: shuffle who was offered inside a metro, 20,000 times, and count how often the
# shuffled gap is at least as far from zero as the real one (two-sided). Week 1 Thursday's check.
SHUFFLES, shuffler = 20000, np.random.default_rng(20261019)


def shuffled_gaps(frames):
    """The offered patients' bookings over what their own metro's other patients book, once per shuffle."""
    got, expected = np.zeros(SHUFFLES), np.zeros(SHUFFLES)
    for frame in frames:
        x, k = frame.n.to_numpy(), int(frame.offered.sum())
        for start in range(0, SHUFFLES, 2000):
            idx = np.argsort(shuffler.random((2000, len(x))), axis=1)[:, :k]
            s = x[idx].sum(axis=1)
            got[start:start + 2000] += s
            expected[start:start + 2000] += k * (x.sum() - s) / (len(x) - k)
    return got / expected - 1


def held_at_metro_rate(frame, col="n"):
    """Offered patients' bookings against what they would book at their own metro's not-offered rate."""
    got = expected = 0.0
    for _, g in frame.groupby("metro"):
        got += g[g.offered][col].sum()
        expected += g.offered.sum() * g[~g.offered][col].mean()
    return got / expected - 1


for m in METROS:
    of_metro = patients[patients.metro == m]
    B[f"permutation_p_{m}"] = float((np.abs(shuffled_gaps([of_metro])) >= abs(W[f"lift_{m}"]) - 1e-12).mean())
B["new_york_permutation_p_two_sided"] = B["permutation_p_New York"]
# Six metros were tested, so New York's p is multiplied by six (Bonferroni, and Holm's first step).
B["new_york_p_corrected_for_six"] = min(1.0, len(METROS) * B["new_york_permutation_p_two_sided"])
in_campaign = patients[patients.metro.isin(CAMPAIGN_METROS)]
B["campaign_metros_gap_held_at_metro_rate"] = held_at_metro_rate(in_campaign)
B["campaign_metros_gap_held_at_metro_rate_before"] = held_at_metro_rate(in_campaign, "before")
gaps = shuffled_gaps([g for _, g in in_campaign.groupby("metro")])
B["campaign_metros_pooled_p"] = float((np.abs(gaps) >= abs(B["campaign_metros_gap_held_at_metro_rate"]) - 1e-12).mean())
B["six_metros_gap_held_at_metro_rate"] = held_at_metro_rate(patients)
# Why the company-wide comparison compares metros: where the offered patients live, and how often
# each metro group's patients book per head, in the window and before it (1 April to 14 July).
outside = patients[~patients.metro.isin(CAMPAIGN_METROS)]
B["offered_in_campaign_metros"] = int(in_campaign.offered.sum())
B["offered_share_living_in_campaign_metros"] = in_campaign.offered.sum() / patients.offered.sum()
B["bookings_per_head_window_campaign_metros"] = in_campaign.n.mean()
B["bookings_per_head_window_other_metros"] = outside.n.mean()
B["bookings_per_head_ratio_window"] = in_campaign.n.mean() / outside.n.mean()
B["bookings_per_head_before_campaign_metros"] = in_campaign.before.mean()
B["bookings_per_head_before_other_metros"] = outside.before.mean()
B["bookings_per_head_ratio_before"] = in_campaign.before.mean() / outside.before.mean()
took = dict(zip(camp.patient_id[camp.took_up == "Y"], camp.offered_on[camp.took_up == "Y"]))
home = rb[(rb.channel == "at-home") & rb.patient_id.isin(took)]
used = home[(home.booking_date >= home.patient_id.map(took)) & (home.booking_date <= OFFER[1])]
B["accepted_and_booked_home_in_window"] = used.patient_id.nunique()
B["accepted_with_no_home_booking_in_window"] = B["accepted"] - B["accepted_and_booked_home_in_window"]
home_done = set(rb[(rb.channel == "at-home") & (rb.status == "completed")].booking_id)
B["home_claims_fee_waived"] = int((claims.booking_id.isin(home_done) & ~claims.booking_id.isin(set(fee.booking_id))).sum())

# ---- Print, then compare ----
for key, value in {**W, **B}.items():
    print(f"{key}: {value:.4f}" if isinstance(value, float) else f"{key}: {value}")

# The spine's figures, as docs/detailing/W03_build1_spine.md prints them (sub-problem 4 re-planted
# on 1 October 2026, decision build1-register-from-bookings).
SPINE = {
    "dashboard_change": 0.051, "booked_change": 0.078, "performed_change": 0.086, "bookings_change": 0.056,
    "employer_tests": 6000, "contract_amount": 180000, "contract_share_of_q3": 0.146,
    "q3_billed": 1231001, "q3_mean_claim": 210.50, "q3_mean_without_contract": 179.75,
    "q3_median_claim": 150, "text_amounts": 60, "claim_lines_non_employer": 22152,
    "tests_on_claimed_bookings_non_employer": 46867, "tests_booked_non_employer": 48235,
    "switch_change_old": -0.230, "switch_change_both": -0.122, "repeated_ids": 180,
    "exact_join_share": 0.019, "unmatched_after_normalising": 0, "double_posts": 280,
    "double_posted_dollars": 19204.63, "reversals": 105, "claims_without_posting": 398,
    "denial_postings": 1137, "denial_rate_retail": 0.104, "denial_rate_Medicaid": 0.149,
    "denial_rate_commercial": 0.113, "denial_rate_Medicare": 0.088, "denial_rate_self-pay": 0.0,
    "denied_billed": 230132, "paid_net_of_double_posts": 801314, "billed_all": 2201099,
    "payer_share_commercial": 0.539, "payer_share_Medicare": 0.239, "payer_share_Medicaid": 0.145,
    "payer_share_self-pay": 0.077,
    "small_rate_all_visits": 0.188, "others_rate_all_visits": 0.079, "small_rate_scheduled": 0.190,
    "others_rate_scheduled": 0.151, "small_site_no_shows": 15, "small_site_scheduled": 79,
    "small_site_walk_ins": 1, "tail_probability": 0.21,
    "campaign_lift_aggregate": 0.090, "lift_Dallas": -0.108, "lift_Atlanta": -0.199,
    "lift_Phoenix": -0.130, "lift_Chicago": -0.048, "lift_Philadelphia": 0.006,
    "lift_New York": 0.235, "campaign_metros_prior_change": 0.069,
}
# Every further figure the Saturday TRAINER files quote, rounded as they print it.
BANK = {
    "legacy_rows": 11729, "legacy_distinct_ids": 11549, "repeated_pairs_identical": 145,
    "repeated_pairs_differing_in_updated_at": 30, "repeated_pairs_differing_in_channel": 6,
    "legacy_rows_with_no_channel": 180, "newsys_rows": 153, "newsys_Chicago": 85,
    "newsys_Philadelphia": 68,
    "dashboard_Q2": 23213, "dashboard_Q3": 24406, "booked_Q2": 23213, "booked_Q3": 25022,
    "performed_Q2": 22468, "performed_Q3": 24399, "bookings_Q2": 5692, "bookings_Q3": 6009,
    "dashboard_raw_rows_Q2": 23788, "dashboard_raw_rows_Q3": 24556, "dashboard_raw_rows_change": 0.032,
    "employer_screenings": 1200, "employer_tests_per_screening": 5,
    "booked_change_with_contract": 0.336, "performed_change_with_contract": 0.353,
    "q2_billed": 970098, "q3_billed_without_contract": 1051001, "billed_change_with_contract": 0.269,
    "billed_change_without_contract": 0.083, "q2_median_claim": 150, "q2_mean_claim": 176.13,
    "q2_claims": 5508, "q3_retail_claims": 5847, "retail_claims_change": 0.062,
    "billed_per_retail_claim_change": 0.021, "fee_lines": 1102, "fee_dollars_Q2": 11220,
    "fee_dollars_Q3": 10820, "claim_lines_tests_or_panels": 21050,
    "billed_change_Atlanta": 0.264, "billed_change_Phoenix": 0.162, "billed_change_Dallas": 0.109,
    "billed_change_New York": 0.055, "billed_change_Chicago": -0.065, "billed_change_Philadelphia": -0.109,
    "retail_claims": 11355,
    "bookings_Chicago_Q2": 754, "bookings_Chicago_Q3_old": 571, "bookings_Chicago_Q3_both": 656,
    "bookings_Philadelphia_Q2": 661, "bookings_Philadelphia_Q3_old": 519,
    "bookings_Philadelphia_Q3_both": 587, "bookings_Chicago_change_old": -0.243,
    "bookings_Chicago_change_both": -0.130, "bookings_Philadelphia_change_old": -0.215,
    "bookings_Philadelphia_change_both": -0.112, "bookings_Dallas_change_both": 0.077,
    "bookings_Phoenix_change_both": 0.130, "bookings_New York_change_both": 0.068,
    "bookings_Atlanta_change_both": 0.212, "switch_Q2": 1415, "switch_Q3_old": 1090,
    "switch_Q3_both": 1243,
    "postings": 11343, "refs_as_claim_ids": 216, "refs_as_CLM_numbers": 2269, "refs_as_bare_digits": 8858,
    "reversal_dollars": 8662.87, "denial_postings_paying_nothing": 1137, "unposted_dollars": 253165,
    "unposted_without_contract": 397, "unposted_dollars_without_contract": 73165, "unposted_months": 6,
    "claims_marked_denied": 1175, "denied_claims_with_no_posting": 38, "paid_raw_sum": 820518.19,
    "paid_share_of_billed": 0.364, "gap_billed_less_paid": 1399785.44, "gap_contractual": 883254.70,
    "gap_no_posting": 253165, "gap_denied_with_posting": 222108, "gap_patient_shares": 32594.87,
    "gap_reversals": 8662.87, "gap_parts_sum": 1399785.44,
    "register_rows": 3685, "register_centres": 12, "tail_probability_all_visits": 0.0014,
    "walk_in_no_shows": 0, "next_worst_rate_all_visits": 0.098, "next_worst_rate_scheduled": 0.185,
    "bookings_with_two_slots": 253, "small_scheduled_bookings": 64, "small_bookings_missing_a_slot": 15,
    "others_share_missing_a_slot": 0.173, "tail_probability_per_booking": 0.13,
    "offered_patients": 2381, "accepted": 948, "offered_share_campaign_metros": 0.505,
    "offered_share_other_metros": 0.214, "gap_before_offer_Dallas": 0.014,
    "gap_before_offer_Atlanta": -0.052, "gap_before_offer_Phoenix": -0.061,
    "new_york_permutation_p_two_sided": 0.03, "offered_New York": 316, "not_offered_New York": 1184,
    "accepted_and_booked_home_in_window": 259, "accepted_with_no_home_booking_in_window": 689,
    "home_claims_fee_waived": 321, "campaign_metros_window_change": 0.074,
    "window_change_New York": 0.030, "double_post_gap_minutes_max": 2.0,
    "offered_share_Dallas": 0.495, "offered_share_Atlanta": 0.520, "offered_share_Phoenix": 0.506,
    "offered_share_Chicago": 0.215, "offered_share_Philadelphia": 0.219,
    "offered_share_New York": 0.211, "visits_to_detect_gap": 712, "billed_change_commercial": 0.130,
    "billed_change_Medicare": 0.060, "billed_change_Medicaid": 0.016, "billed_change_self-pay": -0.022,
    "switch_Q2_old_rows_with_repeats": 1450, "switch_Q3_old_rows_with_repeats": 1099,
    "repeated_pairs_differing_in_both": 1, "text_amount_dollars": 10559, "text_amounts_Q2": 32,
    "text_amounts_Q3": 28, "paid_on_payment_postings": 829181.06, "second_largest_claim": 420,
    "ids_in_both_systems": 0, "patient_and_date_in_both_systems": 0,
    "denial_rate_retail_printed": 0.103, "double_posts_same_channel_ERA": 280, "walk_in_rows": 1721,
    "quarters_to_detect_gap": 9, "patients_with_no_payer": 0,
    # Sub-problem 1: the shortfall against 18 percent, by branch
    "shortfall_dollars": 93714.64, "shortfall_dollars_Chicago": 30437, "shortfall_dollars_Philadelphia": 32999,
    "shortfall_dollars_New York": 21909, "shortfall_dollars_Dallas": 15867, "shortfall_dollars_Phoenix": 3659,
    "shortfall_dollars_Atlanta": -11156, "shortfall_share_Chicago": 0.325, "shortfall_share_Philadelphia": 0.352,
    "shortfall_share_New York": 0.234, "shortfall_share_Dallas": 0.169, "shortfall_share_Phoenix": 0.039,
    "shortfall_share_Atlanta": -0.119, "shortfall_share_Chicago_and_Philadelphia": 0.677,
    "shortfall_dollars_Medicare": 28437, "shortfall_dollars_commercial": 25562,
    "shortfall_dollars_Medicaid": 23672, "shortfall_dollars_self-pay": 16044,
    "shortfall_share_Medicare": 0.303, "shortfall_share_commercial": 0.273,
    "shortfall_share_Medicaid": 0.253, "shortfall_share_self-pay": 0.171,
    "shortfall_tests_share_Philadelphia": 0.444, "shortfall_tests_share_New York": 0.285,
    "shortfall_tests_share_Chicago": 0.237, "shortfall_tests_share_Dallas": 0.086,
    "shortfall_tests_share_Phoenix": 0.061, "shortfall_tests_share_Atlanta": -0.112,
    "shortfall_tests_share_Medicare": 0.338, "shortfall_tests_share_Medicaid": 0.282,
    "shortfall_tests_share_commercial": 0.212, "shortfall_tests_share_self-pay": 0.169,
    "shortfall_tests": 2113, "shortfall_share_Medicaid_and_self-pay": 0.424,
    # Sub-problem 3: double posts by gap, and the money to chase at contract value
    "double_post_gap_minutes_min": 0.0, "double_posts_2_minutes_apart": 274,
    "double_posts_1_minutes_apart": 4, "double_posts_0_minutes_apart": 2,
    "allowed_share_of_billed_Medicaid": 0.28, "allowed_share_of_billed_Medicare": 0.34,
    "allowed_share_of_billed_commercial": 0.53, "allowed_share_of_billed_self-pay": 1.0,
    "unposted_retail_at_contract": 35114.59, "denied_with_posting_at_contract": 97269.45,
    "patient_balance_claims": 1798, "patient_balances_commercial_share": 1.0,
    "reversed_claims": 105, "reversed_claims_billed": 19293, "reversed_claims_largest_net_paid": 0.0,
    "unposted_at_contract_with_employer": 215114.59, "chase_at_contract_before_denials": 256372.33, "co_adjustments_on_kept_postings": 1096542.70,
    "co_adjustments_on_denials": 213288,
    # Sub-problem 4: the unit, the walk-ins and the sample size's assumptions
    "walk_in_rows_other_centres": 1720, "no_shows_all": 300, "no_shows_on_rebooked_bookings": 253,
    "exact_power_at_712": 0.77, "visits_to_detect_gap_two_sample": 745,
    "other_centres_scheduled_slots": 1885,
    # Sub-problem 5: each metro's chance check, the pooled check and the mechanism
    "permutation_p_Dallas": 0.21, "permutation_p_Atlanta": 0.05, "permutation_p_Phoenix": 0.14,
    "permutation_p_Chicago": 0.77, "permutation_p_Philadelphia": 1.0, "new_york_p_corrected_for_six": 0.18,
    "campaign_metros_gap_held_at_metro_rate": -0.141, "campaign_metros_gap_held_at_metro_rate_before": -0.030,
    "campaign_metros_pooled_p": 0.007, "six_metros_gap_held_at_metro_rate": -0.096,
    "offered_in_campaign_metros": 1642, "offered_share_living_in_campaign_metros": 0.69,
    "bookings_per_head_window_campaign_metros": 0.76, "bookings_per_head_window_other_metros": 0.45,
    "bookings_per_head_ratio_window": 1.68, "bookings_per_head_before_campaign_metros": 1.16,
    "bookings_per_head_before_other_metros": 0.81, "bookings_per_head_ratio_before": 1.43,
}
# The dates, ids and yes-or-no findings the TRAINER files state, compared exactly.
FACTS = {
    "repeated_first_date": "2026-06-01", "repeated_last_date": "2026-09-26",
    "newsys_first_date": "09/18/2026", "newsys_last_date": "09/30/2026",
    "switch_metros_last_old_export_date": "2026-09-17",
    "employer_booking_date": "2026-08-06", "employer_site": "KH-DAL-01",
    "contract_claim": "KH-CLM-007802", "contract_account": "EMP-0007", "contract_metro": "Dallas",
    "contract_service_date": "2026-08-06", "employer_claim_unposted": True,
    "offered_first_date": "2026-07-15", "offered_last_date": "2026-08-04",
}
# The chance checks shuffle, so they agree within their own wobble; the binomial tails are exact
# and print with more places.
LOOSE = {"tail_probability": 0.006, "new_york_permutation_p_two_sided": 0.006,
         "tail_probability_per_booking": 0.006, "tail_probability_all_visits": 0.00006,
         "permutation_p_Dallas": 0.01, "permutation_p_Atlanta": 0.006, "permutation_p_Phoenix": 0.01,
         "permutation_p_Chicago": 0.01, "permutation_p_Philadelphia": 0.01, "new_york_p_corrected_for_six": 0.02,
         "campaign_metros_pooled_p": 0.002}
# The spine prints 10.4 percent for the claims file's 1,175 of 11,355, which is 10.35 and rounds to
# 10.3; the pack prints 10.3 (denial_rate_retail_printed) and the provenance records the difference.
SPINE_ROUNDING = {"denial_rate_retail": 0.0006}

def tolerance(key, want):
    """Half a unit in the last place the table prints: 0.146 allows 0.0005, $19,204.63 one half cent."""
    if key in LOOSE:
        return LOOSE[key]
    text = repr(want)
    return 0.5 * 10 ** -(len(text.split(".")[1]) if "." in text else 0) + 1e-9


fails = 0
print()
for name, table in (("spine", SPINE), ("bank", BANK)):
    values = W if name == "spine" else B
    for key, want in table.items():
        got = values[key]
        tol = SPINE_ROUNDING.get(key, tolerance(key, want)) if name == "spine" else tolerance(key, want)
        good = abs(float(got) - want) <= tol
        fails += not good
        print(f"{'PASS' if good else 'FAIL'}  {key}: files {float(got):.4f}, {name} {want}")
for key, want in FACTS.items():
    good = B[key] == want
    fails += not good
    print(f"{'PASS' if good else 'FAIL'}  {key}: files {B[key]}, fact {want}")
print(f"\nRESULT: {'PASS' if not fails else 'FAIL'} ({fails} disagreements with the spine, the bank and the facts)")
sys.exit(1 if fails else 0)

# Test inputs and expected outcomes.
# 1. No arguments, run from the repository root: reads content/W03/D1/data, prints every figure,
#    then one PASS line per spine, bank and fact entry, and ends "RESULT: PASS (0 disagreements with
#    the spine, the bank and the facts)" with exit code 0 while the data pack is unchanged.
# 2. --data content/W03/D1/data: the same output, read from the path given.
# 3. --data pointing at a folder without the files: FileNotFoundError naming the first missing CSV.
# 4. After the generator's seed or a plant changes: one FAIL line per figure that moved and exit 1,
#    the signal to re-read every number the question bank, the run sheet and the week-close notes quote.

"""Recompute every number Build 1 Thursday's pack quotes, and check the pack against the plants.

    python3 content/W03/D4/internal/C2_W03_D04_numbers_INTERNAL.py

Thursday's files quote three kinds of number, and this script proves each kind:

1. The Kalpa Health numbers in the viva prompts and the day sheet, recomputed from the ten CSV files
   in content/W03/D1/data/ the way a group would reach them, each beside the figure the files print.
2. The arithmetic behind the technical half's invented numbers in the question bank, which lie
   outside the ten files on purpose, and the day's grid of slots, seats, sets and minutes.
3. A guard: no STUDENT file names a plant, and no question the assessors read aloud in the technical
   half names a plant or reuses a planted value.

It reads only the data pack and the day's own markdown, uses the standard library alone, and exits 1
on any drift, so it runs cold on a fresh checkout with no install. The data pack is the US pack of
decision build1-us-data, with the visit register drawn from the bookings (decision
build1-register-from-bookings, 1 October 2026).
"""
import csv
import datetime as dt
import math
import pathlib
import random
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
DAY = HERE.parent
DATA = DAY.parent / "D1" / "data"
STEM = "C2_W03_D01_"

FAILS = []


def check(label, got, want, tol=None):
    """Print one number beside the figure the pack prints, and record a drift."""
    if tol is None:
        tol = 0.0006 if isinstance(want, float) and abs(want) < 1 else 0.6
    if isinstance(want, (int, float)) and not isinstance(want, bool):
        ok = got is not None and abs(float(got) - want) <= tol
        shown = f"{got:.4f}" if isinstance(got, float) else str(got)
    else:
        ok = got == want
        shown = str(got)
    print(f"{'PASS' if ok else 'FAIL'}  {label}: {shown} (pack {want})")
    if not ok:
        FAILS.append(label)


def load(name):
    with open(DATA / f"{STEM}{name}_STUDENT.csv", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def iso(text):
    """Both systems' dates: ISO in the old export, month/day/year in the new one."""
    if "/" in text:
        month, day, year = text.split("/")
        return dt.date(int(year), int(month), int(day))
    return dt.date.fromisoformat(text[:10])


def quarter(d):
    return "Q2" if d <= dt.date(2026, 6, 30) else "Q3"


def dollars(text):
    return float(str(text).replace("$", "").replace(",", ""))


def tail(n, k, p):
    """The binomial chance of k or more in n at rate p."""
    return sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k, n + 1))


legacy = load("bookings_legacy")
newsys = load("bookings_newsys")
lines = load("booking_tests")
claims = load("claims")
postings = load("remittances")
visits = load("appointments")
sites = load("sites")
campaign = load("campaign")
patients = load("patients")
catalogue = load("test_catalogue")

# One row per booking across both systems: the old export's repeats dropped on the booking id, the
# new system's codes mapped through the site list and the dictionary's channel and state words.
site_of_new = {s["new_system_code"]: s["site_code"] for s in sites if s["new_system_code"]}
bookings, seen = [], set()
for r in legacy:
    if r["booking_id"] in seen:
        continue
    seen.add(r["booking_id"])
    bookings.append({"id": r["booking_id"], "patient": r["patient_id"], "metro": r["metro"],
                     "date": iso(r["booking_date"]), "channel": r["channel"],
                     "done": r["status"] == "completed", "system": "legacy"})
for r in newsys:
    channel = {"WALKIN": "walk-in", "WEB": "online", "CALL": "phone", "MOBILEDRAW": "at-home"}[r["channel"]]
    bookings.append({"id": r["bkg_ref"], "patient": "P-" + r["patient"], "metro": r["metro"],
                     "date": iso(r["created"]), "channel": channel,
                     "done": r["state"] == "DONE", "system": "new"})
tests_on = {}
for t in lines:
    if t["line"] in ("test", "component"):
        tests_on[t["booking_id"]] = tests_on.get(t["booking_id"], 0) + int(t["quantity"])

print("== The calendar")
check("days in Q2", (dt.date(2026, 7, 1) - dt.date(2026, 4, 1)).days, 91)
check("days in Q3", (dt.date(2026, 10, 1) - dt.date(2026, 7, 1)).days, 92)

print("\n== The headline: what Dr Menon's 5 percent counts")
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
for key, (q2, q3, change) in {"dashboard": (23213, 24406, 0.051), "booked": (23213, 25022, 0.078),
                              "performed": (22468, 24399, 0.086),
                              "bookings": (5692, 6009, 0.056)}.items():
    check(f"{key} Q2", moved[key]["Q2"], q2)
    check(f"{key} Q3", moved[key]["Q3"], q3)
    check(f"{key} change", round(moved[key]["Q3"] / moved[key]["Q2"] - 1, 3), change)
raw = {"Q2": 0, "Q3": 0}
for r in legacy:
    if r["channel"] != "employer":
        raw[quarter(iso(r["booking_date"]))] += tests_on.get(r["booking_id"], 0)
check("dashboard on raw rows Q2", raw["Q2"], 23788)
check("dashboard on raw rows Q3", raw["Q3"], 24556)
check("dashboard on raw rows change", round(raw["Q3"] / raw["Q2"] - 1, 3), 0.032)
employer_ids = {b["id"] for b in bookings if b["channel"] == "employer"}
employer_tests = sum(tests_on.get(i, 0) for i in employer_ids)
check("employer contract tests in Q3", employer_tests, 6000)
check("employer screenings", max(int(t["quantity"]) for t in lines if t["panel_code"] == "PNL-EMP"), 1200)
check("tests per screening", sum(1 for t in lines if t["panel_code"] == "PNL-EMP" and t["line"] == "component"), 5)
check("tests booked with the contract in, change",
      round((moved["booked"]["Q3"] + employer_tests) / moved["booked"]["Q2"] - 1, 3), 0.336)

print("\n== Sub-problem 1, revenue")
contract = [c for c in claims if c["employer_account"]]
check("employer claims", len(contract), 1)
c0 = contract[0]
check("contract claim id", c0["claim_id"], "KH-CLM-007802")
check("contract account", c0["employer_account"], "EMP-0007")
check("contract metro", c0["metro"], "Dallas")
check("contract service date", c0["service_date"], "2026-08-06")
check("contract dollars", dollars(c0["billed_amount"]), 180000)
by_q = {"Q2": [], "Q3": []}
for c in claims:
    by_q[quarter(iso(c["service_date"]))].append(c)
q2_amounts = sorted(dollars(c["billed_amount"]) for c in by_q["Q2"])
q3_amounts = sorted(dollars(c["billed_amount"]) for c in by_q["Q3"])
q3_retail = [dollars(c["billed_amount"]) for c in by_q["Q3"] if not c["employer_account"]]


def median(xs):
    xs = sorted(xs)
    m = len(xs) // 2
    return xs[m] if len(xs) % 2 else (xs[m - 1] + xs[m]) / 2


check("Q3 billed", sum(q3_amounts), 1231001)
check("Q3 billed without the contract", sum(q3_retail), 1051001)
check("Q2 billed", sum(q2_amounts), 970098)
check("contract share of Q3", round(180000 / sum(q3_amounts), 3), 0.146)
check("growth with the contract", round(sum(q3_amounts) / sum(q2_amounts) - 1, 3), 0.269)
check("growth without the contract", round(sum(q3_retail) / sum(q2_amounts) - 1, 3), 0.083)
check("Q3 mean claim", round(sum(q3_amounts) / len(q3_amounts), 2), 210.50, 0.006)
check("Q3 mean without the contract", round(sum(q3_retail) / len(q3_retail), 2), 179.75, 0.006)
check("Q3 median claim", median(q3_amounts), 150)
check("Q2 median claim", median(q2_amounts), 150)
check("Q2 mean claim", round(sum(q2_amounts) / len(q2_amounts), 2), 176.13, 0.006)
retail_claims = [c for c in claims if not c["employer_account"]]
check("claim lines outside the contract", sum(int(c["line_items"]) for c in retail_claims), 22152)
line_dollars = {}
for t in lines:
    if t["line"] in ("test", "panel"):
        line_dollars[t["booking_id"]] = line_dollars.get(t["booking_id"], 0) + float(t["price_each"]) * int(t["quantity"])
fee_claims = [c for c in claims if abs(dollars(c["billed_amount"]) - line_dollars.get(c["booking_id"], 0) - 20) < 1e-6]
check("claims with a $20 collection fee line", len(fee_claims), 1102)
check("claim lines that are tests or panels", sum(int(c["line_items"]) for c in retail_claims) - len(fee_claims), 21050)
completed = {b["id"] for b in bookings if b["done"]}
date_of = {b["id"]: b["date"] for b in bookings}
test_rows = [t for t in lines if t["line"] in ("test", "component") and t["panel_code"] != "PNL-EMP"]
check("tests booked outside the contract", len(test_rows), 48235)
check("tests on completed bookings outside the contract", sum(1 for t in test_rows if t["booking_id"] in completed), 46867)
check("Q3 claim lines outside the contract", sum(int(c["line_items"]) for c in by_q["Q3"] if not c["employer_account"]), 11395)
check("Q3 tests on completed bookings", sum(1 for t in test_rows if t["booking_id"] in completed
                                            and quarter(date_of[t["booking_id"]]) == "Q3"), 24399)
text_amounts = [c for c in claims if not c["billed_amount"].isdigit()]
check("billed amounts written as text", len(text_amounts), 60)
check("text amounts carrying a comma", sum(1 for c in text_amounts if "," in c["billed_amount"]), 0)
check("text amounts all start with a dollar sign", all(c["billed_amount"].startswith("$") for c in text_amounts), True)
check("an amount written as $265.00 exists", any(c["billed_amount"] == "$265.00" for c in text_amounts), True)
check("text amounts in Q2", sum(1 for c in text_amounts if c in by_q["Q2"]), 32)
check("text dollars in Q2", sum(dollars(c["billed_amount"]) for c in text_amounts if c in by_q["Q2"]), 5390)
check("text amounts in Q3", sum(1 for c in text_amounts if c in by_q["Q3"]), 28)
check("text dollars in Q3", sum(dollars(c["billed_amount"]) for c in text_amounts if c in by_q["Q3"]), 5169)
# The shortfall against the plan of 18 percent, in billed dollars outside the contract, by branch.
branch = {}
for key in ("metro", "payer_type"):
    totals = {}
    for c in retail_claims:
        v = totals.setdefault(c[key], [0.0, 0.0])
        v[0 if quarter(iso(c["service_date"])) == "Q2" else 1] += dollars(c["billed_amount"])
    branch[key] = totals
plan = sum(dollars(c["billed_amount"]) for c in retail_claims if quarter(iso(c["service_date"])) == "Q2") * 1.18
check("Q3 plan at 18 percent outside the contract", round(plan), 1144716)
check("Q3 shortfall against the plan", round(plan - sum(q3_retail)), 93715)
short = {m: v[0] * 1.18 - v[1] for m, v in branch["metro"].items()}
for metro, want in {"Chicago": 30437, "Philadelphia": 32999, "New York": 21909, "Dallas": 15867,
                    "Phoenix": 3659, "Atlanta": -11156}.items():
    check(f"shortfall in {metro}", round(short[metro]), want)
check("Chicago and Philadelphia's shortfall", round(short["Chicago"] + short["Philadelphia"]), 63436)
check("their share of the shortfall", round((short["Chicago"] + short["Philadelphia"]) / (plan - sum(q3_retail)), 3), 0.677)
for metro, (q2, q3, change) in {"Chicago": (124097, 115997, -0.065), "Philadelphia": (114014, 101538, -0.109)}.items():
    v = branch["metro"][metro]
    check(f"{metro} billed Q2", round(v[0]), q2)
    check(f"{metro} billed Q3", round(v[1]), q3)
    check(f"{metro} billed change", round(v[1] / v[0] - 1, 3), change)
payer_short = sorted(round(v[0] * 1.18 - v[1]) for v in branch["payer_type"].values())
check("smallest payer shortfall", payer_short[0], 16044)
check("largest payer shortfall", payer_short[-1], 28437)
price = {c["code"]: float(c["list_price_usd"]) for c in catalogue}
wel = sorted({t["test_code"] for t in lines if t["panel_code"] == "PNL-WEL" and t["line"] == "component"})
check("tests in the whole-body wellness panel", len(wel), 12)
check("their list prices added", sum(price[t] for t in wel), 785)
check("the panel's own price", price["PNL-WEL"], 299)

print("\n== Sub-problem 2, bookings")
switch = ("Chicago", "Philadelphia")
retail_bookings = [b for b in bookings if b["channel"] != "employer"]


def count(metros, q, system=None):
    return sum(1 for b in retail_bookings if b["metro"] in metros and quarter(b["date"]) == q
               and (system is None or b["system"] == system))


check("two metros Q2", count(switch, "Q2"), 1415)
check("two metros Q3, old export", count(switch, "Q3", "legacy"), 1090)
check("two metros Q3, both systems", count(switch, "Q3"), 1243)
check("two metros change, old export", round(count(switch, "Q3", "legacy") / count(switch, "Q2") - 1, 3), -0.230)
check("two metros change, both systems", round(count(switch, "Q3") / count(switch, "Q2") - 1, 3), -0.122)
for metro, (q2, old, both, c_old, c_both) in {"Chicago": (754, 571, 656, -0.243, -0.130),
                                              "Philadelphia": (661, 519, 587, -0.215, -0.112)}.items():
    check(f"{metro} Q2", count((metro,), "Q2"), q2)
    check(f"{metro} Q3, old export", count((metro,), "Q3", "legacy"), old)
    check(f"{metro} Q3, both systems", count((metro,), "Q3"), both)
    check(f"{metro} change, old export", round(old / q2 - 1, 3), c_old)
    check(f"{metro} change, both systems", round(both / q2 - 1, 3), c_both)
for metro, change in {"Dallas": 0.077, "Phoenix": 0.130, "New York": 0.068, "Atlanta": 0.212}.items():
    check(f"{metro} bookings change", round(count((metro,), "Q3") / count((metro,), "Q2") - 1, 3), change)
copies = {}
for r in legacy:
    copies.setdefault(r["booking_id"], []).append(r)
repeated = {k: v for k, v in copies.items() if len(v) > 1}
check("old export rows", len(legacy), 11729)
check("old export booking ids", len(copies), 11549)
check("ids that appear twice", len(repeated), 180)
check("first repeated booking date", min(v[0]["booking_date"] for v in repeated.values()), "2026-06-01")
check("last repeated booking date", max(v[0]["booking_date"] for v in repeated.values()), "2026-09-26")
diffs = {}
for v in repeated.values():
    cols = tuple(c for c in v[0] if v[0][c] != v[1][c])
    diffs[cols] = diffs.get(cols, 0) + 1
check("pairs matching on every column", diffs.get((), 0), 145)
check("pairs differing only in updated_at", diffs.get(("updated_at",), 0), 29)
check("pairs differing only in channel", diffs.get(("channel",), 0), 5)
check("pairs differing in both", diffs.get(("channel", "updated_at"), 0), 1)
check("rows left by a whole-row dedupe", len({tuple(r.values()) for r in legacy}), 11584)
check("new system bookings", len(newsys), 153)
check("new system first date", min(iso(r["created"]) for r in newsys).isoformat(), "2026-09-18")
check("new system last date", max(iso(r["created"]) for r in newsys).isoformat(), "2026-09-30")
check("new system dates all written month first with a day of 18 or later",
      all(int(r["created"].split("/")[1]) >= 18 for r in newsys), True)
check("new system DONE", sum(1 for r in newsys if r["state"] == "DONE"), 143)
check("new system CXL", sum(1 for r in newsys if r["state"] == "CXL"), 10)
check("first new system reference", newsys[0]["bkg_ref"], "NB/ORD/000001")
check("ORD-01 maps to", site_of_new["ORD-01"], "KH-CHI-01")
check("old export's last date for the two metros",
      max(b["date"] for b in bookings if b["metro"] in switch and b["system"] == "legacy").isoformat(), "2026-09-17")
months = {}
for b in retail_bookings:
    if b["metro"] in switch:
        months[b["date"].month] = months.get(b["date"].month, 0) + 1
check("two metros by month, April to September", [months[m] for m in range(4, 10)], [488, 478, 449, 452, 420, 371])
rep_q = {"Q2": 0, "Q3": 0}
for v in repeated.values():
    if v[0]["metro"] in switch:
        rep_q[quarter(iso(v[0]["booking_date"]))] += 1
check("repeats in the two metros, Q2", rep_q["Q2"], 35)
check("repeats in the two metros, Q3", rep_q["Q3"], 9)
raw_two = {"Q2": 0, "Q3": 0}
for r in legacy:
    if r["metro"] in switch and r["channel"] != "employer":
        raw_two[quarter(iso(r["booking_date"]))] += 1
check("two metros' fall on raw rows of the old export", round(raw_two["Q3"] / raw_two["Q2"] - 1, 3), -0.242)

print("\n== Sub-problem 3, billing")
claim_ids = {c["claim_id"] for c in claims}
by_digits = {c["claim_id"].split("-")[-1]: c["claim_id"] for c in claims}


def normalise(ref):
    if ref in claim_ids:
        return ref
    if ref.startswith("CLM-"):
        return by_digits.get(f"{int(ref[4:]):06d}")
    return by_digits.get(ref)


check("postings", len(postings), 11343)
check("exact join matches", sum(1 for p in postings if p["claim_ref"] in claim_ids), 216)
check("exact join share", round(216 / len(postings), 3), 0.019)
check("refs written as the claim id", sum(1 for p in postings if p["claim_ref"].startswith("KH-CLM-")), 216)
check("refs written as a CLM-number", sum(1 for p in postings if p["claim_ref"].startswith("CLM-")), 2269)
check("refs written as six bare digits", sum(1 for p in postings if p["claim_ref"].isdigit() and len(p["claim_ref"]) == 6), 8858)
check("postings unmatched once normalised", sum(1 for p in postings if normalise(p["claim_ref"]) is None), 0)
check("a CLM-number drops its zeros", any(p["claim_ref"] == "CLM-1" for p in postings), True)
billed_of = {c["claim_id"]: dollars(c["billed_amount"]) for c in claims}
check("billed amounts agree on every matched pair",
      all(abs(float(p["billed_amount"]) - billed_of[normalise(p["claim_ref"])]) < 1e-6 for p in postings), True)
pairs = {}
for p in postings:
    if p["posting"] == "payment":
        pairs.setdefault((p["claim_ref"], p["paid_amount"]), []).append(p)
doubles = [v for v in pairs.values() if len(v) > 1]
check("double posts", sum(len(v) - 1 for v in doubles), 280)
check("double-posted dollars", round(sum(float(x["paid_amount"]) for v in doubles for x in v[1:]), 2), 19204.63, 0.006)
gaps = [(max(dt.datetime.fromisoformat(x["posted_at"]) for x in v)
         - min(dt.datetime.fromisoformat(x["posted_at"]) for x in v)).total_seconds() / 60 for v in doubles]
check("double posts at most 2 minutes apart", max(gaps), 2.0)
check("double posts at least 0 minutes apart", min(gaps), 0.0)
check("double posts all electronic remittances", all(x["channel"] == "ERA" for v in doubles for x in v), True)
reversals = [p for p in postings if p["posting"] == "reversal"]
check("reversals", len(reversals), 105)
check("dollars taken back", round(-sum(float(p["paid_amount"]) for p in reversals), 2), 8662.87, 0.006)
denials = [p for p in postings if p["posting"] == "denial"]
check("denial postings", len(denials), 1137)
check("denial postings that pay nothing", sum(1 for p in denials if float(p["paid_amount"]) == 0), 1137)
posted = {normalise(p["claim_ref"]) for p in postings}
unposted = [c for c in claims if c["claim_id"] not in posted]
check("claims with no posting", len(unposted), 398)
check("dollars on claims with no posting", sum(dollars(c["billed_amount"]) for c in unposted), 253165)
check("months holding a claim with no posting", sorted({c["service_date"][:7] for c in unposted}),
      ["2026-04", "2026-05", "2026-06", "2026-07", "2026-08", "2026-09"])
check("the employer claim has no posting", "KH-CLM-007802" in {c["claim_id"] for c in unposted}, True)
denied = [c for c in retail_claims if c["denial_category"]]
check("retail claims", len(retail_claims), 11355)
check("retail claims marked denied", len(denied), 1175)
check("denial rate, to two decimals of a percent", round(len(denied) / len(retail_claims), 4), 0.1035, 0.00006)
for payer, rate in {"Medicaid": 0.149, "commercial": 0.113, "Medicare": 0.088, "self-pay": 0.0}.items():
    of_payer = [c for c in retail_claims if c["payer_type"] == payer]
    check(f"denial rate, {payer}", round(sum(1 for c in of_payer if c["denial_category"]) / len(of_payer), 3), rate)
check("billed on denied claims", sum(dollars(c["billed_amount"]) for c in denied), 230132)
check("denied claims with no posting", sum(1 for c in denied if c["claim_id"] not in posted), 38)
check("eligibility or coverage denials", sum(1 for c in denied if c["denial_category"] == "eligibility or coverage"), 283)
check("missing or invalid information denials", sum(1 for c in denied if c["denial_category"] == "missing or invalid information"), 272)
billed_all = sum(dollars(c["billed_amount"]) for c in claims)
paid_raw = sum(float(p["paid_amount"]) for p in postings)
paid_net = paid_raw - sum(float(x["paid_amount"]) for v in doubles for x in v[1:])
check("billed across both quarters", billed_all, 2201099)
check("raw sum of every paid amount", round(paid_raw, 2), 820518.19, 0.006)
check("paid net of the double posts", round(paid_net, 2), 801313.56, 0.006)
check("paid share of billed", round(paid_net / billed_all, 3), 0.364)
kept, keys = [], set()
for p in postings:
    if p["posting"] == "payment":
        k = (p["claim_ref"], p["paid_amount"])
        if k in keys:
            continue
        keys.add(k)
    kept.append(p)
contractual = sum(float(p["adjustment_amount"]) for p in kept if p["posting"] == "payment"
                  and p["reason_category"] == "contractual adjustment")
denial_claims = {normalise(p["claim_ref"]) for p in denials}
denied_with_posting = sum(dollars(c["billed_amount"]) for c in claims if c["claim_id"] in denial_claims)
patient_shares = sum(float(p["patient_responsibility"]) for p in kept if p["posting"] == "payment")
reversed_dollars = -sum(float(p["paid_amount"]) for p in kept if p["posting"] == "reversal")
gap = billed_all - paid_net
check("the gap from billed to paid", round(gap, 2), 1399785.44, 0.006)
check("contractual adjustments", round(contractual, 2), 883254.70, 0.006)
check("billed on claims denied with a posting", denied_with_posting, 222108)
check("patient shares", round(patient_shares, 2), 32594.87, 0.006)
check("the bridge closes", round(contractual + 253165 + denied_with_posting + patient_shares + reversed_dollars, 2),
      round(gap, 2), 0.006)

print("\n== Sub-problem 4, no-shows")
small = "KH-ATL-03"
mine = [v for v in visits if v["site_code"] == small]
rest = [v for v in visits if v["site_code"] != small]
check("KH-ATL-03 visits", len(mine), 80)
check("KH-ATL-03 scheduled", sum(1 for v in mine if v["kind"] == "scheduled"), 79)
check("KH-ATL-03 walk-ins", sum(1 for v in mine if v["kind"] == "walk-in"), 1)
check("KH-ATL-03 missed slots", sum(1 for v in mine if v["attended"] == "N"), 15)
check("KH-ATL-03 rate, all visits", round(15 / 80, 3), 0.188)
check("KH-ATL-03 rate, scheduled", round(15 / 79, 3), 0.190)
rest_sched = [v for v in rest if v["kind"] == "scheduled"]
check("other centres' visits", len(rest), 3605)
check("other centres' walk-ins", sum(1 for v in rest if v["kind"] == "walk-in"), 1720)
check("other centres' walk-in share", round(1720 / len(rest), 3), 0.477)
check("other centres' scheduled", len(rest_sched), 1885)
check("other centres' missed slots", sum(1 for v in rest_sched if v["attended"] == "N"), 285)
check("walk-ins never miss", sum(1 for v in visits if v["kind"] == "walk-in" and v["attended"] == "N"), 0)
p_sched = 285 / 1885
p_all = sum(1 for v in rest if v["attended"] == "N") / len(rest)
check("other centres' rate, all visits", round(p_all, 3), 0.079)
check("other centres' rate, scheduled", round(p_sched, 3), 0.151)
per_site = {}
for v in rest:
    s = per_site.setdefault(v["site_code"], [0, 0, 0, 0])
    s[0] += 1
    s[1] += v["attended"] == "N"
    if v["kind"] == "scheduled":
        s[2] += 1
        s[3] += v["attended"] == "N"
check("next worst, all visits", round(max(s[1] / s[0] for s in per_site.values()), 3), 0.098)
check("next worst, scheduled", round(max(s[3] / s[2] for s in per_site.values()), 3), 0.185)
check("chance of 15 or more in 79 at the others' rate", round(tail(79, 15, p_sched), 2), 0.21, 0.006)
check("the same check on all visits", round(tail(80, 15, p_all), 4), 0.0014, 0.00006)
check("missed slots expected at the others' rate", round(79 * p_sched, 1), 11.9, 0.06)
check("the other Atlanta centre's scheduled rate", round(per_site["KH-ATL-02"][3] / per_site["KH-ATL-02"][2], 3), 0.143)
check("register rows", len(visits), 3685)
slots = {}
for v in visits:
    if v["kind"] == "scheduled":
        slots.setdefault(v["booking_id"], []).append(v)
check("bookings with two rows", sum(1 for s in slots.values() if len(s) == 2), 253)
missed = {b: any(v["attended"] == "N" for v in s) for b, s in slots.items()}
mine_b = [b for b, s in slots.items() if s[0]["site_code"] == small]
rest_b = [b for b, s in slots.items() if s[0]["site_code"] != small]
check("KH-ATL-03 scheduled bookings", len(mine_b), 64)
check("of them missing a slot", sum(missed[b] for b in mine_b), 15)
share_b = sum(missed[b] for b in rest_b) / len(rest_b)
check("other centres' bookings missing a slot", round(share_b, 3), 0.173)
check("chance of that per booking", round(tail(64, 15, share_b), 2), 0.13, 0.006)

print("\n== Sub-problem 5, the at-home collection offer")
lo, hi = dt.date(2026, 7, 15), dt.date(2026, 9, 14)
in_window = {}
for b in retail_bookings:
    if lo <= b["date"] <= hi:
        in_window[b["patient"]] = in_window.get(b["patient"], 0) + 1
offered_ids = {c["patient_id"] for c in campaign}
offered = [p for p in patients if p["patient_id"] in offered_ids]
others = [p for p in patients if p["patient_id"] not in offered_ids]


def per_patient(group):
    return sum(in_window.get(p["patient_id"], 0) for p in group) / len(group)


check("patients offered", len(campaign), 2381)
check("first offer", min(c["offered_on"] for c in campaign), "2026-07-15")
check("last offer", max(c["offered_on"] for c in campaign), "2026-08-04")
check("offers accepted", sum(1 for c in campaign if c["took_up"] == "Y"), 948)
took = {c["patient_id"]: c["offered_on"] for c in campaign if c["took_up"] == "Y"}
used = {b["patient"] for b in retail_bookings if b["channel"] == "at-home" and b["patient"] in took
        and dt.date.fromisoformat(took[b["patient"]]) <= b["date"] <= hi}
check("accepted and booked a collection at home in the window", len(used), 259)
check("accepted and booked none", len(took) - len(used), 689)
check("bookings per offered patient", round(per_patient(offered), 3), 0.633)
check("bookings per patient not offered", round(per_patient(others), 3), 0.581)
check("the report's lift", round(per_patient(offered) / per_patient(others) - 1, 3), 0.090)
lift = {}
for metro in ("Dallas", "Atlanta", "Phoenix", "New York", "Chicago", "Philadelphia"):
    o = [p for p in offered if p["metro"] == metro]
    r = [p for p in others if p["metro"] == metro]
    lift[metro] = per_patient(o) / per_patient(r) - 1
for metro, want in {"Dallas": -0.108, "Atlanta": -0.199, "Phoenix": -0.130, "New York": 0.235,
                    "Chicago": -0.048, "Philadelphia": 0.006}.items():
    check(f"lift inside {metro}", round(lift[metro], 3), want)
camp = ("Dallas", "Atlanta", "Phoenix")
check("share offered, campaign metros", round(sum(1 for p in offered if p["metro"] in camp)
                                              / sum(1 for p in patients if p["metro"] in camp), 3), 0.505)
check("share offered, other metros", round(sum(1 for p in offered if p["metro"] not in camp)
                                           / sum(1 for p in patients if p["metro"] not in camp), 3), 0.214)
rate = {m: per_patient([p for p in patients if p["metro"] == m]) for m in lift}
check("every campaign metro books more per patient than every other metro",
      min(rate[m] for m in camp) > max(rate[m] for m in lift if m not in camp), True)
before = {}
for b in retail_bookings:
    if dt.date(2026, 4, 1) <= b["date"] < lo:
        before[b["patient"]] = before.get(b["patient"], 0) + 1
for metro, want in {"Dallas": 0.014, "Atlanta": -0.052, "Phoenix": -0.061}.items():
    o = [p for p in offered if p["metro"] == metro]
    r = [p for p in others if p["metro"] == metro]
    gap_before = (sum(before.get(p["patient_id"], 0) for p in o) / len(o)
                  / (sum(before.get(p["patient_id"], 0) for p in r) / len(r)) - 1)
    check(f"gap before the offer, {metro}", round(gap_before, 3), want)


def booked(metros, a, b):
    return sum(1 for x in retail_bookings if x["metro"] in metros and a <= x["date"] <= b)


pre_lo, pre_hi = dt.date(2026, 5, 14), dt.date(2026, 7, 14)
check("campaign metros, the two months before against the six weeks before them, per day",
      round(booked(camp, pre_lo, pre_hi) / 62 / (booked(camp, dt.date(2026, 4, 1), dt.date(2026, 5, 13)) / 43) - 1, 3), 0.069)
check("campaign metros into the offer's weeks", round(booked(camp, lo, hi) / booked(camp, pre_lo, pre_hi) - 1, 3), 0.074)
check("New York over the same weeks", round(booked(("New York",), lo, hi) / booked(("New York",), pre_lo, pre_hi) - 1, 3), 0.030)
ny = [p for p in patients if p["metro"] == "New York"]
ny_counts = [in_window.get(p["patient_id"], 0) for p in ny]
ny_labels = [p["patient_id"] in offered_ids for p in ny]


def ny_lift(labels):
    o = [c for c, l in zip(ny_counts, labels) if l]
    r = [c for c, l in zip(ny_counts, labels) if not l]
    return (sum(o) / len(o)) / (sum(r) / len(r)) - 1


observed = ny_lift(ny_labels)
shuffler = random.Random(20261019)
as_large = 0
for _ in range(10000):
    labels = ny_labels[:]
    shuffler.shuffle(labels)
    as_large += abs(ny_lift(labels)) >= abs(observed)
check("New York's permutation p, two-sided, 10,000 shuffles", round(as_large / 10000, 2), 0.03, 0.006)
check("chance of at least one false positive in six tests at 0.05", round(1 - 0.95 ** 6, 2), 0.26, 0.006)

print("\n== The technical half's invented arithmetic, question by question")
check("T01-L3 orders per practice change", round(108 / 120 - 1, 3), -0.100)
check("T01-L3 fewer requisitions", 600 * (120 - 108), 7200)
check("T02-L1 points of the fall from one plan's missing Friday", round(0.70 * (1 - 4 / 5) * 100, 1), 14.0)
check("T03-L3 pickups set aside", 130 + 70 + 20, 220)
check("T03-L3 matched plus set aside", 3960 + 220, 4180)
check("T03-L3 dollars at $16 a stop", [130 * 16, 70 * 16, 20 * 16, 220 * 16], [2080, 1120, 320, 3520])
check("T04-L2 one draw moves the rate, points", 100 / 25, 4.0)
check("T04-L2 chance of 2 or more in 25 at 4 percent", round(tail(25, 2, 0.04), 2), 0.26, 0.006)
check("T04-L2 chance of 8 or more in 100 at 4 percent", round(tail(100, 8, 0.04), 3), 0.048, 0.0006)
check("T04-L3 denials prevented a month", round(0.025 * 4000), 100)
check("T04-L3 forgone a month by a fifth held back", round(0.025 * 4000 / 5), 20)
check("T05-L2 late share, month before", round(1900 / 42000 * 100, 1), 4.5)
check("T05-L2 late share, last month", round(2300 / 52000 * 100, 1), 4.4)
check("T05-L2 late samples rose", round((2300 / 1900 - 1) * 100), 21)
check("T05-L2 samples rose", round((52000 / 42000 - 1) * 100), 24)
check("T05-L2 share within the promise, about", round((1 - 2300 / 52000) * 100, 1), 95.6)
check("T05-L2 share within the promise the month before", round((1 - 1900 / 42000) * 100, 1), 95.5)
check("T05-L2 late share with volume flat", round(2300 / 42000 * 100, 1), 5.5)
check("T06-L2 the real redraw rate", round(37 / 2400 * 100, 1), 1.5)
check("T06-L2 what integer division returns", 37 // 2400, 0)
check("T07-L2 rows after the join over lines before", round(79600 / 41200, 2), 1.93)
ranks, ties = [], [70, 69, 68] + [65] * 21 + [61, 61, 58]
for i, v in enumerate(ties):
    ranks.append(1 + sum(1 for w in ties if w > v))
check("T08-L3 rows RANK ships at a tie on 25th", sum(1 for r in ranks if r <= 25), 26)
check("T09-L3 days read a week late", [d + 7 for d in (83, 89)], [90, 96])

print("\n== The day's grid")
SLOT, CHANGE, BLOCK, HUDDLE, CLOSE, ASSESSORS = 20, 5, 180, 10, 15, 3
per_block1 = (BLOCK - HUDDLE) // (SLOT + CHANGE)
per_block2 = (BLOCK - CLOSE) // (SLOT + CHANGE)
check("slots in block 1", per_block1, 6)
check("slots in block 2", per_block2, 6)
check("places in the day", (per_block1 + per_block2) * ASSESSORS, 36)
groups = [(f"G{g}", 4) for g in range(1, 9)] + [("G9", 3)]
check("learners", sum(n for _, n in groups), 35)
queue = [(g, s) for s in range(1, 5) for g, n in groups if s <= n]
names = ["Programme Head", "Academic TA", "Principal Advisor"]


def set_letter(g, s):
    return "ABCDEFGH"[(int(g[1:]) + s - 2) % 8]


grid, last_end = [], {}
for slot in range(1, per_block1 + per_block2 + 1):
    block = 1 if slot <= per_block1 else 2
    start = HUDDLE + (slot - 1) * (SLOT + CHANGE) if block == 1 else (slot - per_block1 - 1) * (SLOT + CHANGE)
    row = []
    for a in range(ASSESSORS):
        pos = (slot - 1) * ASSESSORS + a
        if pos < len(queue):
            g, s = queue[pos]
            row.append(f"{g}-S{s}, set {set_letter(g, s)}")
            last_end[names[a]] = (block, start + SLOT)
        else:
            row.append("Spare")
    grid.append((slot, f"Block {block}, {start} to {start + SLOT}", row))
check("no two group-mates in one slot",
      all(len({cell.split('-')[0] for cell in row if cell != 'Spare'}) == len([c for c in row if c != 'Spare'])
          for _, _, row in grid), True)
check("last mock, Programme Head", last_end["Programme Head"], (2, 145))
check("last mock, Academic TA", last_end["Academic TA"], (2, 145))
check("last mock, Principal Advisor", last_end["Principal Advisor"], (2, 120))
check("learners per assessor", [sum(1 for _, _, row in grid if row[a] != "Spare") for a in range(3)], [12, 12, 11])
check("checks 1, 2 and 3 across nine groups, minutes", [2 * 9, 3 * 9, 5 * 9], [18, 27, 45])
sheet = (DAY / "trainer" / "C2_W03_D04_day_sheet_TRAINER.md").read_text(encoding="utf-8")
printed = {}
for line in sheet.splitlines():
    m = re.match(r"\| (\d{1,2}) \| (Block \d, \d+ to \d+) \| (.+?) \| (.+?) \| (.+?) \|$", line)
    if m:
        printed[int(m.group(1))] = (m.group(2), [m.group(3), m.group(4), m.group(5)])
check("the day sheet prints every slot", sorted(printed), list(range(1, 13)))
check("the day sheet's grid matches the call order", all(printed.get(s) == (when, row) for s, when, row in grid), True)

print("\n== The guard: no plant in a STUDENT file, none in the technical half's spoken words")
PLANT_WORDS = ["walk-in", "walkin", "employer", "wellness screening", "re-export", "repeated row",
               "double post", "posted twice", "paid twice", "loaded twice", "system switch", "switched system",
               "new booking system", "new system", "month first", "claim_ref", "CLM-", "KH-CLM", "EMP-",
               "ORD-", "PHL-", "target", "at random", "already rising", "component", "dashboard's count",
               "rebook"]
PLANTED_VALUES = ["23,213", "24,406", "25,022", "22,468", "24,399", "5,692", "6,009", "5.1 percent",
                  "7.8 percent", "8.6 percent", "5.6 percent", "180,000", "14.6", "1,231,001", "210.50",
                  "179.75", "$150", "970,098", "26.9", "8.3 percent", "22,152", "46,867", "48,235",
                  "1,102", "$20", "1,415", "1,090", "1,243", "23.0 percent", "12.2", "11,729", "11,549",
                  "18 September", "17 September", "1.9 percent", "2,269", "8,858", "19,204", "398",
                  "253,165", "1,175", "1,137", "10.35", "10.4 percent", "14.9", "11.3", "230,132", "801,31",
                  "2,201,099", "36.4", "18.8", "7.9 percent", "19.0 percent", "15.1", "15 of 79", "0.21",
                  "0.0014", "9.0 percent", "10.8", "19.9", "13.0 percent", "50.5", "21.4", "6.9 percent",
                  "23.5", "0.03", "2,381", "948", "6,000", "1,200"]


def plant_hits(text):
    """Plant words anywhere, and planted values as whole numbers, so 41,200 never reads as 1,200."""
    words = [w for w in PLANT_WORDS if w.lower() in text.lower()]
    values = [v for v in PLANTED_VALUES if re.search(r"(?<![\d,.$])" + re.escape(v) + r"(?![\d])", text)]
    return words + values


student_files = sorted(DAY.rglob("*_STUDENT.md"))
check("STUDENT markdown files in the pack", len(student_files), 1)
for f in student_files:
    check(f"plant words or planted values in {f.name}", plant_hits(f.read_text(encoding="utf-8")), [])
bank = (DAY / "mocks" / "C2_W03_D04_mock_question_bank_TRAINER.md").read_text(encoding="utf-8")
spoken = [line for line in bank.splitlines() if line.startswith("| Ask |") or line.startswith("| Follow-up |")]
check("spoken rows in the bank, an ask and a follow-up for 30 questions", len(spoken), 60)
spoken_text = "\n".join(spoken)
check("plant words or planted values in the technical half's spoken rows", plant_hits(spoken_text), [])

print("\nRESULT:", "FAIL" if FAILS else "PASS", f"({len(FAILS)} drifts)")
for label in FAILS:
    print("  drifted:", label)
sys.exit(1 if FAILS else 0)

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W03/D4/internal/C2_W03_D04_numbers_INTERNAL.py
#     Reads the ten CSV files in content/W03/D1/data/ and Thursday's own markdown, prints every number
#     with the pack's figure beside it, and ends on "RESULT: PASS (0 drifts)" with exit 0 while the data
#     pack and the pack's files are unchanged. The New York permutation test shuffles with seed
#     20261019, so its p prints the same on every run.
# The same command after the data pack is regenerated with a different seed
#     One FAIL line per number that moved, the list of drifted labels, and exit 1: the viva prompts,
#     the day sheet and the provenance need their numbers rewritten before the pack ships again.
# The same command after a STUDENT file gains a plant word such as "walk-in"
#     A FAIL line naming the file and the word, and exit 1.

"""Recompute every number the Build 1 Wednesday pack quotes, from the ten Kalpa Health files.

    python3 content/W03/D3/internal/C2_W03_D03_numbers_INTERNAL.py

The files are read where Monday's pack keeps them, content/W03/D1/data/, the way a group would read
them: every value as text, the old booking export kept at one row per booking_id (the row with the
later updated_at), the new system's month-first dates read as month, day, year, and billed amounts
converted after the dollar sign and any comma are removed. The quarters are calendar Q2 (April to
June) and Q3 (July to September) of 2026, in the US pack of decision build1-us-data, and the visit
register is the one drawn from the bookings on 1 October 2026 (decision
build1-register-from-bookings).

Every number the day sheet, the checkpoint guide, the catch-up plan, the run sheet, the headline
sheet and the parallel build quote is printed here under the file that quotes it. Where the
generator's witness (python3 data/generate_kalpa_health.py --witness) carries the same number, the
script runs the generator, reads its witness and asserts the two agree; where only the spine or
Monday's day sheet carries it, the figure is asserted against the value written there. It ends on
PASS, or stops on the first number that drifted.
"""
import math
import pathlib
import random
import subprocess
import sys

import numpy as np
import pandas as pd

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents
            if (p / "scripts").is_dir() and (p / "content").is_dir())
DATA = ROOT / "content/W03/D1/data"
OUT = {}


def read(name):
    return pd.read_csv(DATA / f"C2_W03_D01_{name}_STUDENT.csv", dtype=str, keep_default_na=False)


def quarter(iso_dates):
    return np.where(iso_dates < "2026-07-01", "Q2", "Q3")


def us_to_iso(d):
    """The new system writes month/day/year; the old one writes ISO dates."""
    month, day, year = d.split("/")
    return f"{year}-{int(month):02d}-{int(day):02d}"


def dollars(text):
    return text.str.replace("$", "", regex=False).str.replace(",", "", regex=False).astype(float)


def plain(value):
    """Numbers as Python prints them, so a line reads 9575.0 rather than np.float64(9575.0)."""
    if isinstance(value, dict):
        return {plain(k): plain(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return type(value)(plain(v) for v in value)
    if isinstance(value, np.generic):
        return value.item()
    return value


def put(key, value):
    OUT[key] = plain(value)


raw_legacy, newsys, claims = read("bookings_legacy"), read("bookings_newsys"), read("claims")
postings, register, campaign = read("remittances"), read("appointments"), read("campaign")
patients, sites, lines = read("patients"), read("sites"), read("booking_tests")

legacy = raw_legacy.sort_values("updated_at").drop_duplicates("booking_id", keep="last").copy()
legacy["q"] = quarter(legacy["booking_date"])
claims["amt"] = dollars(claims["billed_amount"])
claims["q"] = quarter(claims["service_date"])
NEW_CODE = dict(zip(sites["new_system_code"], sites["site_code"]))
NEW_CHANNEL = {"WALKIN": "walk-in", "WEB": "online", "CALL": "phone", "MOBILEDRAW": "at-home"}
new = pd.DataFrame({"booking_id": newsys["bkg_ref"], "patient_id": "P-" + newsys["patient"],
                    "site_code": newsys["site"].map(NEW_CODE), "metro": newsys["metro"],
                    "booking_date": newsys["created"].map(us_to_iso),
                    "channel": newsys["channel"].map(NEW_CHANNEL),
                    "status": newsys["state"].map({"DONE": "completed", "CXL": "cancelled"})})
new["q"] = quarter(new["booking_date"])
both = pd.concat([legacy.assign(system="old"), new.assign(system="new")], ignore_index=True)

# ---------------------------------------------------------------- the New York slice
# Quoted by the notebook, its run sheet, the headline sheet and the day sheet's interview answer.
ny_raw = raw_legacy[raw_legacy["metro"] == "New York"].copy()
ny_raw["q"] = quarter(ny_raw["booking_date"])
ny = legacy[legacy["metro"] == "New York"]
nyc = claims[claims["metro"] == "New York"].copy()
pairs = ny_raw[ny_raw["booking_id"].duplicated(keep=False)].groupby("booking_id")
put("ny rows, distinct ids, repeated ids", (len(ny_raw), ny_raw["booking_id"].nunique(), pairs.ngroups))
put("ny repeated pairs identical, differing only in updated_at",
    (sum(len(g.drop_duplicates()) == 1 for _, g in pairs),
     sum(len(g.drop_duplicates()) == 2 and len(g.drop(columns=["updated_at"]).drop_duplicates()) == 1
         for _, g in pairs)))
put("ny extra rows by quarter", (ny_raw.groupby("q").size() - ny.groupby("q").size()).to_dict())
put("ny rows per quarter", ny_raw.groupby("q").size().to_dict())
put("ny bookings per quarter", ny.groupby("q").size().to_dict())
put("ny change on rows, on bookings", (round(1089 / 1039 - 1, 4), round(1082 / 1013 - 1, 4)))
put("ny blank channel rows", int((ny["channel"] == "").sum()))
put("ny claims rows, distinct claim ids", (len(nyc), nyc["claim_id"].nunique()))
coerced = pd.to_numeric(nyc["billed_amount"], errors="coerce")
put("ny text amounts", nyc.loc[coerced.isna(), "billed_amount"].tolist())
put("ny dollars hidden by coerce, by quarter", nyc[coerced.isna()].groupby("q")["amt"].sum().to_dict())
put("ny coerced totals", coerced.groupby(nyc["q"]).sum().to_dict())
put("ny largest claim", float(nyc["amt"].max()))
fanned = ny_raw.merge(nyc, on="booking_id")
put("ny fanned join rows, dollars; claims dollars", (len(fanned), round(fanned["amt"].sum(), 2),
                                                     round(nyc["amt"].sum(), 2)))
put("ny fanned extra by quarter", (fanned.groupby("q_y")["amt"].sum() - nyc.groupby("q")["amt"].sum()).round(2).to_dict())
put("ny kept, cancelled, completed, claims",
    (len(ny), int((ny["status"] == "cancelled").sum()), int((ny["status"] == "completed").sum()), len(nyc)))
put("ny cancelled by quarter", ny[ny["status"] == "cancelled"].groupby("q").size().to_dict())
tree = nyc.groupby("q")["amt"].agg(["count", "sum", "mean", "median"])
put("ny tree", tree.round(4).to_dict("index"))
q2, q3 = tree.loc["Q2"], tree.loc["Q3"]
volume = (q3["count"] - q2["count"]) * q2["mean"]
value = q3["count"] * (q3["mean"] - q2["mean"])
put("ny change in dollars, percent", (round(q3["sum"] - q2["sum"], 2), round(q3["sum"] / q2["sum"] - 1, 4)))
put("ny claims change, mean change, mean change in dollars",
    (round(q3["count"] / q2["count"] - 1, 4), round(q3["mean"] / q2["mean"] - 1, 4), round(q3["mean"] - q2["mean"], 2)))
put("ny bridge volume, value", (round(volume), round(value)))
put("ny per day change, claims and billed",
    (round(float((q3["count"] / 92) / (q2["count"] / 91) - 1), 4),
     round(float((q3["sum"] / 92) / (q2["sum"] / 91) - 1), 4)))
put("ny per day claims, billed", ((round(q2["count"] / 91, 2), round(q3["count"] / 92, 2)),
                                  (round(q2["sum"] / 91, 2), round(q3["sum"] / 92, 2))))
m = ny.merge(nyc, on="booking_id", suffixes=("", "_c"))
by_site = m.groupby(["site_code", "q_c"])["amt"].agg(["count", "sum"])
put("ny claims and billed by site", {k: (int(v["count"]), round(v["sum"], 2)) for k, v in by_site.iterrows()})
put("ny site kinds", dict(zip(sites.loc[sites["metro"] == "New York", "site_code"],
                              sites.loc[sites["metro"] == "New York", "kind"])))

# Why New York's mean claim fell, for the run sheet's plant table only (TRAINER): the home
# collections, and the collection fee a claim carries above the list prices booked.
listed = lines[lines["line"].isin(["test", "panel"])].assign(
    v=lambda d: d["price_each"].astype(float) * d["quantity"].astype(int)).groupby("booking_id")["v"].sum()
m["fee"] = (m["amt"] - m["booking_id"].map(listed)).round(2)
home = m[m["channel"] == "at-home"]
put("ny home claims by quarter, their mean", (home.groupby("q_c").size().to_dict(),
                                              home.groupby("q_c")["amt"].mean().round(2).to_dict()))
put("ny home claims with no fee, by quarter; all from offered patients",
    (home[home["fee"] == 0].groupby("q_c").size().to_dict(),
     bool(home.loc[home["fee"] == 0, "patient_id"].isin(campaign["patient_id"]).all())))
put("ny other claims' mean by quarter", m[m["channel"] != "at-home"].groupby("q_c")["amt"].mean().round(2).to_dict())
put("ny claims with a $20 fee line", int((m["fee"] == 20).sum()))

# The sizing cell's four options, on the New York files as exported.
put("ny option rows read: totals, claims tree, reconciled tree, export tree",
    (len(nyc), len(nyc), len(ny_raw) + len(nyc), len(ny_raw)))
rows_q = ny_raw.groupby("q").size()
put("ny option D: billed per export row", (round(q2["sum"] / rows_q["Q2"], 2), round(q3["sum"] / rows_q["Q3"], 2)))

# The second route, in SQL: SQLite is in Python's standard library, so the query runs with no server.
import sqlite3  # noqa: E402

con = sqlite3.connect(":memory:")
ny_raw.drop(columns=["q"]).to_sql("bookings", con, index=False)
claims.drop(columns=["amt", "q"]).to_sql("claims", con, index=False)
sql = """
WITH ranked AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY booking_id ORDER BY updated_at DESC) AS n FROM bookings),
kept AS (SELECT * FROM ranked WHERE n = 1 AND status = 'completed')
SELECT CASE WHEN c.service_date < '2026-07-01' THEN 'Q2' ELSE 'Q3' END AS quarter,
       COUNT(*) AS claims,
       ROUND(SUM(CAST(REPLACE(REPLACE(c.billed_amount, '$', ''), ',', '') AS REAL)), 2) AS billed
FROM kept JOIN claims c ON c.booking_id = kept.booking_id
GROUP BY quarter ORDER BY quarter"""
put("ny second route in SQL", [tuple(r) for r in con.execute(sql)])

# ---------------------------------------------------------------- the headline, for every group
tests_on = lines[lines["line"].isin(["test", "component"])].assign(n=lambda d: d["quantity"].astype(int)) \
    .groupby("booking_id")["n"].sum()
retail = both[both["channel"] != "employer"].assign(tests=lambda d: d["booking_id"].map(tests_on).fillna(0))
first_rows = raw_legacy.drop_duplicates("booking_id", keep="first")
dash = retail[retail["system"] == "old"].groupby("q")["tests"].sum()
booked = retail.groupby("q")["tests"].sum()
performed = retail[retail["status"] == "completed"].groupby("q")["tests"].sum()
bookings_q = retail.groupby("q").size()
raw_rows = raw_legacy[raw_legacy["channel"] != "employer"].assign(
    tests=lambda d: d["booking_id"].map(tests_on).fillna(0), q=lambda d: quarter(d["booking_date"]))
raw_tests = raw_rows.groupby("q")["tests"].sum()
emp_tests = int(both.loc[both["channel"] == "employer", "booking_id"].map(tests_on).sum())
put("headline dashboard, booked, performed, bookings, raw rows (Q2, Q3)",
    {k: (int(v["Q2"]), int(v["Q3"])) for k, v in
     {"dashboard": dash, "booked": booked, "performed": performed, "bookings": bookings_q,
      "raw rows": raw_tests}.items()})
put("headline changes", {k: round(v["Q3"] / v["Q2"] - 1, 4) for k, v in
                         {"dashboard": dash, "booked": booked, "performed": performed,
                          "bookings": bookings_q, "raw rows": raw_tests}.items()})
put("headline employer tests, booked change with them",
    (emp_tests, round((booked["Q3"] + emp_tests) / booked["Q2"] - 1, 4)))

# ---------------------------------------------------------------- sub-problem 1, revenue
co_all = pd.to_numeric(claims["billed_amount"], errors="coerce")
put("sp1 claims rows, distinct, text amounts, coerced total, true total, hidden",
    (len(claims), claims["claim_id"].nunique(), int(co_all.isna().sum()), round(co_all.sum(), 2),
     round(claims["amt"].sum(), 2), round(claims["amt"].sum() - co_all.sum(), 2)))
put("sp1 text amount examples", claims.loc[co_all.isna(), "billed_amount"].head(3).tolist())
put("sp1 claims per quarter", claims.groupby("q").size().to_dict())
put("sp1 billed per quarter", claims.groupby("q")["amt"].sum().round(2).to_dict())
emp = claims[claims["employer_account"] != ""]
put("sp1 employer claim", emp[["claim_id", "metro", "service_date", "amt", "employer_account"]].values.tolist())
q3c, q2c = claims[claims["q"] == "Q3"], claims[claims["q"] == "Q2"]
put("sp1 Q3 billed, without contract, contract share",
    (round(q3c["amt"].sum(), 2), round(q3c.loc[q3c["employer_account"] == "", "amt"].sum(), 2),
     round(emp["amt"].sum() / q3c["amt"].sum(), 4)))
put("sp1 growth with, without contract",
    (round(q3c["amt"].sum() / q2c["amt"].sum() - 1, 4),
     round(q3c.loc[q3c["employer_account"] == "", "amt"].sum() / q2c["amt"].sum() - 1, 4)))
put("sp1 Q2 mean, Q3 mean, Q3 mean without contract, medians",
    (round(q2c["amt"].mean(), 2), round(q3c["amt"].mean(), 2),
     round(q3c.loc[q3c["employer_account"] == "", "amt"].mean(), 2),
     float(q2c["amt"].median()), float(q3c["amt"].median())))
put("sp1 largest retail claim", float(claims.loc[claims["employer_account"] == "", "amt"].max()))
put("sp1 old-export completed, new-system done, claims",
    (int((legacy["status"] == "completed").sum()), int((new["status"] == "completed").sum()), len(claims)))
claim_lines = claims.loc[claims["employer_account"] == "", "line_items"].astype(int)
tests = lines[lines["line"].isin(["test", "component"]) & (lines["panel_code"] != "PNL-EMP")]
done = set(both.loc[both["status"] == "completed", "booking_id"])
put("sp1 claim lines, tests on completed bookings, tests on all bookings",
    (int(claim_lines.sum()), int(tests["booking_id"].isin(done).sum()), len(tests)))
put("sp1 claims with a booking in the old export, in the new export",
    (int(claims["booking_id"].isin(legacy["booking_id"]).sum()), int(claims["booking_id"].isin(new["booking_id"]).sum())))

# ---------------------------------------------------------------- sub-problem 2, bookings
put("sp2 old export rows, distinct ids; new system rows by metro",
    (len(raw_legacy), raw_legacy["booking_id"].nunique(), newsys["metro"].value_counts().to_dict()))
put("sp2 old export dates; new system dates as written",
    ((raw_legacy["booking_date"].min(), raw_legacy["booking_date"].max()),
     (newsys["created"].min(), newsys["created"].max())))
rb = both[both["channel"] != "employer"]
sw = ("Chicago", "Philadelphia")


def count(metros, system=None, q=None):
    d = rb[rb["metro"].isin(metros)]
    if system:
        d = d[d["system"] == system]
    if q:
        d = d[d["q"] == q]
    return len(d)


put("sp2 two metros Q2, Q3 old only, Q3 both", (count(sw, q="Q2"), count(sw, "old", "Q3"), count(sw, q="Q3")))
for metro in ("Chicago", "Philadelphia", "Dallas", "Phoenix", "New York", "Atlanta"):
    put(f"sp2 {metro} Q2, Q3 old only, Q3 both",
        (count((metro,), q="Q2"), count((metro,), "old", "Q3"), count((metro,), q="Q3")))
sw_raw = raw_legacy[raw_legacy["metro"].isin(sw) & (raw_legacy["channel"] != "employer")]
put("sp2 two metros rows before the identity rule", pd.Series(quarter(sw_raw["booking_date"])).value_counts().to_dict())
claims_q3 = claims[claims["q"] == "Q3"].groupby("metro").size()
comp_q3 = legacy[(legacy["q"] == "Q3") & (legacy["status"] == "completed")].groupby("metro").size()
put("sp2 Q3 claims less old-export completed, by metro", (claims_q3 - comp_q3).to_dict())
copies = raw_legacy.groupby("booking_id")
rep = copies.filter(lambda g: len(g) > 1)
put("sp2 repeated ids, first and last booking date", (rep["booking_id"].nunique(), rep["booking_date"].min(), rep["booking_date"].max()))

# ---------------------------------------------------------------- sub-problem 3, billing
ref = postings["claim_ref"]
form = np.where(ref.str.startswith("KH-CLM-"), "the claim id", np.where(ref.str.startswith("CLM-"), "CLM-number", "bare digits"))
put("sp3 posting rows, forms, kinds", (len(postings), pd.Series(form).value_counts().to_dict(),
                                       postings["posting"].value_counts().to_dict()))
claim_ids = set(claims["claim_id"])
by_digits = {x.split("-")[-1]: x for x in claim_ids}


def normalise(r):
    if r in claim_ids:
        return r
    if r.startswith("CLM-"):
        return by_digits.get(f"{int(r[4:]):06d}")
    return by_digits.get(r)


postings["claim"] = ref.map(normalise)
postings["paid"] = postings["paid_amount"].astype(float)
pay = postings[postings["posting"] == "payment"]
double = pay[pay.duplicated(["claim_ref", "paid_amount"])]
reversal = postings[postings["posting"] == "reversal"]
unposted = claims[~claims["claim_id"].isin(postings["claim"])]
put("sp3 exact matches, share, unmatched after the rule", (int(ref.isin(claim_ids).sum()),
                                                          round(ref.isin(claim_ids).mean(), 4),
                                                          int(postings["claim"].isna().sum())))
put("sp3 double posts, dollars; reversals, dollars", (len(double), round(double["paid"].sum(), 2),
                                                      len(reversal), round(reversal["paid"].sum(), 2)))
put("sp3 raw paid column sum, paid net of double posts",
    (round(postings["paid"].sum(), 2), round(postings["paid"].sum() - double["paid"].sum(), 2)))
put("sp3 claims with no posting, dollars, employer claim among them",
    (len(unposted), round(unposted["amt"].sum(), 2), bool(emp["claim_id"].isin(unposted["claim_id"]).all())))
retail_claims = claims[claims["employer_account"] == ""]
denied = retail_claims[retail_claims["denial_category"] != ""]
put("sp3 retail claims, marked denied, rate, billed",
    (len(retail_claims), len(denied), round(len(denied) / len(retail_claims), 4), round(denied["amt"].sum(), 2)))
put("sp3 denial rate by payer", {p: round((g["denial_category"] != "").mean(), 4)
                                 for p, g in retail_claims.groupby("payer_type")})
den_post = postings[postings["posting"] == "denial"]
put("sp3 denial postings, paying nothing; denied claims with no posting",
    (len(den_post), int((den_post["paid"] == 0).sum()), len(set(denied["claim_id"]) - set(postings["claim"]))))
billed_all = claims["amt"].sum()
paid_net = postings["paid"].sum() - double["paid"].sum()
put("sp3 billed all, paid net share", (round(billed_all, 2), round(paid_net / billed_all, 4)))
contractual = postings.loc[(postings["posting"] == "payment") & ~postings.index.isin(double.index), "adjustment_amount"].astype(float).sum()
put("sp3 contractual adjustments on payments (double posts excluded)", round(contractual, 2))

# ---------------------------------------------------------------- sub-problem 4, no-shows
small = register["site_code"] == "KH-ATL-03"
sched = register["kind"] == "scheduled"
miss = register["attended"] == "N"
put("sp4 rows, centres, kinds, dates", (len(register), register["site_code"].nunique(),
                                        register["kind"].value_counts().to_dict(),
                                        (register["visit_date"].min(), register["visit_date"].max())))
per_centre = register.groupby("site_code").agg(rows=("kind", "size"), walk_ins=("kind", lambda s: int((s == "walk-in").sum())))
put("sp4 rows per centre", per_centre["rows"].to_dict())
put("sp4 small all, others all, small scheduled, others scheduled",
    ((int((small & miss).sum()), int(small.sum())), (int((~small & miss).sum()), int((~small).sum())),
     (int((small & sched & miss).sum()), int((small & sched).sum())),
     (int((~small & sched & miss).sum()), int((~small & sched).sum()))))
put("sp4 small walk-ins; walk-ins marked not attended", (int((small & ~sched).sum()), int((~sched & miss).sum())))
rates = register.assign(n=miss).groupby("site_code")["n"].mean()
rates_s = register[sched].assign(n=miss[sched]).groupby("site_code")["n"].mean()
put("sp4 next worst rate, all visits and scheduled",
    (round(rates.drop("KH-ATL-03").max(), 4), round(rates_s.drop("KH-ATL-03").max(), 4)))


def tail(n, k, p):
    return sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k, n + 1))


p_sched = (~small & sched & miss).sum() / (~small & sched).sum()
p_all = (~small & miss).sum() / (~small).sum()
put("sp4 chance tail on scheduled, on all visits", (round(tail(79, 15, p_sched), 4), round(tail(80, 15, p_all), 4)))
bk = both[["booking_id", "site_code", "booking_date", "channel", "status"]]
reg = register.merge(bk, on="booking_id", how="left", suffixes=("", "_b"), indicator=True)
put("sp4 register rows with a booking, at the same centre",
    (int((reg["_merge"] == "both").sum()), int((reg["site_code"] == reg["site_code_b"]).sum())))
put("sp4 register: distinct bookings, bookings with two rows",
    (register["booking_id"].nunique(), int((register["booking_id"].value_counts() == 2).sum())))
put("sp4 register rows by booking status, kind, attended",
    reg.groupby(["status", "kind", "attended"]).size().to_dict())
centres = set(sites.loc[sites["kind"] == "patient service center", "site_code"])
q3_centre = both[(both["q"] == "Q3") & both["site_code"].isin(centres) & (both["channel"] != "at-home")]
gone = q3_centre[~q3_centre["booking_id"].isin(register["booking_id"])]
put("sp4 Q3 centre bookings not at home, with no register row, by status and channel",
    (len(q3_centre), len(gone), gone.groupby(["status", "channel"]).size().to_dict()))
sb = register[small & sched].groupby("booking_id")["attended"].apply(lambda s: (s == "N").any())
ob = register[~small & sched].groupby("booking_id")["attended"].apply(lambda s: (s == "N").any())
put("sp4 per booking: small scheduled bookings, missing a slot; others' share; tail",
    (len(sb), int(sb.sum()), round(ob.mean(), 4), round(tail(len(sb), int(sb.sum()), ob.mean()), 4)))

# ---------------------------------------------------------------- sub-problem 5, the campaign
window = legacy[(legacy["booking_date"] >= "2026-07-15") & (legacy["booking_date"] <= "2026-09-14")
                & (legacy["channel"] != "employer")]
per = window.groupby("patient_id").size()
patients["n"] = patients["patient_id"].map(per).fillna(0)
patients["offered"] = patients["patient_id"].isin(campaign["patient_id"])


def lift(df):
    return round(float(df[df["offered"]]["n"].mean() / df[~df["offered"]]["n"].mean() - 1), 4)


put("sp5 offered, took up, by metro, dates", (len(campaign), int((campaign["took_up"] == "Y").sum()),
                                              campaign["metro"].value_counts().to_dict(),
                                              (campaign["offered_on"].min(), campaign["offered_on"].max())))
reg5 = campaign.merge(patients, on="patient_id", how="left", suffixes=("", "_p"), indicator=True)
put("sp5 offered found in the register, in the same metro",
    (int((reg5["_merge"] == "both").sum()), int((reg5["metro"] == reg5["metro_p"]).sum())))
put("sp5 offered with a booking in the window, with any booking in the old export",
    (int(campaign["patient_id"].isin(window["patient_id"]).sum()), int(campaign["patient_id"].isin(legacy["patient_id"]).sum())))
off, rest = patients[patients["offered"]], patients[~patients["offered"]]
put("sp5 bookings per patient offered, rest (patients, bookings)",
    ((len(off), int(off["n"].sum()), round(off["n"].mean(), 4)), (len(rest), int(rest["n"].sum()), round(rest["n"].mean(), 4))))
put("sp5 lift overall and by metro", (lift(patients), {c: lift(patients[patients["metro"] == c])
                                                       for c in sorted(patients["metro"].unique())}))
camp = ("Dallas", "Atlanta", "Phoenix")
put("sp5 offered share, campaign metros and elsewhere",
    (round(patients[patients["metro"].isin(camp)]["offered"].mean(), 4),
     round(patients[~patients["metro"].isin(camp)]["offered"].mean(), 4)))
before = legacy[(legacy["booking_date"] >= "2026-04-01") & (legacy["booking_date"] < "2026-07-15")
                & (legacy["channel"] != "employer")].groupby("patient_id").size()
patients["b"] = patients["patient_id"].map(before).fillna(0)
put("sp5 gap before the offer", {c: round(float(g[g["offered"]]["b"].mean() / g[~g["offered"]]["b"].mean() - 1), 4)
                                 for c, g in patients[patients["metro"].isin(camp)].groupby("metro")})
ny_p = patients[patients["metro"] == "New York"]
counts, labels = ny_p["n"].to_numpy(), ny_p["offered"].to_numpy()


def ny_lift(lab):
    return counts[lab].mean() / counts[~lab].mean() - 1


observed, shuffler, as_large = ny_lift(labels), random.Random(20261019), 0
for _ in range(10000):
    shuffled = labels.copy()
    shuffler.shuffle(shuffled)
    as_large += abs(ny_lift(shuffled)) >= abs(observed)
put("sp5 New York permutation p, two-sided", round(as_large / 10000, 4))


def witness():
    """The generator's witness, read as text so this script never imports the generator."""
    run = subprocess.run([sys.executable, str(ROOT / "data/generate_kalpa_health.py"), "--witness"],
                         capture_output=True, text=True, check=True)
    out = {}
    for line in run.stdout.splitlines():
        if ": " in line:
            k, v = line.split(": ", 1)
            out[k.strip()] = v.strip()
    return out


def close(a, b, tol=0.0005):
    return abs(float(a) - float(b)) <= tol


def same(mine, theirs):
    """Equal item by item: counts exactly, shares and dollars to the rounding the files print."""
    if isinstance(theirs, (list, tuple)):
        return len(mine) == len(theirs) and all(same(a, b) for a, b in zip(mine, theirs))
    if isinstance(theirs, float):
        return close(mine, theirs, 0.0006)
    return mine == theirs


if __name__ == "__main__":
    for k, v in OUT.items():
        print(f"{k}: {v}")
    W = witness()
    checks = [
        # The headline and the New York slice's shared numbers.
        ("dashboard change", OUT["headline changes"]["dashboard"], W["dashboard_q2_to_q3"]),
        ("booked change", OUT["headline changes"]["booked"], W["booked_q2_to_q3"]),
        ("performed change", OUT["headline changes"]["performed"], W["performed_q2_to_q3"]),
        ("bookings change", OUT["headline changes"]["bookings"], W["bookings_q2_to_q3"]),
        # Sub-problem 1.
        ("text amounts", OUT["sp1 claims rows, distinct, text amounts, coerced total, true total, hidden"][2], W["text_amounts"]),
        ("billed all", OUT["sp1 claims rows, distinct, text amounts, coerced total, true total, hidden"][4], W["billed_all"]),
        ("Q3 billed", OUT["sp1 Q3 billed, without contract, contract share"][0], W["q3_billed"]),
        ("Q3 billed without the contract", OUT["sp1 Q3 billed, without contract, contract share"][1], W["q3_billed_without_contract"]),
        ("contract share", OUT["sp1 Q3 billed, without contract, contract share"][2], W["contract_share_of_q3"]),
        ("Q2 billed", OUT["sp1 billed per quarter"]["Q2"], W["q2_billed"]),
        ("Q3 mean", OUT["sp1 Q2 mean, Q3 mean, Q3 mean without contract, medians"][1], W["q3_mean_claim"]),
        ("Q3 mean without the contract", OUT["sp1 Q2 mean, Q3 mean, Q3 mean without contract, medians"][2], W["q3_mean_without_contract"]),
        ("claim lines", OUT["sp1 claim lines, tests on completed bookings, tests on all bookings"][0], W["claim_lines_non_employer"]),
        ("tests on claimed bookings", OUT["sp1 claim lines, tests on completed bookings, tests on all bookings"][1], W["tests_on_claimed_bookings_non_employer"]),
        ("tests booked", OUT["sp1 claim lines, tests on completed bookings, tests on all bookings"][2], W["tests_booked_non_employer"]),
        # Sub-problem 2.
        ("legacy rows", OUT["sp2 old export rows, distinct ids; new system rows by metro"][0], W["legacy_rows"]),
        ("legacy distinct ids", OUT["sp2 old export rows, distinct ids; new system rows by metro"][1], W["legacy_distinct_ids"]),
        ("two metros Q2", OUT["sp2 two metros Q2, Q3 old only, Q3 both"][0], W["switch_metros_q2"]),
        ("two metros Q3 old only", OUT["sp2 two metros Q2, Q3 old only, Q3 both"][1], W["switch_metros_q3_legacy_only"]),
        ("two metros Q3 both", OUT["sp2 two metros Q2, Q3 old only, Q3 both"][2], W["switch_metros_q3_real"]),
        # Sub-problem 3.
        ("remittance rows", OUT["sp3 posting rows, forms, kinds"][0], W["remittance_rows"]),
        ("exact matches", OUT["sp3 exact matches, share, unmatched after the rule"][0], W["exact_join_matches"]),
        ("unmatched after the rule", OUT["sp3 exact matches, share, unmatched after the rule"][2], W["normalised_join_unmatched"]),
        ("double posts", OUT["sp3 double posts, dollars; reversals, dollars"][0], W["double_posts"]),
        ("double-posted dollars", OUT["sp3 double posts, dollars; reversals, dollars"][1], W["double_posted_dollars"]),
        ("reversals", OUT["sp3 double posts, dollars; reversals, dollars"][2], W["reversals"]),
        ("claims with no posting", OUT["sp3 claims with no posting, dollars, employer claim among them"][0], W["claims_without_posting"]),
        ("denial postings", OUT["sp3 denial postings, paying nothing; denied claims with no posting"][0], W["denial_postings"]),
        ("denied billed", OUT["sp3 retail claims, marked denied, rate, billed"][3], W["denied_billed"]),
        ("raw paid sum", OUT["sp3 raw paid column sum, paid net of double posts"][0], W["paid_raw_sum"]),
        ("paid net of double posts", OUT["sp3 raw paid column sum, paid net of double posts"][1], W["paid_net_of_double_posts"]),
        # Sub-problem 4, on the register drawn from the bookings.
        ("register rows", OUT["sp4 rows, centres, kinds, dates"][0], W["register_rows"]),
        ("small centre no-shows", OUT["sp4 small all, others all, small scheduled, others scheduled"][2][0], W["small_site_no_shows"]),
        ("small centre scheduled", OUT["sp4 small all, others all, small scheduled, others scheduled"][2][1], W["small_site_scheduled"]),
        ("small centre walk-ins", OUT["sp4 small walk-ins; walk-ins marked not attended"][0], W["small_site_walk_ins"]),
        ("chance tail on scheduled", OUT["sp4 chance tail on scheduled, on all visits"][0], W["small_site_tail_probability"]),
        # Sub-problem 5.
        ("offered", OUT["sp5 offered, took up, by metro, dates"][0], W["offered_patients"]),
        ("lift overall", OUT["sp5 lift overall and by metro"][0], W["campaign_lift_aggregate"]),
    ]
    by_metro = eval(W["campaign_lift_by_metro"]) | eval(W["campaign_lift_other_metros"])  # the witness prints dicts
    for metro, value in by_metro.items():
        checks.append((f"lift {metro}", OUT["sp5 lift overall and by metro"][1][metro], value))
    for metro, value in eval(W["campaign_gap_before_offer_by_metro"]).items():
        checks.append((f"gap before the offer {metro}", OUT["sp5 gap before the offer"][metro], value))
    rates4 = OUT["sp4 small all, others all, small scheduled, others scheduled"]
    checks += [("small rate all visits", rates4[0][0] / rates4[0][1], W["small_site_rate_all_visits"]),
               ("others rate all visits", rates4[1][0] / rates4[1][1], W["others_rate_all_visits"]),
               ("small rate scheduled", rates4[2][0] / rates4[2][1], W["small_site_rate_scheduled"]),
               ("others rate scheduled", rates4[3][0] / rates4[3][1], W["others_rate_scheduled"])]
    failed = [(name, mine, theirs) for name, mine, theirs in checks if not close(mine, theirs, 0.006 if "dollars" in name or "billed" in name or "sum" in name else 0.0005)]
    # Figures only the spine or Monday's day sheet gives.
    spine = [
        ("New York rows, distinct ids, repeated ids", OUT["ny rows, distinct ids, repeated ids"], (2128, 2095, 33)),
        ("New York text amounts", len(OUT["ny text amounts"]), 6),
        ("Chicago Q2, Q3 old, Q3 both", OUT["sp2 Chicago Q2, Q3 old only, Q3 both"], (754, 571, 656)),
        ("Philadelphia Q2, Q3 old, Q3 both", OUT["sp2 Philadelphia Q2, Q3 old only, Q3 both"], (661, 519, 587)),
        ("next worst rates", OUT["sp4 next worst rate, all visits and scheduled"], (0.0984, 0.1848)),
        ("all-visits tail", OUT["sp4 chance tail on scheduled, on all visits"][1], 0.0014),
        ("per booking", OUT["sp4 per booking: small scheduled bookings, missing a slot; others' share; tail"], (64, 15, 0.173, 0.1303)),
        ("register two-row bookings", OUT["sp4 register: distinct bookings, bookings with two rows"][1], 253),
        ("New York permutation p", OUT["sp5 New York permutation p, two-sided"], 0.0302),
        ("SQL route", OUT["ny second route in SQL"], [("Q2", 977, 174910.0), ("Q3", 1055, 184485.0)]),
    ]
    for name, mine, theirs in spine:
        if not same(mine, theirs):
            failed.append((name, mine, theirs))
    for name, mine, theirs in failed:
        print(f"DRIFT  {name}: this script {mine}, the source {theirs}")
    if failed:
        sys.exit(f"FAIL  {len(failed)} number(s) drifted from the witness, the spine or Monday's sheet")
    print(f"PASS  {len(OUT)} groups of numbers recomputed; {len(checks)} agree with the generator's "
          f"witness and {len(spine)} with the spine or Monday's day sheet")

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W03/D3/internal/C2_W03_D03_numbers_INTERNAL.py
#     Prints one line per group of numbers, then PASS with the count of witness and spine checks.
# The data pack regenerated from a changed seed
#     One DRIFT line per number that moved, then FAIL; the pack's files need the new numbers.
# The visit register drawn the old way (before 1 October 2026)
#     DRIFT on the small centre's scheduled visits and rates, then FAIL.

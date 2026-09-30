"""Recompute every number the Week 3 Wednesday pack quotes, from the Kalpa Health files.

    python3 content/W03/D3/internal/C2_W03_D03_numbers_INTERNAL.py

The files are read where Monday's pack keeps them, content/W03/D1/data/, the way a group would read
them: every value as text, the old booking export de-duplicated on booking_id keeping the later
updated_at, and billed amounts converted after removing the dollar sign and any thousands comma.
The run sheet, the checkpoint guide, the catch-up plan, the headline sheet and the day sheet quote
these outputs, and the ones the spine also gives are asserted against its witness
(python3 data/generate_kalpa_health.py --witness). The files are the US pack of decision
build1-us-data, and the quarters are calendar Q2 (April to June) and Q3 (July to September) of 2026.
"""
import pathlib

import numpy as np
import pandas as pd

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "scripts").is_dir() and (p / "content").is_dir())
DATA = ROOT / "content/W03/D1/data"


def read(name):
    return pd.read_csv(DATA / f"C2_W03_D01_{name}_STUDENT.csv", dtype=str, keep_default_na=False)


def quarter(dates):
    return np.where(dates < "2026-07-01", "Q2", "Q3")


def usd(text):
    return text.str.replace("$", "", regex=False).str.replace(",", "", regex=False).astype(float)


raw_legacy, newsys, claims, postings = read("bookings_legacy"), read("bookings_newsys"), read("claims"), read("remittances")
appointments, campaign, patients = read("appointments"), read("campaign"), read("patients")
legacy = raw_legacy.sort_values("updated_at").drop_duplicates("booking_id", keep="last").copy()
legacy["q"] = quarter(legacy["booking_date"])
claims["amt"] = usd(claims["billed_amount"])
claims["q"] = quarter(claims["service_date"])
out = {}

# ---------------------------------------------------------------- the New York slice
d_raw = raw_legacy[raw_legacy["metro"] == "New York"].copy()
d_raw["q"] = quarter(d_raw["booking_date"])
d = legacy[legacy["metro"] == "New York"]
dc = claims[claims["metro"] == "New York"]
coerced = pd.to_numeric(dc["billed_amount"], errors="coerce")
out["new york rows, distinct ids"] = (len(d_raw), d_raw["booking_id"].nunique())
out["new york rows per quarter"] = d_raw.groupby("q").size().to_dict()
out["new york bookings per quarter"] = d.groupby("q").size().to_dict()
out["new york text amounts, dollars hidden by coerce"] = (int(coerced.isna().sum()),
                                                         dc[coerced.isna()].groupby("q")["amt"].sum().to_dict())
fanned = d_raw.merge(dc, on="booking_id")
out["new york fanned join rows, dollars"] = (len(fanned), int(fanned["amt"].sum()), int(dc["amt"].sum()))
out["new york kept, cancelled, completed, claims"] = (len(d), int((d["status"] == "cancelled").sum()),
                                                     int((d["status"] == "completed").sum()), len(dc))
tree = dc.groupby("q")["amt"].agg(["count", "sum", "mean", "median"])
out["new york tree"] = tree.round(2).to_dict("index")
volume = (tree.loc["Q3", "count"] - tree.loc["Q2", "count"]) * tree.loc["Q2", "mean"]
value = tree.loc["Q3", "count"] * (tree.loc["Q3", "mean"] - tree.loc["Q2", "mean"])
out["new york bridge volume, value"] = (round(volume), round(value))
out["new york per day change, claims and billed"] = (
    round(float((tree.loc["Q3", "count"] / 92) / (tree.loc["Q2", "count"] / 91) - 1), 4),
    round(float((tree.loc["Q3", "sum"] / 92) / (tree.loc["Q2", "sum"] / 91) - 1), 4))
m = d.merge(dc, on="booking_id", suffixes=("", "_c"))
out["new york claims by site"] = m.groupby(["site_code", "q"]).size().unstack().to_dict("index")
home = m[m["channel"] == "at-home"].groupby("q")["amt"].agg(["count", "mean"]).round(0)
rest = m[m["channel"] != "at-home"].groupby("q")["amt"].mean().round(0)
out["new york at-home count and mean, the rest's mean"] = (home.to_dict("index"), rest.to_dict())

# ---------------------------------------------------------------- sub-problem 1
co_all = pd.to_numeric(claims["billed_amount"], errors="coerce")
q3 = claims[claims["q"] == "Q3"]
out["sp1 claims, distinct, text amounts, coerced total, true total"] = (
    len(claims), claims["claim_id"].nunique(), int(co_all.isna().sum()), int(co_all.sum()), int(claims["amt"].sum()))
out["sp1 claims per quarter"] = claims.groupby("q").size().to_dict()
out["sp1 old-export completed, new-system done"] = (int((legacy["status"] == "completed").sum()), int((newsys["state"] == "DONE").sum()))
out["sp1 Q3 mean, median, mean without the contract"] = (round(float(q3["amt"].mean()), 2), float(q3["amt"].median()),
                                                        round(float(q3[q3["employer_account"] == ""]["amt"].mean()), 2))
tests = read("booking_tests")
tests = tests[tests["line"].isin(["test", "component"]) & (tests["panel_code"] != "PNL-EMP")]
done = set(legacy.loc[legacy["status"] == "completed", "booking_id"]) | set(newsys.loc[newsys["state"] == "DONE", "bkg_ref"])
out["sp1 claim lines, tests on completed bookings, tests on all"] = (
    int(claims.loc[claims["employer_account"] == "", "line_items"].astype(int).sum()),
    int(tests["booking_id"].isin(done).sum()), len(tests))

# ---------------------------------------------------------------- sub-problem 2
sw = legacy[legacy["metro"].isin(["Chicago", "Philadelphia"])]
sw_raw = raw_legacy[raw_legacy["metro"].isin(["Chicago", "Philadelphia"])]
out["sp2 old export rows, distinct; new rows by metro"] = (len(raw_legacy), raw_legacy["booking_id"].nunique(),
                                                          newsys["metro"].value_counts().to_dict())
out["sp2 two metros Q2, Q3 old only, Q3 both"] = (int((sw["q"] == "Q2").sum()), int((sw["q"] == "Q3").sum()),
                                                  int((sw["q"] == "Q3").sum()) + len(newsys))
out["sp2 two metros rows before the identity rule"] = pd.Series(quarter(sw_raw["booking_date"])).value_counts().to_dict()
claims_q3 = claims[claims["q"] == "Q3"].groupby("metro").size()
comp_q3 = legacy[(legacy["q"] == "Q3") & (legacy["status"] == "completed")].groupby("metro").size()
out["sp2 Q3 claims less old-export completed, by metro"] = (claims_q3 - comp_q3).to_dict()

# ---------------------------------------------------------------- sub-problem 3
ref = postings["claim_ref"]
form = np.where(ref.str.startswith("KH-CLM-"), "full", np.where(ref.str.startswith("CLM-"), "CLM-n", "digits"))
out["sp3 posting rows, forms, kinds"] = (len(postings), pd.Series(form).value_counts().to_dict(),
                                         postings["posting"].value_counts().to_dict())
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
paid = postings[postings["posting"] == "payment"]
double = paid[paid.duplicated(["claim_ref", "paid_amount"])]
reversed_ = postings[postings["posting"] == "reversal"]
unposted = claims[~claims["claim_id"].isin(postings["claim"])]
collected = paid["paid"].sum() - double["paid"].sum() + reversed_["paid"].sum()
out["sp3 exact matches, unmatched after the rule"] = (int(ref.isin(claim_ids).sum()), int(postings["claim"].isna().sum()))
out["sp3 double posts and dollars, reversal dollars"] = (len(double), round(float(double["paid"].sum()), 2),
                                                         round(float(reversed_["paid"].sum()), 2))
out["sp3 denial postings, claims with no posting and dollars, collected, billed, raw paid column sum"] = (
    int((postings["posting"] == "denial").sum()), len(unposted), int(unposted["amt"].sum()),
    round(float(collected), 2), int(claims["amt"].sum()), round(float(postings["paid"].sum()), 2))

# ---------------------------------------------------------------- sub-problem 4
small = appointments["site_code"] == "KH-ATL-03"
sched = appointments["kind"] == "scheduled"
noshow = appointments["attended"] == "N"
out["sp4 rows, kinds"] = (len(appointments), appointments["kind"].value_counts().to_dict())
out["sp4 small all, others all, small scheduled, others scheduled"] = (
    (int((small & noshow).sum()), int(small.sum())), (int((~small & noshow).sum()), int((~small).sum())),
    (int((small & sched & noshow).sum()), int((small & sched).sum())),
    (int((~small & sched & noshow).sum()), int((~small & sched).sum())))

# ---------------------------------------------------------------- sub-problem 5
window = legacy[(legacy["booking_date"] >= "2026-07-15") & (legacy["booking_date"] <= "2026-09-14")
                & (legacy["channel"] != "employer")]
per = window.groupby("patient_id").size()
patients["n"] = patients["patient_id"].map(per).fillna(0)
patients["offered"] = patients["patient_id"].isin(campaign["patient_id"])
lift = lambda df: round(float(df[df["offered"]]["n"].mean() / df[~df["offered"]]["n"].mean() - 1), 4)
out["sp5 offered, took up, by metro, date range"] = (len(campaign), int((campaign["took_up"] == "Y").sum()),
                                                     campaign["metro"].value_counts().to_dict(),
                                                     (campaign["offered_on"].min(), campaign["offered_on"].max()))
out["sp5 offered with a booking in the old export"] = int(campaign["patient_id"].isin(legacy["patient_id"]).sum())
out["sp5 lift overall and by metro"] = (lift(patients), {c: lift(patients[patients["metro"] == c])
                                                         for c in sorted(patients["metro"].unique())})

if __name__ == "__main__":
    for k, v in out.items():
        print(f"{k}: {v}")
    # The spine's witness, where the pack quotes it.
    assert out["sp2 two metros Q2, Q3 old only, Q3 both"] == (1415, 1090, 1243)
    assert out["sp3 exact matches, unmatched after the rule"] == (216, 0)
    assert out["sp3 double posts and dollars, reversal dollars"][0] == 280
    assert out["sp3 denial postings, claims with no posting and dollars, collected, billed, raw paid column sum"][:2] == (1137, 398)
    assert out["sp1 claim lines, tests on completed bookings, tests on all"][0] == 22152
    assert out["sp1 claim lines, tests on completed bookings, tests on all"][1:] == (46867, 48235)
    assert out["sp1 claims, distinct, text amounts, coerced total, true total"][2] == 60
    assert out["sp4 small all, others all, small scheduled, others scheduled"][2] == (10, 50)
    assert abs(out["sp5 lift overall and by metro"][0] - 0.0900) < 0.0005
    print("PASS  every quoted number recomputed, and the spine's witness holds where the pack quotes it")

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W03/D3/internal/C2_W03_D03_numbers_INTERNAL.py
#     Prints one line per number group and ends on PASS.
# The data pack regenerated from a changed seed
#     An assertion fails on the first witness number that moved, and the pack's files need updating.

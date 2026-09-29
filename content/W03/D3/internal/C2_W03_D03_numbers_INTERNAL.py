"""Recompute every number the Week 3 Wednesday pack quotes, from the Kalpa Health files.

    python3 content/W03/D3/internal/C2_W03_D03_numbers_INTERNAL.py

The files are read where Monday's pack keeps them, content/W03/D1/data/, the way a group would read
them: every value as text, the old booking export de-duplicated on booking_id keeping the later
updated_at, and amounts converted after removing the thousands comma. The run sheet, the checkpoint
guide, the catch-up plan, the headline sheet and the day sheet quote these outputs, and the ones the
spine also gives are asserted against its witness (python3 data/generate_kalpa_health.py --witness).
"""
import pathlib

import numpy as np
import pandas as pd

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "scripts").is_dir() and (p / "content").is_dir())
DATA = ROOT / "content/W03/D1/data"


def read(name):
    return pd.read_csv(DATA / f"C2_W03_D01_{name}_STUDENT.csv", dtype=str, keep_default_na=False)


def quarter(dates):
    return np.where(dates < "2026-07-01", "Q1", "Q2")


raw_legacy, newsys, invoices, payments = read("bookings_legacy"), read("bookings_newsys"), read("invoices"), read("payments")
appointments, campaign, patients = read("appointments"), read("campaign"), read("patients")
legacy = raw_legacy.sort_values("updated_at").drop_duplicates("booking_id", keep="last").copy()
legacy["q"] = quarter(legacy["booking_date"])
invoices["amt"] = invoices["amount"].str.replace(",", "", regex=False).astype(int)
invoices["q"] = quarter(invoices["invoice_date"])
out = {}

# ---------------------------------------------------------------- the Delhi slice
d_raw = raw_legacy[raw_legacy["city"] == "Delhi"].copy()
d_raw["q"] = quarter(d_raw["booking_date"])
d = legacy[legacy["city"] == "Delhi"]
di = invoices[invoices["city"] == "Delhi"]
coerced = pd.to_numeric(di["amount"], errors="coerce")
out["delhi rows, distinct ids"] = (len(d_raw), d_raw["booking_id"].nunique())
out["delhi rows per quarter"] = d_raw.groupby("q").size().to_dict()
out["delhi bookings per quarter"] = d.groupby("q").size().to_dict()
out["delhi comma amounts, rupees hidden by coerce"] = (int(coerced.isna().sum()),
                                                      di[coerced.isna()].groupby("q")["amt"].sum().to_dict())
fanned = d_raw.merge(di, on="booking_id")
out["delhi fanned join rows, rupees"] = (len(fanned), int(fanned["amt"].sum()), int(di["amt"].sum()))
out["delhi kept, cancelled, completed, invoices"] = (len(d), int((d["status"] == "cancelled").sum()),
                                                    int((d["status"] == "completed").sum()), len(di))
tree = di.groupby("q")["amt"].agg(["count", "sum", "mean", "median"])
out["delhi tree"] = tree.round(2).to_dict("index")
volume = (tree.loc["Q2", "count"] - tree.loc["Q1", "count"]) * tree.loc["Q1", "mean"]
value = tree.loc["Q2", "count"] * (tree.loc["Q2", "mean"] - tree.loc["Q1", "mean"])
out["delhi bridge volume, value"] = (round(volume), round(value))
out["delhi per day change, invoices and revenue"] = (
    round((tree.loc["Q2", "count"] / 92) / (tree.loc["Q1", "count"] / 91) - 1, 4),
    round((tree.loc["Q2", "sum"] / 92) / (tree.loc["Q1", "sum"] / 91) - 1, 4))
m = d.merge(di, on="booking_id", suffixes=("", "_i"))
out["delhi invoices by clinic"] = m.groupby(["clinic_code", "q"]).size().unstack().to_dict("index")
home = m[m["channel"] == "home-collection"].groupby("q")["amt"].agg(["count", "mean"]).round(0)
rest = m[m["channel"] != "home-collection"].groupby("q")["amt"].mean().round(0)
out["delhi home-collection count and mean, the rest's mean"] = (home.to_dict("index"), rest.to_dict())

# ---------------------------------------------------------------- sub-problem 1
co_all = pd.to_numeric(invoices["amount"], errors="coerce")
q2 = invoices[invoices["q"] == "Q2"]
out["sp1 invoices, distinct, comma amounts, coerced total"] = (len(invoices), invoices["invoice_no"].nunique(),
                                                              int(co_all.isna().sum()), int(co_all.sum()), int(invoices["amt"].sum()))
out["sp1 invoices per quarter"] = invoices.groupby("q").size().to_dict()
out["sp1 old-export completed, new-system done"] = (int((legacy["status"] == "completed").sum()), int((newsys["state"] == "DONE").sum()))
out["sp1 Q2 mean, median, mean without the contract"] = (round(q2["amt"].mean()), q2["amt"].median(),
                                                        round(q2[q2["corporate_account"] == ""]["amt"].mean()))
tests = read("booking_tests")
tests = tests[tests["line"].isin(["test", "component"]) & (tests["package_code"] != "PKG-CORP")]
done = set(legacy.loc[legacy["status"] == "completed", "booking_id"]) | set(newsys.loc[newsys["state"] == "DONE", "bkg_ref"])
out["sp1 invoice lines, tests on completed bookings, tests on all"] = (
    int(invoices.loc[invoices["corporate_account"] == "", "line_items"].astype(int).sum()),
    int(tests["booking_id"].isin(done).sum()), len(tests))

# ---------------------------------------------------------------- sub-problem 2
sw = legacy[legacy["city"].isin(["Chennai", "Pune"])]
sw_raw = raw_legacy[raw_legacy["city"].isin(["Chennai", "Pune"])]
out["sp2 old export rows, distinct; new rows by city"] = (len(raw_legacy), raw_legacy["booking_id"].nunique(),
                                                         newsys["city"].value_counts().to_dict())
out["sp2 two cities Q1, Q2 old only, Q2 both"] = (int((sw["q"] == "Q1").sum()), int((sw["q"] == "Q2").sum()),
                                                  int((sw["q"] == "Q2").sum()) + len(newsys))
out["sp2 two cities rows before the identity rule"] = pd.Series(quarter(sw_raw["booking_date"])).value_counts().to_dict()
inv_q2 = invoices[invoices["q"] == "Q2"].groupby("city").size()
comp_q2 = legacy[(legacy["q"] == "Q2") & (legacy["status"] == "completed")].groupby("city").size()
out["sp2 Q2 invoices less old-export completed, by city"] = (inv_q2 - comp_q2).to_dict()

# ---------------------------------------------------------------- sub-problem 3
ref = payments["invoice_ref"]
form = np.where(ref.str.startswith("KH/"), "full", np.where(ref.str.startswith("INV-"), "INV-n", "digits"))
out["sp3 payment rows, forms, statuses"] = (len(payments), pd.Series(form).value_counts().to_dict(),
                                            payments["status"].value_counts().to_dict())
inv_nos = set(invoices["invoice_no"])
by_digits = {x.split("/")[-1]: x for x in inv_nos}


def normalise(r):
    if r in inv_nos:
        return r
    if r.startswith("INV-"):
        return by_digits.get(f"{int(r[4:]):06d}")
    return by_digits.get(r)


payments["inv"] = ref.map(normalise)
payments["a"] = payments["amount"].astype(int)
ok = payments[payments["status"] == "success"]
double = ok[ok.duplicated(["invoice_ref", "amount"])]
unpaid = invoices[~invoices["invoice_no"].isin(payments["inv"])]
collected = ok["a"].sum() - double["a"].sum() + payments.loc[payments["status"] == "refund", "a"].sum()
out["sp3 exact matches, unmatched after the rule"] = (int(ref.isin(inv_nos).sum()), int(payments["inv"].isna().sum()))
out["sp3 double posts and rupees, refund rupees"] = (len(double), int(double["a"].sum()),
                                                     int(payments.loc[payments["status"] == "refund", "a"].sum()))
out["sp3 unpaid invoices and rupees, collected, invoiced, raw column sum"] = (
    len(unpaid), int(unpaid["amt"].sum()), int(collected), int(invoices["amt"].sum()), int(payments["a"].sum()))

# ---------------------------------------------------------------- sub-problem 4
small = appointments["clinic_code"] == "KH-HYD-03"
sched = appointments["kind"] == "scheduled"
noshow = appointments["attended"] == "N"
out["sp4 rows, kinds"] = (len(appointments), appointments["kind"].value_counts().to_dict())
out["sp4 small all, others all, small scheduled, others scheduled"] = (
    (int((small & noshow).sum()), int(small.sum())), (int((~small & noshow).sum()), int((~small).sum())),
    (int((small & sched & noshow).sum()), int((small & sched).sum())),
    (int((~small & sched & noshow).sum()), int((~small & sched).sum())))

# ---------------------------------------------------------------- sub-problem 5
window = legacy[(legacy["booking_date"] >= "2026-07-15") & (legacy["booking_date"] <= "2026-09-14")
                & (legacy["channel"] != "corporate")]
per = window.groupby("patient_id").size()
patients["n"] = patients["patient_id"].map(per).fillna(0)
patients["offered"] = patients["patient_id"].isin(campaign["patient_id"])
lift = lambda df: round(df[df["offered"]]["n"].mean() / df[~df["offered"]]["n"].mean() - 1, 4)
out["sp5 offered, took up, by city, date range"] = (len(campaign), int((campaign["took_up"] == "Y").sum()),
                                                    campaign["city"].value_counts().to_dict(),
                                                    (campaign["offered_on"].min(), campaign["offered_on"].max()))
out["sp5 offered with a booking in the old export"] = int(campaign["patient_id"].isin(legacy["patient_id"]).sum())
out["sp5 lift overall and by city"] = (lift(patients), {c: lift(patients[patients["city"] == c])
                                                        for c in sorted(patients["city"].unique())})

if __name__ == "__main__":
    for k, v in out.items():
        print(f"{k}: {v}")
    # The spine's witness, where the pack quotes it.
    assert out["sp2 two cities Q1, Q2 old only, Q2 both"] == (1415, 1090, 1243)
    assert out["sp3 exact matches, unmatched after the rule"] == (247, 0)
    assert out["sp3 double posts and rupees, refund rupees"][0] == 229
    assert out["sp3 unpaid invoices and rupees, collected, invoiced, raw column sum"][0] == 398
    assert out["sp1 invoice lines, tests on completed bookings, tests on all"][0] == 22152
    assert out["sp1 invoice lines, tests on completed bookings, tests on all"][2] == 48235
    assert out["sp4 small all, others all, small scheduled, others scheduled"][2] == (10, 50)
    assert abs(out["sp5 lift overall and by city"][0] - 0.0900) < 0.0005
    print("PASS  every quoted number recomputed, and the spine's witness holds where the pack quotes it")

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W03/D3/internal/C2_W03_D03_numbers_INTERNAL.py
#     Prints one line per number group and ends on PASS.
# The data pack regenerated from a changed seed
#     An assertion fails on the first witness number that moved, and the pack's files need updating.

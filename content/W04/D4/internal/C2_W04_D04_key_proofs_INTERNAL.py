"""Recompute every numeric key in Thursday's exercises and quiz from the data or from the item's own counts.

Run from the repository root, after the generator:
    python3 content/W04/D4/internal/C2_W04_D04_key_proofs_INTERNAL.py

Each line prints PASS or FAIL with the item it proves. The Parsons item in the practice set is run
in all four of its orders on a small table, so the key is the one order that runs and keeps month zero
out, and option b is shown to run while keeping it in.
"""
import pathlib

import pandas as pd

DAY = pathlib.Path(__file__).resolve().parent.parent
DATA = DAY / "data"
fails = 0


def check(name, ok):
    global fails
    fails += not ok
    print(("PASS  " if ok else "FAIL  ") + name)


# ------------------------------------------------------------------------------ the guided set
card = pd.read_csv(DATA / "C2_W04_D04_twelve_rows_STUDENT.csv")
may = card[card.signup_month == "May"]
may_row = [int(may[f"ordered_in_{m}"].sum()) for m in ("jun", "jul", "aug", "sep")]
check("guided Q1: May keeps 3, 2, 1 and 1 of 4 (75, 50, 25, 25)", may_row == [3, 2, 1, 1] and len(may) == 4)
jun = card[card.signup_month == "Jun"]
jun_row = [int(jun[f"ordered_in_{m}"].sum()) for m in ("jul", "aug", "sep")]
check("guided Q2: June keeps 2, 1 and 1 of 3 (67, 33, 33)", jun_row == [2, 1, 1] and len(jun) == 3)
check("guided Q3: the toy's first two steps read 40 and 50 percent", (40 / 100, 20 / 40) == (0.4, 0.5))
check("guided Q4: the same 10 checkouts read 10 of 100 sessions and 10 of 20 people", (10 / 100, 10 / 20) == (0.1, 0.5))

# ------------------------------------------------------------------------- the chapter 2 drill
members = pd.read_csv(DATA / "C2_W04_D04_members_STUDENT.csv")
mm = pd.read_csv(DATA / "C2_W04_D04_member_months_STUDENT.csv").merge(
    members[["member_id", "cohort_month"]], on="member_id")
to_n = lambda s: s.str[:4].astype(int) * 12 + s.str[5:].astype(int)
mm["age"] = to_n(mm["month"]) - to_n(mm["cohort_month"])
mm["active"] = mm["orders"] > 0
tri = mm[mm["age"] >= 1].pivot_table(index="cohort_month", columns="age", values="active", aggfunc="mean")
jan = tri.loc["2026-01"].dropna()
check("ch2 Q1: January drops about 19 points after month one, then about 0.3 a month",
      round(100 * (jan[1] - jan[2])) == 19 and round(100 * (jan[2] - jan[8]) / 6, 1) == 0.3)
check("ch2 Q2: month one reads 58, 53 and 49 for January, April and July",
      [round(100 * tri.loc[c, 1]) for c in ("2026-01", "2026-04", "2026-07")] == [58, 53, 49])
sep = mm[mm.month == "2026-09"]
rates = sep[sep.age >= 1].groupby("cohort_month")["active"].mean()
weighted = sep[sep.age >= 1]["active"].mean()
check("ch2 Q3: the plain mean of the eight rates is 36.9 and the weighted reading 35.9",
      round(100 * rates.mean(), 1) == 36.9 and round(100 * weighted, 1) == 35.9)
dash = sep[sep.age >= 2]
by = dash.groupby("cohort_month")["active"].agg(["size", "mean"])
check("ch2 Q4: size times rate over the seven cohorts gives 13,218 of 35,000",
      round((by["size"] * by["mean"]).sum()) == 13218 and by["size"].sum() == 35000)

# ------------------------------------------------------------------------ the chapter 3 drill
S = {"search": 5000, "view": 6000, "cart": 2000, "order": 1200}
C = {"search": 2100, "view": 2400, "cart": 1400, "order": 1000}
check("ch3 Q1: search to product view reads 120 percent per session", S["view"] / S["search"] == 1.2)
check("ch3 Q3: 58 per customer against 33 per session",
      (round(100 * C["cart"] / C["view"]), round(100 * S["cart"] / S["view"])) == (58, 33))

# --------------------------------------------------------------------------- the fix-first set
ev = pd.read_csv(DATA / "C2_W04_D04_events_STUDENT.csv.gz", parse_dates=["event_ts"])
am = ev[ev.is_member & (ev.platform == "android") & ev.stage.isin(["add_to_cart", "order_placed"])]
after = am[am.event_ts >= "2026-09-14"]
before = am[am.event_ts < "2026-09-14"]
rate = lambda d: d[d.stage == "order_placed"].session_id.nunique() / d[d.stage == "add_to_cart"].session_id.nunique()
carts = after[after.stage == "add_to_cart"].session_id.nunique()
lost = (round(rate(before), 2) - round(rate(after), 2)) * carts
check("fix-first Q1: 22,841 carts, about 1,317 orders a week (188 a day, 3,198 in 17 days)",
      carts == 22841 and round(lost / 17 * 7) == 1317 and round(lost / 17) == 188 and round(lost) == 3198)
check("fix-first Q2: Rs 5.3 lakh at 1,317 and Rs 400; Rs 3.7 lakh at 1,223 and Rs 300, Rs 6.6 lakh at 1,317 and Rs 500",
      [round(1317 * 400 / 1e5, 1), round(1223 * 300 / 1e5, 1), round(1317 * 500 / 1e5, 1)] == [5.3, 3.7, 6.6])
check("fix-first: 1,223 is the 13-point fall net of the comparators' one point, a week",
      round((0.58 - 0.44 - 0.01) * 22841 / 17 * 7) == 1223)

# ------------------------------------------------------------------------------ the Kalpa set
kev = pd.read_csv(DATA / "C2_W04_D04_kalpa_events_STUDENT.csv", parse_dates=["event_ts"])
s = kev.pivot_table(index="session_id", columns="event_type", values="customer_id", aggfunc="size",
                    fill_value=0).gt(0)
s["day"] = kev.groupby("session_id")["event_ts"].min().dt.strftime("%Y-%m-%d")
s["stretch"] = s["day"].map(lambda d: "window" if d >= "2026-09-10" else "comparison" if d >= "2026-08-20" else "before")
k = s.groupby("stretch")[["add_to_cart", "checkout"]].sum()
check("Kalpa: 28 of 34, 10 of 12 and 7 of 11 carts checked out",
      [tuple(k.loc[b]) for b in ("before", "comparison", "window")] == [(34, 28), (12, 10), (11, 7)])
missing = k.loc["window", "add_to_cart"] * 10 / 12 - k.loc["window", "checkout"]
check("Kalpa Q3: about 2 checkouts missing from the window", round(missing) == 2)
mem_k = pd.read_csv(DATA / "C2_W04_D04_kalpa_memberships_STUDENT.csv")
kev["month"] = kev["event_ts"].dt.strftime("%Y-%m")
active_sep = set(kev.loc[kev["month"] == "2026-09", "customer_id"])
joined_before = mem_k[mem_k["member_since"] < "2026-09-01"]
aug = joined_before[joined_before["member_since"] >= "2026-08-01"]
rest = joined_before[joined_before["member_since"] < "2026-08-01"]
aug_act, rest_act = aug["customer_id"].isin(active_sep).sum(), rest["customer_id"].isin(active_sep).sum()
check("Kalpa Q4: the monsoon cohort, 26 of 32 in September, holds the blend up; without it, 23 of 88",
      (aug_act, len(aug), rest_act, len(rest)) == (26, 32, 23, 88) and aug_act / len(aug) > (aug_act + rest_act) / len(joined_before))

# ---------------------------------------------------------------------------- the practice set
check("practice Q1: January keeps 6, 4 and 3 of 8 (75, 50 and 37.5)",
      [round(100 * x / 8, 1) for x in (6, 4, 3)] == [75.0, 50.0, 37.5])
check("practice Q6: 510 of 1,000 and 1,020 of 2,000 are both 51 percent",
      400 * 0.60 + 600 * 0.45 == 510 and 400 * 0.55 + 600 * 0.40 + 1000 * 0.56 == 1020)
subs0 = pd.DataFrame({"cohort": ["2026-01"] * 3, "month": ["2026-01", "2026-02", "2026-03"], "tiffins": [3, 2, 0]})
lines = {
    1: 'tri = subs.pivot_table(index="cohort", columns="age", values="active", aggfunc="mean")',
    2: 'subs = subs[subs["age"] >= 1]',
    3: 'subs["age"] = to_n(subs["month"]) - to_n(subs["cohort"])',
    4: 'subs["active"] = subs["tiffins"] > 0',
}
outcome = {}
for key, order in {"a": (3, 4, 2, 1), "b": (3, 4, 1, 2), "c": (2, 3, 4, 1), "d": (4, 1, 3, 2)}.items():
    env = {"subs": subs0.copy(), "to_n": to_n, "pd": pd}
    try:
        for n in order:
            exec(lines[n], env)
        outcome[key] = 0 in env["tri"].columns
    except Exception:
        outcome[key] = "error"
check("practice Q4: only order a runs and keeps month zero out; b runs with month zero in",
      outcome == {"a": False, "b": True, "c": "error", "d": "error"})

# --------------------------------------------------------------------------------- the quiz
check("Kahoot Q3: two cohorts fall five points and the blend reads 46 both months",
      (300 * 0.60 + 700 * 0.40) / 1000 == 0.46 and (300 * 0.55 + 700 * 0.35 + 1000 * 0.51) / 2000 == 0.46)
check("notes self-check: 236 of 500 is 47.2 percent", (200 * 0.40 + 300 * 0.52) / 500 == 0.472)

print(f"{'FAIL' if fails else 'PASS'}: {fails} failing")
raise SystemExit(1 if fails else 0)

# Test inputs and expected outcomes
# python3 content/W04/D4/internal/C2_W04_D04_key_proofs_INTERNAL.py (after the generator)
#     prints one PASS line per item proved and "PASS: 0 failing", exits 0
# the same run after the twelve-row card is regenerated with a different May member
#     fails "guided Q1" and exits 1, since the card no longer gives 3, 2, 1 and 1 of 4

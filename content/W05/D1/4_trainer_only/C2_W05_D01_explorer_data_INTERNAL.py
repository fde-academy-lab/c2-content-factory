"""Export the real numbers the Week 5 Monday explorer draws, from the same code the notebooks run.

Usage:
    python3 content/W05/D1/4_trainer_only/C2_W05_D01_explorer_data_INTERNAL.py

Writes C2_W05_D01_explorer_data_INTERNAL.json beside this file. scripts/build_companion.py then
inlines it into 1_in_class_training_content/demos/C2_W05_D01_drag_the_line_explorer_STUDENT.html.
The two public datasets are cached in ~/.cache/c2_datasets exactly as the notebooks cache them, so
nothing else is written to the repository. Every number here is one the case notebooks print or
a count taken from the same rows; the concept pages use invented numbers typed in the page.
"""
import io
import json
import pathlib
import urllib.request
import zipfile

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "C2_W05_D01_explorer_data_INTERNAL.json"
CACHE = pathlib.Path.home() / ".cache" / "c2_datasets"
CACHE.mkdir(parents=True, exist_ok=True)


def load_bank():
    """UCI Bank Marketing, bank-additional-full.csv (CC BY 4.0), cached after the first download."""
    f = CACHE / "bank-additional-full.csv"
    if not f.exists():
        url = "https://archive.ics.uci.edu/static/public/222/bank+marketing.zip"  # verified 28 October 2026
        outer = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(url, timeout=60).read()))
        inner = zipfile.ZipFile(io.BytesIO(outer.read("bank-additional.zip")))
        f.write_bytes(inner.read("bank-additional/bank-additional-full.csv"))
    return pd.read_csv(f, sep=";")


def load_cars():
    """UCI Auto MPG (CC BY 4.0), cached after the first download."""
    f = CACHE / "auto-mpg.data"
    if not f.exists():
        url = "https://archive.ics.uci.edu/static/public/9/auto+mpg.zip"  # verified 28 October 2026
        z = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(url, timeout=60).read()))
        f.write_bytes(z.read("auto-mpg.data"))
    names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
    return pd.read_csv(f, sep=r"\s+", names=names, na_values="?")


# The week's pipeline: the same columns, the same split and the same model every day.
PROFILE = ["age", "job", "marital", "education", "default", "housing", "loan"]
HISTORY = ["contact", "month", "day_of_week", "campaign", "previous", "poutcome"]
COLUMNS = PROFILE + HISTORY
MONTHS = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]


def week_split(df, seed=42):
    """Test is sealed first (20 percent, the envelope); the rest splits 75/25 into train and validation."""
    y = (df["y"] == "yes").astype(int)
    rest, test = train_test_split(df.index, test_size=0.20, stratify=y, random_state=seed)
    train, val = train_test_split(rest, test_size=0.25, stratify=y.loc[rest], random_state=seed)
    return df.loc[train], df.loc[val], df.loc[test]


def logistic(columns, df):
    num = [c for c in columns if pd.api.types.is_numeric_dtype(df[c])]
    cat = [c for c in columns if c not in num]
    prep = ColumnTransformer([("num", StandardScaler(), num), ("cat", OneHotEncoder(handle_unknown="ignore"), cat)])
    return Pipeline([("prep", prep), ("model", LogisticRegression(max_iter=2000))])


def r(x, d=4):
    return round(float(x), d)


def bank_numbers():
    bank = load_bank()
    y = (bank["y"] == "yes").astype(int)

    # The calls in time order: the month index drops when a new year starts (as case02 recovers it).
    year, prev, years = 2008, -1, []
    for m in bank["month"]:
        if MONTHS.index(m) < prev:
            year += 1
        prev = MONTHS.index(m)
        years.append(year)
    bank["year"] = years
    monthly = (bank.assign(yes=y).groupby(["year", "month"], sort=False)
               .agg(calls=("yes", "size"), yes=("yes", "sum")).reset_index())
    by_year = bank.assign(yes=y).groupby("year").agg(calls=("yes", "size"), yes=("yes", "sum"))

    train, val, test = week_split(bank)
    y_train, y_val = y.loc[train.index], y.loc[val.index]
    model = logistic(COLUMNS, bank).fit(train[COLUMNS], y_train)
    p_val = model.predict_proba(val[COLUMNS])[:, 1]
    pred = (p_val >= 0.5).astype(int)
    right_model, right_base = int((pred == y_val).sum()), int((y_val == 0).sum())

    names = model.named_steps["prep"].get_feature_names_out()
    coefs = pd.Series(model.named_steps["model"].coef_[0], index=names)
    scale = model.named_steps["prep"].named_transformers_["num"].scale_
    num_cols = [c for c in COLUMNS if pd.api.types.is_numeric_dtype(bank[c])]
    per_call = coefs["num__campaign"] / scale[num_cols.index("campaign")]

    # The trap in case01: a split with no seed and no stratify moves the held-out share of yes.
    # Sixty such splits, each drawn with a different shuffle, stand for sixty unseeded runs.
    unseeded = []
    for k in range(60):
        _, held = train_test_split(bank.index, test_size=0.2, random_state=1000 + k)
        unseeded.append(r(y.loc[held].mean()))

    # Case 3: the junior's loop, exactly as case03 runs it.
    peek_idx, fresh_idx = train_test_split(val.index, train_size=2000, stratify=y.loc[val.index], random_state=7)
    rng = np.random.default_rng(42)
    runs = []
    for k in range(60):
        cols = [str(c) for c in rng.choice(COLUMNS, size=int(rng.integers(3, 14)), replace=False)]
        m = logistic(cols, bank).fit(train[cols], y_train)
        runs.append({"n": len(cols),
                     "peek": accuracy_score(y.loc[peek_idx], m.predict(bank.loc[peek_idx, cols])),
                     "fresh": accuracy_score(y.loc[fresh_idx], m.predict(bank.loc[fresh_idx, cols]))})
    runs = pd.DataFrame(runs)
    best = int(runs["peek"].idxmax())

    return {
        "rows": len(bank), "yes": int(y.sum()), "no": int((y == 0).sum()), "rate": r(y.mean()),
        "monthly": {"year": monthly["year"].tolist(), "month": monthly["month"].tolist(),
                    "calls": monthly["calls"].astype(int).tolist(), "yes": monthly["yes"].astype(int).tolist()},
        "years": {"year": by_year.index.tolist(), "calls": by_year["calls"].astype(int).tolist(),
                  "yes": by_year["yes"].astype(int).tolist()},
        "split": {"train": len(train), "val": len(val), "test": len(test),
                  "share": [r(y_train.mean()), r(y_val.mean()), r(y.loc[test.index].mean())],
                  "val_yes": int(y_val.sum()), "val_no": int((y_val == 0).sum())},
        "unseeded": unseeded,
        "baseline": {"right": right_base, "acc": r(right_base / len(val))},
        "model": {"right": right_model, "acc": r(right_model / len(val)), "mean_p": r(p_val.mean()),
                  "campaign_logodds": r(per_call), "campaign_odds": r(np.exp(per_call))},
        "peek": {"envelope": len(peek_idx), "fresh_rows": len(fresh_idx),
                 "peek": [r(v) for v in runs["peek"]], "fresh": [r(v) for v in runs["fresh"]],
                 "ncols": runs["n"].astype(int).tolist(), "best": best,
                 "base_peek": r(1 - y.loc[peek_idx].mean()), "base_fresh": r(1 - y.loc[fresh_idx].mean()),
                 "sd_peek": r(runs["peek"].std()), "sd_fresh": r(runs["fresh"].std())},
    }


def car_numbers():
    cars = load_cars()
    n_all = len(cars)
    cars = cars.dropna(subset=["horsepower"]).reset_index(drop=True)
    line = LinearRegression().fit(cars[["horsepower"]], cars["mpg"])
    cars["hp2"] = cars["horsepower"] ** 2
    curve = LinearRegression().fit(cars[["horsepower", "hp2"]], cars["mpg"])
    r1 = cars["mpg"] - line.predict(cars[["horsepower"]])
    r2 = cars["mpg"] - curve.predict(cars[["horsepower", "hp2"]])
    bands = pd.qcut(cars["horsepower"], 5)
    edges = [float(bands.cat.categories[0].left)] + [float(iv.right) for iv in bands.cat.categories]

    def ask(hp):
        g = pd.DataFrame({"horsepower": [hp], "hp2": [hp * hp]})
        return {"hp": hp, "line": r(line.predict(g[["horsepower"]])[0], 1), "curve": r(curve.predict(g)[0], 1)}

    return {
        "all": n_all, "kept": len(cars),
        "hp": cars["horsepower"].astype(int).tolist(), "mpg": [r(v, 1) for v in cars["mpg"]],
        "line": {"a": r(line.intercept_), "b": r(line.coef_[0])},
        "curve": {"a": r(curve.intercept_), "b": r(curve.coef_[0], 6), "c": r(curve.coef_[1], 8)},
        "edges": edges,
        "band_line": [r(v, 2) for v in r1.groupby(bands, observed=True).mean()],
        "band_curve": [r(v, 2) for v in r2.groupby(bands, observed=True).mean()],
        "rmse": [r(np.sqrt((r1 ** 2).mean()), 2), r(np.sqrt((r2 ** 2).mean()), 2)],
        "ask": [ask(hp) for hp in (150, 200, 230, 300)],
        "hp_max": int(cars["horsepower"].max()), "hp_min": int(cars["horsepower"].min()),
    }


if __name__ == "__main__":
    data = {
        "label": "Real numbers from UCI Bank Marketing and UCI Auto MPG (both CC BY 4.0), run through the Week 5 pipeline.",
        "bank": bank_numbers(),
        "cars": car_numbers(),
    }
    OUT.write_text(json.dumps(data, separators=(",", ":")) + "\n")
    b, c = data["bank"], data["cars"]
    print(f"wrote {OUT.name}, {OUT.stat().st_size:,} bytes")
    print(f"bank {b['rows']:,} rows, {b['yes']:,} yes; split {b['split']['train']:,} / {b['split']['val']:,} / {b['split']['test']:,}")
    print(f"baseline {b['baseline']['acc']} ({b['baseline']['right']:,}), model {b['model']['acc']} ({b['model']['right']:,}), "
          f"campaign odds x{b['model']['campaign_odds']}")
    p = b["peek"]
    print(f"peek best {p['peek'][p['best']]} (version {p['best']}, {p['ncols'][p['best']]} columns), fresh {p['fresh'][p['best']]}; "
          f"doing nothing {p['base_peek']} / {p['base_fresh']}")
    print(f"unseeded held-out share of yes from {min(b['unseeded'])} to {max(b['unseeded'])}")
    print(f"cars {c['kept']} of {c['all']}; bands {c['band_line']} then {c['band_curve']}; rmse {c['rmse']}")

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W05/D1/4_trainer_only/C2_W05_D01_explorer_data_INTERNAL.py
#     Prints the file it wrote, then: bank 41,188 rows, 4,640 yes; split 24,712 / 8,238 / 8,238;
#     baseline 0.8874 (7,310), model 0.8971 (7,390), campaign odds x0.9334; peek best 0.9055
#     (version 45, 7 columns), fresh 0.8971; doing nothing 0.8875 / 0.8873; unseeded held-out share
#     of yes from 0.1067 to 0.1197; cars 392 of 398;
#     bands [2.73, 0.04, -2.18, -1.74, 0.81] then [0.44, 0.05, -0.99, 0.36, 0.1]; rmse [4.89, 4.36].
# Run it twice: the second run reads both files from ~/.cache/c2_datasets and writes identical JSON,
#     because every split, shuffle and column draw is seeded.

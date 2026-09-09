"""Generate the client-zero spine datasets, deterministically, from one seed.

Every version in section 4 of docs/07_Client_Zero.md is produced here, so day packs read
data rather than invent it and all sixty learners hold byte-identical files.

Usage:
    python3 data/generate_client_zero.py --version v0 --out content/W01/D2/data --stem C2_W01_D02
    python3 data/generate_client_zero.py --version v1 --out content/W01/D3/data --stem C2_W01_D03
    python3 data/generate_client_zero.py --list

Every planted defect is a witness for exactly one teaching point, and each one is named in
WITNESSES below with the day it serves. Changing a witness changes a lesson, so change the
curriculum row first.

Schema is section 3 of the locked file. Segments are Retail-Core, Retail-Plus, Business and
Student. Order status is delivered, returned or cancelled. Channel is app, web or store.
Amounts are in Rs and a typical order sits between Rs 800 and Rs 3,000.
"""
import argparse
import csv
import json
import pathlib
import random

SEED = 20260928  # Cohort 2, Week 1 Monday. Fixed forever; changing it changes every learner's data.

SEGMENTS = ["Retail-Core", "Retail-Plus", "Business", "Student"]
STATUSES = ["delivered", "returned", "cancelled"]
CHANNELS = ["app", "web", "store"]
CITIES = ["Bengaluru", "Chennai", "Hyderabad", "Pune", "Singapore"]
FIELDS = ["order_id", "customer_id", "segment", "amount", "status", "order_date", "discount"]

WITNESSES = {
    "v0": [
        ("amount stored as the text 4500", "W1 Mon, the type break"),
        ("discount absent on a known subset", "W1 Mon, KeyError and .get() with a default"),
        ("amount spelled twelve", "W1 Tue, ValueError on int()"),
        ("one record missing a required amount", "W1 Tue, the rejects log"),
        ("a nested customer sub-record in the JSON", "W1 Tue, nesting and the flattening cost"),
        ("a truncated line in the vendor JSON", "W1 Tue, JSONDecodeError in the exercise"),
    ],
    "v1": [
        ("amount spelled twelve", "W1 Wed, conversion failures counted separately"),
        ("one record missing a required amount", "W1 Wed, presence against convertibility"),
        ("near-duplicate pair sharing an order_id, differing on order_date",
         "W1 Wed, the whole-record dedupe that reports zero"),
        ("one whale order of Rs 480,000", "W1 Wed keep-or-investigate, W1 Thu the mean that misleads"),
        ("a Student segment of exactly 12 records", "W1 Thu, sample size bites"),
        ("a truncated line in the JSON", "W1 Wed, the parser names a position past the end"),
        ("a companion file with the header row duplicated", "W1 Wed, the header is part of the contract"),
        ("text-typed amounts beyond twelve: a thousands separator, an internal space, a currency prefix",
         "W1 Wed, several values fail conversion in one column"),
    ],
}


def _date(rng, day_offset):
    """Order dates across August and early September 2026, weekdays only."""
    from datetime import date, timedelta
    d = date(2026, 8, 3) + timedelta(days=day_offset)
    while d.weekday() > 4:
        d += timedelta(days=1)
    return d.isoformat()


def _typical_amount(rng):
    """A typical order, Rs 800 to Rs 3,000 per section 3 of the locked file."""
    return rng.randrange(800, 3001, 5)


def _base_rows(rng, n, segments):
    rows = []
    for i in range(n):
        seg = segments[i]
        rows.append({
            "order_id": f"KR{4200 + i}",
            "customer_id": f"C{1000 + rng.randrange(1, 900)}",
            "segment": seg,
            "amount": str(_typical_amount(rng)),
            "status": rng.choice(STATUSES),
            "order_date": _date(rng, i // 2),
            "discount": str(rng.randrange(25, 301, 25)) if rng.random() < 0.30 else "",
        })
    return rows


def _segment_plan(rng, n, student_count=None):
    """Assign segments. When student_count is given, exactly that many are Student."""
    if student_count is None:
        plan = [SEGMENTS[i % 4] for i in range(n)]
    else:
        plan = ["Student"] * student_count
        rest = [s for s in SEGMENTS if s != "Student"]
        plan += [rest[i % 3] for i in range(n - student_count)]
    rng.shuffle(plan)
    return plan


def build_v0():
    """About 30 flat order records. Monday's setup cell, and Tuesday's two files."""
    rng = random.Random(SEED)
    rows = _base_rows(rng, 30, _segment_plan(rng, 30))
    rows[0]["amount"] = "4500"          # witness: the type break, an amount stored as text
    rows[10]["amount"] = "twelve"       # witness: ValueError on int()
    rows[14]["amount"] = ""             # witness: a missing required field
    rows[14]["_true_amount"] = "2840"   # witness: the CSV threw it away, the JSON still carries it
    for r in rows[:6]:
        r["discount"] = ""              # witness: absent on a known subset
    return rows


def build_v1():
    """50 records at their dirtiest. Wednesday's profiling pass and Thursday's statistics."""
    rng = random.Random(SEED + 1)
    rows = _base_rows(rng, 49, _segment_plan(rng, 49, student_count=12))
    rows[10]["amount"] = "twelve"       # witness: a word where a number belongs
    rows[14]["amount"] = ""             # witness: a missing required field
    rows[31]["amount"] = "12,400"       # witness: a thousands separator
    rows[35]["amount"] = "24 500"       # witness: an internal space
    rows[40]["amount"] = "Rs 8000"      # witness: a currency prefix
    rows[37]["amount"] = ""             # witness: a second missing amount, so presence bites
    rows[14]["_true_amount"] = "1975"   # witness: recoverable from the nested block
    rows[37]["_true_amount"] = ""       # witness: genuinely lost, so recovery is not automatic
    rows[32]["amount"] = "480000"       # witness: the whale, real and convertible

    # witness: the near-duplicate pair. The twin is copied from a non-Student order on purpose,
    # so the shipped file still holds exactly 12 Student records once the pair is added.
    source = next(i for i, r in enumerate(rows) if r["segment"] != "Student" and r["amount"].isdigit())
    twin = dict(rows[source])
    twin["order_date"] = _date(rng, 40)
    rows.append(twin)
    return rows


# The two files below are not section 4 versions. They are Week 1 Day 2 exercise variants of v0,
# kept here so the day pack never invents client-zero data of its own.

def build_w1d2_lab():
    """A fresh file for Tuesday's AI-free lab. Defects the room has not met."""
    rng = random.Random(SEED + 2)
    rows = _base_rows(rng, 24, _segment_plan(rng, 24))
    for i, r in enumerate(rows):
        r["order_id"] = f"KR5{300 + i}"
    rows[3]["amount"] = "nine hundred"   # a word, as on Tuesday
    rows[7]["amount"] = ""               # a missing required field
    rows[12]["amount"] = "1,240"         # the new one: a thousands separator
    return rows


def build_w1d2_takehome():
    """A third file for Tuesday's take-home. Carries one order that converts and is still wrong."""
    rng = random.Random(SEED + 3)
    rows = _base_rows(rng, 30, _segment_plan(rng, 30))
    for i, r in enumerate(rows):
        r["order_id"] = f"KR6{400 + i}"
    rows[7]["amount"] = "forty two"      # a word
    rows[10]["amount"] = ""              # a missing required field
    rows[18]["amount"] = "2 450"         # an internal space
    rows[3]["amount"] = "-1850"          # converts cleanly and is still wrong: the threshold decision
    return rows


def _customer_block(rng, row):
    return {
        "customer_id": row["customer_id"],
        "city": rng.choice(CITIES),
        "signup_date": _date(rng, rng.randrange(0, 20)),
    }


# Exercise variants ship as a single CSV. Only the spine versions get the JSON pair.
CSV_ONLY = {"w1d2-lab": "lab", "w1d2-takehome": "takehome"}


def write(version, out_dir, stem):
    rows = {"v0": build_v0, "v1": build_v1,
            "w1d2-lab": build_w1d2_lab, "w1d2-takehome": build_w1d2_takehome}[version]()
    out = pathlib.Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    rng = random.Random(SEED + 7)

    if version in CSV_ONLY:
        only = out / f"{stem}_{CSV_ONLY[version]}_STUDENT.csv"
        with only.open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
            w.writeheader(); w.writerows(rows)
        return rows, [only]

    csv_path = out / f"{stem}_orders_STUDENT.csv"
    with csv_path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader(); w.writerows(rows)

    nested = []
    for r in rows:
        rec = {k: r[k] for k in ("order_id", "segment", "status", "order_date")}
        rec["amount"] = int(r["amount"]) if r["amount"].isdigit() else None
        rec["source"] = {"system": "kalpa_retail_orders",
                         "amount_raw": r.get("_true_amount", r["amount"]) or r["amount"]}
        rec["customer"] = _customer_block(rng, r)
        nested.append(rec)
    json_path = out / f"{stem}_orders_STUDENT.json"
    json_path.write_text(json.dumps(nested, indent=2) + "\n")

    lines = json.dumps(nested[:8], indent=2).splitlines()
    trunc = out / f"{stem}_vendor_truncated_STUDENT.json"
    trunc.write_text("\n".join(lines[:47]) + "\n")

    written = [csv_path, json_path, trunc]
    if version in ("v1",):
        dup = out / f"{stem}_companion_STUDENT.csv"
        with dup.open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
            w.writeheader(); w.writeheader()   # witness: the header row duplicated
            w.writerows(rows[:20])
        written.append(dup)
    return rows, written


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--version", choices=["v0", "v1", "w1d2-lab", "w1d2-takehome"])
    ap.add_argument("--out", help="the day pack's data folder, for example content/W01/D3/data")
    ap.add_argument("--stem", help="filename stem, for example C2_W01_D03")
    ap.add_argument("--list", action="store_true", help="list every version and its witnesses")
    a = ap.parse_args()

    if a.list:
        for v, ws in WITNESSES.items():
            print(f"\n{v}")
            for what, serves in ws:
                print(f"  {what:70} -> {serves}")
        print("\nv2, v3, v4 and the document corpus are specified in section 4 of")
        print("docs/07_Client_Zero.md and are not generated yet. They are first needed in")
        print("Week 2, Week 4, Week 5 and Week 11, and each needs its own build.")
        return

    if not (a.version and a.out and a.stem):
        ap.error("--version, --out and --stem are all required unless --list is given")
    rows, written = write(a.version, a.out, a.stem)
    print(f"{a.version}: {len(rows)} rows")
    for p in written:
        print("  wrote", p)


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# --list
#     Prints six v0 witnesses and eight v1 witnesses, then the note about v2 onward.
# --version v0 --out content/W01/D2/data --stem C2_W01_D02
#     30 rows. Exactly one amount reads "4500" as text, one reads "twelve", one is empty.
#     The first six rows carry no discount. Writes three files.
# --version v1 --out content/W01/D3/data --stem C2_W01_D03
#     50 rows, 49 distinct order_ids. Whole-record duplicate count is 0 and the near-duplicate
#     pair differs only on order_date. Exactly 12 rows are Student. One amount is 480000.
#     Six amounts fail int(). Writes four files, the fourth having its header row twice.
# Running the same command twice
#     Produces byte-identical files, because every draw comes from a seeded Random.

"""Write the take-home's second sample from data/generate_client_zero.py, without editing it.

    python3 content/W02/D4/internal/C2_W02_D04_build_takehome_data_INTERNAL.py

The generator's v4 warehouse is built by build_v4(), which draws every table from the module's
SEED. Importing the module and changing SEED before the call gives a second warehouse with the
same families of defect in new places, which is what a take-home needs: the room's answers from
class do not carry over. Only the three tables the take-home reads are written, as CSVs, into
this day's data/ folder. Nothing in data/ is touched.
"""
import csv
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "data"))
import generate_client_zero as gen  # noqa: E402

TAKEHOME_SEED = 20261015
OUT = ROOT / "content" / "W02" / "D4" / "data"


def write(name, rows, fields):
    path = OUT / f"C2_W02_D04_takehome_{name}_STUDENT.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k: r[k] for k in fields})
    print("wrote", path.relative_to(ROOT), len(rows), "rows")


def main():
    gen.SEED = TAKEHOME_SEED
    tables = gen.build_v4()
    write("orders", tables["orders"],
          ["order_id", "customer_id", "order_date", "quarter", "channel", "amount", "status"])
    write("customers", tables["customers"], ["customer_id", "segment", "city", "country", "joined_date"])
    write("exposure", tables["campaign_exposure"], ["customer_id", "campaign_id", "exposed_date"])


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W02/D4/internal/C2_W02_D04_build_takehome_data_INTERNAL.py
#     Writes three CSVs into content/W02/D4/data/: 1,000 orders, 340 customers and the exposure
#     feed, and prints each path with its row count.
# Running it twice
#     Writes byte-identical files, since the seed is fixed.

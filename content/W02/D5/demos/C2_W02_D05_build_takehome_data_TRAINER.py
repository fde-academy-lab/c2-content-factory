"""Write Friday's take-home exports: a second v4 sample with its own plants.

Run from the repository root:  python3 content/W02/D5/demos/C2_W02_D05_build_takehome_data_TRAINER.py

The take-home asks for the three deliverables rebuilt from a fresh export, so the fresh export has
to be a real second sample and not the class file renamed. data/generate_client_zero.py has no
take-home switch for v4, and this session may not edit it, so this script loads the generator,
moves its seed to 20261016 and calls the same two functions that write the class exports. The
quarter totals are pinned by the generator's contract and stay Rs 10.00 crore and Rs 9.84 crore;
the customers, the member left out of the clean table and the double-paid rows all change.

What the sample plants is printed below and recorded in the day sheet, never in a learner file.
"""
import csv
import importlib.util
import pathlib

SEED = 20261016
ROOT = pathlib.Path("content/W02/D5/data")

spec = importlib.util.spec_from_file_location("gen", "data/generate_client_zero.py")
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)
gen.SEED = SEED

tables = gen.build_v4()
tables["campaigns"] = gen.V4_CAMPAIGNS
clean, raw, missing = gen._v4_exports(tables)

for name, rows in (("customer_table", clean), ("raw_export", raw)):
    path = ROOT / f"C2_W02_D05_takehome_{name}_STUDENT.csv"
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print("wrote", path, len(rows), "rows")

print("TRAINER ONLY: the member left out of the take-home clean table is", missing)
print("TRAINER ONLY: orders with two payment rows:",
      len(tables["_meta"]["instalment"]), "instalments and", len(tables["_meta"]["retry"]), "retries")

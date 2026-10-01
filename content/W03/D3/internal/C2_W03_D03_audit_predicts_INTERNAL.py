"""Run scripts/distractor_audit.py on the parallel-build notebook's predict questions.

    python3 content/W03/D3/internal/C2_W03_D03_audit_predicts_INTERNAL.py

The audit reads lettered option sets in exercise folders and their keys in a solutions file, and a
notebook's **Predict before you run.** sets live in markdown cells, so verify.py never sends them
to it. This script lifts every predict set and the letter its **What happened.** cell gives, writes
them as an exercise file and a solutions file in a temporary folder shaped the way the audit
expects, and runs the audit there: no key may be the longest option, and the keys must spread. It
writes nothing inside the repository.
"""
import json
import pathlib
import re
import subprocess
import sys
import tempfile

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "scripts" / "distractor_audit.py").exists())
NOTEBOOK = ROOT / "content/W03/D3/parallel-build/C2_W03_D03_new_york_revenue_tree_STUDENT.ipynb"


def predict_sets(markdown):
    """(stem, [(letter, option)]) for every predict paragraph, in notebook order."""
    sets = []
    for m in re.finditer(r"\*\*Predict before you run\.\*\*(.*?)(?=\n\n|\Z)", markdown, re.S):
        block = " ".join(m.group(1).split())
        stem, options = re.split(r"(?= a\) )", block, maxsplit=1)
        parts = re.split(r";? ([a-d])\) ", " " + options)
        sets.append((stem.strip(), list(zip(parts[1::2], [t.strip().rstrip(".") for t in parts[2::2]]))))
    return sets


def main():
    cells = json.loads(NOTEBOOK.read_text(encoding="utf-8"))["cells"]
    markdown = "\n\n".join("".join(c["source"]) for c in cells if c["cell_type"] == "markdown")
    sets = predict_sets(markdown)
    keys = re.findall(r"\*\*What happened\.\*\* The answer is ([a-d])", markdown)
    if len(sets) != len(keys):
        sys.exit(f"FAIL  {len(sets)} predict sets but {len(keys)} answer letters")
    with tempfile.TemporaryDirectory() as tmp:
        unguided = pathlib.Path(tmp, "exercises", "unguided")
        solutions = pathlib.Path(tmp, "exercises", "solutions")
        unguided.mkdir(parents=True)
        solutions.mkdir(parents=True)
        lines = ["# The parallel build's predict questions", ""]
        for i, (stem, options) in enumerate(sets, 1):
            lines += [f"### Item {i}", "", stem] + [f"   {letter}) {text}" for letter, text in options] + [""]
        (unguided / "C2_W03_D03_predicts_STUDENT.md").write_text("\n".join(lines), encoding="utf-8")
        (solutions / "C2_W03_D03_predicts_STUDENT.md").write_text(
            "Answers: " + " ".join(f"{i}{k}" for i, k in enumerate(keys, 1)) + "\n", encoding="utf-8")
        run = subprocess.run([sys.executable, str(ROOT / "scripts/distractor_audit.py"), str(unguided)],
                             capture_output=True, text=True)
        print(run.stdout.rstrip())
        sys.exit(run.returncode)


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W03/D3/internal/C2_W03_D03_audit_predicts_INTERNAL.py
#     Prints the audit's line for 7 items with keys spread over a to d, then RESULT: PASS.
# A predict set rewritten so its key is the longest option
#     The audit names the item and the run ends on RESULT: FAIL.

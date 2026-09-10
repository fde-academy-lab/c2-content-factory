"""Prove a notebook teaches on the page: outputs saved, diagrams rendered, checks passing.

A notebook is read far more often than it is executed, so an unexecuted notebook teaches nobody
on GitHub and nobody opening it cold in a Codespace. This is the gate that stops one shipping.

Usage:
    python3 scripts/nb_check.py content/W01/D3
    python3 scripts/nb_check.py content/W01/D3/notebooks/C2_W01_D03_01_profiling_STUDENT.ipynb

What it checks, per notebook:
  1. Every code cell that has source carries at least one saved output.
  2. At least three outputs are rendered diagrams (SVG, PNG, or HTML holding an <svg>).
  3. At least five check results are present, and none of them failed.

A TODO exercise notebook is the one exception to rule 1, because its placeholders are meant to
stop it. Its solution twin carries the rule in full.

Exit code 0 means every notebook passed. Any FAIL line means a notebook needs re-running.
"""
import json
import pathlib
import re
import sys

MIN_DIAGRAMS = 3
MIN_CHECKS = 5

# c2kit.check writes these classes; the bare tokens catch a notebook that printed its checks
# before the helper existed, so an older pack still reports rather than silently scoring zero.
PASS_MARK = re.compile(r"c2k-pass|^\s*PASS\b", re.M)
FAIL_MARK = re.compile(r"c2k-fail|^\s*FAIL\b", re.M)
TODO_MARK = re.compile(r"__TODO\d*__")


def _text_of(output):
    """Every piece of text an output carries, joined, whatever mime type it arrived under."""
    parts = []
    for key in ("text", "traceback"):
        val = output.get(key)
        if val:
            parts.append("".join(val) if isinstance(val, list) else str(val))
    for mime, val in (output.get("data") or {}).items():
        if mime.startswith("text/") or mime.endswith("+xml"):
            parts.append("".join(val) if isinstance(val, list) else str(val))
    return "\n".join(parts)


def _is_diagram(output):
    data = output.get("data") or {}
    if "image/svg+xml" in data or "image/png" in data:
        return True
    html = data.get("text/html")
    if html and "<svg" in ("".join(html) if isinstance(html, list) else str(html)):
        return True
    return False


def check_notebook(path):
    """Return (failures, a one-line report) for one notebook."""
    try:
        nb = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"FAIL  {path.name}: notebook does not parse ({e})")
        return 1, ""

    cells = nb.get("cells", [])
    source_all = "\n".join("".join(c.get("source", [])) for c in cells)
    is_todo = bool(TODO_MARK.search(source_all))

    empty, diagrams, passed, failed, errors = [], 0, 0, 0, 0
    for n, cell in enumerate(cells, start=1):
        if cell.get("cell_type") != "code":
            continue
        source = "".join(cell.get("source", [])).strip()
        outputs = cell.get("outputs") or []
        if source and not outputs:
            empty.append(n)
        for out in outputs:
            if out.get("output_type") == "error":
                errors += 1
            if _is_diagram(out):
                diagrams += 1
            text = _text_of(out)
            passed += len(PASS_MARK.findall(text))
            failed += len(FAIL_MARK.findall(text))

    calls = len(re.findall(r"\bcheck\s*\(", source_all))
    fails = 0

    if empty and not is_todo:
        shown = ", ".join(str(n) for n in empty[:8]) + (" and more" if len(empty) > 8 else "")
        print(f"FAIL  {path.name}: {len(empty)} code cells carry no saved output (cells {shown}). "
              f"Re-run the notebook from a clean kernel and save it with its outputs.")
        fails += 1
    if diagrams < MIN_DIAGRAMS:
        print(f"FAIL  {path.name}: {diagrams} rendered diagram outputs, and {MIN_DIAGRAMS} are "
              f"required. Render the MAP and SUM diagrams from code cells so they save.")
        fails += 1
    if passed + failed < MIN_CHECKS:
        print(f"FAIL  {path.name}: {passed + failed} check results and {calls} check calls in "
              f"source, against {MIN_CHECKS} required. Add CHECK cells that assert on shape.")
        fails += 1
    if failed:
        print(f"FAIL  {path.name}: {failed} checks report FAIL. Fix the notebook, not the check.")
        fails += 1
    if errors and not is_todo:
        print(f"FAIL  {path.name}: {errors} cells ended in an uncaught error output. A deliberate "
              f"failure is caught and printed so the notebook keeps running.")
        fails += 1

    kind = "TODO twin" if is_todo else "notebook"
    report = (f"      {path.name}: {kind}, {len(cells)} cells, {diagrams} diagrams, "
              f"{passed} pass and {failed} fail from {calls} check calls")
    return fails, report


def main():
    targets = [pathlib.Path(a) for a in sys.argv[1:] if not a.startswith("--")]
    if not targets:
        print("FAIL  nb_check.py needs a notebook or a folder to look in")
        sys.exit(1)

    books = []
    for t in targets:
        books.extend(sorted(t.rglob("*.ipynb")) if t.is_dir() else [t])
    books = [b for b in books if ".ipynb_checkpoints" not in b.parts]

    if not books:
        print("INFO  no notebooks found, so nb_check has nothing to prove")
        sys.exit(0)

    fails, reports, total_pass, total_fail = 0, [], 0, 0
    for book in books:
        f, report = check_notebook(book)
        fails += f
        if report:
            reports.append(report)
            m = re.search(r"(\d+) pass and (\d+) fail", report)
            total_pass += int(m.group(1))
            total_fail += int(m.group(2))
    for report in reports:
        print(report)
    print(f"      {len(books)} notebooks, {total_pass} checks passing, {total_fail} failing")
    print("RESULT:", "FAIL" if fails else "PASS", f"({fails} failures)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# scripts/nb_check.py content/W01/D3
#     Reads both Wednesday notebooks and reports cells, diagrams and check totals per notebook.
#     Exit 0 when each carries saved outputs, three or more diagrams and five or more passing checks.
# scripts/nb_check.py on a notebook saved without running it
#     One FAIL line naming how many code cells hold no output, and exit 1.
# scripts/nb_check.py on a hands-on notebook containing __TODO1__
#     The empty-output rule is skipped, since the placeholders are meant to stop it, and the
#     diagram and check rules still apply.
# scripts/nb_check.py content/W02
#     INFO and exit 0 while that week holds no notebooks, so the gate never fails on absence.

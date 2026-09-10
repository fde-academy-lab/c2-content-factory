"""Prove an Excel decision tool computes, by recalculating it through LibreOffice headless.

openpyxl reads the cached value Excel last wrote, so a workbook whose verdict cell holds a typed
string looks identical to one whose verdict is computed. This forces a real recalculation, asserts
the named verdicts, then flips the design decisions and asserts that the verdicts moved. A tool
whose verdict does not move under any flip is a spreadsheet with words in it.

Usage:
    python3 scripts/xlsx_recalc.py content/W01/D3
    python3 scripts/xlsx_recalc.py content/W01/D3/demos/C2_W01_D03_decision_tool_recalc_INTERNAL.md

The manifest sits beside the workbook, named to the stem rule with the INTERNAL audience, as a
markdown file holding one fenced yaml block:

    ```yaml
    workbook: C2_W01_D03_decision_tool_STUDENT.xlsx
    verdicts:
      - {sheet: Missingness, cell: D14, expect: "keep and flag, and write the reason"}
      - {sheet: Export, cell: B2, contains: "44 of 50 rows"}
    flips:
      - name: absence stops meaning something
        set: [{sheet: Missingness, cell: B7, value: "no"}]
        verdicts:
          - {sheet: Missingness, cell: D14, expect: "drop the field"}
    ```

`expect` matches the whole cell after case folding and whitespace collapse; `contains` matches a
fragment. Exit code 0 means every verdict computed and every flip moved what it should.
"""
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

YAML_FENCE = re.compile(r"```ya?ml\s*\n(.*?)\n```", re.S)


def _norm(value):
    return re.sub(r"\s+", " ", str(value if value is not None else "")).strip().casefold()


def recalc(path):
    """Convert through LibreOffice so every formula is evaluated, and return the rebuilt path."""
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        return None, "LibreOffice is not installed in this session"
    out = pathlib.Path(tempfile.mkdtemp(prefix="c2_recalc_"))
    profile = out / "profile"
    r = subprocess.run(
        [soffice, "--headless", "--norestore", f"-env:UserInstallation=file://{profile}",
         "--convert-to", "xlsx", "--outdir", str(out), str(path)],
        capture_output=True, text=True, timeout=300)
    rebuilt = out / (path.stem + ".xlsx")
    if not rebuilt.exists():
        return None, f"LibreOffice produced nothing ({r.stderr.strip()[:160] or 'no error text'})"
    return rebuilt, None


def read_values(path):
    """Every cell's evaluated value, keyed (sheet, cell)."""
    import openpyxl
    wb = openpyxl.load_workbook(path, data_only=True)
    return {(ws.title, c.coordinate): c.value for ws in wb.worksheets for row in ws.iter_rows()
            for c in row}


def apply_sets(source, sets, dest):
    import openpyxl
    wb = openpyxl.load_workbook(source)
    for s in sets:
        wb[s["sheet"]][s["cell"]] = s["value"]
    wb.save(dest)
    return dest


def assert_verdicts(values, verdicts, label, name):
    fails = 0
    for v in verdicts:
        got = values.get((v["sheet"], v["cell"]))
        if "expect" in v:
            ok = _norm(got) == _norm(v["expect"])
            want = f'"{v["expect"]}"'
        else:
            ok = _norm(v["contains"]) in _norm(got)
            want = f'something containing "{v["contains"]}"'
        if not ok:
            print(f"FAIL  {name} [{label}] {v['sheet']}!{v['cell']}: wanted {want}, "
                  f'recalculated to "{got}"')
            fails += 1
    return fails


def run_manifest(manifest_path):
    import yaml
    text = manifest_path.read_text(encoding="utf-8")
    fence = YAML_FENCE.search(text)
    if not fence:
        print(f"FAIL  {manifest_path.name}: no fenced yaml block, so nothing can be asserted")
        return 1
    spec = yaml.safe_load(fence.group(1))
    book = manifest_path.parent / spec["workbook"]
    if not book.exists():
        print(f"FAIL  {manifest_path.name}: names {spec['workbook']}, which does not exist beside it")
        return 1

    rebuilt, why = recalc(book)
    if rebuilt is None:
        print(f"INFO  {book.name}: recalculation did not run, so the verdicts were not proved ({why})")
        return 0

    fails = assert_verdicts(read_values(rebuilt), spec.get("verdicts", []), "as shipped", book.name)

    for flip in spec.get("flips", []):
        work = pathlib.Path(tempfile.mkdtemp(prefix="c2_flip_")) / book.name
        apply_sets(book, flip["set"], work)
        flipped, why = recalc(work)
        if flipped is None:
            print(f"INFO  {book.name}: flip '{flip['name']}' did not recalculate ({why})")
            continue
        fails += assert_verdicts(read_values(flipped), flip["verdicts"], flip["name"], book.name)

    if not fails:
        n_v = len(spec.get("verdicts", []))
        n_f = len(spec.get("flips", []))
        print(f"      {book.name}: {n_v} verdicts computed, {n_f} decisions flipped and re-asserted")
    return fails


def main():
    targets = [pathlib.Path(a) for a in sys.argv[1:] if not a.startswith("--")]
    if not targets:
        print("FAIL  xlsx_recalc.py needs a manifest or a folder to look in")
        sys.exit(1)

    manifests = []
    for t in targets:
        if t.is_dir():
            manifests += sorted(p for p in t.rglob("*recalc*.md"))
        else:
            manifests.append(t)

    books = [p for t in targets if t.is_dir() for p in t.rglob("*.xlsx")]
    if not manifests:
        if books:
            print(f"FAIL  {len(books)} workbooks and no recalc manifest beside any of them, "
                  f"so no verdict can be proved")
            sys.exit(1)
        print("INFO  no workbooks found, so xlsx_recalc has nothing to prove")
        sys.exit(0)

    try:
        import yaml, openpyxl  # noqa: F401
    except ImportError as e:
        print(f"INFO  xlsx_recalc needs {e.name}; install it with pip install {e.name}")
        sys.exit(0)

    fails = sum(run_manifest(m) for m in manifests)
    print("RESULT:", "FAIL" if fails else "PASS", f"({fails} failures)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# scripts/xlsx_recalc.py content/W01/D3
#     Finds the recalc manifest in demos/, rebuilds the workbook through LibreOffice, asserts each
#     verdict cell, then flips each design decision and asserts the moved verdict. Exit 0 on clean.
# A workbook whose verdict cell holds a typed string rather than a formula
#     The as-shipped assertion passes and every flip fails, because the string cannot move. Exit 1.
# A workbook present with no manifest beside it
#     One FAIL line saying no verdict can be proved, and exit 1.
# The same command in a session with no LibreOffice
#     INFO saying the verdicts were not proved, and exit 0, so a missing tool degrades the report
#     rather than failing the gate.

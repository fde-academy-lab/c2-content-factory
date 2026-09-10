"""Click every control on every companion page and report what did nothing.

A demo is the one artifact nobody re-reads before a session, so a dead button reaches a projector
in front of sixty people. This opens each page in a headless browser, clicks everything, watches
the page for a visible change, reads the console, and checks each dropdown by the element sitting
at its own screen coordinates, which is how a control covered by an overlay is caught.

Usage:
    python3 scripts/html_sweep.py content/W01/D3
    python3 scripts/html_sweep.py content/W01/D3/demos/C2_W01_D03_identity_rule_STUDENT.html
    python3 scripts/html_sweep.py content/W01/D3 --install    # allow the pip install to run

Without a browser it falls back to a static scan and says plainly that the interactive sweep did
not run, so a report is never mistaken for a proof.
"""
import pathlib
import re
import subprocess
import sys

CONTROLS = "button, [role=button], input, select, textarea, summary, [onclick], a[href^='#']"


def find_chromium():
    for pattern in ("chromium-*/chrome-linux/chrome", "chromium/chrome-linux/chrome",
                    "chromium_headless_shell-*/chrome-linux/headless_shell"):
        for path in sorted(pathlib.Path("/opt/pw-browsers").glob(pattern)):
            if path.is_file():
                return str(path)
    return None


def get_playwright(allow_install):
    """Import playwright, installing it once when asked, and say what happened either way."""
    try:
        from playwright.sync_api import sync_playwright
        return sync_playwright
    except ImportError:
        pass
    if not allow_install:
        return None
    print("INFO  playwright is not installed; installing it now")
    subprocess.run([sys.executable, "-m", "pip", "install", "--quiet", "playwright"],
                   capture_output=True, text=True, timeout=600)
    try:
        from playwright.sync_api import sync_playwright
        return sync_playwright
    except ImportError:
        return None


def ensure_browser(allow_install):
    exe = find_chromium()
    if exe or not allow_install:
        return exe
    print("INFO  no chromium under /opt/pw-browsers; asking playwright to install one")
    subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"],
                   capture_output=True, text=True, timeout=900)
    return find_chromium()


def static_scan(paths):
    """What can be said about a page without running it: controls that nothing refers to."""
    fails = 0
    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        ids = re.findall(r"<(?:button|select|input|a)[^>]*\bid=[\"']([^\"']+)[\"']", text)
        classes = re.findall(r"<(?:button|select|input)[^>]*\bclass=[\"']([^\"']+)[\"']", text)
        script = "".join(re.findall(r"<script[^>]*>(.*?)</script>", text, re.S))
        orphans = [i for i in ids if i not in script and f'"{i}"' not in text.replace(
            f'id="{i}"', "")]
        loose = [c for group in classes for c in group.split()
                 if c not in script and f".{c}" not in text]
        if "localStorage" in text or "sessionStorage" in text:
            print(f"FAIL  {path.name}: uses browser storage, which a companion never does")
            fails += 1
        if orphans:
            print(f"FAIL  {path.name}: {len(orphans)} controls carry an id nothing refers to "
                  f"({', '.join(orphans[:5])}), so they are probably dead")
            fails += 1
        print(f"      {path.name}: {len(ids)} identified controls, "
              f"{len(set(loose))} classes with no rule or handler found, statically")
    print("INFO  the interactive sweep did not run, so no control was actually clicked")
    return fails


def sweep(paths, sync_playwright, exe):
    fails = 0
    launch = {"args": ["--no-sandbox"]}
    if exe:
        launch["executable_path"] = exe
    with sync_playwright() as pw:
        browser = pw.chromium.launch(**launch)
        for path in paths:
            page = browser.new_page(viewport={"width": 1400, "height": 1000})
            errors = []
            page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
            page.on("pageerror", lambda e: errors.append(str(e)))
            page.goto(path.resolve().as_uri(), wait_until="load")

            controls = page.locator(CONTROLS)
            total, dead, unreachable = controls.count(), [], []
            for i in range(total):
                el = controls.nth(i)
                try:
                    label = (el.inner_text(timeout=800) or el.get_attribute("id")
                             or el.get_attribute("aria-label") or f"control {i + 1}")[:34]
                except Exception:
                    label = f"control {i + 1}"
                before = page.evaluate(
                    "() => document.body.innerHTML.length + '|' + document.body.innerText.length")
                try:
                    el.click(timeout=1500)
                except Exception:
                    unreachable.append(label)
                    continue
                after = page.evaluate(
                    "() => document.body.innerHTML.length + '|' + document.body.innerText.length")
                if before == after:
                    dead.append(label)

            # A dropdown can be present, enabled and still unusable because something sits over it.
            covered = page.evaluate("""() => {
                const out = [];
                for (const s of document.querySelectorAll('select')) {
                  const r = s.getBoundingClientRect();
                  if (!r.width || !r.height) { out.push(s.id || s.name || 'a select'); continue; }
                  const hit = document.elementFromPoint(r.left + r.width / 2, r.top + r.height / 2);
                  if (!hit || (hit !== s && !s.contains(hit) && !hit.contains(s)))
                    out.push(s.id || s.name || 'a select');
                }
                return out;
            }""")

            if errors:
                print(f"FAIL  {path.name}: {len(errors)} console errors, first is "
                      f"{errors[0][:110]}")
                fails += 1
            if unreachable:
                print(f"FAIL  {path.name}: {len(unreachable)} controls could not be clicked at all "
                      f"({'; '.join(unreachable[:4])})")
                fails += 1
            if dead:
                print(f"FAIL  {path.name}: {len(dead)} controls changed nothing on the page "
                      f"({'; '.join(dead[:4])}). Every control does something visible.")
                fails += 1
            if covered:
                print(f"FAIL  {path.name}: {len(covered)} dropdowns are covered at their own "
                      f"centre point ({', '.join(covered[:4])})")
                fails += 1
            print(f"      {path.name}: {total} controls clicked, {len(dead)} inert, "
                  f"{len(errors)} console errors")
            page.close()
        browser.close()
    return fails


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    allow_install = "--install" in sys.argv or "--no-install" not in sys.argv
    if not args:
        print("FAIL  html_sweep.py needs a page or a folder to look in")
        sys.exit(1)

    paths = []
    for a in args:
        t = pathlib.Path(a)
        paths += sorted(t.rglob("*.html")) if t.is_dir() else [t]
    if not paths:
        print("INFO  no pages found, so the sweep has nothing to visit")
        sys.exit(0)

    sync_playwright = get_playwright(allow_install)
    exe = ensure_browser(allow_install) if sync_playwright else None
    if sync_playwright and exe:
        fails = sweep(paths, sync_playwright, exe)
    else:
        print("INFO  no usable browser, so falling back to a static scan")
        fails = static_scan(paths)

    print("RESULT:", "FAIL" if fails else "PASS", f"({fails} failures)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# scripts/html_sweep.py content/W01/D3
#     Opens every page under the day, clicks every button, input, select and anchor, and reports
#     the count clicked, the count that changed nothing, and any console error. Exit 0 on clean.
# A page with a button whose handler was renamed
#     One FAIL line naming the button's label as changing nothing, and exit 1.
# A page whose select sits under a fixed header
#     One FAIL line saying the dropdown is covered at its own centre point, and exit 1.
# The same command with no playwright and --no-install
#     A static scan, an INFO line saying the interactive sweep did not run, and exit 0 unless the
#     static scan itself found browser storage or an orphaned control id.

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

A Week 5 kit page (one that carries the kit's nav, [data-w5-nav]) is walked route by route: the
shell's own controls (the nav, the rail, the presenter toggle) are swept once, then each route is
opened in turn and the controls inside its section are swept, tab by tab, until a pass finds no
control it has not already clicked, so a panel that appears only after a click is swept too. The
report gives one line per route. A page without the kit's nav is swept exactly as before.
"""
import pathlib
import re
import subprocess
import sys

CONTROLS = "button, [role=button], input, select, textarea, summary, [onclick], a[href^='#']"

# A content signature rather than a length, because two different states can be the same length.
SIGNATURE = """() => {
  const s = document.body.innerHTML + '\\u0000' + document.body.innerText;
  let h = 5381;
  for (let i = 0; i < s.length; i++) h = ((h * 33) ^ s.charCodeAt(i)) >>> 0;
  return h + ':' + s.length;
}"""

NUDGE = """e => {
  const tag = e.tagName.toLowerCase();
  const fire = () => { e.dispatchEvent(new Event('input', {bubbles:true}));
                       e.dispatchEvent(new Event('change', {bubbles:true})); };
  if (tag === 'select'){
    if (e.options.length < 2) return false;
    e.selectedIndex = (e.selectedIndex + 1) % e.options.length; fire(); return true;
  }
  if (tag === 'textarea'){ e.value = (e.value || '') + 'x'; fire(); return true; }
  if (tag !== 'input') return false;
  const t = (e.type || 'text').toLowerCase();
  if (t === 'checkbox' || t === 'radio' || t === 'button' || t === 'submit') return false;
  if (t === 'number' || t === 'range'){
    const step = Number(e.step) || 1;
    const max = e.max === '' ? Infinity : Number(e.max);
    const min = e.min === '' ? -Infinity : Number(e.min);
    let v = Number(e.value) + step;
    if (v > max) v = Math.max(min, Number(e.value) - step);
    e.value = String(v); fire(); return true;
  }
  e.value = (e.value || '') + 'x'; fire(); return true;
}"""

SHUT_MODALS = """() => {
  for (const d of document.querySelectorAll('dialog[open]'))
    { if (typeof d.close === 'function') d.close(); else d.removeAttribute('open'); }
}"""


def find_chromium():
    """Where this session keeps chromium, which differs between the container and setup.sh.

    Returning None is not a failure: playwright resolves its own download on its own, so the
    caller launches without an executable path and only falls back when that launch fails too.
    """
    import os
    roots = [os.environ.get("PLAYWRIGHT_BROWSERS_PATH"), "/opt/pw-browsers",
             str(pathlib.Path.home() / ".cache" / "ms-playwright")]
    for root in [r for r in roots if r]:
        for pattern in ("chromium-*/chrome-linux/chrome", "chromium/chrome-linux/chrome",
                        "chromium_headless_shell-*/chrome-linux/headless_shell"):
            for path in sorted(pathlib.Path(root).glob(pattern)):
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


def judge(page, el, label):
    """Click or move one control and say whether the page changed: 'live', 'dead' or 'unreachable'."""
    try:
        inside_modal = el.evaluate("e => !!e.closest('dialog[open]')")
    except Exception:
        inside_modal = False
    if not inside_modal:
        page.evaluate(SHUT_MODALS)
    before = page.evaluate(SIGNATURE)
    try:
        moved = el.evaluate(NUDGE)
        if not moved:
            el.click(timeout=1500)
    except Exception:
        return "unreachable"
    return "live" if page.evaluate(SIGNATURE) != before else "dead"


def label_of(el, i):
    try:
        return (el.inner_text(timeout=800) or el.get_attribute("id")
                or el.get_attribute("aria-label") or f"control {i + 1}")[:34]
    except Exception:
        return f"control {i + 1}"


TAG_NEW = """(scope) => {
  const root = scope ? document.querySelector(scope) : document;
  let n = 0;
  for (const e of root.querySelectorAll(%s)) {
    if (!e.hasAttribute('data-sweep-id')) { e.setAttribute('data-sweep-id', 's' + (window.__sweepSeq = (window.__sweepSeq || 0) + 1)); n++; }
  }
  return n;
}""" % repr(CONTROLS)


def walk_scope(page, scope, route, errors):
    """Sweep every control inside one scope, opening each of its tabs, until a pass adds nothing."""
    swept, dead, unreachable = set(), [], []
    hidden_ids = set()
    for _ in range(4):
        page.evaluate(TAG_NEW, scope)
        tabs = page.locator(f"{scope} [role=tab]")
        tab_count = tabs.count()
        progress = False
        for t in range(-1, tab_count):
            if route:
                page.evaluate(f"() => {{ if (location.hash !== '#{route}') location.hash = '{route}'; }}")
            if t >= 0:
                try:
                    if tabs.nth(t).is_visible():
                        tabs.nth(t).click(timeout=1500)
                except Exception:
                    pass
                page.evaluate(TAG_NEW, scope)
            controls = page.locator(f"{scope} [data-sweep-id]")
            for i in range(controls.count()):
                el = controls.nth(i)
                try:
                    sid = el.get_attribute("data-sweep-id")
                except Exception:
                    continue
                if sid in swept:
                    continue
                if route:
                    page.evaluate(f"() => {{ if (location.hash !== '#{route}') location.hash = '{route}'; }}")
                try:
                    visible = el.is_visible()
                except Exception:
                    visible = False
                if not visible:
                    hidden_ids.add(sid)
                    continue
                label = label_of(el, i)
                verdict = judge(page, el, label)
                swept.add(sid)
                hidden_ids.discard(sid)
                progress = True
                if verdict == "dead":
                    dead.append(label)
                elif verdict == "unreachable":
                    unreachable.append(label)
        if not progress:
            break
    return len(swept), dead, unreachable, len(hidden_ids - swept)


def walk_kit(page, path, errors):
    """The route walk for a Week 5 kit page: the shell once, then every route, one line each."""
    fails = 0
    routes = page.evaluate("() => Array.from(document.querySelectorAll('section[data-route]')).map(s => s.getAttribute('data-route'))")
    totals = [0, 0, 0]
    blocks = [("shell", "[data-w5-shell]", None)] + [(f"#{r}", f"section[data-route='{r}']", r) for r in routes]
    for name, scope, route in blocks:
        start_errors = len(errors)
        if route:
            page.evaluate(f"() => {{ location.hash = '{route}'; }}")
            page.wait_for_timeout(150)
        if name == "shell":
            clicked, dead, unreachable, hidden = 0, [], [], 0
            for sc in page.evaluate("() => Array.from(document.querySelectorAll('[data-w5-shell]')).map((e, i) => (e.setAttribute('data-sweep-shell', String(i)), String(i)))"):
                c, d, u, hd = walk_scope(page, f"[data-sweep-shell='{sc}']", None, errors)
                clicked += c; dead += d; unreachable += u; hidden += hd
            page.evaluate("() => { if (window.W5 && W5.presenter) W5.presenter(false); }")
        else:
            clicked, dead, unreachable, hidden = walk_scope(page, scope, route, errors)
        covered = page.evaluate("""(scope) => {
            const out = [];
            for (const s of document.querySelectorAll(scope + ' select')) {
              if (!s.offsetParent) continue;
              s.scrollIntoView({block: 'center'});
              const r = s.getBoundingClientRect();
              const hit = document.elementFromPoint(r.left + r.width / 2, r.top + r.height / 2);
              if (!hit || (hit !== s && !s.contains(hit) && !hit.contains(s))) out.push(s.id || s.name || 'a select');
            }
            return out;
        }""", scope)
        new_errors = errors[start_errors:]
        if new_errors:
            print(f"FAIL  {path.name} {name}: {len(new_errors)} console errors, first is {new_errors[0][:110]}")
            fails += 1
        if unreachable:
            print(f"FAIL  {path.name} {name}: {len(unreachable)} controls could not be clicked at all "
                  f"({'; '.join(unreachable[:4])})")
            fails += 1
        if dead:
            print(f"FAIL  {path.name} {name}: {len(dead)} controls changed nothing on the page "
                  f"({'; '.join(dead[:4])}). Every control does something visible.")
            fails += 1
        if covered:
            print(f"FAIL  {path.name} {name}: {len(covered)} dropdowns are covered at their own "
                  f"centre point ({', '.join(covered[:4])})")
            fails += 1
        print(f"      {path.name} {name}: {clicked} controls clicked, {len(dead)} inert, "
              f"{hidden} never visible, {len(new_errors)} console errors")
        totals[0] += clicked
        totals[1] += len(dead)
        totals[2] += hidden
    print(f"      {path.name}: {len(routes)} routes walked, {totals[0]} controls clicked, {totals[1]} inert, "
          f"{totals[2]} never visible, {len(errors)} console errors")
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

            if page.locator("[data-w5-nav]").count():
                fails += walk_kit(page, path, errors)
                page.close()
                continue

            controls = page.locator(CONTROLS)
            total, dead, unreachable, hidden = controls.count(), [], [], 0
            for i in range(total):
                el = controls.nth(i)
                # A control inside a closed popup is not reachable in the page's opening state and
                # is not a defect; the popup's own controls are exercised when the popup is opened.
                try:
                    if not el.is_visible():
                        hidden += 1
                        continue
                except Exception:
                    hidden += 1
                    continue
                try:
                    label = (el.inner_text(timeout=800) or el.get_attribute("id")
                             or el.get_attribute("aria-label") or f"control {i + 1}")[:34]
                except Exception:
                    label = f"control {i + 1}"
                # A modal left open by the previous click would make everything behind it
                # unclickable, so the sweep dismisses one before judging the next control, unless
                # the next control is the modal's own close button.
                try:
                    inside_modal = el.evaluate("e => !!e.closest('dialog[open]')")
                except Exception:
                    inside_modal = False
                if not inside_modal:
                    page.evaluate(SHUT_MODALS)
                before = page.evaluate(SIGNATURE)
                try:
                    # Clicking a number, range or text field changes nothing on any page, so a
                    # field is exercised by moving it rather than by clicking it.
                    moved = el.evaluate(NUDGE)
                    if not moved:
                        el.click(timeout=1500)
                except Exception:
                    unreachable.append(label)
                    continue
                after = page.evaluate(SIGNATURE)
                if before == after:
                    dead.append(label)

            # A dropdown can be present, enabled and still unusable because something sits over it.
            # Each dropdown is scrolled into view first, because elementFromPoint reads viewport
            # coordinates and would call every control below the fold covered.
            covered = page.evaluate("""() => {
                const out = [];
                for (const s of document.querySelectorAll('select')) {
                  s.scrollIntoView({block: 'center'});
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
            print(f"      {path.name}: {total - hidden} controls clicked, {len(dead)} inert, "
                  f"{hidden} not visible in the opening state, {len(errors)} console errors")
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
    fails = None
    if sync_playwright:
        try:
            fails = sweep(paths, sync_playwright, exe)
        except Exception as e:
            print(f"INFO  the browser would not start ({str(e).splitlines()[0][:120]})")
    if fails is None:
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
# scripts/html_sweep.py scripts/companion/demo/w5kit_demo_INTERNAL.html
#     A Week 5 kit page: one line for the shell and one per route (#story, #map, #p1 and so on),
#     each with the controls clicked, the inert ones and the console errors, every tab of a route
#     opened in turn, then a line of totals. Exit 0 on clean.
# A kit page whose route has a button that does nothing
#     One FAIL line naming that route and the button, and exit 1.
# The same command with no playwright and --no-install
#     A static scan, an INFO line saying the interactive sweep did not run, and exit 0 unless the
#     static scan itself found browser storage or an orphaned control id.

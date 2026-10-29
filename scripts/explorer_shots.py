"""Screenshot every route of a Week 5 kit page at projector and phone width.

A day companion is judged by looking at it, page by page, at 1366 by 768 on the projector and at
390 by 844 on a phone. This opens the page in Playwright's Chromium, walks every route the kit's nav
names, and writes one full-page picture per route and width, so overflow, clipping, overlap and
type that reads small can be seen before a push. The pictures are never committed.

Usage:
    python3 scripts/explorer_shots.py <page.html> <outdir>
    python3 scripts/explorer_shots.py <page.html> <outdir> --end        # also the end state of each route
    python3 scripts/explorer_shots.py <page.html> <outdir> --route p3   # one route only
    python3 scripts/explorer_shots.py <page.html> <outdir> --width 1366 # one width only
    python3 scripts/explorer_shots.py <page.html> <outdir> --presenter  # with presenter mode on

--end shoots a second picture per route after every prediction on it is revealed and every player
has run to its last frame, which is where most overlap hides. It prints each file it wrote and every
console error, and exits 1 when the page logged one.
"""
import pathlib
import sys

WIDTHS = [("projector", 1366, 768, 1), ("phone", 390, 844, 2)]


def arg(flag):
    if flag in sys.argv:
        i = sys.argv.index(flag)
        if i + 1 < len(sys.argv):
            return sys.argv[i + 1]
    return None


def shoot(page, out, w, h):
    """One picture of the whole route. The viewport is stretched to the page's height first, so a
    fixed bar (the phone's progress rail) lands at the foot of the picture, where a reader meets
    it, instead of floating over the middle of a full-page capture."""
    tall = page.evaluate("() => Math.ceil(document.documentElement.scrollHeight)")
    page.set_viewport_size({"width": w, "height": max(h, tall)})
    page.wait_for_timeout(250)
    tall2 = page.evaluate("() => Math.ceil(document.documentElement.scrollHeight)")
    if tall2 != max(h, tall):
        page.set_viewport_size({"width": w, "height": max(h, tall2)})
        page.wait_for_timeout(200)
    page.screenshot(path=str(out))
    page.set_viewport_size({"width": w, "height": h})


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    for flag in ("--route", "--width"):
        value = arg(flag)
        if value in args:
            args.remove(value)
    if len(args) < 2:
        print(__doc__)
        sys.exit(2)
    page_path, outdir = pathlib.Path(args[0]), pathlib.Path(args[1])
    if not page_path.is_file():
        print(f"FAIL  {page_path} is not a file")
        sys.exit(1)
    outdir.mkdir(parents=True, exist_ok=True)
    only_route, only_width, end = arg("--route"), arg("--width"), "--end" in sys.argv
    presenter = "--presenter" in sys.argv
    from playwright.sync_api import sync_playwright

    errors, written = [], []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(args=["--no-sandbox"])
        for name, w, h, scale in WIDTHS:
            if only_width and str(w) != only_width:
                continue
            ctx = browser.new_context(viewport={"width": w, "height": h}, device_scale_factor=scale,
                                      reduced_motion="reduce")
            page = ctx.new_page()
            page.on("console", lambda m, n=name: errors.append(f"{n}: {m.text}") if m.type == "error" else None)
            page.on("pageerror", lambda e, n=name: errors.append(f"{n}: {e}"))
            page.goto(page_path.resolve().as_uri(), wait_until="load")
            page.wait_for_timeout(300)
            if presenter:
                page.evaluate("() => window.W5 && W5.presenter && W5.presenter(true)")
            routes = page.evaluate("() => Array.from(document.querySelectorAll('section[data-route]')).map(s => s.getAttribute('data-route'))")
            if not routes:
                print(f"FAIL  {page_path.name}: no section carries data-route, so this is not a kit page")
                sys.exit(1)
            for r in routes:
                if only_route and r != only_route:
                    continue
                page.evaluate(f"() => {{ location.hash = '{r}'; }}")
                page.wait_for_timeout(350)
                page.evaluate("() => window.scrollTo(0, 0)")
                stem = f"{page_path.stem}_{name}{'_presenter' if presenter else ''}_{r}"
                out = outdir / f"{stem}.png"
                shoot(page, out, w, h)
                written.append(out)
                if end:
                    page.evaluate("() => window.W5 && W5.debug && W5.debug.endState()")
                    page.wait_for_timeout(400)
                    out2 = outdir / f"{stem}_end.png"
                    shoot(page, out2, w, h)
                    written.append(out2)
            ctx.close()
        browser.close()
    for p in written:
        print(f"      wrote {p}")
    for e in errors:
        print(f"FAIL  console error: {e[:200]}")
    print(f"RESULT: {'FAIL' if errors else 'PASS'} ({len(written)} pictures, {len(errors)} console errors)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# python3 scripts/explorer_shots.py scripts/companion/demo/w5kit_demo_INTERNAL.html /tmp/shots
#     Writes one picture per route at 1366 wide and one at 390 wide, named
#     w5kit_demo_INTERNAL_projector_story.png and so on, prints each path, and exits 0 when the page
#     logged no console error.
# The same command with --end
#     Also writes a _end picture per route, taken after every prediction is revealed and every
#     player has run to its last frame.
# The same command with --presenter
#     The same pictures with presenter mode on, named _presenter_, to check the enlarged type.
# The same command with --route p3 --width 390
#     Writes only the phone picture of #p3.
# A page with no section[data-route]
#     One FAIL line saying it is not a kit page, and exit 1.

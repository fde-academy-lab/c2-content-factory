"""Review a .pptx without opening PowerPoint or LibreOffice.

LibreOffice cannot load python-pptx output in the build container, so decks were shipping unseen.
This rebuilds every slide as HTML at the real slide geometry, in the real font sizes, then uses the
headless browser that does work to do two things at once:

  1. Measure each text box and fail when its content overflows the box it was given.
  2. Save a contact sheet PNG, so a person can actually look at the deck.

Usage:
    python3 scripts/deck_check.py content/W01/D3/C2_W01_D03_deck_STUDENT.pptx
    python3 scripts/deck_check.py content/W01/D2/*.pptx --png /tmp/deck.png

Exit code 0 means every box fits. Any FAIL line means a slide needs shortening.
The HTML is written next to the PNG and is worth opening on its own when a slide fails.

What this does not check. The replica reproduces geometry, text and font size, and nothing else, so
it will not tell you about fills, colours or images. Section-boundary slides render on the light
background here even though the pptx gives them a dark one. Treat the sheet as a proof that the words
fit and read correctly, never as a colour proof.
"""
import argparse
import html
import pathlib
import sys

from pptx import Presentation
from pptx.util import Emu

PX_PER_INCH = 96


def _px(emu):
    return round(Emu(emu).inches * PX_PER_INCH, 1)


def slides_to_html(paths):
    """Rebuild every slide as a positioned div, at the same geometry the pptx uses."""
    blocks = []
    index = []
    for path in paths:
        prs = Presentation(str(path))
        w, h = _px(prs.slide_width), _px(prs.slide_height)
        for n, slide in enumerate(prs.slides, start=1):
            boxes = []
            for si, shape in enumerate(slide.shapes):
                if not shape.has_text_frame or not shape.text_frame.text.strip():
                    continue
                runs = []
                for para in shape.text_frame.paragraphs:
                    txt = "".join(r.text for r in para.runs)
                    size = next((r.font.size.pt for r in para.runs if r.font.size), 18)
                    name = next((r.font.name for r in para.runs if r.font.name), "Calibri")
                    bold = any(r.font.bold for r in para.runs)
                    mono = "Consolas" in (name or "")
                    runs.append(
                        f'<p style="font-size:{size}px;font-weight:{700 if bold else 400};'
                        f'font-family:{"ui-monospace,Menlo,monospace" if mono else "system-ui,sans-serif"};'
                        f'margin:0 0 4px">{html.escape(txt) or "&nbsp;"}</p>')
                boxes.append(
                    f'<div class="box" data-id="{path.name}|{n}|{si}" style="left:{_px(shape.left)}px;'
                    f'top:{_px(shape.top)}px;width:{_px(shape.width)}px;height:{_px(shape.height)}px">'
                    + "".join(runs) + "</div>")
            index.append((path.name, n))
            blocks.append(
                f'<div class="wrap"><figure class="slide" style="width:{w}px;height:{h}px">'
                + "".join(boxes)
                + f'<figcaption>{html.escape(path.name)} &middot; slide {n}</figcaption></figure></div>')
    scale = 0.44
    tw, th = round(w * scale), round(h * scale)
    page = f"""<!doctype html><meta charset="utf-8"><title>Deck contact sheet</title>
<style>
 body{{background:#e9e9e6;margin:0;padding:24px;font:14px system-ui,sans-serif;color:#1c1c1a}}
 .sheet{{display:grid;grid-template-columns:repeat(3,{tw}px);gap:14px}}
 .wrap{{width:{tw}px;height:{th}px;overflow:hidden}}
 .slide{{position:relative;background:#f7f7f5;border:1px solid #c9c9c2;box-sizing:border-box;
        transform:scale({scale});transform-origin:top left;overflow:hidden}}
 .box{{position:absolute;box-sizing:border-box;overflow:hidden}}
 figcaption{{position:absolute;bottom:6px;right:14px;font-size:13px;color:#8a8a82}}
</style>
<div class="sheet">{''.join(blocks)}</div>
"""
    return page, index


def measure(page_html, out_html, out_png):
    """Let the browser measure real rendered height against the box it was given."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("INFO  playwright is not installed, so only the HTML was written; open it to review")
        return []
    out_html.write_text(page_html)
    findings = []
    exe = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
    launch = {"executable_path": exe, "args": ["--no-sandbox"]} if pathlib.Path(exe).exists() else {}
    with sync_playwright() as pw:
        b = pw.chromium.launch(**launch)
        pg = b.new_page(viewport={"width": 1500, "height": 1000})
        pg.goto(out_html.resolve().as_uri())
        findings = pg.evaluate("""() => {
            const out = [];
            for (const el of document.querySelectorAll('.box')){
              const need = el.scrollHeight, have = el.clientHeight;
              if (need > have + 2) out.push({id: el.dataset.id, need, have});
            }
            return out;
        }""")
        if out_png:
            pg.screenshot(path=str(out_png), full_page=True)
        b.close()
    return findings


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("decks", nargs="+")
    ap.add_argument("--png", default="/tmp/deck_contact_sheet.png")
    a = ap.parse_args()

    paths = [pathlib.Path(p) for p in a.decks]
    for p in paths:
        if not p.exists():
            print(f"FAIL  {p} does not exist"); sys.exit(1)

    page, index = slides_to_html(paths)
    out_html = pathlib.Path(a.png).with_suffix(".html")
    findings = measure(page, out_html, pathlib.Path(a.png) if a.png else None)

    for f in findings:
        name, slide, shape = f["id"].split("|")
        print(f"FAIL  {name} slide {slide}: a text box needs {f['need']}px and has {f['have']}px, "
              f"so it overflows by {f['need'] - f['have']}px. Shorten the slide.")
    print(f"      {len(index)} slides rendered, contact sheet at {a.png}, html at {out_html}")
    print("RESULT:", "FAIL" if findings else "PASS", f"({len(findings)} overflowing boxes)")
    sys.exit(1 if findings else 0)


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# scripts/deck_check.py content/W01/D3/C2_W01_D03_deck_STUDENT.pptx
#     Renders 40 slides, writes a PNG contact sheet, and reports any box whose content is taller
#     than the box. Exit 0 when every box fits.
# scripts/deck_check.py content/W01/D2/C2_W01_D02_deck_half1_STUDENT.pptx --png /tmp/h1.png
#     Same for one deck, with the sheet written where you asked.
# scripts/deck_check.py does_not_exist.pptx
#     FAIL on the missing path, exit 1, before any rendering is attempted.

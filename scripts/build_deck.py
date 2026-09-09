"""Build a .pptx from a markdown slide source.

The markdown is the authoritative deck, because the verification gate can read it and cannot read a
pptx. This turns it into slides without leaking markdown syntax onto them: tables become real
PowerPoint tables, bold markers become bold runs, and backticks disappear.

Usage:
    python3 scripts/build_deck.py content/W01/D3/slides/C2_W01_D03_deck_STUDENT.md \
        --footer "Week 1 Day 3: profile before you touch"

Slide source format: every `## ` heading starts a slide. A heading beginning with SECTION gets the
section-boundary treatment. `---` rules are ignored.
"""
import argparse
import hashlib
import os
import pathlib
import re
import shutil
import subprocess
import tempfile

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt

INK = RGBColor(0x1C, 0x1C, 0x1A)
MUTED = RGBColor(0x5F, 0x63, 0x60)
ACC = RGBColor(0x2B, 0x4A, 0x7D)
BG = RGBColor(0xF7, 0xF7, 0xF5)
SECBG = RGBColor(0x2B, 0x4A, 0x7D)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

BOLD = re.compile(r"\*\*(.+?)\*\*")
TINT = RGBColor(0xE4, 0xEC, 0xF7)

UNITS = ["Kalpa Retail", "Kalpa Financial Services", "Kalpa Logistics",
         "Kalpa Health", "Kalpa Connect"]


def _node(s, left, top, w, h, text, fill, ink, size=13, bold=False):
    shape = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, w, h)
    shape.fill.solid(); shape.fill.fore_color.rgb = fill
    shape.line.color.rgb = ACC; shape.line.width = Pt(1.0)
    shape.shadow.inherit = False
    shape.text_frame.word_wrap = True
    para = shape.text_frame.paragraphs[0]
    para.alignment = PP_ALIGN.CENTER
    run = para.add_run()
    run.text = text; run.font.size = Pt(size); run.font.bold = bold
    run.font.name = "Calibri"; run.font.color.rgb = ink
    return shape


def _link(s, x1, y1, x2, y2):
    conn = s.shapes.add_connector(1, x1, y1, x2, y2)
    conn.line.color.rgb = ACC; conn.line.width = Pt(1.25)


def draw_units(s, after):
    """Kalpa Group and its five units, from section 2 of the locked client-zero file.

    A line after the fence that opens with a unit's name becomes that box's second line, so the
    slide's own sentences ride inside the diagram instead of being cut off under it.
    """
    said = {}
    for line in after:
        for unit in UNITS:
            if line.strip().startswith(unit):
                said[unit] = line.strip()[len(unit):].strip().rstrip(".")
    group = _node(s, Inches(0.9), Inches(3.15), Inches(3.1), Inches(1.3),
                  "Kalpa Group\nBengaluru Data and AI team", ACC, WHITE, 14, True)
    for i, unit in enumerate(UNITS):
        spine = unit == "Kalpa Retail"
        label = unit + (", the teaching spine" if spine else "")
        if unit in said:
            label += "\n" + said[unit]
        node = _node(s, Inches(5.3), Inches(1.55) + Inches(1.02) * i, Inches(5.9), Inches(0.86),
                     label, TINT if spine else WHITE, INK, 12)
        node.text_frame.paragraphs[0].runs[0].font.bold = True
        _link(s, group.left + group.width, group.top + group.height // 2,
              node.left, node.top + node.height // 2)


def draw_entities(s, after):
    """The six Kalpa Retail entities, from section 3 of the locked client-zero file."""
    boxes = {"CUSTOMERS": (0.9, 2.55), "EVENTS": (0.9, 4.3), "ORDERS": (4.4, 2.55),
             "PAYMENTS": (4.4, 4.3), "ORDER_ITEMS": (7.9, 2.55), "PRODUCTS": (7.9, 4.3)}
    drawn = {n: _node(s, Inches(x), Inches(y), Inches(2.6), Inches(0.85), n, WHITE, INK, 13, True)
             for n, (x, y) in boxes.items()}
    for a, b, label in [("CUSTOMERS", "ORDERS", "places"), ("CUSTOMERS", "EVENTS", "generates"),
                        ("ORDERS", "ORDER_ITEMS", "contains"), ("ORDERS", "PAYMENTS", "settled by"),
                        ("PRODUCTS", "ORDER_ITEMS", "appears in")]:
        one, two = drawn[a], drawn[b]
        if one.top == two.top:
            x1, y1 = one.left + one.width, one.top + one.height // 2
            x2, y2 = two.left, two.top + two.height // 2
        else:
            x1, y1 = one.left + one.width // 2, one.top + one.height
            x2, y2 = two.left + two.width // 2, two.top
        _link(s, x1, y1, x2, y2)
        cap = s.shapes.add_textbox(min(x1, x2) - Inches(0.35), (y1 + y2) // 2 - Inches(0.16),
                                   Inches(1.6), Inches(0.32))
        cap.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
        run = cap.text_frame.paragraphs[0].add_run()
        run.text = label; run.font.size = Pt(10)
        run.font.name = "Calibri"; run.font.color.rgb = MUTED


DIAGRAMS = [(("Kalpa Retail", "Kalpa Connect"), draw_units),
            (("erDiagram", "ORDER_ITEMS"), draw_entities)]


def diagram_for(lines):
    """A mermaid fence renders as nothing in PowerPoint, so the known diagrams are drawn instead."""
    joined = "\n".join(lines)
    for markers, drawer in DIAGRAMS:
        if all(marker in joined for marker in markers):
            return drawer
    return None


def parse(md):
    slides, cur = [], None
    for line in md.splitlines():
        m = re.match(r"^## (.+)$", line)
        if m:
            if cur:
                slides.append(cur)
            cur = (m.group(1).strip(), [])
        elif cur is not None and line.strip() != "---":
            cur[1].append(line)
    if cur:
        slides.append(cur)
    return slides


FENCED = ("code", "mermaid")


def split_blocks(body):
    """Split a slide body into ('text'|'code'|'mermaid'|'table', lines) blocks."""
    blocks, buf, mode = [], [], "text"
    for line in body:
        stripped = line.strip()
        if stripped.startswith("```"):
            if buf:
                blocks.append((mode, buf)); buf = []
            if mode in FENCED:
                mode = "text"
            else:
                mode = "mermaid" if stripped[3:].strip().lower() == "mermaid" else "code"
            continue
        is_row = stripped.startswith("|") and stripped.endswith("|")
        want = mode if mode in FENCED else ("table" if is_row else "text")
        if want != mode and mode not in FENCED:
            if buf:
                blocks.append((mode, buf)); buf = []
            mode = want
        buf.append(line)
    if buf:
        blocks.append((mode, buf))
    return [(m, [l for l in b if l.strip() or m in FENCED])
            for m, b in blocks if any(l.strip() for l in b)]


CACHE = pathlib.Path(tempfile.gettempdir()) / "c2_mermaid_cache"


def _chromium():
    for path in sorted(pathlib.Path("/opt/pw-browsers").glob("chromium-*/chrome-linux/chrome")):
        return str(path)
    return None


def render_mermaid(lines):
    """Render a mermaid fence to a PNG and return its path, or None when mmdc is not installed.

    A mermaid fence renders as nothing at all in PowerPoint, so a deck that draws its thinking in
    mermaid needs the picture baked in. The markdown stays the authoritative source, which is what
    the verification gate reads and what renders on GitHub. Install the renderer with
    `npm install -g @mermaid-js/mermaid-cli`; without it the fence falls back to monospace text.
    Renders are cached by content hash, so rebuilding a deck re-renders only what changed.
    """
    code = "\n".join(lines).strip() + "\n"
    key = hashlib.sha256(code.encode()).hexdigest()[:16]
    CACHE.mkdir(parents=True, exist_ok=True)
    png = CACHE / f"{key}.png"
    if png.exists():
        return png
    if not shutil.which("mmdc"):
        return None
    (CACHE / f"{key}.mmd").write_text(code)
    config = CACHE / "puppeteer.json"
    if not config.exists():
        config.write_text('{"args":["--no-sandbox","--disable-setuid-sandbox"]}\n')
    env = dict(os.environ)
    chrome = _chromium()
    if chrome:
        env["PUPPETEER_EXECUTABLE_PATH"] = chrome
    try:
        subprocess.run(["mmdc", "-i", str(CACHE / f"{key}.mmd"), "-o", str(png),
                        "-b", "transparent", "-w", "2400", "-p", str(config)],
                       capture_output=True, text=True, env=env, timeout=240)
    except Exception:
        return None
    return png if png.exists() else None


def place_picture(s, png, top, width_in=11.6):
    """Drop a rendered diagram into the body area, scaled to fit and centred."""
    from PIL import Image
    with Image.open(png) as img:
        w, h = img.size
    max_w, max_h = width_in, max(1.2, 6.55 - top)
    scale = min(max_w / (w / 96), max_h / (h / 96))
    draw_w, draw_h = (w / 96) * scale, (h / 96) * scale
    s.shapes.add_picture(str(png), Inches(0.85 + (width_in - draw_w) / 2), Inches(top),
                         Inches(draw_w), Inches(draw_h))
    return top + draw_h + 0.15


def box_height(lines, mono=False):
    """Estimate the height a text box needs, in inches, counting wrapped lines.

    Sizing by source-line count alone under-measures every paragraph that wraps, which is most of
    them at 21pt across an 11.6in box, so slides overflowed silently until deck_check.py could
    measure them. Characters per line and line height are read off that measurement: 21pt Calibri
    wraps at about 95 characters and sets on a 26px line, 17pt Consolas at about 105 on 21px.
    """
    per_line, line_px, gap_px = (105, 21, 5) if mono else (95, 26, 13)
    total = 0
    for line in lines:
        text = clean(line).rstrip()
        total += max(1, -(-len(text) // per_line)) * line_px + gap_px
    return (total + 18) / 96


def clean(text):
    """Strip the markdown that must never reach a slide."""
    return BOLD.sub(r"\1", text).replace("`", "")


def add_runs(para, text, size, colour, mono=False):
    """Write text, turning **bold** into real bold runs rather than printing the asterisks."""
    for i, piece in enumerate(BOLD.split(text.replace("`", ""))):
        if not piece:
            continue
        r = para.add_run()
        r.text = piece
        r.font.size = Pt(size)
        r.font.bold = bool(i % 2)
        r.font.color.rgb = colour
        r.font.name = "Consolas" if mono else "Calibri"


def add_bg(slide, prs, colour):
    s = slide.shapes.add_shape(1, 0, 0, prs.slide_width, prs.slide_height)
    s.fill.solid(); s.fill.fore_color.rgb = colour
    s.line.fill.background(); s.shadow.inherit = False
    slide.shapes._spTree.remove(s._element)
    slide.shapes._spTree.insert(2, s._element)


def add_table(slide, rows, top, width):
    """A markdown table becomes a PowerPoint table, never a wall of pipe characters."""
    grid = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows
            if not re.fullmatch(r"\s*\|[\s:\-|]+\|\s*", r)]
    if not grid:
        return top
    cols = max(len(r) for r in grid)
    grid = [r + [""] * (cols - len(r)) for r in grid]
    height = Inches(min(0.42 * len(grid), 4.2))
    shape = slide.shapes.add_table(len(grid), cols, Inches(0.85), Inches(top), width, height)
    for ri, row in enumerate(grid):
        for ci, cell in enumerate(row):
            tc = shape.table.cell(ri, ci)
            tc.text = ""
            para = tc.text_frame.paragraphs[0]
            add_runs(para, cell, 14 if ri else 13, INK if ri else ACC)
            if ri == 0:
                for r in para.runs:
                    r.font.bold = True
            tc.margin_top = tc.margin_bottom = Pt(2)
    return top + height.inches + 0.2


def build(src, out, footer):
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
    width = Inches(11.6)
    for title, body in parse(pathlib.Path(src).read_text()):
        section = title.upper().startswith("SECTION")
        s = prs.slides.add_slide(prs.slide_layouts[6])
        add_bg(s, prs, SECBG if section else BG)

        depth = bool(re.match(r"^D\d+[a-z]?\.", title))
        if depth:
            chip = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(11.15), Inches(0.42),
                                      Inches(1.3), Inches(0.34))
            chip.fill.solid(); chip.fill.fore_color.rgb = ACC
            chip.line.fill.background(); chip.shadow.inherit = False
            cp = chip.text_frame.paragraphs[0]; cp.alignment = PP_ALIGN.CENTER
            cr = cp.add_run(); cr.text = "DEPTH"
            cr.font.size = Pt(11); cr.font.bold = True
            cr.font.name = "Calibri"; cr.font.color.rgb = WHITE

        tb = s.shapes.add_textbox(Inches(0.85), Inches(0.7), width, Inches(1.3))
        tb.text_frame.word_wrap = True
        p0 = tb.text_frame.paragraphs[0]
        add_runs(p0, clean(re.sub(r"^[SD]\d+[a-z]?\.\s*", "", title)), 36 if section else 32,
                 WHITE if section else INK)
        for r in p0.runs:
            r.font.bold = True
        if section:
            p0.alignment = PP_ALIGN.CENTER

        blocks = split_blocks(body)
        drawer = None
        for mode, lines in blocks:
            if mode == "code":
                drawer = drawer or diagram_for(lines)
        if drawer and not section:
            lead = [l for (m, b) in blocks if m == "text" for l in b if l.strip()]
            after = []
            seen_code = False
            for mode, lines in blocks:
                if mode == "code":
                    seen_code = True
                elif seen_code:
                    after.extend(lines)
            head = [l for l in lead if l not in after]
            if head:
                cb = s.shapes.add_textbox(Inches(0.85), Inches(1.85), width, Inches(0.55))
                cb.text_frame.word_wrap = True
                add_runs(cb.text_frame.paragraphs[0], " ".join(head), 17, INK)
            drawer(s, after)
            fb = s.shapes.add_textbox(Inches(0.85), Inches(6.9), width, Inches(0.4))
            fr = fb.text_frame.paragraphs[0].add_run()
            fr.text = footer
            fr.font.size = Pt(10); fr.font.color.rgb = MUTED; fr.font.name = "Calibri"
            continue

        top = 2.15
        for mode, lines in blocks:
            if mode == "table" and not section:
                top = add_table(s, lines, top, width)
                continue
            if mode == "mermaid" and not section:
                png = render_mermaid(lines)
                if png:
                    top = place_picture(s, png, top)
                    continue
            h = max(0.55, min(4.6, box_height(lines, mono=mode == "code")))
            bb = s.shapes.add_textbox(Inches(0.85), Inches(top), width, Inches(h))
            bb.text_frame.word_wrap = True
            first = True
            for line in lines:
                para = bb.text_frame.paragraphs[0] if first else bb.text_frame.add_paragraph()
                first = False
                mono = mode == "code"
                add_runs(para, line.rstrip(), 17 if mono else 21,
                         WHITE if section else (ACC if mono else INK), mono=mono)
                if section:
                    para.alignment = PP_ALIGN.CENTER
                para.space_after = Pt(4 if mono else 10)
            top += h + 0.15
            if top > 6.6:
                break

        fb = s.shapes.add_textbox(Inches(0.85), Inches(6.9), width, Inches(0.4))
        fr = fb.text_frame.paragraphs[0].add_run()
        fr.text = footer
        fr.font.size = Pt(10); fr.font.color.rgb = MUTED; fr.font.name = "Calibri"
    prs.save(out)
    return len(prs.slides.__iter__.__self__._sldIdLst)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("source")
    ap.add_argument("--footer", default="")
    ap.add_argument("--out")
    a = ap.parse_args()
    src = pathlib.Path(a.source)
    out = pathlib.Path(a.out) if a.out else src.with_suffix(".pptx")
    n = build(src, out, a.footer or src.stem)
    print(f"{out.name}: {n} slides")


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# scripts/build_deck.py content/W01/D3/slides/C2_W01_D03_deck_STUDENT.md --footer "Week 1 Day 3"
#     Writes C2_W01_D03_deck_STUDENT.pptx with 40 slides, no pipe characters and no asterisks
#     anywhere in the slide text, and markdown tables rendered as PowerPoint tables.
# A slide whose body holds a markdown table
#     Becomes a real table with a bold header row, never lines beginning with "|".
# A slide whose title starts with SECTION
#     Gets the dark background, centred text and white type.
# A slide holding the client-zero unit map or entity mermaid fence
#     Gets boxes and connectors drawn as PowerPoint shapes, never the mermaid source as text.
# Any other mermaid fence, with mmdc installed
#     Renders to a PNG and is placed scaled and centred in the body area. Without mmdc it falls
#     back to monospace text and the build still succeeds.
# A slide titled "D12. Going deeper: ..."
#     Gets a DEPTH chip at the top right and its number stripped from the heading, which is how a
#     trainer knows at a glance to skip it live.

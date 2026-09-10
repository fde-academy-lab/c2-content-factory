import sys
import pathlib as _pl
sys.path.insert(0, str(_pl.Path(__file__).parent))

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
from pptx.util import Emu, Inches, Pt

from build_cheatsheet import MERMAID_CONFIG
from deck_layout import (ACC, BG, BOLD, INK, LINE, MUTED, TINT, WHITE, MARGIN, WIDTH,
                         BODY_TOP, BODY_BOTTOM, SLIDE_W, SLIDE_H, CALLOUT, CRUMB, NUMBERED,
                         QUOTE, SLIDE_ID, add_runs, background, breadcrumb, callout, clean,
                         code_card, footer_band, numbered, pill, quote_block, rect, table,
                         text_height, textbox, title_band, wrapped_rows)

SECBG = ACC

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

    The theme is the one scripts/build_cheatsheet.py uses, so the drawing a room sees on the slide
    is the drawing they find again on the cheat sheet and in the notebook. Without it mermaid
    paints its own lavender onto a slide that is not lavender.
    """
    code = "\n".join(lines).strip() + "\n"
    key = hashlib.sha256((code + MERMAID_CONFIG).encode()).hexdigest()[:16]
    CACHE.mkdir(parents=True, exist_ok=True)
    png = CACHE / f"{key}.png"
    if png.exists():
        return png
    if not shutil.which("mmdc"):
        return None
    (CACHE / f"{key}.mmd").write_text(code)
    theme = CACHE / f"theme_{hashlib.sha256(MERMAID_CONFIG.encode()).hexdigest()[:8]}.json"
    theme.write_text(MERMAID_CONFIG)
    config = CACHE / "puppeteer.json"
    if not config.exists():
        config.write_text('{"args":["--no-sandbox","--disable-setuid-sandbox"]}\n')
    env = dict(os.environ)
    chrome = _chromium()
    if chrome:
        env["PUPPETEER_EXECUTABLE_PATH"] = chrome
    try:
        subprocess.run(["mmdc", "-i", str(CACHE / f"{key}.mmd"), "-o", str(png),
                        "-b", "transparent", "-w", "2600", "-c", str(theme), "-p", str(config)],
                       capture_output=True, text=True, env=env, timeout=240)
    except Exception:
        return None
    return png if png.exists() else None


def place_picture(s, png, top, bottom=BODY_BOTTOM, width_in=WIDTH, centre=False):
    """Drop a rendered diagram into the body area, scaled to fill it and centred.

    The old rule scaled a diagram down to fit and never up, so a six-box chain drawn at its natural
    size sat two inches tall in the middle of a thirteen inch slide and nobody past the third row
    could read it. A diagram is the argument on these slides, so it takes the room it is given.
    """
    from PIL import Image
    with Image.open(png) as img:
        w, h = img.size
    max_w, max_h = width_in, max(1.2, bottom - top)
    scale = min(max_w / (w / 96), max_h / (h / 96))
    draw_w, draw_h = (w / 96) * scale, (h / 96) * scale
    y = top + max(0.0, (max_h - draw_h) / 2) if centre else top
    s.shapes.add_picture(str(png), Inches(MARGIN + (width_in - draw_w) / 2), Inches(y),
                         Inches(draw_w), Inches(draw_h))
    return y + draw_h + 0.16


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




def classify(lines):
    """Split a run of text lines into the shapes this deck knows how to set."""
    out, buf = [], []

    def flush():
        if buf:
            out.append(("para", list(buf)))
            buf.clear()

    nums = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        crumb = CRUMB.match(stripped)
        call = CALLOUT.match(stripped)
        num = NUMBERED.match(stripped)
        quote = QUOTE.match(stripped)
        if num:
            flush()
            nums.append((num.group(1), num.group(2)))
            continue
        if nums:
            out.append(("numbered", nums))
            nums = []
        if crumb:
            flush()
            out.append(("crumb", stripped))
        elif call:
            flush()
            out.append(("callout", (call.group(1), call.group(2))))
        elif quote:
            flush()
            out.append(("quote", [stripped]))
        else:
            buf.append(line)
    flush()
    if nums:
        out.append(("numbered", nums))
    return out


def paragraph_block(slide, top, lines, section=False, scale=1.0, width=WIDTH, x=MARGIN):
    size = round((20 if not section else 24) * scale)
    h = text_height([l.strip() for l in lines], width, size, gap=0.12)
    tb = textbox(slide, x, top, width, h)
    first = True
    for line in lines:
        p = tb.text_frame.paragraphs[0] if first else tb.text_frame.add_paragraph()
        first = False
        add_runs(p, line.strip(), size, WHITE if section else INK)
        if section:
            from pptx.enum.text import PP_ALIGN
            p.alignment = PP_ALIGN.CENTER
        p.space_after = Pt(round(9 * scale))
    return top + h + 0.14


def render_slide(slide, prs, title, body, footer, number, total, scale=1.0):
    section = title.upper().startswith("SECTION")
    depth = bool(SLIDE_ID.match(title)) and SLIDE_ID.match(title).group(1) == "D"
    background(slide, prs, ACC if section else BG)
    title_band(slide, title, section, depth)

    mark = len(slide.shapes)
    blocks = split_blocks(body)
    drawer = None
    for mode, lines in blocks:
        if mode == "code":
            drawer = drawer or diagram_for(lines)
    if drawer and not section:
        lead = [l for (m, b) in blocks if m == "text" for l in b if l.strip()]
        after, seen = [], False
        for mode, lines in blocks:
            if mode == "code":
                seen = True
            elif seen:
                after.extend(lines)
        head = [l for l in lead if l not in after]
        if head:
            tb = textbox(slide, MARGIN, BODY_TOP, WIDTH, 0.5)
            add_runs(tb.text_frame.paragraphs[0], " ".join(head), 17, INK)
        drawer(slide, after)
        footer_band(slide, footer, number, total, section)
        return

    # An exhibit slide is one whose argument is a single picture, so the picture gets the body.
    pictures = [(m, b) for m, b in blocks if m == "mermaid"]
    words = [(m, b) for m, b in blocks if m != "mermaid"]
    # A picture taller than it is wide is height-limited by the slide, so giving it the whole
    # width buys nothing: it sits narrow in the middle with its labels shrunk to match. Those go
    # beside their words instead, where they get the body's full height.
    portrait = False
    if len(pictures) == 1 and not section:
        probe = render_mermaid(pictures[0][1])
        if probe:
            from PIL import Image
            with Image.open(probe) as im:
                portrait = im.size[1] / im.size[0] > 0.55

    single_exhibit = (len(pictures) == 1 and not section and not portrait
                      and sum(len(b) for m, b in words if m == "text") <= 3
                      and all(m == "text" for m, _ in words))

    top = BODY_TOP if not section else 4.3
    if single_exhibit:
        lead = [l for m, b in words if m == "text" for l in b if l.strip()]
        tail_top = BODY_BOTTOM
        if lead:
            joined = " ".join(l.strip() for l in lead)
            tail_top = BODY_BOTTOM - min(2.4, text_height([joined], WIDTH, 20, gap=0.06))
        png = render_mermaid(pictures[0][1])
        if png:
            place_picture(slide, png, top, tail_top - 0.12, centre=True)
            if lead:
                tb = textbox(slide, MARGIN, tail_top, WIDTH, BODY_BOTTOM - tail_top)
                add_runs(tb.text_frame.paragraphs[0], " ".join(l.strip() for l in lead), 20, INK)
            footer_band(slide, footer, number, total, section)
            return

    # A portrait diagram beside its words beats the same diagram squeezed under them: stacked, it
    # only gets the height nothing else wanted, which is where a six-rank flowchart ends up
    # printing its labels at five points.
    column = None
    if portrait and not single_exhibit:
        png_probe = render_mermaid(pictures[0][1])
        column = (MARGIN + 0.47 * WIDTH, 0.53 * WIDTH)
        place_picture(slide, png_probe, BODY_TOP, BODY_BOTTOM, 0.43 * WIDTH, centre=True)

    x, w = column if column else (MARGIN, WIDTH)
    for mode, lines in blocks:
        if top > BODY_BOTTOM - 0.3:
            break
        if mode == "table" and not section:
            top = table(slide, lines, top, w, BODY_BOTTOM - top, scale, x)
        elif mode == "code":
            top = code_card(slide, top, lines, w, scale, x)
        elif mode == "mermaid" and not section:
            if column:
                continue
            png = render_mermaid(lines)
            if png:
                top = place_picture(slide, png, top, BODY_BOTTOM)
            else:
                top = code_card(slide, top, lines, w, scale, x)
        else:
            for kind, payload in classify(lines):
                if top > BODY_BOTTOM - 0.3:
                    break
                if kind == "crumb":
                    top = breadcrumb(slide, top, payload, section)
                elif kind == "callout":
                    top = callout(slide, top, payload[0], payload[1], w, section, scale, x)
                elif kind == "numbered":
                    top = numbered(slide, top, payload, w, scale, x)
                elif kind == "quote":
                    top = quote_block(slide, top, payload, w, scale, x)
                else:
                    top = paragraph_block(slide, top, payload, section, scale, w, x)
    centre_body(slide, mark, section, skip_pictures=bool(column))
    footer_band(slide, footer, number, total, section)


def centre_body(slide, mark, section=False, skip_pictures=False):
    """Slide everything placed after `mark` down, so a short body sits in the middle of its room.

    A picture already centred in its own column stays where it is, and only the words beside it
    move, otherwise the two halves drift apart.
    """
    added = [sh for sh in list(slide.shapes)[mark:]
             if not (skip_pictures and sh.shape_type is not None
                     and "PICTURE" in str(sh.shape_type))]
    if not added:
        return
    top = min(sh.top for sh in added)
    bottom = max(sh.top + sh.height for sh in added)
    slack = Inches(BODY_BOTTOM).emu - bottom
    if slack <= 0:
        return
    shift = int(slack / 2)
    if shift < Inches(0.3).emu:
        return
    for sh in added:
        sh.top = sh.top + shift


def footer_for(md, stem):
    """The running footer, read off the source rather than typed in again at every build.

    A slide source opens with its own title and the week and day it belongs to, so the footer is
    already written and a build that asks for it again is a build that can disagree with the file.
    """
    title = re.search(r"^#\s+(.+?)\s*$", md, re.M)
    where = re.search(r"^(Week\s+\d+,\s*Day\s+\d+)\b", md, re.M)
    if title and where:
        return f"{where.group(1)}. {title.group(1).strip()}"
    return title.group(1).strip() if title else stem


# Mermaid draws its labels at 16 CSS pixels. A diagram whose own width is css_w pixels, placed
# drawn_in inches wide, prints those labels at 1152 * drawn_in / css_w points, whatever
# resolution the PNG was rendered at. Below about nine points nobody past the third row reads a
# box, so a slide whose picture lands under that sets its words one step smaller and gives the
# room back to the picture.
MIN_LABEL_PT = 9.0
SCALES = (1.0, 0.86, 0.76)
CSS_WIDTHS = {}


def css_width(lines):
    """The diagram's own width in CSS pixels, which the PNG cannot tell us on its own.

    mmdc renders the deck's PNG at a fixed 2600 pixels so it stays sharp on a projector, so the
    file says nothing about how wide the drawing wanted to be. The SVG render of the same fence
    carries that in its viewBox, both renders are cached, and it is what decides whether a label
    lands readable on the slide.
    """
    key = "\n".join(lines).strip()
    if key not in CSS_WIDTHS:
        from build_cheatsheet import render_mermaid as svg_render, svg_width
        svg = svg_render(key, "svg")
        CSS_WIDTHS[key] = svg_width(svg) if svg else 0.0
    return CSS_WIDTHS[key]


def picture_label_pt(slide, mark, widths):
    """The smallest label size any picture on this slide will print at, in points."""
    worst = 99.0
    pics = [sh for sh in list(slide.shapes)[mark:]
            if sh.shape_type is not None and "PICTURE" in str(sh.shape_type)]
    for sh, css_w in zip(pics, widths):
        if css_w:
            worst = min(worst, 1152.0 * Emu(sh.width).inches / css_w)
    return worst


def clear_after(slide, mark):
    for sh in list(slide.shapes)[mark:]:
        sh._element.getparent().remove(sh._element)


def build(src, out, footer):
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(SLIDE_W), Inches(SLIDE_H)
    slides = parse(pathlib.Path(src).read_text())
    total = len(slides)
    shrunk, cramped = 0, []
    for n, (title, body) in enumerate(slides, start=1):
        s = prs.slides.add_slide(prs.slide_layouts[6])
        mark = len(s.shapes)
        widths = [css_width(b) for m, b in split_blocks(body) if m == "mermaid"]
        for i, scale in enumerate(SCALES):
            if i:
                clear_after(s, mark)
            render_slide(s, prs, title, body, footer, n, total, scale)
            pt = picture_label_pt(s, mark, widths)
            if pt >= MIN_LABEL_PT:
                shrunk += bool(i)
                break
        else:
            # Nothing the layout can do reaches a readable label, because the diagram is deeper
            # than a 16:9 slide can show. Name it, so the author can decide to draw it shallower.
            cramped.append((n, round(pt, 1), title[:44]))
    prs.save(out)
    return total, shrunk, cramped


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("source")
    ap.add_argument("--footer", default="")
    ap.add_argument("--out")
    a = ap.parse_args()
    src = pathlib.Path(a.source)
    out = pathlib.Path(a.out) if a.out else src.with_suffix(".pptx")
    n, shrunk, cramped = build(src, out, a.footer or footer_for(src.read_text(), src.stem))
    note = f", {shrunk} set smaller so their diagram stays readable" if shrunk else ""
    print(f"      {out.name}: {n} slides{note}")
    for slide, pt, title in cramped:
        print(f"      slide {slide} prints its diagram labels at {pt}pt, under the "
              f"{MIN_LABEL_PT}pt a room reads: {title}")


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# scripts/build_deck.py content/W01/D3/slides/C2_W01_D03_deck_STUDENT.md --footer "Week 1 Day 3"
#     Writes C2_W01_D03_deck_STUDENT.pptx with 87 slides, no pipe characters and no asterisks
#     anywhere in the slide text, every slide numbered in its footer.
# A slide whose body holds a markdown table
#     Becomes a table in the programme's colours, an accent header band over alternating rows.
# A slide whose only body block is one mermaid fence and a line under it
#     Becomes an exhibit: the diagram fills the body and the line sits beneath it.
# A line reading "**The claim.** ..."
#     Becomes a tinted bar with an accent edge, so the point does not look like the setup.
# A line reading "[profile] > [decide] > [find]" with one step in bold
#     Becomes a row of steps with the bold one filled, which is where the room is in the day.
# A slide titled "SECTION 2: DECIDING PER FIELD"
#     Gets the accent background, the title centred large, and its breadcrumb drawn in white.
# A slide holding the client-zero unit map or entity mermaid fence
#     Gets boxes and connectors drawn as PowerPoint shapes, never the mermaid source as text.

"""Build a .pptx from a markdown slide source.

The markdown is the authoritative deck, because the verification gate can read it and cannot read a
pptx. This turns it into slides without leaking markdown syntax onto them: tables become real
PowerPoint tables, bold markers become bold runs, and backticks disappear.

Usage:
    python3 scripts/build_deck.py content/W01/D3/slides/C2_W01_D03_deck_STUDENT.md \
        --footer "Week 1 Day 3: profile before you touch"

Slide source format: every `## ` heading starts a slide. A heading beginning with SECTION gets the
section-boundary treatment. `---` rules are ignored.

The visual system is the one in the Programme Head's orientation deck (scripts/deck_layout.py and
scripts/brand.py). What a source can ask for:

    # Title                              the deck's title, above the first slide
    Week 1, Day 1. Half one.             the day, which sets the header line and the cover pill
    Quote: Where does our growth ...     a cover slide with the client's words under the title
    Who: Meera Raghavan, CEO ...         who said them
    Kicker: / Header:                    override the cover pill / the header line
    ```notes above the first slide       the cover's speaker notes

    ## SECTION 1: The ask                a chapter opener: numeral, name, the chapter pills; the
                                         numeral is the one written, so an afternoon deck that
                                         opens on SECTION 6 prints 06, on its opener and in the
                                         cover's chapter strip
    *A CEO asks what sales are made of.* its first italic line is the chapter's promise

    ## S3. An action title               a content slide
    *One sentence that frames it.*       the subtitle under the title
    **The client asks.** ...             the three beats get their own strips: The client asks,
    **Kavya's review.** ...              Kavya's review, In the interview (and What breaks,
    **In the interview.** ...            The rule)

    ```cards        icon: users | eyebrow: Branch 1 | title: Customers | body: ... | tone: dark
    ```stats        value: 23 | label: customers | note: who bought at least once
    ```timeline     label: Beat 1 | title: The client asks | body: ...
    ```bar          label: You build | value: 30 | caption: 30 minutes
    ```notes        speaker notes, never drawn: what to say, ask and watch for
    > "No averages." Anand Iyer, ...     a quote, with the speaker set on a line of their own

Every drawing in a deck prints its labels between 9 and 18 points. The body keeps its full size for
as long as some layout places every block at that, and a picture beside its words wins over the
same picture squeezed under them when it prints larger.
Icons are Lucide names in lower case with hyphens (chart-line, shopping-cart, search-check).
"""
import sys
import pathlib as _pl
sys.path.insert(0, str(_pl.Path(__file__).parent))

import argparse
import hashlib
import math
import os
import pathlib
import re
import shutil
import subprocess
import tempfile

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.opc.constants import RELATIONSHIP_TYPE as RT
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.util import Emu, Inches, Pt

import brand
from build_cheatsheet import MERMAID_CONFIG, MermaidError, mmdc_page, mmdc_version, run_mmdc, svg_labels
from deck_layout import (ACC, BG, BOLD, INK, LINE, MUTED, NIGHT, TINT, WHITE, MARGIN, WIDTH,
                         BODY_TOP, BODY_BOTTOM, RULE_Y, SLIDE_W, SLIDE_H, CALLOUT, CRUMB, NUMBERED,
                         QUOTE, SLIDE_ID, BEATS, add_runs, background, bar, bar_height, breadcrumb,
                         callout, callout_height, cards, cards_height, clean, code_card,
                         footer_band, header, icons_in, numbered, pill, quote_block, quote_height,
                         rect,
                         section_slide, stats, stats_height, table, table_geometry, text_height,
                         textbox, timeline, timeline_height, title_band, title_slide,
                         wrapped_rows)

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
                  "Kalpa Group\nGlobal Capability Centre, Bengaluru", ACC, WHITE, 14, True)
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


COMMENT_LINE = re.compile(r"^\s*<!--.*-->\s*$")


def parse(md):
    """Split the markdown into (title, body lines) slides at each `## ` heading.

    A whole-line HTML comment outside a code fence, such as a sync block's opening and closing
    markers, is the source talking to itself, so it never reaches a slide; the lines between the
    markers do.
    """
    slides, cur, fenced = [], None, False
    for line in md.splitlines():
        if line.strip().startswith("```"):
            fenced = not fenced
        m = re.match(r"^## (.+)$", line)
        if m:
            if cur:
                slides.append(cur)
            cur = (m.group(1).strip(), [])
        elif cur is not None and line.strip() != "---":
            if not fenced and COMMENT_LINE.match(line):
                continue
            cur[1].append(line)
    if cur:
        slides.append(cur)
    return slides


COMPONENTS = ("cards", "stats", "timeline", "bar", "notes")
FENCED = ("code", "mermaid") + COMPONENTS


def split_blocks(body):
    """Split a slide body into ('text'|'code'|'mermaid'|'table'|component, lines) blocks."""
    blocks, buf, mode = [], [], "text"
    for line in body:
        stripped = line.strip()
        if stripped.startswith("```"):
            if buf:
                blocks.append((mode, buf)); buf = []
            if mode in FENCED:
                mode = "text"
            else:
                lang = stripped[3:].strip().lower()
                mode = lang if lang in COMPONENTS or lang == "mermaid" else "code"
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


SUBTITLE = re.compile(r"^\*(?!\*)(.+?)(?<!\*)\*$")


def slide_parts(body):
    """A slide's subtitle, its speaker notes, and the body that is drawn.

    The subtitle is the slide's first line when that line is set in italics, the one sentence
    under the title that frames the slide, as the orientation deck puts one under every title.
    Speaker notes live in a ```notes fence, which is never drawn: they carry what the trainer
    says, asks and watches for, which a learner-facing slide must not.
    """
    notes, drawn, inside = [], [], False
    for line in body:
        stripped = line.strip()
        if stripped.startswith("```notes"):
            inside = True
            continue
        if inside and stripped.startswith("```"):
            inside = False
            continue
        (notes if inside else drawn).append(line)
    subtitle = None
    for i, line in enumerate(drawn):
        if not line.strip():
            continue
        m = SUBTITLE.match(line.strip())
        if m:
            subtitle = m.group(1).strip()
            drawn = drawn[:i] + drawn[i + 1:]
        break
    return subtitle, "\n".join(l.rstrip() for l in notes).strip(), drawn


def deck_meta(md, stem):
    """The cover and chrome a deck asks for in the lines above its first slide.

    `# Title` and a `Week N, Day D.` line are what every deck already opens with. A deck that also
    carries `Quote:` gets a cover slide with that quote under its title, `Who:` names the speaker,
    `Kicker:` sets the pill over the title, and `Header:` sets the line at the top right of every
    content slide.
    """
    head = md.split("\n## ", 1)[0]
    meta = {"footer": footer_for(md, stem)}
    t = re.search(r"^#\s+(.+?)\s*$", head, re.M)
    meta["title"] = t.group(1).strip() if t else stem
    where = re.search(r"^Week\s+(\d+),\s*Day\s+(\d+)\b", head, re.M)
    for key in ("quote", "who", "kicker", "header"):
        m = re.search(rf"^{key}:\s*(.+?)\s*$", head, re.M | re.I)
        if m:
            meta[key] = m.group(1).strip().strip('"').strip("“”")
    if where and "header" not in meta:
        meta["header"] = f"WEEK {where.group(1)}  ·  DAY {where.group(2)}  ·  " \
                         f"KALPA GLOBAL CAPABILITY CENTRE"
    if where and "kicker" not in meta:
        meta["kicker"] = f"WEEK {where.group(1)}  ·  DAY {where.group(2)}"
    notes = re.search(r"^```notes\s*$(.*?)^```\s*$", head, re.M | re.S)
    if notes:
        meta["cover_notes"] = notes.group(1).strip()
    meta["cover"] = "quote" in meta
    return meta


SECTION_TITLE = re.compile(r"^SECTION\s*(\d+)?\s*[:.]?\s*(.*)$", re.I)


def chapter_name(title):
    """`SECTION 2: DECIDING PER FIELD` becomes `Deciding per field` for the pills and footer.

    A letter or number the author put before the name (`SECTION A. THE NEW ASK`) is dropped,
    because the chapter opener prints its own numeral beside it.
    """
    m = SECTION_TITLE.match(title)
    name = (m.group(2) if m else title).strip()
    name = re.sub(r"^[A-Z0-9]{1,2}[.:)]\s+", "", name)
    return name[:1].upper() + name[1:].lower() if name.isupper() else name


CACHE = pathlib.Path(tempfile.gettempdir()) / "c2_mermaid_cache"

# The name every diagram picture carries, so the search, the centring and the sharpening pass
# can tell a diagram from the background, the logo and the icons that are pictures too.
MERMAID_PIC = "mermaid diagram"

# A laptop screen 2560 pixels wide shows the slide at 192 pixels to the inch, and a 1080p
# projector at 144, so 192 is sharp everywhere these decks are shown, at 44 percent of the pixels
# a 4K screen would need. mmdc saves one pixel per CSS pixel unless it is given a scale, so a
# drawing 319 pixels wide stretched across the slide showed at 27 pixels to the inch and every
# edge went soft.
RENDER_PPI = 192


def render_scale(lines, width_in=None):
    """The scale mmdc renders a fence at, so the picture holds RENDER_PPI where it is drawn.

    A picture drawn width_in inches wide gets exactly that, so a small drawing the slide blows
    up gets a large scale and a wide one a small scale. The layout search asks without a width
    and gets scale one, because it only needs the drawing's shape, and a sharper render reports
    that shape a fraction differently: 0.0007in of picture was enough to push one table into a
    smaller type size. A fence whose width cannot be measured gets three.
    """
    if width_in is None:
        return 1.0
    css_w = css_width(lines)
    if not css_w:
        return 3.0
    return max(1.0, math.ceil(RENDER_PPI * width_in / css_w * 10) / 10)


def _chromium():
    for path in sorted(pathlib.Path("/opt/pw-browsers").glob("chromium-*/chrome-linux/chrome")):
        return str(path)
    return None


def render_mermaid(lines, width_in=None):
    """Render a mermaid fence to a PNG and return its path, or raise MermaidError.

    A mermaid fence renders as nothing at all in PowerPoint, so a deck that draws its thinking in
    mermaid needs the picture baked in. The markdown stays the authoritative source, which is what
    the verification gate reads and what renders on GitHub. Install the renderer with
    `npm install -g @mermaid-js/mermaid-cli`. When it is missing or writes nothing the build
    stops, because a fence printed as text on a slide looks finished and teaches nobody.

    The theme is the one scripts/build_cheatsheet.py uses, so the drawing a room sees on the slide
    is the drawing they find again on the cheat sheet and in the notebook. Without it mermaid
    paints its own lavender onto a slide that is not lavender.

    The scale from render_scale and the mermaid-cli version are part of the cache key, so a render
    made at another scale or by another version is never picked up again. The scale alone sets the picture's pixels: at scale one a drawing 809
    CSS pixels wide came out 810 pixels wide on a 2600 pixel page. The labels go through the
    cheat sheet's svg_labels, so bold prints as bold and a > survives, as they do on the sheet.
    """
    code = svg_labels("\n".join(lines).strip()) + "\n"
    scale = render_scale(lines, width_in)
    flags, config_text = mmdc_page(2600, MERMAID_CONFIG)
    key = hashlib.sha256((code + config_text + " ".join(flags) + f"scale={scale}" + mmdc_version())
                         .encode()).hexdigest()[:16]
    CACHE.mkdir(parents=True, exist_ok=True)
    png = CACHE / f"{key}.png"
    if png.exists():
        return png
    if not shutil.which("mmdc"):
        raise MermaidError("mermaid-cli is not installed, so this deck's diagrams would print as "
                           "text. Install it with npm install -g @mermaid-js/mermaid-cli.")
    (CACHE / f"{key}.mmd").write_text(code)
    theme = CACHE / f"theme_{hashlib.sha256(config_text.encode()).hexdigest()[:8]}.json"
    theme.write_text(config_text)
    config = CACHE / "puppeteer.json"
    if not config.exists():
        config.write_text('{"args":["--no-sandbox","--disable-setuid-sandbox"]}\n')
    env = dict(os.environ)
    chrome = _chromium()
    if chrome:
        env["PUPPETEER_EXECUTABLE_PATH"] = chrome
    run_mmdc(["mmdc", "-i", str(CACHE / f"{key}.mmd"), "-o", str(png), "-b", "transparent",
              *flags, "-s", str(scale), "-c", str(theme), "-p", str(config)],
             env, png, 240)
    return png


def place_picture(s, png, top, bottom=BODY_BOTTOM, width_in=WIDTH, centre=False,
                  left=MARGIN):
    """Drop a rendered diagram into the body area, scaled to fill it and centred.

    The old rule scaled a diagram down to fit and never up, so a six-box chain drawn at its natural
    size sat two inches tall in the middle of a thirteen inch slide and nobody past the third row
    could read it. A diagram is the argument on these slides, so it takes the room it is given.
    """
    from PIL import Image
    with Image.open(png) as img:
        w, h = img.size
    # Filling the room is right for a deep drawing and wrong for a shallow one: a three-box chain
    # stretched across the slide printed its labels at 34 points, twice the body text, while the
    # tree two slides later printed at 14. Capping the label size keeps every drawing in the deck
    # at one type scale. The PNG here is always the scale-one render, so its pixels are its CSS
    # width, and a label prints at 1152 times the drawn inches over that width.
    max_w = min(width_in, MAX_LABEL_PT * w / 1152)
    max_h = max(1.2, bottom - top)
    scale = min(max_w / (w / 96), max_h / (h / 96))
    draw_w, draw_h = (w / 96) * scale, (h / 96) * scale
    y = top + max(0.0, (max_h - draw_h) / 2) if centre else top
    pic = s.shapes.add_picture(str(png), Inches(left + (width_in - draw_w) / 2), Inches(y),
                         Inches(draw_w), Inches(draw_h))
    pic.name = MERMAID_PIC
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


BODY_PT = 16


def paragraph_block(slide, top, lines, section=False, scale=1.0, width=WIDTH, x=MARGIN):
    size = round(BODY_PT * scale)
    h = text_height([l.strip() for l in lines], width, size, gap=0.12)
    tb = textbox(slide, x, top, width, h)
    first = True
    for line in lines:
        p = tb.text_frame.paragraphs[0] if first else tb.text_frame.add_paragraph()
        first = False
        add_runs(p, line.strip(), size, NIGHT)
        p.space_after = Pt(round(8 * scale))
    return top + h + 0.14


def block_height(mode, lines, width, scale, section=False):
    """Roughly how much height a block will want, used only to look ahead.

    A table is told how much room it may take and fills whatever it is given, so without this a
    nine row table swallows the body and the sentence under it never reaches the slide. The
    estimate only has to be close: when it is wrong the block is dropped, and a layout that drops
    a block never wins the search.
    """
    if mode == "table":
        geo = table_geometry(lines, width, scale, BODY_BOTTOM - BODY_TOP)
        return sum(geo[4]) + 0.28 if geo else 0.0
    if mode == "code":
        size = max(10, round(13.5 * scale))
        rows = sum(wrapped_rows(l, width - 0.6, size, mono=True) for l in lines)
        return 0.5 + (size / 72 * 1.42) * rows + 0.18
    if mode == "mermaid":
        return 1.1
    if mode == "cards":
        return cards_height(lines, width, scale)
    if mode == "stats":
        return stats_height(lines, width, scale)
    if mode == "timeline":
        return timeline_height(lines, width, scale)
    if mode == "bar":
        return bar_height(lines, width, scale)
    if mode == "notes":
        return 0.0
    total = 0.0
    for kind, payload in classify(lines):
        if kind == "crumb":
            total += 0.68
        elif kind == "callout":
            total += callout_height(payload[0], payload[1], width, scale)
        elif kind == "numbered":
            size = round(15 * scale)
            total += sum((size / 72 * 1.36) * wrapped_rows(t, width - 0.62, size) + 0.2
                         for _, t in payload) + 0.12
        elif kind == "quote":
            total += quote_height(payload, width, scale) + 0.16
        else:
            size = round(BODY_PT * scale)
            total += text_height([l.strip() for l in payload], width, size, gap=0.12) + 0.14
    return total


def render_slide(slide, prs, title, body, footer, number, total, scale=1.0, layout=None,
                 reserve=0.0, ctx=None):
    """One content slide on the light surface. Chapter openers and the cover are drawn in build."""
    ctx = ctx or {}
    section = False
    depth = bool(SLIDE_ID.match(title)) and SLIDE_ID.match(title).group(1) == "D"
    background(slide, prs, "light")
    header(slide, right=ctx.get("header"))
    title_band(slide, title, depth=depth, subtitle=ctx.get("subtitle"))

    def foot():
        footer_band(slide, footer, number, total, chapters=ctx.get("chapters"),
                    current=ctx.get("current"), slide_id=ctx.get("slide_id"))

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
        foot()
        return 0

    # An exhibit slide is one whose argument is a single picture, so the picture gets the body.
    pictures = [(m, b) for m, b in blocks if m == "mermaid"]
    words = [(m, b) for m, b in blocks if m != "mermaid"]
    # Whether a picture reads better across the slide or beside its words is arithmetic, not a
    # rule of thumb: down the page it only gets the height the words leave, and beside them it
    # gets the body's full height but under half the width. The build tries both and keeps the
    # one that prints the labels larger, so nothing here has to guess.
    one_picture = len(pictures) == 1 and not section
    single_exhibit = (one_picture and layout not in ("column",) and not reserve
                      and sum(len(b) for m, b in words if m == "text") <= 3
                      and all(m == "text" for m, _ in words))

    top = BODY_TOP if not section else 4.3
    if single_exhibit:
        lead = [l for m, b in words if m == "text" for l in b if l.strip()]
        tail_top = BODY_BOTTOM
        cap_size = round(BODY_PT * scale)
        # A caption is plain words, so it is joined and set as one line of text. Anything the
        # words classify as more than that, such as Kavya's review or a breadcrumb, keeps its own
        # shape under the picture: joined, the review printed as a sentence with a bold start and
        # lost the strip that tells the room a senior is speaking.
        shaped = [part for part in classify(lead) if part[0] != "para"]
        if shaped:
            tail_top = BODY_BOTTOM - min(2.4, block_height("text", lead, WIDTH, scale))
        elif lead:
            joined = " ".join(l.strip() for l in lead)
            tail_top = BODY_BOTTOM - min(2.4, text_height([joined], WIDTH, cap_size, gap=0.02))
        # On an exhibit the picture is the whole argument, so it starts just under the rule and
        # sits close to its caption. A quarter of an inch of politeness elsewhere is a quarter of
        # an inch off a diagram that is already as wide as the slide.
        top = RULE_Y + 0.2
        png = render_mermaid(pictures[0][1])
        if png:
            place_picture(slide, png, top, tail_top - 0.05, centre=True)
            if shaped:
                at = tail_top
                for kind, payload in classify(lead):
                    if kind == "crumb":
                        at = breadcrumb(slide, at, payload, section)
                    elif kind == "callout":
                        at = callout(slide, at, payload[0], payload[1], WIDTH, section, scale)
                    elif kind == "numbered":
                        at = numbered(slide, at, payload, WIDTH, scale)
                    elif kind == "quote":
                        at = quote_block(slide, at, payload, WIDTH, scale)
                    else:
                        at = paragraph_block(slide, at, payload, section, scale)
            elif lead:
                tb = textbox(slide, MARGIN, tail_top, WIDTH, BODY_BOTTOM - tail_top)
                add_runs(tb.text_frame.paragraphs[0], " ".join(l.strip() for l in lead),
                         cap_size, NIGHT)
            foot()
            return 0

    # A portrait diagram beside its words beats the same diagram squeezed under them: stacked, it
    # only gets the height nothing else wanted, which is where a six-rank flowchart ends up
    # printing its labels at five points.
    column = None
    if one_picture and layout == "column" and not single_exhibit:
        png_probe = render_mermaid(pictures[0][1])
        if png_probe:
            column = (MARGIN + 0.47 * WIDTH, 0.53 * WIDTH)
            place_picture(slide, png_probe, BODY_TOP, BODY_BOTTOM, 0.43 * WIDTH, centre=True)

    # A picture that comes last on a crowded slide used to get whatever height the words left,
    # which on a slide carrying a claim, a table and a second claim is almost nothing. It gets a
    # band at the foot instead, sized to what its own labels need.

    x, w = column if column else (MARGIN, WIDTH)

    # A walkthrough slide that runs code, output, a sentence, more output and a closing line is
    # two slides' worth of height and half a slide's worth of width. Running it as two columns
    # uses the width a 13.3in slide actually has, instead of dropping the last two blocks off
    # the bottom. The split falls where the two sides come out closest to even.
    # A trailing picture is not part of the two-column split. It takes a band across the foot,
    # so a slide carrying a claim, a table, a mental model and a recap picture can set its words
    # in two columns above and still give the picture the width its labels need.
    trailing = (reserve and one_picture and not column
                and blocks and blocks[-1][0] == "mermaid")
    floor = max(BODY_TOP + 1.2, BODY_BOTTOM - reserve) if trailing else BODY_BOTTOM

    split_at = None
    if layout == "twocol" and not column and not section:
        splittable = blocks[:-1] if trailing else blocks
        if len(splittable) >= 3:
            heights = [block_height(m, l, WIDTH / 2 - 0.3, scale, section) for m, l in splittable]
            running, total_h, best_gap = 0.0, sum(heights), None
            for i in range(1, len(splittable)):
                running += heights[i - 1]
                gap = abs(running - (total_h - running))
                if best_gap is None or gap < best_gap:
                    best_gap, split_at = gap, i
            w = WIDTH / 2 - 0.3
            x = MARGIN

    dropped = 0
    for bi, (mode, lines) in enumerate(blocks):
        if split_at is not None and bi == split_at:
            x, top = MARGIN + WIDTH / 2 + 0.3, BODY_TOP
        if mode == "mermaid" and column:
            # Already drawn in its own column, so it is neither placed here nor dropped.
            continue
        limit = BODY_BOTTOM if mode == "mermaid" else floor
        # A block is dropped when it does not fit, not when it merely starts late. Testing the
        # start alone let a two line claim begin above the line and finish under the footer.
        needs = 0.3 if mode == "mermaid" else block_height(mode, lines, w, scale, section)
        if top + needs > limit + 0.05:
            dropped += 1
            continue
        if mode == "table" and not section:
            after = sum(block_height(m2, l2, w, scale, section)
                        for m2, l2 in blocks[bi + 1:]
                        if not (m2 == "mermaid" and column))
            top = table(slide, lines, top, w, max(1.0, floor - top - after), scale, x)
        elif mode == "code":
            top = code_card(slide, top, lines, w, scale, x)
        elif mode == "cards":
            top = cards(slide, top, lines, w, scale, x, max_h=floor - top)
        elif mode == "stats":
            top = stats(slide, top, lines, w, scale, x)
        elif mode == "timeline":
            top = timeline(slide, top, lines, w, scale, x)
        elif mode == "bar":
            top = bar(slide, top, lines, w, scale, x)
        elif mode == "notes":
            continue
        elif mode == "mermaid" and not section:
            png = render_mermaid(lines)
            if png:
                pic_x, pic_w = (MARGIN, WIDTH) if trailing else (x, w)
                # Under two columns the picture waits for the band, since the column it would
                # follow may be the shorter one. Under one column it follows the words: the band
                # is the least room it is promised, and parking it at the band's top left a hole
                # under a short client strip with the drawing stranded at the foot.
                at = max(top, floor) if (trailing and split_at is not None) else top
                top = place_picture(slide, png, at, BODY_BOTTOM, pic_w,
                                    centre=trailing and split_at is not None, left=pic_x)
            else:
                top = code_card(slide, top, lines, w, scale, x)
        else:
            for kind, payload in classify(lines):
                if top > floor - 0.3:
                    dropped += 1
                    continue
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
    if split_at is None:
        centre_body(slide, mark, section, skip_pictures=bool(column))
    foot()
    return dropped


def centre_body(slide, mark, section=False, skip_pictures=False, bottom=BODY_BOTTOM):
    """Slide everything placed after `mark` down, so a short body sits in the middle of its room.

    A picture that holds its own place, in a column or in a band at the foot, stays where it is
    and only the words move. Those words are then centred against the picture's own edge rather
    than the bottom of the slide, because centring them against the slide walks them onto it.
    """
    added = [sh for sh in list(slide.shapes)[mark:]
             if not (skip_pictures and sh.name == MERMAID_PIC)]
    if not added:
        return
    top = min(sh.top for sh in added)
    box_bottom = max(sh.top + sh.height for sh in added)
    slack = Inches(bottom).emu - box_bottom
    if slack <= 0:
        return
    # The orientation deck sets its body directly under the subtitle, so a short body gets a
    # breath of space above it and no more; centring it in the whole room opened a gap under the
    # title that read as a missing block.
    shift = min(int(slack / 2), Inches(0.3).emu)
    if shift < Inches(0.12).emu:
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
COMFORT_LABEL_PT = 14.0
MAX_LABEL_PT = 18.0
SCALES = (1.0, 0.86, 0.76, 0.66)
CSS_WIDTHS = {}
CSS_HEIGHTS = {}


def css_height(lines):
    """The diagram's own height in CSS pixels, which is what decides the band it needs."""
    key = "\n".join(lines).strip()
    if key not in CSS_HEIGHTS:
        from build_cheatsheet import render_mermaid as svg_render, svg_size
        svg = svg_render(key, "svg")
        CSS_HEIGHTS[key] = svg_size(svg)[1] if svg else 0.0
    return CSS_HEIGHTS[key]


def css_width(lines):
    """The diagram's own width in CSS pixels, which the PNG cannot tell us on its own.

    mmdc renders the deck's PNG at the scale render_scale picks for sharpness, so the file's
    pixels say nothing about how wide the drawing wanted to be. The SVG render of the same fence
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
            if sh.name == MERMAID_PIC]
    for sh, css_w in zip(pics, widths):
        if css_w:
            worst = min(worst, 1152.0 * Emu(sh.width).inches / css_w)
    return worst


def clear_after(slide, mark):
    for sh in list(slide.shapes)[mark:]:
        sh._element.getparent().remove(sh._element)


def sharpen(slide, mark, body):
    """Swap every picture on a settled slide for a render made for the width it was drawn at.

    The layout search places each picture from its scale-one render. Once the layout is settled,
    each picture is rendered again at RENDER_PPI for its own width and swapped into the same box,
    so sharpening changes pixels and never a layout, and the deck carries the sharpness it shows
    and no more. A picture is matched to its fence by its image, never by counting, since a block
    the layout dropped would shift a count. Images nothing shows any more are dropped, so they do
    not ride along in the file.
    """
    probes = {}
    for mode, lines in split_blocks(body):
        if mode == "mermaid":
            png = render_mermaid(lines)
            if png:
                probes[hashlib.sha1(png.read_bytes()).hexdigest()] = lines
    for sh in list(slide.shapes)[mark:]:
        if sh.name != MERMAID_PIC:
            continue
        lines = probes.get(sh.image.sha1)
        png = render_mermaid(lines, Emu(sh.width).inches) if lines else None
        if png:
            _, rId = slide.part.get_or_add_image_part(str(png))
            sh._element.blipFill.blip.rEmbed = rId
    live = set(slide._element.xpath(".//a:blip/@r:embed"))
    for rId, rel in list(slide.part.rels.items()):
        if rel.reltype == RT.IMAGE and rId not in live:
            slide.part.drop_rel(rId)


def prepare_icons(slides):
    """Rasterise every icon the deck will draw, in one pass, and stop on a name Lucide lacks."""
    names = {beat[0] for beat in BEATS.values()}
    for _, body in slides:
        for mode, lines in split_blocks(slide_parts(body)[2]):
            if mode in ("cards", "timeline"):
                names.update(icons_in(lines))
    missing = brand.ensure_icons([(n, c) for n in names for c in (brand.VIOLET, brand.WHITE)])
    if missing:
        raise SystemExit(f"FAIL  unknown icon name(s): {', '.join(sorted(missing))}. Names are "
                         f"Lucide's, in lower case with hyphens, such as chart-line.")


def set_notes(slide, notes):
    if notes:
        slide.notes_slide.notes_text_frame.text = notes


def build(src, out, footer):
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(SLIDE_W), Inches(SLIDE_H)
    md = pathlib.Path(src).read_text()
    slides = parse(md)
    meta = deck_meta(md, pathlib.Path(src).stem)
    prepare_icons(slides)
    sections = [t for t, _ in slides if t.upper().startswith("SECTION")]
    chapters = [chapter_name(t) for t in sections]
    numbers = []
    for i, t in enumerate(sections):
        sec = SECTION_TITLE.match(t)
        numbers.append(int(sec.group(1)) if sec and sec.group(1) else i + 1)
    total = len(slides) + (1 if meta["cover"] else 0)
    shrunk, cramped = 0, []
    offset = 0
    if meta["cover"]:
        cover = prs.slides.add_slide(prs.slide_layouts[6])
        title_slide(cover, prs, meta, chapters, total, numbers)
        set_notes(cover, meta.get("cover_notes", ""))
        offset = 1
    current = None
    for n, (title, body) in enumerate(slides, start=1 + offset):
        s = prs.slides.add_slide(prs.slide_layouts[6])
        subtitle, notes, drawn = slide_parts(body)
        if title.upper().startswith("SECTION"):
            current = 0 if current is None else current + 1
            promise = subtitle or next((l.strip() for l in drawn if l.strip()), "")
            # The numeral is the one the author wrote, so an afternoon deck that opens on
            # chapter 6 prints 06; a SECTION with no number takes its place in the file.
            sec = SECTION_TITLE.match(title)
            number = int(sec.group(1)) if sec and sec.group(1) else current + 1
            section_slide(s, prs, number, chapter_name(title), promise, chapters, current,
                          footer, total, n)
            set_notes(s, notes)
            continue
        m = SLIDE_ID.match(title)
        ctx = {"subtitle": subtitle, "chapters": chapters or None, "current": current,
               "header": meta.get("header"),
               "slide_id": f"{m.group(1)}{m.group(2)}{m.group(3)}" if m else None}
        body = drawn
        mark = len(s.shapes)
        widths = [css_width(b) for m, b in split_blocks(body) if m == "mermaid"]
        # Three ways to give a slide's picture room: a band reserved at the foot, the words
        # running the whole width with the picture in what is left, or the picture beside the
        # words. The band is tried at four depths, because reserving what the picture wants can
        # leave the words nowhere to go. A layout that cannot place one of the slide's blocks
        # never wins, whatever it does for the picture, since a dropped block is a fact the room
        # never sees.
        plans = ([("reserve", r) for r in (2.6, 2.1, 1.7, 1.3)]
                 + [(None, 0.0), ("column", 0.0), ("twocol", 0.0)]
                 + [("twocol", r) for r in (2.6, 2.1, 1.7)])
        # The body keeps its full size for as long as any layout can place every block with a
        # readable picture, and only then steps down. At each size the first layout whose labels
        # print comfortably wins; when none does, the one printing them largest wins. Taking the
        # first merely readable layout set a four-step funnel at nine points above its question
        # when the same funnel beside the question printed at thirteen.
        best = None
        for i, scale in enumerate(SCALES):
            settled = False
            for layout, reserve in plans:
                clear_after(s, mark)
                dropped = render_slide(s, prs, title, body, footer, n, total, scale, layout,
                                       reserve, ctx)
                pt = picture_label_pt(s, mark, widths)
                cand = (dropped == 0, round(min(pt, MAX_LABEL_PT), 2), -i, layout, scale,
                        reserve)
                if best is None or cand[:3] > best[:3]:
                    best = cand
                if dropped == 0 and pt >= COMFORT_LABEL_PT:
                    settled = True
                    break
            if settled or (best[0] and best[1] >= MIN_LABEL_PT):
                break
        clear_after(s, mark)
        render_slide(s, prs, title, body, footer, n, total, best[4], best[3], best[5], ctx)
        sharpen(s, mark, body)
        set_notes(s, notes)
        shrunk += best[4] != 1.0
        if best[1] < MIN_LABEL_PT:
            # Nothing either layout can do reaches a readable label, because the diagram is
            # deeper than a 16:9 slide shows. Name it, so its author can draw it shallower.
            cramped.append((n, round(best[1], 1), title[:44]))
        if not best[0]:
            print(f"      slide {n} could not place every block: {title[:44]}")
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
# content/W02/D3/slides/C2_W02_D03_deck_STUDENT.md, slide 22, a small fence drawn across the slide
#     Its picture is 2297 pixels across the 11.83 inches it is drawn at, 194 to the inch, where the
#     render without a scale was 319 pixels, 27 to the inch.
# The same deck, slide 19, a portrait fence drawn in a column 3.79 inches wide
#     Its picture is rendered for that column, 742 pixels across.
# Any rebuilt deck, unzipped
#     Holds one image in ppt/media for each distinct picture on its slides and nothing the layout
#     search left behind.

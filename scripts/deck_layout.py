"""The visual system every slide in this programme is built from.

build_deck.py reads a markdown slide source and calls into here for the furniture, so a deck looks
the same on Monday as it does on Thursday. The system is the one in the Programme Head's academic
orientation deck (version 3): a dark indigo surface for the title and the chapter openers, a light
lavender surface for content, Georgia titles over a one-sentence subtitle, cards with an icon in a
circle, small tracked capitals for eyebrows, and a chapter breadcrumb in every footer. Colours and
assets come from scripts/brand.py, which the cheat sheets and notebooks read too.

What a slide can carry, and the shape each takes:

  A claim          `**The claim.** ...` becomes a strip with its label in the accent colour.
  A beat           `**The client asks.**`, `**Kavya's review.**` and `**In the interview.**` are
                   the three recurring beats of the Global Capability Centre frame, and each gets
                   its own icon and tone, so a room learns to spot them.
  A breadcrumb     `[a] > [b] > [c]` with one step in bold becomes a row of steps with that one
                   filled.
  A table          gets an indigo header band and lavender banding, never PowerPoint's blue.
  Code             sits in a dark window, so a room tells typed things from said things.
  Cards, stats, a timeline and a proportion bar come from their own fences in the source.

Geometry is in inches on a 13.333 by 7.5 slide: a 0.58in side margin, the header chrome at 0.22,
the title from 0.74, the subtitle at 1.30, the body from 1.84 to 6.78, and the footer at 6.98.
"""
import re

from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt

import brand


def _c(hex_colour):
    return RGBColor(*brand.rgb(hex_colour))


INK = _c(brand.INK)
NIGHT = _c(brand.NIGHT)
ACC = _c(brand.VIOLET)
ACC_DEEP = _c(brand.VIOLET_DEEP)
ACC_MID = _c(brand.VIOLET_MID)
LAV = _c(brand.LAVENDER)
MUTED = _c(brand.MUTED)
SOFT = _c(brand.SOFT)
LILAC = _c(brand.LILAC)
LINE = _c(brand.LINE)
TINT = _c(brand.TINT)
BG = _c(brand.SURFACE)
WHITE = _c(brand.WHITE)
ROSE = _c(brand.ROSE)
ROSE_TINT = _c(brand.ROSE_TINT)
PASS = _c(brand.GREEN)
PASS_TINT = _c(brand.GREEN_TINT)
FAIL = ROSE

SLIDE_W, SLIDE_H = 13.333, 7.5
MARGIN = 0.58
WIDTH = SLIDE_W - 2 * MARGIN
HEADER_TOP = 0.22
TITLE_TOP = 0.74
SUB_TOP = 1.36
RULE_Y = 1.62
BODY_TOP = 1.84
BODY_BOTTOM = 6.78
FOOTER_Y = 6.98

BOLD = re.compile(r"\*\*(.+?)\*\*")
CALLOUT = re.compile(r"^\*\*([^*]{2,40}?[.:])\*\*\s*(.*)$")
CRUMB = re.compile(r"^`?\s*(\*{0,2}\[[^\]]+\]\*{0,2}(?:\s*>\s*\*{0,2}\[[^\]]+\]\*{0,2}){1,7})\s*`?$")
STEP = re.compile(r"(\*{0,2})\[([^\]]+)\]\1")
NUMBERED = re.compile(r"^\s*(\d{1,2})[.)]\s+(.*)$")
QUOTE = re.compile(r"^>\s?(.*)$")
SLIDE_ID = re.compile(r"^([SD])(\d+)([a-z]?)\.\s*(.*)$")

# The three beats of the Global Capability Centre frame (docs/07_Client_Zero.md, section 1b), and
# the strip each one is drawn as: its icon, its eyebrow, and whether it sits on the dark surface.
BEATS = {
    "the client asks": ("message-square", "THE CLIENT ASKS", True),
    "kavya's review": ("search-check", "KAVYA'S REVIEW", False),
    "in the interview": ("mic", "IN THE INTERVIEW", False),
    "what breaks": ("bug", "WHAT BREAKS", False),
    "the rule": ("list-checks", "THE RULE", False),
}

ICONS_USED = set()


def clean(text):
    """Strip the markdown that must never reach a slide."""
    return BOLD.sub(r"\1", text).replace("`", "")


# Pixels of advance per character per point of type, taken from the widest font the slide is
# likely to be drawn with rather than the narrowest. A deck is authored where Calibri and Consolas
# do not exist and opened where they do, so the renderer substitutes something wider, and an
# estimate built on the narrow font puts a card's last line outside the card. DejaVu Sans advances
# about 0.52em and DejaVu Sans Mono 0.602em, which at 96 pixels to the inch is 0.69 and 0.80
# pixels per character per point; DejaVu Serif, standing in for Georgia, runs about 0.73.
CHAR_W = 0.69
MONO_CHAR_W = 0.80
SERIF_CHAR_W = 0.73


def wrapped_rows(text, width_in, size, mono=False, serif=False):
    """How many lines this text takes in a box that wide, at that size."""
    w = MONO_CHAR_W if mono else (SERIF_CHAR_W if serif else CHAR_W)
    per_line = max(8, int(width_in * 96 / (size * w)))
    return max(1, -(-len(clean(text)) // per_line))


def tracked_width(text, size, tracking=0, bold=True):
    """The width of one line of text in inches, letter spacing included, for sizing pills."""
    per = size * CHAR_W * (1.06 if bold else 1.0) / 96 + tracking / 100 / 72
    return len(clean(text)) * per


def text_height(lines, width_in, size, mono=False, gap=0.1):
    """The height a run of lines needs, in inches, counting the ones that wrap."""
    line_in = size / 72 * (1.32 if mono else 1.36)
    rows = sum(wrapped_rows(l, width_in, size, mono) for l in lines)
    return rows * line_in + gap * len(lines) + 0.12


def _track(run, spacing=200):
    """Letter spacing in hundredths of a point, which is how the eyebrows get their air."""
    run.font._element.set("spc", str(spacing))


def add_runs(para, text, size, colour, mono=False, bold_all=False, font=None, italic=False,
             tracking=None):
    """Write text, turning **bold** into real bold runs rather than printing the asterisks."""
    face = font or (brand.MONO_FONT if mono else brand.BODY_FONT)
    for i, piece in enumerate(BOLD.split(text.replace("`", ""))):
        if not piece:
            continue
        r = para.add_run()
        r.text = piece
        r.font.size = Pt(size)
        r.font.bold = bold_all or bool(i % 2)
        r.font.italic = italic
        r.font.color.rgb = colour
        r.font.name = face
        if tracking:
            _track(r, tracking)


def _shadow(shape, alpha=12):
    """The soft drop the orientation's cards sit on: a 6pt blur, 1.5pt down, indigo at 12 percent."""
    sppr = shape._element.spPr
    for old in sppr.findall(qn("a:effectLst")):
        sppr.remove(old)
    eff = sppr.makeelement(qn("a:effectLst"), {})
    sh = eff.makeelement(qn("a:outerShdw"), {"blurRad": "76200", "dist": "19050",
                                             "dir": "5400000", "algn": "bl",
                                             "rotWithShape": "0"})
    clr = sh.makeelement(qn("a:srgbClr"), {"val": brand.INK.lstrip("#")})
    a = clr.makeelement(qn("a:alpha"), {"val": str(alpha * 1000)})
    clr.append(a)
    sh.append(clr)
    eff.append(sh)
    sppr.append(eff)


def _alpha(shape, pct):
    """Make a solid fill translucent, which python-pptx has no call for."""
    fill = shape._element.spPr.find(qn("a:solidFill"))
    if fill is None:
        return
    clr = fill[0]
    for old in clr.findall(qn("a:alpha")):
        clr.remove(old)
    a = clr.makeelement(qn("a:alpha"), {"val": str(int(pct * 1000))})
    clr.append(a)


def rect(slide, x, y, w, h, fill=None, line=None, line_w=1.0, shape=MSO_SHAPE.RECTANGLE,
         radius=None, shadow=False, gradient=None):
    s = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    if gradient:
        s.fill.gradient()
        s.fill.gradient_angle = 90
        stops = s.fill.gradient_stops
        stops[0].color.rgb, stops[0].position = gradient[0], 0.0
        stops[1].color.rgb, stops[1].position = gradient[1], 1.0
    elif fill is None:
        s.fill.background()
    else:
        s.fill.solid()
        s.fill.fore_color.rgb = fill
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line
        s.line.width = Pt(line_w)
    if radius is not None and shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        s.adjustments[0] = radius
    if shadow:
        _shadow(s)
    else:
        s.shadow.inherit = False
    s.text_frame.word_wrap = True
    return s


def card_shape(slide, x, y, w, h, dark=False, tint=None):
    """A card: white with a hairline and the soft shadow, or indigo on a gradient when it leads."""
    if dark:
        return rect(slide, x, y, w, h, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.05,
                    shadow=True, gradient=(ACC_MID, INK))
    return rect(slide, x, y, w, h, tint or WHITE, LINE, 0.75, MSO_SHAPE.ROUNDED_RECTANGLE,
                radius=0.05, shadow=True)


def textbox(slide, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    # A text frame carries a tenth of an inch of inset on every side by default, which is height
    # the box was never measured for and is why a last line lands outside the card behind it.
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Pt(0)
    return tb


def label(slide, x, y, w, text, size, colour, bold=False, font=None, align=PP_ALIGN.LEFT,
          italic=False, tracking=None, h=None, anchor=MSO_ANCHOR.TOP):
    """One line or paragraph of text in a box sized to it."""
    rows = wrapped_rows(text, w, size, serif=(font == brand.TITLE_FONT))
    box_h = h if h is not None else rows * size / 72 * 1.3 + 0.04
    tb = textbox(slide, x, y, w, box_h, anchor)
    p = tb.text_frame.paragraphs[0]
    p.alignment = align
    add_runs(p, text, size, colour, bold_all=bold, font=font, italic=italic, tracking=tracking)
    return y + box_h


def icon(slide, name, colour_hex, x, y, size):
    """Place a rasterised Lucide icon; build_deck renders every icon a deck needs beforehand."""
    path = brand.icon_path(name, colour_hex)
    ICONS_USED.add((name, colour_hex))
    if path.exists():
        slide.shapes.add_picture(str(path), Inches(x), Inches(y), Inches(size), Inches(size))


def icon_disc(slide, name, x, y, d, dark=False, solid=False):
    """An icon in a circle: lavender with a violet glyph, or solid violet with a white one."""
    if solid or dark:
        rect(slide, x, y, d, d, ACC, shape=MSO_SHAPE.OVAL)
        icon(slide, name, brand.WHITE, x + d * 0.24, y + d * 0.24, d * 0.52)
    else:
        rect(slide, x, y, d, d, TINT, shape=MSO_SHAPE.OVAL)
        icon(slide, name, brand.VIOLET, x + d * 0.24, y + d * 0.24, d * 0.52)


# --------------------------------------------------------------------------- slide furniture
def background(slide, prs, kind):
    """The dark or the light surface, as the orientation deck paints them, sent to the back."""
    path = brand.BG_DARK if kind == "dark" else brand.BG_LIGHT
    pic = slide.shapes.add_picture(str(path), 0, 0, prs.slide_width, prs.slide_height)
    slide.shapes._spTree.remove(pic._element)
    slide.shapes._spTree.insert(2, pic._element)


def pill(slide, x, y, text, fill, ink, w=0.86, h=0.3, size=11, line=None, tracking=None):
    s = rect(slide, x, y, w, h, fill, line, 0.75, MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.5)
    s.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    s.text_frame.margin_left = s.text_frame.margin_right = Pt(2)
    s.text_frame.margin_top = s.text_frame.margin_bottom = Pt(0)
    p = s.text_frame.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = text
    r.font.size = Pt(size)
    r.font.bold = True
    r.font.name = brand.BODY_FONT
    r.font.color.rgb = ink
    if tracking:
        _track(r, tracking)
    return s


def header(slide, dark=False, right=None):
    """The institute's mark and name at the top left, and the programme or the day at the right."""
    slide.shapes.add_picture(str(brand.LOGO), Inches(MARGIN), Inches(HEADER_TOP), Inches(0.46),
                             Inches(0.46))
    ink = WHITE if dark else INK
    sub = LILAC if dark else MUTED
    label(slide, MARGIN + 0.56, HEADER_TOP + 0.03, 5.6, brand.INSTITUTE, 9, ink, bold=True)
    label(slide, MARGIN + 0.56, HEADER_TOP + 0.24, 6.4, brand.ADMIN_LINE, 5.5, sub, bold=True,
          tracking=300)
    label(slide, SLIDE_W - MARGIN - 6.2, HEADER_TOP + 0.12, 6.2, right or brand.PROGRAMME_LINE, 5.5,
          sub, bold=True, align=PP_ALIGN.RIGHT, tracking=300)


def title_band(slide, title, section=False, depth=False, subtitle=None):
    """The slide's title in Georgia and the one sentence that frames it."""
    m = SLIDE_ID.match(title)
    words = m.group(4) if m else title
    text = clean(words)
    box_w = WIDTH - (1.2 if depth else 0)
    size = 26
    while size > 20 and wrapped_rows(text, box_w, size, serif=True) > 1:
        size -= 2
    label(slide, MARGIN, TITLE_TOP, box_w, text, size, INK, font=brand.TITLE_FONT, h=0.56,
          anchor=MSO_ANCHOR.BOTTOM)
    if depth:
        pill(slide, SLIDE_W - MARGIN - 1.05, TITLE_TOP + 0.16, "DEPTH", INK, WHITE, w=1.05, h=0.28,
             size=8, tracking=200)
    if subtitle:
        sub = clean(subtitle)
        s_size = 12 if wrapped_rows(sub, WIDTH, 12) == 1 else 11
        label(slide, MARGIN, SUB_TOP, WIDTH, sub, s_size, MUTED)


def footer_band(slide, footer, number, total, section=False, chapters=None, current=None,
                slide_id=None):
    """The chapter breadcrumb, with the current chapter lit, and the slide's number."""
    ink = LILAC if section else MUTED
    if chapters:
        x = MARGIN
        for i, name in enumerate(chapters):
            here = i == current
            dot = LAV if (section and here) else (ACC if here else (SOFT if section else LILAC))
            rect(slide, x, FOOTER_Y + 0.12, 0.07, 0.07, dot, shape=MSO_SHAPE.OVAL)
            colour = (WHITE if section else ACC) if here else ink
            w = min(2.4, 0.2 + len(name) * 7 * CHAR_W / 96 + 0.1)
            label(slide, x + 0.12, FOOTER_Y + 0.06, w, name, 7, colour, bold=here)
            x += w + 0.22
    else:
        label(slide, MARGIN, FOOTER_Y + 0.06, WIDTH - 1.6, footer, 7.5, ink)
    right = f"{slide_id}  \u00b7  {number} / {total}" if slide_id else f"{number} / {total}"
    label(slide, SLIDE_W - MARGIN - 1.6, FOOTER_Y + 0.06, 1.6, right, 7.5, ink,
          align=PP_ALIGN.RIGHT)


def section_slide(slide, prs, number, title, promise, chapters, current, footer, total, index):
    """A chapter opener: the big numeral, the chapter's name, its promise, and where it sits."""
    background(slide, prs, "dark")
    header(slide, dark=True)
    label(slide, MARGIN + 0.22, 1.25, 4.0, f"{number:02d}", 96, LAV, font=brand.TITLE_FONT, h=1.5)
    label(slide, MARGIN + 0.22, 2.85, WIDTH - 0.5, clean(title), 40, WHITE, font=brand.TITLE_FONT,
          h=0.8)
    if promise:
        label(slide, MARGIN + 0.22, 3.85, 10.4, clean(promise), 15, _c("#E4E1F1"))
    if chapters:
        x, y = MARGIN + 0.22, 5.55
        gap = 0.12
        widths = [min(2.35, 0.36 + len(c) * 8.5 * CHAR_W / 96) for c in chapters]
        scale = min(1.0, (WIDTH - 0.3 - gap * (len(chapters) - 1)) / sum(widths))
        for i, (c, w) in enumerate(zip(chapters, widths)):
            w *= scale
            if i == current:
                pill(slide, x, y, c, LAV, INK, w=w, h=0.34, size=8.5)
            else:
                s = pill(slide, x, y, c, None, LILAC, w=w, h=0.34, size=8.5, line=LILAC)
                s.text_frame.paragraphs[0].runs[0].font.bold = False
            x += w + gap
    footer_band(slide, footer, index, total, section=True)


def title_slide(slide, prs, meta, chapters, total):
    """The deck's cover: the institute, the day, the headline, and the client's words."""
    background(slide, prs, "dark")
    slide.shapes.add_picture(str(brand.LOGO), Inches(MARGIN + 0.1), Inches(0.62), Inches(1.15),
                             Inches(1.15))
    label(slide, MARGIN + 1.5, 0.88, 7.5, brand.INSTITUTE, 16, WHITE, bold=True)
    label(slide, MARGIN + 1.5, 1.24, 8.5, brand.ADMIN_LINE, 7, LAV, bold=True, tracking=300)
    rect(slide, MARGIN + 0.1, 2.12, WIDTH - 0.2, 0.012, SOFT)
    y = 2.45
    if meta.get("kicker"):
        pill(slide, MARGIN + 0.1, y, meta["kicker"], None, WHITE,
             w=min(8.0, tracked_width(meta["kicker"], 9, 250) + 0.5), h=0.36, size=9, line=LILAC,
             tracking=250)
        y += 0.62
    y = label(slide, MARGIN + 0.1, y, WIDTH - 0.6, clean(meta.get("title", "")), 38, WHITE,
              font=brand.TITLE_FONT)
    if meta.get("quote"):
        y = label(slide, MARGIN + 0.1, y + 0.18, WIDTH - 1.2, "\u201c" + clean(meta["quote"]) + "\u201d",
                  19, LAV, font=brand.TITLE_FONT, italic=True)
    if meta.get("who"):
        y = label(slide, MARGIN + 0.1, y + 0.06, WIDTH - 1.2, clean(meta["who"]), 11, LILAC)
    if chapters:
        x, cy = MARGIN + 0.1, max(y + 0.35, 5.7)
        for i, c in enumerate(chapters, start=1):
            w = min(2.6, 0.62 + len(c) * 9 * CHAR_W / 96)
            if x + w > SLIDE_W - MARGIN:
                break
            label(slide, x, cy, 0.4, f"{i:02d}", 13, LAV, font=brand.TITLE_FONT)
            label(slide, x + 0.42, cy + 0.04, w - 0.42, c, 9, WHITE)
            x += w + 0.2
    footer_band(slide, meta.get("footer", ""), 1, total, section=True)


# --------------------------------------------------------------------------- body blocks
def callout(slide, top, label_text, body, width=WIDTH, dark=False, scale=1.0, x=MARGIN):
    """The line that carries the point, set apart from the line before it.

    The three beats of the Global Capability Centre frame get an icon disc and an eyebrow; the
    client's ask sits on indigo, because it is the question the whole slide answers.
    """
    key = label_text.rstrip(".:").strip().lower()
    beat = BEATS.get(key)
    size = round(15 * scale)
    if beat:
        name, eyebrow, on_dark = beat
        text_w = width - 1.25
        rows = wrapped_rows(body, text_w, size)
        h = max(0.9, 0.46 + (size / 72 * 1.36) * rows + 0.2)
        if on_dark:
            card_shape(slide, x, top, width, h, dark=True)
        else:
            card_shape(slide, x, top, width, h, tint=_c("#F7F5FD"))
        d = 0.5
        icon_disc(slide, name, x + 0.25, top + (h - d) / 2, d, solid=True)
        label(slide, x + 0.95, top + 0.16, text_w, eyebrow, 7.5, LAV if on_dark else ACC,
              bold=True, tracking=250)
        tb = textbox(slide, x + 0.95, top + 0.4, text_w, h - 0.48)
        add_runs(tb.text_frame.paragraphs[0], body, size, WHITE if on_dark else NIGHT)
        return top + h + 0.18
    text_w = width - 0.62
    lines = wrapped_rows(label_text + " " + body, text_w, size)
    h = 0.3 + (size / 72 * 1.4) * lines
    base = INK if dark else _c("#F7F5FD")
    rect(slide, x, top, width, h, base, None if dark else LINE, 0.75, MSO_SHAPE.ROUNDED_RECTANGLE,
         radius=0.08)
    rect(slide, x + 0.16, top + 0.14, 0.05, h - 0.28, LAV if dark else ACC,
         shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.5)
    tb = textbox(slide, x + 0.38, top + 0.13, text_w, h - 0.2, MSO_ANCHOR.MIDDLE)
    p = tb.text_frame.paragraphs[0]
    lr = p.add_run()
    lr.text = label_text + " "
    lr.font.size = Pt(size)
    lr.font.bold = True
    lr.font.name = brand.BODY_FONT
    lr.font.color.rgb = LAV if dark else ACC
    if body:
        add_runs(p, body, size, WHITE if dark else NIGHT)
    return top + h + 0.18


def callout_height(label_text, body, width, scale):
    key = label_text.rstrip(".:").strip().lower()
    size = round(15 * scale)
    if key in BEATS:
        rows = wrapped_rows(body, width - 1.25, size)
        return max(0.9, 0.46 + (size / 72 * 1.36) * rows + 0.2) + 0.18
    return 0.3 + (size / 72 * 1.4) * wrapped_rows(label_text + " " + body, width - 0.62, size) + 0.18


def breadcrumb(slide, top, line, section=False):
    """Where the room is in the day, drawn rather than described."""
    steps = [(bool(b), t.strip()) for b, t in STEP.findall(line)]
    if not steps:
        return top
    gap = 0.14
    w = (WIDTH - gap * (len(steps) - 1)) / len(steps)
    h = 0.46
    for i, (here, text) in enumerate(steps):
        x = MARGIN + i * (w + gap)
        if here:
            s = rect(slide, x, top, w, h, ACC, None, 0.75, MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.5)
            ink = WHITE
        else:
            s = rect(slide, x, top, w, h, WHITE if not section else None, LILAC, 0.75,
                     MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.5)
            ink = MUTED if not section else WHITE
        s.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = s.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        r = p.add_run()
        r.text = text
        r.font.size = Pt(11)
        r.font.bold = here
        r.font.name = brand.BODY_FONT
        r.font.color.rgb = ink
    return top + h + 0.22


COMMENT = re.compile(r"^\s*(#|--|//)")


def code_card(slide, top, lines, width=WIDTH, scale=1.0, x=MARGIN):
    """Typed things sit in a dark window, so a room never confuses them with said things."""
    size = max(10, round(13.5 * scale))
    rows = sum(wrapped_rows(l, width - 0.6, size, mono=True) for l in lines)
    h = 0.5 + (size / 72 * 1.42) * rows
    rect(slide, x, top, width, h, NIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.035,
         shadow=True)
    for i, dot in enumerate((ROSE, LAV, PASS)):
        rect(slide, x + 0.2 + i * 0.17, top + 0.14, 0.1, 0.1, dot, shape=MSO_SHAPE.OVAL)
    tb = textbox(slide, x + 0.3, top + 0.36, width - 0.5, h - 0.44)
    first = True
    for line in lines:
        p = tb.text_frame.paragraphs[0] if first else tb.text_frame.add_paragraph()
        first = False
        colour = SOFT if COMMENT.match(line) else _c("#E4E1F1")
        add_runs(p, line.rstrip(), size, colour, mono=True)
        p.space_after = Pt(2)
    return top + h + 0.18


def quote_block(slide, top, lines, width=WIDTH, scale=1.0, x=MARGIN):
    text = " ".join(QUOTE.sub(r"\1", l.strip()) for l in lines if l.strip())
    size = round(16 * scale)
    h = 0.2 + (size / 72 * 1.4) * wrapped_rows(text, width - 0.4, size, serif=True)
    rect(slide, x, top, 0.05, h, LAV, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.5)
    tb = textbox(slide, x + 0.28, top, width - 0.34, h)
    add_runs(tb.text_frame.paragraphs[0], text, size, INK, font=brand.TITLE_FONT, italic=True)
    return top + h + 0.16


def numbered(slide, top, items, width=WIDTH, scale=1.0, x=MARGIN):
    """A counted list gets its numerals in violet Georgia and its text on one grid."""
    size = round(15 * scale)
    for n, text in items:
        rows = wrapped_rows(text, width - 0.62, size)
        h = (size / 72 * 1.36) * rows + 0.12
        label(slide, x, top - 0.04, 0.55, f"{int(n):02d}", size + 3, ACC, font=brand.TITLE_FONT)
        tb = textbox(slide, x + 0.62, top, width - 0.62, h)
        add_runs(tb.text_frame.paragraphs[0], text, size, NIGHT)
        top += h + 0.08
    return top + 0.12


TABLE_STYLE_NONE = "{2D5ABB26-0587-4C30-8999-92F81FD0307C}"


def table_geometry(rows, width, scale, room):
    """The grid, its column widths, its type size and its row heights, or None when empty.

    table() and the lookahead that decides whether the block after a table will fit both read
    this, so the height a slide plans for is the height the table actually takes.
    """
    grid = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows
            if not re.fullmatch(r"\s*\|[\s:\-|]+\|\s*", r)]
    if not grid:
        return None
    cols = max(len(r) for r in grid)
    grid = [r + [""] * (cols - len(r)) for r in grid]

    # Columns are sized by what they hold. Splitting the width evenly gives a column of counts
    # the same room as a column of sentences, so the sentences wrap four deep and the table grows
    # to twice the height it needs. Each column asks for its longest cell, no column may take
    # more than half the table, and none drops below three quarters of an inch.
    pad = 0.24
    base = max(9, round((14 if cols <= 3 else 12) * scale))
    per_char = base * CHAR_W / 96.0
    # A header is set in bold, which runs about a tenth wider, so it asks for that much more.
    want = [max(len(clean(row[ci])) * (1.12 if ri == 0 else 1.0) for ri, row in enumerate(grid))
            for ci in range(cols)]
    floor_w, ceil_w = 1.0, width * 0.5
    raw = [min(ceil_w, wcell * per_char + pad) for wcell in want]

    # Fit the wants into the width without letting any column fall under its floor. Scaling every
    # column by the same factor and then lifting the short ones back up overshoots the width, and
    # a second scaling pushes them under the floor again, which is how an order id ends up split
    # across two lines. The short columns are pinned and only the rest are scaled.
    col_ws = list(raw)
    for _ in range(cols + 1):
        pinned = [i for i, w in enumerate(col_ws) if w <= floor_w + 1e-9]
        spare = width - floor_w * len(pinned)
        rest = sum(col_ws[i] for i in range(cols) if i not in pinned)
        if rest <= 0 or spare <= 0:
            col_ws = [width / cols] * cols
            break
        col_ws = [floor_w if i in pinned else max(floor_w, col_ws[i] * spare / rest)
                  for i in range(cols)]
        if all(w >= floor_w - 1e-9 for w in col_ws) and abs(sum(col_ws) - width) < 0.01:
            break

    def measure(size):
        """A cell that wraps needs a row two lines tall, so the widest cell sets each row."""
        wrapped = [max(wrapped_rows(c, col_ws[ci] - pad, size) for ci, c in enumerate(row))
                   for row in grid]
        return [max(0.34, (size / 72 * 1.36) * n + 0.14) for n in wrapped]

    # A table is fitted by stepping its type down until the rows it really needs fit the room,
    # never by scaling the row heights. PowerPoint treats a row height as a minimum and grows the
    # row back to hold its text, so a scaled table renders taller than it was told to be and lands
    # on whatever comes after it.
    size, row_hs = base, measure(base)
    while sum(row_hs) > room and size > 9:
        size -= 1
        row_hs = measure(size)
    return grid, cols, col_ws, size, row_hs


def table(slide, rows, top, width=WIDTH, max_h=None, scale=1.0, x=MARGIN):
    """A markdown table with an indigo header band and lavender banding."""
    room = (max_h if max_h is not None else BODY_BOTTOM - top) - 0.1
    geo = table_geometry(rows, width, scale, room)
    if geo is None:
        return top
    grid, cols, col_ws, size, row_hs = geo
    height = Inches(sum(row_hs))
    shape = slide.shapes.add_table(len(grid), cols, Inches(x), Inches(top), Inches(width),
                                   height)
    tbl = shape.table
    tblPr = tbl._tbl.tblPr
    tblPr.set("firstRow", "0")
    tblPr.set("bandRow", "0")
    node = tblPr.find(qn("a:tableStyleId"))
    if node is None:
        node = tblPr.makeelement(qn("a:tableStyleId"), {})
        tblPr.append(node)
    node.text = TABLE_STYLE_NONE
    for ci, cw in enumerate(col_ws):
        tbl.columns[ci].width = Inches(cw)
    for ri, row in enumerate(grid):
        tbl.rows[ri].height = Inches(row_hs[ri])
        for ci, cell in enumerate(row):
            tc = tbl.cell(ri, ci)
            tc.text = ""
            tc.fill.solid()
            tc.fill.fore_color.rgb = INK if ri == 0 else (WHITE if ri % 2 else BG)
            tc.margin_left = tc.margin_right = Pt(8)
            tc.margin_top = tc.margin_bottom = Pt(3)
            tc.vertical_anchor = MSO_ANCHOR.MIDDLE
            para = tc.text_frame.paragraphs[0]
            add_runs(para, cell, size + (0 if ri else 0.5), WHITE if ri == 0 else NIGHT,
                     bold_all=ri == 0)
    return top + height.inches + 0.28


# --------------------------------------------------------------------------- fenced components
def parse_items(lines):
    """`key: value | key: value` per line, into one dict per line."""
    items = []
    for line in lines:
        if not line.strip():
            continue
        item = {}
        for part in line.split(" | "):
            if ":" in part:
                k, v = part.split(":", 1)
                item[k.strip().lower()] = v.strip()
        if item:
            items.append(item)
    return items


def icons_in(lines):
    """Every icon a fenced block asks for, so build_deck can render them before drawing."""
    return [i["icon"] for i in parse_items(lines) if i.get("icon")]


def _card_dims(items, width, scale, gap=0.2):
    n = max(1, len(items))
    w = (width - gap * (n - 1)) / n
    tsize, bsize = round(14 * scale), round(11 * scale)
    need = 0.0
    for it in items:
        h = 0.26
        if it.get("icon"):
            h += 0.62
        if it.get("eyebrow"):
            h += 0.26
        if it.get("title"):
            h += wrapped_rows(it["title"], w - 0.44, tsize) * tsize / 72 * 1.3 + 0.08
        if it.get("body"):
            h += wrapped_rows(it["body"], w - 0.44, bsize) * bsize / 72 * 1.36 + 0.06
        need = max(need, h + 0.2)
    return n, w, tsize, bsize, need


def cards_height(lines, width, scale):
    items = parse_items(lines)
    return _card_dims(items, width, scale)[4] + 0.2 if items else 0.0


def cards(slide, top, lines, width=WIDTH, scale=1.0, x=MARGIN, max_h=None):
    """A row of cards: an icon in a circle, a tracked eyebrow, a bold title and a line of body.

    A card marked `tone: dark` leads its row on the indigo gradient; `num: 01` sets a ghost
    numeral in the top corner, as the orientation deck numbers its phases.
    """
    items = parse_items(lines)
    if not items:
        return top
    gap = 0.2
    n, w, tsize, bsize, need = _card_dims(items, width, scale, gap)
    h = min(need, max_h) if max_h else need
    for i, it in enumerate(items):
        cx = x + i * (w + gap)
        dark = it.get("tone") == "dark"
        card_shape(slide, cx, top, w, h, dark=dark)
        y = top + 0.22
        if it.get("num"):
            label(slide, cx + w - 0.95, top + 0.14, 0.8, it["num"], 24, LILAC if not dark else ACC,
                  font=brand.TITLE_FONT, align=PP_ALIGN.RIGHT)
        if it.get("icon"):
            icon_disc(slide, it["icon"], cx + 0.22, y, 0.5, dark=dark, solid=dark)
            y += 0.62
        if it.get("eyebrow"):
            label(slide, cx + 0.22, y, w - 0.44, it["eyebrow"].upper(), 7.5, LAV if dark else ACC,
                  bold=True, tracking=250)
            y += 0.26
        if it.get("title"):
            y = label(slide, cx + 0.22, y, w - 0.44, it["title"], tsize, WHITE if dark else INK,
                      bold=True) + 0.08
        if it.get("body"):
            label(slide, cx + 0.22, y, w - 0.44, it["body"], bsize, LILAC if dark else MUTED)
    return top + h + 0.2


def stats_height(lines, width, scale):
    return 1.35 * scale + 0.25 if parse_items(lines) else 0.0


def stats(slide, top, lines, width=WIDTH, scale=1.0, x=MARGIN):
    """Big numbers with a tracked label and a hairline, the orientation's seven-numbers slide."""
    items = parse_items(lines)
    if not items:
        return top
    gap = 0.3
    n = len(items)
    w = (width - gap * (n - 1)) / n
    vsize = round((44 if n <= 4 else 36) * scale)
    longest = max(len(it.get("value", "")) for it in items)
    while vsize > 20 and longest * vsize * SERIF_CHAR_W / 96 > w - 0.1:
        vsize -= 2
    for i, it in enumerate(items):
        cx = x + i * (w + gap)
        label(slide, cx, top, w, it.get("value", ""), vsize, ACC, font=brand.TITLE_FONT,
              h=vsize / 72 * 1.25)
        y = top + vsize / 72 * 1.25 + 0.04
        label(slide, cx, y, w, it.get("label", "").upper(), 8, INK, bold=True, tracking=250)
        if it.get("note"):
            label(slide, cx, y + 0.22, w, it["note"], 9.5, MUTED)
        rect(slide, cx, top + 1.3 * scale, w, 0.012, LINE)
    return top + 1.35 * scale + 0.25


def timeline_height(lines, width, scale):
    items = parse_items(lines)
    if not items:
        return 0.0
    n = len(items)
    w = (width - 0.2 * (n - 1)) / n
    rows = max(wrapped_rows(it.get("body", ""), w - 0.36, round(10.5 * scale)) for it in items)
    return 0.95 + 0.45 + rows * 10.5 * scale / 72 * 1.36 + 0.5


def timeline(slide, top, lines, width=WIDTH, scale=1.0, x=MARGIN):
    """Dots on a line with a card under each: a sequence the room can see the length of."""
    items = parse_items(lines)
    if not items:
        return top
    gap = 0.2
    n = len(items)
    w = (width - gap * (n - 1)) / n
    line_y = top + 0.52
    rect(slide, x + w / 2, line_y + 0.1, width - w, 0.02, LILAC)
    bsize = round(10.5 * scale)
    rows = max(wrapped_rows(it.get("body", ""), w - 0.36, bsize) for it in items)
    card_h = 0.5 + rows * bsize / 72 * 1.36 + 0.3
    for i, it in enumerate(items):
        cx = x + i * (w + gap)
        label(slide, cx, top, w, it.get("label", "").upper(), 8, ACC, bold=True,
              align=PP_ALIGN.CENTER, tracking=250)
        last = i == n - 1 and it.get("tone") == "dark"
        rect(slide, cx + w / 2 - 0.11, line_y, 0.22, 0.22, LAV if last else ACC,
             shape=MSO_SHAPE.OVAL)
        cy = line_y + 0.45
        card_shape(slide, cx, cy, w, card_h, dark=it.get("tone") == "dark")
        dark = it.get("tone") == "dark"
        y = label(slide, cx + 0.18, cy + 0.16, w - 0.36, it.get("title", ""), round(13 * scale),
                  WHITE if dark else INK, bold=True)
        label(slide, cx + 0.18, y + 0.04, w - 0.36, it.get("body", ""), bsize,
              LILAC if dark else MUTED)
    return line_y + 0.45 + card_h + 0.2


def bar_height(lines, width, scale):
    return 1.05 if parse_items(lines) else 0.0


def bar(slide, top, lines, width=WIDTH, scale=1.0, x=MARGIN):
    """A proportion bar: each segment as wide as its share, labelled, with its caption beneath."""
    items = parse_items(lines)
    if not items:
        return top
    vals = []
    for it in items:
        try:
            vals.append(float(re.sub(r"[^\d.]", "", it.get("value", "1")) or 1))
        except ValueError:
            vals.append(1.0)
    total = sum(vals) or 1.0
    fills = [(TINT, INK), (ACC, WHITE), (INK, WHITE), (ACC_DEEP, WHITE), (LAV, INK)]
    cx = x
    for i, (it, v) in enumerate(zip(items, vals)):
        w = width * v / total
        f, ink = fills[i % len(fills)]
        s = rect(slide, cx, top, w, 0.5, f)
        s.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = s.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        add_runs(p, it.get("label", ""), 12, ink, bold_all=True)
        if it.get("caption"):
            label(slide, cx, top + 0.58, w, it["caption"], 8.5, MUTED, align=PP_ALIGN.CENTER)
        cx += w
    return top + 1.05

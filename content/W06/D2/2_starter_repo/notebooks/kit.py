"""Four small helpers the notebook calls, so its cells stay about Rohan's problem.

check(label, condition)   prints PASS or FAIL beside the label and never stops the notebook
ladder(stages, lit)       draws the eight ladder stages and lights the ones you name
flow(steps, title)        draws boxes joined by arrows, top to bottom: a timeline or a design
bars(rows, title)         draws one bar per (label, number) pair, so three bills compare at a glance

Each drawing is an SVG picture, which GitHub and VS Code both show inside a notebook.
You never need to edit this file.
"""
from html import escape

from IPython.display import SVG, display

INK, ACCENT, TINT, PALE, MUTED = "#1A0F5C", "#5B3FD6", "#EEEAFB", "#CFC9EE", "#6B6690"
SVG_NAME = "http://www.w3.org/2000/svg"  # the name every SVG picture declares (checked 29 October 2026)


def check(label, condition, detail=""):
    """Print PASS or FAIL and the label. A FAIL is a message to your group; nothing stops."""
    word = "PASS" if condition else "FAIL"
    print(f"{word}  {label}" + (f"  ({detail})" if detail and not condition else ""))


def _lines(text, width):
    """Break a label into lines of about `width` characters, at spaces."""
    lines, line = [], ""
    for word in str(text).split():
        if line and len(line) + 1 + len(word) > width:
            lines.append(line)
            line = word
        else:
            line = f"{line} {word}".strip()
    return lines + [line] if line else lines or [""]


def _box(x, y, w, h, text, lit, width_chars):
    fill, stroke, ink = (ACCENT, ACCENT, "white") if lit else (TINT, PALE, INK)
    lines = _lines(text, width_chars)
    top = y + h / 2 - (len(lines) - 1) * 9
    words = "".join(f'<tspan x="{x + w / 2}" y="{top + 18 * i + 5}">{escape(s)}</tspan>'
                    for i, s in enumerate(lines))
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}"/>'
            f'<text text-anchor="middle" font-size="14" fill="{ink}">{words}</text>')


def _show(width, height, body, title):
    head = f'<text x="10" y="22" font-size="15" font-weight="bold" fill="{INK}">{escape(title)}</text>'
    display(SVG(f'<svg xmlns="{SVG_NAME}" width="{width}" height="{height}" '
                f'font-family="Segoe UI, Roboto, sans-serif">{head if title else ""}{body}</svg>'))


def ladder(stages, lit=(), title=""):
    """Draw the stages in two rows of four, lighting the ones whose position is in `lit`."""
    w, h, gap, top = 180, 62, 14, 40
    body = "".join(_box(10 + (i % 4) * (w + gap), top + (i // 4) * (h + gap), w, h, s, i in lit, 20)
                   for i, s in enumerate(stages))
    rows = (len(stages) + 3) // 4
    _show(10 + 4 * (w + gap), top + rows * (h + gap), body, title)


def flow(steps, title=""):
    """Draw the steps top to bottom, each joined to the next by an arrow."""
    w, h, gap, top = 460, 56, 30, 40
    body = ""
    for i, step in enumerate(steps):
        y = top + i * (h + gap)
        body += _box(10, y, w, h, step, False, 52)
        if i < len(steps) - 1:
            x, y1, y2 = 10 + w / 2, y + h, y + h + gap
            body += (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2 - 6}" stroke="{ACCENT}" stroke-width="2"/>'
                     f'<path d="M{x - 6},{y2 - 8} L{x + 6},{y2 - 8} L{x},{y2} Z" fill="{ACCENT}"/>')
    _show(w + 20, top + len(steps) * (h + gap), body, title)


def bars(rows, title="", unit="cost units"):
    """Draw one horizontal bar per (label, number) pair, scaled to the largest number."""
    label_w, bar_w, h, gap, top = 170, 420, 30, 14, 40
    biggest = max(abs(value) for _, value in rows) or 1
    body = ""
    for i, (label, value) in enumerate(rows):
        y = top + i * (h + gap)
        length = bar_w * abs(value) / biggest
        body += (f'<text x="{label_w}" y="{y + 20}" text-anchor="end" font-size="14" fill="{INK}">'
                 f'{escape(str(label))}</text>'
                 f'<rect x="{label_w + 10}" y="{y}" width="{length}" height="{h}" rx="4" fill="{ACCENT}"/>'
                 f'<text x="{label_w + 16 + length}" y="{y + 20}" font-size="14" fill="{MUTED}">'
                 f'{value:,.0f} {escape(unit)}</text>')
    _show(label_w + bar_w + 160, top + len(rows) * (h + gap), body, title)

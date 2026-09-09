#!/usr/bin/env python3
"""Build a study note PDF and HTML from its markdown source.

    python3 build_notes.py path/to/content.md [--brand "#1E6B7A"] [--out DIR]

The markdown file is the source of truth. Front matter supplies the header
block; reading time is computed rather than typed, so it cannot go stale.

Front matter fields:
    title      required, the note's own title
    session    required, e.g. "Session 17"
    strand     optional, e.g. "Grounding and retrieval"
    programme  required, e.g. "Agentic AI Engineering, Cohort 3"
    promise    required, one sentence on what the reader will be able to do
    brand      optional, hex accent colour, overridden by --brand
    footer     optional, running footer text
"""

import argparse
import html
import os
import re
import sys

try:
    import markdown
except ImportError:
    sys.exit("python3 -m pip install markdown --break-system-packages")

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(HERE), "assets")

DEVICES = {
    "IN THE FIELD": "dev-field",
    "WATCH OUT": "dev-watch",
    "ORIGIN": "dev-origin",
    "CALLBACK": "dev-callback",
}

WORDS_PER_MINUTE = 220
SECONDS_PER_FIGURE = 30


def split_front_matter(text):
    if not text.lstrip().startswith("---"):
        return {}, text
    body = text.lstrip()
    end = body.find("\n---", 3)
    if end == -1:
        return {}, text
    raw = body[3:end]
    rest = body[end + 4:]
    meta = {}
    for line in raw.splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            meta[key.strip().lower()] = value.strip().strip('"').strip("'")
    return meta, rest.lstrip("\n")


def reading_time(md_text):
    stripped = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", md_text)
    stripped = re.sub(r"`{1,3}[^`]*`{1,3}", " ", stripped)
    stripped = re.sub(r"[#>*_|\-]", " ", stripped)
    words = len([w for w in stripped.split() if any(c.isalnum() for c in w)])
    figures = len(re.findall(r"!\[[^\]]*\]\([^)]*\)", md_text))
    minutes = words / WORDS_PER_MINUTE + figures * SECONDS_PER_FIGURE / 60
    return words, figures, max(1, round(minutes))


def wrap_figures(text):
    """Turn an image paragraph followed by a Figure N caption into <figure>."""
    pattern = re.compile(
        r'<p>(<img[^>]*>)</p>\s*<p><em>(Figure[^<]*)</em></p>', re.S)
    return pattern.sub(
        lambda m: '<figure>%s<figcaption>%s</figcaption></figure>'
        % (m.group(1), m.group(2)), text)


def tag_devices(text):
    def repl(match):
        inner = match.group(1)
        label = re.search(r"<strong>\s*([A-Z][A-Z ]+?)\s*</strong>", inner)
        cls = "device"
        if label:
            key = label.group(1).strip().upper()
            if key in DEVICES:
                cls = "device " + DEVICES[key]
        return '<blockquote class="%s">%s</blockquote>' % (cls, inner)

    return re.sub(r"<blockquote>(.*?)</blockquote>", repl, text, flags=re.S)


def mark_panels(text):
    """A section whose heading starts with Self-check gets the panel fill."""
    return re.sub(
        r'(<h3[^>]*>\s*Self[- ]check[^<]*</h3>)',
        r'<div class="panel-open"></div>\1', text)


def build(md_path, brand=None, out_dir=None):
    with open(md_path, encoding="utf-8") as fh:
        raw = fh.read()

    meta, body_md = split_front_matter(raw)
    for field in ("title", "session", "programme", "promise"):
        if field not in meta:
            sys.exit("front matter is missing required field: %s" % field)

    words, figures, minutes = reading_time(body_md)

    md = markdown.Markdown(extensions=[
        "tables", "attr_list", "fenced_code", "sane_lists", "footnotes", "md_in_html",
    ])
    body_html = md.convert(body_md)
    body_html = wrap_figures(body_html)
    body_html = tag_devices(body_html)
    body_html = body_html.replace("<!-- page -->", '<div class="pagebreak"></div>')

    with open(os.path.join(ASSETS, "notes.css"), encoding="utf-8") as fh:
        css = fh.read()
    accent = brand or meta.get("brand")
    if accent:
        css = css.replace("--accent: #1E6B7A;", "--accent: %s;" % accent)

    with open(os.path.join(ASSETS, "template.html"), encoding="utf-8") as fh:
        template = fh.read()

    meta_line = " · ".join(
        [v for v in (meta.get("session"), meta.get("strand"), meta.get("programme")) if v])
    stamp = "%d minute read · %d figures · %s words" % (minutes, figures, f"{words:,}")
    runfoot = meta.get("footer") or meta_line

    page = (template
            .replace("__CSS__", css)
            .replace("__TITLE__", html.escape(meta["title"]))
            .replace("__META__", html.escape(meta_line))
            .replace("__PROMISE__", html.escape(meta["promise"]))
            .replace("__STAMP__", html.escape(stamp))
            .replace("__RUNFOOT__", html.escape(runfoot))
            .replace("__BODY__", body_html))

    out_dir = out_dir or os.path.dirname(os.path.abspath(md_path))
    os.makedirs(out_dir, exist_ok=True)
    stem = os.path.splitext(os.path.basename(md_path))[0]
    html_path = os.path.join(out_dir, stem + ".html")
    pdf_path = os.path.join(out_dir, stem + ".pdf")

    with open(html_path, "w", encoding="utf-8") as fh:
        fh.write(page)

    try:
        from weasyprint import HTML
    except ImportError:
        sys.exit("pip install weasyprint --break-system-packages, then rerun")

    HTML(string=page, base_url=os.path.dirname(os.path.abspath(md_path))).write_pdf(pdf_path)

    print("words %d · figures %d · reading time %d min" % (words, figures, minutes))
    print("html  %s" % html_path)
    print("pdf   %s" % pdf_path)
    return pdf_path


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("markdown")
    ap.add_argument("--brand", default=None, help="hex accent colour, e.g. #E6007E")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    build(args.markdown, args.brand, args.out)

"""Print a markdown document (practice set, study notes, cheat sheet, question bank) to PDF.

From Week 5 on, the documents a learner reads after class are written as markdown, which GitHub
renders with its mermaid diagrams, and printed to PDF for reading offline. This renders every
mermaid fence to a PNG through the shared theme (scripts/build_cheatsheet.py), converts the
markdown to HTML with pandoc, and prints it with WeasyPrint on A4.

Usage:
    python3 scripts/build_doc.py content/W05/D1/2_take_home_mandatory/C2_W05_D01_practice_set_STUDENT.md
    python3 scripts/build_doc.py content/W05/D1          # every STUDENT markdown in folders 2 and 3

A page break is written in the markdown as <div class="page-break"></div>, which GitHub ignores.
Images are referenced relative to the markdown file, as GitHub resolves them.
"""
import pathlib
import re
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

FENCE = re.compile(r"```mermaid\s*\n(.*?)```", re.S)
PRINTED = ("2_take_home_mandatory", "3_study_material_for_students")

CSS = """
@page { size: A4; margin: 16mm 15mm 18mm 15mm;
        @bottom-center { content: counter(page) " / " counter(pages); font: 8pt Arial; color: #6B675E; } }
body { font-family: Arial, "Liberation Sans", sans-serif; font-size: 10.5pt; line-height: 1.45; color: #1C1B16; }
h1 { font-family: Georgia, serif; font-size: 20pt; color: #8A5A1F; margin: 0 0 6pt; }
h2 { font-family: Georgia, serif; font-size: 14pt; color: #8A5A1F; border-bottom: 1.2pt solid #B37A33;
     padding-bottom: 2pt; margin-top: 16pt; }
h3 { font-size: 11.5pt; margin: 12pt 0 4pt; }
h4 { font-size: 10.5pt; margin: 10pt 0 3pt; }
p, li { orphans: 2; widows: 2; }
table { border-collapse: collapse; width: 100%; margin: 6pt 0 10pt; font-size: 9.5pt; page-break-inside: avoid; }
th { background: #F3F1EA; text-align: left; }
th, td { border: 0.6pt solid #D5D0C4; padding: 3pt 5pt; vertical-align: top; }
code { font-family: Consolas, "DejaVu Sans Mono", monospace; font-size: 9pt; background: #F3F1EA; padding: 0 2pt; }
pre { background: #F3F1EA; border-left: 2.5pt solid #B37A33; padding: 6pt 8pt; font-size: 8.8pt;
      white-space: pre-wrap; page-break-inside: avoid; }
pre code { background: none; padding: 0; }
img { max-width: 100%; display: block; margin: 6pt auto; page-break-inside: avoid; }
blockquote { border-left: 2.5pt solid #D5D0C4; margin: 6pt 0; padding: 2pt 10pt; color: #3D3B33; }
.page-break { page-break-before: always; }
"""


def render_fences(text, workdir):
    """Each mermaid fence becomes an image line pointing at its PNG, rendered once and cached."""
    from build_cheatsheet import render_mermaid

    def swap(m):
        png = render_mermaid(m.group(1), "png")
        if not png:
            raise SystemExit("mermaid-cli (mmdc) is not installed, so the diagrams cannot print.")
        return f"![]({pathlib.Path(png).resolve()})\n"
    return FENCE.sub(swap, text)


def build(md_path):
    md_path = md_path.resolve()
    pdf_path = md_path.with_suffix(".pdf")
    text = md_path.read_text(encoding="utf-8")
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        body = render_fences(text, tmp)
        src = tmp / "doc.md"
        src.write_text(body, encoding="utf-8")
        css = tmp / "doc.css"
        css.write_text(CSS, encoding="utf-8")
        html = tmp / "doc.html"
        title = next((ln.lstrip("# ").strip() for ln in text.splitlines() if ln.startswith("# ")), md_path.stem)
        # Formulas are written as plain text or code spans, never LaTeX, so GitHub and the PDF
        # print the same characters; dollar signs stay literal.
        subprocess.run(["pandoc", str(src), "-f", "gfm", "-t", "html5", "--standalone",
                        "--css", str(css), "--metadata", f"title={title}",
                        "--variable", "title=", "--resource-path", str(md_path.parent),
                        "-o", str(html)], check=True)
        # pandoc's standalone page prints the title block again; the markdown's own h1 is enough.
        page = html.read_text(encoding="utf-8")
        page = re.sub(r'<header id="title-block-header">.*?</header>', "", page, flags=re.S)
        html.write_text(page, encoding="utf-8")
        from weasyprint import HTML
        HTML(filename=str(html), base_url=str(md_path.parent)).write_pdf(str(pdf_path))
    print(f"wrote {pdf_path}")
    return pdf_path


def main():
    targets = [pathlib.Path(a) for a in sys.argv[1:]]
    if not targets:
        raise SystemExit(__doc__)
    for t in targets:
        if t.is_dir():
            for md in sorted(t.rglob("*_STUDENT.md")):
                if md.parent.name in PRINTED:
                    build(md)
        else:
            build(t)


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# python3 scripts/build_doc.py some/folder/C2_W05_D01_practice_set_STUDENT.md
#     writes C2_W05_D01_practice_set_STUDENT.pdf beside it, every mermaid fence drawn as a picture.
# python3 scripts/build_doc.py content/W05/D1
#     prints every STUDENT markdown in 2_take_home_mandatory and 3_study_material_for_students.
# python3 scripts/build_doc.py
#     prints this usage text and exits.

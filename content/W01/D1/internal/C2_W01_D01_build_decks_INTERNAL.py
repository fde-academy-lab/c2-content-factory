"""Build Monday's two decks with scripts/build_deck.py, printing each chapter opener's own number.

build_deck.py prints the number written in a numeric heading, and numbers a lettered opener by its
place in the file, so `## SECTION A: ...` in the afternoon deck would print a number. Monday pairs each
deck chapter with the notebook of the same number and marks the afternoon's case blocks with letters,
so this wrapper keeps build_deck.py's whole build and changes one thing: the k-th chapter opener
prints the k-th mark written in the headings, on the opener and in the cover's list of chapters.
`## SECTION 5: ...` prints 05; `## SECTION A: ...` prints A.

Run from the repository root:
    python3 content/W01/D1/internal/C2_W01_D01_build_decks_INTERNAL.py
"""
import pathlib
import re
import sys

sys.path.insert(0, "scripts")
import build_deck  # noqa: E402
import deck_layout  # noqa: E402

SLIDES = pathlib.Path("content/W01/D1/slides")
DECKS = [("C2_W01_D01_half1_STUDENT.md", "Week 1, Monday morning: the story and chapters 1 to 4"),
         ("C2_W01_D01_half2_STUDENT.md", "Week 1, Monday afternoon: chapters 5 and 6 and the cases")]
HEADING = re.compile(r"^## SECTION\s*([0-9]+|[A-Z])\b", re.M)


def numerals(md):
    """The numeral each chapter opener prints, in order: two digits for a number, a letter as is."""
    return [f"{int(m):02d}" if m.isdigit() else m for m in HEADING.findall(md)]


def build(name, footer):
    src = SLIDES / name
    marks = numerals(src.read_text())
    original = deck_layout.section_slide
    seen = []

    def section_slide(slide, prs, number, *rest):
        original(slide, prs, number, *rest)
        want = marks[len(seen)]
        seen.append(want)
        for shape in slide.shapes:
            if shape.has_text_frame and shape.text_frame.text == f"{number:02d}":
                shape.text_frame.paragraphs[0].runs[0].text = want
                break

    cover = deck_layout.title_slide

    def title_slide(slide, prs, meta, chapters, total, *numbers):
        cover(slide, prs, meta, chapters, total, *numbers)
        k = 0
        for shape in slide.shapes:
            if shape.has_text_frame and re.fullmatch(r"\d\d", shape.text_frame.text) and k < len(marks):
                shape.text_frame.paragraphs[0].runs[0].text = marks[k]
                k += 1

    build_deck.section_slide = section_slide
    build_deck.title_slide = title_slide
    n, shrunk, cramped = build_deck.build(src, src.with_suffix(".pptx"), footer)
    build_deck.section_slide = original
    build_deck.title_slide = cover
    print(f"      {name}: {n} slides, openers numbered {', '.join(marks)}")
    for slide, pt, title in cramped:
        print(f"      slide {slide} prints its diagram labels at {pt}pt: {title}")


if __name__ == "__main__":
    for name, footer in DECKS:
        if len(sys.argv) == 1 or name in sys.argv[1:]:
            build(name, footer)

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W01/D1/internal/C2_W01_D01_build_decks_INTERNAL.py
#     Writes both decks; the morning deck's openers print 00, 01, 02, 03, 04 and the afternoon's
#     05, 06, A, B, C, D, E.
# python3 content/W01/D1/internal/C2_W01_D01_build_decks_INTERNAL.py C2_W01_D01_half2_STUDENT.md
#     Rebuilds the afternoon deck only.

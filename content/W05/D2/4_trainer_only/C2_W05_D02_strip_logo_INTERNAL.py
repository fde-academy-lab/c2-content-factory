"""Remove the institute's logo and name from a built deck, since no logo appears in any Week 5 artifact.

scripts/build_deck.py draws the shared header (the logo, the institute's name and its administering
line) on every slide, and the shared builder is not changed from a day session. This post-step
deletes those shapes from the built .pptx and leaves everything else as built.

Usage:
    python3 scripts/build_deck.py content/W05/D2/1_in_class_training_content/slides/C2_W05_D02_slides_STUDENT.md
    python3 content/W05/D2/4_trainer_only/C2_W05_D02_strip_logo_INTERNAL.py \\
        content/W05/D2/1_in_class_training_content/slides/C2_W05_D02_slides_STUDENT.pptx
"""
import hashlib
import pathlib
import sys

from pptx import Presentation

REPO = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO / "scripts"))
import brand  # noqa: E402

LOGO_HASH = hashlib.sha1(brand.LOGO.read_bytes()).hexdigest()
BRAND_TEXT = {brand.INSTITUTE.strip().lower(), brand.ADMIN_LINE.strip().lower(), brand.PROGRAMME_LINE.strip().lower()}


def strip(path):
    prs = Presentation(str(path))
    pictures = labels = 0
    for slide in prs.slides:
        for shape in list(slide.shapes):
            gone = False
            if shape.shape_type == 13:  # a picture
                try:
                    gone = hashlib.sha1(shape.image.blob).hexdigest() == LOGO_HASH
                    pictures += gone
                except Exception:
                    gone = False
            elif shape.has_text_frame and shape.text_frame.text.strip().lower() in BRAND_TEXT:
                gone = True
                labels += 1
            if gone:
                shape._element.getparent().remove(shape._element)
    prs.save(str(path))
    print(f"{path.name}: removed {pictures} logo pictures and {labels} institute labels")
    return pictures, labels


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        strip(pathlib.Path(arg))

# Test inputs and expected outcomes
# --------------------------------
# The day's built deck, straight from scripts/build_deck.py
#     removed N logo pictures and M institute labels, N being one per slide that carries the header
# The same deck a second time
#     removed 0 logo pictures and 0 institute labels

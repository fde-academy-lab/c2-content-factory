"""The programme's visual identity, in one place, for every artifact that draws.

The palette, the type and the assets are the ones in the Programme Head's academic orientation deck
(version 3, 28 September 2026), which is the design bar for every deck, cheat sheet, notebook and
companion page in the programme. A deck, a sheet and a notebook that read their colours from here
cannot drift apart.

Icons are Lucide line icons (ISC licence), taken from the react-icons package that ships with the
build environment and rasterised on first use into the render cache, so no icon file is committed.
"""
import hashlib
import json
import os
import pathlib
import shutil
import subprocess
import tempfile

# Colours, as the orientation deck uses them.
INK = "#1A0F5C"          # titles and strong text
NIGHT = "#1A1440"        # body text, code cards
VIOLET = "#5B3FD6"       # the accent: eyebrows, icons, the current step
VIOLET_DEEP = "#4E38AB"
VIOLET_MID = "#2C1A86"   # the top of a dark card's gradient
VIOLET_BRIGHT = "#7B62E8"
LAVENDER = "#D9A7FF"     # numerals and highlights on the dark surface
MUTED = "#6B6690"        # subtitles and secondary text
SOFT = "#A9A3D2"         # secondary text on the dark surface
LILAC = "#CFC9EE"        # borders, inactive steps
LINE = "#E4E1F1"         # hairlines and card borders
TINT = "#EEEAFB"         # icon circles and light strips
SURFACE = "#F4F2FA"      # alternate table rows
WHITE = "#FFFFFF"
ROSE = "#D63A6A"         # what breaks, what is wrong
ROSE_TINT = "#FCEBF0"
GREEN = "#1F8A5B"        # what holds, what is right
GREEN_TINT = "#E8F5EE"

TITLE_FONT = "Georgia"
BODY_FONT = "Calibri"
MONO_FONT = "Consolas"

ASSETS = pathlib.Path(__file__).parent / "assets" / "brand"
BG_DARK = ASSETS / "bg_dark.jpg"
BG_LIGHT = ASSETS / "bg_light.jpg"
LOGO = ASSETS / "iitgn_logo.png"

INSTITUTE = "Indian Institute of Technology Gandhinagar"
ADMIN_LINE = "ADMINISTERED THROUGH THE COMPETENCY ADVANCEMENT ACADEMY"
PROGRAMME_LINE = "PG DIPLOMA IN AI-ML AND AGENTIC AI ENGINEERING  ·  COHORT 2"

ICON_CACHE = pathlib.Path(tempfile.gettempdir()) / "c2_icons"
NODE_MODULES = pathlib.Path("/opt/node22/lib/node_modules")

_ICON_JS = r"""
const React = require('react');
const { renderToStaticMarkup } = require('react-dom/server');
const lu = require('react-icons/lu');
const sharp = require('sharp');
const jobs = JSON.parse(process.argv[process.argv.length - 1]);
(async () => {
  for (const [name, colour, out, px] of jobs) {
    const comp = lu[name];
    if (!comp) { console.log('MISSING ' + name); continue; }
    let svg = renderToStaticMarkup(React.createElement(comp, { size: px, strokeWidth: 2 }));
    svg = svg.replace(/currentColor/g, colour);
    if (!svg.includes('xmlns=')) svg = svg.replace('<svg', '<svg xmlns="http://www.w3.org/2000/svg"');
    await sharp(Buffer.from(svg)).png().toFile(out);
  }
})();
"""


def icon_component(name):
    """`chart-line` becomes `LuChartLine`, the react-icons name for the Lucide icon."""
    return "Lu" + "".join(part[:1].upper() + part[1:] for part in name.split("-"))


def icon_path(name, colour):
    key = hashlib.sha1(f"{name}{colour}".encode()).hexdigest()[:12]
    return ICON_CACHE / f"{name}_{key}.png"


def ensure_icons(pairs, px=160):
    """Rasterise every (name, colour) pair not yet in the cache, in one node call.

    Returns the names Lucide does not have, so a typo in a slide source fails the build loudly
    instead of shipping an empty circle.
    """
    ICON_CACHE.mkdir(parents=True, exist_ok=True)
    jobs = [[icon_component(n), c, str(icon_path(n, c)), px] for n, c in sorted(set(pairs))
            if not icon_path(n, c).exists()]
    if not jobs:
        return []
    if not shutil.which("node"):
        return []
    env = dict(os.environ)
    env["NODE_PATH"] = str(NODE_MODULES)
    run = subprocess.run(["node", "-e", _ICON_JS, json.dumps(jobs)], capture_output=True, text=True,
                         env=env, timeout=300)
    missing = [line.split(" ", 1)[1] for line in run.stdout.splitlines() if line.startswith("MISSING")]
    return missing


def rgb(hex_colour):
    """'#5B3FD6' as the (r, g, b) triple python-pptx and PIL both take."""
    h = hex_colour.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


# Test inputs and expected outcomes
# --------------------------------
# python3 -c "import sys; sys.path.insert(0, 'scripts'); import brand; print(brand.icon_component('chart-line'))"
#     Prints LuChartLine.
# python3 -c "import sys; sys.path.insert(0, 'scripts'); import brand; print(brand.ensure_icons([('search', '#5B3FD6'), ('no-such-icon', '#5B3FD6')]))"
#     Writes search_<hash>.png into the icon cache and prints ['LuNoSuchIcon'].
# python3 -c "import sys; sys.path.insert(0, 'scripts'); import brand; print(brand.rgb('#5B3FD6'))"
#     Prints (91, 63, 214).

#!/usr/bin/env python3
"""Ship gate for a study note. Every FAIL is fixed before the note is shown.

    python3 check_notes.py path/to/content.md [--minutes 120]

--minutes is the length of the session the note covers, which sets the word
and figure budget. Default 120.
"""

import argparse
import re
import sys
from collections import Counter

BANNED_WORDS = [
    "additionally", "moreover", "however", "hence", "thus", "nonetheless",
    "furthermore", "accordingly", "indeed", "dynamic",
]

BANNED_HEADINGS = [
    "introduction", "overview", "background", "key takeaways", "key concepts",
    "takeaways", "summary", "conclusion", "deep dive", "what we learned",
    "recap", "wrapping up", "final thoughts", "let us explore", "in summary",
]

OUTCOME_FILLER = [
    r"this is (a )?(key|critical|essential|important|vital|crucial)",
    r"is foundational to", r"will help you in (your )?(interviews?|career)",
    r"cannot be overstated", r"plays a (key|vital|crucial) role",
]

HEDGE_OPENERS = [
    r"it is worth noting", r"it is important to (note|understand|remember)",
    r"let us (explore|dive|take a look)", r"when it comes to",
    r"in today'?s (fast|rapidly|ever)", r"at the end of the day",
    r"in this section,? we will", r"we will now explore",
]

REGISTER_WORDS = [
    "delve", "tapestry", "seamless", "holistic", "myriad", "robust framework",
    "comprehensive approach", "unlock the power", "game.changer", "landscape of",
    "navigate the complexities",
]

DEVICES = ["IN THE FIELD", "WATCH OUT", "ORIGIN", "CALLBACK"]

REQUIRED_PARTS = {
    "what you can now do": r"what you can now do|what this session put",
    "where this sits": r"where this sits|where this fits|where it sits",
    "picture to remember": r"picture to remember|the one picture",
    "where this shows up": r"shows up in|in the client room|on the job",
    "try this yourself": r"try this|challenge",
    "self-check": r"self.check|check yourself|the answers",
    "where this gets tested": r"gets tested|interview|exam",
    "glossary": r"glossary|the words",
    "go deeper": r"go deeper|reading path|where to read next",
}

BUDGET = [
    (95, 1800, 2500, 4, 6),
    (200, 2800, 4000, 6, 10),
    (10 ** 6, 4000, 5500, 10, 14),
]


def budget_for(minutes):
    for cap, lo, hi, flo, fhi in BUDGET:
        if minutes <= cap:
            return lo, hi, flo, fhi
    return BUDGET[-1][1:]


def strip_code(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", " ", text)


def main(path, minutes):
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()

    fails, warns = [], []
    body = strip_code(raw)
    lower = body.lower()

    # Front matter
    if not raw.lstrip().startswith("---"):
        fails.append("front matter block is missing at the top of the file")
    else:
        for field in ("title:", "session:", "programme:", "promise:"):
            if field not in raw[:1200].lower():
                fails.append("front matter is missing %s" % field.rstrip(":"))

    # Size
    plain = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", body)
    plain = re.sub(r"[#>*_|`\-]", " ", plain)
    words = len([w for w in plain.split() if any(c.isalnum() for c in w)])
    figures = len(re.findall(r"!\[[^\]]*\]\([^)]*\)", body))
    lo, hi, flo, fhi = budget_for(minutes)
    if not lo <= words <= hi:
        fails.append("word count %d is outside the %d to %d budget for a %d minute session"
                     % (words, lo, hi, minutes))
    if not flo <= figures <= fhi:
        fails.append("figure count %d is outside the %d to %d budget" % (figures, flo, fhi))

    # Em-dashes, both literal and escaped
    if "\u2014" in raw or "\\u2014" in raw or "&mdash;" in raw:
        fails.append("em-dash present, in literal or escaped form")

    # Banned words
    for word in BANNED_WORDS:
        hits = len(re.findall(r"\b%s\b" % word, lower))
        if hits:
            fails.append("banned word '%s' appears %d time(s)" % (word, hits))

    # Register words
    for word in REGISTER_WORDS:
        if re.search(word, lower):
            fails.append("register word or phrase matching '%s'" % word)

    # Hedge openers
    for pat in HEDGE_OPENERS:
        if re.search(pat, lower):
            fails.append("hedge opener matching '%s'" % pat)

    # Antithesis
    anti = re.findall(r"\bnot (?:a |an |the )?[\w ]{2,28}, but\b", lower)
    anti += re.findall(r"\bis not about [\w ]{2,28}, it is\b", lower)
    if anti:
        fails.append("antithesis construction: %s" % "; ".join(anti[:3]))

    # Headings
    headings = re.findall(r"^#{2,4}\s+(.+)$", body, flags=re.M)
    for h in headings:
        clean = h.strip().lower().rstrip(":")
        for banned in BANNED_HEADINGS:
            if clean == banned or clean.startswith(banned + " "):
                fails.append("banned heading: '%s'" % h.strip())

    # Required parts
    all_headings = " || ".join(h.lower() for h in headings)
    for name, pat in REQUIRED_PARTS.items():
        if not re.search(pat, all_headings):
            fails.append("no heading found for the '%s' part" % name)

    # Devices
    counts = Counter()
    for dev in DEVICES:
        counts[dev] = len(re.findall(r"\*\*%s\*\*" % dev, body))
    total = sum(counts.values())
    if not 8 <= total <= 16:
        fails.append("device count %d is outside 8 to 16 (%s)"
                     % (total, ", ".join("%s %d" % (d, counts[d]) for d in DEVICES)))
    if counts["CALLBACK"] < 2:
        fails.append("only %d CALLBACK device(s); at least two are required"
                     % counts["CALLBACK"])
    if counts["ORIGIN"] > 2:
        fails.append("%d ORIGIN devices; two is the maximum" % counts["ORIGIN"])

    # Every level-2 section in the body carries IN THE FIELD
    blocks = re.split(r"^##\s+", body, flags=re.M)[1:]
    for block in blocks:
        title = block.splitlines()[0].strip()
        skip = any(k in title.lower() for k in
                   ("glossary", "go deeper", "try this", "gets tested", "self",
                    "where this sits", "picture to remember", "what you can now do",
                    "shows up", "interview", "exam", "reading"))
        if skip:
            continue
        if "**IN THE FIELD**" not in block:
            fails.append("section '%s' has no IN THE FIELD device" % title)

    # Repeated bold labels other than devices
    labels = re.findall(r"\*\*([A-Za-z][A-Za-z ]{2,24}):\*\*", body)
    for label, n in Counter(labels).items():
        if n > 2:
            fails.append("bolded label '%s:' repeated %d times" % (label, n))

    # Bullets that are not sentences
    stubs = []
    for line in body.splitlines():
        m = re.match(r"^\s*(?:[-*+]|\d+\.)\s+(.*\S)\s*$", line)
        if not m:
            continue
        text = re.sub(r"[*_`\[\]()]", "", m.group(1)).strip()
        if text.startswith("!") or "|" in text:
            continue
        if len(text.split()) < 4 or text[-1] not in ".?!:":
            stubs.append(text[:60])
    if stubs:
        warns.append("%d bullet(s) may not be complete sentences, first: %s"
                     % (len(stubs), stubs[0]))

    # Unsourced statistics
    unsourced = []
    for para in re.split(r"\n\s*\n", body):
        if re.search(r"\b\d+(\.\d+)?\s?(%|percent|x faster|million|billion)\b", para, re.I):
            if not re.search(r"\((?:[^)]*,\s*(19|20)\d\d)\)", para):
                unsourced.append(" ".join(para.split())[:70])
    if unsourced:
        warns.append("%d paragraph(s) carry a statistic with no inline source, first: %s"
                     % (len(unsourced), unsourced[0]))

    # Part 3 blocks
    if "**What this session covered.**" not in body:
        fails.append("part 3 has no 'What this session covered.' block")
    for pat in OUTCOME_FILLER:
        if re.search(pat, lower):
            fails.append("outcome tie is asserting importance rather than naming a moment: '%s'"
                         % pat)
    if re.search(r"by the end of this (session|note),? you will", lower):
        fails.append("learning-objective framing; part 2 carries capabilities without the label")

    # Links
    links = re.findall(r"\]\((https?://[^)]+)\)", body)
    if len(links) < 3:
        fails.append("only %d external link(s); the reading path needs at least three"
                     % len(links))

    # Challenge answer pointers
    if not re.search(r"missed this one|re.read|go back to section", lower):
        fails.append("the self-check has no pointer telling the reader which section to re-read")

    # Closing slogan
    tail = " ".join(body.strip().splitlines()[-4:]).lower()
    if re.search(r"that is the whole point|changes everything|happy learning|good luck|"
                 r"keep (learning|building)|see you (next|in)", tail):
        fails.append("closing slogan or encouragement at the end of the note")

    print("words %d · figures %d · devices %d · links %d"
          % (words, figures, total, len(links)))
    print("-" * 60)
    for f in fails:
        print("FAIL  %s" % f)
    for w in warns:
        print("WARN  %s" % w)
    if not fails and not warns:
        print("clean")
    print("-" * 60)
    print("%d fail, %d warn" % (len(fails), len(warns)))
    return 1 if fails else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("markdown")
    ap.add_argument("--minutes", type=int, default=120,
                    help="length of the session the note covers")
    args = ap.parse_args()
    sys.exit(main(args.markdown, args.minutes))

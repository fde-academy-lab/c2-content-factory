"""Audit the option sets in an exercise or a quiz for the three shortcuts a room finds fastest.

Three failures let a learner answer without knowing anything, and all three are mechanical:
the key is the longest option, the keys cluster on one or two positions, or a format line's
illustration happens to be the answer string.

Usage:
    python3 scripts/distractor_audit.py content/W01/D3
    python3 scripts/distractor_audit.py content/W01/D3/kahoot/C2_W01_D03_quiz_STUDENT.md

Two file shapes are read.

  Inline-marked. The correct option carries a marker on its own line, written as `<- correct`.
  Kahoot packs use this, because Kahoot numbers its answers and the pack ships to Kahoot.

  Lettered bank. Options are lettered a) to f) under numbered items, and the keys live in the
  matching file in exercises/solutions/, either as an answer string line such as
  `Answers: 1b 2d 3a` or as a markdown table with a Key column.

A file with options and no findable key is reported as unaudited, which is itself a failure,
because an exercise nobody can audit is an exercise nobody has checked.
"""
import pathlib
import re
import sys

ITEM = re.compile(r"^\s{0,3}#{2,4}\s*(?:Q|Item)\s*(\d+)|^\s{0,3}(\d{1,2})[.)]\s+\S", re.M)
LETTERED = re.compile(r"^\s{0,4}(?:\*\*)?([a-f])(?:\*\*)?[.)]\s+(.+?)\s*$")
NUMBERED = re.compile(r"^\s{0,4}(?:\*\*)?([1-6])(?:\*\*)?[.)]\s+(.+?)\s*$")
BULLET = re.compile(r"^\s{0,4}[-*]\s+(?!\[)(.+?)\s*$")
CORRECT = re.compile(r"(?:<-{1,2}|←|⇐)\s*correct|\[correct\]|\(correct\)|"
                     r"correct\s*(?:<-{1,2}|←)", re.I)
FORMAT_LINE = re.compile(r"format|post one line|answer as|reply with", re.I)
ANSWER_TOKENS = re.compile(r"\b(\d{1,2})\s*([a-f])\b")
ANSWER_LINE = re.compile(r"^\s*(?:[*_]{0,2}Answers?(?:\s+key|\s+string)?[*_]{0,2}\s*[:\-])(.+)$",
                         re.I | re.M)
FENCE = re.compile(r"^\s*```")

POSITIONS = "abcdef"


def _strip_fences(text):
    """Options inside a code fence are sample output, not an option set."""
    out, inside = [], False
    for line in text.splitlines():
        if FENCE.match(line):
            inside = not inside
            out.append("")
            continue
        out.append("" if inside else line)
    return "\n".join(out)


STEM = re.compile(r"\?\s*$|^\s*(?:\*\*)?(?:Options|Which|Pick|Choose|Select)\b", re.I)


def _clean(body):
    body = CORRECT.sub("", body).strip()
    return re.sub(r"^\*\*(.*?)\*\*$", r"\1", body).strip().rstrip(".")


def _option(line):
    """(position or None for a bullet, text, marked_correct) when this line is an option.

    Three shapes ship in this repository and all three are read: lettered `a)` banks in the
    exercises, numbered `1.` options in the earlier Kahoot packs, and bulleted options in the
    later ones. A bullet has no position of its own, so the run gives it one by order.
    """
    for pattern, kind in ((LETTERED, "letter"), (NUMBERED, "number")):
        m = pattern.match(line)
        if not m:
            continue
        raw = m.group(1)
        pos = raw.lower() if kind == "letter" else POSITIONS[int(raw) - 1]
        body = m.group(2)
        return pos, _clean(body), bool(CORRECT.search(body))
    m = BULLET.match(line)
    if m:
        body = m.group(1)
        return None, _clean(body), bool(CORRECT.search(body))
    return None


def parse_items(text):
    """Return [(item_label, [(position, option_text, is_marked_correct), ...]), ...].

    An option set is a contiguous run of three or more options starting at a or 1, running in
    order, with a stem in the six lines above it or a correct marker inside it. Everything else
    that looks like a numbered list is a numbered list: an agenda, a set of steps, a checklist.
    """
    lines = _strip_fences(text).splitlines()
    items, seen, i = [], 0, 0
    heading_label = None
    while i < len(lines):
        head = re.match(r"^\s{0,3}#{2,4}\s*(?:Q|Item)?\s*(\d+)\b", lines[i])
        if head:
            heading_label = head.group(1)
            i += 1
            continue
        if not _option(lines[i]):
            i += 1
            continue

        start, run = i, []
        while i < len(lines):
            here = _option(lines[i])
            if here:
                run.append(here)
                i += 1
            elif not lines[i].strip() and i + 1 < len(lines) and _option(lines[i + 1]):
                i += 1
            else:
                break

        bullets = all(o[0] is None for o in run)
        if bullets:
            run = [(POSITIONS[n], text, marked) for n, (_, text, marked) in enumerate(run)]
            ordered, qualifies = True, any(o[2] for o in run)
        else:
            ordered = [o[0] for o in run] == list(POSITIONS[:len(run)])
            stemmed = any(STEM.search(l) for l in lines[max(0, start - 6):start])
            qualifies = stemmed or any(o[2] for o in run)
        if 3 <= len(run) <= 6 and ordered and qualifies:
            seen += 1
            items.append((heading_label or str(seen), run))
            heading_label = None
    return items


def keys_from_solutions(path):
    """Pull an item-to-letter map out of the matching solutions file, if one exists."""
    stem = path.stem.replace("_STUDENT", "")
    folder = path.parent
    candidates = []
    for root in (folder, folder.parent / "solutions", folder.parent.parent / "exercises" / "solutions"):
        if root.is_dir():
            candidates += [p for p in root.glob("*.md") if stem.split("_")[-1] in p.stem
                           or p.stem.startswith(stem)]
    keys = {}
    for cand in candidates:
        text = cand.read_text(encoding="utf-8", errors="replace")
        for line in ANSWER_LINE.findall(text):
            for item, letter in ANSWER_TOKENS.findall(line):
                keys[item] = letter.lower()
        for row in re.findall(r"^\|\s*(\d{1,2})\s*\|\s*([a-f])\s*\|", text, re.M):
            keys[row[0]] = row[1].lower()
        if keys:
            return keys, cand
    return keys, None


def audit_file(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    items = parse_items(text)
    if not items:
        return 0, None

    inline = any(marked for _, opts in items for *_, marked in opts)
    solution_keys, solution_file = ({}, None) if inline else keys_from_solutions(path)

    fails, key_positions, unaudited = 0, [], []
    for label, opts in items:
        key = None
        if inline:
            marked = [o for o in opts if o[2]]
            if len(marked) == 1:
                key = marked[0]
            elif len(marked) > 1:
                print(f"FAIL  {path.name} item {label}: {len(marked)} options are marked correct, "
                      f"and exactly one must be.")
                fails += 1
                continue
        elif label in solution_keys:
            wanted = solution_keys[label]
            key = next((o for o in opts if o[0] == wanted), None)
            if key is None:
                print(f"FAIL  {path.name} item {label}: the solutions file keys option "
                      f"'{wanted}', which this item does not offer.")
                fails += 1
                continue
        if key is None:
            unaudited.append(label)
            continue

        key_positions.append(key[0])
        longest = max(len(o[1]) for o in opts)
        if len(key[1]) == longest and sum(1 for o in opts if len(o[1]) == longest) == 1:
            print(f"FAIL  {path.name} item {label}: the key is the longest option at "
                  f"{len(key[1])} characters against {sorted(len(o[1]) for o in opts)[-2]} for the "
                  f"next longest. Write the distractors at the key's precision.")
            fails += 1

    if unaudited:
        print(f"FAIL  {path.name}: {len(unaudited)} items carry options with no findable key "
              f"(items {', '.join(unaudited[:8])}). Mark the key inline, or record the letters in "
              f"the solutions file as an Answers line or a Key column.")
        fails += 1

    if key_positions:
        used = sorted(set(p for _, opts in items for p, *_ in opts))
        counts = {p: key_positions.count(p) for p in used}
        n = len(key_positions)
        top = max(counts, key=counts.get)
        if n >= 4 and counts[top] / n > 0.5:
            print(f"FAIL  {path.name}: {counts[top]} of {n} keys sit on position '{top}'. "
                  f"Spread the keys across {', '.join(used)}.")
            fails += 1
        empties = [p for p in used if counts[p] == 0]
        if n >= 8 and empties:
            print(f"FAIL  {path.name}: no key ever lands on {', '.join(empties)} across {n} items, "
                  f"which a room notices by the third quiz.")
            fails += 1

        keyed = {lab: k for (lab, opts), k in zip(
            [(lab, opts) for lab, opts in items], key_positions)}
        for line in text.splitlines():
            if not FORMAT_LINE.search(line):
                continue
            shown = [(i, l.lower()) for i, l in ANSWER_TOKENS.findall(line)]
            if len(shown) < 3:
                continue
            hits = sum(1 for i, l in shown if keyed.get(i) == l)
            if hits >= max(3, int(0.6 * len(shown))):
                print(f"FAIL  {path.name}: a format line shows {hits} of {len(shown)} true answers: "
                      f"{line.strip()[:80]}. Change the illustration, never the key.")
                fails += 1

        spread = " ".join(f"{p}={counts[p]}" for p in used)
        src = f"keys inline" if inline else f"keys from {solution_file.name if solution_file else 'nowhere'}"
        return fails, f"      {path.name}: {len(items)} items, {src}, positions {spread}"

    return fails, f"      {path.name}: {len(items)} items, none keyed"


def main():
    targets = [pathlib.Path(a) for a in sys.argv[1:] if not a.startswith("--")]
    if not targets:
        print("FAIL  distractor_audit.py needs a file or a folder to look in")
        sys.exit(1)

    # Only the folders that hold answerable items. A deck, a brief or a day sheet may carry a
    # lettered list, and auditing it as a quiz reports failures nobody can act on.
    AUDITED = {"unguided", "guided", "exercises", "kahoot", "paper", "answer-key", "notebooks"}
    files = []
    for t in targets:
        if t.is_dir():
            files += sorted(p for p in t.rglob("*.md") if p.parent.name in AUDITED)
        else:
            files.append(t)
    files = [p for p in dict.fromkeys(files) if p.suffix == ".md"]

    fails, reports, audited = 0, [], 0
    for path in files:
        f, report = audit_file(path)
        fails += f
        if report:
            audited += 1
            reports.append(report)

    if not audited:
        print("INFO  no option sets found, so the distractor audit has nothing to check")
        sys.exit(0)
    for report in reports:
        print(report)
    print(f"      {audited} files carrying option sets audited")
    print("RESULT:", "FAIL" if fails else "PASS", f"({fails} failures)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# scripts/distractor_audit.py content/W01/D3/kahoot/C2_W01_D03_quiz_STUDENT.md
#     Reads the inline `<- correct` markers, reports the key-position spread, and exits 0 when
#     no key is the longest option and no position holds more than half the keys.
# scripts/distractor_audit.py content/W01/D3
#     Audits every exercise and quiz under the day, one report line each.
# An exercise whose key is 40 characters longer than every distractor
#     One FAIL line naming both lengths, and exit 1.
# An exercise with lettered options and no Answers line in its solutions file
#     One FAIL line saying the items are unaudited, and exit 1.
# A file whose format line reads "Post one line: 1a 2c 3b 4d" while those are the real keys
#     One FAIL line quoting the format line, and exit 1.

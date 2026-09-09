#!/usr/bin/env python3
"""Check a detailed curriculum file written in the session-row format.

Usage: python3 check_detailing.py <curriculum.md> [--strict]

Flags, per session:
  - more new ideas than the block allows (2h: 4, 3h: 5, day: 8)
  - more new terms than ideas
  - an idea with no depth target, or a first encounter at L3 or L4
  - a revisited idea whose depth did not rise
  - reference pack slots missing, unverified, or left as placeholders
  - continuity lines missing
  - no transfer question, fewer than two follow-ups, no return question
  - narrative with no provenance
  - basics budget missing or over 15 minutes per two-hour block
Exit code 1 when any error is found. Warnings do not fail the run unless --strict.
"""
import re
import sys
from collections import OrderedDict

IDEA_CAP = {"2h": 4, "3h": 5, "day": 8}
BASICS_CAP = {"2h": 15, "3h": 22, "day": 45}
CONTINUITY_KEYS = [
    "covered before", "do not re-teach", "spine case", "fresh cases",
    "case studies", "basics budget", "revisited at",
]
PACK_SLOTS = ["video", "article", "repo", "architecture", "interview"]
PLACEHOLDER = re.compile(r"<[^>]{1,40}>")
DATE = re.compile(r"checked:\s*(\d{4}-\d{2}-\d{2})")


def split_sessions(text):
    parts = re.split(r"^## (S\d+)\s*·\s*", text, flags=re.M)
    sessions = OrderedDict()
    for i in range(1, len(parts), 2):
        sid = parts[i]
        body = parts[i + 1]
        title, _, rest = body.partition("\n")
        sessions[sid] = (title.strip(), rest)
    return sessions


def section(body, name):
    m = re.search(r"^### " + re.escape(name) + r"\s*$(.*?)(?=^### |\Z)", body, flags=re.M | re.S)
    return m.group(1) if m else None


def field(body, key):
    m = re.search(r"^" + re.escape(key) + r":\s*(.*)$", body, flags=re.M | re.I)
    return m.group(1).strip() if m else None


def check(text, strict=False):
    errors, warnings = [], []
    sessions = split_sessions(text)
    if not sessions:
        return ["no sessions found; headings must be '## S07 · <title>'"], []

    for sid, (title, body) in sessions.items():
        E = lambda msg: errors.append(f"{sid}: {msg}")
        W = lambda msg: warnings.append(f"{sid}: {msg}")

        if not title or len(title.split()) < 6:
            W("title should be a full sentence about what the learner can do after the session")

        block = (field(body, "Block") or "").lower()
        if block not in IDEA_CAP:
            E("Block must be one of 2h, 3h, day")
            block = "2h"
        band = (field(body, "Band") or "").lower()
        if band not in ("early", "middle", "late"):
            E("Band must be early, middle or late")

        narrative = field(body, "Narrative") or ""
        if not narrative:
            E("Narrative line missing")
        elif "provenance:" not in narrative:
            E("Narrative carries no provenance (researched | copied | invented | hybrid)")

        # ideas
        ideas_sec = section(body, "Ideas") or ""
        ideas = re.findall(r"^\d+\.\s+(.*)$", ideas_sec, flags=re.M)
        if not ideas:
            E("no ideas listed under ### Ideas")
        new_count = 0
        for n, line in enumerate(ideas, 1):
            depth = re.search(r"depth:\s*L([1-4])", line)
            status = re.search(r"status:\s*(new|revisited from (S\d+) L([1-4])|variant of idea \d+)", line)
            comps = re.search(r"competencies:\s*([\d,\s]+)", line)
            if not depth:
                E(f"idea {n} has no depth target (depth: L1..L4)")
            if not comps:
                W(f"idea {n} names no interview competencies")
            if not status:
                E(f"idea {n} has no status (new | revisited from Sxx Ly | variant of idea n)")
                continue
            st = status.group(1)
            if st == "new":
                new_count += 1
                if depth and int(depth.group(1)) >= 3:
                    E(f"idea {n} is a first encounter at L{depth.group(1)}; first encounters are L1 or L2")
            elif st.startswith("revisited"):
                new_count += 1
                prev = int(status.group(3))
                if depth and int(depth.group(1)) <= prev:
                    E(f"idea {n} revisited from {status.group(2)} L{prev} but depth did not rise (now L{depth.group(1)})")
            # variants do not count toward the cap
        cap = IDEA_CAP[block]
        if new_count > cap:
            E(f"{new_count} ideas in a {block} block; cap is {cap}. Defer, demote or split; never shrink the units")
        if new_count < 2 and block != "day":
            W(f"only {new_count} idea(s) in a {block} block; check for the ten-thousand-feet failure")

        # terms
        terms_sec = section(body, "Terms") or ""
        terms = re.findall(r"^-\s+\S", terms_sec, flags=re.M)
        if len(terms) > max(new_count, 1):
            E(f"{len(terms)} new terms against {new_count} ideas; one term per idea at most")
        for t in re.findall(r"^-\s+(.*)$", terms_sec, flags=re.M):
            if "(after" not in t:
                W(f"term '{t.split('(')[0].strip()}' does not say which problem it is introduced after")

        # prerequisites
        pre = section(body, "Prerequisites")
        if pre is None:
            E("### Prerequisites missing")
        else:
            if field(pre, "concepts") is None:
                E("prerequisites: 'concepts:' line missing (write 'none' if none)")
            if field(pre, "first-use tools") is None:
                E("prerequisites: 'first-use tools:' line missing (write 'none' if none)")

        # continuity
        cont = section(body, "Continuity")
        if cont is None:
            E("### Continuity missing")
        else:
            for k in CONTINUITY_KEYS:
                if field(cont, k) is None:
                    E(f"continuity: '{k}:' line missing")
            bb = field(cont, "basics budget") or ""
            m = re.search(r"(\d+)\s*min", bb)
            if not m:
                E("continuity: basics budget must be '<n> min'")
            elif int(m.group(1)) > BASICS_CAP[block]:
                E(f"continuity: basics budget {m.group(1)} min exceeds {BASICS_CAP[block]} for a {block} block")
            cs = field(cont, "case studies") or ""
            if cs and cs.lower() != "none":
                if PLACEHOLDER.search(cs) or not DATE.search(cs):
                    E("continuity: case studies must name company, number, source and a checked date")

        # reference pack
        pack = section(body, "Reference pack")
        if pack is None:
            E("### Reference pack missing")
        else:
            for slot in PACK_SLOTS:
                v = field(pack, slot)
                if v is None:
                    E(f"reference pack: '{slot}:' slot missing")
                    continue
                low = v.lower()
                if low.startswith("to be found"):
                    W(f"reference pack: {slot} still to be found")
                    continue
                if slot == "repo" and low.startswith("not applicable"):
                    continue
                if PLACEHOLDER.search(v):
                    E(f"reference pack: {slot} contains a placeholder; verify and fill, or write 'to be found'")
                    continue
                if not re.search(r"https?://\S+", v):
                    E(f"reference pack: {slot} has no URL")
                if not DATE.search(v):
                    E(f"reference pack: {slot} has no 'checked: yyyy-mm-dd'; a URL from memory is not a reference")
                if slot == "interview" and not re.search(r"level:\s*L[1-4]", v):
                    W("reference pack: interview slot should carry 'level: Lx'")

        # transfer
        tr = section(body, "Transfer")
        if tr is None:
            E("### Transfer missing")
        else:
            if not field(tr, "question"):
                E("transfer: no question")
            fu = [k for k in ("follow-up 1", "follow-up 2") if field(tr, k)]
            if len(fu) < 2:
                E("transfer: needs two follow-ups (why this over the alternative; what happens when it breaks)")
            rq = field(tr, "return question")
            if not rq:
                E("transfer: no return question")
            elif not re.search(r"from S\d+ \(L[1-4] to L[1-4]\)", rq):
                W("transfer: return question should read 'from Sxx (Ln to Lm): ...' and rise one level")

        # hands-on
        ho = section(body, "Hands-on")
        if ho is None:
            E("### Hands-on missing")
        else:
            if not field(ho, "mid-session"):
                E("hands-on: mid-session line missing")
            if not field(ho, "take-home"):
                E("hands-on: take-home line missing")

    return errors, warnings


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    path = sys.argv[1]
    strict = "--strict" in sys.argv
    text = open(path, encoding="utf-8").read()
    errors, warnings = check(text, strict)
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    n = len(split_sessions(text))
    print(f"\n{n} session(s), {len(errors)} error(s), {len(warnings)} warning(s)")
    if errors or (strict and warnings):
        sys.exit(1)


if __name__ == "__main__":
    main()

"""Create and update the GitHub content board from this repository's own day plan.

The board tracks one card per day pack, which is the unit this repository builds in and the unit a
reviewer signs off. The day plan below is the Content Build Tracker tab of the programme workbook,
transcribed once so the board and the repository cannot drift apart.

Usage:
    python3 scripts/board_sync.py --dry-run              # print what would change, touch nothing
    python3 scripts/board_sync.py --labels --milestones  # the one-time furniture
    python3 scripts/board_sync.py --week W01             # create or update one week's cards
    python3 scripts/board_sync.py --all                  # every week in the plan
    python3 scripts/board_sync.py --status W01 rework    # move a week to a status
    python3 scripts/board_sync.py --status W01/D3 review-1

Every run is safe to repeat. An issue is matched by the marker `<!-- board:W01/D3 -->` in its body,
so a second run updates the card it made the first time rather than opening a duplicate.

Authentication reads GH_TOKEN or GITHUB_TOKEN. The token needs write access to issues on the
repository, which is what a Codespace and a Claude Code session already carry.

What this script cannot do. A GitHub Project board and its Status column live behind the GraphQL
API, and creating one is a one-time click documented in docs/agents/content-board.md. Everything
that hangs off the board, which is the cards, their labels, their milestones and their state, is
here and is repeatable.
"""
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

OWNER = "fde-academy-lab"
REPO = "c2-content-factory"
API = f"https://api.github.com/repos/{OWNER}/{REPO}"

# --------------------------------------------------------------------------- the vocabulary
# Status is the one label a card carries from the STATUS group at a time. The board's Status column
# mirrors these names, so a card dragged on the board and a card relabelled here mean the same.
STATUS = [
    ("status:backlog", "C9C9C2", "Planned, nobody has started it"),
    ("status:building", "2B4A7D", "Being built, one session per day pack"),
    ("status:review-1", "8A6D3B", "First-level review, correctness and completeness"),
    ("status:review-2", "6B3FA0", "Second-level review, the programme call"),
    ("status:spot-check", "0E7C7B", "Ad hoc review, raised outside the two levels"),
    ("status:rework", "8A3D3D", "Sent back with named changes"),
    ("status:done", "1F6F4A", "Signed off and shipped"),
]

# Who holds it. Labels rather than assignees, because the board has to work before every reviewer
# has a GitHub account. docs/agents/content-board.md says how to swap in real handles.
PEOPLE = [
    ("owner:rushikesh", "1D4ED8", "Rushikesh builds this"),
    ("owner:anmol", "1D4ED8", "Anmol builds this"),
    ("owner:claude", "1D4ED8", "Built in a Claude Code session"),
    ("review-1:navaid", "B45309", "Navaid holds the first-level review"),
    ("review-2:akash", "6B21A8", "Akash holds the second-level review"),
    ("spot:ishu", "0F766E", "Ishu has raised a spot check"),
]

DAY_TYPE = [
    ("type:teaching", "E4ECF7", "A regular teaching day"),
    ("type:saturday", "E4ECF7", "The Saturday recap block"),
    ("type:build-week", "E4ECF7", "A build-week day: mini project, no test"),
    ("type:holiday", "F7F7F5", "No session"),
]

ARTIFACT = [
    ("artifact:deck", "DBEAFE", "Slide source and the deck built from it"),
    ("artifact:notebook", "DBEAFE", "Demo and hands-on notebooks"),
    ("artifact:exercises", "DBEAFE", "Guided, unguided and solutions"),
    ("artifact:takehome", "DBEAFE", "After-class task sheet"),
    ("artifact:kahoot", "DBEAFE", "The daily ungraded quiz"),
    ("artifact:preread", "DBEAFE", "Ships the night before"),
    ("artifact:study-notes", "DBEAFE", "Written after delivery"),
    ("artifact:cheatsheet", "DBEAFE", "The printed sheet and its PDF"),
    ("artifact:trainer", "DBEAFE", "Run sheet and facilitation notes"),
    ("artifact:demos", "DBEAFE", "Companion pages and workbooks"),
]

FLAGS = [
    ("gate:verify-pass", "1F6F4A", "scripts/verify.py passes on this day folder"),
    ("gate:verify-fail", "8A3D3D", "scripts/verify.py fails on this day folder"),
    ("blocked", "8A3D3D", "Waiting on a decision or an upstream lock"),
    ("curriculum-rework", "C2410C", "The curriculum row itself is being changed"),
]

ALL_LABELS = STATUS + PEOPLE + DAY_TYPE + ARTIFACT + FLAGS

WEEKS = {
    "W01": ("28 Sep to 03 Oct 2026", "2026-10-03", "Teaching week"),
    "W02": ("05 Oct to 10 Oct 2026", "2026-10-10", "Teaching week"),
    "W03": ("12 Oct to 17 Oct 2026", "2026-10-17", "Build week 1"),
    "W04": ("19 Oct to 24 Oct 2026", "2026-10-24", "Teaching week"),
    "W05": ("26 Oct to 31 Oct 2026", "2026-10-31", "Teaching week, ME1"),
    "W06": ("02 Nov to 07 Nov 2026", "2026-11-07", "Build week 2"),
    "W07": ("09 Nov to 14 Nov 2026", "2026-11-14", "Teaching week"),
    "W08": ("16 Nov to 21 Nov 2026", "2026-11-21", "Teaching week"),
    "W09": ("23 Nov to 28 Nov 2026", "2026-11-28", "Build week 3"),
}

# The Content Build Tracker, one tuple per row: week, day slot, date, focus, day type.
# The day slot is the folder this day writes into, so a card links straight at its content.
DAYS = [
    ("W01", "D1", "Mon 28 Sep", "Python on records: the first business answer", "teaching"),
    ("W01", "D2", "Tue 29 Sep", "Functions, errors and files: the AI-free lab", "teaching"),
    ("W01", "D3", "Wed 30 Sep", "Load, clean and profile: a profiled dataset", "teaching"),
    ("W01", "D4", "Thu 01 Oct", "Descriptive statistics: the segment summary", "teaching"),
    ("W01", "FRI", "Fri 02 Oct", "Gandhi Jayanti: holiday", "holiday"),
    ("W01", "SAT", "Sat 03 Oct", "Recap test 1 and the solution discussion", "saturday"),
    ("W02", "D1", "Mon 05 Oct", "Inference, causation and the insight writeup", "teaching"),
    ("W02", "D2", "Tue 06 Oct", "SQL core: extraction queries", "teaching"),
    ("W02", "D3", "Wed 07 Oct", "Joins, fan-out and validation", "teaching"),
    ("W02", "D4", "Thu 08 Oct", "Window functions and the timed drill", "teaching"),
    ("W02", "D5", "Fri 09 Oct", "Pandas at depth and tool judgment", "teaching"),
    ("W02", "SAT", "Sat 10 Oct", "Recap test 2 and the solution discussion", "saturday"),
    ("W03", "D1", "Mon 12 Oct", "Build 1: online intro and team scoping", "build-week"),
    ("W03", "D2", "Tue 13 Oct", "Build day 2: the parallel build", "build-week"),
    ("W03", "D3", "Wed 14 Oct", "Build day 3 and the catch-up reserve", "build-week"),
    ("W03", "D4", "Thu 15 Oct", "Mock R1 and build completion", "build-week"),
    ("W03", "D5", "Fri 16 Oct", "Expert day 1: group discussions", "build-week"),
    ("W03", "SAT", "Sat 17 Oct", "Expert day 2: demos and closure", "build-week"),
    ("W04", "D1", "Mon 19 Oct", "Metric design: north-star and guardrail", "teaching"),
    ("W04", "TUE", "Tue 20 Oct", "Dussehra: holiday", "holiday"),
    ("W04", "D3", "Wed 21 Oct", "Basket analysis: support, confidence, lift", "teaching"),
    ("W04", "D4", "Thu 22 Oct", "Cohorts, funnels and retention", "teaching"),
    ("W04", "D5", "Fri 23 Oct", "Thresholds and forecasting basics", "teaching"),
    ("W04", "SAT", "Sat 24 Oct", "Recap test 3 and the solution discussion", "saturday"),
    ("W05", "D1", "Mon 26 Oct", "The modelling loop, and ME1 week opens", "teaching"),
    ("W05", "D2", "Tue 27 Oct", "Regression and classification, read honestly", "teaching"),
    ("W05", "D3", "Wed 28 Oct", "The metric trap on imbalance", "teaching"),
    ("W05", "D4", "Thu 29 Oct", "Features and the leak hunt", "teaching"),
    ("W05", "D5", "Fri 30 Oct", "Generalisation and the comparison memo", "teaching"),
    ("W05", "SAT", "Sat 31 Oct", "Recap test 4 and the discussion", "saturday"),
    ("W06", "D1", "Mon 02 Nov", "Build 2: online intro and constraint briefs", "build-week"),
    ("W06", "D2", "Tue 03 Nov", "Build day 2: the parallel build", "build-week"),
    ("W06", "D3", "Wed 04 Nov", "Build day 3 and the catch-up reserve", "build-week"),
    ("W06", "D4", "Thu 05 Nov", "Mock R2 and build completion", "build-week"),
    ("W06", "D5", "Fri 06 Nov", "Expert day 1: group discussions", "build-week"),
    ("W06", "SAT", "Sat 07 Nov", "Expert day 2: demos and closure", "build-week"),
    ("W07", "MON", "Mon 09 Nov", "Diwali: holiday", "holiday"),
    ("W07", "D2", "Tue 10 Nov", "The network: neurons and the forward pass", "teaching"),
    ("W07", "D3", "Wed 11 Nov", "Learning: backprop, loss and learning rate", "teaching"),
    ("W07", "D4", "Thu 12 Nov", "Sick runs and the brakes", "teaching"),
    ("W07", "D5", "Fri 13 Nov", "The bridge to LLMs", "teaching"),
    ("W07", "SAT", "Sat 14 Nov", "Recap test 5 and the solution discussion", "saturday"),
    ("W08", "D1", "Mon 16 Nov", "Tokenization and token economics", "teaching"),
    ("W08", "D2", "Tue 17 Nov", "Attention: Q, K, V and multi-head", "teaching"),
    ("W08", "D3", "Wed 18 Nov", "Embeddings and the classical NLP arc", "teaching"),
    ("W08", "D4", "Thu 19 Nov", "Decoding dials and determinism", "teaching"),
    ("W08", "D5", "Fri 20 Nov", "Context windows, cost and latency", "teaching"),
    ("W08", "SAT", "Sat 21 Nov", "Recap test 6 and the solution discussion", "saturday"),
    ("W09", "D1", "Mon 23 Nov", "Build 3: online intro and contract briefs", "build-week"),
    ("W09", "TUE", "Tue 24 Nov", "Guru Nanak Jayanti: holiday", "holiday"),
    ("W09", "D3", "Wed 25 Nov", "AI-free debug drill and build", "build-week"),
    ("W09", "D4", "Thu 26 Nov", "Mock R3 and build", "build-week"),
    ("W09", "D5", "Fri 27 Nov", "Expert day 1: group discussions", "build-week"),
    ("W09", "SAT", "Sat 28 Nov", "Expert day 2: demos and the two-month close", "build-week"),
]

# Which artifact families a day of each shape owes. A Saturday is not a teaching day, so it owes
# the paper, its key and the discussion guide and nothing else.
OWES = {
    "teaching": ["deck", "trainer", "notebook", "exercises", "takehome", "kahoot", "preread",
                 "study-notes", "cheatsheet", "demos"],
    "build-week": ["trainer", "notebook", "exercises", "study-notes"],
    "saturday": ["paper", "answer-key", "discussion"],
    "holiday": [],
}

ARTIFACT_FOLDER = {
    "deck": "slides", "trainer": "trainer", "notebook": "notebooks", "exercises": "exercises",
    "takehome": "takehome", "kahoot": "kahoot", "preread": "preread",
    "study-notes": "study-notes", "cheatsheet": "cheatsheets", "demos": "demos",
    "paper": "paper", "answer-key": "answer-key", "discussion": "discussion",
}


# --------------------------------------------------------------------------- the API
def token():
    t = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not t:
        sys.exit("FAIL  set GH_TOKEN or GITHUB_TOKEN to a token that can write issues")
    return t


def call(method, path, body=None):
    req = urllib.request.Request(
        path if path.startswith("http") else API + path,
        data=json.dumps(body).encode() if body is not None else None,
        method=method,
        headers={"Authorization": f"Bearer {token()}",
                 "Accept": "application/vnd.github+json",
                 "Content-Type": "application/json",
                 "User-Agent": "c2-content-factory-board-sync"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            raw = r.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")[:200]
        if e.code in (404, 410):
            return None
        raise SystemExit(f"FAIL  {method} {path} -> {e.code} {detail}")


def paged(path):
    out, page = [], 1
    while True:
        chunk = call("GET", f"{path}{'&' if '?' in path else '?'}per_page=100&page={page}")
        if not chunk:
            return out
        out += chunk
        if len(chunk) < 100:
            return out
        page += 1


# --------------------------------------------------------------------------- the furniture
def sync_labels(dry):
    have = {l["name"]: l for l in paged("/labels")}
    for name, colour, desc in ALL_LABELS:
        if name in have:
            if have[name]["color"].lower() != colour.lower() or have[name].get("description") != desc:
                print(f"      update label {name}")
                if not dry:
                    call("PATCH", f"/labels/{urllib.parse.quote(name)}",
                         {"new_name": name, "color": colour, "description": desc})
            continue
        print(f"      create label {name}")
        if not dry:
            call("POST", "/labels", {"name": name, "color": colour, "description": desc})
    print(f"      {len(ALL_LABELS)} labels in the vocabulary")


def sync_milestones(dry):
    have = {m["title"]: m for m in paged("/milestones?state=all")}
    numbers = {}
    for week, (span, due, kind) in WEEKS.items():
        title = f"{week} · {span}"
        if title in have:
            numbers[week] = have[title]["number"]
            continue
        print(f"      create milestone {title}")
        if dry:
            continue
        m = call("POST", "/milestones",
                 {"title": title, "description": kind, "due_on": f"{due}T18:00:00Z"})
        numbers[week] = m["number"]
    return numbers


def milestone_numbers():
    have = {m["title"]: m["number"] for m in paged("/milestones?state=all")}
    return {w: have[f"{w} · {s}"] for w, (s, _, _) in WEEKS.items() if f"{w} · {s}" in have}


# --------------------------------------------------------------------------- the cards
def marker(week, slot):
    return f"<!-- board:{week}/{slot} -->"


def folder(week, slot):
    return f"content/{week}/{slot}"


def present(week, slot, family):
    """Whether the day folder already holds files of this artifact family."""
    d = os.path.join(folder(week, slot), ARTIFACT_FOLDER.get(family, family))
    try:
        return any(not f.startswith(".") for f in os.listdir(d))
    except OSError:
        return False


def body_for(week, slot, date, focus, kind, note):
    owes = OWES[kind]
    lines = [marker(week, slot), "",
             f"**{date}** · {focus}", ""]
    if kind == "holiday":
        lines += ["No session on this day, so nothing is built for it. The card exists so the "
                  "board and the Content Build Tracker have the same rows.", ""]
        return "\n".join(lines)

    url = f"https://github.com/{OWNER}/{REPO}/tree/main/{folder(week, slot)}"
    lines += [f"Day folder: [`{folder(week, slot)}/`]({url})", "",
              "## What this day owes", "",
              "| Artifact | Folder | In the repo |", "|---|---|---|"]
    for family in owes:
        sub = ARTIFACT_FOLDER.get(family, family)
        mark = "yes" if present(week, slot, family) else "not yet"
        lines.append(f"| {family} | `{sub}/` | {mark} |")
    lines += ["",
              "## How this card moves", "",
              "Build, then first-level review, then second-level review, then done. A spot check "
              "can arrive at any point and sends the card to rework with the change named in a "
              "comment. The status label and the board's Status column say the same thing, so "
              "either one can be moved.", "",
              "## Gate", "",
              f"`python3 scripts/verify.py {folder(week, slot)} --execute` is the one command that "
              "proves this day. A pack that has not passed it is not done.", ""]
    if note:
        lines += ["## Notes", "", note, ""]
    return "\n".join(lines)


def labels_for(week, slot, kind, status, extra):
    """A card carries its status, its day shape and whoever holds it, and nothing else.

    The artifact labels exist for the follow-up issues a review raises, where "the deck needs
    another pass" is worth filtering on. Putting all ten on every teaching card would colour every
    card the same and tell a reader nothing, so the artifact table in the body carries that.
    """
    return [f"status:{status}", f"type:{kind}"] + list(extra)


def find_cards():
    """Every card this script has made, keyed week/slot, read off the marker in the body."""
    out = {}
    for issue in paged("/issues?state=all&labels=" + urllib.parse.quote("type:teaching")) + \
            paged("/issues?state=all&labels=" + urllib.parse.quote("type:saturday")) + \
            paged("/issues?state=all&labels=" + urllib.parse.quote("type:build-week")) + \
            paged("/issues?state=all&labels=" + urllib.parse.quote("type:holiday")):
        m = re.search(r"<!-- board:(W\d\d)/([A-Z0-9]+) -->", issue.get("body") or "")
        if m:
            out[f"{m.group(1)}/{m.group(2)}"] = issue
    return out


def sync_week(week, status, extra, note_for, dry, cards, miles):
    made = 0
    for w, slot, date, focus, kind in DAYS:
        if w != week:
            continue
        key = f"{w}/{slot}"
        title = f"{w} {slot} · {date} · {focus}"
        body = body_for(w, slot, date, focus, kind, note_for.get(key, note_for.get(w, "")))
        want_status = "backlog" if kind == "holiday" else status
        labels = labels_for(w, slot, kind, want_status, extra if kind != "holiday" else [])
        payload = {"title": title, "body": body, "labels": labels}
        if week in miles:
            payload["milestone"] = miles[week]
        if key in cards:
            n = cards[key]["number"]
            print(f"      update #{n}  {title[:64]}")
            if not dry:
                call("PATCH", f"/issues/{n}", payload)
                if kind == "holiday" and cards[key]["state"] == "open":
                    call("PATCH", f"/issues/{n}",
                         {"state": "closed", "state_reason": "not_planned"})
        else:
            print(f"      create      {title[:64]}")
            if not dry:
                issue = call("POST", "/issues", payload)
                if kind == "holiday":
                    call("PATCH", f"/issues/{issue['number']}",
                         {"state": "closed", "state_reason": "not_planned"})
            made += 1
    return made


def set_status(target, status, dry, cards):
    """Move one day, or a whole week, to a status."""
    hits = [k for k in cards if k == target or k.startswith(target + "/") or k.split("/")[0] == target]
    if not hits:
        sys.exit(f"FAIL  no card matches {target}")
    for key in sorted(hits):
        issue = cards[key]
        keep = [l["name"] for l in issue["labels"] if not l["name"].startswith("status:")]
        if "type:holiday" in keep:
            continue
        print(f"      #{issue['number']} {key} -> status:{status}")
        if not dry:
            call("PATCH", f"/issues/{issue['number']}",
                 {"labels": keep + [f"status:{status}"]})
            if status == "done":
                call("PATCH", f"/issues/{issue['number']}",
                     {"state": "closed", "state_reason": "completed"})
            elif issue["state"] == "closed":
                call("PATCH", f"/issues/{issue['number']}", {"state": "open"})


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="print the changes and make none")
    ap.add_argument("--labels", action="store_true", help="create or correct the label vocabulary")
    ap.add_argument("--milestones", action="store_true", help="create a milestone per week")
    ap.add_argument("--week", help="create or update one week's cards, as W01")
    ap.add_argument("--all", action="store_true", help="every week in the plan")
    ap.add_argument("--status", nargs=2, metavar=("TARGET", "STATUS"),
                    help="move a week or a day to a status, as --status W01 rework")
    ap.add_argument("--set-status", default="backlog",
                    help="the status new cards are created with")
    ap.add_argument("--label", action="append", default=[],
                    help="an extra label for every card this run touches")
    a = ap.parse_args()
    dry = a.dry_run

    if a.labels:
        sync_labels(dry)
    if a.milestones:
        sync_milestones(dry)
    if not (a.week or a.all or a.status):
        return

    cards = find_cards()
    miles = milestone_numbers()
    if a.status:
        set_status(a.status[0], a.status[1], dry, cards)
        return

    weeks = list(WEEKS) if a.all else [a.week]
    total = 0
    for w in weeks:
        total += sync_week(w, a.set_status, a.label, {}, dry, cards, miles)
    print(f"      {total} cards created, {len(cards)} already existed")


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# scripts/board_sync.py --dry-run --labels --milestones --all
#     Prints every label, milestone and card it would create and writes nothing.
# scripts/board_sync.py --labels --milestones
#     Creates the 27 labels and the 9 week milestones. Safe to run again; it corrects a label
#     whose colour or description has drifted and leaves the rest alone.
# scripts/board_sync.py --week W02 --set-status backlog
#     Opens one card per day of Week 2, each carrying its artifact table and its milestone.
# scripts/board_sync.py --week W01 --set-status building --label owner:rushikesh
#     Updates the six Week 1 cards in place, because they are matched on their board marker.
# scripts/board_sync.py --status W01/D3 review-1
#     Moves one day to the first-level review and reopens it if it had been closed.
# scripts/board_sync.py --status W01 done
#     Moves every Week 1 card to done and closes it as completed.
# The same command with no GH_TOKEN in the environment
#     One FAIL line naming the variable, and exit 1, before any request is made.

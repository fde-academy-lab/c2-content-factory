"""Create and update the GitHub content board from this repository's own day plan.

The board tracks one card per day pack, which is the unit this repository builds in and the unit a
reviewer signs off. The day plan below is the day list of the curriculum workbook,
transcribed once so the board and the repository cannot drift apart.

Usage:
    python3 scripts/board_sync.py --dry-run              # print what would change, touch nothing
    python3 scripts/board_sync.py --labels --milestones  # the one-time furniture
    python3 scripts/board_sync.py --week W01             # create or update one week's cards
    python3 scripts/board_sync.py --all                  # every week in the plan
    python3 scripts/board_sync.py --status W01 rework    # move a week to a status
    python3 scripts/board_sync.py --status W01/D3 review-1
    python3 scripts/board_sync.py --project-add          # put every issue on the board, safe to repeat

Every run is safe to repeat. An issue is matched by the marker `<!-- board:W01/D3 -->` in its body,
so a second run updates the card it made the first time rather than opening a duplicate.

Authentication reads GH_TOKEN or GITHUB_TOKEN. The token needs write access to issues on the
repository, which is what a Codespace and a Claude Code session already carry.

What this script cannot do. Creating the board and naming its Status options is a one-time click
documented in docs/agents/content-board.md, because no API creates a Project's field options for
you. Putting issues on a board that already exists is `--project-add`, and it needs a classic
token with the `project` scope, since a fine-grained token has no Projects permission for a
personal account. Everything else, which is the cards, their labels, their milestones and their
state, runs on the ordinary issues token.
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
GRAPHQL = "https://api.github.com/graphql"
# fde-academy-lab is a personal account, so the board hangs off user() rather than
# organization(). Change this pair together if the repository ever moves to an org.
OWNER_FIELD = "user"
PROJECT_NUMBER = 7

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

# Where the work lives, for issues that are not day packs: a wiki page, a situation card, a
# builder script, a ground truth doc, the curriculum export, or the board itself.
AREA = [
    ("area:wiki", "5F6360", "A page under wiki/, published to the repository wiki"),
    ("area:situations", "5F6360", "A Situation Bank card or the bank's structure"),
    ("area:scripts", "5F6360", "A builder or one of the six proofs"),
    ("area:docs", "5F6360", "Ground truth, method or doctrine under docs/"),
    ("area:curriculum", "5F6360", "The workbook and its markdown exports"),
    ("area:board", "5F6360", "The tracker itself, and scripts/board_sync.py"),
]

HELP = [
    ("good-first-card", "1F6F4A", "A seeded situation somebody can expand into a full card"),
    ("source-check", "8A6D3B", "A link or a movable fact that needs re-verifying with today's date"),
]

ALL_LABELS = STATUS + PEOPLE + DAY_TYPE + ARTIFACT + FLAGS + AREA + HELP

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

# The day plan, one tuple per row: week, day slot, date, focus, day type. The focus strings are the
# 'Day focus' column of each week tab, so a card title says the same thing the curriculum says.
# The day slot is the folder this day writes into, so a card links straight at its content.
DAYS = [
    ("W01", "D1", "Mon 28 Sep", "The revenue tree and the first honest numbers", "teaching"),
    ("W01", "D2", "Tue 29 Sep", "Which lever moved? The sales-drop investigation", "teaching"),
    ("W01", "D3", "Wed 30 Sep", "Can we trust the numbers? Profile, clean, reconcile, recompute", "teaching"),
    ("W01", "D4", "Thu 01 Oct", "Real or noise, cause or coincidence, and the one-page note", "teaching"),
    ("W01", "FRI", "Fri 02 Oct", "Gandhi Jayanti: institute holiday, no session", "holiday"),
    ("W01", "SAT", "Sat 03 Oct", "The pen-and-paper test, then the interview-answer discussion", "saturday"),
    ("W02", "D1", "Mon 05 Oct", "The revenue tree as queries the warehouse runs every Monday", "teaching"),
    ("W02", "D2", "Tue 06 Oct", "Booked against collected: joining payments without lying", "teaching"),
    ("W02", "D3", "Wed 07 Oct", "Top members, falling spend, and the running total against plan", "teaching"),
    ("W02", "D4", "Thu 08 Oct", "The customer table Marketing refreshes every Monday", "teaching"),
    ("W02", "D5", "Fri 09 Oct", "The number reaches the leadership deck, and the tool judgment behind it", "teaching"),
    ("W02", "SAT", "Sat 10 Oct", "The pen-and-paper test, then the interview-answer discussion", "saturday"),
    ("W03", "D1", "Mon 12 Oct", "Online project introduction; groups scope their Kalpa Health sub-problem", "build-week"),
    ("W03", "D2", "Tue 13 Oct", "Build day two: profile, clean, reconcile on unfamiliar data", "build-week"),
    ("W03", "D3", "Wed 14 Oct", "Build day three: the headline claim, plus the catch-up reserve", "build-week"),
    ("W03", "D4", "Thu 15 Oct", "Mock R1 opens; build completion", "build-week"),
    ("W03", "D5", "Fri 16 Oct", "Expert day one: GDs at thirty minutes per group, first presentations", "build-week"),
    ("W03", "SAT", "Sat 17 Oct", "Expert day two plus the flown-in leader: presentations, defence, grade closure", "build-week"),
    ("W04", "D1", "Mon 19 Oct", "The number the growth plan chases, and what stops it being gamed", "teaching"),
    ("W04", "TUE", "Tue 20 Oct", "Dussehra (Vijaya Dashami): gazetted holiday, no session", "holiday"),
    ("W04", "D3", "Wed 21 Oct", "Which pairs lift frequency, and what each is worth", "teaching"),
    ("W04", "D4", "Thu 22 Oct", "Why Retail-Plus frequency fell, and where the loss actually happens", "teaching"),
    ("W04", "D5", "Fri 23 Oct", "How much the plan delivers, against a baseline that is hard to beat", "teaching"),
    ("W04", "SAT", "Sat 24 Oct", "Cross-domain transfer drill, then the recap test and discussion", "saturday"),
    ("W05", "D1", "Mon 26 Oct", "Framing the propensity model, and the baseline it has to beat", "teaching"),
    ("W05", "D2", "Tue 27 Oct", "Scoring the model the way the business will judge it, in two businesses", "teaching"),
    ("W05", "D3", "Wed 28 Oct", "What the model is allowed to know", "teaching"),
    ("W05", "D4", "Thu 29 Oct", "Generalise or memorise, and the honest tuned model", "teaching"),
    ("W05", "D5", "Fri 30 Oct", "The committee memo, and what transfers to Kalpa Financial", "teaching"),
    ("W05", "SAT", "Sat 31 Oct", "Revision, the recap test, and the ME1 window", "saturday"),
    ("W06", "D1", "Mon 02 Nov", "Online project introduction; groups frame their Kalpa Financial sub-problem", "build-week"),
    ("W06", "D2", "Tue 03 Nov", "Build day two: baselines beaten honestly, the metric chosen and written down", "build-week"),
    ("W06", "D3", "Wed 04 Nov", "Build day three: honest evaluation and the recommendation, plus the catch-up reserve", "build-week"),
    ("W06", "D4", "Thu 05 Nov", "Mock R2 opens; build completion", "build-week"),
    ("W06", "D5", "Fri 06 Nov", "Expert day one: GDs at thirty minutes per group, first presentations", "build-week"),
    ("W06", "SAT", "Sat 07 Nov", "Expert day two plus the flown-in leader: presentations, defence, grade closure", "build-week"),
    ("W07", "MON", "Mon 09 Nov", "Diwali: Monday off, no session", "holiday"),
    ("W07", "D2", "Tue 10 Nov", "The first network, and whether it earns the text", "teaching"),
    ("W07", "D3", "Wed 11 Nov", "Making the abandoned loop learn", "teaching"),
    ("W07", "D4", "Thu 12 Nov", "Diagnose, then stabilise, then reproduce", "teaching"),
    ("W07", "D5", "Fri 13 Nov", "Reviews as sequences, and why attention won", "teaching"),
    ("W07", "SAT", "Sat 14 Nov", "The pen-and-paper test, then the interview-answer discussion", "saturday"),
    ("W08", "D1", "Mon 16 Nov", "What a ticket costs, and why the vendor bills by the token", "teaching"),
    ("W08", "D2", "Tue 17 Nov", "How the model knows which 'it' the customer means", "teaching"),
    ("W08", "D3", "Wed 18 Nov", "Finding the five tickets most like this one", "teaching"),
    ("W08", "D4", "Thu 19 Nov", "Making the draft reply repeatable, and stopping it inventing", "teaching"),
    ("W08", "D5", "Fri 20 Nov", "The cost model for the auto-reply at scale", "teaching"),
    ("W08", "SAT", "Sat 21 Nov", "The pen-and-paper test, then the interview-answer discussion", "saturday"),
    ("W09", "D1", "Mon 23 Nov", "Online project introduction; groups scope their Kalpa Connect sub-problem", "build-week"),
    ("W09", "TUE", "Tue 24 Nov", "Guru Nanak Jayanti: gazetted holiday, no session", "holiday"),
    ("W09", "D3", "Wed 25 Nov", "The AI-free debug drill, then the build at pace", "build-week"),
    ("W09", "D4", "Thu 26 Nov", "Mock R3 opens, with behavioural questioning; build completion", "build-week"),
    ("W09", "D5", "Fri 27 Nov", "Expert day one: GDs at thirty minutes per group, first presentations", "build-week"),
    ("W09", "SAT", "Sat 28 Nov", "Expert day two plus the flown-in leader: presentations, defence, grade closure, the two-month close", "build-week"),
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


# --------------------------------------------------------------------------- the board itself
def graphql(query, variables):
    """Call the Projects API, which is GraphQL only and is the one thing REST cannot reach."""
    req = urllib.request.Request(
        GRAPHQL,
        data=json.dumps({"query": query, "variables": variables}).encode(),
        method="POST",
        headers={"Authorization": f"Bearer {token()}",
                 "Content-Type": "application/json",
                 "User-Agent": "c2-content-factory-board-sync"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            out = json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise SystemExit(f"FAIL  the Projects API answered {e.code}. "
                         f"{e.read().decode(errors='replace')[:160]}\n"
                         f"      A 403 here almost always means the token has no `project` scope. "
                         f"A Claude Code session is blocked from GraphQL outright, so run this "
                         f"from a Codespace, a laptop, or the board-add workflow.")
    if out.get("errors"):
        why = "; ".join(e.get("message", "") for e in out["errors"])
        raise SystemExit(
            f"FAIL  the Projects API refused the call: {why}\n"
            f"      A Project is reachable only by a classic token carrying the `project` scope. "
            f"A fine-grained token carries no Projects permission for a personal account, and the "
            f"GITHUB_TOKEN an Actions run is given carries none either.")
    return out["data"]


def project_add(number, dry):
    """Put every card on the board. Adding a card that is already there returns that same card, so
    this is a backfill that is safe to run again rather than a one-shot that duplicates."""
    found = graphql(
        f"query($login:String!,$number:Int!){{{OWNER_FIELD}(login:$login)"
        f"{{projectV2(number:$number){{id title}}}}}}",
        {"login": OWNER, "number": number})
    project = (found.get(OWNER_FIELD) or {}).get("projectV2")
    if not project:
        raise SystemExit(f"FAIL  the {OWNER} account has no project number {number}. Create the "
                         f"board first; docs/agents/content-board.md says how in five clicks.")

    issues = [i for i in paged("/issues?state=all") if "pull_request" not in i]
    print(f"      {project['title']} takes {len(issues)} issues")
    added = 0
    for issue in issues:
        if dry:
            print(f"      #{issue['number']} {issue['title'][:64]}")
            continue
        graphql("mutation($p:ID!,$c:ID!){addProjectV2ItemById(input:{projectId:$p contentId:$c})"
                "{item{id}}}", {"p": project["id"], "c": issue["node_id"]})
        added += 1
    print(f"      {added} issues put on the board")
    return added


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


def prune_labels(dry):
    """Delete labels outside the vocabulary that no issue uses.

    GitHub seeds every new repository with nine generic labels. They colour the label picker,
    they overlap with the vocabulary above, and nobody here uses them. A label that is actually
    on an issue is never touched, so this is safe to run again.
    """
    known = {name for name, _, _ in ALL_LABELS}
    removed = kept = 0
    for label in paged("/labels"):
        name = label["name"]
        if name in known:
            continue
        used = call("GET", f"/issues?state=all&per_page=1&labels={urllib.parse.quote(name)}") or []
        if used:
            print(f"      keep {name}, it is on at least one issue")
            kept += 1
            continue
        print(f"      delete unused label {name}")
        removed += 1
        if not dry:
            call("DELETE", f"/labels/{urllib.parse.quote(name)}")
    print(f"      {removed} removed, {kept} left alone because they are in use")


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
                  "board and the curriculum workbook have the same rows.", ""]
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
    ap.add_argument("--prune-labels", action="store_true",
                    help="delete labels outside the vocabulary that no issue uses")
    ap.add_argument("--milestones", action="store_true", help="create a milestone per week")
    ap.add_argument("--week", help="create or update one week's cards, as W01")
    ap.add_argument("--all", action="store_true", help="every week in the plan")
    ap.add_argument("--status", nargs=2, metavar=("TARGET", "STATUS"),
                    help="move a week or a day to a status, as --status W01 rework")
    ap.add_argument("--set-status", default="backlog",
                    help="the status new cards are created with")
    ap.add_argument("--label", action="append", default=[],
                    help="an extra label for every card this run touches")
    ap.add_argument("--project-add", action="store_true",
                    help="put every issue on the Project board, which no other command can do")
    ap.add_argument("--project", type=int, default=PROJECT_NUMBER,
                    help="the board's project number, which is 7 unless a second board exists")
    a = ap.parse_args()
    dry = a.dry_run

    if a.labels:
        sync_labels(dry)
    if a.prune_labels:
        prune_labels(dry)
    if a.milestones:
        sync_milestones(dry)
    if a.project_add:
        project_add(a.project, dry)
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
# scripts/board_sync.py --project-add --dry-run
#     Names every issue the board would take and adds none. Needs a classic token carrying the
#     `project` scope, so it fails on the first call with a fine-grained token or with the
#     GITHUB_TOKEN an Actions run is handed.
# scripts/board_sync.py --project-add
#     Puts every issue on the board. Adding a card that is already there returns that same card,
#     so a second run reports the same total and changes nothing.
# The same command inside a Claude Code session
#     One FAIL line reporting a 403 from the Projects API, because GraphQL is blocked from those
#     sessions whatever the token carries.

"""Refuse a pull-request merge from a session working on a day-pack branch.

Claude Code runs this before any tool whose name matches the PreToolUse matcher in
.claude/settings.json, which covers the GitHub merge and auto-merge tools. A day session works on a
branch named w{ww}-d{d} or w{ww}-sat (or a variant such as w01-d4-rebuild): it pushes its branch and
stops, and the orchestrating session, on its own claude/ branch, reviews the pack, opens the pull
request and merges it. So the merge is refused with exit code 2 when the session's branch starts
with w and two digits, and allowed on every other branch.

The hook reads Claude Code's JSON on stdin for the session's working directory, falls back to
CLAUDE_PROJECT_DIR and then to the current directory, and asks git which branch is checked out
there. When git names none (no repository, a detached HEAD), the merge is allowed, because a day
session always works with its branch checked out.
"""
import json
import os
import re
import subprocess
import sys

DAY_BRANCH = re.compile(r"^w\d{2}-")

REFUSAL = (
    "A day session never merges a pull request. Leave the pull request open, push any last commit to "
    "your branch, and finish with your report: the orchestrating session reviews the pack and merges it."
)


def branch_of(directory):
    """The checked-out branch, even before its first commit; empty on a detached HEAD or no repo."""
    try:
        out = subprocess.run(["git", "-C", directory, "symbolic-ref", "--quiet", "--short", "HEAD"],
                             capture_output=True, text=True, timeout=5)
    except (OSError, subprocess.SubprocessError):
        return ""
    return out.stdout.strip() if out.returncode == 0 else ""


def main():
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        payload = {}
    directory = payload.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    branch = branch_of(directory)
    if DAY_BRANCH.match(branch):
        print(f"{REFUSAL} (This session is on {branch}.)", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())

# Test inputs and expected outcomes:
#
# echo '{"tool_name":"mcp__github__merge_pull_request","cwd":"<a clone on branch w02-d3>"}' | python3 scripts/hooks/day_branch_merge_guard.py
#     Exit 2, and stderr carries the refusal naming w02-d3.
# The same input with cwd on branch w01-d4-rebuild or w03-sat
#     Exit 2: every day-pack branch variant is refused.
# The same input with cwd on branch claude/vigilant-cannon-ukpbs2, or on main
#     Exit 0, and nothing is printed: the orchestrating session may merge.
# echo 'not json' | CLAUDE_PROJECT_DIR=<a clone on branch w01-d1> python3 scripts/hooks/day_branch_merge_guard.py
#     Exit 2: the environment variable stands in when stdin is not JSON.
# echo '{"cwd":"/tmp"}' | python3 scripts/hooks/day_branch_merge_guard.py
#     Exit 0: no repository there, so git names no branch and the merge is allowed.

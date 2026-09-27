"""Package skills from .claude/skills/ as ZIPs that claude.ai's skill upload accepts.

    python3 scripts/package_skills.py day-pack-builder exercise-builder   # named skills
    python3 scripts/package_skills.py --changed-since origin/main          # skills a branch touched
    python3 scripts/package_skills.py --all --out /tmp/skills              # every skill

Each ZIP holds one top-level folder named after the skill, with SKILL.md inside, which is the shape
the upload asks for (Customize, then Skills, then the plus button, then "Create skill", then "Upload
a skill", with code execution on; checked 27 September 2026). The repository copy is never changed.
The upload copy differs in two ways only:

- Its frontmatter keeps the keys the open specification and Anthropic's validator allow (name,
  description, license, compatibility, metadata, allowed-tools) and drops the rest, such as the
  Claude Code keys user-invocable and argument-hint.
- A description over 200 characters, the limit the claude.ai help article states, is replaced by
  its short form from data/skills/claude_ai.yaml. A skill with no short form fails, rather than
  producing a ZIP the upload would refuse.

The ZIPs land in dist/skills/ unless --out says otherwise; dist/ is never committed.
"""
import argparse
import pathlib
import re
import subprocess
import sys
import zipfile

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / ".claude" / "skills"
SHORT = ROOT / "data" / "skills" / "claude_ai.yaml"
ALLOWED = ["name", "description", "license", "compatibility", "metadata", "allowed-tools"]
LIMIT = 200
NAME = re.compile(r"^[a-z0-9-]{1,64}$")
SKIP = {"__pycache__", ".DS_Store"}


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n?", text, re.S)
    if not m:
        raise ValueError("no frontmatter")
    return yaml.safe_load(m.group(1)) or {}, text[m.end():]


def upload_copy(name, short):
    """The SKILL.md text for the upload, plus notes on what changed. Raises on a blocking problem."""
    text = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
    fm, body = frontmatter(text)
    notes = []
    if fm.get("name") != name:
        raise ValueError(f"frontmatter name '{fm.get('name')}' does not match the folder '{name}'")
    if not NAME.match(name) or "claude" in name or "anthropic" in name:
        raise ValueError("the name must be lowercase letters, digits and hyphens, at most 64, "
                         "without 'claude' or 'anthropic'")
    dropped = [k for k in fm if k not in ALLOWED]
    if dropped:
        notes.append("dropped " + ", ".join(dropped))
    fm = {k: fm[k] for k in ALLOWED if k in fm}
    desc = " ".join(str(fm.get("description", "")).split())
    if len(desc) > LIMIT:
        if name not in short:
            raise ValueError(f"the description is {len(desc)} characters, over {LIMIT}, and "
                             f"data/skills/claude_ai.yaml has no short form for it")
        desc = " ".join(str(short[name]).split())
        notes.append(f"short description ({len(desc)} characters)")
    if len(desc) > LIMIT or "<" in desc or ">" in desc:
        raise ValueError("the description is still over the limit or carries angle brackets")
    fm["description"] = desc
    head = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=10_000).strip()
    return f"---\n{head}\n---\n{body}", notes


def package(name, out, short):
    skill_md, notes = upload_copy(name, short)
    out.mkdir(parents=True, exist_ok=True)
    target = out / f"{name}.zip"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted((SKILLS / name).rglob("*")):
            if p.is_dir() or SKIP & set(p.parts) or p.suffix == ".pyc":
                continue
            arc = f"{name}/{p.relative_to(SKILLS / name).as_posix()}"
            if arc == f"{name}/SKILL.md":
                z.writestr(arc, skill_md)
            else:
                z.write(p, arc)
    with zipfile.ZipFile(target) as z:
        roots = {n.split("/")[0] for n in z.namelist()}
        if roots != {name} or f"{name}/SKILL.md" not in z.namelist():
            raise ValueError("the archive does not hold one top-level folder with SKILL.md")
        frontmatter(z.read(f"{name}/SKILL.md").decode("utf-8"))
    return target, notes


def changed_since(ref):
    r = subprocess.run(["git", "diff", "--name-only", f"{ref}...HEAD", "--", ".claude/skills"],
                       cwd=ROOT, capture_output=True, text=True, check=True)
    return sorted({pathlib.Path(p).parts[2] for p in r.stdout.split() if len(pathlib.Path(p).parts) > 2})


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("skills", nargs="*", help="skill folder names under .claude/skills/")
    ap.add_argument("--all", action="store_true", help="every skill in the repository")
    ap.add_argument("--changed-since", metavar="REF", help="skills changed on this branch since REF")
    ap.add_argument("--out", default=str(ROOT / "dist" / "skills"), help="where the ZIPs go")
    a = ap.parse_args()

    names = list(a.skills)
    if a.all:
        names = sorted(p.parent.name for p in SKILLS.glob("*/SKILL.md"))
    if a.changed_since:
        names += changed_since(a.changed_since)
    names = [n for n in dict.fromkeys(names) if (SKILLS / n / "SKILL.md").exists() or
             sys.exit(f"FAIL  no skill named {n} under .claude/skills/")]
    if not names:
        sys.exit("FAIL  name a skill, or pass --all or --changed-since REF")

    short = yaml.safe_load(SHORT.read_text(encoding="utf-8")) if SHORT.exists() else {}
    out, fails = pathlib.Path(a.out), 0
    for n in names:
        try:
            target, notes = package(n, out, short)
            print(f"PASS  {target}" + (f"  ({'; '.join(notes)})" if notes else ""))
        except (ValueError, yaml.YAMLError) as e:
            print(f"FAIL  {n}: {e}")
            fails += 1
    print(f"\nRESULT: {'FAIL' if fails else 'PASS'} ({len(names) - fails} packaged, {fails} failed)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# python3 scripts/package_skills.py day-pack-builder
#     PASS dist/skills/day-pack-builder.zip (short description, 184 characters): one folder,
#     SKILL.md inside with the short description, references/ beside it.
# python3 scripts/package_skills.py seo-content
#     PASS, noting that user-invocable and argument-hint were dropped from the upload copy.
# python3 scripts/package_skills.py grill-me     (a description under 200 and no short form)
#     PASS with no notes.
# A skill whose description is 300 characters and has no entry in data/skills/claude_ai.yaml
#     FAIL naming the length and the missing short form; no ZIP is left claiming to be ready.
# python3 scripts/package_skills.py no-such-skill
#     FAIL: no skill named no-such-skill, exit 1.
# python3 scripts/package_skills.py --changed-since origin/main
#     Packages every skill whose folder changed on the branch.

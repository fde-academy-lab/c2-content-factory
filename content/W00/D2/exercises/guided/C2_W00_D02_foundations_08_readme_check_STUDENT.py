"""Check a project README against the five-heading shape of Figure 32 in the foundations guide.

A project README opens on a title line with one sentence under it, then carries four headings in
this order: What it shows, How to run, Result and What I would do next. Each section holds text,
and the Result holds a table or a number, because the Result is the heading that proves the code
ran. The checker reports the five checks one by one and exits with a code a script can read.

Usage, with this file saved in the Codespace as readme_check.py beside the README:
    python3 readme_check.py README.md
    python3 readme_check.py README.md --trace
    python3 readme_check.py README.md --predict 2,5

--trace prints every heading the checker meets, with its line number, the heading it matches and
the lines of text under it, so a trace written by hand can be compared with the real one.
--predict takes the numbers of the checks you expect to fail (1 the title, 2 What it shows,
3 How to run, 4 Result, 5 What I would do next), or the word none, and says whether the run agreed.

Exit code 0 when all five checks pass, 1 when any check fails, and 2 when the README cannot be read
or the command is written wrongly.
"""
import pathlib
import re
import sys

SECTIONS = ["What it shows", "How to run", "Result", "What I would do next"]
CHECKS = ["the title"] + SECTIONS

HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
# A number standing on its own, such as 360, 1,200 or 0.67. The 1 in Q1 and the 00 in w00 sit inside
# a word, so they do not count as a result.
NUMBER = re.compile(r"(?<![\w.,])\d[\d,]*(?:\.\d+)?(?!\w)")
TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$")
TABLE_RULE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*$")


def name_of(heading):
    """A heading's name in lower case, without a hint in brackets at its end or a closing colon."""
    heading = re.sub(r"\s*\(.*\)\s*$", "", heading)
    return re.sub(r"\s+", " ", heading).strip().rstrip(":").strip().casefold()


def read_sections(lines):
    """Every heading, in file order, as a dictionary with its line, level, text and the lines under it.

    A line inside a code fence or an HTML comment never starts a section, so a Python comment such
    as # clean the rows, pasted into How to run, stays part of that section's text.
    """
    sections, in_fence, in_comment = [], False, False
    for number, line in enumerate(lines, start=1):
        stripped = line.strip()
        starts_fence = stripped.startswith("```")
        heading = None
        if not (in_fence or in_comment or starts_fence):
            heading = HEADING.match(line)
        if heading:
            sections.append({"line": number, "level": len(heading.group(1)),
                             "text": heading.group(2), "body": []})
        elif sections:
            sections[-1]["body"].append(line)
        if starts_fence:
            in_fence = not in_fence
        if not in_fence:
            if stripped.startswith("<!--") and "-->" not in stripped:
                in_comment = True
            elif in_comment and "-->" in stripped:
                in_comment = False
    return sections


def text_lines(body):
    """The lines of a section that carry text, leaving out blank lines and one-line HTML comments."""
    return [line for line in body
            if line.strip() and not (line.strip().startswith("<!--") and line.strip().endswith("-->"))]


def has_table(body):
    return any(TABLE_ROW.match(a) and TABLE_RULE.match(b) for a, b in zip(body, body[1:]))


def has_number(body):
    return any(NUMBER.search(line) for line in text_lines(body))


def matches(section):
    """Which of the five checks a heading belongs to, or None."""
    if section["level"] == 1:
        return "the title"
    for wanted in SECTIONS:
        if name_of(section["text"]) == wanted.casefold():
            return wanted
    return None


def run_checks(sections):
    """The five results in order, each as (number, name, passed, what the checker saw)."""
    results = []
    first = sections[0] if sections else None
    if first is None or first["level"] != 1:
        seen = f'the first heading is "{first["text"]}" at level {first["level"]}' if first else "no heading at all"
        results.append((1, "the title", False, f"no title line starting with a single #; {seen}"))
    else:
        lines = text_lines(first["body"])
        ok = bool(lines)
        results.append((1, "the title", ok,
                        f'"# {first["text"]}", with {len(lines)} line{"s" if len(lines) != 1 else ""} of text under it'
                        if ok else f'"# {first["text"]}", with no sentence under it'))

    last_position, last_name = -1, None
    for number, wanted in enumerate(SECTIONS, start=2):
        found = [i for i, s in enumerate(sections) if s["level"] > 1 and matches(s) == wanted]
        if not found:
            near = [s["text"] for s in sections if s["level"] > 1 and matches(s) is None
                    and name_of(s["text"])[:4] == wanted.casefold()[:4]]
            hint = f'; "## {near[0]}" is the nearest, and the name has to match' if near else ""
            results.append((number, wanted, False, f'no "## {wanted}" heading{hint}'))
            continue
        position = found[0]
        section = sections[position]
        lines = text_lines(section["body"])
        problems = []
        if position < last_position:
            problems.append(f'it sits above "{last_name}"')
        if not lines:
            problems.append("nothing is written under it")
        if wanted == "Result" and lines and not (has_table(section["body"]) or has_number(section["body"])):
            problems.append("it holds no table and no number")
        where = f'line {section["line"]}, {len(lines)} line{"s" if len(lines) != 1 else ""} of text'
        detail = where + ("; " + "; ".join(problems) if problems else "")
        if wanted == "Result" and not problems:
            detail += ", with " + ("a table" if has_table(section["body"]) else "a number")
        results.append((number, wanted, not problems, detail))
        if position > last_position:
            last_position, last_name = position, wanted
    return results


def print_trace(path, sections):
    print(f"The checker's walk through {path}, one row per heading it met:\n")
    print(f"  {'line':>4}  {'level':>5}  {'heading':<44}  {'matches':<22}  lines of text under it")
    for s in sections:
        label = matches(s) or "none of the five"
        text = s["text"] if len(s["text"]) <= 44 else s["text"][:41] + "..."
        print(f"  {s['line']:>4}  {s['level']:>5}  {text:<44}  {label:<22}  {len(text_lines(s['body']))}")
    print()


def read_prediction(words):
    """The check numbers a learner expects to fail, from text such as 3,4 or 3 4 or none."""
    text = " ".join(words).replace(",", " ").strip().casefold()
    if text in ("none", "0"):
        return set()
    numbers = text.split()
    if not numbers or not all(n.isdigit() and 1 <= int(n) <= 5 for n in numbers):
        return None
    return {int(n) for n in numbers}


def say(numbers):
    ordered = [str(n) for n in sorted(numbers)]
    return ordered[0] if len(ordered) == 1 else ", ".join(ordered[:-1]) + " and " + ordered[-1]


def main(argv):
    args = list(argv)
    trace = "--trace" in args
    if trace:
        args.remove("--trace")
    prediction = False
    if "--predict" in args:
        at = args.index("--predict")
        prediction = read_prediction(args[at + 1:])
        args = args[:at]
        if prediction is None:
            print("--predict takes check numbers from 1 to 5, such as --predict 2,5, or the word none.")
            return 2
    if len(args) != 1:
        print("Usage: python3 readme_check.py README.md [--trace] [--predict 2,5]")
        return 2
    path = pathlib.Path(args[0])
    if not path.is_file():
        print(f"No file at {path}. Run the checker from the folder that holds the README, or give its path.")
        return 2

    sections = read_sections(path.read_text(encoding="utf-8").splitlines())
    if trace:
        print_trace(path, sections)

    results = run_checks(sections)
    print(f"README check for {path}\n")
    width = max(len(name) for name in CHECKS)
    for number, name, passed, detail in results:
        print(f"  {number}  {name:<{width}}  {'PASS' if passed else 'FAIL'}  {detail}")
    failed = {number for number, _, passed, _ in results if not passed}
    names = [name for number, name, passed, _ in results if not passed]
    print()
    if failed:
        print(f"{len(failed)} of 5 checks failed: {', '.join(names)}.")
    else:
        print("All 5 checks pass: the five headings are present, in order and written, and the Result shows a result.")

    if prediction is not False:
        if prediction == failed:
            outcome = (f"check{'s' if len(failed) > 1 else ''} {say(failed)} failed" if failed
                       else "no check failed")
            print(f"Your prediction matches the run: {outcome}.")
        else:
            missed, extra = failed - prediction, prediction - failed
            parts = []
            if missed:
                parts.append(f"it missed check{'s' if len(missed) > 1 else ''} {say(missed)}, which failed")
            if extra:
                parts.append(f"it expected check{'s' if len(extra) > 1 else ''} {say(extra)} to fail, "
                             f"and {'they' if len(extra) > 1 else 'it'} passed")
            print(f"Your prediction differs from the run: {', and '.join(parts)}.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

# Test inputs and expected outcomes
# --------------------------------
# Each case below was run with this file under its programme name, from the folder that holds it.
# python3 C2_W00_D02_foundations_08_readme_check_STUDENT.py C2_W00_D02_foundations_08_readme_pass_sample_STUDENT.md
#     Five PASS lines, the Result "with a table", and "All 5 checks pass". Exit 0.
# python3 C2_W00_D02_foundations_08_readme_check_STUDENT.py C2_W00_D02_foundations_08_readme_fail_sample_STUDENT.md
#     Check 3, How to run, fails with nothing written under it, and check 4, Result, fails with
#     "it holds no table and no number"; the last line reads "2 of 5 checks failed: How to run, Result". Exit 1.
# The same failing sample with --predict 2,5
#     The same report, then "Your prediction differs from the run: it missed checks 3 and 4, which
#     failed, and it expected checks 2 and 5 to fail, and they passed." Exit 1.
# The same failing sample with --predict 3,4
#     The same report, then "Your prediction matches the run: checks 3 and 4 failed." Exit 1.
# The same failing sample with --trace
#     A walk of five rows before the same report, one row per heading, each with its line number,
#     level, the check it matches and the lines of text under it. Exit 1.
# Figure 32's skeleton as a README, the five headings with their hints in brackets and nothing under them
#     The title passes on its one sentence, and checks 2 to 5 fail with nothing written under them. Exit 1.
# A README with every section written and Result placed above How to run
#     Only check 4 fails, with "it sits above "How to run"". Exit 1.
# A README that opens on a level-two title and names its fourth heading Results
#     Check 1 fails on the title's level, and check 4 fails with no "## Result" heading and names
#     "## Results" as the nearest. Exit 1.
# python3 C2_W00_D02_foundations_08_readme_check_STUDENT.py ../solutions/C2_W00_D02_foundations_08_github_solution_STUDENT.md
#     The finished README for mini project 1: five PASS lines, the Result with a table. Exit 0.
# No README named on the command line
#     The usage line. Exit 2.
# A README path that does not exist, such as missing.md
#     "No file at missing.md" with the advice to run from the README's folder. Exit 2.
# --predict 7
#     The line saying --predict takes check numbers from 1 to 5, or the word none. Exit 2.

# Provenance: Week 0, Thursday

INTERNAL.

## What the pack was built from

The Thursday row of `docs/curriculum/W0_Baseline_week.md` (tracker v7, 21 September 2026) for the
SQL brush-up's content and its two tracks, the solution-thinking class, the problem card and the
interview angle. The Wednesday row of the same file for the warden's framing class, its Kahoot plan
and its three interview questions, which moved to Thursday with the Wednesday pack. The student Week 0
sheet, `docs/journey/Week_0.md` (version 2, 27 September 2026), for the running order: Python part
two into SQL, a one-hour class on stating a problem, then the SQL brush-up, and an optional practice
set over the Friday holiday. Wednesday's pre-read, which had already told learners what Thursday is.
The four papers retired from Tuesday's pack (commit 4522a40) for the practice set. The requester's
ask of 28 September 2026 for a self-try, self-check mini-project, practice and exploration.

## Checked on 28 September 2026

| Source | What it settled |
|---|---|
| The `devcontainer.json` of GitHub's `codespaces-jupyter` template, which Monday's learners used | The codespace runs `mcr.microsoft.com/devcontainers/universal:2` |
| The universal image's README and its `devcontainer.json` | Ubuntu 24.04, no Postgres among its listed languages and tools, and the user `codespace` set up through the common-utils feature |
| The common-utils feature's README and install script | `sudoers` defaults to true, writing a `NOPASSWD:ALL` entry for the user, so `sudo apt-get` works |
| `apt-cache depends postgresql` on Ubuntu 24.04 in session | The `postgresql` package depends on `postgresql-16` |
| PostgreSQL 16.13, run in session | Every query in the three `.sql` files, the decks, the exercise and the practice set; the setup file's output; the two deliberate failures, `column "Maths" does not exist` and `syntax error at or near "GROUP"`; the error when the server is down; the repeat-step errors; the `library=#` prompt and the pager |
| Python 3.11.15, run in session | The practice set's Python outputs, the mess project's numbers, and the margin table |
| `jupyter nbconvert`, from each notebook's own folder | The demo notebook and the project's worked solution execute cold with every check passing |
| The self-prep page's links, loaded in session | The Python tutorial index, the PostgreSQL tutorial's Chapter 2, SQLBolt, Aced's decomposition guide and Corey Schafer's playlist all answered, with the titles the page quotes |

## Conflicts, and what the pack did

- **The solution-thinking class.** The tracker's Thursday runs a one-hour class on the coaching
  centre: three options, two ruled out, a thin first version. The student sheet gives Thursday's one
  hour to stating a problem instead, which is the warden's class. The pack follows the student sheet:
  the class's move (three options that differ in kind, one with no model, two ruled out, the thinnest
  version) became step 8 of the weekend project, and the coaching-centre case became the first
  exploration prompt on the self-prep page. Its Kahoot plan does not run, and its four interview
  questions sit in the day sheet with their answers.
- **The problem card.** The tracker assigns it on Thursday, due Saturday. The pack assigns it at the
  close of the warden's class, whose four questions it uses.
- **Running a query from VS Code.** The student sheet promises it and the tracker says a practice
  database is opened from VS Code. The pack runs `psql` in VS Code's own terminal, which needs no
  extension; a database extension in the learner's codespace was not verified.
- **Getting Postgres.** Monday's codespace has no Postgres, so the setup sheet installs it with `apt`
  in the first fifteen minutes, following the checks above. The course's own repository, with its own
  container, is not open to learners yet.
- **The practice platform.** The row's after-class task names CodeChef, which
  `data/programme/facts.yaml` holds as an open decision, so no file names a platform.

## Protected for Week 1 and Week 2

Week 2 Monday stages two reveals, the GROUP BY error and `LIMIT` without `ORDER BY`, and Week 2 plants
join duplicates, orphan rows, ranking ties and duplicate keys in Kalpa's warehouse. Thursday's table
has no NULLs, no joins and no ties at the top of any sorted answer; every sort that could tie carries
a second column; and neither Week 2 reveal is staged. The exercise's item 8 avoids `LIMIT` for the
same reason. The Python half stays away from files, the mean and the median, and `.get()` with a
default.

The practice set's Python and numbers parts touch three Week 1 moments: numbers stored as text (item
9), `.get()` with a default (item 10) and a mean pulled away from the median (items 8 and 19). The
diagnostic already spends the same three, in Q1, Q4 and Q22, and the requester chose to keep that and
rework Weeks 1 and 2. The old key's line quoting the GROUP BY error was left out of the self-check key.

## Own constructions

Weeks 3 and 4 of the library table, with Commerce joining in week 3; the mess register and its Rs 40
price; the framing class's fact sheet, its eight statements and the model answer on D9; the Kahoot's
five items; the exercise's twelve items; the weekend project's steps, the weekday rule and its
margins; the Saturday question bank; the four exploration prompts; and the cheat sheet.

## Not verified, and left for the team

- How the day's files reach learners before the course repository opens: the day sheet says to post
  them where learners can copy them.
- Whether a database extension is present in the learner's codespace: the pack does not rely on one.
- Who the Saturday guest is: no name or organisation is in any source, and no file names one.

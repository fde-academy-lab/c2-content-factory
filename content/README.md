# How content/ is laid out

One folder per session. The folder path says which week and which day, the subfolder says what
kind of artifact it is, and the file name says which topic. `scripts/verify.py` enforces all
three, so a pack that invents its own layout fails the gate rather than shipping.

## The week folder

```
content/W01/
  D1/    Monday
  D2/    Tuesday
  D3/    Wednesday
  D4/    Thursday
  D5/    Friday
  SAT/   Saturday
```

Three rules decide which folders exist:

1. **The numbers are anchored to weekdays.** `D1` is always Monday and `D5` is always Friday, in
   every week of the programme, so a reference to D3 means the same weekday wherever you read it.
2. **A day with no session gets no folder.** Week 0 has no `D5` because Friday 2 October is
   Gandhi Jayanti; Week 3 has no `D2` (Dussehra), Week 6 no `D1` (the Monday after Diwali),
   Week 8 no `D2` (Guru Nanak Jayanti) and Week 12 no `D5` (Christmas Day). The gap in the
   numbering is the holiday, and it is deliberate. The board names a holiday's card by its weekday
   (`W03/TUE`), so the same weekday keeps one card whether the calendar makes it a holiday or not.
3. **A capstone week is one folder.** Weeks 17 to 20 are planned at the week level, so each has
   `content/W{ww}/WEEK/` and one board card. Its layout is set when the capstone packs are
   designed, so the verifier checks names and style there and skips the folder shape.

Saturday sits in `SAT/` rather than `D6/`. On a regular week it runs the recap paper and the
discussion, on a build week it is the expert's second day, in Week 0 it closes the baseline week,
and in Week 16 it teaches (security, responsible AI and testing, then the capstone announcement).

`docs/programme/calendar.md` lists every day with its date, slot, kind and module; it is generated
from the tracker, so it is always the calendar the board and the verifier read.

## The three day-folder shapes

### A teaching day, on weeks 1, 2, 4, 5, 7, 8, 10, 11, 13, 14 and 16

| Folder | What belongs in it |
|---|---|
| `slides/` | The deck, as the markdown source and the built pptx, one file per half when the day splits. |
| `notebooks/` | The teaching notebooks, as `.ipynb`, which must run cold top to bottom. |
| `sql/` | The `.sql` files a day runs against the warehouse, one per exercise or demonstration, which must run unchanged in a fresh Codespace. |
| `demos/` | Anything the trainer runs live that is not a notebook: the toggle-driven HTML activity, a script, a prepared terminal session. |
| `whiteboards/` | The board work: markdown walkthroughs, and images of the diagrams and sketches a topic needs, including anything drawn from deeper research than the row carries. |
| `cheatsheets/` | One per major topic the day earns, plus its gap variant. |
| `study-notes/` | The notes a learner reads after the session, revised against the transcript when it arrives. |
| `exercises/` | An index at the root, then `guided/` for what the trainer builds with the room, `unguided/` for what a learner does alone, and `solutions/` for the answers, kept in one folder so they are easy to withhold until the close. |
| `takehome/` | The brief and its self-check spine. |
| `kahoot/` | The day's quiz pack, ungraded. |
| `preread/` | Tomorrow's vocabulary and tonight's setup, which ships the evening before. |
| `extras/` | The tiered stretch and recovery pair. |
| `data/` | Every dataset the day reads, written by `data/generate_client_zero.py` rather than by hand. |
| `trainer/` | The day sheet and the trainer notes. These never reach a learner. |
| `internal/` | Working records: link slots, data provenance, anything that is neither a learner nor a trainer artifact. |
| `corrections/` | Created only when a live claim proved wrong and needs a correction card. |

A warehouse is the exception to one day, one dataset. Week 2's four SQL and pandas days query one
Postgres database, so the loadable file lives once in the first day that uses it,
`content/W02/D1/data/`, and `.devcontainer/load_warehouse.sh` builds the database from it when the
container is created. The later days carry only what they add: the exposure feed on Thursday, the
two exports on Friday.

### A Week 0 day

The baseline week uses the teaching-day folders plus `paper/` and `answer-key/`, which hold
Tuesday's diagnostic, by topic, and its keys. Its running order follows the student Week 0
sheet (`docs/journey/Week_0.md`), which is later than the tracker's Week 0 tab, and its content
follows the tab.

### A build day, on weeks 3, 6, 9, 12 and 15

Build weeks ship the build-week pack rather than the teaching manifest, so their folders are
different: `briefs/`, `rubrics/`, `gd/`, `parallel-build/`, `checkpoints/`, `mocks/`, `trainer/`
and `internal/`. Most of these artifacts are week-level rather than day-level, so each one lives
in the day folder where it is first used: the five sub-problem briefs in `D1/briefs/`, the mock
material in the mock day's `mocks/`, and the GD prompts in the expert days.

### A Saturday

A regular week's Saturday holds `paper/`, `answer-key/`, `discussion/` and, where the paper's
sources are worth recording, `internal/`. A build week's Saturday
uses the build-day folders, since it runs presentations and grade closure rather than a recap.

## File names

```
C2_W{ww}_D{dd}_{topic}_{AUDIENCE}.{ext}
C2_W{ww}_SAT_{topic}_{AUDIENCE}.{ext}
```

The stem is what survives a download, so it stays on every file even though the path repeats it.
The topic half carries only what the folder and the extension do not already say, which is why the
deck is `C2_W01_D02_half1_STUDENT.pptx` in `slides/` rather than repeating the word deck.
`AUDIENCE` is `STUDENT`, `TRAINER` or `INTERNAL`, and it is never omitted, because it is the
mechanism that stops a trainer file reaching a learner.

## Starting a new day

Copy the matching shape from `content/_TEMPLATE/`, which holds four: `teaching-day/`,
`build-day/`, `saturday-recap/` and `saturday-build/`. Then run
`python3 scripts/verify.py content/W{ww}/D{d}` when the pack is built. Empty subfolders are not
pre-created in every day folder, since several hundred placeholder files would bury the ones that
hold work. The template plus the verifier is what keeps the layout honest.

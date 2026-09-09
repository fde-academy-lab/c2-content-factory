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
  SAT/   Saturday
```

Two rules decide which folders exist:

1. **The numbers are anchored to weekdays.** `D1` is always Monday and `D5` is always Friday, in
   every week of the programme, so a reference to D3 means the same weekday wherever you read it.
2. **A day with no session gets no folder.** Week 1 has no `D5` because Friday 02 October is
   Gandhi Jayanti. Week 4 has no `D2` (Dussehra), Week 7 no `D1` (Diwali) and Week 9 no `D2`
   (Guru Nanak Jayanti). The gap in the numbering is the holiday, and it is deliberate.

Saturday sits in `SAT/` rather than `D6/` because it is not a teaching day. On a regular week it
runs the recap paper and the discussion, and on a build week it is the expert's second day.

## The three day-folder shapes

### A teaching day, on weeks 1, 2, 4, 5, 7 and 8

| Folder | What belongs in it |
|---|---|
| `slides/` | The deck, as the markdown source and the built pptx, one file per half when the day splits. |
| `notebooks/` | The teaching notebooks, as `.ipynb`, which must run cold top to bottom. |
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

### A build day, on weeks 3, 6 and 9

Build weeks ship the build-week pack rather than the teaching manifest, so their folders are
different: `briefs/`, `rubrics/`, `gd/`, `parallel-build/`, `checkpoints/`, `mocks/`, `trainer/`
and `internal/`. Most of these artifacts are week-level rather than day-level, so each one lives
in the day folder where it is first used: the five sub-problem briefs in `D1/briefs/`, the mock
material in the mock day's `mocks/`, and the GD prompts in the expert days.

### A Saturday

A regular week's Saturday holds `paper/`, `answer-key/` and `discussion/`. A build week's Saturday
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

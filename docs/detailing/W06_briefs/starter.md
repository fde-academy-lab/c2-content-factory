# Build 2, starter session: the template repository and the breadcrumb notebook

INTERNAL. Read `common.md` first. Branch `w06-starter`. Skills: `notebook-builder` (the rhythm, the
checks, the TODO twin), `scaffold-exercises`, `tdd` (the small tests), `codebase-design` (a shallow,
readable `src/`), `humanizer`.

## What `content/W06/D2/2_starter_repo/` holds

A repository each group copies into its own GitHub repository on Tuesday and opens in Codespaces.
Its files keep real repository names. Write `SETUP` steps at the top of its README: copy the folder
into a new repository, open a Codespace, `pip install -r requirements.txt`, run the first notebook
cell. Keep it small enough that a weak learner understands every file.

| Path | What it is |
|---|---|
| `README.md` | The template a recruiter reads in sixty seconds: the problem in one line, the result with its honest number and caveat, how to run it, the architecture picture, the decisions, the limits, what the MVP adds. Placeholders the group fills, each with a one-line example. |
| `notebooks/breadcrumbs.ipynb` | The only notebook. Sections 1 to 6 follow the ladder (`common.md`). It is executed through loading the data and printing its shape and first rows, then each stage is a question, three sealed hints in collapsed `<details>` blocks (a question, a pointer, a worked parallel on a different problem such as Week 5's bank data), and `__TODO__` code cells. It never names a trap the room must find. |
| `src/data.py`, `src/features.py`, `src/train.py`, `src/score.py` | Short functions with docstrings and `__TODO__` bodies where the group decides, plus one finished helper each so the pattern is clear. `score.py` exposes `score(customer) -> (probability, reason)`. |
| `app/` | The smallest live demo that runs in a Codespace: enter or pick one customer, see the score, the reason and the cost of each error, change the card's number. Choose Streamlit or a notebook widget, verify the version you pin on its own documentation today and date it, and give a fallback that runs with no server. |
| `tests/` | Three or four tests a weak learner can read: the loader returns 30,000 rows, `score` returns a probability between 0 and 1, the error bill of "call nobody" equals the defaulters times the miss cost. |
| `templates/MODEL_CARD.md`, `templates/DECISIONS.md`, `templates/AI_LOG.md`, `templates/CHALLENGES.md` | One page each, with one invented example entry. The model card follows Mitchell and others' sections as `W06_references.md` gives them. |
| `requirements.txt` | Pinned versions you verified today. |

Do not create `2_starter_repo/presentation/`; the run session builds it.

## The solution twin

The breadcrumb notebook's executed solution is the project session's
`4_trainer_only/C2_W06_D02_reference_build_TRAINER.ipynb`; match its stage order and function
names (`load_cards`, `make_features`, `fit`, `error_bill`, `score`) so a trainer can open both side
by side. Write `4_trainer_only/C2_W06_D02_starter_repo_notes_TRAINER.md`: how groups get the repo,
when a TA unseals which hint, and what each `__TODO__` expects.

Run the tests and the notebook's executed cells before you finish.

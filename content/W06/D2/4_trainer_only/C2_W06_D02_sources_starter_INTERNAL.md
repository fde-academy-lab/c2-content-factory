# Starter repo: sources, decisions and the proof it runs

INTERNAL. The starter session's record for `content/W06/D2/2_starter_repo/` and
`4_trainer_only/C2_W06_D02_starter_repo_notes_TRAINER.md`, built on 29 October 2026 on branch
`w06-starter` to `docs/detailing/W06_briefs/starter.md`.

## Which sources does the starter rest on?

| What | Source | Status |
|---|---|---|
| The data, its licence and citation | https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients (checked 29 October 2026) | Read: CC BY 4.0; the variables table X1 to X23 and Y; the dictionary text for X6 to X11 (-1 pay duly, 1 to 9 months late) |
| The download | https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip (checked 29 October 2026) | HTTP 200, 5,539,494 bytes, through Python's urllib in this session |
| The citation's DOI | https://doi.org/10.24432/C55S3H (checked 29 October 2026) | Resolves |
| Every number on the data and the cards | `docs/detailing/W06_research/W06_datasets.md`, measured 29 October 2026 | Used as given; 9,955 and 7,009 measured again here |
| The model card's nine sections | Mitchell and colleagues, Model Cards for Model Reporting, https://arxiv.org/abs/1810.03993 (checked 29 October 2026) | Read in the PDF's Figure 1 |
| Rules of ML, rule 1 | https://developers.google.com/machine-learning/guides/rules-of-ml (checked 29 October 2026) | HTTP 200; wording from `W06_references.md` |
| Requirements in a design doc | https://eugeneyan.com/writing/ml-design-docs/ (checked 29 October 2026) | HTTP 200; link only, as `W06_references.md` advises |
| Systems design | https://madewithml.com/courses/mlops/systems-design/ (checked 29 October 2026) | HTTP 200; link only |
| MLOps levels 0 to 2 | https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning (checked 29 October 2026) | HTTP 200 |
| Template repositories | https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository and https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template (checked 29 October 2026) | Read: Settings, Template repository; Use this template, Create a new repository |
| Streamlit 1.66.0 | https://docs.streamlit.io/develop/quick-reference/release-notes (checked 29 October 2026) | Read: 1.66.0 is the latest the docs list, released 14 October 2026, Python 3.10 dropped |
| Package versions | https://pypi.org/pypi/{package}/json (checked 29 October 2026) | pandas 3.0.6 (17 September 2026), numpy 2.5.4 (10 October 2026, Python 3.12 or later), scikit-learn 1.9.1 (10 September 2026), xlrd 2.0.2 (14 June 2025), joblib 1.6.0 (31 August 2026), streamlit 1.66.0 (14 October 2026), matplotlib 3.11.2 (11 September 2026), pytest 9.1.1 (19 June 2026), ipykernel 7.4.0 (29 September 2026) |
| The Codespace image | https://mcr.microsoft.com/v2/devcontainers/python/tags/list (checked 29 October 2026) | The tag `3.12-bookworm` is listed |
| The SVG namespace | https://www.w3.org/2000/svg (checked 29 October 2026) | HTTP 200 |
| Week 5's bank numbers in hints 3 and the examples | Week 5 notebooks: D01 case 1 and case 2, D02 case 2 and case 3, D03 case 2, D05 case 1, case 2 and case 3 | Read from their markdown cells on 29 October 2026 |

## Which skills shaped it, and what came from each?

| Skill | What was taken |
|---|---|
| notebook-builder | The TODO twin measured on its source, `check()` on shape, a MAP picture first, executed first cells, no plant named in a saved line |
| scaffold-exercises | A problem workspace with the TODOs and a separate solution twin, which is the project session's reference build |
| tdd | Tests at three seams only (`load_cards`, `error_bill`, `score`), worked hand counts as the expected values, no test tied to how a function is written |
| codebase-design | Four shallow files with one interface each; `score(customer, model=None)` accepts its model so a test can pass one in |
| humanizer and llm-tic-scrubber | `tic_scan.py` clean on the notebook's markdown, the README and the four templates |

## Which decisions did the session take, and why?

| Decision | Why |
|---|---|
| Streamlit 1.66.0, with `app/no_server.py` as the fallback | Port forwarding in Codespaces serves it, and its AppTest drives it headless; the fallback prints the same five facts |
| A Python 3.12 Codespace image in `.devcontainer/` | numpy 2.5.4 needs Python 3.12; the factory's own image is 3.11 |
| Pins at least two weeks old where a release allowed it (pandas 3.0.6 over 3.1.0, pytest 9.1.1 over 9.2.0) | A pin a week old has had no time to collect its own bug fixes |
| Tests skip while a function is a `__TODO__`, naming it | A new copy reads `4 skipped`, the suite passes as shipped, and each test runs the moment its function is written |
| `read_raw()` reads the sheet the default way | The first audit then shows the room the sheet as it is, without the starter fixing anything the room is meant to find |
| `TARGET = "default"` in `src/data.py` | One name every file reads; the reference build should use the same |
| `split_book` fixed at 70 to 30, stratified, seed 42 | It reproduces the research split, so the 9,000-customer test book and the card numbers match |
| `MISS_COST` and `WASTED_COST` in `src/train.py` | Card 1's twist is one edit in one place |
| `notebooks/kit.py`, four helpers drawn as SVG | The starter leaves the factory, so it cannot import `scripts/c2kit.py`; `nb_check.py` reads `kit.` calls |
| `.streamlit/config.toml` turning off usage statistics | The demo shows customer rows, and the week teaches governance |
| Hints in `<details>` blocks, unsealed from the checkpoint after the stage is worked | `W06_pedagogy.md` section 2.1 and the plan's Thursday line, architecture revised against the hints |
| Hint 3 always on Week 5's bank | A worked parallel on a different problem teaches the method and never the group's answer |

## What was cut?

- A per-card version of the app: one marked `__TODO__` asks for the card's control instead.
- A data dictionary inside the starter: the UCI page holds it, linked and dated.
- A builder script for the notebook in the pack: it stays outside the repository, and the notebook
  is edited directly if it needs a change.

## How was it proved?

| Run | Result |
|---|---|
| `python -m pytest -rs` on the starter as shipped, Python 3.12 with the pins | 4 skipped, each naming `load_cards` or `error_bill` |
| The same on a scratch copy with every `src/` TODO filled | 4 passed |
| Streamlit AppTest on the shipped app | One warning, "Not ready yet: load_cards ...", no exception |
| AppTest on the filled copy, row 0, miss cost moved from 5 to 20, row 12 | Metric, reason and cost table shown; the missed-default line moved from 0.83 to 3.31 |
| `streamlit run app/app.py` on the filled copy | `/_stcore/health` answered `ok` |
| `python app/no_server.py --row 12 --miss-cost 20` and `--row 9000` | Five lines printed; exit code 2 with the row message |
| The breadcrumb notebook with every TODO filled, run top to bottom | 21 checks PASS, 5 SVG pictures, no error |
| The shipped notebook's first five cells | Shape (30001, 25), both checks PASS |
| `python3 scripts/nb_check.py` on the notebook | TODO twin, 5 diagram calls, 16 check calls, PASS |

## What must other sessions match?

- **Project session, the reference build:** the function names `load_cards`, `make_features`, `fit`,
  `error_bill`, `score`; `TARGET = "default"`; `error_bill(outcome, called, miss_cost=5,
  wasted_cost=1)`; `split_book(cards, seed=42)` at 70 to 30, stratified; `score(customer,
  model=None)` returning `(probability, reason)`; the model saved at `models/model.joblib`.
- **Project session, the workbook:** the notebook points to workbook pages 2, 3, 4 and 6 for
  stages 1, 2, 3 and 5, and the passport's five numbers to the cells in its closing table.
- **Explorer session:** the notebook's hint 2 points to `#p1` to `#p6`.
- **Run session:** `presentation/` sits in the starter beside these files, and the operations TA
  publishes the whole folder as one template repository before Tuesday.

# First use: the Codespace, VS Code and the notebook

Browser first. Everything below happens in a browser tab, and nothing is installed on your laptop. Work through it once and the environment is yours for the whole programme.

Screens are described by what they ask you for rather than by where a button sits, because labels move and positions move with them.

## What you need before you start

A GitHub account you can sign in to, and the repository link the programme gave you. Nothing else.

## The steps

### 1. Open the repository in a browser

Sign in to GitHub and open the programme repository. You should see the file list, with folders named `content`, `data`, `docs` and `scripts`.

### 2. Ask GitHub for a Codespace on this repository

Find the control that offers to open the repository in a codespace. GitHub groups it with the other ways of getting the code, alongside cloning and downloading, and it asks you which branch to start from.

You should see a new browser tab open with a message about preparing a container. The first time takes a few minutes and later times take seconds.

### 3. Read the layout before you touch anything

You should see three regions: a file list down one side, a large empty editor area, and a panel along the bottom that holds a terminal.

The file list is the repository. Everything you open comes from there, and anything you create lands there.

### 4. Open today's notebook

In the file list, open `content/W01/D1/notebooks/` and click `C2_W01_D01_01_kernel_types_STUDENT.ipynb`.

You should see the notebook open as a stack of cells, with the markdown already rendered and every code cell showing the output it was saved with.

### 5. Choose the interpreter the notebook runs on

The notebook asks which kernel to use the first time you run a cell. Pick the Python 3 environment the Codespace already has. You are not installing anything here; you are telling the notebook which Python to talk to.

You should see the kernel name appear in the notebook's own toolbar once it is chosen.

### 6. Run one cell and read the counter

Run the first code cell. You should see a number appear in square brackets beside it.

That number counts the runs the kernel has done, not the position of the cell on the page. Run the same cell three times and the number climbs to three.

### 7. Run the notebook top to bottom

Use run all. You should see every cell get a counter in ascending order, and the final cell print a line saying how many checks passed and how many failed.

### 8. Restart, and watch what happens

Restart the kernel. You should see every counter clear while every output stays on screen.

That gap is the single most useful thing on this page. The outputs are pictures of a kernel that no longer exists, and nothing on the screen says so.

## The traps, each verified by running it

| The trap | What you see | Why it happens | What to do |
|---|---|---|---|
| Running a counting cell before the setup cell | `NameError: name 'records' is not defined` | The kernel was asked for a name nothing had put on the bench. The cell's position on your screen is not something the kernel can see. | Run the cell that defines the name, then run all. |
| Comparing the planted text amount against a number | `TypeError: '>' not supported between instances of 'str' and 'int'` | KR4200's amount arrived as text. The operator has no honest meaning across those two types, so it refuses and names both. | Convert with `int()` where the comparison happens, and leave the record as it arrived. |
| Reading the data file with a path that starts `data/` | `[Errno 2] No such file or directory: 'data/C2_W01_D01_orders_STUDENT.py'` | A notebook runs with its own folder as the working directory, so from `notebooks/` the day's data is one level up. | Use `../data/`, or let the helper's loader find it, which is what `kit.load_records()` does. |
| Trusting an output after a restart | The output is still there and the name behind it is gone | Outputs are saved into the file. Names live in memory. A restart clears one and not the other. | Run all after any restart, and trust nothing until it finishes. |
| Editing a file and running an old cell | The old behaviour, unchanged | The kernel is holding the version it imported, not the version on disk. | Restart and run all, which is the only way to be certain. |

## The probe list

Each of these is one thing you can check, and what it tells you.

| The probe | What it tests |
|---|---|
| `print(len(records))` | Whether the setup cell has actually run on this kernel |
| The execution counters, read top to bottom | Whether the notebook ran in printed order or in some other order |
| Restart, then run all | Whether the notebook works for somebody who is not you |
| `import pathlib; print(pathlib.Path.cwd())` | Which folder your relative paths are counted from |
| The final `check_summary()` line | Whether every check in the notebook passed on this run |

## Cleaning up

A Codespace keeps running after you close the tab, and it counts against your account's hours while it does. Stop it from the same place you started it, where GitHub lists your running codespaces. Your work is saved on the container until you delete it, and anything you want to keep is committed and pushed like any other change.

## The command line, if you prefer it

Everything above has a terminal equivalent in the panel along the bottom. `python3 -c "import pathlib; print(pathlib.Path.cwd())"` answers the working-directory question, and `python3 scripts/verify.py content/W01/D1` runs the same gate the programme runs. The browser path is the one supported for the cohort, and the terminal is there when you want it.

## Reference

- GitHub Docs, Codespaces with Jupyter quickstart (verified 03 Sep 2026): https://docs.github.com/en/codespaces/developing-in-a-codespace/getting-started-with-github-codespaces-for-machine-learning
- VS Code docs, notebooks on the web and in Codespaces (verified 03 Sep 2026): https://code.visualstudio.com/docs/datascience/notebooks-web

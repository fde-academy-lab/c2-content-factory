# First use: files on the Codespace disk

Browser first. Tuesday is the first day your work leaves the kernel and lands on disk, so this page walks the file side of the Codespace once. Screens are described by what they ask for rather than by where a control sits.

## The steps

### 1. Find out where your code is standing

Run this in a cell before you open any file:

```
import pathlib
print(pathlib.Path.cwd())
```

You should see a path ending in `notebooks`. Every relative path you write from now on is counted from that folder.

### 2. Look at the day's data folder from where you are standing

```
import pathlib
for p in sorted(pathlib.Path("../data").iterdir()):
    print(p.name)
```

You should see the five files Tuesday reads: two CSVs, two JSON files and the lab file.

### 3. Make somewhere for your own output to go

```
import pathlib
pathlib.Path("output").mkdir(exist_ok=True)
```

You should see an `output` folder appear in the file list beside your notebook. `exist_ok=True` means running the cell twice is safe, which matters because you will.

### 4. Write a file and reopen it

Write your clean rows, then read them straight back in the same cell. A file you have not reopened is a file you have not written.

### 5. Look at what you wrote, as text

Open the file from the file list rather than from code. You should see the header row you named and one line per record, with commas between the fields.

That is what everybody downstream of you sees, and it is the moment to notice if a field is missing or a value has quotes around it that you did not intend.

## The traps, each verified by running it

| The trap | What you see | Why it happens | What to do |
|---|---|---|---|
| A path that starts `data/` | `[Errno 2] No such file or directory: 'data/C2_W01_D02_orders_STUDENT.csv'` | The notebook is standing in `notebooks/`, so `data/` means `notebooks/data/`, which does not exist. | Use `../data/`, and print the working directory when you are unsure. |
| Writing before the folder exists | `[Errno 2] No such file or directory: 'output/clean.csv'` | `open` for writing creates a file and never creates a folder. | `pathlib.Path("output").mkdir(exist_ok=True)` first. |
| A word where a number belongs | `ValueError: invalid literal for int() with base 10: 'twelve'` | The CSV handed you text and one of those texts is not digits. | Convert at the point of use, catch `ValueError` by name, and log the record with the reason. |
| A JSON file that stops mid-record | `Expecting ',' delimiter: line 48 column 1 (char 1027)` | JSON parses the whole document or none of it. The named line is past the end of the file, which is the parser saying it ran out. | Open the file at its last line, count what the fragment held, and send the sender the exact message. |
| Reopening a file you wrote and finding text | Numbers you wrote come back as `'2180'` | A CSV agrees about columns and nothing else. | Convert on the way in, every time, and say so in the notebook. |

## The probe list

| The probe | What it tests |
|---|---|
| `print(pathlib.Path.cwd())` | Which folder your relative paths are counted from |
| `sorted(pathlib.Path("../data").iterdir())` | Whether the file you are about to open is actually there |
| `len(list(csv.DictReader(open(path))))` | How many rows the reader actually got, before any cleaning |
| `type(row["amount"])` on a reopened file | Whether the format kept your types or flattened them |
| `assert len(clean) + len(rejects) == len(orders)` | Whether any record fell through both branches |

## Cleaning up

Anything you write to `output/` lives on the container. It survives a kernel restart and it does not survive the Codespace being deleted. Commit what you want to keep. Do not commit the generated output files unless a brief asks for them, since they are reproducible from the input and the notebook.

## The command line, if you prefer it

`ls ../data`, `wc -l ../data/C2_W01_D02_orders_STUDENT.csv` and `head -3 output/clean.csv` answer the same three questions from the terminal panel. The browser path is the one supported for the cohort.

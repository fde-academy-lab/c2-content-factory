"""Assemble a teaching notebook from cells, execute it cold in its own folder, and save the outputs.

A notebook ships executed, so a reader on GitHub sees every diagram and check before anybody presses
run. Writing the cells from a short Python script and executing them here keeps a rebuild to one
command, and running inside the notebook's own folder is what a learner's Codespace does, so the
helper import and the `../data/` loaders are proved the way a learner meets them.

    import sys; sys.path.insert(0, "scripts")
    from nb_make import SETUP, md, code, empty, build

    build("content/W01/D1/notebooks/C2_W01_D01_02_first_count_STUDENT.ipynb", [
        md("# The first count ..."),
        code(SETUP + "ORDERS = kit.load_records()"),
        md("**Your turn.** Type these three lines into the empty cell below ..."),
        empty(),
        code("kit.check_summary()"),
    ])

`empty()` is the your-turn cell: it ships with no source, so it carries no saved output and nothing
it would print reaches the page, which is how a notebook points at a planted record without naming
it. `build(..., execute=False)` writes a TODO twin, which stops at its first placeholder by design.
"""
import pathlib
import textwrap

import nbclient
import nbformat

SETUP = '''import sys, pathlib
here = pathlib.Path.cwd()
for parent in [here, *here.parents]:
    if (parent / "scripts" / "c2kit.py").exists():
        sys.path.insert(0, str(parent / "scripts")); break
import c2kit as kit
'''


def md(text):
    """A markdown cell, with the common indentation of a triple-quoted string removed."""
    return nbformat.v4.new_markdown_cell(textwrap.dedent(text).strip("\n"))


def code(src):
    """A code cell, with the common indentation removed."""
    return nbformat.v4.new_code_cell(textwrap.dedent(src).strip("\n"))


def empty():
    """The your-turn cell: no source, so no output is saved into it."""
    return nbformat.v4.new_code_cell("")


def build(path, cells, execute=True, timeout=120):
    """Write the notebook at path, executed in its own folder unless execute is False."""
    path = pathlib.Path(path)
    nb = nbformat.v4.new_notebook()
    nb.metadata = {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.11"},
    }
    nb.cells = cells
    if execute:
        client = nbclient.NotebookClient(nb, timeout=timeout, kernel_name="python3",
                                         resources={"metadata": {"path": str(path.parent)}})
        client.execute()
    for i, cell in enumerate(nb.cells):
        cell["id"] = f"c{i:02d}"
        if cell.cell_type == "code" and not cell.source:
            cell.outputs = []
            cell.execution_count = None
    nbformat.write(nb, str(path))
    return nb

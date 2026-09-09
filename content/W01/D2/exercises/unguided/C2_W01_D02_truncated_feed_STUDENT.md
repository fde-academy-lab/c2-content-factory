# Day 2 unguided exercise: read what the parser is pointing at

Where the files are: your notebook sits in `notebooks/`, so the day's data is one folder up in `../data/` and anything you write goes into `output/` beside your notebook.

Drop point: the break in the second half. About 15 minutes. Open the file, do not repair it.

Run this and read what comes back:

```
import json
with open("../data/C2_W01_D02_vendor_truncated_STUDENT.json") as f:
    records = json.load(f)
```

You get:

```
json.decoder.JSONDecodeError: Expecting ',' delimiter: line 48 column 1 (char 1027)
```

1. Open the file and go to line 48. Write down what you find there.
2. How many lines does the file actually have? Use Python to check rather than scrolling.
3. Given your answer to 1 and 2, say in one sentence what happened to this file.
4. The parser named a position. Is the defect at that position? Explain the difference between where a parser stops and where a file went wrong.
5. You cannot reach the vendor until tomorrow and your manager wants the other records now. Write the one sentence you would send back, and say what you would refuse to do.
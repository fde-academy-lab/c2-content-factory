# Cheat sheet, gap variant: errors and files

Same eight panels with a quarter of the cells blanked. Fill it from memory first, then check against the full sheet. Filling it in twice a week is worth more than reading it ten times.

---

## Panel 1: read a traceback

Read from the __________ up.

| Line | Question it answers |
|---|---|
| Last | ________________________________ |
| Naming your file | Where you edit |
| Above that | How you got here |

Three questions every time: exception type, my line, and ________________.

**Crux:** _______________________________________________.

---

## Panel 2: return against print

```
def f(r): print(r["order_id"])      # hands back ______
def g(r): return r["order_id"]      # hands back ______
```

`print` is for ________________. `return` is for ________________.

**Crux:** if the caller needs the answer, the function ____________.

---

## Panel 3: catch narrowly

```
try:
    value = int(raw)
except ______________ as e:
    rejects.append({"id": rid, "reason": ________})
```

| Catch | What it survives | What it hides |
|---|---|---|
| `except ValueError` | The failure you predicted | Nothing |
| `except:` | ______________ | ______________________________ |

**Crux:** a crash costs ________, a plausible wrong number costs ________.

---

## Panel 4: the reconciliation

```
assert len(clean) + len(________) == len(________)
```

**Crux:** input equals ____________________, or something disappeared.

---

## Panel 5: the four errors of Day 2

| Error | It means |
|---|---|
| `TypeError: 'NoneType' object is not subscriptable` | ______________________________ |
| `ValueError: invalid literal for int() ...` | A word arrived where a number belonged |
| `FileNotFoundError: [Errno 2] ...` | ______________________________ |
| `JSONDecodeError: ... line N column M` | The parser ran out of valid input there |

**Crux:** every one of these names ____________________.

---

## Panel 6: opening files

```
with open(path) as f:
```

The ________ is guaranteed, including when your code ________ inside the block.

Paths are relative to ________________________.

**Crux:** `FileNotFoundError` prints ____________________.

---

## Panel 7: CSV and JSON

| | CSV | JSON |
|---|---|---|
| Agrees about | ______________________ | Types and nesting |
| Types | Everything is ________ | Numbers stay numbers |
| Nesting | ________________ | Native |
| Partial read | Possible | ________________ |

`csv.DictReader` keys come from ____________________.

**Crux:** everything a CSV agrees to is ________, so conversion is ____________________.

---

## Panel 8: one pass, two files

```
______________   what converted
______________   what did not, and why
```

**Crux:** writing a file is not finishing. ____________________ is finishing.

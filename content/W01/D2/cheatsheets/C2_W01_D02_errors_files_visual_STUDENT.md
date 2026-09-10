# Visual sheet: functions, failures and the file boundary

Week 1, Day 2. Print landscape. Six panels, pictures only. The text sheet beside this one carries the words.

---

## Panel 1: what a function hands back

```mermaid
flowchart LR
    A["the caller"] --> B["your function"]
    B -->|"print"| C["your screen"]
    B -->|"no return"| D["None goes back"]
    B -->|"return"| E["the value goes back"]
    E --> F["the next line can use it"]
    D --> G["the next line raises"]
```

**Crux:** if the caller needs the answer, the function returns it.

---

## Panel 2: reading a traceback

```mermaid
flowchart TB
    A["the last line"] --> B["the exception type and the message"]
    B --> C["which line is mine?"]
    C --> D["what was it holding?"]
    D --> E["the record that broke it"]
```

**Crux:** read the last line first, every time.

---

## Panel 3: three stances on the same bad row

```mermaid
flowchart TB
    A["int('twelve') raises"] --> B["no handler: the run stops"]
    A --> C["except: pass: Rs 53,745 claimed from 30 records"]
    A --> D["except ValueError: Rs 53,745 from 28 of 30, stated"]
    B --> E["expensive and honest"]
    C --> F["cheap and false"]
    D --> G["the one you ship"]
```

**Crux:** a bare except turns a failure into a claim you cannot support.

---

## Panel 4: who decides what a failure means

```mermaid
flowchart TB
    A["normalise_amount converts or refuses"] --> B["the nightly batch skips the row and logs it"]
    A --> C["the submission refuses and names the field"]
    D["one function deciding for both"] -.->|"wrong for one of them"| A
```

**Crux:** convert or refuse in the function, decide what it means in the caller.

---

## Panel 5: two agreements about structure

```mermaid
flowchart LR
    subgraph csv["CSV"]
      C1["columns only"] --> C2["everything is text"]
      C2 --> C3["a truncated file keeps its earlier rows"]
    end
    subgraph json["JSON"]
      J1["types and nesting"] --> J2["numbers stay numbers"]
      J2 --> J3["a truncated file yields nothing"]
    end
```

**Crux:** everything a CSV agrees to is text, and JSON breaks all at once.

---

## Panel 6: the reconciliation

```mermaid
flowchart LR
    A["30 rows in"] --> B["28 clean"]
    A --> C["2 rejected, each with a reason"]
    B --> D{"28 + 2 = 30?"}
    C --> D
    D -->|"yes"| E["the count is defensible"]
    D -->|"no"| F["a record went missing, stop"]
```

**Crux:** a record in neither file is a record nobody will ever look for again.

---

The landscape PDF of this sheet is deferred. The rendering toolchain the `fde-cheat-sheets` method uses was not installed in the session that built this file, and the markdown with its six panels is the shipped artifact until it is.

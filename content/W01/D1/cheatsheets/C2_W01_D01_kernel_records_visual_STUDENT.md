# Visual sheet: the kernel, the type and the accumulator

Week 1, Day 1. Print landscape. Six panels, pictures only. The text sheet beside this one carries the words; this one is what you redraw from memory.

---

## Panel 1: the bench

```mermaid
flowchart LR
    A["you click a cell"] --> B["the kernel runs it"]
    B --> C["names go on the bench"]
    C --> D["the next cell reads them"]
    D -->|"restart"| E["the bench is empty again"]
    E --> A
```

**Crux:** the kernel holds exactly what you gave it, in the order you gave it.

---

## Panel 2: the order that matters

```mermaid
flowchart TB
    subgraph screen["on your screen"]
      S1["cell 1 setup"] --> S2["cell 2 count"] --> S3["cell 3 total"]
    end
    subgraph kernel["what the kernel ran"]
      K1["[1] cell 3"] --> K2["[2] cell 1"] --> K3["[3] cell 2"]
    end
    K1 --> X["NameError: records not set"]
```

**Crux:** the number in square brackets counts runs, and it is the only order the kernel knows about.

---

## Panel 3: type decides what the operator means

```mermaid
flowchart TB
    A["'4500' > 2000"] --> B{"same type?"}
    B -->|"yes"| D["a bool comes back"]
    B -->|"no"| C["TypeError, both types named<br/>int() at the point of use"]
    C --> D
```

**Crux:** convert at the point of use, so the record still shows what the source sent.

---

## Panel 4: the accumulator, and the one place it can start

```mermaid
flowchart TB
    A["total = 0"] --> B["for every order"]
    B --> C{"does it qualify?"}
    C -->|"yes"| D["total = total + amount"]
    C -->|"no"| B
    D --> B
    B --> E["print total"]
    F["total = 0 here instead"] -.->|"keeps one record"| D
```

**Crux:** a total that equals one record's amount is a reset inside the loop.

---

## Panel 5: what to check, and in what order

```mermaid
flowchart TB
    B{"did anything print?"} -->|"no"| C["read the last traceback line"]
    C --> D["NameError: run that cell<br/>TypeError: fix the type"]
    B -->|"yes"| F{"beats its largest member?"}
    F -->|"no"| G["a reset in the loop"]
    F -->|"yes"| H["check before sending"]
```

**Crux:** nothing on screen flags a wrong number, so the check has to come from you.

---

## Panel 6: the shape every answer takes

```mermaid
flowchart TB
    A["a list of records"] --> B["one walk"]
    B --> C["one condition"]
    C --> D["two accumulators"]
    D --> E["a count and a total"]
    E --> F["a sentence naming the group"]
```

**Crux:** a count without its group is not an answer to anything.

---


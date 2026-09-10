# Visual sheet: typical, spread and the count underneath

Week 1, Day 4. Print landscape. Six panels, pictures only. The text sheet beside this one carries the words.

---

## Panel 1: three answers to one question

```mermaid
flowchart LR
    A["what is typical?"] --> B["mean: share the total out equally"]
    A --> C["median: the one standing in the middle"]
    A --> D["mode: the exact value that repeats most"]
    B --> E["every value takes part, so one huge value drags it"]
    C --> F["only the middle position matters"]
    D --> G["on money, almost nothing repeats"]
```

**Crux:** the shape of the column decides which of the three is honest.

---

## Panel 2: what one order does

```mermaid
flowchart TB
    A["44 orders"] --> B["mean Rs 12,753"]
    A --> C["median Rs 1,910"]
    B --> D["1 of the 44 reaches it"]
    C --> E["22 sit either side of it"]
    F["take KR4232 out"] --> G["mean falls to about Rs 1,720"]
```

**Crux:** a mean that only one record reaches is a number about that record.

---

## Panel 3: reading the shape with no chart

```mermaid
flowchart TB
    A["sort the column"] --> B["distance from median down to min"]
    A --> C["distance from median up to max"]
    B --> D{"which is larger?"}
    C --> D
    D -->|"up"| E["a long right tail, mean above median"]
    D -->|"down"| F["a long left tail, mean below median"]
    D -->|"about equal"| G["roughly symmetric"]
```

**Crux:** skew reads off sorted values, with no library and no formula.

---

## Panel 4: spread, and what each measure is made of

```mermaid
flowchart TB
    A["range: max minus min"] --> B["built from the two least typical values"]
    C["interquartile range: the middle half"] --> D["ignores both tails on purpose"]
    D --> E["the fence, for spotting a tail quickly"]
    E --> F["a convenience, never a test"]
```

**Crux:** the fence spots the tail, and it proves nothing about the row it catches.

---

## Panel 5: one event, three denominators

```mermaid
flowchart LR
    A["one more return"] --> B["on 12 records: 8.3 points"]
    A --> C["on 120 records: 0.8 points"]
    A --> D["on 1,200 records: 0.1 points"]
    B --> E["the rate is measuring the denominator"]
    D --> F["the rate is measuring the business"]
```

**Crux:** every rate travels with the count it rests on.

---

## Panel 6: what leaves your desk

```mermaid
flowchart LR
    A["the number"] --> D["the honest sentence"]
    B["what it describes"] --> D
    C["the count it rests on"] --> D
    D --> E["and a flag on anything that owns it"]
```

**Crux:** the deliverable is the sentence, and the table is the working.

---


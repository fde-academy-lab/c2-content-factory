# Visual sheet: profile, decide, record

Week 1, Day 3. Print landscape. Six panels, pictures only. The text sheet beside this one carries the words.

---

## Panel 1: three counts per field

```mermaid
flowchart LR
    A["one column"] --> B["present: the box has something"]
    A --> C["converts: what is in it is usable"]
    A --> D["distinct: what kind of field this is"]
    B --> E["present minus converts is your work list"]
    C --> E
```

**Crux:** distinct is the only count that can fall, so it is the only count that can warn you.

---

## Panel 2: reading a profile as a shape

```mermaid
flowchart TB
    A["distinct 3 or 4 on 50 rows"] --> B["a category"]
    C["distinct near the row count"] --> D["an id or a free value"]
    E["distinct below the row count on an id"] --> F["something repeats that should not"]
    G["converts 0 on a text field"] --> H["correct, and not a failure"]
```

**Crux:** you know where the work is before you have touched anything.

---

## Panel 3: missing is a three-way decision

```mermaid
flowchart TB
    A["a field is incomplete"] --> B{"what does the absence mean?"}
    B -->|"nothing happened"| C["keep absent, flag it, log the meaning"]
    B -->|"the field is required"| D["reject the row with its reason"]
    B -->|"you cannot say"| E["that is the question to ask, not a default to apply"]
```

**Crux:** a default you did not state is data you invented.

---

## Panel 4: the coercion trap

```mermaid
flowchart LR
    A["48 present, 44 converts, 46 distinct"] --> B["coerce everything to 0"]
    B --> C["50 present, 50 converts, 41 distinct"]
    C --> D["two counts rose and looked like progress"]
    C --> E["one count fell, and it was the only warning"]
```

**Crux:** a pass that never fails is a pass that destroyed the evidence.

---

## Panel 5: an identity rule is something you state

```mermaid
flowchart TB
    A["two rows share KR4201"] --> B["every field: 0 groups"]
    A --> C["order_id alone: 1 group"]
    A --> D["order_id plus order_date: 0 groups"]
    B --> E["the rule is the decision, the number follows"]
    C --> E
    D --> E
```

**Crux:** the data cannot tell you what the same record means, so somebody has to.

---

## Panel 6: what ships

```mermaid
flowchart LR
    A["50 orders in"] --> B["44 clean"]
    A --> C["6 rejected, each with its reason"]
    B --> D["the decisions log"]
    C --> D
    D --> E["a reviewer can rebuild your count without asking you"]
```

**Crux:** what ships is the data plus every decision taken on it.

---

The landscape PDF of this sheet is deferred. The rendering toolchain the `fde-cheat-sheets` method uses was not installed in the session that built this file, and the markdown with its six panels is the shipped artifact until it is.

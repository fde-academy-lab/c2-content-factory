# Board diagrams: Week 1, Day 4

Every diagram the day uses, as a fence a trainer can draw from and a learner can redraw.

## 1. Three answers to what is typical

```mermaid
flowchart LR
    A["what is typical?"] --> B["mean"]
    A --> C["median"]
    A --> D["mode"]
    B --> E["uses every value"]
    C --> F["uses only the middle position"]
    D --> G["uses only exact repeats"]
```

## 2. The whale

```mermaid
flowchart TB
    A["43 ordinary orders, Rs 800 to Rs 2,995"] --> C["mean Rs 12,753"]
    B["KR4232 at Rs 480,000"] --> C
    C --> D["1 of the 44 reaches it"]
    A --> E["median Rs 1,910"]
    B --> E
    E --> F["and the median barely moved"]
```

## 3. Reading skew off sorted values

```mermaid
flowchart LR
    A["min"] --> B["median"]
    B --> C["max"]
    A -.->|"short"| B
    B -.->|"long"| C
    C --> D["a long right tail"]
```

## 4. Spread, three ways

```mermaid
flowchart TB
    A["min and max"] --> B["range, from the two least typical values"]
    C["the middle half"] --> D["interquartile range"]
    D --> E["the fence: q3 plus 1.5 times the IQR"]
    E --> F["catches one order, and proves nothing about it"]
```

## 5. Grouping without knowing the keys

```mermaid
flowchart TB
    A["a dictionary you typed out"] --> B["a segment you did not expect"]
    B --> C["KeyError"]
    D["an empty dictionary"] --> E["a segment you did not expect"]
    E --> F["build the key, then count"]
```

## 6. One event, three denominators

```mermaid
flowchart LR
    A["one more return"] --> B["12 records: 8.3 points"]
    A --> C["120 records: 0.8 points"]
    A --> D["1,200 records: 0.1 points"]
```

## 7. The ranking, and what it measures

```mermaid
flowchart TB
    A["rank the segments by return rate"] --> B["Business 11.1% on 9"]
    A --> C["Student 20.0% on 10"]
    A --> D["Retail-Core 35.7% on 14"]
    A --> E["Retail-Plus 36.4% on 11"]
    B --> F["the two best are the two smallest"]
    C --> F
```

## 8. The honest sentence

```mermaid
flowchart LR
    A["the number"] --> E["one sentence somebody repeats"]
    B["what it describes"] --> E
    C["the count it rests on"] --> E
    D["a flag on whatever owns it"] --> E
```

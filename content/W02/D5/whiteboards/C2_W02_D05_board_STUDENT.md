# The board, Week 2 Friday

The drawings in the order they go up. Each is small enough to draw in a minute and stays up until
the end of the day, so by the close the board holds the whole last mile.

---

## 1. Where Excel sits, drawn during the ask

The first drawing, and the one the afternoon's operating rule is read from.

```mermaid
flowchart LR
    W["<b>warehouse</b><br/>computes and cleans"] --> P["<b>pandas</b><br/>the analyst's iteration"]
    W --> X["<b>export</b><br/>one grain, dated"]
    P --> X
    X --> E["<b>Excel</b><br/>presents and explores"]
    E -.->|"never typed back"| W
```

## 2. Four places a sheet lies, drawn during the ask

Draw the four boxes in rose. Each turns green as its round fixes it.

```mermaid
flowchart TB
    S["<b>the sheet a director opens</b>"] --> G["<b>the grain</b><br/>rows or orders"]
    S --> L["<b>the lookup</b><br/>found or neighbour"]
    S --> V["<b>the total</b><br/>visible or all"]
    S --> C["<b>the card</b><br/>period and base"]
    classDef bad fill:#FCEBF0,stroke:#D63A6A,color:#1A0F5C
    class G,L,V,C bad
```

## 3. Three grains, round 1

```mermaid
flowchart LR
    C["<b>customer table</b><br/>1 row per customer<br/>300 rows"] --- O["<b>warehouse</b><br/>1 row per order<br/>1,000 orders"] --- P["<b>raw export</b><br/>1 row per payment<br/>1,450 rows"]
```

Write under it: a Sum adds one value per row, so the grain decides what it counts.

## 4. From the warehouse to the hurried pivot, round 1

```mermaid
flowchart LR
    W["<b>warehouse</b><br/>Rs 19.84 crore"] -->|"+ second instalment rows"| I["<b>still rising</b>"]
    I -->|"+ gateway copies"| H["<b>hurried pivot</b><br/>Rs 39.41 crore"]
    H -->|"count each order once"| F["<b>fixed tree</b><br/>Rs 19.84 crore"]
    classDef good fill:#E8F5EE,stroke:#1F8A5B,color:#1A0F5C
    class F good
```

Write the flag beside it: `=IF(COUNTIF($A$2:A2,A2)=1,1,0)`.

## 5. A lookup has two exits, round 2

```mermaid
flowchart LR
    I["<b>id typed in</b>"] --> M{"<b>match</b>"}
    M -->|"exact, found"| F["<b>the member's row</b>"]
    M -->|"exact, missing"| N["<b>not in the table</b>"]
    M -.->|"approximate, missing"| B["<b>a neighbour's row</b><br/>no warning"]
    classDef bad fill:#FCEBF0,stroke:#D63A6A,color:#1A0F5C
    class B bad
```

## 6. The foot of a filtered list, round 2

| At the foot | Rows a filter hid | Rows hidden by hand | Mumbai, filtered |
|---|---|---|---|
| `SUM` | added | added | Rs 7,14,890 |
| `SUBTOTAL(109)` | left out | left out | Rs 1,56,790 |

## 7. The card, round 3

```mermaid
flowchart LR
    N["<b>number</b><br/>Rs 9.84 crore"] --> P["<b>period</b><br/>Q2, Jul to Sep"] --> C["<b>comparison</b><br/>down 1.6% on Q1"] --> B["<b>base</b><br/>share of revenue"] --> S["<b>sentence</b><br/>where it moved"]
```

## 8. What a typed-over cell does, the second case

```mermaid
flowchart LR
    E["<b>export</b><br/>Rs 4.13 lakh"] --> S["<b>typed cell</b><br/>Rs 5.00 lakh"] --> C["<b>card</b><br/>down 14.6%"]
    E -.->|"Monday refresh"| W["<b>edit wiped</b><br/>down 29.4%"]
    classDef bad fill:#FCEBF0,stroke:#D63A6A,color:#1A0F5C
    class S,C bad
```

---

## On the board when the day ends

Drawing 2 with all four boxes green, drawing 1 with the dashed arrow crossed out, and the operating
rule in three lines beside them:

1. The warehouse owns the number.
2. pandas owns the iteration.
3. Excel owns the last mile, and nobody types over the source.

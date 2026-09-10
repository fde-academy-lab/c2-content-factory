# Board diagrams: Week 1, Day 1

Every diagram the day uses, as a fence a trainer can draw from and a learner can redraw. The same shapes appear on the slides, in the notebooks and on the companion page, so a learner meets one drawing three times rather than three drawings once.

## 1. The bench

Draw this first, before any code runs. The whole day hangs off it.

```mermaid
flowchart LR
    A["you click a cell"] --> B["the kernel runs it"]
    B --> C["names go on the bench"]
    C --> D["the next cell reads them"]
    D -->|"restart"| E["the bench is empty"]
    E --> A
```

## 2. The two orders

The order on the screen and the order the kernel saw are two different things, and this is the drawing that separates them.

```mermaid
flowchart TB
    subgraph screen["what the screen shows"]
      S1["cell 1: setup"] --> S2["cell 2: count"] --> S3["cell 3: total"]
    end
    subgraph kernel["what the kernel did"]
      K1["run [1]: cell 3"] --> K2["run [2]: cell 1"] --> K3["run [3]: cell 2"]
    end
    K1 --> X["NameError: name 'records' is not defined"]
```

## 3. Type decides the operator

```mermaid
flowchart TB
    A["'4500' > 2000"] --> B{"are both sides the same kind of thing?"}
    B -->|"no"| C["TypeError, and both types are named"]
    B -->|"yes"| D["True or False comes back"]
    C --> E["int() where the comparison happens"]
    E --> D
    F["the record still holds '4500'"] -.-> E
```

## 4. The accumulator

```mermaid
flowchart TB
    A["total = 0"] --> B["take the next order"]
    B --> C{"does it qualify?"}
    C -->|"yes"| D["total = total + the amount"]
    C -->|"no"| B
    D --> B
    B --> E["print total"]
    F["total = 0 here instead"] -.->|"keeps only the last one"| D
```

## 5. A list of dictionaries

```mermaid
flowchart LR
    L["records, a list"] --> R0["records[0]"]
    L --> R1["records[1]"]
    L --> R29["records[29]"]
    R0 --> K1["order_id"]
    R0 --> K2["segment"]
    R0 --> K3["amount"]
    R0 --> K4["status"]
```

## 6. The absent key

```mermaid
flowchart TB
    A["r['discount']"] --> B{"does this record carry it?"}
    B -->|"yes, 2 of 30"| C["the value the file holds"]
    B -->|"no, 28 of 30"| D["KeyError, and the loop stops"]
    D --> E["r.get('discount', 0)"]
    E --> F["Rs 250 reported, which is what the file holds"]
    E --> G["default 100 instead: Rs 3,050 reported, Rs 2,800 invented"]
```

## 7. The diagnosis order

```mermaid
flowchart TB
    A["your cell has run"] --> B{"did anything print?"}
    B -->|"no"| C["read the last line of the traceback first"]
    C --> D["NameError: run the cell that defines the name"]
    C --> E["TypeError: check the type of both operands"]
    B -->|"yes"| F{"does the total beat its largest member?"}
    F -->|"no"| G["a reset sits inside the loop"]
    F -->|"yes"| H["run the invariant, then send it"]
```

## 8. The day, end to end

The position bar the deck repeats at every section boundary.

```mermaid
flowchart LR
    A["open the workbench"] --> B["the kernel remembers"]
    B --> C["type decides"]
    C --> D["walk the records"]
    D --> E["the business answer"]
```

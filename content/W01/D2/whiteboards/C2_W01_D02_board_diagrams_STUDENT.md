# Board diagrams: Week 1, Day 2

Every diagram the day uses, as a fence a trainer can draw from and a learner can redraw. The same shapes appear on the slides, in the notebooks and on the companion page.

## 1. What a function hands back

```mermaid
flowchart LR
    A["the caller"] --> B["your function"]
    B -->|"print"| C["your screen"]
    B -->|"no return"| D["None goes back to the caller"]
    B -->|"return"| E["the value goes back"]
```

## 2. Reading a traceback, bottom up

```mermaid
flowchart TB
    A["the last line: the exception and the message"] --> B["the frame above it: which line is mine"]
    B --> C["the value in the message: what it was holding"]
    C --> D["the record that broke it"]
```

## 3. The three stances

```mermaid
flowchart TB
    A["int(r['amount']) raises"] --> B["no handler: the loop stops here"]
    A --> C["except: pass: the loop continues and the claim becomes false"]
    A --> D["except ValueError: the loop continues and the count stays true"]
```

## 4. Validate early, catch narrowly, log the rejection

```mermaid
flowchart LR
    A["one record"] --> B{"does the amount convert?"}
    B -->|"yes"| C["clean.append(record)"]
    B -->|"no"| D["rejects.append(id and reason)"]
    C --> E["clean.csv"]
    D --> F["rejects.csv"]
```

## 5. The reconciliation

```mermaid
flowchart LR
    A["30 in"] --> B["28 clean"]
    A --> C["2 rejected"]
    B --> D{"28 + 2 = 30?"}
    C --> D
    D -->|"no"| E["stop, a record went missing"]
```

## 6. Where a relative path is counted from

```mermaid
flowchart TB
    A["the notebook you opened"] --> B["its own folder, notebooks/"]
    B --> C[".. goes up one, to the day folder"]
    C --> D["../data/ is where the day's files live"]
    B --> E["'data/orderz.csv' looked inside notebooks/ and found nothing"]
```

## 7. Two agreements about structure

```mermaid
flowchart LR
    subgraph csv["CSV"]
      C1["columns"] --> C2["all text"]
    end
    subgraph json["JSON"]
      J1["types"] --> J2["nesting"]
    end
    C2 --> X["you convert at the boundary"]
    J2 --> Y["one missing bracket loses the file"]
```

## 8. The day, end to end

```mermaid
flowchart LR
    A["a rule you wrote three times"] --> B["the rule gets a name"]
    B --> C["it returns rather than prints"]
    C --> D["it survives the failure you expected"]
    D --> E["and the rejection is a deliverable"]
```

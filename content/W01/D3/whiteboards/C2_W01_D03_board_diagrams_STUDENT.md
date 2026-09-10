# Board diagrams: Week 1, Day 3

Every diagram the day uses, as a fence a trainer can draw from and a learner can redraw.

## 1. The profiler, as two loops and a set

```mermaid
flowchart TB
    A["for every field in the header"] --> B["for every row"]
    B --> C{"is the value anything at all?"}
    C -->|"yes"| D["present + 1"]
    C -->|"no"| E["absent"]
    D --> F{"does it convert?"}
    F -->|"yes"| G["converts + 1"]
    F -->|"no"| H["present and unusable"]
    D --> I["add the value to a set"]
    I --> J["distinct is the size of that set"]
```

## 2. The three counts as a work list

```mermaid
flowchart LR
    A["present"] --> D["present minus converts"]
    B["converts"] --> D
    D --> E["the rows that look filled in and are not"]
    C["distinct"] --> F["what kind of field this is"]
```

## 3. Missing is a three-way decision

```mermaid
flowchart TB
    A["a field is incomplete"] --> B{"what does the absence mean?"}
    B -->|"nothing happened"| C["keep absent, flag it"]
    B -->|"required to compute"| D["reject the row with its reason"]
    B -->|"you cannot say"| E["ask, do not default"]
```

## 4. The coercion trap

```mermaid
flowchart LR
    A["raw: 48 / 44 / 46"] --> B["coerce everything"]
    B --> C["coerced: 50 / 50 / 41"]
    C --> D["present rose"]
    C --> E["converts rose"]
    C --> F["distinct fell, the only warning"]
```

## 5. Two numbers that disagree

```mermaid
flowchart TB
    A["compare whole rows"] --> B["0 duplicates"]
    C["count distinct order_ids"] --> D["49 across 50 rows"]
    B --> E["nothing in the code connects these two lines"]
    D --> E
```

## 6. Four identity rules, three answers

```mermaid
flowchart TB
    A["the pair sharing KR4201"] --> B["every field: 0"]
    A --> C["order_id: 1"]
    A --> D["order_id and order_date: 0"]
    A --> E["order_id and amount: 1"]
```

## 7. The order at the end of the column

```mermaid
flowchart TB
    A["sort the amounts"] --> B["Rs 800 ... Rs 2,900"]
    B --> C["Rs 480,000"]
    C --> D{"does the record look wrong?"}
    D -->|"no"| E["keep it, flag it, state its share"]
    D -->|"yes"| F["reject it with a reason"]
```

## 8. What ships

```mermaid
flowchart LR
    A["50 in"] --> B["44 clean"]
    A --> C["6 rejected with reasons"]
    B --> D["the decisions log"]
    C --> D
```

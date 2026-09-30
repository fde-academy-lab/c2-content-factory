# Which drawings go up on the board, in order, to answer Anand's Monday question?

These are the board drawings for Week 2, Monday, in the order they go up. Anand Iyer, Kalpa Retail's
finance controller, wants last week's revenue tree every Monday, for every segment, "computed from
the warehouse itself. No notebooks, no exports, nothing a person can mistype." The warehouse is
Kalpa's Postgres database, and the book is its two quarters of orders, the one copy everybody reads:
Q1 is April to June 2026 and Q2 is July to September 2026, and revenue is booked revenue, every
order at its amount, whatever its status. Anand's analyst audits every line of the suite. The decks,
the notebooks and the cheat sheet use these same drawings.

---

## What does Anand's rule rule out, and what does it still allow?

Anand named three things he never wants behind a Monday number, and they go up first. Beside them
the room writes what the rule still allows: exploring in a notebook is fine, so long as the reported
number comes from a saved query that reruns on the book every Monday.

```mermaid
flowchart LR
    A["<b>a notebook</b><br/>on someone's laptop"] --> X["<b>the Monday number</b><br/>on Anand's sheet"]
    B["<b>an export</b><br/>a file that ages"] --> X
    C["<b>a typed value</b><br/>copied by hand"] --> X
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class A,B,C bad
    class X bet
```

---

## In what order does the database run a query's clauses?

Seven boxes go up left to right, drawn once and left up all day. A query is written SELECT, FROM, WHERE,
GROUP BY, HAVING, ORDER BY, LIMIT, and it runs as the arrows show; most of the day's refusals and
wrong numbers are explained by this order. SELECT is drawn dark because it comes fifth.

```mermaid
flowchart LR
    F["<b>1 FROM</b><br/>the table,<br/>and the lookup"] --> W["<b>2 WHERE</b><br/>keep rows"] --> G["<b>3 GROUP BY</b><br/>form groups"] --> H["<b>4 HAVING</b><br/>keep groups"] --> S["<b>5 SELECT</b><br/>pick and<br/>compute columns"] --> O["<b>6 ORDER BY</b><br/>sort"] --> L["<b>7 LIMIT</b><br/>cut"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class F,W,G,H,O,L known
    class S bet
```

---

## Which numbers does the Monday sheet carry, and which table holds each?

Week 1 Monday's revenue tree goes up under the run order: revenue is customers who bought, times
orders per customer, times revenue per order. Every leaf comes from the orders table, and the segment
lives on the customer table. Beside it goes the definition the day's first trap tests: a customer
who bought is a customer with at least one order in the quarter, counted once.

```mermaid
flowchart TB
    R["<b>revenue</b><br/>sum(amount)"] --> C["<b>customers who bought</b><br/>each counted once"]
    R --> F["<b>orders per customer</b><br/>orders over customers"]
    R --> V["<b>revenue per order</b><br/>revenue over orders"]
    C --> O["<b>orders</b><br/>one row each"]
    F --> O
    V --> O
    O --> SEG["<b>the segment</b><br/>on the customer table"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class C,F,V,O,SEG known
    class R bet
```

---

## How do you connect VS Code to the warehouse and run one block of a `.sql` file?

This is the day's first-use step, taken before chapter 1's first query. The steps follow Microsoft
Learn's quickstart for the PostgreSQL extension,
https://learn.microsoft.com/en-us/azure/postgresql/development/vs-code-extension/quickstart-connect-query (checked 30 September 2026),
and the settings come from the Codespace's own configuration, which installs the extension
(`ms-ossdata.vscode-pgsql`) and loads the warehouse into a database called `kalpa`. The extension's
screens were not run in this build, so the labels below are the quickstart's.

| Step | What you do | What you should see |
|---|---|---|
| 1 | Open the PostgreSQL view with `Ctrl+Alt+D` (`Cmd+Alt+D` on a Mac) or the PostgreSQL icon in the Activity Bar. | A Connections section, empty the first time. |
| 2 | Hover over the Connections header and choose Add New Connection, the plus icon. | A connection dialog on its Parameters tab. |
| 3 | Enter server name `localhost`, authentication type Password, user name `postgres`, password `postgres` and database name `kalpa`. | The fields filled, with a connection name of your choice. |
| 4 | Choose Save & Connect. | The server in the Connections tree with a green status mark. |
| 5 | Open `sql/C2_W02_D01_01_book_STUDENT.sql`, select the first block, `c1_tables`, and run it with `Ctrl+Shift+E` (`Cmd+Shift+E` on a Mac). | Seven tables with the number of columns each carries. |

Whether those shortcuts behave the same in a Codespace opened in a browser was not verified. If the
extension reports "Connection refused", the database server is not running: in the terminal, run
`bash .devcontainer/load_warehouse.sh`, which waits for the server and reloads the warehouse. The same
check without the extension is `psql -c "SELECT count(*) FROM orders;"`, which prints 1000 once the
warehouse is loaded, since the Codespace's settings name the host, the user and the database.

---

## What does the warehouse hold, and where does each leaf live?

The first query reads the catalogue, `information_schema`, and the board records its answer: seven
tables, of which today's tree needs two. An order carries its customer, date, quarter, channel,
amount and status; the segment is on the customer.

```mermaid
flowchart LR
    ORD["<b>orders</b><br/>1,000 rows<br/>7 columns"] -->|"customer_id"| CUS["<b>customers</b><br/>340 rows<br/>the segment"]
    OTH["<b>five more tables</b><br/>for later<br/>this week"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    class ORD,CUS known
    class OTH unknown
```

---

## What does each count count on one table?

Chapter 1's check goes up next. The hurried query's `count(*) AS customers` said 538 and 462
customers, 1.00 order each, so three counts, each named for what it counts, go up side by side.
Under them the room writes the fix per quarter: 244 and 227 customers who bought, 2.20 and 2.04
orders each.

```mermaid
flowchart LR
    R["<b>order rows</b><br/>count(*)<br/>1,000"] --- B["<b>customers who bought</b><br/>count(DISTINCT customer_id)<br/>301"] --- K["<b>members on the book</b><br/>count(*) over customers<br/>340"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class R,K known
    class B bet
```

---

## How can two sources agree on the total and part on the branches?

For chapter 2, last week's extract and the warehouse both fell 1.6 percent, and their two trees go
up as products of their branches, each Q2 over Q1. Under them goes the check, who bought in both
quarters: 69 of 69 in the extract, 170 of 301 in the book.

```mermaid
flowchart LR
    E["<b>last week's extract</b><br/>1.000 x 0.860 x 1.144"] --> T["<b>the same total</b><br/>0.984, down 1.6%"]
    B["<b>the warehouse</b><br/>0.930 x 0.923 x 1.146"] --> T
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class E,B known
    class T bad
```

The second route goes up beside it as a bridge: Q1's 244 customers, less the 74 who bought in Q1 and
not in Q2, plus the 57 who bought in Q2 and not in Q1, is 227.

```mermaid
flowchart LR
    A["<b>Q1 customers</b><br/>244"] --> B["<b>less: bought in Q1,<br/>not in Q2</b><br/>74"]
    B --> C["<b>plus: bought in Q2,<br/>not in Q1</b><br/>57"]
    C --> D["<b>Q2 customers</b><br/>227"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class A,C known
    class B bad
    class D bet
```

---

## Where does a test on a group go, and how is a ratio checked?

Chapter 3's drawing takes three boxes from the run order and adds the test the day uses: a rate on
fewer than 30 customers goes on the sheet flagged, and only HAVING can see a group's count. Beside it
goes the multiply-back check on the hurried ratio: 140 orders over 76 customers printed 1, and 1 times
76 is 76, where the orders are 140; in numeric it is 1.84.

```mermaid
flowchart LR
    W["<b>WHERE</b><br/>tests one order,<br/>before groups exist"] --> G["<b>GROUP BY</b><br/>one group per<br/>segment and quarter"] --> H["<b>HAVING</b><br/>tests each group:<br/>fewer than 30?"]
    H --> R["<b>Student Q1: 15<br/>Student Q2: 20</b><br/>flagged"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class W,G,H known
    class R bet
```

---

## How do named steps set Q1 beside Q2, and who is inside each average?

Chapter 4's drawing is the shape of the query, one named step per job, read from the top down. Beside
it go the members inside the hurried average of Retail-Plus spend: 107 in the step, 91 inside Q1's
average and 76 inside Q2's, so Q1 and Q2 were averaged over different people. With Rs 0 written in on
purpose, the same 107 members spent Rs 5,474 and then Rs 3,863, down 29.4 percent.

```mermaid
flowchart LR
    B["<b>book</b><br/>each order<br/>with its segment"] --> Q1["<b>q1</b><br/>Q1 leaves<br/>per segment"]
    B --> Q2["<b>q2</b><br/>Q2 leaves<br/>per segment"]
    Q1 --> R["<b>ratios</b><br/>Q2 over Q1,<br/>per branch"]
    Q2 --> R
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class B,Q1,Q2 known
    class R bet
```

---

## Why can the half-year's customers not be added from the quarters?

In chapter 5, adding Retail-Plus's two quarter rows gave 167 customers in a tier of 120 members.
The overlap explains the gap, and the counted half-year goes up as the answer.

```mermaid
flowchart LR
    Q1["<b>Q1 buyers</b><br/>91"] --> O["<b>less: bought<br/>in both quarters</b><br/>60"]
    Q2["<b>Q2 buyers</b><br/>76"] --> O
    O --> H["<b>the half-year</b><br/>107 of the tier's 120"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class Q1,Q2 known
    class O bad
    class H bet
```

Beside it goes the rule the drawing proves. Orders and rupees add across quarters, because an order
sits in one quarter, and customers add across segments, because a customer sits in one segment; the
half-year's customers are counted again from the orders.

---

## How does a run show that the book held still while the sample moved?

Chapter 6 sets the unordered sample beside the fingerprint. The sample drew Rs 3,900 on Monday and
Rs 4,590 after an overnight reload that changed no value, while the book's fingerprint held at 1,000
rows, Rs 19,84,00,000 and 301 customers. The fix goes under it: `ORDER BY order_id LIMIT 5` draws
the same five, Rs 3,900, both times.

```mermaid
flowchart LR
    A["<b>LIMIT 5</b><br/>no ORDER BY"] --> B["<b>rows as the<br/>database reaches them</b>"]
    B --> C["<b>a reload rewrites<br/>two rows</b><br/>new versions, new places"]
    C --> D["<b>a different five</b><br/>Rs 690 apart"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class A,B,C known
    class D bad
```

---

## What does the Monday suite tell Anand?

The day's answer goes up as one chain, the evidence in the order Anand reads it and the caveat last.

```mermaid
flowchart LR
    B["<b>the book</b><br/>down 1.6%"] --> S["<b>the segment</b><br/>Retail-Plus<br/>down 29.4%"] --> R["<b>the branches</b><br/>customers -16.5%,<br/>frequency -22.0%"] --> A["<b>the audit</b><br/>sums tie out;<br/>runs repeat"] --> C["<b>the caveat</b><br/>customers fell 7.0%"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class B,S,R,A known
    class C bet
```

---

## What is on the board when the day ends?

The run order is still up with SELECT drawn dark, and the tree beside it carries the day's numbers on
its leaves: 244 and 227 customers who bought, 2.20 and 2.04 orders each, Rs 10,00,00,000 and
Rs 9,84,00,000. Under them sit the three counts, the two trees that multiply to 0.984 with the bridge
from 244 to 227, the HAVING test with Student flagged and the multiply-back check, the named steps
with 107, 91 and 76 written beside them, the half-year with 107 of 120 ringed, and the sample that
moved beside the fingerprint that held. The chain to Anand runs across the bottom, and beside it the
six lines the cheat sheet prints:

1. A count says what it counts: order rows are count(*), customers are count(DISTINCT customer_id).
2. A matching total is one leaf matching, so compare every leaf as a change.
3. Divide in numeric, round on purpose, and keep the counts beside the ratio.
4. An average names who is inside it, so write the zero on purpose.
5. Orders and rupees add across quarters; customers are counted again from the orders.
6. Order every list on a column no two rows share, and print the book's fingerprint beside the numbers.

Tomorrow's question goes in the corner, left open: how much of what was booked was collected?

# Trainer day sheet: Week 2, Monday. SQL foundations

TRAINER ONLY. Nothing on this page is shown to the room.

## Before the room opens

Run `psql -c "SELECT count(*) FROM orders;"` in your own Codespace and confirm it returns 1000.
If the warehouse is not there, `bash .devcontainer/load_warehouse.sh` rebuilds it in about ten
seconds. Have both drawings from the whiteboard file on the board before anyone sits down.

## The shape of the day

| Block | Minutes | What has to happen |
|---|---|---|
| Anand's ask | 10 | The room lists what "from the warehouse itself" rules out |
| The connection and the schema | 30 | First-use tool: Postgres from VS Code, a `.sql` file, the schema read |
| SELECT, FROM, WHERE, ORDER BY, LIMIT | 45 | Last week's leaf answers re-asked one at a time |
| Aggregates, GROUP BY, HAVING | 50 | The execution order walked aloud, revenue per segment per quarter |
| CTEs as named steps | 40 | The two-quarter comparison |
| Guided then unguided | 45 | The Monday suite, solution at close |
| Kahoot and close | 20 | Seven questions, the return question last |

Total 240 minutes.

## What is planted in v4, and how the room is meant to find it

**Never name any of this.** Each one is found by running something.

| Planted | Found by | Where it matters |
|---|---|---|
| The warehouse holds 1,000 orders where last week's extract held 186 distinct | Running last week's headline and getting Rs 10.00 crore | The whole of section D |
| The same segment story at book scale: Retail-Plus down 34.9 percent, Retail-Core down 3.0 | The two-CTE comparison | Confirms the sample was honest about shape |
| 450 orders carrying more than one payment row | Nothing today; it is tomorrow's | Do not let a curious learner open `payments` and derail the afternoon |
| An exact Q2 revenue tie at the fiftieth Retail-Plus position | Nothing today; it is Wednesday's | |

If somebody opens `payments` early, the answer is "that is tomorrow, and you will want today's
counting habit before you touch it". Do not explain the fan-out.

## The two failures to stage, with their exact text

**One, in the aggregates block.** Have the room write revenue per segment and channel while
grouping by segment alone. Postgres answers:

```
ERROR:  column "o.channel" must appear in the GROUP BY clause or be used in an aggregate function
```

Read it out loud, slowly, twice. Then take both fixes from the room: adding `channel` to the
grouping gives twelve rows, wrapping it as `count(DISTINCT channel)` keeps four. Neither is more
correct. Make somebody say what question each one answers before moving on.

**Two, in the first block after the connection.** Have everyone run
`SELECT order_id, amount FROM orders LIMIT 5;` and compare with a neighbour. On most Codespaces
they will match, which is the trap: the belief survives because it is right often enough. The
question that breaks it is "what would have to change about the table for these to differ", and
the answer is nothing about the table, only about the plan.

## The moment the day turns

Section D, when the warehouse says Rs 10.00 crore and last week's note said Rs 2.10 crore.

Let the room sit in it. Somebody will say the data is wrong, somebody else will say last week was
wrong, and both are worth hearing before the answer arrives. The answer is that a sample is
reliable about shape long before it is reliable about level, and the proof is that Retail-Plus is
still the branch that moved.

The sentence on slide S16 is the deliverable of that section. Have one learner read it aloud as if
sending it to Anand.

## Where this day usually goes wrong

The temptation is to teach SQL syntax and let the business scenario be decoration. The room
already knows every right answer from Week 1, which is the entire advantage: attention goes to the
language because the thinking is already done. Keep saying what each query is for.

The second temptation is to rescue people from the `GROUP BY` error. Do not. It is the most
useful thirty seconds of the day.

## Timing pressure

If you are running long, cut subqueries entirely and go straight to CTEs. That is the row's own
instruction. Never cut the execution-order walk or the `GROUP BY` error; both are load-bearing for
the rest of the week.

## Close-out

Release the two solution files and the suite solution. Set the take-home, and say plainly that the
four comment lines are the deliverable and the SQL is not. Preview tomorrow in one sentence:
booked revenue is not collected revenue, and the first honest-looking join returns roughly twice
the truth.

# Triage labels

The skills speak in terms of five canonical triage roles. This file maps those roles to the label strings this repository actually uses, and the defaults were kept, so the two columns match.

| Label in mattpocock/skills | Label in our tracker | Meaning                                   |
| -------------------------- | -------------------- | ----------------------------------------- |
| `needs-triage`             | `needs-triage`       | Someone needs to evaluate this issue      |
| `needs-info`               | `needs-info`         | Waiting on the reporter for more detail   |
| `ready-for-agent`          | `ready-for-agent`    | Fully specified and ready for an AFK agent |
| `ready-for-human`          | `ready-for-human`    | Requires human implementation             |
| `wontfix`                  | `wontfix`            | Will not be actioned                      |

When a skill mentions a role, for example "apply the AFK-ready triage label", use the label string from the right-hand column.

The tracker is local markdown, so a label is the value on the `Status:` line near the top of an issue file rather than a GitHub label. Edit the right-hand column if the vocabulary ever changes.

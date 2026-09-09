# CURRICULUM MAP SCHEMA
## The day-wise plan the project needs before it can build anything

This file defines the shape. The filled version becomes `05_Curriculum_Map_C2.xlsx` and is the second-highest ground-truth source in the project.

Cohort 1's curriculum listed topics without listing prerequisites, and sessions ended up depending on concepts that had not been established. The prerequisite and environment columns below are the fix. They are the columns most likely to get skipped and the ones that matter most.

---

## SHEET 1: DAY MAP

One row per day. 120 rows.

| Column | Content | Example |
|---|---|---|
| `week` | 1 to 20 | 2 |
| `week_type` | Teaching or Build | Teaching |
| `phase` | M1 Genesis, M2 Forge, M3 Ascent, M4 Build, M5 Launch | M1 Genesis |
| `day` | 1 to 6 | 3 |
| `date` | Calendar date | 2026-10-07 |
| `module` | Module name | Python and Data Fundamentals |
| `session_1_topic` | Morning block | Dictionaries and nested structures |
| `session_2_topic` | Second block | Iterating nested data |
| `session_3_topic` | Afternoon practical | Cleaning nested records |
| `concepts_introduced` | Atomic concepts, one per line, in teaching order | dict lookup; nested access; KeyError; .get() default |
| `prerequisites_concepts` | Concept references from earlier days, with the day number | W2D1 list indexing; W2D2 for loop |
| `prerequisites_tools` | Any tool used for the first time today | VS Code notebook kernel |
| `client_zero_artifact` | Which table, dataset or entity today's examples use | orders records, nested customer object |
| `environment` | Notebook, SQL file, terminal, browser | ipynb |
| `deliberate_failure` | What breaks and the exact error text | KeyError: 'discount' on a record missing the key |
| `mid_session_exercise_count` | Integer | 2 |
| `guided_exercise` | One line description | Build a nested-record reader step by step |
| `unguided_exercise` | One line description | Clean 20 malformed order records, no hints |
| `take_home` | One line description | Extend the cleaner to log every record it rejected |
| `kahoot_topic` | Quiz focus | Dict access and KeyError |
| `neo_mcq_tag` | Tag for the daily platform check pool | W2_dict_nested |
| `trainer_type` | In-house, Industry, or IIT | In-house |
| `iit_faculty_session` | Y or N | N |
| `reference_written` | Locked written source URL | |
| `reference_video` | Locked video source URL | |
| `assessment_touchpoint` | Which graded item this day feeds | ME1 |
| `pack_status` | Not started, Drafted, Reviewed, Locked | Not started |

---

## SHEET 2: CONCEPT LEDGER

The prerequisite chain lives here. One row per atomic concept across the whole programme.

| Column | Content |
|---|---|
| `concept_id` | Stable ID, for example `PY-DICT-01` |
| `concept` | Short name |
| `module` | Which module owns it |
| `first_taught` | Week and day |
| `depends_on` | Comma-separated concept IDs |
| `revisited_on` | Weeks and days where it is deliberately reused |
| `assessed_in` | Where it appears in a graded item |
| `client_zero_expression` | How this concept appears in the client-zero world |

Two checks this sheet makes possible, and neither is possible without it:

1. No concept is taught before its dependencies. Sort by `first_taught` and confirm every `depends_on` entry has an earlier `first_taught`.
2. Every concept assessed in ME1, ME2 or ME3 was taught and revisited at least once.

---

## SHEET 3: BUILD WEEK MAP

One row per build week. Five rows.

| Column | Content |
|---|---|
| `build_number` | 1 to 5 |
| `week` | 3, 6, 9, 12, 15 |
| `assessor` | Named assessor |
| `mini_project_brief` | One line |
| `modules_covered` | Which teaching modules the project integrates |
| `business_use_case_topic` | The separate discussion thread topic for this week |
| `data_source` | Fictional scenario or real dataset |
| `catch_up_day` | Which of the five days is reserved for teaching backlog |
| `mock_interview_focus` | What the mocks test this cycle |
| `industry_leader_confirmed` | Y or N |

---

## SHEET 4: CLIENT ZERO

The scenario definition, filled once and referenced everywhere.

| Field | Content |
|---|---|
| `company_name` | Fictional company |
| `domain` | Industry |
| `business_model` | Two or three sentences a trainer can state from memory |
| `entities` | The core entities and their relationships |
| `primary_dataset` | The records that carry from Python through Pandas, SQL and ML |
| `secondary_dataset` | Introduced later for joins and scale |
| `corpus` | The document set used when RAG arrives |
| `metrics` | The business metrics the cohort computes repeatedly, for example conversion rate |
| `domain_switch_points` | The at most two weeks where the domain changes, and what it changes to |

Pick a domain where the data is intuitive without explanation and where the business questions are obvious to a 22-year-old. Domains that need their own teaching (insurance underwriting, clinical trials, derivatives) cost teaching time before any concept is taught.

---

## HOW THE PROJECT USES THIS

Given a week and a day, the project reads the day map row, pulls the concept ledger entries, pulls the client-zero definition, and builds the day pack against `03_Day_Pack_Spec.md`.

If the row is missing or `reference_written` and `reference_video` are empty, the project says so and stops rather than generating a plausible day.

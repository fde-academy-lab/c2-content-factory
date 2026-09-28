# Posting the diagnostic's discussion threads

TRAINER ONLY. For the Academic TA, who posts the threads and answers replies in them.

## What there is to post

Seven posts, each ready to paste as written, in `content/W00/D2/study-notes/`. Each post's first
heading is its title.

| File | Post |
|---|---|
| `C2_W00_D02_discussion_00_index_STUDENT.md` | The pinned index: the map, the answers at a glance, the questions learners ask, and the best of the reading |
| `C2_W00_D02_discussion_A1_python_STUDENT.md` | Section A, part 1: Q1 to Q6 |
| `C2_W00_D02_discussion_A2_python_STUDENT.md` | Section A, part 2: Q7 to Q12 |
| `C2_W00_D02_discussion_B_sql_STUDENT.md` | Section B: Q13 to Q20 |
| `C2_W00_D02_discussion_C_numbers_STUDENT.md` | Section C: Q21 to Q28 |
| `C2_W00_D02_discussion_D_case_STUDENT.md` | Section D: Q29 to Q34 |
| `C2_W00_D02_discussion_E_judgment_STUDENT.md` | Section E: Q35 to Q40 |

## When

Post after the last sitting, which is the make-up first thing on Wednesday, since every thread carries
every answer. Tuesday's sitters already have the short explanations in their report emails, so a
make-up sitter may have heard some answers from them. The diagnostic is ungraded and the make-up runs
early, which keeps that cost small.

## Before posting

1. Watch each video the threads recommend, at least far enough to confirm it matches its line. The
   titles and channels were checked on 28 September 2026, and the running times of the Python videos
   were checked too; the other videos' running times and content were not verified.
2. Paste one post into a draft and preview it. GitHub's documentation says diagram rendering is
   available in GitHub Discussions, so each mermaid block should draw as a diagram; a block that shows
   as code means the paste lost its fence.
3. Post the index first and pin it, then the six section threads, in the category the course
   repository uses for exercises.

## Answering replies

- A learner who says a key is wrong gets the snippet or query run in front of them, in the thread,
  with the output pasted. Every snippet in the threads ran in Python 3.11.15 and every query in
  PostgreSQL 16.13 on 28 September 2026.
- A learner whose output differs in wording should compare the type of error first; error wording
  can shift between Python versions.
- A learner who asks about their own score moves to their one-to-one. No score, band or track is ever
  posted in a thread.
- A question that comes up three times goes into the index's list of questions learners ask.

## Posting through the API

GitHub's GraphQL API has a `createDiscussion` mutation that takes a repository id, a category id, a
title and a body, so once the course repository exists the seven posts can be created from these
files in one run. The repository id and category id come from that repository, which does not exist
yet.

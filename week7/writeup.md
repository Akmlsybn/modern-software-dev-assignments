# Week 7 Write-up

Tip: To preview this markdown file

- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## Instructions

Fill out all of the `TODO`s in this file.

## Submission Details

Name: Akmallullail Sya'ban \
SUNet ID: 2310817310010 \
Citations: AI Assistant (Warp/Cursor) for code generation, Graphite Diamond for AI code review.

This assignment took me about **2.5** hours to do.

## Task 1: Add more endpoints and validations

a. Links to relevant commits/issues

> https://github.com/akmlsybn/modern-software-dev-assignments/pull/1

b. PR Description

> Implemented Task 1 by adding strict input validations and missing API endpoints. Added Pydantic `Field` validators in `schemas.py` to ensure `title` (min 3 chars) and `content` (min 1 char) are not empty. Added a new `GET /action-items/{item_id}` endpoint with 404 handling.

c. Graphite Diamond generated code review

> Graphite Diamond reviewed the PR and found no issues. It approved the code as-is without any additional comments, confirming the immediate technical correctness of the API logic.

## Task 2: Extend extraction logic

a. Links to relevant commits/issues

> https://github.com/akmlsybn/modern-software-dev-assignments/pull/2

b. PR Description

> Implemented Task 2 by upgrading the `extract_action_items` function to use advanced regex pattern matching. Split text by newlines and sentence-ending punctuation. Extracted sentences containing action keywords and excluded questions. Added regex cleanup to strip leading bullet points.

c. Graphite Diamond generated code review

> Graphite Diamond found no issues and approved the PR immediately. It focused solely on syntax and code safety, completely missing the potential edge case regarding abbreviations that I pointed out in my manual review.

## Task 3: Try adding a new model and relationships

a. Links to relevant commits/issues

> https://github.com/akmlsybn/modern-software-dev-assignments/pull/3

b. PR Description

> Implemented Task 3 by adding a new `Tag` model and an association table for a Many-to-Many relationship between `Note` and `Tag`. Updated schemas (`NoteRead`, `NoteCreate`, `NotePatch`) to handle tags, and modified the `/notes/` endpoints to resolve and attach tags properly.

c. Graphite Diamond generated code review

> Graphite Diamond found no issues and approved the implementation. It reliably validated the standard SQLAlchemy boilerplate and relationship logic without asking for deeper architectural considerations.

## Task 4: Improve tests for pagination and sorting

a. Links to relevant commits/issues

> https://github.com/akmlsybn/modern-software-dev-assignments/pull/4

b. PR Description

> Implemented Task 4 by adding comprehensive test coverage for pagination (`limit`, `skip`) and sorting (`sort=created_at`, `sort=-created_at`) across the application. Also fixed a pre-existing Windows teardown bug in `conftest.py` by calling `engine.dispose()` before `os.unlink`.

c. Graphite Diamond generated code review

> Graphite Diamond again found no issues and approved the PR. While it correctly validated the test structures, it missed the opportunity to comment on the OS-specific file lock fix (`engine.dispose()`), showing a lack of environmental context.

## Brief Reflection

a. The types of comments you typically made in your manual reviews (e.g., correctness, performance, security, naming, test gaps, API shape, UX, docs).

> My manual review comments heavily leaned towards architectural foresight, edge cases, and real-world semantic context. For example, I pointed out potential security/validation gaps (like empty string bypasses in Task 1), regex limitations with abbreviations (Task 2), and OS-specific quirks during testing (Task 4).

b. A comparison of **your** comments vs. **Graphite’s** AI-generated comments for each PR.

> Graphite Diamond acted much like an advanced, hyper-fast linter. It was excellent at verifying that the syntax was correct and endpoints were reachable, consistently outputting "no issues" across all four PRs. In contrast, my manual comments were more critical and speculative about _future_ failures or context-specific bugs, whereas Graphite focused entirely on the _present_ state of the code.

c. When the AI reviews were better/worse than yours (cite specific examples)

> **Worse:** The AI was notably worse at spotting domain-specific edge cases (like the "Mr." abbreviation potentially breaking the sentence splitter in Task 2) and environmental context (like the Windows SQLite teardown bug in Task 4).
> **Better:** The AI is significantly better at instantly validating structural correctness and ensuring standard SQLAlchemy relationships (Task 3) are perfectly written, saving a lot of time on initial code scans.

d. Your comfort level trusting AI reviews going forward and any heuristics for when to rely on them.

> I feel comfortable using AI code reviews as a "first line of defense" to quickly catch typos, syntax errors, and standard boilerplate mistakes. However, I will not rely on them entirely. My heuristic going forward is: let the AI verify _technical correctness and syntax_, but I must still perform manual reviews to ensure _semantic context, edge cases, and architectural integrity_.

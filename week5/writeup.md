# Week 5 Write-up

Tip: To preview this markdown file

- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## INSTRUCTIONS

Fill out all of the `TODO`s in this file.

## SUBMISSION DETAILS

Name: Akmallullail Sya'ban \
SUNet ID: 2310817310010 \
Citations: Warp AI Agent

This assignment took me about **2** hours to do.

## YOUR RESPONSES

### Automation A: Warp Drive saved prompts, rules, MCP servers

a. Design of each automation, including goals, inputs/outputs, steps

> **Goal:** To automate the tedious cycle of running tests and fixing errors (Test-Driven Development loop).
> **Inputs:** The terminal output of the `pytest backend/tests/` command.
> **Outputs:** Modified backend source code that successfully passes the test suite.
> **Steps:** 1) Run full test suite. 2) If any test fails, automatically analyze the error trace. 3) Read the relevant source code. 4) Fix the logic. 5) Re-run tests until everything passes.
> **Saved Prompt Link/Definition:** [PASTE_LINK_WARP_DRIVE_KAMU_DISINI] (or named "Auto-Test Fixer" in my local Warp Drive).

b. Before vs. after (i.e. manual workflow vs. automated workflow)

> **Before:** I had to manually run `make test`, scroll through the terminal to find the error trace, open the specific file, deduce the logical error, fix it, and re-run the test command.
> **After:** By triggering this saved prompt, the Warp Agent handles the entire feedback loop autonomously. It reads the error, finds the file, proposes the fix, and verifies it.

c. Autonomy levels used for each completed task (what code permissions, why, and how you supervised)

> I used the **Partial Autonomy** level. The agent was allowed to run the read commands and plan autonomously, but it required my explicit approval before writing any changes to the Python files or re-running the test command. I supervised it by reviewing its proposed code diffs.

d. (if applicable) Multi‑agent notes: roles, coordination strategy, and concurrency wins/risks/failures

> N/A for this specific Warp Drive prompt, as it is designed to be a standalone utility tool used by a single agent during the testing phase.

e. How you used the automation (what pain point it resolves or accelerates)

> It completely resolves the pain point of context-switching between the terminal (reading error logs) and the code editor. It accelerates the debugging process significantly.

### Automation B: Multi‑agent workflows in Warp

a. Design of each automation, including goals, inputs/outputs, steps

> **Goal:** Implement Pagination for all lists (Task 8) and Improve Test Coverage for 400/404/422 scenarios (Task 10) simultaneously.
> **Inputs:** Instructions from `docs/TASKS.md` for Task 8 and Task 10.
> **Outputs:** Modified `routers`, `schemas`, `app.js`, `index.html` (for Task 8), and a new `test_error_scenarios.py` file (for Task 10).
> **Steps:** Deploy two independent Warp Agents in separate terminal tabs concurrently, assigning each a distinct task to execute simultaneously.

b. Before vs. after (i.e. manual workflow vs. automated workflow)

> **Before:** Sequential development. I would have to finish the full-stack pagination feature first, verify it, and then switch my mental context entirely to write negative test cases for error handling.
> **After:** Parallel development. Two agents worked at the exact same time. Development time was effectively halved, as boilerplate code (Pydantic schemas and test assertions) was generated concurrently.

c. Autonomy levels used for each completed task (what code permissions, why, and how you supervised)

> I used **Partial Autonomy** for both concurrent agents.
> **Why:** Running multiple agents simultaneously carries the risk of them overwriting each other's work or causing database locks.
> **Supervision:** I acted as the human coordinator, switching between tabs. I reviewed their plans and only clicked "Approve" when I was sure they were modifying separate, isolated files.

d. (if applicable) Multi‑agent notes: roles, coordination strategy, and concurrency wins/risks/failures

> **Roles:** Agent 1 was the Feature Developer (Task 8: Pagination). Agent 2 was the QA Tester (Task 10: Error coverage).
> **Coordination Strategy:** I used a staggered start. I let Agent 1 begin planning first to avoid immediate rate limits or simultaneous SQLite test DB locking. They were assigned tasks that touched entirely different files to avoid Git conflicts.
> **Concurrency Wins:** The separation of concerns worked flawlessly. Agent 1 successfully updated both backend and frontend for pagination, while Agent 2 built a robust test suite for edge cases.

e. How you used the automation (what pain point it resolves or accelerates)

> This multi-agent workflow eliminates the sequential bottleneck of software development. It accelerates the creation of repetitive boilerplate (like wiring frontend pagination UI or writing 404 test cases) and allows me to act as an architectural reviewer rather than a manual typist.

### (Optional) Automation C: Any Additional Automations

> (Left blank as the required 2 automations have been fulfilled comprehensively above).

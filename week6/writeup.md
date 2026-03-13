# Week 6 Write-up

Tip: To preview this markdown file

- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## Instructions

Fill out all of the `TODO`s in this file.

## Submission Details

Name: Akmallullail Sya'ban \
SUNet ID: 2310817310010 \
Citations: Warp AI Agent, Semgrep Documentation

This assignment took me about 3 hours to do.

## Brief findings overview

Semgrep performed a static analysis scan (SAST) and identified 6 blocking security vulnerabilities. The findings were categorized into several critical areas:

- **Injection Attacks:** SQL Injection, Command Injection, and Code Injection (`eval`).
- **Frontend Security:** Cross-Site Scripting (XSS) via insecure DOM manipulation.
- **Server Misconfiguration:** Insecure Wildcard CORS policy.
- **Request Forgery:** Server-Side Request Forgery (SSRF) risk in dynamic URL opening.

I prioritized fixing the three most exploitable injection vulnerabilities (SQLi, XSS, and Command Injection) to meet the assignment requirements while ensuring the application logic remains intact.

## Fix #1

a. File and line(s)

> `backend/app/routers/notes.py` (Lines 71-79)

b. Rule/category Semgrep flagged

> `python.sqlalchemy.security.audit.avoid-sqlalchemy-text`

c. Brief risk description

> The application used Python f-strings to inject user-provided search queries directly into a raw SQL string passed to `sqlalchemy.text()`. This allows a malicious user to craft input that escapes the intended query and executes unauthorized SQL commands, potentially leading to data leaks or database destruction.

d. Your change (short code diff or explanation, AI coding tool usage)

> I used a Warp Agent to refactor the query. The f-string was removed, and the query was changed to use SQLAlchemy's built-in `filter()` and `like()` operators.
>
> **Before:** `sql = text(f"SELECT ... WHERE title LIKE '%{q}%' ...")`
> **After:** `db.query(models.Note).filter(models.Note.title.contains(q)).all()`

e. Why this mitigates the issue

> SQLAlchemy's query builder uses parameterized queries under the hood. This ensures that user input is treated strictly as data (a string) and never as executable SQL code, effectively neutralizing SQL injection.

## Fix #2

a. File and line(s)

> `frontend/app.js` (Line 14)

b. Rule/category Semgrep flagged

> `javascript.browser.security.insecure-document-method`

c. Brief risk description

> The frontend rendered note titles and content using `.innerHTML`. If a user saves a note containing a `<script>` tag, that script would execute in the browser of anyone viewing the note, leading to a Stored Cross-Site Scripting (XSS) attack.

d. Your change (short code diff or explanation, AI coding tool usage)

> I used a Warp Agent to replace the insecure `.innerHTML` assignment with `.textContent` for the individual title and content spans.
>
> **Before:** `li.innerHTML = "<strong>" + n.title + "</strong>..."`
> **After:** `li.textContent = n.title + ": " + n.content` (or creating separate elements and setting their `.textContent`).

e. Why this mitigates the issue

> Unlike `.innerHTML`, `.textContent` does not parse string content as HTML. It renders everything as plain text, meaning any injected HTML or Script tags are displayed as harmless characters on the screen instead of being executed by the browser.

## Fix #3

a. File and line(s)

> `backend/app/routers/notes.py` (Line 112)

b. Rule/category Semgrep flagged

> `python.lang.security.audit.subprocess-shell-true`

c. Brief risk description

> The `subprocess.run()` function was called with `shell=True`. This tells Python to run the command through the system's shell (like `/bin/sh` or `cmd.exe`). If user input is part of the command string, they can use shell metacharacters (like `;` or `&`) to execute arbitrary system commands on the server.

d. Your change (short code diff or explanation, AI coding tool usage)

> I used a Warp Agent to refactor the subprocess call. I set `shell=False` and modified the command input to be a list of arguments rather than a single interpolated string.
>
> **Before:** `subprocess.run(f"command {input}", shell=True)`
> **After:** `subprocess.run(["command", input], shell=False)`

e. Why this mitigates the issue

> Setting `shell=False` bypasses the shell interpreter entirely. The program is executed directly, and the arguments are passed as literal strings, preventing any shell-based command chaining or injection.

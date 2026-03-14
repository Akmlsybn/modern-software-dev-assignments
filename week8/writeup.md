# Week 8 Write-up

Tip: To preview this markdown file

- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## Instructions

Fill out all of the `TODO`s in this file.

## Submission Details

Name: Akmallullail Sya'ban \
SUNet ID: 2310817310010 \
Citations: Claude AI (claude.ai) was used to assist in generating code for V2 and V3.

This assignment took me about **8** hours to do.

## App Concept

```
Notes Manager is a full-stack web application that allows users to manage their
personal notes. The app supports full CRUD functionality — users can create notes
with a title and content, view all saved notes, edit existing notes, and delete
notes they no longer need. Each note displays a timestamp of when it was created.
The app features persistent storage so notes are saved across sessions, basic
input validation to prevent empty submissions, and a clean, intuitive UI.
```

## Version #1 Description

```
APP DETAILS:
===============
Folder name: v1-mern-bolt
AI app generation platform: Bolt.new
Tech Stack: React + TypeScript + Supabase
Persistence: Supabase (PostgreSQL cloud database)
Frameworks/Libraries Used: React 18, TypeScript, Vite, Tailwind CSS,
Supabase JS Client, Lucide React
(Optional but recommended) Screenshots of core flows: -

REFLECTIONS:
===============
a. Issues encountered per stack and how you resolved them:
Bolt.new ran out of tokens before the ZIP file could be downloaded,
so all files had to be manually copied one by one from the Bolt editor
into VS Code. Files were also initially copied into the wrong directory
(week8/ instead of week8/v1-mern-bolt/), resolved by using Move-Item
command in PowerShell.

b. Prompting (e.g. what required additional guidance; what worked poorly/well):
A single detailed prompt describing the full app concept, data model, backend
routes, and frontend components was sent to Bolt.new. Bolt generated a working
app on the first try. The main issue was hitting the token limit before being
able to download the ZIP file.

c. Approximate time-to-first-run and time-to-feature metrics:
Time to generate: ~2 minutes. Time to first run: ~45 minutes (due to manual
file copying). All CRUD features working: ~1 hour.
```

## Version #2 Description

```
APP DETAILS:
===============
Folder name: v2-flask-js
AI app generation platform: Claude AI (claude.ai)
Tech Stack: Flask (Python) + Vanilla HTML/CSS/JavaScript
Persistence: SQLite (via Flask-SQLAlchemy)
Frameworks/Libraries Used: Flask, Flask-SQLAlchemy, Flask-CORS,
python-dotenv, Vanilla JS
(Optional but recommended) Screenshots of core flows: -

REFLECTIONS:
===============
a. Issues encountered per stack and how you resolved them:
No major issues encountered. Flask setup was straightforward and all files
were generated cleanly. SQLite database was automatically created on first
run via db.create_all().

b. Prompting (e.g. what required additional guidance; what worked poorly/well):
Claude AI generated each file one by one (app.py, requirements.txt, index.html,
style.css, script.js). No additional guidance was needed as each file worked
correctly on the first attempt.

c. Approximate time-to-first-run and time-to-feature metrics:
Time to generate all files: ~15 minutes. Time to first run: ~20 minutes.
All CRUD features working: ~25 minutes.
```

## Version #3 Description

```
APP DETAILS:
===============
Folder name: v3-nextjs
AI app generation platform: Claude AI (claude.ai)
Tech Stack: Next.js 15 + TypeScript + SQLite
Persistence: SQLite (via better-sqlite3)
Frameworks/Libraries Used: Next.js 15, React 18, TypeScript,
Tailwind CSS, better-sqlite3
(Optional but recommended) Screenshots of core flows: -

REFLECTIONS:
===============
a. Issues encountered per stack and how you resolved them:
Edit and delete features were not working initially due to a breaking change
in Next.js 15 where route params are now async (Promise-based). Resolved by
updating [id]/route.ts to use "await params" instead of accessing params directly.

b. Prompting (e.g. what required additional guidance; what worked poorly/well):
Claude AI generated all files including database connection, API routes, and
main page component. Additional guidance was needed for the Next.js 15 params
breaking change which required a fix to the route handlers.

c. Approximate time-to-first-run and time-to-feature metrics:
Time to generate all files: ~20 minutes. Time to first run: ~25 minutes.
All CRUD features working: ~35 minutes (after fixing params issue).
```

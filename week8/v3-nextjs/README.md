# Notes Manager - V3 (Next.js + SQLite)

A full-stack notes management application built with Next.js App Router and SQLite database.

## Tech Stack

**Frontend:**

- Next.js 15
- React 18
- TypeScript
- Tailwind CSS

**Backend:**

- Next.js API Routes
- better-sqlite3
- SQLite (database)

## Prerequisites

- Node.js v18 or higher
- npm

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd week8/v3-nextjs
```

### 2. Install dependencies

```bash
npm install
```

### 3. Run the application

```bash
npm run dev
```

The app will be available at `http://localhost:3000`

## Project Structure

```
v3-nextjs/
├── app/
│   ├── api/
│   │   └── notes/
│   │       ├── route.ts        # GET, POST endpoints
│   │       └── [id]/
│   │           └── route.ts    # PUT, DELETE endpoints
│   ├── page.tsx                # Main UI
│   └── layout.tsx              # App layout
├── lib/
│   └── db.ts                   # SQLite connection
└── package.json
```

## API Endpoints

| Method | Endpoint       | Description       |
| ------ | -------------- | ----------------- |
| GET    | /api/notes     | Get all notes     |
| POST   | /api/notes     | Create a new note |
| PUT    | /api/notes/:id | Update a note     |
| DELETE | /api/notes/:id | Delete a note     |

## Features

- Create notes with title and content
- View all notes
- Edit existing notes
- Delete notes with confirmation
- Persistent storage with SQLite
- Basic validation and error handling

## Known Issues

- No authentication (demo purposes only)
- SQLite not recommended for production

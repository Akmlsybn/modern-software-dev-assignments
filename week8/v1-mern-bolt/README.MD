# Notes Manager

A full-stack notes management application built with React, TypeScript, and Supabase. Create, read, update, and delete notes with a clean and intuitive interface.

## Features

- Create notes with title and content
- View all notes in a responsive grid layout
- Edit existing notes
- Delete notes with confirmation
- Timestamp display showing when each note was created
- Real-time updates with Supabase
- Clean, modern UI with Tailwind CSS

## Tech Stack

**Frontend:**

- React 18
- TypeScript
- Vite
- Tailwind CSS
- Lucide React (icons)

**Backend:**

- Supabase (Database & Backend)
- PostgreSQL (via Supabase)

## Database Schema

The app uses a `notes` table with the following structure:

```sql
notes {
  id: uuid (primary key)
  title: text
  content: text
  created_at: timestamptz
  updated_at: timestamptz
}
```

## Prerequisites

- Node.js (v18 or higher)
- npm or yarn
- A Supabase account and project

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd notes-manager
```

### 2. Install dependencies

```bash
npm install
```

### 3. Set up environment variables

The project includes a `.env` file with Supabase credentials already configured. If you need to use your own Supabase project:

Create a `.env` file in the root directory:

```env
VITE_SUPABASE_URL=your_supabase_project_url
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
```

You can find these values in your Supabase project settings under API.

### 4. Database setup

The database migration has already been applied. If you're setting up a new Supabase project, you'll need to run the migration to create the `notes` table.

The migration is located in `supabase/migrations/` and includes:

- Table creation
- Row Level Security (RLS) policies
- Indexes for performance

### 5. Run the development server

```bash
npm run dev
```

The app will be available at `http://localhost:5173`

### 6. Build for production

```bash
npm run build
```

The built files will be in the `dist` directory.

## Project Structure

```
src/
├── components/
│   ├── NoteCard.tsx      # Individual note card component
│   └── NoteForm.tsx      # Form for creating/editing notes
├── lib/
│   └── supabase.ts       # Supabase client configuration
├── types/
│   └── database.ts       # TypeScript types for database
├── App.tsx               # Main application component
├── main.tsx              # Application entry point
└── index.css             # Global styles
```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint
- `npm run typecheck` - Run TypeScript type checking

## Features in Detail

### Create a Note

1. Fill in the title and content fields in the form at the top
2. Click "Add Note" to save

### Edit a Note

1. Click the edit icon (pencil) on any note card
2. The form will populate with the note's current data
3. Make your changes and click "Update Note"
4. Click "Cancel" to abort editing

### Delete a Note

1. Click the delete icon (trash) on any note card
2. Confirm the deletion in the popup dialog

## Security

The app uses Supabase Row Level Security (RLS) to control access to data. Currently configured for public access (demo mode). For production, you should implement authentication and restrict access to authenticated users.

## License

MIT

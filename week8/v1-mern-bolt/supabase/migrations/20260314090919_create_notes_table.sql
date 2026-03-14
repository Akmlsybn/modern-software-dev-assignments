/*
  # Create notes table

  1. New Tables
    - `notes`
      - `id` (uuid, primary key) - Unique identifier for each note
      - `title` (text) - Note title
      - `content` (text) - Note content/body
      - `created_at` (timestamptz) - Timestamp when note was created
      - `updated_at` (timestamptz) - Timestamp when note was last updated

  2. Security
    - Enable RLS on `notes` table
    - Add policy for anyone to read all notes
    - Add policy for anyone to insert notes
    - Add policy for anyone to update notes
    - Add policy for anyone to delete notes
    
  Note: This is a simple demo app without authentication.
  In production, you would restrict access to authenticated users and their own notes.
*/

CREATE TABLE IF NOT EXISTS notes (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  title text NOT NULL DEFAULT '',
  content text NOT NULL DEFAULT '',
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now()
);

ALTER TABLE notes ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Anyone can read notes"
  ON notes
  FOR SELECT
  USING (true);

CREATE POLICY "Anyone can insert notes"
  ON notes
  FOR INSERT
  WITH CHECK (true);

CREATE POLICY "Anyone can update notes"
  ON notes
  FOR UPDATE
  USING (true)
  WITH CHECK (true);

CREATE POLICY "Anyone can delete notes"
  ON notes
  FOR DELETE
  USING (true);
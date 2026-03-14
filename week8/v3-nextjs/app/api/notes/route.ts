import { NextResponse } from "next/server";
import db from "@/lib/db";

export async function GET() {
  const notes = db
    .prepare("SELECT * FROM notes ORDER BY created_at DESC")
    .all();
  return NextResponse.json(notes);
}

export async function POST(request: Request) {
  const body = await request.json();

  if (!body.title || !body.content) {
    return NextResponse.json(
      { error: "Title and content are required" },
      { status: 400 },
    );
  }

  const stmt = db.prepare("INSERT INTO notes (title, content) VALUES (?, ?)");
  const result = stmt.run(body.title, body.content);

  const note = db
    .prepare("SELECT * FROM notes WHERE id = ?")
    .get(result.lastInsertRowid);
  return NextResponse.json(note, { status: 201 });
}

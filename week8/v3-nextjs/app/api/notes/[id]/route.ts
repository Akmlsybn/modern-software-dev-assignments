import { NextResponse } from "next/server";
import db from "@/lib/db";

export async function PUT(
  request: Request,
  { params }: { params: Promise<{ id: string }> },
) {
  const { id } = await params;
  const body = await request.json();

  if (!body.title || !body.content) {
    return NextResponse.json(
      { error: "Title and content are required" },
      { status: 400 },
    );
  }

  const note = db.prepare("SELECT * FROM notes WHERE id = ?").get(id);
  if (!note) {
    return NextResponse.json({ error: "Note not found" }, { status: 404 });
  }

  db.prepare("UPDATE notes SET title = ?, content = ? WHERE id = ?").run(
    body.title,
    body.content,
    id,
  );

  const updated = db.prepare("SELECT * FROM notes WHERE id = ?").get(id);
  return NextResponse.json(updated);
}

export async function DELETE(
  _: Request,
  { params }: { params: Promise<{ id: string }> },
) {
  const { id } = await params;

  const note = db.prepare("SELECT * FROM notes WHERE id = ?").get(id);
  if (!note) {
    return NextResponse.json({ error: "Note not found" }, { status: 404 });
  }

  db.prepare("DELETE FROM notes WHERE id = ?").run(id);
  return NextResponse.json({ message: "Note deleted" });
}

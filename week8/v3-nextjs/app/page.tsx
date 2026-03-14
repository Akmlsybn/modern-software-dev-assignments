"use client";

import { useEffect, useState } from "react";

interface Note {
  id: number;
  title: string;
  content: string;
  created_at: string;
}

export default function Home() {
  const [notes, setNotes] = useState<Note[]>([]);
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [editingId, setEditingId] = useState<number | null>(null);

  useEffect(() => {
    loadNotes();
  }, []);

  async function loadNotes() {
    const res = await fetch("/api/notes");
    const data = await res.json();
    setNotes(data);
  }

  async function saveNote() {
    if (!title.trim() || !content.trim()) {
      alert("Title and content cannot be empty!");
      return;
    }

    if (editingId) {
      await fetch(`/api/notes/${editingId}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, content }),
      });
      cancelEdit();
    } else {
      await fetch("/api/notes", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, content }),
      });
    }

    setTitle("");
    setContent("");
    loadNotes();
  }

  function editNote(note: Note) {
    setEditingId(note.id);
    setTitle(note.title);
    setContent(note.content);
    window.scrollTo(0, 0);
  }

  function cancelEdit() {
    setEditingId(null);
    setTitle("");
    setContent("");
  }

  async function deleteNote(id: number) {
    if (!confirm("Are you sure you want to delete this note?")) return;
    await fetch(`/api/notes/${id}`, { method: "DELETE" });
    loadNotes();
  }

  return (
    <main className="min-h-screen bg-gray-100 py-8 px-4">
      <div className="max-w-2xl mx-auto">
        <h1 className="text-3xl font-bold text-blue-600 mb-6">
          📄 Notes Manager
        </h1>

        {/* Form */}
        <div className="bg-white rounded-xl shadow p-6 mb-6">
          <h2 className="text-xl font-semibold mb-4">
            {editingId ? "Edit Note" : "Create New Note"}
          </h2>
          <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Title
            </label>
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="Enter note title"
              className="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:border-blue-500"
            />
          </div>
          <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Content
            </label>
            <textarea
              value={content}
              onChange={(e) => setContent(e.target.value)}
              placeholder="Enter note content"
              className="w-full border border-gray-300 rounded-lg px-4 py-2 h-32 resize-y focus:outline-none focus:border-blue-500"
            />
          </div>
          <div className="flex gap-2">
            <button
              onClick={saveNote}
              className="w-full bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700"
            >
              {editingId ? "Update Note" : "Add Note"}
            </button>
            {editingId && (
              <button
                onClick={cancelEdit}
                className="w-full bg-gray-200 text-gray-700 py-2 rounded-lg hover:bg-gray-300"
              >
                Cancel
              </button>
            )}
          </div>
        </div>

        {/* Notes List */}
        {notes.length === 0 ? (
          <p className="text-center text-gray-400">No notes yet. Create one!</p>
        ) : (
          notes.map((note) => (
            <div key={note.id} className="bg-white rounded-xl shadow p-5 mb-4">
              <div className="flex justify-between items-center mb-2">
                <h3 className="font-semibold text-gray-800">{note.title}</h3>
                <div className="flex gap-2">
                  <button onClick={() => editNote(note)} className="text-xl">
                    ✏️
                  </button>
                  <button
                    onClick={() => deleteNote(note.id)}
                    className="text-xl"
                  >
                    🗑️
                  </button>
                </div>
              </div>
              <p className="text-gray-600 mb-2">{note.content}</p>
              <p className="text-xs text-gray-400">
                Created: {note.created_at}
              </p>
            </div>
          ))
        )}
      </div>
    </main>
  );
}

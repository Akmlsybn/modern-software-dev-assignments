import { useState, useEffect } from "react";
import { StickyNote } from "lucide-react";
import { supabase } from "./lib/supabase";
import { NoteCard } from "./components/NoteCard";
import { NoteForm } from "./components/NoteForm";
import type { Note } from "./types/database";

function App() {
  const [notes, setNotes] = useState<Note[]>([]);
  const [editingNote, setEditingNote] = useState<Note | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchNotes();
  }, []);

  const fetchNotes = async () => {
    try {
      setLoading(true);
      setError(null);
      const { data, error } = await supabase
        .from("notes")
        .select("*")
        .order("created_at", { ascending: false });

      if (error) throw error;
      setNotes(data || []);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to fetch notes");
    } finally {
      setLoading(false);
    }
  };

  const handleCreateNote = async (title: string, content: string) => {
    try {
      setError(null);
      const { error } = await supabase
        .from("notes")
        .insert([{ title, content }]);

      if (error) throw error;
      await fetchNotes();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to create note");
    }
  };

  const handleUpdateNote = async (title: string, content: string) => {
    if (!editingNote) return;

    try {
      setError(null);
      const { error } = await supabase
        .from("notes")
        .update({ title, content, updated_at: new Date().toISOString() })
        .eq("id", editingNote.id);

      if (error) throw error;
      setEditingNote(null);
      await fetchNotes();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to update note");
    }
  };

  const handleDeleteNote = async (id: string) => {
    try {
      setError(null);
      const { error } = await supabase.from("notes").delete().eq("id", id);

      if (error) throw error;
      await fetchNotes();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to delete note");
    }
  };

  const handleSubmit = (title: string, content: string) => {
    if (editingNote) {
      handleUpdateNote(title, content);
    } else {
      handleCreateNote(title, content);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
      <div className="max-w-6xl mx-auto px-4 py-8">
        <div className="flex items-center gap-3 mb-8">
          <StickyNote className="text-blue-600" size={40} />
          <h1 className="text-4xl font-bold text-gray-800">Notes Manager</h1>
        </div>

        {error && (
          <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg mb-6">
            {error}
          </div>
        )}

        <div className="mb-8">
          <NoteForm
            note={editingNote}
            onSubmit={handleSubmit}
            onCancel={() => setEditingNote(null)}
          />
        </div>

        {loading ? (
          <div className="text-center py-12">
            <div className="inline-block h-8 w-8 animate-spin rounded-full border-4 border-solid border-blue-600 border-r-transparent"></div>
            <p className="mt-4 text-gray-600">Loading notes...</p>
          </div>
        ) : notes.length === 0 ? (
          <div className="text-center py-12 bg-white rounded-lg shadow-md">
            <StickyNote className="mx-auto text-gray-400 mb-4" size={48} />
            <p className="text-gray-600 text-lg">
              No notes yet. Create your first note above!
            </p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {notes.map((note) => (
              <NoteCard
                key={note.id}
                note={note}
                onEdit={setEditingNote}
                onDelete={handleDeleteNote}
              />
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;

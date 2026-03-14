import { useState, useEffect } from "react";
import { X } from "lucide-react";
import type { Note } from "../types/database";

interface NoteFormProps {
  note?: Note | null;
  onSubmit: (title: string, content: string) => void;
  onCancel: () => void;
}

export function NoteForm({ note, onSubmit, onCancel }: NoteFormProps) {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  useEffect(() => {
    if (note) {
      setTitle(note.title);
      setContent(note.content);
    } else {
      setTitle("");
      setContent("");
    }
  }, [note]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (title.trim() || content.trim()) {
      onSubmit(title, content);
      setTitle("");
      setContent("");
    }
  };

  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-2xl font-bold text-gray-800">
          {note ? "Edit Note" : "Create New Note"}
        </h2>
        {note && (
          <button
            onClick={onCancel}
            className="p-2 text-gray-500 hover:bg-gray-100 rounded-md transition-colors"
            aria-label="Cancel editing"
          >
            <X size={20} />
          </button>
        )}
      </div>
      <form onSubmit={handleSubmit}>
        <div className="mb-4">
          <label
            htmlFor="title"
            className="block text-sm font-medium text-gray-700 mb-2"
          >
            Title
          </label>
          <input
            type="text"
            id="title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none"
            placeholder="Enter note title"
          />
        </div>
        <div className="mb-4">
          <label
            htmlFor="content"
            className="block text-sm font-medium text-gray-700 mb-2"
          >
            Content
          </label>
          <textarea
            id="content"
            value={content}
            onChange={(e) => setContent(e.target.value)}
            rows={6}
            className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none resize-none"
            placeholder="Enter note content"
          />
        </div>
        <div className="flex gap-3">
          <button
            type="submit"
            className="flex-1 bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 transition-colors font-medium"
          >
            {note ? "Update Note" : "Add Note"}
          </button>
          {note && (
            <button
              type="button"
              onClick={onCancel}
              className="px-6 py-2 border border-gray-300 text-gray-700 rounded-md hover:bg-gray-50 transition-colors font-medium"
            >
              Cancel
            </button>
          )}
        </div>
      </form>
    </div>
  );
}

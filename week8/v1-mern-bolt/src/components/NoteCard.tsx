import { CreditCard as Edit2, Trash2 } from "lucide-react";
import type { Note } from "../types/database";

interface NoteCardProps {
  note: Note;
  onEdit: (note: Note) => void;
  onDelete: (id: string) => void;
}

export function NoteCard({ note, onEdit, onDelete }: NoteCardProps) {
  const handleDelete = () => {
    if (window.confirm("Are you sure you want to delete this note?")) {
      onDelete(note.id);
    }
  };

  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleDateString("en-US", {
      year: "numeric",
      month: "short",
      day: "numeric",
      hour: "2-digit",
      minute: "2-digit",
    });
  };

  return (
    <div className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow">
      <div className="flex justify-between items-start mb-3">
        <h3 className="text-xl font-semibold text-gray-800 flex-1">
          {note.title}
        </h3>
        <div className="flex gap-2 ml-4">
          <button
            onClick={() => onEdit(note)}
            className="p-2 text-blue-600 hover:bg-blue-50 rounded-md transition-colors"
            aria-label="Edit note"
          >
            <Edit2 size={18} />
          </button>
          <button
            onClick={handleDelete}
            className="p-2 text-red-600 hover:bg-red-50 rounded-md transition-colors"
            aria-label="Delete note"
          >
            <Trash2 size={18} />
          </button>
        </div>
      </div>
      <p className="text-gray-600 whitespace-pre-wrap mb-4">{note.content}</p>
      <div className="text-sm text-gray-400">
        Created: {formatDate(note.created_at)}
      </div>
    </div>
  );
}

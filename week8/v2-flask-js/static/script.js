const API = "http://localhost:5000/api/notes";
let editingId = null;

// Load semua notes saat halaman dibuka
document.addEventListener("DOMContentLoaded", loadNotes);

async function loadNotes() {
  const res = await fetch(API);
  const notes = await res.json();
  const list = document.getElementById("notes-list");

  if (notes.length === 0) {
    list.innerHTML =
      '<p style="text-align:center; color:#999;">No notes yet. Create one!</p>';
    return;
  }

  list.innerHTML = notes
    .map(
      (note) => `
        <div class="note-card">
            <div class="note-header">
                <span class="note-title">${note.title}</span>
                <div class="note-actions">
                    <button class="btn-edit" onclick="editNote(${note.id}, '${escapeQuotes(note.title)}', '${escapeQuotes(note.content)}')">✏️</button>
                    <button class="btn-delete" onclick="deleteNote(${note.id})">🗑️</button>
                </div>
            </div>
            <p class="note-content">${note.content}</p>
            <p class="note-date">Created: ${note.created_at}</p>
        </div>
    `,
    )
    .join("");
}

async function saveNote() {
  const title = document.getElementById("title").value.trim();
  const content = document.getElementById("content").value.trim();

  if (!title || !content) {
    alert("Title and content cannot be empty!");
    return;
  }

  if (editingId) {
    // Update
    await fetch(`${API}/${editingId}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, content }),
    });
    cancelEdit();
  } else {
    // Create
    await fetch(API, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, content }),
    });
  }

  document.getElementById("title").value = "";
  document.getElementById("content").value = "";
  loadNotes();
}

function editNote(id, title, content) {
  editingId = id;
  document.getElementById("title").value = title;
  document.getElementById("content").value = content;
  document.getElementById("form-title").textContent = "Edit Note";
  document.getElementById("cancel-btn").style.display = "block";
  document.querySelector(".btn-primary").textContent = "Update Note";
  window.scrollTo(0, 0);
}

function cancelEdit() {
  editingId = null;
  document.getElementById("title").value = "";
  document.getElementById("content").value = "";
  document.getElementById("form-title").textContent = "Create New Note";
  document.getElementById("cancel-btn").style.display = "none";
  document.querySelector(".btn-primary").textContent = "Add Note";
}

async function deleteNote(id) {
  if (!confirm("Are you sure you want to delete this note?")) return;
  await fetch(`${API}/${id}`, { method: "DELETE" });
  loadNotes();
}

function escapeQuotes(str) {
  return str.replace(/'/g, "\\'").replace(/"/g, '\\"');
}

const PAGE_SIZE = 10;

let notesPage = 1;
let actionsPage = 1;

async function fetchJSON(url, options) {
  const res = await fetch(url, options);
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

async function loadNotes(page) {
  notesPage = page;
  const list = document.getElementById('notes');
  list.innerHTML = '';
  const { items, total } = await fetchJSON(`/notes/?page=${page}&page_size=${PAGE_SIZE}`);
  for (const n of items) {
    const li = document.createElement('li');
    li.textContent = `${n.title}: ${n.content}`;
    list.appendChild(li);
  }
  const totalPages = Math.max(1, Math.ceil(total / PAGE_SIZE));
  document.getElementById('notes-page-info').textContent = `Page ${page} of ${totalPages}`;
  document.getElementById('notes-prev').disabled = page <= 1;
  document.getElementById('notes-next').disabled = page >= totalPages;
}

async function loadActions(page) {
  actionsPage = page;
  const list = document.getElementById('actions');
  list.innerHTML = '';
  const { items, total } = await fetchJSON(`/action-items/?page=${page}&page_size=${PAGE_SIZE}`);
  for (const a of items) {
    const li = document.createElement('li');
    li.textContent = `${a.description} [${a.completed ? 'done' : 'open'}]`;
    if (!a.completed) {
      const btn = document.createElement('button');
      btn.textContent = 'Complete';
      btn.onclick = async () => {
        await fetchJSON(`/action-items/${a.id}/complete`, { method: 'PUT' });
        loadActions(actionsPage);
      };
      li.appendChild(btn);
    }
    list.appendChild(li);
  }
  const totalPages = Math.max(1, Math.ceil(total / PAGE_SIZE));
  document.getElementById('actions-page-info').textContent = `Page ${page} of ${totalPages}`;
  document.getElementById('actions-prev').disabled = page <= 1;
  document.getElementById('actions-next').disabled = page >= totalPages;
}

window.addEventListener('DOMContentLoaded', () => {
  document.getElementById('note-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const title = document.getElementById('note-title').value;
    const content = document.getElementById('note-content').value;
    await fetchJSON('/notes/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title, content }),
    });
    e.target.reset();
    loadNotes(notesPage);
  });

  document.getElementById('action-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const description = document.getElementById('action-desc').value;
    await fetchJSON('/action-items/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ description }),
    });
    e.target.reset();
    loadActions(actionsPage);
  });

  document.getElementById('notes-prev').addEventListener('click', () => loadNotes(notesPage - 1));
  document.getElementById('notes-next').addEventListener('click', () => loadNotes(notesPage + 1));
  document.getElementById('actions-prev').addEventListener('click', () => loadActions(actionsPage - 1));
  document.getElementById('actions-next').addEventListener('click', () => loadActions(actionsPage + 1));

  loadNotes(1);
  loadActions(1);
});

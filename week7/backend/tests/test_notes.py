from datetime import datetime


# ── helpers ───────────────────────────────────────────────────────────────────


def _post_notes(client, n: int) -> list[dict]:
    """Create n notes and return their response bodies."""
    notes = []
    for i in range(n):
        r = client.post("/notes/", json={"title": f"Note {i:02d}", "content": f"Content {i}"})
        assert r.status_code == 201
        notes.append(r.json())
    return notes


# ── existing tests ────────────────────────────────────────────────────────────


def test_create_list_and_patch_notes(client):
    payload = {"title": "Test", "content": "Hello world"}
    r = client.post("/notes/", json=payload)
    assert r.status_code == 201, r.text
    data = r.json()
    assert data["title"] == "Test"
    assert "created_at" in data and "updated_at" in data

    r = client.get("/notes/")
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

    r = client.get("/notes/", params={"q": "Hello", "limit": 10, "sort": "-created_at"})
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

    note_id = data["id"]
    r = client.patch(f"/notes/{note_id}", json={"title": "Updated"})
    assert r.status_code == 200
    patched = r.json()
    assert patched["title"] == "Updated"


# ── Pagination: limit ─────────────────────────────────────────────────────────


def test_notes_pagination_limit(client):
    """limit caps the number of results returned."""
    _post_notes(client, 5)

    r = client.get("/notes/", params={"limit": 3})
    assert r.status_code == 200
    assert len(r.json()) == 3


def test_notes_pagination_limit_zero(client):
    """limit=0 returns an empty list."""
    _post_notes(client, 2)

    r = client.get("/notes/", params={"limit": 0})
    assert r.status_code == 200
    assert r.json() == []


# ── Pagination: skip ──────────────────────────────────────────────────────────


def test_notes_pagination_skip(client):
    """skip offsets the result window relative to a stable sort."""
    _post_notes(client, 5)

    r_all = client.get("/notes/", params={"sort": "created_at", "limit": 10})
    assert r_all.status_code == 200
    all_ids = [item["id"] for item in r_all.json()]
    assert len(all_ids) == 5

    r_skip = client.get("/notes/", params={"sort": "created_at", "skip": 2, "limit": 10})
    assert r_skip.status_code == 200
    skipped_ids = [item["id"] for item in r_skip.json()]

    assert len(skipped_ids) == 3
    assert skipped_ids == all_ids[2:]


def test_notes_pagination_skip_beyond_total(client):
    """skip >= total count returns an empty list."""
    _post_notes(client, 3)

    r = client.get("/notes/", params={"skip": 100})
    assert r.status_code == 200
    assert r.json() == []


# ── Sorting ───────────────────────────────────────────────────────────────────


def test_notes_sort_ascending_created_at(client):
    """sort=created_at returns notes in oldest-first (ascending) order."""
    _post_notes(client, 4)

    r = client.get("/notes/", params={"sort": "created_at", "limit": 10})
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 4

    timestamps = [datetime.fromisoformat(item["created_at"]) for item in items]
    assert timestamps == sorted(timestamps), "Notes should be in ascending (oldest-first) order"


def test_notes_sort_descending_created_at(client):
    """sort=-created_at returns notes in newest-first (descending) order."""
    _post_notes(client, 4)

    r = client.get("/notes/", params={"sort": "-created_at", "limit": 10})
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 4

    timestamps = [datetime.fromisoformat(item["created_at"]) for item in items]
    assert timestamps == sorted(timestamps, reverse=True), "Notes should be in descending (newest-first) order"


def test_notes_sort_ascending_vs_descending(client):
    """Ascending and descending sort on created_at return the same items in opposite order."""
    _post_notes(client, 4)

    r_asc = client.get("/notes/", params={"sort": "created_at", "limit": 10})
    r_desc = client.get("/notes/", params={"sort": "-created_at", "limit": 10})
    assert r_asc.status_code == 200
    assert r_desc.status_code == 200

    asc_ids = [item["id"] for item in r_asc.json()]
    desc_ids = [item["id"] for item in r_desc.json()]

    assert set(asc_ids) == set(desc_ids), "Both sorts must return the same set of notes"
    assert asc_ids == list(reversed(desc_ids)), "Descending order must be the reverse of ascending"


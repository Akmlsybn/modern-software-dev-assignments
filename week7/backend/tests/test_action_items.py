from datetime import datetime


# ── helpers ───────────────────────────────────────────────────────────────────


def _post_items(client, n: int) -> list[dict]:
    """Create n action items and return their response bodies."""
    items = []
    for i in range(n):
        r = client.post("/action-items/", json={"description": f"Task {i:02d}"})
        assert r.status_code == 201
        items.append(r.json())
    return items


# ── existing tests ────────────────────────────────────────────────────────────


def test_create_complete_list_and_patch_action_item(client):
    payload = {"description": "Ship it"}
    r = client.post("/action-items/", json=payload)
    assert r.status_code == 201, r.text
    item = r.json()
    assert item["completed"] is False
    assert "created_at" in item and "updated_at" in item

    r = client.put(f"/action-items/{item['id']}/complete")
    assert r.status_code == 200
    done = r.json()
    assert done["completed"] is True

    r = client.get("/action-items/", params={"completed": True, "limit": 5, "sort": "-created_at"})
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

    r = client.patch(f"/action-items/{item['id']}", json={"description": "Updated"})
    assert r.status_code == 200
    patched = r.json()
    assert patched["description"] == "Updated"


# ── Pagination: limit ─────────────────────────────────────────────────────────


def test_action_items_pagination_limit(client):
    """limit caps the number of results returned."""
    _post_items(client, 5)

    r = client.get("/action-items/", params={"limit": 3})
    assert r.status_code == 200
    assert len(r.json()) == 3


def test_action_items_pagination_limit_zero(client):
    """limit=0 returns an empty list."""
    _post_items(client, 2)

    r = client.get("/action-items/", params={"limit": 0})
    assert r.status_code == 200
    assert r.json() == []


# ── Pagination: skip ──────────────────────────────────────────────────────────


def test_action_items_pagination_skip(client):
    """skip offsets the result window relative to a stable sort."""
    _post_items(client, 5)

    r_all = client.get("/action-items/", params={"sort": "created_at", "limit": 10})
    assert r_all.status_code == 200
    all_ids = [item["id"] for item in r_all.json()]
    assert len(all_ids) == 5

    r_skip = client.get("/action-items/", params={"sort": "created_at", "skip": 2, "limit": 10})
    assert r_skip.status_code == 200
    skipped_ids = [item["id"] for item in r_skip.json()]

    assert len(skipped_ids) == 3
    assert skipped_ids == all_ids[2:]


def test_action_items_pagination_skip_beyond_total(client):
    """skip >= total count returns an empty list."""
    _post_items(client, 3)

    r = client.get("/action-items/", params={"skip": 100})
    assert r.status_code == 200
    assert r.json() == []


# ── Sorting ───────────────────────────────────────────────────────────────────


def test_action_items_sort_ascending_created_at(client):
    """sort=created_at returns action items in oldest-first (ascending) order."""
    _post_items(client, 4)

    r = client.get("/action-items/", params={"sort": "created_at", "limit": 10})
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 4

    timestamps = [datetime.fromisoformat(item["created_at"]) for item in items]
    assert timestamps == sorted(timestamps), "Items should be in ascending (oldest-first) order"


def test_action_items_sort_descending_created_at(client):
    """sort=-created_at returns action items in newest-first (descending) order."""
    _post_items(client, 4)

    r = client.get("/action-items/", params={"sort": "-created_at", "limit": 10})
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 4

    timestamps = [datetime.fromisoformat(item["created_at"]) for item in items]
    assert timestamps == sorted(timestamps, reverse=True), "Items should be in descending (newest-first) order"


def test_action_items_sort_ascending_vs_descending(client):
    """Ascending and descending sort on created_at return the same items in opposite order."""
    _post_items(client, 4)

    r_asc = client.get("/action-items/", params={"sort": "created_at", "limit": 10})
    r_desc = client.get("/action-items/", params={"sort": "-created_at", "limit": 10})
    assert r_asc.status_code == 200
    assert r_desc.status_code == 200

    asc_ids = [item["id"] for item in r_asc.json()]
    desc_ids = [item["id"] for item in r_desc.json()]

    assert set(asc_ids) == set(desc_ids), "Both sorts must return the same set of action items"
    assert asc_ids == list(reversed(desc_ids)), "Descending order must be the reverse of ascending"


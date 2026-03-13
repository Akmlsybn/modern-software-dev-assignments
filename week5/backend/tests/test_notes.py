def test_create_and_list_notes(client):
    payload = {"title": "Test", "content": "Hello world"}
    r = client.post("/notes/", json=payload)
    assert r.status_code == 201, r.text
    data = r.json()
    assert data["title"] == "Test"

    r = client.get("/notes/")
    assert r.status_code == 200
    body = r.json()
    assert "items" in body
    assert "total" in body
    assert body["total"] >= 1
    assert len(body["items"]) >= 1

    r = client.get("/notes/search/")
    assert r.status_code == 200

    r = client.get("/notes/search/", params={"q": "Hello"})
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1


def test_notes_pagination_empty_last_page(client):
    # Create 3 notes, then fetch page 2 with page_size=2 (should yield 1 item)
    for i in range(3):
        client.post("/notes/", json={"title": f"Note {i}", "content": "content"})

    r = client.get("/notes/", params={"page": 2, "page_size": 2})
    assert r.status_code == 200
    body = r.json()
    assert body["total"] == 3
    assert len(body["items"]) == 1

    # Page beyond last — should return 0 items but total unchanged
    r = client.get("/notes/", params={"page": 3, "page_size": 2})
    assert r.status_code == 200
    body = r.json()
    assert body["total"] == 3
    assert len(body["items"]) == 0


def test_notes_pagination_large_page_size(client):
    for i in range(3):
        client.post("/notes/", json={"title": f"Note {i}", "content": "content"})

    r = client.get("/notes/", params={"page": 1, "page_size": 100})
    assert r.status_code == 200
    body = r.json()
    assert body["total"] == 3
    assert len(body["items"]) == 3

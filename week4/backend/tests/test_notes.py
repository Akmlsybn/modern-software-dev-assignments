def test_create_and_list_notes(client):
    payload = {"title": "Test", "content": "Hello world"}
    r = client.post("/notes/", json=payload)
    assert r.status_code == 201, r.text
    data = r.json()
    assert data["title"] == "Test"

    r = client.get("/notes/")
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

    r = client.get("/notes/search/")
    assert r.status_code == 200

    r = client.get("/notes/search/", params={"q": "Hello"})
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

def test_search_notes(client):
    client.post("/notes/", json={"title": "Resep Masakan", "content": "Bawang, telur"})
    client.post("/notes/", json={"title": "Tugas Kuliah", "content": "Belajar AI"})
    
    response = client.get("/notes/search/?q=Masakan")
    assert response.status_code == 200
    assert len(response.json()) >= 1



# Tests for 400/422 (invalid input) and 404 (not found) error scenarios.
# FastAPI returns HTTP 422 Unprocessable Entity for Pydantic validation failures
# (missing required fields, wrong types), and HTTP 404 for explicit not-found raises.


# ---------------------------------------------------------------------------
# Notes – 404 scenarios
# ---------------------------------------------------------------------------


def test_get_note_not_found(client):
    """GET /notes/{id} returns 404 when the note does not exist."""
    r = client.get("/notes/99999")
    assert r.status_code == 404


# ---------------------------------------------------------------------------
# Notes – 422 (bad-request / validation) scenarios
# ---------------------------------------------------------------------------


def test_create_note_missing_title(client):
    """POST /notes/ without 'title' returns 422."""
    r = client.post("/notes/", json={"content": "Some content"})
    assert r.status_code == 422


def test_create_note_missing_content(client):
    """POST /notes/ without 'content' returns 422."""
    r = client.post("/notes/", json={"title": "Some title"})
    assert r.status_code == 422


def test_create_note_empty_body(client):
    """POST /notes/ with an empty JSON object returns 422."""
    r = client.post("/notes/", json={})
    assert r.status_code == 422


def test_get_note_invalid_id_type(client):
    """GET /notes/{id} with a non-integer path segment returns 422."""
    r = client.get("/notes/not-an-int")
    assert r.status_code == 422


# ---------------------------------------------------------------------------
# Action items – 404 scenarios
# ---------------------------------------------------------------------------


def test_complete_action_item_not_found(client):
    """PUT /action-items/{id}/complete returns 404 when the item does not exist."""
    r = client.put("/action-items/99999/complete")
    assert r.status_code == 404


# ---------------------------------------------------------------------------
# Action items – 422 (bad-request / validation) scenarios
# ---------------------------------------------------------------------------


def test_create_action_item_missing_description(client):
    """POST /action-items/ without 'description' returns 422."""
    r = client.post("/action-items/", json={})
    assert r.status_code == 422


def test_create_action_item_no_body(client):
    """POST /action-items/ with no body at all returns 422."""
    r = client.post("/action-items/")
    assert r.status_code == 422


def test_complete_action_item_invalid_id_type(client):
    """PUT /action-items/{id}/complete with a non-integer path segment returns 422."""
    r = client.put("/action-items/not-an-int/complete")
    assert r.status_code == 422

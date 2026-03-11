# Action Item Extractor

**A FastAPI-based application for extracting and managing action items from notes with support for both rule-based and LLM-powered extraction.**

## 📋 Project Overview

Action Item Extractor is a web application built with FastAPI and SQLite that helps users extract actionable tasks from unstructured notes. The application supports two extraction methods:

- **Rule-based Extraction**: Uses pattern matching to identify common action item formats (bullet points, checkboxes, imperative starters)
- **LLM-based Extraction**: Leverages Ollama's `llama3.1:8b` model for intelligent, semantic understanding of action items

The application includes a minimal HTML frontend for easy interaction and a RESTful API for programmatic access. All notes and action items are persisted in SQLite for data durability.

### Key Features

✨ **Dual Extraction Methods** - Choose between fast pattern matching or LLM-powered understanding  
📝 **Note Management** - Save notes alongside extracted action items  
✅ **Action Item Tracking** - Mark items as done/not done with persistent state  
🔍 **Filtering Capabilities** - Query action items by note ID or list all items  
📱 **Minimal Web UI** - Pure HTML/CSS/JS frontend with no frameworks  
⚡ **RESTful API** - Well-structured endpoints with proper HTTP status codes  
🗄️ **SQLite Database** - Automatic initialization and schema migration

---

## 🚀 Setup & Installation

### Prerequisites

- **Python 3.10+** (<=3.11 recommended for compatibility)
- **Conda** or **Poetry** for dependency management
- **Ollama** (if using LLM extraction)
- **Git**

### Option 1: Setup with Poetry (Recommended)

Poetry is the preferred dependency manager for this project.

```bash
# Navigate to the project root
cd "d:\Semester 6\PPKPL\LLM Project\modern-software-dev-assignments"

# Install dependencies using Poetry
poetry install

# Activate the Poetry virtual environment
poetry shell
```

### Option 2: Setup with Conda

If you prefer using Conda:

```bash
# Create a conda environment
conda create -n action-extractor python=3.10

# Activate the environment
conda activate action-extractor

# Navigate to the project root
cd "d:\Semester 6\PPKPL\LLM Project\modern-software-dev-assignments"

# Install dependencies from pyproject.toml
pip install -e .
# Or manually install key packages:
pip install fastapi uvicorn sqlalchemy pydantic python-dotenv openai ollama
```

### Setup Ollama (For LLM Extraction)

If you plan to use the LLM extraction endpoint, you need to have Ollama running:

```bash
# Install Ollama (if not already installed)
# Visit: https://ollama.ai

# Pull the required model
ollama pull llama3.1:8b

# Start Ollama service (in a separate terminal)
ollama serve

# By default, Ollama listens on http://localhost:11434
```

### Environment Configuration

Create a `.env` file in the project root (optional):

```env
# .env
# Ollama configuration (defaults shown)
OLLAMA_HOST=http://localhost:11434

# OpenAI configuration (if using OpenAI APIs)
OPENAI_API_KEY=your_key_here
```

---

## 🏃 Running the Application

### Start the Backend Server

Once dependencies are installed and Ollama is running (if using LLM extraction):

```bash
# Using Poetry
poetry run uvicorn week2.app.main:app --reload --port 8000

# Or if you've activated the Poetry shell
uvicorn week2.app.main:app --reload --port 8000

# Or with Conda
uvicorn week2.app.main:app --reload --port 8000
```

**Options:**

- `--reload`: Auto-restart on code changes (development only)
- `--port 8000`: Specify port (default is 8000)
- `--host 0.0.0.0`: Listen on all interfaces

### Access the Application

Once the server is running:

- **Web UI**: http://localhost:8000
- **API Docs (Swagger)**: http://localhost:8000/docs
- **API Schema (ReDoc)**: http://localhost:8000/redoc

---

## 📡 API Endpoints

All endpoints return JSON responses with appropriate HTTP status codes. The base URL is `/api` (currently at root, but can be namespaced).

### Action Items Endpoints

#### Extract Items (Rule-based)

```http
POST /action-items/extract
Content-Type: application/json

{
  "text": "- [ ] Set up database\n- Implement extract endpoint\nTODO: Write tests",
  "save_note": true
}
```

**Response (200 OK):**

```json
{
  "note_id": 1,
  "items": [
    {
      "id": 1,
      "note_id": 1,
      "text": "Set up database",
      "done": false,
      "created_at": "2024-03-11T10:30:45"
    },
    {
      "id": 2,
      "note_id": 1,
      "text": "Implement extract endpoint",
      "done": false,
      "created_at": "2024-03-11T10:30:45"
    }
  ]
}
```

#### Extract Items (LLM-powered)

```http
POST /action-items/extract-llm
Content-Type: application/json

{
  "text": "During the meeting, we discussed improving API performance...",
  "save_note": true
}
```

**Response:** Same as rule-based extraction (200 OK)

#### List All Action Items

```http
GET /action-items/
```

**Query Parameters:**

- `note_id` (optional): Filter by note ID

**Response (200 OK):**

```json
[
  {
    "id": 1,
    "note_id": 1,
    "text": "Set up database",
    "done": false,
    "created_at": "2024-03-11T10:30:45"
  },
  {
    "id": 2,
    "note_id": null,
    "text": "Review PR #42",
    "done": true,
    "created_at": "2024-03-11T10:32:00"
  }
]
```

#### Get Single Action Item

```http
GET /action-items/{action_item_id}
```

**Response (200 OK):**

```json
{
  "id": 1,
  "note_id": 1,
  "text": "Set up database",
  "done": false,
  "created_at": "2024-03-11T10:30:45"
}
```

**Error Responses:**

- `400 Bad Request`: Invalid action item ID
- `404 Not Found`: Action item does not exist

#### Create Action Item

```http
POST /action-items/
Content-Type: application/json

{
  "text": "Schedule team standup"
}
```

**Response (201 Created):**

```json
{
  "id": 3,
  "text": "Schedule team standup"
}
```

#### Mark Action Item as Done

```http
PUT /action-items/{action_item_id}/done
Content-Type: application/json

{
  "done": true
}
```

**Response (200 OK):**

```json
{
  "id": 1,
  "note_id": 1,
  "text": "Set up database",
  "done": true,
  "created_at": "2024-03-11T10:30:45"
}
```

**Legacy POST method (deprecated):**

```http
POST /action-items/{action_item_id}/done
```

---

### Notes Endpoints

#### Create Note

```http
POST /notes/
Content-Type: application/json

{
  "content": "Meeting notes from March 11, 2024..."
}
```

**Response (201 Created):**

```json
{
  "id": 1,
  "content": "Meeting notes from March 11, 2024...",
  "created_at": "2024-03-11T10:30:45"
}
```

#### List All Notes

```http
GET /notes/
```

**Response (200 OK):**

```json
[
  {
    "id": 1,
    "content": "Meeting notes...",
    "created_at": "2024-03-11T10:30:45"
  },
  {
    "id": 2,
    "content": "Another note...",
    "created_at": "2024-03-11T09:15:30"
  }
]
```

#### Get Single Note

```http
GET /notes/{note_id}
```

**Response (200 OK):**

```json
{
  "id": 1,
  "content": "Meeting notes from March 11, 2024...",
  "created_at": "2024-03-11T10:30:45"
}
```

**Error Responses:**

- `400 Bad Request`: Invalid note ID
- `404 Not Found`: Note does not exist

---

## 🧪 Testing

### Running Unit Tests

The project uses **pytest** for unit testing with test fixtures and mocking support.

```bash
# Run all tests
poetry run pytest

# Run tests for week2 only
poetry run pytest week2/tests/

# Run a specific test file
poetry run pytest week2/tests/test_extract.py

# Run with verbose output
poetry run pytest week2/tests/ -v

# Run with coverage report
poetry run pytest week2/tests/ --cov=week2.app

# Run tests and stop on first failure
poetry run pytest week2/tests/ -x

# Run tests matching a pattern
poetry run pytest week2/tests/ -k "extract"
```

### Test File Structure

```
week2/tests/
├── __init__.py
├── conftest.py              # Fixtures and shared test config
├── test_extract.py          # Tests for extraction logic
├── test_action_items.py     # Tests for action item endpoints
└── test_notes.py            # Tests for note endpoints
```

### Example Test Setup

The test suite uses pytest fixtures (defined in `conftest.py`) for:

- **Test database**: In-memory SQLite for isolated tests
- **FastAPI test client**: HTTPx-based client for endpoint testing
- **Mock Ollama responses**: For LLM extraction testing without API calls

```bash
# Run tests with custom markers
poetry run pytest -m "not slow" week2/tests/
```

---

## 📂 Project Structure

```
week2/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app initialization
│   ├── db.py                # Database connection & schema
│   ├── models.py            # SQLAlchemy models (if used)
│   ├── schemas.py           # Pydantic schemas for validation
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── action_items.py  # /action-items endpoints
│   │   └── notes.py         # /notes endpoints
│   └── services/
│       ├── __init__.py
│       └── extract.py       # Extraction logic & LLM integration
├── frontend/
│   ├── index.html           # Main HTML interface
│   ├── app.js               # Frontend JavaScript
│   └── styles.css           # Frontend styling
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Pytest fixtures
│   ├── test_extract.py
│   ├── test_action_items.py
│   └── test_notes.py
├── data/
│   └── app.db               # SQLite database (auto-created)
└── README.md                # This file
```

---

## 🛠️ Development Workflow

### Code Quality Tools

The project includes pre-configured tools for code quality:

```bash
# Format code with Black
poetry run black week2/

# Lint with Ruff
poetry run ruff check week2/

# Run all pre-commit hooks
poetry run pre-commit run --all-files
```

### Configuration

- **Black**: Line length 100, targets Python 3.10+
- **Ruff**: Line length 100, checks: E, F, I, UP, B (excludes long lines and B008)
- **Pre-commit**: Hooks for formatting, linting, and common issues

---

## 🔧 Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'ollama'`

**Solution**: Make sure dependencies are installed:

```bash
poetry install
poetry shell
```

### Issue: Ollama connection error when using LLM extraction

**Solution**: Ensure Ollama is running:

```bash
ollama serve  # In a separate terminal
# Then verify: curl http://localhost:11434/api/tags
```

### Issue: Database locked error

**Solution**: Delete the database and restart:

```bash
rm -rf week2/data/app.db
# Restart the server (it will recreate the database)
```

### Issue: Port 8000 already in use

**Solution**: Use a different port:

```bash
uvicorn week2.app.main:app --port 8001
```

---

## 📝 API Documentation

Interactive API documentation is automatically generated by FastAPI:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

These tools allow you to test endpoints directly in your browser.

---

## 🤝 Contributing

When contributing code:

1. Follow the code style (Black formatting, Ruff linting)
2. Add tests for new functionality
3. Update documentation
4. Use descriptive commit messages
5. Include comments for non-obvious logic (especially include `# --- GENERATED BY AI ---` markers for generated code)

---

## 📜 License

Part of course assignments for modern software development practices.

---

## ❓ FAQ

**Q: Can I use the rule-based extraction without Ollama?**  
A: Yes! The `/action-items/extract` endpoint uses rule-based extraction and works without Ollama. Only `/action-items/extract-llm` requires Ollama.

**Q: How can I add more extraction methods?**  
A: Add new extraction functions in `week2/app/services/extract.py` and create corresponding endpoints in `week2/app/routers/action_items.py`.

**Q: What happens to notes when I delete an action item?**  
A: Action items and notes are independent. Deleting an action item doesn't affect the note it came from.

**Q: Can I export notes and action items?**  
A: Currently, you can query the API and save results. Consider adding CSV/JSON export endpoints in a future version.

---

**Last Updated**: March 2024  
**Version**: 0.1.0

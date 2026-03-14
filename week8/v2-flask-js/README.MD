# Notes Manager - V2 (Flask + HTML/JS)

A full-stack notes management application built with Python Flask backend and vanilla HTML/CSS/JavaScript frontend.

## Tech Stack

**Frontend:**

- HTML5
- CSS3
- Vanilla JavaScript

**Backend:**

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-CORS
- SQLite (database)

## Prerequisites

- Python 3.8 or higher
- pip

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd week8/v2-flask-js
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python app.py
```

The app will be available at `http://localhost:5000`

## Project Structure

```
v2-flask-js/
├── app.py              # Flask backend (API + routes)
├── requirements.txt    # Python dependencies
├── README.md           # Documentation
└── static/
    ├── index.html      # Frontend HTML
    ├── style.css       # Styling
    └── script.js       # Frontend logic
```

## API Endpoints

| Method | Endpoint       | Description       |
| ------ | -------------- | ----------------- |
| GET    | /api/notes     | Get all notes     |
| POST   | /api/notes     | Create a new note |
| PUT    | /api/notes/:id | Update a note     |
| DELETE | /api/notes/:id | Delete a note     |

## Features

- Create notes with title and content
- View all notes
- Edit existing notes
- Delete notes with confirmation
- Persistent storage with SQLite
- Basic validation and error handling

## Known Issues

- No authentication (demo purposes only)
- SQLite not recommended for production

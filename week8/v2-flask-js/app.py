from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at.strftime('%b %d, %Y, %I:%M %p')
        }

# Routes
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/notes', methods=['GET'])
def get_notes():
    notes = Note.query.order_by(Note.created_at.desc()).all()
    return jsonify([note.to_dict() for note in notes])

@app.route('/api/notes', methods=['POST'])
def create_note():
    data = request.get_json()
    if not data.get('title') or not data.get('content'):
        return jsonify({'error': 'Title and content are required'}), 400
    note = Note(title=data['title'], content=data['content'])
    db.session.add(note)
    db.session.commit()
    return jsonify(note.to_dict()), 201

@app.route('/api/notes/<int:id>', methods=['PUT'])
def update_note(id):
    note = Note.query.get_or_404(id)
    data = request.get_json()
    if not data.get('title') or not data.get('content'):
        return jsonify({'error': 'Title and content are required'}), 400
    note.title = data['title']
    note.content = data['content']
    db.session.commit()
    return jsonify(note.to_dict())

@app.route('/api/notes/<int:id>', methods=['DELETE'])
def delete_note(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return jsonify({'message': 'Note deleted'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
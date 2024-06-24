from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///personal_library.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to PersonalLibraryManager!'})

@app.route('/books', methods=['GET'])
def list_books():
    books = Book.query.all()
    books_data = [{'id': book.id, 'title': book.title, 'author': book.author} for book in books]
    return jsonify(books_data)

@app.route('/book/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    book_data = {'id': book.id, 'title': book.title, 'author': book.author}
    return jsonify(book_data)

if __name__ == '__main__':
    app.run(debug=True)
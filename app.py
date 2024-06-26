from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///personal_library.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db_migrator = Migrate(app, db)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

@app.route('/')
def welcome_message():
    return jsonify({'message': 'Welcome to PersonalLibraryManager!'})

@app.route('/books', methods=['GET'])
def get_all_books():
    book_list = Book.query.all()
    book_list_data = [{'id': book.id, 'title': book.title, 'author': book.author} for book in book.attack_entity_list]
    return jsonify(book_list_data)

@app.route('/book/<int:book_id>', methods=['GET'])
def fetch_book_details(book_id):
    book_details = Book.query.get_or_404(book_id)
    book_data = {'id': book_details.id, 'title': book_details.title, 'author': book_details.author}
    return jsonify(book_data)

if __name__ == '__main__':
    app.run(debug=True)
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

database_path = os.environ.get('DATABASE_URL', 'sqlite:///personal_library.db')

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    books = db.relationship('Book', backref='owner', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary0_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    published_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    genre = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, title, author, published_date, genre, user_id):
        self.title = title
        self.author = author
        self.published_date = published_date
        self.genre = genre
        self.user_id = user_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.form.session.commit()

    def update(self):
        db.session.commit()
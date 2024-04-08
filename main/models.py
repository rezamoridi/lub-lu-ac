from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key= True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    user_name = db.Column(db.String(150))
    phone_number = db.Column(db.String(11), unique=True)
    notes = db.relationship('Note')

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    genere = db.Column(db.String(20))
    image = db.Column(db.String(255))
    author = db.Column(db.String(25))
    link = db.Column(db.String(255))

    def __init__(self, title, genere, image_link, author, book_link) -> None:
        self.title = title
        self.genere = genere
        self.image = image_link
        self.author = author
        self.link = book_link

from sqlalchemy.sql import func
from config import db

owner_table = db.Table('owner', 
    db.Column('author_id', db.Integer, db.ForeignKey('author.id', ondelete='cascade'), primary_key=True), 
    db.Column('book_id', db.Integer, db.ForeignKey('book.id', ondelete='cascade'), primary_key=True))

class book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(500))
    description = db.Column(db.Text())
    authors = db.relationship('author', secondary = owner_table)

class author(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    notes = db.Column(db.Text())
    books = db.relationship('book', secondary = owner_table)
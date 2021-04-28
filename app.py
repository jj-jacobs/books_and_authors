from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_migrate import Migrate
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books_and_authors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

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

@app.route("/")
def home():
    authors = author.query.all()
    books = book.query.all()
    print(authors, books)
    return render_template("home.html", books = books, authors = authors)

@app.route("/create_author", methods = ["POST"])
def create_author():
    new_author = author(first_name = request.form["first_name"], last_name = request.form["last_name"], notes = request.form["notes"])
    db.session.add(new_author)
    db.session.commit()
    return redirect("/")

@app.route("/create_book", methods = ["POST"])
def create_book():
    new_book = book(title = request.form["title"], description = request.form["description"], author_id = request.form["choose_author"])
    db.session.add(new_book)
    existing_book = book.query.get(1)
    existing_author = author.query.get(1)
    existing_book.authors.append(existing_author)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
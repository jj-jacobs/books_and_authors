from flask import render_template, redirect, request
from config import db
from models import author, book

def home():
    authors = author.query.all()
    books = book.query.all()
    print(authors, books)
    return render_template("home.html", books = books, authors = authors)

def create_author():
    new_author = author(first_name = request.form["first_name"], last_name = request.form["last_name"], notes = request.form["notes"])
    db.session.add(new_author)
    db.session.commit()
    return redirect("/")

def create_book():
    new_book = book(title = request.form["title"], description = request.form["description"])
    db.session.add(new_book)
    existing_author = author.query.get(request.form["choose_author"])
    new_book.authors.append(existing_author)
    db.session.commit()
    return redirect("/")

from flask import Blueprint, render_template, request, redirect, flash, url_for
from .models import Book
from . import db


views = Blueprint('views', __name__)


# root view
@views.route('/')
def home():
    return render_template("home.html")



# Associations view
@views.route('/associations')
def associations():
    return render_template("associations.html")

# Advanture view
@views.route('advanture')
def advanture():
    return render_template("advanture.html")

# project detail view
@views.route('/project')
def project_detail():
    return render_template("project_detail.html")


# library Views

# book shelf
@views.route('/library', methods=['GET'])
def library():
    books = Book.query.all()
    for book in books:
        print(f'Title: {book.title}, Author: {book.author}')
    return render_template("library.html", books=books)


# add book
@views.route('/add-book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        genere = request.form.get('genere')
        image = request.form.get('image')
        link = request.form.get('book-link')
        if title:
            new_book = Book(title=title, genere=genere, image_link=image,
                            author=author,
                            book_link=link)
            db.session.add(new_book)
            db.session.commit()
            flash('Book Added Successfully', category="success")
            return redirect(url_for('views.library'))  # Redirect after successful submission
        else:
            flash('Inputs are required!', category='error')

    return render_template('add-book.html')


# delete book
@views.route('/edit-books', methods=['GET', 'POST'])
def delete_book():
    books = Book.query.all()
    if 'delete-btn' in request.form:
        book_id = request.form.get('delete-btn')
        book_to_delete = Book.query.get(book_id)

        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect(url_for('views.library'))
        
    return render_template('delete-book.html', books=books)
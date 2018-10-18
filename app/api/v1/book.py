from flask import jsonify
from sqlalchemy import or_

from app.libs.redprint import Redprint
from app.models.book import Book
from app.validators.forms import SearchForm

api = Redprint('book')


@api.route('/get')
def get_book():
    return 'book'


@api.route('/search')
def search():
    form = SearchForm().validate_for_api()
    q = form.q.data.strip()
    q = '%' + form.q.data + '%'
    books = Book.query.filter(
        or_(Book.title.like(q), Book.publisher.like(q))).all()
    books = [book.hide('summary') for book in books]
    return jsonify(books)



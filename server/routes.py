
from flask import request, render_template, make_response

from server.webapp import flaskapp, cursor
from server.models import Book


@flaskapp.route('/')
def index():
    name = request.args.get('name')
    author = request.args.get('author')
    read = bool(request.args.get('read'))

    if name:
        cursor.execute(
            "SELECT * FROM books WHERE name LIKE '%" + name + "%'"
        )
        books = [Book(*row) for row in cursor]

    elif author:
        cursor.execute(
            "SELECT * FROM books WHERE author LIKE '%" + author + "%'"
        )
        books = [Book(*row) for row in cursor]

    else:
        cursor.execute("SELECT name, author, read FROM books")
        books = [Book(*row) for row in cursor]

    return render_template('books.html', books=books)

@flaskapp.route('/search-demo')
def search_demo():
    search_term = request.args.get('search')

    query = (
        "SELECT * FROM books WHERE name LIKE '%"
        + search_term
        + "%'"
    )

        cursor.execute(query)

        books = [Book(*row) for row in cursor]

    return render_template('books.html', books=books)




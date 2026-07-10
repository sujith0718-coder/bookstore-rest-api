# Flask REST API

from flask import Flask, jsonify, request
from bookstore import Bookstore

app = Flask(__name__)

# Use the Library API
store = Bookstore()

# Sample data
store.add_book("The Great Gatsby", "F. Scott Fitzgerald")
store.add_book("To Kill a Mockingbird", "Harper Lee")


# 1. Home Route
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Bookstore REST API"
    })


# 2. Get all books
@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(store.get_all_books())


# 3. Get book by ID
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = store.get_book_by_id(book_id)

    if book:
        return jsonify(book)

    return jsonify({"message": "Book not found"}), 404


# 4. Add book
@app.route("/books", methods=["POST"])
def add_book():

    data = request.get_json()

    new_book = store.add_book(
        data["title"],
        data["author"]
    )

    return jsonify(new_book), 201


# 5. About
@app.route("/about", methods=["GET"])
def about():
    return jsonify({
        "project": "Bookstore Management REST API",
        "library": "Bookstore Library API",
        "framework": "Flask"
    })


if __name__ == "__main__":
    app.run(debug=True)
# Library API
class Bookstore:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = {
            "id": len(self.books) + 1,
            "title": title,
            "author": author
        }
        self.books.append(book)
        return book

    def get_all_books(self):
        return self.books

    def get_book_by_id(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                return book
        return None
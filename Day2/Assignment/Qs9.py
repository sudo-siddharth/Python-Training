class Book:
    def __init__(self, title: str, author: str, isbn: str, available: bool = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
    
    def __str__(self):
        return f"Book: {self.title} by {self.author} (ISBN: {self.isbn}) - Available: {'Yes' if self.available else 'No'}"


class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book: Book):
        self.books.append(book)
    
    def list_books(self):
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")
    
    def borrow_book(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print(f"Successfully borrowed '{book.title}'")
                    return
                else:
                    print(f"'{book.title}' is already checked out")
                    return
        print("Book not available.")
    
    def return_book(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    print(f"Successfully returned '{book.title}'")
                    return
                else:
                    print(f"'{book.title}' was not checked out")
                    return
        print("Book not found in library.")

library = Library()
library.add_book(Book("Mastering Python in few Days", "Sai Sanketh", "84845"))
library.add_book(Book("BIP Reports Mastery", "Aakash Kurunth", "94567"))

print("\nAll books:")
library.list_books()

print("\nBorrowing books:")
library.borrow_book("Mastering Python in few Days")
library.borrow_book("BIP Reports Mastery")

print("\nReturning books:")
library.return_book("BIP Reports Mastery")
library.return_book("Missing Book")

print("\nUpdated book list:")
library.list_books()
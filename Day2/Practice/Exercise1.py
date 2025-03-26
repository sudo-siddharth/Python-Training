class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")


book1 = Book("Python Master Guide", "Sai Sanketh", 100)
book2 = Book("Becoming OG in MS Excel", "Darshan JS", 200)
book3 = Book("BIP Reports Mastery", "Aakash Kurunth", 5000)


book1.display_details()
book2.display_details()
book3.display_details()
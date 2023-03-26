class Author:
    def __init__(self, first_name, last_name, birth_date):
        self.dict_info = \
            {
                "first name": first_name,
                "last name": last_name,
                "birth date": birth_date
            }

    def __str__(self):
        return f"{self.dict_info['first name']} " \
               f"{self.dict_info['last name']} " \
               f"({self.dict_info['birth date']})"


class Book:
    def __init__(self, title, author, publication_year):
        self.dict_book = \
            {
                "title": title,
                "author": author,
                "publication_year": publication_year
            }
        self.author = author

    def __str__(self):
        return f"{self.dict_book['title']}" \
               f" {self.dict_book['author']['first_name']} " \
               f"{self.dict_book['author']['last_name']} " \
               f"({self.dict_book['publication_year']})"


class Library:
    def __init__(self):
        self.library = {}

    def add_book(self, book):
        self.library.update(book)

    def __str__(self):
        return f"{self.library}"


author1 = Author("Джордж", "Оруелл", "25.06.1903")
author2 = Author("Алдус", "Хаксли", "26.07.1894")

book1 = Book("Війна світів", author1, 1939)
book2 = Book("1984", author1, 1949)
book3 = Book("Красне рабство", author2, 1932)

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library)

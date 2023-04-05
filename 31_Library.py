import json


class Author:
    def __init__(self, first_name, last_name, birth_day):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_day

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.birth_date})"


class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return f"{self.title} {self.author.first_name} " \
               f"{self.author.last_name} " \
               f"({self.publication_year})"


class Library:
    def __init__(self):
        self.library = []

    def add_book(self, book):
        self.library.append(book)

    def remove_book(self, book):
        self.library.remove(book)

    def dump_to_json(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([{
                "title": book.title,
                "author": {
                    "first_name": book.author.first_name,
                    "last_name": book.author.last_name,
                    "birth_date": book.author.birth_date
                },
                "publication_year": book.publication_year
            } for book in self.library], f, indent=4, ensure_ascii=False)

    def __str__(self):
        return "\n".join(str(book) for book in self.library)


author1 = Author("Джордж", "Оруэлл", "25.06.1903")
author2 = Author("Алдус", "Хаксли", "26.07.1894")

book1 = Book("Война миров", author1, 1939)
book2 = Book("1984", author1, 1949)
book3 = Book("Красное рабство", author2, 1932)

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
# library.remove_book(book1)


print(library)
library.dump_to_json("library.json")

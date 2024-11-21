# Класс библиотеки и методы работы с книгами.
import json
from typing import List, Optional

from models.book import Book


class Library:
    def __init__(self, filename='data/library.json'):
        self.filename = filename
        self.books: List[Book] = self.load_books()

    def load_books(self):
        try:
            with open(self.filename, 'r') as file:
                books_data = json.load(file)
                return [
                    Book(book_id=book['id'],
                         title=book['title'],
                         author=book['author'],
                         year=book['year'],
                         status=book['status']) for book in books_data
                    ]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_books(self):
        with open(self.filename, 'w') as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4)

    def add_book(self, title, author, year, status='в наличии'):
        for book in self.books:
            if book.title == title and book.author == author:
                return f"\nКнига '{title}' автора {author} уже существует."

        max_id = max((book.id for book in self.books), default=0)
        book_id = max_id + 1
        new_book = Book(book_id, title, author, year, status)
        self.books.append(new_book)
        self.save_books()
        return f"\nКнига '{title}' успешно добавлена."

    def delete_book(self, book_id):
        book_to_remove = next(
            (book for book in self.books if book.id == book_id),
            None
            )

        if book_to_remove:
            self.books.remove(book_to_remove)
            self.save_books()
            return "Книга успешно удалена."
        else:
            return "Книга не найдена!"

    def search_book(self, book_search):
        results = []
        for book in self.books:
            if (book_search.lower() in book.title.lower() or
                    book_search.lower() in book.author.lower() or
                    book_search == str(book.year)):
                results.append(
                            f"|{book.id}| "
                            f"{book.title}| "
                            f"{book.author}| "
                            f"{book.year}| "
                            f"{book.status}|"
                )

        return results if results else ["Книга не найдена."]

    def update_book_status(self, book_id):
        for book in self.books:
            if book.id == book_id:
                new_status = input("Введите новый статус: ")
                book.status = new_status
                self.save_books()
                return f"Статус книги изменен на '{new_status}'."

        return "Книга не найдена."

    def list_books(self):
        if not self.books:
            return "\nСписок книг пуст."

        output = "\nСписок всех книг:\n"
        for book in self.books:
            output += (
                        f"{book.id} | "
                        f"{book.title} "
                        f"{book.author} "
                        f"({book.year}) "
                        f"{book.status} \n"
                    )

        return output

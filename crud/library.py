import json
from typing import List, Optional

from models.book import Book


class Library:
    """
    Класс для управления библиотекой книг.

    Атрибуты: books (list): Список книг в библиотеке.
    """
    def __init__(self, filename='data/library.json'):
        self.filename = filename
        self.books: List[Book] = self.load_books()

    # Функция загрузки всех книг.
    def load_books(self) -> List[Book]:
        """
        Загружает книги из указанного файла.

        :param filename: Путь к файлу с данными о книгах.
        """
        try:
            # Открываем файл и читаем данные.
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

    #  Функция сохраниня книг.
    def save_books(self) -> None:
        """
        Эта функция открывает файл, указанный в атрибуте `self.filename`,
        и записывает все книги из списка `self.books` в формате JSON.
        Каждая книга преобразуется в словарь с помощью метода `to_dict()`.
        """
        with open(self.filename, 'w') as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4)

    #  Функция сохраниня книг.
    def add_book(
        self, title: str, author: str,
        year: int, status: str = 'в наличии'
    ) -> str:
        """
        Эта функция проверяет, есть ли книга с указанным заголовком и автором.
        Если книга уже есть, возвращается сообщение об этом. В противном случае
        создается новая книга и добавляется в список `self.books`.
        После добавления книги, список книг сохраняется в файл.

        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год публикации книги.
        :param status: Статус книги. По умолчанию 'в наличии'.
        :return: Сообщение о результате операции добавления книги.
        """
        for book in self.books:
            if book.title == title and book.author == author:
                return f"\nКнига '{title}' автора {author} уже существует."

        max_id = max((book.id for book in self.books), default=0)
        book_id = max_id + 1
        new_book = Book(book_id, title, author, year, status)
        self.books.append(new_book)
        self.save_books()
        return f"\nКнига '{title}' успешно добавлена."

    # Функция удаления книги.
    def delete_book(self, book_id: int) -> str:
        """
        Эта функция ищет книгу с указанным идентификатором в
        списке `self.books`. Если книга найдена, она удаляется,
        и список книг сохраняется в файл. Если книга с заданным
        идентификатором не найдена, возвращается соответствующее сообщение.

        :param book_id: Идентификатор книги, которую необходимо удалить.
        :return: Сообщение о результате операции удаления книги.
        """
        book_to_remove: Optional[Book] = next(
            (book for book in self.books if book.id == book_id),
            None
            )

        if book_to_remove:
            self.books.remove(book_to_remove)
            self.save_books()
            return "\nКнига успешно удалена."
        else:
            return "\nКнига не найдена!"

    # Функция поиска книг.
    def search_book(self, book_search: str) -> List[str]:
        """
        Эта функция выполняет поиск книг в списке `self.books`, проверяя,
        содержится ли строка `book_search` в заголовке книги, имени автора
        или годе публикации.
        Результаты поиска возвращаются в виде списка строк,
        каждая из которых содержит информацию о найденной книге.
        Если книги не найдены, возвращается сообщение "Книга не найдена."

        :param book_search: Строка для поиска, которая может содержать часть
                        заголовка книги, имя автора или год публикации.
        :return: Список строк с информацией о найденных книгах или сообщение
             о том, что книга не найдена.
        """
        results: List[str] = []
        for book in self.books:
            if (book_search.lower() in book.title.lower() or
                    book_search.lower() in book.author.lower() or
                    book_search == str(book.year)):
                results.append(
                            f"|{book.id}| "
                            f"{book.title} "
                            f"{book.author} "
                            f"{book.year} "
                            f"{book.status} "
                )

        return results if results else ["Книга не найдена."]

    # Функция изменения статуса книг.
    def update_book_status(self, book_id: int) -> str:
        """
        Эта функция ищет книгу с указанным идентификатором
        в списке `self.books`.
        Если книга найдена, пользователю предлагается ввести новый статус.
        Статус может быть либо 'в наличии', либо 'выдана'.
        Если введенный статус некорректен, возвращается сообщение об ошибке.
        Если статус книги уже соответствует введенному, функция также
        уведомляет об этом. После изменения статуса книга сохраняется в файл.

        :param book_id: Идентификатор книги, статус которой
        необходимо изменить.
        :return: Сообщение о результате операции изменения статуса книги.
        """
        valid_statuses = ['в наличии', 'выдана']
        for book in self.books:
            if book.id == book_id:
                new_status = input("Введите новый статус: ")

                if new_status not in valid_statuses:
                    return "Ошибка: введите корректный статус."

                if book.status == new_status:
                    return f"Статус книги уже установлен на '{new_status}'."

                book.status = new_status
                self.save_books()
                return f"Статус книги изменен на '{new_status}'."

        return "Книга не найдена."

    # Функция вывода списка книг.
    def list_books(self) -> str:
        """
        Эта функция проверяет, есть ли книги в списке `self.books`.
        Если список пуст, возвращается сообщение о том, что список книг пуст.
        Если книги есть, функция формирует строку с информацией о каждой книге,
        включая идентификатор, заголовок, автора, год публикации и статус.

        :return: Строка с информацией о всех книгах или сообщение о том,
        что список пуст.
        """
        if not self.books:
            return "\nСписок книг пуст."

        output = (
            f"\n{'ID':<5} | "
            f"{'Название':<30} | "
            f"{'Автор':<20} | "
            f"{'Год':<5} | "
            f"{'Статус':<10}\n"
        )
        output += "-" * 80 + "\n"

        for book in self.books:
            output += (
                f"{book.id:<5} | "
                f"{book.title:<30} | "
                f"{book.author:<20} | "
                f"{book.year:<5} | "
                f"{book.status:<10}\n"
            )

        return output

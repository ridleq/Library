import unittest
from crud.library import Library


class TestAddBook(unittest.TestCase):  # Тест добавления книг и вызов ошибок.

    def test_add_book(self):
        library = Library()

        result = library.add_book("1984", "Джо", 1949)
        self.assertEqual(result, "\nКнига '1984' успешно добавлена.")
        self.assertEqual(len(library.books), 1)
        self.assertEqual(library.books[0].title, "1984")

        result = library.add_book("1984", "Джо", 1949)
        self.assertEqual(result, "\nКнига '1984' автора Джо уже существует.")
        self.assertEqual(len(library.books), 1)

        result = library.add_book("Братья", "Федор", 1880)
        self.assertEqual(result, "\nКнига 'Братья' успешно добавлена.")
        self.assertEqual(len(library.books), 2)
        self.assertEqual(library.books[1].title, "Братья")


if __name__ == "__main__":
    unittest.main()

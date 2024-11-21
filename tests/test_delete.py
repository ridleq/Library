import unittest

from crud.library import Library


class TestDeleteBook(unittest.TestCase):  # Тест удаления книг и вызов ошибок.
    def test_delete_book(self):
        library = Library()

        result = library.delete_book(1)
        assert result == "\nКнига успешно удалена."
        assert len(library.books) == 1
        assert library.books[0].id == 2

        result = library.delete_book(2)
        assert result == "\nКнига успешно удалена."
        assert len(library.books) == 0

        result = library.delete_book(3)
        assert result == "\nКнига не найдена!"


if __name__ == "__main__":
    unittest.main()

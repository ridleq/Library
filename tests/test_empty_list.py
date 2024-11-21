import unittest

from crud.library import Library


class TestEmptyListBook(unittest.TestCase):  # Тест пустого списка книг.
    def test_empty_list_books(self):
        library = Library()
        result = library.list_books()
        assert result == '\nСписок книг пуст.'


if __name__ == "__main__":
    unittest.main()

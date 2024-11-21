import unittest

from crud.library import Library


class TestSearchBook(unittest.TestCase):  # Тест поиска книг.
    def test_search_book(self):
        library = Library()
        result = library.search_book("Братья")
        assert result == [
            '|2| Братья Федор 1880 в наличии '
        ]

        result = library.search_book("Море")
        assert result == ['Книга не найдена.']


if __name__ == "__main__":
    unittest.main()

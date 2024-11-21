import unittest

from crud.library import Library


class TestListBook(unittest.TestCase):  # Тест вывода всех книг.
    def test_list_books(self):
        library = Library()
        result = library.list_books()

        expected_result = (
            '\nСписок всех книг:\n'
            '1 | 1984 Джо (1949) выдана \n'
            '2 | Братья Федор (1880) в наличии \n'
        )

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()

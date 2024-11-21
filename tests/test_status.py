import unittest

from unittest.mock import patch

from crud.library import Library


class TestUpdateStatus(unittest.TestCase):  # Тест обновления статуса и ошибок.
    def test_update_book_status(self):
        library = Library()

        with patch('builtins.input', return_value='выдана'):
            result = library.update_book_status(1)
            self.assertEqual(result, "Статус книги изменен на 'выдана'.")

        with patch('builtins.input', return_value='выдана'):
            result = library.update_book_status(1)
            self.assertEqual(
                result,
                "Статус книги уже установлен на 'выдана'."
            )

        with patch('builtins.input', return_value='недоступна'):
            result = library.update_book_status(1)
            self.assertEqual(result, "Ошибка: введите корректный статус.")

        result = library.update_book_status(3)
        self.assertEqual(result, "Книга не найдена.")


if __name__ == "__main__":
    unittest.main()

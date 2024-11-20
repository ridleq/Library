# Класс книги и ее поля.
class Book:
    def __init__(self, book_id, title, author, year, status):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    # Метод преобразования объекта в словарь для сохранения в Json.
    def to_dict(self):
        return {
            'id': self.id,  # Уникальный id.
            'title': self.title,  # Название книги.
            'author': self.author,  # Автор киниги.
            'year': self.year,  # Год издания.
            'status': self.status  # Статус книги.
        }

# Класс книги и ее поля.
class Book:
    """
    Этот класс используется для создания объектов книги с
    уникальным идентификатором, заголовком, автором, годом издания и статусом.
    Он также предоставляет метод для преобразования объекта книги в словарь,
    что удобно для сохранения в формате JSON.
    """
    def __init__(
        self, book_id: int,
        title: str, author: str,
        year: int, status: str
    ):  # Инициализирует объект книги.
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    # Метод преобразования объекта в словарь для сохранения в Json.
    def to_dict(self) -> dict:
        return {
            'id': self.id,  # Уникальный id.
            'title': self.title,  # Название книги.
            'author': self.author,  # Автор киниги.
            'year': self.year,  # Год издания.
            'status': self.status  # Статус книги.
        }

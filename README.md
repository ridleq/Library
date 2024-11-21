# Система управления библиотекой

[Автор: Дмитрий](https://github.com/ridleq)

Система управления библиотекой - это небольшое консольное приложение, созданное для отслеживания книг в библиотеке.

## Функционал приложения:

- Пользователь может добавлять книгу 
- Пользователь может удалять книгу
- Пользователь может изменять статус книги (В налачии/Выдана)
- Поиск книг по 3 параметрам: по названию, автору или году издания
- Вывод всех книг с их ID, названием, автором, годом издания и статусом

### Как запустить приложение локально:

Клонировать репозиторий и перейти в него в командной строке:

```
1. git clone https://github.com/ridleq/Library.git
```

```
2. cd ~/library
```

```
3. Запустить приложение командой python main.py
```


## Перед запуском приложения необходимо произвести тестрирование.
## Запуск тестов:

```
1. Переходим в корневую попку проекта - cd ~/library
```

```
2. Запускаем тесты командой - python -m tests.all_tests
```

```
3. Смотрим результаты
```

## Технологический стек приложения:
[Python](https://www.python.org/)

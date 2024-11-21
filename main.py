from crud.library import Library


def main():
    library = Library()

    while True:
        print("\n1| Добавить книгу")
        print("2| Удалить книгу")
        print("3| Найти книгу")
        print("4| Изменить статус книги")
        print("5| Отобразить все книги")
        print("6| Выход")
        choice = input("\nВыберите действие: ")

        if choice == '1':
            title = input("\nВведите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            print(library.add_book(title, author, year))

        elif choice == '2':
            book_id = int(input("\nВведите ID книги: "))
            print(library.delete_book(book_id))

        elif choice == '3':
            book_search = input("\nВведите данные для поиска: ")
            found_book = library.search_book(book_search)
            for book in found_book:
                print(book)

        elif choice == '4':
            book_id = int(input("\nВведите ID книги: "))
            print(library.update_book_status(book_id))

        elif choice == '5':
            print(library.list_books())

        elif choice == '6':
            print("\nВы вышли из приложения.")
            break

        else:
            print('\nВыберите цифру из списка.')


if __name__ == "__main__":
    main()

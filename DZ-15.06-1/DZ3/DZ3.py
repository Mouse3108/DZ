# Задание 3.
# Создайте приложение для работы в библиотеке. Оно должно оперировать следующими сущностями:
# Книга, Библиотекарь, Читатель. Приложение должно позволять вводить, удалять, изменять, сохранять в файл,
# загружать из файла, логгировать действия, искать информацию
# (результаты поиска выводятся на экран или файл) о сущностях.
# При реализации используйте максимально возможное количество паттернов проектирования.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'"{self.title}", автор - {self.author}'


class Librarian:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Reader:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Result_on_screen:
    @staticmethod
    def search_results(result):
        print(result)


class Result_to_file:
    @staticmethod
    def search_results(result):
        with open('search.txt', 'w') as file:
            file.write(result)
        print('Вы можете посмотреть результаты поиска в файле search.txt')


class Strategy:
    def __init__(self):
        self.__strategy = None

    @property
    def strategy(self):
        return self.__strategy

    @strategy.setter
    def strategy(self, output):
        if output == 'экран':
            self.__strategy = Result_on_screen()
        else:
            self.__strategy = Result_to_file()

    def strategy_output(self):
        output = None
        while output not in ['экран', 'файл']:
            output = input('Куда вывести информацию (экран/файл): ')
            if output in ['экран', 'файл']:
                self.strategy = output
                break
            else:
                print('Такого варианта нет!')


class Logger:
    @staticmethod
    def log(message):
        with open('log.txt', 'a') as log_file:
            log_file.write(f'{message}\n')

class Actions_with_books:
    def __init__(self):
        self.books = []

    def books_info(self):
        return (f'Просмотр списка книг:\n' +
                '\n'.join([f'{n}. "{book.title}", автор - {book.author}' for n, book in enumerate(self.books, 1)]))

    def add_book(self):
        result = 'Добавление книги в список:\n'
        title = input('Введите название книги: ')
        author = input('Введите автора книги: ')
        for book in self.books:
            if title == book.title and author == book.author:
                print(f'Книга "{title}" автора {author} уже есть в списке!')
                result += f'Книга "{title}" автора {author} уже есть в списке!'
                return result
        self.books.append(Book(title, author))
        print(f'Добавлена книга "{title}", автор - {author}')
        result += f'Добавлена книга "{title}", автор - {author}'
        return result

    def remove_book(self):
        remove_list = 'Удаление книг из списка:\n'
        while True:
            command = input('Что необходимо удалить: книга/автор: ')
            if command == 'книга':
                title = input('Введите название книги: ')
                add_book = False
                for book in self.books:
                    if book.title == title:
                        if input(f'Удалить книгу "{book.title}" - {book.author} (да/нет): ') == 'да':
                            remove_list += f'"{book.title}" - {book.author}\n'
                            print(f'Удалена книга "{book.title}" - {book.author}')
                            self.books.remove(book)
                            add_book = True
                if not add_book:
                    print(f'Необходимая книга "{title}" не найдена в списке!')
                    remove_list += f'Необходимая книга "{title}" не найдена в списке!'
                break
            elif command == 'автор':
                author = input('Введите автора: ')
                add_book = False
                for book in self.books:
                    if book.author == author:
                        if input(f'Найдена книга: "{book.title}" - {book.author}. Удалить (да\нет)? ') == 'да':
                            print(f'Удалена книга "{book.title}" - {book.author}')
                            remove_list += f'"{book.title}" - {book.author}\n'
                            self.books.remove(book)
                            add_book = True
                if not add_book:
                    print(f'Необходимый автор {author} не найден в списке!')
                    remove_list += f'Необходимый автор {author} не найден в списке!'
                break
            else:
                print('Такого варианта нет!')
                continue
        return remove_list

    def replace_book(self):
        new_book = 'Изменение информации о книгах:\n'
        while True:
            command = input('Что необходимо изменить: книга/автор: ')
            if command == 'книга':
                title = input('Введите название книги: ')
                found = False
                for book in self.books:
                    if book.title == title:
                        if input(f'Найдена книга: "{book.title}" - {book.author}. Изменить (да\нет)? ') == 'да':
                            new_title = input('Введите новое название книги: ')
                            print(f'Книга "{book.title}" автора {book.author} изменена на "{new_title}"')
                            new_book += f'Книга "{book.title}" автора {book.author} изменена на "{new_title}"\n'
                            book.title = new_title
                            found = True
                if not found:
                    print(f'Необходимая книга "{title}" не найдена в списке!')
                    new_book += f'Необходимая книга "{title}" не найдена в списке!'
                break
            elif command == 'автор':
                author = input('Введите автора: ')
                found = False
                for book in self.books:
                    if book.author == author:
                        if input(f'Найдена книга: "{book.title}" - {book.author}. Изменить (да\нет)? ') == 'да':
                            new_author = input('Введите новое имя автора: ')
                            print(f'У книги "{book.title}" автор {book.author} изменен на {new_author}')
                            new_book += f'У книги "{book.title}" автор {book.author} изменен на {new_author}\n'
                            book.author = new_author
                            found = True
                if not found:
                    print(f'Необходимый автор {author} не найден в списке!')
                    new_book += f'Необходимый автор {author} не найден в списке!'
                break
            else:
                print('Такого варианта нет!')
                continue
        return new_book

    def search_book(self):
        result = 'Результаты поиска книги:\n'
        while True:
            command = input('Что необходимо найти: книга/автор: ')
            if command == 'книга':
                title = input('Введите название книги: ')
                found = False
                for book in self.books:
                    if book.title == title:
                        result += f'"{book.title}" - {book.author}\n'
                        found = True
                if not found:
                    result += f'Книга {title} не найдена в списке!'
                break
            elif command == 'автор':
                author = input('Введите автора: ')
                found = False
                for book in self.books:
                    if book.author == author:
                        result += f'"{book.title}" - {book.author}\n'
                        found = True
                if not found:
                    result += f'Автор {author} не найден в списке!'
                break
            else:
                print('Такого варианта нет!')
                continue
        return result

    def save_books_to_file(self):
        with open('books.txt', 'w', encoding='utf-16') as file:
            for book in self.books:
                file.write(f'{book.title}, {book.author}\n')
        return 'Обновлена информация в файле books.txt'

    def load_books_from_file(self):
        with open('books.txt', 'r', encoding='utf-16') as file:
            for book in file:
                if book.split():
                    title, author = book.strip().split(', ')
                    if not any(b.title == title and b.author == author for b in self.books):
                        self.books.append(Book(title, author))
        return 'Получена информация из файла books.txt'


class Actions_with_librarians:
    def __init__(self):
        self.librarians = []

    def librarians_info(self):
        return ('Просмотр списка библиотекарей:\n' +
                '\n'.join([f'{n}. {name}' for n, name in enumerate(self.librarians, 1)]))

    def check_user_in_librarians(self, user_name):
        for librarian in self.librarians:
            if librarian.name == user_name:
                return True
        return False

    def add_librarian(self):
        result = 'Добавление библиотекаря в список:\n'
        name = input('Введите данные библиотекаря: ')
        if any(librarian.name == name for librarian in self.librarians):
            print(f'Библиотекарь {name} уже есть в списке!')
            result += f'Библиотекарь {name} уже есть в списке!'
            return result
        self.librarians.append(Librarian(name))
        print(f'В список добавлен библиотекарь {name}')
        result += f'В список добавлен библиотекарь {name}'
        return result

    def remove_librarian(self):
        result = 'Удаление библиотекаря из списка:\n'
        name = input('Введите данные библиотекаря: ')
        if all(librarian.name != name for librarian in self.librarians):
            print(f'Библиотекарь {name} не найден в списке!')
            result += f'Библиотекарь {name} не найден в списке!'
            return result
        for librarian in self.librarians:
            if librarian.name == name:
                self.librarians.remove(librarian)
                print(f'Библиотекарь {name} удален из списка')
                result += f'Библиотекарь {name} удален из списка'
                return result

    def replace_librarian(self):
        result = 'Изменение данных о библиотекаре:\n'
        name = input('Введите данные библиотекаря: ')
        if all(librarian.name != name for librarian in self.librarians):
            print(f'Библиотекарь {name} не найден в списке!\n')
            result += f'Библиотекарь {name} не найден в списке!'
            return result
        for librarian in self.librarians:
            if librarian.name == name:
                new_name = input('Введите новые данные библиотекаря: ')
                librarian.name = new_name
                print(f'Библиотекарь {name} теперь {new_name}\n')
                result += f'Библиотекарь {name} теперь {new_name}'
                return result

    def search_librarian(self):
        result = 'Результаты поиска библиотекаря:\n'
        name = input('Введите имя библиотекаря для поиска в списке: ')
        if all(librarian.name != name for librarian in self.librarians):
            result += f'Библиотекарь {name} отсутствует в списке!'
        else:
            result += f'Библиотекарь {name} найден в списке!'
        return result

    def save_librarians_to_file(self):
        with open('librarian.txt', 'w') as file:
            for librarian in self.librarians:
                file.write(f'{librarian}\n')
        return f'Обновлена информация в файле librarian.txt'

    def load_librarians_from_file(self):
        with open('librarian.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line and not any(librarian.name == line for librarian in self.librarians):
                    self.librarians.append(Librarian(line))
        return f'Получена информация из файла librarian.txt'


class Actions_with_readers:
    def __init__(self):
        self.readers = []

    def readers_info(self):
        return f'Просмотр списка читателей:\n' + '\n'.join([f'{n}. {name}' for n, name in enumerate(self.readers, 1)])

    def check_user_in_readers(self, user_name):
        for reader in self.readers:
            if reader.name == user_name:
                return True
        return False

    def add_reader(self):
        result = 'Добавление читателя в список:\n'
        name = input('Введите данные читателя: ')
        if any(reader.name == name for reader in self.readers):
            print(f'Читатель {name} уже есть в списке!')
            result += f'Читатель {name} уже есть в списке!'
            return result
        self.readers.append(Reader(name))
        print(f'Читатель {name} добавлен в список')
        result += f'Читатель {name} добавлен в список'
        return result

    def remove_reader(self):
        result = 'Удаление читателя из списка:\n'
        name = input('Введите данные читателя: ')
        if all(reader.name != name for reader in self.readers):
            print(f'Читатель {name} не найден в списке!')
            result += f'Читатель {name} не найден в списке!'
            return result
        for reader in self.readers:
            if reader.name == name:
                self.readers.remove(reader)
                print(f'Читатель {name} удален из списка')
                result += f'Читатель {name} удален из списка'
                return result

    def replace_reader(self):
        result = 'Изменение данных о читателе:\n'
        name = input('Введите данные читателя: ')
        if all(reader.name != name for reader in self.readers):
            print(f'Читатель {name} не найден в списке!')
            result += f'Читатель {name} не найден в списке!'
            return result
        for reader in self.readers:
            if reader.name == name:
                new_name = input('Введите новые данные читателя: ')
                reader.name = new_name
                print(f'Читатель {name} теперь {new_name}')
                result += f'Читатель {name} теперь {new_name}'
                return result

    def search_reader(self):
        result = 'Результаты поиска читателя:\n'
        name = input('Введите данные читателя: ')
        if all(reader.name != name for reader in self.readers):
            result += f'Читатель {name} отсутствует в списке!'
        else:
            result += f'Читатель {name} найден в списке!'
        return result

    def save_readers_to_file(self):
        with open('readers.txt', 'w') as file:
            for reader in self.readers:
                file.write(f'{reader}\n')
        return f'Обновлена информация в файле readers.txt'

    def load_readers_from_file(self):
        with open('readers.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line and not any(reader.name == line for reader in self.readers):
                    self.readers.append(Reader(line))
        return f'Получена информация из файла readers.txt'


class Menu_Proxy:
    def __init__(self, user):
        self.user = user

    def show_menu(self):
        if isinstance(self.user, Librarian):
            self.librarian_menu()
        elif isinstance(self.user, Reader):
            self.reader_menu()
        else:
            self.visitor_menu()

    def librarian_menu(self):
        library.log(f'В библиотеке начал работу библиотекарь {user_name}')
        print('Вы вошли как библиотекарь! Можете приступать к работе')
        while True:
            print('\t1. Работа с книгами\n'
                  '\t2. Работа со списком читателей\n'
                  '\t3. Работа со списком библиотекарей\n'
                  '\t4. Покинуть библиотеку')
            choice = input('Ваш выбор (1 / 2 / 3 / 4): ')
            if choice == '4':
                library.log(f'{user_name} закончил работу в библиотеке!\n')
                print('Пока!')
                break
            elif choice == '1':
                while True:
                    print('\t\t1. Посмотреть список книг\n'
                          '\t\t2. Добавить книгу\n'
                          '\t\t3. Удалить книгу\n'
                          '\t\t4. Изменить информацию о книге\n'
                          '\t\t5. Найти книгу\n'
                          '\t\t6. Сохранить информацию о книгах в файл\n'
                          '\t\t7. Получить информацию из файла\n'
                          '\t\t8. Закончить работу с книгами')
                    choice_book = input('Ваш выбор (1 / 2 / 3 / 4 / 5 / 6 / 7 / 8): ')
                    if choice_book == '8':
                        break
                    elif choice_book == '1':
                        library.strategy_output(library.get_books_info())
                        library.log('Просмотр списка книг')
                    elif choice_book == '2':
                        library.log(library.add_book())
                    elif choice_book == '3':
                        library.log(library.remove_book())
                    elif choice_book == '4':
                        library.log(library.replace_book())
                    elif choice_book == '5':
                        result = library.search_book()
                        library.strategy_output(result)
                        library.log(result)
                    elif choice_book == '6':
                        library.log(library.save_books_to_file())
                    elif choice_book == '7':
                        library.log(library.load_books_from_file())
                    else:
                        print('Такого варианта нет! Выберите ещё раз!')
            elif choice == '2':
                while True:
                    print('\t\t1. Посмотреть список читателей\n'
                          '\t\t2. Добавить читателя\n'
                          '\t\t3. Удалить читателя\n'
                          '\t\t4. Изменить информацию о читателе\n'
                          '\t\t5. Найти читателя\n'
                          '\t\t6. Сохранить информацию о читателях в файл\n'
                          '\t\t7. Получить информацию из файла\n'
                          '\t\t8. Закончить работу со списком читателей')
                    choice_book = input('Ваш выбор (1 / 2 / 3 / 4 / 5 / 6 / 7 / 8): ')
                    if choice_book == '8':
                        break
                    elif choice_book == '1':
                        result = library.get_readers_info()
                        library.strategy_output(result)
                        library.log('Просмотр списка читателей')
                    elif choice_book == '2':
                        library.log(library.add_reader())
                    elif choice_book == '3':
                        library.log(library.remove_reader())
                    elif choice_book == '4':
                        library.log(library.replace_reader())
                    elif choice_book == '5':
                        result = library.search_reader()
                        library.strategy_output(result)
                        library.log(result)
                    elif choice_book == '6':
                        library.log(library.save_readers_to_file())
                    elif choice_book == '7':
                        library.log(library.load_readers_from_file())
                    else:
                        print('Такого варианта нет! Выберите ещё раз!')
            elif choice == '3':
                while True:
                    print('\t\t1. Посмотреть список библиотекарей\n'
                          '\t\t2. Добавить библиотекаря\n'
                          '\t\t3. Удалить библиотекаря\n'
                          '\t\t4. Изменить информацию о библиотекаре\n'
                          '\t\t5. Найти библиотекаря\n'
                          '\t\t6. Сохранить информацию о библиотекарях в файл\n'
                          '\t\t7. Получить информацию из файла\n'
                          '\t\t8. Закончить работу со списком библиотекарей')
                    choice_book = input('Ваш выбор (1 / 2 / 3 / 4 / 5 / 6 / 7 / 8): ')
                    if choice_book == '8':
                        break
                    elif choice_book == '1':
                        result = library.get_librarians_info()
                        library.strategy_output(result)
                        library.log('Просмотр списка библиотекарей')
                    elif choice_book == '2':
                        library.log(library.add_librarian())
                    elif choice_book == '3':
                        library.log(library.remove_librarian())
                    elif choice_book == '4':
                        library.log(library.replace_librarian())
                    elif choice_book == '5':
                        result = library.search_librarian()
                        library.strategy_output(result)
                        library.log(result)
                    elif choice_book == '6':
                        library.log(library.save_librarians_to_file())
                    elif choice_book == '7':
                        library.log(library.load_librarians_from_file())
                    else:
                        print('Такого варианта нет! Выберите ещё раз!')
            else:
                print('Такого варианта нет! Выберите ещё раз!')

    def reader_menu(self):
        library.log(f'В библиотеке начал работу читатель {user_name}')
        print('Вы вошли как читатель! Можете приступать к работе')
        while True:
            print('\t1. Работа с книгами\n'
                  '\t2. Работа со списком читателей\n'
                  '\t3. Покинуть библиотеку')
            choice = input('Ваш выбор (1 / 2 / 3): ')
            if choice == '3':
                library.log(f'{user_name} закончил работу в библиотеке!\n')
                print('Пока!')
                break
            elif choice == '1':
                while True:
                    print('\t\t1. Посмотреть список книг\n'
                          '\t\t2. Найти книгу\n'
                          '\t\t3. Закончить работу с книгами')
                    choice_book = input('Ваш выбор (1 / 2 / 3): ')
                    if choice_book == '3':
                        break
                    elif choice_book == '1':
                        library.strategy_output(library.get_books_info())
                        library.log('Просмотр списка книг')
                    elif choice_book == '2':
                        result = library.search_book()
                        library.strategy_output(result)
                        library.log(result)
                    else:
                        print('Такого варианта нет! Выберите ещё раз!')
            elif choice == '2':
                while True:
                    print('\t\t1. Посмотреть список читателей\n'
                          '\t\t2. Найти читателя\n'
                          '\t\t3. Закончить работу со списком читателей')
                    choice_book = input('Ваш выбор (1 / 2 / 3): ')
                    if choice_book == '3':
                        break
                    elif choice_book == '1':
                        result = library.get_readers_info()
                        library.strategy_output(result)
                        library.log('Просмотр списка читателей')
                    elif choice_book == '2':
                        result = library.search_reader()
                        library.strategy_output(result)
                        library.log(result)
                    else:
                        print('Такого варианта нет! Выберите ещё раз!')
            else:
                print('Такого варианта нет! Выберите ещё раз!')

    def visitor_menu(self):
        library.log(f'В библиотеке начал работу незарегистрированный посетитель {user_name}')
        print('Вы вошли как незарегистрированный посетитель! Можете приступать к работе')
        while True:
            print('\t1. Работа с книгами\n'
                  '\t2. Покинуть библиотеку')
            choice = input('Ваш выбор (1 / 2): ')
            if choice == '2':
                library.log(f'{user_name} закончил работу в библиотеке!\n')
                print('Пока!')
                break
            elif choice == '1':
                while True:
                    print('\t\t1. Посмотреть список книг\n'
                          '\t\t2. Найти книгу\n'
                          '\t\t3. Закончить работу с книгами')
                    choice_book = input('Ваш выбор (1 / 2 / 3): ')
                    if choice_book == '3':
                        break
                    elif choice_book == '1':
                        library.strategy_output(library.get_books_info())
                        library.log('Просмотр списка книг')
                    elif choice_book == '2':
                        result = library.search_book()
                        library.strategy_output(result)
                        library.log(result)
                    else:
                        print('Такого варианта нет! Выберите ещё раз!')
            else:
                print('Такого варианта нет! Выберите ещё раз!')


class Library_Facade:
    def __init__(self):
        self.actions_with_books = Actions_with_books()
        self.actions_with_librarians = Actions_with_librarians()
        self.actions_with_readers = Actions_with_readers()
        self.strategy = Strategy()

    def strategy_output(self, result):
        self.strategy.strategy_output()
        if self.strategy.strategy:
            return self.strategy.strategy.search_results(result)

    def log(self, message):
        Logger.log(message)

    def show_menu(self, user):
        menu_proxy = Menu_Proxy(user)
        menu_proxy.show_menu()

    def get_books_info(self):
        return self.actions_with_books.books_info()

    def add_book(self):
        return self.actions_with_books.add_book()

    def remove_book(self):
        return self.actions_with_books.remove_book()

    def replace_book(self):
        return self.actions_with_books.replace_book()

    def search_book(self):
        return self.actions_with_books.search_book()

    def save_books_to_file(self):
        return self.actions_with_books.save_books_to_file()

    def load_books_from_file(self):
        return self.actions_with_books.load_books_from_file()

    def get_librarians_info(self):
        return self.actions_with_librarians.librarians_info()

    def check_user_in_librarians(self):
        return self.actions_with_librarians.check_user_in_librarians(user_name)

    def add_librarian(self):
        return self.actions_with_librarians.add_librarian()

    def remove_librarian(self):
        return self.actions_with_librarians.remove_librarian()

    def replace_librarian(self):
        return self.actions_with_librarians.replace_librarian()

    def search_librarian(self):
        return self.actions_with_librarians.search_librarian()

    def save_librarians_to_file(self):
        return self.actions_with_librarians.save_librarians_to_file()

    def load_librarians_from_file(self):
        return self.actions_with_librarians.load_librarians_from_file()

    def get_readers_info(self):
        return self.actions_with_readers.readers_info()

    def check_user_in_readers(self):
        return self.actions_with_readers.check_user_in_readers(user_name)

    def add_reader(self):
        return self.actions_with_readers.add_reader()

    def remove_reader(self):
        return self.actions_with_readers.remove_reader()

    def replace_reader(self):
        return self.actions_with_readers.replace_reader()

    def search_reader(self):
        return self.actions_with_readers.search_reader()

    def save_readers_to_file(self):
        return self.actions_with_readers.save_readers_to_file()

    def load_readers_from_file(self):
        return self.actions_with_readers.load_readers_from_file()


print('Добро пожаловать в библиотеку!')
user_name = input('Введите своё имя: ')
user = None
library = Library_Facade()
library.log(library.load_books_from_file())
library.log(library.load_librarians_from_file())
library.log(library.load_readers_from_file())
if library.check_user_in_librarians():
    user = Librarian(user_name)
elif library.check_user_in_readers():
    user = Reader(user_name)
Menu_Proxy(user).show_menu()
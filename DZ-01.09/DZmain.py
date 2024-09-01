from DZклиенты import *
from DZпродукты import *
from DZзаказы import *
import re


if __name__ == '__main__':
    while True:
        print('''
\033[32mДобро пожаловать в "Онлайн-магазин"!\033[0m
    МЕНЮ:
1. Войти (для зарегистрированных пользователей)
2. Зарегистрироваться
3. Покинуть магазин
''')
        command = input('Выбор сделайте цифрой: ')
        if command == '3':
            print('\033[34mДо новых встреч!\033[0m')
            break
        elif command == '2':
            name = input('Введите своё имя: ')
            while True:
                password = input('Введите пароль (не менее пяти символов): ')
                if len(password) < 5:
                    print('\033[31mПароль слишком короткий! Попробуйте ещё раз!\033[0m')
                    continue
                else:
                    break
            address = input('Введите свой адрес: ')
            while True:
                phone_number = input('Введите свой номер телефона в формате +0(000)000-0000: ')
                if not re.match(r'\+\d\(\d{3}\)\d{3}-\d{4}', phone_number):
                    print('\033[31mНеверный формат номера телефона! Попробуйте ещё раз!\033[0m')
                    continue
                break
            try:
                add_client(name, password, address, phone_number)
                print(f'{name}, Вы успешно зарегистрировались!')
                continue
            except sqlite3.IntegrityError:
                print('\033[31mВы не были зарегистрированы, так как такой номер телефона уже используется!\033[0m')
                continue
        elif command == '1':
            while True:
                name = input('Введите своё имя: ')
                password = input('Введите пароль: ')
                client = search_client(name, password)
                if client:
                    client = client[0]
                    break
                else:
                    print('\033[31mНеверное имя или пароль! Попробуйте ещё раз!\033[0m')
                    continue
            while True:
                print('''
1. Просмотреть каталог товаров
2. Изменить свои свои данные
3. Удалить свою учетную запись
4. Выйти в главное меню
''')
                search = input('Выбор сделайте цифрой: ')
                if search == '4':
                    break
                elif search == '2':
                    name = input('Введите новое имя клиента (или оставьте пустую строку): ')
                    while True:
                        password = input('Введите новый пароль (не менее пяти символов) '
                                         '(или оставьте пустую строку): ')
                        if len(password) < 5:
                            print('\033[31mПароль слишком короткий! Попробуйте ещё раз!\033[0m')
                            continue
                        else:
                            break
                    address = input('Введите новый адрес (или оставьте пустую строку): ')
                    while True:
                        phone_number = input('Введите новый номер телефона в формате +0(000)000-0000 '
                                             '(или оставьте пустую строку): ')
                        if phone_number != '' and not re.match(r'\+\d\(\d{3}\)\d{3}-\d{4}', phone_number):
                            print('\033[31mНеверный формат номера телефона! Попробуйте ещё раз!\033[0m')
                            continue
                        break
                    try:
                        update_client(client, name, password, address, phone_number)
                        print('Данные клиента успешно изменены')
                    except sqlite3.IntegrityError:
                        print('\033[31mТакой номер телефона уже используется! Данные клиента не были изменены!\033[0m')
                elif search == '3':
                    del_client(client)
                    print('Клиент успешно удален!')
                elif search == '1':
                    basket = {'product_number': [],
                              'product_name': [],
                              'product_quantity': [],
                              'product_price': [],
                              }
                    while True:
                        rows = show_product()
                        if len(rows) == 0:
                            print('\033[31mК сожалению, в настоящее время на складе нет товаров!\033[0m')
                            continue
                        else:
                            print('\nСписок товаров (номер / название / цена / количество):')
                            for row in rows:
                                print(*row)
                            product = input('Введите номер товара для добавления в корзину: ')
                            try:
                                product = int(product)
                            except ValueError:
                                print(f'\033[31m{product} - это не номер!\033[0m')
                                continue
                            if search_product(product) is None:
                                print('\033[31mТовара с таким номером нет в списке!\033[0m')
                                continue
                            quantity_of_products = quantity_product(product)
                            quantity = input(
                                f'Введите количество товара для добавления в корзину цифрой '
                                f'от 1 до {int(*quantity_of_products)}: ')
                            try:
                                quantity = int(quantity)
                            except ValueError:
                                print(f'\033[31m{quantity} - это не цифра! Товар не добавлен!\033[0m')
                                continue
                            if quantity > int(*quantity_of_products):
                                print('\033[31mСлишком большое количество товара! Товар не добавлен!\033[0m')
                                continue
                            number_of_product = search_product(product)[0]
                            name_of_product = search_product(product)[1]
                            basket['product_number'].append(int(number_of_product))
                            basket['product_name'].append(str(name_of_product))
                            basket['product_quantity'].append(quantity)
                            price_of_product = price_product(product)
                            basket['product_price'].append(quantity * float(*price_of_product))
                            update_product(product, int(*quantity_of_products) - quantity)
                            while True:
                                print('''
1. Продолжить выбор товаров
2. Просмотреть товары в корзине
3. Оформить заказ
                                ''')
                                new_search = input('Выбор сделайте цифрой: ')
                                if new_search == '1':
                                    break
                                elif new_search == '2':
                                    for i in range(len(basket['product_name'])):
                                        product_name = basket['product_name'][i]
                                        product_quantity = basket['product_quantity'][i]
                                        product_price = basket['product_price'][i]
                                        print(f'{i + 1}. {product_name} '
                                              f'в количестве {product_quantity} шт., '
                                              f'стоимостью {product_price}.')
                                    continue
                                elif new_search == '3':
                                    number_order = search_order()
                                    try:
                                        number_order = int(*number_order) + 1
                                    except TypeError:
                                        number_order = 1
                                    for i in range(len(basket['product_name'])):
                                        product_number = basket['product_number'][i]
                                        product_price = basket['product_price'][i]
                                        add_order(number_order, client, product_number, product_price)
                                    print(f'Ваш заказ успешно оформлен под номером {number_order}!')
                                    break
                                else:
                                    print('\033[31mТакого варианта нет!\033[0m')
                                    continue
                        if new_search == '3':
                            break
                        else:
                            continue
                else:
                    print('\033[31mТакого варианта нет!\033[0m')
                    continue
        else:
            print('\033[31mТакого варианта нет!\033[0m')
            continue

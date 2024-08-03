from DZклиенты import *
from DZпродукты import *
from DZзаказы import *
import re

if __name__ == '__main__':
    while True:
        print('''
    \033[32mКЛИЕНТЫ:\033[0m
1. Добавить клиента\t\t2. Просмотреть клиентов\t\t3. Изменить данные клиента\t\t4. Удалить клиента
    \033[32mПРОДУКТЫ:\033[0m
5. Добавить продукт\t\t6. Просмотреть продукты\t\t7. Изменить данные продукта\t\t8. Удалить продукт
    \033[32mЗАКАЗЫ:\033[0m
9. Добавить заказ\t\t10. Просмотреть заказы\t\t11. Изменить данные заказа\t\t12. Удалить заказ
0. выйти из программы
''')
        command = input('Выбор сделайте цифрой: ')
        if command == '0':
            print('\033[34mДо новых встреч!\033[0m')
            break
        elif command == '1':
            first_name = input('Введите имя клиента: ')
            last_name = input('Введите фамилию клиента: ')
            address = input('Введите адрес клиента: ')
            phone_number = input('Введите номер телефона клиента в формате +0(000)000-0000: ')
            if not re.match(r'\+\d\(\d{3}\)\d{3}-\d{4}', phone_number):
                print('\033[31mНеверный формат номера телефона! Клиент не был добавлен!\033[0m')
                continue
            try:
                add_client(first_name, last_name, address, phone_number)
                print(f'В таблицу "Клиенты" добавлена запись: {first_name} {last_name}, {address}, {phone_number}')
            except sqlite3.IntegrityError:
                print('\033[31mТакой номер телефона уже используется! Клиент не был добавлен!\033[0m')
                continue
        elif command == '2':
            first_name, last_name, address, phone_number = '', '', '', ''
            print('''
Как искать клиента:
1. По имени
2. По фамилии
3. По адресу
4. По телефону
5. Вывести список всех клиентов
''')
            search = input('Выбор сделайте цифрой: ')
            try:
                search = int(search)
                if search < 1 or search > 5:
                    print('\033[31mТакого варианта нет!\033[0m')
                    continue
                elif search == 1:
                    first_name = input('Введите имя клиента: ')
                elif search == 2:
                    last_name = input('Введите фамилию клиента: ')
                elif search == 3:
                    address = input('Введите адрес клиента: ')
                elif search == 4:
                    phone_number = input('Введите номер телефона клиента в формате +0(000)000-0000: ')
                show_client(first_name, last_name, address, phone_number)
            except ValueError:
                print(f'\033[31m{search} - это не номер!\033[0m')
        elif command == '3':
            number = input('Введите номер клиента, данные которого необходимо изменить: ')
            try:
                number = int(number)
            except ValueError:
                print(f'\033[31m{number} - это не номер!\033[0m')
                continue
            if search_client(number) is None:
                print('\033[31mКлиента с таким номером нет в списке!\033[0m')
                continue
            first_name = input('Введите новое имя клиента (или оставьте пустую строку): ')
            last_name = input('Введите новую фамилию (или оставьте пустую строку): ')
            address = input('Введите новый адрес (или оставьте пустую строку): ')
            phone_number = input('Введите новый телефон (или оставьте пустую строку): ')
            try:
                update_client(number, first_name, last_name, address, phone_number)
                print(f'Данные клиента под номером {number} успешно изменены')
            except sqlite3.IntegrityError:
                print('\033[31mТакой номер телефона уже используется! Данные клиента не были изменены!\033[0m')
        elif command == '4':
            number = input('Введите номер клиента, которого необходимо удалить: ')
            try:
                number = int(number)
            except ValueError:
                print(f'\033[31m{number} - это не номер!\033[0m')
                continue
            if search_client(number) is None:
                print('\033[31mКлиента с таким номером нет в списке!\033[0m')
                continue
            del_client(number)
            print(f'Клиент под номером {number} успешно удален из таблицы "Клиенты"')
        elif command == '5':
            name = input('Введите название продукта: ')
            price = input('Введите цену продукта: ')
            quantity = input('Введите количество продукта (цифрой): ')
            try:
                quantity = int(quantity)
            except ValueError:
                print(f'\033[31mВариант {quantity} не подходит! Продукт не был добавлен!\033[0m')
                continue
            add_product(name, price, quantity)
            print(f'В таблицу "Продукты" добавлена запись: {name}, цена: {price}, количество: {quantity}')
        elif command == '6':
            name, price, quantity = '', '', ''
            print('''
Как искать продукт:
1. По названию
2. По цене
3. По количеству
4. Вывести список всех продуктов
''')
            search = input('Выбор сделайте цифрой: ')
            try:
                search = int(search)
                if search < 1 or search > 4:
                    print('\033[31mТакого варианта нет!\033[0m')
                    continue
                elif search == 1:
                    name = input('Введите название продукта: ')
                elif search == 2:
                    price = input('Введите цену продукта: ')
                elif search == 3:
                    quantity = input('Введите количество продукта (цифрой): ')
                    try:
                        quantity = int(quantity)
                    except ValueError:
                        print(f'\033[31mВариант {quantity} не подходит! Поиск по количеству не проведен!\033[0m')
                        quantity = ''
                show_product(name, price, quantity)
            except ValueError:
                print(f'\033[31m{search} - это не номер!\033[0m')
        elif command == '7':
            number = input('Введите номер продукта, данные которого необходимо изменить: ')
            try:
                number = int(number)
            except ValueError:
                print(f'\033[31m{number} - это не номер!\033[0m')
                continue
            if search_product(number) is None:
                print('\033[31mПродукта с таким номером нет в списке!\033[0m')
                continue
            name = input('Введите новое название продукта (или оставьте пустую строку): ')
            price = input('Введите новую цену продукта (или оставьте пустую строку): ')
            quantity = input('Введите новое количество продукта цифрой (или оставьте пустую строку): ')
            if quantity != '':
                try:
                    quantity = int(quantity)
                except ValueError:
                    print(f'\033[31m{quantity} - это не цифра! Данные о продукте не изменены!\033[0m')
                    continue
            update_product(number, name, price, quantity)
            print(f'Данные продукта под номером {number} успешно изменены')
        elif command == '8':
            number = input('Введите номер продукта, который необходимо удалить: ')
            try:
                number = int(number)
            except ValueError:
                print(f'\033[31m{number} - это не номер!\033[0m')
                continue
            if search_product(number) is None:
                print('\033[31mПродукта с таким номером нет в списке!\033[0m')
                continue
            del_product(number)
            print(f'Продукт под номером {number} успешно удален из таблицы "Продукты"')
        elif command == '9':
            client = input('Введите номер клиента, который будет оформлять заказ: ')
            try:
                client = int(client)
            except ValueError:
                print(f'\033[31m{client} - это не номер!\033[0m')
                continue
            if search_client(client) is None:
                print('\033[31mКлиента с таким номером нет в списке!\033[0m')
                continue
            product = input('Введите номер продукта для добавления в заказ: ')
            try:
                product = int(product)
            except ValueError:
                print(f'\033[31m{product} - это не номер!\033[0m')
                continue
            if search_product(product) is None:
                print('\033[31mПродукта с таким номером нет в списке!\033[0m')
                continue
            quantity_of_products = quantity_product(product)
            quantity = input(f'Введите количество продукта в заказе цифрой от 1 до {int(*quantity_of_products)}: ')
            try:
                quantity = int(quantity)
            except ValueError:
                print(f'\033[31m{quantity} - это не цифра! Заказ не добавлен!\033[0m')
                continue
            if quantity > int(*quantity_of_products):
                print('\033[31mСлишком большое количество продукта для заказа! Заказ не добавлен!\033[0m')
                continue
            add_order(client, product, quantity)
            update_product(product, '', '', int(*quantity_of_products) - quantity)
            print('В таблицу "Заказы" добавлен новый заказ')
        elif command == '10':
            client, product, cost = '', '', ''
            print('''
Как искать заказ:
1. По номеру клиента
2. По номеру продукта
3. По стоимости заказа
4. Вывести список всех заказов
''')
            search = input('Выбор сделайте цифрой: ')
            try:
                search = int(search)
                if search < 1 or search > 4:
                    print('\033[31mТакого варианта нет!\033[0m')
                    continue
                elif search == 1:
                    client = input('Введите номер клиента, который делал заказ (цифрой): ')
                    try:
                        client = int(client)
                    except ValueError:
                        print(f'\033[31m{client} - это не цифра! Поиск не выполнен!\033[0m')
                        continue
                elif search == 2:
                    product = input('Введите номер продукта, добавленного в заказ (цифрой): ')
                    try:
                        product = int(product)
                    except ValueError:
                        print(f'\033[31m{product} - это не цифра! Поиск не выполнен!\033[0m')
                        continue
                elif search == 3:
                    cost = input('Введите стоимость заказа: ')
                show_order(client, product, cost)
            except ValueError:
                print(f'\033[31m{search} - это не номер!\033[0m')
        elif command == '11':
            number = input('Введите номер заказа, информацию о котором необходимо изменить: ')
            try:
                number = int(number)
            except ValueError:
                print(f'\033[31m{number} - это не номер!\033[0m')
                continue
            if search_order(number) is None:
                print('\033[31mЗаказ с таким номером отсутствует в списке!\033[0m')
                continue
            client = input('Введите цифрой новый номер клиента (или оставьте пустую строку): ')
            if client != '':
                try:
                    client = int(client)
                except ValueError:
                    print(f'\033[31m{client} - это не цифра!\033[0m')
                    continue
            product = input('Введите цифрой новый номер продукта (или оставьте пустую строку): ')
            if product != '':
                try:
                    product = int(product)
                except ValueError:
                    print(f'\033[31m{product} - это не цифра!\033[0m')
                    continue
            cost = input('Введите новую стоимость продукта (или оставьте пустую строку): ')
            update_order(number, client, product, cost)
            print(f'Данные заказа под номером {number} успешно изменены')
        elif command == '12':
            number = input('Введите номер заказа, который необходимо удалить: ')
            try:
                number = int(number)
            except ValueError:
                print(f'\033[31m{number} - это не номер!\033[0m')
                continue
            if search_order(number) is None:
                print('\033[31mЗаказ с таким номером отсутствует в списке!\033[0m')
                continue
            del_order(number)
            print(f'Заказ под номером {number} успешно удален из таблицы "Заказы"')
        else:
            print('\033[31mТакого варианта нет!\033[0m')

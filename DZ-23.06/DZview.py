def add_title(title):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(title.center(40, '_'))
            result = func(*args, **kwargs)
            print('\033[90m~\033[0m' * 40)
            return result
        return wrapper
    return decorator


class View:
    @add_title('Запрошенная информация:')
    def show_info(self, info):
        print(info)

    @add_title('Ваш выбор:')
    def choice(self):
        return input('Ваш выбор (цифрой) или пустая строка для выхода: ')

    @add_title('Выберите продукт')
    def add_topping_and_souse(self):
        return input('Ваш выбор (цифрой): ')

    @add_title('Редактирование заказа:')
    def choice_delete(self):
        return input('Выберите, какой хот-дог удалить (цифрой) или пустая строка для выхода: ')

    @add_title('Ошибка ввода')
    def print_error(self, text_error):
        print(f'Вариант \033[91m{text_error}\033[0m не подходит!')

    @add_title('Ошибка ввода')
    def error_topping_and_souse(self, text_error):
        print(f'Вы уже добавили \033[91m{text_error}\033[0m! Можно добавить только одну порцию продукта!')

    @add_title('Главное меню')
    def main_menu(self):
        print('\033[92m\033[4mВас приветствует \033[1m"ХОТ-ДОГ НА ЛЮБОЙ ВКУС"!\033[0m')
        print('1. Войти как администратор\n'
              '2. Войти как покупатель\n'
              '3. Закончить работу')
        return input('Ваш выбор (цифрой): ')

    @add_title('Выход из программы')
    def exit_menu(self):
        print('\033[94mДо новых встреч!\033[0m')

    @add_title('Проверка уровня доступа')
    def admin_password(self):
        return input('Введите пароль: ')

    @add_title('Меню администратора')
    def admin_menu(self):
        print('1. Просмотреть количество проданных хот-догов\n'
              '2. Посмотреть общую выручку\n'
              '3. Посмотреть "чистую" прибыль\n'
              '4. Посмотреть остаток товара на складе\n'
              '5. Пополнить количество товара на складе\n'
              '6. Вернуться в главное меню')
        return input('Ваш выбор (цифрой): ')

    @add_title('Меню покупателя')
    def buyer_menu(self):
        print('1. Выбрать готовый хот-дог\n'
              '2. Заказать хот-дог по своему рецепту\n'
              '3. Посмотреть заказ\n'
              '4. Внести изменения в заказ\n'
              '5. Выбрать способ оплаты и завершить заказ\n'
              '6. Отменить заказ и вернуться в главное меню')
        return input('Ваш выбор (цифрой): ')

    @add_title('Выбор способа оплаты')
    def payment_method(self):
        print('1. Наличные\n'
              '2. Карта')
        return input('Ваш выбор (цифрой): ')

    @add_title('Добавление продуктов')
    def add_product(self):
        return input('Какое количество добавить на склад (цифрой): ')

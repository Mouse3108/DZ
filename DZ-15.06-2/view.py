class ShoeType:
    MALE = 'мужская'
    FEMALE = 'женская'


class ShoeStyle:
    SNEAKERS = 'кроссовки'
    BOOTS = 'сапоги'
    SANDALS = 'сандалии'
    SHOES = 'туфли'


class ShoeView:
    def menu(self):
        print('Выберите действие:\n'
              '\t1. Добавить новую обувь\n'
              '\t2. Просмотреть варианты обуви\n'
              '\t3. Найти нужную обувь\n'
              '\t4. Удалить лишнюю обувь\n'
              '\t5. Выйти из программы')
        query_menu = input('Введите свой выбор (1 / 2 / 3 / 4 / 5): ')
        return query_menu

    def new_shoe(self):
        while True:
            try:
                shoe_type = input('Введите тип обуви (мужская/женская): ')
                if shoe_type not in (ShoeType.MALE, ShoeType.FEMALE):
                    raise ValueError('Недопустимый тип обуви')
                style = input('Введите вид обуви (кроссовки/сапоги/сандалии/туфли): ')
                if style not in (ShoeStyle.SNEAKERS, ShoeStyle.BOOTS, ShoeStyle.SANDALS, ShoeStyle.SHOES):
                    raise ValueError('Недопустимый вид обуви')
                color = input('Введите цвет обуви: ')
                price = input('Введите цену обуви: ')
                manufacturer = input('Введите производителя обуви: ')
                size = input('Введите размер обуви: ')
                dict_shoe = {
                    'тип': shoe_type,
                    'стиль': style,
                    'цвет': color,
                    'цена': price,
                    'производитель': manufacturer,
                    'размер': size
                }
                return dict_shoe
            except ValueError as e:
                print(e)
                print('Введите данные повторно!')

    def print_shoes(self, shoes):
        if shoes:
            [print(i, shoe) for i, shoe in enumerate(shoes, 1)]
        else:
            print('Обуви нет :(')

    def find_shoes(self):
        criteria = input('Введите через пробел критерии, по которым искать обувь '
                         '(тип, стиль, цвет, цена, производитель, размер): ').split()
        return criteria

    def delete_shoe(self):
        name = input('Введите критерий, по которому искать обувь для удаления: ')
        return name

    def delete_context(self):
        number = int(input('Введите порядковый номер обуви, которую нужно удалить: '))
        return number

    def return_delete_result(self, result):
        print(result)
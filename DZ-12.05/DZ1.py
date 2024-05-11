# Задание 1.
# Пользователь вводит с клавиатуры набор чисел. Полученные числа необходимо сохранить в список
# (тип списка нужно выбрать в зависимости от поставленной ниже задачи).
# После чего нужно показать меню, в котором предложить пользователю набор пунктов:
# 1. Добавить новое число в список (если такое число существует в списке,
# нужно вывести сообщение пользователю об этом, без добавления числа).
# 2. Удалить все вхождения числа из списка (пользователь вводит с клавиатуры число для удаления)
# 3. Показать содержимое списка (в зависимости от выбора пользователя список нужно показать с начала или с конца)
# 4. Проверить есть ли значение в списке
# 5. Заменить значение в списке (пользователь определяет заменить ли только первое вхождение или все вхождения)
# В зависимости от выбора пользователя выполняется действие, после чего меню отображается снова.
class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next


class Double_linked_list:
    def __init__(self):
        self.head = None

    @property
    def tail(self):
        current = self.head
        while current.next:
            current = current.next
        return current

    def append(self, value):
        node = Node(value, None, None)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node
        node.prev = current

    def remove(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current.prev is None:
                    self.head = current.next
                    if self.head is not None:
                        self.head.prev = None
                else:
                    current.prev.next = current.next
                    if current.next is not None:
                        current.next.prev = current.prev
                current = current.next
            else:
                current = current.next

    def show_list(self):
        result = "None -> "
        current = self.head
        while current:
            result += str(current.value) + ' -> '
            current = current.next
        result += 'None'
        return result

    def show_list_reverse(self):
        result = "None -> "
        current = self.tail
        while current:
            result += str(current.value) + " -> "
            current = current.prev
        result += "None"
        return result

    def contains(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def replace(self, num, new_num):
        current = self.head
        while current:
            if current.value == num:
                current.value = new_num
                return
            current = current.next

    def replace_all(self, num, new_num):
        current = self.head
        while current:
            if current.value == num:
                current.value = new_num
            current = current.next


numbers_list = Double_linked_list()
while True:
    try:
        numbers = map(int, input('Введите список чисел через пробел: ').split())
        for num in numbers:
            numbers_list.append(num)
        break
    except ValueError:
        print('\033[91mНеверный ввод! Введите числа через пробел ещё раз.\033[0m')

while True:
    print("""\n\t1. Добавить новое число в список
    2. Удалить все вхождения числа из списка.
    3. Показать содержимое списка
    4. Проверить, есть ли значение в списке
    5. Заменить значение в списке
    6. Закончить""")
    command = input('\nВведите номер команды: ')
    if command == '1':
        num = int(input('\nВведите число для добавления: '))
        if numbers_list.contains(num):
            print('\033[91mТакое число уже есть в списке.\033[0m')
            continue
        else:
            numbers_list.append(num)
            print(f'Число {num} добавлено в список')
    elif command == '2':
        num = int(input('Введите число для удаления: '))
        if numbers_list.contains(num):
            numbers_list.remove(num)
            print(f'Число {num} удалено из списка')
        else:
            print('\033[91mТакого числа нет списке!\033[0m')
            continue
    elif command == '3':
        print('Как показать содержимое списка?')
        dop_command = input('С начала или с конца: start / end ')
        if dop_command == 'start':
            print(numbers_list.show_list())
        elif dop_command == 'end':
            print(numbers_list.show_list_reverse())
        else:
            print('\033[91mТакого варианта нет!\033[0m')
    elif command == '4':
        num = int(input('Какое число найти в списке: '))
        if numbers_list.contains(num):
            print(f'Число {num} есть в списке')
        else:
            print(f'Число {num} отсутствует в списке')
    elif command == '5':
        num = int(input('Какое число заменить: '))
        if numbers_list.contains(num):
            new_num = int(input('Введите новое число: '))
            replace_one_all = input(f'Заменить все вхождения числа {num} или одно: one / all ')
            if replace_one_all == 'one':
                numbers_list.replace(num, new_num)
                print(f'Одно число {num} было заменено на {new_num}')
            elif replace_one_all == 'all':
                numbers_list.replace_all(num, new_num)
                print(f'Все числа {num} были заменены на {new_num}')
            else:
                print('\033[91mТакого варианта нет!\033[0m')
        else:
            print(f'Число {num} отсутствует в списке')
    elif command == '6':
        print('\033[95mРабота со списком чисел окончена!\033[0m')
        break
    else:
        print('Такой команды нет! Попробуйте снова')
# Задание 2.
# Реализуйте класс стека для работы со строками (стек строк). Стек должен иметь фиксированный размер.
# Реализуйте набор операций для работы со стеком:
# ■ помещение строки в стек;
# ■ выталкивание строки из стека;
# ■ подсчет количества строк в стеке;
# ■ проверку пустой ли стек;
# ■ проверку полный ли стек;
# ■ очистку стека;
# ■ получение значения без выталкивания верхней строки из стека.
# При старте приложения нужно отобразить меню с помощью, которого пользователь может выбрать необходимую операцию.
class Stack:
    def __init__(self, size, *args):
        self.items = list(args)
        self.size = size

    def push(self, value):
        if len(self.items) < self.size:
            self.items.append(value)
            print(f'В стек добавлена строка: {value}')
        else:
            print('\033[91mСтек полностью заполнен!\033[0m')

    def pop(self):
        if len(self.items) != 0:
            return self.items.pop()
        else:
            print('\033[91mСтек пуст!\033[0m')

    def count(self):
        return len(self.items)

    def is_empty(self):
        if len(self.items) == 0:
            return 'Стек пустой'
        elif len(self.items) < self.size:
            return 'Стек заполнен не полностью'
        else:
            return 'Стек полностью заполнен'

    def is_full(self):
        if len(self.items) == self.size:
            return 'Стек полностью заполнен'
        else:
            return 'Стек пустой или заполнен не полностью'

    def clear(self):
        self.items = []

    def peek(self):
        if len(self.items) != 0:
            return print(f'Верхняя строка в стеке: {self.items[-1]}')
        else:
            return print('\033[91mСтек пустой!\033[0m')


stack = Stack(int(input("Введите размер стека: ")))
while True:
    print("""\n\t1. Поместить строку в стек
    2. Выталкивание строки из стека
    3. Подсчет количества строк в стеке
    4. Проверка пустой ли стек
    5. Проверка полный ли стек
    6. Очистка стека
    7. Получение значения верхней строки без её выталкивания
    8. Выход""")
    command = input('\nВведите номер команды: ')
    if command == '1':
        value = input('Введите строку для помещения в стек: ')
        stack.push(value)
    elif command == '2':
        print(f'Из стека выталкивается строка: {stack.pop()}')
    elif command == '3':
        print(f'Количество строк в стеке: {stack.count()}')
    elif command == '4':
        print(stack.is_empty())
    elif command == '5':
        print(stack.is_full())
    elif command == '6':
        stack.clear()
        print('Стек очищен')
    elif command == '7':
        stack.peek()
    elif command == '8':
        print('\033[95mРабота со стеком окончена!\033[0m')
        break
    else:
        print('\033[91mТакой команды нет! Попробуйте снова\033[0m')
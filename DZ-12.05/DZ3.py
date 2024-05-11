# Задание 3.
# Измените стек из второго задания, таким образом, чтобы его размер был нефиксированным.
class Stack:
    def __init__(self, *args):
        self.items = list(args)

    def push(self, value):
        self.items.append(value)
        print(f'В стек добавлена строка: {value}')

    def pop(self):
        if len(self.items) != 0:
            print(f'Из стека выталкивается строка: {self.items.pop()}')
        else:
            print('\033[91mСтек пуст!\033[0m')

    def count(self):
        return len(self.items)

    def is_empty(self):
        if len(self.items) == 0:
            return 'Стек пустой'
        else:
            return 'Стек заполнен'

    def is_full(self):
        if len(self.items) != 0:
            return 'Стек заполнен'
        else:
            return 'Стек пустой'

    def clear(self):
        self.items = []

    def peek(self):
        if len(self.items) != 0:
            return print(f'Верхняя строка в стеке: {self.items[-1]}')
        else:
            return print('\033[91mСтек пустой!\033[0m')


stack = Stack()
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
        stack.pop()
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
# Задание 2.
# Есть класс, предоставляющий доступ к набору чисел. Источником этого набора чисел является некоторый файл.
# Приложение должно получать доступ к этим данным и выполнять набор операций над ними
# (сумма, максимум, минимум и т.д.). При каждой попытке доступа к этому набору необходимо вносить запись в лог-файл.
# При реализации используйте паттерн Proxy (для логгирования).
class Numbers:
    def __init__(self, file_name):
        self.file_name = file_name
        with open(self.file_name, 'r', encoding='utf-8') as file:
            self.data = [int(num) for line in file for num in line.strip().split()]

    def mathematical_operations(self):
        summa = sum(self.data)
        multiplying = 1
        for num in self.data:
            multiplying *= num
        max_number = max(self.data)
        min_number = min(self.data)
        min_to_max = " ".join(map(str, sorted(self.data)))
        max_to_min = " ".join(map(str, reversed(sorted(self.data))))
        return (f'Сумма всех чисел: {summa}\nПроизведение всех чисел: {multiplying}\n'
                f'Максимальное число: {max_number}\nМинимальное число: {min_number}\n'
                f'Все числа от меньшего к большему: {min_to_max}\nВсе числа от большего к меньшему: {max_to_min}\n')


class NumbersProxy:
    def __init__(self, file_name):
        self.numbers = None
        with open(file_name, 'r', encoding='utf-8') as file:
            data = [num for line in file for num in line.strip().split()]
        self.log_file = open('log.txt', 'a', encoding='utf-8')
        if len(data) > 1:
            self.numbers = Numbers(file_name)
            self.log_file.write(f'Был доступ к файлу "{self.numbers.file_name}"\n')
        else:
            self.log_file.write(f'Был доступ к файлу "{file_name}". Математические операции не проводились!\n')

    def mathematical_operations(self):
        if self.numbers is not None:
            result = self.numbers.mathematical_operations()
            self.log_file.write(f'Проведенные с числами математические операции:\n{result}\n')
            return result
        else:
            return 'С одним числом математические операции не проводятся!'


numbers = NumbersProxy('numbers2.txt')
print(numbers.mathematical_operations())

numbers = NumbersProxy('numbers.txt')
print(numbers.mathematical_operations())
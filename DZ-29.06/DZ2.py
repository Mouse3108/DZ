# Задание 2.
# Пользователь с клавиатуры вводит путь к файлу. После чего запускаются три потока.
# Первый поток заполняет файл случайными числами. Два других потока ожидают заполнения.
# Когда файл заполнен оба потока стартуют. Первый поток находит все простые числа,
# второй поток - факториал каждого числа в файле. Результаты поиска каждый поток должен записать в новый файл.
# На экран необходимо отобразить статистику выполненных операций.
import threading
import random
import time


class NumbersThread(threading.Thread):
    def __init__(self, func, filename):
        super().__init__()
        self.func = func
        self.filename = filename
        self.result = None

    def run(self):
        start = time.time()
        print(f'Поток {self.func} запущен')
        self.result = self.func(self.filename)
        end = time.time()
        print(f'Поток {self.func} завершен за {end - start} сек.')


def write_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write(text)


def read_from_file(filename):
    with open(filename, 'r') as file:
        str_nums = file.read().split()
    nums = [int(num) for num in str_nums]
    return nums


def random_numbers(filename):
    nums = [random.randint(20, 40) for i in range(500)]
    write_to_file(filename, ' '.join(map(str, nums)))
    return f'В файл {filename} записан список случайных чисел'


def prime_numbers(filename):
    nums = read_from_file(filename)
    prime_nums = [num for num in nums if all(num % i != 0 for i in range(2, (num // 2 + 1) + 1))]
    write_to_file('newfile.txt', ('Простые числа:' + ' '.join(map(str, prime_nums)) + '\n'))
    return f'Количество простых чисел - {len(prime_nums)}. Числа записаны в файл newfile.txt'


def factorial_of_numbers(filename):
    nums = read_from_file(filename)
    factorial_of_nums = ''
    for num in nums:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        factorial_of_nums += f'Факториал числа {num} = {factorial}\n'
    write_to_file('newfile.txt', factorial_of_nums)
    return f'Факториал каждого из чисел записан в файл newfile.txt'


filename = input('Введите имя файла: ')

thread1 = NumbersThread(random_numbers, filename)
thread1.start()
thread1.join()
thread2 = NumbersThread(prime_numbers, filename)
thread3 = NumbersThread(factorial_of_numbers, filename)
thread2.start()
thread3.start()
thread2.join()
thread3.join()

print(thread1.result)
print(thread2.result)
print(thread3.result)
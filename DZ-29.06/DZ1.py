# Задание 1.
# При старте приложения запускаются три потока. Первый поток заполняет список случайными числами.
# Два других потока ожидают заполнения. Когда список заполнен оба потока запускаются.
# Первый поток находит сумму элементов списка, второй поток среднеарифметическое значение в списке.
# Полученный список, сумма и среднеарифметическое выводятся на экран.
import threading
import random


class NumbersThread(threading.Thread):
    def __init__(self, func, nums=None):
        super().__init__()
        self.func = func
        self.nums = nums
        self.result = None

    def run(self):
        if self.nums is not None:
            self.result = self.func(self.nums)
        else:
            self.result = self.func()


def random_numbers():
    nums = [random.randint(10, 50) for i in range(50000)]
    return nums


def sum_numbers(nums):
    return sum(nums)


def average_numbers(nums):
    return sum(nums) / len(nums)


thread1 = NumbersThread(random_numbers)
thread1.start()
thread1.join()
thread2 = NumbersThread(sum_numbers, thread1.result)
thread3 = NumbersThread(average_numbers, thread1.result)
thread2.start()
thread3.start()

print('Список чисел:', *thread1.result)
print(f'Сумма чисел: {thread2.result}')
print(f'Среднеарифметическое чисел: {thread3.result}')

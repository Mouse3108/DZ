# Задание 1.
# Создайте функцию, возвращающую список со всеми простыми числами от 0 до 1000.
# Используя механизм декораторов посчитайте сколько секунд потребовалось для вычисления всех простых чисел.
# Отобразите на экран количество секунд и простые числа.
import time


def times(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        numbers = func(*args, **kwargs)
        print(f'Затраченное время в секундах: {time.time() - start}')
        return numbers
    return wrapper


@times
def prime_numbers():
    primes = [num for num in range(1, 1001) if len([i for i in range(1, int(num / 2 + 1)) if num % i == 0]) == 1]
    print('Простые числа от 0 до 1000:')
    for i in range(0, len(primes), 30):
        print(*primes[i:i + 30])


prime_numbers()
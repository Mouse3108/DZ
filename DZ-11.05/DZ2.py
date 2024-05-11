# Задание 2.
# Добавьте к первому заданию возможность передавать границы диапазона для поиска всех простых чисел.
import time


def times(func):
    def wrapper(start_range, end_range):
        start = time.time()
        numbers = func(start_range, end_range)
        print(f'Затраченное время в секундах: {time.time() - start}')
        return numbers
    return wrapper


@times
def prime_numbers(start_range, end_range):
    primes = [num for num in range(start_range, end_range + 1)
              if len([i for i in range(1, int(num / 2 + 1)) if num % i == 0]) == 1]
    print(f'Простые числа от {start_range} до {end_range}:')
    for i in range(0, len(primes), 30):
        print(*primes[i:i + 30])


prime_numbers(1, 27)
prime_numbers(15, 527)
prime_numbers(1005, 1598)
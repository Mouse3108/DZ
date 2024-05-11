# Задание 3.
# Реализуйте декоратор для обработки исключений, возникающих внутри функции,
# и вывода соответствующего сообщения об ошибке.
def error():
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ZeroDivisionError:
                return 'На ноль делить нельзя!'
            except TypeError:
                return 'Необходимо ввести целое число!'
        return wrapper
    return decorator


@error()
def division(dividend: int, divisor: int):
    return dividend / divisor


print(division(5, 0))
print(division('5', 2))
print(division(5, 2))
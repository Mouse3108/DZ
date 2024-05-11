# Задание 1.
# К уже реализованному классу «Дробь» добавьте статический метод,
# который при вызове возвращает количество созданных объектов класса «Дробь».

def common_divisors(a, b, c):
    if c <= 0:
        c = max(a, b)
        if c == 0:
            c = 1
            return c
    if a % c == 0 and b % c == 0:
        return c
    return common_divisors(a, b, c - 1)


class Fraction:
    num_objects = 0

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if denominator == 0:
            print('На ноль делить нельзя!')
            self.denominator = int(input('Введите новый делитель: '))

    @staticmethod
    def get_num_objects():
        return Fraction.num_objects

    def get_addition(self, b):
        new_numerator = self.numerator * b.denominator + b.numerator * self.denominator
        new_denominator = self.denominator * b.denominator
        Fraction.num_objects += 1
        return (new_numerator // common_divisors(new_numerator, new_denominator, min(new_numerator, new_denominator)),
                '/',
                new_denominator // common_divisors(new_numerator, new_denominator, min(new_numerator, new_denominator)))

    def get_subtraction(self, b):
        new_numerator = self.numerator * b.denominator - b.numerator * self.denominator
        new_denominator = self.denominator * b.denominator
        Fraction.num_objects += 1
        return (new_numerator // common_divisors(new_numerator, new_denominator, min(new_numerator, new_denominator)),
                '/',
                new_denominator // common_divisors(new_numerator, new_denominator, min(new_numerator, new_denominator)))

    def get_multiplication(self, b):
        new_numerator = self.numerator * b.numerator
        new_denominator = self.denominator * b.denominator
        Fraction.num_objects += 1
        return (new_numerator // common_divisors(new_numerator, new_denominator, min(new_numerator, new_denominator)),
                '/',
                new_denominator // common_divisors(new_numerator, new_denominator, min(new_numerator, new_denominator)))

    def get_division(self, b):
        new_numerator = self.numerator * b.denominator
        new_denominator = self.denominator * b.numerator
        Fraction.num_objects += 1
        return (new_numerator // common_divisors(new_numerator, new_denominator, min(new_numerator, new_denominator)),
                '/',
                new_denominator // common_divisors(new_numerator, new_denominator, min(new_numerator, new_denominator)))


a = Fraction(5, 14)
b = Fraction(7, 14)
c = Fraction(2, 3)
print(*a.get_addition(b))
print(*a.get_subtraction(b))
print(*a.get_multiplication(b))
print(*a.get_division(b))
print(*b.get_addition(c))
print(*b.get_subtraction(c))
print(*b.get_multiplication(c))
print(*b.get_division(c))
print(f'Количество созданных объектов: {Fraction.get_num_objects()}')
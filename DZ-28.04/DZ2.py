# Задание 2.
# Создайте класс Complex (комплексное число). Создайте перегруженные операторы
# для реализации арифметических операций по работе с комплексными числами (операции +, -, *, /).
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        if self.imaginary == 0:
            self.imaginary = -1
        if other.imaginary == 0:
            other.imaginary = -1
        if self.imaginary + other.imaginary > 0:
            return f'{self.real + other.real} + {self.imaginary + other.imaginary}i'
        elif self.imaginary + other.imaginary < 0:
            return f'{self.real + other.real} - {-(self.imaginary + other.imaginary)}i'
        else:
            return f'{self.real + other.real} + i'

    def __sub__(self, other):
        if self.imaginary == 0:
            self.imaginary = -1
        if other.imaginary == 0:
            other.imaginary = -1
        if self.imaginary - other.imaginary > 0:
            return f'{self.real - other.real} + {self.imaginary - other.imaginary}i'
        elif self.imaginary - other.imaginary < 0:
            return f'{self.real - other.real} - {-(self.imaginary - other.imaginary)}i'
        else:
            return f'{self.real + other.real} + i'

    def __mul__(self, other):
        if self.imaginary == 0:
            self.imaginary = -1
        if other.imaginary == 0:
            other.imaginary = -1
        if self.real * other.imaginary + self.imaginary * other.real > 0:
            return (f'{self.real * other.real - self.imaginary * other.imaginary} '
                    f'+ {self.real * other.imaginary + self.imaginary * other.real}i')
        elif self.real * other.imaginary + self.imaginary * other.real < 0:
            return (f'{self.real * other.real - self.imaginary * other.imaginary} '
                    f'- {-(self.real * other.imaginary + self.imaginary * other.real)}i')
        else:
            return f'{self.real + other.real} + i'

    def __truediv__(self, other):
        if self.imaginary == 0:
            self.imaginary = -1
        if other.imaginary == 0:
            other.imaginary = -1
        try:
            if (self.imaginary * other.real - self.real * other.imaginary) / other.real**2 + other.imaginary**2 > 0:
                return (f'{(self.real * other.real + self.imaginary * other.imaginary)} '
                        f'/ {other.real**2 + other.imaginary**2} '
                        f'+ {(self.imaginary * other.real - self.real * other.imaginary)} '
                        f'/ {other.real**2 + other.imaginary**2}i')
            elif (self.imaginary * other.real - self.real * other.imaginary) / other.real**2 + other.imaginary**2 < 0:
                return (f'{(self.real * other.real + self.imaginary * other.imaginary)} '
                        f'/ {other.real**2 + other.imaginary**2} '
                        f'- {(self.imaginary * other.real - self.real * other.imaginary)} '
                        f'/ {other.real**2 + other.imaginary**2}i')
            else:
                return (f'{(self.real * other.real + self.imaginary * other.imaginary)} '
                        f'/ {other.real**2 + other.imaginary**2} + i')
        except ZeroDivisionError:
            return f'вычислить {self.real}/0 и {other.real}/0 невозможно! На ноль делить нельзя!'


c1 = Complex(5, -7)
c2 = Complex(4, 6)
c3 = Complex(0, 0)
c4 = Complex(1, 7)

print(f'c1 + c2 = {c1 + c2}')
print(f'c1 - c2 = {c1 - c2}')
print(f'c1 * c2 = {c1 * c2}')
print(f'c1 / c2 = {c1 / c2}')
print(f'c4 / c3 = {c4 / c3}')
print(f'c1 + c4 = {c1 + c4}')
print(f'c3 - c4 = {c3 - c4}')
print(f'c2 * c4 = {c2 * c4}')
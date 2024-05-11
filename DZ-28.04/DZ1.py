# Задание 1.
# Создайте класс Circle (окружность). Для данного класса реализуйте ряд перегруженных операторов:
# ■ Проверка на равенство радиусов двух окружностей (операция ==);
# ■ Сравнения длин двух окружностей (операции >, <, <=, >=);
# ■ Пропорциональное изменение размеров окружности, путем изменения ее радиуса (операции + - += -=)
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        if self.radius == other.radius:
            return f'Радиусы окружностей равны: {self.radius}'
        else:
            return f'Радиусы окружностей не равны: {self.radius} и {other.radius}'

    def __gt__(self, other):
        if self.radius * 2 * 3.14 > other.radius * 2 * 3.14:
            return (f'Длина окружности с радиусом {self.radius} больше длины окружности с радиусом {other.radius}: '
                    f'{round(self.radius * 2 * 3.14, 1)} > {round(other.radius * 2 * 3.14, 1)}')
        else:
            return (f'Длина окружности с радиусом {self.radius} не больше длины окружности с радиусом {other.radius}: '
                    f'{round(self.radius * 2 * 3.14, 1)} < или = {round(other.radius * 2 * 3.14, 1)}')

    def __lt__(self, other):
        if self.radius * 2 * 3.14 < other.radius * 2 * 3.14:
            return (f'Длина окружности с радиусом {self.radius} меньше длины окружности с радиусом {other.radius}: '
                    f'{round(self.radius * 2 * 3.14, 1)} < {round(other.radius * 2 * 3.14, 1)}')
        else:
            return (f'Длина окружности с радиусом {self.radius} не меньше длины окружности с радиусом {other.radius}: '
                    f'{round(self.radius * 2 * 3.14, 1)} > или = {round(other.radius * 2 * 3.14, 1)}')

    def __le__(self, other):
        if self.radius * 2 * 3.14 <= other.radius * 2 * 3.14:
            return (f'Длина окружности с радиусом {self.radius} меньше или равна длине окружности с радиусом {other.radius}: '
                    f'{round(self.radius * 2 * 3.14, 1)} <= {round(other.radius * 2 * 3.14, 1)}')
        else:
            return (f'Длина окружности с радиусом {self.radius} больше длины окружности с радиусом {other.radius}: '
                    f'{round(self.radius * 2 * 3.14, 1)} > {round(other.radius * 2 * 3.14, 1)}')

    def __ge__(self, other):
        if self.radius * 2 * 3.14 >= other.radius * 2 * 3.14:
            return (
                f'Длина окружности с радиусом {self.radius} больше или равна длине окружности с радиусом {other.radius}: '
                f'{round(self.radius * 2 * 3.14, 1)} >= {round(other.radius * 2 * 3.14, 1)}')
        else:
            return (f'Длина окружности с радиусом {self.radius} меньше длины окружности с радиусом {other.radius}: '
                    f'{round(self.radius * 2 * 3.14, 1)} < {round(other.radius * 2 * 3.14, 1)}')

    def __add__(self, value):
        return (f'У круга с радиусом {self.radius} длина окружности: {round(self.radius * 2 * 3.14, 1)}, '
                f'площадь {round(self.radius * self.radius * 3.14, 1)}. '
                f'Радиус окружности увеличен на {value}. '
                f'Новая длина окружности: {round((self.radius + value) * 2 * 3.14, 1)}, '
                f'новая площадь окружности: {round((self.radius + value) * (self.radius + value) * 3.14, 1)}')

    def __sub__(self, value):
        return (f'У круга с радиусом {self.radius} длина окружности: {round(self.radius * 2 * 3.14, 1)}, '
                f'площадь {round(self.radius * self.radius * 3.14, 1)}. '
                f'Радиус окружности уменьшен на {value}. '
                f'Новая длина окружности: {round((self.radius - value) * 2 * 3.14, 1)}, '
                f'новая площадь окружности: {round((self.radius - value) * (self.radius - value) * 3.14, 1)}')

    def __iadd__(self, value):
        length_circle = round(self.radius * 2 * 3.14, 1)
        area_circle = round(self.radius * self.radius * 3.14, 1)
        self.radius += value
        return (f'У круга с радиусом {self.radius - value} длина окружности: {length_circle}, площадь {area_circle}. '
                f'Радиус окружности увеличен на {value}. '
                f'Новая длина окружности: {round(self.radius * 2 * 3.14, 1)}, '
                f'новая площадь окружности: {round(self.radius * self.radius * 3.14, 1)}')

    def __isub__(self, value):
        length_circle = round(self.radius * 2 * 3.14, 1)
        area_circle = round(self.radius * self.radius * 3.14, 1)
        self.radius -= value
        return (f'У круга с радиусом {self.radius + value} длина окружности: {length_circle}, площадь {area_circle}. '
                f'Радиус окружности уменьшен на {value}. '
                f'Новая длина окружности: {round(self.radius * 2 * 3.14, 1)}, '
                f'новая площадь окружности: {round(self.radius * self.radius * 3.14, 1)}')


c1 = Circle(15)
c2 = Circle(10)
c3 = Circle(15)
print(c1 == c2)
print(c1 == c3)
print(c1 > c2)
print(c2 > c3)
print(c2 < c3)
print(c1 < c3)
print(c1 >= c3)
print(c1 <= c2)
print(c1 <= c3)
print(c1 + 3)
print(c2 - 2)
c1 += 3
print(c1)
c2 -= 2
print(c2)
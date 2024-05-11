# Задание 3.
# Вам необходимо создать класс Airplane (самолет). С помощью перегрузки операторов реализовать:
# ■ Проверка на равенство типов самолетов (операция ==);
# ■ Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
# ■ Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции > < <= >=).
class Airplane:
    def __init__(self, airplane_type, max_passengers):
        self.airplane_type = airplane_type
        self.max_passengers = max_passengers

    def __eq__(self, other):
        if self.airplane_type == other.airplane_type:
            return f'Самолёты одного типа: {self.airplane_type}'
        else:
            return f'Самолёты разных типов: {self.airplane_type} и {other.airplane_type}'

    def __add__(self, value):
        return (f'У самолёта "{self.airplane_type}" количество пассажиров было увеличено на: {value}. '
                f'Теперь в самолёте: {self.max_passengers + value} пассажиров')

    def __sub__(self, value):
        return (f'У самолёта "{self.airplane_type}" количество пассажиров было уменьшено на: {value}. '
                f'Теперь в самолёте: {self.max_passengers - value} пассажиров')

    def __iadd__(self, value):
        self.max_passengers += value
        return (f'У самолёта "{self.airplane_type}" количество пассажиров было увеличено на: {value}. '
                f'Теперь в самолёте: {self.max_passengers} пассажиров')

    def __isub__(self, value):
        self.max_passengers -= value
        return (f'У самолёта "{self.airplane_type}" количество пассажиров было уменьшено на: {value}. '
                f'Теперь в самолёте: {self.max_passengers} пассажиров')

    def __gt__(self, other):
        if self.max_passengers > other.max_passengers:
            return (f'Верно, что у самолёта "{self.airplane_type}" максимальное количество пассажиров больше, '
                    f'чем у самолёта "{other.airplane_type}": {self.max_passengers} > {other.max_passengers}')
        else:
            return (f'Не верно, что у самолёта "{self.airplane_type}" максимальное количество пассажиров больше, '
                    f'чем у самолёта "{other.airplane_type}": {self.max_passengers} < {other.max_passengers}')

    def __lt__(self, other):
        if self.max_passengers < other.max_passengers:
            return (f'Верно, что у самолёта "{self.airplane_type}" максимальное количество пассажиров меньше, '
                    f'чем у самолёта "{other.airplane_type}": {self.max_passengers} < {other.max_passengers}')
        else:
            return (f'Не верно, что у самолёта "{self.airplane_type}" максимальное количество пассажиров меньше, '
                    f'чем у самолёта "{other.airplane_type}": {self.max_passengers} > {other.max_passengers}')

    def __le__(self, other):
        if self.max_passengers <= other.max_passengers:
            return (f'Верно, что у самолёта "{self.airplane_type}" '
                    f'максимальное количество пассажиров меньше или равно количеству пассажиров '
                    f'у самолёта "{other.airplane_type}": {self.max_passengers} < или = {other.max_passengers}')
        else:
            return (f'Не верно, что у самолёта "{self.airplane_type}" '
                    f'максимальное количество пассажиров меньше или равно количеству пассажиров '
                    f'у самолёта "{other.airplane_type}": {self.max_passengers} > или = {other.max_passengers}')

    def __ge__(self, other):
        if self.max_passengers >= other.max_passengers:
            return (f'Верно, что у самолёта "{self.airplane_type}" '
                    f'максимальное количество пассажиров больше или равно количеству пассажиров '
                    f'у самолёта "{other.airplane_type}": {self.max_passengers} > или = {other.max_passengers}')
        else:
            return (f'Не верно, что у самолёта "{self.airplane_type}" '
                    f'максимальное количество пассажиров больше или равно количеству пассажиров '
                    f'у самолёта "{other.airplane_type}": {self.max_passengers} < или = {other.max_passengers}')


airplane1 = Airplane('ИЛ-62', 186)
airplane2 = Airplane('ТУ-134', 72)
airplane3 = Airplane('Airbus', 180)
airplane4 = Airplane('Boeing', 186)
airplane5 = Airplane('ТУ-134', 72)

print(airplane1 == airplane4)
print(airplane2 == airplane5)

print(airplane1 > airplane2)
print(airplane3 > airplane4)
print(airplane2 < airplane4)
print(airplane4 < airplane3)
print(airplane2 >= airplane3)
print(airplane1 >= airplane4)
print(airplane3 <= airplane1)
print(airplane4 <= airplane2)

print(airplane3 - 10)
print(airplane5 + 10)
airplane5 += 12
print(airplane5)
airplane1 -= 10
print(airplane1)
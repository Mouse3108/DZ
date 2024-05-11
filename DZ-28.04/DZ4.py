# Задание 4.
# Создать класс Flat (квартира). Реализовать перегруженные операторы:
# ■ Проверка на равенство площадей квартир (операция ==);
# ■ Проверка на неравенство площадей квартир (операция !=);
# ■ Сравнение двух квартир по цене (операции > < <= >=).
class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        if self.area == other.area:
            return f'Верно, что площади квартир равны: {self.area}'
        else:
            return f'Не верно, что площади квартир равны: {self.area} и {other.area}'

    def __ne__(self, other):
        if self.area != other.area:
            return f'Верно, что площади квартир не равны: {self.area} и {other.area}'
        else:
            return f'Не верно, что площади квартир не равны: {self.area}'

    def __gt__(self, other):
        if self.price > other.price:
            return (f'Верно, что цена первой квартиры больше, чем цена второй квартиры: '
                    f'{self.price} > {other.price}')
        else:
            return (f'Не верно, что цена первой квартиры больше, чем цена второй квартиры: '
                    f'{self.price} < {other.price}')

    def __lt__(self, other):
        if self.price < other.price:
            return (f'Верно, что цена первой квартиры меньше, чем цена второй квартиры: '
                    f'{self.price} < {other.price}')
        else:
            return (f'Не верно, что цена первой квартиры меньше, чем цена второй квартиры: '
                    f'{self.price} > {other.price}')

    def __le__(self, other):
        if self.price <= other.price:
            return (f'Верно, что цена первой квартиры меньше или равна цене второй квартиры: '
                    f'{self.price} < или = {other.price}')
        else:
            return (f'Не верно, что цена первой квартиры меньше или равна цене второй квартиры: '
                    f'{self.price} > или = {other.price}')

    def __ge__(self, other):
        if self.price >= other.price:
            return (f'Верно, что цена первой квартиры больше или равна цене второй квартиры: '
                    f'{self.price} > или = {other.price}')
        else:
            return (f'Не верно, что цена первой квартиры больше или равна цене второй квартиры: '
                    f'{self.price} < или = {other.price}')


flat1 = Flat(50, 3000000)
flat2 = Flat(30, 2000000)
flat3 = Flat(55, 3000000)
flat4 = Flat(30, 2900000)

print(flat1 == flat2)
print(flat2 == flat4)
print(flat2 != flat3)
print(flat2 != flat4)
print(flat1 > flat2)
print(flat4 > flat3)
print(flat1 < flat4)
print(flat2 < flat3)
print(flat1 >= flat3)
print(flat2 >= flat3)
print(flat4 <= flat1)
print(flat3 <= flat2)
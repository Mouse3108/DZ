# Задание 2.
# Создайте класс для конвертирования температуры из Цельсия в Фаренгейт и наоборот.
# У класса должно быть два статических метода: для перевода из Цельсия в Фаренгейт
# и для перевода из Фаренгейта в Цельсий. Также класс должен считать количество подсчетов температуры
# и возвращать это значение с помощью статического метода.
class Fraction:
    num_temperature = 0

    @staticmethod
    def fahrenheit_to_celsius(temperature):
        Fraction.num_temperature += 1
        return (temperature - 32) * 5 / 9

    @staticmethod
    def celsius_to_fahrenheit(temperature):
        Fraction.num_temperature += 1
        return temperature * 9 / 5 + 32

    @staticmethod
    def get_num_temperature():
        return Fraction.num_temperature


print(f'32°F = {Fraction.fahrenheit_to_celsius(32)}°C')
print(f'10°C = {Fraction.celsius_to_fahrenheit(10)}°F')
print(f'15°F = {Fraction.fahrenheit_to_celsius(15)}°C')
print(f'-20°C = {Fraction.celsius_to_fahrenheit(-20)}°F')
print(f'Количество подсчетов температуры: {Fraction.get_num_temperature()}')
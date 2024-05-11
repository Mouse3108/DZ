# Задание 4.
# Создайте декоратор, который применяется к классу и изменяет его поведение или добавляет новые методы.
def add_methods(calculator):
    def add(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    calculator.add = add
    calculator.subtraction = subtraction
    return calculator


@add_methods
class Calculator:
    def __init__(self):
        return


print(Calculator().add(20, 7))
print(Calculator().subtraction(7, 20))
print(Calculator().add(20, 7) / Calculator().subtraction(7, 20))
# Задание 3. Создайте реализацию паттерна Prototype. Протестируйте работу созданного класса
from abc import ABC, abstractmethod


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Ravioli(Prototype):
    def __init__(self, type_of_paste, sauce, filling):
        self.type_of_paste = type_of_paste
        self.sauce = sauce
        self.filling = filling

    def clone(self):
        return Ravioli(self.type_of_paste, self.sauce, self.filling)

    def __str__(self):
        ravioli = '\033[32mРавиоли в ассортименте:\033[0m' + '\n'
        ravioli += '\033[4mТип пасты:\033[0m ' + str(self.type_of_paste) + '\n'
        ravioli += '\033[4mСоус:\033[0m ' + str(self.sauce) + '\n'
        ravioli += '\033[4mНачинка:\033[0m ' + str(self.filling) + '\n'
        return ravioli


ravioli_shrimps = Ravioli('паста с начинкой',
                          'соус песто из базилика, оливкового масла, орехов и чеснока',
                          'креветки')
print(ravioli_shrimps)
ravioli_meat = ravioli_shrimps.clone()
ravioli_meat.filling = 'мясной фарш и сыр пармезан'
print(ravioli_meat)
ravioli_mushrooms = ravioli_meat.clone()
ravioli_mushrooms.filling = 'грибы'
print(ravioli_mushrooms)
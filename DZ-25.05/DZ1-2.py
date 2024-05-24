# Задание 1. Создайте реализацию паттерна Builder. Протестируйте работу созданного класса.
# Задание 2. Создайте приложение для приготовления пасты. Приложение должно уметь создавать минимум три вида пасты.
# Классы различной пасты должны иметь следующие методы:
# ■ Тип пасты;
# ■ Соус;
# ■ Начинка;
# ■ Добавки.
# Для реализации используйте порождающие паттерны.

class Pasta:
    def __init__(self):
        self.types_of_paste = []
        self.sauces = []
        self.fillings = []
        self.supplements = []

    def __str__(self):
        ingredients = ''
        ingredients += '\033[4mТип пасты:\033[0m '
        for type_of_paste in self.types_of_paste:
            ingredients += str(type_of_paste) + '\n'
        ingredients += '\033[4mСоус:\033[0m '
        for sauce in self.sauces:
            ingredients += str(sauce) + '\n'
        ingredients += '\033[4mНачинка:\033[0m '
        for filling in self.fillings:
            ingredients += str(filling) + '\n'
        ingredients += '\033[4mДобавки:\033[0m '
        for supplement in self.supplements:
            ingredients += str(supplement) + '\n'
        return ingredients


class Short_pasta:
    def __str__(self):
        return 'короткая паста (фузилли или пенне)'


class Long_pasta:
    def __str__(self):
        return 'длинная паста (спагетти, букатини, феттуччини, паппарделле или тальятелле)'


class Curly_pasta:
    def __str__(self):
        return 'фигурная паста (фарфалле)'


class Stuffed_pasta:
    def __str__(self):
        return 'паста с начинкой (равиоли)'


class Bolognese_sauce:
    def __str__(self):
        return 'соус болоньезе из мясного фарша и протертых помидоров'


class Pesto_sauce:
    def __str__(self):
        return 'соус песто из базилика, оливкового масла, орехов и чеснока'


class Carbonara_sauce:
    def __str__(self):
        return 'соус карбонара из бекона, яиц, сливок и твердого сыра'


class Meat_and_cheese:
    def __str__(self):
        return 'мясной фарш и сыр пармезан'


class Shrimps:
    def __str__(self):
        return 'креветки'


class No_filling:
    def __str__(self):
        return 'без начинки'


class Black_pepper:
    def __str__(self):
        return 'черный перец'


class Mushrooms:
    def __str__(self):
        return 'грибы'


class No_additives:
    def __str__(self):
        return 'без добавок'


from abc import ABC, abstractmethod


class Cooking_pasta(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def types_of_pasta(self):
        pass

    @abstractmethod
    def sauces(self):
        pass

    @abstractmethod
    def fillings(self):
        pass

    @abstractmethod
    def supplements(self):
        pass


class Pasta_carbonara(Cooking_pasta):
    def __init__(self):
        self.pasta = Pasta()

    def reset(self):
        self.pasta = Pasta()

    def get_pasta(self):
        print('\033[32mПаста "Карбонара":\033[0m')
        return self.pasta

    def types_of_pasta(self):
        self.pasta.types_of_paste.append(Long_pasta())

    def sauces(self):
        self.pasta.sauces.append(Carbonara_sauce())

    def fillings(self):
        self.pasta.fillings.append(No_filling())

    def supplements(self):
        self.pasta.supplements.append(Mushrooms())


class Ravioli_with_meat(Cooking_pasta):
    def __init__(self):
        self.pasta = Pasta()

    def reset(self):
        self.pasta = Pasta()

    def get_pasta(self):
        print('\033[32mРавиоли с мясом:\033[0m')
        return self.pasta

    def types_of_pasta(self):
        self.pasta.types_of_paste.append(Stuffed_pasta())

    def sauces(self):
        self.pasta.sauces.append(Bolognese_sauce())

    def fillings(self):
        self.pasta.fillings.append(Meat_and_cheese())

    def supplements(self):
        self.pasta.supplements.append(No_additives())


class Ravioli_with_shrimps(Cooking_pasta):
    def __init__(self):
        self.pasta = Pasta()

    def reset(self):
        self.pasta = Pasta()

    def get_pasta(self):
        print('\033[32mРавиоли с креветками:\033[0m')
        return self.pasta

    def types_of_pasta(self):
        self.pasta.types_of_paste.append(Stuffed_pasta())

    def sauces(self):
        self.pasta.sauces.append(Pesto_sauce())

    def fillings(self):
        self.pasta.fillings.append(Shrimps())

    def supplements(self):
        self.pasta.supplements.append(No_additives())


class Pasta_bolognese(Cooking_pasta):
    def __init__(self):
        self.pasta = Pasta()

    def reset(self):
        self.pasta = Pasta()

    def get_pasta(self):
        print('\033[32mПаста "Болоньезе":\033[0m')
        return self.pasta

    def types_of_pasta(self):
        self.pasta.types_of_paste.append(Curly_pasta())

    def sauces(self):
        self.pasta.sauces.append(Bolognese_sauce())

    def fillings(self):
        self.pasta.fillings.append(No_filling())

    def supplements(self):
        self.pasta.supplements.append(Mushrooms())


class Pasta_pesto(Cooking_pasta):
    def __init__(self):
        self.pasta = Pasta()

    def reset(self):
        self.pasta = Pasta()

    def get_pasta(self):
        print('\033[32mПаста "Песто":\033[0m')
        return self.pasta

    def types_of_pasta(self):
        self.pasta.types_of_paste.append(Short_pasta())

    def sauces(self):
        self.pasta.sauces.append(Pesto_sauce())

    def fillings(self):
        self.pasta.fillings.append(No_filling())

    def supplements(self):
        self.pasta.supplements.append(Black_pepper())


while True:
    print('Выберите блюдо из меню:')
    print('''\t1 - Паста "Карбонара"
    2 - Паста "Болоньезе"
    3 - Равиоли с мясом
    4 - Равиоли с креветками
    5 - Паста "Песто"
    6 - Спасибо! Не хочу есть''')
    menu = input('Введите порядковый номер: ')
    if menu == '6':
        print('\033[31mДо свидания!')
        break
    elif menu == '1':
        pasta = Pasta_carbonara()
        pasta.types_of_pasta()
        pasta.sauces()
        pasta.fillings()
        pasta.supplements()
        print('\nВы выбрали:')
        print(pasta.get_pasta())
    elif menu == '2':
        pasta = Pasta_bolognese()
        pasta.types_of_pasta()
        pasta.sauces()
        pasta.fillings()
        pasta.supplements()
        print('\nВы выбрали:')
        print(pasta.get_pasta())
    elif menu == '3':
        pasta = Ravioli_with_meat()
        pasta.types_of_pasta()
        pasta.sauces()
        pasta.fillings()
        pasta.supplements()
        print('\nВы выбрали:')
        print(pasta.get_pasta())
    elif menu == '4':
        pasta = Ravioli_with_shrimps()
        pasta.types_of_pasta()
        pasta.sauces()
        pasta.fillings()
        pasta.supplements()
        print('\nВы выбрали:')
        print(pasta.get_pasta())
    elif menu == '5':
        pasta = Pasta_pesto()
        pasta.types_of_pasta()
        pasta.sauces()
        pasta.fillings()
        pasta.supplements()
        print('\nВы выбрали:')
        print(pasta.get_pasta())
    else:
        print('\033[31mТакого блюда нет в меню! Выберите ещё раз!\033[0m')
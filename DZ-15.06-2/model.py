import json


class Shoe:
    def __init__(self, shoe_type, style, color, price, manufacturer, size):
        self.shoe_type = shoe_type
        self.style = style
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

    def __str__(self):
        return (f'Обувь {self.shoe_type}: {self.style}, '
                f'цвет - {self.color}, '
                f'производитель - {self.manufacturer}, '
                f'размер - {self.size}, '
                f'цена: {self.price} руб.')


class Model:
    def __init__(self):
        self.__shoes = {}
        try:
            self.data = json.load(open('shoes.txt', 'r', encoding='utf-8'))
            for shoe in self.data.values():
                self.__shoes[f'{shoe.style} {shoe.shoe_type} {shoe.color} {shoe.size}'] = Shoe(*shoe.values())
        except json.JSONDecodeError as e:
            print(f'Неверный формат данных в файле shoes.txt: {e}')
        except FileNotFoundError:
            print('Файл не найден, создается новый файл с пустым словарем.')
            with open('shoes.txt', 'w') as file:
                file.write("{}")

    @property
    def shoes(self):
        return self.__shoes

    def save_shoes(self):
        dict_shoes = {s.style: s.__dict__ for s in self.__shoes.values()}
        json.dump(dict_shoes, open('shoes.txt', 'w'))

    def add_new_shoe(self, shoe_data):
        new_shoe = Shoe(*shoe_data.values())
        self.__shoes[(f'{new_shoe.style} {new_shoe.shoe_type} {new_shoe.color} {new_shoe.size}')] = new_shoe
        self.save_shoes()
        print('Обувь успешно добавлена')

    def search_shoes(self, criteria):
        shoes = []
        for shoe in self.__shoes.values():
            props = shoe.__dict__
            for crit in criteria:
                if shoe in shoes:
                    break
                for prop in props.values():
                    if crit.lower() in prop.lower():
                        shoes.append(shoe)
                        break
        return shoes

    def delete_shoes(self, shoes):
        if len(shoes) == 0:
            return 'Обуви нет!'
        elif len(shoes) == 1:
            shoe = shoes[0]
            key = f'{shoe.style} {shoe.shoe_type} {shoe.color} {shoe.size}'
            self.__shoes.pop(key)
            self.save_shoes()
            return 'Пара обуви удалена!'
        else:
            return 'Слишком много обуви!'

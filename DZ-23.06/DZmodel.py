from abc import ABC, abstractmethod
import time


class Hot_dog:
    def __init__(self, name, bun, toppings, sauces, price):
        self.name = name
        self.bun = bun
        self.toppings = toppings
        self.sauces = sauces
        self.price = price

    def __str__(self):
        return (f'Хот-Дог "{self.name}".\n'
                f'Основа - {self.bun}.\n'
                f'Начинка: {", ".join(self.toppings)},\n'
                f'а также {", ".join(self.sauces)}.\n'
                f'Стоимость: {self.price} руб.\n')


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} - {self.price}'


class Buns:
    data = {'булка': 40,
            'багет': 45,
            'лаваш': 30}
    buns = {}

    @staticmethod
    def init_buns():
        n = 1
        for key, value in Buns.data.items():
            if Food_supplies.quantity_buns[key] > 0:
                Buns.buns[n] = Product(key, value)
                n += 1
        return ''.join([f'{str(n)}. {product} руб.\n' for n, product in Buns.buns.items()])

    def choice_buns(self):
        n = 1
        for key, value in Buns.data.items():
            if Food_supplies.quantity_buns[key] > 0:
                Buns.buns[str(n)] = Product(key, value)
                n += 1
        return Buns.buns

    def clean_buns(self):
        Buns.buns = {}
        return Buns.buns


class Toppings:
    data = {'сосиска': 60,
            'баварская колбаска': 80,
            'маринованный лук': 30,
            'ялтинский лук': 35,
            'соленый огурец': 30,
            'квашенная капуста': 25,
            'свежий огурец': 40,
            'свежий помидор': 40}
    toppings = {}

    @staticmethod
    def init_toppings():
        for n, (key, value) in enumerate(Toppings.data.items(), 1):
            Toppings.toppings[n] = str(Product(key, value))
        return ''.join([f'{str(n)}. {product} руб.\n' for n, product in Toppings.toppings.items()])

    def choice_toppings(self):
        for n, (key, value) in enumerate(Toppings.data.items(), 1):
            Toppings.toppings[str(n)] = Product(key, value)
        return Toppings.toppings

    def clean_toppings(self):
        toppings = {}
        return toppings


class Sauces:
    data = {'майонез': 20,
            'кетчуп': 15,
            'горчица': 15}
    sauces = {}

    @staticmethod
    def init_sauces():
        for n, (key, value) in enumerate(Sauces.data.items(), 1):
            Sauces.sauces[n] = str(Product(key, value))
        return ''.join([f'{str(n)}. {product} руб.\n' for n, product in Sauces.sauces.items()])

    def choice_sauces(self):
        for n, (key, value) in enumerate(Sauces.data.items(), 1):
            Sauces.sauces[str(n)] = Product(key, value)
        return Sauces.sauces

    def clean_sauces(self):
        sauces = {}
        return sauces


class Order:
    def __init__(self):
        self.hot_dogs = []
        self.price = 0
        self.discount = None
        self.payment_method = None

    def __str__(self):
        return ('\n'.join([f'{n}. {str(hot_dog)}' for n, hot_dog in enumerate(self.hot_dogs, 1)]) +
                f'\nОбщая стоимость: {self.price} руб.\n{str(self.discount)}. ' +
                f'Итого к оплате: {self.price * self.discount.discount} руб.\n')

    def init_payment_method(self):
        payment_method = self.payment_method.payment
        return str(payment_method)

    def add_hot_dog(self, hot_dog):
        self.hot_dogs.append(hot_dog)
        return self.hot_dogs

    def delete_hot_dog(self, index):
        self.hot_dogs.pop(index)
        return self.hot_dogs

    def add_price(self, hot_dog_price):
        self.price += hot_dog_price
        return self.price

    def delete_price(self, hot_dog_price):
        self.price -= hot_dog_price
        return self.price

    def add_discount(self, discount_method):
        self.discount = discount_method
        return self.discount

    def add_payment_method(self, payment_method):
        self.payment_method = payment_method
        return self.payment_method

    def clean_order(self):
        self.hot_dogs = []
        self.price = 0
        self.discount = None
        self.payment_method = None
        return self.hot_dogs, self.price, self.discount, self.payment_method


class Sales:
    sold_hot_dogs = {}
    revenue = 0
    profit = 0

    def init_sold_hot_dogs(self):
        return ('Продано хот-догов:\n\t' +
                '\t'.join([f'Хот-дог "{key}": {value} шт.\n' for key, value in self.sold_hot_dogs.items()]))

    def init_revenue(self):
        return f'Общая выручка: {self.revenue} руб.'

    def init_profit(self):
        return f'"Чистая" прибыль от продаж: {self.profit} руб.'

    def add_hot_dog_to_sales(self, hot_dog):
        if hot_dog in self.sold_hot_dogs.keys():
            self.sold_hot_dogs[hot_dog] += 1
            return self.sold_hot_dogs
        self.sold_hot_dogs[hot_dog] = 1
        return self.sold_hot_dogs

    def add_revenue(self, price):
        self.revenue += price
        return self.revenue

    def add_profit(self, price, all_price):
        self.profit += all_price / 2 - (all_price - price)
        return self.profit


class Food_supplies:
    quantity_buns = {'булка': 5,
                     'багет': 2,
                     'лаваш': 2}
    quantity_toppings = {'сосиска': 15,
                         'баварская колбаска': 5,
                         'маринованный лук': 5,
                         'ялтинский лук': 5,
                         'соленый огурец': 5,
                         'квашенная капуста': 5,
                         'свежий огурец': 5,
                         'свежий помидор': 5}
    quantity_sauces = {'майонез': 10,
                       'кетчуп': 10,
                       'горчица': 10}

    @staticmethod
    def init_products():
        return ('1. Наличие основы для хот-догов на складе (количество порций):\n\t' +
                '\t'.join([f'{key} = {value} шт.\n' for key, value in Food_supplies.quantity_buns.items()]) +
                '2. Наличие начинки для хот-догов на складе (количество порций):\n\t' +
                '\t'.join([f'{key} = {value} шт.\n' for key, value in Food_supplies.quantity_toppings.items()]) +
                '3. Наличие соусов для хот-догов на складе (количество порций):\n\t' +
                '\t'.join([f'{key} = {value} шт.\n' for key, value in Food_supplies.quantity_sauces.items()]))

    def init_buns(self):
        return '\n'.join([f'{str(n)}. {Product(key, value)} шт.'
                          for n, (key, value) in enumerate(Food_supplies.quantity_buns.items(), 1)])

    def choice_buns(self):
        buns = {}
        for n, (key, value) in enumerate(Food_supplies.quantity_buns.items(), 1):
            buns[str(n)] = Product(key, value)
        return buns


    def init_toppings(self):
        return '\n'.join([f'{str(n)}. {Product(key, value)} шт.'
                          for n, (key, value) in enumerate(Food_supplies.quantity_toppings.items(), 1)])

    def choice_toppings(self):
        toppings = {}
        for n, (key, value) in enumerate(Food_supplies.quantity_toppings.items(), 1):
            toppings[str(n)] = Product(key, value)
        return toppings

    def init_sauces(self):
        return '\n'.join([f'{str(n)}. {Product(key, value)} шт.'
                          for n, (key, value) in enumerate(Food_supplies.quantity_sauces.items(), 1)])

    def choice_sauces(self):
        sauces = {}
        for n, (key, value) in enumerate(Food_supplies.quantity_sauces.items(), 1):
            sauces[str(n)] = Product(key, value)
        return sauces

    def minus_product(self, products, name):
        if products[name] > 0:
            products[name] -= 1
        return products

    def plus_product(self, products, name, quantity):
        products[name] += quantity
        return products


class Payment(ABC):
    @abstractmethod
    def payment(self):
        pass


class Cash_payment(Payment):
    @property
    def payment(self):
        return 'Подготовьте необходимую сумму наличными для оплаты заказа при получении'


class Payment_by_card(Payment):
    @property
    def payment(self):
        return 'Приложите карту к платежному терминалу для оплаты заказа'


class Discount(ABC):
    @abstractmethod
    def discount(self):
        pass


class No_discount(Discount):
    @property
    def discount(self):
        return 1

    def __str__(self):
        return 'Скидка не предоставляется'


class Discount_five_percent(Discount):
    @property
    def discount(self):
        return 0.95

    def __str__(self):
        return 'Скидка составляет 5%'


class Discount_ten_percent(Discount):
    @property
    def discount(self):
        return 0.9

    def __str__(self):
        return 'Скидка составляет 10%'


class Discount_twenty_percent(Discount):
    @property
    def discount(self):
        return 0.8

    def __str__(self):
        return 'Скидка составляет 20%'


class Logger:
    @staticmethod
    def log(message):
        with open('log.txt', 'a') as log_file:
            log_file.write(f'Заказ от {time.strftime("%d-%m-%Y", time.localtime(time.time()))} '
                           f'{time.strftime("%H:%M:%S", time.localtime(time.time()))}:'
                           f'\n{message}\n')


class Recipes:
    @staticmethod
    def classic():
        name = 'Классический'
        bun = 'булка'
        toppings = ['сосиска', 'ялтинский лук', 'свежий помидор', 'свежий огурец']
        sauces = ['майонез', 'кетчуп', 'горчица']
        price = (Buns.data['булка'] + Toppings.data['сосиска'] + Toppings.data['ялтинский лук']
                 + Toppings.data['свежий помидор'] + Toppings.data['свежий огурец']
                 + Sauces.data['майонез'] + Sauces.data['кетчуп'] + Sauces.data['горчица'])
        if Food_supplies().quantity_buns['булка'] > 0 \
                and Food_supplies().quantity_toppings['сосиска'] > 0 \
                and Food_supplies().quantity_toppings['ялтинский лук'] > 0 \
                and Food_supplies().quantity_toppings['свежий помидор'] > 0 \
                and Food_supplies().quantity_toppings['свежий огурец'] > 0 \
                and Food_supplies().quantity_sauces['майонез'] > 0 \
                and Food_supplies().quantity_sauces['кетчуп'] > 0 \
                and Food_supplies().quantity_sauces['горчица'] > 0:
            return Hot_dog(name, bun, toppings, sauces, price)
        return None

    @staticmethod
    def french():
        name = 'Французский'
        bun = 'багет'
        toppings = ['сосиска']
        sauces = ['майонез', 'кетчуп', 'горчица']
        price = (Buns.data['багет'] + Toppings.data['сосиска'] + Sauces.data['майонез']
                 + Sauces.data['кетчуп'] + Sauces.data['горчица'])
        if Food_supplies().quantity_buns['багет'] > 0 \
                and Food_supplies().quantity_toppings['сосиска'] > 0 \
                and Food_supplies().quantity_sauces['майонез'] > 0 \
                and Food_supplies().quantity_sauces['кетчуп'] > 0 \
                and Food_supplies().quantity_sauces['горчица'] > 0:
            return Hot_dog(name, bun, toppings, sauces, price)

    @staticmethod
    def in_pita_bread():
        name = 'В лаваше'
        bun = 'лаваш'
        toppings = ['баварская колбаска', 'маринованный лук', 'соленый огурец', 'квашенная капуста']
        sauces = ['майонез', 'горчица']
        price = (Buns.data['лаваш'] + Toppings.data['баварская колбаска'] + Toppings.data['маринованный лук']
                 + Toppings.data['соленый огурец'] + Toppings.data['квашенная капуста']
                 + Sauces.data['майонез'] + Sauces.data['горчица'])
        if Food_supplies().quantity_buns['лаваш'] > 0 \
                and Food_supplies().quantity_toppings['баварская колбаска'] > 0 \
                and Food_supplies().quantity_toppings['маринованный лук'] > 0 \
                and Food_supplies().quantity_toppings['соленый огурец'] > 0 \
                and Food_supplies().quantity_toppings['квашенная капуста'] > 0 \
                and Food_supplies().quantity_sauces['майонез'] > 0 \
                and Food_supplies().quantity_sauces['горчица'] > 0:
            return Hot_dog(name, bun, toppings, sauces, price)

    def show_all_recipes(self):
        all_recipes = {}
        n = 1
        if Recipes.classic() != None:
            all_recipes[n] = Recipes.classic()
            n += 1
        if Recipes.french() != None:
            all_recipes[n] = Recipes.french()
            n += 1
        if Recipes.in_pita_bread() != None:
            all_recipes[n] = Recipes.in_pita_bread()
        return '\n'.join([f'{key}. {value}' for key, value in all_recipes.items()])

    def choice_recipes(self):
        all_recipes = {}
        n = 1
        if Recipes.classic() != None:
            all_recipes[str(n)] = Recipes.classic()
            n += 1
        if Recipes.french() != None:
            all_recipes[str(n)] = Recipes.french()
            n += 1
        if Recipes.in_pita_bread() != None:
            all_recipes[str(n)] = Recipes.in_pita_bread()
        return all_recipes


class Model:
    def __init__(self):
        self.buns = Buns()
        self.toppings = Toppings()
        self.sauces = Sauces()
        self.food_supplies = Food_supplies()
        self.recipes = Recipes()
        self.logger = Logger()
        self.bun = ''
        self.topping = []
        self.sauce = []
        self.payment_method = None
        self.discount_method = None
        self.sales = Sales()
        self.order = Order()

    def show_recipes(self):
        return self.recipes.show_all_recipes()

    def choice_recipe(self):
        return self.recipes.choice_recipes()

    def show_buns(self):
        return self.buns.init_buns()

    def show_quantity_buns(self):
        return self.food_supplies.init_buns()

    def choice_quantity_buns(self):
        return self.food_supplies.choice_buns()

    def choice_bun(self):
        return self.buns.choice_buns()

    def show_toppings(self):
        return self.toppings.init_toppings()

    def show_quantity_toppings(self):
        return self.food_supplies.init_toppings()

    def choice_quantity_toppings(self):
        return self.food_supplies.choice_toppings()

    def choice_toppings(self):
        return self.toppings.choice_toppings()

    def show_sauces(self):
        return self.sauces.init_sauces()

    def show_quantity_sauces(self):
        return self.food_supplies.init_sauces()

    def choice_quantity_sauces(self):
        return self.food_supplies.choice_sauces()

    def choice_sauces(self):
        return self.sauces.choice_sauces()

    def add_topping(self, topping):
        self.topping.append(topping)
        return self.topping

    def add_sauce(self, sauce):
        self.sauce.append(sauce)
        return self.sauce

    def products(self):
        return self.food_supplies.init_products()

    @staticmethod
    def price_increase(price, plus_price):
        price += plus_price
        return price

    def clean_hot_dog(self):
        self.buns.clean_buns()
        self.toppings.clean_toppings()
        self.sauces.clean_sauces()
        self.bun = ''
        self.topping = []
        self.sauce = []
        return self.buns, self.toppings, self.sauces, self.bun, self.topping, self.sauce

    def collect_hot_dog(self, name, bun, toppings, sauces, price):
        hot_dog = Hot_dog(name, bun, toppings, sauces, price)
        return hot_dog

    def add_new_hot_dog(self, hot_dog):
        self.order.add_hot_dog(hot_dog)
        self.food_supplies.minus_product(self.food_supplies.quantity_buns, hot_dog.bun)
        for topping in hot_dog.toppings:
            self.food_supplies.minus_product(self.food_supplies.quantity_toppings, topping)
        for sauce in hot_dog.sauces:
            self.food_supplies.minus_product(self.food_supplies.quantity_sauces, sauce)
        self.order.add_price(hot_dog.price)
        self.order.add_discount(self.set_discount_method(self.discount_calculation()))
        return self.order, self.food_supplies

    def delete_hot_dog(self, choice):
        hot_dog = self.order.hot_dogs[choice - 1]
        self.food_supplies.plus_product(self.food_supplies.quantity_buns, hot_dog.bun, 1)
        for topping in hot_dog.toppings:
            self.food_supplies.plus_product(self.food_supplies.quantity_toppings, topping, 1)
        for sauce in hot_dog.sauces:
            self.food_supplies.plus_product(self.food_supplies.quantity_sauces, sauce, 1)
        self.order.delete_price(hot_dog.price)
        self.order.delete_hot_dog(choice - 1)
        self.order.add_discount(self.set_discount_method(self.discount_calculation()))
        return self.order, self.food_supplies

    def add_product(self, products, name, quantity):
        self.food_supplies.plus_product(products, name, quantity)
        return self.food_supplies

    def new_order(self):
        return self.order.clean_order()

    def show_order(self):
        if len(self.order.hot_dogs) > 0:
            return str(self.order)
        else:
            return 'Вы ещё ничего не заказывали!'

    def hot_dog_list(self):
        return [str(n) for n in range(1, len(self.order.hot_dogs) + 1)]

    def cancel_order(self):
        for n in range(len(self.order.hot_dogs), 0, -1):
            self.delete_hot_dog(n)
        return self.food_supplies

    def choice_payment_method(self, method):
        if method == 'наличные':
            payment_method = Cash_payment()
            return payment_method
        elif method == 'карта':
            payment_method = Payment_by_card()
            return payment_method

    def set_payment_method(self, payment_method):
        self.payment_method = payment_method
        self.order.add_payment_method(payment_method)
        return self.order

    def show_payment_method(self):
        return self.order.init_payment_method()

    def discount_calculation(self):
        if 2 < len(self.order.hot_dogs) < 10:
            discount_method = Discount_five_percent()
            return discount_method
        elif 9 < len(self.order.hot_dogs) < 20:
            discount_method = Discount_ten_percent()
            return discount_method
        elif len(self.order.hot_dogs) > 19:
            discount_method = Discount_twenty_percent()
            return discount_method
        else:
            discount_method = No_discount()
            return discount_method

    def set_discount_method(self, discount_method):
        self.discount_method = discount_method
        return self.discount_method

    def get_sold_hot_dogs(self):
        return self.sales.init_sold_hot_dogs()

    def get_revenue(self):
        return self.sales.init_revenue()

    def get_profit(self):
        return self.sales.init_profit()

    def finish_the_order(self):
        for hot_dog in self.order.hot_dogs:
            self.sales.add_hot_dog_to_sales(hot_dog.name)
        price = self.order.price * self.order.discount.discount
        self.sales.add_revenue(price)
        all_price = self.order.price
        self.sales.add_profit(price, all_price)
        return self.sales

    def add_message(self):
        message = str(self.order)
        self.logger.log(message)
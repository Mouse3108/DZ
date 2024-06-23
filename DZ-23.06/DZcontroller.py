from DZview import View
from DZmodel import Model


class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model()

    def run(self):
        while True:
            user = self.view.main_menu()
            if user == '3':
                self.view.exit_menu()
                break
            elif user == '1':
                password = self.view.admin_password()
                if password == '12345':
                    while True:
                        command = self.view.admin_menu()
                        if command == '6':
                            break
                        elif command in ['1', '2', '3', '4', '5']:
                            self.admin_actions(command)
                        else:
                            self.view.print_error(command)
                else:
                    self.view.print_error(password)
                    continue
            elif user == '2':
                self.model.new_order()
                while True:
                    command = self.view.buyer_menu()
                    if command == '6':
                        self.model.cancel_order()
                        break
                    elif command == '5':
                        while True:
                            choice = self.view.payment_method()
                            if choice == '1':
                                self.model.set_payment_method(self.model.choice_payment_method('наличные'))
                                self.view.show_info(self.model.show_order())
                                self.view.show_info(self.model.show_payment_method())
                                break
                            if choice == '2':
                                self.model.set_payment_method(self.model.choice_payment_method('карта'))
                                self.view.show_info(self.model.show_order())
                                self.view.show_info(self.model.show_payment_method())
                                break
                            else:
                                self.view.print_error(choice)
                                continue
                        self.model.finish_the_order()
                        self.model.add_message()
                        break
                    elif command in ['1', '2', '3', '4', '5']:
                        self.buyer_actions(command)
                    else:
                        self.view.print_error(command)
            else:
                self.view.print_error(user)

    def admin_actions(self, command):
        if command == '1':
            self.view.show_info(self.model.get_sold_hot_dogs())
        elif command == '2':
            self.view.show_info(self.model.get_revenue())
        elif command == '3':
            self.view.show_info(self.model.get_profit())
        elif command == '4':
            self.view.show_info(self.model.products())
        elif command == '5':
            while True:
                self.view.show_info(self.model.products())
                choice = self.view.choice()
                if choice == '':
                    break
                elif choice in ['1', '2', '3']:
                    self.add_product(choice)
                else:
                    self.view.print_error(choice)

    def buyer_actions(self, command):
        if command == '1':
            while True:
                self.view.show_info(self.model.show_recipes())
                choice = self.view.choice()
                if choice == '':
                    break
                elif choice in self.model.choice_recipe():
                    hot_dog = self.model.choice_recipe()[choice]
                    self.model.add_new_hot_dog(hot_dog)
                else:
                    self.view.print_error(choice)
        elif command == '2':
            price = self.model.price_increase(0, 0)
            bun = self.model.bun
            topping = self.model.topping
            souse = self.model.sauce
            show_buns = self.model.show_buns()
            self.view.show_info(show_buns)
            while True:
                choice = self.view.add_topping_and_souse()
                if not choice:
                    self.view.print_error('пустая строка')
                    continue
                elif choice not in self.model.choice_bun():
                    self.view.print_error(choice)
                    continue
                else:
                    product = self.model.choice_bun()[choice]
                    bun += product.name
                    price = self.model.price_increase(price, product.price)
                    break
            show_toppings = self.model.show_toppings()
            self.view.show_info(show_toppings)
            while True:
                choice = self.view.choice()
                if choice == '':
                    break
                elif choice in self.model.choice_toppings():
                    product = self.model.choice_toppings()[choice]
                    if product.name in topping:
                        self.view.error_topping_and_souse(product.name)
                        continue
                    topping = self.model.add_topping(product.name)
                    price = self.model.price_increase(price, product.price)
                else:
                    self.view.print_error(choice)
            show_sauces = self.model.show_sauces()
            self.view.show_info(show_sauces)
            while True:
                choice = self.view.choice()
                if choice == '':
                    break
                elif choice in self.model.choice_sauces():
                    product = self.model.choice_sauces()[choice]
                    if product.name in souse:
                        self.view.error_topping_and_souse(product.name)
                        continue
                    souse = self.model.add_sauce(product.name)
                    price = self.model.price_increase(price, product.price)
                else:
                    self.view.print_error(choice)
            hot_dog = self.model.collect_hot_dog('Свой рецепт', bun, topping, souse, price)
            self.model.add_new_hot_dog(hot_dog)
            self.model.clean_hot_dog()
        elif command == '3':
            self.view.show_info(self.model.show_order())
        elif command == '4':
            self.view.show_info(self.model.show_order())
            while True:
                choice = self.view.choice_delete()
                if choice == '':
                    break
                elif choice in self.model.hot_dog_list():
                    self.model.delete_hot_dog(int(choice))
                    break
                else:
                    self.view.print_error(choice)

    def add_product(self, choice):
        if choice == '1':
            self.view.show_info(self.model.show_quantity_buns())
            product = self.view.add_topping_and_souse()
            if product in self.model.choice_quantity_buns():
                name = self.model.choice_quantity_buns()[product]
                quantity = self.view.add_product()
                if quantity.isdigit():
                    self.model.add_product(self.model.food_supplies.quantity_buns, name.name, int(quantity))
                else:
                    self.view.print_error(quantity)
            else:
                self.view.print_error(product)
        if choice == '2':
            self.view.show_info(self.model.show_quantity_toppings())
            product = self.view.add_topping_and_souse()
            if product in self.model.choice_quantity_toppings():
                name = self.model.choice_quantity_toppings()[product]
                quantity = self.view.add_product()
                if quantity.isdigit():
                    self.model.add_product(self.model.food_supplies.quantity_toppings, name.name, int(quantity))
                else:
                    self.view.print_error(quantity)
            else:
                self.view.print_error(product)
        if choice == '3':
            self.view.show_info(self.model.show_quantity_sauces())
            product = self.view.add_topping_and_souse()
            if product in self.model.choice_quantity_sauces():
                name = self.model.choice_quantity_sauces()[product]
                quantity = self.view.add_product()
                if quantity.isdigit():
                    self.model.add_product(self.model.food_supplies.quantity_sauces, name.name, int(quantity))
                else:
                    self.view.print_error(quantity)
            else:
                self.view.print_error(product)

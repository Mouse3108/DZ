from model import Model
from view import ShoeView


class ShoeController:
    def __init__(self):
        self.view = ShoeView()
        self.model = Model()

    def run(self):
        query = None
        while query != '5':
            query = self.view.menu()
            self.process_user_answer(query)

    def process_user_answer(self, query):
        if query == "1":
            shoe_data = self.view.new_shoe()
            self.model.add_new_shoe(shoe_data)
        elif query == "2":
            all_shoes = self.model.shoes
            self.view.print_shoes(all_shoes)
        elif query == "3":
            criteria = self.view.find_shoes()
            shoes = self.model.search_shoes(criteria)
            self.view.print_shoes(shoes)
        elif query == "4":
            shoe_name = self.view.delete_shoe()
            shoes = self.model.search_shoes([shoe_name])
            result = self.model.delete_shoes(shoes)
            if result == 'Слишком много обуви!':
                self.view.print_shoes(shoes)
                number = self.view.delete_context()
                try:
                    result = self.model.delete_shoes([shoes[number - 1]])
                except IndexError:
                    result = 'Этой обуви нет в списке!'
            self.view.return_delete_result(result)
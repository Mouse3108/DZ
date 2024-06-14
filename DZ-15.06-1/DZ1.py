# Задание 1.
# Создайте реализацию паттерна Command. Протестируйте работу созданного класса.
from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, command, action):
        self.command = command
        self.action = action

    @abstractmethod
    def perform_an_action(self):
        pass


class TV(Command):
    def perform_an_action(self):
        if self.command == 'Включить':
            self.action.turn_on_the_TV()
        elif self.command == 'Выключить':
            self.action.turn_off_the_TV()
        elif self.command == 'Сделать громче':
            self.action.increase_the_volume()
        elif self.command == 'Сделать тише':
            self.action.lower_the_volume()
        elif self.command == 'Предыдущий канал':
            self.action.previous_channel()
        elif self.command == 'Следующий канал':
            self.action.next_channel()
        else:
            self.action.error()


class Remote_controller:
    def turn_on_the_TV(self):
        print('* Телевизор включен')

    def turn_off_the_TV(self):
        print('* Телевизор выключен')

    def increase_the_volume(self):
        print('* Громкость увеличена')

    def lower_the_volume(self):
        print('* Громкость уменьшена')

    def previous_channel(self):
        print('* Включен предыдущий канал')

    def next_channel(self):
        print('* Включен следующий канал')

    def error(self):
        print('* На пульте не предусмотрено такое действие!')


class User:
    def __init__(self, command_user):
        self.command_user = command_user

    def execute(self):
        self.command_user.perform_an_action()


User(TV('Включить', Remote_controller())).execute()
User(TV('Сделать громче', Remote_controller())).execute()
User(TV('Следующий канал', Remote_controller())).execute()
User(TV('Предыдущий канал', Remote_controller())).execute()
User(TV('Сделать тише', Remote_controller())).execute()
User(TV('Сделать что-нибудь', Remote_controller())).execute()
User(TV('Выключить', Remote_controller())).execute()
# Создать БД “онлайн-магазина” с таблицами users, orders, products
# (таблицы можно создать через СУБД и наполнить их можно там же) и требования:
# a. Пользователи могут регистрироваться, входить в систему и изменять свои данные.
# b. Пользователи могут просматривать каталог товаров, добавлять их в корзину и оформлять заказы.

import sqlite3

con = sqlite3.connect('DZ.db')
cursor = con.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    номер_продукта INTEGER PRIMARY KEY,
    название TEXT NOT NULL,
    цена TEXT NOT NULL,
    количество INTEGER NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    номер_клиента INTEGER PRIMARY KEY,
    имя TEXT NOT NULL,
    пароль TEXT NOT NULL CHECK (length(пароль) >= 5),
    адрес TEXT NOT NULL,
    телефон TEXT UNIQUE
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    номер_заказа INTEGER NOT NULL,
    дата_заказа TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    продукт INTEGER NOT NULL,
    клиент INTEGER NOT NULL,
    стоимость TEXT NOT NULL,
    FOREIGN KEY (продукт) REFERENCES products(номер_продукта),
    FOREIGN KEY (клиент) REFERENCES users(номер_клиента)
);
''')

con.close()

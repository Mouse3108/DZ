# Создать таблицу "Продукты" с полями: Название, Цена, Количество.
# Создать таблицу "Клиенты" с полями: Имя, Фамилия, Адрес, Телефон.
# Создать таблицу "Заказы" с полями: Номер заказа, Дата заказа, Сумма заказа + номер продукта и номер клиента.

import sqlite3

con = sqlite3.connect('DZ.db')
cursor = con.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Продукты (
    номер INTEGER PRIMARY KEY,
    название TEXT NOT NULL,
    цена TEXT NOT NULL,
    количество INTEGER NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Клиенты (
    номер INTEGER PRIMARY KEY,
    имя TEXT NOT NULL,
    фамилия TEXT NOT NULL,
    адрес TEXT NOT NULL,
    телефон TEXT UNIQUE
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Заказы (
    номер INTEGER PRIMARY KEY,
    дата_заказа TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    продукт INTEGER NOT NULL,
    клиент INTEGER NOT NULL,
    стоимость TEXT NOT NULL,
    FOREIGN KEY (продукт) REFERENCES Продукты(номер),
    FOREIGN KEY (клиент) REFERENCES Клиенты(номер)
);
''')

con.close()

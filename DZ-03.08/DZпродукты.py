from DZconfig import *


def add_product(name, price, quantity):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        cursor.execute(f'''INSERT INTO Продукты (Название, Цена, Количество) VALUES
        ('{name}', '{price}', {quantity});
        ''')
        con.commit()


def show_product(name, price, quantity):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        script = f'''SELECT * FROM Продукты WHERE true'''
        if name != '':
            script += f' AND Название = "{name}" '
        if price != '':
            script += f' AND Цена = "{price}" '
        if quantity != '':
            script += f' AND Количество = {quantity} '
        script += ';'
        cursor.execute(script)
        rows = cursor.fetchall()
        if len(rows) == 0:
            print('\033[31mТакого продукта нет в списке!\033[0m')
        else:
            print('\nСписок продуктов (номер / название / цена / количество):')
            for row in rows:
                print(*row)


def update_product(number, name, price, quantity):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        if name != '':
            cursor.execute(f''' UPDATE Продукты
                                SET Название = '{name}'
                                WHERE номер = {number};''')
        if price != '':
            cursor.execute(f''' UPDATE Продукты
                                SET Цена = '{price}'
                                WHERE номер = {number};''')
        if quantity != '':
            cursor.execute(f''' UPDATE Продукты
                                SET Количество = {quantity}
                                WHERE номер = {number};''')
        con.commit()


def del_product(number):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        cursor.execute(f'''DELETE FROM Продукты WHERE номер = {number};''')
        con.commit()


def search_product(number):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        cursor.execute(f'''SELECT номер FROM Продукты WHERE номер = {number};''')
        return cursor.fetchone()


def quantity_product(number):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        cursor.execute(f'''SELECT Количество FROM Продукты WHERE номер = {number};''')
        return cursor.fetchone()

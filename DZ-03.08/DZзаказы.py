from DZconfig import *


def add_order(client, product, quantity):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        cursor.execute(f'''SELECT Цена FROM Продукты WHERE номер = {product};
                             ''')
        price = cursor.fetchone()
        cost = quantity * int(*price)
        cursor.executescript(f'''INSERT INTO Заказы (продукт, клиент, стоимость) VALUES
        ({product}, {client}, '{cost}');
        ''')
        con.commit()


def show_order(client, product, cost):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        script = f'''SELECT z.номер, z.дата_заказа, p.Название, (z.стоимость / p.Цена) AS количество, 
                            z.стоимость, k.имя, k.фамилия
                     FROM Заказы z 
                     JOIN Продукты p ON p.номер = z.продукт
                     JOIN Клиенты k ON k.номер = z.клиент
                     WHERE true'''
        if client != '':
            script += f' AND k.номер = {client} '
        if product != '':
            script += f' AND p.номер = {product} '
        if cost != '':
            script += f' AND z.стоимость = "{cost}" '
        script += ';'
        cursor.execute(script)
        rows = cursor.fetchall()
        if len(rows) == 0:
            print('\033[31mТакого заказа нет в списке!\033[0m')
        else:
            print('\nСписок заказов (номер / дата и время / продукт / количество / стоимость / имя и фамилия клиента):')
            for row in rows:
                print(*row)


def update_order(number, client, product, cost):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        if client != '':
            cursor.execute(f''' UPDATE Заказы
                                SET клиент = {client}
                                WHERE номер = {number};''')
        if product != '':
            cursor.execute(f''' UPDATE Заказы
                                SET продукт = {product}
                                WHERE номер = {number};''')
        if cost != '':
            cursor.execute(f''' UPDATE Заказы
                                SET стоимость = '{cost}'
                                WHERE номер = {number};''')
        con.commit()


def del_order(number):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        cursor.execute(f'''DELETE FROM Заказы WHERE номер = {number};''')
        con.commit()


def search_order(number):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        cursor.execute(f'''SELECT номер FROM Заказы WHERE номер = {number};''')
        return cursor.fetchone()

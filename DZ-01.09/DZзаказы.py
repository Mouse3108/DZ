from DZconfig import *


def add_order(number, client, product, price):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        cursor.executescript(f'''INSERT INTO orders (номер_заказа, продукт, клиент, стоимость) VALUES
        ({number}, {product}, {client}, '{price}');
        ''')
        con.commit()


def search_order():
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        cursor.execute('''SELECT MAX(номер_заказа) FROM orders;''')
        return cursor.fetchone()

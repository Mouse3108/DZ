from DZconfig import *


def show_product():
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        cursor.execute('''SELECT * FROM products WHERE количество > 0;''')
        rows = cursor.fetchall()
        return rows


def update_product(number, quantity):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        cursor.execute(f''' UPDATE products
                            SET количество = {quantity}
                            WHERE номер_продукта = {number};''')
        con.commit()


def search_product(number):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        cursor.execute(f'''SELECT номер_продукта, название FROM products WHERE номер_продукта = {number};''')
        return cursor.fetchone()


def quantity_product(number):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        cursor.execute(f'''SELECT количество FROM products WHERE номер_продукта = {number};''')
        return cursor.fetchone()


def price_product(number):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        cursor.execute(f'''SELECT цена FROM products WHERE номер_продукта = {number};''')
        return cursor.fetchone()

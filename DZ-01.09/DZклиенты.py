from DZconfig import *


def add_client(name, password, address, phone_number):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        cursor.execute(f'''INSERT INTO users (имя, пароль, адрес, телефон) VALUES
        ('{name}', '{password}', '{address}', '{phone_number}');
        ''')
        con.commit()


def search_client(name, password):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        cursor.execute(f'''SELECT номер_клиента FROM users WHERE имя = '{name}' AND пароль = '{password}';''')
        client = cursor.fetchone()
        return client


def update_client(number, name, password, address, phone_number):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        if name != '':
            cursor.execute(f''' UPDATE users
                                SET имя = '{name}'
                                WHERE номер_клиента = {number};''')
        if password != '':
            cursor.execute(f''' UPDATE users
                                SET пароль = '{password}'
                                WHERE номер_клиента = {number};''')
        if address != '':
            cursor.execute(f''' UPDATE users
                                SET адрес = '{address}'
                                WHERE номер_клиента = {number};''')
        if phone_number != '':
            cursor.execute(f''' UPDATE users
                                SET телефон = '{phone_number}'
                                WHERE номер_клиента = {number};''')
        con.commit()


def del_client(number):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        cursor.execute(f'''DELETE FROM users WHERE номер_клиента = {number};''')
        con.commit()




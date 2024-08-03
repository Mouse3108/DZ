from DZconfig import *


def add_client(first_name, last_name, address, phone_number):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        cursor.execute(f'''INSERT INTO Клиенты (имя, фамилия, адрес, телефон) VALUES
        ('{first_name}', '{last_name}', '{address}', '{phone_number}');
        ''')
        con.commit()


def show_client(first_name, last_name, address, phone_number):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        script = f'''SELECT * FROM Клиенты WHERE true'''
        if first_name != '':
            script += f' AND имя = "{first_name}" '
        if last_name != '':
            script += f' AND фамилия = "{last_name}" '
        if address != '':
            script += f' AND адрес = "{address}" '
        if phone_number != '':
            script += f' AND телефон = "{phone_number}" '
        script += ';'
        cursor.execute(script)
        rows = cursor.fetchall()
        if len(rows) == 0:
            print('\033[31mТакого клиента нет в списке!\033[0m')
        else:
            print('\nСписок клиентов (номер / имя / фамилия / адрес / телефон):')
            for row in rows:
                print(*row)


def update_client(number, first_name, last_name, address, phone_number):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        if first_name != '':
            cursor.execute(f''' UPDATE Клиенты
                                SET имя = '{first_name}'
                                WHERE номер = {number};''')
        if last_name != '':
            cursor.execute(f''' UPDATE Клиенты
                                SET фамилия = '{last_name}'
                                WHERE номер = {number};''')
        if address != '':
            cursor.execute(f''' UPDATE Клиенты
                                SET адрес = '{address}'
                                WHERE номер = {number};''')
        if phone_number != '':
            cursor.execute(f''' UPDATE Клиенты
                                SET телефон = '{phone_number}'
                                WHERE номер = {number};''')
        con.commit()


def del_client(number):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        cursor.execute(f'''DELETE FROM Клиенты WHERE номер = {number};''')
        con.commit()


def search_client(number):
    with sqlite3.connect('DZ.db') as con:
        cursor = con.cursor()
        cursor.execute(f'''SELECT номер FROM Клиенты WHERE номер = {number};''')
        return cursor.fetchone()

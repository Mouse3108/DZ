import sqlite3 as sq

# 1. Вставить из Т2 в Т1 ID, фамилия и должность, Or если ID<23 и ID>18

# Пыталась прикрепить одну БД к другой, но выдавал ошибку:
# (sqlite3.OperationalError: attached databases must use the same text encoding as main database)

# with sq.connect('db_1.db') as con:
#     con.execute("ATTACH DATABASE 'db_3.db' AS db3")
#     cur = con.cursor()
#
#     cur.execute("""
#         INSERT INTO T1 (FName, Doljnost, ORab)
#         SELECT FName, Doljnost, ORab
#         FROM db1.T2
#         WHERE ID < 23 AND ID > 18
#     """)

# Смогла сделать только в таком варианте:
with sq.connect('db_1.db') as con1, sq.connect('db_3.db') as con2:
    cur1 = con1.cursor()
    cur2 = con2.cursor()

    cur2.execute("""
        SELECT FName, Doljnost, ORab
        FROM T2
        WHERE ID < 23 AND ID > 18
    """)
    rows = cur2.fetchall()
    cur1.executemany("""
        INSERT INTO T1 (FName, Doljnost, ORab)
        VALUES (?, ?, ?)
    """, rows)

# 2. Вставить оставшиеся записи (ID>22), уменьшив зарплату на 10%, а опыт работы в 2 раза.
    cur2.execute("""
            SELECT FName, Doljnost, ORab, ZP
            FROM T2
            WHERE ID > 22
    """)
    rows = cur2.fetchall()
    cur1.executemany("""
            INSERT INTO T1 (FName, Doljnost, ORab, ZP)
            VALUES (?, ?, ? / 2, ? * 0.9)
    """, rows)

# 3. Создать копию полученной таблицы с менеджерами и директорами (все данные)
    cur1.execute("""
            CREATE TABLE New_Table AS
            SELECT *
            FROM T1
            WHERE Doljnost = 'Менеджер' OR Doljnost = 'Директор'
    """)

# 4. Создать копию таблицы, в которой будет зарплата <1000 и увеличить зарплату на 100 единиц.
    cur1.execute("""
            CREATE TABLE Copy_Table AS
            SELECT *    # или SELECT ZP, если в копию таблицы нужна только зарплата
            FROM T1
            WHERE ZP < 1000
    """)
    cur1.execute("""
            UPDATE Copy_Table
            SET ZP = ZP + 100
    """)

# 5. В таблице Т1, если зарплата не определена и опыт работы более 0, присвоить 900.
    cur1.execute("""
            UPDATE T1
            SET ZP = 900
            WHERE ZP IS NULL AND ORab > 0
    """)

# 6. Удалить записи с неопределенной зарплатой из Т1.
    cur1.execute("""
            DELETE FROM T1
            WHERE ZP IS NULL
    """)

# 7. Удалить все записи из таблицы Т2.
    cur2.execute("""
            DELETE FROM T2
    """)

import sqlite3

con = sqlite3.connect('test1.db')
cur = con.cursor()

# ----- Створити БД -------

# cur.execute("CREATE TABLE user(name, year, title)")
# cur.execute(''' CREATE TABLE user_1(
#         id INTEGER PRIMARY KEY,
#         name TEXT DEFAULT 'Невідомий',
#         year INTEGER DEFAULT 0,
#         title TEXT NOT NULL
#     );''')
# con.commit()

# -------- Додати до БД інформацію --------

# cur.execute("""INSERT INTO user_1 (name, year ,title)
#         VALUES('Тарас',2000, 'Дідусь');""")
# con.commit()

# name = 'Петрович'
# year =2001
# title = 'Без змін'
# cur.execute(f"""INSERT INTO user_1 (name, year ,title)
#         VALUES('{name}',{year}, '{title}');""")
# con.commit()

name = 'Петрович'
year =2001
title = 'Запис'
cur.execute(f"""INSERT INTO user_1 (name, year ,title)
        VALUES(?, ?, ?);""", (name, year, title))
con.commit()

con.close()
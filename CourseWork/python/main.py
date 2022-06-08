import sqlite3

conn = sqlite3.connect('accountant.db')
cursor = conn.cursor()

cursor.execute("insert into profile values (55, 'nick', 21, 'tmb', 'm', 'link', 'lox')")
conn.commit()

cursor.execute("select * from profile")
results=cursor.fetchall()
print(results)

conn.close()


""""
def add_user(self, user_id, name, gender, age, city, photo, about_me):
    # Добавление
    self.cursor.execute("INSERT INTO `users` (user_id,name, gender,"
                        " age, city, photo, about_me ) VALUES (?,?,?,?,?,?,?)",
                        (user_id, name, gender, age, city, photo, about_me))
    return self.conn.commit()
"""""


def add_user(self, user_id, name):
    # Добавление
    self.cursor.execute("INSERT INTO `users` (user_id,name) VALUES (?,?)", (user_id, name))
    return self.conn.commit()


def add_user(self, user_id):
    # Добавление
    self.cursor.execute("INSERT INTO `users` (user_id) VALUES (?)", (user_id,))
    return self.conn.commit()
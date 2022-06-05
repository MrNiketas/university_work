import sqlite3

class Database:

    def __init__(self, db_file):
        #Инициализация базы данных
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        #Проверка, есть ли пользователь в БД
        result = self.cursor.execute("SELECT 'id' FROM 'users' WHERE  'user_id' = ?", (user_id,))
        return bool(len(result.fetchall()))

    def add_user(self, user_id):
        # Добавление
        self.cursor.execute("INSERT INTO 'users' (user_id) VALUES (?)", (user_id,))
        return self.conn.commit()
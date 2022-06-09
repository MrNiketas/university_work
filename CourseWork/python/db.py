import sqlite3

class Database:

    def __init__(self, db_file):
        #Инициализация базы данных
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        #Проверка, есть ли пользователь в БД
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE  `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))


    def add_user(self, user_id, name, gender, age, city, photo, about_me):
        # Добавление
        self.cursor.execute("INSERT INTO `users` (user_id,name, gender,"
                            " age, city, photo, about_me ) VALUES (?,?,?,?,?,?,?)",
                            (user_id, name, gender, age, city, photo, about_me))
        return self.conn.commit()

    def delete_user(self, user_id):
        # Удаление профиля
        self.cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
        return self.conn.commit()

    def show_profile(self, user_id):
        # Показать профиль
        profile = self.cursor.execute("SELECT name,gender, age,city,photo FROM users WHERE user_id = ?",(user_id,))
        return profile.fetchone()


    def show_all_profiles(self, user_id):
        # Показать профиль
        profiles = self.cursor.execute("SELECT * FROM users WHERE user_id != ?", (user_id,))
        return profiles.fetchall()
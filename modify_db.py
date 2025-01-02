import sqlite3


def create_new_user(user_name, password, role):
    connection_obj = sqlite3.connect('db/library.db')
    cursor = connection_obj.cursor()

    cursor.execute("INSERT INTO users (user_name, password, role) VALUES (?, ?, ?)",
                   (user_name, password, role))

    connection_obj.commit()
    connection_obj.close()


def delete_user(user_name):
    connection_obj = sqlite3.connect('db/library.db')
    cursor = connection_obj.cursor()

    cursor.execute("DELETE FROM users WHERE user_name = ?", (user_name,))

    connection_obj.commit()
    connection_obj.close()
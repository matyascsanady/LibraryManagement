"""I know that storing the hash of the password would be more elegant.
But for now this would suffice."""

import sqlite3


def login():
    """Handles user login by finding a record that matches the given username and password."""

    while True:
        user_name = input("Username: ")
        password = input("Password: ")

        try:
            connection_obj = sqlite3.connect("db/library.db")
            cursor_obj = connection_obj.cursor()

            query = """
            SELECT * FROM USERS
            WHERE User_Name = ? AND Password = ?
            """

            cursor_obj.execute(query, (user_name, password))
            result = cursor_obj.fetchone()

            if result:
                print(f"\nLogin successful! Welcome, {user_name} (Role: {result[3]})!")
                connection_obj.close()
                return result

            else:
                print("Invalid username or password. Please try again.\n")
                continue

        except sqlite3.Error as e:
            print("Database error:", e)
        except Exception as e:
            print("An unexpected error occurred:", e)

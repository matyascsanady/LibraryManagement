"""I know that storing the hash of the password would be more elegant.
But for now this would suffice."""

from common_db import *


def login():
    """Handles user login by finding a record that matches the given username and password."""

    while True:
        user_name = input("Username: ")
        password = input("Password: ")

        try:
            connection_obj = create_connection()

            query = """
            SELECT * FROM USERS
            WHERE User_Name = ? AND Password = ?
            """

            result = execute_query(connection_obj, query, (user_name, password))
            if result:
                print(f"\nLogin successful! Welcome, {user_name} (Role: {result[0][3]})!")
                connection_obj.close()
                return result[0]

            else:
                print("Invalid username or password. Please try again.\n")
                continue

        except sqlite3.Error as e:
            print("Database error:", e)
        except Exception as e:
            print("An unexpected error occurred:", e)

import sqlite3


def login():
    # Prompt the user for credentials
    user_name = input("Username: ")
    password = input("Password: ")

    try:
        # Connect to the database
        connection_obj = sqlite3.connect("db/users.db")
        cursor_obj = connection_obj.cursor()

        # Query to verify credentials
        query = """
        SELECT * FROM USERS
        WHERE User_Name = ? AND Password = ?
        """

        # Execute the query with user input
        cursor_obj.execute(query, (user_name, password))
        result = cursor_obj.fetchone()

        # Check if a matching record exists
        if result:
            print(f"Welcome, {user_name}! Login successful.")
        else:
            print("Invalid username or password. Please try again.")

    except sqlite3.Error as e:
        print("Database error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
    finally:
        # Close the database connection
        if connection_obj:
            connection_obj.close()



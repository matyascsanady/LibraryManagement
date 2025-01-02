import sqlite3


def create_connection(db_name="db/library.db"):
    """Creates a connection to the SQLite database."""
    return sqlite3.connect(db_name)


def execute_query(connection, query, data=None):
    """Executes a single query with optional data."""
    cursor = connection.cursor()
    if data:
        cursor.execute(query, data)
    else:
        cursor.execute(query)
    connection.commit()


def create_new_user(user_name, password, role):
    """Adds a new user to the USERS table."""
    connection = create_connection()
    insert_query = "INSERT INTO USERS (User_Name, Password, Role) VALUES (?, ?, ?)"
    execute_query(connection, insert_query, (user_name, password, role))
    connection.close()
    print(f"User '{user_name}' added successfully.")


def delete_user(user_name):
    """Deletes a user from the USERS table by user name."""
    connection = create_connection()
    delete_query = "DELETE FROM USERS WHERE User_Name = ?"
    execute_query(connection, delete_query, (user_name,))
    connection.close()
    print(f"User '{user_name}' deleted successfully.")

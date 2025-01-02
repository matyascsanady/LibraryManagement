import sqlite3

def create_connection(db_name="db/library.db"):
    """Creates a connection to the SQLite database."""
    return sqlite3.connect(db_name)


def execute_query(connection, query, data=None):
    """Executes a single query with optional data."""
    cursor = connection.cursor()
    if data:
        cursor.executemany(query, data)
    else:
        cursor.execute(query)
    connection.commit()


def create_users_table(connection):
    """Creates the USERS table."""
    table_query = """
        CREATE TABLE IF NOT EXISTS USERS (
            User_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            User_Name CHAR(50) NOT NULL,
            Password CHAR(50) NOT NULL,
            Role CHAR(25) NOT NULL
        );
    """
    execute_query(connection, table_query)

    # Initial users
    users = [
        ("Admin", "Admin Password", "Admin"),
        ("Librarian", "Library Password", "Librarian"),
        ("Reader", "Reader Password", "Reader"),
        ("csana", "123", "Admin")
    ]
    insert_query = "INSERT INTO USERS (User_Name, Password, Role) VALUES (?, ?, ?)"
    execute_query(connection, insert_query, users)
    print("\"USERS\" table is created and initial records inserted.")


def create_books_table(connection):
    """Creates the BOOKS table."""
    table_query = """
        CREATE TABLE IF NOT EXISTS BOOKS (
            Book_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name CHAR(50) NOT NULL,
            Author CHAR(50) NOT NULL
        );
    """
    execute_query(connection, table_query)

    # Initial books
    books = [
        ("Vörös Lázadás", "Pierce Brown"),
        ("Arany Háború", "Pierce Brown"),
        ("Hajnal Csillag", "Pierce Brown"),
        ("Káosz Évei", "Pierce Brown")
    ]
    insert_query = "INSERT INTO BOOKS (Name, Author) VALUES (?, ?)"
    execute_query(connection, insert_query, books)
    print("\"BOOKS\" table is created and initial records inserted.")


def main():
    connection = create_connection()
    create_users_table(connection)
    create_books_table(connection)
    connection.close()


if __name__ == "__main__":
    main()

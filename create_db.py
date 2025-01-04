import os
import sqlite3


def create_connection(db_name="db/library.db"):
    """Creates a connection to the SQLite database."""
    os.makedirs(os.path.dirname(db_name), exist_ok=True)

    return sqlite3.connect(db_name)


def execute_query(connection, query, data=None):
    """Executes a single query with optional data."""
    cursor = connection.cursor()
    if data:
        cursor.executemany(query, data)
    else:
        cursor.execute(query)
    connection.commit()


def drop_all_tables(connection):
    """Drops all tables by temporarily disabling foreign key checks."""
    connection.execute("PRAGMA foreign_keys = OFF;")

    execute_query(connection, "DROP TABLE IF EXISTS RENTS;")
    execute_query(connection, "DROP TABLE IF EXISTS USERS;")
    execute_query(connection, "DROP TABLE IF EXISTS BOOKS;")

    connection.execute("PRAGMA foreign_keys = ON;")


def create_users_table(connection):
    """Creates the USERS table."""
    table_query = """
        CREATE TABLE USERS (
            User_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            User_Name CHAR(50) NOT NULL,
            Password CHAR(50) NOT NULL,
            Role CHAR(25) NOT NULL
        );
    """
    execute_query(connection, table_query)

    # Initial users
    init_users = [
        ("Admin", "Admin Password", "Admin"),
        ("Librarian", "Library Password", "Librarian"),
        ("Reader", "Reader Password", "Reader"),
        ("csana", "123", "Admin")
    ]
    insert_query = "INSERT INTO USERS (User_Name, Password, Role) VALUES (?, ?, ?)"
    execute_query(connection, insert_query, init_users)
    print("\"USERS\" table is created and initial records inserted.")


def create_books_table(connection):
    """Creates the BOOKS table."""
    table_query = """
        CREATE TABLE BOOKS (
            Book_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name CHAR(50) NOT NULL,
            Author CHAR(50) NOT NULL
        );
    """
    execute_query(connection, table_query)

    # Initial books
    init_books = [
        ("Vörös Lázadás", "Pierce Brown"),
        ("Arany Háború", "Pierce Brown"),
        ("Hajnal Csillag", "Pierce Brown"),
        ("Káosz Évei", "Pierce Brown")
    ]
    insert_query = "INSERT INTO BOOKS (Name, Author) VALUES (?, ?)"
    execute_query(connection, insert_query, init_books)
    print("\"BOOKS\" table is created and initial records inserted.")


def create_rents_table(connection):
    """Creates the RENTS table."""
    table_query = """
        CREATE TABLE RENTS (
            Rent_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Book_ID INTEGER NOT NULL,
            Reader_ID INTEGER NOT NULL,
            Rent_Out_Date DATE DEFAULT (DATE('now')),
            Due_Date DATE DEFAULT (DATE('now', '+30 days')),
            Return_Date DATE DEFAULT NULL,
            FOREIGN KEY (Reader_ID) REFERENCES USERS(User_ID),
            FOREIGN KEY (Book_ID) REFERENCES BOOKS(Book_ID)
        );
    """
    execute_query(connection, table_query)

    # Initial rents
    init_rents = [
        (1, 3)
    ]
    insert_query = "INSERT INTO RENTS (Book_ID, Reader_ID) VALUES (?, ?)"
    execute_query(connection, insert_query, init_rents)
    print("\"RENTS\" table is created and initial records inserted.")


def main():
    connection = create_connection()
    connection.execute("PRAGMA foreign_keys = ON;")

    drop_all_tables(connection)

    create_users_table(connection)
    create_books_table(connection)
    create_rents_table(connection)

    connection.close()


if __name__ == "__main__":
    main()

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
        ("Manager", "Manager123", "Admin"),
        ("AssistantLibrarian", "AssistLib456", "Librarian"),
        ("GuestUser", "Welcome789", "Reader"),
        ("JohnDoe", "secure123", "Reader"),
        ("JaneSmith", "pass456", "Librarian"),
        ("csana", "123", "Admin"),
        ("AliceReader", "read123", "Reader"),
        ("BobReader", "page456", "Reader"),
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
            Author CHAR(50) NOT NULL,
            Pages INTEGER,
            Release_Year INTEGER,
            Language CHAR(25)
        );
    """
    execute_query(connection, table_query)

    # Initial books
    init_books = [
        ("Vörös Lázadás", "Pierce Brown", 424, 2014, "magyar"),
        ("Arany Háború", "Pierce Brown", 494, 2015, "magyar"),
        ("Hajnal Csillag", "Pierce Brown", 566, 2016, "magyar"),
        ("Káosz Évei", "Pierce Brown", 606, 2018, "magyar"),
        ("A Sötétség Kora", "Pierce Brown", 892, 2019, "magyar"),
        ("Fényhozó", "Pierce Brown", 828, 2023, "magyar"),
        ("Supermarket", "Bobby Hall", 266, 2019, "angol"),
        ("Az idő rövid története", "Stephen Hawking", 247, 1988, "magyar"),
        ("Billy Summers", "Stephen King", 528, 2021, "angol"),
        ("20,000 Leagues Under The Sea", "Jules Verne", 368, 1870, "angol"),
        ("A Halál Szobrásza", "Chris Carter", 378, 2010, "magyar"),
        ("Vérrel Írva", "Chris Carter", 328, 2011, "magyar"),
        ("A Holtak Csarnoka", "Chris Carter", 344, 2012, "magyar"),
        ("A Gonosz Nyomában", "Chris Carter", 256, 2013, "magyar"),
        ("A Kívülálló", "Stephen King", 504, 2018, "magyar"),
        ("The Call of the Wild", "Jack London", 144, 1903, "angol"),
        ("How To Solve Your Own Murder", "Kristen Perrin", 358, 2024, "angol"),
        ("American Prometheus", "Kai Bird, Martin J. Sherwin", 721, 2005, "angol"),
        ("How To Build A Car", "Adrian Newey", 504, 2017, "angol"),
        ("Clean Code: A Handbook of Agile Software Craftsmanship", "Robert C. Martin", 464, 2008, "angol")
    ]

    insert_query = "INSERT INTO BOOKS (Name, Author, Pages, Release_Year, Language) VALUES (?, ?, ?, ?, ?)"
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

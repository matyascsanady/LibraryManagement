import sqlite3

def create_users_db():

    connection_obj = sqlite3.connect("db/users.db")
    cursor_obj = connection_obj.cursor()
    cursor_obj.execute("DROP TABLE IF EXISTS USERS")

    table = """ CREATE TABLE USERS (
                User_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                User_Name CHAR(50) NOT NULL,
                Password CHAR(50) NOT NULL,
                Role CHAR(25) NOT NULL
              ); """

    cursor_obj.execute(table)
    print("\"users\" table is created/overridden'")

    # Initial users
    users = [
        ("Admin", "Admin Password", "Admin"),
        ("Librarian", "Library Password", "Librarian"),
        ("Reader", "Reader Password", "Reader"),
        ("csana", "123", "Admin")
    ]

    cursor_obj.executemany("INSERT INTO USERS (User_Name, Password, Role) VALUES (?, ?, ?)", users)
    print("Initial records inserted.")

    connection_obj.commit()
    connection_obj.close()


def create_books_db():
    connection_obj = sqlite3.connect("db/books.db")
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute("DROP TABLE IF EXISTS BOOKS")

    table = """ CREATE TABLE BOOKS (
                Book_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name CHAR(50) NOT NULL,
                Author CHAR(50) NOT NULL
              ); """

    cursor_obj.execute(table)
    print("\"books\" table is created/overridden'")

    # Initial books
    books = [
        ("Vörös Lázadás", "Pierce Brown"),
        ("Arany Háború", "Pierce Brown"),
        ("Hajnal Csillag", "Pierce Brown"),
        ("Káosz Évei", "Pierce Brown")
    ]

    cursor_obj.executemany("INSERT INTO BOOKS (Name, Author) VALUES (?, ?)", books)
    print("Initial records inserted.")

    connection_obj.commit()
    connection_obj.close()


def main():
    create_users_db()
    create_books_db()


if __name__ == "__main__":
    main()
from common_db import *


def create_new_user(user_name, password, role):
    """Adds a new user to the USERS table."""
    connection = create_connection()
    insert_query = "INSERT INTO USERS (User_Name, Password, Role) VALUES (?, ?, ?)"
    execute_query(connection, insert_query, (user_name, password, role))
    connection.close()
    print(f"User '{user_name}' added successfully.")


def delete_user(user_id):
    """Deletes a user from the USERS table by User_ID."""
    connection = create_connection()
    delete_query = "DELETE FROM USERS WHERE User_ID = ?"
    execute_query(connection, delete_query, (user_id,))
    connection.close()
    print(f"User '{user_id}' deleted successfully.")


def crete_new_rent(user_id, book_id):
    """Adds a new rent to the rents table."""

    connection = create_connection()
    insert_query = "INSERT INTO RENTS (Reader_ID, Book_ID) VALUES (?, ?)"
    execute_query(connection, insert_query, (user_id, book_id))
    connection.close()
    print(f"Rent for '{book_id}' created successfully.")


def finish_rent(user_id, book_id):
    """Closes the rent by filling the return date."""
    connection = create_connection()
    cursor = connection.cursor()

    update_query = """
        UPDATE RENTS
        SET Return_Date = DATE('now')
        WHERE Reader_ID = ?
        AND Book_ID = ?
        AND Return_Date IS NULL;
    """

    cursor.execute(update_query, (user_id, book_id))
    connection.commit()
    connection.close()
    print(f"Rent for '{book_id}' finished successfully.")


def create_book(name, author, pages, release_year, language, quality):
    """Creates a new book record in the Books table."""

    connection = create_connection()
    insert_query = "INSERT INTO BOOKS (Name, Author, Pages, Release_Year, Language, Quality) VALUES (?, ?, ?, ?, ?, ?)"
    execute_query(connection, insert_query, (name, author, pages, release_year, language, quality))

    connection.close()
    print(f"Book '{name}' created successfully.")


def delete_book_by_id(book_id):
    """Deletes the record in books where book_id matches."""

    connection = create_connection()
    delete_query = "DELETE FROM BOOKS WHERE Book_ID = ?"
    execute_query(connection, delete_query, (book_id,))
    connection.close()
    print(f"Book '{book_id}' deleted successfully.")

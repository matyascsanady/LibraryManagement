from common_db import *


def get_available_books():
    """Returns the books that are available to rent."""
    connection = create_connection()

    query = """
        SELECT * 
        FROM BOOKS
        WHERE Book_ID NOT IN (
            SELECT Book_ID
            FROM RENTS
            WHERE Return_Date IS NULL
        );
    """

    results = execute_query(connection, query)
    connection.close()

    return results


def get_user_books(user_id):
    """Returns the books that the user currently rents."""
    connection = create_connection()

    query = """
        SELECT BOOKS.*
        FROM BOOKS
        INNER JOIN RENTS ON BOOKS.Book_ID = RENTS.Book_ID
        WHERE RENTS.Reader_ID = ?
        AND RENTS.Return_Date IS NULL;
    """

    results = execute_query(connection, query, (user_id,))
    connection.close()

    return results


def get_user_read_books(user_id):
    """Returns the books that the user has read (rented) before."""

    connection = create_connection()

    query = """
        SELECT BOOKS.*
        FROM BOOKS
        INNER JOIN RENTS ON BOOKS.Book_ID = RENTS.Book_ID
        WHERE RENTS.Reader_ID = ?
        AND RENTS.Return_Date IS NOT NULL;
    """

    results = execute_query(connection, query, (user_id,))
    connection.close()

    return results


def get_all_books():
    """Returns every book in the library."""
    connection = create_connection()

    results = execute_query(connection, "SELECT * FROM BOOKS;")
    connection.close()

    return results


def get_users():
    """Returns all the users in the library."""
    connection = create_connection()

    results = execute_query(connection, "SELECT * FROM USERS;")
    connection.close()

    return results


def get_user_by_id(user_id):
    """Returns the username of the given user id."""

    connection = create_connection()
    results = execute_query(connection, "SELECT * FROM USERS WHERE User_ID = ?;", (user_id,))
    connection.close()

    return results[0]
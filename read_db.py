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


def get_available_books():
    """Returns the books that are available to rent."""
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        SELECT * 
        FROM BOOKS
        WHERE Book_ID NOT IN (
            SELECT Book_ID
            FROM RENTS
            WHERE Return_Date IS NULL
        );
    """

    cursor.execute(query)
    results = cursor.fetchall()

    connection.close()

    return results

def get_user_books(user_id):
    """Returns the books that the user currently rents."""
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        SELECT BOOKS.*
        FROM BOOKS
        INNER JOIN RENTS ON BOOKS.Book_ID = RENTS.Book_ID
        WHERE RENTS.Reader_ID = ?
        AND RENTS.Return_Date IS NULL;
    """

    cursor.execute(query, (user_id,))
    results = cursor.fetchall()

    connection.close()

    return results


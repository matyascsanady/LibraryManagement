import os
import sqlite3


def create_connection(db_name="db/library.db"):
    """Creates a connection to the SQLite database."""
    os.makedirs(os.path.dirname(db_name), exist_ok=True)

    return sqlite3.connect(db_name)


def execute_query(connection, query, data=None):
    """Executes a single query with optional data."""
    cursor = connection.cursor()
    if type(data) is tuple:
        cursor.execute(query, data)
    elif type(data) is list:
        cursor.executemany(query, data)
    else:
        cursor.execute(query)
    connection.commit()

    return cursor.fetchall()

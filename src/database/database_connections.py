"""
Establish a database connection
"""
import sqlite3
from config import DB_FILE_PATH


connection = sqlite3.connect(DB_FILE_PATH)
connection.row_factory = sqlite3.Row


def get_database_connection():
    """
    Return connection

    Returns:
        sqlite3 connection
    """
    return connection

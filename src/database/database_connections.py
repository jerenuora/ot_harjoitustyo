"""
Form a filepath and establish a database connection
"""
import os
import sqlite3

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(
    dirname, "..", "assets", "scores.db"))
connection.row_factory = sqlite3.Row


def get_database_connection():
    """
    Return connection

    Returns:
        sqlite3 connection
    """
    return connection
